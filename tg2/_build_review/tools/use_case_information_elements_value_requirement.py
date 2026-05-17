#!/usr/bin/env python3

"""
Query bdqtest.ttl and determine, for each Use Case, which acted-upon Information Elements
occur in Validation Tests, and whether those Information Elements "require a value" based on
related MultiRecord QA Measures.

Improved rule
-------------
For a given Use Case and acted-upon Information Element in a Validation:

1. Find Validation Tests in that Use Case acting upon that Information Element.
2. Find related MultiRecord QA Measures by following:
      MultiRecord Measure
        -> hasActedUponInformationElement
        -> aggregatesResponsesFrom
        -> unversioned Validation test
   where the Measure label starts with "MULTIRECORD_MEASURE_QA_".
3. Examine the expected response text for the related QA Measure specification.

Default classification:
- If ANY related MULTIRECORD_MEASURE_QA measure lacks the clause
    "or Response.status=INTERNAL_PREREQUISITES_NOT_MET"
  then mark the Information Element as "must have value".
- Otherwise mark it as "may be empty".

Override for grouped non-empty Validations:
- If the source Validation has multiple acted-upon Information Elements AND appears to be
  a NOTEMPTY-style Validation, then no individual acted-upon Information Element is inferred
  to be individually required; classify those acted-upon Information Elements as "may be empty".
"""

import argparse
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


def looks_like_notempty_validation(label: str, description: str, comment: str) -> bool:
    text = " ".join(x for x in [label, description, comment] if x).lower()
    return (
        "notempty" in text
        or "not empty" in text
        or "empty" in text
    )


def build_matrix(graph: Graph):
    """
    Returns:
      use_case_order: list[str]
      info_element_order: list[str]
      matrix: dict[info_element][use_case] = classification
    """
    results = graph.query(QUERY)

    use_case_display = OrderedDict()

    # Group by use case and validation first so we can count how many acted-upon info elements
    # are in each validation.
    validations = defaultdict(lambda: defaultdict(lambda: {
        "label": "",
        "description": "",
        "comment": "",
        "info_elements": set(),
        "qa_expected_responses": [],
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
        qa_expected_response = str(row.qaExpectedResponse) if row.qaExpectedResponse else ""

        v = validations[use_case_name][validation]
        v["label"] = validation_label
        v["description"] = validation_description
        v["comment"] = validation_comment
        v["info_elements"].add(info_element)
        v["qa_expected_responses"].append(qa_expected_response)

    # Compute per use case / info element classification
    matrix = defaultdict(dict)
    all_info_elements = set()

    per_usecase_info_status = defaultdict(lambda: defaultdict(list))

    for use_case_name, validation_map in validations.items():
        for validation_iri, v in validation_map.items():
            info_elements = sorted(v["info_elements"])
            all_info_elements.update(info_elements)

            grouped_notempty = (
                len(info_elements) > 1 and
                looks_like_notempty_validation(v["label"], v["description"], v["comment"])
            )

            any_strict_qa = any(
                not qa_clause_allows_empty(text)
                for text in v["qa_expected_responses"]
            )

            for info_element in info_elements:
                if grouped_notempty:
                    per_usecase_info_status[use_case_name][info_element].append("may be empty")
                elif any_strict_qa:
                    per_usecase_info_status[use_case_name][info_element].append("must have value")
                else:
                    per_usecase_info_status[use_case_name][info_element].append("may be empty")

    # Consolidate across validations in same use case / information element
    # If any contributing validation requires value, keep "must have value",
    # unless all statuses are "may be empty".
    for use_case_name, info_map in per_usecase_info_status.items():
        for info_element, statuses in info_map.items():
            if "must have value" in statuses:
                matrix[info_element][use_case_name] = "must have value"
            else:
                matrix[info_element][use_case_name] = "may be empty"

    use_case_order = list(use_case_display.values())
    info_element_order = sorted(all_info_elements, key=str.lower)

    return use_case_order, info_element_order, matrix


def print_per_use_case(use_case_order, info_element_order, matrix):
    for use_case in use_case_order:
        print(f"Use Case: {use_case}")
        print("Information Elements:")
        found_any = False
        for info_element in info_element_order:
            if use_case in matrix[info_element]:
                print(f"{info_element}\t{matrix[info_element][use_case]}")
                found_any = True
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
            row.append(matrix[info_element].get(use_case, ""))
        print("| " + " | ".join(row) + " |")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "For each Use Case in bdqtest.ttl, list acted-upon Information Elements in Validation Tests "
            "and determine whether related MultiRecord QA Measures imply the Information Element must have a value."
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
    args = parser.parse_args()

    g = Graph()
    g.parse(args.bdqtest_ttl, format="turtle")

    use_case_order, info_element_order, matrix = build_matrix(g)

    if args.markdown_table:
        print_markdown_table(use_case_order, info_element_order, matrix)
    else:
        print_per_use_case(use_case_order, info_element_order, matrix)


if __name__ == "__main__":
    main()