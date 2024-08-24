**NOTE** This is a placeholder for the BDQ Core User's Guide

# BDQ Core User's Guide

**Date version issued**  (Draft)

**Date created** (Draft)

**Part of TDWG Standard**

**This version**

**Latest version**

**Previous version**

**Contributors**

**Creator**

TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions).

## Introduction

This users guide describes how consumers of data quality reports can interpret the content of those reports.  

See also the [Implementer's Guide](BDQ_Core_Implementers_guide.md) for those writing sofware to implement the tests.

Each test is intended to examine just one specific aspect of data quality.   Tests are assembled into test suites (profiles) that assess the fitness for use of data for a specific use.


## Kinds of Tests and what they do

A Validation examines specific elements in the data (that is, particular Darwin Core terms) and asks whether those data conform to a single specific criterion for quality.

An Amendment examines specific elements in the data and asks if it can propose changes to improve the quality of the data under a single specific criterion for quality.

Issues are like Validations, but they can identify potential problems in the data that may or may not be problems for all users of the same data. For example, there is a Validation that identifies whether or not dwc:dataGeneralizations contains any value, if it does, then users need to examine the specific statements made and evaluate them against their quality needs.  These are different from Validations which assert that the data are fit for use or not.  

Measures count things.

## Parts of a Response from a test.

Results from each test are delivered in the form of a Response.status, Response.result, and Response.comment.  Each test produces one Response.   A Response.qualifier may also be included.  

The Response.status tells you if the test was able to run. 

The Response.result tells you the conclusion of the test if it was able to be run.

The Response.comment is a brief explanation of why the test reached the conclusion it did, examine the Response comment first to understand why a test provided a particular response.

A Response.status of EXTERNAL_PREREQUISITES_NOT_MET tells you that the test was looking information up on some remote resource, such as a web service to look up taxon names, which was not available at the time the test was run.  This Response.status means that if the same test is run again on the same data at a different time, it may have a different result (e.g. if the web service became available and could be queried).

A Response.status of INTERNAL_PREREQUISITES_NOT_MET, however, means that some aspect of the data itself does not meet the prerequisites for running the test, such as an empty dwc:eventDate for a test that evaluates whether the eventDate falls within a particular time span.  If the same test is run again on the same, unmodified data, the same result is expected.

Validations can also have a Response.status of RUN_HAS_RESULT, this tells you that the test ran, and the result of the test (COMPLIANT or NOT_COMPLIANT) will be found in the Response.result.

Amendments can have a Response.status of either of the prerequisites not met, or FILLED_IN, AMENDED, or NOT_AMENDED.  FILLED_IN tells you that the amendment is proposing that a value that was empty in the data under test can be filled in with a non empty value.  This proposal will be found in the Response.result.  AMENDED tell you that the amendment is proposing a change to an existing value, this proposal will be found in the Response.result.  NOT_AMENDED tells you that the prerequisites for running the amendment were met, but that it did not propose any change to the data.

Measures

Issues

