#!/usr/bin/env python3
# Script to read repeated Use Case / Tests sections from a text file, query bdqtest.ttl,
# and output the MultiRecord Measure labels whose bdqffdq:aggregatesResponsesFrom links
# correspond to the listed tests for each Use Case.
#
# @author GitHub CoPilot (OpenAI ChatGPT) from prompt by Paul J. Moris @chicoreus
#

import argparse
import re
import sys
from collections import OrderedDict
from rdflib import Graph

USE_CASE_RE = re.compile(r"^\s*Use\s+Case\s*:\s*(.+?)\s*$", re.IGNORECASE)
TESTS_RE = re.compile(r"^\s*Tests\s*:\s*$", re.IGNORECASE)

QUERY_TEMPLATE = """
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT DISTINCT ?measureLabel
WHERE {
  VALUES ?sourceLabel {
    %s
  }

  # Find the versioned source test by label
  ?sourceTestVersion rdfs:label ?sourceLabel ;
                     dcterms:isVersionOf ?sourceTest .

  # Find MultiRecord Measures whose ActedUpon aggregates responses from that unversioned test
  ?measure a bdqffdq:Measure ;
           bdqffdq:hasResourceType bdqffdq:MultiRecord ;
           rdfs:label ?measureLabel ;
           bdqffdq:hasActedUponInformationElement ?actedUpon .

  ?actedUpon bdqffdq:aggregatesResponsesFrom ?sourceTest .
}
ORDER BY LCASE(STR(?measureLabel))
"""

