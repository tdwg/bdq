<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Core User's Guide

Title
: BDQ Core User's Guide

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Abstract
: This document is a reference for the (Draft) BDQ Core Standard, describing the BDQ Core tests for consumers of data quality reports produced from the BDQ Core tests.

Authors:
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core User's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2024-09-10>

Draft Standard for Submission

### Table of Contents ###

- [1 Introduction](#1-introduction)
- [1.1 Purpose](#11-purpose)
- [1.2 Audience](#12-audience)
- [1.3 Associated Documents](#13-associated-documents)
- [1.4 Status of the content of this document](#14-status-of-the-content-of-this-document)
- [1.5 RFC 2119 key words](#15-rfc-2119-key-words)
- [2 A Guide to the Tests](#2-a-guide-to-the-tests)
- [2.1 Test Types (non-normative)](#21-test-types-non-normative)
- [2.2 Test Inputs and Outputs](#22-test-inputs-and-outputs)
- [2.2.1 Inputs to Tests (non-normative)](#221-inputs-to-tests-non-normative)
- [2.2.2 Data Quality Reports (non-normative)](#222-data-quality-reports-non-normative)
- [2.2.2 Responses From Tests (normative)](#222-responses-from-tests-normative)
- [2.2.3 Responses From Different Types of Test (normative)](#223-responses-from-different-types-of-test-normative)
- [2.3 Amendments Propose Changes (normative)](#23-amendments-propose-changes-normative)
- [2.4 Test Parameters (normative)](#24-test-parameters-normative)
- [2.4.1 Test Parameters Example (non-normative)](#241-test-parameters-example-non-normative)
- [3 Context for Quality, Uses and Purposes (non-normative)](#3-context-for-quality,-uses-and-purposes-non-normative)
- [4 Using the BDQ Core Quick Reference Guide (non-normative)](#4-using-the-bdq-core-quick-reference-guide-non-normative)
- [5 Time and TimeZones (non-normative)](#5-time-and-timezones-non-normative)


## 1 Introduction

This document describes how consumers of BDQ Core data quality reports can interpret the content of those reports.  

### 1.1 Purpose

This is a users guide to the BDQ Core tests and assertions that they make.

### 1.2 Audience

This document is for consumers of data quality reports.

### 1.3 Associated Documents

- The [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) provides a brief summary of the tests in BDQ Core
- The [BDQ Core Introduction](../../intro/index.md) provides an introduction to the BDQ Core standard and the tests
- The [BDQ Core Implementer's Guide](../implementers/index.md) provides a more detailed view for those seeking to implement BDQ Core

### 1.4 Status of the content of this document

Each sections of this document is marked as normative or non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 2 A Guide to the Tests

BDQ Core defines a set of tests to assess the quality of biodiversity data.  Implementations of these tests may produce data quality reports.  The format of such data quality reports may vary, but they should contain specific information about outputs from each test.  This guide describes the tests, their inputs, expectations about their outputs, how they may be used for Quality Control and Quality Assurance, and describes the quick reference guide that gives the details of each BDQ Core test. 

### 2.1 Test Types (non-normative)

There are four types of tests: Validations, Issues, Amendments and Measures. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into test suites (profiles) that assess the fitness for use of data for a specific use.

**Validation Tests** examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a criterion for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe) where dwc:countryCode is checked against a source authority for validity.

**Issue Tests** are like Validations in identifying potential issues in the data that may be problems for some users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) alerts users to a non-empty value that should be examined against their data quality needs. Issues are a 'warning flag' while Validations assert that the data are fit for use or not. 

**Amendment Tests** examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and may propose changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350) where a valid ISO country code could be inferred.

**Measure Tests** either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](https://rs.tdwg.org/bdqcore/terms/453844ae-9df4-439f-8e24-c52498eca84a) that returns the number of tests of Type Validation that had a response of "NOT_COMPLIANT" on a record.

### 2.2 Test Inputs and Outputs

#### 2.2.1 Inputs to Tests (non-normative)

Each Test is defined to take a specific set of input terms (InformationElements, generally [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021)), and then perform some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the BDQ Core Validation, Amendment, and Issue Tests examine a set of Darwin Core terms from a Single Record, e.g. from a single Occurrence record, rather than looking at the input term(s) over multiple records.  

Consider the Test [VALIDATION_EVENTDATE_STANDARD](https://rs.tdwg.org/bdqcore/terms/4f2bf8fd-fc5c-493f-a44c-e7b16153c803), it takes as input the InformationElement dwc:eventDate from a Single Record, and then asks "Is the value of dwc:eventDate a valid ISO date?".  It will then produce a Response describing the conclusion it reached in asking that question for that record.

All of the Validations, Amendments, and Issues currently defined in BDQ Core operate on single records.  Each of these tests takes the values for the specified information elements (e.g. for VALIDATION_EVENTDATE_STANDARD, dwc:eventDate) from a Single Record (e.g. a dwc:Occurrence), and then evaluates those values for that record.  Tests can also operate on a data set (a Multi Record), and examine the values for information elements across the entire data set.  The only Multi Record Tests currently defined in BDQ Core are Measures that take the outputs of single record tests as their inputs and report on the results of those single record tests aggregated across the data set.  The names of these tests all begin with `MULTIRECORD_'. 

#### 2.2.2 Data Quality Reports (non-normative) 

Software that includes implementations of the Tests may produce data quality reports.  The form that such data quality reports may take is not specified by BDQ Core, however, it does specify elements that should be present in such reports.

#### 2.2.2 Responses From Tests (normative) 

Reports SHOULD identify Tests to you using at least the Label (rdfs:Label) for the test class, e.g. [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134).  

Results from each Test MUST be delivered in the form of a Response.status, Response.result, and Response.comment.  Each test produces one Response.   A Response.qualifier may also be included.  

- The Response.status tells you if the Test was able to run.  
- The Response.result tells you the conclusion of the Test if it was able to be run.  Look only to the Response.result to understand if data have quality for some use or not.
- The Response.comment is a brief explanation of why the Test reached the conclusion it did, examine the Response comment first to understand why a Test provided a particular response.
- The optional Response.qualifier MAY provide additional information.

The Response.status MUST NOT be interpreted as a assertion concerning the quality of the data.  

The Response.result MUST be treated as the sole conclusion about data quality made by the Test.  This conclusion MUST be explained in the Response.comment, and MAY be expanded upon in an optional Response.qualifier.

A Response.status="EXTERNAL_PREREQUISITES_NOT_MET" states that the test was looking information up on some remote resource, such as a web service to look up taxon names, which was not available at the time the Test was run.  This Response.status means that if the same Test is run again on the same data at a different time, it may have a different result (e.g. if the web service became available and could be queried).

A Response.status="INTERNAL_PREREQUISITES_NOT_MET" however, means that some aspect of the data itself does not meet the prerequisites for running the Test, such as an empty dwc:eventDate for a Test that evaluates whether the eventDate falls within a particular time span.  If the same Test is run again on the same, unmodified data, the same result is expected.  It is too easy to interpret a Response.status="INTERNAL_PREREQUISITES_NOT_MET" as pointing to some quality problem in the data, and while this may seem so, it is is misleading. Look instead to some Validation Test that specifically makes that evaluation and returns a Response.result="COMPLIANT" or "NOT_COMPLIANT", or some measure that returns a Response.result="COMPLETE" or "NOT_COMPLETE". 

#### 2.2.3 Responses From Different Types of Test (normative) 

Any type of test may have a Response.status of EXTERNAL_PREREQUISITES_NOT_MET or INTERNAL_PREREQUISITES_NOT_MET.  

Validation Tests can have a Response.status of RUN_HAS_RESULT which tells you that the test ran, and the Response.result of the test will be COMPLIANT or NOT_COMPLIANT.

Amendment Tests can have a Response.status of FILLED_IN, AMENDED, or NOT_AMENDED. FILLED_IN tells you that the Amendment is proposing that a value that was empty in the data under test can be filled in with a non empty value.  This proposal will be found in the Response.result. A Response.status="AMENDED" tells you that the Amendment is proposing a change to an existing value, and this proposal will be found in the Response.result.  "NOT_AMENDED" tells you that the prerequisites for running the Amendment were met, but that it did not propose any change to the data.

Measure Tests that return a Response.status of RUN_HAS_RESULT MUST return either a numeric value or either COMPLETE or NOT_COMPLETE.  Measure Tests generally summarize the results of running the Validations and Amendments and in one case provide a numeric value for the length of the period of time represented in the value of dwc:eventDate.  Most Measures in BDQ Core summarize the results of other tests across data sets.  The Test [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53) returns a Response.result containing a number which represents the number of seconds represented the value in dwc:eventDate interpreted as an interval of time.  This Measure can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs.  For example, an event date to at least one day might be need for phenology studies while resolution to at least one year might serve for other purposes.  

Issues Tests with a Response.status of RUN_HAS_RESULT MAY have a Response.result of POTENTIAL_ISSUE or NOT_ISSUE.  Potential issues require a human review. For example, the Test [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) will return a Response.result="POTENTIAL_ISSUE" if dwc:dataGeneralizations contains a value (the value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) will require human review for any Use Case to determine if the data are fit for purpose or not).   An Issue Test that has a Response.result="POTENTIAL_ISSUE" is making an assertion that is the same as a Validation Test reporting a Response.result="NOT_COMPLIANT". Issue Tests approximate the converse of Validation Tests.  The meaning, however, of a Response.result="NOT_ISSUE" is not the same as a Response.result="COMPLIANT" from a Validation Test. NOT_ISSUE means that no issue was detected, not that the data comply with any criteria for fitness, while COMPLIANT explicitly means that the data satisfy some criterion for fitness for some Use Case.  A Response.result="POTENTIAL_ISSUE" has no analog in Validation Tests; it marks the presence of something in the data that SHOULD BE evaluated by a human to determine whether or not the data are fit for their use or not.  For example, one Issue Test in BDQ Core evaluates whether dwc:dataGeneralizations contains any value, if it does, then the Test reports a Response.result="POTENTIAL_ISSUE", meaning that a human will need to evaluate whether the information in dwc:dataGeneralizations indicates that the data in that record have been generalized in a way that makes the data unfit for their purpose.  See [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2).  

### 2.3 Amendments Propose Changes (normative)

Amendment Tests **propose changes** to data.  It is up to the consumers of data quality reports to choose whether or not to accept those changes, particularly into authoritative databases of record.  Consumers of data quality reports MAY choose to change data based on assertions made by Amendment Tests, or consumers of data quality reports MAY choose to not change their data based on assertions made by Amendment Tests.  Databases of record SHOULD NOT automatically alter data based on assertions made by Amendment Tests without human evaluation.   

### 2.4 Test Parameters (normative) 

Some Tests are parameterized.  When a Test is Parameterized, and a value other than the default value is used for some Parameter, reports SHOULD identify the Tests to you using at least the Label (rdfs:Label) for the Test class, in combination with the Parameter and the value of the argument that replaced the Parameter in this specific case.

Values of parameters other than the defaults SHOULD also be present in the Response.comment.

More normative guidance can be found in the [implementer's guide](../implemeters/index.md#61-Parameters-and-Changing-the-Behavior-of-a-Test-normative).

### 2.4.1 Test Parameters Example (non-normative) 

For example, a test with a non-default parameter value is used, this should be represented with at least the Label (rdfs:Label) for the Test class, e.g. [VALIDATION_MINDEPTH_INRANGE](https://rs.tdwg.org/bdqcore/terms/04b2c8f3-c71b-4e95-8e43-f70374c5fb92) in combination with the Parameter (e.g. bdq:maximumValidDepthInMeters) and the value of the argument that replaced the Parameter in this specific case (e.g. 1642), thus: 

	VALIDATION_MINDEPTH_INRANGE with bdq:maximumValidDepthInMeters=1642

This should be accompanied by a Response.comment that includes text expressing something similar to "Non-default bdq:maximumValidDepthInMeters=1642".

So, a value of dwc:minimumDepthInMeters of 2000m would be NOT_COMPLIANT in this case; while with the default value for that parameter it would be COMPLIANT.

## 3 Context for Quality, Uses and Purposes (non-normative)

Data does not have quality in the abstract, it only has quality with respect to some use.  The [bdqffdq:](../bdqffdq/index.md) Framework for data quality used in BDQ Core, describes uses for data as Use Cases, and expects that tests are run in suites that form policy for data quality with respect to Use Cases.  That is, sets of tests are expected to be run together in order to assess quality of data for some specified use, and reports of results from test should be understood within the context of that use for the data.

Tests for data quality may serve two purposes, Quality Control and Quality Assurance.  In Quality Control, tests are used to find data that lacks fitness for particular uses and the results are used to improve the quality of the data.  In Quality Assurance, data are filtered so that only data that are fit for some purpose are used for that purpose.

The Fitness for use Framework (Veiga 2016, Veiga et al., 2017) provides a formal means for filtering records for [Quality Assurance](../../bdqffdq/index.md#5-Fitness-For-Use-Framework-Summary-of-Mathematical-Formalization-normative) (involving only Measures), but informally, data may be thought as being fit for some use if all Validation Tests comprising that Use Case have a Response.result="COMPLIANT", and all non-numeric Measure Tests comprising that Use Case have a Response.result="COMPLETE".  The BDQ Core Tests include a set of MultiRecord Measures who's purpose is to enable formal filtering (for Quality Assurance) and reporting (for Quality Control) under the Framework Ontology (bdqffdq:).

#5-Fitness-For-Use-Framework-Summary-of-Mathematical-Formalization-normative

The Framework provides a formal statement of [Quality Control](../../bdqffdq/index.md#5-Fitness-For-Use-Framework-Summary-of-Mathematical-Formalization-normative) but the application of Quality Control 'in the wild' is more nuanced, and is more complex than simple filtering under Quality Assurance.  The context of Quality Control may affect how Tests and their results are applied to data, information systems, and processes.

Quality Control is most efficient at the time of data capture where the prevention of incorrect values avoids subsequent far less efficient issue detection and correction. Issues such as transposition of values are far easier to detect and correct at the point of recording than during subsequent downstream processing where context may be lost or held on paper records remote from data entry, and errors may be propagated.  Validation Tests may be though of as framing constraints to impose on data entry interfaces, such as validation of data against a controlled vocabulary being imposed by the presentation of the controlled vocabulary as a pick list in a user interface, or may be implemented as checks on entered data values with immediate feedback for users. 

When data quality reports result from analysis of data in databases of record, numerous validation failures are likely, particularly in historical data where data values may be poorly know, or data may have passed through multiple life cycles of collection management systems.  In a data base of record, the focus of quality control processes is very likely on identifying tractable targeted data cleanup projects.  Data cleanup projects can involve multiple staff with different skills and are likely to last for long periods of time.  Data cleaning projects are expensive, and data quality reports driven by Tests organized by Use Cases can be a management tool for identifying and prioritizing suitable and tractable projects for data cleanup. 

Complicating the analysis of data quality reports on databases of record is that when relational database tables are denormalized to flat files for analyses and reporting, propagated errors could trace back to a single 'point of failure'.  What appear in reports as large numbers of errors may result from a single problem in a single record of a relational table.  A clear understanding of the structure of a database of record is needed to interpret data quality reports into targeted data cleanup projects.   The keys for applying data quality reports to improvement of data in databases of record is identification of focused areas for data cleanup projects, and identification of places where data quality problems may be reduced by improvements to workflow processes or user interfaces for entry and manipulation of data.  Some validations may point to places where controlled vocabularies should be in use but are not, pointing to a need for a coordinated set of changes (for example splitting a single free text field into a controlled vocabulary field and a free text field for further elaboration, a data cleanup project to map all existing values onto a controlled vocabulary, and then changes to user interface to reflect the split into a controlled field and associated remarks.

Correcting issues subsequent to data capture introduces further complexities in that any amendment to existing values requires careful human evaluation and a forking of data records to maintain original data, and an audit trail. Data cleaning often requires far more time than data analysis.

When performing Quality Control when preparing data for aggregation, or when reports are provided by aggregators to upstream data providers, analysis of reports may reveal simple errors introduced in mapping data onto Darwin Core terms, such as field transpositions in mapping in addition to underlying problems in the data.  Validation, particularly at this step may reveal cases where the a database of record holds more authoritative information than an upstream resource relied upon by the aggregator (or a source authority for a test), and is correct despite NOT_COMPLIANT Validation results.  Careful analysis of data quality control results is needed, again with a need to identify focused areas for data cleanup projects, as they involve significant work effort.  

Quality Control to improve data during downstream analysis of aggregated data has other challenges.  The volume of aggregated data may be large enough to make both examination of the proposal of Amendments and reporting of proposed changes to upstream databases of record infeasible.  Quality Control in the workflow processing of data streams from large scale aggregation may include acceptance of proposals from Amendments into a data stream for downstream analysis.  This should be done with some care in checking that the proposed amendments are not introducing errors or false precision, and both unamended and amended data should be preserved, with accepted proposals from amendments clearly identifiable as manipulations of the data stream.  

## 4 Using the BDQ Core Quick Reference Guide (non-normative)

The [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) is a companion to this Guide and lists the tests by a subset of Test Descriptors. This subset is intended to provide a quick summary of the nature of each of the Tests. Some Test Descriptors can be used to filter the Tests down to those that may be applicable for an application.  An index is provided for each Test by example UseCase.  Both SingleRecord Tests (Validations, Amendments, Issues, Measures) and MultiRecord tests (at this time only Measures that evaluate the output of SingleRecord Validations across a data set) are included.  

While the [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) provides a description each individual Test, data Quality Reports may vary in how they present results from the execution of tests, including displaying test results individually, aggregating counts of results for each test run over all records in a data set, and separating results into pre- and post-amendment phases.  In the latter case, results may be shown for all Validation and Measure Tests run in a pre-amendment phase, then proposals for changes from all Amendment Tests run in an amendment phase, and then results from the same Validation and Measure Tests run in a post-amendment phase as if all proposed changes from the Amendment Tests were evaluated and accepted.  It is thus important to identify both the Test for which results are being reported, and the context for the report.  The Quick Reference Guide describes what each Test does independent of this context.

For each Test, the [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) lists ways to identify the Test (**Label:** the brief human readable means for identifying a Test; **skos:prefLabel:** A human readable label spelled out in words; **Versioned IRI:** the means for software to identify the Test).  For each Test, the guide identifies whether the Test operates on SingleRecords or a MultiRecord (a data set).  A brief description follows of what the Test is intended to do, with a more detailed description for implementers (consisting of Specification, InformationElements ActedUpon and Consulted, any Parameters that could change the behavior of the Tests, default values for any bdq:sourceAuthority consulted by the Test or other parameters).  

Two examples of Test data input and output are provided to illustrate opposing behaviors of the Test. For Validation Tests, one example provides a Response.result="COMPLIANT", the other of "NOT_COMPLIANT".  See the [BDQ Core Implementer's Guide](../implementers/index.md)  for information about Test validation data. 

Each Test lists UseCases describing data quality needs to which each Test is applicable. Notes provide additional guidance for understanding test results and for implementation.  

The definitions of the terms used for the tests can be found at [Terms in bdqcore: Quick Reference Guide](../../terms/bdqcore/bdqcore_qrg_term_descriptions.md).

## 5 Time and TimeZones (non-normative)

Time is not considered in any of the BDQ Core Tests.  There are Use Cases where time zone data is important. Dates within a dataset (bdqffdq:MultiRecord) aggregated from multiple sources may have plus or minus one day errors introduced.  New Tests are required if ignorance of time would make such data unfit for purpose.  For further information, see Section [4.2 Time](../../supplement/index.md#42-Time) in the supplement.

## Acronyms

For a list of Acronyms see [Acronyms](../../intro/index.md#5-acronyms) in the Introduction document.

## Glossary

A glossary of terms additional to those in the various namespaces can be found at [Glossary](../../intro/index.md#6-glossary) in the Introduction document.

## References

The bibliography for BDQ Core is in the [References](../../references/index.md#2-references) document.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core User's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


