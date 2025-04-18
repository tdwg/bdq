<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Core User's Guide

**Title**<br>
BDQ Core User's Guide

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
<http://rs.tdwg.org/bdq/terms/2025-04-11>

**Latest version**<br>
<http://rs.tdwg.org/bdq/terms/>

**Previous version**<br>

**Abstract**<br>
This document serves as a reference for the BDQ Core Standard, outlining the BDQ Core Tests used in data quality reports.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Core User's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-04-11>

**Comment**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Audience](#12-audience)
  - [1.3 Associated Documents](#13-associated-documents)
  - [1.4 Status of the content of this document](#14-status-of-the-content-of-this-document)
  - [1.5 RFC 2119 key words](#15-rfc-2119-key-words)
  - [1.6 Namespace abbreviations](#16-namespace-abbreviations)

[2 A Guide to the Tests](#2-a-guide-to-the-tests)
  - [2.1 Test Types (non-normative)](#21-test-types-non-normative)
  - [2.2 Test Inputs and Outputs](#22-test-inputs-and-outputs)
    - [2.2.1 Inputs to Tests (non-normative)](#221-inputs-to-tests-non-normative)
    - [2.2.2 Data Quality Reports (non-normative)](#222-data-quality-reports-non-normative)
    - [2.2.3 Responses From Tests (normative)](#223-responses-from-tests-normative)
    - [2.2.4 Responses From Different Test Types (normative)](#224-responses-from-different-test-types-normative)
  - [2.3 Amendments Propose Changes (normative)](#23-amendments-propose-changes-normative)
  - [2.4 Test Parameters (normative)](#24-test-parameters-normative)
    - [2.4.1 Test Parameters Example (non-normative)](#241-test-parameters-example-non-normative)

[3 Context for Quality, Uses and Purposes (non-normative)](#3-context-for-quality-uses-and-purposes-non-normative)

[4 Using the BDQ Core Quick Reference Guide (non-normative)](#4-using-the-bdq-core-quick-reference-guide-non-normative)

[5 Time and Time Zones (non-normative)](#5-time-and-time-zones-non-normative)

[Acronyms](#acronyms)

[Glossary](#glossary)

[References](#references)

[Cite BDQ Core](#cite-bdq-core)

## 1 Introduction

### 1.1 Purpose

The purpose of this document is to help users understand and effectively apply the BDQ Core Tests for assessing the quality of biodiversity data. It serves as a practical guide to interpreting Test outcomes, selecting appropriate Tests for specific data use scenarios, and understanding how the components of BDQ Core work together to support assessments of fitness for use.

This guide explains the conceptual and operational structure of the Tests, their inputs and outputs, and how different types of Tests behave. It also provides non-normative guidance on Test parameters, report interpretation, and practical concerns such as handling time zones. The document complements the formal specification of Tests by offering real-world orientation and examples designed for practitioners.

### 1.2 Audience

This guide is intended for biodiversity data users, curators, and quality assurance professionals who are responsible for evaluating the usability and reliability of biodiversity datasets. It is especially relevant for:

- Data providers, curators, and aggregator staff seeking to understand test results and improve data quality
- Researchers assessing dataset suitability for specific projects or analyses
- Data standards developers aiming to understand how BDQ Core supports fitness-for-use evaluations
- Anyone interpreting or configuring BDQ Core Tests, but not necessarily implementing them in software.

The document is written for readers with a practical need to work with data quality assessments. It assumes no formal training in ontologies or software development, but may reference those areas for context.

### 1.3 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality (BDQ) Core](../../index.md) page, which lists the parts of the standard.

### 1.4 Status of the content of this document

Each sections of this document is marked as normative or non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |

## 2 A Guide to the Tests

BDQ Core defines a set of Tests to assess the quality of biodiversity data. Implementations of these Tests may produce data quality reports. The format of such data quality reports may vary, but they should contain specific information about outputs from each Test. This guide describes the Tests, their inputs, expectations about their outputs, how they may be used for Quality Control and Quality Assurance, and describes the [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md), which gives the details of each BDQ Core Test. 

Biodiversity data encompasses information about the variety of life on Earth. This includes observations of where and when organisms were found (such as the date and location of a bird sighting including the species name, and potentially other details about its behavior, observed habitat, or physical characteristics. BDQ Core is designed to assess the quality of these data for a variety of uses including research and conservation. Implementations of the Tests defined in BDQ Core examine such Occurrence data expressed using Darwin Core terms. Darwin Core is a standardized set of terms used to describe biodiversity data, it provides a common vocabulary that allows different databases and researchers to share information in a consistent way.

The BDQ Core Tests are each very specific. Some Tests are very simple and self explanatory, such as the Test that asserts that the value of dwc:day should be an integer in the range 1 to 31. Other Tests reference external authoritative sources of information to evaluate data quality, these are referred to as source authorities. For example, testing values of dwc:countryCode involves comparison with the source authority that is the list of valid ISO country codes.

### 2.1 Test Types (non-normative)

There are four types of Tests: Validation, Issue, Amendment, and Measure. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into Test suites (Policies) that assess the fitness of data for a specific use.

**Validation Tests** can be thought of as fact-checking. They compare the data against known standards or rules. Validation Tests examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a Criterion for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe) where dwc:countryCode is checked against a Source Authority for validity.

**Issue Tests** can be thought of as warning flags. They don't necessarily mean the data are wrong, but they highlight something that might be a problem for some users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) alerts users to a NotEmpty value that should be examined against their data quality needs. 

**Amendment Tests** can be thought of as suggestions for improvement. Amendment Tests examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and may propose changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350), where a valid ISO country code could be inferred.

**Measure Tests** can be thought of as metrics. Measure Tests either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](https://rs.tdwg.org/bdqcore/terms/453844ae-9df4-439f-8e24-c52498eca84a), which returns the number of Tests of Type Validation that had a response of "NOT_COMPLIANT" on a record.

### 2.2 Test Inputs and Outputs

#### 2.2.1 Inputs to Tests (non-normative)

Each Test is defined to take a specific set of input terms (InformationElements, generally [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021)), and then perform some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the BDQ Core Validation, Amendment, and Issue Tests examine a set of Darwin Core terms from a Single Record (e.g., from a single Occurrence record) rather than looking at the input term(s) over multiple records.

Consider the Test [VALIDATION_EVENTDATE_STANDARD](https://rs.tdwg.org/bdqcore/terms/4f2bf8fd-fc5c-493f-a44c-e7b16153c803). It takes as input value of the InformationElement dwc:eventDate from a Single Record, and then asks, "Is the value of dwc:eventDate a valid ISO date?". It will then produce a Response describing the conclusion it reached when analyzing that record.

Tests can also operate on a dataset (a Multi Record), and examine the values for Information Elements across the entire dataset. The only Multi Record Tests currently defined in BDQ Core are Measures, which take the outputs of Single Record Tests as their inputs and report on the results of those Single Record Tests aggregated across the dataset. The names of these Tests all begin with `MULTIRECORD_`. 

#### 2.2.2 Data Quality Reports (non-normative) 

Software that includes implementations of the Tests may produce data quality reports. The form that such data quality reports may take is not specified by BDQ Core, however, it does specify elements that should be present in such reports.

#### 2.2.3 Responses From Tests (normative) 

Reports SHOULD identify Tests using at least the Label (rdfs:label) for the Test class (e.g., [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134)).

Results from each Test MUST be delivered in the form of a Response.status, Response.result, and Response.comment. Each Test MUST produce one Response. A Response.qualifier MAY also be included.

- The Response.status tells you if the Test was able to run. The Response.status MUST NOT be interpreted as a assertion concerning the quality of the data.
- The Response.result tells you the conclusion of the Test if it was able to be run. Look only to the Response.result to understand if data have quality for some use or not. The Response.result MUST be treated as the sole conclusion about data quality made by the Test. This conclusion MUST be explained in the Response.comment, and MAY be expanded upon in an optional Response.qualifier.
- The Response.comment is a brief explanation of why the Test reached the conclusion it did. Examine the Response comment first to understand why a Test provided a particular response.
- The optional Response.qualifier MAY provide additional information.

A Response.status="EXTERNAL_PREREQUISITES_NOT_MET" means the Test couldn't run because it needed information from an outside source (e.g., a web service to look up taxon names), which was unavailable at the time the Test was run. This Response.status means that if the same Test is run again on the same data at a different time, it may have a different result (e.g., if the web service became available and could be queried).

A Response.status="INTERNAL_PREREQUISITES_NOT_MET" means the Test couldn't run because the data were unable meet the prerequisites for running the Test, such as a bdq:Empty dwc:eventDate for a Test that evaluates whether the dwc:eventDate falls within a particular time span. If the same Test is run again on the same, unmodified data, the same result is expected. It is too easy to interpret a Response.status="INTERNAL_PREREQUISITES_NOT_MET" as pointing to some quality problem in the data, and while this may seem so, it is misleading. Look instead to some Validation Test that specifically makes that evaluation and returns a Response.result="COMPLIANT" or "NOT_COMPLIANT", or some Measure that returns a Response.result="COMPLETE" or "NOT_COMPLETE". 

#### 2.2.4 Responses From Different Test Types (normative) 

Any type of Test may have a Response.status of EXTERNAL_PREREQUISITES_NOT_MET or INTERNAL_PREREQUISITES_NOT_MET.

Validation Tests can have a Response.status of RUN_HAS_RESULT, which tells you that the Test ran, and the Response.result of the Test will be COMPLIANT or NOT_COMPLIANT.

Amendment Tests can have a Response.status of FILLED_IN, AMENDED, or NOT_AMENDED. FILLED_IN tells you that the Amendment is proposing that a value that was bdq:Empty in the data evaluated by the Test can be filled in with a value that is bdq:NotEmpty. This proposal will be found in the Response.result. A Response.status="AMENDED" tells you that the Amendment is proposing a change to an existing value, and this proposal will be found in the Response.result. "NOT_AMENDED" tells you that the prerequisites for running the Amendment were met, but that it did not propose any change to the data.

Measure Tests that return a Response.status of RUN_HAS_RESULT MUST return either a numeric value or one of COMPLETE or NOT_COMPLETE. Most Measure Tests are summaries of the results of running Validation or Amendment Tests across datasets, though some (e.g., [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53)), can provide a conversion from one representation of the data to another.

Issue Tests with a Response.status of RUN_HAS_RESULT MAY have a Response.result of POTENTIAL_ISSUE or NOT_ISSUE. Potential issues require review to evaluate if the record is suitable for a particular use. For example, the Test [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2) evaluates whether dwc:dataGeneralizations contains any value, if it does, then the Test reports a Response.result="POTENTIAL_ISSUE", meaning that a human will need to evaluate whether the information in dwc:dataGeneralizations indicates that the data in that record have been generalized in a way that makes the data unfit for their purpose. An Issue Test that has a Response.result="POTENTIAL_ISSUE" is making an assertion that is the similar to that of a Validation Test that has a Response.result="NOT_COMPLIANT". Issue Tests approximate the converse of Validation Tests. The meaning, Response.result="NOT_ISSUE", however, is not the same as a Response.result="COMPLIANT" from a Validation Test. NOT_ISSUE means that no (data quality) issue was detected, not that the data comply with any criteria for fitness, while COMPLIANT explicitly means that the data satisfy some criterion for fitness for some Use Case. A Response.result="POTENTIAL_ISSUE" has no analog in Validation Tests; it marks the presence of something in the data that SHOULD BE evaluated by a human to determine whether or not the data are fit for their use.

### 2.3 Amendments Propose Changes (normative)

Amendment Tests **propose changes** to data. It is up to the consumers of data quality reports to choose whether or not to accept those changes, particularly into an authoritative database of record. Consumers of data quality reports MAY choose to change data based on assertions made by Amendment Tests, or consumers of data quality reports MAY choose to not change their data based on assertions made by Amendment Tests. Databases of record SHOULD NOT automatically alter data based on assertions made by Amendment Tests without human evaluation of the proposed changes.

### 2.4 Test Parameters (normative) 

Some Tests are parameterized. When a Test is Parameterized, and a value other than the default value is used for some Parameter, reports SHOULD identify the Tests using at least the Label (rdfs:label) for the Test class, in combination with the Parameter and the value of the argument that replaced the Parameter in this specific case.

Values of Parameters, other than the defaults, SHOULD also be present in the Response.comment.

More normative guidance on Test Parameters can be found in the section [Parameters and Changing the Behavior of a Test](../implementers/index.md#61-Parameters-and-Changing-the-Behavior-of-a-Test-normative) of the [BDQ Core Implementer's Guide](../guide/implementers/index.md).

#### 2.4.1 Test Parameters Example (non-normative) 

If a Test with a non-default Parameter value is used, this should be represented with at least the Label (rdfs:label) for the Test class (e.g., [VALIDATION_MINDEPTH_INRANGE](https://rs.tdwg.org/bdqcore/terms/04b2c8f3-c71b-4e95-8e43-f70374c5fb92)) in combination with the Parameter (e.g., bdq:maximumValidDepthInMeters) and the value of the argument that replaced the default Parameter value in this specific case (e.g., 1642). For example:

	`VALIDATION_MAXDEPTH_INRANGE with bdq:maximumValidDepthInMeters=1642`

should be accompanied by a Response.comment that includes text expressing something similar to "Non-default bdq:maximumValidDepthInMeters=1642".

So, a value of dwc:minimumDepthInMeters of 2000m would be NOT_COMPLIANT in this case, while with the default value for that parameter (11000), it would be COMPLIANT.

## 3 Context for Quality, Uses and Purposes (non-normative)

Data do not have quality in the abstract, they only have quality with respect to some use (BDQ Core Use Case). The Fitness for Use Framework (see [Fitness For Use Framework Ontology Guide](../bdqffdq/index.md)) used in BDQ Core describes uses for data as Use Cases, and expects that Tests are run in suites that form policy for data quality with respect to Use Cases. That is, sets of Tests are expected to be run together in order to assess quality of data for some specified use, and both Tests and reports of results from Tests should be understood within the context of that use for the data.

Tests for data quality may serve two purposes, Quality Control and Quality Assurance. In Quality Control, Tests are used to find data that lack fitness for particular uses and the results are used to improve the quality of the data. In Quality Assurance, data are filtered so that only data that are fit for some use are used for that purpose.

The Fitness for use Framework (Veiga 2016, Veiga et al., 2017) provides a formal means for filtering records for [Quality Assurance](../../bdqffdq/index.md#5-Fitness-For-Use-Framework-Summary-of-Mathematical-Formalization-normative) (involving only Measures), but informally, data may be thought as being fit for some use if all Validation Tests comprising that Use Case have a Response.result="COMPLIANT", and all non-numeric Measure Tests comprising that Use Case have a Response.result="COMPLETE". The BDQ Core Tests include a set of MultiRecord Measures who's purpose is to enable formal filtering (Quality Assurance) and reporting (for Quality Control) under the [Fitness for Use Ontology](../../bdqffdq/index.md).

The Framework provides a formal statement of [Quality Control](../../bdqffdq/index.md#5-Fitness-For-Use-Framework-Summary-of-Mathematical-Formalization-normative), but the application of Quality Control 'in the wild' is more nuanced; more complex than simple filtering under Quality Assurance. The context of Quality Control may affect how Tests and their results are applied to data, information systems and processes.

Quality Control is most efficient at the time of data capture where the prevention of incorrect values avoids subsequent, far less efficient issue detection and correction. For example, issues such as transposition of values are far easier to detect and correct at the point of recording than during subsequent downstream processing where context may be lost or held on paper records remote from data entry, and errors may be propagated. Validation Tests may be thought of as framing constraints to impose on data entry interfaces, such as validation of data against a controlled vocabulary being imposed by the presentation of the controlled vocabulary as a pick list in a user interface, or may be implemented as checks on entered data values with immediate feedback for users. 

When data quality reports result from the analysis of data in databases of record, numerous reports of INTERNAL_PREREQUISITES_NOT_MET or NOT_COMPLIANT are likely, particularly in historical data where data values may be poorly known, or data may have passed through multiple life cycles of collection management systems. In a database of record, the focus of the quality control processes is very likely on the identification of tractable targeted data cleanup projects. Such data cleanup projects can involve multiple staff with different skills and are likely to last for long periods of time. Data cleaning projects are expensive, and data quality reports driven by Tests organized by Use Cases can be an effective management tool for identifying and prioritizing suitable and tractable projects for data cleanup. 

Complicating the analysis of data quality reports on databases of record is that when relational database tables are denormalized to flat files for analyses and reporting, propagated errors could trace back to a single 'point of failure'. What appear in reports as large numbers of errors may result from a single problem in a single record of a relational table. A clear understanding of the structure of a database of record is needed to interpret data quality reports into targeted data cleanup projects. The keys for applying data quality reports to improvement of databases of record is identification of focused areas for data cleanup projects, and identification of places where data quality problems may be reduced by improvements to workflow processes or user interfaces for entry and manipulation of data. Some Validation Tests may point to places where controlled vocabularies should be in use but are not, suggesting a need for a coordinated set of changes. For example, splitting a single free text field into a controlled vocabulary field and a free text field for further elaboration, a data cleanup project to map all existing values onto a controlled vocabulary, and then changes to user interface to reflect the split into a controlled field and associated remarks.
 
Correcting issues subsequent to data capture introduces further complexities in that any amendment to existing values requires careful human evaluation and a forking of data records to maintain original data and an audit trail. Data cleaning often requires far more time than data analysis.

When performing Quality Control while preparing data for aggregation, or when reports are provided by aggregators to upstream data providers, analysis of reports may reveal simple errors introduced in mapping data onto Darwin Core terms. For example, field transpositions in mapping in addition to underlying problems in the data. Validation, particularly at this step may reveal cases where the a database of record holds more authoritative information than an upstream resource relied upon by the aggregator (or a source authority for a Test), and is correct despite NOT_COMPLIANT Validation Test results. Careful analysis of data Quality Control results is needed, with a need to identify focused areas for data cleaning projects, as they involve a significant effort.

Quality Control to improve data during downstream analysis of aggregated data has other challenges. The volume of aggregated data may be large enough to make both examination of the proposed Amendments and reporting of proposed changes to upstream databases of record infeasible. Quality Control in the workflow processing of data streams from large scale aggregation may include acceptance of proposals from Amendments into a data stream for downstream analysis. This should be done with some care in checking that the proposed amendments are not introducing errors or false precision, and both unamended and amended data should be preserved, with accepted proposals from amendments clearly identifiable as manipulations of the data stream.

## 4 Using the BDQ Core Quick Reference Guide (non-normative)

The [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) is a companion to this Guide and lists the Tests with a subset of Test Descriptors. This subset is intended to provide a quick summary of the nature of each of the Tests that is sufficient of most cases. Some Test Descriptors can be used to filter the Tests down to those that may be applicable for an application (Use Case). An index is provided for each Test by example UseCase. Both SingleRecord Tests (Validations, Amendments, Issues, Measures) and MultiRecord Tests (at this time only Measures that evaluate the output of SingleRecord Validations across a dataset) are included. Term definitions with the full set of Test Descriptors can be found in the [BDQ Core Tests and Assertions List of Terms](../../list/bdqcore/index.md).

While the [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) provides a description of each individual BDQ Core Test, Data Quality Reports may vary in how they present results from the execution of these Tests. Possible presentations include displaying Test results individually, aggregating counts of results for each Test run over all records in a dataset, and separating results into pre- and post-amendment phases. In the latter case, results may be shown for all Validation and Measure Tests run in a pre-amendment phase, then proposals for changes from all Amendment Tests run in an amendment phase, and then results from the same Validation and Measure Tests run in a post-amendment phase as if all proposed changes from the Amendment Tests were evaluated and accepted. It is thus important to identify both the Test for which results are being reported, and the context for the report. The Quick Reference Guide describes what each Test does independent of this context.

For each Test, the [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) lists ways to identify the Test (**Label:** - the brief human readable means for identifying a Test; **skos:prefLabel:** - the human readable label spelled out in words; **Versioned IRI:** - the means for software to identify the Test). For each Test, the Quick Reference Guide identifies whether the Test operates on SingleRecords or a MultiRecord (a dataset). A brief description of what the Test is intended to do follows, with a more detailed description for implementers, consisting of Specification, InformationElements ActedUpon and Consulted, any Parameters that could change the behavior of the Tests, default values for any bdq:sourceAuthority consulted by the Test, or other parameters.

Two Examples of Test data input and output are provided to illustrate opposing behaviors of the Test. For Validation Tests, one example provides a Response.result="COMPLIANT", the other "NOT_COMPLIANT". See the [BDQ Core Implementer's Guide](../implementers/index.md) for information about Test Validation Data. 

Each Test lists UseCases describing data quality needs to which each Test is applicable. Notes provide additional guidance for understanding Test results and for implementation.

The definitions of the terms used for the Tests can be found at [Terms used in the Quick Reference Guide to BDQ Core Tests](../../terms/bdqcore/bdqcore_qrg_term_descriptions.md).

## 5 Time and Time Zones (non-normative)

Time is not considered in any of the BDQ Core Tests. There are Use Cases where the time zone is important. Dates within a dataset (bdqffdq:MultiRecord) aggregated from multiple sources may have plus or minus one day errors introduced. New Tests are required if ignorance of time would make such data unfit for a purpose. For further information, see Section [4.2 Time](../../supplement/index.md#42-Time) in [BDQ Core Supplemental Information](../../supplement/index.md).

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Core User's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