QUERY_EXISTING_TEST_LABELS = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?sourceLabel
WHERE {
  VALUES ?sourceLabel {
    %s
  }
  ?sourceTestVersion rdfs:label ?sourceLabel .
}
ORDER BY LCASE(STR(?sourceLabel))
"""

QUERY_MATCHED_SOURCE_LABELS = """
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT DISTINCT ?sourceLabel
WHERE {
  VALUES ?sourceLabel {
    %s
  }

  ?sourceTestVersion rdfs:label ?sourceLabel ;
                     dcterms:isVersionOf ?sourceTest .

  ?measure a bdqffdq:Measure ;
           bdqffdq:hasResourceType bdqffdq:MultiRecord ;
           bdqffdq:hasActedUponInformationElement ?actedUpon .

  ?actedUpon bdqffdq:aggregatesResponsesFrom ?sourceTest .
}
ORDER BY LCASE(STR(?sourceLabel))
"""


def sparql_escape_string(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_use_case_test_file(path: str):
    """
    Parse a file of the form:

    Use Case: Taxon-Management
    Tests:
    VALIDATION_SCIENTIFICNAME_FOUND
    VALIDATION_SCIENTIFICNAME_NOTEMPTY
    ...

    Repeated sections allowed.

    Returns OrderedDict[str, list[str]]
      {use_case_name: [test_label, ...]}
    preserving first-seen order.
    """
    use_cases = OrderedDict()
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
                if current_use_case not in use_cases:
                    use_cases[current_use_case] = []
                in_tests = False
                continue

            if TESTS_RE.match(line):
                in_tests = True
                continue

            if in_tests and current_use_case is not None:
                use_cases[current_use_case].append(line)

    # deduplicate within each use case, preserving order
    for uc in use_cases:
        seen = set()
        deduped = []
        for t in use_cases[uc]:
            if t not in seen:
                seen.add(t)
                deduped.append(t)
        use_cases[uc] = deduped

    return use_cases


def run_label_query(graph: Graph, query_template: str, test_labels):
    if not test_labels:
        return []

    values_clause = " ".join(sparql_escape_string(label) for label in test_labels)
    query = query_template % values_clause
    results = graph.query(query)
    # each query returns one projected variable
    return [str(row[0]) for row in results]


def find_multirecord_measures(graph: Graph, test_labels):
    """
    Given a list of source test labels, return matching MultiRecord Measure labels.
    """
    return run_label_query(graph, QUERY_TEMPLATE, test_labels)


def find_existing_test_labels(graph: Graph, test_labels):
    """
    Given input test labels, return those labels that match any labeled test in bdqtest.ttl.
    """
    return run_label_query(graph, QUERY_EXISTING_TEST_LABELS, test_labels)


def find_labels_with_matching_multirecord_measures(graph: Graph, test_labels):
    """
    Given input test labels, return those labels that have at least one matching MultiRecord Measure.
    """
    return run_label_query(graph, QUERY_MATCHED_SOURCE_LABELS, test_labels)


def format_output(use_cases_to_measures, include_input_tests=False, use_cases_to_input_tests=None):
    """
    Produce output in the same style as input:

    Use Case: {use case}
    Tests:
    {labels...}
    """
    lines = []

    for use_case, measure_labels in use_cases_to_measures.items():
        lines.append(f"Use Case: {use_case}")
        lines.append("Tests:")

        if include_input_tests and use_cases_to_input_tests is not None:
            for test in use_cases_to_input_tests.get(use_case, []):
                lines.append(test)

        for label in measure_labels:
            lines.append(label)

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def print_diagnostics(use_cases, use_cases_to_measures, use_cases_to_existing, use_cases_to_matched_sources):
    """
    Print diagnostic information to stderr.
    """
    print("Diagnostics:", file=sys.stderr)

    any_problem = False
    for use_case, input_tests in use_cases.items():
        existing = set(use_cases_to_existing.get(use_case, []))
        matched_sources = set(use_cases_to_matched_sources.get(use_case, []))
        measures = use_cases_to_measures.get(use_case, [])

        missing_in_bdqtest = [t for t in input_tests if t not in existing]
        no_matching_measures = [t for t in input_tests if t in existing and t not in matched_sources]

        if missing_in_bdqtest or no_matching_measures:
            any_problem = True
            print(f"\nUse Case: {use_case}", file=sys.stderr)

            if missing_in_bdqtest:
                print("  Input labels not found as tests in bdqtest.ttl:", file=sys.stderr)
                for t in missing_in_bdqtest:
                    print(f"    - {t}", file=sys.stderr)

            if no_matching_measures:
                print("  Input labels found in bdqtest.ttl but with no matching MultiRecord Measure:", file=sys.stderr)
                for t in no_matching_measures:
                    print(f"    - {t}", file=sys.stderr)

            if not measures:
                print("  No MultiRecord Measures matched for this Use Case.", file=sys.stderr)

    if not any_problem:
        print("  All input labels matched tests in bdqtest.ttl and had matching MultiRecord Measures.", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Given a file containing repeated Use Case / Tests sections, query bdqtest.ttl "
            "to find MultiRecord Measure labels whose bdqffdq:aggregatesResponsesFrom "
            "matches the listed tests."
        )
    )
    parser.add_argument(
        "bdqtest_ttl",
        help="Path to bdqtest.ttl"
    )
    parser.add_argument(
        "input_file",
        help="Path to input file containing Use Case / Tests sections"
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Optional output file. Default is to write to console."
    )
    parser.add_argument(
        "--include-input-tests",
        action="store_true",
        help="Also include the original input tests for each use case in the output."
    )
    parser.add_argument(
        "--diagnostic",
        action="store_true",
        help=(
            "Print diagnostics to stderr indicating which input labels were not found as tests "
            "in bdqtest.ttl and which found tests had no matching MultiRecord Measures."
        )
    )
    args = parser.parse_args()

    g = Graph()
    g.parse(args.bdqtest_ttl, format="turtle")

    use_cases = parse_use_case_test_file(args.input_file)

    use_cases_to_measures = OrderedDict()
    use_cases_to_existing = OrderedDict()
    use_cases_to_matched_sources = OrderedDict()

    for use_case, test_labels in use_cases.items():
        measures = find_multirecord_measures(g, test_labels)
        use_cases_to_measures[use_case] = measures

        if args.diagnostic:
            use_cases_to_existing[use_case] = find_existing_test_labels(g, test_labels)
            use_cases_to_matched_sources[use_case] = find_labels_with_matching_multirecord_measures(g, test_labels)

    output_text = format_output(
        use_cases_to_measures,
        include_input_tests=args.include_input_tests,
        use_cases_to_input_tests=use_cases,
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"Wrote output to {args.output}")
    else:
        print(output_text, end="")

    if args.diagnostic:
        print_diagnostics(use_cases, use_cases_to_measures, use_cases_to_existing, use_cases_to_matched_sources)


if __name__ == "__main__":
    main()
