# Table of Contents
{toc}

## 1.0 Introduction

This document lists the BDQ Core tests. It includes terms from the
namespaces `bdqcore:` (the core tests), `bdq:` (parent namespace),
`bdqffdq:` (framework for data quality), `bdqdim:` (data quality dimension
from xxx), `bdqenh:` (test enhancements) and `bdqcrit:` (test criteria).
For background details see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J,
Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA,
Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved
Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity
Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889.

The focus of this standard are a suite of tests that operate on a single
(SingleRecord) Darwin Core (https://dwc.tdwg.org/) encoded record, for
example VALIDATION_COUNTRYCODE_STANDARD. This test checks the value of
dwc:countryCode against the source authority ISO 3166-1-alpha-2 Country
Code using https://www.iso.org/obp/ui/#search. The data quality framework
(ref) on which these tests are based, allows for MultiRecord tests that
could identify outliers within a data set or could accumulate results of a
SingleRecord tests, such as above, for example 70% of records in a dataset
had a valid dwc:countryCode.

Each test is designed to stand in isolation. This is by design to both
support the mixing and matching of these and other tests to meet particular
data quality needs, and so as not impose any particular model of test
execution on implementation frameworks. Implementations of test execution
frameworks may execute tests in on data records in parallel, on data
records in sequence, as queries on data sets, on unique values.

Tests are paired in that all AMENDMENTs require a corresponding VALIDATION
that assesses some aspect of data quality. An AMENDMENT may be able to
improve the quality of data with respect to that VALIDATION.

## 2.0 Types of Tests
There are four types of tests: Validations, Amendments, Measures, and
Issues.

A **Validation** examines the values of Darwin Core terms against a
criterion for quality. An example is VALIDATION_COUNTRYCODE_STANDARD where
dwc:countryCode is checked against a source authority for validity.

An **Amendment** examines the values of Darwin Core terms to identify
potential changes to improve the quality. An example is
AMENDMENT_COUNTRYCODE_STANDARDIZED where a valid ISO country code could be
inferred.

**Issues** are like Validations in identifying potential problems in the
data that may or may not be problems for all users. For example,
ISSUE_DATAGENERALIZATIONS_NOTEMPTY alerts users to a non-empty value that
should be examined against their data quality needs. Issues are a 'warning
flag' while Validations assert that the data are fit for use or not.

**Measures** either count things, or assert that data evaluate as fit for
some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is
MEASURE_VALIDATIONTESTS_NOTCOMPLIANT that returns the number of tests of
Type Validation that had a response of "Not Compliant".

## 3.0 Test Descriptors

The Test Descriptors are terms that are necessary to comprehensively
describe the test. Some terms, such as the GUID are intended for machine
consumption. Some terms such as the "Description" are designed to be
human-readable and to be understood by consumers of biodiversity data
quality reports. Terms such as the "Specification" ensure that implementers
have no ambiguity about how the test should be coded.

**Term Name**. The full identifier for the test in the form of
"bdqcore:"test GUID, for example
"bdqcore:42408a00-bf71-4892-a399-4325e2bc1fb8"
**Label**. An easy-to-read English descriptive label in the form of Test
Type_Darwin Core Term(s) used_criterion, for example
"VALIDATION_BASISOFRECORD_STANDARD"
**iri**. A composite of the web address of the test with its GUID and date
last updated appended, for example "
https://rs.tdwg.org/bdqcore/terms/version/15f78619-811a-4c6f-997a-a4c7888ad849-2023-09-18
"
**term-iri**. The unversioned form of the iri, as for example "
https://rs.tdwg.org/bdqcore/terms/15f78619-811a-4c6f-997a-a4c7888ad849"
**issued**. The date the test was finalized for submission (ISO 8601), for
example "2023-01-17"
**DateLastUpdated**. The date the test was last updated (ISO 8601), for
example "2024-09-30"
**prefLabel**. An easy to read label for the test, for example "Validation
dcterms:license Standard"
**IE Class**. The Darwin Core Information Element class, for example
"Record-level"
**InformationElement:ActedUpon**. The Darwin Core term(s) that are the
focus of the test, for example "dwc:country, dwc:countryCode"
**InformationElement:Consulted**. The Darwin Core term(s) that are required
to be consulted in the process of evaluating the
InformationElements:ActedUpon, for example "dwc:countryCode"
**Specification**. The formal definition of how the test must be
implemented, for example "EXTERNAL_PREREQUISITES_NOT_MET if the
bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the
dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be
unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the
bdq:sourceAuthority; otherwise NOT_COMPLIANT"
**AuthoritiesDefaults**. The source authority that the test must consult to
provide a response. The format is ideally in two parts, the first part
referring to what the authority is, and if available, a second part that
provides an API that can be used for evaluation. For example
"bdq:sourceAuthority default = "ISO 3166 Country Codes" {[
https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2
Country Code search [https://www.iso.org/obp/ui/#search]}"
**Description**. A breif English description of what the test does
**Criterion Label**. A combination of the Dimension (bdqdim:) value and the
bdqcrit: value, for example "Conformance: standard"
**Type**. The type of the test, one of VALIDATION, ISSUE, AMENDMENT or
MEASURE, for example "**VALIDATION**_DECIMALLONGITUDE_INRANGE"
**Resource Type**. The test either operates on a Single Record or Multiple
Records (?? bdq...used here or keep it simple English)...this generally
relates to this list.
**Dimension**. The Data Quality Dimension focus of the test: One of
"Completeness", "Conformance", "Consistency", "Likeliness", "Reliability"
or "Resolution".
**Enhancement**. For AMENDMENTS: The type of enhancement that is bring
proposed. One of "Assumed Default", "Converted", "Fill in From",
"STandardized" and "Transposed".
**Examples**. Two examples of input and output data and test responses for
a 'pass' and 'fail' case, for example "[dwc:country="Eswatini":
Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT,
Response.comment="dwc:country is a valid country name in the
bdq:sourceAuthority"], [dwc:country="Tasmania":
Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT,
Response.comment="Tasmania is not found at the level of national in the
bdq:sourceAuthority"]
**Source**. The origin of the concept of the test, for example "ALA" (The
Atlas of Living Australia)
**References**. The minimum set of references that are required for an
understanding of the nature of the test
**Notes**. Additional information that may not be obvious from the
Specification, for example for the test "VALIDATION_COUNTRYCODE_STANDARD",
the Notes are "Locations outside of a jurisdiction covered by a country
code may have a value in the field dwc:countryCode, the ISO user defined
codes include XZ used by the UN for installations on the high seas and
suitable for a marker for the high seas.  Also available in the ISO user
defined codes is ZZ, used by GBIF to mark unknown countries.  This test
should accept both XZ and ZZ as COMPLIANT country codes. This test must
return NOT_COMPLIANT if there is leading or trailing whitespace or there
are leading or trailing non-printing characters".
**UseCases**. An example of one or more Use Cases where this test would
apply. Note that one test will likely have many Use Cases, and one Use Case
will likely have many applicable tests.
**skos:historyNote**. A link (URL) to the github issue that provides a
history (changes and comments) of the development of the test, for example
https://github.com/tdwg/bdq/issues/36.
**bdqffdq:AmendmentMethod**. For AMENDMENTs: A URN to the
AmendmentMethodLabel in for form of "urn:uuid:GUID", for example
"urn:uuid:1f38a0bc-4e1f-47a4-bd4a-b6be1c9a456a"
**AmendmentMethod label**. For AMENDMENTs: The nature of the method of
AMENDMENT, for example "AmendmentMethod: Proposes an amendment to the value
of dc:type using the DCMI type vocabulary.Amedment for SingleRecord with
Specification Specification for: AMENDMENT_DCTYPE_STANDARDIZED"
**bdqffdq:Specification**. For AMENDMENTs: A urn in the form of
"urn:uuid:GUID" that points to the Specification label, for example
"urn:uuid:825f551a-2adf-4509-9f95-5a42601a8e88"
**Specification label**. A descriptive label for the specification of an
AMENDMENT, for example "Specification for: AMENDMENT_LICENSE_STANDARDIZED"

## 4.0 Example RDF (non-normative)

A more complete description of the tests can be found in the RDF
representation of this vocabulary.

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe
VALIDATION_COUNTRYCODE_STANDARD

<rdf:Description rdf:about="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe">
    <rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/Specification"/>
    <rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string
">VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>  
    <rdfs:comment
rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET  
if bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if
the dwc:countryCode was EMPTY; COMPLIANT if dwc:countryCode can be
unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code;
otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country
Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO
3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]
}</rdfs:comment>
</rdf:Description>

