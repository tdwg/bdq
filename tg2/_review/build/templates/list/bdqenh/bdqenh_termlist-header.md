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

## 1 Introduction (non-normative)

This document includes terms that are individuals of type bdqffdq:Enhancement intended to be used as a controlled value for bdqffdq:hasEnhancement in the BDQ Core tests.

### 1.1 Data Quality Enhancement

Enhancement as used in the context of BDQ Core, was originally defined by Viega 2016 and Veiga et at. 2017, where it is a fundamental concept. The concept of bdqffdq:Enhancement (AssumedDefault, Converted, From, Standardized, and Transposed)  describes how a bdqffdq:Amendment may act to produce proposals to improve data quality for a given use case.

The Enhancement describes, in abstract terms, how proposals can modify data to improve fitness.  An enhancement expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Enhancements have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

Each Amendment in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) and following a particular bdqffdq:Enhancement propose how the quality of data may be improved. For example, the test [AMENDMENT_EVENTDATE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/718dfc3c-cb52-4fca-b8e2-0e722f375da7) evaluates the value of dwc:eventDate and may propose an a amendment which would conform the value to the expectations of the ISO 8601 standard, proposing to improve the quality of the record under test for the bdq:Spatial-Temporal_Patterns and bdq:Record-Management use cases.  The appropriate value for bdqenh: to use as the bdqffdq:hasEnhancement property for this test is bdqenh:Standardized, that is, a change is proposed to the value of dwc:eventDate that would conform it to the ISO date format standard, specified in the Comments on dwc:eventDate as the recommended best practice for this term.

Enhancement only applies to tests of type bdqffdq:Amendment.

### 1.2 Status of the content of this document

Section 2 is normative.

In Section 4, the values of the `Term IRI`, `Term Name`, `Type`, `Definition` and `Controlled value` are normative. The values of `Comments`, `Label` and `Preferred Label` are non-normative. 

### 1.3 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| ------ | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqenh:  | https://rs.tdwg.org/bdqenh/terms |
| bbqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.5 Key to Vocabulary Terms

{term_key}

## 2 Use of Terms (normative) 

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of `bdqffdq:Enhancement`.

Each bdqffdq:Amendment SHOULD have exactly one bdqffdq:hasEnhancement property relating it to a term in this bdqenh: vocabulary.

Instances of bdqffdq:Measure, bdqffdq:Validation, and bdqffdq:Issue SHOULD NOT have bdqffdq:hasEnhancement properties relating them to a term in this bdqenh: vocabulary.

### 2.1 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 3 Term index
