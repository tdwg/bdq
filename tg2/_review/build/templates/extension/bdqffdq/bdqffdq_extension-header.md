<!--- Template for header, values provided from yaml configuration --->
# {document_title}

Title
: {document_title}

Date version issued
: {ratification_date}

Date created
: {created_date}

Part of TDWG Standard
: <{standard_iri}>

Preferred namespace abbreviation
: {pref_namespace_prefix}

This version
: <{current_iri}{ratification_date}>

Latest version
: <{current_iri}>

{previous_version_slot}

Abstract
: {abstract}

Authors
: {authors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}

### Table of Contents ###

{toc}

## 1 Introduction

This document includes terms that extend the basic bdqffdq vocabulary and are integral to bdqffdq as an ontology.  

The bdqffdq framework is represented as an owl ontology.  The basic terms for that framework are in the
[basic bdqffdq vocabulary](../../list/bdqffdq/index.md).  The TDWG Standards Documentation Specification requires
that the human readable documentation for ontologies be presented as a term list with additional axioms included
in a vocabulary extension.  This file documents the additional axioms in isolation.  

The bdqffdq ontology includes few restrictions, this is by design.  Domain and range restrictions do not limit
what is in the domain or range of a property, but add assertions about the types of objects that are the subjects
or objects of predicates bearing the restrictions.  Some types of restrictions limit which owl profiles are
available to tools that reason on the ontology and on data stores that include the ontology.  See the landing page 
and the bdqffdq: guide for expected uses of the properties that are not provided by these axioms.  

### 1.1 Purpose 

This document provides the required vocabulary extension listing axioms that extend the vocabulary terms in the bdqffdq: term list document.

### 1.2 Audience

This document is for those needing a technical understanding of the bdqffdq Framework. 

### 1.3 Documents about the bdqffdq: ontology

The bdqffdq: vocabulary is an ontology, documentation for it can be found in: 

- A [landing page](../../bdqffdq/index.md) with normative guidance on the use of this ontology.
- The [term list](../../list/bdqffdq/index.md) document listing just the vocabulary terms in the ontology.
- This page, additional axioms that extend the vocabulary terms.
- The bdqffdq framework ontology is best technically understood as its [Owl Ontology Distribution](../../../vocabulary/bdqffdq.owl) 

An illustrated guide to the use of the bdqffdq ontology is provided in the [Guide to the bdqffdq: framework](../../guide/bdqffdq/index.md) 

The [supplement](../../supplement/index.md) includes competency questions providing rationalle for 
the use of framework in the form of an ontology with additional axioms as a vocabulary for 
describing the bdqcore: tests.

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

| Prefix | IRI |
| --- | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bdqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.7 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

{term_key}

## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqffdq:` namespace MUST use the Term IRI (e.g., `http://rs.tdwg.org/bdq/bdqffdq/hasExpectedResponse`) or Term Qualified name (e.g., `bdqffdq:hasExpectedResponse`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `hasExpectedResponse`) MAY be used. In a purely human context a Label (e.g., `Expected Response`) MAY be used.

## 3 Axiom Index (non-normative)
