#!/usr/bin/env python3

"""
Query bdqtest.ttl and determine, for each Use Case, which acted-upon Information Elements
occur in Validation Tests, how many Tests in that Use Case involve each Information Element,
and whether those Information Elements require a value.

Classification
--------------
For each Use Case / Information Element, classify as one of:

(a) sole must have value
    - acted upon by at least one Validation as the sole acted-upon Information Element
    - has a Validation testing emptiness
    - has a corresponding MULTIRECORD_MEASURE_QA test

(b) sole must have value
    - tested singly in a Validation for something other than emptiness
    - has a corresponding MULTIRECORD_MEASURE_QA lacking the clause
      "or Response.status=INTERNAL_PREREQUISITES_NOT_MET"

(c) sole may be empty
    - only tested singly by Validations
    - all corresponding MULTIRECORD_MEASURE_QA tests include the clause
      "or Response.status=INTERNAL_PREREQUISITES_NOT_MET"

(d) multiple may be empty / multiple must have value
    - Information Element appears in one or more Validation Tests composed with other
      acted-upon Information Elements
    - default to "multiple may be empty"
    - only classify as "multiple must have value" if there is explicit conjunctive wording
      indicating that all acted-upon terms are required

Counts
------
For each Use Case / Information Element, report the number of distinct Validation Tests
in that Use Case that involve the Information Element.
"""

import argparse
import re
from collections import defaultdict, OrderedDict
from rdflib import Graph

QUERY = """
PREFIX rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:     <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dcterms:  <http://purl.org/dc/terms/>
PREFIX bdqffdq:  <https://rs.tdwg.org/bdqffdq/terms/>

SELECT DISTINCT
  ?useCase
  ?useCaseLabel
  ?validation
  ?validationLabel
  ?validationDescription
  ?validationComment
  ?infoElement
  ?qaMeasureLabel
  ?qaExpectedResponse
WHERE {
  ?useCase rdf:type bdqffdq:UseCase .
  OPTIONAL { ?useCase rdfs:label ?useCaseLabel . }

  ?policy bdqffdq:hasUseCase ?useCase ;
          bdqffdq:includedInPolicy ?validation .

  ?validation rdf:type bdqffdq:Validation ;
              rdfs:label ?validationLabel ;
              dcterms:isVersionOf ?validationUnversioned ;
              bdqffdq:hasActedUponInformationElement ?validationIE .

  OPTIONAL { ?validation dcterms:description ?validationDescription . }
  OPTIONAL { ?validation rdfs:comment ?validationComment . }

  ?validationIE bdqffdq:composedOf ?infoElement .

  OPTIONAL {
    ?qaMeasure rdf:type bdqffdq:Measure ;
               rdfs:label ?qaMeasureLabel ;
               bdqffdq:hasResourceType bdqffdq:MultiRecord ;
               bdqffdq:hasActedUponInformationElement ?qaActedUpon .

    FILTER(STRSTARTS(STR(?qaMeasureLabel), "MULTIRECORD_MEASURE_QA_"))

    ?qaActedUpon bdqffdq:aggregatesResponsesFrom ?validationUnversioned .

    ?qaMethod bdqffdq:forMeasure ?qaMeasure ;
              bdqffdq:hasSpecification ?qaSpec .

    OPTIONAL { ?qaSpec bdqffdq:hasExpectedResponse ?qaExpectedResponse . }
  }
}
ORDER BY
  LCASE(STR(COALESCE(?useCaseLabel, ?useCase)))
  LCASE(STR(?validationLabel))
  LCASE(STR(?infoElement))
  LCASE(STR(?qaMeasureLabel))
"""


def to_curie(uri: str) -> str:
    prefix_map = OrderedDict([
        ("http://rs.tdwg.org/dwc/terms/", "dwc:"),
        ("https://rs.tdwg.org/bdqval/terms/", "bdqval:"),
        ("https://rs.tdwg.org/bdqffdq/terms/", "bdqffdq:"),
        ("https://rs.tdwg.org/bdquc/terms/", "bdquc:"),
        ("https://rs.tdwg.org/bdqtest/terms/", "bdqtest:"),
        ("https://rs.tdwg.org/bdqdim/terms/", "bdqdim:"),
        ("https://rs.tdwg.org/bdqcrit/terms/", "bdqcrit:"),
        ("https://rs.tdwg.org/bdqenh/terms/", "bdqenh:"),
        ("http://purl.org/dc/terms/", "dcterms:"),
        ("http://purl.org/dc/elements/1.1/", "dc:"),
        ("http://www.w3.org/2000/01/rdf-schema#", "rdfs:"),
    ])
    for namespace, prefix in prefix_map.items():
        if uri.startswith(namespace):
            return prefix + uri[len(namespace):]
    return uri


