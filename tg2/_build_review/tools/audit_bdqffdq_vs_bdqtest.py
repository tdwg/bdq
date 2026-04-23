#!/usr/bin/env python3
"""
Audit for ontology/data inconsistencies between bdqffdq.owl (ontology) and bdqtest.ttl (test data).

Enhancement (requested):
- Validate that all bdqffdq: terms used anywhere in bdqtest.ttl exist in the ontology as either
  an owl:Class, a property (owl:ObjectProperty/owl:DatatypeProperty/owl:AnnotationProperty), or
  an owl:NamedIndividual. Missing terms are reported as ERROR.

Usage (from tg2/_build_review):
  python3 tools/audit_bdqffdq_vs_bdqtest.py \
    --owl ../_review/vocabulary/bdqffdq.owl \
    --ttl ../_review/dist/bdqtest.ttl

@author GitHub CoPilot with human review by Paul Morris
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Set, Tuple

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL

BDQFFDQ_TERMS = "https://rs.tdwg.org/bdqffdq/terms/"
BDQFFDQ_HASH = "https://rs.tdwg.org/bdqffdq/terms#"

# Known "wrong" or legacy-ish names we've seen creep in from other sources/tooling.
KNOWN_BAD_BDQFFDQ_TERMS = [
    BDQFFDQ_TERMS + "includesInPolicy",   # correct is includedInPolicy
    BDQFFDQ_TERMS + "producesAssertion",  # framework uses producesResponse
    BDQFFDQ_TERMS + "Assertion",          # if used as a class/term in data
]

# "Suspicious but not automatically wrong" tokens -> WARN
SUSPICIOUS_LOCALNAME_SUBSTRINGS = [
    "assert",       # Assertion/Asssertion typos, assertion vs Response drift
    "MeasureResponse",
    "MeasureMethod",
]


@dataclass(frozen=True)
class Finding:
    severity: str  # "ERROR" or "WARN"
    message: str


def load_graph(path: Path, fmt: str) -> Graph:
    g = Graph()
    g.parse(str(path), format=fmt)
    return g


def local_name(uri: str) -> str:
    if uri.startswith(BDQFFDQ_TERMS):
        return uri[len(BDQFFDQ_TERMS):]
    if uri.startswith(BDQFFDQ_HASH):
        return uri[len(BDQFFDQ_HASH):]
    return uri.rsplit("/", 1)[-1].rsplit("#", 1)[-1]


def collect_declared_properties(owl_g: Graph) -> Set[str]:
    declared: Set[str] = set()
    for p in (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty):
        for s in owl_g.subjects(RDF.type, p):
            declared.add(str(s))
    return declared


def collect_declared_classes(owl_g: Graph) -> Set[str]:
    return {str(s) for s in owl_g.subjects(RDF.type, OWL.Class)}


def collect_named_individuals(owl_g: Graph) -> Set[str]:
    return {str(s) for s in owl_g.subjects(RDF.type, OWL.NamedIndividual)}


def collect_bdqffdq_terms_used_any_position(ttl_g: Graph) -> Set[str]:
    used: Set[str] = set()
    for s, p, o in ttl_g:
        for term in (s, p, o):
            if isinstance(term, URIRef):
                ts = str(term)
                if ts.startswith(BDQFFDQ_TERMS) or ts.startswith(BDQFFDQ_HASH):
                    used.add(ts)
    return used


def collect_bdqffdq_predicates_used(ttl_g: Graph) -> Set[str]:
    preds: Set[str] = set()
    for _, p, _ in ttl_g:
        if isinstance(p, URIRef):
            ps = str(p)
            if ps.startswith(BDQFFDQ_TERMS) or ps.startswith(BDQFFDQ_HASH):
                preds.add(ps)
    return preds


def run_audit(owl_path: Path, ttl_path: Path) -> Tuple[List[Finding], List[Finding]]:
    errors: List[Finding] = []
    warns: List[Finding] = []

    owl_g = load_graph(owl_path, fmt="ttl")
    ttl_g = load_graph(ttl_path, fmt="turtle")

    declared_props = collect_declared_properties(owl_g)
    declared_classes = collect_declared_classes(owl_g)
    declared_inds = collect_named_individuals(owl_g)

    declared_any = declared_props | declared_classes | declared_inds

    used_terms = collect_bdqffdq_terms_used_any_position(ttl_g)
    used_preds = collect_bdqffdq_predicates_used(ttl_g)

    # 0) Disallow bdqffdq terms# usage in bdqtest.ttl
    hash_terms = sorted([t for t in used_terms if t.startswith(BDQFFDQ_HASH)], key=str.lower)
    if hash_terms:
        errors.append(Finding(
            "ERROR",
            f"bdqtest.ttl uses bdqffdq terms in the 'terms#' namespace ({BDQFFDQ_HASH}). "
            f"Found {len(hash_terms)} term(s), e.g. {hash_terms[0]}"
        ))

    # 1) Known-bad/legacy terms
    for bad in KNOWN_BAD_BDQFFDQ_TERMS:
        if bad in used_terms:
            errors.append(Finding(
                "ERROR",
                f"Found known-bad/legacy bdqffdq term in bdqtest.ttl: {bad} (localName='{local_name(bad)}')."
            ))

    # 2) All bdqffdq predicates used should be declared as properties in the OWL
    undeclared_preds = sorted(
        [p for p in used_preds if p.startswith(BDQFFDQ_TERMS) and p not in declared_props],
        key=str.lower,
    )
    if undeclared_preds:
        errors.append(Finding(
            "ERROR",
            "bdqtest.ttl uses bdqffdq predicate(s) not declared as properties in bdqffdq.owl:\n"
            + "\n".join(f"  - {p}" for p in undeclared_preds[:200])
            + ("" if len(undeclared_preds) <= 200 else f"\n  ... ({len(undeclared_preds)-200} more)")
        ))

    # 3) NEW (requested): every bdqffdq term used anywhere in bdqtest.ttl must exist as Class OR Property OR NamedIndividual
    # Note: We only enforce this for /terms/ namespace, not for terms# (already handled as error above).
    missing_terms = sorted(
        [t for t in used_terms if t.startswith(BDQFFDQ_TERMS) and t not in declared_any],
        key=str.lower,
    )
    if missing_terms:
        errors.append(Finding(
            "ERROR",
            "bdqtest.ttl uses bdqffdq term(s) that are not declared in bdqffdq.owl as a Class, Property, or NamedIndividual:\n"
            + "\n".join(f"  - {t} (localName='{local_name(t)}')" for t in missing_terms[:200])
            + ("" if len(missing_terms) <= 200 else f"\n  ... ({len(missing_terms)-200} more)")
        ))

    # 4) Suspicious token scan (WARN)
    for term in sorted([t for t in used_terms if t.startswith(BDQFFDQ_TERMS)], key=str.lower):
        ln = local_name(term)
        for token in SUSPICIOUS_LOCALNAME_SUBSTRINGS:
            if token.lower() in ln.lower():
                warns.append(Finding(
                    "WARN",
                    f"Suspicious bdqffdq term usage in bdqtest.ttl (possible terminology drift): "
                    f"{term} (localName='{ln}') matched token '{token}'."
                ))
                break

    # 5) Helpful specific check for includedInPolicy vs includesInPolicy
    if (BDQFFDQ_TERMS + "includesInPolicy") in used_terms:
        errors.append(Finding(
            "ERROR",
            "bdqtest.ttl uses bdqffdq:includesInPolicy, but bdqffdq.owl declares bdqffdq:includedInPolicy (no 's')."
        ))

    return errors, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--owl", required=True, help="Path to bdqffdq.owl (Turtle)")
    ap.add_argument("--ttl", required=True, help="Path to bdqtest.ttl (Turtle)")
    args = ap.parse_args()

    owl_path = Path(args.owl)
    ttl_path = Path(args.ttl)

    errors, warns = run_audit(owl_path, ttl_path)

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

    print("OK: no blocking inconsistencies found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
