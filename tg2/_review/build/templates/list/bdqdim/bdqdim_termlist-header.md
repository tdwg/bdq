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


## 1 Introduction

This document provides the full details of the controlled vocabulary values (individuals of the type bdqffdq:DataQualityDimension) for the term bdqffdq:hasDataQualityDimension in the BDQ Core Tests.

### 1.1 Purpose

This is the term-list document for the bdqdim: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.

### 1.3 Data Quality Dimensions 

DataQualityDimension as used in the context of BDQ Core, was originally defined by Veiga 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:DataQualityDimension (Completeness, Conformance, Consistency, Likeliness, Reliability, and Resolution) describes the aspect of data quality that a test examines to assess 'quality' for a given use case.

DataQualityDimensions are measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved.

Each test in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) against a single bdqffdq:DataQualityDimension. For example, the test VALIDATION_COUNTRY_FOUND tests the value of dwc:country against a source authority for a use case, (e.g., bdq:Record-Management). The appropriate type of bdqffq:DataQualityDimension in this case is bdqdim:Conformance: i.e., how well does the country value conform to an appropriate reference standard when you are evaluating the quality of a Darwin Core record (in the context of the use case with which VALIDATION_COUNTRY_FOUND is composed)?

DataQualityDimension applies to all Test Types (all subclasses of bsqffdq:DataQualityNeed that is, bdqffdq:VALIDATION, bdqffdq:ISSUE, bdqffdq:MEASURE and bdqffdq:AMENDMENT).

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.5 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

Section [1.8 Key to Vocabulary Terms](#18-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bdqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |

### 1.8 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

{term_key}

## 2 Use of Terms (normative)

A value for `bdqffdq:hasdataQualityDimension` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqdim/terms/Completeness`) or Term Qualified name (e.g., `bdqdim:Completeness`) from the bdqdim: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `Completeness`) SHOULD be used. In a purely human context a Label (e.g., `Completeness`) MAY be used.

Each instance of a Test, regardless of Test Type, SHOULD have exactly one bdqffdq:hasdataQualityDimension property relating it to a term in this bdqdim: vocabulary.

## 3 Term index
