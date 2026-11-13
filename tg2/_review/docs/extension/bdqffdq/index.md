<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness For Use Framework Ontology Vocabulary Extension

**Title**<br>
Fitness For Use Framework Ontology Vocabulary Extension

**Date version issued**<br>
2026-11-13

**Date created**<br>
2026-11-13

**Part of TDWG Standard**<br>
<http://www.tdwg.org/standards/YYY>

**Preferred namespace abbreviation**<br>
bdqffdq

**This version**<br>
<https://rs.tdwg.org/bdqffdq/doc/extension/2026-11-13>

**Latest version**<br>
<https://rs.tdwg.org/bdqffdq/doc/extension/>

**Abstract**<br>
This document is a reference for the BDQ standard, documenting additional axioms that extend the basic vocabulary of the Fitness For Use Framework Ontology.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2026. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <https://rs.tdwg.org/bdqffdq/doc/extension/2026-11-13>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
- [1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
    - [1.3.1 Term List Distributions (non-normative)](#131-term-list-distributions-non-normative)
  - [1.4 Status of the Content of this Document (normative)](#14-status-of-the-content-of-this-document-normative)
  - [1.5 RFC 2119 key words (normative)](#15-rfc-2119-key-words-normative)
  - [1.6 Namespace abbreviations (non-normative)](#16-namespace-abbreviations-non-normative)
  - [1.7 Referring to Terms (normative)](#17-referring-to-terms-normative)
  - [1.8 Key to Vocabulary Terms (normative)](#18-key-to-vocabulary-terms-normative)

- [2 Axiom Index (non-normative)](#2-axiom-index-non-normative)

- [4 Vocabulary Extension (normative)](#4-vocabulary-extension-normative)
  - [4.1 Range Axioms (normative)](#41-range-axioms-normative)
  - [4.2 Restrictions on Classes (normative)](#42-restrictions-on-classes-normative)
  - [4.3 General Axioms (normative)](#43-general-axioms-normative)
    - [4.3.1 Disjointness (normative)](#431-disjointness-normative)
    - [4.3.2 AllDisjointClasses (normative)](#432-alldisjointclasses-normative)
    - [4.3.3 EquivalentClass (normative)](#433-equivalentclass-normative)
    - [4.3.4 EquivalentProperty (normative)](#434-equivalentproperty-normative)
    - [4.3.5 InverseOf (normative)](#435-inverseof-normative)
    - [4.3.6 AllDifferent (normative)](#436-alldifferent-normative)
    - [4.3.7 DifferentFrom (normative)](#437-differentfrom-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to define the official vocabulary extension for the `bdqffdq:` ontology. It provides additional axioms, such as range constraints and logical distinctions, that refine and extend the semantics of the core vocabulary terms in the BDQ Fitness For Use Framework.

These axioms enable more precise reasoning, validation, and integration with OWL tools. They are intended to complement the human-readable term list provided in the main ontology documentation without altering the open and minimally constrained design of the core Fitness For Use Framework.  Additional normative expectations, which are not formally represented in the ontology or included here, are listed in [Section 3 of the Fitness For Use Framework Ontology: Concepts and Use document](../../guide/bdqffdq/index.md#3-use-of-ontology-terms-normative) to clarify the intended use of these terms in practice.

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

- [**Fitness For Use Framework Ontology: Concepts and Use**](../../guide/bdqffdq/index.md) - Provides a visual and narrative introduction to the concepts and application of the ontology along with normative guidance.
- [**Fitness For Use Framework Ontology List of Terms**](../../list/bdqffdq/index.md) - The term list document, which enumerates and describes the vocabulary terms.
- **Fitness For Use Framework Ontology Vocabulary Extension** - Defines additional axioms extending the core vocabulary *(this document)*.
- [**Biodiversity Data Quality Fitness For Use Framework (Ontology)**](../../../vocabulary/bdqffdq.owl) - The ontology, which provides the formal RDF/OWL representation of the vocabulary.

#### 1.3.1 Term List Distributions (non-normative)

| Description | IRI | Download URL | Notes | 
| ----------- | --- | -----------  | ----- | 
| HTML file   | https://rs.tdwg.org/bdqffdq/doc/extension/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/extension/bdqffdq/index.md | This file | 
| OWL Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.4 Status of the Content of this Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Section [1.8 Key to Vocabulary Terms (normative)](#18-key-to-vocabulary-terms-normative) identifies which values in Section 4 are normative and which are non-normative.

### 1.5 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.6 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| **bdqffdq:** | https://rs.tdwg.org/bdqffdq/terms/          |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#          |

### 1.7 Referring to Terms (normative)

In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., `https://rs.tdwg.org/bdqffdq/terms/` for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (`skos:prefLabel`, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. The BDQ documents use all these methods.

### 1.8 Key to Vocabulary Terms (normative)

The terminology used to describe the terms in this vocabulary follows the [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/) (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Name (rdf:value) | normative | Idiomatic property used for structured values. | Amendment |
| Type (rdf:type) | normative | The subject is an instance of a class. | owl:Class |
| Range (rdfs:range) | normative | A range of the subject property. In present context: a named class or datatype that every value of the property is an instance of. | bdqffdq:DataQualityNeed |
| SubClass Of (restriction) (rdfs:subClassOf) | normative | The subject is a subclass of a class. In present context: a restriction on the subject class, in the form [ owl:onProperty P ; owl:allValuesFrom C ]: for each instance of the class, every value of the property P is an instance of the class C. | [ owl:onProperty bdqffdq:hasEnhancement ; owl:allValuesFrom bdqffdq:Enhancement ] |
| All Different (owl:AllDifferent) | normative | The class of collections of pairwise different individuals. In present context: the named individuals listed are pairwise different (distinct codes). | bdqffdq:AMENDED, bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET, bdqffdq:FILLED_IN, bdqffdq:INTERNAL_PREREQUISITES_NOT_MET, bdqffdq:NOT_AMENDED, bdqffdq:RUN_HAS_RESULT |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Amendment |


## 2 Axiom Index (non-normative)

- [Range Axioms (normative)](#41-range-axioms-normative)
- [Restrictions on Classes (normative)](#42-restrictions-on-classes-normative)
- [General Axioms (normative)](#43-general-axioms-normative)

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


#### aggregatesResponsesFrom

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:aggregatesResponsesFrom |
| Type | owl:ObjectProperty |
| Range | bdqffdq:DataQualityNeed |


#### hasArgument

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:hasArgument |
| Type | owl:ObjectProperty |
| Range | bdqffdq:Argument |


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


### 4.2 Restrictions on Classes (normative)

Each restriction is stated on a class: for each instance of the class, the values of the property are restricted as given (for owl:allValuesFrom, every value of the property is an instance of the given class).

#### Amendment

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:Amendment |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:hasEnhancement ; owl:allValuesFrom bdqffdq:Enhancement ] |
| SubClass Of | [ owl:onProperty bdqffdq:improvedBy ; owl:allValuesFrom bdqffdq:ImprovementTarget ] |


#### AmendmentMethod

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:AmendmentMethod |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:forAmendment ; owl:allValuesFrom bdqffdq:Amendment ] |


#### DataQualityMethod

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:DataQualityMethod |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:hasSpecification ; owl:allValuesFrom bdqffdq:Specification ] |


#### DataQualityNeed

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:DataQualityNeed |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:hasDataQualityDimension ; owl:allValuesFrom bdqffdq:DataQualityDimension ] |


#### Implementation

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:Implementation |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:implementedBy ; owl:allValuesFrom bdqffdq:Mechanism ] |
| SubClass Of | [ owl:onProperty bdqffdq:usesSpecification ; owl:allValuesFrom bdqffdq:Specification ] |


#### ImprovementTarget

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:ImprovementTarget |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:targetedIssue ; owl:allValuesFrom bdqffdq:Issue ] |
| SubClass Of | [ owl:onProperty bdqffdq:targetedMeasure ; owl:allValuesFrom bdqffdq:Measure ] |
| SubClass Of | [ owl:onProperty bdqffdq:targetedValidation ; owl:allValuesFrom bdqffdq:Validation ] |


#### Issue

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:Issue |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:hasCriterion ; owl:allValuesFrom bdqffdq:Criterion ] |


#### IssueMethod

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:IssueMethod |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:forIssue ; owl:allValuesFrom bdqffdq:Issue ] |


#### MeasurementMethod

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:MeasurementMethod |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:forMeasure ; owl:allValuesFrom bdqffdq:Measure ] |


#### Policy

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:Policy |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:hasUseCase ; owl:allValuesFrom bdqffdq:UseCase ] |


#### Validation

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:Validation |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:hasCriterion ; owl:allValuesFrom bdqffdq:Criterion ] |


#### ValidationMethod

| Property | Value |
| -------- | ----- |
| Name | bdqffdq:ValidationMethod |
| Type | owl:Class |
| SubClass Of | [ owl:onProperty bdqffdq:forValidation ; owl:allValuesFrom bdqffdq:Validation ] |


### 4.3 General Axioms (normative)
#### 4.3.1 Disjointness (normative)

None

#### 4.3.2 AllDisjointClasses (normative)

| Property | Value |
| -------- | ----- |
| Axiom | owl:AllDisjointClasses |
| Members | bdqffdq:AbstractInformationElement, bdqffdq:ActedUpon, bdqffdq:Consulted |

| Property | Value |
| -------- | ----- |
| Axiom | owl:AllDisjointClasses |
| Members | bdqffdq:Amendment, bdqffdq:Issue, bdqffdq:Measure, bdqffdq:Validation |

#### 4.3.3 EquivalentClass (normative)

None

#### 4.3.4 EquivalentProperty (normative)

None

#### 4.3.5 InverseOf (normative)

None

#### 4.3.6 AllDifferent (normative)

| Property | Value |
| -------- | ----- |
| Axiom | owl:AllDifferent |
| Members | bdqffdq:AMENDED, bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET, bdqffdq:FILLED_IN, bdqffdq:INTERNAL_PREREQUISITES_NOT_MET, bdqffdq:NOT_AMENDED, bdqffdq:RUN_HAS_RESULT |

| Property | Value |
| -------- | ----- |
| Axiom | owl:AllDifferent |
| Members | bdqffdq:COMPLETE, bdqffdq:COMPLIANT, bdqffdq:IS_ISSUE, bdqffdq:NOT_COMPLETE, bdqffdq:NOT_COMPLIANT, bdqffdq:NOT_ISSUE, bdqffdq:POTENTIAL_ISSUE |

#### 4.3.7 DifferentFrom (normative)

None

## Glossary (non-normative)

A glossary of acronyms and terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2026. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <https://rs.tdwg.org/bdqffdq/doc/extension/2026-11-13>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](https://creativecommons.org/licenses/by/4.0/)
