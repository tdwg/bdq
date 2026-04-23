#!/usr/bin/env python3
"""
List BDQ Tests by Use Case from bdqtest.ttl, excluding `MultiRecord` `Measures`.

@author: GitHub copilot with human review and adjustments by Paul J. Morris

Outputs pairs of:
- useCaseName: a CURIE-like identifier for the `Use Case` (e.g., "bdqval:Biotic-Relationships")
- testLabel: the Test's rdfs:label (e.g., "VALIDATION_COUNTRYCODE_STANDARD")

Optional enhancements:
- Filter to a single `Use Case` by its computed useCaseName (e.g., "bdqval:Taxon-Management").
- Include the `rdfs:comment` from the `Specification` related to the Test via the appropriate `Method`.

Important modeling assumption
-----------------------------
This script is designed to run with ONLY bdqtest.ttl loaded (no bdqffdq.owl),
so it MUST NOT rely on subclass reasoning such as:
  ?test a bdqffdq:DataQualityNeed .
  ?method a bdqffdq:Method .

Instead, it explicitly enumerates the concrete Test types and Method types used
in bdqtest.ttl.

Relationship patterns (from bdqtest.ttl)
----------------------------------------
Use Cases are related to Tests via Policies:
  ?policy bdqffdq:hasUseCase ?useCase ;
          bdqffdq:includesInPolicy ?test .

Tests are related to Specifications via Methods (type-specific):
  Validation:  ?method a bdqffdq:ValidationMethod ;  bdqffdq:forValidation  ?test .
  Issue:       ?method a bdqffdq:IssueMethod ;       bdqffdq:forIssue       ?test .
  Measure:     ?method a bdqffdq:MeasurementMethod ; bdqffdq:forMeasurement ?test .
  Amendment:   ?method a bdqffdq:AmendmentMethod ;   bdqffdq:forAmendment   ?test .

And then:
  ?method bdqffdq:hasSpecification ?spec .
  ?spec rdfs:comment ?specComment .

Exclusion
---------
Exclude Tests that are `MultiRecord` `Measures`, i.e.:
  ?test a bdqffdq:Measure ;
        bdqffdq:hasResourceType bdqffdq:MultiRecord .

Output
------
- Default: TSV to `usecase_tests.tsv`
- Optional: CSV to `usecase_tests.csv`

If --include-spec-comment is set, output columns become:
  useCaseName, testLabel, specComment
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

from rdflib import Graph

PREFIXES = """
PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>

PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdqval:     <https://rs.tdwg.org/bdq/terms/>
"""

# NOTE: useCaseName is BOUND in WHERE so it can be FILTERed reliably.
SPARQL_BASE = (
    PREFIXES
    + """
