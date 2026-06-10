#!/usr/bin/env python3
"""
validate_bdqtest_against_shacl.py

Validates a bdqtest.ttl RDF file against bdqffdq: SHACL constraints.

Loads the primary data graph, an optional ontology for RDFS inference,
an optional Use Case vocabulary file, and any number of additional
supplementary vocabulary files, then runs pyshacl and reports results.

Default paths are set relative to the expected location of this script
inside the tg2/_build_review/tools/ directory of the BDQ repository:

    --data    ../../_review/dist/bdqtest.ttl
    --shapes  ../../core/bdqffdq_SHACL_constraints.ttl
    --ont     ../../_review/vocabulary/bdqffdq.owl
    --usecase ../../_review/dist/bdquc.xml

Requirements:
    pip install pyshacl rdflib

Usage:
    python validate_bdqtest_against_shacl.py [-h]
        [--data    PATH]
        [--shapes  PATH]
        [--ont     PATH]
        [--usecase PATH]
        [--supplementary PATH [...]]
        [--output  PATH]
        [--format  text|json|table]
        [--severity WARNING|VIOLATION|INFO]
        [--verbose]
        [--exit-zero]

Examples:
    # Run with all defaults (no arguments required)
    python validate_bdqtest_against_shacl.py

    # Override the data file only
    python validate_bdqtest_against_shacl.py --data /path/to/other.ttl

    # Add supplementary vocabulary files and write a JSON report
    python validate_bdqtest_against_shacl.py \\
        --supplementary bdqdim.ttl \\
        --supplementary bdqcrit.ttl \\
        --format json --output report.json

    # Show VIOLATION-level results only
    python validate_bdqtest_against_shacl.py --severity VIOLATION

    # Show everything including INFO as a tab-separated table
    python validate_bdqtest_against_shacl.py \\
        --format table --severity INFO --output results.tsv

@author Claude Sonnet 4.5 (Anthropic), with guidance by
        @chicoreus Paul J. Morris
"""

import argparse
import json
import sys
import textwrap
from pathlib import Path

try:
    import rdflib
    from rdflib import Graph, Namespace
    from rdflib.namespace import RDF, RDFS, SH
except ImportError:
    sys.exit("rdflib is not installed.  Run:  pip install rdflib")

try:
    from pyshacl import validate as shacl_validate
except ImportError:
    sys.exit("pyshacl is not installed.  Run:  pip install pyshacl")


# ---------------------------------------------------------------------------
# Default file paths (relative to this script's expected location in
# tg2/_build_review/tools/ within the BDQ repository)
# ---------------------------------------------------------------------------

_HERE = Path(__file__).parent

DEFAULT_DATA    = _HERE / "../../_review/dist/bdqtest.ttl"
DEFAULT_SHAPES  = _HERE / "../../core/bdqffdq_SHACL_constraints.ttl"
DEFAULT_ONT     = _HERE / "../../_review/vocabulary/bdqffdq.owl"
DEFAULT_USECASE = _HERE / "../../_review/dist/bdquc.xml"


# ---------------------------------------------------------------------------
# Namespaces
# ---------------------------------------------------------------------------

BDQFFDQ = Namespace("https://rs.tdwg.org/bdqffdq/terms/")
SKOS    = Namespace("http://www.w3.org/2004/02/skos/core#")


# ---------------------------------------------------------------------------
# Severity helpers
# ---------------------------------------------------------------------------

SEVERITY_ORDER = {
    str(SH.Info):      0,
    str(SH.Warning):   1,
    str(SH.Violation): 2,
}

SEVERITY_LABELS = {
    str(SH.Info):      "INFO",
    str(SH.Warning):   "WARNING",
    str(SH.Violation): "VIOLATION",
}

SEVERITY_URI = {v: k for k, v in SEVERITY_LABELS.items()}


def severity_level(uri: str) -> int:
    return SEVERITY_ORDER.get(str(uri), 0)


# ---------------------------------------------------------------------------
# Parse pyshacl results graph
# ---------------------------------------------------------------------------

def parse_results(results_graph: Graph) -> list:
    results = []
    for node in results_graph.subjects(RDF.type, SH.ValidationResult):

        def first(pred, default=""):
            val = next(results_graph.objects(node, pred), None)
            return str(val) if val is not None else default

        sev = first(SH.resultSeverity)
        results.append({
            "focus_node":   first(SH.focusNode),
            "result_path":  first(SH.resultPath),
            "message":      first(SH.resultMessage),
            "severity":     sev,
            "severity_label": SEVERITY_LABELS.get(sev, sev),
            "source_constraint_component": first(SH.sourceConstraintComponent),
            "source_shape": first(SH.sourceShape),
            "value":        first(SH.value),
        })

    results.sort(key=lambda r: (-severity_level(r["severity"]), r["focus_node"]))
    return results


