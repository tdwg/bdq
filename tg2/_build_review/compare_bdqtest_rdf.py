#!/usr/bin/env python3
"""
compare_bdqtest_rdf.py — Validation harness for bdqtest RDF serializations.

Compares generated RDF outputs against baseline files in tg2/_review/dist/
and reports:
  - byte-level equality (informational)
  - RDF graph isomorphism (authoritative pass/fail)
  - if non-isomorphic, a summary of missing and extra triples to aid debugging

Usage (from repo root):
  # Compare generated files against the dist/ baselines
  python3 tg2/_build_review/compare_bdqtest_rdf.py \\
      --new-ttl    /path/to/new_bdqtest.ttl \\
      --new-rdfxml /path/to/new_bdqtest.xml \\
      --new-jsonld /path/to/new_bdqtest.json \\
      --baseline-dir tg2/_review/dist

  # Generate and compare in a single step (builds to /tmp then compares)
  python3 tg2/_build_review/compare_bdqtest_rdf.py --auto-build

All three serializations are parsed independently and checked for graph
isomorphism against the corresponding baseline file.  Byte equality is
reported as informational only (serializer formatting is not guaranteed to
match across rdflib versions or runs).
"""

import argparse
import os
import subprocess
import sys
import tempfile

try:
    from rdflib import Graph
    from rdflib.compare import isomorphic, to_isomorphic, graph_diff
except ImportError:
    print("ERROR: rdflib is required. Install with: pip install rdflib",
          file=sys.stderr)
    sys.exit(1)

# Formats to check: (description, extension, rdflib_format)
_FORMATS = [
    ("Turtle",   "ttl",  "turtle"),
    ("RDF/XML",  "xml",  "xml"),
    ("JSON-LD",  "json", "json-ld"),
]

_THIS_DIR   = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT  = os.path.dirname(os.path.dirname(_THIS_DIR))
_BUILDER    = os.path.join(_THIS_DIR, "build_bdqtest_rdf.py")
_DIST_DIR   = os.path.join(_REPO_ROOT, "tg2", "_review", "dist")

