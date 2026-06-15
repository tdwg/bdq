#!/usr/bin/env python3
"""
Extract a single BDQ test subgraph by label and serialize in ordered Turtle,
RDF/XML, or JSON-LD.

HOW THE SUBGRAPH IS OBTAINED (without SPARQL)
=============================================
Rather than running a SPARQL CONSTRUCT query (which proved difficult to
constrain to exactly one test without following links sideways to other tests
via shared Policy nodes), the subgraph is built by direct *imperative
traversal* of the RDF graph using rdflib's Python API:

  1. The single test node is located by matching rdfs:label, giving us its
     subject IRI as a URIRef.

  2. Starting from that node we follow specific *outgoing* predicates using
     rdflib's g.objects(subject, predicate), collecting each object as a new
     subject to include:
       - Information elements:
             hasInformationElement
             hasActedUponInformationElement
             hasConsultedInformationElement
       - Other DataQualityNeed properties:
             hasResourceType, hasDataQualityDimension, hasCriterion,
             hasEnhancement

  3. Method nodes that point *back to* the test are found using rdflib's
     g.subjects(predicate, object) reverse traversal:
       - ValidationMethod  via forValidation
       - IssueMethod       via forIssue
       - MeasurementMethod via forMeasure
       - AmendmentMethod   via forAmendment
     Each Method's rdf:type is verified before it is accepted, so unrelated
     nodes that happen to use the same predicate are excluded.

  4. From each Method we follow hasSpecification forward; from each
     Specification we follow hasArgument; from each Argument we follow
     hasParameter.

  5. Policy nodes (ValidationPolicy, IssuePolicy, MeasurementPolicy,
     AmendmentPolicy) that include *this specific test* are found via reverse
     traversal of bdqffdq:includedInPolicy.  Their UseCases are then found by
     following bdqffdq:hasUseCase forward.

  5b. dcterms:references is followed from every collected subject (primarily
      the test node itself) to include any dcterms:BibliographicResource nodes
      that document the authorities and sources cited by the test.

  6. All collected subjects are placed in a Python set.  A new subgraph is
     built containing every triple from the source graph whose subject is in
     that set.

  7. Finally, bdqffdq:includedInPolicy triples in each Policy node that point
     to *other* tests (not the requested one) are pruned, so the Policy block
     in the output references only the requested test.

This traversal is precise (only the predicate paths that form the test's own
description chain are followed), avoids SPARQL parser quirks, and never walks
sideways to other tests via a shared Policy node.

=============================================================================

The extracted graph is the set of triples that *fully describe one test*:

  - The test instance itself (any subclass of bdqffdq:DataQualityNeed:
    Validation, Issue, Measure, Amendment).
  - Its InformationElements:
        bdqffdq:hasInformationElement
        bdqffdq:hasActedUponInformationElement
        bdqffdq:hasConsultedInformationElement
  - Its bdqffdq:hasResourceType, bdqffdq:hasDataQualityDimension,
    bdqffdq:hasCriterion, bdqffdq:hasEnhancement (for Amendments).
  - Its Method(s):
        bdqffdq:ValidationMethod    via bdqffdq:forValidation
        bdqffdq:IssueMethod         via bdqffdq:forIssue
        bdqffdq:MeasurementMethod   via bdqffdq:forMeasure
        bdqffdq:AmendmentMethod     via bdqffdq:forAmendment
  - Their bdqffdq:Specification(s) via bdqffdq:hasSpecification.
  - Specifications' bdqffdq:Argument(s) via bdqffdq:hasArgument.
  - Arguments' bdqffdq:Parameter(s) via bdqffdq:hasParameter.
  - Policies that include *this test* via bdqffdq:includedInPolicy ?need:
        bdqffdq:ValidationPolicy
        bdqffdq:IssuePolicy
        bdqffdq:MeasurementPolicy
        bdqffdq:AmendmentPolicy
    (but *only* keep includedInPolicy triples whose object is this test).
  - UseCases of those policies via bdqffdq:hasUseCase.
  - dcterms:BibliographicResource nodes linked via dcterms:references from
    any collected subject (primarily the test node itself).

Subject blocks in the output are ordered by rdf:type:

  1. bdqffdq:Validation
  2. bdqffdq:Issue
  3. bdqffdq:Measure
  4. bdqffdq:Amendment
  5. bdqffdq:Criterion
  6. bdqffdq:DataQualityDimension
  7. bdqffdq:ActedUpon
  8. bdqffdq:Consulted
  9. bdqffdq:AbstractInformationElement
 10. bdqffdq:ResourceType
 11. dcterms:BibliographicResource
 12. bdqffdq:ValidationMethod
 13. bdqffdq:IssueMethod
 14. bdqffdq:MeasurementMethod
 15. bdqffdq:AmendmentMethod
 16. bdqffdq:Specification
 17. bdqffdq:Argument
 18. bdqffdq:Parameter
 19. bdqffdq:ValidationPolicy
 20. bdqffdq:IssuePolicy
 21. bdqffdq:MeasurementPolicy
 22. bdqffdq:AmendmentPolicy
 23. bdqffdq:UseCase
 24. Any remaining subjects

CLI:

    -l / --label   (required)  rdfs:label of the test instance
    -i / --input   (default: tg2/_review/dist/bdqtest.ttl)
    -f / --format  (turtle|ttl [default], xml|rdfxml, or jsonld|json-ld)
    -o / --output  (default: stdout)
    -h / --help
"""

