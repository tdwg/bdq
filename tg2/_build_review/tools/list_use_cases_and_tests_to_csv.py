#!/usr/bin/env python3

import argparse
import csv
from rdflib import Graph

QUERY = """
PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>

SELECT DISTINCT
  (REPLACE(STR(?useCase), "^.*/", "") AS ?useCaseLocalName)
  (STR(?testLabel) AS ?testLabelStr)
  ?testType
  ?resourceType
WHERE {
  ?useCase rdf:type bdqffdq:UseCase .
  OPTIONAL { ?useCase rdfs:label ?useCaseLabel . }

  ?policy bdqffdq:hasUseCase ?useCase ;
          bdqffdq:includedInPolicy ?test .

  ?test rdf:type ?testType ;
        rdfs:label ?testLabel ;
        bdqffdq:hasResourceType ?resourceType .

  FILTER(?testType IN (
    bdqffdq:Validation,
    bdqffdq:Issue,
    bdqffdq:Measure,
    bdqffdq:Amendment
  ))
}
ORDER BY
  LCASE(STR(COALESCE(?useCaseLabel, ?useCase)))
  ?testType
  ?resourceType
  LCASE(STR(?testLabel))
"""

def shorten_bdqffdq(iri: str) -> str:
    return iri.replace("https://rs.tdwg.org/bdqffdq/terms/", "bdqffdq:")

def simplify_resource_type(iri: str) -> str:
    if iri == "https://rs.tdwg.org/bdqffdq/terms/SingleRecord":
        return "SingleRecord"
    if iri == "https://rs.tdwg.org/bdqffdq/terms/MultiRecord":
        return "MultiRecord"
    return iri

def main():
    parser = argparse.ArgumentParser(
        description="Extract use case local names and associated test labels/types/resource types from bdqtest.ttl"
    )
    parser.add_argument(
        "bdqtest_ttl",
        help="Path to bdqtest.ttl"
    )
    parser.add_argument(
        "-o", "--output",
        default="use_cases_and_tests.csv",
        help="Output CSV file path (default: use_cases_and_tests.csv)"
    )
    args = parser.parse_args()

    g = Graph()
    g.parse(args.bdqtest_ttl, format="turtle")

    results = g.query(QUERY)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["useCaseLocalName", "testLabel", "testType", "resourceType"])

        for row in results:
            use_case_local_name = str(row.useCaseLocalName)
            test_label = str(row.testLabelStr)
            test_type = shorten_bdqffdq(str(row.testType))
            resource_type = simplify_resource_type(str(row.resourceType))
            writer.writerow([use_case_local_name, test_label, test_type, resource_type])

    print(f"Wrote {args.output}")

if __name__ == "__main__":
    main()