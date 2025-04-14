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

**Comment**<br>
{comment}

{toc}

## 1 Introduction

### 1.1 Purpose

The purpose of this document is to list and describe the terms that define the BDQ Core Tests, each represented as a term in the `bdqcore:` namespace. This document provides normative values and explanations for the properties used to describe each Test, including its label, expected input, outputs, parameters, and relationships to Use Cases and quality dimensions.

The Tests defined here are intended to be modular and interoperable. They can be combined into Profiles tailored to particular data quality needs or assessment goals. Each Test is specified independently to support implementation flexibility, but all Tests are grounded in the principles of fitness for use as described in the BDQ Core framework.

### 1.2 Audience

This document is intended for users who need to understand the detailed structure and semantics of the BDQ Core Tests. It is particularly useful for:

- Software developers implementing or integrating BDQ Core Test logic into applications;
- Data managers and curators reviewing or selecting appropriate Tests for assessing data quality;
- Standards developers and information architects building upon the BDQ Core framework;
- Anyone requiring detailed, machine-readable specifications of the Tests used in BDQ Core.

Familiarity with RDF vocabularies, Darwin Core, and fitness for use principles will help readers make full use of this document, though the structure and examples are designed to support a broad technical audience.

### 1.3 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality Core](../../index.md) page, which lists the parts of the standard.

### 1.4 Term List Distributions

<!--- This same table appears in bdqcore_landing_header. Edit here, edit there. --->
| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | TBD | [BDQ Core Tests and Assertions List of Terms](../docs/list/bdqcore/index.md) | Complete term list for the bdqcore: vocabulary as a web page. | 
| RDF/XML file | TBD | [Tests in RDF/XML](../dist/bdqcore.xml) | An RDF representation of the Tests in an RDF/XML serialization. | 
| Turtle file | TBD | [Tests in Turtle](../dist/bdqcore.ttl) | An RDF representation of the Tests in a Turtle serialization. | 
| JSON-LD file | TBD | [Tests in JSON/LD](../dist/bdqcore.json) | An RDF representation of the Tests in a JSON-LD serialization. | 
| CSV file | TBD | [Tests in CSV](../vocabulary/bdqcore_term_versions.csv) | CSV file listing all of the Tests. | 
| SingleRecord Test CSV file | TBD | [SingleRecord Tests in CSV](../dist/bdqcore_singlerecord_tests_current.csv) | CSV file listing just the SingleRecord Tests. |
| MultiRecord Test CSV file | TBD | [MultiRecord Tests in CSV](../dist/bdqcore_multirecord_tests_current.csv) | CSV file listing just the MultiRecord Tests. |

### 1.5 Status of the Content of this Document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.9 Key to Vocabulary Terms](#19-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

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
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| dwciri:      | http://rs.tdwg.org/dwc/iri/                 |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.8 Test Types (non-normative)

There are four types of BDQ Core Tests: Validations, Issues, Amendments and Measures. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into Test suites (bdqffdq:Policies) that assess the fitness for use of data for a specific use.

**Validation Tests** can be thought of as fact-checking. They compare the data against known standards or rules. Validation Tests examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a Criterion for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe) where dwc:countryCode is checked against a Source Authority for validity.

**Issue Tests** can be thought of as warning flags. They don't necessarily mean the data are wrong, but they highlight something that might be a problem for some users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) alerts users to a NotEmpty value that should be examined against their data quality needs. 

**Amendment Tests** can be thought of as suggestions for improvement. Amendment Tests examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and may propose changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350), where a valid ISO country code could be inferred.

**Measure Tests** can be thought of as metrics. Measure Tests either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](https://rs.tdwg.org/bdqcore/terms/453844ae-9df4-439f-8e24-c52498eca84a), which returns the number of Tests of Type Validation that had a response of "NOT_COMPLIANT" on a record.

### 1.9 Key to Vocabulary Terms

These "Test Descriptors" are terms that are necessary to comprehensively describe each Test. Some terms, such as those labeled `Term Version IRI (rdf:about)`, `Term IRI (dcterms:isVersionOf)` and `Term Name (rdf:value)` are intended for machine consumption. Some terms such as the `Description (rdfs:comment)` are designed to be human-readable and to be understood by consumers of biodiversity data quality reports. Terms such as the `Specification (bdqffdq:Specification)` ensure that implementers have no ambiguity about how the Test should be coded.

Terms used to describe the terms in this vocabulary follow the guidance of the [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/). Term definitions include the definition of the underlying RDF vocabulary term, and may include a TDWG-specific meaning from the SDS, and may also include a specific definition in this local context. See section [2.4.1 Listing Identifiers for Tests](../../supplement/index.md#241-Listing-Identifiers-for-Tests) in [BDQ Core Supplemental Information](../../supplement/index.md) for a competency question clarifying the relationships among `Term Version IRI`, `Term IRI`, `Term Name`, and `Label`.

{term_key}

## 2 Normative Guidance

See [BDQ Core Tests and Assertions](../../bdqcore/index.md) for normative guidance on the use of BDQ Core terms.

## 3 Term Indices
