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

Reports SHOULD identify tests to you using at least the skos:prefLabel for the test class, e.g. VALIDATION_COUNTRY_FOUND.  

Results from each test MUST be delivered in the form of a Response.status, Response.result, and Response.comment.  Each test produces one Response.   A Response.qualifier may also be included.  

- The Response.status tells you if the test was able to run. 
- The Response.result tells you the conclusion of the test if it was able to be run.
- The Response.comment is a brief explanation of why the test reached the conclusion it did, examine the Response comment first to understand why a test provided a particular response.
- The optional Response.qualifier MAY provide additional information.

A Response.status of EXTERNAL_PREREQUISITES_NOT_MET tells you that the test was looking information up on some remote resource, such as a web service to look up taxon names, which was not available at the time the test was run.  This Response.status means that if the same test is run again on the same data at a different time, it may have a different result (e.g. if the web service became available and could be queried).

A Response.status of INTERNAL_PREREQUISITES_NOT_MET, however, means that some aspect of the data itself does not meet the prerequisites for running the test, such as an empty dwc:eventDate for a test that evaluates whether the eventDate falls within a particular time span.  If the same test is run again on the same, unmodified data, the same result is expected.

Validations can also have a Response.status of RUN_HAS_RESULT, this tells you that the test ran, and the result of the test (COMPLIANT or NOT_COMPLIANT) will be found in the Response.result.

Amendments can have a Response.status of either of the prerequisites not met, or FILLED_IN, AMENDED, or NOT_AMENDED.  FILLED_IN tells you that the amendment is proposing that a value that was empty in the data under test can be filled in with a non empty value.  This proposal will be found in the Response.result.  AMENDED tell you that the amendment is proposing a change to an existing value, this proposal will be found in the Response.result.  NOT_AMENDED tells you that the prerequisites for running the amendment were met, but that it did not propose any change to the data.

Measures 

A Measure returns a numeric value or INTERNAL_PREREQUISITES_NOT_MET. Most Measures count the number of Validation or Amendment tests that a specifified Response.Result. MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. 

Issues

Issues are a form of warning flag where the test is drawing attention to potential problem with the value of a Darwin Core term for at least one use case. 
Issues result in a Response.status of "RUN_HAS_RESULT" and a Response.status of ISSUE, "POTENTIAL_ISSUE" or "NOT_ISSUE".  Potential issues require a human review. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POSSIBLE_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.  


### Reading the Quick Reference Guide to the tests

The BDQ Core Quick Reference Guide lists the tests by a subset of Descriptors. This subset provides a summary of the nature of each of the tests, and some Descriptors can be used to filter the tests to those that may be applicable to an application.

The following block of text is from the QRG:

**rdfs:Label** [normative]: A brief human-readable label for consumers and implementors using the structure TESTTYPE_INFORMATIONELEMENT_CRITERION e.g. VALIDATION_COUNTRYCODE_STANDARD\
**skos:prefLabel** [normative]: A human readable label that follows the pattern 'Test Type' 'Focus Information Element' 'Criterion'. Example: "Validation dwc:countryCode Standard"\
**Versioned IRI** [normative]:A machine readable unique identifier with a Date Last Updated appended. Example: "0493bcfb-652e-4d17-815b-b0cce0742fb 2024-08-30"\
**Resource Type** [normative]: What record type the tests operate on - 'SingleRecord' or 'MultiRecord'. Example: "bdqffdq:SingleRecord"\
**Description** [non-normative]: A non-technical description of what the test does. Example: "Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?"\
<!--- Darwin Core Class isn't present in the RDF, part of rationale management, not terms --->
<!--- **Information Element Class** [non-normative]: The focus Darwin Core Class. Example: "dwc:Location"\--->
**Specification** [normative]: The concise logic of the test for implementors. Example: "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is EMPTY; COMPLIANT if there is a match of the contents of dwc:scientificName with the bdq:sourceAuthority; otherwise NOT_COMPLIANT"\
**Information Elements ActedUpon** [normative]: For implementors and consumers. A list of Darwin Core terms that are the focus of the test. Example: "dwc:countryCode"\
**Information Elements Consulted** [normative]: A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon. Example: "dwc:country"\
**Parameters** [normative]: Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain. Example: "bdq:taxonIsMarine.\
**Default Parameter Values** [normative]: The default values for any bdq:sourceAuthority and any paramters used in the Specification that define the default behavior of the test. Example: bdq:maximumValidElevationInMeters default = "8850" .\
**Examples** [non-normative]: 'Pass' and 'Fail' examples of inputs and outputs for the test from the Test Validation Data. Example: "[dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in bdq:sourceAuthority"]
[dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in bdq:sourceAuthority"]"\
**Use Cases** [non-normative]: For Consumers and Implementors. Descriptions of data example quality needs that this test helps to support. Example: "bdq:Record-Management", "bdq:alien-species"
**Notes** [non-normative]: For implementors and Consumers. Additional, guidance that may be necessary for the accurate implementation of the tests. Example: "Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters."\


## Amendments only propose changes

Amendments propose changes to data, but it is up to the consumers of data quality reports to choose whether or not to accept those changes, particularly into authoritative databases of record. 

## Time and TimeZone

Time is not considered in any of the bdqcore: test descriptions.  This means that some cases where time zone data is important, dates within a dataset (bdqffdq:MultiRecord) aggregated from multiple sources may have plus or minus one day errors introduced.  If this would make such data unfit for your purposes, you will need to introduce additional tests. 


