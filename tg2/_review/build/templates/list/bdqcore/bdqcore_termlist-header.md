# Table of Contents
{toc}

## 1 Introduction

This document lists the BDQ Core tests. These are the terms from the namespace `bdqcore:` (the core tests).  The description of these terms relies heavily on the [bdqffdq:](../bdqffdq/index.md) data quality framework vocabulary.  Terms are also used from the namespaces: [bdqdim:](../bdqdim/index.md) (data quality dimension from Veiga et al. 2017), [bdqenh:](../bdqenh/index.md) (test enhancements), [bdqcrit:](../bdqcrit/index.md) (test criteria), and [bdq:](../bdq/index.md) (additional vocabulary terms).  For background details see Chapman et al. (2017).

The focus of this standard is the specifications for a suite of tests that operate on a single (SingleRecord) Darwin Core (Wieczorek et al. 2012) encoded record, for example VALIDATION_COUNTRYCODE_STANDARD. This test checks the value of dwc:countryCode against the source authority ISO 3166-1-alpha-2 Country Code using https://www.iso.org/obp/ui/#search.  This standard also includes specifications for MultiRecord tests that accumulate results of a SingleRecord tests, for example allowing determination that 70% of records in a dataset had a valid dwc:countryCode.

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values.  While tests are described in isolation, they must be used in sets that are related to a use of the data, as data does not have quality in the abstract, it only has quality with respect to some use.  Thus each test is linked to one or more UseCases, which are formal descriptions of uses to which data may be put.  The bdq: vocabulary defines the set of use cases referenced here.  The tests here can be freely composed in other ways for other uses.  

Tests described here are paired in that all Validation Tests that assesses some aspect of data quality are associated with an Amendment Test that may be able to improve the quality of data with respect to that Validation Test.

### 1.1 Purpose

This document lists the BDQ Core Tests, provides values for the terms that describe these tests, and provides a brief explanation of those terms.

### 1.2 Audience

Users who need to understand the tests, including all technical details required in the standard. 

### 1.3 Asociated Documents

The bdqcore: vocabulary includes: 

- A [Quick Reference Guide](../terms/bdqcore/index.md) to the tests.
- This document, a term-list for the vocabulary, containing the vocabulary terms and their metadata.
- A [landing page](../bdqcore/index.md) document with normative guidance on the use of the bdqcore vocabulary.

In addition, A users guide to the use of the bdqcore tests is provided in the [Users Guide](../guide/users/index.md) and a guide to implemetation of the bdqcore tests is provided in the [Implementers Guide](../guide/implementers/index.md) 

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note |
| ----------- | --- | -----------  | ---- |
| HTML file   | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcore/index.md | Complete term list for the bdqcore: vocabulary  | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.xml | An rdf representation of the tests in an RDF/XML serialization | 
| Turtle file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.ttl | An rdf representation of the tests in a Turtle serialization | 
| CSV file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqcore_terms.csv | CSV  filelisting the tests | 

### 1.5 Status of the Content of this Document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section 1.5 identifies which values in Section 4 are normative.

<!--- TODO: Confirm that metadata for 1.5 has these values ---> 
In Section 4 the values of the rdfs:Label, skos:prefLabel, Versioned IRI,
Resource Type, Specification, Information Elements ActedUpon, Information
Elements Consulted, and Parameters are normative.  The values of
Description, Examples, Use Cases, and Notes are non-normative.

## 1.6 Namespace abbreviations

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
| rdfs         | http://www.w3.org/2000/01/rdf-schema#            |
| owl          | http://www.w3.org/2002/07/owl#                   |

## 1.7 Types of Tests

There are four types of BDQ Core Tests: Validations, Issues, Amendments and Measures. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into test suites (profiles) that assess the fitness for use of data for a specific use.

**Validation Tests** examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a criterion for quality. An example is VALIDATION_COUNTRYCODE_STANDARD where dwc:countryCode is checked against a source authority for validity.

**Issue Tests** are like Validations in identifying potential issues in the data that may be problems for all users. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY alerts users to a non-empty value that should be examined against their data quality needs. Issues are a 'warning flag' while Validations assert that the data are fit for use or not. 

**Amendment Tests** examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) to identify potential changes to improve the quality. An example is AMENDMENT_COUNTRYCODE_STANDARDIZED where a valid ISO country code could be inferred.

**Measure Tests** either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is MEASURE_VALIDATIONTESTS_NOTCOMPLIANT that returns the number of tests of Type Validation that had a response of "NOT_COMPLIANT".

### 1.8 Test Descriptors 

The Test Descriptors are terms that are necessary to comprehensively
describe each test. Some terms, such as the IRI and term_localName are 
intended for machine consumption. Some terms such as the "Description" 
are designed to be human-readable and to be understood by consumers 
of biodiversity data quality reports. Terms such as the "Specification" 
ensure that implementers have no ambiguity about how the test should be coded.

{term_key}

