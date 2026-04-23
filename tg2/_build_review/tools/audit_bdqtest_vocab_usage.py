#!/usr/bin/env python3
"""
Audit bdqtest.ttl usage of BDQ vocabularies beyond bdqffdq.

Checks that any term used in bdqtest.ttl from these namespaces is declared in the corresponding
distributed vocabulary file:

- bdqval:  https://rs.tdwg.org/bdqval/terms/    (RDF/XML in tg2/_review/dist/bdqval.xml)
- bdqcrit: https://rs.tdwg.org/bdqcrit/terms/  (RDF/XML in tg2/_review/dist/bdqcrit.xml)
- bdqdim:  https://rs.tdwg.org/bdqdim/terms/   (RDF/XML in tg2/_review/dist/bdqdim.xml)
- bdqenh:  https://rs.tdwg.org/bdqenh/terms/   (RDF/XML in tg2/_review/dist/bdqenh.xml)

This script is intentionally simple and practical:
- It extracts all URIRefs used anywhere in bdqtest.ttl (subject/predicate/object).
- It filters them by namespace.
- It verifies that each URIRef exists as a subject in the corresponding vocabulary graph
  (or as an object of dcterms:isVersionOf, if you only have versioned subjects in the dist).

Usage (from tg2/_build_review):
  python3 tools/audit_bdqtest_vocab_usage.py \
    --bdqtest ../_review/dist/bdqtest.ttl \
    --bdqval  ../_review/dist/bdqval.xml \
    --bdqcrit ../_review/dist/bdqcrit.xml \
    --bdqdim  ../_review/dist/bdqdim.xml \
    --bdqenh  ../_review/dist/bdqenh.xml

Exit code:
  0 if OK (warnings may still be printed)
  1 if errors found
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS


NS = {
    "bdqval": "https://rs.tdwg.org/bdqval/terms/",
    "bdqcrit": "https://rs.tdwg.org/bdqcrit/terms/",
    "bdqdim": "https://rs.tdwg.org/bdqdim/terms/",
    "bdqenh": "https://rs.tdwg.org/bdqenh/terms/",
    # (bdqtest is the data file being checked, so we don't validate bdqtest terms here)
}


@dataclass(frozen=True)
class Finding:
    severity: str  # "ERROR" or "WARN"
    message: str


def load_graph(path: Path, fmt: str) -> Graph:
    g = Graph()
    g.parse(str(path), format=fmt)
    return g


def all_urirefs(g: Graph) -> Set[str]:
    used: Set[str] = set()
    for s, p, o in g:
        for t in (s, p, o):
            if isinstance(t, URIRef):
                used.add(str(t))
    return used


def build_vocab_index(vocab_g: Graph) -> Tuple[Set[str], Set[str]]:
    """
    Returns:
      - subjects: all subject IRIs present in the vocab graph
      - is_version_of_objects: all objects of dcterms:isVersionOf (typically the 'unversioned' term IRIs)
    """
    subjects = {str(s) for s in vocab_g.subjects()}
    is_version_of_objects = {str(o) for o in vocab_g.objects(None, DCTERMS.isVersionOf)}
    return subjects, is_version_of_objects


def run_audit(
    bdqtest_ttl: Path,
    vocab_files: Dict[str, Path],
) -> Tuple[List[Finding], List[Finding]]:
    errors: List[Finding] = []
    warns: List[Finding] = []

    bdqtest_g = load_graph(bdqtest_ttl, fmt="turtle")
    used = all_urirefs(bdqtest_g)

    # Load vocab graphs and build indices
    vocab_index: Dict[str, Tuple[Set[str], Set[str]]] = {}
    for prefix, path in vocab_files.items():
        vg = load_graph(path, fmt="xml")  # dist/*.xml are RDF/XML
        vocab_index[prefix] = build_vocab_index(vg)

    # For each vocab namespace, verify terms used in bdqtest.ttl exist in that vocab distribution
    for prefix, base in NS.items():
        subjects, is_version_of_objects = vocab_index[prefix]
        used_terms = sorted([u for u in used if u.startswith(base)], key=str.lower)

        missing: List[str] = []
        for term in used_terms:
            # Accept if:
            # - term appears as a subject in the distribution (some files include unversioned subjects), OR
            # - term appears as an object of dcterms:isVersionOf (common when distribution subjects are versioned)
            if term not in subjects and term not in is_version_of_objects:
                missing.append(term)

        if missing:
            errors.append(Finding(
                "ERROR",
                f"bdqtest.ttl uses {len(missing)} term(s) in {prefix}: that are not found in {vocab_files[prefix]}.\n"
                + "\n".join(f"  - {m}" for m in missing[:200])
                + ("" if len(missing) <= 200 else f"\n  ... ({len(missing)-200} more)")
            ))

        # Optional helpful warning: namespaces used but empty vocab? (unlikely, but aids debugging)
        if used_terms and len(subjects) == 0:
            warns.append(Finding(
                "WARN",
                f"Vocabulary file {vocab_files[prefix]} for {prefix}: parsed with 0 subjects; "
                "is it the expected RDF/XML distribution?"
            ))

    return errors, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bdqtest", required=True, help="Path to bdqtest.ttl (Turtle)")

    ap.add_argument("--bdqval", required=True, help="Path to bdqval.xml (RDF/XML)")
    ap.add_argument("--bdqcrit", required=True, help="Path to bdqcrit.xml (RDF/XML)")
    ap.add_argument("--bdqdim", required=True, help="Path to bdqdim.xml (RDF/XML)")
    ap.add_argument("--bdqenh", required=True, help="Path to bdqenh.xml (RDF/XML)")

    args = ap.parse_args()

    vocab_files = {
        "bdqval": Path(args.bdqval),
        "bdqcrit": Path(args.bdqcrit),
        "bdqdim": Path(args.bdqdim),
        "bdqenh": Path(args.bdqenh),
    }

    errors, warns = run_audit(Path(args.bdqtest), vocab_files)

    if warns:
        print("WARNINGS:")
        for w in warns:
            print(f"- {w.message}")
        print()

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"- {e.message}")
        return 1

    print("OK: bdqtest.ttl vocabulary references (bdqval/bdqcrit/bdqdim/bdqenh) are consistent with dist files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())