SELECT DISTINCT ?useCaseName ?testLabel
WHERE {
  ?policy bdqffdq:hasUseCase ?useCase ;
          bdqffdq:includesInPolicy ?test .

  # Compute the display form of the Use Case IRI as a CURIE-like bdqval:... if possible.
  BIND(
    IF(STRSTARTS(STR(?useCase), STR(bdqval:)),
      CONCAT("bdqval:", STRAFTER(STR(?useCase), STR(bdqval:))),
      STR(?useCase)
    )
    AS ?useCaseName
  )

  ?test rdfs:label ?testLabel .

  # Exclude MultiRecord Measures:
  FILTER NOT EXISTS {
    ?test a bdqffdq:Measure ;
          bdqffdq:hasResourceType bdqffdq:MultiRecord .
  }
"""
)

SPARQL_WITH_SPEC_COMMENT = (
    PREFIXES
    + """
SELECT DISTINCT ?useCaseName ?testLabel ?specComment
WHERE {
  ?policy bdqffdq:hasUseCase ?useCase ;
          bdqffdq:includesInPolicy ?test .

  BIND(
    IF(STRSTARTS(STR(?useCase), STR(bdqval:)),
      CONCAT("bdqval:", STRAFTER(STR(?useCase), STR(bdqval:))),
      STR(?useCase)
    )
    AS ?useCaseName
  )

  ?test rdfs:label ?testLabel .

  # Exclude MultiRecord Measures:
  FILTER NOT EXISTS {
    ?test a bdqffdq:Measure ;
          bdqffdq:hasResourceType bdqffdq:MultiRecord .
  }

  # Link Test -> Method -> Specification (explicit enumeration; no ontology inference required)
  OPTIONAL {
    {
      ?test a bdqffdq:Validation .
      ?method a bdqffdq:ValidationMethod ;
              bdqffdq:forValidation ?test .
    }
    UNION
    {
      ?test a bdqffdq:Issue .
      ?method a bdqffdq:IssueMethod ;
              bdqffdq:forIssue ?test .
    }
    UNION
    {
      ?test a bdqffdq:Measure .
      ?method a bdqffdq:MeasurementMethod ;
              bdqffdq:forMeasurement ?test .
    }
    UNION
    {
      ?test a bdqffdq:Amendment .
      ?method a bdqffdq:AmendmentMethod ;
              bdqffdq:forAmendment ?test .
    }

    ?method bdqffdq:hasSpecification ?spec .
    ?spec rdfs:comment ?specComment .
  }
"""
)


def build_sparql(include_spec_comment: bool, use_case_name: str | None) -> str:
    sparql = SPARQL_WITH_SPEC_COMMENT if include_spec_comment else SPARQL_BASE

    if use_case_name:
        # Now this is safe: ?useCaseName is bound in WHERE.
        sparql += f'\n  FILTER( ?useCaseName = "{use_case_name}" )\n'

    sparql += "}\nORDER BY LCASE(STR(?useCaseName)) LCASE(STR(?testLabel))\n"
    return sparql


def run_query(ttl_path: Path, include_spec_comment: bool, use_case_name: str | None) -> List[Tuple[str, ...]]:
    g = Graph()
    g.parse(ttl_path.as_posix(), format="turtle")

    sparql = build_sparql(include_spec_comment=include_spec_comment, use_case_name=use_case_name)

    rows: List[Tuple[str, ...]] = []
    for r in g.query(sparql):
        if include_spec_comment:
            rows.append((str(r.useCaseName), str(r.testLabel), "" if r.specComment is None else str(r.specComment)))
        else:
            rows.append((str(r.useCaseName), str(r.testLabel)))
    return rows


def write_tsv(rows: Iterable[Tuple[str, ...]], headers: Sequence[str], out_path: Path) -> None:
    lines = ["\t".join(headers)]
    for row in rows:
        norm = [c.replace("\t", " ").replace("\r", " ").replace("\n", " ") for c in row]
        lines.append("\t".join(norm))
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(rows: Iterable[Tuple[str, ...]], headers: Sequence[str], out_path: Path) -> None:
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(list(headers))
        for row in rows:
            w.writerow(list(row))


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
    ap.add_argument(
        "--use-case-name",
        dest="use_case_name",
        default=None,
        help='Optional filter to a single Use Case, matching the output column useCaseName (e.g. "bdqval:Taxon-Management").',
    )
    ap.add_argument(
        "--include-spec-comment",
        action="store_true",
        help="Include the rdfs:comment from the Specification related to the Test via its Method.",
    )
    args = ap.parse_args()

    out_path = args.out or default_out_path(args.format)
    headers = ["useCaseName", "testLabel"] + (["specComment"] if args.include_spec_comment else [])

    rows = run_query(
        args.ttl,
        include_spec_comment=args.include_spec_comment,
        use_case_name=args.use_case_name,
    )

    if args.format == "csv":
        write_csv(rows, headers, out_path)
    else:
        write_tsv(rows, headers, out_path)

    extra = ""
    if args.use_case_name:
        extra += f", filtered to useCaseName={args.use_case_name!r}"
    if args.include_spec_comment:
        extra += ", including Specification rdfs:comment"
    print(f"Wrote {len(rows)} rows to {out_path} ({args.format.upper()}){extra}")


if __name__ == "__main__":
    main()
