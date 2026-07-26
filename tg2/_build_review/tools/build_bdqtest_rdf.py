#!/usr/bin/env python3
"""
build_bdqtest_rdf.py — Python replacement for kurator-ffdq RDF generation of
bdqtest artifacts.

Generates Turtle, RDF/XML, and JSON-LD serializations of bdqtest from the
canonical bdqtest_term_versions.csv term-version file, mirroring the semantics
of the Java test-util.sh / kurator-ffdq workflow.

Usage (from repo root):
  python3 tg2/_build_review/tools/build_bdqtest_rdf.py \\
      --in-term-versions  tg2/_review/vocabulary/bdqtest_term_versions.csv \\
      --guid-file          tg2/core/TG2_tests_additional_guids.csv \\
      --ie-guid-file       tg2/core/information_element_guids.csv \\
      --policy-guid-file   tg2/core/TG2_policy_guids.csv \\
      --citation-guid-file tg2/core/TG2_citation_guids.csv \\
      --out-ttl    tg2/_review/dist/bdqtest.ttl \\
      --out-rdfxml tg2/_review/dist/bdqtest.xml \\
      --out-jsonld tg2/_review/dist/bdqtest.json

The --argument-guid-file argument (TG2_tests_argument_guids.csv) is accepted
for CLI compatibility with kurator-ffdq but is not used; argument details are
derived directly from the Parameters and AuthoritiesDefaults columns in
bdqtest_term_versions.csv.

Key behavioural invariants that mirror the Java implementation:
  - Only rows with status=="recommended" are emitted.
  - Any row whose CSV text contains "AllAmendmentTestsRunOnSingleRecord" or
    "AllDarwin" (in any column) is excluded.
  - Method/Specification GUIDs are taken from TG2_tests_additional_guids.csv
    (keyed by term_localName), which takes precedence over the SpecificationGuid
    and MethodGuid columns of the term-versions file.
  - InformationElement GUIDs are looked up from information_element_guids.csv
    by label; when the file has duplicate labels the FIRST occurrence wins.
  - Citation GUIDs are looked up from TG2_citation_guids.csv; duplicate URLs
    also use the FIRST occurrence. Only URLs present in the citation file are
    emitted as dcterms:references / dcterms:BibliographicResource nodes.
  - ValidationMethod labels use "with Specification for:" (no redundant word).
    All other method types use "with Specification Specification for:".
"""

import argparse
import csv
import re
import sys

try:
    from rdflib import Graph, Namespace, URIRef, Literal
    from rdflib.namespace import RDF, RDFS, XSD, SKOS, DCTERMS
except ImportError:
    print("ERROR: rdflib is required. Install with: pip install rdflib",
          file=sys.stderr)
    sys.exit(1)

# ── Namespace declarations ──────────────────────────────────────────────────

BDQTEST = Namespace("https://rs.tdwg.org/bdqtest/terms/")
BDQFFDQ = Namespace("https://rs.tdwg.org/bdqffdq/terms/")
BDQCRIT  = Namespace("https://rs.tdwg.org/bdqcrit/terms/")
BDQDIM   = Namespace("https://rs.tdwg.org/bdqdim/terms/")
BDQENH   = Namespace("https://rs.tdwg.org/bdqenh/terms/")
BDQVAL   = Namespace("https://rs.tdwg.org/bdqval/terms/")
BDQUC    = Namespace("https://rs.tdwg.org/bdquc/terms/")
DWC      = Namespace("http://rs.tdwg.org/dwc/terms/")
DWCIRI   = Namespace("http://rs.tdwg.org/dwc/iri/")
DC       = Namespace("http://purl.org/dc/elements/1.1/")
OA       = Namespace("http://www.w3.org/ns/oa#")

