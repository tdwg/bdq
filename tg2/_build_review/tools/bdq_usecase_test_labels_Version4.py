#!/usr/bin/env python3
"""
List BDQ Tests by Use Case from bdqtest.ttl, excluding `MultiRecord` `Measures`.

Outputs pairs of:
- useCaseName: a CURIE-like identifier for the `Use Case` (e.g., "bdq:Biotic-Relationships")
- testLabel: the Test's rdfs:label (e.g., "VALIDATION_COUNTRYCODE_STANDARD")

Relationship pattern (from bdqtest.ttl)
---------------------------------------
`Use Cases` are related to Tests via Policies:
  ?policy bdqffdq:hasUseCase ?useCase ;
          bdqffdq:includesInPolicy ?test .

Exclusion
---------
Exclude Tests that are `MultiRecord` `Measures`, i.e.:
  ?test a bdqffdq:Measure ;
        bdqffdq:hasResourceType bdqffdq:MultiRecord .

This matches your concrete bdqtest.ttl example:
  ... a bdqffdq:Measure ;
      bdqffdq:hasResourceType bdqffdq:MultiRecord ;
      rdfs:label "MULTIRECORD_MEASURE_..." .

Output
------
- Default: TSV to `usecase_tests.tsv`
- Optional: CSV to `usecase_tests.csv`

The output filename extension is chosen based on `--format` when --out is omitted.

Usage
-----
  pip install rdflib

  python bdq_usecase_test_labels.py path/to/bdqtest.ttl
  python bdq_usecase_test_labels.py path/to/bdqtest.ttl --format csv
  python bdq_usecase_test_labels.py path/to/bdqtest.ttl --format csv --out my_pairs.csv
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable, List, Tuple

from rdflib import Graph


SPARQL = """
PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>

PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdq:     <https://rs.tdwg.org/bdq/terms/>

SELECT DISTINCT
  (IF(STRSTARTS(STR(?useCase), STR(bdq:)),
      CONCAT("bdq:", STRAFTER(STR(?useCase), STR(bdq:))),
      STR(?useCase)
  ) AS ?useCaseName)
  ?testLabel
WHERE {
  ?policy bdqffdq:hasUseCase ?useCase ;
          bdqffdq:includesInPolicy ?test .

  ?test rdfs:label ?testLabel .

  # Exclude MultiRecord Measures:
  FILTER NOT EXISTS {
    ?test a bdqffdq:Measure ;
          bdqffdq:hasResourceType bdqffdq:MultiRecord .
  }
}
ORDER BY LCASE(STR(?useCaseName)) LCASE(STR(?testLabel))
"""


def run_query(ttl_path: Path) -> List[Tuple[str, str]]:
    g = Graph()
    g.parse(ttl_path.as_posix(), format="turtle")

    rows: List[Tuple[str, str]] = []
    for r in g.query(SPARQL):
        rows.append((str(r.useCaseName), str(r.testLabel)))
    return rows


def write_tsv(rows: Iterable[Tuple[str, str]], out_path: Path) -> None:
    lines = ["useCaseName\ttestLabel"]
    for use_case_name, test_label in rows:
        lines.append(f"{use_case_name}\t{test_label}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(rows: Iterable[Tuple[str, str]], out_path: Path) -> None:
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["useCaseName", "testLabel"])
        for use_case_name, test_label in rows:
            w.writerow([use_case_name, test_label])


def default_out_path(fmt: str) -> Path:
    return Path("usecase_tests.csv" if fmt == "csv" else "usecase_tests.tsv")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="List (Use Case name, Test rdfs:label) pairs from bdqtest.ttl, excluding MultiRecord Measures."
    )
    ap.add_argument("ttl", type=Path, help="Path to bdqtest.ttl")
    ap.add_argument("--format", choices=("tsv", "csv"), default="tsv", help="Output format")
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output filename. If omitted, a default name with a matching extension is used.",
    )
    args = ap.parse_args()

    out_path = args.out or default_out_path(args.format)

    rows = run_query(args.ttl)

    if args.format == "csv":
        write_csv(rows, out_path)
    else:
        write_tsv(rows, out_path)

    print(f"Wrote {len(rows)} rows to {out_path} ({args.format.upper()})")


if __name__ == "__main__":
    main()