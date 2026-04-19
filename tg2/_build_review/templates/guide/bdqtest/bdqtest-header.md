<!--- Template for header, values provided from yaml configuration --->
# {document_title}

**Title**<br>
{document_title}

**Date version issued**<br>
{ratification_date}

**Date created**<br>
{created_date}

**Part of TDWG Standard**<br>
<{standard_iri}>

<!--
**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}
-->

**This version**<br>
<{current_iri}{ratification_date}>

**Latest version**<br>
<{current_iri}>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
{abstract}

**Authors**<br>
{authors}

**Creator**<br>
{creator}

**Bibliographic citation**<br>
{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

**Status**<br>
{comment}

{toc}

## 1 Introduction (non-normative)

This document provides both normative specifications and explanatory guidance for the BDQ Tests. It defines how each Test is modeled using standard vocabulary terms and how conforming implementations are expected to behave under various conditions. It also distinguishes among Test types (`Validation`, `Issue`, `Measure`, and `Amendment`), outlines the semantics of single- versus multi-record evaluation, and explains how `Parameters` influence Test behavior. The content here provides the foundation for interpreting BDQ Test descriptions and for implementing BDQ-conformant test suites and reports.  This document also provides context on the role of Tests within the broader BDQ standard, including their relationship to `Use Cases`, `Policies`, and `Implementations` and the products that result from running Tests, `Responses` and `Data Quality Reports`.

Data quality is an evolving field, and there will always be "one more test" that we could conceive. BDQ focuses on a suite of Tests that have reached community consensus.  By mapping these tests across key Darwin Core terms, BDQ provides high coverage for the data that researchers use the most. The BDQ framework is modular and extensible: communities may define additional Tests to address domain-specific needs, and future versions of the standard may incorporate new Tests as consensus and practice evolve. Within BDQ, Tests are applied in the context of the use of data (`Use Cases` via `Policies`), allowing users select and apply Tests relevant to their stated data quality needs.

### 1.1 Purpose (non-normative)

The purpose of this document is to define and explain the BDQ Tests — the primary mechanism for evaluating the quality of biodiversity data in the BDQ standard.  This document describes the structure, types, and formal characteristics of the Tests, along with description of their context within BDQ, providing a clear and consistent specification that can be used by implementers, analysts, and quality assessors.

### 1.2 Audience (non-normative)

This document is intended for audiences who need a detailed understanding of the BDQ Tests, including:

- Data quality specialists configuring or analyzing BDQ Test outputs
- Software developers and data platform architects implementing BDQ Tests
- Researchers and data managers evaluating dataset readiness for specific uses
- Standards developers integrating BDQ Test logic into broader biodiversity data infrastructures.

While familiarity with controlled vocabularies and RDF modeling may be useful, this document is designed to be accessible to both technical and semi-technical users who want to understand, apply, or extend BDQ Tests.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../index.md).

The set of information most relevant to the Biodiversity Data Quality (BDQ) Tests can be found in the following subset of resources:

- **BDQ Tests and Assertions** - This document. Defines how each Test is modelled using standard vocabulary terms and how it should behave under various conditions.
- [**BDQ Tests Quick Reference Guide**](../terms/bdqtest/index.md) - Provides a concise, easy-to-read reference about the BDQ Tests.
  - [BDQ Test Index by Use Case](../terms/bdqtest/qrg_index_by_usecase.md)
  - [BDQ Test Index by Information Element Acted Upon](../terms/bdqtest/qrg_index_by_ie_actedupon.md)
  - [BDQ Test Index by Information Element Class](../terms/bdqtest/qrg_index_by_ie_class.md)
  - [BDQ Test Index by Data Quality Dimension](../terms/bdqtest/qrg_index_by_dimension.md)
  - [BDQ Multi Record Measure Test Index](../terms/bdqtest/qrg_multirecord_index.md)
