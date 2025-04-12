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

**Comment**
{comment}

## 1 Introduction

This document provides the full details of the controlled vocabulary values (individuals of the type bdqffdq:Criterion) for the term bdqffdq:hasCriterion in the BDQ Core Tests.

### 1.1. Purpose

This is the term-list document for the bdqcrit: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology, especially with respect to the controlled vocabulary for the term bdqffdq:hasCriterion.

### 1.3 Data Quality Criteria

Criterion as used in the context of BDQ Core was originally defined by Veiga 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:Criterion (Complete, Consistent, Found, InRange, Likely, NotEmpty, Standard, Unambiguous) describes, in abstract terms, how data can be evaluated for quality for a given Use Case.

A Criterion expresses in general terms what a bdqffdq:Specification expresses in specific terms. Criteria have an informal relationship to bdqffdq:Dimensions, expressed here in the comments These relationships could be formalized, but we have not done so.

Each bdqffdq:Validation and bdqffdq:Issue in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) following a single bdqffdq:Criterion. For example, the Test VALIDATION_COUNTRY_FOUND tests the value of dwc:country against a source authority for a Use Case, (e.g., bdq:Record-Management). The appropriate type of bdqffq:Criterion in this case is bdqcrit:Found, i.e., does the value of dwc:contry conform to the values in a specfied authority when you are evaluating the quality of a Darwin Core record in the context of the Use Case in which VALIDATION_COUNTRY_FOUND is found?

Criterion applies only to Test types bdqffdq:Validation and bdqffdq:Issue.

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

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
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

A value for `bdqffdq:hasCriterion` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqcrit/terms/NotEmpty`) or Term Qualified name (e.g., `bdqcrit:NotEmpty`) from the bdqcrit: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `NotEmpty`) MAY be used. In a purely human context a Label (e.g., `Not Empty`) MAY be used.

Each instance of bdqffdq:Validation and bdqffdq:Issue SHOULD have exactly one bdqffdq:hasCriterion property relating it to a term in this bdqcrit: vocabulary.

An instance of bdqffdq:Measure or bdqffdq:Amendment SHOULD NOT have a bdqffdq:hasCriterion property relating it to a term in this bdqcrit: vocabulary.

## 3 Term index
