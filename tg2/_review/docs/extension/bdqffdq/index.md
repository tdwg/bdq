<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness For Use Framework Ontology Vocabulary Extension

**Title**<br>
Fitness For Use Framework Ontology Vocabulary Extension

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqffdq

**This version**<br>
<http://rs.tdwg.org/bdqffdq/extension/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdqffdq/extension/>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
This document is a reference for the BDQ standard, documenting additional axioms that extend the basic vocabulary of the Fitness For Use Framework Ontology.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/extension/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1. Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
    - [1.3.1 Term List Distributions (non-normative)](#131-term-list-distributions-non-normative)
  - [1.4 Status of the content of this document (normative)](#14-status-of-the-content-of-this-document-normative)
  - [1.5 RFC 2119 key words (normative)](#15-rfc-2119-key-words-normative)
  - [1.6 Namespace abbreviations (non-normative)](#16-namespace-abbreviations-non-normative)
  - [1.7 Key to Vocabulary Terms (normative)](#17-key-to-vocabulary-terms-normative)

[2 Use of Terms (normative)](#2-use-of-terms-normative)

[3 Axiom Index (non-normative)](#3-axiom-index-non-normative)

[4 Vocabulary Extension (normative)](#4-vocabulary-extension-normative)
  - [4.1 Range Axioms (normative)](#41-range-axioms-normative)
    - [hasAuthoritiesDefaults](#hasauthoritiesdefaults)
    - [hasDateLastUpdated](#hasdatelastupdated)
    - [hasExpectedResponse](#hasexpectedresponse)
    - [hasResponseComment](#hasresponsecomment)
    - [forAmendment](#foramendment)
    - [forIssue](#forissue)
    - [forMeasure](#formeasure)
    - [forValidation](#forvalidation)
    - [hasArgument](#hasargument)
    - [hasCriterion](#hascriterion)
    - [hasDataQualityDimension](#hasdataqualitydimension)
    - [hasEnhancement](#hasenhancement)
    - [hasInformationElement](#hasinformationelement)
    - [hasParameter](#hasparameter)
    - [hasSpecification](#hasspecification)
    - [hasUseCase](#hasusecase)
    - [implementedBy](#implementedby)
    - [improvedBy](#improvedby)
    - [targetedIssue](#targetedissue)
    - [targetedMeasure](#targetedmeasure)
    - [targetedValidation](#targetedvalidation)
    - [usesSpecification](#usesspecification)
  - [4.2 Different From Axioms (normative)](#42-different-from-axioms-normative)
    - [COMPLETE](#complete)
    - [COMPLIANT](#compliant)
    - [IS_ISSUE](#is_issue)
    - [NOT_ISSUE](#not_issue)
    - [AMENDED](#amended)
    - [EXTERNAL_PREREQUISITES_NOT_MET](#external_prerequisites_not_met)
    - [FILLED_IN](#filled_in)

## 1. Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to define the official vocabulary extension for the `bdqffdq:` ontology. It provides additional axioms, such as range constraints and logical distinctions, that refine and extend the semantics of the core vocabulary terms in the BDQ Fitness For Use Framework.

These axioms enable more precise reasoning, validation, and integration with OWL tools. They are intended to complement the human-readable term list provided in the main ontology documentation without altering the open and minimally constrained design of the core Fitness For Use Framework.  Additional normative expectations, which are not formally represented in the ontology or included here, are listed in [Section 2 of the bdqffdq: landing page](../../bdqffdq/index.md#2-use-of-terms-normative) to clarify the intended use of these terms in practice.

This extension follows the TDWG Standards Documentation Specification and maintains a clear separation between core term definitions and ontology logic.

### 1.2 Audience (non-normative)

This document is intended for ontology engineers, semantic modelers, and developers who are applying the BDQ Fitness For Use Framework in OWL environments. It will be especially useful for:

- Implementers using OWL reasoners or validators to enforce or explore logical structures
- Developers of semantic tooling and metadata pipelines based on the BDQ Standard
- Standards developers needing a detailed view of the formal semantics behind Fitness For Use Framework concepts.

This document assumes familiarity with OWL constructs, reasoning profiles, and RDF/OWL modeling practices.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

Information about the bdqffdq: ontology, its usage, and its extensions can be found in the following subset of Biodiversity Data Quality (BDQ) resources:

- [**Fitness For Use Framework Ontology Guide**](../../guide/bdqffdq/index.md) - Provides a visual and narrative introduction to the concepts and application of the ontology.
- [**Fitness For Use Framework Ontology List of Terms**](../../list/bdqffdq/index.md) - The term list document, which enumerates and describes the vocabulary terms.
- [**Fitness For Use Framework Ontology**](../../bdqffdq/index.md) - Provides normative guidance on the use of the vocabulary.
- **Fitness For Use Framework Ontology Vocabulary Extension** - Defines additional axioms extending the core vocabulary. This document.
- [**Biodiversity Data Quality Fitness For Use Framework (Ontology)**](../../../vocabulary/bdqffdq.owl) - The ontology, which provides the formal RDF/OWL representation of the vocabulary.

#### 1.3.1 Term List Distributions (non-normative)

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdqffdq/extension/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/extension/bdqffdq/index.md | This file | 
| OWL Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.4 Status of the content of this document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Section [1.7 Key to Vocabulary Terms (normative)](#17-key-to-vocabulary-terms-normative) identifies which values in Section 4 are normative and which are non-normative.

### 1.5 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.6 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |

### 1.7 Key to Vocabulary Terms (normative)

The terminology used to describe the terms in this vocabulary follows the [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/) (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Name (rdf:value) | normative | Idiomatic property used for structured values. | [https://rs.tdwg.org/ bdqffdq/terms/ COMPLETE](https://rs.tdwg.org/bdqffdq/terms/COMPLETE) |
| Type (rdf:type) | normative | The subject is an instance of a class. | [https://rs.tdwg.org/ bdqffdq/terms/ ResponseResult](https://rs.tdwg.org/bdqffdq/terms/ResponseResult) |
| Range (rdfs:range) | normative | A range of the subject property. In present context: shown as either a simple range in the form of a class, or as an owl:restriction. | [ owl:someValuesFrom bdqffdq:forValidation ] |
| DifferentFrom (owl:differentFrom) | normative | The property that determines that two given individuals are different. | [https://rs.tdwg.org/ bdqffdq/terms/ NOT_COMPLETE](https://rs.tdwg.org/bdqffdq/terms/NOT_COMPLETE) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | COMPLETE |


## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqffdq:` namespace MUST use the Term IRI (e.g., `http://rs.tdwg.org/bdq/bdqffdq/hasExpectedResponse`) or Term Qualified name (e.g., `bdqffdq:hasExpectedResponse`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `hasExpectedResponse`) MAY be used. In a purely human context a label (e.g., `Expected Response`) MAY be used.

## 3 Axiom Index (non-normative)

- [Range Axioms (normative)](#41-range-axioms-normative)
- [Different From Axioms (normative)](#42-different-from-axioms-normative)

## 4 Vocabulary Extension (normative)

### 4.1 Range Axioms (normative)
#### hasAuthoritiesDefaults

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasAuthoritiesDefaults |
| Type | owl:DatatypeProperty |
| Range | xsd:string |


#### hasDateLastUpdated

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasDateLastUpdated |
| Type | owl:DatatypeProperty |
| Range | xsd:date |


#### hasExpectedResponse

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasExpectedResponse |
| Type | owl:DatatypeProperty |
| Range | xsd:string |


#### hasResponseComment

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasResponseComment |
| Type | owl:DatatypeProperty |
| Range | xsd:string |


#### forAmendment

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:forAmendment |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:forAmendment ] |


#### forIssue

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:forIssue |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:forIssue ] |


#### forMeasure

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:forMeasure |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:forMeasure ] |


#### forValidation

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:forValidation |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:forValidation ] |


#### hasArgument

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasArgument |
| Type | owl:ObjectProperty |
| Range | bdqffdq:Argument |


#### hasCriterion

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasCriterion |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:hasCriterion ] |


#### hasDataQualityDimension

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasDataQualityDimension |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:hasDataQualityDimension ] |


#### hasEnhancement

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasEnhancement |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:hasEnhancement ] |


#### hasInformationElement

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasInformationElement |
| Type | owl:ObjectProperty |
| Range | bdqffdq:InformationElement |


#### hasParameter

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasParameter |
| Type | owl:ObjectProperty |
| Range | bdqffdq:Parameter |


#### hasSpecification

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasSpecification |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:hasSpecification ] |


#### hasUseCase

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasUseCase |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:hasUseCase ] |


#### implementedBy

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:implementedBy |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:implementedBy ] |


#### improvedBy

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:improvedBy |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:improvedBy ] |


#### targetedIssue

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:targetedIssue |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:targetedIssue ] |


#### targetedMeasure

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:targetedMeasure |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:targetedMeasure ] |


#### targetedValidation

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:targetedValidation |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:targetedValidation ] |


#### usesSpecification

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:usesSpecification |
| Type | owl:ObjectProperty |
| Range | [ owl:someValuesFrom bdqffdq:usesSpecification ] |


### 4.2 Different From Axioms (normative)
#### COMPLETE

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:COMPLETE |
| Type | bdqffdq:ResponseResult |
| Different From | bdqffdq:NOT_COMPLETE |


#### COMPLIANT

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:COMPLIANT |
| Type | bdqffdq:ResponseResult |
| Different From | bdqffdq:NOT_COMPLIANT |


#### IS_ISSUE

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:IS_ISSUE |
| Type | bdqffdq:ResponseResult |
| Different From | bdqffdq:NOT_ISSUE, bdqffdq:POTENTIAL_ISSUE |


#### NOT_ISSUE

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:NOT_ISSUE |
| Type | bdqffdq:ResponseResult |
| Different From | bdqffdq:POTENTIAL_ISSUE |


#### AMENDED

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:AMENDED |
| Type | bdqffdq:ResponseStatus |
| Different From | bdqffdq:NOT_AMENDED |


#### EXTERNAL_PREREQUISITES_NOT_MET

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET |
| Type | bdqffdq:ResponseStatus |
| Different From | bdqffdq:INTERNAL_PREREQUISITES_NOT_MET |


#### FILLED_IN

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:FILLED_IN |
| Type | bdqffdq:ResponseStatus |
| Different From | bdqffdq:NOT_AMENDED |


## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../../index.md#5-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/extension/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