# Prefix list matching the kurator-ffdq / rdf4j prefix ordering.
# Semantic equivalence is required; ordering is desirable but not required.
_PREFIXES = [
    ("rdfbeans", "http://viceversatech.com/rdfbeans/2.0/"),
    ("bdqenh",   "https://rs.tdwg.org/bdqenh/terms/"),
    ("bdqval",   "https://rs.tdwg.org/bdqval/terms/"),
    ("bdqcrit",  "https://rs.tdwg.org/bdqcrit/terms/"),
    ("dwcloud",  "http://datakurator.org/none/"),
    ("bdquc",    "https://rs.tdwg.org/bdquc/terms/"),
    ("bdqdim",   "https://rs.tdwg.org/bdqdim/terms/"),
    ("skos",     "http://www.w3.org/2004/02/skos/core#"),
    ("dwciri",   "http://rs.tdwg.org/dwc/iri/"),
    ("dwc",      "http://rs.tdwg.org/dwc/terms/"),
    ("oa",       "http://www.w3.org/ns/oa#"),
    ("bdqffdq",  "https://rs.tdwg.org/bdqffdq/terms/"),
    ("bdqtest",  "https://rs.tdwg.org/bdqtest/terms/"),
    ("dcterms",  "http://purl.org/dc/terms/"),
    ("dc",       "http://purl.org/dc/elements/1.1/"),
    ("rdf",      "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
    ("rdfs",     "http://www.w3.org/2000/01/rdf-schema#"),
    ("rdf4j",    "http://rdf4j.org/schema/rdf4j#"),
    ("sesame",   "http://www.openrdf.org/schema/sesame#"),
    ("owl",      "http://www.w3.org/2002/07/owl#"),
    ("xsd",      "http://www.w3.org/2001/XMLSchema#"),
    ("fn",       "http://www.w3.org/2005/xpath-functions#"),
]

# Map well-known prefixes used in CSV columns to full IRIs.
_PREFIX_MAP = {
    "dwc":     "http://rs.tdwg.org/dwc/terms/",
    "dwciri":  "http://rs.tdwg.org/dwc/iri/",
    "dc":      "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    # Java/kurator-ffdq resolves "oa:" to http://www.w3.org/ns/ (not oa#),
    # replicating this so that oa:hasTarget → http://www.w3.org/ns/hasTarget.
    "oa":      "http://www.w3.org/ns/",
    "bdqval":  "https://rs.tdwg.org/bdqval/terms/",
    "bdquc":   "https://rs.tdwg.org/bdquc/terms/",
    "bdqffdq": "https://rs.tdwg.org/bdqffdq/terms/",
    "bdqtest": "https://rs.tdwg.org/bdqtest/terms/",
    "skos":    "http://www.w3.org/2004/02/skos/core#",
    "rdfs":    "http://www.w3.org/2000/01/rdf-schema#",
    "rdf":     "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "xsd":     "http://www.w3.org/2001/XMLSchema#",
}


# ── CURIE resolution ────────────────────────────────────────────────────────

def resolve_curie(curie: str) -> URIRef:
    """Resolve a CURIE like 'dwc:scientificName' to a URIRef."""
    curie = curie.strip()
    if curie.startswith("http://") or curie.startswith("https://"):
        return URIRef(curie)
    if curie.startswith("urn:"):
        return URIRef(curie)
    if ":" in curie:
        prefix, local = curie.split(":", 1)
        if prefix in _PREFIX_MAP:
            return URIRef(_PREFIX_MAP[prefix] + local)
    raise ValueError(f"Cannot resolve CURIE: {curie!r}")


# ── URL extraction from HTML references ─────────────────────────────────────

_URL_RE = re.compile(r'https?://[^\s<>"\],]+')


def extract_reference_urls(html: str) -> list:
    """
    Extract ordered, deduplicated URLs from a References field.

    The field may be an HTML ``<ul><li>…</li></ul>`` block, a plain-text
    paragraph, or a mix.

    When the text contains proper ``<li>…</li>`` items, only those items are
    processed (malformed items ending with ``</i>`` instead of ``</li>`` are
    intentionally skipped, mirroring Java/kurator-ffdq behaviour).

    When a list item contains multiple comma-separated URLs (e.g.
    ``https://a.example/,https://b.example/``), each URL is extracted
    individually.

    If the text has no ``<li>`` items (plain text), all URLs in the raw text
    are extracted.
    """
    urls = []
    seen = set()
    li_items = re.findall(r'<li>(.*?)</li>', html, flags=re.IGNORECASE | re.DOTALL)
    if li_items:
        for item in li_items:
            text = re.sub(r'<[^>]+>', '', item).strip()
            if not text:
                continue
            for url in _URL_RE.findall(text):
                url = url.rstrip('.,;)')
                if url not in seen:
                    seen.add(url)
                    urls.append(url)
    else:
        # Plain-text references (common for MultiRecord rows)
        text = re.sub(r'<[^>]+>', '', html).strip()
        for url in _URL_RE.findall(text):
            url = url.rstrip('.,;)')
            if url not in seen:
                seen.add(url)
                urls.append(url)
    return urls


# ── Examples parsing ─────────────────────────────────────────────────────────

def parse_examples(raw: str) -> list:
    """
    Parse the Examples CSV column into a list of example strings.

    Format: [example1],[example2],…

    Java/kurator-ffdq behaviour:
      - If there is only ONE example (no '],['  separator), the raw string is
        returned as-is, including any outer brackets.
      - If there are MULTIPLE examples, split on '],[', strip the leading '['
        from the first part and the trailing ']' from the last part.
    Returns [''] for an empty / missing field (Java emits skos:example "").
    """
    raw = raw.strip()
    if not raw:
        return ['']
    if '],[' in raw:
        parts = raw.split('],[')
        parts[0] = parts[0].lstrip('[')
        parts[-1] = parts[-1].rstrip(']')
        return parts if parts else ['']
    # Single example: return the full string, brackets and all
    return [raw]


# ── Argument default-value extraction ────────────────────────────────────────

def extract_default_value(authorities_defaults: str, param: str) -> str:
    """
    Extract the default value for `param` from an AuthoritiesDefaults string.

    Format (loosely):
      {param} default[ ]=[" ]{value}"[ {extra}][, {param2} default = "{value2}" …]

    Returns the value without enclosing quotes, or '' if not found.
    """
    param_esc = re.escape(param.strip())
    m = re.search(param_esc + r'\s+default\s*=\s*"([^"]*)"', authorities_defaults)
    if m:
        return m.group(1)
    return ''


# ── CSV loaders ──────────────────────────────────────────────────────────────

def load_additional_guids(path: str) -> dict:
    """
    Load TG2_tests_additional_guids.csv.

    Returns {term_localName (GUID): {'method': method_iri, 'spec': spec_iri}}.
    This file is the authoritative source for Method and Specification GUIDs.
    """
    result = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            guid   = row['GUID'].strip()
            method = row['Method'].strip()
            spec   = row['Specification'].strip()
            if guid and (method or spec):
                result[guid] = {'method': method, 'spec': spec}
    return result


def load_ie_guids(path: str) -> dict:
    """
    Load information_element_guids.csv → {label: guid_iri}.

    When the file contains duplicate labels the FIRST occurrence is kept
    (matching the Java behaviour).
    """
    result = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            label = row['label'].strip()
            guid  = row['guid'].strip()
            if label and guid and label not in result:
                result[label] = guid
    return result


def load_policy_guids(path: str) -> dict:
    """Load TG2_policy_guids.csv → {(usecase, policytype): guid_iri}."""
    result = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            uc  = row['UseCase'].strip()
            pt  = row['PolicyType'].strip()
            gid = row['PolicyGuid'].strip()
            if uc and pt and gid:
                result[(uc, pt)] = gid
    return result


def load_citation_guids(path: str) -> tuple:
    """
    Load TG2_citation_guids.csv.

    Returns a (guid_map, url_to_guid) pair:
      - guid_map: {guid_iri → bibliographic_citation}
        The guid_iri is the IRI used for the dcterms:BibliographicResource node.
        It may be an HTTP/HTTPS URL or a urn:uuid: URI.
      - url_to_guid: {url → guid_iri}
        Reverse index for entries where the guid is a urn:uuid: — the URL is
        extracted from the citation text and maps back to the urn:uuid key.

    In both maps the FIRST occurrence of each key wins (no overwriting of
    earlier entries), matching the Java behaviour.
    """
    guid_map: dict  = {}
    url_to_guid: dict = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            guid = row['guid'].strip()
            cite = row['citation'].strip()
            if not guid or not cite:
                continue
            if guid not in guid_map:
                guid_map[guid] = cite
            # For urn:uuid-keyed entries build a URL→guid reverse index.
            if guid.startswith('urn:uuid:'):
                for url in re.findall(r'https?://[^\s,]+', cite):
                    url = url.rstrip('.,;)')
                    if url not in url_to_guid and url not in guid_map:
                        url_to_guid[url] = guid
    return guid_map, url_to_guid


def load_test_rows(path: str) -> list:
    """
    Load bdqtest_term_versions.csv and return only the rows that should be
    included in the RDF output.

    Inclusion criteria (mirroring copy_files.sh):
      - status == "recommended"
      - The entire row text does NOT contain "AllAmendmentTestsRunOnSingleRecord"
      - The entire row text does NOT contain "AllDarwin"
    """
    rows = []
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row.get('status', '').strip() != 'recommended':
                continue
            row_text = ','.join(row.values())
            if 'AllAmendmentTestsRunOnSingleRecord' in row_text:
                continue
            if 'AllDarwin' in row_text:
                continue
            rows.append(row)
    return rows


# ── RDF ontology-support helpers ─────────────────────────────────────────────

def _bind_namespaces(g: Graph) -> None:
    for prefix, uri in _PREFIXES:
        g.bind(prefix, Namespace(uri), override=True)


def _test_class(test_type: str) -> URIRef:
    return {
        'Validation': BDQFFDQ.Validation,
        'Issue':      BDQFFDQ.Issue,
        'Measure':    BDQFFDQ.Measure,
        'Amendment':  BDQFFDQ.Amendment,
    }[test_type]


def _method_class_name(test_type: str) -> str:
    return {
        'Validation': 'ValidationMethod',
        'Issue':      'IssueMethod',
        'Measure':    'MeasurementMethod',
        'Amendment':  'AmendmentMethod',
    }[test_type]


def _method_class(test_type: str) -> URIRef:
    return BDQFFDQ[_method_class_name(test_type)]


def _for_predicate(test_type: str) -> URIRef:
    return {
        'Validation': BDQFFDQ.forValidation,
        'Issue':      BDQFFDQ.forIssue,
        'Measure':    BDQFFDQ.forMeasure,
        'Amendment':  BDQFFDQ.forAmendment,
    }[test_type]


def _policy_class(policy_type: str) -> URIRef:
    return {
        'ValidationPolicy':  BDQFFDQ.ValidationPolicy,
        'IssuePolicy':       BDQFFDQ.IssuePolicy,
        'MeasurementPolicy': BDQFFDQ.MeasurementPolicy,
        'AmendmentPolicy':   BDQFFDQ.AmendmentPolicy,
    }[policy_type]


def _policy_noun(policy_type: str) -> str:
    return {
        'ValidationPolicy':  'validations',
        'IssuePolicy':       'issues',
        'MeasurementPolicy': 'measures',
        'AmendmentPolicy':   'amendments',
    }[policy_type]


def _test_type_to_policy_type(test_type: str) -> str:
    return {
        'Validation': 'ValidationPolicy',
        'Issue':      'IssuePolicy',
        'Measure':    'MeasurementPolicy',
        'Amendment':  'AmendmentPolicy',
    }[test_type]


def _ensure_once(g: Graph, subject: URIRef, predicate: URIRef,
                 obj, seen: set, key: object) -> None:
    """Add a triple exactly once, identified by `key` in the `seen` set."""
    if key not in seen:
        seen.add(key)
        g.add((subject, predicate, obj))


def _ensure_resource_type(g: Graph, rt: str, seen: set) -> URIRef:
    node = BDQFFDQ[rt]
    key  = ('rt', rt)
    if key not in seen:
        seen.add(key)
        g.add((node, RDF.type, BDQFFDQ.ResourceType))
        g.add((node, RDFS.label, Literal(rt)))
    return node


def _ensure_dimension(g: Graph, dim: str, seen: set) -> URIRef:
    node = BDQDIM[dim]
    key  = ('dim', dim)
    if key not in seen:
        seen.add(key)
        g.add((node, RDF.type, BDQFFDQ.DataQualityDimension))
        g.add((node, RDFS.label, Literal(dim)))
    return node


def _ensure_criterion(g: Graph, crit: str, seen: set) -> URIRef:
    node = BDQCRIT[crit]
    key  = ('crit', crit)
    if key not in seen:
        seen.add(key)
        g.add((node, RDF.type, BDQFFDQ.Criterion))
        g.add((node, RDFS.label, Literal(crit)))
    return node


def _ensure_enhancement(g: Graph, enh: str, seen: set) -> URIRef:
    node = BDQENH[enh]
    key  = ('enh', enh)
    if key not in seen:
        seen.add(key)
        g.add((node, RDF.type, BDQFFDQ.Enhancement))
        g.add((node, RDFS.label, Literal(enh)))
    return node


def _ensure_test_subclass(g: Graph, test_type: str, seen: set) -> None:
    key = ('subclass', test_type)
    if key not in seen:
        seen.add(key)
        g.add((_test_class(test_type), RDFS.subClassOf, BDQFFDQ.DataQualityNeed))


def _ensure_method_subclass(g: Graph, test_type: str, seen: set) -> None:
    key = ('msubclass', test_type)
    if key not in seen:
        seen.add(key)
        g.add((_method_class(test_type), RDFS.subClassOf, BDQFFDQ.DataQualityMethod))


def _ensure_ie_subclass(g: Graph, ie_type: str, seen: set) -> None:
    key = ('iesubclass', ie_type)
    if key not in seen:
        seen.add(key)
        g.add((BDQFFDQ[ie_type], RDFS.subClassOf, BDQFFDQ.InformationElement))


# ── Information-Element helpers ───────────────────────────────────────────────

def _ie_label(ie_type: str, terms_csv: str) -> str:
    """Construct the canonical label used for ie_guids lookup."""
    terms = [t.strip() for t in terms_csv.split(',') if t.strip()]
    return f"Information Element {ie_type} {', '.join(terms)}"


def _resolve_ie_terms(terms_csv: str) -> list:
    """Parse 'dwc:foo,dwc:bar' etc. into a list of URIRefs."""
    result = []
    for t in terms_csv.split(','):
        t = t.strip()
        if t:
            try:
                result.append(resolve_curie(t))
            except ValueError:
                pass
    return result


def _add_standard_ie_node(g: Graph, ie_type: str, ie_guid_iri: str,
                           terms_csv: str, seen_ies: dict,
                           seen_ontology: set) -> URIRef:
    """
    Add a standard (non-MultiRecord) ActedUpon or Consulted IE node.
    Deduped by ie_guid_iri.  Returns the URIRef.
    """
    node = URIRef(ie_guid_iri)
    if ie_guid_iri not in seen_ies:
        seen_ies[ie_guid_iri] = node
        g.add((node, RDF.type, BDQFFDQ[ie_type]))
        _ensure_ie_subclass(g, ie_type, seen_ontology)
        for term_uri in _resolve_ie_terms(terms_csv):
            g.add((node, BDQFFDQ.composedOf, term_uri))
        label = _ie_label(ie_type, terms_csv)
        g.add((node, RDFS.label, Literal(label)))
        g.add((node, SKOS.prefLabel, Literal(label)))
    return node


def _add_multirecord_ie_node(g: Graph, row: dict, term_iri_to_label: dict,
                              ie_guids: dict, seen_ies: dict,
                              seen_ontology: set):
    """
    Add the ActedUpon IE node for a MultiRecord measure that aggregates
    responses from a single-record test.

    Returns the URIRef or None if data is missing.
    """
    agg_iri = row.get('aggregatesResponsesFrom', '').strip()
    if not agg_iri:
        return None

    ref_guid  = agg_iri.split('/')[-1]
    ref_label = term_iri_to_label.get(agg_iri, ref_guid)

    ie_label = (f"Information Element ActedUpon bdqval:AggregatedTestResponseOutcomes"
                f" for bdqtest:{ref_label}.Response")
    ie_guid_iri = ie_guids.get(ie_label)
    if not ie_guid_iri:
        return None

    node = URIRef(ie_guid_iri)
    if ie_guid_iri not in seen_ies:
        seen_ies[ie_guid_iri] = node
        g.add((node, RDF.type, BDQFFDQ.ActedUpon))
        _ensure_ie_subclass(g, 'ActedUpon', seen_ontology)
        g.add((node, SKOS.note,
               Literal(f"Aggregated Response outcomes produced by {ref_label}"
                       f" across a MultiRecord.")))
        g.add((node, BDQFFDQ.aggregatesResponsesFrom, BDQTEST[ref_guid]))
        g.add((node, BDQFFDQ.composedOf, BDQVAL.AggregatedTestResponseOutcomes))
        g.add((node, RDFS.label, Literal(ie_label)))
        g.add((node, SKOS.prefLabel, Literal(ie_label)))
    return node


# ── BibliographicResource helper ─────────────────────────────────────────────

def _add_bib_resource(g: Graph, url: str, guid_map: dict,
                      url_to_guid: dict, seen_refs: set):
    """
    Add a dcterms:BibliographicResource node for `url` if, and only if, the
    URL is resolvable via the citation lookup (matching Java behaviour).

    Resolution order:
      1. `url` is a direct key in guid_map  →  node IRI = url.
      2. `url` appears in the citation text of a urn:uuid entry (via
         url_to_guid reverse index)  →  node IRI = urn:uuid:…

    Returns the URIRef of the emitted BibliographicResource, or None if the
    URL has no known citation entry.
    """
    if url in guid_map:
        node_uri  = URIRef(url)
        citation  = guid_map[url]
    elif url in url_to_guid:
        guid      = url_to_guid[url]
        node_uri  = URIRef(guid)
        citation  = guid_map[guid]
    else:
        return None

    key = str(node_uri)
    if key not in seen_refs:
        seen_refs.add(key)
        g.add((node_uri, RDF.type, DCTERMS.BibliographicResource))
        g.add((node_uri, DCTERMS.bibliographicCitation, Literal(citation)))
    return node_uri


# ── Argument-node helper ──────────────────────────────────────────────────────

def _add_argument_nodes(g: Graph, row: dict, spec_uri: URIRef,
                        seen_params: set) -> None:
    """
    Build bdqffdq:Argument nodes attached to the Specification.

    GUIDs come from the ArgumentGuids column; labels and values are derived
    from the Parameters and AuthoritiesDefaults columns.
    """
    arg_guids_raw = row.get('ArgumentGuids', '').strip()
    params_raw    = row.get('Parameters', '').strip()
    auth_defaults = row.get('AuthoritiesDefaults', '').strip()

    if not arg_guids_raw or not params_raw:
        return

    arg_guids = [a.strip() for a in arg_guids_raw.split(',') if a.strip()]
    params    = [p.strip() for p in params_raw.split(',') if p.strip()]

    if len(arg_guids) != len(params):
        return  # data mismatch — skip silently

    for guid, param in zip(arg_guids, params):
        arg_uri = URIRef('urn:uuid:' + guid)
        value   = extract_default_value(auth_defaults, param)
        label   = f'Default value for {param}:"{value}"'

        g.add((spec_uri, BDQFFDQ.hasArgument, arg_uri))
        g.add((arg_uri, RDF.type, BDQFFDQ.Argument))
        g.add((arg_uri, BDQFFDQ.hasArgumentValue, Literal(value)))
        g.add((arg_uri, RDFS.label, Literal(label)))

        try:
            param_uri = resolve_curie(param)
            g.add((arg_uri, BDQFFDQ.hasParameter, param_uri))
            if param not in seen_params:
                seen_params.add(param)
                g.add((param_uri, RDF.type, BDQFFDQ.Parameter))
        except ValueError:
            pass


# ── Main graph builder ────────────────────────────────────────────────────────

def build_graph(rows: list, additional_guids: dict, ie_guids: dict,
                policy_guids: dict, citation_guids: tuple) -> Graph:
    """
    Build a complete RDF graph for all included bdqtest terms.

    `citation_guids` is the (guid_map, url_to_guid) tuple returned by
    load_citation_guids().
    """
    g = Graph()
    _bind_namespaces(g)

    guid_map, url_to_guid = citation_guids

    seen_ies      = {}   # guid_iri (str) -> URIRef
    seen_refs     = set()
    seen_ontology = set()
    seen_params   = set()

    # policy_collections: (usecase, policy_type) -> [version_iri, …]
    policy_collections = {}

    # Build term_iri -> label map for aggregatesResponsesFrom look-up
    term_iri_to_label = {r['term_iri'].strip(): r['Label'].strip()
                         for r in rows}

    for row in rows:
        label        = row['Label'].strip()
        guid         = row['term_localName'].strip()
        issued       = row['issued'].strip()
        test_type    = row['Type'].strip()
        res_type     = row['Resource Type'].strip()
        dimension    = row.get('Dimension', '').strip()
        criterion    = row.get('Criterion', '').strip()
        enhancement  = row.get('Enhancement', '').strip()
        description  = row.get('Description', '').strip()
        notes        = row.get('Notes', '').strip()
        pref_label   = row.get('prefLabel', '').strip()
        history_url  = row.get('historyNoteUrl', '').strip()
        references   = row.get('References', '').strip()
        examples_raw = row.get('Examples', '').strip()
        source       = row.get('Source', '').strip()
        mechanisms   = row.get('Example Implementations (Mechanisms)', '').strip()
        source_code  = row.get('Link to Specification Source Code', '').strip()
        issue_labels = row.get('IssueLabels', '').strip()
        exp_response = row.get('ExpectedResponse', '').strip()
        auth_def     = row.get('AuthoritiesDefaults', '').strip()
        au_ie        = row.get('InformationElement:ActedUpon', '').strip()
        cons_ie      = row.get('InformationElement:Consulted', '').strip()
        use_cases_raw = row.get('UseCases', '').strip()
        agg_from     = row.get('aggregatesResponsesFrom', '').strip()

        # Prefer Method/Spec GUIDs from additional_guids (authoritative file).
        ag = additional_guids.get(guid, {})
        method_guid = ag.get('method') or row.get('MethodGuid', '').strip()
        spec_guid   = ag.get('spec')   or row.get('SpecificationGuid', '').strip()

        if test_type not in ('Validation', 'Issue', 'Measure', 'Amendment'):
            continue

        # ── IRIs ────────────────────────────────────────────────────────────
        version_iri = BDQTEST[f"{guid}-{issued}"]

        # ── Ontology support: test subClassOf DataQualityNeed ────────────────
        _ensure_test_subclass(g, test_type, seen_ontology)

        # ── Test instance triples ────────────────────────────────────────────
        g.add((version_iri, RDF.type, _test_class(test_type)))

        if res_type:
            rt_node = _ensure_resource_type(g, res_type, seen_ontology)
            g.add((version_iri, BDQFFDQ.hasResourceType, rt_node))

        g.add((version_iri, SKOS.note, Literal(notes)))

        if dimension:
            dim_node = _ensure_dimension(g, dimension, seen_ontology)
            g.add((version_iri, BDQFFDQ.hasDataQualityDimension, dim_node))

        g.add((version_iri, DCTERMS.description, Literal(description)))

        if criterion and test_type in ('Validation', 'Issue'):
            crit_node = _ensure_criterion(g, criterion, seen_ontology)
            g.add((version_iri, BDQFFDQ.hasCriterion, crit_node))

        if enhancement and test_type == 'Amendment':
            enh_node = _ensure_enhancement(g, enhancement, seen_ontology)
            g.add((version_iri, BDQFFDQ.hasEnhancement, enh_node))

        # ── Information Elements ─────────────────────────────────────────────
        is_multirecord_agg = (res_type == 'MultiRecord' and agg_from)

        if is_multirecord_agg:
            au_node = _add_multirecord_ie_node(g, row, term_iri_to_label,
                                               ie_guids, seen_ies, seen_ontology)
            if au_node is not None:
                g.add((version_iri, BDQFFDQ.hasActedUponInformationElement, au_node))
        else:
            if au_ie:
                ie_lbl = _ie_label('ActedUpon', au_ie)
                ie_gid = ie_guids.get(ie_lbl)
                if ie_gid:
                    node = _add_standard_ie_node(g, 'ActedUpon', ie_gid,
                                                 au_ie, seen_ies, seen_ontology)
                    g.add((version_iri, BDQFFDQ.hasActedUponInformationElement, node))

            if cons_ie:
                ie_lbl = _ie_label('Consulted', cons_ie)
                ie_gid = ie_guids.get(ie_lbl)
                if ie_gid:
                    node = _add_standard_ie_node(g, 'Consulted', ie_gid,
                                                 cons_ie, seen_ies, seen_ontology)
                    g.add((version_iri, BDQFFDQ.hasConsultedInformationElement, node))

        # Issued date
        g.add((version_iri, DCTERMS.issued, Literal(issued, datatype=XSD.date)))

        # References → BibliographicResource (only URLs in citation_guids)
        if references:
            for url in extract_reference_urls(references):
                ref_uri = _add_bib_resource(g, url, guid_map, url_to_guid, seen_refs)
                if ref_uri is not None:
                    g.add((version_iri, DCTERMS.references, ref_uri))

        if history_url:
            g.add((version_iri, SKOS.historyNote, Literal(history_url)))

        g.add((version_iri, RDFS.label, Literal(label)))
        g.add((version_iri, DCTERMS.isVersionOf, BDQTEST[guid]))

        full_pref = f"{pref_label} for {res_type}" if res_type else pref_label
        g.add((version_iri, SKOS.prefLabel, Literal(full_pref)))

        # ── Method node ──────────────────────────────────────────────────────
        _ensure_method_subclass(g, test_type, seen_ontology)

        if method_guid:
            method_uri = URIRef(method_guid)
            g.add((method_uri, RDF.type, _method_class(test_type)))

            if issue_labels:
                g.add((method_uri, SKOS.note, Literal(issue_labels)))
            if mechanisms:
                g.add((method_uri, SKOS.note,
                        Literal(f"Example Implementations: {mechanisms}")))
            if source_code:
                g.add((method_uri, SKOS.note,
                        Literal(f"Example Implementations Source Code: {source_code}")))

            if spec_guid:
                g.add((method_uri, BDQFFDQ.hasSpecification, URIRef(spec_guid)))

            if source:
                g.add((method_uri, SKOS.historyNote,
                        Literal(f"Source: {source}")))

            # Label / prefLabel — Validation uses "with Specification for:",
            # all other types use "with Specification Specification for:".
            mn = _method_class_name(test_type)
            if test_type == 'Validation':
                m_label = (f"{mn}: {label}"
                           f" with Specification for: {label}")
            else:
                m_label = (f"{mn}: {label}"
                           f" with Specification Specification for: {label}")

            g.add((method_uri, RDFS.label, Literal(m_label)))
            g.add((method_uri, SKOS.prefLabel, Literal(m_label)))
            g.add((method_uri, _for_predicate(test_type), version_iri))

        # ── Specification node ───────────────────────────────────────────────
        if spec_guid:
            spec_uri = URIRef(spec_guid)
            g.add((spec_uri, RDF.type, BDQFFDQ.Specification))

            for ex in parse_examples(examples_raw):
                g.add((spec_uri, SKOS.example, Literal(ex)))

            g.add((spec_uri, BDQFFDQ.hasAuthoritiesDefaults, Literal(auth_def)))
            g.add((spec_uri, BDQFFDQ.hasExpectedResponse, Literal(exp_response)))
            g.add((spec_uri, RDFS.label, Literal(f"Specification for: {label}")))

            spec_desc = exp_response
            if auth_def:
                spec_desc = f"{exp_response} {auth_def}"
            g.add((spec_uri, DCTERMS.description, Literal(spec_desc)))

            _add_argument_nodes(g, row, spec_uri, seen_params)

        # ── Policy collection tracking ────────────────────────────────────────
        pt = _test_type_to_policy_type(test_type)
        for uc in [u.strip() for u in use_cases_raw.split(',') if u.strip()]:
            policy_collections.setdefault((uc, pt), []).append(version_iri)

    # ── Policy / UseCase nodes ────────────────────────────────────────────────
    seen_usecases = set()

    for (uc, pt), members in policy_collections.items():
        policy_guid = policy_guids.get((uc, pt))
        if not policy_guid:
            continue

        policy_uri = URIRef(policy_guid)
        noun       = _policy_noun(pt)

        g.add((policy_uri, RDF.type, _policy_class(pt)))
        for m in members:
            g.add((policy_uri, BDQFFDQ.includedInPolicy, m))

        lbl = f"{pt}: ({len(members)}) {noun}  in UseCase {uc}"
        g.add((policy_uri, RDFS.label, Literal(lbl)))

        try:
            uc_uri = resolve_curie(uc)
        except ValueError:
            uc_uri = URIRef(uc)

        g.add((policy_uri, BDQFFDQ.hasUseCase, uc_uri))

        # ValidationPolicy also gets skos:prefLabel
        if pt == 'ValidationPolicy':
            g.add((policy_uri, SKOS.prefLabel, Literal(lbl)))

        if str(uc_uri) not in seen_usecases:
            seen_usecases.add(str(uc_uri))
            g.add((uc_uri, RDF.type, BDQFFDQ.UseCase))
            g.add((uc_uri, RDFS.label, Literal(uc)))

    return g


# ── Serialization ─────────────────────────────────────────────────────────────

def serialize_graph(g: Graph, out_ttl: str, out_rdfxml: str,
                    out_jsonld: str) -> None:
    if out_ttl:
        g.serialize(destination=out_ttl, format='turtle', encoding='utf-8')
        print(f"Written: {out_ttl}", file=sys.stderr)
    if out_rdfxml:
        g.serialize(destination=out_rdfxml, format='xml', encoding='utf-8')
        print(f"Written: {out_rdfxml}", file=sys.stderr)
    if out_jsonld:
        g.serialize(destination=out_jsonld, format='json-ld', encoding='utf-8')
        print(f"Written: {out_jsonld}", file=sys.stderr)


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument('--in-term-versions',   required=True,
                   help='bdqtest_term_versions.csv')
    p.add_argument('--guid-file',          required=True,
                   help='TG2_tests_additional_guids.csv')
    p.add_argument('--ie-guid-file',       required=True,
                   help='information_element_guids.csv')
    p.add_argument('--policy-guid-file',   required=True,
                   help='TG2_policy_guids.csv')
    p.add_argument('--citation-guid-file', required=True,
                   help='TG2_citation_guids.csv')
    # Accepted for CLI compatibility; not used
    p.add_argument('--argument-guid-file', default=None,
                   help='TG2_tests_argument_guids.csv (accepted; not used)')
    p.add_argument('--out-ttl',    default=None, help='Output Turtle file')
    p.add_argument('--out-rdfxml', default=None, help='Output RDF/XML file')
    p.add_argument('--out-jsonld', default=None, help='Output JSON-LD file')
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    print("Loading CSV files …", file=sys.stderr)
    additional_guids  = load_additional_guids(args.guid_file)
    ie_guids          = load_ie_guids(args.ie_guid_file)
    policy_guids      = load_policy_guids(args.policy_guid_file)
    citation_guids    = load_citation_guids(args.citation_guid_file)
    rows              = load_test_rows(args.in_term_versions)
    print(f"  {len(rows)} recommended test rows loaded.", file=sys.stderr)

    print("Building RDF graph …", file=sys.stderr)
    g = build_graph(rows, additional_guids, ie_guids, policy_guids,
                    citation_guids)
    print(f"  {len(g)} triples.", file=sys.stderr)

    serialize_graph(g, args.out_ttl, args.out_rdfxml, args.out_jsonld)
    print("Done.", file=sys.stderr)


if __name__ == '__main__':
    main()
