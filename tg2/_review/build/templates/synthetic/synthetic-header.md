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

<!--
**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}
-->

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

The purpose of this document is to provide guidance for marking and identifying synthetic or modified biodiversity data that has been created for the purpose of validating BDQ Core Test implementations. It establishes conventions for distinguishing such artificial or altered data from authentic biodiversity occurrence records, ensuring that validation datasets are not unintentionally incorporated into biodiversity analyses or downstream data pipelines.

The document specifies how to explicitly mark validation data, including wholly synthetic records, real-world data with synthetic modifications, and real data reused for illustrative or example purposes. These practices support the integrity of analytical results and uphold trust in biodiversity data platforms.

### 1.2 Audience

This document is intended for two primary audiences:

- **Dataset creators** preparing synthetic or modified datasets to test or validate BDQ Core Test implementations, who need to mark those datasets appropriately;
- **Aggregators and data consumers**, including biodiversity researchers and system integrators, who need to recognize and exclude synthetic or altered data to avoid contaminating biodiversity analyses.

The document assumes a working familiarity with biodiversity data concepts, but no prior knowledge of BDQ Core Test internals is required.

### 1.3 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality Core](../../index.md) page, which lists the parts of the standard.

### 1.4 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

Section 3 is non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## 2 Synthetic and Example Data (normative)

Implementers of BDQ Core tests, and other tests of biodiversity data quality may wish to use datasets containing known errors and issues for the purposes of testing the behavior of their test implementations and to validate that those test implementations perform as expected. To do so, they may wish to create modified example data or synthetic data into which known errors have been introduced (and then see if test implementations correctly identify those errors). To reduce the risk of such modified or synthetic data being mingled with actual biodiversity data in analyses, such data SHOULD BE marked in a consistent manner known to consumers of such data.

### 2.1 Identifying Example Data (normative)

Data sets consisting of partly or wholly synthetic data, including datasets into which errors have been deliberately introduced may be used to test, validate, and demonstrate the operation of implementations of data quality tests. It is important that such synthetic and modified data not become conflated with actual biodiversity data in analyses. The following processes SHOULD be followed to identify original, modified, and synthetic example biodiversity data.

### 2.2 Data Fragments and Occurrence Data Sets (normative)

Inputs to unit tests and testing frameworks for individual test implementations are likely to be organized as fragments of Occurrence data not easily mistaken for actual occurrence data. A record forming a fragment of an Occurrence record for validating the behaviour of the implementation of a particular test SHOULD only contain the set of terms that form the Information Element for a particular test, along with test parameters, expected outputs, and related metadata, and SHOULD NOT contain values in other [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) not relevant to the test under consideration, except data fragments MAY be marked as synthetic by adding the term values described in 6.6.3 and 6.6.4 Testing frameworks MAY take as input more complete Darwin Core records, and when these are partly or wholly synthetic, they MUST be identified as synthetic, and MUST be treated as synthetic by consumers of Occurrence data.

### 2.3 Real Data Used as Examples (normative)

Use the values in the original source, without modification except: If no dwc:datasetID is provided, a value for dwc:datasetID MAY be added, this SHOULD be the doi of the source dataset in which the example record was found. 

### 2.4 Real Data with Synthetic Modifications Used as Examples (normative)

A. The dataset MUST set values for record level terms to unambiguously mark the record as modified.

The dataset SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode = "Modified Example"
dwc:collectionID = "urn:uuid:1887c794-7291-4005-8eee-1afbe9d7814e"

B. Each modified record MUST provide a new GUID for the modified record distinct from the original GUID.
 			
dwc:occurrenceID = urn:uuid: + a random type 4 UUID.

C. Each Occurrence record SHOULD include resource relationship terms in the modified example pointing at the original source:

dwc:relatedResourceID = the ID (e.g., occurrenceID) for the original source record.

dwc:relationshipOfResource = “source for modified example record”

dwc:relationshipRemarks: Structured data specifying the original values for institutionID, institutionCode, collectionCode, collectionID, and occurrenceID, the doi for the dataset the original example record was found in, a list of the modifications made to the original record, and potentially, a list of standard tests and expected test results that this example illustrates. 

### 2.5 Wholly Synthetic Data (normative)

Wholly Synthetic Data MAY be used. This is not recommended for entire Occurrence records or entire Occurrence datasets.

A. The dataset MUST set values for record level terms to unambiguously mark the record as synthetic.

The dataset SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode = "Synthetic Example"
dwc:collectionID = "urn:uuid:0b1b9546-64aa-446b-bd9c-cbb0eacf4332"

B. Each modified record MUST provide a GUID for the synthetic record.

dwc:occurrenceID = urn:uuid: + a random type 4 UUID

## 3 BDQ Core Validation Data (non-normative) 

BDQ Core includes two datasets for the validation of test implemetations. These are sparsely populated data fragments unlikely to be mistaken for real data, and are not marked. 

  - File: [Test Validation Data](../guide/implementers/TG2_test_validation_data.csv "Test Validation Data CSV file")
  - File: [Test Validation Data for non-printing characters](../guide/implementers/TG2_test_validation_data_nonprintingchars.csv "Test Validation Data CSV file for testing implementations of bdq:Empty, containing non-printing characters")
