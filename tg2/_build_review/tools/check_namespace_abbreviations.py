#!/usr/bin/env python3
"""
check_namespaces.py – Validate namespace abbreviation tables in Markdown files.

Recursively scans a directory for .md files that contain a namespace-
abbreviation table (a Markdown table whose header row contains the words
"Abbreviation" and "Namespace"), then reports:

Per file:
  (1) Namespace prefixes used in the document (outside the table) that are
      NOT declared in the table.
  (2) Namespace prefixes declared in the table that are NOT used anywhere
      in the document (outside the table itself).

Globally (after all files):
  (3) A markdown table of every unique Abbreviation | Namespace pair found
      across all scanned documents, sorted alphabetically by abbreviation.
  (4) Any prefix in KNOWN_PREFIXES not found in any document's table.
  (5) Any prefix that resolves to more than one namespace URI (conflict).

Prefix detection
----------------
Rather than an open-ended CURIE regex, the script searches for each member
of the hard-coded KNOWN_PREFIXES set (the union of all "Defined" prefixes
observed across the full document collection).  Both "prefix:LocalName" and
bare "prefix:" forms are matched.  Each pattern uses a negative lookbehind
so it is never matched inside a URI or a longer identifier.

Edit KNOWN_PREFIXES below as the collection grows.

Usage
-----
    python check_namespaces.py <directory> [-v] [-q] [--summary-md FILE]

Options
-------
  -v / --verbose     Also list files that have no namespace table.
  -q / --quiet       Only print files that have at least one mismatch.
  --summary-md FILE  Write the global summary markdown table to FILE.

Exit codes
----------
  0  No mismatches found.
  1  At least one mismatch found.
  2  Argument or I/O error.
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# URI schemes – never treated as namespace abbreviations
# ---------------------------------------------------------------------------
EXCLUDED_SCHEMES: frozenset[str] = frozenset({
    "http", "https", "urn", "ftp", "ftps", "mailto",
    "file", "data", "tel", "geo", "news", "ldap",
})

# ---------------------------------------------------------------------------
# Master prefix list
#
# The union of every "Defined" set observed across the full document
# collection.  Edit this set to add new prefixes as the collection grows.
# ---------------------------------------------------------------------------
KNOWN_PREFIXES: frozenset[str] = frozenset({
    "ac",
    "bdqcrit", "bdqdim", "bdqenh", "bdqffdq",
    "bdqtest", "bdquc", "bdqval",
    "dc", "dcmitype", "dcterms", "dcat", "dqv",
    "dwc", "dwciri",
    "foaf",
    "ldqd",
    "mids",
    "oa", "owl",
    "prov",
    "rdf", "rdfs",
    "skos",
    "tdwgutility",
    "xsd",
})

# ---------------------------------------------------------------------------
# Per-prefix search patterns
#
# Negative lookbehind  (?<![:/\w])
#   The prefix must NOT be immediately preceded by a word character, ':'
#   or '/'.  This prevents false matches inside URIs
#   (e.g. ".org/dwc/terms/") and inside longer identifiers.
#
# No lookahead after ':'
#   Accepts both "prefix:LocalName" AND bare "prefix:" (e.g. in prose).
# ---------------------------------------------------------------------------
_PREFIX_RE: dict[str, re.Pattern] = {
    p: re.compile(r"(?<![:/\w])" + re.escape(p) + r":")
    for p in KNOWN_PREFIXES
}

_RULE = "=" * 72

# ---------------------------------------------------------------------------
# Table-parsing helpers
# ---------------------------------------------------------------------------
_HEADER_RE = re.compile(
    r"\|\s*\*{0,2}\s*Abbreviation\s*\*{0,2}\s*\|"
    r"\s*\*{0,2}\s*Namespace\s*\*{0,2}\s*\|",
    re.IGNORECASE,
)
_BOLD_RE     = re.compile(r"\*+")
_PREFIX_NAME = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]*$")   # valid prefix name


def _is_separator_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and "-" in s and all(c in "| \t:-" for c in s)


def _pattern_for(prefix: str) -> re.Pattern:
    """Return (and cache) the compiled search pattern for *prefix*."""
    if prefix not in _PREFIX_RE:
        _PREFIX_RE[prefix] = re.compile(
            r"(?<![:/\w])" + re.escape(prefix) + r":"
        )
    return _PREFIX_RE[prefix]


# ---------------------------------------------------------------------------
# Table detection
# ---------------------------------------------------------------------------

def find_namespace_table(
    lines: list[str],
) -> tuple[int, int, dict[str, str]] | None:
    """
    Find the first namespace-abbreviation table in *lines*.

    Returns ``(table_start, table_end, abbreviations)`` where:
      table_start    0-based index of the header row.
      table_end      0-based exclusive upper bound (first line after table).
                     Equals the 1-based inclusive line number of the last row.
      abbreviations  {prefix_without_colon: namespace_uri}

    Returns ``None`` when no suitable table is found.
    """
    for i, line in enumerate(lines):
        if not _HEADER_RE.search(line):
            continue
        # Require a separator row immediately after the header
        if i + 1 >= len(lines) or not _is_separator_row(lines[i + 1]):
            continue

        abbrevs: dict[str, str] = {}
        j = i + 2   # index of first data row

        while j < len(lines) and lines[j].strip().startswith("|"):
            cells = [c.strip() for c in lines[j].split("|")]
            if len(cells) >= 4:
                raw  = _BOLD_RE.sub("", cells[1]).strip()
                uri  = _BOLD_RE.sub("", cells[2]).strip()
                name = raw[:-1] if raw.endswith(":") else None
                if (
                    name
                    and _PREFIX_NAME.match(name)
                    and name.lower() not in EXCLUDED_SCHEMES
                ):
                    abbrevs[name] = uri
            j += 1

        if abbrevs:
            return i, j, abbrevs     # j is 0-based exclusive end of table

    return None


# ---------------------------------------------------------------------------
# Prefix-usage detection
# ---------------------------------------------------------------------------

def find_used_prefixes(
    text: str,
    search_set: frozenset[str],
) -> set[str]:
    """
    Return the subset of *search_set* whose prefixes appear in *text*.

    Matches both ``prefix:LocalName`` and bare ``prefix:`` forms.
    """
    return {p for p in search_set if _pattern_for(p).search(text)}


# ---------------------------------------------------------------------------
# Per-file analysis
# ---------------------------------------------------------------------------

def analyze_file(path: Path) -> dict | None:
    """
    Analyse one Markdown file for namespace-prefix consistency.

    Returns ``None`` when the file has no namespace abbreviation table.

    Otherwise returns a dict:
      table_abbrevs      {prefix: ns_uri}   — from the table
      used_prefixes      set[str]           — found outside the table
      missing_from_table sorted list        — used but not declared
      missing_from_doc   sorted list        — declared but not used
      table_line_start   int (1-based)
      table_line_end     int (1-based inclusive last row)
    """
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"WARNING: cannot read {path}: {exc}", file=sys.stderr)
        return None

    lines  = content.splitlines()
    result = find_namespace_table(lines)
    if result is None:
        return None

    table_start, table_end, table_abbrevs = result

    # Remove the table block before scanning for usages so that the
    # abbreviation declarations themselves do not count as usages.
    non_table_text = "\n".join(lines[:table_start] + lines[table_end:])

    # Search for KNOWN_PREFIXES ∪ any prefix declared in this table.
    # The union handles tables that declare a prefix not yet in KNOWN_PREFIXES.
    search_set = KNOWN_PREFIXES | frozenset(table_abbrevs)
    used       = find_used_prefixes(non_table_text, search_set)

    table_keys = set(table_abbrevs)
    return {
        "table_abbrevs":      table_abbrevs,
        "used_prefixes":      used,
        "missing_from_table": sorted(used - table_keys),
        "missing_from_doc":   sorted(table_keys - used),
        "table_line_start":   table_start + 1,
        "table_line_end":     table_end,    # 0-based excl == 1-based incl last row
    }


# ---------------------------------------------------------------------------
# Global namespace summary helpers
# ---------------------------------------------------------------------------

def _build_summary(
    global_ns: dict[str, set[str]],
) -> tuple[list[tuple[str, str]], dict[str, list[str]], list[str]]:
    """
    Derive summary data from *global_ns* ({prefix: {uri, ...}}).

    Returns
    -------
    rows            Sorted list of (prefix, uri) unique pairs.
    conflicts       {prefix: [uri, ...]} for prefixes with multiple URIs.
    never_in_table  Sorted list of KNOWN_PREFIXES not seen in any table.
    """
    rows: list[tuple[str, str]] = [
        (p, uri)
        for p in sorted(global_ns)
        for uri in sorted(global_ns[p])
    ]
    conflicts = {
        p: sorted(uris)
        for p, uris in global_ns.items()
        if len(uris) > 1
    }
    never_in_table = sorted(KNOWN_PREFIXES - set(global_ns))
    return rows, conflicts, never_in_table


def print_global_summary(
    global_ns: dict[str, set[str]],
    summary_md: str | None = None,
) -> None:
    """
    Print the global namespace summary to stdout.
    Optionally write it as an aligned, standalone Markdown file to *summary_md*.
    """
    rows, conflicts, never_in_table = _build_summary(global_ns)

    # ── Console output (raw Markdown – renders in any viewer) ─────────────
    print(f"\n{_RULE}")
    print("  GLOBAL SUMMARY: All unique namespace abbreviations across all documents")
    print(_RULE)
    print()

    print("| **Abbreviation** | **Namespace** |")
    print("| :--------------- | :------------ |")
    for prefix, uri in rows:
        print(f"| {prefix}: | {uri} |")
    print()

    if conflicts:
        print("  CONFLICTS – abbreviation mapped to more than one namespace URI:")
        for p in sorted(conflicts):
            print(f"    {p}:")
            for uri in conflicts[p]:
                print(f"      -> {uri}")
        print()

    if never_in_table:
        print("  Known prefixes NOT found in any document's abbreviation table:")
        for p in never_in_table:
            print(f"    {p}:")
    else:
        print("  All known prefixes appear in at least one document's table.")
    print()

    if not summary_md:
        return

    # ── Standalone Markdown file (column-aligned) ─────────────────────────
    a_hdr = "**Abbreviation**"
    n_hdr = "**Namespace**"

    # Compute column widths from data (minimum = header width)
    a_w = max(len(a_hdr), max((len(p) + 1 for p, _ in rows), default=0))
    n_w = max(len(n_hdr), max((len(u)     for _, u in rows), default=0))

    def _trow(abbrev: str, ns: str) -> str:
        return f"| {abbrev:<{a_w}} | {ns:<{n_w}} |"

    md: list[str] = [
        "# Namespace Abbreviations – Global Summary",
        "",
        "All unique `Abbreviation | Namespace` pairs found across every"
        " scanned document, sorted alphabetically by abbreviation.",
        "",
        _trow(a_hdr, n_hdr),
        _trow("-" * a_w, "-" * n_w),
    ]
    for prefix, uri in rows:
        md.append(_trow(f"{prefix}:", uri))
    md.append("")

    if conflicts:
        md += [
            "",
            "## Conflicts",
            "",
            "These abbreviations resolve to **more than one** namespace URI"
            " across the scanned documents:",
            "",
        ]
        for p in sorted(conflicts):
            md.append(f"- `{p}:`")
            for uri in conflicts[p]:
                md.append(f"  - `{uri}`")
        md.append("")

    if never_in_table:
        md += [
            "",
            "## Master-list prefixes absent from all tables",
            "",
            "These prefixes are in `KNOWN_PREFIXES` but were not declared in"
            " any scanned document's namespace abbreviation table:",
            "",
        ]
        for p in never_in_table:
            md.append(f"- `{p}:`")
        md.append("")

    try:
        Path(summary_md).write_text("\n".join(md) + "\n", encoding="utf-8")
        print(f"  Summary markdown written to: {summary_md}\n")
    except OSError as exc:
        print(f"WARNING: cannot write {summary_md}: {exc}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Directory scanner / main reporter
# ---------------------------------------------------------------------------

def scan_directory(
    root: str,
    verbose: bool = False,
    quiet: bool = False,
    summary_md: str | None = None,
) -> tuple[int, int, int]:
    """
    Recursively scan *root* for .md files and report namespace issues.

    Returns ``(total_files, files_with_tables, files_with_issues)``.
    """
    root_path = Path(root)
    md_files  = sorted(root_path.rglob("*.md"))

    if not md_files:
        print(f"No .md files found under '{root}'.")
        return 0, 0, 0

    total = tables = issues = 0
    global_ns: dict[str, set[str]] = defaultdict(set)

    for path in md_files:
        total += 1
        result = analyze_file(path)

        if result is None:
            if verbose:
                print(f"[no table]  {path}")
            continue

        tables += 1
        for prefix, uri in result["table_abbrevs"].items():
            global_ns[prefix].add(uri)

        has_issues = bool(result["missing_from_table"] or result["missing_from_doc"])
        if has_issues:
            issues += 1
        if not has_issues and quiet:
            continue

        # ── Per-file report ───────────────────────────────────────────────
        print(f"\n{_RULE}")
        print(f"  FILE : {path}")
        print(f"{_RULE}")
        print(
            f"  Table   : lines {result['table_line_start']}–"
            f"{result['table_line_end']}"
            f"  ({len(result['table_abbrevs'])} entries)"
        )
        print(
            "  Defined : "
            + (
                ", ".join(f"{p}:" for p in sorted(result["table_abbrevs"]))
                or "(none)"
            )
        )
        print(
            "  Used    : "
            + (
                ", ".join(f"{p}:" for p in sorted(result["used_prefixes"]))
                or "(none)"
            )
        )

        mft = result["missing_from_table"]
        if mft:
            print(
                f"\n  !! {len(mft)} prefix(es) USED in document"
                " but NOT declared in table:"
            )
            for p in mft:
                print(f"       {p}:")
        else:
            print("\n  OK  All used prefixes are declared in the table.")

        mfd = result["missing_from_doc"]
        if mfd:
            print(
                f"\n  !! {len(mfd)} prefix(es) declared in table"
                " but NOT used in document:"
            )
            for p in mfd:
                print(f"       {p}:  ->  {result['table_abbrevs'][p]}")
        else:
            print("\n  OK  All table entries are used in the document.")

    # ── Scan totals ───────────────────────────────────────────────────────
    print(f"\n{_RULE}")
    print(f"  .md files scanned     : {total}")
    print(f"  files with NS tables  : : {tables}")
    print(f"  files with mismatches : {issues}")
    print(_RULE)

    if global_ns:
        print_global_summary(global_ns, summary_md)

    return total, tables, issues


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Check namespace abbreviation consistency in Markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exit codes:\n"
            "  0  no mismatches found\n"
            "  1  at least one mismatch found\n"
            "  2  argument or I/O error\n"
        ),
    )
    parser.add_argument(
        "directory",
        help="Root directory to scan recursively for .md files.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Also list .md files that contain no namespace abbreviation table.",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Only print output for files that have at least one mismatch.",
    )
    parser.add_argument(
        "--summary-md",
        metavar="FILE",
        help="Write the global namespace summary as a standalone Markdown file.",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a directory.", file=sys.stderr)
        sys.exit(2)

    _total, _tables, issues = scan_directory(
        args.directory,
        verbose=args.verbose,
        quiet=args.quiet,
        summary_md=args.summary_md,
    )
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
