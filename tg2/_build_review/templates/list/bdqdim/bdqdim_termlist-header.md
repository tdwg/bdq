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

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to provide the full term list for the `bdqdim:` controlled vocabulary, which defines the values of `bdqffdq:DataQualityDimension` used in BDQ Tests. Each `Data Quality Dimension` describes a specific aspect of quality that a Test is intended to assess, such as completeness, conformance, or reliability.

These `Dimensions` serve as a semantic anchor for describing the intent of Tests and enable structured classification and interpretation of Test results across diverse `Use Cases`.

### 1.2 Audience (non-normative)

This document is intended for users who need a technical understanding of how BDQ Tests relate to conceptual `Dimensions` of data quality. It will be especially useful for:

- Implementers who need to map Tests to `Dimensions` in automated systems
- Standards developers and data quality modelers applying the Fitness for Use Framework Ontology
- Analysts and curators needing to understand the conceptual basis for different Tests’ evaluation

A working familiarity with the BDQ Test structure and the Fitness for Use Framework Ontology is helpful, though not required to benefit from this document.

### 1.3 Data Quality Dimensions (non-normative)

The concept of `bdqffdq:DataQualityDimension`, originally introduced by Veiga (2016) and Veiga et al. (2017), represents the aspect or attribute of data quality being evaluated. Common `Dimensions` include `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, and `Resolution`. These serve as high-level categories that group Tests according to the type of quality issue they address.

`Dimensions` are measurable characteristics of an `bdqffdq:InformationElement` and provide insight into how quality is defined and assessed for a given `Use Case`.

Each BDQ Test typically evaluates one or more data values (`Information Elements`) with respect to a single `Data Quality Dimension`. For example, the Test VALIDATION_COUNTRY_FOUND assesses the value of `dwc:country` for conformance to a `sourceAuthority`. In this case, the relevant dimension is `bdqdim:Conformance`.

Unlike `Criteria`, which apply only to `Validation` and `Issue` Tests, `Data Quality Dimensions` apply to all BDQ Test types: `bdqffdq:Validation`, `bdqffdq:Issue``bdqffdq:Measure`, and `bdqffdq:Amendment`.

### 1.4 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.5 Term List Distributions (non-normative)

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.6 Status of the content of this document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Section [1.9 Key to Vocabulary Terms (normative)](#19-key-to-vocabulary-terms-normative) identifies which values in Section 4 are normative and which are non-normative.

### 1.7 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.8 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.9 Key to Vocabulary Terms (normative)

The terminology used to describe the terms in this vocabulary follows the TDWG [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

{term_key}

## 2 Use of Terms (normative)

A value for `bdqffdq:hasdataQualityDimension` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqdim/terms/Completeness`) or Term Qualified name (e.g., `bdqdim:Completeness`) from the `bdqdim:` namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `Completeness`) MAY be used. In a purely human context a abel (e.g., `Completeness`) MAY be used.

Each instance of a Test, regardless of Test type, SHOULD have exactly one `bdqffdq:hasdataQualityDimension` property relating it to a term in this `bdqdim:` vocabulary.

## 3 Term index (non-normative)
