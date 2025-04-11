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

This document provides the full details of the controlled vocabulary values (individuals of the type bdqffdq:Enhancement) for the term bdqffdq:hasEnhancement in the BDQ Core Tests.

### 1.1 Purpose

This is the term-list document for the bdqenh: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and application of the Framework Ontology. 

### 1.3 Data Quality Enhancement

Enhancement as used in the context of BDQ Core, was originally defined by Veiga 2016 and Veiga et at. 2017, where it is a fundamental concept. The concept of bdqffdq:Enhancement (AssumedDefault, Converted, From, Standardized, and Transposed)  describes how a bdqffdq:Amendment may act to produce proposals to improve data quality for a given use case.

The Enhancement describes, in abstract terms, how proposals can modify data to improve fitness.  An enhancement expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Enhancements have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

Each Amendment in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) and following a particular bdqffdq:Enhancement propose how the quality of data may be improved. For example, the test [AMENDMENT_EVENTDATE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/718dfc3c-cb52-4fca-b8e2-0e722f375da7) evaluates the value of dwc:eventDate and may propose an a amendment which would conform the value to the expectations of the ISO 8601 standard, proposing to improve the quality of the record under test for the bdq:Spatial-Temporal_Patterns and bdq:Record-Management use cases.  The appropriate value for bdqenh: to use as the bdqffdq:hasEnhancement property for this test is bdqenh:Standardized, that is, a change is proposed to the value of dwc:eventDate that would conform it to the ISO date format standard, specified in the Comments on dwc:eventDate as the recommended best practice for this term.

Enhancement only applies to tests of type bdqffdq:Amendment.

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 1.5 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.8 Key to Vocabulary Terms](#18-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms            |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.8 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

{term_key}

## 2 Use of Terms (normative) 

A value for `bdqffdq:hasEnhancement` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqenh/terms/AssumedDefault`) or Term Qualified name (e.g., `bdqdim:AssumedDefault`) from the bdqenh: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `AssumedDefault`) MAY be used. In a purely human context a Label (e.g., `Assumed Default`) MAY be used.

Each instance of bdqffdq:Amendment SHOULD have exactly one bdqffdq:hasEnhancement property relating it to a term in this bdqenh: vocabulary.

An instance of bdqffdq:Validation, bdqffdq:Issue, or bdqffdq:Measure SHOULD NOT have a bdqffdq:hasEnhancement property relating it to a term in this bdqenh: vocabulary.

## 3 Term index
