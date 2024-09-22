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
This document includes terms intended to be used as a controlled value for BDQ Core tests with local name `Criterion`.  For details and rationale, see Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>

### 1.1 Data Quality Criteria

The scope of the standard is the fundamental information about core tests of type bdqffdq:Validation or bdqffdq:Issue. The Criterion describes, in abstract terms how data can be evaluated for fitness.  A criterion expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Criteria have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

### 1.2 Data Quality Criteria Vocabulary

<!-- Generated table of terms goes here --->

[CSV File of list of terms to generate content for this section](../../vocabulary/bdqcrit_terms.csv "File from which to generate this section")

| term_localName | definition | comments |
| --------------------- | ----------- | ------------- |
| Complete | Data are present and sufficiently comprehensive for use. | Data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use.  Corresponding dimension is bdqdim:Completeness |
| Consistent | Data are internally consistent and consistent with any authorities consulted.  | A set of bdqffdq:InformationElements and bdq:sourceAuthorities are consistent.   Corresponding dimension is bdqdim:Consistency |
| Found | Data conform to the values in an authority. | Data in a bdqffdq:InformationElement conform to a bdq:sourceAuthority.  Corresponding dimension is bdqdim:Conformance |
| InRange | Data conform to an expected range of values. | Data in a bdqffdq:InformationElement conform to an expected range of values.  Corresponding dimension is bdqdim:Conformance |
| Likely | Data are likely to be true or expected values. | Data in a bdqffdq:InformationElement is likely to be true or expected values.  Corresponding dimension is bdqdim:Likeliness |
| NotEmpty | Some data value is present. | Some value is present in a bdqffdq:InformationElement.  Corresponding dimension is bdqdim:Completeness.   See also bdq:EMPTY and bdq:NOT_EMPTY |
| Standard | Data conform to a format, syntax, data type, or standard. | Data in a bdqffdq:InformationElement conform to a format, syntax, data type, or standard.  Corresponding dimension is bdqdim:Conformance |
| Unambiguous | Data adequately identify a unique entity. | Data in a bdqffdq:InformationElement adequately identifies a unique entity.  Corresponding dimension is bdqdim:Conformance |

<!-- End generated table of terms --->

## 1.3 Use of Terms

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), controlled values from this vocabulary are REQUIRED values of `bdqffdq:Criterion`.

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | {current_iri} | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/{pref_namespace_prefix}/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/{pref_namespace_prefix}.xml | Example for submission, to be generated | 

### 2 Status of the content of this document

In Section 1.2 the values of the `Term IRI`, `Definition` and `Controlled value` are normative. The values of `Term Name`, 'Comments' and `skos:prefLabel` are non-normative. 

### 2.1 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