import argparse
import json
import re
import sys
from pathlib import Path

from rdflib import Graph, Namespace, RDF, URIRef, RDFS
from rdflib.namespace import NamespaceManager, DCTERMS


# ---------- Locate the test by label ----------

def find_test_iri_by_label(input_path: Path, label: str) -> str:
    g = Graph()
    g.parse(input_path, format="turtle")

    matching_subjects = set(
        s for s in g.subjects(RDFS.label, None)
        if any(str(o) == label for o in g.objects(s, RDFS.label))
    )

    if not matching_subjects:
        sys.stderr.write(f"Error: No resource with rdfs:label '{label}' found in {input_path}.\n")
        sys.exit(1)
    if len(matching_subjects) > 1:
        sys.stderr.write(f"Error: Multiple resources with rdfs:label '{label}' found:\n")
        for s in matching_subjects:
            sys.stderr.write(f"  {s}\n")
        sys.stderr.write("Please use a more specific label or disambiguate.\n")
        sys.exit(1)

    (subject,) = tuple(matching_subjects)
    return str(subject)


# ---------- Build subgraph by imperative traversal ----------

def build_subgraph(input_path: Path, test_iri: str) -> (Graph, Namespace):
    """
    Build and return the subgraph that fully describes the single test
    identified by test_iri.  See module docstring for a full explanation of
    the traversal strategy.
    """
    g = Graph()
    g.parse(input_path, format="turtle")

    # Namespaces
    BDQTEST = Namespace("https://rs.tdwg.org/bdqtest/terms/")
    BDQFFDQ = Namespace("https://rs.tdwg.org/bdqffdq/terms/")
    BDQCRIT = Namespace("https://rs.tdwg.org/bdqcrit/terms/")
    BDQDIM  = Namespace("https://rs.tdwg.org/bdqdim/terms/")
    BDQVAL  = Namespace("https://rs.tdwg.org/bdqval/terms/")
    SKOS    = Namespace("http://www.w3.org/2004/02/skos/core#")
    DWC     = Namespace("http://rs.tdwg.org/dwc/terms/")
    RDFS_NS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    XSD     = Namespace("http://www.w3.org/2001/XMLSchema#")

    g.bind("bdqtest", BDQTEST)
    g.bind("bdqffdq", BDQFFDQ)
    g.bind("bdqcrit", BDQCRIT)
    g.bind("bdqdim",  BDQDIM)
    g.bind("bdqval",  BDQVAL)
    g.bind("dcterms", DCTERMS)
    g.bind("skos",    SKOS)
    g.bind("dwc",     DWC)
    g.bind("rdf",     RDF)
    g.bind("rdfs",    RDFS_NS)
    g.bind("xsd",     XSD)

    need = URIRef(test_iri)
    subjects = set([need])

    # Step 2: follow outgoing predicates from the test node
    info_preds = [
        BDQFFDQ.hasInformationElement,
        BDQFFDQ.hasActedUponInformationElement,
        BDQFFDQ.hasConsultedInformationElement,
    ]
    for p in info_preds:
        for o in g.objects(need, p):
            subjects.add(o)
    for o in g.objects(need, BDQFFDQ.hasResourceType):
        subjects.add(o)
    for o in g.objects(need, BDQFFDQ.hasDataQualityDimension):
        subjects.add(o)
    for o in g.objects(need, BDQFFDQ.hasCriterion):
        subjects.add(o)
    for o in g.objects(need, BDQFFDQ.hasEnhancement):
        subjects.add(o)

    # Steps 3-4: reverse-traverse to Methods, then forward to Specs/Args/Params
    method_type_and_for = [
        (BDQFFDQ.ValidationMethod,   BDQFFDQ.forValidation),
        (BDQFFDQ.IssueMethod,        BDQFFDQ.forIssue),
        (BDQFFDQ.MeasurementMethod,  BDQFFDQ.forMeasure),
        (BDQFFDQ.AmendmentMethod,    BDQFFDQ.forAmendment),
    ]

    for mtype, for_prop in method_type_and_for:
        for m in g.subjects(for_prop, need):
            # Verify the node is actually the expected Method subtype
            if (m, RDF.type, mtype) not in g:
                continue
            subjects.add(m)
            for spec in g.objects(m, BDQFFDQ.hasSpecification):
                subjects.add(spec)
                for arg in g.objects(spec, BDQFFDQ.hasArgument):
                    subjects.add(arg)
                    for param in g.objects(arg, BDQFFDQ.hasParameter):
                        subjects.add(param)

    # Step 5: reverse-traverse to Policies, forward to UseCases
    policy_types = [
        BDQFFDQ.ValidationPolicy,
        BDQFFDQ.IssuePolicy,
        BDQFFDQ.MeasurementPolicy,
        BDQFFDQ.AmendmentPolicy,
    ]
    policies = set()
    for pol in g.subjects(BDQFFDQ.includedInPolicy, need):
        if not any((pol, RDF.type, pt) in g for pt in policy_types):
            continue
        policies.add(pol)
        subjects.add(pol)
        for uc in g.objects(pol, BDQFFDQ.hasUseCase):
            subjects.add(uc)

    # Step 5b: follow dcterms:references from every collected subject to
    # include dcterms:BibliographicResource nodes (sources / authority
    # citations referenced by the test and its related nodes).
    for s in list(subjects):
        for o in g.objects(s, DCTERMS.references):
            if isinstance(o, URIRef):
                subjects.add(o)

    # Step 6: build subgraph from collected subjects
    sub_g = Graph()
    nm = NamespaceManager(sub_g)
    nm.bind("bdqtest", BDQTEST, replace=True)
    nm.bind("bdqffdq", BDQFFDQ, replace=True)
    nm.bind("bdqcrit", BDQCRIT, replace=True)
    nm.bind("bdqdim",  BDQDIM,  replace=True)
    nm.bind("bdqval",  BDQVAL,  replace=True)
    nm.bind("dcterms", DCTERMS, replace=True)
    nm.bind("skos",    SKOS,    replace=True)
    nm.bind("dwc",     DWC,     replace=True)
    nm.bind("rdf",     RDF,     replace=True)
    nm.bind("rdfs",    RDFS_NS, replace=True)
    nm.bind("xsd",     XSD,     replace=True)
    sub_g.namespace_manager = nm

    for s in subjects:
        for _, p, o in g.triples((s, None, None)):
            sub_g.add((s, p, o))

    # Step 7: prune extraneous includedInPolicy triples
    # (keep only the triple pointing to this test)
    for pol in policies:
        for _, p, o in list(sub_g.triples((pol, BDQFFDQ.includedInPolicy, None))):
            if o != need:
                sub_g.remove((pol, p, o))

    return sub_g, BDQFFDQ