<rdf:Description rdf:about="urn:uuid:54fdf7a8-c1b1-4c21-b0a2-1f5aa86d3461">
    <rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ValidationMethod"/>
    <hasValidation xmlns="http://rs.tdwg.org/bdq/ffdq/"
rdf:resource="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9"/>
   <hasSpecification xmlns="http://rs.tdwg.org/bdq/ffdq/"
rdf:resource="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
</rdf:Description>

<rdf:Description rdf:about="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9">
    <rdf:type rdf:resource="
http://rs.tdwg.org/bdq/ffdq/ContextualizedCriterion"/>  
    <hasActedUponInformationElement xmlns="http://rs.tdwg.org/bdq/ffdq/"
rdf:resource="urn:uuid:c8c64b57-6bed-49f0-b273-d6bc95b12916"/>
    <hasCriterion xmlns="http://rs.tdwg.org/bdq/ffdq/"
rdf:resource="urn:uuid:1f717a19-54b5-4240-a2c8-fff86d237c2e"/>
    <hasResourceType xmlns="http://rs.tdwg.org/bdq/ffdq/"
rdf:resource="rt:SingleRecord"/>  
    <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is
the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country
code?</rdfs:comment>
    <rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is
the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?
Validation for SingleRecord</rdfs:label>
</rdf:Description>


