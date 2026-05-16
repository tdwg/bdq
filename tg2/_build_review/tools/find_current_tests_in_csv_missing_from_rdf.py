#!/usr/bin/env python3

"""
Compare recommended/current tests in bdqtest_term_versions.csv against tests present in bdqtest.ttl.

This script:
- loads bdqtest.ttl with rdflib
- reads bdqtest_term_versions.csv
- extracts labels for rows with status = recommended
- reports labels found in the CSV but missing from the RDF
"""

import argparse
import csv
import sys
from rdflib import Graph

QUERY_RDF_TEST_LABELS = """
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?label
WHERE {
  ?test a ?type ;
        rdfs:label ?label .

  VALUES ?type {
    bdqffdq:Validation
    bdqffdq:Issue
    bdqffdq:Measure
    bdqffdq:Amendment
  }
}
ORDER BY LCASE(STR(?label))
"""


def normalize(value):
    return "" if value is None else str(value).strip()


def load_rdf_test_labels(bdqtest_ttl):
    g = Graph()
    g.parse(bdqtest_ttl, format="turtle")
    results = g.query(QUERY_RDF_TEST_LABELS)
    return {str(row.label).strip() for row in results}


def load_recommended_csv_test_labels(csv_path):
    labels = set()

    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        required_columns = {"Label", "status"}
        missing = required_columns - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV missing required columns: {sorted(missing)}")

        for row in reader:
            label = normalize(row.get("Label"))
            status = normalize(row.get("status")).lower()

            if label and status == "recommended":
                labels.add(label)

    return labels


def main():
    parser = argparse.ArgumentParser(
        description="List recommended tests in bdqtest_term_versions.csv that are missing from bdqtest.ttl"
    )
    parser.add_argument("bdqtest_ttl", help="Path to bdqtest.ttl")
    parser.add_argument("term_versions_csv", help="Path to bdqtest_term_versions.csv")
    args = parser.parse_args()

    rdf_labels = load_rdf_test_labels(args.bdqtest_ttl)
    csv_labels = load_recommended_csv_test_labels(args.term_versions_csv)

    missing = sorted(csv_labels - rdf_labels, key=str.lower)

    if missing:
        print("Recommended tests in bdqtest_term_versions.csv missing from bdqtest.ttl:")
        for label in missing:
            print(label)
        sys.exit(1)
    else:
        print("All recommended tests in bdqtest_term_versions.csv are present in bdqtest.ttl.")
        sys.exit(0)


if __name__ == "__main__":
    main()