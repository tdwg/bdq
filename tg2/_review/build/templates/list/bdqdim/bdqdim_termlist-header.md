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

{toc}

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to provide the full term list for the `bdqdim:` controlled vocabulary, which defines the values of `bdqffdq:DataQualityDimension` used in BDQ Core Tests. Each Data Quality Dimension describes a specific aspect of quality that a Test is intended to assess, such as completeness, conformance, or reliability.

These Dimensions serve as a semantic anchor for describing the intent of Tests and enable structured classification and interpretation of Test results across diverse Use Cases.

### 1.2 Audience

This document is intended for users who need a technical understanding of how BDQ Core Tests relate to conceptual dimensions of data quality. It will be especially useful for:

- Standards developers and modelers applying the BDQ Core Framework Ontology;
- Implementers who need to map Tests to dimensions in automated systems;
- Curators and analysts reviewing Test results in the context of data improvement initiatives.

A working familiarity with the BDQ Core Test structure and the Framework Ontology is helpful, though not required to benefit from this document.

### 1.3 Data Quality Dimensions

The concept of `bdqffdq:DataQualityDimension`, originally introduced by Veiga (2016) and Veiga et al. (2017), represents the aspect or attribute of data quality being evaluated. Common dimensions include `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, and `Resolution`. These serve as high-level categories that group Tests according to the type of quality issue they address.

Dimensions are measurable characteristics of an `bdqffdq:InformationElement` and provide insight into how quality is defined and assessed for a given Use Case.

Each BDQ Core Test typically evaluates one or more data values (Information Elements) with respect to a single Data Quality Dimension. For example, the Test `VALIDATION_COUNTRY_FOUND` assesses the value of `dwc:country` for conformance to a reference authority. In this case, the relevant dimension is `bdqdim:Conformance`.

Unlike Criteria, which apply only to Validation and Issue Tests, Data Quality Dimensions apply to all BDQ Core Test types: `bdqffdq:Validation`, `bdqffdq:Issue`, `bdqffdq:Amendment`, and `bdqffdq:Measure`.

### 1.4 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality (BDQ) Core](../../index.md) page, which lists the parts of the standard.

### 1.5 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.6 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

Section [1.9 Key to Vocabulary Terms](#19-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.7 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.8 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
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

A value for `bdqffdq:hasdataQualityDimension` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqdim/terms/Completeness`) or Term Qualified name (e.g., `bdqdim:Completeness`) from the bdqdim: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `Completeness`) MAY be used. In a purely human context a Label (e.g., `Completeness`) MAY be used.

Each instance of a Test, regardless of Test type, SHOULD have exactly one bdqffdq:hasdataQualityDimension property relating it to a term in this bdqdim: vocabulary.

## 3 Term index
