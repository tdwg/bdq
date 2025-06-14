<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness For Use Framework Ontology Guide

**Title**<br>
Fitness For Use Framework Ontology Guide

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
This document is a user's guide for the BDQ standard, describing the organization and use of the bdqffdq: ontology. The Fitness For Use Framework ontology formally describes the terms and relationships between them for evaluating the quality of biodiversity data. Because of its comprehensive nature, the Fitness For Use Framework supports varied interpretations and uses by different stakeholders. The Framework also provides a base for the bdq: and bdqtest: namespace vocabularies.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1. Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
  - [1.4 Status of the content of this document (normative)](#14-status-of-the-content-of-this-document-normative)
  - [1.5 RFC 2119 key words (normative)](#15-rfc-2119-key-words-normative)
  - [1.6 Namespace abbreviations (non-normative)](#16-namespace-abbreviations-non-normative)
  - [1.7 Referring to Terms (normative)](#17-referring-to-terms-normative)

[2 Use of Terms (normative)](#2-use-of-terms-normative)

[3 Framework for describing data quality (non-normative)](#3-framework-for-describing-data-quality-non-normative)
  - [3.1 Introduction and Context (non-normative)](#31-introduction-and-context-non-normative)
  - [3.2 Description of the Fitness For Use Framework ontology (non-normative)](#32-description-of-the-fitness-for-use-framework-ontology-non-normative)
    - [3.2.1 Data Quality Control and Data Quality Assurance (non-normative)](#321-data-quality-control-and-data-quality-assurance-non-normative)
    - [3.2.2 Information Elements (non-normative)](#322-information-elements-non-normative)
    - [3.2.3 Concepts in the Framework, Test Types: Validation, Issue, Measure, Amendment (non-normative)](#323-concepts-in-the-framework-test-types-validation-issue-measure-amendment-non-normative)
  - [3.3 Data Quality Needs, Data Quality Mechanisms, Data Quality Reports (non-normative)](#33-data-quality-needs-data-quality-mechanisms-data-quality-reports-non-normative)
  - [3.4 Responses (non-normative)](#34-responses-non-normative)
  - [3.5 Organization of the bdqtest: classes  (non-normative)](#35-organization-of-the-bdqtest-classes--non-normative)
  - [3.6 Example representation of a BDQ Test (non-normative)](#36-example-representation-of-a-bdq-test-non-normative)
  - [3.7 Cardinality of bdqffdq: terms (non-normative)](#37-cardinality-of-bdqffdq-terms-non-normative)

[4 Term index (non-normative)](#4-term-index-non-normative)
  - [4.1 Alphabetical Index of classes (non-normative)](#41-alphabetical-index-of-classes-non-normative)
  - [4.2 Alphabetical Index of object properties (non-normative)](#42-alphabetical-index-of-object-properties-non-normative)
  - [4.3 Alphabetical Index of data properties (non-normative)](#43-alphabetical-index-of-data-properties-non-normative)
  - [4.4 Alphabetical Index of named individuals (non-normative)](#44-alphabetical-index-of-named-individuals-non-normative)

[5 List of Terms with axioms in the Fitness For Use Framework ontology (normative)](#5-list-of-terms-with-axioms-in-the-fitness-for-use-framework-ontology-normative)
  - [5.1 Class terms (normative)](#51-class-terms-normative)
    - [AbstractInformationElement](#abstractinformationelement)
    - [ActedUpon](#actedupon)
    - [Amendment](#amendment)
    - [AmendmentAssertion](#amendmentassertion)
    - [AmendmentMethod](#amendmentmethod)
    - [AmendmentPolicy](#amendmentpolicy)
    - [Argument](#argument)
    - [Assertion](#assertion)
    - [Consulted](#consulted)
    - [Criterion](#criterion)
    - [DataQualityDimension](#dataqualitydimension)
    - [DataQualityMethod](#dataqualitymethod)
    - [DataQualityNeed](#dataqualityneed)
    - [DataQualityProfile](#dataqualityprofile)
    - [DataQualityReport](#dataqualityreport)
    - [DataResource](#dataresource)
    - [Enhancement](#enhancement)
    - [FundamentalConcept](#fundamentalconcept)
    - [Implementation](#implementation)
    - [ImprovementTarget](#improvementtarget)
    - [InformationElement](#informationelement)
    - [Issue](#issue)
    - [IssueAssertion](#issueassertion)
    - [IssueConcept](#issueconcept)
    - [IssueMethod](#issuemethod)
    - [IssuePolicy](#issuepolicy)
    - [Measure](#measure)
    - [MeasurementAssertion](#measurementassertion)
    - [MeasurementMethod](#measurementmethod)
    - [MeasurementPolicy](#measurementpolicy)
    - [Mechanism](#mechanism)
    - [NeedConcept](#needconcept)
    - [Parameter](#parameter)
    - [Policy](#policy)
    - [ReportConcept](#reportconcept)
    - [ResourceType](#resourcetype)
    - [ResponseQualifier](#responsequalifier)
    - [ResponseResult](#responseresult)
    - [ResponseStatus](#responsestatus)
    - [SolutionsConcept](#solutionsconcept)
    - [Specification](#specification)
    - [UseCase](#usecase)
    - [Validation](#validation)
    - [ValidationAssertion](#validationassertion)
    - [ValidationConcept](#validationconcept)
    - [ValidationMethod](#validationmethod)
    - [ValidationPolicy](#validationpolicy)
  - [5.2 ObjectProperty terms (normative)](#52-objectproperty-terms-normative)
    - [amendmentProperty](#amendmentproperty)
    - [appliesTo](#appliesto)
    - [composedOf](#composedof)
    - [containsAssertion](#containsassertion)
    - [forAmendment](#foramendment)
    - [forDataQualityNeed](#fordataqualityneed)
    - [forIssue](#forissue)
    - [forMeasure](#formeasure)
    - [forValidation](#forvalidation)
    - [hasActedUponInformationElement](#hasacteduponinformationelement)
    - [hasArgument](#hasargument)
    - [hasConsultedInformationElement](#hasconsultedinformationelement)
    - [hasCriterion](#hascriterion)
    - [hasDataQualityDimension](#hasdataqualitydimension)
    - [hasEnhancement](#hasenhancement)
    - [hasInformationElement](#hasinformationelement)
    - [hasParameter](#hasparameter)
    - [hasResourceType](#hasresourcetype)
    - [hasResponseQualifier](#hasresponsequalifier)
    - [hasResponseResult](#hasresponseresult)
    - [hasResponseStatus](#hasresponsestatus)
    - [hasSpecification](#hasspecification)
    - [hasUseCase](#hasusecase)
    - [implementedBy](#implementedby)
    - [improvedBy](#improvedby)
    - [includedInPolicy](#includedinpolicy)
    - [issueProperty](#issueproperty)
    - [measurementProperty](#measurementproperty)
    - [producesAssertion](#producesassertion)
    - [reportProperty](#reportproperty)
    - [targetedIssue](#targetedissue)
    - [targetedMeasure](#targetedmeasure)
    - [targetedValidation](#targetedvalidation)
    - [usesSpecification](#usesspecification)
    - [validationProperty](#validationproperty)
  - [5.3 DataProperty terms (normative)](#53-dataproperty-terms-normative)
    - [hasAuthoritiesDefaults](#hasauthoritiesdefaults)
    - [hasDateLastUpdated](#hasdatelastupdated)
    - [hasExpectedResponse](#hasexpectedresponse)
    - [hasResponseComment](#hasresponsecomment)
    - [hasResponseResultValue](#hasresponseresultvalue)
  - [5.4 NamedIndividual terms (normative)](#54-namedindividual-terms-normative)
    - [MultiRecord](#multirecord)
    - [SingleRecord](#singlerecord)
    - [COMPLETE](#complete)
    - [IS_ISSUE](#is_issue)
    - [IS_ISSUE](#is_issue)
    - [NOT_COMPLETE](#not_complete)
    - [NOT_ISSUE](#not_issue)
    - [POTENTIAL_ISSUE](#potential_issue)
    - [AMENDED](#amended)
    - [NOT_AMENDED](#not_amended)
    - [RUN_HAS_RESULT](#run_has_result)

[Acronyms (non-normative)](#acronyms-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1. Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to provide a practical guide to understanding and using the [Biodiversity Data Quality Fitness for Use Framework Ontology](../../../vocabulary/bdqffdq.owl), represented by the `bdqffdq:` vocabulary. This ontology defines a formal framework for describing data quality in the context of biodiversity data, emphasizing that quality is always relative to a particular purpose or use.

The document explains key concepts from the ontology, including `Use Case`, `Information Element`, `Specification`, and `Criterion`, and shows how they support the structure and semantics of BDQ Tests. It provides context, illustrative examples, and guidance for interpreting the ontology as applied in real-world implementations.

### 1.2 Audience (non-normative)

This guide is intended for users who need a technical understanding of the Fitness for Use Framework and its ontology. It will be particularly useful for:

- Ontology engineers and information modelers incorporating the BDQ standard into semantic systems
- Standards developers aligning other biodiversity data quality frameworks with the BDQ standard
- Implementers needing to understand how BDQ Tests are formally structured and classified
- Advanced users exploring the logical foundation behind BDQ Test design.

Some familiarity with RDF/OWL ontologies is assumed.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

Information about the Fitness For Use Framework ontology, its usage, and its extensions can be found in the following subset of BDQ resources:

- **Fitness For Use Framework Ontology Guide** - Provides a visual and narrative introduction to the concepts and application of the ontology. This document.
- [**Fitness For Use Framework Ontology List of Terms**](../../list/bdqffdq/index.md) - The term list document, which enumerates and describes the vocabulary terms.
- [**Fitness for Use Framework Ontology**](../../bdqffdq/index.md) - Provides normative guidance on the use of the vocabulary.
- [**Fitness For Use Framework Ontology Vocabulary Extension**](../../extension/bdqffdq/index.md) - Defines additional axioms extending the core vocabulary.
- [**Biodiversity Data Quality Fitness for Use Framework (Ontology)**](../../../vocabulary/bdqffdq.owl) - The ontology, which provides the formal RDF/OWL representation of the vocabulary.

### 1.4 Status of the content of this document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Figures are non-normative.

### 1.5 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

### 1.7 Referring to Terms (normative)

In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., `https://rs.tdwg.org/bdqffdq/terms/` for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (skos:prefLabel, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. You will find all of these methods of referring to BDQ-related terms throughout the BDQ documentation.

## 2 Use of Terms (normative)

When not represented as objects, controlled value strings MUST be used as values of `bdqffdq:ResponseStatus`, and `bdqffdq:ResponseResult`.

IRIs MUST be used as values for all individual class instances and object properties when using bdqffdq: terms.

## 3 Framework for describing data quality (non-normative)

### 3.1 Introduction and Context (non-normative)

The `bdqffdq:` portion of the BDQ standard is a specification for a framework for describing data quality. This Fitness for Use Framework (often referred to simply as "The Framework") is based on a mathematical formulation, using set theory (Veiga, 2016), and is represented as an OWL ontology. This document describes the organization and use of the OWL ontology.

This document provides a background for understanding the `bdqtest:` Test descriptions. Each of the Tests in the `bdqtest:` namespace have been designed and described within this Framework and are framed using the terms and concepts from the Framework. The Fitness for Use Framework provides the context for each Test, and has shaped decisions made about each Test.

See the [Fitness for Use Framework Ontology](../../bdqffdq/index.md) for a concise description and normative information about the `bdqffdq:` ontology and a summary of the mathematical formalization. See the [Fitness For Use Framework Ontology List of Terms](../../list/bdqffdq/index.md) document for the list of terms in the `bdqffdq:` vocabulary. See the [Fitness For Use Framework Ontology Vocabulary Extension](../../extension/bdqffdq/index.md) for documentation on additional axioms. See the [Biodiversity Data Quality Fitness for Use Framework (Ontology)](../../../vocabulary/bdqffdq.owl) for the formal representation of the vocabulary as an OWL ontology. The mathematical formalization provides a description of inferences and reasoning that may be made with the terms in the vocabulary.

### 3.2 Description of the Fitness For Use Framework ontology (non-normative)

The Fitness for Use Framework defines data quality in relation to a specified use, emphasizing that data quality is not abstract but purpose-dependent. It provides a formal way to describe a `Use Case` (`bdqffdq:UseCase`) and the `Criteria` for evaluating whether a dataset is fit for that purpose. By linking data quality explicitly to use, the Framework enables consistent assessment and assurance of fitness for a given purpose.

The Framework can be conceptually divided into three horizontal layers: `Data Quality Needs`, `Data Quality Solutions`, and `Data Quality Reports`. Needs describe what it means for data to have quality for some use, Solutions describe tools to evaluate quality, and Reports are produced by Solutions to describe the evaluation of quality in particular datasets.

The Framework can also be conceptually divided into four vertical themes, four sets of related concepts that carry through the Needs, Solutions, and Reports layers. These concepts are `Validation`, `Issue`, `Measure`, and `Amendment`. 

We use the informal term "Test" to describe these four vertical themes, a Test involves terms in both Needs and Solutions, and Tests produce particular reporting elements.

#### 3.2.1 Data Quality Control and Data Quality Assurance (non-normative)

The Framework draws a distinction between **Quality Control** and **Quality Assurance**. Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data to improve their quality. Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is, to assure that data used for some purpose are fit for that purpose.

#### 3.2.2 Information Elements (non-normative)

The Framework has an abstract concept of `Information Elements`. To frame Tests on Darwin Core terms in a usable way, we list specific Darwin Core terms as the `Information Elements` in each Test.

#### 3.2.3 Concepts in the Framework, Test Types: Validation, Issue, Measure, Amendment (non-normative)

The Framework defines four central concepts for describing and evaluating `Data Quality Needs`: `Validation`, `Issue`, `Measure`, and `Amendment`.  

![Diagram of Validation, Issue, Measure, and Amendment classes with DataQualityNeed as a parent node.](dataqualityneeds.png "The 4 central DataQualityNeed types in the Framework - Validation, Issue, Measure, and Amendment.")

A `Validation` assesses compliance with a need. Data have quality if they are compliant with the requirements of the Validation Test. A `Validation` relates `Information Elements` and `Resource Types` with a `Specification` of exactly how to assess fitness of the data under some narrow `Criteria`, and themselves are assembled into `Validation Policies`, which are linked to other `Policies` to cover a description of the `Data Quality Needs` of a `Use Case`.  Data have quality only with respect to some use, so `Validations` must be composed with `Use Cases` to be able to assess fitness for use.

![Diagram of the classes involved in expressing Data Quality Needs with Validations.](bdqffdq_data_quality_needs_validation.svg "Expressing `Data Quality Needs`: Validations.")

`Issues` are the converse of `Validations`. Data lack quality if an `Issue` identifies a potential problem in the data that would require further human review to determine if the data have quality for some purpose.  Like `Validations`, `Issues` relate `Information Elements` and `Resource Types` with a `Specification` of exactly how to assess fitness of the data under some `Use Case`.  No illustration is provided here, as the `Issue` concept is very similar to the `Validation` concept, but with a different focus on identifying potential problems rather than confirming compliance.  

`Measures` make an aggregate summary of some specific aspect of data quality.

![Diagram of the classes involved in expressing Data Quality Needs with Measures.](bdqffdq_data_quality_needs_measure.svg "Expressing Data Quality Needs: Measures")

`Amendments` propose changes to data or processes that, if accepted, may improve the fitness of data for a specific use.

![Diagram of the classes involved in expressing Data Quality Needs with Amendments.](bdqffdq_data_quality_needs_amendment.svg "Expressing Data Duality Needs: Amendments")

Formally, in the `Data Quality Needs` level, the Framework starts with a `Use Case`, a framing of some use to which data may be put. `Use Cases` are related to the formal description of `Data Quality Needs` through `Policies` and `Contexts`. `Contexts` (`ContextualizedCriterion`, `ContextualizedDimension`, `ContextualizedEnhancement`, `ContextualizedIssue`) relate the `Specification` of a `Need Concept`, such as a `Validation`, to the `Information Elements` that need to be examined, and to the `Resource Type` that is operated on. Each of the Tests described in this standard has a formal specification that includes each of these elements. A `Use Case` includes a set of `Policies`, `Policies` relate the `Use Case` to `Contexts`, `Contexts` link `Information Elements` to `Need Concepts` and to `Resource Types`, a `Need Concept` specifies what properties data must have to have quality. 

`Data Quality Needs` can relate to the data quality of single records (`bdqffdq:SingleRecord`) or of datasets (`bdqffdq:MultiRecord`).

![Diagram of Single Record and Multi Record as named individual instances of the Resource class, showing Resource as a rectangular node above rectangular nodes for Multi Record and Amendment. ](resource_types.png "Representation of Single Record and Multi Record as named individual instances of the Resource class.")

### 3.3 Data Quality Needs, Data Quality Mechanisms, Data Quality Reports (non-normative)

The Fitness for Use Framework organizes data quality concepts into three core areas — Needs, Mechanisms, and Reports — which can be viewed as horizontal slices through the Framework (Veiga et al., 2017).

**Data Quality Needs** begin with a `Use Case`, a formal description of a purpose for which data may be used. Each `Use Case` includes a set of `Policies`, which in turn relate to `Contexts`. `Contexts` (e.g., `ContextualizedCriterion`, `ContextualizedDimension`, `ContextualizedEnhancement`, `ContextualizedIssue`) specify the data quality requirement (Need), the relevant `Information Elements` (such as specific Darwin Core terms), and the `Resource Type` the requirement applies to. A 
Need defines the properties data must have to be considered fit for use and may include ways to improve unfit data. The Tests described in this standard are formal specifications of such Needs for BDQ purposes.

**Data Quality Mechanisms** are formal descriptions of software or other tools that implement the Tests. They execute the `Specifications` defined in the Needs layer.

**Data Quality Reports** are the outputs generated when `Mechanisms` are applied to data. The Tests include formal specifications of `Assertions` that are expected to appear in these Reports.

The Framework includes an abstract concept of `Information Elements`, which are concretely represented by specific Darwin Core terms within each Test to make evaluations practical.

For **Quality Assurance**, the Framework defines `Measures` that operate on `Multi Records` and return a `Response.result` of `COMPLETE` or `NOT_COMPLETE`. A `Multi Record` `Measure` may be `COMPLETE` if all instances of a related `Single Record` `Validation` are `COMPLIANT`.

For **Quality Control**, `Multi Record` `Measures` can return a count of `COMPLIANT` results for `Validations`, thereby indicating how fit a dataset is for its intended purpose and what adjustments are needed to make it fully fit.

![Diagram of ValidationAssertion, IssueAssertion, MeasureAssertion and AmendmentAssertion classes as subtypes of the Assertion class with ReportConcept as its parent.](assertions.png "The 4 central Assertion types in the Framework - ValidationAssertion, IssueAssertion, MeasureAssertion and AmendmentAssertion.")

Diagram of the composition of `Validation`, `Validation Method`, and `Validation Assertion` illustrating the `Data Quality Needs`, `Solutions`, and `Reports` layers of the Fitness for Use Framework, with the responsibilities of `bdqtest:` (solid lines), and implementations (dashed lines).

![Diagram of Validation, ValidationMethod, and ValidationAssertion with related classes](bdqffdq_data_quality_needs_solutions_report_validation.svg "Validation concepts in the Needs, Solutions, and Reports levels.")

A useful way to think of the Framework is to divide it horizontally into Needs, Solutions, and Reports layers, and then track the Test concepts vertically through each layer (see [Figure 3](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0178731#pone-0178731-g003) in Veiga et al., 2017). Below is a diagram that brings together the horizontal Needs, Solutions, and Reports layers with the vertical Test concepts (`Validations`, `Issues`, `Measures` and `Amendments`), with `Validation`-related concepts expanded to show all related entities in the Fitness for Use Framework.

![Diagram Illustrating both the horizontal (Needs/Solutions/Reports) layers and the vertical Test concepts (Validations, Issues, Measures and Amendments)](bdqffdq_data_quality_layers.svg "All four Tests concepts in the Needs Solutions, and Reports levels.")

### 3.4 Responses (non-normative)

The content of this section is non-normative, related normative guidance is in section [5.1 The Response Object (normative)](../implementers/index.md#51-the-response-object-normative) of the [BDQ Implementer's Guide](../implementers/index.md).

Assertions are expected to assert Response objects. These will involve, in RDF, a combination of object properties and data properties.

| Concept | bdqffdq: Term(s) | Description |
| ------- | ------- | ----------- |
| Response | bdqffdq:Assertion | The report from a single execution of a single Test, consisting of a bdq:Response.status, a bdq:Response.result, a bdq:Response.comment, and optionally, a bdq:Response.qualifier.| 
| Response.status | bdqffdq:ResponseStatus, bdqffdq:hasResponseStatus | A metadata element in a bdq:Response indicating whether a particular Test (bdqffdq:Validation, bdqffdq:Issue, bdqffdq:Measure, or bdqffdq:Amendment) was able to be performed or not. |
| Response.result | bdqffdq:ResponseResult, bdqffdq:hasResponseResult, bdqffdq:hasResponseResultValue | The element in a bdq:Response containing the value returned by a Test (bdqffdq:Validation, bdqffdq:Issue, bdqffdq:Measure, or bdqffdq:Amendment)|
| Response.comment | bdqffdq:hasResponseComment | A human readable interpretation of the results of the Test.|
| Response.qualifier | bdqffdq:ResponseQualifier, bdqffdq:hasResponseQualifier | Additional structured information that qualifies the bdq:Response, intended as an extension point for uncertainty.|

See [3.1 Structure of a Response (normative)](../../bdqtest/index.md#31-structure-of-response-normative) in [BDQ Tests and Assertions](../../bdqtest/index.md) for further normative guidance on Responses as RDF or as data structures in non-RDF settings.

### 3.5 Organization of the bdqtest: classes  (non-normative)

Following is a knowledge graph showing the is-a relationships between the classes in the Fitness for Use Framework:

![Diagram of the is-a class relationships of bdqffdq:, as a tree expanding left to right, with the root owl:Thing node not shown.](bdqffdq_class_diagram.png "Diagram showing the relationships among the bdqffdq: classes.")

### 3.6 Example representation of a BDQ Test (non-normative)

Below is a fragment in Turtle describing VALIDATION_COUNTRY_FOUND, composed of a `Validation`, linking an `Acted Upon` `Information Element`, a `Criterion`, and the `Resource Type` `Single Record`, with the `Validation` linked to a `Validation Method`, and from there a `Specification`. Also shown is a `Validation Policy` linking this `Validation` to a `Use Case`.

     <bdqtest:69b2efdc-6269-45a4-aecb-4cb99c2ae134> a <bdqffdq:Validation> ;
         rdfs:comment "Does the value of dwc:country occur in the bdq:sourceAuthority?" ;
         rdfs:label "Does the value of dwc:country occur in the bdq:sourceAuthority? Validation for SingleRecord" ;
         skos:prefLabel "VALIDATION_COUNTRY_FOUND" ;
         <bdqffdq:hasActedUponInformationElement> <urn:uuid:8a2bbe0d-7218-4861-8d70-e4f2108a6dc4> ;
         <bdqffdq:hasCriterion> <bdqcrit:Found> ;
         <bdqffdq:hasDataQualityDimension> <bdqdim:Conformance> ;
         <bdqffdq:hasResourceType> <bdqffdq:SingleRecord> .
     
     <urn:uuid:8a2bbe0d-7218-4861-8d70-e4f2108a6dc4> a <bdqffdq:ActedUpon> ;
         rdfs:label "Information Element ActedUpon dwc:country" ;
         <bdqffdq:composedOf> dwc:country ;
         <skos:prefLabel> "Information Element ActedUpon dwc:country" .
     
     <bdqcrit:Found> a <bdqffdq:Criterion> ;
         rdfs:label "Found" .

     <bdqdim:Conformance> a <bdqffdq:DataQualityDimension> ;
         rdfs:label "Conformance" .     

     <urn:uuid:04cee4e0-0c83-40cc-8de2-e7391f0a97a9> a <bdqffdq:ValidationMethod> ;
         rdfs:label "ValidationMethod: Does the value of dwc:country occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_COUNTRY_FOUND" ;
         skos:prefLabel "ValidationMethod: Does the value of dwc:country occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_COUNTRY_FOUND" ;
         <bdqffdq:forValidation> <bdqtest:69b2efdc-6269-45a4-aecb-4cb99c2ae134> ;
         <bdqffdq:hasSpecification> <urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848> .
     
     <urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848> a <bdqffdq:Specification> ;
         rdfs:comment "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:country is bdq:Empty; COMPLIANT if value of dwc:country is a place type equivalent to administrative entity of \"nation\" in the bdq:sourceAuthority; otherwise NOT_COMPLIANT bdq:sourceAuthority default = \"The Getty Thesaurus of Geographic Names (TGN)\" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}" ;
         rdfs:label "Specification for: VALIDATION_COUNTRY_FOUND" ;
         <bdqffdq:hasAuthoritiesDefaults> "bdq:sourceAuthority default = \"The Getty Thesaurus of Geographic Names (TGN)\" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}" ;
         <bdqffdq:hasExpectedResponse> "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:country is bdq:Empty; COMPLIANT if value of dwc:country is a place type equivalent to administrative entity of \"nation\" in the bdq:sourceAuthority; otherwise NOT_COMPLIANT" .
     
     <urn:uuid:0053ca4f-7d45-41ea-912e-c8847bb70142> a <bdqffdq:ValidationPolicy> ;
     	rdfs:label "ValidationPolicy: (65) validations  in UseCase bdq:Record-Management" ;
     	<http://www.w3.org/2004/02/skos/core#prefLabel> "ValidationPolicy: (65) validations  in UseCase bdq:Record-Management" ;
     	<bdqffdq:hasUseCase> <bdqffdq:Record-Management> ;
     	<bdqffdq:includesInPolicy> <bdqtest:01c6dafa-0886-4b7e-9881-2c3018c98bdc> , <bdqtest:0493bcfb-652e-4d17-815b-b0cce0742fbe> , <bdqtest:04b2c8f3-c71b-4e95-8e43-f70374c5fb92> , <bdqtest:06851339-843f-4a43-8422-4e61b9a00e75> , <bdqtest:0949110d-c06b-450e-9649-7c1374d940d1> , <bdqtest:0bb8297d-8f8a-42d2-80c1-558f29efe798> , <bdqtest:125b5493-052d-4a0d-a3e1-ed5bf792689e> , <bdqtest:14da5b87-8304-4b2b-911d-117e3c29e890> , <bdqtest:15f78619-811a-4c6f-997a-a4c7888ad849> , <bdqtest:17f03f1f-f74d-40c0-8071-2927cfc9487b> , <bdqtest:239ec40e-a729-4a8e-ba69-e0bf03ac1c44> , <bdqtest:2750c040-1d4a-4149-99fe-0512785f2d5f> , <bdqtest:2cd6884e-3d14-4476-94f7-1191cfff309b> , <bdqtest:3136236e-04b6-49ea-8b34-a65f25e3aba1> , <bdqtest:3667556d-d8f5-454c-922b-af8af38f613c> , <bdqtest:36ed36c9-b1a7-40b2-b5e2-0d012e772098> , <bdqtest:374b091a-fc90-4791-91e5-c1557c649169> , <bdqtest:3cff4dc4-72e9-4abe-9bf3-8a30f1618432> , <bdqtest:3f1db29a-bfa5-40db-9fd1-fde020d81939> , <bdqtest:3f335517-f442-4b98-b149-1e87ff16de45> , <bdqtest:401bf207-9a55-4dff-88a5-abcd58ad97fa> , <bdqtest:42408a00-bf71-4892-a399-4325e2bc1fb8> , <bdqtest:47ff73ba-0028-4f79-9ce1-ee7008d66498> , <bdqtest:4833a522-12eb-4fe0-b4cf-7f7a337a6048> , <bdqtest:49f1d386-5bed-43ae-bd43-deabf7df64fc> , <bdqtest:4c09f127-737b-4686-82a0-7c8e30841590> , <bdqtest:4daa7986-d9b0-4dd5-ad17-2d7a771ea71a> , <bdqtest:4eb48fdf-7299-4d63-9d08-246902e2857f> , <bdqtest:4f2bf8fd-fc5c-493f-a44c-e7b16153c803> , <bdqtest:5424e933-bee7-4125-839e-d8743ea69f93> , <bdqtest:5618f083-d55a-4ac2-92b5-b9fb227b832f> , <bdqtest:58486cb6-1114-4a8a-ba1e-bd89cfe887e9> , <bdqtest:66269bdd-9271-4e76-b25c-7ab81eebe1d8> , <bdqtest:69b2efdc-6269-45a4-aecb-4cb99c2ae134> , <bdqtest:6ce2b2b4-6afe-4d13-82a0-390d31ade01c> , <bdqtest:6eeac3ed-f691-457f-a42e-eaa9c8a71ce8> , <bdqtest:7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47> , <bdqtest:7bdb13a4-8a51-4ee5-be7f-20693fdb183e> , <bdqtest:7c4b9498-a8d9-4ebb-85f1-9f200c788595> , <bdqtest:7d2485d5-1ba7-4f25-90cb-f4480ff1a275> , <bdqtest:7e0c0418-fe16-4a39-98bd-80e19d95b9d1> , <bdqtest:81cc974d-43cc-4c0f-a5e0-afa23b455aa3> , <bdqtest:853b79a2-b314-44a2-ae46-34a1e7ed85e4> , <bdqtest:85803c7e-2a5a-42e1-b8d3-299a44cafc46> , <bdqtest:88d8598b-3318-483d-9475-a5acf9887404> , <bdqtest:8d787cb5-73e2-4c39-9cd1-67c7361dc02e> , <bdqtest:8f1e6e58-544b-4365-a569-fb781341644e> , <bdqtest:9a39d88c-7eee-46df-b32a-c109f9f81fb8> , <bdqtest:9beb9442-d942-4f42-8b6a-fcea01ee086a> , <bdqtest:ac2b7648-d5f9-48ca-9b07-8ad5879a2536> , <bdqtest:ad0c8855-de69-4843-a80c-a5387d20fbc8> , <bdqtest:b6ecda2a-ce36-437a-b515-3ae94948fe83> , <bdqtest:c09ecbf9-34e3-4f3e-b74a-8796af15e59f> , <bdqtest:c486546c-e6e5-48a7-b286-eba7f5ca56c4> , <bdqtest:c6adf2ea-3051-4498-97f4-4b2f8a105f57> , <bdqtest:c971fe3f-84c1-4636-9f44-b1ec31fd63c7> , <bdqtest:cdaabb0d-a863-49d0-bc0f-738d771acba5> , <bdqtest:d257eb98-27cb-48e5-8d3c-ab9fca4edd11> , <bdqtest:d708526b-6561-438e-aa1a-82cd80b06396> , <bdqtest:dc8aae4b-134f-4d75-8a71-c4186239178e> , <bdqtest:eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f> , <bdqtest:eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf> , <bdqtest:f2ce7d55-5b1d-426a-b00e-6d4efe3058ec> , <bdqtest:f51e15a6-a67d-4729-9c28-3766299d2985> , <bdqtest:ff59f77d-71e9-4eb1-aac9-8bd05c50ff70> .

### 3.7 Cardinality of bdqffdq: terms (non-normative)

The content of this section is non-normative, see the [Fitness for Use Framework Ontology](../../bdqffdq/index.md) document for related normative guidance.  These expectations are based on the mathematical formalization of the Fitness for Use Framework, and are intended to provide additional explanatory guidance on how class instances in `bdqffdq:` are expected to be related to each other through properties, failure to follow these expectations may result in an inability to use the Framework effectively.

The expected relationships between classes in the Fitness for Use Framework can be expressed as cardinality statements. Selected cardinality statements are given here to provide additional explanatory guidance on how class instances in `bdqffdq:` are expected to be related to each other through object properties. Examples here are given for terms related to `Validations`.

A `Policy` is an associative entity relating a `Use Case` to a `Data Quality Need`.

Each `Use Case` has one-to-many `Validation Policies`.
Each `Validation Policy` is for one and only one `Use Case`.
Each `Validation Policy` has one and only one `Validation` included in the `Policy`.
Each `Validation` has one-to-many related `Validation Policies`.

Each `Validation` has one and only one `Data Quality Dimension`.
Each `Validation` has one and only one `Criterion`.
Each `Validation` has one and only one `Acted Upon` `Information Element`.
Each `Acted Upon` `Information Element` is `composedOf` one-to-many concrete `Information Element` terms.
Each `Validation` has zero or one `Consulted` `Information Elements`.
Each `Consulted` `Information Element` is `composedOf` one-to-many concrete `Information Element` terms.
Each `Validation` has one and only one `Resource Type`.

A `Method` looks like, but is not, an associative entity relating a `Data Quality Need` to a `Specification`.

Each `Validation` has one and only one `ValidationMethod`.
Each `ValidationMethod` is for one and only one `Validation`.
Each `ValidationMethod` is for one and only one `Specification`.
Each `Specification` has one and only one related `ValidationMethod`.

Each `Specification` has one and only one `hasExpectedResponse`.
Each `Specification` has zero or one `hasAuthoritiesDefaults`.
Each `Specification` has zero-to-many `Arguments`.
Each `Argument` has one and only one `Parameter`.
Each `Argument` has one and only one `hasArgumentValue`.

An `Implementation` looks like, but is not, an associative entity relating `Specifications`, `Mechanisms`, and `Assertions`.

Each `Specification` is used in zero-to-many `Implementations`.
Each `Mechanism` implements one-to-many `Implementations`.
Each `Assertion` is produced by one and only one `Implementation`.
Each `Implementation` uses one and only one `Specification`.
Each `Implementation` is implemented by one and only one `Mechansism`.
Each `Implementation` produces one-to-many `Assertions`.

It is important that the chain of relationships from an instance of an `Assertion` to a `Data Quality Need` (e.g., an instance of a `bdqffdq:Validation`) be a chain of one-to-one relationships. To identify what Test with what `Parameters` made an `Assertion`, it must be possible to follow the chain of relationships from an `Assertion` to a single `Implementation` to a single `Specification` (with zero-to-many `Parameters`) to a single method to a single `Data Quality Need` (e.g., a `Validation`, with one-to-many `Information Elements`). Multiplicity should only be possible following on through `Policy` to `Use Cases` (an `Assertion` may pertain to multiple `Use Cases`), or when going from a `Data Quality Need` to `Assertions`. It is expected that an instance of a `Validation` would produce many instances of `Validation Assertions`, each of those `Validation Assertions` must be able to be related to the sole `Validation` that produced it.

## 4 Term index (non-normative)



- [Classes](#51-class-terms-normative)
- [Object Properties](#52-objectproperty-terms-normative)
- [Data Properties](#53-dataproperty-terms-normative)
- [Named Individuals](#54-namedindividual-terms-normative)

### 4.1 Alphabetical Index of classes (non-normative)

[AbstractInformationElement](#AbstractInformationElement)
[ActedUpon](#ActedUpon)
[Amendment](#Amendment)
[AmendmentAssertion](#AmendmentAssertion)
[AmendmentConcept](#AmendmentConcept)
[AmendmentMethod](#AmendmentMethod)
[AmendmentPolicy](#AmendmentPolicy)
[Argument](#Argument)
[Assertion](#Assertion)
[Consulted](#Consulted)
[Criterion](#Criterion)
[DataQualityDimension](#DataQualityDimension)
[DataQualityMethod](#DataQualityMethod)
[DataQualityNeed](#DataQualityNeed)
[DataQualityProfile](#DataQualityProfile)
[DataQualityReport](#DataQualityReport)
[DataResource](#DataResource)
[Enhancement](#Enhancement)
[FundamentalConcept](#FundamentalConcept)
[Implementation](#Implementation)
[ImprovementTarget](#ImprovementTarget)
[InformationElement](#InformationElement)
[Issue](#Issue)
[IssueAssertion](#IssueAssertion)
[IssueConcept](#IssueConcept)
[IssueMethod](#IssueMethod)
[IssuePolicy](#IssuePolicy)
[Measure](#Measure)
[MeasurementAssertion](#MeasurementAssertion)
[MeasurementConcept](#MeasurementConcept)
[MeasurementMethod](#MeasurementMethod)
[MeasurementPolicy](#MeasurementPolicy)
[Mechanism](#Mechanism)
[NeedConcept](#NeedConcept)
[Parameter](#Parameter)
[Policy](#Policy)
[ReportConcept](#ReportConcept)
[ResourceType](#ResourceType)
[ResponseQualifier](#ResponseQualifier)
[ResponseResult](#ResponseResult)
[ResponseStatus](#ResponseStatus)
[SolutionsConcept](#SolutionsConcept)
[Specification](#Specification)
[UseCase](#UseCase)
[Validation](#Validation)
[ValidationAssertion](#ValidationAssertion)
[ValidationConcept](#ValidationConcept)
[ValidationMethod](#ValidationMethod)
[ValidationPolicy](#ValidationPolicy)

### 4.2 Alphabetical Index of object properties (non-normative)

[amendmentProperty](#amendmentProperty)
[appliesTo](#appliesTo)
[composedOf](#composedOf)
[containsAssertion](#containsAssertion)
[forAmendment](#forAmendment)
[forDataQualityNeed](#forDataQualityNeed)
[forIssue](#forIssue)
[forMeasure](#forMeasure)
[forValidation](#forValidation)
[hasActedUponInformationElement](#hasActedUponInformationElement)
[hasArgument](#hasArgument)
[hasConsultedInformationElement](#hasConsultedInformationElement)
[hasCriterion](#hasCriterion)
[hasDataQualityDimension](#hasDataQualityDimension)
[hasEnhancement](#hasEnhancement)
[hasInformationElement](#hasInformationElement)
[hasParameter](#hasParameter)
[hasResourceType](#hasResourceType)
[hasResponseQualifier](#hasResponseQualifier)
[hasResponseResult](#hasResponseResult)
[hasResponseStatus](#hasResponseStatus)
[hasSpecification](#hasSpecification)
[hasUseCase](#hasUseCase)
[implementedBy](#implementedBy)
[improvedBy](#improvedBy)
[includedInPolicy](#includedInPolicy)
[issueProperty](#issueProperty)
[measurementProperty](#measurementProperty)
[producesAssertion](#producesAssertion)
[reportProperty](#reportProperty)
[targetedIssue](#targetedIssue)
[targetedMeasure](#targetedMeasure)
[targetedValidation](#targetedValidation)
[usesSpecification](#usesSpecification)
[validationProperty](#validationProperty)

### 4.3 Alphabetical Index of data properties (non-normative)

[hasArgumentValue](#hasArgumentValue)
[hasAuthoritiesDefaults](#hasAuthoritiesDefaults)
[hasDateLastUpdated](#hasDateLastUpdated)
[hasExpectedResponse](#hasExpectedResponse)
[hasResponseComment](#hasResponseComment)
[hasResponseResultValue](#hasResponseResultValue)

### 4.4 Alphabetical Index of named individuals (non-normative)

[AMENDED](#AMENDED)
[COMPLETE](#COMPLETE)
[COMPLIANT](#COMPLIANT)
[EXTERNAL_PREREQUISITES_NOT_MET](#EXTERNAL_PREREQUISITES_NOT_MET)
[FILLED_IN](#FILLED_IN)
[INTERNAL_PREREQUISITES_NOT_MET](#INTERNAL_PREREQUISITES_NOT_MET)
[IS_ISSUE](#IS_ISSUE)
[MultiRecord](#MultiRecord)
[NOT_AMENDED](#NOT_AMENDED)
[NOT_COMPLETE](#NOT_COMPLETE)
[NOT_COMPLIANT](#NOT_COMPLIANT)
[NOT_ISSUE](#NOT_ISSUE)
[POTENTIAL_ISSUE](#POTENTIAL_ISSUE)
[RUN_HAS_RESULT](#RUN_HAS_RESULT)
[SingleRecord](#SingleRecord)



## 5 List of Terms with axioms in the Fitness For Use Framework ontology (normative)

This list brings together definitions of terms in the Fitness For Use Framework vocabulary, listed in more detail in [Fitness For Use Framework Ontology List of Terms](../../list/bdqffdq/index.md). with the additional axioms in the [Fitness For Use Framework Ontology Vocabulary Extension](../../extension/bdqffdq/index.md). 


### 5.1 Class terms (normative)
#### AbstractInformationElement

- Name: bdqffdq:AbstractInformationElement
- Definition: A bdqffdq:InformationElement described in abstract terms and not linked with any concrete terms.
- SubClass Of: InformationElement

********************

#### ActedUpon

- Name: bdqffdq:ActedUpon
- Definition: A bdqffdq:InformationElement, expressed in concrete terms, about which a bdqffdq:DataQualityNeed expresses bdqffdq:Assertions about the data quality in that bdqffdq:InformationElement.
- SubClass Of: InformationElement

********************

#### Amendment

- Name: bdqffdq:Amendment
- Definition: A bdqffdq:DataQualityNeed that expresses how proposals may be made to improve the fitness for use of data.
- SubClass Of: AmendmentConcept; DataQualityNeed

********************

#### AmendmentAssertion

- Name: bdqffdq:AmendmentAssertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation evaluating a bdqffdq:Amendment supporting a particular bdqffdq:DataQualityNeed to improve a particular bdqffdq:DataResource.
- SubClass Of: AmendmentConcept; Assertion

********************

#### AmendmentMethod

- Name: bdqffdq:AmendmentMethod
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Amendment to its bdqffdq:Specifications.
- SubClass Of: AmendmentConcept; DataQualityMethod

********************

#### AmendmentPolicy

- Name: bdqffdq:AmendmentPolicy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Amendments.
- SubClass Of: AmendmentConcept; Policy

********************

#### Argument

- Name: bdqffdq:Argument
- Definition: A value that, when provided to a Test bdqffdq:Specification to replace a bdqffdq:Parameter changes the behavior of the Test in a defined manner.
- SubClass Of: SolutionsConcept

********************

#### Assertion

- Name: bdqffdq:Assertion
- Definition: A bdqffdq:ReportConcept expressing a statement about a data quality bdqffdq:Assertion following a bdqffdq:Specification produced by a bdqffdq:Implementation pertaining to a bdqffdq:DataResource.
- SubClass Of: ReportConcept

********************

#### Consulted

- Name: bdqffdq:Consulted
- Definition: A bdqffdq:InformationElement, expressed in concrete terms, about which a bdqffdq:DataQualityNeed examines in order to expresses bdqffdq:Assertions about the data quality in another bdqffdq:InformationElement.
- SubClass Of: InformationElement

********************

#### Criterion

- Name: bdqffdq:Criterion
- Definition: Rule against which data are evaluated for conformance to quality bdqffdq:Criteria.
- SubClass Of: FundamentalConcept; NeedConcept

********************

#### DataQualityDimension

- Name: bdqffdq:DataQualityDimension
- Definition: An aspect of data quality.
- SubClass Of: FundamentalConcept; NeedConcept

********************

#### DataQualityMethod

- Name: bdqffdq:DataQualityMethod
- Definition: A bdqffdq:SolutionsConcept that relates a bdqffdq:DataQualityNeed to a bdqffdq:Specification.
- SubClass Of: SolutionsConcept

********************

#### DataQualityNeed

- Name: bdqffdq:DataQualityNeed
- Definition: A bdqffdq:NeedConcept that expresses what bdqffdq:Assertions may be made about data with respect to fitness for use.
- SubClass Of: NeedConcept

********************

#### DataQualityProfile

- Name: bdqffdq:DataQualityProfile
- Definition: A bdqffdq:NeedConcept expressing the composition of bdqffdq:Policies to satisfy a bdqffdq:UseCase.
- SubClass Of: NeedConcept

********************

#### DataQualityReport

- Name: bdqffdq:DataQualityReport
- Definition: A bdqffdq:ReportConcept comprising a set of data quality bdqffdq:Assertions.
- SubClass Of: ReportConcept

********************

#### DataResource

- Name: bdqffdq:DataResource
- Definition: An owl:Thing to which a data quality bdqffdq:Assertion applies.
- SubClass Of: ReportConcept

********************

#### Enhancement

- Name: bdqffdq:Enhancement
- Definition: Description of a means by which data could be improved.
- SubClass Of: AmendmentConcept; FundamentalConcept; NeedConcept

********************

#### FundamentalConcept

- Name: bdqffdq:FundamentalConcept
- Definition: Category of fitness for use concepts that are not derived by composition with other concepts.

********************

#### Implementation

- Name: bdqffdq:Implementation
- Definition: A bdqffdq:SolutionsConcept that describes the portion of a bdqffdq:Mechanism that carries out the proccess described in a particular bdqffdq:Specification.
- SubClass Of: SolutionsConcept

********************

#### ImprovementTarget

- Name: bdqffdq:ImprovementTarget
- Definition: A specific bdqffdq:DataQualityNeed that a specific bdqffdq:Amendment is intended to improve.
- SubClass Of: NeedConcept

********************

#### InformationElement

- Name: bdqffdq:InformationElement
- Definition: A portion of data with which a bdqffdq:DataQualityNeed is concerned.
- SubClass Of: FundamentalConcept

********************

#### Issue

- Name: bdqffdq:Issue
- Definition: A bdqffdq:DataQualityNeed that expresses how quality problems may be identified in data.
- SubClass Of: DataQualityNeed; IssueConcept

********************

#### IssueAssertion

- Name: bdqffdq:IssueAssertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation evaluating a bdqffdq:Issue for a particular bdqffdq:DataQualityNeed in a particular bdqffdq:DataResource.
- SubClass Of: Assertion; IssueConcept

********************

#### IssueConcept

- Name: bdqffdq:IssueConcept
- Definition: A term involved in flagging problems or potential problems in assessment of data quality that would or might prevent the data from meeting an expressed bdqffdq:DataQualityNeed.

********************

#### IssueMethod

- Name: bdqffdq:IssueMethod
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Issue to its bdqffdq:Specifications.
- SubClass Of: DataQualityMethod; IssueConcept

********************

#### IssuePolicy

- Name: bdqffdq:IssuePolicy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Issues.
- SubClass Of: IssueConcept; Policy

********************

#### Measure

- Name: bdqffdq:Measure
- Definition: A bdqffdq:DataQualityNeed that expresses how the fitness of data for some use may be measured.
- SubClass Of: DataQualityNeed; MeasurementConcept

********************

#### MeasurementAssertion

- Name: bdqffdq:MeasurementAssertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation measuring a particular bdqffdq:DataQualityNeed in a particular bdqffdq:DataResource.
- SubClass Of: Assertion; MeasurementConcept

********************

#### MeasurementMethod

- Name: bdqffdq:MeasurementMethod
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Measure to its bdqffdq:Specifications.
- SubClass Of: DataQualityMethod; MeasurementConcept

********************

#### MeasurementPolicy

- Name: bdqffdq:MeasurementPolicy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Measures.
- SubClass Of: MeasurementConcept; Policy

********************

#### Mechanism

- Name: bdqffdq:Mechanism
- Definition: An entity that can execute bdqffdq:DataQualityMethods.
- SubClass Of: FundamentalConcept; SolutionsConcept

********************

#### NeedConcept

- Name: bdqffdq:NeedConcept
- Definition: A concept that expresses an aspect of a bdqffdq:DataQualityNeed.

********************

#### Parameter

- Name: bdqffdq:Parameter
- Definition: A placeholder for a value that, when provided to a Test bdqffdq:Specification changes the behavior of the Test in a defined manner.
- SubClass Of: SolutionsConcept

********************

#### Policy

- Name: bdqffdq:Policy
- Definition: The set of bdqffdq:DataQualityNeeds for a bdqffdq:UseCase.
- SubClass Of: NeedConcept

********************

#### ReportConcept

- Name: bdqffdq:ReportConcept
- Definition: A concept concerning data quality expressed in a bdqffdq:DataQualityReport.

********************

#### ResourceType

- Name: bdqffdq:ResourceType
- Definition: Category of things that are data objects about which data quality bdqffdq:Assertions may be made.
- SubClass Of: FundamentalConcept

********************

#### ResponseQualifier

- Name: bdqffdq:ResponseQualifier
- Definition: A bdqffdq:ReportConcept to which additional bdqffdq:Assertions providing additional information beyond that of bdqffdq:ResponseResult from the execution of the bdqffdq:Specification of a bdqffdq:DataQualityNeed are attached.
- SubClass Of: ReportConcept

********************

#### ResponseResult

- Name: bdqffdq:ResponseResult
- Definition: A bdqffdq:ReportConcept to which controlled vocabulary bdqffdq:Assertions about the result of the execution of the bdqffdq:Specification of a bdqffdq:DataQualityNeed are attached.
- SubClass Of: ReportConcept

********************

#### ResponseStatus

- Name: bdqffdq:ResponseStatus
- Definition: A bdqffdq:ReportConcept expressing controlled vocabulary values about the exit state of an execution process of a data quality bdqffdq:Specification by a bdqffdq:Implementation.
- SubClass Of: ReportConcept

********************

#### SolutionsConcept

- Name: bdqffdq:SolutionsConcept
- Definition: A concept that expresses an aspect of a data quality solution.

********************

#### Specification

- Name: bdqffdq:Specification
- Definition: A specific statement about how to evaluate a bdqffdq:DataQualityNeed.
- SubClass Of: FundamentalConcept; SolutionsConcept

********************

#### UseCase

- Name: bdqffdq:UseCase
- Definition: A bdqffdq:NeedConcept expressing a purpose to which data are put for which the data must have quality for the result to have meaning and reliability.
- SubClass Of: FundamentalConcept; NeedConcept

********************

#### Validation

- Name: bdqffdq:Validation
- Definition: A bdqffdq:DataQualityNeed that expresses how data may be evaluated for fitness for use.
- SubClass Of: DataQualityNeed; ValidationConcept

********************

#### ValidationAssertion

- Name: bdqffdq:ValidationAssertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation validating compliance with a particular bdqffdq:DataQualityNeed in a particular bdqffdq:DataResource.
- SubClass Of: Assertion; ValidationConcept

********************

#### ValidationConcept

- Name: bdqffdq:ValidationConcept
- Definition: A term involved in statements about the conformance of data to expressed bdqffdq:DataQualityNeeds.

********************

#### ValidationMethod

- Name: bdqffdq:ValidationMethod
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Validation to its bdqffdq:Specifications.
- SubClass Of: DataQualityMethod; ValidationConcept

********************

#### ValidationPolicy

- Name: bdqffdq:ValidationPolicy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Validations.
- SubClass Of: Policy; ValidationConcept

********************

### 5.2 ObjectProperty terms (normative)
#### amendmentProperty

- Name: bdqffdq:amendmentProperty
- Definition: Category of object properties that apply to bdqffdq:Amendments

********************

#### appliesTo

- Name: bdqffdq:appliesTo
- Definition: Describes the bdqffdq:DataResource about which a bdqffdq:Assertion is made.

********************

#### composedOf

- Name: bdqffdq:composedOf
- Definition: Specific vocabulary term that comprises a bdqffdq:InformationElement that is not a bdqffdq:AbstractInformationElement.

********************

#### containsAssertion

- Name: bdqffdq:containsAssertion
- Definition: Connects a bdqffdq:DataQualityReport with bdqffdq:Assertions that comprise that bdqffdq:DataQualityReport.

********************

#### forAmendment

- Name: bdqffdq:forAmendment
- Definition: Relates a bdqffdq:AmendmentMethod to a bdqffdq:Amendment.
- SubClass Of: amendmentProperty; forDataQualityNeed
- Range [ owl:someValuesFrom bdqffdq:forAmendment ]

********************

#### forDataQualityNeed

- Name: bdqffdq:forDataQualityNeed
- Definition: Category of properties that relates a bdqffdq:DataQualityNeed to specific bdqffdq:Methods.

********************

#### forIssue

- Name: bdqffdq:forIssue
- Definition: Relates a bdqffdq:IssueMethod to a bdqffdq:Issue.
- SubClass Of: forDataQualityNeed; issueProperty
- Range [ owl:someValuesFrom bdqffdq:forIssue ]

********************

#### forMeasure

- Name: bdqffdq:forMeasure
- Definition: Relates a bdqffdq:MeasurementMethod to a bdqffdq:Measure.
- SubClass Of: forDataQualityNeed; measurementProperty
- Range [ owl:someValuesFrom bdqffdq:forMeasure ]

********************

#### forValidation

- Name: bdqffdq:forValidation
- Definition: Relates a bdqffdq:ValidationMethod to a bdqffdq:Validation.
- SubClass Of: forDataQualityNeed; validationProperty
- Range [ owl:someValuesFrom bdqffdq:forValidation ]

********************

#### hasActedUponInformationElement

- Name: bdqffdq:hasActedUponInformationElement
- Definition: Describes the bdqffdq:ActedUpon bdqffdq:InformationElements assessed by a bdqffdq:DataQualityNeed about which bdqffdq:Assertions arising from the bdqffdq:DataQualityNeed would apply.
- SubClass Of: hasInformationElement

********************

#### hasArgument

- Name: bdqffdq:hasArgument
- Definition: Relates a bdqffdq:Specification to a bdqffdq:Argument
- Range bdqffdq:Argument

********************

#### hasConsultedInformationElement

- Name: bdqffdq:hasConsultedInformationElement
- Definition: Describes the bdqffdq:InformationElements assessed by a bdqffdq:DataQualityNeed in order to make bdqffdq:Assertions concerning bdqffdq:ActedUpon bdqffdq:InformationElements.
- SubClass Of: hasInformationElement

********************

#### hasCriterion

- Name: bdqffdq:hasCriterion
- Definition: The bdqffdq:Criterion under which a bdqffdq:Validation or bdqffdq:Issue assesses for data quality.
- SubClass Of: issueProperty; validationProperty
- Range [ owl:someValuesFrom bdqffdq:hasCriterion ]

********************

#### hasDataQualityDimension

- Name: bdqffdq:hasDataQualityDimension
- Definition: The bdqffdq:DataQualityDimension to which a bdqffdq:DataQualityNeed applies.
- SubClass Of: amendmentProperty; issueProperty; measurementProperty; validationProperty
- Range [ owl:someValuesFrom bdqffdq:hasDataQualityDimension ]

********************

#### hasEnhancement

- Name: bdqffdq:hasEnhancement
- Definition: The bdqffdq:Enhancement that describes how a bdqffdq:Amendment may propose changes to improve data quality.
- SubClass Of: amendmentProperty
- Range [ owl:someValuesFrom bdqffdq:hasEnhancement ]

********************

#### hasInformationElement

- Name: bdqffdq:hasInformationElement
- Definition: Describes the bdqffdq:InformationElements assessed by a bdqffdq:DataQualityNeed.
- SubClass Of: amendmentProperty; issueProperty; measurementProperty; validationProperty
- Range bdqffdq:InformationElement

********************

#### hasParameter

- Name: bdqffdq:hasParameter
- Definition: Relates a bdqffdq:Argument to a bdqffdq:Parameter.
- Range bdqffdq:Parameter

********************

#### hasResourceType

- Name: bdqffdq:hasResourceType
- Definition: The bdqffdq:ResourceType to which a bdqffdq:DataQualityNeed applies.

********************

#### hasResponseQualifier

- Name: bdqffdq:hasResponseQualifier
- Definition: ResponseQualifier object asserted by an Assertion.
- SubClass Of: reportProperty

********************

#### hasResponseResult

- Name: bdqffdq:hasResponseResult
- Definition: The bdqffdq:ResponseResult object asserted by a bdqffdq:Assertion.
- SubClass Of: reportProperty

********************

#### hasResponseStatus

- Name: bdqffdq:hasResponseStatus
- Definition: The bdqffdq:ResponseStatus object asserted by a bdqffdq:Assertion.
- SubClass Of: reportProperty

********************

#### hasSpecification

- Name: bdqffdq:hasSpecification
- Definition: Relates a bdqffdq:Method to a bdqffdq:Specification.
- Range [ owl:someValuesFrom bdqffdq:hasSpecification ]

********************

#### hasUseCase

- Name: bdqffdq:hasUseCase
- Definition: Relates a bdqffdq:Policy to a bdqffdq:UseCase.
- Range [ owl:someValuesFrom bdqffdq:hasUseCase ]

********************

#### implementedBy

- Name: bdqffdq:implementedBy
- Definition: The bdqffdq:Mechanism that provides a bdqffdq:Implementation
- Range [ owl:someValuesFrom bdqffdq:implementedBy ]

********************

#### improvedBy

- Name: bdqffdq:improvedBy
- Definition: The bdqffdq:ImprovementTarget that would have data quality improved by bdqffdq:Assertions resulting from a bdqffdq:Amendment.
- Range [ owl:someValuesFrom bdqffdq:improvedBy ]

********************

#### includedInPolicy

- Name: bdqffdq:includedInPolicy
- Definition: Assserts that a bdqffdq:DataQualityNeed is part of a bdqffdq:Policy.

********************

#### issueProperty

- Name: bdqffdq:issueProperty
- Definition: Category of object properties that apply to bdqffdq:Issues.

********************

#### measurementProperty

- Name: bdqffdq:measurementProperty
- Definition: Category of object properties that apply to bdqffdq:Measures.

********************

#### producesAssertion

- Name: bdqffdq:producesAssertion
- Definition: Connects an entity with a bdqffdq:Assertion that the entity created.

********************

#### reportProperty

- Name: bdqffdq:reportProperty
- Definition: Category of object properties that apply to bdqffdq:Assertions.

********************

#### targetedIssue

- Name: bdqffdq:targetedIssue
- Definition: A bdqffdq:Issue for which the data conformance with a bdqffdq:NeedConcept may be improved by accepting proposals from a bdqffdq:Amendment via a bdqffdq:ImprovementTarget.
- Range [ owl:someValuesFrom bdqffdq:targetedIssue ]

********************

#### targetedMeasure

- Name: bdqffdq:targetedMeasure
- Definition: A bdqffdq:Measure for which the data conformance with a bdqffdq:NeedConcept may be improved by accepting proposals from a bdqffdq:Amendment via a bdqffdq:ImprovementTarget.
- Range [ owl:someValuesFrom bdqffdq:targetedMeasure ]

********************

#### targetedValidation

- Name: bdqffdq:targetedValidation
- Definition: A bdqffdq:Validation for which the data conformance with a bdqffdq:NeedConcept may be improved by accepting proposals from a bdqffdq:Amendment via a bdqffdq:ImprovementTarget.
- SubClass Of: http://www.w3.org/2002/07/owl#topObjectProperty
- Range [ owl:someValuesFrom bdqffdq:targetedValidation ]

********************

#### usesSpecification

- Name: bdqffdq:usesSpecification
- Definition: The bdqffdq:Specification that a bdqffdq:Implementation implements.
- Range [ owl:someValuesFrom bdqffdq:usesSpecification ]

********************

#### validationProperty

- Name: bdqffdq:validationProperty
- Definition: Category of object properties that apply to bdqffdq:Validations.

********************

### 5.3 DataProperty terms (normative)
#### hasAuthoritiesDefaults

- Name: bdqffdq:hasAuthoritiesDefaults
- Definition: Text describing bdq:sourceAuthorities and bdqffdq:Parameters with their default values to attach to a bdqffdq:Specification to further specify the behavior described in the bdqffdq:hasExpectedResponse.
- Range xsd:string

********************

#### hasDateLastUpdated

- Name: bdqffdq:hasDateLastUpdated
- Definition: Date of the most recent dcterms:issued for this class with a change that would be pertinent to a bdqffdq:Implementation.
- Range xsd:date

********************

#### hasExpectedResponse

- Name: bdqffdq:hasExpectedResponse
- Definition: Text describing the logic to be followed by a bdqffdq:Implementation of a bdqffdq:Specification specifying the values of bdqffdq:ResponseStatus and bdqffdq:ResponseResults that should be produced from the evaluation of input bdqffdq:InformationElements.
- Range xsd:string

********************

#### hasResponseComment

- Name: bdqffdq:hasResponseComment
- Definition: Free text describing the bdqffdq:Assertion made in the response and why that conclusion was reached.
- Range xsd:string

********************

#### hasResponseResultValue

- Name: bdqffdq:hasResponseResultValue
- Definition: Data property carrying the value of a bdqffdq:Assertion when the value is not an object.

********************

### 5.4 NamedIndividual terms (normative)
#### MultiRecord

- Name: bdqffdq:MultiRecord
- Type: bdqffdq:ResourceType
- Definition: A set of one or more bdqffdq:SingleRecords.

********************

#### SingleRecord

- Name: bdqffdq:SingleRecord
- Type: bdqffdq:ResourceType
- Definition: A single entity comprised of encoded data with a defined structure that contains one instance of a core concept from the perspective of bdqffdq:InformationElements assessed for a bdqffdq:DataQualityNeed.

********************

#### COMPLETE

- Name: bdqffdq:COMPLETE
- Type: bdqffdq:ResponseResult
- DifferentFrom: bdqffdq:NOT_COMPLETE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Measure that asserts that data are present and sufficiently comprehensive for use.

********************

#### IS_ISSUE

- Name: bdqffdq:IS_ISSUE
- Type: bdqffdq:ResponseResult
- DifferentFrom: bdqffdq:NOT_ISSUE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue indicating that the data do not have sufficient quality for a use.

********************

#### IS_ISSUE

- Name: bdqffdq:IS_ISSUE
- Type: bdqffdq:ResponseResult
- DifferentFrom: bdqffdq:POTENTIAL_ISSUE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue indicating that the data do not have sufficient quality for a use.

********************

#### NOT_COMPLETE

- Name: bdqffdq:NOT_COMPLETE
- Type: bdqffdq:ResponseResult
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Measure which asserts that data are not present or are not sufficiently comprehensive for a use.

********************

#### NOT_ISSUE

- Name: bdqffdq:NOT_ISSUE
- Type: bdqffdq:ResponseResult
- DifferentFrom: bdqffdq:POTENTIAL_ISSUE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue where no potential problems were detected.

********************

#### POTENTIAL_ISSUE

- Name: bdqffdq:POTENTIAL_ISSUE
- Type: bdqffdq:ResponseResult
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue that indicates that the data may not have sufficient quality for a use. The user will need to evaluate if the data are fit for their particular use or not.

********************

#### AMENDED

- Name: bdqffdq:AMENDED
- Type: bdqffdq:ResponseStatus
- DifferentFrom: bdqffdq:NOT_AMENDED
- Definition: A bdqffdq:ResponseStatus used to indicate that a bdqffdq:hasResponseResultValue from a bdqffdq:Amendment contains a proposed change.

********************

#### NOT_AMENDED

- Name: bdqffdq:NOT_AMENDED
- Type: bdqffdq:ResponseStatus
- Definition: A bdqffdq:ResponseStatus used to indicate that a bdqffdq:Amendment proposed no change.

********************

#### RUN_HAS_RESULT

- Name: bdqffdq:RUN_HAS_RESULT
- Type: bdqffdq:ResponseStatus
- Definition: A bdqffdq:ResponseStatus used to indicate that that a result was correctly generated.

********************



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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
