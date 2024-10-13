<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Biodiversity Data Quality (BDQ) Core: Identifying Synthetic and Modified Data

Title
: Biodiversity Data Quality (BDQ) Core: Identifying Synthetic and Modified Data

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Abstract
: This document is a standard for the marking of synthetic and modified biodiversity data to allow users of biodiversity data to identify and exclude modified and synthetic data from analysies and other uses.

Authors:
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Biodiversity Data Quality (BDQ) Core: Identifying Synthetic and Modified Data. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2024-09-10>

Draft Standard for Submission

### Table of Contents ###


- [1 Introduction](#1-introduction)
- [1.1 Audience](#11-audience)
- [1.2. Status of the content of this document](#12-status-of-the-content-of-this-document)
- [1.3 RFC 2119 keywords](#13-rfc-2119-keywords)
- [2 Synthetic and Example Data](#2-synthetic-and-example-data-)
- [2.1 Identifying example data (normative)](#21-identifying-example-data-(normative))
- [2.2 Data Fragments and Occurrence Data Sets (normative)](#22-data-fragments-and-occurrence-data-sets-(normative))
- [2.2.1 BDQ Core validation data (informative)](#221-bdq-core-validation-data-(informative)-)
- [2.3 Real data used as examples. (normative)](#23-real-data-used-as-examples-(normative))
- [2.4  Real data with synthetic modifications used as examples: (normative)](#24--real-data-with-synthetic-modifications-used-as-examples-(normative))
- [2.5 Wholly Synthetic Data (normative)](#25-wholly-synthetic-data-(normative))



# 1 Introduction

## 1.1 Audience

This document is designed for creators of data sets for the validation of implementations of BDQ Core tests, to see how to mark their data, and for aggregators and users of biodiversity data, to identify criteria for excluding synthetic or modified data from their pipelines . 

## 1.2. Status of the content of this document

All sections of this document are non-normative unless explicitly noted as normative.

## 1.3 RFC 2119 keywords

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

# 2 Synthetic and Example Data 

Implementors of BDQ Core tests, and other tests of biodiversity data quality may wish to use data sets containing known errors and issues for the purposes of testing the behavior of their test implementations and to validate that those test implementations perform as expected.  To do so, they may wish to create modified example data or synthetic data into which known errors have been introduced (and then see if test implementations correctly identify those errors).  To reduce the risk of such modified or synthetic data being mingled with actual biodiversity data in analysies, it is important to mark such data in a consistent manner known to consumers of such data.

## 2.1 Identifying example data (normative)

Data sets consisting of partly or wholly synthetic data, including data sets into which errors have been deliberately introduced may be used to test, validate, and demonstrate the operation of implementations of data quality tests.  It is important that such synthetic and modified data not become conflated with actual biodiversity data in analyses.  The following processes SHOULD be followed to identify original, modified, and synthetic example biodiversity data.

## 2.2 Data Fragments and Occurrence Data Sets (normative)

Inputs to unit tests and testing frameworks for individual test implementations are likely to be organized as fragments of Occurrence data not easily mistaken for actual occurrence data.  A record forming a fragment of an Occurrence record for validating the behaviour of the implementation of a particular test SHOULD only contain the set of terms that form the Information Element for a particular test, along with test parameters, expected outputs, and related metadata, and SHOULD_NOT contain values in other Darwin Core terms not relevant to the test under consideration, except data fragments MAY be marked as synthetic by adding the term values described in 6.6.3 and 6.6.4  Testing frameworks MAY take as input more complete Darwin Core records, and when these are partly or wholly synthetic, they MUST be identified as synthetic, and MUST be treated as synthetic by consumers of Occurrence data.

## 2.2.1 BDQ Core validation data (informative) 

BDQ Core includes two data sets for the validation of test implemetations.  These are sparsely populated data fragments unlikely to be mistaken for real data, and are not marked. 

  - File: [Test Validation Data](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/implementers/TG2_test_validation_data.csv "Test validation data csv file")
  - File: [Test Validation Data for non-printing characters](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/implementers/TG2_test_validation_data_nonprintingchars.csv "Test validation data csv file for testing implementations of EMPTY, containing non-printing characters")

## 2.3 Real data used as examples. (normative)

Use the values in the original source, without modification except:  If no dwc:datasetID is provided, a value for dwc:datasetID MAY be added, this SHOULD be the doi of the source data set in which the example record was found.   

## 2.4  Real data with synthetic modifications used as examples: (normative)

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

## 2.5 Wholly Synthetic Data (normative)

Wholly Synthetic Data MAY be used.  This is not recommended for entire Occurrence records or entire Occurrence data sets.

A. The data set MUST set values for record level terms to unambiguously mark the record as synthetic.

The data set SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode =  "Synthetic Example"
dwc:collectionID = "urn:uuid:0b1b9546-64aa-446b-bd9c-cbb0eacf4332"

B.  Each modified record MUST provide a GUID for the synthetic record.

dwc:occurrenceID = urn:uuid: + a random type 4 UUID

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Biodiversity Data Quality (BDQ) Core: Identifying Synthetic and Modified Data. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


