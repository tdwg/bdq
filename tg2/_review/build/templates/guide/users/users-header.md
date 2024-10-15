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

# 1 Introduction

This users guide describes how consumers of data quality reports can interpret the content of those reports.  

See also the [Implementer's Guide](BDQ_Core_Implementers_guide.md) for those writing sofware to implement the tests.

Purpose
: This is a users guide to the BDQ Core tests and assertions that they make.

### 1.1 Target Audience

This document is for consumers of data quality reports.

### 1.2 Status of the content of this document

Each sections of this document is marked as normative or non-normative.

### 1.3 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 2 A Guide to the Tests

## 2.1 Kinds of Tests and what they do (non-normative)

TThere are four types of tests: Validations, Issues, Amendments and Measures. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into test suites (profiles) that assess the fitness for use of data for a specific use.

**Validation Tests** examine the values of one or more Darwin Core terms (https://dwc.tdwg.org/list/) against a criterion for quality. An example is VALIDATION_COUNTRYCODE_STANDARD where dwc:countryCode is checked against a source authority for validity.

**Issue Tests** are like Validations in identifying potential issues in the data that may be problems for all users. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY alerts users to a non-empty value that should be examined against their data quality needs. Issues are a 'warning flag' while Validations assert that the data are fit for use or not. 

**Amendment Tests** examine the values of Darwin Core terms to identify potential changes to improve the quality. An example is AMENDMENT_COUNTRYCODE_STANDARDIZED where a valid ISO country code could be inferred.

**Measure Tests** either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is MEASURE_VALIDATIONTESTS_NOTCOMPLIANT that returns the number of tests of Type Validation that had a response of "NOT_COMPLIANT".

## 2.2 Test inputs and outputs

### 2.2.1 Inputs to a test (non-normative)

Each test is defined to take a specific set of input terms (InformationElements, generally Darwin Core terms), and then perform some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the Validations, Amendments, and Issues currently defined in BDQ Core examine a set of Darwin Core terms from a single record, e.g. from a single Occurrence record, rather than looking at the input term(s) over multiple records.  

Consider the test VALIDATION_EVENTDATE_STANDARD, it takes as input the InformationElement dwc:eventDate from a single record, and then asks "Is the value of dwc:eventDate a valid ISO date?".  It will then produce a Response describing the conclusion it reached in asking that question for that record.

## 2.2.2 Parts of a Response from a test. (normative) 

Reports SHOULD identify tests to you using at least the Label (rdfs:Label) for the test class, e.g. VALIDATION_COUNTRY_FOUND.  

Results from each test MUST be delivered in the form of a Response.status, Response.result, and Response.comment.  Each test produces one Response.   A Response.qualifier may also be included.  

- The Response.status tells you if the test was able to run.  
- The Response.result tells you the conclusion of the test if it was able to be run.  Look only to the Response.result to understand if data have quality for some use or not.
- The Response.comment is a brief explanation of why the test reached the conclusion it did, examine the Response comment first to understand why a test provided a particular response.
- The optional Response.qualifier MAY provide additional information.

The Response.status MUST NOT be interpreted as a assertion concerning the quality of the data.  

The Response.result MUST be treated as the sole conclusion about data quality made by the test.  This conclusion MUST be explained in the Response.comment, and MAY be expaned upon in an optional Response.qualifier.

A Response.status of EXTERNAL_PREREQUISITES_NOT_MET tells you that the test was looking information up on some remote resource, such as a web service to look up taxon names, which was not available at the time the test was run.  This Response.status means that if the same test is run again on the same data at a different time, it may have a different result (e.g. if the web service became available and could be queried).

A Response.status of INTERNAL_PREREQUISITES_NOT_MET, however, means that some aspect of the data itself does not meet the prerequisites for running the test, such as an empty dwc:eventDate for a test that evaluates whether the eventDate falls within a particular time span.  If the same test is run again on the same, unmodified data, the same result is expected.  It is all to easy to interpret INTERNAL_PREREQUISITES_NOT_MET as pointing to some quality problem in the data, and while this may seem so, it is is misleading to think so, look instead to some Validation that specifically makes that evaluation and returns a Response.result of COMPLIANT or NOT_COMPLIANT, or some measure that returns a Response.result of COMPLETE or NOT_COMPLETE. 

## 2.2.3 Responses from different kinds of test. (normative) 

Validations can also have a Response.status of RUN_HAS_RESULT, this tells you that the test ran, and the result of the test (COMPLIANT or NOT_COMPLIANT) will be found in the Response.result.

Amendments can have a Response.status of either of the prerequisites not met, or FILLED_IN, AMENDED, or NOT_AMENDED.  FILLED_IN tells you that the amendment is proposing that a value that was empty in the data under test can be filled in with a non empty value.  This proposal will be found in the Response.result.  AMENDED tell you that the amendment is proposing a change to an existing value, this proposal will be found in the Response.result.  NOT_AMENDED tells you that the prerequisites for running the amendment were met, but that it did not propose any change to the data.

Measures 

A Measure MUST return either a numeric value or INTERNAL_PREREQUISITES_NOT_MET. Most Measures count the number of Validation or Amendment tests that a specifified Response.Result. MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. 

Issues

Issues result in a Response.status of "RUN_HAS_RESULT" and a Response.status of ISSUE, "POTENTIAL_ISSUE" or "NOT_ISSUE".  Potential issues require a human review. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POSSIBLE_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.   An issue that reports ISSUE is making an assertions that is the same as a Validation reporting a Response.result of NOT_COMPLIANT, in this sense, Issues are the converse of Validations.  The meaning, however, of NOT_ISSUE from an Issue is not the same as COMPLIANT from a Validation.  NOT_ISSUE means that no issue was detected, not that the data comply with any criteria for fitness, while COMPLIANT explicitly means that the data satisify some critierion for fitness for some use.  POTENTIAL_ISSUE has no analog in validations, it marks the presence of something in the data that will need evaluation by a human to determine whether or not the data are fit for their use or not.  One Issue in BDQ Core evaluates whether dwc:dataGeneralizations contains any value, if it does, then it reports POTENTIAL_ISSUE, meaning that a human will need to evaluate whether the information in dwc:dataGeneralizations indicates that the data in that record have been generalized in a way that makes the data unfit for their purpose.  See: [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../bdqcore/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY)  Very few Issues are defined in BDQ Core.

# 2.3 Amendments only propose changes (normative)

Amendments only propose changes to data.  It is up to the consumers of data quality reports to choose whether or not to accept those changes, particularly into authoritative databases of record.  Consumers of data quality reports MAY choose to change data based on assertions made by Ammendments, or consumers of data quality reports MAY choose to not change their data based on assertions made by Amendments.  Databases of record SHOULD NOT automatically alter data based on assertions made by Amendments without human evaluation.   

## 2.4 Test Parameters. (normative) 

Some tests are parameterized. 

When a test is parameterized, and a value other than the default value is used for some parameter, reports SHOULD identify tests to you using at least the Label (rdfs:Label) for the test class, e.g. VALIDATION_MINDEPTH_INRANGE in combination with the parameter (e.g. bdq:maximumValidDepthInMeters) and the value of the argument that replaced the parameter in this specific case (e.g. 1642).

    VALIDATION_MINDEPTH_INRANGE with bdq:maximumValidDepthInMeters=1642  

# 3 Reading the Quick Reference Guide to the tests (non-normative)

The BDQ Core Quick Reference Guide lists the tests by a subset of Descriptors. This subset provides a summary of the nature of each of the tests, and some Descriptors can be used to filter the tests to those that may be applicable to an application.   An index is provided for each test by UseCase.  Both SingleRecord tests (Validations, Amendments, Issues, Measures) and MultiRecord tests (at this time only Measures that evaluate the output of SingleRecord Validations across a data set) are included.  

For each test, the Quick Reference Guide lists ways to identify the test (Label: the brief human readable means for identifying a test; skos:prefLabel: a human readable label spelled out in words; Versioned IRI: the means for software to identify the test).  It is noted whether a test operates on SingleRecords or a MultiRecord (data set).   A brief description of what the test is intended to do is provided, along with a more detailed description for implementors (consisting of Specification, InformationElements ActedIpon and Consulted, any Paramters that could change the behaviour of the tests, default values for any bdq:sourceAuthority consulted by the test or other parameters).  

Two examples are given, each illustrating opposing behaviors of the test. For Validations, one example provides a Response.result of COMPLIANT, the other of NOT_COMPLIANT.  See the implementation guide for information on a larger set of test validation data.   

A list of UseCases describing data quality needs to which each test is seen to be applicable is provided, along with notes that provide additional guidance for understanding test results and for implementation.  

[Quick Reference Guide to the tests](../bdqcore/index.md)

# 4 Time and TimeZone (non-normative)

Time is not considered in any of the bdqcore: test descriptions.  This means that some cases where time zone data is important, dates within a dataset (bdqffdq:MultiRecord) aggregated from multiple sources may have plus or minus one day errors introduced.  If this would make such data unfit for your purposes, you will need to introduce additional tests. 