# ---------- Priority computation (shared by all serializers) ----------

def compute_subject_priority_and_order(sub_g: Graph, BDQFFDQ: Namespace):
    """
    Return (subj_best_priority dict, TYPE_ORDER list, ordered_subjects list).

    TYPE_ORDER defines the desired output ordering of subject blocks.
    dcterms:BibliographicResource is placed between bdqffdq:ResourceType and
    bdqffdq:ValidationMethod, matching the position these nodes occupy in the
    source bdqtest.ttl file.

    ordered_subjects is a deterministic list of all subjects in sub_g sorted
    first by TYPE_ORDER priority then lexically within each priority group.
    Both Turtle and JSON-LD serializers use this list directly; RDF/XML uses
    the parallel TYPE_ORDER_URIS list in serialize_and_reorder_rdfxml.
    """
    TYPE_ORDER = [
        BDQFFDQ.Validation,
        BDQFFDQ.Issue,
        BDQFFDQ.Measure,
        BDQFFDQ.Amendment,
        BDQFFDQ.Criterion,
        BDQFFDQ.DataQualityDimension,
        BDQFFDQ.ActedUpon,
        BDQFFDQ.Consulted,
        BDQFFDQ.AbstractInformationElement,
        BDQFFDQ.ResourceType,
        DCTERMS.BibliographicResource,   # dcterms:BibliographicResource nodes
        BDQFFDQ.ValidationMethod,
        BDQFFDQ.IssueMethod,
        BDQFFDQ.MeasurementMethod,
        BDQFFDQ.AmendmentMethod,
        BDQFFDQ.Specification,
        BDQFFDQ.Argument,
        BDQFFDQ.Parameter,
        BDQFFDQ.ValidationPolicy,
        BDQFFDQ.IssuePolicy,
        BDQFFDQ.MeasurementPolicy,
        BDQFFDQ.AmendmentPolicy,
        BDQFFDQ.UseCase,
    ]
    type_priority = {t: i for i, t in enumerate(TYPE_ORDER)}

    # Best priority per subject (smallest index of any of its rdf:types)
    subj_best_priority = {}
    for s in set(sub_g.subjects()):
        types = list(sub_g.objects(s, RDF.type))
        prios = [type_priority[t] for t in types if t in type_priority]
        if prios:
            subj_best_priority[s] = min(prios)

    # Build ordered_subjects: group by priority then sort lexically within group
    groups = {}
    max_prio = len(TYPE_ORDER)
    for s in set(sub_g.subjects()):
        prio = subj_best_priority.get(s, max_prio)
        groups.setdefault(prio, []).append(s)

    ordered_subjects = []
    for prio in sorted(groups.keys()):
        ordered_subjects.extend(sorted(groups[prio], key=str))

    return subj_best_priority, TYPE_ORDER, ordered_subjects


