<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ User's Guide

**Title**<br>
BDQ User's Guide

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

<!--
**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}
-->

**This version**<br>
<http://rs.tdwg.org/bdq/terms/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdq/terms/>

**Previous version**<br>

**Abstract**<br>
This document serves as a reference for the BDQ standard, outlining the BDQ Tests used in `Data Quality Reports`.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ User's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
  - [1.4 Status of the content of this document (normative)](#14-status-of-the-content-of-this-document-normative)
  - [1.5 RFC 2119 key words (normative)](#15-rfc-2119-key-words-normative)
  - [1.6 Namespace abbreviations (non-normative)](#16-namespace-abbreviations-non-normative)
  - [1.7 Referring to Terms (normative)](#17-referring-to-terms-normative)

[2 Context for Quality, Uses and Purposes (non-normative)](#2-context-for-quality-uses-and-purposes-non-normative)

[2.1 Quality Control and Quality Assurance (non-normative)](#21-quality-control-and-quality-assurance-non-normative)
  - [2.1.1 Quality Assurance (non-normative)](#211-quality-assurance-non-normative)
  - [2.1.2 Quality Control (non-normative)](#212-quality-control-non-normative)
  - [2.1.3 Quality Control in Data Aggregation (non-normative)](#213-quality-control-in-data-aggregation-non-normative)

[3 A Guide to the Tests (non-normative)](#3-a-guide-to-the-tests-non-normative)
  - [3.1 Test Types (non-normative)](#31-test-types-non-normative)
  - [3.2 Test Inputs and Outputs (non-normative)](#32-test-inputs-and-outputs-non-normative)
    - [3.2.1 Inputs to Tests (non-normative)](#321-inputs-to-tests-non-normative)
    - [3.2.2 Outputs: Data Quality Reports (non-normative)](#322-outputs-data-quality-reports-non-normative)
    - [3.2.3 Outputs: Responses from Tests (normative)](#323-outputs-responses-from-tests-normative)
      - [3.2.3.1 Shorthand for Responses from Tests (non-normative)](#3231-shorthand-for-responses-from-tests-non-normative)
      - [3.2.3.2 Validation Test Reports (non-normative)](#3232-validation-test-reports-non-normative)
      - [3.2.3.3 Issue Test Reports (non-normative)](#3233-issue-test-reports-non-normative)
      - [3.2.3.4 Measure Test Reports (non-normative)](#3234-measure-test-reports-non-normative)
      - [3.2.3.5 Amendment Test Reports (non-normative)](#3235-amendment-test-reports-non-normative)
  - [3.3 Amendments Propose Changes (normative)](#33-amendments-propose-changes-normative)
    - [3.3.1 Caution in Proposing Changes (non-normative)](#331-caution-in-proposing-changes-non-normative)
  - [3.4 Test Parameters (non-normative)](#34-test-parameters-non-normative)
  - [3.4.1 Test Parameters in Reports (normative)](#341-test-parameters-in-reports-normative)
    - [3.4.2 Test Parameters Example (non-normative)](#342-test-parameters-example-non-normative)

[4 Using the BDQ Tests Quick Reference Guide (non-normative)](#4-using-the-bdq-tests-quick-reference-guide-non-normative)

[5 Time of Day and Time Zones (non-normative)](#5-time-of-day-and-time-zones-non-normative)

[6 Dates and Calendars (non-normative)](#6-dates-and-calendars-non-normative)

[7 Creating New Tests (non-normative)](#7-creating-new-tests-non-normative)
  - [7.1 Elements of a New Test (non-normative)](#71-elements-of-a-new-test-non-normative)
  - [7.2 Proposing to add a Test to the BDQ Standard (non-normative)](#72-proposing-to-add-a-test-to-the-bdq-standard-non-normative)

[8 Creating New Use Cases (non-normative)](#8-creating-new-use-cases-non-normative)
  - [8.1 Elements of a New Use Case (non-normative)](#81-elements-of-a-new-use-case-non-normative)
  - [8.2 Proposing to add a Use Case to the BDQ Standard (non-normative)](#82-proposing-to-add-a-use-case-to-the-bdq-standard-non-normative)

[Acronyms (non-normative)](#acronyms-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to help users understand and effectively apply the BDQ Tests for assessing the quality of biodiversity data. It serves as a practical guide to interpreting Test outcomes, selecting appropriate Tests for specific data use scenarios, and understanding how the components of the BDQ standard work together to support assessments of fitness for use.

This guide explains the conceptual and operational structure of the Tests, their inputs and outputs, and how different types of Tests behave. It also provides non-normative guidance on Test parameters, report interpretation, and practical concerns such as handling time zones. The document complements the formal specification of Tests by offering real-world orientation and examples designed for practitioners.

### 1.2 Audience (non-normative)

This guide is intended for biodiversity data users, curators, and quality assurance professionals who are responsible for evaluating the usability and reliability of biodiversity datasets. It is especially relevant for:

- Data providers, curators, and aggregator staff seeking to understand test results and improve data quality
- Researchers assessing dataset suitability for specific projects or analyses
- Data standards developers aiming to understand how the BDQ standard supports fitness-for-use evaluations
- Anyone interpreting or configuring BDQ Tests, but not necessarily implementing them in software.

The document is written for readers with a practical need to work with data quality assessments. It assumes no formal training in ontologies or software development, but may reference those areas for context.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

The set of information most relevant to users of Biodiversity Data Quality (BDQ) Tests can be found in the following subset of resources:

- [**BDQ Tests and Assertions**](../../bdqtest/index.md) - Defines how each Test is modeled using standard vocabulary terms and how it should behave under various conditions.
- [**BDQ Tests Quick Reference Guide**](../../terms/bdqtest/index.md) - Provides a concise, easy-to-read reference about the BDQ Tests.
- **BDQ User's Guide** - For anyone interested in how to use the BDQ Tests in practice. This document.
- [**BDQ Implementer's Guide**](../implementers/index.md) - For anyone interested in the technical implementation of the BDQ Tests.
- [**BDQ Supplemental Information**](../../supplement/index.md) - This supplementary information may be relevant for curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners who wish to understand, evaluate and/or improve the quality of biodiversity data within their domain. This document provides some key developmental issues in the building of the BDQ standard that are not covered in other documents within the standard. This document may also be useful to those seeking to evaluate their current Tests or generate additional Tests for their domain.

### 1.4 Status of the content of this document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

### 1.5 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| ac:          | https://rs.tdwg.org/ac/terms/               |

### 1.7 Referring to Terms (normative)

In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., `https://rs.tdwg.org/bdqffdq/terms/` for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (skos:prefLabel, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. You will find all of these methods of referring to BDQ-related terms throughout the BDQ documentation.

## 2 Context for Quality, Uses and Purposes (non-normative)

Data do not have quality in the abstract; they only have quality with respect to a particular use. The Fitness for Use Framework (see [Fitness For Use Framework Ontology Guide](../bdqffdq/index.md)) in the BDQ standard describes uses for data as `Use Cases`.

A set of `Tests` appropriate to a`Use Case` is run on a set of data and a `Data Quality Report` is produced. Both the Tests and the associated report should be interpreted in the context of that `Use Case`.

More formally, Tests are run in suites that form `Policy` for data quality with respect to `Use Cases`.   More importantly, sets of Tests are expected to be run together in order to assess the quality of data for some specified use, and both Tests and the reports of their results should be interpreted in the context of that specified use.  Just as data do not have quality in the abstract, the results of a test on some data have meaning only in the context of a particular use.

More broadly, the concept of fitness for purpose refers to whether data are adequate to support a given goal or objective beyond the immediate use — such as policy formulation, scientific modeling, or legal compliance. Achieving fitness for purpose may involve additional considerations such as provenance, trustworthiness, and completeness, and it is possible to frame additional Tests to assess these `Dimensions` of data quality.

## 2.1 Quality Control and Quality Assurance (non-normative)

Tests for data quality may serve two purposes: Quality Control and Quality Assurance. 

- In Quality Assurance (QA), data are evaluated for fitness for use and are filtered down to just those data that are fit for that use.

- In Quality Control (QC), Tests are used to identify data that are not fit for particular uses, with the goal of improving the data quality, and the tests may propose changes to improve the quality of the data.

The success of `Quality Assurance` and `Quality Control` depends on organisational context and resources. These include establishing clear validation, monitoring, and feedback procedures to maintain high quality data, and encouraging collaboration among data custodians, analysts, and end-users to ensure data quality aligns with practical needs and supports reliable decisions. It also requires developing formal methodologies to understand and process the Test outputs in the `Data Quality Reports`.

### 2.1.1 Quality Assurance (non-normative)

The Fitness for Use Framework (Veiga 2016, Veiga et al., 2017) provides a formal means for filtering records for [Quality Assurance](../../bdqffdq/index.md#3447-quality-assurance-normative) (involving only Measures), but informally, data may be thought of as being fit for some use if all `Validation` Tests comprising that `Use Case` have a `Response.result`="COMPLIANT", and all non-numeric `Measure` Tests comprising that `Use Case` have a `Response.result`="COMPLETE". The BDQ Tests include a set of `Multi Record` `Measures` whose purpose is to enable formal filtering (Quality Assurance) and reporting (for Quality Control) under the [Fitness for Use Framework Ontology](../../bdqffdq/index.md).

### 2.1.2 Quality Control (non-normative)

The Framework provides a formal statement of [Quality Control](../../bdqffdq/index.md#3446-quality-control-normative), but the application of Quality Control 'in the wild' is more nuanced; more complex than simple filtering under Quality Assurance. The context of Quality Control may affect how Tests and their results are applied to data, information systems and processes.

Quality Control is most efficient at the time of data capture where the prevention of incorrect values avoids subsequent, far less efficient issue detection and correction. For example, issues such as transposition of values are far easier to detect and correct at the point of recording than during subsequent downstream processing where context may be lost or held on paper records remote from data entry, and errors may be propagated. `Validation` Tests may be thought of as framing constraints to impose on data entry interfaces, such as validation of data against a controlled vocabulary being imposed by the presentation of the controlled vocabulary as a pick list in a user interface, or they may be implemented as checks on entered data values with immediate feedback for users. 

When `Data Quality Reports` result from the analysis of data in databases of record, numerous reports of INTERNAL_PREREQUISITES_NOT_MET or NOT_COMPLIANT are likely, particularly in historical data where data values may be poorly known, or data may have passed through multiple life cycles of collection management systems. In a database of record, the focus of the quality control processes is very likely on the identification of tractable targeted data cleanup projects. Such data cleanup projects can involve multiple staff with different skills and are likely to last for long periods of time. Data cleaning projects are expensive, and `Data Quality Reports` driven by Tests organized by `Use Cases` can be an effective management tool for identifying and prioritizing suitable and tractable projects for data cleanup. 

Complicating the analysis of `Data Quality Reports` on databases of record is that when relational database tables are denormalized to flat files for analyses and reporting, propagated errors could trace back to a single 'point of failure'. What appear in reports as large numbers of errors may result from a single problem in a single record of a relational table. A clear understanding of the structure of a database of record is needed to interpret `Data Quality Reports` into targeted data cleanup projects. The keys for applying `Data Quality Reports` to improvement of databases of record is identification of focused areas for data cleanup projects, and identification of places where data quality problems may be reduced by improvements to workflow processes or user interfaces for entry and manipulation of data. Some `Validation` Tests may point to places where controlled vocabularies should be in use but are not, suggesting a need for a coordinated set of changes. For example, splitting a single free text field into a controlled vocabulary field and a free text field for further elaboration, a data cleanup project to map all existing values onto a controlled vocabulary, and then changes to user interfaces to reflect the split into a controlled field and associated remarks.
 
Correcting issues subsequent to data capture introduces further complexities in that any amendment to existing values requires careful human evaluation and a forking of data records to maintain original data and an audit trail. Data cleaning often requires far more time than data analysis.

### 2.1.3 Quality Control in Data Aggregation (non-normative)

When a data provider is performing `Quality Control` while preparing data for aggregation (or when reports are provided by aggregators back to upstream data providers) analysis of the resulting reports can uncover both simple errors introduced in mapping data onto Darwin Core terms (e.g., field transpositions in mapping) as well as underlying problems in the data itself.   Data validation at this stage may also reveal cases where the database of record contains more authoritative information than the resource used as a `sourceAuthority` for a Test.  In such cases the data in the database of record could be correct even if a `Validation` Test returns `NOT_COMPLIANT`.  Careful analysis of `Quality Control` reports is essential, to understand the origin of potential problems, what changes may be acceptable in a database of record, and as data cleaning involves significant effort, it is essential to identify specific areas for targeted data cleaning projects.

`Quality Control` in downstream analysis of aggregated data faces other challenges. The volume of aggregated data is likely to be large, making it infeasible to either review all proposed `Amendments` or to report proposed changes to upstream databases of record. Quality Control in the workflow processing of data streams from large scale aggregation may include acceptance of proposals from `Amendments` into a data stream for downstream analysis. This should be done with some care in checking that the proposed `Amendments` are not introducing errors or false precision, and both unamended and amended data should be preserved, with accepted proposals from `Amendments` clearly identifiable as changes to the data stream.

## 3 A Guide to the Tests (non-normative)

The BDQ standard defines a set of Tests to assess the quality of biodiversity data. Implementations of these Tests may produce `Data Quality Reports`. The format of such `Data Quality Reports` may vary, but they should contain specific information about outputs from each Test. This guide describes the Tests, their inputs, expectations about their outputs, how they may be used for Quality Control and Quality Assurance, and describes the [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md), which gives the details of each BDQ Test. 

Biodiversity data encompasses information about the variety of life on Earth, including observations of where and when organisms were found. For example, a record of a bird sighting might include the date, location, and species name, along with additional observed details such as behavior, habitat, or physical characteristics.  The BDQ standard is designed to assess the quality of these data for a variety of uses, including research and conservation. Implementations of the BDQ Tests examine such `dwc:Occurrence` data expressed using Darwin Core terms. Darwin Core provides a standardized set of terms—a common vocabulary that allows different databases and researchers to share biodiversity data in a consistent way.

The BDQ Tests are each very specific. Some Tests are very simple and self-explanatory, such as the Test that asserts that the value of `dwc:day` should be an integer in the range 1 to 31. Other Tests reference external authoritative sources of information to evaluate data quality, these are referred to as source authorities. For example, testing values of `dwc:countryCode` involves comparison with the `sourceAuthority` that is the list of valid ISO country codes.

### 3.1 Test Types (non-normative)

There are four types of Tests: `Validation`, `Issue`, `Measure`, and `Amendment`. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into Test suites (`Policies`) that assess the fitness of data for a specific use (`Use Case`).  In the Fitness for Use Framework, `Policies` are the formal mechanism for linking a `Use Case` to the relevant `DataQualityNeed` instances (Tests).

**`Validation` Tests** can be thought of as fact-checking. They compare the data against known standards or rules. `Validation` Tests examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a `Criterion` for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD) where `dwc:countryCode` is checked against a `sourceAuthority` for validity.

**`Issue` Tests** can be thought of as warning flags. They don't necessarily mean the data are wrong, but they highlight something that might be a problem for some users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY) alerts users to a `NotEmpty` value that should be examined against their `Data Quality Needs`. 

**`Measure` Tests** can be thought of as metrics. `Measure` Tests either count things or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT), which returns the number of Tests of Type `Validation` that had a response of "NOT_COMPLIANT" on a record.

**`Amendment` Tests** can be thought of as suggestions for improvement. `Amendment` Tests examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and may propose changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_STANDARDIZED), where a valid ISO country code could be inferred.

### 3.2 Test Inputs and Outputs (non-normative)

#### 3.2.1 Inputs to Tests (non-normative)

Each Test is defined to take a specific set of input terms (`Information Elements`), generally [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021), but `Information Elements` may be from other vocabularies (such as [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), e.g. `dcterms:license`). The Test performs some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the BDQ `Validation`, `Issue`, and `Amendment` Tests examine a set of Darwin Core terms from a `Single Record` (e.g., from a single `dwc:Occurrence` record) rather than looking at the input term(s) over multiple records.

Consider the Test [VALIDATION_EVENTDATE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_STANDARD). It takes as input value of the `Information Element` `dwc:eventDate` from a `Single Record`, and then asks, "Is the value of dwc:eventDate a valid ISO date?". It will then produce a Response describing the conclusion it reached when analyzing that record.

Tests can also operate on a dataset (a `Multi Record`) and examine the values for `Information Elements` across the entire dataset. The only `Multi Record` Tests currently defined in BDQ are `Measures`, which take the outputs of `Single Record` Tests as their inputs and report on the results of those `Single Record` Tests aggregated across the dataset. The names of these Tests all begin with "MULTIRECORD_".  

#### 3.2.2 Outputs: Data Quality Reports (non-normative) 

Software that includes an implementation of one or more Tests may produce `Data Quality Reports`. The form that such `Data Quality Reports` may take is not specified by the BDQ standard, however, it does specify elements that should be present in such reports (see [7.1 Data Quality Reports (normative)](../implementers/index.md#71-data-quality-reports-normative) in the [Implementer's Guide](../implementers/index.md)).  A detailed discussion of how `Data Quality Reports` relate to the Tests can be found at [3.1](../../bdqtest/index.md#31-structure-of-response-normative) in the [BDQ Tests and Assertions Document](../../bdqtest/index.md).

#### 3.2.3 Outputs: Responses from Tests (normative) 

The specifications for the structure of a response from running a Test can be found in [3.1 Structure of Response (normative)](../../bdqtest/index.md#31-structure-of-response-normative) in the document [BDQ Tests and Assertions](../../bdqtest/index.md).

##### 3.2.3.1 Shorthand for Responses from Tests (non-normative) 

A `Data Quality Report` from a BDQ `Test` is expected to include a Response for each `Test` run.   

Response is shorthand for a formal Fitness for Use Framework concept: an instance of a subtype of `bdqffdq:Assertion` produced by running a Test, which carries a response status, result, comment and optional qualifier via the `bdqffdq:hasResponseStatus`, `bdqffdq:hasResponseResult`/`bdqffdq:hasResponseResultValue`, `bdqffdq:hasResponseComment`, and `bdqffdq:hasResponseQualifier` properties.

In brief, each Response consists of the following elements:

* __`Response.status`__ - Metadata describing the status of the `Test` run, including whether the `Test` was executed successfully.  Values include `RUN_HAS_RESULT`, `INTERNAL_PREREQUISITES_NOT_MET` and `EXTERNAL_PREREQUISITES_NOT_MET`.
* __`Response.result`__ - The result of the evaluation of the `Test` against the input data.  Values include "COMPLIANT", "NOT_COMPLIANT", "COMPLETE", "NOT_COMPLETE", or data values (such as numeric measurement values), depending on the type of `Test`.
* __`Response.comment`__ - A human-readable comment providing additional context or information to assist users in the interpretation of the `Test` result.

The presentation of a Response to users is not defined by the BDQ standard and will vary.

##### 3.2.3.2 Validation Test Reports (non-normative)

As `Validation` tests compare the data against known standards or rules, the `Response.result` for a `Validation` Test is expected to be either "COMPLIANT" or "NOT_COMPLIANT". 

The Test `VALIDATION_DAY_INRANGE` checks if the value of `dwc:day` is interpretable as a valid integer between 1 and 28 inclusive, or if it is validly 29, 30 or 31 given the `dwc:month` and `dwc:year`.

For example, where input data has `dwc:day` = "15" and no month or year; a Response may be: 

* `Response.status`=RUN_HAS_RESULT
* `Response.result`=COMPLIANT
* `Response.comment`="The provided value of dwc:day [15] is in range"

Alternatively, if the input data has values `dwc:day`="30", `dwc:month`="2", `dwc:year`="1952"; a Response may be:

* `Response.status`=RUN_HAS_RESULT
* `Response.result`=NOT_COMPLIANT 
* `Response.comment`="The provided value of dwc:day [30] is not in range for the provided dwc:month [2] and dwc:year [1952]".

The content of Response.comment is not defined by the BDQ standard and may vary, so phrasing such as "There was no day 30 in February of 1952" is also acceptable.

Another case is that the input data contain values that cannot be interpreted within the definition of the test, for example, where the input data has `dwc:day`="31", `dwc:month`="", `dwc:year`="1932"; a Response may specify that the test could not be evaluated because a prerequisite in the input data was not met, for example:

* `Response.status`=INTERNAL_PREREQUISITES_NOT_MET
* `Response.result`=
* `Response.comment`="The provided value of dwc:day [31] cannot be evaluated for compliance because the prerequisites of a valid dwc:month and dwc:year were not met for days between 29 and 31."

A Response.status of INTERNAL_PREREQUISITES_NOT_MET indicates that the data themselves did not meet the prerequisites for the test to be evaluated, and thus the test could not be evaluated, and will always return this result with the same input data. In contrast, a Response.status of EXTERNAL_PREREQUISITES_NOT_MET indicates that the test could not be evaluated because some external resource (e.g., a source authority) was not available at the time the test was run, and running the test again at a different time might yield a different result.

##### 3.2.3.3 Issue Test Reports (non-normative)

`Issue` Tests can be thought of as warning flags. These Tests provide a warning that an issue may need further investigation by a human who could determine what action should be taken.

If we look at the Test `ISSUE_DATAGENERALIZATIONS_NOTEMPTY`, the Test alerts users that there is value in the field that indicates that the data may have been generalized in some way.
For example, the field for `dwc:dataGeneralizations` may say "placed on quarter degree grid". A Response could be:

* `Response.status`=RUN_HAS_RESULT 
* `Response.result`=POTENTIAL_ISSUE 
* `Response.comment`="dwc:dataGeneralizations contains some value, these data have been generalized in some way and may or may not be fit for your use."

Alternatively, if there is nothing in the `dwc:dataGeneralizations` field, i.e. it is empty; the Response may be:

* `Response.status`=RUN_HAS_RESULT 
* `Response.result`=NOT_ISSUE 
* `Response.comment`="dwc:dataGeneralizations is bdq:Empty"

##### 3.2.3.4 Measure Test Reports (non-normative)

`Measure` Tests can be thought of as metrics. These Tests either count things or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE).  Almost all the `Measure` Tests defined in BDQ are `Multi Record` Tests that are powerful tools for formal support of `Quality Control` and `Quality Assurance` under the [Fitness for Use Framework Ontology](../../bdqffdq/index.md).  

There is one `Single Record` `Measure` Test that provides a metric on a Darwin Core term in a `Single Record`, MEASURE_EVENTDATE_DURATION_SECONDS, which provides a measure of the duration in seconds of the `dwc:eventDate`.  This test is intended to allow consumers of data quality reports to quickly identify records where the collecting event is known to a precision of about a day or less, or about a year or less, or any arbitrary time range that may be of interest to a particular use. 

For example, if the `dwc:eventDate` is "2020", the Response would be:

* `Response.status`=RUN_HAS_RESULT
* `Response.result`="31622400"
* `Response.comment`="The provided dwc:eventDate [2020] represents a time interval of a year that was a leap year, so it had 366 days or 31622400 seconds"

A calendar year is usually 31,536,000 seconds (365 days), but it is not always that simple: some years have 366 days (leap years), and in some time scales additional leap seconds may be inserted.  (Because of these complexities, it is not straightforward to make precise assertions such as “this `dwc:eventDate` represents a duration of less than a year".  Such complexities contributed to us not defining specific `Validation` Tests that would ask such questions, this measure allows users to determine what duration of event dates provides sufficient quality for their specific purposes.)

There are a small set of `Measures` that count the results of other tests run on the same `SingleRecord` one of these is the Test `MEASURE_AMENDMENTS_PROPOSED`, it provides a count of the number of Amendment Tests that proposed changes to that record.

For example, if 17 tests proposed amendments on a particular `SingleRecord`; the Response would be

* `Response.status`=RUN_HAS_RESULT 
* `Response.result`="17"
* `Response.comment`="17 Tests of TYPE AMENDMENT proposed changes to the record"

Most `Measure` Tests are `Multi Record` Tests that take as input the results of `Single Record` Test on some data set and provide metrics or filters on those data.  These support formal application of `Quality Control` and `Quality Assurance` and are not discussed further here.

##### 3.2.3.5 Amendment Test Reports (non-normative)

`Amendment` Tests can be thought of as suggestions for improvement. These Tests examine input values and may propose changes or additions to improve the quality (they could also propose changes to processes, but BDQ includes only `Amendments` that propose changes to data values).

If we look at the Test `AMENDMENT_DAY_STANDARDIZED`, the Test may suggest changing a value to comply with the requirements for `dwc:day`, i.e. that it is interpretable as a valid integer.

For example, for a record where the `dwc:day` is given as the "23rd" the suggestion may be to change this to "23" – a Response may be: 

* `Response.status`=AMENDED
* `Response.result`={dwc:day="23"} 
* `Response.comment`="The provided value for dwc:day [23rd] is interpretable as 23, which is compliant with the requirements for dwc:day, so the value has been standardized to 23."

Alternatively, for a record where the day is given as "X" which is ambiguous, the Response may be:

* `Response.status`=NOT_AMENDED
* `Response.result`=
* `Response.comment`="The provided value of dwc:day [X] is ambiguous."

### 3.3 Amendments Propose Changes (normative)

Amendment Tests **propose changes** to data. It is up to the consumers of `Data Quality Reports` to choose whether or not to accept those changes, particularly into an authoritative database of record. Consumers of `Data Quality Reports` MAY choose to change data based on `Assertions` made by `Amendment` Tests, or consumers of `Data Quality Reports` MAY choose to **not** change their data based on `Assertions` made by `Amendment` Tests. Databases of record SHOULD NOT **automatically** alter data based on `Assertions` made by `Amendment` Tests without human evaluation of the proposed changes.

#### 3.3.1 Caution in Proposing Changes (non-normative)

To maintain the integrity and reliability of the BDQ Framework, we have been careful to avoid proposing `Amendments` in cases where there is significant uncertainty — whether due to ambiguous data, unclear provenance, or unresolved conflicts between sources. This principle helps ensure that changes are justifiable and that the risks of introducing erroneous or misleading data through overcorrection are minimized.

### 3.4 Test Parameters (non-normative) 

Some tests are parameterized.  Parameters allow those running a Test to change the behavior of the test at the time it is run.  This allows users to easily adapt the tests to their specific needs and contexts, making them more flexible and applicable to a wider range of scenarios.  

For example, a user working with data from just one country may wish to change a default `bdq:sourceAuthority` for some test to an authority that is more appropriate for that particular country – e.g. to change the default species names authority (which covers the whole world) to one specific for just that country, all while retaining the same decision making process within the Test. For more details see [3.3](../../bdqtest/index.md#33-parameterizing-the-tests-normative) in the [BDQ Tests and Assertions](../../bdqtest/index.md) document.

Similarly a parameterized Test may change default numerical values to values more appropriate to the local area – e.g. setting a maximum elevation that is more appropriate to the country, rather than using a default global maximum, such that for some parameterized `Validation` elevations higher than the local maximum, but still lower than the global maximum elevation would be `NOT_COMPLIANT`, fitting the local needs, while they would be `COMPLIANT` and not identified as problematic for local needs if the default global maximum elevation were used.

### 3.4.1 Test Parameters in Reports (normative) 

When a Test is parameterized, and a value other than the default value is used for some `Parameter`, reports SHOULD identify the Tests using at least the Label (`rdfs:label`) for the Test class, in combination with the `Parameter` and the value of the `Argument` that replaced the `Parameter` in this specific case.

Values of `Parameters`, other than the defaults, SHOULD also be present in the `Response.comment`.

More normative guidance on Test `Parameters` can be found in the section [6.1 Parameters and Changing the Behavior of a Test (normative)](../implementers/index.md#61-parameters-and-changing-the-behavior-of-a-test-normative) of the [BDQ Implementer's Guide](../implementers/index.md).

#### 3.4.2 Test Parameters Example (non-normative) 

Consider the Test `VALIDATION_MAXELEVATION_INRANGE`.  If you are evaluating data that could come from anywhere in the world, you would want to use the default value for the 'Parameter' that sets the maximum elevation to that of the highest point on Earth.  However, if you are working on a dataset consisting entirely of data pertaining to locations in New Zealand, you may wish to set the `Parameter` bdq:maximumValidElevationInMeters value to the maximum elevation in New Zealand (i.e., 3724 meters).  

So, for a record where dwc:maximumElevationinMeters is given as "4500" which is out of range for New Zealand, the Response for the test with the default value for the parameter would be:

* `Response.status`=RUN_HAS_RESULT
* `Response.result`=COMPLIANT
* `Response.comment`="The provided value of dwc:maximumElevationInMeters [4500] is in range`.

But if the test is run on the same data, but with the parameter bqd:maximumValidElevationInMeters set to 3724, appropriate for New Zealand, the Response would be:

* `Response.status`=RUN_HAS_RESULT
* `Response.result`=NOT_COMPLIANT
* `Response.comment`="The provided value of dwc:maximumElevationInMeters [4500] is out of range using the non-default bdq:maximumValidElevationInMeters=3724`.

Thus the parameter changes the behavior of the test to fit local needs.

It is important to identify the use of non-default parameter values in reports, so that users can understand the context in the test results.

If a Test with a non-default `Parameter` value is used, this should be represented to consumers of data quality reports by combining at least the Label (`rdfs:label`) for the Test class (e.g., [VALIDATION_MINDEPTH_INRANGE](../../terms/bdqtest/index.md#VALIDATION_MINDEPTH_INRANGE)) in combination with the `Parameter` (e.g., `bdq:maximumValidDepthInMeters`) and the value of the argument that replaced the default `Parameter` value in this specific case (e.g., 1642). For example, a Data Quality Report could identify this Test as `VALIDATION_MAXDEPTH_INRANGE with bdq:maximumValidDepthInMeters=1642` rather than simply `VALIDATION_MAXDEPTH_INRANGE`

Similarly, Test Results should be accompanied by a `Response.comment` that includes text expressing something similar to "Non-default bdq:maximumValidDepthInMeters=1642" as in the example above.  Both are important to help users understand the context of test results, and to allow users to identify where non-default parameter values are used.

## 4 Using the BDQ Tests Quick Reference Guide (non-normative)

The [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) is a companion to this Guide and lists the Tests with a subset of Test descriptors. This subset is intended to provide a brief summary of the nature of each of the Tests that is sufficient for most cases. Some Test descriptors can be used to filter the Tests down to those that may be applicable for an application (`Use Case`). An index is provided for each Test by example `Use Case`. Both `Single Record` Tests (`Validations`, `Issues`, `Measures`, `Amendments`) and `Multi Record` Tests are included. Term definitions with the full set of Test descriptors can be found in the [BDQ Tests and Assertions List of Terms](../../list/bdqtest/index.md).

While the [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) provides a description of each individual BDQ Test, `Data Quality Reports` may vary in how they present results from the execution of these Tests. Possible presentations include displaying Test results individually, aggregating counts of results for each Test run over all records in a dataset, and separating results into pre- and post-amendment phases. In the latter case, results may be shown for all `Validation` and `Measure` Tests run in a pre-amendment phase, then proposals for changes from all `Amendment` Tests run in an amendment phase, and then results from the same `Validation` and `Measure` Tests run in a post-amendment phase as if all proposed changes from the `Amendment` Tests were evaluated and accepted. It is thus important to identify both the Test for which results are being reported, and the context for the report. The [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) describes what each Test does independent of this context.

For each Test, the [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) provides a set of test descriptors.  These include three ways to identify the Test, each serving a particular purpose:

* **Label:** - the brief human readable means for identifying a Test (e.g. VALIDATION_BASISOFRECORD_NOTEMPTY). The Label is expected to be the primary means for humans to identify a Test.  
* **skos:prefLabel:** - the human readable label spelled out in words (e.g. "Validation dwc:basisOfRecord` `Not Empty"). The prefLabel is expected to support translations, screen readers and other means for improving accessibility for humans in the identification of a Test.
* **Versioned IRI:** - the means for software to identify the Test (e.g. https://rs.tdwg.org/bdqtest/terms/version/ac2b7648-d5f9-48ca-9b07-8ad5879a2536-2023-09-17)). The Versioned IRI is the definitive identifier for a particular version of a Test and is intended for use by software.

The Quick Reference Guide also identifies whether a Test operates on `Single Records` or a `Multi Record` (a dataset). A brief description of what the Test is intended to do follows, with a more detailed description for implementers, consisting of `Expected Response`, `Information Elements` `Acted Upon` and `Consulted`, any `Parameters` that could change the behavior of the Tests, default values for any `Parameters` or `bdq:sourceAuthority` consulted by the Test.

Two Examples of Test data input and output are provided to illustrate opposing behaviors of the Test. For `Validation` Tests, one example provides a `Response.result`="COMPLIANT", the other "NOT_COMPLIANT". See the [BDQ Implementer's Guide](../implementers/index.md) for information about Test Validation Data. 

Each Test lists `Use Cases` describing `Data Quality Needs` to which each Test is applicable. Notes provide additional guidance for understanding Test results and for implementation.

The definitions of the terms used for the Tests can be found in [Terms Used in the BDQ Tests Quick Reference Guide](../../terms/bdqtest/bdqtest_qrg_term_descriptions.md).

## 5 Time of Day and Time Zones (non-normative)

Time of day (as opposed to dates) is not considered in any of the BDQ Tests. There are `Use Cases` where the time zone is important. Dates within a dataset (`bdqffdq:MultiRecord`) aggregated from multiple sources may have plus or minus one day errors introduced. New Tests are required if ignorance of time would make such data unfit for a purpose. For further information, see Section [4.2 Time (non-normative)](../../supplement/index.md#42-time-non-normative) in [BDQ Supplemental Information](../../supplement/index.md).

## 6 Dates and Calendars (non-normative)

Different calendars have been used at different times in different places, and the transcription of an original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date. Metadata may or not be present to even identify such records. For more details of how the differences in Calendar dates should be treated see Section [4.1 Dates and Calendars (non-normative)](../../supplement/index.md#41-dates-and-calendars-non-normative) in [BDQ Supplemental Information](../../supplement/index.md).

## 7 Creating New Tests (non-normative)

The `Tests` in the BDQ Standard are a subset of all the possible tests that could be developed for testing biodiversity data quality, even within the `Darwin Core` environment. [2.1 Definition of Core](../../supplement/index.md#21-definition-of-core-non-normative) in the [BDQ Supplemental Information](../../supplement/index.md) provides the background context as to why the current suite of Tests were chosen.

Users and communities are free to define, implement, and use their own tests for their own purposes, and may propose tests for inclusion within the BDQ Standard.

When considering development of a new Test, users are urged to first review existing Test proposals in GitHub that may be related to their intended Test. In particular, there are a number of Tests that were proposed but not included in BDQ and tagged "`Supplementary`", as well as Tests that were proposed but rejected and tagged "`DO_NOT_IMPLEMENT`".

The `Supplementary` Tests may provide a close match for a specific `Use Case`, or may provide a useful template to build from, and should be reviewed before proposing a new Test from scratch. The `DO_NOT_IMPLEMENT` Tests document proposals that were judged to be problematic; the accompanying comments describe the rationale for rejection and reviewing them can help avoid re-proposing Tests with similar issues.

Implementers are free to implement a subset of the `CORE` Tests, or `Supplementary` Tests, or new Tests when there is a particular data quality need within their domain - e.g., testing for a value of sub-genus against a taxonomic name authority or testing for a valid depth against maximum depth around the location of an observation. Note however, that an implementation of BDQ will only be compliant with the standard if all `Tests` for at least one `Use Case` are implemented. 

### 7.1 Elements of a New Test (non-normative)

Formally, the description of a Test is complex.  Informally, there are a few central elements that describe a test and what it does.  

* First, a Test serves some purpose. A Test evaluates some way in which data are fit for some purpose, thus each Test starts from one or more `Use Cases`. 
* Second, a Test operates on specific inputs, specific elements of data, these are the `Information Elements`.  
* Third, a Test has some specific purpose, described in simple language.  This is the Test Description.
* Fourth, this plain language description of the Test must be expanded into specific language that allows an implementer to understand exactly what code implementing a Test should do, and what outputs it should provide for different possible input values, this is the `Expected Response`.   
* Fifth, it is important to be clear whether a Test evaluates a `SingleRecord` or operates over multiple records in a data set (a `MultiRecord` test).

Tests may be expected to form related clusters, for example, a `Validation` that assesses whether the value of `ac:variantLiteral` in a `SingleRecord` is found in as a controlled value string in the Audiovisual Core variant: List of Terms, combined with an `Amendment` that proposes changes to values of `ac:variantLiteral` to conform them to that controlled vocabulary, combined with a `MultiRecord` `Measure` that counts the number of `COMPLIANT` values for the `Validation` evaluated for each record in a data set.  Under `QualityControl`, this `Measure` can evaluate how much the data set could be improved for some purpose if all the proposed changes from the `Amendment` were accepted (by running the tests in pre-amendment, amendment, and post-amendment phases) 

### 7.2 Proposing to add a Test to the BDQ Standard (non-normative)

To propose to add a Test to the BDQ Standard, follow the instructions provided by the BDQ Maintenance Group.

## 8 Creating New Use Cases (non-normative)

BDQ is based on `Use Cases`: An evaluation of data quality must be within the context of a `Use Case`.  In the Fitness for Use Framework, `Use Cases` are needs-layer concepts.
A `Use Case` is linked to sets of relevant Tests through `Policies` (e.g., `ValidationPolicy`, `IssuePolicy`, `MeasurementPolicy`, and `AmendmentPolicy`). Together, these `Policies` identify which Tests should be run for a given `Use Case` and, therefore, which `Assertions` about data quality are expected from running that set of Tests.

Five over-arching `Use Cases` have been used in the BDQ Standard. These were developed through the TDWG Biodiversity Data Quality Interest Group Task Group 3: Data Quality Use Cases (Rees and Nicholls, 2020). These, of course, are only a small subset of all possible `Use Cases` and users may wish to develop `Use Cases` for their own purposes.

### 8.1 Elements of a New Use Case (non-normative)

`Use Cases` are straightforward to describe.  A `Use Case` has a name, a description, and a list of Tests.  The list of Tests is expressed as four `Policies`, a `ValidationPolicy` comprised of the `Validations` related to the `Use Case`, an `AmendmentPolicy` listing related `Amendments`, a `MeasurementPolicy` listing related `Measures`, and an `IssuePolicy` listing any related `Issues`.   

### 8.2 Proposing to add a Use Case to the BDQ Standard (non-normative)

To propose to add a new `Use Case` to the BDQ Standard, follow the instructions provided by the BDQ Maintenance Group.

## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../../index.md#5-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## References (non-normative)

The references for the BDQ standard can be found in the [References (non-normative)](../../../index.md#7-references-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ User's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