# ---------------------------------------------------------------------------
# Severity filter
# ---------------------------------------------------------------------------

def filter_by_severity(results: list, min_label: str) -> list:
    uri = SEVERITY_URI.get(min_label.upper())
    if uri is None:
        raise ValueError(
            f"Unknown severity '{min_label}'.  "
            f"Choose from: {list(SEVERITY_URI)}"
        )
    threshold = severity_level(uri)
    return [r for r in results if severity_level(r["severity"]) >= threshold]


# ---------------------------------------------------------------------------
# Prefix shortener
# ---------------------------------------------------------------------------

def make_prefixes(g: Graph) -> dict:
    prefixes = {
        "bdqffdq": str(BDQFFDQ),
        "sh":      str(SH),
        "rdf":     str(RDF),
        "rdfs":    str(RDFS),
    }
    for p, ns in g.namespaces():
        if p and str(ns) not in prefixes.values():
            prefixes[str(p)] = str(ns)
    return prefixes


def shorten(uri: str, prefixes: dict) -> str:
    for prefix, ns in prefixes.items():
        if uri.startswith(ns):
            return f"{prefix}:{uri[len(ns):]}"
    return uri


# ---------------------------------------------------------------------------
# Smart graph loader  (format detection by content, not extension)
# ---------------------------------------------------------------------------

_FORMAT_PROBE_ORDER = [
    "turtle",
    "xml",
    "n3",
    "nt",
    "json-ld",
    "trig",
    "nquads",
]


def _sniff_format(path: Path) -> str | None:
    """
    Peek at the first non-whitespace bytes of the file and return a format
    hint, or None when the content is ambiguous.

    Heuristics:
        '@' or 'PREFIX' at the start  →  Turtle / N3
        '<' at the start              →  RDF/XML (or OWL/XML)
        '{' or '[' at the start       →  JSON-LD
    """
    try:
        with path.open("rb") as fh:
            raw = fh.read(512)
        if raw.startswith(b"\xef\xbb\xbf"):    # strip UTF-8 BOM
            raw = raw[3:]
        head = raw.lstrip().decode("utf-8", errors="replace")
    except OSError:
        return None

    if head.startswith("@") or head.upper().startswith("PREFIX"):
        return "turtle"
    if head.startswith("<"):
        return "xml"
    if head.startswith("{") or head.startswith("["):
        return "json-ld"
    return None


def load_graph(path: Path, verbose: bool = False) -> Graph:
    """
    Load an RDF file into a new Graph, detecting the serialisation format
    by inspecting the file content rather than relying on the extension.

    The .owl extension in particular is unreliable: the bdqffdq ontology
    is serialised as Turtle despite carrying a .owl extension.  Content
    sniffing resolves this transparently.

    Falls back to trying every known format in _FORMAT_PROBE_ORDER when
    sniffing is inconclusive or the sniffed format fails to parse.
    """
    hint = _sniff_format(path)

    probe = [hint] if hint else []
    for fmt in _FORMAT_PROBE_ORDER:
        if fmt not in probe:
            probe.append(fmt)

    last_exc = None
    for fmt in probe:
        g = Graph()
        try:
            g.parse(str(path), format=fmt)
            if verbose:
                print(f"  Loaded {path.name} as {fmt} "
                      f"({len(g)} triples)", file=sys.stderr)
            return g
        except Exception as exc:
            last_exc = exc
            continue

    raise RuntimeError(
        f"Could not parse '{path}' in any supported RDF format. "
        f"Last error: {last_exc}"
    )


def merge_graphs(base: Graph, extra: Graph) -> Graph:
    """
    Add all triples from *extra* into *base* and copy namespace bindings.
    Returns *base* for convenience.
    """
    for triple in extra:
        base.add(triple)
    for prefix, ns in extra.namespaces():
        base.bind(prefix, ns)
    return base