# ---------- Turtle serialization and block ordering ----------

def serialize_and_reorder_turtle(sub_g: Graph, BDQFFDQ) -> str:
    """
    Serialize sub_g to Turtle and reorder subject blocks according to the
    type priority defined in compute_subject_priority_and_order.
    BDQFFDQ may be None when called internally; in that case it is
    reconstructed from the well-known namespace IRI.
    """
    if BDQFFDQ is None:
        BDQFFDQ = Namespace("https://rs.tdwg.org/bdqffdq/terms/")

    subj_best_priority, TYPE_ORDER, ordered_subjects = \
        compute_subject_priority_and_order(sub_g, BDQFFDQ)
    nm = sub_g.namespace_manager

    turtle_text = sub_g.serialize(format="turtle")
    if isinstance(turtle_text, bytes):
        turtle_text = turtle_text.decode("utf-8")

    lines = turtle_text.splitlines()

    # Separate @prefix lines and body lines
    prefix_lines = []
    body_lines = []
    in_prefix_section = True
    for line in lines:
        if in_prefix_section and line.startswith("@prefix"):
            prefix_lines.append(line)
        else:
            in_prefix_section = False
            body_lines.append(line)

    # Group body into subject blocks:
    # a block starts on a non-indented line and ends on a line ending with ' .'
    blocks = []
    current_block = []
    for line in body_lines:
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")) and not current_block:
            current_block = [line]
        elif current_block:
            current_block.append(line)
        else:
            continue

        if line.rstrip().endswith(" ."):
            blocks.append(current_block)
            current_block = []
    if current_block:
        blocks.append(current_block)

    def block_key(block):
        first_line = next((ln for ln in block if ln.strip()), "")
        if not first_line:
            return (len(ordered_subjects) + 1, "~")

        subject_token = first_line.split()[0]

        # Find the subject URIRef in the graph whose n3() matches the token
        subj_node = None
        for s in sub_g.subjects():
            if s.n3(nm) == subject_token:
                subj_node = s
                break

        if subj_node is None:
            return (len(ordered_subjects) + 1, subject_token)

        # Use position in ordered_subjects as the primary sort key
        try:
            idx = ordered_subjects.index(subj_node)
        except ValueError:
            idx = len(ordered_subjects)
        return (idx, subject_token)

    blocks_sorted = sorted(blocks, key=block_key)

    output_lines = []
    output_lines.extend(prefix_lines)
    if prefix_lines:
        output_lines.append("")
    for i, block in enumerate(blocks_sorted):
        if i > 0:
            output_lines.append("")
        output_lines.extend(block)

    return "\n".join(output_lines) + "\n"


