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

# Table of Contents
{toc}

## 1 Introduction

This document lists the BDQ Core Tests. These are the terms from the namespace `bdqcore:` (the CORE Tests). The description of these terms relies heavily on the [Fitness For Use Framework Ontology List of Terms](../bdqffdq/index.md) (Veiga 2016, Veiga et al. 2017). Terms are also used from the [Data Quality Dimension Controlled Vocabulary List of Terms](../list/bdqdim/index.md) (data quality Dimension from Veiga et al. 2017), [Data Quality Enhancement Controlled Vocabulary List of Terms](../list/bdqenh/index.md) (Test Enhancements), [Data Quality Criterion Controlled Vocabulary List of Terms](../list/bdqcrit/index.md) (Test Criteria), and [BDQ Controlled Vocabulary List of Terms](../list/bdq/index.md) (additional vocabulary terms). For background details see Chapman et al. (2017).

The focus of this standard is the specification of a suite of Tests that operate on single Darwin Core (Wieczorek et al. 2012) encoded records, for example the Test [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe). This (SingleRecord) Test checks the value of dwc:countryCode against the source authority ISO 3166-1-alpha-2 Country Code (which imlementations may access at https://www.iso.org/obp/ui/#search). This standard also includes specifications for MultiRecord Tests that accumulate results of multiple SingleRecord Tests, allowing, for example, a determination that 70% of records in a dataset had a valid dwc:countryCode.

Each Test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other Tests to meet particular data quality needs, and so as not impose any particular model of Test execution on implementation frameworks. Implementations of Test execution frameworks MAY execute Tests in on data records in parallel, on data records in sequence, as queries on datasets, or even on unique values. While the BDQ Core Tests are described in isolation, they MUST be used in sets that are related to a use of the data, as data does not have quality in the abstract, it only has quality with respect to some use. Thus each Test is linked to one or more Use Cases, which are formal descriptions of uses to which data may be put. The bdq: vocabulary defines the set of Use Cases referenced here. BDQ Core Tests can be freely composed in other ways for other uses. Additional Tests can be defined, including those that expand in scope beyond Darwin Core terms.

Tests described here are paired in that all Validation Tests that assesses some aspect of data quality are associated with an Amendment Test that may be able to improve the quality of data with respect to that Validation Test.

### 1.1 Purpose

This document lists the BDQ Core Tests, provides values for the terms that describe these Tests, and provides a brief explanation of those terms.

### 1.2 Audience

Users who need to understand the BDQ Core Tests, including all technical details required by the standard. 

### 1.3 Associated Documents

The bdqcore: vocabulary includes: 

- A [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md) to the BDQ Core Tests.
- This document, a term-list for the vocabulary, containing the vocabulary terms and their metadata.
- A [BDQ Core Tests and Assertions](../bdqcore/index.md) document with normative guidance on the use of the bdqcore vocabulary.

In addition, guides are provided in the form of the [BDQ Core User's Guide](../guide/users/index.md) and the [BDQ Core Implementer's Guide](../guide/implementers/index.md) .

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
