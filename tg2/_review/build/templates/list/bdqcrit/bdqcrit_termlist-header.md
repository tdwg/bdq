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

## 1 Introduction (non-normative)

This document includes terms that are individuals of type bdqffdq:Criterion intended to be used as a controlled value for bdqffdq:hasCriterion in the BDQ Core tests.

### 1.1 Data Quality Criteria

Criterion as used in the context of BDQ Core, was originally defined by Viega 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:Criterion (Complete, Consistent, Found, InRange, Likely, NotEmpty, Standard, Unambiguous) describes, in abstract terms how data can be evaluated for quality for a given use case.
  
A criterion expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Criteria have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

Each bdqffdq:Validation and bdqffdq:Issue in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) following a single bdqffdq:Criterion. For example, the test VALIDATION_COUNTRY_FOUND tests the value of dwc:country against a source authority for a use case, (e.g.  bdq:Record-Management).  The appropriate type of bdqffq:Criterion in this case is bdqcrit:Found i.e. does the value of dwc:contry conform to the values in a specfied authority when you are evaluating the quality of a Darwin Core record (in the context of the use case with which VALIDATION_COUNTRY_FOUND is composed)?

Criterion applies only Test Types bdqffdq:Validation and bdqffdq:Issue.

### 1.2 Status of the content of this document

Section 2 is normative.

In Section 4, the values of the `Term IRI`, `Term Name`, `Type`, `Definition` and `Controlled value` are normative. The values of `Comments`, `Label` and `Preferred Label` are non-normative. 

### 1.3 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| ------ | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqcrit: | https://rs.tdwg.org/bdqcrit/terms |
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

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used values of `bdqffdq:Criterion`.

Each bdqffdq:Validation and bdqffdq:Issue SHOULD have exactly one bdqffdq:hasCriterion property relating it to a term in this bdqcrit: vocabulary.

Instances of bdqffdq:Measure and bdqffdq:Amendment SHOULD NOT have bdqffdq:hasCriterion properties relating them to a term in this bdqcrit: vocabulary.

### 2.1 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


## 3 Term index
