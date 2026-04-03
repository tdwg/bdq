<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Implementer's Guide

**Title**<br>
BDQ Implementer's Guide

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
This document is a users guide for the BDQ standard, providing guidance for those wishing to create software implementations (bdqffdq:Mechanism) of BDQ Tests.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Implementer's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
  - [1.4 Status of the Content of this document (normative)](#14-status-of-the-content-of-this-document-normative)
  - [1.5 RFC 2119 key words (normative)](#15-rfc-2119-key-words-normative)
  - [1.6 Namespace Abbreviations (non-normative)](#16-namespace-abbreviations-non-normative)
  - [1.7 Referring to Terms (normative)](#17-referring-to-terms-normative)

[2 About the Tests and their Implementation (normative)](#2-about-the-tests-and-their-implementation-normative)
  - [2.1 Independence (normative)](#21-independence-normative)
  - [2.2 The Concept of "EMPTY" in the BDQ Standard (normative)](#22-the-concept-of-empty-in-the-bdq-standard-normative)
    - [2.2.1 The Concept of Empty (normative)](#221-the-concept-of-empty-normative)
    - [2.2.2 Example Implementation of a Function to Assess Empty (non-normative)](#222-example-implementation-of-a-function-to-assess-empty-non-normative)
  - [2.3 Reading Test Descriptors (non-normative)](#23-reading-test-descriptors-non-normative)
    - [2.3.1 Key Parts of a Test Descriptor (non-normative)](#231-key-parts-of-a-test-descriptor-non-normative)
    - [2.3.2 Reading a Specification (non-normative)](#232-reading-a-specification-non-normative)
      - [2.3.2.1 Response as Shorthand for a Set of bdqffdq: Concepts (non-normative)](#2321-response-as-shorthand-for-a-set-of-bdqffdq-concepts-non-normative)
      - [2.3.2.2 Guidance for Reading a Specification (normative)](#2322-guidance-for-reading-a-specification-normative)
      - [2.3.2.3 Further Guidance for Reading a Specification (non-normative)](#2323-further-guidance-for-reading-a-specification-non-normative)
      - [2.3.2.4 Default Value Strings in Parameters (normative)](#2324-default-value-strings-in-parameters-normative)
      - [2.3.2.5 Example Interpretation of a Parameter String Default Value (non-normative)](#2325-example-interpretation-of-a-parameter-string-default-value-non-normative)
    - [2.3.3 The Concept of "interpreted as" (normative)](#233-the-concept-of-interpreted-as-normative)
    - [2.3.4 Handling Leading and Trailing Whitespace (normative)](#234-handling-leading-and-trailing-whitespace-normative)

[3 Compliant Implementation (normative)](#3-compliant-implementation-normative)
  - [3.1 Compliance depends on `Use Case` (normative)](#31-compliance-depends-on-use-case-normative)
  - [3.2 Minimum Test Suite composition (normative)](#32-minimum-test-suite-composition-normative)
  - [3.3 Rationale and expectations for suite design (non-normative)](#33-rationale-and-expectations-for-suite-design-non-normative)
  - [3.4 Required outputs for every Test execution (normative)](#34-required-outputs-for-every-test-execution-normative)
    - [3.4.1 Amendment Response.result ordering (normative)](#341-amendment-responseresult-ordering-normative)
  - [3.5 Describing additional Tests (normative)](#35-describing-additional-tests-normative)
  - [3.6 Parameterized Tests: default behavior and unsupported values (normative)](#36-parameterized-tests-default-behavior-and-unsupported-values-normative)
  - [3.7 Bulk / non-Framework execution (normative)](#37-bulk-/-non-framework-execution-normative)

[4 Extension Points (normative)](#4-extension-points-normative)

[5 Responses from Tests (normative)](#5-responses-from-tests-normative)
  - [5.1 The Response Object (normative)](#51-the-response-object-normative)
  - [5.1.1 Amendment Test Responses (normative)](#511-amendment-test-responses-normative)
  - [5.1.2 Response Serialization and Presentation (normative)](#512-response-serialization-and-presentation-normative)
  - [5.1.3 Further Guidance on Responses (non-normative)](#513-further-guidance-on-responses-non-normative)
  - [5.1.4 Results from Measures (normative)](#514-results-from-measures-normative)
  - [5.2 Framework Elements Not Included in BDQ Test Descriptions (normative)](#52-framework-elements-not-included-in-bdq-test-descriptions-normative)

[6 Guidelines for Implementers (normative)](#6-guidelines-for-implementers-normative)
  - [6.1 Parameters and Changing the Behavior of a Test (normative)](#61-parameters-and-changing-the-behavior-of-a-test-normative)
    - [6.1.1 Identifying non-default `Parameter` values in reports (normative)](#611-identifying-non-default-parameter-values-in-reports-normative)
    - [6.1.2 Identifying non-default `Parameter` values in `Response.comment` (normative)](#612-identifying-non-default-parameter-values-in-responsecomment-normative)
    - [6.1.3 Expectations for Tests with `Parameters` (normative)](#613-expectations-for-tests-with-parameters-normative)
    - [6.1.4 Test departures from specifications (normative)](#614-test-departures-from-specifications-normative)
    - [6.1.3 Further guidance on `Parameters` and `Arguments` (non-normative)](#613-further-guidance-on-parameters-and-arguments-non-normative)
  - [6.2 Execution Process Agnostic (non-normative)](#62-execution-process-agnostic-non-normative)
  - [6.3 Considerations for Test Execution (normative)](#63-considerations-for-test-execution-normative)
  - [6.4 Order of Test Execution (normative)](#64-order-of-test-execution-normative)
    - [6.4.1 Phases: Pre-Amendment, Amendment, Post-Amendment (normative)](#641-phases-pre-amendment-amendment-post-amendment-normative)
      - [6.4.1.1 Explanation of Phases (non-normative)](#6411-explanation-of-phases-non-normative)
      - [6.4.1.2 Phases and Quality Assurance (normative)](#6412-phases-and-quality-assurance-normative)
      - [6.4.1.3 Phases and Quality Control (normative)](#6413-phases-and-quality-control-normative)
    - [6.4.2 Test Dependencies (normative)](#642-test-dependencies-normative)
      - [6.4.2.1 Terms for describing Test Dependencies (non-normative)](#6421-terms-for-describing-test-dependencies-non-normative)
    - [6.4.3 Implementing a complete Test (normative)](#643-implementing-a-complete-test-normative)
    - [6.4.4 Presenting Darwin Core Data to a Method that Implements a Test (non-normative)](#644-presenting-darwin-core-data-to-a-method-that-implements-a-test-non-normative)
      - [6.4.4.1 Binding Darwin Core Data (normative)](#6441-binding-darwin-core-data-normative)
      - [6.4.4.2 Examples of matching input Darwin Core to Method parameters (non-normative)](#6442-examples-of-matching-input-darwin-core-to-method-parameters-non-normative)
    - [6.4.5 Example Test Implementations (non-normative)](#645-example-test-implementations-non-normative)
      - [6.4.5.1 Example in Pseudocode (non-normative)](#6451-example-in-pseudocode-non-normative)
      - [6.4.5.2 Example in Java (non-normative)](#6452-example-in-java-non-normative)
    - [6.4.6 Implementing an Abstract Test (normative)](#646-implementing-an-abstract-test-normative)
    - [6.4.7 Implementing a Test in a Specific Environment (non-normative)](#647-implementing-a-test-in-a-specific-environment-non-normative)

[6.5 Common Pattern for Implementing a Test (non-normative)](#65-common-pattern-for-implementing-a-test-non-normative)
  - [6.5.1 Responsibilities of a Test (non-normative)](#651-responsibilities-of-a-test-non-normative)
  - [6.5.1 Checklist for a Validation test (non-normative)](#651-checklist-for-a-validation-test-non-normative)
  - [6.5.2 Checklist for Implementing an Amendment Test (non-normative)](#652-checklist-for-implementing-an-amendment-test-non-normative)

[6.6 Responsibilities of a Test Execution Framework (non-normative)](#66-responsibilities-of-a-test-execution-framework-non-normative)
  - [6.6.1 Linking raw input terms, Tests, and outputs in a workflow (non-normative)](#661-linking-raw-input-terms-tests-and-outputs-in-a-workflow-non-normative)

[7 Presentation of Results (normative)](#7-presentation-of-results-normative)
  - [7.1 Data Quality Reports (normative)](#71-data-quality-reports-normative)
    - [7.1.1 Identifying Tests (normative)](#711-identifying-tests-normative)
    - [7.1.2 Information Elements Acted Upon and Consulted in Results (normative)](#712-information-elements-acted-upon-and-consulted-in-results-normative)
      - [7.1.2.1 Information Elements Acted Upon and Consulted Example (non-normative)](#7121-information-elements-acted-upon-and-consulted-example-non-normative)
    - [7.1.3 Example (non-normative)](#713-example-non-normative)
  - [7.2 Annotations (normative)](#72-annotations-normative)
    - [7.2.1 Example of Test Responses as Annotations (non-normative)](#721-example-of-test-responses-as-annotations-non-normative)

[8 Conformance Testing Implementations (normative)](#8-conformance-testing-implementations-normative)
  - [8.1 Introduction to Test Conformance Testing (non-normative)](#81-introduction-to-test-conformance-testing-non-normative)
    - [8.1.1 DataID as a conformance testing data record identifier (normative)](#811-dataid-as-a-conformance-testing-data-record-identifier-normative)
  - [8.2 Structure of the Test Conformance Testing Data (non-normative)](#82-structure-of-the-test-conformance-testing-data-non-normative)
  - [8.3 Examples of the Data for Conformance Testing (non-normative)](#83-examples-of-the-data-for-conformance-testing-non-normative)
  - [8.4 Where to Get the Test Conformance Testing Data (non-normative)](#84-where-to-get-the-test-conformance-testing-data-non-normative)
  - [8.5 Implementation and the Conformance Testing Data (normative)](#85-implementation-and-the-conformance-testing-data-normative)
  - [8.6 Existing Software tools (non-normative)](#86-existing-software-tools-non-normative)
    - [8.6.1 Tools for Validating Test Implementations with the Conformance Testing Data (non-normative)](#861-tools-for-validating-test-implementations-with-the-conformance-testing-data-non-normative)
    - [8.6.2 Tools to assist with Implementations and RDF presentation (non-normative)](#862-tools-to-assist-with-implementations-and-rdf-presentation-non-normative)

[9 Existing Test Implementations (non-normative)](#9-existing-test-implementations-non-normative)

[Acronyms (non-normative)](#acronyms-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to provide implementation guidance for software developers and systems architects building tools or workflows that conform to the BDQ standard. It explains how to interpret and operationalize the BDQ Test specifications, including the semantics of inputs and outputs, expected behaviors, parameter handling, dependency resolution, and result reporting.

This guide supports consistent, standards-compliant implementations across various environments by clarifying technical aspects of the Tests, detailing extension points, and describing conformance testing procedures using shared datasets. It includes both normative content necessary for implementation conformance and non-normative advice for implementers seeking efficiency, clarity, and compatibility.

### 1.2 Audience (non-normative)

This document is intended for technical audiences responsible for implementing BDQ Tests in software applications or data processing pipelines. It will be particularly useful to:

- Software developers integrating the BDQ standard into biodiversity data infrastructures
- Tool builders seeking to support data validation or annotation workflows
- Technical architects and standards implementers creating reusable data quality services
- Power users customizing or extending BDQ Test suites.

Readers should be familiar with basic software development concepts and, ideally, have experience working with data structures and RDF vocabularies. This guide assumes a need for detailed implementation-level knowledge, but provides both high-level explanations and concrete examples (e.g., in pseudocode and Java).

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

The set of information most relevant to implementers of Biodiversity Data Quality (BDQ) Tests can be found in the following subset of resources:

- [**BDQ Tests and Assertions**](../../bdqtest/index.md) - Defines how each Test is modeled using standard vocabulary terms and how it should behave under various conditions.
- [**BDQ Tests Quick Reference Guide**](../../terms/bdqtest/index.md) - Provides a concise, easy-to-read reference about the BDQ Tests.
- [**BDQ User's Guide**](../users/index.md) - For anyone interested in how to use the BDQ Tests in practice.
- **BDQ Implementer's Guide** - For anyone interested in the technical implementation of the BDQ Tests. This document.
- [**BDQ Supplemental Information**](../../supplement/index.md) - This supplementary information may be relevant for curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners who wish to understand, evaluate and/or improve the quality of biodiversity data within their domain. This document provides some key developmental issues in the building of the BDQ standard that are not covered in other documents within the standard. This document may also be useful to those seeking to evaluate their current Tests or generate additional Tests for their domain.
- [**Current Single Record Tests**](../../../dist/bdqtest_singlerecord_tests_current.csv) - Convenient list of BDQ `Single Record` Tests.
- [**Current Multi Record Tests**](../../../dist/bdqtest_multirecord_tests_current.csv) - Convenient list of BDQ `Multi Record` Tests.

### 1.4 Status of the Content of this document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

### 1.5 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.6 Namespace Abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| prov:        | http://www.w3.org/ns/prov#                  |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.7 Referring to Terms (normative)

In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., `https://rs.tdwg.org/bdqffdq/terms/` for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (`skos:prefLabel`, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. The BDQ documents use all these methods.

## 2 About the Tests and their Implementation (normative)

### 2.1 Independence (normative) 

Test implementations SHOULD be independent of how data are stored and transported, data serializations, and the framework or environment in which the Tests are being executed. 

### 2.2 The Concept of "EMPTY" in the BDQ Standard (normative)

`Empty` and `Not Empty` in the context of the BDQ standard are defined as follows: 

| term | definition |
| ---  | ---------- |
| bdq:Empty | An evaluation of a value, which in the context of the evaluation, returns true if the value does not contain any characters or values other than those in the range U+0000 to U+0020, otherwise returns false. |
| bdq:NotEmpty |An evaluation of a value, which in the context of the evaluation, returns false if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns true. |

See the formal definitions and usage comments of [bdq:Empty](../../list/bdq/index.md#bdq_Empty) and [bdq:NotEmpty](../../list/bdq/index.md#bdq_NotEmpty) terms in the [BDQ Controlled Vocabulary List of Terms](../../list/bdq/index.md)

Data that have passed through arbitrary serializations and transformations can contain anomalies. `bdq:Empty` is defined to allow Tests to clearly separate concerns. A `bdqffdq:InformationElement` containing invalid characters, (e.g., letters in an `Information Element` that would be expected to contain integers) or values (including string serializations of the NULL value) are `bdq:NotEmpty` and are the concern of Tests that evaluate `bdqdim:Conformance`. Presence or absence of data is a concern for Tests evaluating `bdqdim:Completeness`.

#### 2.2.1 The Concept of Empty (normative)

(1) Spaces, tabs, and other non-printing characters are `bdq:Empty`.

Unicode characters in the range U+0000 to U+0020, equivalent to ASCII characters 0-32, MUST be treated as `bdq:Empty`.

(2) Actual NULLs are `bdq:Empty`.

Objects that are null (or are null values in a relational database) at the point of Test execution MUST be treated as `bdq:Empty`.

(3) Serializations of NULL are `bdq:NotEmpty`.

Data serialized from relational database systems may contain string representations of NULL.  We considered, and explicitly rejected, treating common string serializations of null such as "&#92;N" and "NULL" as empty values. 

String serializations of NULL outside of a database, present at the point of evaluation of a Test, MUST be treated as `bdq:NotEmpty`. 

A Test execution environment MAY deserialize these string serializations of NULL as null objects (see 5), and present them to a test as NULL objects, where they would evaluate as `bdq:notEmpty` (see 2).

(4) Data values indicating an unknown are treated as `bdq:NotEmpty`.

The definition of `bdq:Empty` is not applicable to a discussion of what value to include in a controlled vocabulary to indicate that no meaningful value is present, so no suggestion is made that "EMPTY" should be used as a data value to represent some form of "null", "unknown", "not recorded", etc. Choices there would fall into the semantics for some set of controlled vocabularies. The relevance to such a discussion is that this definition would treat an empty string as an empty value, with no semantics attached as to why the value is empty.

(5) Independence of Tests from the execution framework. 

The evaluation of `bdq:Empty` MUST be at the point of evaluation of the Test. This allows the Tests to be independent of data serializations for transport and the representation of data in Test execution environments. 

In the BDQ standard, `bdq:Empty` is used to evaluate `bdqffdq:InformationElements` within a Test specification, it therefore means empty if the dataset being evaluated does not contain the term matching the `Information Element`, or if the dataset contains that term but the value for that term is empty. This is to allow the application programming interface expressed by the Test `bdqffdq:DataQualityNeed` to be agnostic about the structure presented to a framework for executing the Tests. 

For CSV data, a column is either there or not in a dataset, but in an RDF representation, some data objects could have relevant properties and others not - and the Tests are independent of that.

#### 2.2.2 Example Implementation of a Function to Assess Empty (non-normative)

Here is a Java function to evaluate Empty, using trim() to exclude U+0020 (space), U+000A (LF), U+000D (CR) and the other non-printing characters in the unicode range U+0000 to U+0020, and also evaluating null as Empty. Test implementations can reuse a function like this for any Test that evaluates `bdq:Empty` in its specification (`hasExpectedResponse`).

    public boolean isEmpty(String aString)  {
        boolean result = true;
        if (aString != null && aString.trim().length()>0) { 
            result = false;
        }
        return result;
    }

Here is a MariaDB implementation of a lightweight version of [VALIDATION_KINGDOM_NOTEMPTY](../../terms/bdqtest/index.md#VALIDATION_KINGDOM_NOTEMPTY), which provides a list of NOT_COMPLIANT records for some flat taxonomy table in a database, again handing off the responsibility for evaluation of non-printing characters to the trim function available in the language.

    SELECT taxonomy_id, kingdom,
         'VALIDATION_KINGDOM_NOTEMPTY' as test, 'NOT_COMPLIANT' as response_result, 'RUN_HAS_RESULT' as response_status,
         'The value of kingdom is Empty.' as response_comment
    FROM taxonomy
    WHERE 
         kingdom is null
         OR
         length(trim(kingdom)) == 0
    ;

### 2.3 Reading Test Descriptors (non-normative)

The Tests defined in BDQ are described in the [BDQ Tests Quick Reference Guide](../../terms/bdqtest/index.md), with more detail in the [BDQ Tests and Assertions List of Terms](../../list/bdqtest/index.md). A [CSV file of just the Single Record Tests](../../../dist/bdqtest_singlerecord_tests_current.csv) is available for the convenience of implementers. Viewing the data in this file in a spreadsheet program can be an effective way to examine and compare the descriptions of the Tests.

#### 2.3.1 Key Parts of a Test Descriptor (non-normative)

The descriptions of the Tests are complex. The following (abstracted from [the Key to bdqtest: vocabulary terms](../../list/bdqtest/index.md#110-key-to-vocabulary-terms-normative) and the `bdqffdq:` [ontology](../../list/bdqffdq/index.md)) are the most important terms to understand for implementation:

- Term Name (`rdf:value`) - a UUID that identifies the Test (e.g., 3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e).
- Term IRI (`dcterms:isVersionOf`) - the machine readable identifier for the Test, in the form of an IRI terminating in the Term Name UUID (https://rs.tdwg.org/bdqtest/terms/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e).
- Versioned IRI - the machine readable identifier for a specific version of the Test, in the form of an IRI terminating in the Term Name UUID and a date (https://rs.tdwg.org/bdqtest/terms/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e-2025-03-07)  Term IRI and Versioned IRI follow the guidance of the [TDWG Metadata Standards](https://tdwg.github.io/rs.tdwg.org/README-2020-02-03.html#4th-level-terms) document for IRIs for Terms.
- Label (`rdfs:label`) - a human readable identifier for the Test (e.g., VALIDATION_COUNTRYCODE_STANDARD).
- ExpectedResponse ([bdqffdq:hasExpectedResponse](../../list/bdqffdq/index.md#hasexpectedresponse)) - the description of the expected behavior of a Test implementation.
- SourceAuthorities/Defaults ([bdqffdq:hasAuthoritiesDefaults](../../list/bdqffdq/index.md#hasauthoritiesdefaults)) - information about source authorities and parameters listed in the expected response, including default values for parameters.
- Information Elements Acted Upon ([bdqffdq:composedOf](../../list/bdqffdq/index.md#composedof); [bdqffdq:ActedUpon](../../list/bdqffdq/index.md#actedupon)) - the inputs to the Test that the Test affects.
- Information Elements Consulted ([bdqffdq:composedOf](../../list/bdqffdq/index.md#composedof); [bdqffdq:Consulted](../../list/bdqffdq/index.md#consulted)) - the inputs to the Test that the Test uses.
- Parameters ([bdqffdq:hasParameter](../../list/bdqffdq/index.md#hasParameter); [bdqffdq:Parameter](../../list/bdqffdq/index.md#parameter)) - optional inputs to a Test that can change the behavior of the Test by changing the range or scope of values or the authority to use.
- Examples (`skos:example`) - examples of expected inputs and outputs from a Test implementation.
- Notes (`skos:note`) - additional notes about the Test, including clarification and guidance for implementation.


#### 2.3.2 Reading a Specification (non-normative)

Consider these properties of an example `Specification` (for the `Validation` [VALIDATION_PHYLUM_FOUND](../../terms/bdqtest/index.md#VALIDATION_PHYLUM_FOUND)): 

hasExpectedResponse: 
```
EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdq:Empty; COMPLIANT if the value of dwc:phylum is found as a value at the rank of Phylum in the bdq:sourceAuthority; otherwise NOT_COMPLIANT
```

hasAuthoritiesDefaults: 
```
bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&amp;name=]}
```

example: 
```
dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"
```

These properties describe the expected behavior of an Implementation of this Test. This section gives further guidance on how to interpret these properties in order to produce an implementation that follows this specification.

##### 2.3.2.1 Response as Shorthand for a Set of bdqffdq: Concepts (non-normative)

We regularly (particularly in examples) use `Response`, `Response.status`, `Response.result`, and `Response.comment` as shorthand for a more complicated set of `bdqffdq:` classes, object properties and datatype properties. The table below describes how these concepts are related.

| Shorthand Concept | bdqffdq Term(s) | Description |
| ----------------- | --------------- | ----------- |
| Response          | bdqffdq:Assertion | The report from a single execution of a single Test, consisting of a Response.status, a Response.result, a Response.comment, and optionally, a Response.qualifier. | 
| Response.status   | bdqffdq:ResponseStatus, bdqffdq:hasResponseStatus | A metadata element in a Response indicating whether a Test was able to be performed or not. | 
| Response.result   | bdqffdq:ResponseResult, bdqffdq:hasResponseResult, bdqffdq:hasResponseResultValue | The element in a Response containing the value returned by a Test. |
| Response.comment  | bdqffdq:hasResponseComment | A human readable interpretation of the results of the Test. |
| Response.qualifier | bdqffdq:ResponseQualifier, bdqffdq:hasResponseQualifier | Additional structured information that qualifies the Response, intended as an extension point for uncertainty. |

##### 2.3.2.2 Guidance for Reading a Specification (normative)

A `bdqffdq:hasExpectedResponse` property of a `bdqffdq:Specification` provides expectations for the behavior of an implementation of a Test. A `bdqffdq:hasExpectedResponse` consists of a sequence of blocks of "RESPONSE, criteria;".  The "criteria" are a sequence of options for that "RESPONSE". When reading a specification (`hasExpectedResponse`), implementers SHOULD read each block in sequence, evaluating each of the "criteria" in sequence, and return the first response for which the specified "criteria" are met. An exception to this is the placement of EXTERNAL_PREREQUISITES_NOT_MET as the first "RESPONSE" in the specification. This does not imply that the responsiveness of an external resource should be assessed first. Implementers MAY handle failure of an external resource in any appropriate manner, for example, with exception handling.

Some `Amendment` Tests can propose values for a single [Darwin Core Term](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021). A few `Amendment` Tests can propose values for multiple [Darwin Core Terms](https://dwc.tdwg.org/list/). 

##### 2.3.2.3 Further Guidance for Reading a Specification (non-normative)

`Responses` in a `hasExpectedResponse` property of a `Specification` are expressed in a concise and abbreviated form for readability by implementers, expanding these to string properties on a `Response` object gives:

EXTERNAL_PREREQUISITES_NOT_MET means 
```
Response.status=EXTERNAL_PREREQUISITES_NOT_MET, Response.result=null, Response.comment={some bdq:NotEmpty description of the failure condition}
```

INTERNAL_PREREQUISITES_NOT_MET means 
```
Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.result=null, Response.comment={some bdq:NotEmpty description of the failure condition}.
```

COMPLIANT means 
```
Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment={some bdq:NotEmpty description of the success condition}.
```

Expressed with `bdqffdq:` terms, as would be if Assertions are expressed in RDF, the first example above these would be:

EXTERNAL_PREREQUISITES_NOT_MET means 
```
@prefix bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

# Example: an Assertion with Response.status = EXTERNAL_PREREQUISITES_NOT_MET
# In this case, Response.result is omitted (i.e., there is no hasResponseResult triple),
# which matches the BDQ guidance that the result MUST be empty/null for this status.

[] a bdqffdq:Assertion ;
   bdqffdq:hasResponseStatus bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET ;
   bdqffdq:hasResponseComment "Source authority service was not available at time of evaluation."^^xsd:string .
```
Note that in RDF representations, the `Response` is an instance of `bdqffdq:Assertion`, and the `Response.status` is a value of `bdqffdq:hasResponseStatus`, while the `Response.result` may be either a literal using `bdqffdq:hasResponseResultValue` or a Named Individual using bdqffdq:hasResponseResult, or, as a best practice with RDF, when null, is ommitted, and the `Response.comment` is a value of `bdqffdq:hasResponseComment`.


For example, the `bdqffdq:hasExpectedResponse` for the `Specification` for [VALIDATION_COUNTRYCODE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD) states:

```
EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT
```

To understand the meaning of `bdq:sourceAuthority` in the expected response, see the `bdqffdq:hasAuthoritiesDefaults` for the `Specification`:

```
bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}
```

The `Specification` is thus intended to be read as: 

1. Return EXTERNAL_PREREQUISITES_NOT_MET if the ISO Country codes list (https://www.iso.org/iso-3166-country-codes.html, searchable at https://www.iso.org/obp/ui/#search) is not available; 
2. else Return INTERNAL_PREREQUISITES_NOT_MET if the `dwc:countryCode` is `bdq:Empty`; 
3. else Return COMPLIANT if `dwc:countryCode` can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the ISO Country Codes list; 
4. otherwise NOT_COMPLIANT

This could be implemented with a local copy of the ISO 3166 Country Codes (likely the better choice for this small, stable list), or with a web service call. 

Any EXTERNAL_PREREQUISITES_NOT_MET can also be read as exception handling, thus: 

1. Return INTERNAL_PREREQUISITES_NOT_MET if the `dwc:countryCode` is `bdq:Empty`; 
2. else 
  - try :
    - Return COMPLIANT if `dwc:countryCode` can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the ISO Country Codes list (https://www.iso.org/iso-3166-country-codes.html, searchable at https://www.iso.org/obp/ui/#search);
  - catch :   
    - Return EXTERNAL_PREREQUISITES_NOT_MET (as the the ISO Country codes list is not available); 
3. otherwise NOT_COMPLIANT

Where a Test is parameterized or when a `bdq:sourceAuthority` is specified in the text of the expected response the `Specification` should include a `bdqffdq:hasAuthoritiesDefaults` data type property containing the parameters, default values, and references to resources, including API endpoints that would provide access to values in the authority. 

Values of `bdqffdq:hasAuthoritiesDefaults` are text strings listing parameters in the form of a semicolon-delimited list of one or more of the following: 
 
- parameter default = "default value" 
- parameter default = "default value" {[resource]}
- parameter default = "default value" {[resource]} {API endpoint [resource]}

The `bdqffdq:hasAuthoritiesDefaults` property may be present in isolation (to make the expected response easier to read) as in the Test [VALIDATION_COUNTRYCODE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD) example above when a Test is not parameterized, or when a Test is parameterized, with corresponding `bdqffdq:Arguments` and `bdqffdq:Parameters`.

See section [Parameterizing the Tests (normative)](../../bdqtest/index.md#33-parameterizing-the-tests-normative) of the [BDQ Tests and Assertions](../../bdqtest/index.md) page for further guidance on `bdq:sourceAuthority` values, `Parameters`, and `Arguments`. 

##### 2.3.2.4 Default Value Strings in Parameters (normative)

When a Test is defined as parameterized, implementations SHOULD support the parameter in addition to the `Information Elements`. 

When a Test is defined as parameterized:
- Implementations MAY choose to only support the default value.
- Implementations MAY choose to not include the parameter(s) in the Test API, that is, only support the default value internally to the Test.
--  Note that some Test Conformance Testing Data provide non-default `Parameter` values, and implementations that only support the default value will be unable to validate against all of the Test Conformance Testing Data (see [8 Validating Test Implementations](#8-validating-test-implementations-normative))).

When the parameter has a default value and a resource, and an implementation includes the parameter in its API, that implementation MUST support the string literal given as the default value, and internally choose the resource "{[resource]}" or "{API endpoint [resource]}" based on that string literal "default value". Implementations MAY also accept other values including the "{[resource]}" or "{API endpoint [resource]}" as the value for the parameter in the API for the Test implementation.

##### 2.3.2.5 Example Interpretation of a Parameter String Default Value (non-normative)

The following code snippet in Java from the FilteredPush `rec_occur_qc` library (Morris 2025) illustrates interpretation of the default value "Creative Commons" when provided as a parameter to an implementation of [AMENDMENT_LICENSE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_LICENSE_STANDARDIZED). The literal "Creative Commons" is accepted as a parameter value.

    @Amendment(label="AMENDMENT_LICENSE_STANDARDIZED", description="Propose amendment to the value of dwc:license using bdq:sourceAuthority.")
    @Provides("dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8-2023-09-18")
    @Specification("EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; AMENDED value of dcterms:license if it could be unambiguously interpreted as a value in bdq:sourceAuthority; otherwise NOT_AMENDED. bdq:sourceAuthority default = 'Creative Commons' {[https://creativecommons.org/]} {Creative Commons licenses [https://creativecommons.org/about/cclicenses/]}")
    public static DQResponse<AmendmentValue> amendmentLicenseStandardized(
        @ActedUpon("dcterms:license") String license,
        @Parameter(name="bdq:sourceAuthority") String sourceAuthority
    ) {
        DQResponse<AmendmentValue> result = new DQResponse<AmendmentValue>();

        if (MetadataUtils.isEmpty(license)) { 
            result.addComment("No Value provided for dcterms:license");
            result.setResultState(ResultState.NOT_AMENDED);
        } else { 
            if (MetadataUtils.isEmpty(sourceAuthority)) { 
                sourceAuthority = "Creative Commons";
            }
            try { 
                MetadataSourceAuthority sourceAuthorityObject = new MetadataSourceAuthority(sourceAuthority);
                if (sourceAuthorityObject.getAuthority().equals(EnumMetadataSourceAuthority.INVALID)) { 
                    result.setResultState(ResultState.EXTERNAL_PREREQUISITES_NOT_MET);
                }
                String pattern = "";
                if (sourceAuthorityObject.getAuthority().equals(EnumMetadataSourceAuthority.CREATIVE_COMMONS)) {
                   ....

This library also includes a method whose signature does not include the parameter, but which runs the implementation of [AMENDMENT_LICENSE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_LICENSE_STANDARDIZED) with the default parameter.

    @Amendment(label="AMENDMENT_LICENSE_STANDARDIZED", description="Propose amendment to the value of dwc:license using bdq:sourceAuthority.")
    @Provides("dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8-2023-09-18")
    @Specification("EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; AMENDED value of dcterms:license if it could be unambiguously interpreted as a value in bdq:sourceAuthority; otherwise NOT_AMENDED. bdq:sourceAuthority default = 'Creative Commons' {[https://creativecommons.org/]} {Creative Commons licenses [https://creativecommons.org/about/cclicenses/]}")
    public static DQResponse<AmendmentValue> amendmentLicenseStandardized(
        @ActedUpon("dcterms:license") String license
    ) {
        return amendmentLicenseStandardized(license, null);
    }

#### 2.3.3 The Concept of "interpreted as" (normative)

In the `hasExpectedResponse` of a `Specification` the phrase "interpreted as" SHOULD BE interpreted by Implementers to mean: 

1. where Darwin Core (Wieczorek et al. 2012) data are serialized as strings, but the Test refers to data as numeric or other non-string data type, can the string value be cast into the target data type in the language of implementation (e.g., "1" as the integer 1), **or**
2. matching a representation of a value unambiguously onto a controlled vocabulary (e.g., ‘WGS84’ to ’EPSG:4326’), **or**
3. interpreting the representation of a numeric value (e.g., a Roman numeral) as a number (e.g., an integer).

When interpretations of strings containing Roman numerals as numbers is intended, guidance associated with the text, usually in the `skos:note` for the Test, MUST be explicit about this meaning. For example, the `skos:note` for the Test [AMENDMENT_MONTH_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_MONTH_STANDARDIZED) states: "Implementations should translate interpretable Roman numerals in the range I-XII in dwc:month as integer month values 1-12, as some natural science domains use Roman numeral months to avoid language and day/month vs month/day order." This is explicit guidance for the meaning of "interpreted as" in the specification for this Test: "AMENDED the value of dwc:month if it can be unambiguously interpreted as an integer between 1 and 12 inclusive".

#### 2.3.4 Handling Leading and Trailing Whitespace (normative)

Whitespace refers to characters such as spaces and tabs that affect rendering of printed or displayed output, but which themselves are not printed (see the [Glossary](../../../index.md#6-glossary-non-normative)). 

A field that only includes whitespace MUST be treated as `bdq:Empty`.

In `bdqffdq:Validation` Tests that require the lookup of a `bdq:sourceAuthority`, leading and/or trailing whitespace may cause the Test to return a NOT_COMPLIANT result as no preprocessing is performed on the data, and the literal value, with leading or trailing whitespace is not exactly matched in the `sourceAuthority`. This behavior MAY be subject to the internals and behavior of external source authorities, and may not be under the control of Test implementers. Leading and trailing whitespaces SHOULD be stripped out in a subsequent `bdqffdq:Amendment` Tests. When the same `bdqffdq:Validation` Test is re-run in a post-amendment phase with the proposed changes applied to its inputs, COMPLIANT results would be expected (if the value matches a value in the `sourceAuthority`).

`Validations` that match input values against a `sourceAuthority` SHOULD perform an exact match against that `sourceAuthority` (unless the Test specifies otherwise).

`Amendments` SHOULD propose changes with leading or trailing whitespace removed unless the Test specifies otherwise.

## 3 Compliant Implementation (normative)

The BDQ Tests are part of a coherent framework for describing and reporting on data quality, and the Tests are intended to be implemented as suites of Tests that fit particular `Use Cases` (see [BDQ Fitness for Use Framework](../../bdqffdq/index.md)). The following sections provide normative guidance on what is required for an implementation of a Test Suite to be compliant with the BDQ standard, and non-normative guidance on the rationale for these requirements and expectations for how implementers will design their Test Suites.

![Non-normative diagram illustrating the relationships among Use Cases, Policies, Tests, Parameters, Implementations and Reports in bdqffdq, use cases are at the top of the diagram linked down to tests (Validations, Measures, Amendments, Issues) via Policies, Tests are shown to be complex composed of many classes and properties, including Specifications which can take Parameters, below these sit Implementations, which can produce data quality reports containing assertions (Response objects):](bdqffdq_overview_diagram.svg)
*Non-normative diagram illustrating the relationships among Use Cases, Policies, Tests, Parameters, Implementations and Reports in bdqffdq:*

### 3.1 Compliance depends on `Use Case` (normative)

The BDQ standard defines a library of Tests that can produce `Data Quality Reports` and can be used in `Quality Control` and `Quality Assurance`.  See the discussion of `Quality Control` and `Quality Assurance` in the [Users Guide](../../guide/users/index.md#21-quality-control-and-quality-assurance-non-normative).  Compliance of Test implementations with the BDQ standard depend upon several conditions:
- Tests can not assert or assure quality independently of a `Use Case`.  
- A `Use Case` (through a set of `Policies`) defining a suite of Tests needed to assert or filter for quality is required. Without it, an implementation of a set of Tests in a `Mechanism` IS NOT compliant with the BDQ standard. 
- All of the Tests required by the `Policies` of a `Use Case` MUST be implemented and individually compliant with BDQ Test specifications in order for the `Use Case` Test suite to be compliant with the BDQ standard. 

Note that BDQ Compliance of a Test Suite implementation does not mean that the `Use Case` that defines the Test Suite is valid or useful, rather, it simply means that every Test in the `Use Case` is (1) in the implementation and (2) each Test implementation is independently compliant with the Test's BDQ specification.

### 3.2 Minimum Test Suite composition (normative)

An implementation of a Test Suite MUST include all `bdqtest:SingleRecord` `Validation`, `Measure`, and `Amendment` Tests for each `Use Case` it implements. An implementation MUST provide complete coverage for at least one `bdqffdq:UseCase`. Implementations MAY include additional Tests and additional `Use Cases`. Implementations SHOULD be explicit about the composition of implemented Tests into `Policies` and `Use Cases`.

### 3.3 Rationale and expectations for suite design (non-normative)

The most important elements of the BDQ standard are the structure that holds explicit descriptions of what a data quality Test is intended to do, and the consistent structure for reporting the results from the execution of a Test upon data. We expect that implementers will implement suites of these Tests that fit their `Data Quality Needs` (their `Use Case`), including Tests that are specifically suited for their domain. The BDQ standard provides a coherent library of Tests that can be applied to the set of defined `bdqffdq:UseCases` in BDQ, and considerable thought has gone into describing Tests that isolate particular data quality issues and work together as a coherent suite.

### 3.4 Required outputs for every Test execution (normative)

Results from each Test MUST be produced in the form `Response.status`, `Response.result`, and `Response.comment`, with one Test producing one Response. Results MAY include `Response.qualifier` (see section [4 Extension Points](#4-extension-points-normative)). The values of `Response.status` and `Response.result` MUST be those specified. This standard is agnostic concerning data structures and serializations of a `Response`. The standard is agnostic concerning internationalization and languages of labels applied to human readable presentations of values within a `Response`. See  [3.1 Structure of Response (normative)](../../bdqtest/index.md#31-structure-of-response-normative) in [BDQ Tests and Assertions](../../bdqtest/index.md) for further normative guidance on `Responses` as RDF or as data structures. See section [5.1 The Response Object](#51-the-response-object-normative) for further normative guidance on `Responses`.

#### 3.4.1 Amendment Response.result ordering (normative)

Within the `Response.result` for an `Amendment` Test, the order of key-value pairs is not specified and MAY vary.

### 3.5 Describing additional Tests (normative)

Additional Tests that conform to the BDQ standard MUST describe those Tests using the BDQ [Fitness for Use Framework Ontology](../../bdqffdq/index.md), those Tests MUST use the same `Response` structures, and those Tests MUST be related to `bdqffdq:UseCases`, either those defined in the standard or additional `Use Cases`.

### 3.6 Parameterized Tests: default behavior and unsupported values (normative)

Implementations MUST provide Parameterized Tests that support the default `Parameter` values. Implementations SHOULD provide for Parameterized Tests to take parameters, but MAY produce an implementation of a Parameterized Test that takes no parameters but only uses a default parameter value applicable within their domain.

BDQ does not specify how a Test implementation is to respond when given a `Parameter` value that is not supported by the implementation. Implementers SHOULD handle this in a manner appropriate for their implementation framework. Unless otherwise noted in properties of the `Specification`, implementations MUST NOT use `Response.status`="EXTERNAL_PREREQUISITES_NOT_MET" to indicate a non-supported parameter value.

### 3.7 Bulk / non-Framework execution (normative)

Implementers are encouraged to produce the means to test data quality in bulk in settings such as SQL queries on relational data stores where construction of `Response` objects is not feasible, but the logic of a specification (`hasExpectedResponse`) can be framed as a question on a data store. Such non-Framework implementations MUST NOT assert compliance with the BDQ standard.

## 4 Extension Points (normative)

A response MAY include a `Response.qualifier` (in RDF, a `bdqffdq:hasResponseQualifier` object property on an instance of a `bdqffdq:Assertion`). This is intended as a place to include structured `Assertions` concerning uncertainty in a response. This is also intended as a place to include structured `Assertions` about the details of `Amendment` Tests (e.g., TRANSPOSED MAY be attached to a `Response.qualifier` for some `Amendment` Tests).

`MultiRecord` (`bdqffdq:MultiRecord`) `Measures` that count results from `SingleRecord` Tests (that is, that return counts where the input `Information Element` consists of `Response` values from Tests on `Single Records` (`bdqffdq:SingleRecord`)) MUST report only a single count as the `Response.result`.  Such `MultiRecord` `Measures` MAY provide a `Response.qualifier` containing structured data describing additional information such as the total number of `Single Records` evaluated (to calculate percentages), the number of each value of `Response.status` encountered, and the number of each `Response.result` encountered. `Measures` under the Framework are only allowed to return "COMPLETE", "NOT_COMPLETE", or a single number. If it is desirable for any `Measure` to return more than a single number, `Response.qualifier` is the extension point to use. 

## 5 Responses from Tests (normative)

### 5.1 The Response Object (normative)

The four Test Types (`Validation`, `Issue`, `Amendment`, and `Measure`) all provide a `Response` from the execution of the Test. The `Response` from a Test is an `Assertion` which MAY form part of a `Data Quality Report` or MAY be wrapped in an `Annotation`.   

Responses from each of the Tests MUST consist of structured data, and MUST NOT be simple pass fail flags. 

The Response MUST include the following three components: 

1. `Response.result` is a result returned for a Test - a controlled vocabulary consisting of "COMPLIANT" or "NOT_COMPLIANT" for `Validation` Tests, "NOT_ISSUE" or "POTENTIAL_ISSUE" for `Issue` Tests, either a numeric value or a controlled vocabulary consisting of "COMPLETE" or "NOT_COMPLETE" for `Measure` Tests, and a data structure (e.g., a list of key value pairs) for proposed changes for `Amendment` Tests.

2. `Response.status` provides a controlled vocabulary, metadata concerning the success, failure, or problems with the Test. The `Response.status` also serves as a link to information about warning type values and, in the future, probabilistic `Assertions` about the likeliness of the value could be made. 

3. The `Response.comment` supplies human-readable text describing reasons for the Test result.

### 5.1.1 Amendment Test Responses (normative)

An `Amendment` Test may propose a change to a value found in an existing Darwin Core (Wieczorek et al. 2012), or a set of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021), including potentially filling in a missing value. `Amendment` Tests are intended to improve one or more components of the quality of the record. The `Response.result` from an `Amendment` Test MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database of record when a `Data Quality Report` is used for Quality Control of an existing record. Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed `Amendments` as part of a pipeline in preparing data for an analysis. The Framework also supports changes to procedures but we have not framed any such Tests in this form.

An `Amendment` Test `Response.result` SHOULD consist of a set of key:value pairs, where each key is an `Information Element` to be modified, and each value is a proposed new value for that `Information Element`. The `Response.result` key:value pairs SHOULD be a JSON serialization of the proposed changes.

Under the Fitness For Use Framework, `Amendment` Tests may propose changes to processes as well as data.  BDQ prescribes no structure for the `Response.result` of an `Amendment` Test that proposes changes to processes.  Implementers MAY develop their own structures and serializations for the `Response.result` of `Amendment` Tests that propose changes to processes.

### 5.1.2 Response Serialization and Presentation (normative)

Nothing in this section should be taken as a requirement for a particular format or serialization of `bdqffdq:Assertions` or `Responses`. Implementations MAY serialize `Assertions` in any appropriate form for their needs.

Nothing in this document should be taken as a requirement for how `bdqffdq:Assertions` or `Responses` are to be presented to consumers of `Data Quality Reports`. Implementations MAY present the results of Tests in any form appropriate for their consumers.

### 5.1.3 Further Guidance on Responses (non-normative)

See [3.1 Structure of a Response (normative)](../../bdqtest/index.md#31-structure-of-response-normative) in [BDQ Tests and Assertions](../../bdqtest/index.md) for further normative guidance on representing Responses as RDF or in data structures.

See [Definitions for Named Individuals](../../list/bdqffdq/index.md#complete) in the `bdqffdq:` ontology for formal definitions of the named individuals that are used as values (e.g. COMPLIANT, NOT_COMPLIANT, RUN_HAS_RESULT) for `Response.status` and `Response.result` in the expected responses of Test specifications.

### 5.1.4 Results from Measures (normative)

Measure Tests that return numeric values MUST return a single numeric value in `Response.result`. The value MAY be zero, a positive or negative integer, or a real number. Implementers SHOULD be mindful of interoperability issues when numbers are serialized or exchanged across programming languages, runtimes, or storage systems (for example, loss of integer precision, floating-point rounding differences, and handling of non-finite values such as NaN or ±Infinity).

`Measure` Tests that return "COMPLETE" or "NOT_COMPLETE" MUST return one of those two values as the `Response.result`. 

A single `Measure` Test MUST NOT return a list of numbers.  A single `Measure` Test MUST NOT return a list of "COMPLETE"/"NOT_COMPLETE" values.

### 5.2 Framework Elements Not Included in BDQ Test Descriptions (normative)

Implementers SHOULD create an instance of `bdqffdq:Mechanism` to uniquely identify their suite of Test `Implementations`.

Implementations producing `Data Quality Reports` SHOULD create instances of `bdqffdq:Assertions` grouped in `bdqffdq:DataQualityReports` that also specify the `bdqffdq:DataResource` that the `bdqffdq:DataQualityReport` concerns.

Implementers MUST provide `Response` data in `Data Quality Reports` consisting of `Response.status`, `Response.result`, and `Response.comment`.

Implementations MAY perform data `Quality Control`, data `Quality Assurance`, or both. 

## 6 Guidelines for Implementers (normative)

### 6.1 Parameters and Changing the Behavior of a Test (normative)

Many Tests specify `bdqffdq:Parameters` that are intended to change the behavior of a Test to fit local `Data Quality Needs` without changing the `Specification` of the Test.

A Parameterized Test will behave differently on the same data when using different `Parameter` values. 

Implementers SHOULD only present non-default `Parameter` values to a Test implementation if needed for local `Data Quality Needs`. 

#### 6.1.1 Identifying non-default `Parameter` values in reports (normative)

When a Test is executed with non-default `Arguments` specified for `Parameters`, consumers of `Assertions` and Data Quality Reports resulting from such MUST be able to tell that non-default `Arguments` were used, and what the non-default values were.

When a Test is Parameterized, and a value other than the default value is used for some `Parameter`, reports: SHOULD identify the Tests using at least:
- the `Label` (`rdfs:label`) for the Test class, 
- in combination with the `Parameter`, 
- and the value of the argument that replaced the `Parameter` in this specific case.

For example: "VALIDATION_MINDEPTH_INRANGE with bdq:maximumValidDepthInMeters=1642"  (Label with Parameter=non-default value).

When a non-default `Argument` is used, a new instance of an `Implementation` linked to a new instance of a `Specification` linked to an instance of an `Argument` asserting the non-default value SHOULD be used. 

When `Assertions` are represented in RDF an `Assertion` produced by a Test run with a non-default `Argument` value
- MUST NOT be linked to the instance of the `Specification` with the `Argument` with the default value, 
- MUST be linked to novel instances of `Implementation`, `Specification`, and `Argument`, such that a query on the `Assertion` can identify what `Argument` value was used for the `Parameter` to produce the `Assertion`. It is the novel instances of these classes that provides the non-default value for software consumers.

#### 6.1.2 Identifying non-default `Parameter` values in `Response.comment` (normative)

When a non-default `Argument` is used, a `Response.comment` SHOULD include the `Parameter` and the non-default value. This provides the non-default value for human consumers.

#### 6.1.3 Expectations for Tests with `Parameters` (normative)

An implementation of a Test:
- MUST support the Test execution with the default `Parameter` values.
- MAY optionally support other `Parameter` values. 
- Provided `Parameters` MUST NOT change the behavior of the Test to depart from the `Specification` `hasExpectedResponse`. 
- `Parameters` MUST only change the behavior of the Test as specified in the `Specification` `hasExpectedResponse`.

#### 6.1.4 Test departures from specifications (normative)

An implementation of a Test that, by design, has a behavior that departs from the `Specification` `hasExpectedResponse` MUST be identified by different identifiers than the BDQ Test from which it departs.  

An implementation of a parameterized Test that only supports non-default `Parameter` values MUST be identified by different identifiers than the BDQ Test that supports the default `Parameter` values.  For example, an implementation of VALIDATION_LICENSE_STANDARD that does not support the default bdq:sourceAuthority "Creative Commons 4.0 Licenses or CC0", but only supports a different source authority is not the same test as VALIDATION_LICENSE_STANDARD, and must be identified by a different identifier.

#### 6.1.3 Further guidance on `Parameters` and `Arguments` (non-normative)

See also the [Test Parameters](../../guide/users/index.md#34-test-parameters-non-normative) section in the [User's Guide)](../../guide/users/index.md) for further guidance on `Parameters` and `Arguments`.

### 6.2 Execution Process Agnostic (non-normative)

The Test descriptions in the BDQ standard are designed to be able to be used anywhere in the life cycle of biodiversity data, and are designed to be independent of the environment in which the Tests are run. Test implementations may be run within a framework that evaluates entire records one at a time, behind user interface elements that evaluate single `Information Elements` one at a time, on streams of data within workflows, on distinct values aggregated within streams of data within workflows, and more.

Tests may be run

- at the point of initial collection or observation of organisms,
- to support data transcription,
- in loading data into databases of record from field or transcription sources,
- in preparing data from databases of record for aggregation,
- during data aggregation,
- individually on single Darwin Core records,
- on fragments of Darwin Core (Wieczorek et al. 2012) records within a data capture interface,
- in sequence in a processing pipeline of Darwin Core records, or
- in parallel in a processing pipeline of Darwin Core records, or
- in a workflow environment that produces lists of unique values of `Information Elements` for each Test, executes the Test on the unique values, and then maps the results back out into rows in the dataset.

Data may be presented to an execution framework as [Simple Darwin Core](https://dwc.tdwg.org/simple/), or as Structured Darwin Core, or in another structure that can be mapped to the `Information Elements` of relevant Tests. The commonalities the Tests support are clearly defined specific Tests, which produce standard outputs from input `Information Elements` onto which domain specific terms (i.e., Darwin Core) are mapped.

Multiple sequential and parallel workflows that process streams of data are possible. One possible workflow for Test execution is to group the unique values of applicable `Information Elements` within a `bdqffdq:MultiRecord` from each `Validation` or `Measure` Test, and then execute the `Validation` or `Measure` Tests on the unique values, and then disaggregate the results back to each `bdqffdq:SingleRecord`. This is analogous to performing Tests as SQL queries. Another possible workflow is to present each data record sequentially to all of the `Validation` and `Measure` Tests. Yet another is to split the data into streams by `Information Element`, and then, in parallel, present data in each streams to relevant Tests.

### 6.3 Considerations for Test Execution (normative)

Many Tests invoke external `bdq:sourceAuthorities`. Some of these `bdq:sourceAuthorities` are downloadable vocabulary files, others are web services with changing data.

Implementations of Tests SHOULD locally cache the results of calls to remote web services, particularly if they operate on a sequence of `bdqffdq:SingleRecords` instead of operating on distinct values of `bdqffdq:InformationElements`. Data sets typically contain many repeated values, and remote web services SHOULD NOT be subject to repeated requests using the same question. 

Some source authorities are highly stable small vocabularies. Implementers MAY choose to query a local copy of such a vocabulary, even if a remote service is specified in a `bdq:sourceAuthority` for a Test. Implementers SHOULD monitor for changes to that vocabulary in the authoritative source and update local data when changes occur. 

### 6.4 Order of Test Execution (normative)

#### 6.4.1 Phases: Pre-Amendment, Amendment, Post-Amendment (normative)

Tests MAY be run in Pre-Amendment, Amendment, and Post-Amendment phases.

##### 6.4.1.1 Explanation of Phases (non-normative)

A good practice for executing the BDQ Tests is to follow a sequence that begins by executing all `bdqffdq:SingleRecord` `Validation` and `Measure` Tests in a pre-amendment phase. Then, to execute all `Amendment` Tests in an amendment phase. Finally, re-run all `Validation` and `Measure` Tests on the data with the proposed changes asserted by the `Amendments` applied to the data in a post-amendment phase. Such a sequence of phases allows `Assertions` to be made first about the quality of the data as they were initially presented, and then about how much the quality of the data would be improved if all proposed changes from the `Amendments` were accepted. The order and method of running `Validation` and `Measure` Tests within the pre-amendment and post-amendment phases is not specified by the BDQ standard. Within pre-amendment and post-amendment phases, the `Validation` and `Measure` Tests are agnostic about the order in which they are run, the extent to which they are run in parallel, or the extent to which they are run on single records or on unique values within a dataset.

##### 6.4.1.2 Phases and Quality Assurance (normative)

It is RECOMMENDED, for Quality Assurance with the current suite of BDQ Tests, to run all pertinent (to a `Use Case`) `bdqffdq:SingleRecord` `Validation` and `Measure` Tests, then run all pertinent `MultiRecord` `Measures` that return "COMPLETE" or "NOT_COMPLETE"". These `Measures` MAY be used as filters. Exclude records from the dataset until all `MultiRecord` `Measure` Tests return "COMPLETE". This, under the mathematical formulation of the Framework, is the assertion that the data are fit for the purpose of the selected `Use Case`. This process MAY be performed in a single `Validation` and `Measure` phase without `Amendments`. This process MAY be performed on a post-amendment phase with all or selected proposed changes from `Amendments` accepted into the data stream. Acceptance of proposals for changes to the data in a processing stream SHOULD NOT be done blindly, and SHOULD involve thoughtful consideration of the proposed changes.

##### 6.4.1.3 Phases and Quality Control (normative)

Under Quality Control, `bdqffdq:MultiRecord` `Measure` Tests that return numeric values MAY be used to assess the prevalence of quality issues in the data with respect to the selected `bdqffdq:UseCase`. This MAY be done in a pre-amendment phase and again in a post-amendment phase with all proposed changes applied to the data stream to evaluate how much accepting proposed `Amendments` would improve the data. Acceptance of proposals for changes to the data in a processing stream SHOULD NOT be done blindly, and SHOULD involve thoughtful consideration of the proposed changes.

Numeric values from `MultiRecord` `Measure` Tests under Quality Control MAY be used to identify areas to target effort to improve data quality in a database of record for one or more `Use Cases`.

#### 6.4.2 Test Dependencies (normative)

While BDQ Tests are designed to be independent and agnostic to sequence of test execution, some `Amendment` Tests have potential interactions given the by-design redundancies in Darwin Core (Wieczorek et al. 2012). In consequence the order of execution of some `Amendment` Tests can affect results. This is a particular concern when developing workflows with parallel data streams. When `Amendment` Tests are executed in a workflow where downstream `Amendments` operate on data with the changes proposed by upstream `Amendments` applied, the following sequences SHOULD be followed.

Given that `Amendment` Tests propose a value to a primary term (e.g., `dwc:eventDate`, `dwc:taxonID`) from secondary terms (e.g., `dwc:day`, `dwc:year`, `dwc:scientificName`), primary-from-secondary SHOULD be applied before secondary-from-primary. Where multiple `Amendments` on secondary terms could propose conflicting changes to a primary term, the sequence of `Amendment` Tests SHOULD be ordered. 

For `dwc:eventDate`:

| Order | Test |
|-------|------|
| 1 | [AMENDMENT_EVENTDATE_FROM_VERBATIM](../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_VERBATIM) |
| 2 | [AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR](../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR) |
| 3 | [AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY](../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY) |
| 4 | [AMENDMENT_EVENTDATE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_STANDARDIZED) |
| 5 | [AMENDMENT_EVENT_FROM_EVENTDATE](../../terms/bdqtest/index.md#AMENDMENT_EVENT_FROM_EVENTDATE)

See [5.2.1 Diagram of the NAME-oriented Tests and Information Elements Acted Upon (non-normative)](../../supplement/index.md#523-diagram-of-the-time-oriented-tests-and-information-elements-acted-upon-non-normative) in [BDQ Supplemental Information](../../supplement/index.md)for the relationships between the Tests and associated `Information Elements` `Acted Upon` that operate on aspects of date and time (Darwin Core class `dwc:Event`). 

Similarly, for `dwc:taxonID`:

| Order | Test |
|-------|------|
| 1 | [AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON](../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON) |
| 2 | [AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID) |

The corresponding [NAME Tests diagram](../../supplement/index.md#521-diagram-of-the-name-oriented-tests-and-information-elements-acted-upon-non-normative) displays the Tests and associated `Information Elements` `Acted Upon` that operate on aspects of taxonomic name (Darwin Core class `dwc:Taxon`).

See also the [SPACE Tests diagram](../../supplement/index.md#522-diagram-of-the-space-oriented-tests-and-information-elements-acted-upon-non-normative) and the [OTHER Tests diagram](../../supplement/index.md#524-diagram-of-the-other-oriented-tests-and-information-elements-acted-upon-non-normative).

The BDQ standard does not specify how the ordering of these Tests should be accomplished. Ordering of Tests COULD be done by describing an `Amendment` Test with an expected response that specifies the execution of each Test in order. Such a composition of `Amendment` Tests would be the preferred method of sequencing under the Framework, but to keep Tests as independent a possible, and to allow the maximum flexibility for the composition of Tests in Profiles to support `bdqffdq:UseCases`, the BDQ standard does not provide such a Test specification. Ordering of Tests could be done by providing a configuration file for a Test execution framework specifying Test dependencies. Ordering could be supported in a workflow environment by composing a workflow to execute these Tests in sequence. The order specified above SHOULD be followed.

##### 6.4.2.1 Terms for describing Test Dependencies (non-normative)

The [Fitness for Use Framework Ontology](../../bdqffdq/index.md) does not include a property to describe sequence inter-dependencies among `Amendments`. The Ontology does provide the terms `bdqffdq:targetedMeasure`, `bdqffdq:targetedValidation`, and `bdqffdq:TargetedIssue`, which could be used, together with `bdqffdq:improvedBy` to relate `Amendment` Tests to `Validation`, `Measure`, and `Issue` Tests. The BDQ standard does not use these terms to describe Test interrelationships, though they could be used for this purpose. 

#### 6.4.3 Implementing a complete Test (normative)

An implementation of a Test MAY be complete as described with `bdqffdq:` terms in [BDQ Tests and Assertions List of Terms](../../list/bdqtest/index.md). A complete Test implementation MUST encompass the elements of the Test defined in an instance of `bdqffdq:DataQualityNeed`, plus its associated `bdqffdq:InformationElements`, instance of a subclass of `bdqffdq:Method`, instance of `bdqffdq:Specification`, any related `Arguments` and `Parameters`, and MUST be able to produce instances of `bdqffdq:Assertion` (carrying `Response.status`, `Response.result`, `Response.comment`). In contrast, see Section [6.4.6 Implementing an Abstract Test (normative)](#646-implementing-an-abstract-test-normative) for settings where implementations may abstractly consider only the instance of `bdqffdq:DataQualityNeed` with its associated `bdqffdq:InformationElements`.

#### 6.4.4 Presenting Darwin Core Data to a Method that Implements a Test (non-normative)

One complexity introduced by the abstraction of Tests into APIs that take [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) as input and output is to make sure that `Response` objects are correctly mapping Darwin Core terms loaded in an execution framework onto the parameters of an implementation method. Consider an implementation of the Test [VALIDATION_ENDDAYOFYEAR_INRANGE](../../terms/bdqtest/index.md#VALIDATION_ENDDAYOFYEAR_INRANGE) that has the following method signature: 

    public Response validationEnddayofyearInrange(String startDayOfYear, String eventDate) 

If an implementation framework calls this method, reversing the binding of `dwc:startDayOfYear` and `dwc:eventDate`, for example: 

    Response endDayTestResponse = validationEnddayofyearInrange(eventDate, startDayOfYear);

the Test will not return the desired result, even if the implementation is correct. Thus correct matching of input terms to the implementation of each Test is critical. 

Multiple approaches are possible to correctly match input Darwin Core terms onto method signatures for methods that implement Tests. 

##### 6.4.4.1 Binding Darwin Core Data (normative) 

The BDQ standard is entirely agnostic as to how the binding between domain terms (i.e., input Darwin Core terms) and `Information Elements` considered inside Test implementations is done. Implementers MAY freely implement in any appropriate way for their environment. However, Test Implementations MUST provide structured `Responses` containing `Response.status`, `Response.result`, and `Response.comment`.

Implementations MAY define objects corresponding to the set of `Information Elements` for each Test, and may pass the object to the Test implementation (pushing the problem of binding input values to the correct properties of these objects upstream).  Implementations MAY operate on domain objects (e.g., Darwin Core objects), with a Test implementation taking a domain object as input and extracting the `Information Element` `Acted Upon` and the `Information Element` `Consulted` from that object internally. Implementations MAY be methods on domain objects (e.g., Darwin Core objects) and assert the results as properties of the domain object.

Implementers MAY use any approach appropriate for their language(s) and environment to pass data into Test implementations.

##### 6.4.4.2 Examples of matching input Darwin Core to Method parameters (non-normative) 

If a Test implementation is a function that takes Darwin Core terms as input parameters, the function (or method) call becomes the point of concern for correctly matching input Darwin Core terms to the `Parameters` of the Test (function or method).

In Java, annotating method parameters and using reflection to bind between the execution framework and Test implementations works well. Following is a simplified code snippet from the FilteredPush `event_date_qc` library (Morris & Lowery 2025) that uses Java annotations, (e.g., @ActedUpon(value="dwc:endDayOfYear") to provide metadata about which parameter goes with which `Information Element`.

    public Response validationEnddayofyearInrange(
            @ActedUpon(value="dwc:endDayOfYear") String endDay,
            @Consulted(value="dwc:eventDate") String eventDate) {

An execution framework can use reflection to determine, from the annotations on the parameter, which Darwin Core term to bind to which parameter.

Additional metadata can be added in Java annotations. In the following, again from the FilteredPush `event_date_qc` (Morris & Lowery 2025) library, annotations enable an implementation framework to look up a Test implementation by the Test GUID, and can provide metadata about the Test to users. For maintenance, annotations can be used to determine if an implementation is up to date with the latest version of a Test specification.

    @Validation(label="_ENDDAYOFYEAR_INRANGE", description="Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?")
    @Provides("9a39d88c-7eee-46df-b32a-c109f9f81fb8")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8-2023-09-18")
    @Specification("INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is bdq:Empty or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT")
    public static DQResponse<ComplianceValue> validationEnddayofyearInrange(
            @ActedUpon(value="dwc:endDayOfYear") String endDay,
            @Consulted(value="dwc:eventDate") String eventDate) {
        ....
    } 

This approach will only work with a subset of programming languages.

In many languages, a domain object can be passed as a method parameter.

    public Response validationEnddayofyearInrange(Event event) { 
        
    }

Here, both the execution framework and the internals of the validationEnddayofyearInrange method must be able to work with the `Event` (object or structure) and work with its `Event.enddayofyear` and `Event.eventdate` properties.

It is also possible to implement this in an object-oriented manner as methods on a class: 

    public class Event() { 

        private eventDate;
        private enddayofyear;

        public Response validationEnddayofyearInRange()...

    } 

Other approaches are also possible.

#### 6.4.5 Example Test Implementations (non-normative)

##### 6.4.5.1 Example in Pseudocode (non-normative)

A specification (the content of a `hasExpectedResponse` property of a `Specification`) is a sequence of statements in the form of a string representing the `Response` followed by the `Criteria` that would result in that `Response`. Thus, given the following specification: 

```
EXTERNAL_PREREQUISITES_NOT_MET if the bdq:SourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if the value of dwc:countryCode is found in bdq:sourceAuthority; otherwise NOT_COMPLIANT
```

'EXTERNAL_PREREQUISITES_NOT_MET' is a `Response` and 'if the `bdq:SourceAuthority` is not available' is the `Criterion`.

The expected response provides a sequence of `Criteria` to evaluate. This should be done in the order specified in the expected response, except for EXTERNAL_PREREQUISITES_NOT_MET, which can be handled as an exception raised from an invocation of an external resource.

Following is pseudocode that follows the same order of evaluation of the `Criteria`, returning a result for the first matched `Criterion`, or EXTERNAL_PREREQUISITES_NOT_MET for the first failure to invoke the external resource. 

```
    Function validationCountrycodeStandard(countryCode) returns Result {
      String sourceAuthority = "ISO 3166-1-alpha-2"
      Result result = new Result()
      try { 
          if (isEmpty(countryCode) { 
              result.setStatus(INTERNAL_PREREQUISITES_NOT_MET) 
              result.setComment("provided countryCode is empty."
          } else {
              result.setStatus(RUN_HAS_RESULT) 
              if (isFoundCountryCode(countryCode,sourceAuthority)) { 
                 result.setValue(COMPLIANT)
                 result.setComment("provided countryCode ["+countryCode+"] is a known "+sourceAuthority+" countryCode ")
              } else { 
                 result.setValue(NOT_COMPLIANT)
                 result.setComment("provided countryCode ["+countryCode+"] is not a known "+sourceAuthority+" countryCode ")
              }
          } 
      } catch NetworkException {
          result.setStatus(EXTERNAL_PREREQUISITES_NOT_MET) 
          result.setComment("Temporary failure looking up countryCode, try later")
      }
      return result
    }

    Function isfoundCountryCode(countryCode,sourceAuthority) returns boolean throws NetworkException {...}
```

The `Criteria` for EXTERNAL_PREREQUISITES_NOT_MET do not have to be evaluated first, but would be expected to be raised from wherever in the sequence the external resource first fails to be invoked, and is handled within the construct that builds a `Result` object.

Note that this implementation will reach the block that can return EXTERNAL_PREREQUISITES_NOT_MET only if the input `dwc:countryCode` contains a value. This deviation from the logical sequence implied by the specification (EXTERNAL_PREREQUISITES_NOT_MET if the `bdq:SourceAuthority` is not available; INTERNAL_PREREQUISITES_NOT_MET if the `dwc:countryCode` was EMPTY;) is perfectly acceptable, for the case of network resources being evaluated later in the implementation than other conditions.

Below is pseudocode for a similar implementation as a method on a Darwin Core domain object, less general, and more tightly bound to the domain concept, but making the concern of correctly binding input data to domain concepts not a concern of the Test. 

```
    class flatDarwinCore {
       property countryCode

       method setCountryCode(countryCode) { 
          this.countryCode = countryCode
       } 

        method validationCountrycodeStandard() returns Result {
          String sourceAuthority = "ISO 3166-1-alpha-2"
          Result result = new Result()
          try { 
              if (isEmpty(this.countryCode) { 
                  result.setStatus(INTERNAL_PREREQUISITES_NOT_MET) 
                  result.setComment("provided countryCode is empty."
              } else {
                  result.setStatus(RUN_HAS_RESULT) 
                  if (AuthorityUtility.isFoundCountryCode(this.countryCode,sourceAuthority)) { 
                     result.setValue(COMPLIANT)
                     result.setComment("provided countryCode ["+this.countryCode+"] is a known "+sourceAuthority+" countryCode ")
                  } else { 
                     result.setValue(NOT_COMPLIANT)
                     result.setComment("provided countryCode ["+this.countryCode+"] is not a known "+sourceAuthority+" countryCode ")
                  }
              } 
          } catch NetworkException {
              result.setStatus(EXTERNAL_PREREQUISITES_NOT_MET) 
              result.setComment("Temporary failure looking up countryCode, try later")
          }
          return result
       }
    }
```

##### 6.4.5.2 Example in Java (non-normative)

Consider the following Test `Specification` for [VALIDATION_DAY_STANDARD](../../terms/bdqtest/index.md#VALIDATION_DAY_STANDARD) from BDQ: 

Specification: 

```
hasExpectedResponse: INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.
```

`Information Elements` `Acted Upon`: `dwc:day`

Below is an example implementation from the FilteredPush `event_date_qc` library (Morris & Lowery 2024). In this implementation, Java annotations are used to provide metadata that can be used by an implementation framework to pick out a Test to run by its Term Version IRI (`rdf:about`) or Term Name (`rdf:value`) and match an input Darwin Core term to a (Java) parameter in the method signature. The implementation walks through the elements of the `hasExpectedResponse` in sequence, and return the first matching response in a `Response` object, which has `Response.state`, `Response.result` (here called value), and `Response.comment` properties.

```
    @Validation(label="VALIDATION_DAY_STANDARD", description="Is the value of dwc:day an integer between 1 and 31 inclusive?")
    @Provides("47ff73ba-0028-4f79-9ce1-ee7008d66498")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498-2023-09-18")
    @Specification("INTERNAL_PREREQUISITES_NOT_MET if dwc:day is EMPTY; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.")
    public static DQResponse<ComplianceValue> validationDayStandard(@ActedUpon("dwc:day") String day) {
        DQResponse<ComplianceValue> result = new DQResponse<ComplianceValue>();

		if (DateUtils.isEmpty(day)) {
			result.addComment("No value provided for day.");
			result.setResultState(ResultState.INTERNAL_PREREQUISITES_NOT_MET);
		} else {
			try {
				int numericDay = Integer.parseInt(day.trim());
				if (DateUtils.isDayInRange(numericDay)) {
					result.setValue(ComplianceValue.COMPLIANT);
					result.addComment("Provided value for day '" + day + "' is an integer in the range 1 to 31.");
				} else {
					result.setValue(ComplianceValue.NOT_COMPLIANT);
					result.addComment("Provided value for day '" + day + "' is not an integer in the range 1 to 31.");
				}
				result.setResultState(ResultState.RUN_HAS_RESULT);
			} catch (NumberFormatException e) {
				logger.debug(e.getMessage());
				result.setValue(ComplianceValue.NOT_COMPLIANT);
				result.setResultState(ResultState.RUN_HAS_RESULT);
				result.addComment(e.getMessage());
			}
		}
		return result;
    }
```

#### 6.4.6 Implementing an Abstract Test (normative)

In some environments, an implementation MAY be a lightweight implementation of an abstract Test. Such abstract implementations MAY encompass only the elements of the Test defined in an instance of `bdqffdq:DataQualityNeed`, plus its associated `bdqffdq:InformationElements`, and may not be able to produce instances of `bdqffdq:Assertion`, but SHOULD be able to produce analogs of `Response` objects (with `Response.status`, `Response.result`, and `Response.comment` properties). 

Consider the `Validation` Test [VALIDATION_ENDDAYOFYEAR_INRANGE](../../terms/bdqtest/index.md#VALIDATION_ENDDAYOFYEAR_INRANGE)

An SQL query that implements the abstract concept of the `dwc:enddayofyear` being in range could take the following form, using available database fields that contain data related to the abstract `Information Element`, but are not precisely mapped to the concrete `Acted Upon` and `Consulted` [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) in the specification. This query produces a `Data Quality Report` with: 

```
    SELECT collecting_event_id, enddayofyear,
         'VALIDATION_ENDDAYOFYEAR_INRANGE' as test, 'NOT_COMPLIANT' as response_result, 'RUN_HAS_RESULT' as response_status, 
         'The value of enddayofyear [' || enddayofyear ||'] is not an integer between 1 and 365 inclusive, or 366 if ended_date falls in a leap year.' as response_comment
    FROM collecting_event
    WHERE NOT ( 
          enddayofyear BETWEEN 1 AND 365
          OR (
             enddayofyear = 366
             AND 
             (
                 ( 
                   MOD(EXTRACT (year from TO_DATE(ended_date, 'yyyy-mm-dd')),4) = 0
                   AND
                   MOD(EXTRACT (year from TO_DATE(ended_date, 'yyyy-mm-dd')),100) != 0
                 )
                 OR
                 MOD(EXTRACT (year from TO_DATE(ended_date, 'yyyy-mm-dd')),400) = 0
             )
          )
        );
```

#### 6.4.7 Implementing a Test in a Specific Environment (non-normative)

Given data stored in a known and controlled environment, Test implementations can be specifically tailored to that environment, both in language and in assumptions about formats and data types. 

Consider the `Validation` Test [VALIDATION_DAY_STANDARD](../../terms/bdqtest/index.md#VALIDATION_DAY_STANDARD) with the `hasExpectedResponse`:

```
INTERNAL_PREREQUISITES_NOT_MET if dwc:day is EMPTY; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT."
```

Given a hypothetical Event table with fields including a primary key `event_id` and an integer field `day`, an implementation of VALIDATION_DAY_STANDARD in SQL that operates on data in the aggregate might look like:

    SELECT
        ‘VALIDATION_DAY_STANDARD’ as test name, 
        event_id,
        ‘INTERNAL_PREREQUISITES_NOT_MET’ as Result_status, 
        null as Result_value,
        ‘No value for dwc:day to evaluate’ as Result_comment 
    FROM event
        WHERE day is null
    UNION 
    SELECT
        ‘VALIDATION_DAY_STANDARD’ as test name, 
        event_id,
        ‘RUN_HAS_RESULT’ as Result_status, 
        ‘COMPLIANT’ as Result_value,
        ‘Value of dwc:day [‘|| day ||’] is in the range 1-31’ as Result_comment 
    FROM event
        WHERE day >=1 and day <=31
    UNION 
    SELECT
        ‘VALIDATION_DAY_STANDARD’ as test name, 
        event_id,
        ‘RUN_HAS_RESULT’ as Result_status, 
        ‘NOT COMPLIANT’ as Result_value,
        ‘Value of dwc:day [‘|| day ||’] is outside the range 1-31’ as Result_comment 
    FROM event
        WHERE day < 1 or day > 31


This implementation is dependent on the schema the data are stored in, in particular, the definition of `event.day` as a field holding integers.

This implementation does not generalize, as for example, day in a numeric data type that supports numbers in addition to integers would return incorrect values (per the Test specification, which requires day to be an integer), for values of day such as "8.5"

Implementations should carefully consider the assumptions inherent in the environment on which Tests are being run. For example, the FilteredPush implementations in `event_date_qc` (Morris & Lowery 2025), `sci_name_qc` (Morris & Dou 2025), `rec_occur_qc` (Morris 2025), and `geo_ref_qc` (Morris & Lowery 2025b), expect that all data will be presented to the Test methods as strings. Therefore each Test implementation that deals with numeric values must convert the input strings to appropriate numeric types for evaluation, and can use the failure to convert the data type as a means to identify INTERNAL_PREREQUISITES_NOT_MET.

## 6.5 Common Pattern for Implementing a Test (non-normative)

This section provides language- and framework-agnostic checklists that implementers can use to write (or review) implementations of BDQ `Validation` and `Amendment` Tests. It summarizes common conventions used in existing implementations, while remaining independent of any particular execution environment.


### 6.5.1 Responsibilities of a Test (non-normative)

BDQ keeps Tests portable by standardizing semantics (inputs, decision rules, outputs).  It deliberately leaves execution mechanics (binding to input data, orchestration of test execution, presentation of test output) to whatever framework fits the implementer's environment.  

The definition of a test focuses on (1) the inputs (`Information Elements` `Acted Upon` and `Consulted`, and any `Parameters`), then (2) the logic or decision rules of the expected response, with (3) all tests returning a similarly structured Response consisting of a `Response.status`, `Response.result`, and `Response.comment`. 

The description of a test, in essence, frames an API with `Information Element` and `Parameter` inputs, and a standard Response output, encapsulating the logic and decision rules of the expected response. The responsibility of a Test implementation lies in correctly implementing the logic and decision rules of the expected response, and in producing the expected structured output.  The responsibility of an execution framework lies in correctly binding input data to the `Information Elements` and `Parameters` of a Test implementation, and in correctly presenting the structured output from a Test implementation.

The checklists below are designed to help implementers ensure that their implementations of Tests follow this separation of concerns, are consistent with the semantics of the Test as defined in the BDQ standard, and that they produce the expected structured outputs.

### 6.5.1 Checklist for a Validation test (non-normative)

1 Implement utility functions or methods to evaluate `bdq:Empty` and bdq:NotEmpty consistently (see Section 2.2, “The Concept of `EMPTY` in the BDQ Standard (normative)”).

1 **Confirm the required inputs**
   - Identify the `Information Element`(s) `Acted Upon` and `Consulted` named in the `Specification` (the value of `bdqffdq:hasExpectedResponse`).
   - Identify any `Parameter`(s) and their default value(s) (from `bdqffdq:hasAuthoritiesDefaults` and/or `bdqffdq:hasArgument` / `bdqffdq:Argument`).

1 **Expose a stable callable API**
   - Implement the `Test` as a callable unit (function/method) whose inputs correspond to the `Information Element`(s) and any supported `Parameter`(s).
   - If your API exposes a `Parameter`:
     * it must accept the **string literal** default value exactly as it appears in the Test descriptor (see “Default Value Strings in Parameters (normative)” in this guide).
     * it may also support other **string literal** values of that `Parameter` to produce different behavior.

1 **Write a Unit Test**
  * Examine the decision rules in the `hasExpectedResponse` property of the `Specification` and write a unit test that covers each of the criteria in the expected response, including EXTERNAL_PREREQUISITES_NOT_MET, INTERNAL_PREREQUISITES_NOT_MET, COMPLIANT, and NOT_COMPLIANT. If the expected response includes multiple criteria for a given `Response.status`, write unit tests to cover each of those criteria.  Include tests for edge case values including empty values, values that are just inside and just outside of any specified ranges, and values that are not in the expected format. If the Test includes `Parameters`, write unit tests to cover the default value(s) and any non-default value(s) that your implementation supports.

1 **Implement the Test logic (decision rules) following the expected response criteria in order**
   * Follow the sequence of criteria in the `hasExpectedResponse` property of the `Specification`, returning the first matching `Response` for the first matched criterion.
   * Handle EXTERNAL_PREREQUISITES_NOT_MET as an exception raised from an invocation of an external resource, and return that response immediately when such an exception is raised.
   * **Evaluate internal prerequisites first**
     - Evaluate `bdq:Empty` and `bdq:NotEmpty` consistently (with utility functions).
     - Implement `bdq:Empty` consistently (see Section 2.2, “The Concept of `EMPTY` in the BDQ Standard (normative)”).
     - If the `Specification` states that an `Information Element` being `bdq:Empty` prevents evaluation, return:
       - `Response.status` = `INTERNAL_PREREQUISITES_NOT_MET`
       - `Response.result` omitted / null
       - `Response.comment` containing a `bdq:NotEmpty` explanation
   * **Handle external prerequisites and parameter support separately**
     * If a `Parameter` value is not supplied, substitute the default value.
     * If the `Test` depends on an external resource (e.g., a `bdq:sourceAuthority`) and that resource is unavailable at runtime, return:
       - `Response.status` = `EXTERNAL_PREREQUISITES_NOT_MET`
       - `Response.result` omitted / null
       - `Response.comment` containing a `bdq:NotEmpty` explanation
     * If an unsupported non-default `Parameter` value is supplied, implementations must not use `Response.status` = `EXTERNAL_PREREQUISITES_NOT_MET` to report “unsupported parameter value” (see Section 3.6, “Parameterized Tests: default behavior and unsupported values (normative)”).
  * **Run the core validation and return a conforming `Response`**
    * Apply the `Test`’s stated criterion (e.g., exact match, interpretation rules, range checks) exactly as described in the `Specification`, and avoid undocumented preprocessing.
    * When evaluation succeeds, return:
      - `Response.status` = `RUN_HAS_RESULT`
      - `Response.result` = `COMPLIANT` or `NOT_COMPLIANT`
      - `Response.comment` containing a `bdq:NotEmpty` explanation
    * If a non-default `Parameter` value was used, `Response.comment` should include the `Parameter` name and the non-default value (see Section 6.1.2, “Identifying non-default `Parameter` values in `Response.comment` (normative)”).

### 6.5.2 Checklist for Implementing an Amendment Test (non-normative)

1 Implement utility functions to evaluate `bdq:Empty` and bdq:NotEmpty consistently (see Section 2.2, “The Concept of `EMPTY` in the BDQ Standard (normative)”).

1 **Confirm the required inputs and intended outputs**
   - Identify the `Information Element`(s) `Acted Upon` and `Consulted` named in the `Specification` (the value of `bdqffdq:hasExpectedResponse`).
   - Identify any `Parameter`(s) and their default value(s) (from `bdqffdq:hasAuthoritiesDefaults` and/or `bdqffdq:hasArgument` / `bdqffdq:Argument`).
   - Identify which `Information Element`(s) may appear as keys in the `Response.result` payload when the result is an amendment proposal (some `Amendment` Tests propose changes to more than one `Information Element`).

1 **Expose a stable callable API**
   - Implement the `Test` as a callable unit (function/method) whose inputs correspond to the `Information Element`(s) and any supported `Parameter`(s).
   - If your API exposes a `Parameter`, 
     * it must accept the **string literal** default value exactly as it appears in the Test descriptor (see Section 2.3.2.4 “Default Value Strings in Parameters (normative)”).
     * it may also support other **string literal** values of that `Parameter` to produce different behavior.

1 **Write a Unit Test**
  * Examine the decision rules in the `hasExpectedResponse` property of the `Specification` and write a unit test that covers each of the criteria in the expected response, including EXTERNAL_PREREQUISITES_NOT_MET, INTERNAL_PREREQUISITES_NOT_MET, FILLED_IN, AMENDED, and NOT_AMENDED. If the expected response includes multiple criteria for a given `Response.status`, write unit tests to cover each of those criteria.  Include tests for edge case values including empty values, values that are just inside and just outside of any specified ranges, and values that are not in the expected format. If the Test includes `Parameters`, write unit tests to cover the default value(s) and any non-default value(s) that your implementation supports.

1 **Implement the Test logic (decision rules) following the expected response criteria in order**
   * **Evaluate internal prerequisites first**
     - Evaluate `bdq:Empty` and `bdq:NotEmpty` consistently (with utilty functions).
     - If the `Specification` states that one or more required `Information Element`(s) being `bdq:Empty` prevents generating a proposal, return:
       - `Response.status` = `INTERNAL_PREREQUISITES_NOT_MET`
       - `Response.result` omitted / null
       - `Response.comment` containing a `bdq:NotEmpty` explanation

   * **Handle external prerequisites and parameter support separately**
     - If a `Parameter` value is not supplied, substitute the default value.
     - If the `Test` depends on an external resource (e.g., a `bdq:sourceAuthority`) and that resource is unavailable at runtime, return:
       - `Response.status` = `EXTERNAL_PREREQUISITES_NOT_MET`
       - `Response.result` omitted / null
       - `Response.comment` containing a `bdq:NotEmpty` explanation
     - If an unsupported non-default `Parameter` value is supplied, implementations must not use `Response.status` = `EXTERNAL_PREREQUISITES_NOT_MET` to report “unsupported parameter value” (see Section 3.6 “Parameterized Tests: default behavior and unsupported values (normative)”).

   * **Generate a proposal (or decide no proposal is warranted)**
     - Apply the `Test`’s criterion exactly as described in the `Specification`, including any “interpreted as” rules (see Section 2.3.3 “The Concept of ‘interpreted as’ (normative)”).
     - Do not propose changes that are not explicitly allowed by the `Specification`. In particular, avoid “helpful” normalizations that would alter meaning or introduce false precision unless specified.
     - If a proposal is made, represent the proposed changes as structured data (typically a list/map of key:value pairs where keys are `Information Element` identifiers and values are proposed new values).

   * **Return a conforming `Response` for an `Amendment`**
     - When evaluation succeeds, use `Response.status` values appropriate to `Amendment` Tests:
       - `FILLED_IN` when proposing new value(s) for `Information Element`(s) that were `bdq:Empty`.
       - `AMENDED` when proposing changes to existing `bdq:NotEmpty` value(s).
       - `NOT_AMENDED` when prerequisites are met but no proposal is made.
     - For `FILLED_IN` and `AMENDED`:
       - `Response.result` MUST be present and MUST contain the structured proposal payload (e.g., JSON key:value pairs).
       - `Response.comment` MUST be `bdq:NotEmpty` and SHOULD explain how the proposal was derived (including any non-default `Parameter` values used).
     - For `NOT_AMENDED`:
       - `Response.result` must be omitted / null.
       - `Response.comment` must be `bdq:NotEmpty` and should explain why no proposal was made (e.g., ambiguous input, not interpretable, no unambiguous match in authority).

1 **Keep `Amendment` semantics clearly distinct from applying changes**
  - An `Amendment` `Response.result` is a proposal. Implementations should not automatically apply the proposed changes to authoritative data.
  - The application of a Response.result from an `Amendment` Test is a separate concern from the generation of that proposal, and external to the Test API. Implementations should keep these concerns separate.
  - Implementations may support pipelines that apply proposals downstream for Quality Assurance use cases, but must preserve the ability to retain the original (unamended) values and to report both pre- and post-amendment results (see Section 6.4.1 “Phases: Pre-Amendment, Amendment, Post-Amendment (normative)”).

## 6.6 Responsibilities of a Test Execution Framework (non-normative)

BDQ `Test` descriptions are intentionally independent of any particular software framework, data storage system, serialization, or workflow environment. This separation of concerns supports portability:

* The `Test` descriptor defines **what** must be evaluated (via the `Specification`, `Information Elements`, and any `Parameters`) and **what** must be reported (via `Response.status`, `Response.result`, and `Response.comment`).  The logic or decision rules of the `Test` are internal to the Test
* An execution framework defines **how** to obtain the required values from raw data, **how** to invoke the corresponding `Implementation`, and **how** to package results into `Data Quality Reports` or for other downstream processes.

### 6.6.1 Linking raw input terms, Tests, and outputs in a workflow (non-normative)

A `Test` execution framework (or “runner”) typically needs to accomplish the following steps between raw input data, a Test `Implementation`, and handling output from a Test:

1. **Pick a `Use Case` and its associated `Policies`**
   - Determine which `Use Case` is being addressed, and which `Policies` are relevant to that `Use Case`.
   - Identify which `Tests` are required by the relevant `Policies`.

1. **Choose the unit of evaluation**
   - Determine whether input is being treated as a `Single Record` (`bdqffdq:SingleRecord`) or a `Multi Record` (`bdqffdq:MultiRecord`) resource.
   - Iterate records (for `Single Record` execution) or assemble appropriate aggregates (for `Multi Record` execution).

1. **Determine the workflow for Test execution**
   - If the `Policies` for a `Use Case` include both `Validation` and `Amendment` Tests, determine the order of execution (e.g., run all `Validation` Tests first, then run `Amendment` Tests on the records that passed validation; or run each `Validation` Test followed immediately by its corresponding `Amendment` Test).
   - A workflow that may be expected, and is the responsibility of the execution framework, is to run:
     - All `Validation` tests, all `Issue` tests and all `Measure` tests in a pre-amendent phase.
     - Run all `Amendment` tests in an amendment phase.
     - Apply all proposed changes from the `Amendment` tests to a copy of the input data.
     - Apply all `Validation` tests, all `Issue` tests and all `Measure` tests in a post-amendment phase using the amended copy of the data as input.
     - Compare the results of `MultiRecord` `Measures` from the pre-and post-amendment phases (giving a measure of how much accepting the proposed changes from `Amendments` would improve the quality of the data for the `Use Case` at hand..
     - Produce a `Data Quality Report` that includes both pre- and post-amendment results, and that retains the original (unamended) values for reference. 

1. **Consider Aggregation of unique values for `Single Record` Tests**
   - For `SingleRecord` tests, it may be appropriate to aggregate distinct input values and run the same Test implementation once per distinct value, rather than once per record (e.g., for a `Validation` Test that checks if a particular value is found in an authority, it may be more efficient to run the Test once per distinct value rather than once per record).
   - Aggregation should normally be by distinct values of the set of `Information Elements` for each Test, and not by distinct values of a single `Information Elements`, to ensure that the correct `Response` is associated with the correct combination of input values.
   - If aggregation is used, ensure that the `Response` for each distinct value is correctly associated with all records that contain that value to pass down a processing pipeline or to return in the final `Data Quality Report`.

1. **Bind raw data to the `Test` API**
   - Map the framework’s internal representation of data (rows, objects, RDF graphs, etc.) onto the specific `Information Element`(s) required by the `Test`.
   - Ensure correct binding of `Acted Upon` values and `Consulted` values to the correct inputs of the `Implementation`.
   - Provide values for `Parameter`(s), or omit them and rely on default behavior where supported.

1. **Locate and invoke the correct Tests**
   - The `Policies` from the `Use Case` identify which `Tests` are required, but an execution framework must still determine how to locate the corresponding implementation for each Test.
   - Resolve which callable unit implements which Test (preferably by Term Name (UUID), or Versioned IRI).
   - Invoke the `Implementation` with the bound inputs in a way that is consistent and repeatable.

1. **Execute a Test and Capture results as a structured `Response`**
   - Ensure that every Test execution yields one Response containing:
     - `Response.status`
     - `Response.result` (present only when appropriate for the status and `Test Type`)
     - `Response.comment` (a human-readable `bdq:NotEmpty` explanation)
   - Ensure returned values use the controlled vocabulary strings defined by the BDQ standard (e.g., `RUN_HAS_RESULT`, `COMPLIANT`, `NOT_COMPLIANT`).
   - Exceptions raised from within a Test must be be captured and handled according to the expected response criteria in the `Specification` (e.g., returning `EXTERNAL_PREREQUISITES_NOT_MET` when an external resource is unavailable, with an appropriate comment).  An exception within a test should not be raised into the execution framework.

1. **Consider Handling of EXTERNAL_PREREQUISITES_NOT_MET**
   - If a `Test` implementation raises an exception or error due to an unavailable external resource, the test is expected to capture that and return a `Response` with `Response.status` = `EXTERNAL_PREREQUISITES_NOT_MET`, and a `Response.comment` containing a `bdq:NotEmpty` explanation.
   - A framework for Test execution may choose to simply pass these failure conditions on, or to handle such exceptions at a higher level (e.g., by skipping all Tests that depend on that resource for the remainder of a run, or by retrying after a delay), but must ultimately ensure that the appropriate `Response` is returned for each individual Test execution that encounters an unavailable external resource.

1. **If unique values were aggregated, deaggregate and associate results with all relevant records**
   - If the framework uses aggregation of distinct values for `Single Record` Tests, ensure that the `Response` for each distinct value is correctly associated with all records that contain that value to pass down a processing pipeline or to return in the final `Data Quality Report`.

1. **Serialize and report results**
   - Record or transmit results as part of a `Data Quality Report` (or as `bdqffdq:Assertion` instances in RDF), in any serialization that fits the implementation environment.
   - When non-default `Parameter`(s) are used, ensure the report can communicate which `Argument` value(s) were applied (for both human and machine consumers), consistent with the guidance in this standard.

## 7 Presentation of Results (normative)

The BDQ standard is agnostic about the form and appearance of `Data Quality Reports` (e.g., as aggregated results, on web pages for individual records, as spreadsheets of results with issues for quality control, etc.).

### 7.1 Data Quality Reports (normative)

#### 7.1.1 Identifying Tests (normative)

Reports SHOULD identify Tests to consumers of those reports using at least the Label (`rdfs:label`) for the Test class (e.g., "VALIDATION_COUNTRY_FOUND" for [VALIDATION_COUNTRY_FOUND](../../terms/bdqtest/index.md#VALIDATION_COUNTRY_FOUND)).

Reports MAY describe Tests to consumers of those reports using the Description (`rdfs:comment`) for the Test class (e.g., "Does the value of dwc:country occur in the bdq:sourceAuthority?" for [VALIDATION_COUNTRY_FOUND](../../terms/bdqtest/index.md#VALIDATION_COUNTRY_FOUND)).

#### 7.1.2 Information Elements Acted Upon and Consulted in Results (normative)

`Information Elements` may be `bdqffdq:ActedUpon` or `bdqffdq:Consulted` (the sub-types of `bdqffdq:InformationElement`). Presentations of data quality results MAY use `Information Element` sub-types to identify which specific values `Assertions` are being made about, and which values are being used to support those `Assertions`. `Information Elements` `Acted Upon` are those for which a `Validation` Test is asserting compliance/non-compliance, or for which an `Amendment` Test is proposing an improvement to the data. `Information Elements` `Consulted` are those which inform such decisions, but are not themselves the subject of the decision. For example, in the Test [AMENDMENT_EVENTDATE_FROM_VERBATIM](../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_VERBATIM), the `Information Element` `dwc:eventDate` is `Acted Upon`, while the `Information Element` `dwc:verbatimEventDate` is `Consulted`. Implementers may wish to clearly represent to consumers of `Data Quality Reports` (particularly `Data Quality Reports` in the form of spreadsheets), which terms are particular Tests are making `Assertions` about.

Data quality reports should be clear which input terms are subject to compliance tests and thus SHOULD NOT assert that `Information Elements` `Consulted` for a `Validation` are NOT_COMPLIANT with respect to that `Validation`.

##### 7.1.2.1 Information Elements Acted Upon and Consulted Example (non-normative)

The `Test` VALIDATION_COUNTRY_NOTEMPTY has two `Information Elements` in its specification: `dwc:country` is the `Information Element` `Acted Upon`, and `dwc:countryCode` is the `Information Element` `Consulted`.   

VALIDATION_COUNTRY_NOTEMPTY has the `expectedResponse`: COMPLIANT if dwc:country is bdq:NotEmpty or dwc:countryCode has a value of "XZ" and either dwc:country is bdq:Empty or has a value of "High seas"; otherwise NOT_COMPLIANT

Given the following record as input:

* dwc:country = ""
* dwc:countryCode = "US"

In this case, the `Information Element` `Acted Upon` is `dwc:country`, and the `Information Element` `Consulted` is `dwc:countryCode`. The Test would return NOT_COMPLIANT for this record, with a comment that dwc:country is empty, and that the value of dwc:countryCode does not have the value "XZ".  The Test would return NOT_COMPLIANT because of the value of dwc:country, not because of the value of dwc:countryCode. The value of dwc:countryCode is consulted in the Test, but is not itself the subject of a non-compliance assertion.  Therefore, when presenting the results of this Test, it would be important to make clear that the non-compliance is with respect to dwc:country, and not dwc:countryCode.

A hypothetical (partial) presentation of the results of this `Test` in a spreadsheet might color code the `Information Element` `Acted Upon` (dwc:country) in red to indicate that it is the subject of a non-compliance assertion, while the `Information Element` `Consulted` (dwc:countryCode) should not be similarly marked as it is not the subject of a non-compliance assertion, even though it was consulted in the `Test`.

![Example Spreadsheet presentation with just the `actedUpon` for a `Validation` highlighted.](validation_actedupon_cell_red.png "Example Spreadsheet presentation with just the `actedUpon` for a `Validation` highlighted, a spreadsheet with column headers dwc:country and dwc:countryCode and one row of data, the data cell under dwc:country is empty but has a background color of red, while the data cell under dwc:countryCode contains the value US and has no background color set.")

#### 7.1.3 Example (non-normative)

Below is an example, adapted from MCZbase (Kennedy et al. 2024), of a portion of a `Data Quality Report` for a single specimen using an implementation of BDQ Tests integrated into that collection management system.

This example shows the results of the Test Suite (the full set of BDQ Taxon Name-related Tests) that was run, with the Description (`rdfs:comment`) to identify the action taken by the Test to the collection management staff reading the report. The results (`Response.status` or `Response.result`) for the pre-amendment phase are given along with the `Response.comment` explaining why the Test returned the given results. The post-amendment phase `Responses` show what the results would be if all proposed `Amendments`, listed below the table, had been accepted. `Amendments` are not applied automatically. Users must explicitly change the data if they want to accept the proposals from the `Amendments`. A subset of the real results are shown here, so the percentages of COMPLIANT results does not agree with the subset of results in the table.

**QC Taxon Name for MCZ:Herp:R-1440**

Results of the Biodiversity Data Quality (BDQ) Taxon Name-related Tests.

**Tests run using (Mechanism)**: Kurator Scientific Name Validator - DwCSciNameDQ:v1.0.1.

**Compliant Results**: Pre-amendment 75%, Post-amendment: 94%

| Test Description | Pre-amendment Result | Comment | Post-Amendment Result | Comment |
|------------------|----------------------|---------|-----------------------|---------|
| Is there a value in dwc:taxonRank? | **COMPLIANT** | Some value provided for taxonRank. | **COMPLIANT** | Some value provided for taxonRank. |
| Is the combination of higher classification taxonomic terms consistent using GBIF? | **COMPLIANT** | Genus Chelydra found in GBIF_BACKBONE_TAXONOMY\|Matches to higher ranks found in GBIF_BACKBONE_TAXONOMY\|No more higher ranks found to compare | **COMPLIANT** | Genus Chelydra found in GBIF_BACKBONE_TAXONOMY\|Matches to higher ranks found in GBIF_BACKBONE_TAXONOMY\|No more higher ranks found to compare |
| Does the value of dwc:taxonRank occur in bdq:sourceAuthority? | **COMPLIANT** | Provided value for taxonRank \[species\] found in the GBIF taxon rank vocabulary. | **COMPLIANT** | Provided value for taxonRank \[species\] found in the GBIF taxon rank vocabulary. |
| Is there a value in dwc:taxonID? | **NOT_COMPLIANT** | No value provided for taxonID. | **COMPLIANT** | Some value provided for taxonID. |
| dwc:scientificName contains a value | **COMPLIANT** | Some value provided for scientificName. | **COMPLIANT** | Some value provided for scientificName. |
| dwc:family is known to GBIF | **COMPLIANT** | Exact match to provided Family found in GBIF Backbone Taxonomy at rank Family. | **COMPLIANT** | Exact match to provided Family found in GBIF Backbone Taxonomy at rank Family. |
| dwc:genus is known to GBIF | **COMPLIANT** | Exact match to provided genus found in GBIF Backbone Taxonomy as a genus. | **COMPLIANT** | Exact match to provided genus found in GBIF Backbone Taxonomy as a genus. |
| dwc:scientificName is known to GBIF | **COMPLIANT** | Exact Match found for \[Chelydra serpentina (Linnaeus, 1758)\] to \[https://www.gbif.org/species/2441905\] | **COMPLIANT** | Exact Match found for \[Chelydra serpentina (Linnaeus, 1758)\] to \[https://www.gbif.org/species/2441905\] |
| Can the taxon be unambiguously resolved from GBIF using the available taxon terms? | **NOT_COMPLIANT** | Provided taxon \[:Animalia:Chordata:Reptilia:Testudinata:Chelydridae:Chelydra:Chelydra serpentina (Linnaeus, 1758):(Linnaeus, 1758):Chelydra:\]\|No exact match found for provided taxon in GBIF_BACKBONE_TAXONOMY. | **COMPLIANT** | Provided taxon \[urn:lsid:marinespecies.org:taxname:1378193:Animalia:Chordata:Reptilia:Testudinata:Chelydridae:Chelydra:Chelydra serpentina (Linnaeus, 1758):(Linnaeus, 1758):Chelydra:\]\|Exact match to provided taxonID found in WORMS, matching the provided value of dwc:scientificName |
| Does the value of dwc:taxonID contain a complete identifier? | **INTERNAL_PREREQUISITES_NOT_MET** | No value provided for taxonId. | **COMPLIANT** | Provided taxonID recognized as an LSID. |

**Proposed Amendments**

-   lookup taxonID for taxon FILLED_IN
    > **{dwc:taxonID=urn:lsid:marinespecies.org:taxname:1378193}**
    > Provided taxon
    > \[:Animalia:Chordata:Reptilia:Testudinata:Chelydridae:Chelydra:Chelydra
    > serpentina (Linnaeus, 1758):(Linnaeus, 1758):Chelydra:\] \| 1
    > potential matches returned from authority. \| Match for provided
    > taxon in WORMS with exact match on authorship. \| Exact match to
    > provided taxon found in WORMS.

### 7.2 Annotations (normative)

The `bdqffdq:` OWL representation of the [Fitness for Use Framework Ontology](../../bdqffdq/index.md) and the framing of the [BDQ Tests as RDF](../../../dist/bdq.xml) using that ontology make Test results particularly amenable to being wrapped in `Annotations` following the [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) (Sanderson et al. 2017). Test responses MAY be represented as `Annotations`.

The responses from Tests could be structured as elements that can be wrapped in the body `Annotation` document along with metadata from the Framework to describe which Test is being reported upon, and metadata within the target of the `Annotation` to describe which `DataResource` is being annotated, and the state it was in at the time of annotation.

When Test `Responses` are being returned as `Annotations`, they SHOULD use the W3C Web Annotation Data Model for the `Annotations`, and SHOULD place Test `Responses` within the body of the `Annotation`. Such `Annotations` SHOULD include reference to the source Test by the versioned fully qualified name of the Test (e.g., bdqtest:47ff73ba-0028-4f79-9ce1-ee7008d66498-2023-09-18) and the Test Label (`rdfs:label`) (e.g., VALIDATION_DAY_STANDARD). Such annotations SHOULD also provide the `bdqffdq:Mechanism` that generated the Test response. 

When Test responses are persisted as `Annotations` in association with the annotated data, a means SHOULD be provided to mark `Annotations` as having been evaluated, and to carry the results of such evaluations. `Annotation` conversations (that is, `Annotations` with other annotations as their target) MAY provide such a means. Vocabularies related to bug/issue tracking MAY provide such a means.

#### 7.2.1 Example of Test Responses as Annotations (non-normative)

The following is an example of a Test response represented as an `Annotation` in TURTLE format following the W3C Web Annotation Data Model (Sanderson et al. 2017). The body of the `Annotation` contains the Test response, and the metadata about the Test and the mechanism that generated the response are included in the body of the `Annotation`. The target of the `Annotation` is a URI for a particular record in a dataset.

This example is written to be consistent with the following expectations:

* The `oa:body` of the `oa:Annotation` is the `Assertion`.
* The `oa:target` of the `oa:Annotation` is the IRI of the record being annotated.
* The `dcterms:created` value on the `oa:Annotation` provides the annotation date.
* The `oa:motivatedBy` value on the `oa:Annotation` provides the motivation for creating the annotation.
* The `Implementation` is related to the `Assertion` it generated using `bdqffdq:producesAssertion`, is related to the `Specification` it ran using `bdqffdq:usesSpecification`, and is related to the `Mechanism` that executed it using `bdqffdq:implementedBy`.
* The `bdqffdq:usesSpecification` property points to the specific instance of `bdqffdq:Specification` that the `Implementation` used for the Test execution.

In a complete dataset the `Specification` is linked (via a `Method` instance) to the corresponding Test in bdqtest, that is, we could look up that the Test is VALIDATION_DAY_STANDARD given the `Specification` IRI. 

```
@prefix bdq:     <https://rs.tdwg.org/bdq/terms/> .
@prefix bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/> .
@prefix bdqtest: <https://rs.tdwg.org/bdqtest/terms/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix oa:      <http://www.w3.org/ns/oa#> .
@prefix prov:    <http://www.w3.org/ns/prov#> .
@prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/bdq/assertion/1>
  a bdqffdq:ValidationAssertion ;
  bdqffdq:hasResponseStatus bdqffdq:RUN_HAS_RESULT ;
  bdqffdq:hasResponseResult bdqffdq:NOT_COMPLIANT ;
  bdqffdq:hasResponseComment "Provided value for day '32' is not an integer in the range 1 to 31."^^xsd:string ;
  bdqffdq:appliesTo <http://example.org/dataset/record/12345> .

<https://example.org/bdq/implementation/1>
  a bdqffdq:Implementation ;
  bdqffdq:producesAssertion <https://example.org/bdq/assertion/1> ;
  bdqffdq:implementedBy <https://example.org/bdq/mechanism/kurator-dwcsciNameDQ-v1.0.1> ;
  bdqffdq:usesSpecification bdqtest:47ff73ba-0028-4f79-9ce1-ee7008d66498-2025-03-06 .

<https://example.org/bdq/mechanism/kurator-dwcsciNameDQ-v1.0.1>
  a bdqffdq:Mechanism ,
    prov:SoftwareAgent ;
  rdfs:label "Kurator Scientific Name Validator - DwCSciNameDQ:v1.0.1"^^xsd:string .

<https://example.org/annotation/1>
  a oa:Annotation ;
  oa:body <https://example.org/bdq/assertion/1> ;
  oa:target <http://example.org/dataset/record/12345> ;
  dcterms:created "2015-01-28T12:00:00Z"^^xsd:dateTime ;
  oa:creator <https://example.org/bdq/mechanism/kurator-dwcsciNameDQ-v1.0.1> ;
  oa:motivatedBy oa:assessing .
```

See also (Framework Competency Question including an oa:annotation](../../supplementary/index.md#242-framework-competency-question-including-an-oaannotation-non-normative) and the [discussion](../../supplement/index.md#38-amendments-and-annotations-non-normative) in the [Supplementary Material](../../supplement/index.md). 

## 8 Conformance Testing Implementations (normative)

Implementers of the BDQ Tests SHOULD validate the behavior of the internals of their Test implementations with unit tests, and MUST validate that each Test implementation is capable of taking relevant input from a set of standard Test Conformance Testing Data, and returning the expected responses.

For synthetic Test Conformance Testing Data that could be conflated with actual data, see [Guide to Marking and Identifying Synthetic and Modified Data](../synthetic/index.md)

### 8.1 Introduction to Test Conformance Testing (non-normative)

A set of "Test Conformance Testing Data" accompanies the BDQ Test descriptors. These data are intended for implementers for conformance testing, that is to use to evaluate whether or not their Test implementations produce the expected `Response` values for a set of input cases for each Test. Each Test specification could be graphed as a flow chart with several paths, the Test Conformance Testing Data are intended to cover each node and each path within each Test specification with at least a single case. These data are, however, not exhaustive unit tests covering large numbers of edge cases, but rather a minimal set of Tests for conformance with expected behaviors.

The Test Conformance Testing Data are organized as two flat CSV files. Each row in each file is intended for the evaluation of a single behavior of a single Test, that is, each row represents a single test case. The file has columns identifying the Test, the input data, the expected `Response.status`, `Response.result`, an example `Response.comment`, `Parameter` values (if any), and a set of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021). Most of the terms for a given Test are `bdq:Empty`.

The Test Conformance Testing Data records are all fragmentary [Simple Darwin Core](https://dwc.tdwg.org/simple/) (Wieczorek et al. 2012) dwc:Occurrence records. Each row contains values for only those Darwin Core terms that are relevant input to the particular cate and consists of a mixture of real and artificial data. The conformance testing data consist of over 1100 records, with an average of about 10 cases for each Test (designed to exercise all of the decision pathways in the specification of the Test (that is, all paths within each Expected Response)). The set of rows for a given Test are intended to be sufficient to validate that an implementation of that particular Test performs as expected against the specification.

#### 8.1.1 DataID as a conformance testing data record identifier (normative)

Test Conformance Testing Data rows SHOULD be uniquely identified within the conformance testing dataset with a dataID.

Additional Test records can be readily generated or adapted from real data using the following template based on the specifications below. In consideration of the community, the `dataID` values MUST uniquely identify a conformance test case for each additional Test data record and the resulting data SHOULD be added to the appropriate [TG2_test_validation_data.csv](./TG2_test_validation_data.csv) or [TG2_test_validation_data_nonprintingchars.csv](TG2_test_validation_data_nonprintingchars.csv) file. 
Frameworks that validate Test implementations against the Test Conformance Testing Data SHOULD report failure cases including the `dataID` of the conformance testing data for rows that did not validate.

### 8.2 Structure of the Test Conformance Testing Data (non-normative)

The Test Conformance Testing Data are intended as input into a testing system that can evaluate the implementations of Tests, evaluating each Test independently. Each Test Conformance Testing Data record contains only the values of the `Information Elements` ([Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021)) for a single Test as input. A conformance testing framework is expected to present those `Information Elements` as input to a Test implementation and assesses whether the `Response` from the Test implementation for that input conforms to the expected `Response` values for that row in the Test Conformance Testing Data.

The Test Conformance Testing Data could be processed as input for unit tests using some unit testing framework for Test implementations, or it could be used as the basis for presenting synthetic records to a larger Test execution system. The Test Conformance Testing Data are designed to be used at a level where individual Tests are being assessed.  The structure of the conformance testing data sits at a middle level of abstraction above the method signature specificity needed in unit tests and below the level of full system testing with complete Darwin Core records as inputs and rich `Data Quality Reports` as output.  That is, the structure of the Test Conformance Testing Data is generic, not specific to a particular Test, but still at a level that is examining individual Test implementations.

The chosen level of abstraction for the Test Conformance Testing Data avoids forcing particular formats on `Data Quality Reports` as a whole, as the responses from individual Tests are validated, not `Data Quality Reports`.

The header for the data in the Test Conformance Testing Data files includes a column for each
`Information Element` and each `Parameter` among all those used in the BDQ standard. Following are definitions for a subset of all columns in the Test Conformance Testing Data files:

| Column Name | Description |
| ------ | ---------- |
| Last Updated | The date on which this conformance test record was last updated. |
| GitHub Issue | The URL of the GitHub issue number where rationale management of the Test under conformance testing is maintained. |
| GitHubIssueNo | The last section of the GitHub Issue URL - a number, e.g., 20 can be found at https://github.com/tdwg/bdq/issues/20. |
| GUID | The machine readable identifier for the Test being evaluated (the Term Name (rdf:value) for the Test), e.g., 69b2efdc-6269-45a4-aecb-4cb99c2ae134. |
| Test Type | The type of the Test (i.e., `Validation`, `Issue`, `Amendment` or `Measure`. |
| Label | The second two components of the full English Test label, for example 'COUNTRYCODE_STANDARD' (`concat(upper(Test Type),"\_",Label)` to get the Test rdfs:label.) |
| Data Dimension | Does the Test apply to data that is essentially [NAME](../../../index.md#6-glossary-non-normative), [SPACE](../../../index.md#6-glossary-non-normative), [TIME](../../../index.md#6-glossary-non-normative) or [OTHER](../../../index.md#6-glossary-non-normative)? |
| dataID | A local to the Test Conformance Testing Data unique integer to identify each Test Conformance Testing Data record. | 
| LineForTest | An local identifier for Test records within one Test. This is present for maintaining the sort order within a Test, and with two special cases: "88" when Input.data contains a NULL character and "99" when Input.data contains non-printing characters (both managed in a separate file). | 
| Input.data | Data for the Information Elements that are required by the Specification for unambiguous running of the Test, (e.g., for [VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT](../../terms/bdqtest/index.md#VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT), dwc:country="México", dwc:countryCode="MX"). |
| Output.data | For Amendments only and when Response.status="AMENDED", suggested changes to the Input.data to improve quality, in the same format as Input.data. |
| Response.status | The status on applying the Test to the data record. For VALIDATIONS, one of the terms `EXTERNAL_PREREQUISITES_NOT_MET`, `INTERNAL_PREREQUISITES_NOT_MET` or `RUN_HAS_RESULT`. For AMENDMENTS, one of the terms `EXTERNAL_PREREQUISITES_NOT_MET`, `INTERNAL_PREREQUISITES_NOT_MET`, `FILLED_IN`, `AMENDED` or `NOT_AMENDED`. For ISSUE, one of the terms `INTERNAL_PREREQUISITES_NOT_MET` or `RUN_HAS_RESULT`. For MEASURES, either `RUN_HAS_RESULT` or `INTERNAL_PREREQUISITES_NOT_MET`. |
| Response.result | The result of running the Test on the data record. For VALIDATIONS and AMENDMENTS, NULL where the Response.status is either `EXTERNAL_PREREQUISITES_NOT_MET`, `INTERNAL_PREREQUISITES_NOT_MET`. For VALIDATIONS, either `COMPLIANT` or `NOT_COMPLIANT` where Response.status is `RUN_HAS_RESULT`. For AMENDMENTS where Response.status is either `FILLED_IN` or `AMENDED`, the Response.result is a JSON structure containing a key:value list of Darwin Core terms and values for changes proposed by the AMENDMENT. For MEASURES, a resulting value or `NOT_REPORTED`. |
| Response.comment | A human-readable example statement identifying the reason for the Test result given the input data. Implementations are not expected to produce this exact value. |
| IssuesWithThisRow | A working column for recording issues while developing conformance testing data. Used only for management while developing Test Conformance Testing Data. |
| bdq:annotation | A placeholder for an annotation when Testing for their presence (this value does not imply the existence of the term annotation in the bdq: namespace). |
| bdq:sourceAuthority | Input parameter for some Parameterized Tests. |

**NOTE:** We have implemented examples of EXTERNAL_PREREQUISITES_NOT_MET using the `Input.Data` structure containing `bdq:sourceAuthority`=`https://invalid/invalidservice`, for example:

```
bdq:taxonomyIsMarine="https://invalid/invalidservice", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:scientificName=""
```

### 8.3 Examples of the Data for Conformance Testing (non-normative)

The conformance testing files contain one column (e.g., `dwc:countryCode`) for each of [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that are referenced as an `Information Element` somewhere in the BDQ standard, but only terms relevant to the particular case for the row are populated, therefore the conformance testing files are sparse. They contain fragments of [Simple Darwin Core](https://dwc.tdwg.org/simple/) records. 

For example, given the header line for the Test Conformance Testing Data files:

"LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Response.status","Response.result","Response.comment","IssuesWithThisRow","bdq:annotation","bdq:sourceAuthority","dc:type","dcterms:license","dwc:acceptedNameUsageID","dwc:basisOfRecord","dwc:class","dwc:continent","dwc:coordinateUncertaintyInMeters","dwc:country","dwc:countryCode","dwc:county","dwc:dataGeneralizations","dwc:dateIdentified","dwc:day","dwc:decimalLatitude","dwc:decimalLongitude","dwc:endDayOfYear","dwc:establishmentMeans","dwc:eventDate","dwc:family","dwc:genus","dwc:geodeticDatum","dwc:higherClassification","dwc:higherGeography","dwc:higherGeographyID","dwc:infraspecificEpithet","dwc:island","dwc:islandGroup","dwc:kingdom","dwc:locality","dwc:locationID","dwc:maximumDepthInMeters","dwc:maximumElevationInMeters","dwc:minimumDepthInMeters","dwc:minimumElevationInMeters","dwc:month","dwc:municipality","dwc:occurrenceID","dwc:occurrenceStatus","dwc:order","dwc:originalNameUsageID","dwc:parentNameUsageID","dwc:phylum","dwc:scientificName","dwc:scientificNameAuthorship","dwc:scientificNameID","dwc:specificEpithet","dwc:startDayOfYear","dwc:stateProvince","dwc:subgenus","dwc:taxon","dwc:taxonConceptID","dwc:taxonID","dwc:taxonRank","dwc:verbatimCoordinateSystem","dwc:verbatimCoordinates","dwc:verbatimDepth","dwc:verbatimElevation","dwc:verbatimEventDate","dwc:verbatimLatitude","dwc:verbatimLocality","dwc:verbatimLongitude","dwc:verbatimSRS","dwc:vernacularName","dwc:waterBody","dwc:year","dwc:subfamily","dwc:superfamily","dwc:tribe","dwc:subtribe","dwc:genericName","dwc:infragenericEpithet","dwc:cultivarEpithet","dwc:individualCount","dwc:organismQuantity","dwc:footprintWKT","dwc:coordinatePrecision","dwc:namePublishedInYear","dwc:sex","dwc:typeStatus","dwc:pathway","dwc:degreeOfEstablishment","bdq:taxonIsMarine","bdq:geospatialLand","bdq:assumptionOnUnknownBiome","bdq:latestValidDate","bdq:earliestValidDate",

a conformance test case evaluating `bdq:Empty`, where no `dwc:` term columns contain a value (dataID=1) would look like this:

"2","1","1","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","INTERNAL_PREREQUISITES_NOT_MET","","dwc:countryCode is EMPTY","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A `Validation` Test case for a `Validation` where the input data result in a `Response.result` of NOT_COMPLIANT (dataID=7) would look like this:

"8","7","7","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","NOT_COMPLIANT","dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value ","","","","","","","","","","","","Austria","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A `Validation` Test case for a `Validation` where the input data result in a `Response.result` of COMPLIANT (dataID=8) would look like this:

"9","8","8","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","COMPLIANT","dwc countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value","","","","","","","","","","","","US","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

### 8.4 Where to Get the Test Conformance Testing Data (non-normative)

The conformance testing data are in two files, one containing normal data values, the other containing test cases containing non-printing characters.

1. [TG2_test_validation_data.csv](./TG2_test_validation_data.csv) - file containing data values that might be expected to be encountered in real-world data.
2. [TG2_test_validation_data_nonprintingchars.csv](./TG2_test_validation_data_nonprintingchars.csv) - file containing non-printing characters for testing implementation of `bdq:Empty`.

Both of these files have the same set of columns, but the latter has rows that contain input values for selected [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that are either the `0x00` null character (e.g., `dwc:scientificName="0x00"`), or a pair of ASCII control characters (`0x0E` and `0x0F`, e.g., `dwc:day="0x0E0x0F`). This file is intended to validate that Test implementations are consistently evaluating inputs as consistent with the definition of `bdq:Empty`.

The non-printing characters file MUST only be edited with a tool that will maintain the non-printing characters.

Both files have a header line identifying the columns as described in [Structure of the Test Conformance Testing Data (non-normative)](#82-structure-of-the-test-conformance-testing-data-non-normative).

The `Response` when executed against a row as input is expected to contain "Response.status", "Response.result" and "Response.comment". An implementation is expected to produce the exact `Response.status`, the exact `Response.result` (ignoring order of any key-value pairs for an `Amendment` `Response`), while `Response.comment` is an example of what a comment in English might look like.

Parameter values are specified in a `bdq:sourceAuthority` column, when more than one `sourceAuthority` is involved, then these are given separate names.

Dublin Core and Darwin Core term input columns are specified with the appropriate namespace abbreviation prepended (e.g., `dc:type`, `dcterms:license`, `dwc:acceptedNameUsageID`).

### 8.5 Implementation and the Conformance Testing Data (normative)

To be compliant with the BDQ standard, an implementation of a Test MUST fulfill all of the REQUIRED elements of this section.

Implementations MUST produce structured `Response` values with a `Response.status`, `Response.result` and `Response.comment`.

Implementations SHOULD provide support for each `Parameter` value specified in the example data. 

Human readable `Data Quality Reports` for Quality Control MAY take any appropriate form, they MAY aggregate `Response` values and comments, they MAY present results organized by Test, or by data record, or by frequency of problem, or any other form suitable for presentation. `Data Quality Reports` for Quality Control SHOULD allow users to access individual `Response.status`, `Response.result`, and `Response.comment` results.

`Response.comment` values SHOULD be internationalized as appropriate for the the consumers of `Data Quality Reports`.

`Response.status` and `Response.result` constants SHOULD be given internationalized labels as appropriate for the the consumers of `Data Quality Reports`.

For each Test in an implementation, that Test MUST produce the same results as are specified in a row of the conformance testing data for that Test, except when a `bdq:sourceAuthority` parameter specifies a source other than the default `sourceAuthority` specified for that Test.

### 8.6 Existing Software tools (non-normative) 

#### 8.6.1 Tools for Validating Test Implementations with the Conformance Testing Data (non-normative) 

The `bdqtestrunner` tool (Morris, 2024), written in Java, was written to validate the implementations of the BDQ Tests in various FilteredPush data quality libraries against the Test Conformance Testing Data. This tool uses Java annotations on methods that implement Tests in order to match inputs from the conformance testing data to methods under Test that implement individual Tests. The tool could be reused to validate implementations in other Java classes that follow the same use of `ffdq-api` (Lowery and Morris 2024).

Java annotations can be used to match Test implementation methods to Tests and `Information Elements` to method parameters. The [ffdq-api](https://github.com/kurator-org/ffdq-api) (Lowery and Morris 2024) provides a set of annotations intended to enable code using Java reflection to detect methods that implement particular Tests, and then again through Java reflection, bind Darwin Core terms and other `Information Elements` in input data onto appropriate method parameters.

#### 8.6.2 Tools to assist with Implementations and RDF presentation (non-normative) 

The Test implementations listed below use Java Annotations (as shown in the example in [2.3.2.5 Example Interpretation of a Parameter String Default Value (non-normative)](#2325-example-interpretation-of-a-parameter-string-default-value-non-normative) to carry metadata to identify Tests and to allow binding of Darwin Core terms to Java method parameters. The Java Annotations are themselves related to Fitness For Use Framework concepts, are available in a library ffdq-api (Lowery and Morris 2024), and are intended to be used with rdfbeans to serialize Java result objects produced by Test implementations into `bdqffdq:Assertion` objects in RDF. In addition, a Java library, `kurator-ffdq` (Lowery et al., 2025) is available for working with Test descriptions as RDF, being an implementation of the Framework Ontology in Java. The `kurator-ffdq` library also includes classes for generating stub methods for each Test in either Java or Python.

- [ffdq-api](https://github.com/kurator-org/ffdq-api) (Lowery and Morris 2024) Java annotations for decorating Test implementations.
- [kurator-ffdq](https://github.com/kurator-org/kurator-ffdq) (Lowery et al. 2025) Java class representation of `bdqffdq:` classes, able to produce stub code for Test implementations in Java or Python. `kurator-ffdq` is also able (code is rusty as of v3.0.0) to run Java Test implementations annotated with `ffdq-api` annotations and produce `Data Quality Report` spreadsheets.

For more information on stub method generation used by the Kurator/FilteredPush libraries, see the following README files:

- event_date_qc/generation [README](https://github.com/FilteredPush/event_date_qc/blob/master/generation/README.md)
- sci_name_qc/generation [README](https://github.com/FilteredPush/sci_name_qc/blob/master/generation/README.md)
- geo_ref_qc/generation [README](https://github.com/FilteredPush/geo_ref_qc/blob/master/generation/README.md)
- rec_occur_qc/generation [README](https://github.com/FilteredPush/rec_occur_qc/blob/master/generation/README.md)
- and kurator-ffdq [README](https://github.com/kurator-org/kurator-ffdq/blob/master/README.md)

These libraries are available in Maven Central, source code is archived in Zenodo.

## 9 Existing Test Implementations (non-normative) 

A set of open source Java libraries provide classes that implement each of the `bdqffdq:SingleRecord` Tests that operate directly on data. These libraries are not part of the BDQ standard, but have been implemented as part of the process of writing the standard.

- [event_date_qc](https://github.com/filteredpush/event_date_qc) (Morris & Lowery 2025) Tests related to spatial terms.
- [sci_name_qc](https://github.com/filteredpush/sci_name_qc) (Morris & Dou 2025) Tests related to taxonomy and identification terms.
- [geo_ref_qc](https://github.com/filteredpush/geo_ref_qc) (Morris, Lowery & Wieczorek 2025b) Tests related to spatial terms.
- [rec_occur_qc](https://github.com/FilteredPush/rec_occur_qc) (Morris 2025) Tests related to metadata terms.

These libraries are available in Maven Central.
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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Implementer's Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
