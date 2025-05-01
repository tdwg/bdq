<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness for Use Ontology

**Title**<br>
Fitness for Use Ontology

**Date version issued**<br>
2025-04-11

**Date created**<br>
2025-04-11

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqffdq

**This version**<br>
<http://rs.tdwg.org/bdqffdq/2025-04-11>

**Latest version**<br>
<http://rs.tdwg.org/bdqffdq/>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
This document is a reference for the BDQ standard, forming the landing page for the bdqffdq ontology, describing the ontology, its uses, its vocabulary, and its vocabulary extension.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness for Use Ontology. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/2025-04-11>

**Comment**<br>
Draft Standard for Review

## Table of Contents ##
[1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Audience](#12-audience)
  - [1.3 Associated Documents](#13-associated-documents)
  - [1.4 Namespace abbreviations](#14-namespace-abbreviations)
  - [1.5 Status of the Content of this Document](#15-status-of-the-content-of-this-document)
  - [1.6 RFC 2119 key words](#16-rfc-2119-key-words)
  - [1.7 Diagram of Classes and Properties](#17-diagram-of-classes-and-properties)

[2 Use of Terms (normative)](#2-use-of-terms-normative)
  - [2.1 Use of Properties (normative)](#21-use-of-properties-normative)
    - [2.1.1 Properties Relating to Data Quality Needs (normative)](#211-properties-relating-to-data-quality-needs-normative)
    - [2.1.2 Properties Relating Data Quality Needs to Data Quality Solutions](#212-properties-relating-data-quality-needs-to-data-quality-solutions)
    - [2.1.3 Properties Relating to Data Quality Solutions Provided in a Test Description](#213-properties-relating-to-data-quality-solutions-provided-in-a-test-description)
    - [2.1.4 Properties relating to data quality solutions provided by an implementation](#214-properties-relating-to-data-quality-solutions-provided-by-an-implementation)
    - [2.1.5 Properties relating data quality reports](#215-properties-relating-data-quality-reports)
    - [2.1.6 Identifying the Test that produced an Assertion](#216-identifying-the-test-that-produced-an-assertion)
      - [2.1.6.1 Properties that should be one to one](#2161-properties-that-should-be-one-to-one)

[3. Fitness For Use Framework Summary of Mathematical Formalization (normative)](#3-fitness-for-use-framework-summary-of-mathematical-formalization-normative)
  - [3.1 Fundamental Concepts](#31-fundamental-concepts)
  - [3.2. Properties](#32-properties)
  - [3.3 Notation](#33-notation)
  - [3.4 Derived Concepts](#34-derived-concepts)
    - [3.4.1 General](#341-general)
      - [3.4.1.1 Measure](#3411-measure)
      - [3.4.1.2 Validation](#3412-validation)
      - [3.4.1.3 Amendment](#3413-amendment)
      - [3.4.1.4 Issue](#3414-issue)
    - [3.4.2 Data Quality Needs](#342-data-quality-needs)
      - [3.4.2.1 Measurement Policy](#3421-measurement-policy)
      - [3.4.2.2 Validation Policy](#3422-validation-policy)
      - [3.4.2.3 Enhancement Policy](#3423-enhancement-policy)
      - [3.4.2.4 Data Quality Profile](#3424-data-quality-profile)
      - [3.4.2.5 Use Case Coverage](#3425-use-case-coverage)
      - [3.4.2.6 Valuable Information Elements](#3426-valuable-information-elements)
      - [3.4.2.7 Acceptable Data Quality Measure](#3427-acceptable-data-quality-measure)
      - [3.4.2.8 Improvement Target](#3428-improvement-target)
    - [3.4.3 Data Quality Solutions](#343-data-quality-solutions)
      - [3.4.3.1 Measurement Method](#3431-measurement-method)
      - [3.4.3.2 Validation Method](#3432-validation-method)
      - [3.4.3.3 Enhancement Method](#3433-enhancement-method)
      - [3.4.3.4 Implementation](#3434-implementation)
      - [3.4.3.5 Mechanism Coverage](#3435-mechanism-coverage)
    - [3.4.4 Data Quality Reports](#344-data-quality-reports)
      - [3.4.4.1 Data Resource](#3441-data-resource)
      - [3.4.4.2 ValidationAssertion](#3442-validationassertion)
      - [3.4.4.3 MeasurementAssertion](#3443-measurementassertion)
      - [3.4.4.4 AmendmentAssertion](#3444-amendmentassertion)
      - [3.4.4.5 Data Quality Assessment](#3445-data-quality-assessment)
      - [3.4.4.6 Quality Control](#3446-quality-control)
      - [3.4.4.7 Quality Assurance](#3447-quality-assurance)

[Acronyms](#acronyms)

[Glossary](#glossary)

[References](#references)

[Cite BDQ](#cite-bdq)

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to present the formal ontology of the Biodiversity Data Quality Fitness for Use Framework (the "Framework"), referred to by the namespace `bdqffdq:`. This ontology defines the terms, classes, and relationships used to represent data quality concepts in a structured and interoperable manner. It forms the conceptual and semantic foundation for the BDQ standard.

This document gathers normative statements for the ontology, explains how to use it meaningfully within biodiversity data quality workflows, and reflects the open world assumptions of RDF/OWL modeling. It provides a reference for tools and implementations that rely on this ontology for describing quality-related elements such as Use Cases, Specifications, Criteria, Amendments, and Test responses.

### 1.2 Audience

This document is intended for technical users who need to interact directly with the BDQ ontology. It will be especially useful for:

- Ontology engineers and developers working on semantic web applications or data validation systems
- Standards developers seeking to align other vocabularies with the BDQ standard
- Implementers generating or consuming RDF data that describes BDQ Tests or their results
- Researchers modeling Use Cases for biodiversity data quality assessments.

Readers should be familiar with ontology concepts, RDF/OWL syntax, and open world reasoning.

### 1.3 Associated Documents

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../index.md) page.

Information about the bdqffdq: ontology, its usage, and its extensions can be found in the following subset of BDQ resources:

- [**Fitness For Use Framework Ontology Guide**](../guide/bdqffdq/index.md) Provides a visual and narrative introduction to the concepts and application of the ontology.
- [**Fitness For Use Framework Ontology List of Terms**](../list/bdqffdq/index.md) The term list document, which enumerates and describes the vocabulary terms.
- Fitness for Use Ontology** Provides normative guidance on the use of the vocabulary. This document.
- [**Fitness For Use Framework Ontology Vocabulary Extension**](../extension/bdqffdq/index.md) Defines additional axioms extending the core vocabulary.
- [**Biodiversity Data Quality Fitness for Use Framework (Ontology)**](../../vocabulary/bdqffdq.owl) The ontology, which provides the formal RDF/OWL representation of the vocabulary.

### 1.4 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms            |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

### 1.5 Status of the Content of this Document

Sections 2 and 3 are normative.

Section 1 is non-normative

Other sections of this document are marked as normative or non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.7 Diagram of Classes and Properties

The (non-normative) diagram below is intended to help understand the normative statements in section 2 below.

![Diagram of Validation, ValidationMethod, and ValidationAssertion with related classes](../guide/bdqffdq/bdqffdq_data_quality_needs_solutions_report_validation.svg "Validation concepts in the Needs, Solutions, and Reports levels.")

The use of classes and properties in [bdqtest:](../../dist/bdqtest.ttl). See also the guidance provided in [Use of Properties (normative)
](#21-use-of-properties-normative).

## 2 Use of Terms (normative) 

When not represented as objects, controlled value strings MUST be used as values of bdqffdq:ResponseStatus, and bdqffdq:ResponseResult.

### 2.1 Use of Properties (normative) 

This guidance describes the use of the Framework Ontology, that is the bdqffdq: vocabulary terms, in an RDF context. This guidance MAY be used to develop models of the bdqffdq data quality Framework in more constrained forms, including UML object models, information models, classes in a programming language, or database schemas. 

This section describes normative expectations for the use of object and datatype properties to related instances of bdqffdq: classes in their intended ways given the open world limited use of domains, ranges, and other axioms in the [Biodiversity Data Quality Fitness for Use Framework (Ontology)](../../vocabulary/bdqffdq.owl) ontology. This guidance builds on the normative definitions of bdqffdq: object properties and datatype properties to describe how bdqffdq: terms can be composed in a useful and consistent way.

Section [2.1.6 Identifying the Test that produced an Assertion](#216-identifying-the-test-that-produced-an-assertion) highlights the importance of using the object properties with the correct cardinality to preserve the relationship between an Assertion produced by a Test and the particular Test that produced it.

#### 2.1.1 Properties Relating to Data Quality Needs (normative)

Each description of a data quality Test SHOULD include the properties and related instances described in the following paragraphs.

The bdqffdq:hasUseCase object property SHOULD have an individual with a type that is a subclass of bdqffdq:Policy as its subject. 

The bdqffdq:hasUseCase object property MAY have an individual from the bdq: vocabulary that represents a bdqffdq:UseCase as its object. 

An axiom types the range of bdqffdq:hasUseCase as a bdqffdq:UseCase. 

The bdqffdq:includedInPolicy object property SHOULD have an individual that is a subclass of bdqffdq:Policy as its subject.

The bdqffdq:includedInPolicy object property SHOULD have an individual that is a subclass of bdqffdq:DataQualityNeed as its object.

The four subclasses of bdqffdq:DataQualityNeed are bdqffdq:Validation, bdqffdq:Issue, bdqffdq:Measure and bdqffdq:Amendment.

Each individual that is a subclass of bdqffdq:DataQualityNeed SHOULD have at least one bdqffdq:includedInPolicy relationship to an instance of a subclass of bdqffdq:Policy, which is in turn related to an instance of a bdqffdq:UseCase. 

User communities MAY provide new Use Cases and MAY compose instances that are subtypes of bdqffdq:DataQualityNeed with instances of bdqffdq:Policy subclasses and instances of bdqffdq:UseCase with the object properties bdqffdq:includesInPolicy and bdqffdq:hasUseCase in new ways. 

Each instance of a subclass of a bdqffdq:DataQualityNeed SHOULD have an rdfs:label in all upper case, with underscores separating components. Tests that have a bdqffdq:hasResourceType of bdqffdq:SingleRecord SHOULD follow the convention of the subclass of bdqffdq:DataQualityNeed in all upper case as the first word, and a representation of the bdqffdq:AbstractInformationElement as a single word in all upper case as the second word, in the form TESTTYPE_INFORMATIONELEMENT_CRITERIA or TESTTYPE_INFORMATIONELEMENT_ACTION_INFORMATIONELEMENT. Tests that have a bdqffdq:hasResourceType of bdqffdq:MultiRecord SHOULD have "MULTIRECORD_" as the first element in their rdfs:label, and MAY follow the pattern MULTIRECORD_TESTTYPE_COUNT_RESULT_INFORMATIONELEMENT_CRITERIA, or MULTIRECORD_TESTTYPE_QA_INFORMATIONELEMENT_CRITERIA. The rdfs:label of the instance of the subclass of bdqffdq:DataQualityNeed SHOULD be used by humans to identify Tests.

Each instance of a subclass of bdqffdq:DataQualityNeed MUST have exactly one bdqffdq:hasResourceType object property linking it to a bdqffdq:SingleRecord or a bdqffdq:MultiRecord.

The bdqffdq:hasCriterion object property SHOULD have an individual with a type that is a bdqffdq:Validation or a bdqffdq:Issue as its subject.

The bdqffdq:hasCriterion object property MAY have an individual from the bdqcrit: vocabulary as its object.

An axiom types the range of bdqffdq:hasCriterion as a bdqffdq:Criterion.

The bdqffdq:hasEnhancement object property SHOULD have an individual with a type that is a bdqffdq:Amendment as its subject.

The bdqffdq:hasEnhancement object property MAY have an individual from the bdqenh: vocabulary as its object.

An axiom types the range of bdqffdq:hasEnhancement as a bdqffdq:Enhancement.

The bdqffdq:hasDataQualityDimension object property SHOULD have an individual with a type that is a subclass of bdqffdq:DataQualityNeed as its subject.

The bdqffdq:hasDataQualityDimension object property MAY have an individual in the bdqdim: vocabulary is its object. 

An axiom types the range of bdqffdq:hasDataQualityDimension as a bdqffdq:DataQualityDimension.

Each individual instance of a bdqffdq:Validation SHOULD have exactly one bdqffdq:hasDataQualityDimension property and exactly one bdqffdq:Criterion property.

Each individual instance of a bdqffdq:Issue SHOULD have exactly one bdqffdq:hasDataQualityDimension property and exactly one bdqffdq:Criterion property.

Each individual instance of a bdqffdq:Measure SHOULD have exactly one bdqffdq:hasDataQualityDimension property.

Each individual instance of a bdqffdq:Amendment SHOULD have exactly one bdqffdq:hasDataQualityDimension property and exactly one bdqffdq:Enhancement property.

A subproperty of the bdqffdq:hasInformationElement object property SHOULD have an individual that is a subclass of bdqffdq:InformationElement as its object.

A subproperty of the bdqffdq:hasInformationElement object property SHOULD have an individual that is a subclass of bdqffdq:DataQualityNeed as its subject.

Each instance of a subclass of bdqffdq:DataQualityNeed SHOULD have exactly one bdqffdq:hasActedUponInformationElement property linking it to a bdqffdq:ActedUpon. 

Each instance of bdqffdq:ActedUpon SHOULD have one to many bdqffdq:composedOf object properties linking it to specific Information Elements.

Each instance of a subclass of bdqffdq:DataQualityNeed MAY have exactly one bdqffdq:hasConsultedInformationElement property linking it to a bdqffdq:Consulted.

Each instance of bdqffdq:Consulted SHOULD have one to many bdqffdq:composedOf object properties linking it to specific Information Elements.

Each instance of a subclass of bdqffdq:DataQualityNeed MAY have a bdqffdq:hasInformationElement property linking it to a bdqffdq:AbstractInformationElement.

Each instance of bdqffdq:AbstractInformationElement SHOULD have rdfs:label and rdfs:comment properties describing the scope of the Information Element with the rdfs:label corresponding to the INFORMATIONELEMENT portion of the rdfs:label for an instance of a subclass of bdqffdq:DataQualityNeed following the convention described above in this section. 

#### 2.1.2 Properties Relating Data Quality Needs to Data Quality Solutions

Each description of a data quality Test SHOULD include the properties and related instances given below.

The bdqffdq:forValidation object property SHOULD have have an individual with a type that is a subclass of bdqffdq:ValidationMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forValidation object property as a bdqffdq:Validation.

Each bdqffdq:Validation method SHOULD have exactly one bdqffdq:forValidation object property.

The bdqffdq:forAmendment object property SHOULD have have an individual with a type that is a subclass of bdqffdq:AmendmentMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forAmendment object property as a bdqffdq:Amendment.

Each bdqffdq:Amendment method SHOULD have exactly one bdqffdq:forAmendment object property.

The bdqffdq:forMeasure object property SHOULD have have an individual with a type that is a subclass of bdqffdq:MeasureMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forMeasure object property as a bdqffdq:Measure.

Each bdqffdq:Measure method SHOULD have exactly one bdqffdq:forMeasure object property.

The bdqffdq:forIssue object property SHOULD have have an individual with a type that is a subclass of bdqffdq:IssueMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forIssue object property as a bdqffdq:Issue.

Each bdqffdq:Issue method SHOULD have exactly one bdqffdq:forIssue object property.

#### 2.1.3 Properties Relating to Data Quality Solutions Provided in a Test Description

Each description of a data quality Test SHOULD include the following properties and related instances.

The bdqffdq:hasSpecification object property SHOULD have an instance of a subclass of bdqffdq:DataQualityMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:hasSpecification object property as a bdqffdq:Specification.

An instance of bdqffdq:Specification SHOULD be the object of exactly one bdqffdq:hasSpecification property linking it to an instance of a subclass of bdqffdq:DataQualityMethod, which SHOULD be the subject of exactly one subproperty of a bdqffdq:forDataQualityNeed property linking it to a subclass of bdqffdq:DataQualityNeed.

The bdqffdq:hasArgument object property SHOULD have a bdqffdq:Specification as its subject.

An axiom types the object of the bdqffdq:hasArgument object as a bdqffdq:Argument.

An instance of bdqffdq:Argument SHOULD have exactly one bdqffdq:hasArgumentValue data property holding the value of the argument that replaces the bdqffdq:Parameter in the bdqffdq:hasExpectedResponse of the bdqffdq:Specification. An instance of bdqffdq:Argument SHOULD have exactly one bdqffdq:hasParameter object property that denotes the parameter within the bdqffdq:hasExpectedResponse that is to be replaced by the value of the bdqffdq:hasArgumentValue. An instance of bdqffdq:Argument SHOULD be related to exactly one instance of a bdqffdq:Specification with the bdqffdq:hasArgument object property.

Each instance of a bdqffdq:Specification MAY have zero to many bdqffdq:hasArgument object properties relating it to zero to many bdqffdq:Argument instances.

Each instance of a bdqffdq:Specification with a bdqffdq:hasAuthoritiesDefaults value that references at least one parameter MUST have a corresponding bdqffdq:hasArgument object property. The instances of bdqffdq:Argument related through these bdqffdq:hasArgument object properties SHOULD have appropriate bdqffdq:hasArgumentValue and bdqffdq:hasParameter triples to express the actual and formal parameters for the bdqffdq:Specification instance.

The bdqffdq:hasParameter object property SHOULD have a bdqffdq:Argument as its subject.

An axiom types the object of the bdqffdq:hasParameter object property as a bdqffdq:Parameter.

#### 2.1.4 Properties relating to data quality solutions provided by an implementation

Each data quality mechanism that produces data quality reports using the bdqffdq: vocabulary SHOULD include the following properties and related instances.

The bdqffdq:usesSpecification object property SHOULD have a bdqffdq:Implementation as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:usesSpecification object property as a bdqffdq:Specification.

Each bdqffdq:Implementation SHOULD have one and only one bdqffdq:usesSpecification object property.

The bdqffdq:implementedBy object property SHOULD have a bdqffdq:Implementation as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:implementedBy object property as a bdqffdq:Mechanism.

Each bdqffdq:Implementation SHOULD have a bdqffdq:implementedBy object property.

A bdqffdq:Implementation SHOULD have one and only one bdqffdq:implementedBy object property.

#### 2.1.5 Properties relating data quality reports

Each data quality mechanism that produces data quality reports using the bdqffdq: vocabulary SHOULD include the following properties and related instances.

Nothing in this section is to be construed as relaxing the normative statements in the [User's Guide](../guide/users/index.md) and [Implementer's Guide](../guide/implementers/index.md) concerning the expression of data quality responses in forms other than RDF. Each data quality mechanism MUST produce results corresponding to bdqffdq:Assertions with bdqffdq:hasResponseStatus, bdqffdq:hasResponseResult, and bdqffdq:hasResponseComment as specified in those guides. 

The bdqffdq:producesAssertion object property SHOULD have an instance of bdqffdq:Implementation as its subject.

The bdqffdq:producesAssertion object property SHOULD have an instance of a subclass of bdqffdq:Assertion as its object.

Each instance of a bdqffdq:Implementation MAY have zero to many bdqffdq:producesAssertion object properties.

Each instance of a bdqffdq:Asssertion SHOULD be the object of exactly one bdqffdq:producesAssertion object property. 

#### 2.1.6 Identifying the Test that produced an Assertion

Following the object properties from an instance of a bdqffdq:Assertion to an instance of a subclass of a bdqffdq:DataQualityNeed SHOULD identify one and only one instance of a subclass of a bdqffdq:DataQualityNeed for a single instance of a bdqffdq:Assertion. If this condition is not met, it is not possible to tell which Test with which parameter argument values produced the Assertion.

Each instance of a bdqffdq:ValidationAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property linking it to an instance of a bdqffdq:Implementation, which in turn SHOULD be the subject of one and only one bdqffdq:usesSpecification property linking it to an instance of a bdqffdq:Specification, which in turn SHOULD be the object of one and only one bdqffdq:hasSpecification property linking it to an instance of a bdqffdq:ValidationMethod, which in turn SHOULD be the subject for one and only one bdqffdq:forValidation property linking it to an instance of a bdqffdq:Validation.

Each instance of a bdqffdq:IssueAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property linking it to an instance of a bdqffdq:Implementation, which in turn SHOULD be the subject of one and only one bdqffdq:usesSpecification property linking it to an instance of a bdqffdq:Specification, which in turn SHOULD be the object of one and only one bdqffdq:hasSpecification property linking it to an instance of a bdqffdq:IssueMethod, which in turn SHOULD be the subject for one and only one bdqffdq:forIssue property linking it to an instance of a bdqffdq:Issue.

Each instance of a bdqffdq:MeasurementAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property linking it to an instance of a bdqffdq:Implementation, which in turn SHOULD be the subject of one and only one bdqffdq:usesSpecification property linking it to an instance of a bdqffdq:Specification, which in turn SHOULD be the object of one and only one bdqffdq:hasSpecification property linking it to an instance of a bdqffdq:MeasurementMethod, which in turn SHOULD be the subject for one and only one bdqffdq:forMeasure property linking it to an instance of a bdqffdq:Measure.

Each instance of a bdqffdq:AmendmentAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property linking it to an instance of a bdqffdq:Implementation, which in turn SHOULD be the subject of one and only one bdqffdq:usesSpecification property linking it to an instance of a bdqffdq:Specification, which in turn SHOULD be the object of one and only one bdqffdq:hasSpecification property linking it to an instance of a bdqffdq:AmendmentMethod, which in turn SHOULD be the subject for one and only one bdqffdq:forAmendment property linking it to an instance of a bdqffdq:Amendment.

Given an Assertion, the following query returns which Test was run with which argument values for which parameters by which mechanism to produce it. This query SHOULD only return a single row. 
 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT ?test ?label ?description  (GROUP_CONCAT(DISTINCT ?params; separator='; ') as ?parameters) ?mechanism
    WHERE {
      ?test rdf:type bdqffdq:Validation . ?test rdfs:label ?label . ?method bdqffdq:forValidation ?test .
      ?method bdqffdq:hasSpecification ?specification . ?specification rdfs:comment ?description .
      OPTIONAL {
         ?specification bdqffdq:hasArgument ?argument . ?argument bdqffdq:hasArgumentValue ?argumentValue . ?argument bdqffdq:hasParameter ?parameter .
         BIND (CONCAT(STR(?parameter), "=" , ?argumentValue ) as ?params )
      } .
      ?implementation bdqffdq:usesSpecification ?specification . ?implementation bdqffdq:producesAssertion ?assertion .
      ?implementation bdqffdq:implementedBy ?mechanism .
      FILTER (STR(?assertion) = "{id of assertion to look up}")
    }
    GROUP BY ?test ?label ?description ?mechanism

Where, in this query, the text {id of assertion to look up} is a placeholder to replace with the id of the instance of the bdqffdq:Assertion to look up.

##### 2.1.6.1 Properties that should be one to one

**Validation**

- Each instance of a bdqffdq:Validation SHOULD be the object of one and only one bdqffdq:forValidation property.
- Each instance of a bdqffdq:ValidationMethod SHOULD be the subject of one and only one bdqffdq:forValidation property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:hasSpecification property.
- Each instance of a bdqffdq:Implementation SHOULD be the subject of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Implementation MAY be the subject of zero to many bdqffdq:producesAssertion properties.
- Each instance of a bdqffdq:ValidationAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property.

**Issue**

- Each instance of a bdqffdq:Issue SHOULD be the object of one and only one bdqffdq:forIssue property.
- Each instance of a bdqffdq:IssueMethod SHOULD be the subject of one and only one bdqffdq:forIssue property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:hasSpecification property.
- Each instance of a bdqffdq:Implementation SHOULD be the subject of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Implementation MAY be the subject of zero to many bdqffdq:producesAssertion properties.
- Each instance of a bdqffdq:IssueAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property.

**Measure**

- Each instance of a bdqffdq:Measure SHOULD be the object of one and only one bdqffdq:forMeasure property.
- Each instance of a bdqffdq:MeasurementMethod SHOULD be the subject of one and only one bdqffdq:forMeasure property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:hasSpecification property.
- Each instance of a bdqffdq:Implementation SHOULD be the subject of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Implementation MAY be the subject of zero to many bdqffdq:producesAssertion properties.
- Each instance of a bdqffdq:MeasurementAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property.

**Amendment**

- Each instance of a bdqffdq:Amendment SHOULD be the object of one and only one bdqffdq:forAmendment property.
- Each instance of a bdqffdq:AmendmentMethod SHOULD be the subject of one and only one bdqffdq:forAmendment property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:hasSpecification property.
- Each instance of a bdqffdq:Implementation SHOULD be the subject of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Specification SHOULD be the object of one and only one bdqffdq:usesSpecification property.
- Each instance of a bdqffdq:Implementation MAY be the subject of zero to many bdqffdq:producesAssertion properties.
- Each instance of a bdqffdq:AmendmentAssertion SHOULD be the object of one and only one bdqffdq:producesAssertion property.

<!-- Term definitions here are redundant with term list document. Omitting here. -->
<!-- Code that generated the term lists here should be commented out in draft_build_bdqffdq.py. -->

<!--
 3 Term Index

 3.1 Key to Vocabulary Terms

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Name (rdf:value) | normative | Idiomatic property used for structured values. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Preferred Label (skos:prefLabel) | non-normative | The preferred lexical label for a resource, in a given language. | Abstract Information Element |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Such bdqffdq:InformationElements as DATE and DAY are abstract, they could reference any representation of those concepts. In contrast, dwc:eventDate and dwc:day can be linked to concrete bdqffdq:ActedUponInformationElements or bdqffdq:ConsultedInformationElements. |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | A bdqffdq:InformationElement described in abstract terms and not linked with any concrete terms. |
| Type (rdf:type) | normative | The subject is an instance of a class. | [http://www.w3.org/2002/07/ owl#Class](http://www.w3.org/2002/07/owl#Class) |
| SubClass Of (rdfs:subClassOf) | normative | The subject is a subclass of a class. | [https://rs.tdwg.org/ bdqffdq/terms/ InformationElement](https://rs.tdwg.org/bdqffdq/terms/InformationElement) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Abstract Information Element |


 3.2 Indexes
-->

## 3. Fitness For Use Framework Summary of Mathematical Formalization (normative) 

This is a Summary of pp.89-108 in: Veiga, A.K. 2016. A conceptual framework on biodiversity data quality. Tese (Doutorado) [Doctoral Thesis] Escola Politécnica da Universidade de São Paulo.  Departamento de Engenharia de Computação e Sistemas Digitais.156p. 

The following changes have been made to the original formulation: 

- dcmitype:Dataset replaced with MultiRecord.  
- Improvement Method changed to Enhancement Method.
- Improvement Policy changed to Enhancement Policy.
- Data Quality Improvement changed to Data QualityAmendment.
- Issue, IssuePolicy, IssueMethod, and IssueAssertion added as converse of Validation.
- Dimension in Context renamed Measure.
- Criterion in Context renamed Validation.
- Enhancement in Context renamed Amendment.

The bdqffdq ontology is framed with limited constraints and no rdfs:range axioms.  Under open world principles, it could be used in ways other than the constraints framed by this mathematical formulation, but this formulation SHOULD be treated as a guide for how to phrase Assertions using bdqffdq: terms, and how a set of Assertions made with those terms SHOULD be queried.  

### 3.1 Fundamental Concepts
* U = Use Case
* D = Dimension (e.g., Completeness)  
* IE = Information Element (e.g., coordinates)
* M = Mechanism 
* C = Criterion (e.g., “in controlled vocabulary”)
* E = Enhancement (description of a means by which data could be improved, e.g., recommend replacement value from a controlled vocabulary).
* S = Specification (specification of how a Criterion is to be evaluated, e.g., “Iterate records and calculate the proportion of records with scientific name different from null”).

### 3.2. Properties
* US = Usages 
* ID = Identifier for a resource
* RT = Resource Type {SingleRecord, MultiRecord}
* sr = instance of Single Records 
* ds = instance of Dataset
* V = Data Resource Value
* R = Assertion (result from a Mechanism, of Validation, Measurement, Improvement on Resource).

### 3.3 Notation
* X: Domain (Uppercase symbols) 
* x: instance (lowercase symbols)
* { } set
* < > tuple	
* ⋃ union
* ∁ complement
* ⋀ and (logical conjunction)
* ∈ is a member of

TODO: Update Domain/instance letters to reflect class name changes.

### 3.4 Derived Concepts
#### 3.4.1 General
##### 3.4.1.1 Measure
    ME = { me | me =< ie, d, rt >, ie ∈ IE, d ∈ D ⋀ rt ∈ RT }

    me1 = < ie1, d1, rt1 >

* “coordinate precision of single records”

##### 3.4.1.2 Validation
     VA = { va | va = < ie, c, rt >, ie ∈ IE, c ∈ C ⋀ rt ∈ RT }   

     va1 = < ie1, c1, rt1 >

* “The value of dwc:basisOfRecord of single records must be in the controlled vocabulary”

##### 3.4.1.3 Amendment

    AM = { am | am = < ie, e, rt >, ie ∈ IE, e ∈ E ⋀ rt ∈ RT }

    am1 = { < ie1, e1, rt1 >}

* “Recommend valid value for taxon name in single record”

##### 3.4.1.4 Issue

    IS = { is | is = < ie, c, rt >, ie ∈ IE, c ∈ ∁C ⋀ rt ∈ RT }

    is1 = { < ie1, c1, rt1 >}

* “Potential issue if geographic coordinate is at 0,0”

Note: Issue concepts would parallel Validation concepts, but are not shown further here.

#### 3.4.2 Data Quality Needs
##### 3.4.2.1 Measurement Policy

    MP(u) = {me | me ⊂ ME ⋀ u ∈ U }

    mp(u1) = {me1, me2, me3, me4}
    mp(u1) = {< ie1, d1, rt2 >, < ie1, d1, rt1 >, < ie2, d1, rt1 >, < ie2, d2, rt2 >}

##### 3.4.2.2 Validation Policy

    VP (u) = {va | va ⊂ VA ⋀ u ∈ U }

    vp(u1) = {va1, va2}
    vp(u1) = {< ie1, c1, rt1>, < ie2, c2, rt2> }

##### 3.4.2.3 Enhancement Policy

     EP(u) = {am | am ⊂ AM ⋀ u ∈ U }

     ep(u1) = {am1, am2}

##### 3.4.2.4 Data Quality Profile

      DQP (u) = {dqp | dqp = mp(u) ⋃ vp(u) ⋃ ep(u), mp ∈ MP , vp ∈ VP , ep ∈ EP ⋀ u ∈ U }

      dqp(u1) = {mp(u1), vp(u1), ep(u1)}

##### 3.4.2.5 Use Case Coverage 
   
     UC(u) = { us | u ∈ U ⋀ us ⊂ US}

     uc(u1) = {us1, us2}

* “A Use Case for Niche Modeling covers MAXENT and GARP modeling”

##### 3.4.2.6 Valuable Information Elements

     VIE(u) = {ie | ie ⊂ I E ⋀ u ∈ U }

* For a Use Case, what information elements are valuable.

##### 3.4.2.7 Acceptable Data Quality Measure 

     MEaq(me) = {va | me ∈ C D ⋀ va ⊂ C C}

     meaq(me1) = {va1, va2}

* For the dimension in context coordinate completeness in a dataset, acceptable quality is met by all records having coordinates COMPLETE.

Note: This is a representation of the MultiRecord Measures that return COMPLETE/NOT_COMPLETE

##### 3.4.2.8 Improvement Target

    IT(am) = {me ⋃ va | me ∈ ME, va ∈ VA ⋀ am ∈ AM}

    it(am1) = {me1, va2}

* Recommending coordinates based on textual locality improves the coordinate completeness of single records and may result in compliance with the criterion dataset must have all records with coordinates.

#### 3.4.3 Data Quality Solutions
##### 3.4.3.1 Measurement Method
    MM(me) = {s | s ⊂ S ⋀ me ∈ ME}

##### 3.4.3.2 Validation Method
    VM(va) = {s | s ⊂ S ⋀ va ∈ VA}

##### 3.4.3.3 Enhancement Method
    EM(am) = {s | s ⊂ S ⋀ am ∈ AM}

##### 3.4.3.4 Implementation 
     I (s) = {m | m ⊂ M ⋀ s ∈ S}

     i(s1) = {m1, m2}

##### 3.4.3.5 Mechanism Coverage
    MC(m) = {s | s ⊂ S ⋀ m ∈ M }

    mc(m1) = {s1, s2}

#### 3.4.4 Data Quality Reports
##### 3.4.4.1 Data Resource
    DR = { dr | dr = < id, rt, v >, id ∈ I D, rt ∈ RT , (rt = sr ⋁ rt = ds) ⋀ v ∈ V }

    dr1 =< id1, rt1, v1 >

* “dr1 is a Data Resource which represents the Dataset "3cc6171e-8c52-4f65-ad7a-32c74e395f29" which contains 251,744 records” 

##### 3.4.4.2 ValidationAssertion 

     DQV(dr) = {dqv | dqv = < va, s, m, r >, va ∈ VA, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

     dqv(dr1) = {< va1, s1, m1, r1 >}

* A DQ Validation asserts that the Contextualized Criterion “Geodetic Datum must be supplied” is COMPLIANT for a specific species occurrence and this validation was performed by the software Darwin Test by checking if the field dwc:geodeticDatum of the record was bdq:NotEmpty.

##### 3.4.4.3 MeasurementAssertion 
     DQM(dr) = {dqm | dqm =< me, s, m, r >, me ∈ ME, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}
     
     dqm(dr1) = {< me1, s1, m1, r1 >}

* Coordinate numerical precision of the dataset 3cc6171e-8c52-4f65-ad7a-32c74e395f29 is 6.16 and this value was assigned by the software DwC-A Validator 2.0 which calculated the value by the average of significant digits of each record of the dataset.

##### 3.4.4.4 AmendmentAssertion
     DQA(dr) = {dqa | dqa = < am, s, m, r >, am ∈ AM, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

     dqa(dr1) = {< am1, s1, m1, r1 >}

* An amendment is proposed to replace the current value of the dwc:scientificName by the value “Apis” because Apis is the most similar valid name based on the Levenshtein distance in the Catalog of Life database using the software DwC-A Validator 2.0.

##### 3.4.4.5 Data Quality Assessment
     A(dr) = {dqm(dr) ⋃ dqv(dr) ⋃ dqa(dr) | dqm ∈ DQM, dqv ∈ DQV , dqa ∈ DQA ⋀ dr ∈ DR}

     a(dr1) = {dqm1, dqm2, dqm3, dqv1, dqa1}

##### 3.4.4.6 Quality Control
     QC(dr) = {dqv(dr) ⋃ dqa(dr) | dqv ∈ DQV , dqa ∈ DQI ⋀ dr ∈ DR}

     qc(dr1) = {dqv1, dqa1}

##### 3.4.4.7 Quality Assurance
     QA(dr) = {dqv(dr) | dqv ∈ DQV ⋀ dr ∈ DR}

     qa(dr1) = {dqv1, dqv2}

## Acronyms

A list of Acronyms can be found in the [Acronyms](../../index.md#5-acronyms) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary

A glossary of terms additional to those in the various namespaces can be found in the [Glossary](../../index.md#6-glossary) section of the Biodiversity Data Quality (BDQ) landing page.

## References

The references for the BDQ standard can be found in the [References](../../index.md#7-references) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness for Use Ontology. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


