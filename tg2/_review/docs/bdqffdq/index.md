<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness For Use Framework Ontology

**Title**<br>
Fitness For Use Framework Ontology

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqffdq

**This version**<br>
<http://rs.tdwg.org/bdqffdq/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdqffdq/>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
This document is a reference for the BDQ standard, describing the Fitness for Use Framework ontology, its uses, its vocabulary, and its vocabulary extension.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
    - [1.3.1 Distributions (non-normative)](#131-distributions-non-normative)
  - [1.4 Namespace abbreviations (non-normative)](#14-namespace-abbreviations-non-normative)
  - [1.5 Status of the Content of this Document (normative)](#15-status-of-the-content-of-this-document-normative)
  - [1.6 RFC 2119 key words (normative)](#16-rfc-2119-key-words-normative)
  - [1.7 Referring to Terms (normative)](#17-referring-to-terms-normative)
  - [1.8 Relating Classes and Properties (non-normative)](#18-relating-classes-and-properties-non-normative)

[2 Use of Terms (normative)](#2-use-of-terms-normative)
  - [2.1 Use of Properties (normative)](#21-use-of-properties-normative)
    - [2.1.1 Properties Relating to Data Quality Needs (normative)](#211-properties-relating-to-data-quality-needs-normative)
    - [2.1.2 Properties Relating Data Quality Needs to Data Quality Solutions (normative)](#212-properties-relating-data-quality-needs-to-data-quality-solutions-normative)
    - [2.1.3 Properties Relating to Data Quality Solutions Provided in a Test Description (normative)](#213-properties-relating-to-data-quality-solutions-provided-in-a-test-description-normative)
    - [2.1.4 Properties relating to data quality solutions provided by an implementation (normative)](#214-properties-relating-to-data-quality-solutions-provided-by-an-implementation-normative)
    - [2.1.5 Properties relating `Data Quality Reports` (normative)](#215-properties-relating-`data-quality-reports`-normative)
    - [2.1.6 Identifying the Test that produced an Assertion (normative)](#216-identifying-the-test-that-produced-an-assertion-normative)
      - [2.1.6.1 Properties that should be one-to-one (normative)](#2161-properties-that-should-be-one-to-one-normative)

[3 Fitness For Use Framework Summary of Mathematical Formalization (normative)](#3-fitness-for-use-framework-summary-of-mathematical-formalization-normative)
  - [3.1 Fundamental Concepts (normative)](#31-fundamental-concepts-normative)
  - [3.2 Properties (normative)](#32-properties-normative)
  - [3.3 Notation (normative)](#33-notation-normative)
  - [3.4 Derived Concepts (normative)](#34-derived-concepts-normative)
    - [3.4.1 General (normative)](#341-general-normative)
      - [3.4.1.1 Validation (normative)](#3411-validation-normative)
      - [3.4.1.2 Issue (normative)](#3412-issue-normative)
      - [3.4.1.3 Measure (normative)](#3413-measure-normative)
      - [3.4.1.4 Amendment (normative)](#3414-amendment-normative)
    - [3.4.2 Data Quality Needs (normative)](#342-data-quality-needs-normative)
      - [3.4.2.1 Validation Policy (normative)](#3421-validation-policy-normative)
      - [3.4.2.2 Measurement Policy (normative)](#3422-measurement-policy-normative)
      - [3.4.2.3 Enhancement Policy (normative)](#3423-enhancement-policy-normative)
      - [3.4.2.4 Data Quality Profile (normative)](#3424-data-quality-profile-normative)
      - [3.4.2.5 Use Case Coverage (normative)](#3425-use-case-coverage-normative)
      - [3.4.2.6 Valuable Information Elements (normative)](#3426-valuable-information-elements-normative)
      - [3.4.2.7 Acceptable Data Quality Measure (normative)](#3427-acceptable-data-quality-measure-normative)
      - [3.4.2.8 Improvement Target (normative)](#3428-improvement-target-normative)
    - [3.4.3 Data Quality Solutions (normative)](#343-data-quality-solutions-normative)
      - [3.4.3.1 Validation Method (normative)](#3431-validation-method-normative)
      - [3.4.3.2 Measurement Method (normative)](#3432-measurement-method-normative)
      - [3.4.3.3 Enhancement Method (normative)](#3433-enhancement-method-normative)
      - [3.4.3.4 Implementation  (normative)](#3434-implementation--normative)
      - [3.4.3.5 Mechanism Coverage (normative)](#3435-mechanism-coverage-normative)
    - [3.4.4 Data Quality Reports (normative)](#344-data-quality-reports-normative)
      - [3.4.4.1 Data Resource (normative)](#3441-data-resource-normative)
      - [3.4.4.2 ValidationAssertion (normative)](#3442-validationassertion-normative)
      - [3.4.4.3 MeasurementAssertion (normative)](#3443-measurementassertion-normative)
      - [3.4.4.4 AmendmentAssertion (normative)](#3444-amendmentassertion-normative)
      - [3.4.4.5 Data Quality Assessment (normative)](#3445-data-quality-assessment-normative)
      - [3.4.4.6 Quality Control (normative)](#3446-quality-control-normative)
      - [3.4.4.7 Quality Assurance (normative)](#3447-quality-assurance-normative)

[Acronyms (non-normative)](#acronyms-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to present the formal ontology of the Biodiversity Data Quality Fitness for Use Framework (the "Framework"), referred to by the namespace `bdqffdq:`. This ontology defines the terms, classes, and relationships used to represent data quality concepts in a structured and interoperable manner. It forms the conceptual and semantic foundation for the BDQ standard.

This document gathers normative statements for the ontology, explains how to use it meaningfully within biodiversity data quality workflows, and reflects the open world assumptions of RDF/OWL modeling. It provides a reference for tools and implementations that rely on this ontology for describing quality-related elements such as `Use Cases`, `Specifications`, `Criteria`, `Amendments`, and Test Responses.

### 1.2 Audience (non-normative)

This document is intended for technical users who need to interact directly with the BDQ ontology. It will be especially useful for:

- Ontology engineers and developers working on semantic web applications or data validation systems
- Standards developers seeking to align other vocabularies with the BDQ standard
- Implementers generating or consuming RDF data that describes BDQ Tests or their results
- Researchers modeling Use Cases for biodiversity data quality assessments.

Readers should be familiar with ontology concepts, RDF/OWL syntax, and open world reasoning.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../index.md) page.

Information about the Fitness for Use ontology, its usage, and its extensions can be found in the following subset of BDQ resources:

- [**Fitness For Use Framework Ontology Guide**](../guide/bdqffdq/index.md) - Provides a visual and narrative introduction to the concepts and application of the ontology.
- [**Fitness For Use Framework Ontology List of Terms**](../list/bdqffdq/index.md) - The term list document, which enumerates and describes the vocabulary terms.
- **Fitness For Use Framework Ontology** - Provides normative guidance on the use of the vocabulary. This document.
- [**Fitness For Use Framework Ontology Vocabulary Extension**](../extension/bdqffdq/index.md) - Defines additional axioms extending the core vocabulary.

#### 1.3.1 Distributions (non-normative)

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| Owl ontology | TBD | [Biodiversity Data Quality Fitness For Use Framework (Ontology)](../../vocabulary/bdqffdq.owl) | The formal RDF/OWL representation of the vocabulary. |

### 1.4 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

### 1.5 Status of the Content of this Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

### 1.6 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.7 Referring to Terms (normative)
In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., 'https://rs.tdwg.org/bdqffdq/terms/' for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (skos:prefLabel, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. You will find all of these methods of referring to BDQ-related terms throughout the BDQ documentation.

### 1.8 Relating Classes and Properties (non-normative)

The (non-normative) diagram below illustrating `Validation` related concepts across needs, solutions, and reports areas of the framework is intended to help understand the normative statements in [2 Use of Terms (normative)](#2-use-of-terms-normative).  The diagram shows the expected relationships among `Validation`, `ValidationMethod`, and `Specification` classes, as well as their expected connections to other subclasses of `DataQualityNeed`, `DataQualitySolution`, and `DataQualityReport`.  Section [2 Use of Terms (normative)](#2-use-of-terms-normative) provides normative guidance on how properties are expected to be used to relate instances of these classes in a consistent way, as expectations limiting the open world assumptions of the RDF/OWL modeling of the `bdqffdq:` vocabulary.

![Diagram of Validation, ValidationMethod, and ValidationAssertion with related classes](../guide/bdqffdq/bdqffdq_data_quality_needs_solutions_report_validation.svg "Validation concepts in the Needs, Solutions, and Reports levels.")

The use of classes and properties in [bdqtest:](../../dist/bdqtest.ttl) also follow the guidance provided in [2.1 Use of Properties (normative)](#21-use-of-properties-normative).  The`DataQualityNeeds` (blue here) and `DataQualitySolutions` (green here) concepts in this diagram illustrate how this guidance is used in `bdqtest:` to relate the set of terms used to define a `Validation`.  The `DataQualityReports` (tan here) concepts in the diagram illustrate how a `ValidationAssertion` in a `DataQualityReport` can be related to a `Validation` and its `Specification`.  The minimal use of rdfs:range and other global axioms in `bdqffdq:` aligns with best practices for ontologies intended for reuse, integration, and extension.  This approach trades strict, machine-enforceable validation and inference for flexibility, extensibility, and a low barrier to adoption.  The normative guidance in this document mitigates the risk of inconsistent usage that is allowed by the open world design of `bdqffdq:`.

## 2 Use of Terms (normative) 

When not represented as objects, controlled value strings MUST be used as values of `bdqffdq:ResponseStatus`, and `bdqffdq:ResponseResult`.

### 2.1 Use of Properties (normative) 

This guidance describes the use of the Framework Ontology, that is the Fitness for Use (`bdqffdq:`) vocabulary terms, in an RDF context. This guidance MAY be used to develop models of the Fitness For Use Framework in more constrained forms, including UML object models, information models, classes in a programming language, or database schemas. 

This section describes normative expectations for the use of object and datatype properties to related instances of `bdqffdq:` classes in their intended ways given the open world limited use of domains, ranges, and other axioms in the [Biodiversity Data Quality Fitness for Use Framework (Ontology)](../../vocabulary/bdqffdq.owl) ontology. This guidance builds on the normative definitions of `bdqffdq:` object properties and datatype properties to describe how `bdqffdq:` terms can be composed in a useful and consistent way.

Section [2.1.6 Identifying the Test that produced an Assertion (normative)](#216-identifying-the-test-that-produced-an-assertion-normative) highlights the importance of using the object properties with the correct cardinality to preserve the relationship between an `Assertion` produced by a Test and the particular Test that produced it.

#### 2.1.1 Properties Relating to Data Quality Needs (normative)

Each description of a data quality Test SHOULD include the properties and related instances described in the following paragraphs.

The `bdqffdq:hasUseCase` object property SHOULD have an individual with a type that is a subclass of `bdqffdq:Policy` as its subject. 

The `bdqffdq:hasUseCase` object property MAY have an individual from the `bdq:` vocabulary that represents a `bdqffdq:UseCase` as its object. 

An axiom types the range of `bdqffdq:hasUseCase` as a `bdqffdq:UseCase`. 

The `bdqffdq:includedInPolicy` object property SHOULD have an individual that is a subclass of `bdqffdq:Policy` as its subject.

The `bdqffdq:includedInPolicy` object property SHOULD have an individual that is a subclass of `bdqffdq:DataQualityNeed` as its object.

The four subclasses of `bdqffdq:DataQualityNeed` are `bdqffdq:Validation`, `bdqffdq:Issue`, `bdqffdq:Measure` and `bdqffdq:Amendment`.

Each individual that is a subclass of `bdqffdq:DataQualityNeed` SHOULD have at least one `bdqffdq:includedInPolicy` relationship to an instance of a subclass of `bdqffdq:Policy`, which is in turn related to an instance of a `bdqffdq:UseCase`. 

User communities MAY provide new Use Cases and MAY compose instances that are subtypes of `bdqffdq:DataQualityNeed` with instances of `bdqffdq:Policy` subclasses and instances of `bdqffdq:UseCase` with the object properties `bdqffdq:includesInPolicy` and `bdqffdq:hasUseCase` in new ways. 

Each instance of a subclass of a `bdqffdq:DataQualityNeed` SHOULD have an `rdfs:label` in all upper case, with underscores separating components. Tests that have a `bdqffdq:hasResourceType` of `bdqffdq:SingleRecord` SHOULD follow the convention of the subclass of `bdqffdq:DataQualityNeed` in all upper case as the first word, and a representation of the `bdqffdq:AbstractInformationElement` as a single word in all upper case as the second word, in the form TESTTYPE_INFORMATIONELEMENT_CRITERIA or TESTTYPE_INFORMATIONELEMENT_ACTION_INFORMATIONELEMENT. Tests that have a `bdqffdq:hasResourceType` of `bdqffdq:MultiRecord` SHOULD have "MULTIRECORD_" as the first element in their `rdfs:label`, and MAY follow the pattern MULTIRECORD_TESTTYPE_COUNT_RESULT_INFORMATIONELEMENT_CRITERIA, or MULTIRECORD_TESTTYPE_QA_INFORMATIONELEMENT_CRITERIA. The `rdfs:label` of the instance of the subclass of `bdqffdq:DataQualityNeed` SHOULD be used by humans to identify Tests.

Each instance of a subclass of `bdqffdq:DataQualityNeed` MUST have exactly one `bdqffdq:hasResourceType` object property linking it to a `bdqffdq:SingleRecord` or a `bdqffdq:MultiRecord`.

The `bdqffdq:hasCriterion` object property SHOULD have an individual with a type that is a `bdqffdq:Validation` or a `bdqffdq:Issue` as its subject.

The `bdqffdq:hasCriterion` object property MAY have an individual from the `bdqcrit:` vocabulary as its object.

An axiom types the range of bdqffdq:hasCriterion as a bdqffdq:Criterion.

The `bdqffdq:hasEnhancement` object property SHOULD have an individual with a type that is a `bdqffdq:Amendment` as its subject.

The `bdqffdq:hasEnhancement` object property MAY have an individual from the `bdqenh:` vocabulary as its object.

An axiom types the range of `bdqffdq:hasEnhancement` as a `bdqffdq:Enhancement`.

The `bdqffdq:hasDataQualityDimension` object property SHOULD have an individual with a type that is a subclass of `bdqffdq:DataQualityNeed` as its subject.

The `bdqffdq:hasDataQualityDimension` object property MAY have an individual in the `bdqdim:` vocabulary is its object. 

An axiom types the range of `bdqffdq:hasDataQualityDimension` as a `bdqffdq:DataQualityDimension`.

Each individual instance of a `bdqffdq:Validation` SHOULD have exactly one `bdqffdq:hasDataQualityDimension` property and exactly one `bdqffdq:Criterion` property.

Each individual instance of a `bdqffdq:Issue` SHOULD have exactly one `bdqffdq:hasDataQualityDimension` property and exactly one `bdqffdq:Criterion` property.

Each individual instance of a `bdqffdq:Measure` SHOULD have exactly one `bdqffdq:hasDataQualityDimension` property.

Each individual instance of a `bdqffdq:Amendment` SHOULD have exactly one `bdqffdq:hasDataQualityDimension` property and exactly one `bdqffdq:Enhancement` property.

A subproperty of the `bdqffdq:hasInformationElement` object property SHOULD have an individual that is a subclass of `bdqffdq:InformationElement` as its object.

A subproperty of the `bdqffdq:hasInformationElement` object property SHOULD have an individual that is a subclass of `bdqffdq:DataQualityNeed` as its subject.

Each instance of a subclass of `bdqffdq:DataQualityNeed` SHOULD have exactly one `bdqffdq:hasActedUponInformationElement` property linking it to a `bdqffdq:ActedUpon`. 

Each instance of `bdqffdq:ActedUpon` SHOULD have one to many `bdqffdq:composedOf` object properties linking it to specific `Information Elements`.

Each instance of a subclass of `bdqffdq:DataQualityNeed` MAY have exactly one `bdqffdq:hasConsultedInformationElement` property linking it to a `bdqffdq:Consulted`.

Each instance of `bdqffdq:Consulted` SHOULD have one to many `bdqffdq:composedOf` object properties linking it to specific `Information Elements`.

Each instance of a subclass of `bdqffdq:DataQualityNeed` MAY have a `bdqffdq:hasInformationElement` property linking it to a `bdqffdq:AbstractInformationElement`.

Each instance of `bdqffdq:AbstractInformationElement` SHOULD have `rdfs:label` and `rdfs:comment` properties describing the scope of the `Information Element` with the `rdfs:label` corresponding to the INFORMATIONELEMENT portion of the `rdfs:label` for an instance of a subclass of `bdqffdq:DataQualityNeed` following the convention described above in this section. 

#### 2.1.2 Properties Relating Data Quality Needs to Data Quality Solutions (normative)

Each description of a data quality Test SHOULD include the properties and related instances given below.

The `bdqffdq:forValidation` object property SHOULD have an individual with a type that is a subclass of `bdqffdq:ValidationMethod` as its subject.

An axiom places an `owl:restriction` on the object of the `bdqffdq:forValidation` object property as a `bdqffdq:Validation`.

Each `bdqffdq:Validation` method SHOULD have exactly one `bdqffdq:forValidation` object property.

The `bdqffdq:forAmendment` object property SHOULD have an individual with a type that is a subclass of `bdqffdq:AmendmentMethod` as its subject.

An axiom places an `owl:restriction` on the object of the `bdqffdq:forAmendment` object property as a `bdqffdq:Amendment`.

Each `bdqffdq:Amendment` method SHOULD have exactly one `bdqffdq:forAmendment` object property.

The `bdqffdq:forMeasure` object property SHOULD have an individual with a type that is a subclass of `bdqffdq:MeasureMethod` as its subject.

An axiom places an `owl:restriction` on the object of the `bdqffdq:forMeasure` object property as a `bdqffdq:Measure`.

Each `bdqffdq:Measure` method SHOULD have exactly one `bdqffdq:forMeasure` object property.

The `bdqffdq:forIssue` object property SHOULD have an individual with a type that is a subclass of `bdqffdq:IssueMethod` as its subject.

An axiom places an `owl:restriction` on the object of the `bdqffdq:forIssue` object property as a `bdqffdq:Issue`.

Each `bdqffdq:Issue` method SHOULD have exactly one `bdqffdq:forIssue` object property.

#### 2.1.3 Properties Relating to Data Quality Solutions Provided in a Test Description (normative)

Each description of a data quality Test SHOULD include the following properties and related instances.

The `bdqffdq:hasSpecification` object property SHOULD have an instance of a subclass of `bdqffdq:DataQualityMethod` as its subject.

An axiom places an `owl:restriction` on the object of the `bdqffdq:hasSpecification` object property as a `bdqffdq:Specification`.

An instance of `bdqffdq:Specification` SHOULD be the object of exactly one `bdqffdq:hasSpecification` property linking it to an instance of a subclass of `bdqffdq:DataQualityMethod`, which SHOULD be the subject of exactly one subproperty of a `bdqffdq:forDataQualityNeed` property linking it to a subclass of `bdqffdq:DataQualityNeed`.

The `bdqffdq:hasArgument` object property SHOULD have a `bdqffdq:Specification` as its subject.

An axiom types the object of the `bdqffdq:hasArgument` object as a `bdqffdq:Argument`.

An instance of `bdqffdq:Argument` SHOULD have exactly one `bdqffdq:hasArgumentValue` data property holding the value of the argument that replaces the `bdqffdq:Parameter` in the `bdqffdq:hasExpectedResponse` of the `bdqffdq:Specification`. An instance of `bdqffdq:Argument` SHOULD have exactly one `bdqffdq:hasParameter` object property that denotes the parameter within the `bdqffdq:hasExpectedResponse` that is to be replaced by the value of the `bdqffdq:hasArgumentValue`. An instance of `bdqffdq:Argument` SHOULD be related to exactly one instance of a `bdqffdq:Specification` with the `bdqffdq:hasArgument` object property.

Each instance of a `bdqffdq:Specification` MAY have zero to many `bdqffdq:hasArgument` object properties relating it to zero to many `bdqffdq:Argument` instances.

Each instance of a `bdqffdq:Specification` with a `bdqffdq:hasAuthoritiesDefaults` value that references at least one parameter MUST have a corresponding `bdqffdq:hasArgument` object property. The instances of `bdqffdq:Argument` related through these `bdqffdq:hasArgument` object properties SHOULD have appropriate `bdqffdq:hasArgumentValue` and `bdqffdq:hasParameter` triples to express the actual and formal parameters for the `bdqffdq:Specification` instance.

The `bdqffdq:hasParameter` object property SHOULD have a `bdqffdq:Argument` as its subject.

An axiom types the object of the `bdqffdq:hasParameter` object property as a `bdqffdq:Parameter`.

#### 2.1.4 Properties relating to data quality solutions provided by an implementation (normative)

Each data quality `Mechanism` that produces `Data Quality Reports` using the `bdqffdq:` vocabulary SHOULD include the following properties and related instances.

The `bdqffdq:usesSpecification` object property SHOULD have a `bdqffdq:Implementation` as its subject.

An axiom places an `owl:restriction` on the object of the `bdqffdq:usesSpecification` object property as a `bdqffdq:Specification`.

Each `bdqffdq:Implementation` SHOULD have one and only one `bdqffdq:usesSpecification` object property.

The `bdqffdq:implementedBy` object property SHOULD have a `bdqffdq:Implementation` as its subject.

An axiom places an `owl:restriction` on the object of the `bdqffdq:implementedBy` object property as a `bdqffdq:Mechanism`.

Each `bdqffdq:Implementation` SHOULD have a `bdqffdq:implementedBy` object property.

A `bdqffdq:Implementation` SHOULD have one and only one `bdqffdq:implementedBy` object property.

#### 2.1.5 Properties relating `Data Quality Reports` (normative)

Each data quality `Mechanism` that produces `Data Quality Reports` using the `bdqffdq:` vocabulary SHOULD include the following properties and related instances.

Nothing in this section is to be construed as relaxing the normative statements in the [User's Guide](../guide/users/index.md) and [Implementer's Guide](../guide/implementers/index.md) concerning the expression of data quality responses in forms other than RDF. Each data quality `Mechanism` MUST produce results corresponding to `bdqffdq:Assertions` with `bdqffdq:hasResponseStatus`, `bdqffdq:hasResponseResult`, and `bdqffdq:hasResponseComment` as specified in those guides. 

The `bdqffdq:producesAssertion` object property SHOULD have an instance of `bdqffdq:Implementation` as its subject.

The `bdqffdq:producesAssertion` object property SHOULD have an instance of a subclass of `bdqffdq:Assertion` as its object.

Each instance of a `bdqffdq:Implementation` MAY have zero to many `bdqffdq:producesAssertion` object properties.

Each instance of a `bdqffdq:Asssertion` SHOULD be the object of exactly one `bdqffdq:producesAssertion` object property. 

#### 2.1.6 Identifying the Test that produced an Assertion (normative)

Following the object properties from an instance of a `bdqffdq:Assertion` to an instance of a subclass of a `bdqffdq:DataQualityNeed` SHOULD identify one and only one instance of a subclass of a `bdqffdq:DataQualityNeed` for a single instance of a `bdqffdq:Assertion`. If this condition is not met, it is not possible to tell which Test with which `Parameter` argument values produced the `Assertion`.

Each instance of a `bdqffdq:ValidationAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property linking it to an instance of a `bdqffdq:Implementation`, which in turn SHOULD be the subject of one and only one `bdqffdq:usesSpecification` property linking it to an instance of a `bdqffdq:Specification`, which in turn SHOULD be the object of one and only one `bdqffdq:hasSpecification` property linking it to an instance of a `bdqffdq:ValidationMethod`, which in turn SHOULD be the subject for one and only one `bdqffdq:forValidation` property linking it to an instance of a `bdqffdq:Validation`.

Each instance of a `bdqffdq:IssueAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property linking it to an instance of a `bdqffdq:Implementation`, which in turn SHOULD be the subject of one and only one `bdqffdq:usesSpecification` property linking it to an instance of a `bdqffdq:Specification`, which in turn SHOULD be the object of one and only one `bdqffdq:hasSpecification` property linking it to an instance of a `bdqffdq:IssueMethod`, which in turn SHOULD be the subject for one and only one `bdqffdq:forIssue` property linking it to an instance of a `bdqffdq:Issue`.

Each instance of a `bdqffdq:MeasurementAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property linking it to an instance of a `bdqffdq:Implementation`, which in turn SHOULD be the subject of one and only one `bdqffdq:usesSpecification` property linking it to an instance of a `bdqffdq:Specification`, which in turn SHOULD be the object of one and only one `bdqffdq:hasSpecification` property linking it to an instance of a `bdqffdq:MeasurementMethod`, which in turn SHOULD be the subject for one and only one `bdqffdq:forMeasure` property linking it to an instance of a `bdqffdq:Measure`.

Each instance of a `bdqffdq:AmendmentAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property linking it to an instance of a `bdqffdq:Implementation`, which in turn SHOULD be the subject of one and only one `bdqffdq:usesSpecification` property linking it to an instance of a `bdqffdq:Specification`, which in turn SHOULD be the object of one and only one `bdqffdq:hasSpecification` property linking it to an instance of a `bdqffdq:AmendmentMethod`, which in turn SHOULD be the subject for one and only one `bdqffdq:forAmendment` property linking it to an instance of a `bdqffdq:Amendment`.

Given an `Assertion`, the following query returns which Test was run with which argument values for which parameters by which mechanism to produce it. This query SHOULD only return a single row. 
 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT ?test ?label ?description  (GROUP_CONCAT(DISTINCT ?params; separator='; ') as ?parameters) ?mechanism
    WHERE {
      ?test rdf:type bdqffdq:Validation . ?test rdfs:label ?label . ?method bdqffdq:forValidation ?test .
      ?method `bdqffdq:hasSpecification` ?specification . ?specification rdfs:comment ?description .
      OPTIONAL {
         ?specification bdqffdq:hasArgument ?argument . ?argument bdqffdq:hasArgumentValue ?argumentValue . ?argument bdqffdq:hasParameter ?parameter .
         BIND (CONCAT(STR(?parameter), "=" , ?argumentValue ) as ?params )
      } .
      ?implementation bdqffdq:usesSpecification ?specification . ?implementation `bdqffdq:producesAssertion` ?assertion .
      ?implementation bdqffdq:implementedBy ?mechanism .
      FILTER (STR(?assertion) = "{id of assertion to look up}")
    }
    GROUP BY ?test ?label ?description ?mechanism

Where, in this query, the text {id of assertion to look up} is a placeholder to replace with the id of the instance of the `bdqffdq:Assertion` to look up.

##### 2.1.6.1 Properties that should be one-to-one (normative)

**Validation**

- Each instance of a `bdqffdq:Validation` SHOULD be the object of one and only one `bdqffdq:forValidation` property.
- Each instance of a `bdqffdq:ValidationMethod` SHOULD be the subject of one and only one `bdqffdq:forValidation` property.
- Each instance of a `bdqffdq:Specification` SHOULD be the object of one and only one `bdqffdq:hasSpecification` property.
- Each instance of a `bdqffdq:Implementation` SHOULD be the subject of one and only one `bdqffdq:usesSpecification` property.
- Each instance of a `bdqffdq:Implementation` MAY be the subject of zero to many `bdqffdq:producesAssertion` properties.
- Each instance of a `bdqffdq:ValidationAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property.

**Issue**

- Each instance of a `bdqffdq:Issue` SHOULD be the object of one and only one `bdqffdq:forIssue` property.
- Each instance of a `bdqffdq:IssueMethod` SHOULD be the subject of one and only one `bdqffdq:forIssue` property.
- Each instance of a `bdqffdq:Specification` SHOULD be the object of one and only one `bdqffdq:hasSpecification` property.
- Each instance of a `bdqffdq:Implementation` SHOULD be the subject of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:usesSpecification property.
- Each instance of a `bdqffdq:Implementation` MAY be the subject of zero to many `bdqffdq:producesAssertion` properties.
- Each instance of a `bdqffdq:IssueAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property.

**Measure**

- Each instance of a `bdqffdq:Measure` SHOULD be the object of one and only one `bdqffdq:forMeasure` property.
- Each instance of a `bdqffdq:MeasurementMethod` SHOULD be the subject of one and only one `bdqffdq:forMeasure` property.
- Each instance of a `bdqffdq:Specification` SHOULD be the object of one and only one `bdqffdq:hasSpecification` property.
- Each instance of a `bdqffdq:Implementation` SHOULD be the subject of one and only one `bdqffdq:usesSpecification` property.
- Each instance of a `bdqffdq:Specification` SHOULD be the object of one and only one `bdqffdq:usesSpecification` property.
- Each instance of a `bdqffdq:Implementation` MAY be the subject of zero to many `bdqffdq:producesAssertion` properties.
- Each instance of a `bdqffdq:MeasurementAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property.

**Amendment**

- Each instance of a `bdqffdq:Amendment` SHOULD be the object of one and only one `bdqffdq:forAmendment` property.
- Each instance of a `bdqffdq:AmendmentMethod` SHOULD be the subject of one and only one `bdqffdq:forAmendment` property.
- Each instance of a `bdqffdq:Specification` SHOULD be the object of one and only one `bdqffdq:hasSpecification` property.
- Each instance of a `bdqffdq:Implementation` SHOULD be the subject of one and only one `bdqffdq:usesSpecification` property.
- Each instance of a `bdqffdq:Specification` SHOULD be the object of one and only one `bdqffdq:usesSpecification` property.
- Each instance of a `bdqffdq:Implementation` MAY be the subject of zero to many `bdqffdq:producesAssertion` properties.
- Each instance of a `bdqffdq:AmendmentAssertion` SHOULD be the object of one and only one `bdqffdq:producesAssertion` property.

## 3 Fitness For Use Framework Summary of Mathematical Formalization (normative) 

This is a Summary of pp.89-108 in: Veiga, A.K. 2016. A conceptual framework on biodiversity data quality. Tese (Doutorado) [Doctoral Thesis] Escola Politécnica da Universidade de São Paulo. Departamento de Engenharia de Computação e Sistemas Digitais.156p. 

The following changes have been made to the original formulation: 

- `dcmitype:Dataset` replaced with `Multi Record`.
- `Dimension` replaced with `Data Quality Dimension`.
- 'Data Quality Dimension' can apply to classes other than `Measure`, that is `Validation`, `Issue`, and `Amendment` can have `Data Quality Dimensions`.
- Improvement Method changed to Enhancement `Method`.
- Improvement Policy changed to Enhancement `Policy`.
- Data Quality Improvement changed to Data Quality `Amendment`.
- `Issue`, `IssuePolicy`, `IssueMethod`, and `IssueAssertion` added as converse of `Validation`.
- Dimension in Context renamed `Measure`.
- Criterion in Context renamed `Validation`.
- Enhancement in Context renamed `Amendment`.

The Fitness For Use Framework ontology is framed with limited constraints and no `rdfs:range` axioms. Under open world principles, it could be used in ways other than the constraints framed by this mathematical formulation, but this formulation SHOULD be treated as a guide for how to phrase `Assertions` using `bdqffdq:` terms, and how a set of `Assertions` made with those terms SHOULD be queried.

### 3.1 Fundamental Concepts (normative)
* U = `Use Case`
* D = `Dimension` (e.g., `Completeness`)  
* IE = `Information Element` (e.g., `dwc:countryCode`)
* M = `Mechanism`
* C = `Criterion` (e.g., "in controlled vocabulary")
* E = `Enhancement` (description of a means by which data could be improved, e.g., recommend replacement value from a controlled vocabulary).
* S = `Specification` (specification of how a `Criterion` is to be evaluated, e.g., "Iterate records and calculate the proportion of records with scientific name different from null").

### 3.2 Properties (normative)
* US = Usages 
* ID = Identifier for a resource
* RT = `Resource Type` {`Single Record`, `Multi Record`}
* sr = instance of `Single Record` 
* ds = instance of Dataset
* V = Data Resource Value
* R = `Assertion` (result from a `Mechanism`, of `Validation`, `Measurement`, `Improvement` on Resource).

### 3.3 Notation (normative)
* X: Domain (Uppercase symbols) 
* x: instance (lowercase symbols)
* { } set
* < > tuple	
* ⋃ union
* ∁ complement
* ⋀ and (logical conjunction)
* ∈ is a member of

### 3.4 Derived Concepts (normative)
#### 3.4.1 General (normative)
##### 3.4.1.1 Validation (normative)
     VA = { va | va = < ie, c, rt >, ie ∈ IE, c ∈ C ⋀ rt ∈ RT }   

     va1 = < ie1, c1, rt1 >

* "The value of dwc:basisOfRecord of single records must be in the controlled vocabulary"

##### 3.4.1.2 Issue (normative)

    IS = { is | is = < ie, c, rt >, ie ∈ IE, c ∈ ∁C ⋀ rt ∈ RT }

    is1 = { < ie1, c1, rt1 >}

* "Potential issue if geographic coordinate is at 0,0"

Note: `Issue` concepts would parallel `Validation` concepts, but are not shown further here.

##### 3.4.1.3 Measure (normative)
    ME = { me | me =< ie, d, rt >, ie ∈ IE, d ∈ D ⋀ rt ∈ RT }

    me1 = < ie1, d1, rt1 >

* "coordinate precision of single records"

##### 3.4.1.4 Amendment (normative)

    AM = { am | am = < ie, e, rt >, ie ∈ IE, e ∈ E ⋀ rt ∈ RT }

    am1 = { < ie1, e1, rt1 >}

* "Recommend valid value for taxon name in single record"

#### 3.4.2 Data Quality Needs (normative)
##### 3.4.2.1 Validation Policy (normative)

    VP (u) = {va | va ⊂ VA ⋀ u ∈ U }

    vp(u1) = {va1, va2}
    vp(u1) = {< ie1, c1, rt1>, < ie2, c2, rt2> }

##### 3.4.2.2 Measurement Policy (normative)

    MP(u) = {me | me ⊂ ME ⋀ u ∈ U }

    mp(u1) = {me1, me2, me3, me4}
    mp(u1) = {< ie1, d1, rt2 >, < ie1, d1, rt1 >, < ie2, d1, rt1 >, < ie2, d2, rt2 >}

##### 3.4.2.3 Enhancement Policy (normative)

     EP(u) = {am | am ⊂ AM ⋀ u ∈ U }

     ep(u1) = {am1, am2}

##### 3.4.2.4 Data Quality Profile (normative)

      DQP (u) = {dqp | dqp = mp(u) ⋃ vp(u) ⋃ ep(u), mp ∈ MP , vp ∈ VP , ep ∈ EP ⋀ u ∈ U }

      dqp(u1) = {mp(u1), vp(u1), ep(u1)}

##### 3.4.2.5 Use Case Coverage (normative)
   
     UC(u) = { us | u ∈ U ⋀ us ⊂ US}

     uc(u1) = {us1, us2}

* "A Use Case for Niche Modeling covers MAXENT and GARP modeling"

##### 3.4.2.6 Valuable Information Elements (normative)

     VIE(u) = {ie | ie ⊂ I E ⋀ u ∈ U }

* For a `Use Case`, what `Information Elements` are valuable.

##### 3.4.2.7 Acceptable Data Quality Measure (normative)

     MEaq(me) = {va | me ∈ VA ⋀ va ⊂ ME}

     meaq(me1) = {va1, va2}

* For the `Measure` coordinate completeness in a dataset, acceptable quality is met by all records having coordinates COMPLETE.

Note: This is a representation of the `Multi Record` `Measures` that return COMPLETE/NOT_COMPLETE.

##### 3.4.2.8 Improvement Target (normative)

    IT(am) = {me ⋃ va | me ∈ ME, va ∈ VA ⋀ am ∈ AM}

    it(am1) = {me1, va2}

* Recommending coordinates based on textual locality improves the coordinate completeness of `Single Records` and may result in compliance with the `Criterion` dataset must have all records with coordinates.

#### 3.4.3 Data Quality Solutions (normative)
##### 3.4.3.1 Validation Method (normative)
    VM(va) = {s | s ⊂ S ⋀ va ∈ VA}

##### 3.4.3.2 Measurement Method (normative)
    MM(me) = {s | s ⊂ S ⋀ me ∈ ME}

##### 3.4.3.3 Enhancement Method (normative)
    EM(am) = {s | s ⊂ S ⋀ am ∈ AM}

##### 3.4.3.4 Implementation  (normative)
     I (s) = {m | m ⊂ M ⋀ s ∈ S}

     i(s1) = {m1, m2}

##### 3.4.3.5 Mechanism Coverage (normative)
    MC(m) = {s | s ⊂ S ⋀ m ∈ M }

    mc(m1) = {s1, s2}

#### 3.4.4 Data Quality Reports (normative)
##### 3.4.4.1 Data Resource (normative)
    DR = { dr | dr = < id, rt, v >, id ∈ I D, rt ∈ RT , (rt = sr ⋁ rt = ds) ⋀ v ∈ V }

    dr1 =< id1, rt1, v1 >

* "dr1 is a Data Resource which represents the Dataset "3cc6171e-8c52-4f65-ad7a-32c74e395f29" which contains 251,744 records"

##### 3.4.4.2 ValidationAssertion (normative)

     DQV(dr) = {dqv | dqv = < va, s, m, r >, va ∈ VA, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

     dqv(dr1) = {< va1, s1, m1, r1 >}

* A DQ `Validation` asserts that the `Validation` "Geodetic Datum must be supplied" is COMPLIANT for a specific species `dwc:Occurrence` and this `Validation` was performed by the software Darwin Test by checking if the field `dwc:geodeticDatum` of the record was `bdq:NotEmpty`.

##### 3.4.4.3 MeasurementAssertion (normative)
     DQM(dr) = {dqm | dqm =< me, s, m, r >, me ∈ ME, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}
     
     dqm(dr1) = {< me1, s1, m1, r1 >}

* Coordinate numerical precision of the dataset 3cc6171e-8c52-4f65-ad7a-32c74e395f29 is 6.16 and this value was assigned by the software DwC-A Validator 2.0 which calculated the value by the average of significant digits of each record of the dataset.

##### 3.4.4.4 AmendmentAssertion (normative)
     DQA(dr) = {dqa | dqa = < am, s, m, r >, am ∈ AM, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

     dqa(dr1) = {< am1, s1, m1, r1 >}

* An `Amendment` is proposed to replace the current value of the `dwc:scientificName` by the value "Apis" because Apis is the most similar valid name based on the Levenshtein distance in the Catalog of Life database using the software DwC-A Validator 2.0.

##### 3.4.4.5 Data Quality Assessment (normative)
     A(dr) = {dqm(dr) ⋃ dqv(dr) ⋃ dqa(dr) | dqm ∈ DQM, dqv ∈ DQV , dqa ∈ DQA ⋀ dr ∈ DR}

     a(dr1) = {dqm1, dqm2, dqm3, dqv1, dqa1}

##### 3.4.4.6 Quality Control (normative)
     QC(dr) = {dqv(dr) ⋃ dqa(dr) | dqv ∈ DQV , dqa ∈ DQA ⋀ dr ∈ DR}

     qc(dr1) = {dqv1, dqa1}

##### 3.4.4.7 Quality Assurance (normative)
     QA(dr) = {dqv(dr) | dqv ∈ DQV ⋀ dr ∈ DR}

     qa(dr1) = {dqv1, dqv2}
## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../index.md#5-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## References (non-normative)

The references for the BDQ standard can be found in the [References (non-normative)](../../index.md#7-references-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