# ---------- RDF/XML serialization and block ordering ----------

def serialize_and_reorder_rdfxml(sub_g: Graph, BDQFFDQ: Namespace) -> str:
    """
    Serialize sub_g to RDF/XML and reorder rdf:Description blocks by their
    rdf:type, using the same TYPE_ORDER as the Turtle serializer.

    Root cause of previous header-detection failures: rdflib emits the
    <rdf:RDF ...> opening tag across multiple lines with '>' on its own line:

        <rdf:RDF
           xmlns:foo="..."
        >

    The condition  '"<rdf:RDF" in line and ">" in line'  was therefore never
    True, so in_header never became False, ALL lines went into header_lines,
    body_lines stayed empty, no blocks were found, and output was unsorted.

    Fix: end the header at the first line containing '<rdf:Description',
    which is always the start of the first subject block.

    Block identification: '<rdf:Description' opens a block;
    '</rdf:Description>' closes it.  Self-closing property elements such as
    '<rdf:type rdf:resource="..."/>' are safely kept inside the block because
    they do not contain '</rdf:Description>'.

    Block ordering: the rdf:type URI is extracted directly from the XML text
    of each block and mapped to a numeric priority matching TYPE_ORDER.
    dcterms:BibliographicResource is included in TYPE_ORDER_URIS between
    bdqffdq:ResourceType and bdqffdq:ValidationMethod.
    """
    # Full type-URI -> priority map, mirroring TYPE_ORDER in
    # compute_subject_priority_and_order above
    BDQFFDQ_BASE = "https://rs.tdwg.org/bdqffdq/terms/"
    TYPE_ORDER_URIS = [
        BDQFFDQ_BASE + "Validation",
        BDQFFDQ_BASE + "Issue",
        BDQFFDQ_BASE + "Measure",
        BDQFFDQ_BASE + "Amendment",
        BDQFFDQ_BASE + "Criterion",
        BDQFFDQ_BASE + "DataQualityDimension",
        BDQFFDQ_BASE + "ActedUpon",
        BDQFFDQ_BASE + "Consulted",
        BDQFFDQ_BASE + "AbstractInformationElement",
        BDQFFDQ_BASE + "ResourceType",
        "http://purl.org/dc/terms/BibliographicResource",  # dcterms:BibliographicResource
        BDQFFDQ_BASE + "ValidationMethod",
        BDQFFDQ_BASE + "IssueMethod",
        BDQFFDQ_BASE + "MeasurementMethod",
        BDQFFDQ_BASE + "AmendmentMethod",
        BDQFFDQ_BASE + "Specification",
        BDQFFDQ_BASE + "Argument",
        BDQFFDQ_BASE + "Parameter",
        BDQFFDQ_BASE + "ValidationPolicy",
        BDQFFDQ_BASE + "IssuePolicy",
        BDQFFDQ_BASE + "MeasurementPolicy",
        BDQFFDQ_BASE + "AmendmentPolicy",
        BDQFFDQ_BASE + "UseCase",
    ]
    type_priority = {uri: i for i, uri in enumerate(TYPE_ORDER_URIS)}
    fallback_priority = len(TYPE_ORDER_URIS)

    rdfxml = sub_g.serialize(format="xml")
    if isinstance(rdfxml, bytes):
        rdfxml = rdfxml.decode("utf-8")

    lines = rdfxml.splitlines()

    # Split into header and body.
    # Header = everything before the first <rdf:Description line.
    # We do NOT use '<rdf:RDF' + '>' because rdflib puts them on separate lines.
    header_lines = []
    body_lines = []
    in_header = True
    for line in lines:
        if in_header:
            if "<rdf:Description" in line:
                in_header = False
                body_lines.append(line)
            else:
                header_lines.append(line)
        else:
            body_lines.append(line)

    # Parse body into individual rdf:Description blocks and the closing tag.
    blocks = []
    current_block = []
    inside_block = False
    closing_lines = []

    for line in body_lines:
        if "</rdf:RDF" in line:
            if current_block:
                blocks.append(current_block)
                current_block = []
                inside_block = False
            closing_lines.append(line)
            break

        if "<rdf:Description" in line:
            # Start of a new subject block (guard: close any orphan block)
            if inside_block and current_block:
                blocks.append(current_block)
            current_block = [line]
            inside_block = True

        elif inside_block:
            current_block.append(line)
            if "</rdf:Description>" in line:
                blocks.append(current_block)
                current_block = []
                inside_block = False
    else:
        if current_block:
            blocks.append(current_block)

    # Regexes to extract type URI and subject IRI from block text
    type_re  = re.compile(r'<rdf:type\s+rdf:resource="([^"]+)"')
    about_re = re.compile(r'rdf:about="([^"]+)"')

    def get_type_priority(block):
        """Return the lowest priority index for any rdf:type found in block."""
        best = fallback_priority
        for l in block:
            m = type_re.search(l)
            if m:
                prio = type_priority.get(m.group(1), fallback_priority)
                if prio < best:
                    best = prio
        return best

    def get_subject_iri(block):
        """Return the rdf:about IRI from the block's opening line."""
        for l in block:
            m = about_re.search(l)
            if m:
                return m.group(1)
        return "~"

    def block_key(block):
        # Primary key: type priority; secondary: subject IRI for stable sort
        return (get_type_priority(block), get_subject_iri(block))

    blocks_sorted = sorted(blocks, key=block_key)

    output_lines = []
    output_lines.extend(header_lines)
    for block in blocks_sorted:
        output_lines.extend(block)
    output_lines.extend(closing_lines)

    return "\n".join(output_lines) + "\n"


