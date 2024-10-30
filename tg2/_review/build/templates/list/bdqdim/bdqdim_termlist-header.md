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

This document includes terms that are individuals of type bdqffdq:DataQualityDimension intended to be used as a controlled value for bdqffdq:hasDataQualityDimension in the BDQ Core tests.

### 1.1 Purpose

This is the term-list document for the bdqdim: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.

### 1.3 Data Quality Dimensions 

DataQualityDimension as used in the context of BDQ Core, was originally defined by Viega 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:DataQualityDimension (Completeness, Conformance, Consistency, Likeliness, Reliability, and Resolution) describes the aspect of data quality that a test examines to assess 'quality' for a given use case.

DataQualityDimensions are measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved.

Each test in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) against a single bdqffdq:DataQualityDimension. For example, the test VALIDATION_COUNTRY_FOUND tests the value of dwc:country against a source authority for a use case, (e.g.  bdq:Record-Management).  The appropriate type of bdqffq:DataQualityDimension in this case is bdqdim:Conformance: i.e. how well does the country value conform to an appropriate reference standard when you are evaluating the quality of a Darwin Core record (in the context of the use case with which VALIDATION_COUNTRY_FOUND is composed)?

DataQualityDimension applies to all Test Types (all subclasses of bsqffdq:DataQualityNeed that is, bdqffdq:VALIDATION, bdqffdq:ISSUE, bdqffdq:MEASURE and bdqffdq:AMENDMENT).

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.5 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

In Section 4, the values of the `Term IRI`, `Term Name`, `Type`, `Definition` and `Controlled value` are normative. The values of `Comments`, `Label` and `Preferred Label` are non-normative. 

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bbqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |

### 1.8 Key to Vocabulary Terms

{term_key}

## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of `bdqffdq:dataQualityDimension`.

Each individual instance of subclasses of bdqffdq:DataQualityNeed SHOULD have exactly one bdqffdq:hasDataQualityDimension property relating it to a term in this bdqdim: vocabulary.

## 3 Term index