def count_subjects(g: Graph) -> int:
    return len(set(g.subjects()))


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def format_text(results, conforms, data_graph, total_subjects):
    prefixes = make_prefixes(data_graph)
    lines = []

    lines.append("=" * 72)
    lines.append("  BDQ Test Validation Report")
    lines.append("=" * 72)
    lines.append(f"  Data graph subjects : {total_subjects}")
    lines.append(f"  Conforms            : {conforms}")
    lines.append(f"  Constraint results  : {len(results)}")

    counts = {}
    for r in results:
        counts[r["severity_label"]] = counts.get(r["severity_label"], 0) + 1
    for label in ("VIOLATION", "WARNING", "INFO"):
        if label in counts:
            lines.append(f"    {label:<12}: {counts[label]}")

    if not results:
        lines.append("\nNo constraint results found at the selected severity.")
        return "\n".join(lines)

    current_severity = None
    for idx, r in enumerate(results, start=1):
        if r["severity_label"] != current_severity:
            current_severity = r["severity_label"]
            lines.append("\n" + "-" * 72)
            lines.append(f"  {current_severity}S")
            lines.append("-" * 72)

        focus = shorten(r["focus_node"],  prefixes)
        path  = shorten(r["result_path"], prefixes) if r["result_path"] else "—"
        shape = shorten(r["source_shape"], prefixes)
        comp  = shorten(r["source_constraint_component"], prefixes)
        value = r["value"] if r["value"] else "—"

        lines.append(f"\n[{idx}] {r['severity_label']}")
        lines.append(f"  Focus node : {focus}")
        lines.append(f"  Path       : {path}")
        lines.append(f"  Value      : {value}")
        lines.append(f"  Shape      : {shape}")
        lines.append(f"  Component  : {comp}")
        wrapped = textwrap.wrap(
            r["message"], width=66,
            initial_indent="             ",
            subsequent_indent="             ",
        )
        lines.append(f"  Message    : {wrapped[0].strip()}")
        for wl in wrapped[1:]:
            lines.append(wl)

    lines.append("\n" + "=" * 72)
    return "\n".join(lines)


def format_table(results, conforms, data_graph, total_subjects):
    prefixes = make_prefixes(data_graph)
    rows = ["\t".join(
        ["Severity", "FocusNode", "Path", "Message", "Shape"]
    )]
    for r in results:
        rows.append("\t".join([
            r["severity_label"],
            shorten(r["focus_node"],  prefixes),
            shorten(r["result_path"], prefixes) if r["result_path"] else "",
            r["message"].replace("\n", " "),
            shorten(r["source_shape"], prefixes),
        ]))
    return "\n".join(rows)


def format_json(results, conforms, data_graph, total_subjects):
    return json.dumps({
        "conforms":       conforms,
        "total_subjects": total_subjects,
        "result_count":   len(results),
        "results":        results,
    }, indent=2)


FORMATTERS = {
    "text":  format_text,
    "table": format_table,
    "json":  format_json,
}


# ---------------------------------------------------------------------------
# Core validation
# ---------------------------------------------------------------------------

