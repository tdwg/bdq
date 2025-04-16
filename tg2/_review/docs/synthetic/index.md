<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Core: Identifying Synthetic and Modified Data

**Title**<br>
BDQ Core: Identifying Synthetic and Modified Data

**Date version issued**<br>
2025-04-11

**Date created**<br>
2025-04-11

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

<!--
**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}
-->

**This version**<br>
<https://bdq.tdwg/org/vocabularies/2025-04-11>

**Latest version**<br>
<https://bdq.tdwg/org/vocabularies/>

**Previous version**<br>

**Abstract**<br>
This document is a standard for the marking of synthetic and modified biodiversity data to allow users of biodiversity data to identify and exclude modified and synthetic data from analysies and other uses.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Core: Identifying Synthetic and Modified Data. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2025-04-11>

**Comment**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Audience](#12-audience)
  - [1.3 Associated Documents](#13-associated-documents)
  - [1.4 Status of the content of this document](#14-status-of-the-content-of-this-document)
  - [1.5 RFC 2119 key words](#15-rfc-2119-key-words)

[2 Synthetic and Example Data (normative)](#2-synthetic-and-example-data-normative)
  - [2.1 Identifying Example Data (normative)](#21-identifying-example-data-normative)
  - [2.2 Data Fragments and Occurrence Datasets (normative)](#22-data-fragments-and-occurrence-datasets-normative)
  - [2.3 Real Data Used as Examples (normative)](#23-real-data-used-as-examples-normative)
  - [2.4 Real Data with Synthetic Modifications Used as Examples (normative)](#24-real-data-with-synthetic-modifications-used-as-examples-normative)
  - [2.5 Wholly Synthetic Data (normative)](#25-wholly-synthetic-data-normative)

[3 BDQ Core Validation Data (non-normative)](#3-bdq-core-validation-data-non-normative)

[Acronyms](#acronyms)

[Bibliography](#bibliography)

[Cite BDQ Core](#cite-bdq-core)

## 1 Introduction

### 1.1 Purpose

The purpose of this document is to provide guidance for marking and identifying synthetic or modified biodiversity data that has been created for the purpose of validating BDQ Core Test implementations. It establishes conventions for distinguishing such artificial or altered data from authentic biodiversity occurrence records, ensuring that validation datasets are not unintentionally incorporated into biodiversity analyses or downstream data pipelines.

The document specifies how to explicitly mark validation data, including wholly synthetic records, real-world data with synthetic modifications, and real data reused for illustrative or example purposes. These practices support the integrity of analytical results and uphold trust in biodiversity data platforms.

### 1.2 Audience

This document is intended for two primary audiences:

- **Dataset creators** preparing synthetic or modified datasets to test or validate BDQ Core Test implementations, who need to mark those datasets appropriately;
- **Aggregators and data consumers**, including biodiversity researchers and system integrators, who need to recognize and exclude synthetic or altered data to avoid contaminating biodiversity analyses.

The document assumes a working familiarity with biodiversity data concepts, but no prior knowledge of BDQ Core Test internals is required.

### 1.3 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality (BDQ) Core](../../index.md) page, which lists the parts of the standard.

### 1.4 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

Section 3 is non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## 2 Synthetic and Example Data (normative)

Implementers of BDQ Core Tests, and other tests of biodiversity data quality may wish to use datasets containing known errors and issues for the purposes of testing the behavior of their test implementations and to validate that those test implementations perform as expected. To do so, they may wish to create modified example data or synthetic data into which known errors have been introduced (and then see if test implementations correctly identify those errors). To reduce the risk of such modified or synthetic data being mingled with actual biodiversity data in analyses, such data SHOULD BE marked in a consistent manner known to consumers of such data.

### 2.1 Identifying Example Data (normative)

Datasets consisting of partly or wholly synthetic data, including datasets into which errors have been deliberately introduced, may be used to test, validate, and demonstrate the operation of implementations of data quality tests. It is important that such synthetic and modified data not become conflated with actual biodiversity data in analyses. The following processes SHOULD be followed to identify original, modified, and synthetic example biodiversity data.

### 2.2 Data Fragments and Occurrence Datasets (normative)

Inputs to unit tests and testing frameworks for individual test implementations are likely to be organized as fragments of Occurrence data not easily mistaken for actual Occurrence data. A record forming a fragment of a dwc:Occurrence record for validating the behaviour of the implementation of a particular Test SHOULD only contain the set of terms that form the Information Element for a particular Test, along with Test parameters, expected outputs, and related metadata, and SHOULD NOT contain values in other [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) not relevant to the Test under consideration, except data fragments MAY be marked as synthetic by adding the term values described in 6.6.3 and 6.6.4. Testing frameworks MAY take as input more complete Darwin Core records, and when these are partly or wholly synthetic, they MUST be identified as synthetic, and MUST be treated as synthetic by consumers.

### 2.3 Real Data Used as Examples (normative)

Use the values in the original source, without modification except, if no dwc:datasetID is provided, a value for dwc:datasetID MAY be added. This SHOULD be the doi of the source dataset in which the example record was found.

### 2.4 Real Data with Synthetic Modifications Used as Examples (normative)

A. The dataset MUST set values for record level terms to unambiguously mark the record as modified.

The dataset SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual Occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode = "Modified Example"
dwc:collectionID = "urn:uuid:1887c794-7291-4005-8eee-1afbe9d7814e"

B. Each modified record MUST provide a identifier for the modified record distinct from the original identifier. For example,
 			
dwc:occurrenceID = urn:uuid: + a random type 4 UUID.

C. Each dwc:Occurrence record SHOULD include [ResourceRelationship](https://dwc.tdwg.org/terms/#resourcerelationship) terms in the modified example pointing at the original source. For example,

dwc:relatedResourceID = the identifier (e.g., dwc:occurrenceID) for the original source record.

dwc:relationshipOfResource = “source for modified example record”

dwc:relationshipRemarks: Structured data specifying the original values for institutionID, institutionCode, collectionCode, collectionID, and occurrenceID, the doi for the dataset the original example record was found in, a list of the modifications made to the original record, and potentially, a list of standard Tests and expected Test results that this example illustrates.

### 2.5 Wholly Synthetic Data (normative)

Wholly synthetic data MAY be used. This is not recommended for entire dwc:Occurrence records or entire dwc:Occurrence datasets.

A. The dataset MUST set values for record level terms to unambiguously mark the record as synthetic.

The dataset SHOULD use the following values, and consumers MUST treat these values as not representing actual Occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode = "Synthetic Example"
dwc:collectionID = "urn:uuid:0b1b9546-64aa-446b-bd9c-cbb0eacf4332"

B. Each modified record MUST provide an identifier for the synthetic record. For example,

dwc:occurrenceID = urn:uuid: + a random type 4 UUID

## 3 BDQ Core Validation Data (non-normative) 

BDQ Core includes two datasets for the validation of Test implementations. These are sparsely populated data fragments unlikely to be mistaken for real data, and are not marked. 

  - File: [Test Validation Data](../guide/implementers/TG2_test_validation_data.csv "Test Validation Data CSV file")
  - File: [Test Validation Data for non-printing characters](../guide/implementers/TG2_test_validation_data_nonprintingchars.csv "Test Validation Data CSV file for testing implementations of bdq:Empty, containing non-printing characters")

## Acronyms

For a list of Acronyms see [5. Acronyms](../intro/index.md#5-acronyms) in the Introduction document.

## Bibliography

The bibliography for BDQ Core is in the [Bibliography](../references/index.md#2-bibliography) document.

## Cite BDQ Core

**To cite BDQ Core in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite the standard document upon which this page is built, use
the following:**

BDQ Core Maintenance Group 2024. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/bdq/doc/list/

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Core: Identifying Synthetic and Modified Data. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


