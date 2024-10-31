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

This document includes terms that form the bdqffdq: vocabulary.  The bdqffdq: vocabulary is used to describe the the BDQ Core tests.

The bdqffdq: terms include classes, object properties, datatype properties, and named individuals.  
This document only lists the terms, it does not provide additional axioms or normative guidance needed for their use.

The bdqffdq framework is represented as an owl ontology (the Framework Ontology).  The basic terms for that framework are listed in this document.  
The TDWG Standards Documentation Specification requires that the human readable documentation for ontologies be presented 
as a term list with additional axioms included in a vocabulary extension.  A [vocabulary extension](../../extension/bdqffdq/index.md) 
documents additional axioms.  

### 1.1 Purpose
: This is the term-list document for the bdqffdq: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.

### 1.3 Documents about the bdqffdq: ontology

The bdqffdq: vocabulary is an ontology, documentation for it can be found in: 

- A [landing page](../../bdqffdq/index.md) with normative guidance on the use of this ontology.
- This page, the list of vocabulary terms in the ontology.
- Additional axioms that extend the vocabulary terms in the [vocabulary extension list](../../extension/bdqffdq/index.md) 
- The bdqffdq framework ontology is best technically understood as its [Owl Ontology Distribution](../../../vocabulary/bdqffdq.owl) 

An illustrated guide to the use of the bdqffdq ontology is provided in the [Guide to the bdqffdq: framework](../../guide/bdqffdq/index.md) 

### 1.3.1 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| Owl Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.4 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4, the values of following terms are normative: Term IRI, Name, Type, Definition.

In Section 4, the values of the following term are non-normative: Comment, skos:prefLabel, rdfs:label

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.6 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bbqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.7 Key to Vocabulary Terms

{term_key}

## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values from the `bdq:` namespace, except for bdq:empty and bdq:notEmpty, where controlled value strings MUST be used.

## 3 Term index (non-normative)
