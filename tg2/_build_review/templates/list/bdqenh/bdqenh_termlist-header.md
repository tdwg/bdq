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

The purpose of this document is to provide the full term list for the `bdqenh:` controlled vocabulary, which defines the values of `bdqffdq:Enhancement` used in BDQ Amendment Tests. Each Enhancement describes a general strategy by which data may be modified or supplemented to improve its quality in alignment with a specified Use Case.

These terms support the formal description of how Amendments propose changes to data and clarify the intended nature of those proposals.

### 1.2 Audience

This document is intended for users who need a technical understanding of how BDQ Amendment Tests describe proposed improvements to data. It will be especially useful for:

- Implementers developing systems that generate or evaluate data quality Amendments
- Standards developers and data quality modelers working with the BDQ Framework Ontology
- Analysts and data curators reviewing Test results in the context of proposed changes to datasets

Some familiarity with the structure of BDQ Tests and the Framework Ontology is recommended.

### 1.3 Data Quality Enhancements

The concept of `bdqffdq:Enhancement`, as defined by Veiga (2016) and Veiga et al. (2017), captures the general nature of a proposed change intended to improve data quality. Examples of Enhancements include `AssumedDefault`, `Converted`, `From`, `Standardized`, and `Transposed`. These represent high-level categories of amendment strategies.

Enhancements describe, in abstract terms, what a `bdqffdq:Specification` expresses concretely. While Enhancements are informally related to Data Quality Dimensions (e.g., a `Standardized` enhancement might relate to `Conformance`), those relationships are not formally encoded.

Each `bdqffdq:Amendment` Test in `bdqtest:` proposes a change to one or more data values (`bdqffdq:InformationElements`) based on a specific Enhancement. For example, the Test [AMENDMENT_EVENTDATE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_STANDARDIZED) evaluates the term `dwc:eventDate` and may propose a revised value formatted according to the ISO 8601 standard. The Enhancement in this case is `bdqenh:Standardized`.

Enhancements are only applicable to Tests of type `bdqffdq:Amendment`.

### 1.4 Associated Documents

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.5 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | ------------ | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.6 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.9 Key to Vocabulary Terms](#19-key-to-vocabulary-terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.7 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.8 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms            |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.9 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

{term_key}

## 2 Use of Terms (normative) 

A value for `bdqffdq:hasEnhancement` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqenh/terms/AssumedDefault`) or Term Qualified name (e.g., `bdqdim:AssumedDefault`) from the bdqenh: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `AssumedDefault`) MAY be used. In a purely human context a Label (e.g., `Assumed Default`) MAY be used.

Each instance of bdqffdq:Amendment SHOULD have exactly one bdqffdq:hasEnhancement property relating it to a term in this bdqenh: vocabulary.

An instance of bdqffdq:Validation, bdqffdq:Issue, or bdqffdq:Measure SHOULD NOT have a bdqffdq:hasEnhancement property relating it to a term in this bdqenh: vocabulary.

## 3 Term index
