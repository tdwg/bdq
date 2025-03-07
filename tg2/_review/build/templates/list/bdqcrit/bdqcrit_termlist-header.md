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

This document includes terms that are individuals of type bdqffdq:Criterion intended to be used as a controlled value for bdqffdq:hasCriterion in the BDQ Core tests.

### 1.1. Purpose

This is the term-list document for the bdqcrit: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.

### 1.3 Data Quality Criteria

Criterion as used in the context of BDQ Core, was originally defined by Veiga 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:Criterion (Complete, Consistent, Found, InRange, Likely, NotEmpty, Standard, Unambiguous) describes, in abstract terms how data can be evaluated for quality for a given use case.
  
A criterion expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Criteria have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

Each bdqffdq:Validation and bdqffdq:Issue in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) following a single bdqffdq:Criterion. For example, the test VALIDATION_COUNTRY_FOUND tests the value of dwc:country against a source authority for a use case, (e.g.  bdq:Record-Management).  The appropriate type of bdqffq:Criterion in this case is bdqcrit:Found i.e. does the value of dwc:contry conform to the values in a specfied authority when you are evaluating the quality of a Darwin Core record (in the context of the use case with which VALIDATION_COUNTRY_FOUND is composed)?

Criterion applies only Test Types bdqffdq:Validation and bdqffdq:Issue.

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
| ------ | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqcrit: | https://rs.tdwg.org/bdqcrit/terms |
| bdqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.8 Key to Vocabulary Terms

{term_key}

Terms used to describe the terms in this vocabulary follow the guidance of the [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/).  Term definitions include the definition of the underlying RDF vocabulary term, and may include a TDWG specific meaning from the SDS, and may also include specific definition in this local context.

## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used values of `bdqffdq:Criterion`.

Each bdqffdq:Validation and bdqffdq:Issue SHOULD have exactly one bdqffdq:hasCriterion property relating it to a term in this bdqcrit: vocabulary.

Instances of bdqffdq:Measure and bdqffdq:Amendment SHOULD NOT have bdqffdq:hasCriterion properties relating them to a term in this bdqcrit: vocabulary.

## 3 Term index