# Default input CSV paths relative to repo root
_DEFAULT_INPUTS = {
    "--in-term-versions":   "tg2/_review/vocabulary/bdqtest_term_versions.csv",
    "--guid-file":          "tg2/core/TG2_tests_additional_guids.csv",
    "--ie-guid-file":       "tg2/core/information_element_guids.csv",
    "--policy-guid-file":   "tg2/core/TG2_policy_guids.csv",
    "--citation-guid-file": "tg2/core/TG2_citation_guids.csv",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _bytes_equal(path_a: str, path_b: str) -> bool:
    with open(path_a, 'rb') as fa, open(path_b, 'rb') as fb:
        return fa.read() == fb.read()


def _parse_graph(path: str, fmt: str) -> Graph:
    g = Graph()
    g.parse(path, format=fmt)
    return g


def _diff_report(baseline: Graph, candidate: Graph, max_triples: int = 20
                 ) -> str:
    """Return a short text report of missing / extra triples."""
    gb = to_isomorphic(baseline)
    gc = to_isomorphic(candidate)
    _, only_baseline, only_candidate = graph_diff(gb, gc)

    lines = []
    if only_baseline:
        lines.append(
            f"  MISSING from candidate ({len(only_baseline)} triples, "
            f"showing first {min(max_triples, len(only_baseline))}):"
        )
        for s, p, o in list(only_baseline)[:max_triples]:
            lines.append(f"    - {s!r}  {p!r}  {o!r}")
    if only_candidate:
        lines.append(
            f"  EXTRA in candidate ({len(only_candidate)} triples, "
            f"showing first {min(max_triples, len(only_candidate))}):"
        )
        for s, p, o in list(only_candidate)[:max_triples]:
            lines.append(f"    + {s!r}  {p!r}  {o!r}")
    return "\n".join(lines)


def compare_one(label: str, ext: str, fmt: str,
                new_path: str, baseline_dir: str) -> bool:
    """
    Compare one serialization format.  Returns True if graph-isomorphic.
    """
    baseline_path = os.path.join(baseline_dir, f"bdqtest.{ext}")
    ok = True

    print(f"\n{'='*60}")
    print(f"  {label}  —  {os.path.basename(new_path)}")
    print(f"{'='*60}")

    # Byte equality
    byte_eq = _bytes_equal(new_path, baseline_path)
    print(f"  Byte equality:        {'YES' if byte_eq else 'NO  (informational)'}")

    # Parse both
    try:
        baseline_g = _parse_graph(baseline_path, fmt)
    except Exception as exc:
        print(f"  ERROR parsing baseline {baseline_path}: {exc}")
        return False
    try:
        new_g = _parse_graph(new_path, fmt)
    except Exception as exc:
        print(f"  ERROR parsing candidate {new_path}: {exc}")
        return False

    print(f"  Baseline triples:     {len(baseline_g)}")
    print(f"  Candidate triples:    {len(new_g)}")

    iso = isomorphic(baseline_g, new_g)
    print(f"  Graph isomorphism:    {'PASS ✓' if iso else 'FAIL ✗'}")
    if not iso:
        ok = False
        print(_diff_report(baseline_g, new_g))

    return ok


def build_outputs(out_dir: str) -> dict:
    """Run build_bdqtest_rdf.py and return {ext: path} for each output."""
    paths = {}
    cmd = [sys.executable, _BUILDER]
    for flag, rel in _DEFAULT_INPUTS.items():
        cmd += [flag, os.path.join(_REPO_ROOT, rel)]
    for desc, ext, fmt in _FORMATS:
        out = os.path.join(out_dir, f"new_bdqtest.{ext}")
        flag = {"ttl": "--out-ttl", "xml": "--out-rdfxml", "json": "--out-jsonld"}[ext]
        cmd += [flag, out]
        paths[ext] = out

    print("Generating RDF outputs …", file=sys.stderr)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: build script failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    sys.stderr.write(result.stderr)
    return paths


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument('--new-ttl',    default=None,
                   help='Candidate Turtle file (required unless --auto-build)')
    p.add_argument('--new-rdfxml', default=None,
                   help='Candidate RDF/XML file (required unless --auto-build)')
    p.add_argument('--new-jsonld', default=None,
                   help='Candidate JSON-LD file (required unless --auto-build)')
    p.add_argument('--baseline-dir', default=_DIST_DIR,
                   help=f'Directory containing baseline bdqtest.* files '
                        f'(default: {_DIST_DIR})')
    p.add_argument('--auto-build', action='store_true',
                   help='Generate candidate outputs via build_bdqtest_rdf.py '
                        'before comparing (writes to a temp directory)')
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    if args.auto_build:
        tmpdir = tempfile.mkdtemp(prefix='bdqtest_compare_')
        paths  = build_outputs(tmpdir)
        new_ttl    = paths['ttl']
        new_rdfxml = paths['xml']
        new_jsonld = paths['json']
    else:
        if not (args.new_ttl and args.new_rdfxml and args.new_jsonld):
            print("ERROR: provide --new-ttl, --new-rdfxml, --new-jsonld or "
                  "use --auto-build.", file=sys.stderr)
            sys.exit(1)
        new_ttl    = args.new_ttl
        new_rdfxml = args.new_rdfxml
        new_jsonld = args.new_jsonld

    candidate_paths = {
        "ttl":  new_ttl,
        "xml":  new_rdfxml,
        "json": new_jsonld,
    }

    all_pass = True
    for desc, ext, fmt in _FORMATS:
        ok = compare_one(desc, ext, fmt,
                         candidate_paths[ext], args.baseline_dir)
        if not ok:
            all_pass = False

    print(f"\n{'='*60}")
    if all_pass:
        print("  Overall result: ALL PASS ✓")
    else:
        print("  Overall result: FAIL — see details above")
    print(f"{'='*60}\n")

    sys.exit(0 if all_pass else 1)


if __name__ == '__main__':
    main()
