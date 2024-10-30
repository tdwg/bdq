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

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 2 A Guide to the Tests

### 2.1 Test Types (non-normative)

There are four types of tests: Validations, Issues, Amendments and Measures. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into test suites (profiles) that assess the fitness for use of data for a specific use.

**Validation Tests** examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a criterion for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe) where dwc:countryCode is checked against a source authority for validity.

**Issue Tests** are like Validations in identifying potential issues in the data that may be problems for all users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) alerts users to a non-empty value that should be examined against their data quality needs. Issues are a 'warning flag' while Validations assert that the data are fit for use or not. 

**Amendment Tests** examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) to identify potential changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350) where a valid ISO country code could be inferred.

**Measure Tests** either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](https://rs.tdwg.org/bdqcore/terms/453844ae-9df4-439f-8e24-c52498eca84a) that returns the number of tests of Type Validation that had a response of "NOT_COMPLIANT".

### 2.2 Test Inputs and Outputs

#### 2.2.1 Inputs to Tests (non-normative)

Each Test is defined to take a specific set of input terms (InformationElements, generally [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021)), and then perform some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the BDQ Core Validation, Amendment, and Issue Tests examine a set of Darwin Core terms from a Single Record, e.g. from a single Occurrence record, rather than looking at the input term(s) over multiple records.  

Consider the Test [VALIDATION_EVENTDATE_STANDARD](https://rs.tdwg.org/bdqcore/terms/4f2bf8fd-fc5c-493f-a44c-e7b16153c803), it takes as input the InformationElement dwc:eventDate from a Single Record, and then asks "Is the value of dwc:eventDate a valid ISO date?".  It will then produce a Response describing the conclusion it reached in asking that question for that record.

#### 2.2.2 Data Quality Reports (non-normative) 

#### 2.2.2 Responses From Tests (normative) 

Reports SHOULD identify Tests to you using at least the Label (rdfs:Label) for the test class, e.g. [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134).  

Results from each Test MUST be delivered in the form of a Response.status, Response.result, and Response.comment.  Each test produces one Response.   A Response.qualifier may also be included.  

- The Response.status tells you if the Test was able to run.  
- The Response.result tells you the conclusion of the Test if it was able to be run.  Look only to the Response.result to understand if data have quality for some use or not.
- The Response.comment is a brief explanation of why the Test reached the conclusion it did, examine the Response comment first to understand why a Test provided a particular response.
- The optional Response.qualifier MAY provide additional information.

The Response.status MUST NOT be interpreted as a assertion concerning the quality of the data.  

The Response.result MUST be treated as the sole conclusion about data quality made by the Test.  This conclusion MUST be explained in the Response.comment, and MAY be expaned upon in an optional Response.qualifier.

A Response.status="EXTERNAL_PREREQUISITES_NOT_MET" states that the test was looking information up on some remote resource, such as a web service to look up taxon names, which was not available at the time the Test was run.  This Response.status means that if the same Test is run again on the same data at a different time, it may have a different result (e.g. if the web service became available and could be queried).

A Response.status="INTERNAL_PREREQUISITES_NOT_MET" however, means that some aspect of the data itself does not meet the prerequisites for running the Test, such as an empty dwc:eventDate for a Test that evaluates whether the eventDate falls within a particular time span.  If the same Test is run again on the same, unmodified data, the same result is expected.  It is too easy to interpret a Response.status="INTERNAL_PREREQUISITES_NOT_MET" as pointing to some quality problem in the data, and while this may seem so, it is is misleading. Look instead to some Validation Test that specifically makes that evaluation and returns a Response.result="COMPLIANT" or "NOT_COMPLIANT", or some measure that returns a Response.result="COMPLETE" or "NOT_COMPLETE". 

#### 2.2.3 Responses From Different Types of Test (normative) 

Validation Tests can also have a response of RUN_HAS_RESULT which tells you that the test ran, and the result of the test will be COMPLIANT or NOT_COMPLIANT.

Amendment Tests can have a response of INTERNAL_PREREQUISITES_NOT_MET or FILLED_IN, AMENDED, or NOT_AMENDED. FILLED_IN tells you that the Amendment is proposing that a value that was empty in the data under test can be filled in with a non empty value.  This proposal will be found in the Response.result. A Response.status="AMENDED" tells you that the Amendment is proposing a change to an existing value, and this proposal will be found in the Response.result.  "NOT_AMENDED" tells you that the prerequisites for running the Amendment were met, but that it did not propose any change to the data.

Mesure Tests generally summarise the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. Measure Tests MUST return either a numeric value or a Response.status="INTERNAL_PREREQUISITES_NOT_MET". Most Measure Tests count the number of Validation or Amendment Tests that have a specified Response.Result. For example, the Test [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53) returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs. For example, an event date to at least one day for phenology studies or to at least one year for other purposes.  

Issues Tests result in a response of INTERNAL_PREREQUISITES_NOT_MET or RUN_HAS_RESULT and a result of POTENTIAL_ISSUE or NOT_ISSUE.  Potential issues require a human review. For example, the Test [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) will return a Response.result="POTENTIAL_ISSUE" if dwc:dataGeneralizations contains a value. The value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) will require human review for any Use Case to determine if the data are fit for purpose or not.   An Issue Test that has a Response.result="POTENTIAL_ISSUE" is making an assertion that is the same as a Validation Test reporting a Response.result="NOT_COMPLIANT". Issue Tests are the converse of Validation Tests.  The meaning, however, of a Response.result="NOT_ISSUE" is not the same as a Response.result="COMPLIANT" from a Validation Test. NOT_ISSUE means that no issue was detected, not that the data comply with any criteria for fitness, while COMPLIANT explicitly means that the data satisify some critierion for fitness for some Use Case.  A Response.result="POTENTIAL_ISSUE" has no analog in Validation Tests; it marks the presence of something in the data that will need evaluation by a human to determine whether or not the data are fit for their use or not.  One Issue Test in BDQ Core evaluates whether dwc:dataGeneralizations contains any value. If it does, then the Test reports a Response.result="POTENTIAL_ISSUE", meaning that a human will need to evaluate whether the information in dwc:dataGeneralizations indicates that the data in that record have been generalized in a way that makes the data unfit for their purpose.  See [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2).  

### 2.3 Amendments Propose Changes (normative)

Amendment Tests **propose changes** to data.  It is up to the consumers of data quality reports to choose whether or not to accept those changes, particularly into authoritative databases of records.  Consumers of data quality reports MAY choose to change data based on assertions made by Ammendment Tests, or consumers of data quality reports MAY choose to not change their data based on assertions made by Amendment Tests.  Databases of records SHOULD NOT automatically alter data based on assertions made by Amendment Tests without human evaluation.   

### 2.4 Test Parameters (normative) 

Some Tests are parameterized. When a Test is Parameterized, and a value other than the default value is used for some Parameter, reports SHOULD identify the Tests to you using at least the Label (rdfs:Label) for the Test class, e.g. [VALIDATION_MINDEPTH_INRANGE](https://rs.tdwg.org/bdqcore/terms/04b2c8f3-c71b-4e95-8e43-f70374c5fb92) in combination with the Parameter (e.g. bdq:maximumValidDepthInMeters) and the value of the argument that replaced the Parameter in this specific case (e.g. 1642).

    VALIDATION_MINDEPTH_INRANGE with bdq:maximumValidDepthInMeters=1642 

So a value of dwc:minimumDepthInMeters of 2000m would be NOT_COMPLIANT in this case; while with the default value for that parameter it would be COMPLIANT.

## 3 Context for Quality, Uses and Purposes (non-normative)

Data does not have quality in the abstract, it only has quality with respect to some use.  The [bdqffdq:](../bdqffdq/index.md) Framework for data quality used in BDQ Core, describes uses for data as Use Cases, and expects that tests are run in suites that form policy for data quality with respect to Use Cases.  That is, sets of tests are expected to be run together in order to assess quality of data for some specified use, and reports of results from test should be understood within the context of that use for the data.

Tests for data quality may serve two purposes, Quality Control and Quality Assurance.  In Quality Control, tests are used to find data that lacks fitness for particular uses and the results are used to improve the quality of the data.  In Quality Assurance, data are filtered so that only data that are fit for some purpose are used for that purpose.

The Framework Ontology (bdqffdq:) provides a formal means for filtering records for Quality Assurance (involving only Measures), but informally, data may be thought as being fit for some use if all Validation Tests comprising that Use Case have a Response.result="COMPLIANT", and all non-numeric Measure Tests comprising that Use Case have a Response.result="COMPLETE".  The BDQ Core Tests include a set of MultiRecord Measures who's purpose is to enable formal filtering (for Quality Assurance) and reporting (for Quality Control) under the Framework Ontology.

<!--- Lee's go at changing the TODOs below into paragraphs with edits by Paul. --->

The Framework Ontology provides a formal statement of Quality Control but the application of Qualtity Control 'in the wild' is more nuanced, and is more complex than simple filtering under Quality Assurance.
The context of Quality Control may affect how Tests and their results are applied to data, information systems, and processes.
  Quality Control is most efficient at the time of data capture where the prevention of incorrect values avoids subsequent far less efficient issue detection and correction. Issues such as transposition of values are far easier to detect and correct at the point of recording than during subsequent downstream processing where context may be lost or held on paper records remote from data entry, and errors may be propagated.  Validation Tests may be though of as framing constraints to impose on data entry interfaces, such as validation of data against a controlled vocabulary being imposed by the presentation of the controlled vocabulary as a pick list in a user interface, or may be implemented as checks on entered data values with immediate feedback for users. 

When data quality reports result from analysis of data in databases of record, numerous validation failures are likely, particularly in historical data where data values may be poorly know, or data may have passed through multiple life cycles of collection management systems.  In a data base of record, the focus of quality control processes is very likely on identifing tractable targeted data cleanup projects.  Data cleanup projects can involve multiple staff with different skills and are likely to last for long periods of time.  Datacleanup projects are expensive, and data quality reports driven by Tests organized by Use Cases can be a management tool for identifying and prioritizing suitable and tractable projects for data cleanup. 

Complicating the analysis of data quality reports on databases of record is that when relational database tables are denormalized to flat files for analyses and reporting, propagated errors could trace back to a single 'point of failure'.  What appear in reports as large numbers of errors may result from a single problem in a single record of a relational table.  A clear understanding of the structure of a database of record is needed to interpret data quality reports into targeted data cleanup projects.   The keys for applying data quality reports to impovement of data in databases of record is identification of focused areas for data cleanup projects, and identification of places where data quality problems may be reduced by improvements to workflow processes or user interfaces for entry and manipulation of data.  Some validations may point to places where controlled vocabularies should be in use but are not, pointing to a need for a coordinated set of changes (for example splitting a single free text field into a controlled vocabulary field and a free text field for further elaboration, a data cleanup project to map all existing values onto a controlled vocabulary, and then changes to user interface to reflect the split into a controlled field and associated remarks.

Correcting issues subesquent to data capture introduces further complexities in that any amendment to existing values requires careful human evaluation and a forking of data records to maintain original data, and an audit trail. Data cleaning often requires far more time than data analysis.

When performing Quality Control when preparing data for aggregation, or when reports are provided by aggregators to upstream data providers, analysis of reports may reveal simple errors introduced in mapping data onto Darwin Core terms, such as field transpositions in mapping in addition to underlying problems in the data.  Validation, particularly at this step may reveal cases where the a database of record holds more authoritative information than an upstream resource relied upon by the aggregator (or a source authority for a test), and is correct despite NOT_COMPLIANT Validation results.  Careful analysis of data quality control results is needed, again with a need to identify focused areas for data cleanup projects, as they involve significant work effort.  

Quality Control to improve data during downstream analysis of aggregated data has other chalenges.  The volume of aggregated data may be large enough to make both examination of the proposal of Amendments and reporting of proposed changes to upstream databases of record infeasable.  Quality Control in the workflow processing of data streams from large scale aggregation may include acceptance of proposals from Amendments into a data stream for downstream analysis.  This should be done with some care in checking that the proposed amendments are not introducing errors or false precision, and both unamended and amended data should be preserved, with accepted proposals from amendments clearly identifiable as manipulations of the data stream.  

## 4 Using the BDQ Core Quick Reference Guide (non-normative)

The [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) is a companion to this Guide and lists the tests by a subset of Test Descriptors. This subset is intended to provide a quick summary of the nature of each of the Tests. Some Test Descriptors can be used to filter the Tests down to those that may be applicable for an application.  An index is provided for each Test by example UseCase.  Both SingleRecord Tests (Validations, Amendments, Issues, Measures) and MultiRecord tests (at this time only Measures that evaluate the output of SingleRecord Validations across a data set) are included.  

The [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) provides a description of individual Tests.  Data Quality Reports may vary in how they present this information, including displaying test results individually, aggregating counts of results for each test run over all records in a data set, and separating results into pre- and post-amendment phases.  In the latter case, results may be shown for all Validation and Measure Tests run in a pre-amendment phase, then proposals for changes from all Amendment Tests run in an amendment phase, and then results from the same Validation and Measure Tests run in a post-amendement phase as if all proposed changes from the Amendment Tests were evaluated and accepted.  It is thus important to identify both the Test for which results are being reported, and the context for the report.  The Quick Reference Guide describes what each Test does independent of this context.

For each Test, the [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) lists ways to identify the Test (**Label:** the brief human readable means for identifying a Test; **skos:prefLabel:** A human readable label spelled out in words; **Versioned IRI:** the means for software to identify the Test).  For each Test, the guide identifies whether the Test operates on SingleRecords or a MultiRecord (a data set).  A brief description follows of what the Test is intended to do, with a more detailed description for implementors (consisting of Specification, InformationElements ActedUpon and Consulted, any Parameters that could change the behaviour of the Tests, default values for any bdq:sourceAuthority consulted by the Test or other parameters).  

Two examples of Test data input and output are provided to illustrate opposing behaviors of the Test. For Validation Tests, one example provides a Response.result="COMPLIANT", the other of "NOT_COMPLIANT".  See the [BDQ Core Implementer's Guide](../implementers/index.md)  for information about Test validation data. 

Each Test lists UseCases describing data quality needs to which each Test is applicable. Notes provide additional guidance for understanding test results and for implementation.  

The definitions of the terms used for the tests can be found at [Terms in bdqcore: Quick Reference Guide](../../terms/bdqcore/bdqcore_qrg_term_descriptions.md).

## 5 Time and TimeZones (non-normative)

Time is not considered in any of the BDQ Core Tests.  There are Use Cases where time zone data is important. Dates within a dataset (bdqffdq:MultiRecord) aggregated from multiple sources may have plus or minus one day errors introduced.  New Tests are required if ignorance of time would make such data unfit for purpose. 
