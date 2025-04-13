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

**Comment**<br>
{comment}

### Table of Contents ###

{toc}

## 1 Introduction

This document defines a vocabulary extension for the bdqffdq: ontology, specifying additional axioms that extend the basic vocabulary terms. These axioms support more precise semantic expression within the Biodiversity Data Quality (BDQ) Fitness for Use Framework Ontology and are essential for its use as a fully functional ontology.

The core terms of the ontology—such as classes, object properties, datatype properties, and named individuals—are listed separately in the Fitness For Use Framework Ontology List of Terms. In line with the TDWG Standards Documentation Specification, this extension document presents only the additional axioms, while keeping the core term list distinct and human-readable.

The BDQ Framework intentionally limits its use of restrictions to preserve compatibility with OWL profiles and reasoning tools. While domain and range axioms appear in this document, they do not constrain data but rather assert expectations about the kinds of resources involved in a given relation. For additional context on usage and intended semantics, refer to the normative and illustrative materials listed below.

### 1.1 Purpose 

This document serves as the official vocabulary extension for the bdqffdq: ontology, listing additional axioms that refine and extend the semantics of the core vocabulary terms. It supports implementers who require these axioms for reasoning, validation, or advanced modeling within the BDQ Framework.

### 1.2 Audience

This document is intended for ontology engineers, semantic tool developers, and others seeking a deeper, technically precise understanding of how the BDQ Fitness for Use Framework operates as an OWL ontology. It assumes familiarity with OWL constructs, reasoning profiles, and the structure of TDWG vocabularies.

### 1.3 Documents about the bdqffdq: ontology

The bdqffdq: ontology is supported by multiple documents that together describe its structure, intended use, and implementation:

- The [Fitness for Use Ontology](../../bdqffdq/index.md), which provides normative guidance on the use of the vocabulary.
- The [Fitness For Use Framework Ontology List of Terms](../../list/bdqffdq/index.md) , which enumerates and describes the vocabulary terms.
- This document, which defines additional axioms extending the core vocabulary.
- The [Fitness For Use Framework Ontology Guide](../../guide/bdqffdq/index.md), a visual and narrative introduction to the concepts and application of the ontology.
- The ontology itself: [Biodiversity Data Quality Fitness for Use Framework](../../../vocabulary/bdqffdq.owl), which provides the formal RDF/OWL representation of the vocabulary.

### 1.3.1 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/extension/{pref_namespace_prefix}/index.md | This file | 
| Owl Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.4 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.7 Key to Vocabulary Terms](#17-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.6 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
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