def run_validation(
    data_path,
    shapes_path,
    ont_path,
    usecase_path,
    supplementary_paths,
    min_severity,
    output_format,
    output_path,
    verbose,
):
    def log(msg):
        if verbose:
            print(msg, file=sys.stderr)

    # ── Load primary data graph ───────────────────────────────────────────
    log(f"Loading data graph    : {data_path}")
    data_graph = load_graph(data_path, verbose=verbose)

    # ── Merge Use Case vocabulary ─────────────────────────────────────────
    # The Use Case vocabulary (bdquc.xml) defines bdqffdq:UseCase instances
    # including the bdqffdq:hasFitnessRequirements property that the SHACL
    # shapes check for.  Merging it into the data graph ensures those
    # property values are visible during validation even though the primary
    # bdqtest.ttl file only references the UseCase URIs.
    if usecase_path is not None:
        log(f"Loading use cases     : {usecase_path}")
        uc_graph = load_graph(usecase_path, verbose=verbose)
        before = len(data_graph)
        merge_graphs(data_graph, uc_graph)
        log(f"  Merged {len(data_graph) - before} new triples "
            f"(total {len(data_graph)})")

    # ── Merge supplementary vocabulary graphs ─────────────────────────────
    # Additional vocabulary files (e.g. bdqdim.ttl, bdqcrit.ttl, bdqenh.ttl)
    # can be supplied with --supplementary and are merged in order.  Each
    # provides definitions for classes or individuals referenced in the
    # primary data file whose full property sets live in that vocabulary.
    for sup_path in (supplementary_paths or []):
        log(f"Loading supplementary : {sup_path}")
        sup_graph = load_graph(sup_path, verbose=verbose)
        before = len(data_graph)
        merge_graphs(data_graph, sup_graph)
        log(f"  Merged {len(data_graph) - before} new triples "
            f"(total {len(data_graph)})")

    total_subjects = count_subjects(data_graph)

    # ── Load shapes graph ─────────────────────────────────────────────────
    log(f"Loading shapes graph  : {shapes_path}")
    shapes_graph = load_graph(shapes_path, verbose=verbose)

    # ── Load optional ontology ────────────────────────────────────────────
    ont_graph = None
    if ont_path is not None:
        log(f"Loading ontology      : {ont_path}")
        ont_graph = load_graph(ont_path, verbose=verbose)

    log("Running SHACL validation …")

    conforms, results_graph, _results_text = shacl_validate(
        data_graph,
        shacl_graph=shapes_graph,
        ont_graph=ont_graph,
        # RDFS inference lets pyshacl see subclass relationships so that
        # sh:targetClass on bdqffdq:DataQualityNeed also targets Validation,
        # Issue, Measure, and Amendment instances without needing to enumerate
        # every subclass in each shape.
        inference="rdfs",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
        meta_shacl=False,
        debug=False,
    )

    log(f"Raw pyshacl conforms  : {conforms}")

    all_results   = parse_results(results_graph)
    shown_results = filter_by_severity(all_results, min_severity)

    log(f"Results shown         : {len(shown_results)} "
        f"(severity >= {min_severity.upper()})")

    report = FORMATTERS[output_format](
        shown_results, conforms, data_graph, total_subjects
    )

    if output_path:
        output_path.write_text(report, encoding="utf-8")
        log(f"Report written to     : {output_path}")
    else:
        print(report)

    threshold = severity_level(SEVERITY_URI[min_severity.upper()])
    return not any(
        severity_level(r["severity"]) >= threshold
        for r in all_results
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(
        prog="validate_bdqtest_against_shacl.py",
        description=(
            "Validate a bdqtest.ttl RDF file against bdqffdq: SHACL "
            "constraints.  Merges the Use Case vocabulary and any "
            "supplementary vocabulary files into the data graph before "
            "running pyshacl, so that property checks on referenced "
            "individuals (such as bdqffdq:hasFitnessRequirements on "
            "bdqffdq:UseCase instances) are satisfied even when those "
            "properties are defined in a separate file."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Default paths (relative to the script location, assuming
            tg2/_build_review/tools/ in the BDQ repository):

              --data    ../../_review/dist/bdqtest.ttl
              --shapes  ../../core/bdqffdq_SHACL_constraints.ttl
              --ont     ../../_review/vocabulary/bdqffdq.owl
              --usecase ../../_review/dist/bdquc.xml

            Running with no arguments uses all of the above defaults.

            Examples:
              # Run entirely with defaults
              python validate_bdqtest_against_shacl.py

              # Override the data file, keep all other defaults
              python validate_bdqtest_against_shacl.py \\
                  --data /path/to/other_bdqtest.ttl

              # Add supplementary vocabulary files
              python validate_bdqtest_against_shacl.py \\
                  --supplementary bdqdim.ttl \\
                  --supplementary bdqcrit.ttl

              # Write a JSON report showing only hard violations
              python validate_bdqtest_against_shacl.py \\
                  --format json --severity VIOLATION \\
                  --output report.json

              # Write a TSV table showing everything including INFO
              python validate_bdqtest_against_shacl.py \\
                  --format table --severity INFO \\
                  --output results.tsv
        """),
    )

    # ── Input files ───────────────────────────────────────────────────────
    input_group = p.add_argument_group("input files")

    input_group.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA,
        metavar="PATH",
        help=(
            "Primary RDF data file to validate. "
            f"(default: {DEFAULT_DATA})"
        ),
    )
    input_group.add_argument(
        "--shapes",
        type=Path,
        default=DEFAULT_SHAPES,
        metavar="PATH",
        help=(
            "SHACL shapes file containing the bdqffdq: constraints. "
            f"(default: {DEFAULT_SHAPES})"
        ),
    )
    input_group.add_argument(
        "--ont",
        type=Path,
        default=DEFAULT_ONT,
        metavar="PATH",
        help=(
            "Ontology file loaded for RDFS inference, enabling subclass "
            "reasoning (e.g. so that bdqffdq:Validation instances are "
            "recognised as bdqffdq:DataQualityNeed instances). "
            "Pass an empty string to disable. "
            f"(default: {DEFAULT_ONT})"
        ),
    )
    input_group.add_argument(
        "--usecase",
        type=Path,
        default=DEFAULT_USECASE,
        metavar="PATH",
        help=(
            "Use Case vocabulary file (e.g. bdquc.xml).  Its triples are "
            "merged into the data graph before validation so that SHACL "
            "shapes can check properties such as "
            "bdqffdq:hasFitnessRequirements on bdqffdq:UseCase instances "
            "that are referenced in the primary data file. "
            "Pass an empty string to skip. "
            f"(default: {DEFAULT_USECASE})"
        ),
    )
    input_group.add_argument(
        "--supplementary", "-s",
        type=Path,
        action="append",
        default=[],
        metavar="PATH",
        dest="supplementary",
        help=(
            "Additional RDF vocabulary file to merge into the data graph "
            "before validation.  Repeat the flag for multiple files "
            "(e.g. --supplementary bdqdim.ttl --supplementary bdqcrit.ttl). "
            "Use this for vocabulary files whose instances are referenced "
            "in the primary data file but whose full property definitions "
            "live in a separate file."
        ),
    )

    # ── Output options ────────────────────────────────────────────────────
    output_group = p.add_argument_group("output options")

    output_group.add_argument(
        "--output",
        type=Path,
        default=None,
        metavar="PATH",
        help="Write the report to this file instead of stdout.",
    )
    output_group.add_argument(
        "--format",
        choices=list(FORMATTERS),
        default="text",
        help=(
            "Output format: 'text' for human-readable output, "
            "'table' for a tab-separated table, "
            "'json' for machine-readable JSON. "
            "(default: text)"
        ),
    )
    output_group.add_argument(
        "--severity",
        choices=["INFO", "WARNING", "VIOLATION"],
        default="WARNING",
        help=(
            "Minimum severity level to include in the report. "
            "INFO includes all results; "
            "WARNING includes warnings and violations; "
            "VIOLATION includes only hard errors. "
            "(default: WARNING)"
        ),
    )

    # ── Behaviour options ─────────────────────────────────────────────────
    behaviour_group = p.add_argument_group("behaviour options")

    behaviour_group.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print progress messages to stderr while running.",
    )
    behaviour_group.add_argument(
        "--exit-zero",
        action="store_true",
        help=(
            "Always exit with code 0, even when violations are found. "
            "Useful in CI pipelines where the report should be inspected "
            "without failing the build."
        ),
    )

    return p


def _resolve_optional_path(raw) -> Path | None:
    """
    Convert an argparse Path value to None if the user passed an empty
    string (to disable a default), or return the Path unchanged.
    """
    if raw is None:
        return None
    p = Path(raw)
    if str(p) == "":
        return None
    return p


def main():
    parser = build_parser()
    args   = parser.parse_args()

    # Allow the user to pass "" to disable the ont or usecase defaults
    ont_path     = _resolve_optional_path(args.ont)
    usecase_path = _resolve_optional_path(args.usecase)

    # ── Check that all specified files actually exist ─────────────────────
    missing = []

    if not args.data.exists():
        missing.append(f"Data file not found         : {args.data}")
    if not args.shapes.exists():
        missing.append(f"Shapes file not found       : {args.shapes}")
    if ont_path is not None and not ont_path.exists():
        missing.append(f"Ontology file not found     : {ont_path}")
    if usecase_path is not None and not usecase_path.exists():
        missing.append(f"Use Case file not found     : {usecase_path}")
    for sup in args.supplementary:
        if not sup.exists():
            missing.append(f"Supplementary file not found: {sup}")

    if missing:
        for m in missing:
            print(f"ERROR: {m}", file=sys.stderr)
        sys.exit(1)

    # ── Run validation ────────────────────────────────────────────────────
    try:
        filtered_conforms = run_validation(
            data_path           = args.data,
            shapes_path         = args.shapes,
            ont_path            = ont_path,
            usecase_path        = usecase_path,
            supplementary_paths = args.supplementary,
            min_severity        = args.severity,
            output_format       = args.format,
            output_path         = args.output,
            verbose             = args.verbose,
        )
    except Exception as exc:
        print(f"ERROR during validation: {exc}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(2)

    if args.exit_zero:
        sys.exit(0)

    sys.exit(0 if filtered_conforms else 1)


if __name__ == "__main__":
    main()
