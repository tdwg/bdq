<!--- Template for header, values provided from yaml configuration --->
# {document_title}

**Title**<br>
{document_title}

**Date version issued**<br>
{ratification_date}

**Date created**<br>
{created_date}

**Part of TDWG Standard**<br>
<{standard_iri}>

**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}

**This version**<br>
<{current_iri}{ratification_date}>

**Latest version**<br>
<{current_iri}>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
{abstract}

**Authors**<br>
{authors}

**Creator**<br>
{creator}

**Bibliographic citation**<br>
{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

**Status**<br>
{comment}

{toc}

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to provide the landing page for the `bdqffdq:` vocabulary, which defines the ontology elements used in the Biodiversity Data Quality Fitness for Use Framework (Ontology). The vocabulary includes classes, object properties, data properties, and named individuals that collectively support the semantic description of BDQ Tests and related quality constructs. Additional axioms, implementation guidance, or usage recommendations are addressed in the [1.3 Associated Documents](#13-associated-documents).

### 1.2 Audience

This document is intended for technical users who need to reference the `bdqffdq:` vocabulary in detail. It is particularly useful for:

- Ontology developers integrating BDQ concepts into semantic systems
- Data quality analysts and system implementers interpreting or expressing BDQ Test structures using RDF/OWL
- Standards developers needing access to term-level details when aligning or extending the BDQ Framework.

Familiarity with RDF, OWL, and the structure of the BDQ Tests is recommended.

### 1.3 Associated Documents

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

Information about the bdqffdq: ontology, its usage, and its extensions can be found in the following subset of BDQ resources:

- [**Fitness For Use Framework Ontology Guide**](../../guide/bdqffdq/index.md) Provides a visual and narrative introduction to the concepts and application of the ontology.
- **Fitness For Use Framework Ontology List of Terms** The term list document, which enumerates and describes the vocabulary terms. This document.
- [**Fitness for Use Framework Ontology**](../../bdqffdq/index.md) Provides normative guidance on the use of the vocabulary.
- [**Fitness For Use Framework Ontology Vocabulary Extension**](../../extension/bdqffdq/index.md) Defines additional axioms extending the core vocabulary.
- [**Biodiversity Data Quality Fitness for Use Framework (Ontology)**](../../../vocabulary/bdqffdq.owl) The ontology, which provides the formal RDF/OWL representation of the vocabulary.

#### 1.3.1 Distributions for bdqffdq:

| Description | IRI | Download URL |
| ----------- | --- | ------------ |
| Human Readable Term List            | TBD | [/docs/list/bdqffdq/index.md](../../list/bdqffdq/index.md) | 
| Human Readable Vocabulary Extension | TBD | [/docs/extension/bdqffdq/index.md](../../extension/bdqffdq/index.md) | 
| OWL Ontology                        | TBD | [/vocabulary/bdqffdq.owl](../../../vocabulary/bdqffdq.owl) |


### 1.4 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.7 Key to Vocabulary Terms](#17-key-to-vocabulary-terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.6 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

**Status**
## 3 Term index (non-normative)