def qa_clause_allows_empty(text: str) -> bool:
    if not text:
        return False
    return "or Response.status=INTERNAL_PREREQUISITES_NOT_MET" in text


def looks_like_emptiness_test(label: str, description: str, comment: str) -> bool:
    text = " ".join(x for x in [label, description, comment] if x).lower()
    return (
        "notempty" in text
        or "not empty" in text
        or re.search(r"\bempty\b", text) is not None
    )


def multiple_validation_requires_all_terms(label: str, description: str, comment: str) -> bool:
    """
    Strong heuristic for multi-element validations that truly require all acted-upon
    Information Elements to have values.

    We intentionally keep this conservative:
    default multi-element case is "may be empty" unless there is explicit conjunctive wording.
    """
    text = " ".join(x for x in [label, description, comment] if x).lower()

    conjunctive_patterns = [
        r"\ball of\b.*\bmust\b",
        r"\beach of\b.*\bmust\b",
        r"\ball fields\b.*\bmust\b",
        r"\ball terms\b.*\bmust\b",
        r"\ball .* are required\b",
        r"\beach .* is required\b",
        r"\bmust all be\b",
        r"\ball .* not empty\b",
        r"\beach .* not empty\b",
        r"\ball acted[- ]upon .* not empty\b",
    ]

    disjunctive_or_consistency_patterns = [
        r"\bat least one\b",
        r"\bone or more\b",
        r"\bany one\b",
        r"\bif all .* are empty\b",
        r"\bif all .* empty\b",
        r"\bconsistent\b",
        r"\bcombination of values\b",
        r"\blowest ranking matched element\b",
        r"\bdetermine the taxon\b",
        r"\bexists and is\b",
    ]

    if any(re.search(p, text) for p in disjunctive_or_consistency_patterns):
        return False

    return any(re.search(p, text) for p in conjunctive_patterns)


def build_matrix(graph: Graph):
    results = graph.query(QUERY)

    use_case_display = OrderedDict()

    validations = defaultdict(lambda: defaultdict(lambda: {
        "label": "",
        "description": "",
        "comment": "",
        "info_elements": set(),
        "qa_expected_responses": [],
        "qa_measure_labels": set(),
    }))

    for row in results:
        use_case = str(row.useCase)
        use_case_label = str(row.useCaseLabel) if row.useCaseLabel else ""
        use_case_name = use_case_label if use_case_label else use_case
        use_case_display[use_case] = use_case_name

        validation = str(row.validation)
        validation_label = str(row.validationLabel) if row.validationLabel else ""
        validation_description = str(row.validationDescription) if row.validationDescription else ""
        validation_comment = str(row.validationComment) if row.validationComment else ""
        info_element = to_curie(str(row.infoElement))

        qa_measure_label = str(row.qaMeasureLabel) if row.qaMeasureLabel else ""
        qa_expected_response = str(row.qaExpectedResponse) if row.qaExpectedResponse else ""

        v = validations[use_case_name][validation]
        v["label"] = validation_label
        v["description"] = validation_description
        v["comment"] = validation_comment
        v["info_elements"].add(info_element)

        if qa_measure_label:
            v["qa_measure_labels"].add(qa_measure_label)
            v["qa_expected_responses"].append(qa_expected_response)

    matrix = defaultdict(dict)
    all_info_elements = set()

    per_usecase_info_data = defaultdict(lambda: defaultdict(lambda: {
        "classes": [],
        "validation_labels": set(),
        "multiple_must_labels": set(),
    }))

    for use_case_name, validation_map in validations.items():
        for validation_iri, v in validation_map.items():
            info_elements = sorted(v["info_elements"])
            all_info_elements.update(info_elements)

            is_single = len(info_elements) == 1
            is_multiple = len(info_elements) > 1
            is_emptiness = looks_like_emptiness_test(v["label"], v["description"], v["comment"])
            has_qa = len(v["qa_measure_labels"]) > 0
            all_qa_allow_empty = (
                has_qa and
                all(qa_clause_allows_empty(text) for text in v["qa_expected_responses"])
            )
            any_strict_qa = (
                has_qa and
                any(not qa_clause_allows_empty(text) for text in v["qa_expected_responses"])
            )

            for info_element in info_elements:
                info_data = per_usecase_info_data[use_case_name][info_element]
                info_data["validation_labels"].add(v["label"])

                if is_single and is_emptiness and has_qa:
                    info_data["classes"].append("sole must have value")
                elif is_single and (not is_emptiness) and any_strict_qa:
                    info_data["classes"].append("sole must have value")
                elif is_single and all_qa_allow_empty:
                    info_data["classes"].append("sole may be empty")
                elif is_multiple:
                    # Revised heuristic: default multi-element validations to may be empty.
                    if multiple_validation_requires_all_terms(
                        v["label"], v["description"], v["comment"]
                    ):
                        info_data["classes"].append("multiple must have value")
                        info_data["multiple_must_labels"].add(v["label"])
                    else:
                        info_data["classes"].append("multiple may be empty")

    precedence = [
        "sole must have value",
        "sole may be empty",
        "multiple must have value",
        "multiple may be empty",
    ]

    diagnostics = defaultdict(dict)

    for use_case_name, info_map in per_usecase_info_data.items():
        for info_element, info_data in info_map.items():
            chosen = ""
            for p in precedence:
                if p in info_data["classes"]:
                    chosen = p
                    break

            matrix[info_element][use_case_name] = {
                "classification": chosen,
                "count": len(info_data["validation_labels"]),
                "multiple_must_labels": sorted(info_data["multiple_must_labels"], key=str.lower),
            }

            diagnostics[info_element][use_case_name] = matrix[info_element][use_case_name]

    use_case_order = list(use_case_display.values())
    info_element_order = sorted(all_info_elements, key=str.lower)

    return use_case_order, info_element_order, matrix, diagnostics


