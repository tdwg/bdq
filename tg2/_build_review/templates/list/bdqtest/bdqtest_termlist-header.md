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

**Status**<br>
{comment}

{toc}

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to list and describe the terms that define the BDQ Tests, each represented as a term in the `bdqtest:` namespace. This document provides normative values and explanations for the properties used to describe each Test, including its label, expected input, outputs, parameters, and relationships to `Use Cases` and quality `Dimensions`.

The Tests defined here are intended to be modular and interoperable. They can be combined into `Profiles` tailored to particular `Data Quality Needs` or assessment goals. Each Test is specified independently to support implementation flexibility, but all Tests are grounded in the principles of fitness for use as described in the Fitness for Use Framework.

### 1.2 Audience (non-normative)

This document is intended for users who need to understand the detailed structure and semantics of the BDQ Tests. It is particularly useful for:

- Software developers implementing or integrating BDQ Test logic into applications
- Data managers and curators reviewing or selecting appropriate Tests for assessing data quality
- Standards developers and information architects building upon the Fitness for Use Framework
- Anyone requiring detailed, machine-readable specifications of the Tests used in the BDQ standard.

Familiarity with RDF vocabularies, Darwin Core, and fitness for use principles will help readers make full use of this document, though the structure and examples are designed to support a broad technical audience.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

The set of information most relevant to the BDQ Tests can be found in the following subset of resources:

- **BDQ Tests and Assertions** - Defines how each Test is modeled using standard vocabulary terms and how it should behave under various conditions. This document.
- [**BDQ Tests Quick Reference Guide**](../../terms/bdqtest/index.md) - Provides a concise, easy-to-read reference about the BDQ Tests.
- **BDQ Tests and Assertions List of Terms** - Provides the complete normative definitions of the BDQ Tests. This document.
  - [**CSV list of BDQ Tests**](../../../dist/bdqtest_singlerecord_tests_current.csv) - A convenience CSV file listing single record Tests.
  - [**CSV term-version file of BDQ Tests**](../../../vocabulary/bdqtest_term_versions.csv) 
  - [**RDF/Turtle Serialization of BDQ Tests**](../../../dist/bdqtest.ttl) 
  - [**RDF/XML Serialization of BDQ Tests**](../../../dist/bdqtest.xml) 
- [**BDQ User's Guide**](../../guide/users/index.md) - For anyone interested in how to use the BDQ Tests in practice.
- [**BDQ Implementer's Guide**](../../guide/implementers/index.md) - For anyone interested in the technical implementation of the BDQ Tests.

### 1.4 Term List Distributions (non-normative)

<!--- This same table appears in bdqtest_landing_header. Edit here, edit there. --->
| Description | IRI | Download URL | Notes | 
| ----------- | --- | -----------  | ----- | 
| HTML file   | TBD | [BDQ Tests and Assertions List of Terms](../../list/bdqtest/index.md) | Complete term list for the `bdqtest:` vocabulary as a web page. | 
| RDF/XML file | TBD | [Tests in RDF/XML](../../../dist/bdqtest.xml) | An RDF representation of the Tests in an RDF/XML serialization. | 
| Turtle file | TBD | [Tests in Turtle](../../../dist/bdqtest.ttl) | An RDF representation of the Tests in a Turtle serialization. | 
| JSON-LD file | TBD | [Tests in JSON/LD](../../../dist/bdqtest.json) | An RDF representation of the Tests in a JSON-LD serialization. | 
| CSV file | TBD | [Tests in CSV](../../../vocabulary/bdqtest_term_versions.csv) | CSV file listing all BDQ Tests. | 
| Single Record Test CSV file | TBD | [Single Record Tests in CSV](../../../dist/bdqtest_singlerecord_tests_current.csv) | CSV file listing just the `Single Record` Tests. |
| Multi Record Test CSV file | TBD | [Multi Record Tests in CSV](../../../dist/bdqtest_multirecord_tests_current.csv) | CSV file listing just the 		`Multi Record` Tests. |

### 1.5 Status of the Content of this Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Section [1.10 Key to Vocabulary Terms (normative)](#110-key-to-vocabulary-terms-normative) identifies which values in Section 4 are normative and which are non-normative.

### 1.6 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| dwciri:      | http://rs.tdwg.org/dwc/iri/                 |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

## 1.8 Use of Terms (normative)

In an RDF context, a reference to a term in the `{pref_namespace_prefix}:` namespace MUST use the Term IRI (e.g., `https://rs.tdwg.org/{pref_namespace_prefix}/terms/b3471c65-b53e-453b-8282-abfa27bf1805`) or Term Qualified name (e.g., `{pref_namespace_prefix}:b3471c65-b53e-453b-8282-abfa27bf1805`).  In a non-RDF context in which resources may be used by software (e.g., a Java method annotation, or a value in a database table), the Term IRI or Term Qualified Name (either the base IRI or the versioned IRI) SHOULD be used. In a non-RDF context in which resources are expected to be read by humans (e.g., a value in a spreadsheet or database table) the Label (`rdfs:label`, e.g., `AMENDMENT_TYPESTATUS_STANDARDIZED`) SHOULD be used. In a purely human context for readability or accessibility, the preferred label (e.g., `Amendment dwc:typeStatus Standardized`) MAY be used.

### 1.9 Test Types (non-normative)

There are four types of BDQ Tests: `Validations`, `Issues`, `Measures` and `Amendments`. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into Test suites (`bdqffdq:Policies`) that assess the fitness for use of data for a specific use (`bdqffdq:UseCase`).

**Validation Tests** can be thought of as fact-checking. They compare the data against known standards or rules. `Validation` Tests examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a `Criterion` for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD) where `dwc:countryCode` is checked against a `sourceAuthority` for validity.

**Issue Tests** can be thought of as warning flags. They don't necessarily mean the data are wrong, but they highlight something that might be a problem for some users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY) alerts users to a `NotEmpty` value that should be examined against their `Data Quality Needs`. 

**Measure Tests** can be thought of as metrics. `Measure` Tests either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT), which returns the number of Tests of Type `Validation` that had a response of "NOT_COMPLIANT" on a record.

**Amendment Tests** can be thought of as suggestions for improvement. `Amendment` Tests examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and may propose changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_STANDARDIZED), where a valid ISO country code could be inferred.

### 1.10 Key to Vocabulary Terms (normative)

These "Test Descriptors" are terms that are necessary to comprehensively describe each Test. Some terms, such as those labeled `Term Version IRI` (`rdf:about`), `Term IRI` (`dcterms:isVersionOf`) and `Term Name` (`rdf:value`) are intended for machine consumption. Some terms such as the `Description` (`rdfs:comment`) are designed to be human-readable and to be understood by consumers of biodiversity `Data Quality Reports`. Terms such as the `Specification` (`bdqffdq:Specification`) ensure that implementers have no ambiguity about how the Test should be coded.

The terminology used to describe the terms in this vocabulary follows the TDWG [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/) (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.
See section [2.4.1 Listing Identifiers for Tests (non-normative)](../../supplement/index.md#241-listing-identifiers-for-tests-non-normative) in [BDQ Supplemental Information](../../supplement/index.md) for a competency question clarifying the relationships among `Term Version IRI`, `Term IRI`, `Term Name`, and `Label`.

{term_key}

## 2 Term Indices (non-normative)
