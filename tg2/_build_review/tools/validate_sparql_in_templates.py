#!/usr/bin/env python3
"""
Validate and/or report results for SPARQL queries embedded in BDQ markdown templates.

What it does
------------
- Loads the RDF graphs:
  - tg2/_review/dist/bdqtest.ttl
  - tg2/_review/vocabulary/bdqffdq.owl   (this file is Turtle syntax in this repo)
  into a single rdflib.Graph "triplestore" (in-memory).
- Extracts SPARQL code blocks from:
  - tg2/_build_review/templates/supplement/supplement-header.md
  - tg2/_build_review/templates/guide/bdqffdq/bdqffdq-header.md
  where code blocks are fenced with:
      ```sparql
      ...
      ```

- Executes each query against the loaded graph.
- Reports how many result rows the query returns.

@author GitHub Copilot (with human review and adjustments by Paul J. Morris (chicoreus))

Skip directive
--------------
If the line immediately preceding the opening ```sparql fence (ignoring whitespace)
matches:

  <!-- skip when testing -->

(case-insensitive), the query block is identified and reported as SKIPPED and is
not executed. This supports template blocks that are fragments or placeholders.

Modes / options
---------------
Default:
  - Print each query id, source template, and row count.

--strict:
  - Exit with non-zero status if any query:
      * fails to parse/execute, OR
      * returns 0 rows
    Prints which query failed and why.
  - SKIPPED queries do not count as failures.
  - In strict mode, normal per-query output is suppressed:
      * on failure: only failure cases are reported
      * on success: a short summary is printed

--example:
  - Print count plus a single example row (first row) for SELECT queries.
    For ASK queries, prints True/False.
    For CONSTRUCT/DESCRIBE, prints number of triples in result graph.

--all-rows:
  - For SELECT, print all rows.
    For CONSTRUCT/DESCRIBE, print serialized Turtle of the returned graph.
    For ASK, print True/False.

Notes / assumptions
-------------------
- This expects to live in and be run from: tg2/_build_review/tools/
- rdflib SPARQL supports SELECT/ASK/CONSTRUCT/DESCRIBE.
- Queries that rely on PREFIX declarations should include them in the code block.
  If they don't, you can optionally add a default prefix header via --prefix-file
  or adjust DEFAULT_PREFIXES below.

Install
-------
  pip install rdflib

Examples
--------
  python validate_sparql_in_templates.py
  python validate_sparql_in_templates.py --example
  python validate_sparql_in_templates.py --all-rows
  python validate_sparql_in_templates.py --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple

from rdflib import Graph


# Templates that are known (from the conversation) to contain ```sparql fenced blocks.
TEMPLATE_PATHS = [
    Path("../templates/supplement/supplement-header.md"),
    Path("../templates/guide/bdqffdq/bdqffdq-header.md"),
]

# RDF inputs (relative to tg2/_build_review/tools/)
BDQTEST_TTL = Path("../../_review/dist/bdqtest.ttl")
BDQFFDQ_OWL_TTL = Path("../../_review/vocabulary/bdqffdq.owl")


# If you want to inject shared PREFIX lines into queries that omit them, put them here.
# Leave blank by default to avoid changing query semantics.
DEFAULT_PREFIXES = ""


FENCE_RE = re.compile(
    r"```sparql\s*\n(?P<body>.*?)(?:\n```)",
    re.IGNORECASE | re.DOTALL,
)

SKIP_LINE_RE = re.compile(r"^\s*<!--\s*skip when testing\s*-->\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class ExtractedQuery:
    template_path: Path
    line_number: int  # 1-based line where ```sparql starts
    sparql: str
    skipped: bool = False
    skip_reason: str = ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _line_immediately_before(md_text: str, start_index: int) -> str:
    """
    Return the content of the line immediately preceding md_text[start_index],
    where start_index is the index where the opening ```sparql begins.

    If the fence is on the first line, returns "".
    """
    if start_index <= 0:
        return ""
    # Find newline before the fence line
    prev_newline = md_text.rfind("\n", 0, start_index)
    if prev_newline == -1:
        return ""
    # Find newline before that (start of previous line)
    prev_prev_newline = md_text.rfind("\n", 0, prev_newline)
    line_start = 0 if prev_prev_newline == -1 else prev_prev_newline + 1
    return md_text[line_start:prev_newline].rstrip("\r\n")


def _line_number_at(md_text: str, index: int) -> int:
    """
    Convert a character index into a 1-based line number.
    """
    return md_text.count("\n", 0, index) + 1


def extract_sparql_blocks(md_text: str, template_path: Path) -> List[ExtractedQuery]:
    out: List[ExtractedQuery] = []
    for m in FENCE_RE.finditer(md_text):
        body = m.group("body").strip()
        line_number = _line_number_at(md_text, m.start())

        prev_line = _line_immediately_before(md_text, m.start())
        if SKIP_LINE_RE.match(prev_line or ""):
            out.append(
                ExtractedQuery(
                    template_path=template_path,
                    line_number=line_number,
                    sparql=body,
                    skipped=True,
                    skip_reason="skip when testing directive",
                )
            )
        else:
            out.append(ExtractedQuery(template_path=template_path, line_number=line_number, sparql=body))

    return out


def load_graph() -> Graph:
    g = Graph()
    g.parse(BDQTEST_TTL.as_posix(), format="turtle")
    g.parse(BDQFFDQ_OWL_TTL.as_posix(), format="turtle")
    return g


def is_ask_query(sparql: str) -> bool:
    return bool(re.search(r"^\s*ASK\b", sparql, flags=re.IGNORECASE | re.MULTILINE))


def is_construct_query(sparql: str) -> bool:
    return bool(re.search(r"^\s*CONSTRUCT\b", sparql, flags=re.IGNORECASE | re.MULTILINE))


def is_describe_query(sparql: str) -> bool:
    return bool(re.search(r"^\s*DESCRIBE\b", sparql, flags=re.IGNORECASE | re.MULTILINE))


def query_id(q: ExtractedQuery) -> str:
    return f"{q.template_path.name}#sparql line {q.line_number}"


def format_row(row) -> str:
    try:
        labels = list(row.labels)
    except Exception:
        return str(row)
    parts = []
    for lab in labels:
        val = getattr(row, lab, None)
        parts.append(f"{lab}={val}")
    return "; ".join(parts)


def run_one_query(g: Graph, q: ExtractedQuery):
    sparql = (DEFAULT_PREFIXES + "\n" + q.sparql).strip() if DEFAULT_PREFIXES else q.sparql
    return g.query(sparql)


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Extract ```sparql fenced blocks from BDQ markdown templates, execute, and report row counts."
    )
    ap.add_argument("--strict", action="store_true", help="Fail (exit non-zero) if any query errors or returns zero rows.")
    ap.add_argument("--example", action="store_true", help="Print an example row for each query.")
    ap.add_argument("--all-rows", action="store_true", help="Print all rows (SELECT) or full graph (CONSTRUCT/DESCRIBE).")
    ap.add_argument("--limit", type=int, default=None, help="Cap number of rows printed under --all-rows (SELECT only).")
    args = ap.parse_args()

    if args.all_rows and args.example:
        print("ERROR: choose only one of --example or --all-rows", file=sys.stderr)
        raise SystemExit(2)

    quiet = bool(args.strict)

    # Collect queries
    queries: List[ExtractedQuery] = []
    for tp in TEMPLATE_PATHS:
        if not tp.exists():
            print(f"ERROR: template not found: {tp}", file=sys.stderr)
            raise SystemExit(2)
        md = read_text(tp)
        queries.extend(extract_sparql_blocks(md, tp))

    if not queries:
        print("No ```sparql fenced blocks found in the configured templates.", file=sys.stderr)
        raise SystemExit(1)

    for rdf_path in (BDQTEST_TTL, BDQFFDQ_OWL_TTL):
        if not rdf_path.exists():
            print(f"ERROR: RDF input not found: {rdf_path}", file=sys.stderr)
            raise SystemExit(2)

    g = load_graph()

    failures: List[str] = []

    # Summary counters (used mainly for --strict success summary)
    total_blocks = len(queries)
    skipped_blocks = 0
    executed_blocks = 0
    succeeded_blocks = 0
    succeeded_gt1 = 0  # "more than one result" as requested

    for q in queries:
        qid = query_id(q)

        if q.skipped:
            skipped_blocks += 1
            if not quiet:
                print(f"\n== {qid} ==")
                print(f"Source: {q.template_path.as_posix()}")
                print(f"SKIPPED: {q.skip_reason}")
            continue

        executed_blocks += 1

        if not quiet:
            print(f"\n== {qid} ==")
            print(f"Source: {q.template_path.as_posix()}")

        try:
            res = run_one_query(g, q)
        except Exception as e:
            msg = f"{qid}: SPARQL ERROR: {e.__class__.__name__}: {e}"
            failures.append(msg)
            if not quiet:
                print(msg, file=sys.stderr)
            continue

        # Determine result type and count
        try:
            succeeded_blocks += 1

            if is_ask_query(q.sparql):
                ask_val = bool(res)
                if not quiet:
                    print("Type: ASK")
                    print(f"Result: {ask_val}")
                # In strict mode, ASK FALSE counts as "0 rows"
                if args.strict and not ask_val:
                    failures.append(f"{qid}: returned FALSE (treated as 0 rows in strict mode)")
                # For "more than one result", ASK can never be >1; treat TRUE as 1
                continue

            if is_construct_query(q.sparql) or is_describe_query(q.sparql):
                out_graph = getattr(res, "graph", None)
                if out_graph is None:
                    out_graph = Graph()
                    for t in res:
                        out_graph.add(t)
                triple_count = len(out_graph)
                if not quiet:
                    print(f"Type: {'CONSTRUCT' if is_construct_query(q.sparql) else 'DESCRIBE'}")
                    print(f"Triples: {triple_count}")

                if args.strict and triple_count == 0:
                    failures.append(f"{qid}: returned 0 triples")

                if triple_count > 1:
                    succeeded_gt1 += 1

                if args.all_rows and not quiet:
                    print("\n--- Result graph (Turtle) ---")
                    print(out_graph.serialize(format="turtle"))
                elif args.example and not quiet:
                    print("\nExample triples:")
                    shown = 0
                    for t in out_graph:
                        print(f"  {t[0]} {t[1]} {t[2]}")
                        shown += 1
                        if shown >= 5:
                            break
                continue

            # Default assume SELECT-like tabular result
            rows = list(res)
            count = len(rows)
            if not quiet:
                print("Type: SELECT")
                print(f"Rows: {count}")

            if args.strict and count == 0:
                failures.append(f"{qid}: returned 0 rows")

            if count > 1:
                succeeded_gt1 += 1

            if args.example and rows and not quiet:
                print("\nExample row:")
                print(f"  {format_row(rows[0])}")

            if args.all_rows and not quiet:
                print("\nAll rows:")
                limit = args.limit if args.limit is not None else len(rows)
                for i, r in enumerate(rows[:limit], start=1):
                    print(f"{i}. {format_row(r)}")
                if limit < len(rows):
                    print(f"... ({len(rows) - limit} more rows not shown; adjust with --limit or omit it)")

        except Exception as e:
            msg = f"{qid}: RESULT PROCESSING ERROR: {e.__class__.__name__}: {e}"
            failures.append(msg)
            if not quiet:
                print(msg, file=sys.stderr)

    if failures:
        # In strict mode, only report failures.
        print("\n==== Failures ====", file=sys.stderr)
        for f in failures:
            print(f"- {f}", file=sys.stderr)
        if args.strict:
            raise SystemExit(1)
        raise SystemExit(0)

    # Success case
    if args.strict:
        # requested: "a short summary of the number of sparql queries that succeeded and had more than one result"
        print(
            f"STRICT OK: {succeeded_gt1} queries succeeded and returned >1 result "
            f"(executed: {executed_blocks}, skipped: {skipped_blocks}, total blocks: {total_blocks})."
        )
        raise SystemExit(0)

    raise SystemExit(0)


if __name__ == "__main__":
    main()