- [**BDQ Tests and Assertions List of Terms**](../list/bdqtest/index.md) - Provides the complete normative definitions of the BDQ Tests.
- [**BDQ User's Guide**](../guide/users/index.md) - For anyone interested in how to use the BDQ Tests in practice.
- [**BDQ Implementer's Guide**](../guide/implementers/index.md) - For anyone interested in the technical implementation of the BDQ Tests.

#### 1.3.1 Term List Distributions for the BDQ Standard (non-normative)

<!--- This same table appears in bdqtest_termlist_header. Edit here, edit there. --->
| Description | IRI | Download URL | Notes | 
| ----------- | --- | -----------  | ----- | 
| HTML file   | TBD | [BDQ Tests and Assertions List of Terms](../list/bdqtest/index.md) | Complete term list for the bdqtest: vocabulary as a web page. | 
| RDF/XML file | TBD | [Tests in RDF/XML](../../dist/bdqtest.xml) | An RDF representation of the Tests in an RDF/XML serialization. | 
| Turtle file | TBD | [Tests in Turtle](../../dist/bdqtest.ttl) | An RDF representation of the Tests in a Turtle serialization. | 
| JSON-LD file | TBD | [Tests in JSON/LD](../../dist/bdqtest.json) | An RDF representation of the Tests in a JSON-LD serialization. | 
| CSV file | TBD | [Tests in CSV](../../vocabulary/bdqtest_term_versions.csv) | CSV file listing all BDQ Tests. | 
| Single Record Test CSV file | TBD | [Single Record Tests in CSV](../../dist/bdqtest_singlerecord_tests_current.csv) | CSV file listing just the Single Record Tests. |
| Multi Record Test CSV file | TBD | [Multi Record Tests in CSV](../../dist/bdqtest_multirecord_tests_current.csv) | CSV file listing just the Multi Record Tests. |

### 1.4 Status of the Content of this Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

### 1.5 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace Abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | http://www.w3.org/ns/oa#                    |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |


### 1.7 Referring to Terms (normative)

In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., `https://rs.tdwg.org/bdqffdq/terms/` for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (`skos:prefLabel`, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. The BDQ documents use all these methods.

## 2 A Brief Context for the BDQ Tests (non-normative)

The terminology of BDQ is based primarily on the Fitness for Use Framework (Veiga 2016, Veiga et al. 2017, Biodiversity Information Standards (TDWG) Task Group 1) expressed as an ontology, but additional vocabularies are required for a complete description of the Tests and how to use them. See [3.4 Vocabularies](../../index.md#34-vocabularies-non-normative) in [The Biodiversity Data Quality (BDQ) Standard](../../index.md).

BDQ Tests focus on values of a subset of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) composed as `bdqffdq:InformationElements` as inputs (along with optional `Parameters`) to the Tests.  Tests have defined outputs expressed as `Responses` and specifications of what input values should produce what `Responses`.  Each Test is independent, to support the mixing and matching of Tests to meet particular data quality needs and not impose a particular model of Test execution on implementation frameworks. Tests may execute in parallel, on data records in sequence, as queries on datasets and on unique values. Tests are paired in that all `Amendment` Tests are matched with a corresponding `Validation` Test that assesses some aspect of data quality. An `Amendment` Test may propose improvements to term values, but the BDQ standard recommends that all proposed improvements be evaluated before application.

Some BDQ Tests also require reference to external data such as standard vocabularies of terms or names.

The emphasis in BDQ is on Tests that evaluate values from a `Single Record` (`bdqffdq:SingleRecord`). Test results may also be accumulated across multiple records (`bdqffdq:MultiRecord`). Tests that accumulate information about results across multiple records are necessary for formal application of Quality Assurance and Quality Control principles.

### 2.1 What is meant by "Test"? (non-normative)

We use the capitalized term "Test" to mean something specific in the BDQ Standard. A Test is any instance of a subclass of `bdqffdq:DataQualityNeed` (e.g., `bdqffdq:Validation`) composed with an instance of a subclass of `bdqffdq:Method` (e.g., `bdqffdq:ValidationMethod`) composed with an instance of `bdqffdq:Specification`. When run by a `bdqffdq:Implementation`, each BDQ Test can produce a `bdqffdq:DataQualityReport` consisting of `bdqffdq:Responses`. See the diagram in [What is a "Test"](../../index.md#511-what-is-a-test-non-normative) in [The Biodiversity Data Quality (BDQ) Standard](../../index.md).

The scope of each BDQ Test is largely provided by the properties of a `bdqffdq:Specification`. The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) used in the specification are included in the `Information Elements` (`bdqffdq:InformationElement`). The specification also includes references to external authorities (external to the test specification, and usually also external to the Darwin Core standard, Wieczorek et al. 2012) that are required to implement the Test, for example, references to an ISO standard or a GBIF maintained controlled vocabulary. Such authoritative references are listed under `sourceAuthority` (`bdq:sourceAuthority`) with a link to the authority and optionally, a link to a specific online resource required for the `Implementation` of the Test.

Each BDQ Test is defined to operate on a `SingleRecord` or a `MultiRecord`. The Framework allows `MultiRecord` Tests to take data as input, for example to able to identify outliers within a dataset, or for `MultiRecord` Tests that take the output of `SingleRecord` tests as their input to provide an assessment of quality across the dataset.  No BDQ `MultiRecord` Tests have been defined to take data as input (but such could be defined).  No BDQ `SingleRecord` Tests have been defined to use data in other records within a dataset to evaluate the quality of data in a `Single Record` (but such could be defined).  The only `Multi Record` Tests included in BDQ accumulate the outputs of other Tests.

### 2.2 Use Cases (non normative)

BDQ Tests are designed to be applied in the context of particular uses of data. The BDQ standard defines a set of `Use Cases` that represent common uses of biodiversity data. Each `Use Case` is associated with one or more Tests that can be used to evaluate whether data meet that need. By applying the appropriate Tests for a given `Use Case`, users can assess the fitness of their data for that particular use and identify areas for improvement.

BDQ defines five 'Use Cases`.  These use cases were based on the work of Data Quality Task Group 3 ([Data Quality Use Cases](https://www.tdwg.org/community/bdq/tg-3/)). The BDQ Tests can only relate to the concept of ‘quality’ as a consequence of their application to a specific use case.  The five use cases included in the BDQ standard were intended to cover a range of applications that were considered in common use, but they are far from being comprehensive. The use cases were intended as a template or guide for those who may want to generate other use cases for their environments.  See the [Tutorial](../tutorial/index.md) for a step-by-step example of how to define a `Use Case` and select appropriate Tests for that `Use Case`.

The BDQ `Use Cases` are:
* [bdq:Alien-Species](../list/bdq/index.md#bdq_Alien-Species)
* [bdq:Biotic-Relationships](../list/bdq/index.md#bdq_Biotic-Relationships)
* [bdq:Record-Management](../list/bdq/index.md#bdq_Record-Management)
* [bdq:Spatial-Temporal_Patterns](../list/bdq/index.md#bdq_Spatial-Temporal_Patterns)
* [bdq:Taxon-Management](../list/bdq/index.md#bdq_Taxon-Management)

Under the principle that data has quality only with respect to use, each of the BDQ Tests is allocated to at least one `Use Case`.  Note that there is a many-to-many relationship here: One BDQ Test can be in multiple `Use Cases` and one `Use Case` may have many associated BDQ Tests, with `Policies` relating Tests to `Use Cases`.  See [Compliance depends on Use Case](../guide/implementers/index.md#31-compliance-depends-on-use-case-normative) in the Implementer's Guide for further explanation.

## 3 Test Types (non-normative)

The concept of 'Tests' in the context of BDQ include four distinct types: `Validation` (`bdqffdq:Validation`); `Issue` (`bdqffdq:Issue`); `Amendment` (`bdqffdq:Amendment`) and `Measure` (`bdqffdq:Measure`).

### 3.1 Validation Tests (normative)

Each `Validation` Test is composed of an instance of `bdqffdq:Validation` (which expresses a data quality need in the abstract) with an instance of `bdqffdq:ValidationMethod` linking it to an instance of a `bdqffdq:Specification` (which gives details of how that data quality need is to be concretely assessed).

`Validation` Tests in BDQ evaluate values in one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) for fitness for a particular `Data Quality Need`. In some cases, `Validation` Tests check for the presence or the lack of a value. `Validation` Tests are phrased as positive statements consistent with the Fitness For Use Framework (Veiga 2016, Veiga et al. 2017). For example, [VALIDATION_TAXONRANK_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_TAXONRANK_NOTEMPTY) will return a `Response.status`="RUN_HAS_RESULT" and `Response.result`="COMPLIANT" if a record being tested contains a value in `dwc:taxonRank`, rather than being phrased in the negative (i.e., VALIDATION_TAXONRANK_EMPTY) and flagging a potential problem. Data are found to be fit for some use if all `Validations` comprising a corresponding `Use Case` have a `Response.result`="COMPLIANT".

The response of a `Validation` Test (i.e., an instance of a `bdqffdq:ValidationResponse`) MUST take one of three forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., a `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` (`bdqffdq:InformationElement`) are such that the Test cannot be meaningfully run.
3. A `Response.status` of "RUN_HAS_RESULT" when the prerequisites for running the Test have been met, and in this situation:
  - A `Response.result` of either "COMPLIANT" if the values of the `Information Elements` (`bdqffdq:InformationElement`) meet the `Criteria`, or "NOT_COMPLIANT" if they do not.

In each case, a `Response.comment` MUST be present with text explaining to consumers of the `Data Quality Report` why the Test produced this response in this case.

### 3.2 Issue Tests (normative)

Each Issue Test is composed of an instance of `bdqffdq:Issue` (which expresses a data quality need in the abstract) with an instance of `bdqffdq:IssueMethod`, which links it to an instance of a `bdqffdq:Specification` (which gives details of how that data quality need is to be concretely assessed).

`Issue` Tests are a form of warning flag where the Test is drawing attention to potential problem with the value of an `Information Element` for at least one use of the data.

We have used `Issue` Tests for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of these cases would take human review. For example, the Test [ISSUE_ANNOTATION_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_ANNOTATION_NOTEMPTY) is informing the tester than there is at least one annotation associated with a record and this should be evaluated before using the record. Similarly for the other two `Issue` Tests: [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY) where some form of transformation has occurred, and the Test [ISSUE_ESTABLISHMENTMEANS_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_ESTABLISHMENTMEANS_NOTEMPTY) where the value needs to be assessed for utility.

The response of an `Issue` Test (an instance of a `bdqffdq:IssueResponse`) MUST take one of three forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., a `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result. In this case, the `Response.result` MUST be empty.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` are such that the Test cannot be meaningfully run. In this case, the `Response.result` MUST be empty.
3. A `Response.status` of "RUN_HAS_RESULT" when the prerequisites for running the Test have been met, and in this case:
  - A `Response.result`="POTENTIAL_ISSUE", a `Response.result`="NOT_ISSUE", or a `Response.result`="IS_ISSUE".

In each case, a `Response.comment` MUST be present with text explaining to consumers of the `Data Quality Report` why the Test produced this response in this case.

None of the currently defined BDQ Issue Tests return a `Response.result` of IS_ISSUE.

### 3.3 Measure Tests (normative) 

Each `Measure` Test is composed of an instance of `bdqffdq:Measure` (which expresses how to measure fitness of data for a data quality need in the abstract) with an instance of `bdqffdq:MeasurementMethod`, which links it to an instance of a `bdqffdq:Specification` (which gives details of how that data quality is to be measured).

`Measure` Tests return a `Response.result` of either a numeric value or one of the values "COMPLETE" or "NOT_COMPLETE". `Measure` Tests may directly measure properties of data. Alternatively, `Measure` Tests may measure the outputs of other Tests, for example, a `Measure` may count the number of `Response.results` from all COMPLIANT `Validation` Tests run on a `bdqffdq:SingleRecord`.

The only `Measure` defined in the BDQ standard that directly examines data is the Test [MEASURE_EVENTDATE_DURATIONINSECONDS](../terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS). This Test returns a `Response.result` measuring the amount of time represented by the value in `dwc:eventDate`, and can be used in Quality Assurance under specific research `Data Quality Needs` to identify `dwc:Occurrences` where the date observed or collected is known well enough for particular analytical needs (e.g., to at least one day for phenology studies, to at least one year for other purposes). The Test basically interprets the results of running the `Validation` and `Amendment` Tests and provides an indication of the length of the period of the value of `dwc:eventDate`.

Most `Single Record` `Measure` Tests defined in the BDQ standard count the number of `Validation` or `Amendment` Tests with a specified `Response.result` from a `Single Record` Test.

The response of a `Measure` Test (an instance of a `bdqffdq:MeasureResponse`) MUST take one of three forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., a `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result. In this case, the `Response.result` MUST be empty.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` are such that the Test cannot be meaningfully run. In this case, the `Response.result` MUST be empty.
3. A `Response.status` of "RUN_HAS_RESULT" when the prerequisites for running the Test have been met, and in this case either:
  - a `Response.result`="COMPLETE", or a `Response.result`="NOT_COMPLETE".
or
  - a `Response.result` containing a single number.

In each case, a `Response.comment` MUST be present with text explaining to consumers of the `Data Quality Report` why the Test produced this response in this case.

### 3.4 Amendment Tests (normative) 

Each `Amendment` Test is composed of an instance of `bdqffdq:Amendment` (which expresses how to improve data to fit a data quality need in the abstract) with an instance of `bdqffdq:AmendmentMethod`, which links it to an instance of a `bdqffdq:Specification` (which gives details of how proposals could be made to improve data for that need).

An `Amendment` Test MAY propose a change to one or more Darwin Core term values, or MAY propose to fill in missing values. The `Response` produced by an `Amendment` is intended to improve one or more components of the quality of the record. The `Response.result` from an `Amendment` MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database of record when a `Data Quality Report` is used for Quality Control of an existing database of record. Consumers of `Data Quality Reports` under Quality Assurance uses MAY choose to accept all proposed `Amendments` as part of a pipeline in preparing data for an analysis. `Amendments`, under the Fitness For Use Framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in the BDQ Tests at the time of first release.

The response of an `Amendment` Test (an instance of a `bdqffdq:AmendmentResponse`) MUST take one of four forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` are such that the Test cannot be meaningfully run.
3. A `Response.status` of "FILLED_IN" when the prerequisites for running the Test have been met and a proposal is made to fill in a value for one or more input terms that were `Empty`, and in this situation:
  - A `Response.result` containing a list of key-value pairs of the terms for which values are to be filled in, and the proposed new values for those terms.
4. A `Response.status` of "AMENDED" when the prerequisites for running the Test have been met and a proposal is made to change a value for one or more input terms that were Empty, and in this situation:
  - A `Response.result` containing a list of key-value pairs of the terms for which new values are proposed, and the proposed new values for those terms.

In each case, a `Response.comment` MUST be present with text explaining to consumers of the `Data Quality Report` why the Test produced this response in this case.

### 3.5 Single Record and Multi Record Tests (non-normative) 

Tests may operate on a `Single Record` (e.g., one row of [Simple Darwin Core](https://dwc.tdwg.org/simple/)) or on a `Multi Record` (a dataset).

The BDQ [Fitness for Use Framework](../bdqffdq/index.md) allows for Tests of all types to operate on either (`bdqffdq:hasResourceType`) `Single Record` or `Multi Record`. In the BDQ standard, the only `Multi Record` Tests that have been defined are `Measures`. We refer to these as `Multi Record` `Measures` (instances of `bdqffdq:Measure` that are the subject of a `bdqffdq:hasResourceType` property whose object is `bdqffdq:MultiRecord`).

The focus of the BDQ Tests are the `Single Record` Tests. To allow for standard means for summarizing the results of these Tests, and for filtering data under Quality Assurance, we have also defined two sets of `Multi Record` `Measures`.

In the BDQ standard, for each `Single Record` `Validation` Test, we have defined a `Multi Record` `Measure` Test that returns a `Response.result`="COMPLETE" when all records in the `Multi Record` have a `Response.result`="COMPLIANT", and a `Response.result`="NOT_COMPLETE" when they are not. Under Quality Assurance, these `Measure` Tests are the key criterion for identifying data that have quality for a `Use Case`. Under Quality Assurance, a `Multi Record` is filtered to remove records that do not fit the `Multi Record` `Measure` Tests for completeness, such that a filtered `Multi Record` has `Response.result`="COMPLETE" for all `Multi Record` `Measure` Tests.

In the BDQ standard, for each `Single Record` `Validation` Test, we have also defined a `Multi Record` `Measure` Test that returns a `Response.result` counting the number of `Response.results` from that `Validation` Test that are COMPLIANT (or in a few cases, COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET). Under Quality Control, these `Multi Record` `Measures` allow calculation of how much the quality of a dataset would be improved by accepting changes proposed by `Amendments`, and allow identification of areas in the data where quality improvement is most needed to fit the needs of some `Use Case`.

See the [Fitness For Use Framework Summary of Mathematical Formalization (normative)](../bdqffdq/index.md#3-fitness-for-use-framework-summary-of-mathematical-formalization-normative) for the formal expression of how `Measures` are intended to be used in Quality Control and Quality Assurance, and User's Guide section [2 Context for Quality, Uses and Purposes (non-normative)](../guide/users/index.md#2-context-for-quality-uses-and-purposes-non-normative) for a further explanation.

## 4 Use of Terms (normative)

The technical (normative) details of the BDQ Test terms (those in the `bdqtest:` namespace) are found in the [BDQ Tests and Assertions List of Terms](../list/bdqtest/index.md).

The technical definitions of the `bdqtest:` terms are supported by terms in several additional namespaces in the BDQ standard, namely `bdq:`, `bdqffdq:`, `bdqdim:`, `bdqenh:`, and `bdqcrit:`. For the details and rationale, see Chapman et al. (2017).

| **Abbreviation**  | **Technical List of Terms** |
| -------- | ----------------------- |
| bdq:     | [BDQ Controlled Vocabulary List of Terms](../list/bdq/index.md) |
| bdqtest: | [BDQ Tests and Assertions List of Terms](../list/bdqtest/index.md) |
| bdqcrit: | [Data Quality Criterion Controlled Vocabulary List of Terms](../list/bdqcrit/index.md) |
| bdqdim:  | [Data Quality Dimension Controlled Vocabulary List of Terms](../list/bdqdim/index.md) |
| bdqenh:  | [Data Quality Enhancement Controlled Vocabulary List of Terms](../list/bdqenh/index.md) |
| bdqffdq: | [Fitness For Use Framework Ontology List of Terms](../list/bdqffdq/index.md) |

### 4.1 Structure of Response (normative)

Output from each of the Tests MUST be structured data, and MUST NOT be simple pass/fail flags. The output from a Test is an `Response`, which can form part of a `Data Quality Report` or be wrapped in an `Annotation`, and MUST include the following three components: 

1. `Response.result` is the returned result for the Test, i.e., a numeric value for `Measure` Tests, a strictly controlled vocabulary value (consisting of "COMPLIANT" or "NOT_COMPLIANT" only) for `Validation` Tests, a strictly controlled vocabulary value ("NOT_ISSUE" or "POTENTIAL_ISSUE" only) for `Issue` Tests, a numeric value or a strictly controlled vocabulary value (consisting of exactly "COMPLETE" or "NOT_COMPLETE" for `Measure` Tests, and a data structure (e.g., a list of key value pairs) for proposed changes for `Amendment` Tests.
2. `Response.status` provides a controlled vocabulary, metadata concerning the success, failure, or problems with the Test. The Status also serves as a link to information about warning type values and where, with future development, probabilistic assertions about the likeliness of the value could be made.
3. `Response.comment` supplies human-readable text describing reasons for the Test result output.

A `Response` MUST be represented as either RDF or as a data structure.

When responses are in the form of RDF, the RDF MUST meet the following conditions: 

1. The `Response` MUST be an instance of `bdqffdq:Response` or one of its subclasses (`bdqffdq:ValidationResponse`, `bdqffdq:IssueResponse`, `bdqffdq:MeasurementResponse`, `bdqffdq:AmendmentResponse`). An instance of a subclass of `bdqffdq:Response` SHOULD be used.
2. The `Response` MUST have exactly one `bdqffdq:hasResponseStatus` object property linking it to one of the named individuals that has type `bdqffdq:ResponseStatus` (`bdqffdq:INTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:NOT_AMENDED`, `bdqffdq:AMENDED`, `bdqffdq:FILLED_IN`, or `bdqffdq:RUN_HAS_RESULT`).
3. The `Response` MUST have a `bdqffdq:hasResponseResult` object property or `bdqffdq:hasResponseResultValue` data property, unless the object of the `bdqffdq:hasResponseStatus` indicates that none should be present.
  - If the object of the `bdqffdq:hasResponseStatus` is `bdqffdq:RUN_HAS_RESULT`, then the instance of the `Response` MUST have one and only one `bdqffdq:hasResponseResult` object property linking it to one of the named individuals that has type `bdqffdq:ResponseResult` (`bdqffdq:COMPLETE`, `bdqffdq:COMPLIANT`, `bdqffdq:IS_ISSUE`, `bdqffdq:NOT_COMPLETE`, `bdqffdq:NOT_COMPLIANT`, `bdqffdq:NOT_ISSUE`, or `bdqffdq:POTENTIAL_ISSUE`).
    - Unless the `bdqffdq:Response` is a `bdqffdq:MeasureResponse` that returns a numeric value, in which case the `Response` MUST have one and only one `bdqffdq:hasResponseResultValue` data property linking it to a numeric value.
  - If the object of the `bdqffdq:hasResponseStatus` is one of `bdqffdq:AMENDED` or `bdqffdq:FILLED_IN`, then the instance of the `Response` MUST have one and only one `bdqffdq:hasResponseResultValue` data property linking it to structured data presenting the result of the `Amendment`. The string in the `bdqffdq:hasResponseResultValue` SHOULD be a JSON list of key:value pairs, where the keys are specific `Information Elements` (e.g., `dwc:eventDate`), and the values are the new values proposed by the `Amendment`.
  - If the object of the `bdqffdq:hasResponseStatus` is one of `bdqffdq:INTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:NOT_AMENDED`, then no `bdqffdq:hasResponseResult` SHOULD be present.
4. The `Response` MUST have at least one `bdqffdq:hasResponseComment` data property. This `bdqffdq:hasResponseComment` must provide a human readable text explanation of why the conclusion expressed in the `Response` was reached. The `bdqffdq:hasResponseComment` MAY be repeated to provide the comment in different languages. Each `bdqffdq:hasResponseComment` SHOULD be a independent and complete explanation.
5. The `Response` MAY have a `bdqffdq:hasResponseQualifier` object property.

When the `Response` is represented as a data structure in a form other than RDF, the data structure MUST:

1. Have properties corresponding to `Response.status`, `Response.result`, and `Response.comment`. These properties SHOULD have these labels.
2. Have one `Response.status` property, containing a string constant that MUST be one of the local names of one of the named individuals in `bdqffdq:` with a type `bdqffdq:ResponseStatus` ("INTERNAL_PREREQUISITES_NOT_MET", "EXTERNAL_PREREQUISITES_NOT_MET", "NOT_AMENDED", "AMENDED", "FILLED_IN", or "RUN_HAS_RESULT"").
3. Have one `Response.result` property.
  - If the `Response.status` is "RUN_HAS_RESULT" then the value of the `Response.result` property MUST be a string constant that is one of the local names of one of the named individuals of type `bdqffdq:ResponseResult` ("COMPLETE", "COMPLIANT", "IS_ISSUE", "NOT_COMPLETE", "NOT_COMPLIANT", "NOT_ISSUE", or "POTENTIAL_ISSUE").
    - Unless the `Response` is from a `Measure` Test that returns a numeric value, in which case the value of the `Response.result` property MUST be a numeric value.
  -  If the `Response.status` is one of  "AMENDED" or "FILLED_IN" then the value of the `Response.result` property MUST be structured data presenting the result of the `Amendment`. The string in the `Response.result` SHOULD be a JSON list of key:value pairs, where the keys are specific `Information Elements` (e.g., `dwc:eventDate`), and the values are the new values proposed by the `Amendment`.
  - If the `Response.status` is one of "INTERNAL_PREREQUISITES_NOT_MET", "EXTERNAL_PREREQUISITES_NOT_MET", or "NOT_AMENDED", then the `Response.result` MUST be empty or null.
4. Have one `Response.comment` property. This `Response.comment` must provide a human readable text explanation of why the conclusion expressed in the `Response` was reached. Internationalization of content of the `Response.comment` MAY be provided, nothing in this section should be taken as a constraint on how that may be accomplished.
5. A `Response.qualifier` property may be included to provide additional information.

Nothing in this section should be taken as:

* constraining how `Data Quality Reports` are presented to consumers of those reports, so long as all three elements of `Response.result`, `Response.status`, and `Response.comment` can be accessed.
* constraining internationalization and languages of labels applied to human readable presentations of Responses from Tests.
* a requirement for a particular format or serialization of `bdqffdq:Responses`. `Implementations` MAY serialize `Responses` in any appropriate form for the context. When `Responses` are wrapped in `oa:Annotations` or presented as linked open data, an RDF representation SHOULD be used.
* a requirement to how `bdqffdq:Responses` are to be presented to consumers of `Data Quality Reports`. `Implementations` MAY present the results of Tests in any form appropriate for their consumers, so long as none of the required information is suppressed.

### 4.2 Resource Types (normative)

Each BDQ Test (each instance of a `bdqffdq:DataQualityNeed`) MUST have exactly one `bdqffdq:hasResourceType` object property that relates the Test to a `Resource Type` of `bdqffdq:SingleRecord` or `bdqffdq:MultiRecord`.

Tests operate on data. Data may be understood as representing a single record or multiple records. The `Single Record` (`bdqffdq:SingleRecord`) BDQ Tests MAY be applied to a single [Simple Darwin Core](https://dwc.tdwg.org/simple/)) record, or to a single instance of a Darwin Core `dwc:Occurrence`, `dwc:Taxon`, `dwc:Event`, or other class, and MAY extend across one to many relations from that class instance to instances of classes of other types in a structured representation of Darwin Core data (Wieczorek et al. 2012). A BDQ `Single Record` Test SHOULD NOT take multiple rows from a flat file (e.g. Simple Darwin Core) as input. A BDQ `Single Record` Test SHOULD NOT take multiple objects of the same core type in structured Darwin Core as input (for example, input Darwin Core data in RDF should be presented to a BDQ `Single Record` Test one `dwc:Occurrence` at a time, although the `dwc:Occurrence` could be linked to multiple other instances of other classes such as `dwc:Identifications`).

The BDQ Test [ISSUE_ANNOTATION_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_ANNOTATION_NOTEMPTY) similarly operates on a single Simple Darwin Core record, or a single core Darwin Core class instance, and asks whether `Annotations` exist related to that class, here this standard encourages the implementation of a standard for annotating `dwc:Occurrence` records beyond the [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021).

BDQ `Multi Record` (`bdqffdq:MultiRecord`) Tests operate on a dataset as a whole. BDQ `Multi Record` Tests in `bdqtest:` sum up results across all records for each `bdqffdq:SingleRecord` Test.

### 4.3 Parameterizing the Tests (normative)

Where a Test is parameterized, a `Parameter` (e.g., `bdq:sourceAuthority`) is specified in the text of the `bdqffdq:hasExpectedResponse` data type property of the instance of the `bdqffdq:Specification` for the Test. Such a `bdqffdq:Specification` MUST also have a `bdqffdq:hasArgument` object property linking it to an instance of a `bdqffdq:Argument`, which MUST have a `bdqffdq:hasArgumentValue` data type property carrying the default value for the `Parameter`, and this `bdqffdq:Argument` MUST have a `bdqffdq:hasParameter` object property linking it to a `bdqffdq:Parameter`. The `bdqffdq:Parameter` SHOULD be a class instance in the `bdq:` namespace (e.g., `bdq:sourceAuthority`).

An instance of the `bdqffdq:Specification` SHOULD have a `bdqffdq:hasAuthoritiesDefaults` data type property containing the parameters, default values, and references to resources, including API endpoints that would provide access to values in the authority.

These elements MUST be understood in concert.

Values of `bdqffdq:hasAuthoritiesDefaults` SHOULD be a text string listing `Parameters` in the form of a semicolon-delimited list of one or more of the following: 
 
- parameter default = "default value" 
- parameter default = "default value" {[resource]}
- parameter default = "default value" {[resource]} {API endpoint [resource]}

The `bdqffdq:hasAuthoritiesDefaults` data property MAY be used without corresponding `bdqffdq:Arguments` and `bdqffdq:Parameters` when a Test is not parameterized, but a `bdq:sourceAuthority` is mentioned within a `bdqffdq:hasExpectedResponse` for the `bdqffdq:Specification` and the `bdqffdq:hasAuthoritiesDefaults` provides details on this `sourceAuthority`. This usage allows for simpler and easier-to-read expected responses.

Section [2.3.2 Reading a Specification (non-normative)](../guide/implementers/index.md#232-reading-a-specification-non-normative) of the [BDQ Implementer's Guide](../guide/implementers/index.md) contains additional guidance for handling parameters in BDQ Test `Implementations`.

#### 4.3.1 Parameter Examples (non-normative)

Example values for `bdqffdq:hasAuthoritiesDefaults`: 

     bdq:earliestValidDate default ="1582-11-15"

     bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&amp;name=]}

Example RDF fragment showing use of `Arguments` and `bdqffdq:hasAuthoritiesDefaults`: 

    <rdf:Description rdf:about="urn:uuid:9f12e2c3-17ac-42c0-91f4-c40a02d3f133">
        <rdf:type rdf:resource="bdqffdq:Argument"/>
        <rdfs:label rdf:datatype="xsd:string">Default value for bdq:maximumValidDepthInMeters:"11000"</rdfs:label>
        <hasArgumentValue xmlns="bdqffdq:" rdf:datatype="xsd:string">11000</hasArgumentValue>
        <hasParameter xmlns="bdqffdq:" rdf:resource="bdq:maximumValidDepthInMeters"/>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:d23e61b3-07b6-4326-bac2-1457b030efef">
        <rdf:type rdf:resource="bdqffdq:Argument"/>
        <rdfs:label rdf:datatype="xsd:string">Default value for bdq:minimumValidDepthInMeters:"0"</rdfs:label>
        <hasArgumentValue xmlns="bdqffdq:" rdf:datatype="xsd:string">0</hasArgumentValue>
        <hasParameter xmlns="bdqffdq:" rdf:resource="bdq:minimumValidDepthInMeters"/>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544">
        <rdf:type rdf:resource="bdqffdq:Specification"/>
        <rdfs:label rdf:datatype="xsd:string">Specification for: VALIDATION_MINDEPTH_INRANGE</rdfs:label>
        <hasArgument xmlns="bdqffdq:" rdf:resource="urn:uuid:9f12e2c3-17ac-42c0-91f4-c40a02d3f133"/>
        <hasArgument xmlns="bdqffdq:" rdf:resource="urn:uuid:d23e61b3-07b6-4326-bac2-1457b030efef"/>
        <hasAuthoritiesDefaults xmlns="bdqffdq:" rdf:datatype="xsd:string">bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</hasAuthoritiesDefaults>
        <hasExpectedResponse xmlns="bdqffdq:" rdf:datatype="xsd:string">INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters is bdq:Empty, or the value is not interpretable as number greater than or equal to zero; COMPLIANT if the value of dwc:minimumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT</hasExpectedResponse>
        ...
    </rdf:Description>

Example RDF Fragment from the `Specification` for [VALIDATION_COUNTRYCODE_STANDARD](../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD), where `bdqffdq:hasAuthoritiesDefaults` is present to provide a `bdq:sourceAuthority` for the `Specification`, but the Test is not parameterized, so no `bdqffdq:hasArgument` properties are present: 

    <hasAuthoritiesDefaults xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</hasAuthoritiesDefaults>
    <hasExpectedResponse xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</hasExpectedResponse

## 5 Design of the Tests (normative)

BDQ `Tests` are designed with a clear boundary of responsibility: they take a defined set of input `Information Elements` (and optional `Parameters`) and return a structured `Response` describing the outcome. This standardization of inputs and outputs means a `Test` implementation can be treated as a small, self-contained component whose behavior is determined by its `Specification` and is consistent across programming languages and environments. The surrounding execution framework is responsible for obtaining and binding raw data to the required `Information Elements`, selecting which `Tests` to run (e.g., by `Use Case` via `Policies`), and assembling the resulting `Responses` into `Data Quality Reports`. In this way, BDQ separates the semantics of `Test` behavior (what is evaluated and how results are expressed) from the mechanics of test execution (how data are accessed, orchestrated, filtered, and reported).

### 5.1.1 What is a "Test" (non-normative)

A Test is a defined evaluation that takes specific inputs and produces a structured output. A Test is defined using a set of `bdqffdq:` classes and properties that specify the inputs to the Test (the relevant `Information Elements` and any `Parameters`) and how those input values are to be evaluated under a `Specification` to produce a structured output (a `Response`) that can be interpreted consistently across implementations. The Test definitions are provided in the `bdqtest:` vocabulary, and the semantics of the terms used in those definitions are provided by the `bdqffdq:` vocabulary and supporting vocabularies.

![Diagram of the relationship between the concept Test and the bdqffdq: classes and properties that define it](docs/guide/implementers/bdqffdq_overview_diagram.svg)

A Test is not a software implementation; it is a formal definition of an evaluation that *can* be implemented in software. In the Fitness For Use Framework, each Test is an instance of a subtype of `Data Quality Need` that identifies what is being evaluated (through its required `Information Elements` and its `Resource Type`) and why it matters (through its association with one or more `Use Cases` via `Policies`). The Test is linked to a `Method`, which in turn links to a `Specification` that describes expected behavior and expected outcomes (e.g., via `hasExpectedResponse`), and may reference `Parameters` and source authorities that further constrain or parameterize execution. When an `Implementation` runs a Test, it produces one or more `Responses` that can be assembled into `Data Quality Reports` for interpretation, filtering, and aggregation.

Conceptually, Tests can be viewed in two complementary ways: vertically, they connect the `Data Quality Needs` and `Data Quality Solutions` layers and produce outputs in the `Data Quality Reports` layer; and horizontally by type, BDQ defines four main categories of Tests—`Validation`, `Issue`, `Measure`, and `Amendment`—each of which produces corresponding kinds of `Responses`.

### 5.1 Data Quality Control, Data Quality Assurance (normative)

The BDQ standard draws a distinction between Quality Control and Quality Assurance. Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data. Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose. Implementations of the BDQ Tests MAY be used to perform Quality Control, Quality Assurance, or both. The [mathematical formalization](docs/bdqffdq/index.md#3-fitness-for-use-framework-summary-of-mathematical-formalization-normative) of the [Fitness for Use Ontology](docs/bdqffdq/index.md) provides a formal definition of Quality Control and Quality Assurance, and how Test `Responses` SHOULD be used for each.

### 5.2 When to Run Tests (normative)

The BDQ Tests are designed to be run at any point in the life cycle of biodiversity data. 
* They MAY be run at the point of initial collection or observation of organisms. 
* They MAY be run to support data transcription. 
* They MAY be run in loading data into databases of record from field or transcription sources. 
* They MAY be run in preparing data from databases of record for aggregation. 
* They MAY be run during data aggregation and the presentation of aggregated data. 
* They MAY be run in workflows for analysis of data for research purposes.

### 5.3 Results of Test Executions (normative)

The BDQ standard is agnostic about the format of presentation of results from BDQ Tests. BDQ does, however, specify that Test implementations and presentations MUST return structured data with at least Response.status, Response.result, and Response.comment. Responses MAY also contain more information in Response.qualifier.
See the [Implementer's Guide](docs/guide/implementers/index.md) section on [Presentation of Results](docs/guide/implementers/index.md#7-presentation-of-results-normative) for further normative and non-normative guidance about result presentation. See [Structure of a Response](docs/bdqtest/index.md#31-structure-of-response-normative) in the [BDQ Tests and Assertions](docs/bdqtest/index.md) document for normative guidance on `Responses` as RDF or as data structures.

The results of the execution of implementations of the BDQ Tests MAY be presented as Data Quality reports. The Framework Ontology provides vocabulary and structure that MAY be used for such data quality reports.

The bdqffdq: vocabulary enables the wrapping of the results of BDQ Tests within annotations. The bdqffdq: vocabularies in particular are intended to support the framing of `Responses` from Tests within annotations that follow the W3C Web Annotation Data Model (Sanderson et al. 2017), and are suitable for inclusion in semantic data stores. See the [Implementer's Guide](docs/guide/implementers/index.md) section on [Annotations](docs/guide/implementers/index.md#72-annotations-normative) for more guidance.

### 5.4 Test Execution Environments and Workflows (non-normative)

Neither the Test descriptions nor the framework impose constraints on environments or workflows for execution. One possible workflow is to run all validations, then all amendments, then all validations again on a modified copy of the input data to which all proposed amendments have been applied.

A single validation step, with measures evaluating the results of the amendments could look like the diagram below.

![Diagram of workflow through single validation step](workflow_single_iteration.svg)

Expanding on this single validation step, amendments can be run and their results fed back into a second phase of post-amendment validation, with measures again evaluating the results of validation of the input data if all changes proposed by amendments are accepted. Presentation of a data quality report would be an expected result from this workflow for Quality Control purposes, while using the Measures in the second step to filter data in a processing pipeline to just those that are fit for purpose for a particular use would be expected for Quality Assurance purposes.

![Diagram of workflow with pre-amendment validation+measure phase, followed by amendment phase, followed by post-amendment validation-measure phase](workflow_two_iterations.svg)

### 6 Example RDF description of a Test (non-normative) 

A complete description of BDQ Tests can be found in the RDF representation of this vocabulary. Following the Fitness for Use Framework Ontology (`bdqffdq:`), a Test is composed of an instance of a subclass of a `bdqffdq:DataQualityNeed` (e.g., `bdqffdq:Validation`), an instance of a `bdqffdq:ActedUpon` `Information Element`, optionally an instance of a `bdqffdq:Consulted` `Information Element`, an instance of a subclass of `bdqffdq:Method` (e.g., `bdqffdq:ValidationMethod`), and an instance of a `bdqffdq:Specification`. Most of the information associated with a `bdqtest:` term is expressed in other vocabularies, in particular `bdqffdq:`. This structure and dependence on other vocabularies can be seen in the formal example description of [VALIDATION_COUNTRYCODE_STANDARD](../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD), below.

    <rdf:Description rdf:about="https://rs.tdwg.org/bdqtest/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe-2025-03-07">
        <dcterms:bibliographicCitation>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html; ISO (n.dat) 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2; DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list; Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</dcterms:bibliographicCitation>
        <dcterms:isVersionOf rdf:resource="https://rs.tdwg.org/bdqtest/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
        <dcterms:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-03-07</dcterms:issued>
        <rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Validation"/>
        <comment xmlns="http://www.w3.org/2000/01/rdf-schema#">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</comment>
        <label xmlns="http://www.w3.org/2000/01/rdf-schema#">VALIDATION_COUNTRYCODE_STANDARD</label>
        <skos:historyNote>https://github.com/tdwg/bdq/issues/20</skos:historyNote>
        <skos:note>Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and recommended in Darwin Core to designate the high seas. Also available in the ISO user defined codes is ZZ, used by Darwin Core and GBIF to mark unknown countries. This Test should accept both XZ and ZZ as COMPLIANT country codes. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</skos:note>
        <skos:prefLabel>Validation dwc:countryCode Standard for SingleRecord</skos:prefLabel>
        <bdqffdq:hasActedUponInformationElement rdf:resource="urn:uuid:c3620a97-65d6-4f9c-8a03-32e0d240a423"/>
        <bdqffdq:hasCriterion rdf:resource="https://rs.tdwg.org/bdqcrit/terms/Standard"/>
        <bdqffdq:hasDataQualityDimension rdf:resource="https://rs.tdwg.org/bdqdim/terms/Conformance"/>
        <bdqffdq:hasResourceType rdf:resource="https://rs.tdwg.org/bdqffdq/terms/SingleRecord"/>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:c3620a97-65d6-4f9c-8a03-32e0d240a423">
        <rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/ActedUpon"/>
        <label xmlns="http://www.w3.org/2000/01/rdf-schema#">Information Element ActedUpon dwc:countryCode</label>
        <skos:prefLabel>Information Element ActedUpon dwc:countryCode</skos:prefLabel>
        <bdqffdq:composedOf rdf:resource="http://rs.tdwg.org/dwc/terms/countryCode"/>
    </rdf:Description>
        
    <rdf:Description rdf:about="urn:uuid:02f5a440-a473-42cf-a3f1-6c10334d5eb8">
        <rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/ValidationMethod"/>
        <label xmlns="http://www.w3.org/2000/01/rdf-schema#">ValidationMethod: VALIDATION_COUNTRYCODE_STANDARD with Specification for: VALIDATION_COUNTRYCODE_STANDARD</label>
        <skos:historyNote>Source: TG2</skos:historyNote>
        <skos:note>Example Implementations Source Code: https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L99</skos:note>
        <skos:note>Example Implementations: Kurator/FilteredPush geo_ref_qc Library (Morris &amp; Lowery 2025b)</skos:note>
        <skos:note>TG2 Validation SPACE CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</skos:note>
        <skos:prefLabel>ValidationMethod: VALIDATION_COUNTRYCODE_STANDARD with Specification for: VALIDATION_COUNTRYCODE_STANDARD</skos:prefLabel>
        <bdqffdq:forValidation rdf:resource="https://rs.tdwg.org/bdqtest/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe-2025-03-07"/>
        <bdqffdq:hasSpecification rdf:resource="urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047"/>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047">
        <rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Specification"/>
        <comment xmlns="http://www.w3.org/2000/01/rdf-schema#">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</comment>
        <label xmlns="http://www.w3.org/2000/01/rdf-schema#">Specification for: VALIDATION_COUNTRYCODE_STANDARD</label>
        <skos:example>dwc:countryCode="GL": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value"</skos:example>
        <skos:example>dwc:countryCode="GRL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value"</skos:example>
        <bdqffdq:hasAuthoritiesDefaults>bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</bdqffdq:hasAuthoritiesDefaults>
        <bdqffdq:hasExpectedResponse>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</bdqffdq:hasExpectedResponse>
    </rdf:Description>

