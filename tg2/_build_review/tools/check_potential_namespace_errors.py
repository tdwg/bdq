#!/usr/bin/env python3
"""
find_unknown_prefixes.py – Detect unknown / possibly-mistyped namespace
prefixes in a directory tree of Markdown documents.

For each .md file the script:

  1. Reads the namespace-abbreviation table (if any) and merges its prefixes
     with the hard-coded KNOWN_PREFIXES to form that file's "good" set.
  2. Blanks out the table rows and (by default) fenced code blocks so their
     content is not scanned.
  3. Searches the remaining text for ``prefix:LocalName`` patterns whose
     prefix is NOT in the good set — these are potential typos or missing
     table entries.
  4. Reports each suspicious occurrence with its line number and source
     context, and suggests the most similar known-good prefix as a likely
     intended spelling.

Why ``prefix:LocalName`` and not bare ``prefix:``?
---------------------------------------------------
Bare ``prefix:`` without an immediately following local name is
indistinguishable from ordinary prose ("Note: the following…") or YAML
front-matter ("title: My Doc").  Requiring at least one letter/underscore
directly after the colon — no space — keeps the false-positive rate very
low.  The companion ``check_namespaces.py`` handles completeness checking
(used vs declared) for the known-good set, including bare prefixes.

Fenced code blocks (``` / ~~~) are masked out by default because
host-language syntax (Python type annotations, JSON keys, etc.) can look
like CURIEs.  Use ``--include-code-blocks`` to override.

Usage
-----
    python find_unknown_prefixes.py <directory> [options]

Options
-------
  -v / --verbose            List files with no unknown prefixes too.
  -q / --quiet              Show only the global summary; skip per-file detail.
  --include-code-blocks     Also scan inside fenced code blocks.

Exit codes
----------
  0  No unknown prefixes found.
  1  At least one unknown prefix found.
  2  Argument or I/O error.
"""
from __future__ import annotations

import argparse
import difflib
import os
import re
import sys
from collections import defaultdict
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# Configuration — edit these as the document collection grows
# ─────────────────────────────────────────────────────────────────────────────

# URI schemes – never treated as namespace prefixes no matter where they appear.
EXCLUDED_SCHEMES: frozenset[str] = frozenset({
    "http", "https", "urn", "ftp", "ftps", "mailto",
    "file", "data", "tel", "geo", "news", "ldap",
})

