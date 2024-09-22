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

Contributors
: {contributors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}

## 1 Introduction
This document includes terms intended to be used as a controlled value for BDQ Core tests with local name `Enhancement`.  For details and rationale, see Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>

### 1.1 Data Quality Criteria

The scope of the standard is the fundamental information about core tests of type bdqffdq:Amendment. The Enhancement describes, in abstract terms, how proposals can modify data to improve fitness.  An enhancement expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Enhancements have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

### 1.2 Data Quality Criteria Vocabulary

<!-- Generated table of terms goes here --->

[CSV File of list of terms to generate content for this section](../../vocabulary/bdqenh_terms.csv "File from which to generate this section")

| term_localName |definition | comments | 
| ------------------ |----------- | ------------- | 
| AssumedDefault |Data could be improved by setting an empty value to a default value | Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in with a default value.  Corresponding dimension is bdqdim:Completeness | 
| Converted |Data could be improved by converting from one representation to another | As in spatial coordinate transformations.  Data in a bdqffdq:InformationElement that do not conform to some specification may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance | 
| FillInFrom |Data could be improved by using one data value to fill in the empty value in another | As in filling in from verbatim terms.  Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in by interpretation of values in one or more other terms.  Corresponding dimension is bdqdim:Completeness. | 
| Standardized |Data could be improved by conforming them to a standard representation. | Data in a bdqffdq:InformationElement that do not conform to some format, syntax, data type, or standard may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance | 
| Transposed |Data could be improved by switching values between two or more fields. | Data in a set of at least two bdqffdq:InformationElements that do not conform to expectations may be proposed to have their values switched in order to produce conforming values.  Corresponding dimension is bdqdim:Consistency. | 


<!-- End generated table of terms --->

## 1.3 Use of Terms

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), controlled values from this vocabulary are REQUIRED values of `bdqffdq:Enhancement`.

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 2 Status of the content of this document

In Section 1.2 the values of the `Term IRI`, `Definition` and `Controlled value` are normative. The values of `Term Name`, 'Comments' and `skos:prefLabel` are non-normative. 

### 2.1 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