def print_per_use_case(use_case_order, info_element_order, matrix, report_multiple_must_tests=False):
    for use_case in use_case_order:
        print(f"Use Case: {use_case}")
        print("Information Elements:")
        found_any = False
        for info_element in info_element_order:
            if use_case in matrix[info_element]:
                cell = matrix[info_element][use_case]
                print(f"{info_element}\t{cell['count']}\t{cell['classification']}")
                found_any = True

                if report_multiple_must_tests and cell["classification"] == "multiple must have value":
                    if cell["multiple_must_labels"]:
                        print("\tCaused by Tests:")
                        for label in cell["multiple_must_labels"]:
                            print(f"\t- {label}")
        if not found_any:
            print("(none)")
        print()


def print_markdown_table(use_case_order, info_element_order, matrix):
    headers = ["Information Element"] + use_case_order
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["---"] * len(headers)) + " |")

    for info_element in info_element_order:
        row = [info_element]
        for use_case in use_case_order:
            if use_case in matrix[info_element]:
                cell = matrix[info_element][use_case]
                row.append(f"{cell['count']}: {cell['classification']}")
            else:
                row.append("")
        print("| " + " | ".join(row) + " |")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "For each Use Case in bdqtest.ttl, list acted-upon Information Elements in Validation Tests, "
            "report the number of Tests involving each Information Element, and classify whether it must have a value."
        )
    )
    parser.add_argument(
        "bdqtest_ttl",
        help="Path to bdqtest.ttl"
    )
    parser.add_argument(
        "--markdown-table",
        action="store_true",
        help="Output results as a markdown table with rows as Information Elements and columns as Use Cases."
    )
    parser.add_argument(
        "--report-multiple-must-tests",
        action="store_true",
        help="For 'multiple must have value' cases, also report the labels of the Tests causing that classification."
    )
    args = parser.parse_args()

    g = Graph()
    g.parse(args.bdqtest_ttl, format="turtle")

    use_case_order, info_element_order, matrix, diagnostics = build_matrix(g)

    if args.markdown_table:
        print_markdown_table(use_case_order, info_element_order, matrix)
    else:
        print_per_use_case(
            use_case_order,
            info_element_order,
            matrix,
            report_multiple_must_tests=args.report_multiple_must_tests
        )


if __name__ == "__main__":
    main()