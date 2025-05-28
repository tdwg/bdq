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

[2 A Guide to the Tests (non-normative)](#2-a-guide-to-the-tests-non-normative)
  - [2.1 Test Types (non-normative)](#21-test-types-non-normative)
  - [2.2 Test Inputs and Outputs (non-normative)](#22-test-inputs-and-outputs-non-normative)
    - [2.2.1 Inputs to Tests (non-normative)](#221-inputs-to-tests-non-normative)
    - [2.2.2 Outputs: Data Quality Reports (non-normative)](#222-outputs-data-quality-reports-non-normative)
    - [2.2.3 Outputs: Responses From Tests (normative)](#223-outputs-responses-from-tests-normative)
  - [2.3 Amendments Propose Changes (normative)](#23-amendments-propose-changes-normative)
  - [2.4 Test Parameters (normative)](#24-test-parameters-normative)
    - [2.4.1 Test Parameters Example (non-normative)](#241-test-parameters-example-non-normative)

[3 Context for Quality, Uses and Purposes (non-normative)](#3-context-for-quality-uses-and-purposes-non-normative)

[4 Using the BDQ Tests Quick Reference Guide (non-normative)](#4-using-the-bdq-tests-quick-reference-guide-non-normative)

[5 Time of Day and Time Zones (non-normative)](#5-time-of-day-and-time-zones-non-normative)

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

### 1.7 Referring to Terms (normative)
In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., `https://rs.tdwg.org/bdqffdq/terms/` for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (skos:prefLabel, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. You will find all of these methods of referring to BDQ-related terms throughout the BDQ documentation.

## 2 A Guide to the Tests (non-normative)

The BDQ standard defines a set of Tests to assess the quality of biodiversity data. `Implementations` of these Tests may produce `Data Quality Reports`. The format of such `Data Quality Reports` may vary, but they should contain specific information about outputs from each Test. This guide describes the Tests, their inputs, expectations about their outputs, how they may be used for Quality Control and Quality Assurance, and describes the [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md), which gives the details of each BDQ Test. 

Biodiversity data encompasses information about the variety of life on Earth. This includes observations of where and when organisms were found (such as the date and location of a bird sighting including the species name, and potentially other details about its behavior, observed habitat, or physical characteristics. The BDQ standard is designed to assess the quality of these data for a variety of uses including research and conservation. `Implementations` of the Tests defined in BDQ examine such `dwc:Occurrence` data expressed using Darwin Core terms. Darwin Core is a standardized set of terms used to describe biodiversity data, it provides a common vocabulary that allows different databases and researchers to share information in a consistent way.

The BDQ Tests are each very specific. Some Tests are very simple and self explanatory, such as the Test that asserts that the value of `dwc:day` should be an integer in the range 1 to 31. Other Tests reference external authoritative sources of information to evaluate data quality, these are referred to as source authorities. For example, testing values of `dwc:countryCode` involves comparison with the `sourceAuthority` that is the list of valid ISO country codes.

### 2.1 Test Types (non-normative)

There are four types of Tests: `Validation`, `Issue`, `Measure`, and `Amendment`. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into Test suites (`Policies`) that assess the fitness of data for a specific use.

**Validation Tests** can be thought of as fact-checking. They compare the data against known standards or rules. `Validation` Tests examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a `Criterion` for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD) where `dwc:countryCode` is checked against a `sourceAuthority` for validity.

**Issue Tests** can be thought of as warning flags. They don't necessarily mean the data are wrong, but they highlight something that might be a problem for some users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY) alerts users to a `NotEmpty` value that should be examined against their `Data Quality Needs`. 

**Measure Tests** can be thought of as metrics. `Measure` Tests either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT), which returns the number of Tests of Type `Validation` that had a response of "NOT_COMPLIANT" on a record.

**Amendment Tests** can be thought of as suggestions for improvement. `Amendment` Tests examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and may propose changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_STANDARDIZED), where a valid ISO country code could be inferred.

### 2.2 Test Inputs and Outputs (non-normative)

#### 2.2.1 Inputs to Tests (non-normative)

Each Test is defined to take a specific set of input terms (`Information Elements`, generally [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021)), and then perform some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the BDQ `Validation`, `Issue`, and `Amendment` Tests examine a set of Darwin Core terms from a `Single Record` (e.g., from a single `dwc:Occurrence` record) rather than looking at the input term(s) over multiple records.

Consider the Test [VALIDATION_EVENTDATE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_STANDARD). It takes as input value of the `Information Element` `dwc:eventDate` from a `Single Record`, and then asks, "Is the value of dwc:eventDate a valid ISO date?". It will then produce a Response describing the conclusion it reached when analyzing that record.

Tests can also operate on a dataset (a `Multi Record`), and examine the values for `Information Elements` across the entire dataset. The only `Multi Record` Tests currently defined in BDQ are `Measures`, which take the outputs of `Single Record` Tests as their inputs and report on the results of those `Single Record` Tests aggregated across the dataset. The names of these Tests all begin with "MULTIRECORD_". 

#### 2.2.2 Outputs: Data Quality Reports (non-normative) 

Software that include an `Implementation` of a Test may produce `Data Quality Reports`. The form that such `Data Quality Reports` may take is not specified by the BDQ standard, however, it does specify elements that should be present in such reports (see [7.1 Data Quality Reports (normative)](../implementers/index.md#71-data-quality-reports-normative)) in the [Implementer's Guide](../implementers/index.md).

#### 2.2.3 Outputs: Responses From Tests (normative) 

The specifications for the structure of a response from running a Test can be found in [3.1 Structure of Response (normative)](../../bdqtest/index.md#31-structure-of-response-normative) in the document [BDQ Tests and Assertions](../../bdqtest/index.md).

### 2.3 Amendments Propose Changes (normative)

Amendment Tests **propose changes** to data. It is up to the consumers of `Data Quality Reports` to choose whether or not to accept those changes, particularly into an authoritative database of record. Consumers of `Data Quality Reports` MAY choose to change data based on `Assertions` made by `Amendment` Tests, or consumers of `Data Quality Reports` MAY choose to not change their data based on `Assertions` made by `Amendment` Tests. Databases of record SHOULD NOT automatically alter data based on `Assertions` made by `Amendment` Tests without human evaluation of the proposed changes.

### 2.4 Test Parameters (normative) 

Some Tests are parameterized. When a Test is parameterized, and a value other than the default value is used for some `Parameter`, reports SHOULD identify the Tests using at least the Label (`rdfs:label`) for the Test class, in combination with the `Parameter` and the value of the `Argument` that replaced the `Parameter` in this specific case.

Values of `Parameters`, other than the defaults, SHOULD also be present in the `Response.comment`.

More normative guidance on Test `Parameters` can be found in the section [6.1 Parameters and Changing the Behavior of a Test (normative)](../implementers/index.md#61-parameters-and-changing-the-behavior-of-a-test-normative) of the [BDQ Implementer's Guide](../implementers/index.md).

#### 2.4.1 Test Parameters Example (non-normative) 

If a Test with a non-default `Parameter` value is used, this should be represented with at least the Label (`rdfs:label`) for the Test class (e.g., [VALIDATION_MINDEPTH_INRANGE](../../terms/bdqtest/index.md#VALIDATION_MINDEPTH_INRANGE)) in combination with the `Parameter` (e.g., `bdq:maximumValidDepthInMeters`) and the value of the argument that replaced the default `Parameter` value in this specific case (e.g., 1642). For example:

	`VALIDATION_MAXDEPTH_INRANGE with bdq:maximumValidDepthInMeters=1642`

should be accompanied by a `Response.comment` that includes text expressing something similar to "Non-default bdq:maximumValidDepthInMeters=1642".

So, a value of `dwc:minimumDepthInMeters` of 2000m would be NOT_COMPLIANT in this case, while with the default value for that parameter (11000), it would be COMPLIANT.

## 3 Context for Quality, Uses and Purposes (non-normative)

Data do not have quality in the abstract; they only have quality with respect to a particular use. The Fitness for Use Framework (see [Fitness For Use Framework Ontology Guide](../../bdqffdq/index.md)) used in the BDQ standard describes uses for data as `Use Cases`, and expects that Tests are run in suites that form `Policy` for data quality with respect to those `Use Cases`. That is, sets of Tests are expected to be run together in order to assess the quality of data for some specified use, and both Tests and the reports of their results should be interpreted in the context of that use.

Tests for data quality may serve two purposes: Quality Control and Quality Assurance. 

- In Quality Control, Tests are used to identify data that are not fit for particular uses, with the goal of improving the data quality.

- In Quality Assurance, data are evaluated for fitness for use (i.e., whether they meet the requirements of specific operational tasks) and are filtered accordingly so that only data that are fit for use are included.

More broadly, the concept of fitness for purpose refers to whether data are adequate to support a given goal or objective beyond the immediate use — such as policy formulation, scientific modeling, or legal compliance. Achieving fitness for purpose may involve additional considerations such as provenance, trustworthiness, and completeness beyond what is required for fitness for use.

The Fitness for use Framework (Veiga 2016, Veiga et al., 2017) provides a formal means for filtering records for [Quality Assurance](../../bdqffdq/index.md#3447-quality-assurance-normative) (involving only Measures), but informally, data may be thought as being fit for some use if all `Validation` Tests comprising that `Use Case` have a `Response.result`="COMPLIANT", and all non-numeric `Measure` Tests comprising that `Use Case` have a `Response.result`="COMPLETE". The BDQ Tests include a set of `Multi Record` `Measures` whose purpose is to enable formal filtering (Quality Assurance) and reporting (for Quality Control) under the [Fitness for Use Framework Ontology](../../bdqffdq/index.md).

The Framework provides a formal statement of [Quality Control](../../bdqffdq/index.md#3446-quality-control-normative), but the application of Quality Control 'in the wild' is more nuanced; more complex than simple filtering under Quality Assurance. The context of Quality Control may affect how Tests and their results are applied to data, information systems and processes.

Quality Control is most efficient at the time of data capture where the prevention of incorrect values avoids subsequent, far less efficient issue detection and correction. For example, issues such as transposition of values are far easier to detect and correct at the point of recording than during subsequent downstream processing where context may be lost or held on paper records remote from data entry, and errors may be propagated. `Validation` Tests may be thought of as framing constraints to impose on data entry interfaces, such as validation of data against a controlled vocabulary being imposed by the presentation of the controlled vocabulary as a pick list in a user interface, or may be implemented as checks on entered data values with immediate feedback for users. 

When `Data Quality Reports` result from the analysis of data in databases of record, numerous reports of INTERNAL_PREREQUISITES_NOT_MET or NOT_COMPLIANT are likely, particularly in historical data where data values may be poorly known, or data may have passed through multiple life cycles of collection management systems. In a database of record, the focus of the quality control processes is very likely on the identification of tractable targeted data cleanup projects. Such data cleanup projects can involve multiple staff with different skills and are likely to last for long periods of time. Data cleaning projects are expensive, and `Data Quality Reports` driven by Tests organized by `Use Cases` can be an effective management tool for identifying and prioritizing suitable and tractable projects for data cleanup. 

Complicating the analysis of `Data Quality Reports` on databases of record is that when relational database tables are denormalized to flat files for analyses and reporting, propagated errors could trace back to a single 'point of failure'. What appear in reports as large numbers of errors may result from a single problem in a single record of a relational table. A clear understanding of the structure of a database of record is needed to interpret `Data Quality Reports` into targeted data cleanup projects. The keys for applying `Data Quality Reports` to improvement of databases of record is identification of focused areas for data cleanup projects, and identification of places where data quality problems may be reduced by improvements to workflow processes or user interfaces for entry and manipulation of data. Some `Validation` Tests may point to places where controlled vocabularies should be in use but are not, suggesting a need for a coordinated set of changes. For example, splitting a single free text field into a controlled vocabulary field and a free text field for further elaboration, a data cleanup project to map all existing values onto a controlled vocabulary, and then changes to user interface to reflect the split into a controlled field and associated remarks.
 
Correcting issues subsequent to data capture introduces further complexities in that any amendment to existing values requires careful human evaluation and a forking of data records to maintain original data and an audit trail. Data cleaning often requires far more time than data analysis.

When performing Quality Control while preparing data for aggregation, or when reports are provided by aggregators to upstream data providers, analysis of reports may reveal simple errors introduced in mapping data onto Darwin Core terms. For example, field transpositions in mapping in addition to underlying problems in the data. Validation, particularly at this step may reveal cases where the a database of record holds more authoritative information than an upstream resource relied upon by the aggregator (or a `sourceAuthority` for a Test), and is correct despite NOT_COMPLIANT `Validation` Test results. Careful analysis of data Quality Control results is needed, with a need to identify focused areas for data cleaning projects, as they involve a significant effort.

Quality Control to improve data during downstream analysis of aggregated data has other challenges. The volume of aggregated data may be large enough to make both examination of the proposed `Amendments` and reporting of proposed changes to upstream databases of record infeasible. Quality Control in the workflow processing of data streams from large scale aggregation may include acceptance of proposals from `Amendments` into a data stream for downstream analysis. This should be done with some care in checking that the proposed `Amendments` are not introducing errors or false precision, and both unamended and amended data should be preserved, with accepted proposals from `Amendments` clearly identifiable as manipulations of the data stream.

To maintain the integrity and reliability of the BDQ Framework, we have been careful to avoid proposing `Amendments` in cases where there is significant uncertainty — whether due to ambiguous data, unclear provenance, or unresolved conflicts between sources. This principle helps ensure that changes are justifiable and that the risks of introducing erroneous or misleading data through overcorrection are minimized.

## 4 Using the BDQ Tests Quick Reference Guide (non-normative)

The [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) is a companion to this Guide and lists the Tests with a subset of Test descriptors. This subset is intended to provide a brief summary of the nature of each of the Tests that is sufficient for most cases. Some Test descriptors can be used to filter the Tests down to those that may be applicable for an application (`Use Case`). An index is provided for each Test by example `Use Case`. Both `Single Record` Tests (`Validations`, `Issues`, `Measures`, `Amendments`) and `Multi Record` Tests (at this time only `Measures` that evaluate the output of `Single Record` `Validations` across a dataset) are included. Term definitions with the full set of Test descriptors can be found in the [BDQ Tests and Assertions List of Terms](../../list/bdqtest/index.md).

While the [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) provides a description of each individual BDQ Test, `Data Quality Reports` may vary in how they present results from the execution of these Tests. Possible presentations include displaying Test results individually, aggregating counts of results for each Test run over all records in a dataset, and separating results into pre- and post-amendment phases. In the latter case, results may be shown for all `Validation` and `Measure` Tests run in a pre-amendment phase, then proposals for changes from all `Amendment` Tests run in an amendment phase, and then results from the same `Validation` and `Measure` Tests run in a post-amendment phase as if all proposed changes from the `Amendment` Tests were evaluated and accepted. It is thus important to identify both the Test for which results are being reported, and the context for the report. The [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) describes what each Test does independent of this context.

For each Test, the [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md) lists ways to identify the Test (**Label:** - the brief human readable means for identifying a Test; **skos:prefLabel:** - the human readable label spelled out in words; **Versioned IRI:** - the means for software to identify the Test). The Quick Reference Guide identifies whether a Test operates on `Single Records` or a `Multi Records` (a dataset). A brief description of what the Test is intended to do follows, with a more detailed description for implementers, consisting of `Specification`, `Information Elements` `Acted Upon` and `Consulted`, any `Parameters` that could change the behavior of the Tests, default values for any `bdq:sourceAuthority` consulted by the Test, or other `Parameters`.

Two Examples of Test data input and output are provided to illustrate opposing behaviors of the Test. For `Validation` Tests, one example provides a `Response.result`="COMPLIANT", the other "NOT_COMPLIANT". See the [BDQ Implementer's Guide](../implementers/index.md) for information about Test Validation Data. 

Each Test lists `Use Cases` describing `Data Quality Needs` to which each Test is applicable. Notes provide additional guidance for understanding Test results and for implementation.

The definitions of the terms used for the Tests can be found in [Terms Used in the BDQ Tests Quick Reference Guide](../../terms/bdqtest/bdqtest_qrg_term_descriptions.md).

## 5 Time of Day and Time Zones (non-normative)

Time of day (as opposed to dates) is not considered in any of the BDQ Tests. There are `Use Cases` where the time zone is important. Dates within a dataset (`bdqffdq:MultiRecord`) aggregated from multiple sources may have plus or minus one day errors introduced. New Tests are required if ignorance of time would make such data unfit for a purpose. For further information, see Section [4.2 Time (non-normative)](../../supplement/index.md#42-time-non-normative) in [BDQ Supplemental Information](../../supplement/index.md).
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
