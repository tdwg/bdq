#!/usr/bin/env python3

import argparse
import csv
import re
from pathlib import Path
from rdflib import Graph

#
# This script lists unique Information Elements that are acted upon in bdqtest.ttl.
# If a test list file is provided, it also marks each information element Yes/No depending on whether it is acted upon by at least one of the listed tests.
# The output can be piped to sort, e.g. | sort -k 2,2r -k 1,1 to sort by Yes/No and then alphabetically within each.
# Example usage:
#   python list_unique_acted_upon_information_elements.py path/to/bdqtest.ttl --test-list path/to/test_list.txt --output output.csv --curie
#
# @author: GitHub Copilot with human review and adjustments by Paul J. Morris @chicoreus.
#

QUERY_ALL = """
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>

SELECT DISTINCT ?informationElement
WHERE {
  ?test bdqffdq:hasActedUponInformationElement ?ie .
  ?ie bdqffdq:composedOf ?informationElement .
}
ORDER BY LCASE(STR(?informationElement))
"""

QUERY_BY_TEST_LABEL = """
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?informationElement
WHERE {
  VALUES ?testLabel {
    %s
  }

  ?test rdfs:label ?testLabel ;
        bdqffdq:hasActedUponInformationElement ?ie .
  ?ie bdqffdq:composedOf ?informationElement .
}
ORDER BY LCASE(STR(?informationElement))
"""

PREFIX_MAP = {
    "http://rs.tdwg.org/dwc/terms/": "dwc:",
    "https://rs.tdwg.org/bdqval/terms/": "bdqval:",
    "https://rs.tdwg.org/bdqffdq/terms/": "bdqffdq:",
    "https://rs.tdwg.org/bdqdim/terms/": "bdqdim:",
    "https://rs.tdwg.org/bdqcrit/terms/": "bdqcrit:",
    "https://rs.tdwg.org/bdqenh/terms/": "bdqenh:",
    "https://rs.tdwg.org/bdqtest/terms/": "bdqtest:",
    "http://purl.org/dc/terms/": "dcterms:",
    "http://purl.org/dc/elements/1.1/": "dc:",
}

USE_CASE_RE = re.compile(r"^\s*Use\s+Case\s*:\s*(.+?)\s*$", re.IGNORECASE)
TESTS_RE = re.compile(r"^\s*Tests\s*:\s*$", re.IGNORECASE)


def to_curie(uri: str) -> str:
    for namespace, prefix in PREFIX_MAP.items():
        if uri.startswith(namespace):
            return prefix + uri[len(namespace):]
    return uri


def parse_test_list_file(path: str):
    """
    Parse a file with repeated sections like:

    Use Case: Taxon-Management
    Tests:
    VALIDATION_SCIENTIFICNAME_FOUND
    VALIDATION_SCIENTIFICNAME_NOTEMPTY

    Use Case and Tests blocks may repeat.
    We collect all test labels found.
    """
    tests = []
    current_use_case = None
    in_tests = False

    with open(path, encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()

            if not line:
                continue

            m = USE_CASE_RE.match(line)
            if m:
                current_use_case = m.group(1).strip()
                in_tests = False
                continue

            if TESTS_RE.match(line):
                in_tests = True
                continue

            if in_tests:
                # treat non-empty line as test label
                tests.append(line)

    return sorted(set(tests))


def sparql_escape_string(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    parser = argparse.ArgumentParser(
        description=(
            "List unique Information Elements acted upon in bdqtest.ttl. "
            "Optionally compare against a provided list of test labels and mark each "
            "information element Yes/No depending on whether it is acted upon by one of those tests."
            "output can be piped to sort , e.g. | sort -k 2,2r -k 1,1 to sort by Yes/No and then alphabetically within each. "
        )
    )
    parser.add_argument(
        "bdqtest_ttl",
        help="Path to bdqtest.ttl"
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Optional CSV output file"
    )
    parser.add_argument(
        "--curie",
        action="store_true",
        help="Output values as CURIEs where possible"
    )
    parser.add_argument(
        "--test-list",
        default=None,
        help=(
            "Optional path to a text file containing repeated 'Use Case:' and 'Tests:' sections. "
            "If provided, output includes Yes/No for whether each information element is acted upon "
            "by at least one listed test."
        )
    )
    args = parser.parse_args()

    g = Graph()
    g.parse(args.bdqtest_ttl, format="turtle")

    # Get all unique acted-upon information elements
    all_results = g.query(QUERY_ALL)
    all_elements = [str(row.informationElement) for row in all_results]

    matched_elements = set()
    test_labels = []

    if args.test_list:
        test_labels = parse_test_list_file(args.test_list)
        if test_labels:
            values_clause = " ".join(sparql_escape_string(label) for label in test_labels)
            query = QUERY_BY_TEST_LABEL % values_clause
            subset_results = g.query(query)
            matched_elements = {str(row.informationElement) for row in subset_results}

    output_rows = []
    for value in all_elements:
        display_value = to_curie(value) if args.curie else value
        if args.test_list:
            flag = "Yes" if value in matched_elements else "No"
            output_rows.append((display_value, flag))
        else:
            output_rows.append((display_value,))

    if args.output:
        with open(args.output, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if args.test_list:
                writer.writerow(["informationElement", "actedUponByListedTest"])
            else:
                writer.writerow(["informationElement"])
            writer.writerows(output_rows)
        print(f"Wrote {len(output_rows)} rows to {args.output}")
    else:
        for row in output_rows:
            print(" ".join(row))


if __name__ == "__main__":
    main()
