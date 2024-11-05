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

# Table of Contents
{toc}

## 1 Introduction

This document lists the BDQ Core Tests. These are the terms from the namespace `bdqcore:` (the CORE Tests).  The description of these terms relies heavily on the [bdqffdq:](../bdqffdq/index.md) data quality Framework Ontology (Veiga 2016, Veiga et al. 2017).  Terms are also used from the namespaces: [bdqdim:](../bdqdim/index.md) (data quality dimension from Veiga et al. 2017), [bdqenh:](../bdqenh/index.md) (test enhancements), [bdqcrit:](../bdqcrit/index.md) (test criteria), and [bdq:](../bdq/index.md) (additional vocabulary terms).  For background details see Chapman et al. (2017).

The focus of this standard is the specifications for a suite of Tests that operate on single Darwin Core (Wieczorek et al. 2012) encoded records, for example the Test  [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe). This (SingleRecord) Test checks the value of dwc:countryCode against the source authority ISO 3166-1-alpha-2 Country Code (which imlementations may access at https://www.iso.org/obp/ui/#search).  This standard also includes specifications for MultiRecord Tests that accumulate results of a SingleRecord Tests, for example allowing determination that 70% of records in a dataset had a valid dwc:countryCode.  

Each Test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other Tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values.  While the BDQ Core Tests are described in isolation, they must be used in sets that are related to a use of the data, as data does not have quality in the abstract, it only has quality with respect to some use.  Thus each Test is linked to one or more UseCases, which are formal descriptions of uses to which data may be put.  The bdq: vocabulary defines the set of use cases referenced here.  BDQ Core Tests can be freely composed in other ways for other uses.  Additional tests can be defined, including those that expand in scope beyond Darwin Core terms.

Tests described here are paired in that all Validation Tests that assesses some aspect of data quality are associated with an Amendment Test that may be able to improve the quality of data with respect to that Validation Test.

### 1.1 Purpose

This document lists the BDQ Core Tests, provides values for the terms that describe these Tests, and provides a brief explanation of those terms.

### 1.2 Audience

Users who need to understand the BDQ Core Tests, including all technical details required in the standard. 

### 1.3 Associated Documents

The bdqcore: vocabulary includes: 

- A [Quick Reference Guide](../terms/bdqcore/index.md) to the BDQ Core Tests.
- This document, a term-list for the vocabulary, containing the vocabulary terms and their metadata.
- A [landing page](../bdqcore/index.md) document with normative guidance on the use of the bdqcore vocabulary.

In addition, A users guide to the use of the BDQ Core Tests is provided in the [BDQ Core User's Guide](../guide/users/index.md) and a guide to implementation of the BDQ Core Tests is provided in the [BDQ Core Implementer's Guide](../guide/implementers/index.md) 

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note |
| ----------- | --- | -----------  | ---- |
| HTML file   | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcore/index.md | Complete term list for the bdqcore: vocabulary  | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.xml | An rdf representation of the Tests in an RDF/XML serialization | 
| Turtle file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.ttl | An rdf representation of the Tests in a Turtle serialization | 
| JSON-LD file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.json | An rdf representation of the Tests in a json-ld serialization | 
| CSV file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqcore_term_versions.csv | CSV file listing the Tests | 
| SingleRecord Test CSV file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore_singlerecord_tests_current.csv | CSV file listing just the SingleRecord tests. |

### 1.5 Status of the Content of this Document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.9 Key to Vocabulary Terms](#19-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix |  IRI |
| ------ |  --- |
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms/               |
| bdqcrit      | https://rs.tdwh.org/bdqcrit/terms/               |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms/                |
| bdqenh       | https://rs.tdwg.org/bdqenh/terms/                |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms/               |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema#            |
| owl          | http://www.w3.org/2002/07/owl#                   |

### 1.8 Types of Tests

There are four types of BDQ Core Tests: Validations, Issues, Amendments and Measures. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into test suites (bdqffdq:Policies) that assess the fitness for use of data for a specific use.

**Validation Tests** examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a criterion for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe) where dwc:countryCode is checked against a source authority for validity.

**Issue Tests** are like Validations in identifying potential issues in the data that may be problems for all users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) alerts users to a non-empty value that should be examined against their data quality needs. Issues are a 'warning flag' while Validations assert that the data are fit for use or not. 

**Amendment Tests** examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) to identify potential changes to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350) where a valid ISO country code could be inferred.

**Measure Tests** either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](https://rs.tdwg.org/bdqcore/terms/453844ae-9df4-439f-8e24-c52498eca84a) that returns the number of Tests of Type Validation that had a response of "NOT_COMPLIANT".

### 1.9 Key to Vocabulary Terms

These "Test Descriptors" (terms used to describe the terms in this vocabulary) are the set of terms that are necessary to comprehensively describe each Test. Some terms, such as the `IRI` and `term_localName` are intended for machine consumption. Some terms such as the `Description` are designed to be human-readable and to be understood by consumers of biodiversity data quality reports. Terms such as the `Specification` ensure that implementers have no ambiguity about how the Test should be coded.

Terms used to describe the terms in this vocabulary follow the guidance of the [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/).  Term definitions include the definition of the underlying RDF vocabulary term, and may include a TDWG specific meaning from the SDS, and may also include specific definition in this local context.

{term_key}

## 2 Normative Guidance

See the [landing page](../../bdqcore/index.md) for normative guidance on the use of bdqcore terms.

## 3 Term Indices