# ---------- JSON-LD serialization and node ordering ----------

def serialize_and_reorder_jsonld(sub_g: Graph, BDQFFDQ: Namespace) -> str:
    """
    Serialize sub_g to JSON-LD and reorder the @graph nodes by rdf:type,
    using the same TYPE_ORDER as the Turtle and RDF/XML serializers.

    Node ordering strategy:
      The ordered_subjects list produced by compute_subject_priority_and_order
      (a list of URIRef objects already in the correct sequence) is used as
      the canonical order.  Each JSON-LD node's '@id' is resolved to a full
      URI (expanding any compact IRI using the '@context' prefix map if
      present) and its position in ordered_subjects determines its sort rank.
      This avoids any dependency on how rdflib chooses to format the JSON-LD
      '@type' values (full URI vs compact IRI).

    rdflib may emit JSON-LD as either:
      a) a bare list of nodes (expanded form, no @context), or
      b) a dict with '@context' and '@graph' (compacted form).
    Both cases are handled.
    """
    # Get the canonical subject order from the RDF graph
    _, _, ordered_subjects = compute_subject_priority_and_order(sub_g, BDQFFDQ)
    # Map full URI string -> position index for O(1) lookup
    subj_order = {str(s): i for i, s in enumerate(ordered_subjects)}
    fallback = len(ordered_subjects)

    jsonld_text = sub_g.serialize(format="json-ld", indent=2)
    if isinstance(jsonld_text, bytes):
        jsonld_text = jsonld_text.decode("utf-8")

    data = json.loads(jsonld_text)

    # Identify graph nodes and whether we have a wrapper dict with @context
    if isinstance(data, list):
        # Expanded JSON-LD: top-level list of nodes, full URIs everywhere
        graph_nodes = data
        wrapper = None
    elif isinstance(data, dict) and "@graph" in data:
        # Compacted JSON-LD: dict with @context and @graph
        graph_nodes = data["@graph"]
        wrapper = data
    else:
        # Single node or unexpected structure; return unchanged
        return jsonld_text

    # Build a prefix -> base-URI map from @context (if present) so we can
    # expand compact IRIs like "bdqtest:uuid-..." to their full form.
    prefix_map = {}
    if wrapper and "@context" in wrapper:
        ctx = wrapper["@context"]
        if isinstance(ctx, dict):
            for k, v in ctx.items():
                if not k.startswith("@") and isinstance(v, str):
                    prefix_map[k] = v

    def expand_id(node_id):
        """Expand a possibly-compact IRI to its full URI."""
        if not node_id:
            return ""
        # Already a full URI or URN
        if node_id.startswith("http") or node_id.startswith("urn"):
            return node_id
        # Compact IRI of the form "prefix:local"
        if ":" in node_id:
            prefix, local = node_id.split(":", 1)
            if prefix in prefix_map:
                return prefix_map[prefix] + local
        return node_id

    def node_sort_key(node):
        full_id = expand_id(node.get("@id", ""))
        idx = subj_order.get(full_id, fallback)
        return (idx, full_id)

    graph_nodes_sorted = sorted(graph_nodes, key=node_sort_key)

    if wrapper is None:
        return json.dumps(graph_nodes_sorted, indent=2, ensure_ascii=False) + "\n"
    else:
        wrapper["@graph"] = graph_nodes_sorted
        return json.dumps(wrapper, indent=2, ensure_ascii=False) + "\n"


