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

The purpose of this document is to define the official vocabulary extension for the `bdqffdq:` ontology. It provides additional axioms, such as range constraints and logical distinctions, that refine and extend the semantics of the core vocabulary terms in the BDQ Fitness for Use Framework.

These axioms enable more precise reasoning, validation, and integration with OWL tools. They are intended to complement the human-readable term list provided in the main ontology documentation without altering the open and minimally constrained design of the core Fitness For Use Framework.

This extension follows the TDWG Standards Documentation Specification and maintains a clear separation between core term definitions and ontology logic.

### 1.2 Audience

This document is intended for ontology engineers, semantic modelers, and developers who are applying the BDQ Fitness for Use Framework in OWL environments. It will be especially useful for:

- Implementers using OWL reasoners or validators to enforce or explore logical structures
- Developers of semantic tooling and metadata pipelines based on the BDQ Standard
- Standards developers needing a detailed view of the formal semantics behind BDQ Framework concepts.

This document assumes familiarity with OWL constructs, reasoning profiles, and RDF/OWL modeling practices.

### 1.3 Associated Documents

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

Information about the bdqffdq: ontology, its usage, and its extensions can be found in the following subset of Biodiversity Data Quality (BDQ) resources:

- [**Fitness For Use Framework Ontology Guide**](../../guide/bdqffdq/index.md) Provides a visual and narrative introduction to the concepts and application of the ontology.
- [**Fitness For Use Framework Ontology List of Terms**](../../list/bdqffdq/index.md) The term list document, which enumerates and describes the vocabulary terms.
- [**Fitness for Use Framework Ontology**](../../bdqffdq/index.md) Provides normative guidance on the use of the vocabulary.
- **Fitness For Use Framework Ontology Vocabulary Extension** Defines additional axioms extending the core vocabulary. This document.
- [**Biodiversity Data Quality Fitness for Use Framework (Ontology)**](../../../vocabulary/bdqffdq.owl) The ontology, which provides the formal RDF/OWL representation of the vocabulary.

#### 1.3.1 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/extension/{pref_namespace_prefix}/index.md | This file | 
| OWL Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

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
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |

### 1.7 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

{term_key}

## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqffdq:` namespace MUST use the Term IRI (e.g., `http://rs.tdwg.org/bdq/bdqffdq/hasExpectedResponse`) or Term Qualified name (e.g., `bdqffdq:hasExpectedResponse`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `hasExpectedResponse`) MAY be used. In a purely human context a Label (e.g., `Expected Response`) MAY be used.

## 3 Axiom Index (non-normative)