# Master list of known-good namespace prefixes.
# This is the union of every "Defined" list observed across the full document
# collection.  Add new entries here when new namespaces are introduced.
KNOWN_PREFIXES: frozenset[str] = frozenset({
    "ac",
    "bdqcrit", "bdqdim", "bdqenh", "bdqffdq",
    "bdqtest",  "bdquc",  "bdqval",
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

# Maximum individual occurrences printed per unknown prefix per file.
# Any extras are summarised as "… and N more".
_MAX_SHOW_PER_PREFIX: int = 8

_RULE = "=" * 72


# ─────────────────────────────────────────────────────────────────────────────
# Compiled regular expressions
# ─────────────────────────────────────────────────────────────────────────────

# Candidate CURIE pattern:  prefix:LocalName
#
# Lookbehind  (?<![:/\w#])  — blocks matches that are:
#   ·  preceded by a word-char  → inside a longer identifier
#   ·  preceded by ':'          → already part of a URI scheme path
#   ·  preceded by '/'          → inside a URL path segment
#   ·  preceded by '#'          → URL fragment identifier  (#rdf:type)
#
# Prefix group  ([a-zA-Z][a-zA-Z0-9_]*)
#   Standard XML / CURIE prefix name.
#
# LocalName group  ([a-zA-Z_][a-zA-Z0-9_]*)
#   Must start IMMEDIATELY after ':' with a letter or underscore.
#   This filters out:
#     "Note: the …"       — space before 'the'
#     "http://…"          — '/' after ':', and scheme is excluded anyway
#     "YAML key: value"   — space before 'value'
#     "version: 1.2"      — digit, not letter / underscore
#     "http:// path"      — already caught by scheme exclusion
_CURIE_RE = re.compile(
    r"(?<![:/\w#])"
    r"([a-zA-Z][a-zA-Z0-9_]*)"    # group 1: prefix
    r":"
    r"([a-zA-Z_][a-zA-Z0-9_]*)",  # group 2: local name (≥ 1 char)
)

# Fenced code blocks  (``` … ``` or ~~~ … ~~~).
# Matched blocks are replaced with spaces (newlines preserved → line numbers
# are not disturbed).
_FENCE_RE = re.compile(
    r"(?P<fence>`{3,}|~{3,})[^\n]*\n"   # opening fence line + optional lang
    r".*?"                                # block content  (non-greedy)
    r"(?P=fence)[ \t]*(?:\n|$)",         # matching closing fence
    re.DOTALL,
)

# Namespace-abbreviation table header
_NS_HDR_RE = re.compile(
    r"\|\s*\*{0,2}\s*Abbreviation\s*\*{0,2}\s*\|"
    r"\s*\*{0,2}\s*Namespace\s*\*{0,2}\s*\|",
    re.IGNORECASE,
)
_BOLD_RE    = re.compile(r"\*+")
_PFXNAME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]*$")


# ─────────────────────────────────────────────────────────────────────────────
# Namespace-table parser  (shared with check_namespaces.py)
# ─────────────────────────────────────────────────────────────────────────────

def parse_ns_table(
    lines: list[str],
) -> tuple[int, int, dict[str, str]] | None:
    """
    Find and parse the first namespace-abbreviation table in *lines*.

    Returns ``(start_0based, end_0based_exclusive, {prefix: uri})`` or
    ``None`` when no valid table is found.
    """
    for i, line in enumerate(lines):
        if not _NS_HDR_RE.search(line):
            continue
        if i + 1 >= len(lines):
            continue
        sep = lines[i + 1].strip()
        if not (sep.startswith("|") and "-" in sep
                and all(c in "| \t:-" for c in sep)):
            continue

        abbrevs: dict[str, str] = {}
        j = i + 2
        while j < len(lines) and lines[j].strip().startswith("|"):
            cells = [c.strip() for c in lines[j].split("|")]
            if len(cells) >= 4:
                raw = _BOLD_RE.sub("", cells[1]).strip()
                uri = _BOLD_RE.sub("", cells[2]).strip()
                if raw.endswith(":"):
                    name = raw[:-1]
                    if (_PFXNAME_RE.match(name)
                            and name.lower() not in EXCLUDED_SCHEMES):
                        abbrevs[name] = uri
            j += 1

        if abbrevs:
            return i, j, abbrevs   # (start_0, end_0_excl, abbrevs)

    return None


# ─────────────────────────────────────────────────────────────────────────────
# Text preparation helpers
# ─────────────────────────────────────────────────────────────────────────────

def blank_line_range(lines: list[str], start: int, end: int) -> list[str]:
    """Return a copy of *lines* with rows [start, end) replaced by ''."""
    out = list(lines)
    for k in range(start, min(end, len(out))):
        out[k] = ""
    return out


def mask_code_fences(text: str) -> str:
    """Replace non-newline characters inside fenced code blocks with spaces."""
    return _FENCE_RE.sub(
        lambda m: re.sub(r"[^\n]", " ", m.group()),
        text,
    )


# ─────────────────────────────────────────────────────────────────────────────
# CURIE scanner
# ─────────────────────────────────────────────────────────────────────────────

def find_curie_candidates(text: str) -> list[tuple[int, str, str]]:
    """
    Return ``[(line_no_1based, prefix, localname), …]`` for every
    ``prefix:LocalName`` pattern found in *text*, excluding URI schemes.
    """
    out: list[tuple[int, str, str]] = []
    for m in _CURIE_RE.finditer(text):
        pfx = m.group(1)
        if pfx.lower() in EXCLUDED_SCHEMES:
            continue
        lno = text[: m.start()].count("\n") + 1
        out.append((lno, pfx, m.group(2)))
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Typo suggestion
# ─────────────────────────────────────────────────────────────────────────────

def suggest_fixes(prefix: str, good: frozenset[str]) -> list[str]:
    """Return up to 3 known-good prefixes whose name is close to *prefix*."""
    return difflib.get_close_matches(prefix, sorted(good), n=3, cutoff=0.6)


# ─────────────────────────────────────────────────────────────────────────────
# Per-file analysis
# ─────────────────────────────────────────────────────────────────────────────

def analyze_file(
    path: Path,
    include_code_blocks: bool,
) -> dict | None:
    """
    Analyse *path* for unknown ``prefix:LocalName`` usages.

    Returns a result dict (see keys below) or ``None`` on read error.

    Result keys
    -----------
    source_lines  list[str]             original file lines (for context display)
    table_abbrevs dict[str, str]        prefixes from the NS table (may be {})
    table_range   (int, int) | None     1-based (start, end_inclusive)
    good_prefixes frozenset[str]        KNOWN_PREFIXES ∪ table_abbrevs
    unknowns      list[(lno, pfx, loc)] deduplicated, sorted by line number
    """
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"WARNING: cannot read {path}: {exc}", file=sys.stderr)
        return None

    source_lines = raw.splitlines()
    working      = list(source_lines)

    # ── Parse and mask the namespace abbreviation table ───────────────────
    table_abbrevs: dict[str, str] = {}
    table_range:   tuple[int, int] | None = None

    tbl = parse_ns_table(working)
    if tbl is not None:
        ts, te, table_abbrevs = tbl
        table_range = (ts + 1, te)            # 1-based inclusive last row
        working = blank_line_range(working, ts, te)

    good = KNOWN_PREFIXES | frozenset(table_abbrevs)

    # ── Prepare the text for scanning ─────────────────────────────────────
    text = "\n".join(working)
    if not include_code_blocks:
        text = mask_code_fences(text)

    # ── Find candidates and filter to unknowns (deduplicated) ─────────────
    seen:     set[tuple[int, str, str]]  = set()
    unknowns: list[tuple[int, str, str]] = []

    for item in find_curie_candidates(text):
        lno, pfx, loc = item
        if pfx not in good and item not in seen:
            seen.add(item)
            unknowns.append(item)

    unknowns.sort(key=lambda t: (t[1], t[0]))   # sort by prefix then line

    return {
        "source_lines":  source_lines,
        "table_abbrevs": table_abbrevs,
        "table_range":   table_range,
        "good_prefixes": good,
        "unknowns":      unknowns,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Per-file report
# ─────────────────────────────────────────────────────────────────────────────

def report_file(path: Path, info: dict) -> None:
    source   = info["source_lines"]
    unknowns = info["unknowns"]
    n_unique = len({pfx for _, pfx, _ in unknowns})

    print(f"\n{_RULE}")
    print(f"  FILE : {path}")
    print(_RULE)

    if info["table_range"]:
        ts, te = info["table_range"]
        print(f"  Namespace table  : lines {ts}–{te}  "
              f"({len(info['table_abbrevs'])} entries)")

    print(f"  Unknown prefixes : {n_unique} unique  "
          f"({len(unknowns)} occurrence(s) total)\n")

    # Group occurrences by prefix
    by_pfx: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for lno, pfx, loc in unknowns:
        by_pfx[pfx].append((lno, loc))

    for pfx in sorted(by_pfx):
        hits = sorted(by_pfx[pfx])       # sort by line number
        sug  = suggest_fixes(pfx, info["good_prefixes"])

        if sug:
            sug_str = ("  — did you mean: "
                       + ", ".join(f"{s}:" for s in sug) + "?")
        else:
            sug_str = "  — (no similar known prefix found)"

        print(f"  ?? {pfx}:{sug_str}")

        for lno, loc in hits[: _MAX_SHOW_PER_PREFIX]:
            ctx = source[lno - 1].strip() if 0 <= lno - 1 < len(source) else ""
            if len(ctx) > 110:
                ctx = ctx[:107] + "..."
            print(f"       line {lno:>5}:  {pfx}:{loc}")
            if ctx:
                print(f"                   -> {ctx}")

        extra = len(hits) - _MAX_SHOW_PER_PREFIX
        if extra > 0:
            print(f"       … and {extra} more occurrence(s) not shown")
        print()


# ─────────────────────────────────────────────────────────────────────────────
# Directory scanner
# ─────────────────────────────────────────────────────────────────────────────

def scan_directory(
    root: str,
    verbose: bool,
    quiet: bool,
    include_code_blocks: bool,
) -> tuple[int, int, int]:
    """
    Walk *root* recursively, report unknown namespace prefixes in .md files.

    Returns ``(n_files, n_files_with_issues, n_total_occurrences)``.
    """
    root_path = Path(root)
    md_files  = sorted(root_path.rglob("*.md"))

    if not md_files:
        print(f"No .md files found under '{root}'.")
        return 0, 0, 0

    n_files = n_issues = n_occ = 0

    # Accumulator: {unknown_prefix: {filepath_str: [line_nos]}}
    global_map: dict[str, dict[str, list[int]]] = (
        defaultdict(lambda: defaultdict(list))
    )

    for path in md_files:
        n_files += 1
        info = analyze_file(path, include_code_blocks)
        if info is None:
            continue                       # unreadable – warning already printed

        if not info["unknowns"]:
            if verbose:
                print(f"[ok]  {path}")
            continue

        n_issues += 1
        n_occ    += len(info["unknowns"])

        for lno, pfx, _ in info["unknowns"]:
            global_map[pfx][str(path)].append(lno)

        if not quiet:
            report_file(path, info)

    # ── Global summary ────────────────────────────────────────────────────
    print(f"\n{_RULE}")
    print("  GLOBAL SUMMARY")
    print(_RULE)
    print(f"  .md files scanned           : {n_files}")
    print(f"  files with unknown prefixes : {n_issues}")
    print(f"  total unknown occurrences   : {n_occ}")

    if global_map:
        w = 28
        print()
        print(f"  {'UNKNOWN PREFIX':<{w}}  {'OCC':>5}  {'FILES':>5}  "
              f"SUGGESTION(S)")
        print(f"  {'-' * w}  {'-----':>5}  {'-----':>5}  {'-' * 32}")
        for pfx in sorted(global_map):
            n_f     = len(global_map[pfx])
            n_o     = sum(len(v) for v in global_map[pfx].values())
            sug     = suggest_fixes(pfx, KNOWN_PREFIXES)
            sug_str = ", ".join(f"{s}:" for s in sug) if sug else "—"
            print(f"  {pfx + ':':<{w}}  {n_o:>5}  {n_f:>5}  {sug_str}")

    print(_RULE)
    return n_files, n_issues, n_occ


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description=(
            "Find unknown / possibly-mistyped namespace prefixes "
            "in a tree of Markdown files."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exit codes:\n"
            "  0  no unknown prefixes found\n"
            "  1  at least one unknown prefix found\n"
            "  2  argument or I/O error\n"
        ),
    )
    ap.add_argument("directory", help="Root directory to scan recursively.")
    ap.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Also list files in which no unknown prefixes were found.",
    )
    ap.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Show only the global summary; suppress per-file detail.",
    )
    ap.add_argument(
        "--include-code-blocks",
        action="store_true",
        help=(
            "Also scan inside fenced code blocks.  "
            "Expect more false positives from host-language syntax."
        ),
    )
    args = ap.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a directory.", file=sys.stderr)
        sys.exit(2)

    _, n_issues, _ = scan_directory(
        args.directory,
        verbose=args.verbose,
        quiet=args.quiet,
        include_code_blocks=args.include_code_blocks,
    )
    sys.exit(1 if n_issues else 0)


if __name__ == "__main__":
    main()
