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

{previous_version_slot}

Abstract
: {abstract}

Authors:
: {authors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}

### Table of Contents ###

{toc}

## 1 Introduction

With tests for data quality comes the need for validation data to test the behavior of test implementations.  It is important that synthetic data created for the purposes of validating the behavior of test implementation, or data representing real occurences that has been modified for that purpose not be conflated with real data in analysies of patterns of biodiversity.  This document explains how the creators of such validation data sets can unambiguosly mark such data for exclusion, and how users can use these markings to exclude such data from analysies.

### 1.1 Purpose

This document specifies the marking and identification of synthetic data as clearly distinguisable from real world occurrences.

### 1.2 Audience

This document is designed for creators of data sets for the validation of implementations of BDQ Core Tests, to see how to mark their data, and for aggregators and users of biodiversity data, to identify criteria for excluding synthetic or modified data from their pipelines. 

### 1.3 Associated Documents

See the introduction to the [BDQ Core Standard](../intro/index.md) for more context.

See the [Implementer's Guide](../guide/implementers/index.md) for discussion of validation of implementations of bdqcore: tests.

### 1.4 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.  

Section 3 is non-normative.

### 1.5 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## 2 Synthetic and Example Data (normative)

Implementors of BDQ Core tests, and other tests of biodiversity data quality may wish to use data sets containing known errors and issues for the purposes of testing the behavior of their test implementations and to validate that those test implementations perform as expected.  To do so, they may wish to create modified example data or synthetic data into which known errors have been introduced (and then see if test implementations correctly identify those errors).  To reduce the risk of such modified or synthetic data being mingled with actual biodiversity data in analysies, such data SHOULD BE marked in a consistent manner known to consumers of such data.

### 2.1 Identifying Example Data (normative)

Data sets consisting of partly or wholly synthetic data, including data sets into which errors have been deliberately introduced may be used to test, validate, and demonstrate the operation of implementations of data quality tests.  It is important that such synthetic and modified data not become conflated with actual biodiversity data in analyses.  The following processes SHOULD be followed to identify original, modified, and synthetic example biodiversity data.

### 2.2 Data Fragments and Occurrence Data Sets (normative)

Inputs to unit tests and testing frameworks for individual test implementations are likely to be organized as fragments of Occurrence data not easily mistaken for actual occurrence data.  A record forming a fragment of an Occurrence record for validating the behaviour of the implementation of a particular test SHOULD only contain the set of terms that form the Information Element for a particular test, along with test parameters, expected outputs, and related metadata, and SHOULD_NOT contain values in other [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) not relevant to the test under consideration, except data fragments MAY be marked as synthetic by adding the term values described in 6.6.3 and 6.6.4  Testing frameworks MAY take as input more complete Darwin Core records, and when these are partly or wholly synthetic, they MUST be identified as synthetic, and MUST be treated as synthetic by consumers of Occurrence data.

### 2.3 Real Data Used as Examples (normative)

Use the values in the original source, without modification except:  If no dwc:datasetID is provided, a value for dwc:datasetID MAY be added, this SHOULD be the doi of the source data set in which the example record was found.   

### 2.4  Real Data with Synthetic Modifications Used as Examples (normative)

A. The data set MUST set values for record level terms to unambiguously mark the record as modified.

The data set SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode =  "Modified Example"
dwc:collectionID = "urn:uuid:1887c794-7291-4005-8eee-1afbe9d7814e"

B. Each modified record MUST provide a new GUID for the modified record distinct from the original GUID.
 			
dwc:occurrenceID = urn:uuid: + a random type 4 UUID.

C. Each Occurrence record SHOULD include resource relationship terms in the modified example pointing at the original source:

dwc:relatedResourceID = the ID (e.g. occurrenceID) for the original source record.

dwc:relationshipOfResource = “source for modified example record”

dwc:relationshipRemarks:  Structured data specifying the original values for institutionID, institutionCode, collectionCode, collectionID, and occurrenceID, the doi for the data set the original example record was found in, a list of the modifications made to the original record, and potentially, a list of standard tests and expected test results that this example illustrates. 

### 2.5 Wholly Synthetic Data (normative)

Wholly Synthetic Data MAY be used.  This is not recommended for entire Occurrence records or entire Occurrence data sets.

A. The data set MUST set values for record level terms to unambiguously mark the record as synthetic.

The data set SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode =  "Synthetic Example"
dwc:collectionID = "urn:uuid:0b1b9546-64aa-446b-bd9c-cbb0eacf4332"

B.  Each modified record MUST provide a GUID for the synthetic record.

dwc:occurrenceID = urn:uuid: + a random type 4 UUID

## 3 BDQ Core Validation Data (non-normative) 

BDQ Core includes two data sets for the validation of test implemetations.  These are sparsely populated data fragments unlikely to be mistaken for real data, and are not marked. 

  - File: [Test Validation Data](../guide/implementers/TG2_test_validation_data.csv "Test validation data csv file")
  - File: [Test Validation Data for non-printing characters](../guide/implementers/TG2_test_validation_data_nonprintingchars.csv "Test validation data csv file for testing implementations of EMPTY, containing non-printing characters")

