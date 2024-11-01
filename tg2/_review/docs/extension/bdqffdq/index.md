<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness For Use Framework Ontology Vocabulary Extension

Title
: Fitness For Use Framework Ontology Vocabulary Extension

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Preferred namespace abbreviation
: bdqffdq

This version
: <http://rs.tdwg.org/bdqffdq/extension/2024-09-10>

Latest version
: <http://rs.tdwg.org/bdqffdq/extension/>

{previous_version_slot}

Abstract
: This document is a reference for the (Draft) BDQ Core Standard, documenting additional axioms that extend the basic vocabulary of the Fittness For Use Framework Ontology.

Authors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/extension/2024-09-10>

Draft Standard for Submission

### Table of Contents ###

- [1 Introduction](#1-introduction)
- [1.1 Purpose](#11-purpose)
- [1.2 Audience](#12-audience)
- [1.3 Documents about the bdqffdq: ontology](#13-documents-about-the-bdqffdq-ontology)
- [1.3.1 Term List Distributions](#131-term-list-distributions)
- [1.4 Status of the content of this document](#14-status-of-the-content-of-this-document)
- [1.5 RFC 2119 key words](#15-rfc-2119-key-words)
- [1.6 Namespace abbreviations](#16-namespace-abbreviations)
- [1.7 Key to Vocabulary Terms](#17-key-to-vocabulary-terms)
- [2 Use of Terms (normative)](#2-use-of-terms-normative)
- [3 Axiom Index (non-normative)](#3-axiom-index-non-normative)
- [4 Vocabulary Extension](#4-vocabulary-extension)
- [4.1 Range Axioms](#41-range-axioms)
- [4.2 Different From Axioms](#42-different-from-axioms)


## 1 Introduction

This document includes terms that extend the basic bdqffdq vocabulary and are integral to bdqffdq as an ontology.  

The bdqffdq framework is represented as an owl ontology.  The basic terms for that framework are in the
[basic bdqffdq vocabulary](../../list/bdqffdq/index.md).  The TDWG Standards Documentation Specification requires
that the human readable documentation for ontologies be presented as a term list with additional axioms included
in a vocabulary extension.  This file documents the additional axioms in isolation.  

The bdqffdq ontology includes few restrictions, this is by design.  Domain and range restrictions do not limit
what is in the domain or range of a property, but add assertions about the types of objects that are the subjects
or objects of predicates bearing the restrictions.  Some types of restrictions limit which owl profiles are
available to tools that reason on the ontology and on data stores that include the ontology.  See the landing page 
and the bdqffdq: guide for expected uses of the properties that are not provided by these axioms.  

### 1.1 Purpose 

This document provides the required vocabulary extension listing axioms that extend the vocabulary terms in the bdqffdq: term list document.

### 1.2 Audience

This document is for those needing a technical understanding of the bdqffdq Framework. 

### 1.3 Documents about the bdqffdq: ontology

The bdqffdq: vocabulary is an ontology, documentation for it can be found in: 

- A [landing page](../../bdqffdq/index.md) with normative guidance on the use of this ontology.
- The [term list](../../list/bdqffdq/index.md) document listing just the vocabulary terms in the ontology.
- This page, additional axioms that extend the vocabulary terms.
- The bdqffdq framework ontology is best technically understood as its [Owl Ontology Distribution](../../../vocabulary/bdqffdq.owl) 

An illustrated guide to the use of the bdqffdq ontology is provided in the [Guide to the bdqffdq: framework](../../guide/bdqffdq/index.md) 

The [supplement](../../supplement/index.md) includes competency questions providing rationalle for 
the use of framework in the form of an ontology with additional axioms as a vocabulary for 
describing the bdqcore: tests.

### 1.3.1 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdqffdq/extension/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/extension/bdqffdq/index.md | This file | 
| Owl Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.4 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.7 Key to Vocabulary Terms](#17-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.6 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bdqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.7 Key to Vocabulary Terms

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Name (rdf:value) | normative | Idiomatic property used for structured values. | [https://rs.tdwg.org/ bdqffdq/terms/ COMPLETE](https://rs.tdwg.org/bdqffdq/terms/COMPLETE) |
| Type (rdf:type) | normative | The subject is an instance of a class. | [https://rs.tdwg.org/ bdqffdq/terms/ ResponseResult](https://rs.tdwg.org/bdqffdq/terms/ResponseResult) |
| Range (rdfs:range) | normative | A range of the subject property. In present context: shown as either a simple range in the form of a class, or as an owl:restriction in the form [ owl:someValuesFrom bdqffdq:targetedMeasure ]. | n290555c196304d61aa78fa4df4a806dcb1 |
| DifferentFrom (owl:differentFrom) | normative | The property that determines that two given individuals are different. | [https://rs.tdwg.org/ bdqffdq/terms/ NOT_COMPLETE](https://rs.tdwg.org/bdqffdq/terms/NOT_COMPLETE) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | COMPLETE |


## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values from the `bdq:` namespace, except for bdq:empty and bdq:notEmpty, where controlled value strings MUST be used.

## 3 Axiom Index (non-normative)

- [Range Axioms](#41-Range Axioms)
- [Different From Axioms](#41-Different From Axioms)

## 4 Vocabulary Extension

### 4.1 Range Axioms
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


### 4.2 Different From Axioms
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
| Different From | bdqffdq:NOT_ISSUE |


#### IS_ISSUE

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:IS_ISSUE |
| Type | bdqffdq:ResponseResult |
| Different From | bdqffdq:POTENTIAL_ISSUE |


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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/extension/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


