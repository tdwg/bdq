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

The purpose of this document is to provide the full term list for the `bdqcrit:` controlled vocabulary, which defines the values of `bdqffdq:Criterion` used in BDQ Tests. Each Criterion represents an abstract way of evaluating whether a data value meets expectations for a particular Use Case.

These terms are central to describing the logic of BDQ Validation and Issue Tests. They express the general kind of judgment being applied to a data value (e.g., whether it is complete, found, or unambiguous), helping users understand what each Test is assessing in a formalized way.

### 1.2 Audience

This document is intended for users who need a technical understanding of how BDQ Tests apply evaluation logic through the use of Criteria. It is especially useful for:

- Implementers interpreting or building Tests that rely on data quality criteria
- Standards developers and data quality modelers applying the BDQ Framework Ontology
- Analysts and curators needing to understand the conceptual basis for different Test evaluations

A working familiarity with the BDQ Test structure and the Framework Ontology is helpful, though not required to benefit from this document.

### 1.3 Data Quality Criteria

The concept of `bdqffdq:Criterion` — originally defined by Veiga (2016) and Veiga et al. (2017) — describes, in abstract terms, how a data value may be evaluated with respect to a particular Use Case. Criteria such as `Found`, `InRange`, `NotEmpty`, `Unambiguous`, and others express broad evaluation patterns that BDQ Validation and Issue Tests apply to one or more `bdqffdq:InformationElements`.

While related informally to `bdqffdq:Dimensions`, Criteria serve a distinct purpose. A `bdqffdq:Criterion` articulates the *type of judgment* applied to data, whereas a `bdqffdq:Specification` captures the *specific logic* used to make that judgment.

Each `bdqtest:` Validation or Issue Test references a Criterion to clarify what kind of quality is being assessed. For example, the Test `VALIDATION_COUNTRY_FOUND` evaluates the value of `dwc:country` against a specified source authority, using the Criterion `bdqcrit:Found` to indicate that the key  quality concern is whether the value exists in the authority’s domain.

### 1.4 Associated Documents

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.5 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.6 Status of the content of this document

Section 1 is non-normative.

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

A value for `bdqffdq:hasCriterion` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqcrit/terms/NotEmpty`) or Term Qualified name (e.g., `bdqcrit:NotEmpty`) from the bdqcrit: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `NotEmpty`) MAY be used. In a purely human context a Label (e.g., `Not Empty`) MAY be used.

Each instance of bdqffdq:Validation and bdqffdq:Issue SHOULD have exactly one bdqffdq:hasCriterion property relating it to a term in this bdqcrit: vocabulary.

An instance of bdqffdq:Measure or bdqffdq:Amendment SHOULD NOT have a bdqffdq:hasCriterion property relating it to a term in this bdqcrit: vocabulary.

## 3 Term index
