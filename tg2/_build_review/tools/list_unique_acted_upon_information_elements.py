#!/usr/bin/env python3

import argparse
import csv
from rdflib import Graph

QUERY = """
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>

SELECT DISTINCT ?informationElement
WHERE {
  ?test bdqffdq:hasActedUponInformationElement ?ie .
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

def to_curie(uri: str) -> str:
    for namespace, prefix in PREFIX_MAP.items():
        if uri.startswith(namespace):
            return prefix + uri[len(namespace):]
    return uri

def main():
    parser = argparse.ArgumentParser(
        description="List unique Information Elements that are acted upon in bdqtest.ttl"
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
    args = parser.parse_args()

    g = Graph()
    g.parse(args.bdqtest_ttl, format="turtle")

    results = g.query(QUERY)

    rows = []
    for row in results:
        value = str(row.informationElement)
        if args.curie:
            value = to_curie(value)
        rows.append(value)

    if args.output:
        with open(args.output, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["informationElement"])
            for value in rows:
                writer.writerow([value])
        print(f"Wrote {len(rows)} rows to {args.output}")
    else:
        for value in rows:
            print(value)

if __name__ == "__main__":
    main()