# ---------- CLI ----------

def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Extract a single BDQ test subgraph by label and serialize it in "
            "ordered Turtle, RDF/XML, or JSON-LD.  See module docstring for a "
            "full explanation of how the subgraph is obtained."
        )
    )
    parser.add_argument(
        "-l", "--label",
        required=True,
        help="rdfs:label of the test instance to extract (e.g. VALIDATION_COUNTRYCODE_STANDARD)."
    )
    parser.add_argument(
        "-i", "--input",
        default="tg2/_review/dist/bdqtest.ttl",
        help="Input Turtle file (default: tg2/_review/dist/bdqtest.ttl)."
    )
    parser.add_argument(
        "-f", "--format",
        default="turtle",
        choices=["turtle", "ttl", "xml", "rdfxml", "jsonld", "json-ld"],
        help="Output format: turtle|ttl, xml|rdfxml, or jsonld|json-ld (default: turtle)."
    )
    parser.add_argument(
        "-o", "--output",
        default="-",
        help="Output file (default: stdout)."
    )
    return parser.parse_args()


def main():
    args = parse_args()

    input_path = Path(args.input)
    out_fmt = args.format.lower()
    label = args.label

    test_iri = find_test_iri_by_label(input_path, label)
    sub_g, BDQFFDQ = build_subgraph(input_path, test_iri)

    if out_fmt in ("turtle", "ttl"):
        out_text = serialize_and_reorder_turtle(sub_g, BDQFFDQ)
    elif out_fmt in ("xml", "rdfxml"):
        out_text = serialize_and_reorder_rdfxml(sub_g, BDQFFDQ)
    else:  # jsonld / json-ld
        out_text = serialize_and_reorder_jsonld(sub_g, BDQFFDQ)

    if args.output == "-" or not args.output:
        sys.stdout.write(out_text)
    else:
        Path(args.output).write_text(out_text, encoding="utf-8")


if __name__ == "__main__":
    main()
