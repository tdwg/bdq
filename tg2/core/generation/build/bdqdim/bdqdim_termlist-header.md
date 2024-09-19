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
[!--- JRW finished first draft to here ---]
This document includes terms intended to be used as a controlled value for BDQ Core tests with local name `Dimension`. For details and rationale, see Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>

#### Data Quality Dimensions 

The scope of the standard is the fundamental information about core tests applied to occurrence type Darwin Core records. These tests evaluate one of Data Quality Dimension of the Fitness for Use Framework (Chapman et al., 2020): Measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved. These dimensions are:

* Completeness: The extent to which data are present and sufficiently comprehensive for use.
* Conformance: Conforms to a format, syntax, data type, range, or standard of the Information Element.
* Consistency: Agreement among related Information Elements (q.v.) that are present in the data. Note that missing Information Elements do not make a test Inconsistent.
* Likeliness: The likelihood of Darwin Core Term(s) having true or expected values.
* Reliability: Measure of how the data values agree with an identified source of truth. The degree to which data correctly describes the truth (object, event or any abstract or real 'thing').
* Resolution: Refers to the data having sufficiently detailed information. Measure of the granularity of the data, or the smallest measurable increment.


A "Warning Type" for each test was originally envisioned to provide insight into the nature of the issues, but a review the relationship with "Data Quality Dimension" across the tests suggested such a high degree of correlation that "Warning Type" is effectively redundant. See table xx below. **NEEDS UPDATING**

| Data Quality Dimension/Warning Type | Ambiguous | Amended | Incomplete | Inconsistent | Invalid | Issue | Report | Unlikely | Total |
|-------------------------------------|-----------|---------|------------|--------------|---------|-------|--------|----------|-------|
| Completeness                        |           |   11    |    19      |              |         |   1   |    2   |          |  33   |
| Conformance                         |     2     |   13    |            |       3      |    35   |       |        |          |  53   |
| Consistency                         |           |    1    |            |       5      |         |       |        |          |   6   |
| Likeliness                          |           |         |            |              |         |       |        |     2    |   2   |
| Reliability                         |           |         |            |              |         |   1   |    2   |          |   3   |
| Resolution                          |           |         |            |              |         |   1   |    1   |          |   2   |
| Total                               |     2     |   25    |    19      |       8      |    35   |   3   |    5   |     2    |  99   |

Caption: Data Quality Dimension vs Warning Type with the number of tests as cell values. 

### 1.1 Status of the content of this document

In Section 4, the values of the `Term IRI`, `Definition` and `Controlled value` are normative. The values of `Term Name` and `skos:prefLabel` are non-normative. 

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 2 Use of Terms

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), controlled value strings MUST be used as values of `bdqffdq:dataQualityDimension`.

## 3 Term index