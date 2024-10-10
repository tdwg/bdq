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

## 1 Introduction (non-normative)

This document includes terms that extend the basic bdqffdq vocabulary and are integral to bdqffdq as an ontology..

### 1.1 Fittness for Use Framework Vocabulary terms.

The bdqffdq framework is represented as an owl ontology.  The basic terms for that framework are in the
[basic bdqffdq vocabulary](../../list/bdqffdq/index.md).  The TDWG Standards Documentation Specification requires
that the human readable documentation for ontologies be presented as a term list with additional axioms included
in a vocabulary extension.  This file documents the additional axioms in isolation.  

See the [landing page for bdqffdq:](../../bdqffdq/index.md) for normative guidance on the bdqffdq: framework 
ontology, and the [guide to bdqffdq:](../../guide/bdqffdq/index.md) page for a guide to the ontology.

The bdqffdq ontology includes few restrictions, this is by design.  Domain and range restrictions do not limit
what is in the domain or range of a property, but add assertions about the types of objects that are the subjects
or objects of predicates bearing the restrictions.  Some types of restrictions limit which owl profiles are
available to tools that reason on the ontology and on data stores that include the ontology.

### 1.2 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section 1.5 lists which values in Section 4 are normative and which are non-normative.

### 1.3 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bbqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/extension/{pref_namespace_prefix}/index.md | This file | 
| Owl Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.5 Key to Vocabulary Terms

{term_key}

## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values from the `bdq:` namespace, except for bdq:empty and bdq:notEmpty, where controlled value strings MUST be used.

### 2.1 RFC 2119 key words (normative)
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

## 3 Term index (non-normative)
