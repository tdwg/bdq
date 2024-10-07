<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
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

Authors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Contributors
: [Yi-Ming Gan](https://orcid.org/0000-0001-7087-2646) ([Royal Belgian Institute of Natural Sciences](http://www.wikidata.org/entity/Q16665660)), [António Mauro Saraiva](https://orcid.org/0000-0003-2283-1123) ([Universidade de São Paulo](https://www.wikidata.org/wiki/Q835960)), [Alan Koch Veiga](http://orcid.org/0000-0003-2672-8115) ([Universidade de São Paulo](https://www.wikidata.org/wiki/Q835960)), [Paula F Zermoglio](https://orcid.org/0000-0002-6056-5084) ([Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN): San Carlos de Bariloche](https://www.irnad.com/)), [Alexander Thompson](https://orcid.org/0000-0002-8981-4048) ([Google](https://www.wikidata.org/wiki/Q95)), [David Lowery](https://github.com/lowery) , [Christian Gendreau](https://orcid.org/0000-0003-4898-4291) ([Agriculture and Agri-Food Canada](http://www.wikidata.org/entity/Q1046164)), [Tim Roberston](https://orcid.org/0000-0001-6215-3617) ([Global Biodiversity Information Facility](https://www.wikidata.org/wiki/Q1531570)), [Dmitry Schigel](https://orcid.org/0000-0002-2919-1168) ([Global Biodiversity Information Facility](https://www.wikidata.org/wiki/Q1531570)), [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) 

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core User's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2024-09-10>

Draft Standard for Submission


### Table of Contents ###


- [ 1 Introduction](#1-introduction)
- [ 1.1 Kinds of Tests and what they do (non-normative)](#11-kinds-of-tests-and-what-they-do-(non-normative))
- [ 1.2 Inputs to a test ](#12-inputs-to-a-test-)
- [ 1.3 Parts of a Response from a test. (normative) ](#13-parts-of-a-response-from-a-test-(normative)-)
- [ 2 Reading the Quick Reference Guide to the tests (non-normative)](#2-reading-the-quick-reference-guide-to-the-tests-(non-normative))
- [ 2.1 Amendments only propose changes (normative)](#21-amendments-only-propose-changes-(normative))
- [ 2.2 Time and TimeZone (non-normative)](#22-time-and-timezone-(non-normative))



# 1 Introduction

This users guide describes how consumers of data quality reports can interpret the content of those reports.  

See also the [Implementer's Guide](BDQ_Core_Implementers_guide.md) for those writing sofware to implement the tests.

Each test is intended to examine just one specific aspect of data quality.   Tests are assembled into test suites (profiles) that assess the fitness for use of data for a specific use.

## 1.1 Kinds of Tests and what they do (non-normative)

There are four kinds of kinds of tests: Validations, Amendments, Measures, and Issues.

A Validation examines specific elements in the data (that is, particular Darwin Core terms) and asks whether those data conform to a single specific criterion for quality.

An Amendment examines specific elements in the data and asks if it can propose changes to improve the quality of the data under a single specific criterion for quality.

Issues are like Validations, but they can identify potential problems in the data that may or may not be problems for all users of the same data. For example, there is a Validation that identifies whether or not dwc:dataGeneralizations contains any value, if it does, then users need to examine the specific statements made and evaluate them against their quality needs.  These are different from Validations which assert that the data are fit for use or not.   Issues are a form of warning flag where the test is drawing attention to potential problem with the value of a Darwin Core term for at least one use case. 

Measures either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE).  

## 1.2 Inputs to a test 

Each test is defined to take a specific set of input terms (InformationElements, generally Darwin Core terms), and then perform some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the Validations, Amendments, and Issues currently defined in BDQ Core examine a set of Darwin Core terms from a single record, e.g. from a single Occurrence record, rather than looking at the input term(s) over multiple records.  

Consider the test VALIDATION_EVENTDATE_STANDARD, it takes as input the InformationElement dwc:eventDate from a single record, and then asks "Is the value of dwc:eventDate a valid ISO date?".  It will then produce a Response describing the conclusion it reached in asking that question for that record.

## 1.3 Parts of a Response from a test. (normative) 

Reports SHOULD identify tests to you using at least the skos:prefLabel for the test class, e.g. VALIDATION_COUNTRY_FOUND.  

Results from each test MUST be delivered in the form of a Response.status, Response.result, and Response.comment.  Each test produces one Response.   A Response.qualifier may also be included.  

- The Response.status tells you if the test was able to run.  
- The Response.result tells you the conclusion of the test if it was able to be run.  Look only to the Response.result to understand if data have quality for some use or not.
- The Response.comment is a brief explanation of why the test reached the conclusion it did, examine the Response comment first to understand why a test provided a particular response.
- The optional Response.qualifier MAY provide additional information.

The Response.status MUST NOT be interpreted as a assertion concerning the quality of the data.  

The Response.result MUST be treated as the sole conclusion about data quality made by the test.  This conclusion MUST be explained in the Response.comment, and MAY be expaned upon in an optional Response.qualifier.

A Response.status of EXTERNAL_PREREQUISITES_NOT_MET tells you that the test was looking information up on some remote resource, such as a web service to look up taxon names, which was not available at the time the test was run.  This Response.status means that if the same test is run again on the same data at a different time, it may have a different result (e.g. if the web service became available and could be queried).

A Response.status of INTERNAL_PREREQUISITES_NOT_MET, however, means that some aspect of the data itself does not meet the prerequisites for running the test, such as an empty dwc:eventDate for a test that evaluates whether the eventDate falls within a particular time span.  If the same test is run again on the same, unmodified data, the same result is expected.  It is all to easy to interpret INTERNAL_PREREQUISITES_NOT_MET as pointing to some quality problem in the data, and while this may seem so, it is is misleading to think so, look instead to some Validation that specifically makes that evaluation and returns a Response.result of COMPLIANT or NOT_COMPLIANT, or some measure that returns a Response.result of COMPLETE or NOT_COMPLETE. 

Validations can also have a Response.status of RUN_HAS_RESULT, this tells you that the test ran, and the result of the test (COMPLIANT or NOT_COMPLIANT) will be found in the Response.result.

Amendments can have a Response.status of either of the prerequisites not met, or FILLED_IN, AMENDED, or NOT_AMENDED.  FILLED_IN tells you that the amendment is proposing that a value that was empty in the data under test can be filled in with a non empty value.  This proposal will be found in the Response.result.  AMENDED tell you that the amendment is proposing a change to an existing value, this proposal will be found in the Response.result.  NOT_AMENDED tells you that the prerequisites for running the amendment were met, but that it did not propose any change to the data.

Measures 

A Measure returns a numeric value or INTERNAL_PREREQUISITES_NOT_MET. Most Measures count the number of Validation or Amendment tests that a specifified Response.Result. MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. 

Issues

Issues result in a Response.status of "RUN_HAS_RESULT" and a Response.status of ISSUE, "POTENTIAL_ISSUE" or "NOT_ISSUE".  Potential issues require a human review. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POSSIBLE_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.   An issue that reports ISSUE is making an assertions that is the same as a Validation reporting a Response.result of NOT_COMPLIANT, in this sense, Issues are the converse of Validations.  The meaning, however, of NOT_ISSUE from an Issue is not the same as COMPLIANT from a Validation.  NOT_ISSUE means that no issue was detected, not that the data comply with any criteria for fitness, while COMPLIANT explicitly means that the data satisify some critierion for fitness for some use.  POTENTIAL_ISSUE has no analog in validations, it marks the presence of something in the data that will need evaluation by a human to determine whether or not the data are fit for their use or not.  One Issue in BDQ Core evaluates whether dwc:dataGeneralizations contains any value, if it does, then it reports POTENTIAL_ISSUE, meaning that a human will need to evaluate whether the information in dwc:dataGeneralizations indicates that the data in that record have been generalized in a way that makes the data unfit for their purpose.  See: [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../bdqcore/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY)  Very few Issues are defined in BDQ Core.


# 2 Reading the Quick Reference Guide to the tests (non-normative)

The BDQ Core Quick Reference Guide lists the tests by a subset of Descriptors. This subset provides a summary of the nature of each of the tests, and some Descriptors can be used to filter the tests to those that may be applicable to an application.   An index is provided for each test by UseCase.  Both SingleRecord tests (Validations, Amendments, Issues, Measures) and MultiRecord tests (at this time only Measures that evaluate the output of SingleRecord Validations across a data set) are included.  

For each test, the Quick Reference Guide lists ways to identify the test (Label: the brief human readable means for identifying a test; skos:prefLabel: a human readable label spelled out in words; Versioned IRI: the means for software to identify the test).  It is noted whether a test operates on SingleRecords or a MultiRecord (data set).   A brief description of what the test is intended to do is provided, along with a more detailed description for implementors (consisting of Specification, InformationElements ActedIpon and Consulted, any Paramters that could change the behaviour of the tests, default values for any bdq:sourceAuthority consulted by the test or other parameters).  

Two examples are given, each illustrating opposing behaviors of the test. For Validations, one example provides a Response.result of COMPLIANT, the other of NOT_COMPLIANT.  See the implementation guide for information on a larger set of test validation data.   

A list of UseCases describing data quality needs to which each test is seen to be applicable is provided, along with notes that provide additional guidance for understanding test results and for implementation.  

[Quick Reference Guide to the tests](../bdqcore/index.md)

# 2.1 Amendments only propose changes (normative)

Amendments only propose changes to data.  It is up to the consumers of data quality reports to choose whether or not to accept those changes, particularly into authoritative databases of record.  Consumers of data quality reports MAY choose to change data based on assertions made by Ammendments, or consumers of data quality reports MAY choose to not change their data based on assertions made by Amendments.  Databases of record SHOULD NOT automatically alter data based on assertions made by Amendments without human evaluation.   

# 2.2 Time and TimeZone (non-normative)

Time is not considered in any of the bdqcore: test descriptions.  This means that some cases where time zone data is important, dates within a dataset (bdqffdq:MultiRecord) aggregated from multiple sources may have plus or minus one day errors introduced.  If this would make such data unfit for your purposes, you will need to introduce additional tests. 


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