<!--- @Tasilee text for comparison with generated table.  Some of these will need to be incorporated into definitions in the generated table.

**Term Name**. The full identifier for the test in the form of "bdqcore:"test GUID, for example "bdqcore:42408a00-bf71-4892-a399-4325e2bc1fb8"

**Label**. An easy-to-read English descriptive label in the form of Test Type_Darwin Core Term(s) used_criterion, for example "VALIDATION_BASISOFRECORD_STANDARD"

**iri**. A composite of the web address of the test with its GUID and date last updated appended, for example " https://rs.tdwg.org/bdqcore/terms/version/15f78619-811a-4c6f-997a-a4c7888ad849-2023-09-18 "

**term-iri**. The unversioned form of the iri, as for example " https://rs.tdwg.org/bdqcore/terms/15f78619-811a-4c6f-997a-a4c7888ad849" 

**issued**. The most recent date for any change to any element of the test (ISO 8601), for example "2023-01-17" 

**DateLastUpdated**. The date an element of the test that would affect implementations was last updated (ISO 8601), for example "2024-09-30" 

**prefLabel**. An easy to read label for the test, for example "Validation dcterms:license Standard"

**IE Class**. The Darwin Core Information Element class, for example "Record-level"

**InformationElement:ActedUpon**. The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that are the focus of the test, for example "dwc:country, dwc:countryCode"

**InformationElement:Consulted**. The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that are required to be consulted in the process of evaluating the InformationElements:ActedUpon, for example "dwc:countryCode"

**Specification**. The formal definition of how the test must be implemented, for example "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT"

**AuthoritiesDefaults**. The source authority that the test must consult to provide a response. The format is ideally in two parts, the first part referring to what the authority is, and if available, a second part that provides an API that can be used for evaluation. For example "bdq:sourceAuthority default = "ISO 3166 Country Codes" {[ https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}"

**Description**. A breif English description of what the test does

**Criterion Label**. A combination of the Dimension (bdqdim:) value and the bdqcrit: value, for example "Conformance: standard"

**Type**. The type of the test, one of VALIDATION, ISSUE, AMENDMENT or MEASURE, for example "**VALIDATION**_DECIMALLONGITUDE_INRANGE"

**Resource Type**. The test either operates on a Single Record or Multiple Records (?? bdq...used here or keep it simple English)...this generally relates to this list.

**Dimension**. The Data Quality Dimension focus of the test: One of "Completeness", "Conformance", "Consistency", "Likeliness", "Reliability" or "Resolution"

**Enhancement**. For AMENDMENTS: The type of enhancement that is bring proposed. One of "Assumed Default", "Converted", "Fill in From", "STandardized" and "Transposed".

**Examples**. Two examples of input and output data and test responses for a 'pass' and 'fail' case, for example "[dwc:country="Eswatini": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country is a valid country name in the bdq:sourceAuthority"], [dwc:country="Tasmania": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Tasmania is not found at the level of national in the bdq:sourceAuthority"]

**Source**. The origin of the concept of the test, for example "ALA" (The Atlas of Living Australia)

**References**. The minimum set of references that are required for an understanding of the nature of the test

**Notes**. Additional information that may not be obvious from the Specification, for example for the test "VALIDATION_COUNTRYCODE_STANDARD", the Notes are "Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and suitable for a marker for the high seas.  Also available in the ISO user defined codes is ZZ, used by GBIF to mark unknown countries.  This test should accept both XZ and ZZ as COMPLIANT country codes. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters".

**UseCases**. An example of one or more Use Cases where this test would apply. Note that one test will likely have many Use Cases, and one Use Case will likely have many applicable tests.

**skos:historyNote**. A link (URL) to the github issue that provides a history (changes and comments) of the development of the test, for example https://github.com/tdwg/bdq/issues/36.

**bdqffdq:AmendmentMethod**. For AMENDMENTs: A URN to the AmendmentMethodLabel in for form of "urn:uuid:GUID", for example "urn:uuid:1f38a0bc-4e1f-47a4-bd4a-b6be1c9a456a"

**AmendmentMethod label**. For AMENDMENTs: The nature of the method of AMENDMENT, for example "AmendmentMethod: Proposes an amendment to the value of dc:type using the DCMI type vocabulary.Amedment for SingleRecord with Specification Specification for: AMENDMENT_DCTYPE_STANDARDIZED"

**bdqffdq:Specification**. For AMENDMENTs: A urn in the form of "urn:uuid:GUID" that points to the Specification label, for example "urn:uuid:825f551a-2adf-4509-9f95-5a42601a8e88"

**Specification label**. A descriptive label for the specification of an AMENDMENT, for example "Specification for: AMENDMENT_LICENSE_STANDARDIZED"
--->

## 2 Normative Guidance

See the [landing page](../../bdqcore/index.md) for normative guidance on the use of bdqcore terms.

### 2.1 RFC 2119 Keywords (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 3 Term Indices