## 5.0 Status of the content of this document

**left as is for now**
Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4 the values of the rdfs:Label, skos:prefLabel, Versioned IRI,
Resource Type, Specification, Information Elements ActedUpon, Information
Elements Consulted, and Parameters are normative.  The values of
Description, Examples, Use Cases, and Notes are non-normative.

In Section 4, the values of the `Term IRI` and `Definition` are normative.
The values of `Term Name` `skos:pref:Label` are non-normative, although one
can expect that the namespace abbreviation prefix is one commonly used for
the term namespace.  `Label` and the values of all other properties (such
as `Examples` and `Notes`) are non-normative.

## 6.0 Term List Distributions for bdqcore:

| Description | IRI | Download URL | Note |
| ----------- | --- | -----------  | ---- |
| HTML file   | TBD |
https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcore/index.md
| Complete term list  |
| RDF/XML file | TBD |
https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.xml
| RDF/XML  |
| Turtle file | TBD |
https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.ttl
| Turtle  |
| CSV file | TBD |
https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqcore_terms.csv
| CSV list of tests |

## 7.0 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix |  IRI |
| ------ |  --- |
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms/               |
| bdqcrit      | https://rs.tdwh.org/bdqcrit/terms/               |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms/                |
| bdqenh       | https://rs.tdwg.org/bdqenh/terms/                |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema             |
| owl          | http://www.w3.org/2002/07/owl#                   |

## 8.0 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms),
resources MUST be used as values of classes and object properties in the
`bdqffdq:` namespace.
Due to the requirements of [bdq](https://rs.tdwg.org/bdqdim/terms),
resources MUST be used as values of the `bdqdim:` namespace.
Due to the requirements of [bdq](https://rs.tdwg.org/bdqenh/terms),
resources MUST be used as values of the `bdqenh:` namespace.
Due to the requirements of [bdq](https://rs.tdwg.org/bdqcrit/terms),
resources MUST be used as values of the `bdqcrit:` namespace.
Due to the requirements of [bdq](https://rs.tdwg.org/bdq/terms), resources
MUST be used as values of the `bdq:` namespace.

## 9.0 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC 2119](
https://tools.ietf.org/html/rfc2119).

