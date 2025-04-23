<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness For Use Framework Ontology List of Terms

**Title**<br>
Fitness For Use Framework Ontology List of Terms

**Date version issued**<br>
2025-04-11

**Date created**<br>
2025-04-11

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqffdq

**This version**<br>
<http://rs.tdwg.org/bdqffdq/terms/2025-04-11>

**Latest version**<br>
<http://rs.tdwg.org/bdqffdq/terms/>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
This document is a reference for the BDQ Core Standard, documenting vocabulary values in the Fitness For Use Framework Ontology, excluding additional axioms.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/terms/2025-04-11>

**Comment**<br>
Draft Standard for Review

## Table of Contents ##
[1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Audience](#12-audience)
  - [1.3 Associated Documents](#13-associated-documents)
    - [1.3.1 Term List Distributions](#131-term-list-distributions)
  - [1.4 Status of the content of this document](#14-status-of-the-content-of-this-document)
  - [1.5 RFC 2119 key words](#15-rfc-2119-key-words)
  - [1.6 Namespace abbreviations](#16-namespace-abbreviations)
  - [1.7 Key to Vocabulary Terms](#17-key-to-vocabulary-terms)

[2 Use of Terms (normative)](#2-use-of-terms-normative)

[3 Term index (non-normative)](#3-term-index-non-normative)
  - [3.1 Alphabetical Index of classes](#31-alphabetical-index-of-classes)
  - [3.2 Alphabetical Index of object properties](#32-alphabetical-index-of-object-properties)
  - [3.3 Alphabetical Index of data properties](#33-alphabetical-index-of-data-properties)
  - [3.4 Alphabetical Index of named individuals](#34-alphabetical-index-of-named-individuals)

[4 Vocabulary](#4-vocabulary)
  - [4.1 Class terms](#41-class-terms)
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
  - [4.2 ObjectProperty terms](#42-objectproperty-terms)
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
  - [4.3 DataProperty terms](#43-dataproperty-terms)
    - [hasAuthoritiesDefaults](#hasauthoritiesdefaults)
    - [hasDateLastUpdated](#hasdatelastupdated)
    - [hasExpectedResponse](#hasexpectedresponse)
    - [hasResponseComment](#hasresponsecomment)
    - [hasResponseResultValue](#hasresponseresultvalue)
  - [4.4 NamedIndividual terms](#44-namedindividual-terms)
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

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to provide the official term list for the `bdqffdq:` vocabulary, which defines the ontology elements used in the Biodiversity Data Quality Fitness for Use Framework. This includes classes, object properties, data properties, and named individuals that collectively support the semantic description of BDQ Core Tests and related quality constructs.

This document presents a human-readable view of the vocabulary and follows the TDWG Standards Documentation Specification. It does not include additional axioms, implementation guidance, or usage recommendations — those are addressed in complementary documentation and the [Fitness For Use Framework Ontology Vocabulary Extension](docs/extension/bdqffdq/index.md).

### 1.2 Audience

This document is intended for technical users who need to reference the `bdqffdq:` vocabulary in detail. It is particularly useful for:

- Ontology developers integrating BDQ Core concepts into semantic systems
- Data quality analysts and system implementers interpreting or expressing BDQ Test structures using RDF/OWL
- Standards developers needing access to term-level details when aligning or extending the BDQ Core framework.

Familiarity with RDF, OWL, and the structure of the BDQ Core Tests is recommended.

### 1.3 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality (BDQ) Core](../../index.md) page, which lists the parts of the standard.

#### 1.3.1 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdqffdq/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdqffdq/index.md | This file | 
| OWL Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.4 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.7 Key to Vocabulary Terms](#17-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.6 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

### 1.7 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Abstract Information Element |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | A bdqffdq:InformationElement described in abstract terms and not linked with any concrete terms. |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Such bdqffdq:InformationElements as DATE and DAY are abstract, they could reference any representation of those concepts. In contrast, dwc:eventDate and dwc:day can be linked to concrete bdqffdq:ActedUponInformationElements or bdqffdq:ConsultedInformationElements. |
| Type (rdf:type) | normative | The subject is an instance of a class. | [http://www.w3.org/2002/07/ owl#Class](http://www.w3.org/2002/07/owl#Class) |


## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqffdq:` namespace MUST use the Term IRI (e.g., `http://rs.tdwg.org/bdq/bdqffdq/InformationElement`) or Term Qualified name (e.g., `bdqffdq:InformationElement`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `InformationElement`) MAY be used. In a purely human context a Label (e.g., `Information Element`) MAY be used.

## 3 Term index (non-normative)

- [Classes](#41-Class-terms)
- [Object Properties](#42-ObjectProperty-terms)
- [Data Properties](#43-DataProperty-terms)
- [Named Individuals](#44-NamedIndividual-terms)

### 3.1 Alphabetical Index of classes

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
### 3.2 Alphabetical Index of object properties

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
### 3.3 Alphabetical Index of data properties

[hasArgumentValue](#hasArgumentValue)
[hasAuthoritiesDefaults](#hasAuthoritiesDefaults)
[hasDateLastUpdated](#hasDateLastUpdated)
[hasExpectedResponse](#hasExpectedResponse)
[hasResponseComment](#hasResponseComment)
[hasResponseResultValue](#hasResponseResultValue)
### 3.4 Alphabetical Index of named individuals

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

## 4 Vocabulary

### 4.1 Class terms
#### AbstractInformationElement

- Name: bdqffdq:AbstractInformationElement
- Preferred Label: Abstract Information Element
- Definition: A bdqffdq:InformationElement described in abstract terms and not linked with any concrete terms.
- SubClass Of: InformationElement
- Comments: Such bdqffdq:InformationElements as DATE and DAY are abstract, they could reference any representation of those concepts. In contrast, dwc:eventDate and dwc:day can be linked to concrete bdqffdq:ActedUponInformationElements or bdqffdq:ConsultedInformationElements.

********************

#### ActedUpon

- Name: bdqffdq:ActedUpon
- Preferred Label: Acted Upon
- Definition: A bdqffdq:InformationElement, expressed in concrete terms, about which a bdqffdq:DataQualityNeed expresses bdqffdq:Assertions about the data quality in that bdqffdq:InformationElement.
- SubClass Of: InformationElement
- Comments: A bdqffdq:InformationElement to which a bdqffdq:ResponseResult applies.

********************

#### Amendment

- Name: bdqffdq:Amendment
- Preferred Label: Amendment
- Definition: A bdqffdq:DataQualityNeed that expresses how proposals may be made to improve the fitness for use of data.
- SubClass Of: AmendmentConcept; DataQualityNeed
- Comments: ContextualizedEnhacement in the original framework. Describes an instance of a bdqffdq:Enhancement in the context of the associated bdqffdq:InformationElements from a controlled vocabulary (fields bdqffdq:ActedUpon or bdqffdq:Consulted), and a bdqffdq:ResourceType of bdqffdq:SingleRecord or bdqffdq:MultiRecord.  
Describes a proposal for a bdqffdq:Enhancement of original data, which if accepted, would improve the quality of the data for a use. For example: 'Recommends valid value for taxon name in a SingleRecord.'  
bdqffdq:Amendments may describe proposed changes to data values, or proposed changes to processes for the production and manipulation of data, for example, a bdqffdq:Amendment on a bdqffdq:SingleRecord may provide bdqffdq:Criteria for proposing that dwc:decimalLatitude and dwc:decimalLongitude are transposed in that record. Similarly, a bdqffdq:Amendment on a bdqffdq:MultiRecord may provide bdqffdq:Critera for proposing that all dwc:decimalLatitudes and dwc:decimalLongitudes from a data source have been transposed, and the mapping of data values to transport terms should be changed.  
A bdqffdq:Amendment is the bdqffdq:DataQualityNeed that parallels a bdqffdq:AmendmentMethod in the Solutions layer (see Figure 3 in Veiga et al., 2017), and a bdqffdq:AmendmentAssertion in the Report layer (see Figure 3 in Veiga et al., 2017).  
AM = { am | am = < ie, e, rt >, ie ∈ IE, e ∈ E ⋀ rt ∈ RT }

********************

#### AmendmentAssertion

- Name: bdqffdq:AmendmentAssertion
- Preferred Label: Amendment Assertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation evaluating a bdqffdq:Amendment supporting a particular bdqffdq:DataQualityNeed to improve a particular bdqffdq:DataResource.
- SubClass Of: AmendmentConcept; Assertion
- Comments: The bdqffdq:AmendmentAssertion type is a Report layer concept (see Figure 3 in Veiga et al., 2017) that describes the results of the execution of a Test that performs a bdqffdq:AmendmentMethod following a bdqffdq:Specification to propose changes based on a bdqffdq:Amendment.   
A bdqffdq:Amendment is expected to carry a bdqffdq:ResponseStatus result that includes a status bdqffdq:FILLED_IN or bdqffdq:AMENDED, as well as a bdqffdq:ResponseResult that asserts proposed changes to values from the original data.  
DQA(dr) = {dqa | dqa = < am, s, m, r >, am ∈ AM, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

********************

#### AmendmentMethod

- Name: bdqffdq:AmendmentMethod
- Preferred Label: Amendment Method
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Amendment to its bdqffdq:Specifications.
- SubClass Of: AmendmentConcept; DataQualityMethod
- Comments: The bdqffdq:AmendmentMethod is a bdqffdq:DataQualityMethod describing the relationship between a bdqffdq:Specification (technical description of a Test) and a bdqffdq:Amendment (a bdqffdq:Enhancement in the context of bdqffdq:ResourceType (bdqffdq:SingleRecord or bdqffdq:MultiRecord) and associated bdqffdq:InformationElements).  
EM(am) = {s | s ⊂ S ⋀ am ∈ AM}

********************

#### AmendmentPolicy

- Name: bdqffdq:AmendmentPolicy
- Preferred Label: Amendment Policy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Amendments.
- SubClass Of: AmendmentConcept; Policy
- Comments: A data quality Need layer concept (see Figure 3 in Veiga et al., 2017) that describes how a bdqffdq:Amendment relates to a bdqffdq:UseCase. This relationship defines which bdqffdq:Amendments are supported by a given bdqffdq:UseCase.  
EP(u) = {am | am ⊂ AM ⋀ u ∈ U }

********************

#### Argument

- Name: bdqffdq:Argument
- Preferred Label: Argument
- Definition: A value that, when provided to a Test bdqffdq:Specification to replace a bdqffdq:Parameter changes the behavior of the Test in a defined manner.
- SubClass Of: SolutionsConcept
- Comments: The bdqffdq:Argument is an Actual Parameter, for which a bdqffdq:Parameter is the corresponding Formal Parameter. An extension to the original fitness for use framework as described in Veiga et al., 2017.

********************

#### Assertion

- Name: bdqffdq:Assertion
- Preferred Label: Assertion
- Definition: A bdqffdq:ReportConcept expressing a statement about a data quality bdqffdq:Assertion following a bdqffdq:Specification produced by a bdqffdq:Implementation pertaining to a bdqffdq:DataResource.
- SubClass Of: ReportConcept
- Comments: The bdqffdq:Assertion type is the bdqffdq:FundamentalConcept that makes up a bdqffdq:DataQualityReport. A bdqffdq:Assertion can be any one of four types (represented as subclasses), bdqffdq:Validation, bdqffdq:Issue, bdqffdq:Measure, and bdqffdq:Amendment. The bdqffdq:Assertion concept consists of a bdqffdq:Specification (the technical description of a performed Test), a bdqffdq:DataResource (initial values of input data expressed in terms of a controlled vocabulary), the bdqffdq:Mechanism (external service, actor, or code that performs the Test), and a form of result.

********************

#### Consulted

- Name: bdqffdq:Consulted
- Preferred Label: Acted Upon
- Definition: A bdqffdq:InformationElement, expressed in concrete terms, about which a bdqffdq:DataQualityNeed examines in order to expresses bdqffdq:Assertions about the data quality in another bdqffdq:InformationElement.
- SubClass Of: InformationElement
- Comments: A bdqffdq:InformationElement the content of which is examined to assert a result on one or more other bdqffdq:InformationElements.

********************

#### Criterion

- Name: bdqffdq:Criterion
- Preferred Label: Criterion
- Definition: Rule against which data are evaluated for conformance to quality bdqffdq:Criteria.
- SubClass Of: FundamentalConcept; NeedConcept
- Comments: General statement, for example, 'In a controlled vocabulary.' Composed with both bdqffdq:Validations and bdqffdq:Issues.

********************

#### DataQualityDimension

- Name: bdqffdq:DataQualityDimension
- Preferred Label: Data Quality Dimension
- Definition: An aspect of data quality.
- SubClass Of: FundamentalConcept; NeedConcept
- Comments: Describes the aspect of data quality (accuracy, precision, completeness, etc.) that a Test examines. For example, [precision] in [coordinate precision of SingleRecords]. In the original framework, only related to Measures, here may be related to any bdqffdq:DataQualityNeed.

********************

#### DataQualityMethod

- Name: bdqffdq:DataQualityMethod
- Preferred Label: Data Quality Method
- Definition: A bdqffdq:SolutionsConcept that relates a bdqffdq:DataQualityNeed to a bdqffdq:Specification.
- SubClass Of: SolutionsConcept
- Comments: A bdqffdq:DataQualityMethod is an associative entity that allows bdqffdq:Specifications or data quality Tests to be reused by supporting a many-to-many relationship between the two.

********************

#### DataQualityNeed

- Name: bdqffdq:DataQualityNeed
- Preferred Label: Data Quality Need
- Definition: A bdqffdq:NeedConcept that expresses what bdqffdq:Assertions may be made about data with respect to fitness for use.
- SubClass Of: NeedConcept
- Comments: Subtypes of bdqffdq:DataQualityNeed are the Test Types (Validation, Issue, Measure, and Amendment). The bdqffdq:DataQualityNeed appoximates the informal concept of a Test as used in BDQ Core.

********************

#### DataQualityProfile

- Name: bdqffdq:DataQualityProfile
- Preferred Label: Data Quality Profile
- Definition: A bdqffdq:NeedConcept expressing the composition of bdqffdq:Policies to satisfy a bdqffdq:UseCase.
- SubClass Of: NeedConcept
- Comments: The bdqffdq:DataQualityProfile is a data quality Need layer concept (see Figure 3 in Veiga et al., 2017) describing the bdqffdq:UseCases that make up a data quality operation such as the behavior of a single actor or workflow producing the relevant bdqffdq:Assertions.  
DQP (u) = {dqp | dqp = mp(u) ⋃ vp(u) ⋃ ep(u), mp ∈ MP , vp ∈ VP , ep ∈ EP ⋀ u ∈ U }

********************

#### DataQualityReport

- Name: bdqffdq:DataQualityReport
- Preferred Label: Data Quality Report
- Definition: A bdqffdq:ReportConcept comprising a set of data quality bdqffdq:Assertions.
- SubClass Of: ReportConcept
- Comments: A bdqffdq:DataQualityReport consists of a set of bdqffdq:Assertions (bdqffdq:ValidationAssertions, bdqffdq:IssueAssertions, bdqffdq:MeasureAssertions, and bdqffdq:AmendmentAssertions) that represent the output of a workflow/actor run. These bdqffdq:Assertions form an account of the fitness for use of a tested data set for a specified bdqffdq:UseCase, as produced by a bdqffdq:Mechanism.

********************

#### DataResource

- Name: bdqffdq:DataResource
- Preferred Label: Data Resource
- Definition: An owl:Thing to which a data quality bdqffdq:Assertion applies.
- SubClass Of: ReportConcept
- Comments: Describes a bdqffdq:DataResource containing terms from a vocabulary such as Darwin Core that can be related to bdqffdq:InformationElements, and represents the original values of the data operated on by a bdqffdq:Assertion Test (e.g., an instance of dwc:Occurrence). Ideally, bdqffdq:DataResources have persistent GUIDs.  
A bdqffdq:DataResource could be the oa:target of a oa:Annotation of which a bdqffdq:Assertion is the oa:body.  
DR = { dr | dr = < id, rt, v >, id ∈ I D, rt ∈ RT , (rt = sr ⋁ rt = ds) ⋀ v ∈ V }

********************

#### Enhancement

- Name: bdqffdq:Enhancement
- Preferred Label: Enhancement
- Definition: Description of a means by which data could be improved.
- SubClass Of: AmendmentConcept; FundamentalConcept; NeedConcept
- Comments: A general statement about improvement, for example, 'Recommend replacement value from a controlled vocabulary'.

********************

#### FundamentalConcept

- Name: bdqffdq:FundamentalConcept
- Preferred Label: Fundamental Concept
- Definition: Category of fitness for use concepts that are not derived by composition with other concepts.
- Comments: Contrast with derived concepts, which are compositions of two or more bdqffdq:FundamentalConcepts, see Veiga et al., 2017. Derived concepts can be organized by Test type into bdqffdq:ValidationConcept, bdqffdq:IssueConcept, bdqffdq:MeasurementConcept, or bdqffdq:AmendmentConcept. Derived concepts can also be organized by framework layer into bdqffdq:NeedConcept, bdqffdq:SolutionsConcept, and bdqffdq:ReportConcept (see Figure 3 in Veiga et al., 2017).

********************

#### Implementation

- Name: bdqffdq:Implementation
- Preferred Label: Implementation
- Definition: A bdqffdq:SolutionsConcept that describes the portion of a bdqffdq:Mechanism that carries out the proccess described in a particular bdqffdq:Specification.
- SubClass Of: SolutionsConcept
- Comments: A bdqffdq:Implementation describes the relationship between a bdqffdq:Specification (technical description of a Test) and the bdqffdq:Mechanism that implements it.  
I (s) = {m | m ⊂ M ⋀ s ∈ S}

********************

#### ImprovementTarget

- Name: bdqffdq:ImprovementTarget
- Preferred Label: Improvement Target
- Definition: A specific bdqffdq:DataQualityNeed that a specific bdqffdq:Amendment is intended to improve.
- SubClass Of: NeedConcept
- Comments: A bdqffdq:ImprovementTarget describes which bdqffdq:Validations, bdqffdq:Issues, and bdqffdq:Measures are improved by a bdqffdq:Amendment. The bdqffdq:ImprovementTarget includes relationships between a bdqffdq:Amendment and one or more bdqffdq:Validations or bdqffdq:Measures.  
IT(am) = {me ⋃ va | me ∈ ME, va ∈ VA ⋀ am ∈ AM}

********************

#### InformationElement

- Name: bdqffdq:InformationElement
- Preferred Label: Information Element
- Definition: A portion of data with which a bdqffdq:DataQualityNeed is concerned.
- SubClass Of: FundamentalConcept
- Comments: A bdqffdq:InformationElement identifies a portion of data to which a Test pertains. A bdqffdq:InformationElement can be represented as a single or composite element that consists of one or more terms from a controlled vocabulary (fields bdqffdq:ActedUpon or bdqffdq:Consulted by a bdqffdq:Assertion Test) that identifies concepts in data relevant to a bdqffdq:UseCase. An abstraction or a concrete term that represents relevant content (e.g., coordinates; dwc:decimalLatitude, dwc:decimalLongitude).

********************

#### Issue

- Name: bdqffdq:Issue
- Preferred Label: Issue
- Definition: A bdqffdq:DataQualityNeed that expresses how quality problems may be identified in data.
- SubClass Of: DataQualityNeed; IssueConcept
- Comments: Added to the original framework. Inverse of ContextualizedCriterion in the original framework. Describes an instance of the bdqffdq:IssueConcept in terms of the associated bdqffdq:InformationElements from a controlled vocabulary (fields bdqffdq:ActedUpon or bdqffdq:Consulted), and a bdqffdq:ResourceType of bdqffdq:SingleRecord or bdqffdq:MultiRecord. Describes bdqffdq:Criteria by which data that lack quality for some purpose may be identified. A bdqffdq:Issue is phrased in a negative sense, and approximates an inverse of a bdqffdq:Validation. A bdqffdq:Issue identifies data that lack or may lack quality. A bdqffdq:Issue may flag a bdqffdq:POTENTIAL_ISSUE that would need further review to determine if the data have quality for some purpose. If the conditions described by a bdqffdq:Issue are identified by a Test, the bdqffdq:ResponseResult will be either bdqffdq:IS_ISSUE or bdqffdq:POTENTIAL_ISSUE, if no bdqffdq:Issue is found with the data, the bdqffdq:ResponseResult will be bdqffdq:NOT_ISSUE. The term bdqffdq:NOT_ISSUE, unlike bdqffdq:COMPLIANT for a bdqffdq:Validation, does not assert that data are fit for some purpose. A bdqffdq:Issue is the bdqffdq:DataQualityNeed concept that parallels a bdqffdq:IssueMethod in the Solutions layer (see Figure 3 in Veiga et al., 2017), and a bdqffdq:IssueAssertion in the Report layer (see Figure 3 in Veiga et al., 2017).  
IS = { is | is = < ie, c, rt >, ie ∈ IE, c ∈ ∁C ⋀ rt ∈ RT }

********************

#### IssueAssertion

- Name: bdqffdq:IssueAssertion
- Preferred Label: Issue Assertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation evaluating a bdqffdq:Issue for a particular bdqffdq:DataQualityNeed in a particular bdqffdq:DataResource.
- SubClass Of: Assertion; IssueConcept
- Comments: The bdqffdq:DataQualityReport concept describing the result of a Test in the negative (i.e., identifying the potential absence of data quality).   
If a problem was found, the bdqffdq:ResponseResult is expected to carry a value of bdqffdq:IS_ISSUE, if a potential problem was found that requires human review, the bdqffdq:ResponseResult is expected to be bdqffdq:POTENTIAL_ISSUE, otherwise if the bdqffdq:ResponseStatus is bdqffdq:RUN_HAS_RESULT, the bdqffdq:ResponseResult is expected to be bdqffdq:NOT_ISSUE.

********************

#### IssueConcept

- Name: bdqffdq:IssueConcept
- Preferred Label: Issue Concept
- Definition: A term involved in flagging problems or potential problems in assessment of data quality that would or might prevent the data from meeting an expressed bdqffdq:DataQualityNeed.
- Comments: A bdqffdq:Issue term is expressed in a negative sense, it identifies data that do not or may not conform to bdqffdq:DataQualityNeeds.

********************

#### IssueMethod

- Name: bdqffdq:IssueMethod
- Preferred Label: Issue Method
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Issue to its bdqffdq:Specifications.
- SubClass Of: DataQualityMethod; IssueConcept
- Comments: A bdqffdq:IssueMethod is a data quality Solutions layer concept (see Figure 3 in Veiga et al., 2017) describing the relationship between a bdqffdq:Specification (technical description of a Test) and a bdqffdq:Issue (a bdqffdq:Criterion in the context of bdqffdq:ResourceType (bdqffdq:SingleRecord or bdqffdq:MultiRecord) and associated bdqffdq:InformationElements).

********************

#### IssuePolicy

- Name: bdqffdq:IssuePolicy
- Preferred Label: Issue Policy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Issues.
- SubClass Of: IssueConcept; Policy
- Comments: A bdqffdq:IssuePolicy is a data quality Need layer concept (see Figure 3 in Veiga et al., 2017) that describes how a bdqffdq:Issue relates to a bdqffdq:UseCase. This relationship defines which bdqffdq:Issues are supported by a given bdqffdq:UseCase.

********************

#### Measure

- Name: bdqffdq:Measure
- Preferred Label: Measure
- Definition: A bdqffdq:DataQualityNeed that expresses how the fitness of data for some use may be measured.
- SubClass Of: DataQualityNeed; MeasurementConcept
- Comments: ContextualizedDimension in the original framework. Describes an instance of the bdqffdq:MeasurementConcept in terms of the associated bdqffdq:InformationElements from a controlled vocabulary (fields bdqffdq:ActedUpon or bdqffdq:Consulted), and a bdqffdq:ResourceType of bdqffdq:SingleRecord or bdqffdq:MultiRecord.   
Describes the bdqffdq:Criteria for measuring an aspect of data quality related to a bdqffdq:DataQualityNeed. May be bdqffdq:Criteria for determining that data are bdqffdq:COMPLETE or bdqffdq:NOT_COMPLETE, or may be bdqffdq:Criteria for asserting a numeric bdqffdq:Measure. The bdqffdq:COMPLETE and bdqffdq:NOT_COMPLETE bdqffdq:Measures are fundamental to data quality control, as a set of data is filtered to the subset of data that have quality for some need if all records are bdqffdq:COMPLETE for all pertinent bdqffdq:Measures.  
A bdqffdq:Measure is the bdqffdq:DataQualityNeed concept that parallels a bdqffdq:MeasurementMethod in the Solutions layer (see Figure 3 in Veiga et al., 2017), and a bdqffdq:MeasurementAssertion in the Report layer (see Figure 3 in Veiga et al., 2017).  
ME = { me | me =< ie, d, rt >, ie ∈ IE, d ∈ D ⋀ rt ∈ RT }  
also acceptable bdqffdq:Measure  
AM(me) = {va | me ∈ C D ⋀ va ⊂ C C}

********************

#### MeasurementAssertion

- Name: bdqffdq:MeasurementAssertion
- Preferred Label: Measurement Assertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation measuring a particular bdqffdq:DataQualityNeed in a particular bdqffdq:DataResource.
- SubClass Of: Assertion; MeasurementConcept
- Comments: A bdqffdq:MeasurementAssertion is a Report layer concept (see Figure 3 in Veiga et al., 2017) that describes the results of the execution of a Test that performs a bdqffdq:MeasurementMethod following a bdqffdq:Specification to assess a data quality bdqffdq:Measure.   
A MeasurementAssertion is expected to carry a bdqffdq:ResponseResult of bdqffdq:COMPLETE or bdqffdq:NOT_COMPLETE or a numeric measured value (e.g., a bdqffdq:Measure of a dwc:eventDate duration in seconds).  
DQM(dr) = {dqm | dqm =< me, s, m, r >, me ∈ ME, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

********************

#### MeasurementMethod

- Name: bdqffdq:MeasurementMethod
- Preferred Label: Measurement Method
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Measure to its bdqffdq:Specifications.
- SubClass Of: DataQualityMethod; MeasurementConcept
- Comments: A bdqffdq:MeasurementMethod is a data quality Solutions layer concept (see Figure 3 in Veiga et al., 2017) describing the relationship between a bdqffdq:Specification (technical description of a Test) and a bdqffdq:Measurement (a bdqffdq:Dimension in the context of bdqffdq:ResourceType (bdqffdq:SingleRecord or bdqffdq:MultiRecord) and associated bdqffdq:InformationElements).  
MM(me) = {s | s ⊂ S ⋀ me ∈ ME}

********************

#### MeasurementPolicy

- Name: bdqffdq:MeasurementPolicy
- Preferred Label: Measurement Policy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Measures.
- SubClass Of: MeasurementConcept; Policy
- Comments: A bdqffdq:MeasurementPolicy is a data quality Need layer concept (see Figure 3 in Veiga et al., 2017) that describes how a bdqffdq:Measurement relates to a bdqffdq:UseCase. This relationship defines which bdqffdq:Measures are supported by a given bdqffdq:UseCase.  
MP(u) = {me | me ⊂ ME ⋀ u ∈ U }

********************

#### Mechanism

- Name: bdqffdq:Mechanism
- Preferred Label: Mechanism
- Definition: An entity that can execute bdqffdq:DataQualityMethods.
- SubClass Of: FundamentalConcept; SolutionsConcept
- Comments: A bdqffdq:Mechanism may produce bdqffdq:DataQualityReports as products.  
A bdqffdq:Mechanism describes the entity that performs a bdqffdq:Assertion Test (code, external service, actor, etc.). Tied to a bdqffdq:Specification via the concept of a bdqffdq:Implementation.

********************

#### NeedConcept

- Name: bdqffdq:NeedConcept
- Preferred Label: Need Concept
- Definition: A concept that expresses an aspect of a bdqffdq:DataQualityNeed.
- Comments: Category of concepts forming the Need layer of the fitness for use framework (see Figure 3 in Veiga et al., 2017).

********************

#### Parameter

- Name: bdqffdq:Parameter
- Preferred Label: Parameter
- Definition: A placeholder for a value that, when provided to a Test bdqffdq:Specification changes the behavior of the Test in a defined manner.
- SubClass Of: SolutionsConcept
- Comments: A bdqffdq:Parameter is a Formal Parameter for which an bdqffdq:Argument is an Actual Parameter that replaces it to determine the behavior of a bdqffdq:Specification. An extension to the original fitness for use framework as described in Veiga et al., 2017.

********************

#### Policy

- Name: bdqffdq:Policy
- Preferred Label: Policy
- Definition: The set of bdqffdq:DataQualityNeeds for a bdqffdq:UseCase.
- SubClass Of: NeedConcept
- Comments: Composition of bdqffdq:DataQualityNeeds into a bdqffdq:UseCase.

********************

#### ReportConcept

- Name: bdqffdq:ReportConcept
- Preferred Label: Report Concept
- Definition: A concept concerning data quality expressed in a bdqffdq:DataQualityReport.
- Comments: Category of concepts forming the Report layer of the fitness for use framework (see Figure 3 in Veiga et al., 2017).

********************

#### ResourceType

- Name: bdqffdq:ResourceType
- Preferred Label: Resource Type
- Definition: Category of things that are data objects about which data quality bdqffdq:Assertions may be made.
- SubClass Of: FundamentalConcept
- Comments: The concept of bdqffdq:ResourceType has instances for bdqffdq:SingleRecord or bdqffdq:MultiRecord.

********************

#### ResponseQualifier

- Name: bdqffdq:ResponseQualifier
- Preferred Label: Response Qualifier
- Definition: A bdqffdq:ReportConcept to which additional bdqffdq:Assertions providing additional information beyond that of bdqffdq:ResponseResult from the execution of the bdqffdq:Specification of a bdqffdq:DataQualityNeed are attached.
- SubClass Of: ReportConcept
- Comments: Intended as an extension point for qualifying information about uncertainty or ambiguity.

********************

#### ResponseResult

- Name: bdqffdq:ResponseResult
- Preferred Label: Response.result
- Definition: A bdqffdq:ReportConcept to which controlled vocabulary bdqffdq:Assertions about the result of the execution of the bdqffdq:Specification of a bdqffdq:DataQualityNeed are attached.
- SubClass Of: ReportConcept
- Comments: For a bdqffdq:Validation, a bdqffdq:ResponseResult may be bdqffdq:COMPLIANT, or bdqffdq:NOT_COMPLIANT. For a bdqffdq:Measure, a bdqffdq:ResponseResult object may be bdqffdq:COMPLETE or bdqffdq:NOT_COMPLETE. For a bdqffdq:Issue, a bdqffdq:ResponseResult may be bdqffdq:IS_ISSUE, bdqffdq:POTENTIAL_ISSUE, or bdqffdq:NOT_ISSUE. A bdqffdq:Measure may also use a numeric data property. A bdqffdq:Amendment asserts a string data property.  
The bdqffdq:ResponseResult is represented as a value or a result object for bdqffdq:MeasureAsssertions, or just a result object for bdqffdq:ValidationAssertions or just values for changes proposed in bdqffdq:AmendmentAssertions.

********************

#### ResponseStatus

- Name: bdqffdq:ResponseStatus
- Preferred Label: Response.status
- Definition: A bdqffdq:ReportConcept expressing controlled vocabulary values about the exit state of an execution process of a data quality bdqffdq:Specification by a bdqffdq:Implementation.
- SubClass Of: ReportConcept
- Comments: The bdqffdq:ResponseStatus is metadata, indicating if data should be present in a bdqffdq:ResponseResult. Any bdqffdq:Assertion may have the values bdqffdq:INTERNAL_PREREQUISITES_NOT_MET or bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET, indicating that no value would be present in the accompanying bdqffdq:ResponseResult. Other values depend on the bdqffdq:Assertion type; bdqffdq:RUN_HAS_RESULT for a bdqffdq:Validation, bdqffdq:Issue or bdqffdq:Measure, and bdqffdq:FILLED_IN, bdqffdq:AMENDED, or bdqffdq:NOT_AMENDED for a bdqffdq:Amendment. Additional metadata qualifying the bdqffdq:Assertion in a bdqffdq:ResponseResult, such as statements of uncertainy or ambiguity may be placed in the bdqffdq:ResponseQualifier.

********************

#### SolutionsConcept

- Name: bdqffdq:SolutionsConcept
- Preferred Label: Solutions Concept
- Definition: A concept that expresses an aspect of a data quality solution.
- Comments: Category of concepts forming the Solutions layer of the fitness for use framework (see Figure 3 in Veiga et al., 2017). A bdqffdq:SolutionsConcept is a tool that evaluates data against bdqffdq:NeedConcepts and express conclusions in bdqffdq:DataQualityReports.

********************

#### Specification

- Name: bdqffdq:Specification
- Preferred Label: Specification
- Definition: A specific statement about how to evaluate a bdqffdq:DataQualityNeed.
- SubClass Of: FundamentalConcept; SolutionsConcept
- Comments: A bdqffdq:Specification is a technical description of a bdqffdq:Assertion Test. A bdqffdq:Specification is expected to have the following properties:  (1) bdqffdq:hasExpectedResponse and (2) bdqffdq:hasAuthoritiesDefaults.

********************

#### UseCase

- Name: bdqffdq:UseCase
- Preferred Label: Use Case
- Definition: A bdqffdq:NeedConcept expressing a purpose to which data are put for which the data must have quality for the result to have meaning and reliability.
- SubClass Of: FundamentalConcept; NeedConcept
- Comments: A bdqffdq:UseCase describes a data quality control use case. The bdqffdq:ValidationPolicies, bdqffdq:MeasurementPolicies and bdqffdq:AmendmentPolicies that make up a bdqffdq:UseCase define which bdqffdq:Assertions cover a given bdqffdq:UseCase. An example of a bdqffdq:UseCase could be 'Check for internal consistency of dates', with bdqffdq:ValidationPolicies for checking consistency between atomic date fields and a bdqffdq:Amendment such as 'eventDate filled in from verbatim'. A bdqffdq:UseCase is not the same as a use cases in the software engineering sense, it is a similar formal bdqffdq statement derived from analyis of user stories.

********************

#### Validation

- Name: bdqffdq:Validation
- Preferred Label: Validation
- Definition: A bdqffdq:DataQualityNeed that expresses how data may be evaluated for fitness for use.
- SubClass Of: DataQualityNeed; ValidationConcept
- Comments: ContextualizedCriterion in the original framework. Describes the bdqffdq:Criteria for determining compliance of data to fill a bdqffdq:DataQualityNeed. A description of a bdqffdq:Criterion applied to a bdqffdq:InformationElement for a bdqffdq:ResourceType. Describes an instance of a bdqffdq:Criterion in terms of the associated bdqffdq:InformationElements from a controlled vocabulary (fields bdqffdq:ActedUpon or bdqffdq:Consulted), and a bdqffdq:ResourceType of bdqffdq:SingleRecord or bdqffdq:MultiRecord.  
A bdqffdq:Validation is phrased in a positive sense. It identifies data which have quality for some need. For example, the value of dwc:basisOfRecord of bdqffdq:SingleRecords must be in the controlled vocabulary for dwc:basisOfRecord.  
A bdqffdq:Validation is the bdqffdq:DataQualityNeed that parallels a bdqffdq:ValidationMethod in the Solutions layer (see Figure 3 in Veiga et al., 2017), and a bdqffdq:ValidationAssertion in the Report layer (see Figure 3 in Veiga et al., 2017). A bdqffdq:ValidationAssertion may specify a result that is bdqffdq:COMPLIANT, where the data have quality, or bdqffdq:NOT_COMPLIANT, where the data lack quality for a bdqffdq:UseCase.  
VA = { va | va = < ie, c, rt >, ie ∈ IE, c ∈ C ⋀ rt ∈ RT }

********************

#### ValidationAssertion

- Name: bdqffdq:ValidationAssertion
- Preferred Label: Validation Assertion
- Definition: A bdqffdq:Assertion expressing the result of a bdqffdq:Implementation validating compliance with a particular bdqffdq:DataQualityNeed in a particular bdqffdq:DataResource.
- SubClass Of: Assertion; ValidationConcept
- Comments: The bdqffdq:ValidationAssertion is a Report layer concept (see Figure 3 in Veiga et al., 2017) that describes the results of the execution of a Test that performs a bdqffdq:ValidationMethod following a bdqffdq:Specification to assess the validity of some data with respect to the bdqffdq:Criteria of a bdqffdq:Validation.   
The bdqffdq:ValidationAssertion concept is expected to carry a bdqffdq:ResponseResult of bdqffdq:COMPLIANT or bdqffdq:NON_COMPLIANT.  
DQV(dr) = {dqv | dqv = < va, s, m, r >, va ∈ VA, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

********************

#### ValidationConcept

- Name: bdqffdq:ValidationConcept
- Preferred Label: Validation Concept
- Definition: A term involved in statements about the conformance of data to expressed bdqffdq:DataQualityNeeds.
- Comments: A bdqffdq:Validation term is expressed in a positive sense, it identifies data that conform to a bdqffdq:NeedConcept.

********************

#### ValidationMethod

- Name: bdqffdq:ValidationMethod
- Preferred Label: Validation Method
- Definition: A data quality bdqffdq:SolutionsConcept that relates a bdqffdq:Validation to its bdqffdq:Specifications.
- SubClass Of: DataQualityMethod; ValidationConcept
- Comments: A bdqffdq:ValidationMethod is a data quality Solutions layer concept (see Figure 3 in Veiga et al., 2017) describing the relationship between a bdqffdq:Specification (technical description of a Test) and a bdqffdq:Validation (a bdqffdq:Criterion in the context of bdqffdq:ResourceType (bdqffdq:SingleRecord or MultiRecordbdqffdq:) and associated bdqffdq:InformationElements).  
VM(va) = {s | s ⊂ S ⋀ va ∈ VA}

********************

#### ValidationPolicy

- Name: bdqffdq:ValidationPolicy
- Preferred Label: Validation Policy
- Definition: A bdqffdq:NeedConcept that relates a bdqffdq:UseCase to a set of supporting bdqffdq:Validations.
- SubClass Of: Policy; ValidationConcept
- Comments: A bdqffdq:ValidationPolicy is a data quality Need layer concept (see Figure 3 in Veiga et al., 2017) that describes how a bdqffdq:Validation relates to a bdqffdq:UseCase. This relationship defines which bdqffdq:Validations are needed to identify quality in a given bdqffdq:UseCase.  
VP (u) = {va | va ⊂ VA ⋀ u ∈ U }

********************

### 4.2 ObjectProperty terms
#### amendmentProperty

- Name: bdqffdq:amendmentProperty
- Preferred Label: amendment Property
- Definition: Category of object properties that apply to bdqffdq:Amendments
- Comments: Subproperties of this type group object properties that apply to bdqffdq:AmendmentConcepts such as bdqffdq:AmendmentPolicy (bdqffdq:DataQualityNeed), bdqffdq:AmendmentMethod (bdqffdq:DataQualityMethod) and bdqffdq:Amendment (bdqffdq:DataQualityReports).

********************

#### appliesTo

- Name: bdqffdq:appliesTo
- Preferred Label: applies To
- Definition: Describes the bdqffdq:DataResource about which a bdqffdq:Assertion is made.
- Comments: If a bdqffdq:Assertion forms the oa:body of an oa:Annotation, the bdqffdq:appliesTo bdqffdq:DataResource would be the oa:target of the bdqffdq:Annotation. If bdqffdq:Assertions are composed in bdqffdq:DataQualityReports, the bdqffdq:appliesTo bdqffdq:DataResource is an item examined as part of the bdqffdq:DataQualityReport. Expectation for bdqffdq:SingleRecord Test bdqffdq:Assertions on Darwin Core data in BDQ Core is that bdqffdq:appliesTo would point at a dwc:Occurrence record.

********************

#### composedOf

- Name: bdqffdq:composedOf
- Preferred Label: composed Of
- Definition: Specific vocabulary term that comprises a bdqffdq:InformationElement that is not a bdqffdq:AbstractInformationElement.
- Comments: Describes the properties from a controlled vocabulary that compose an InformationElement. For example, an InformationElement may be composedOf properties such as dwc:day, dwc:month and dwc:year.

********************

#### containsAssertion

- Name: bdqffdq:containsAssertion
- Preferred Label: contains Assertion
- Definition: Connects a bdqffdq:DataQualityReport with bdqffdq:Assertions that comprise that bdqffdq:DataQualityReport.
- Comments: Connects bdqffdq:Assertions together into bdqffdq:DataQualityReports. Alternatively, bdqffdq:Assertions can be contained in oa:Annotations, in which case this property is not used.

********************

#### forAmendment

- Name: bdqffdq:forAmendment
- Preferred Label: for Amendment
- Definition: Relates a bdqffdq:AmendmentMethod to a bdqffdq:Amendment.
- SubClass Of: amendmentProperty; forDataQualityNeed
- Range [ owl:someValuesFrom bdqffdq:forAmendment ]
- Comments: Use to link a bdqffdq:AmendmentMethod to a bdqffdq:Amendment. Describes the relationship between a bdqffdq:AmendmentMethod (Solutions layer, see Figure 3 in Veiga et al., 2017) and a bdqffdq:Amendment (Need layer, see Figure 3 in Veiga et al., 2017).

********************

#### forDataQualityNeed

- Name: bdqffdq:forDataQualityNeed
- Preferred Label: for Data Quality Need
- Definition: Category of properties that relates a bdqffdq:DataQualityNeed to specific bdqffdq:Methods.
- Comments: Category of properties that link Tests to their bdqffdq:Methods.

********************

#### forIssue

- Name: bdqffdq:forIssue
- Preferred Label: for Issue
- Definition: Relates a bdqffdq:IssueMethod to a bdqffdq:Issue.
- SubClass Of: forDataQualityNeed; issueProperty
- Range [ owl:someValuesFrom bdqffdq:forIssue ]
- Comments: Use to link a bdqffdq:IssueMethod to a bdqffdq:Issue. Describes the relationship between a bdqffdq:IssueMethod (Solutions layer, see Figure 3 in Veiga et al., 2017) and a bdqffdq:Issue (Need layer, see Figure 3 in Veiga et al., 2017). Parallel concepts are bdqffdq:forAmendment, bdqffdq:forValidation, and bdqffdq:forMeasure.

********************

#### forMeasure

- Name: bdqffdq:forMeasure
- Preferred Label: for Measure
- Definition: Relates a bdqffdq:MeasurementMethod to a bdqffdq:Measure.
- SubClass Of: forDataQualityNeed; measurementProperty
- Range [ owl:someValuesFrom bdqffdq:forMeasure ]
- Comments: Use to link bdqffdq:MeasurementMethods (Solutions layer, see Figure 3 in Veiga et al., 2017) to bdqffdq:Measures (Need layer, see Figure 3 in Veiga et al., 2017). Parallel concepts are bdqffdq:forAmendment, bdqffdq:forValidation, and bdqffdq:forIssue.

********************

#### forValidation

- Name: bdqffdq:forValidation
- Preferred Label: for Validation
- Definition: Relates a bdqffdq:ValidationMethod to a bdqffdq:Validation.
- SubClass Of: forDataQualityNeed; validationProperty
- Range [ owl:someValuesFrom bdqffdq:forValidation ]
- Comments: Use to link bdqffdq:ValidationMethods to bdqffdq:Validations. Describes the relationship between a bdqffdq:ValidationMethod (Solutions layer, see Figure 3 in Veiga et al., 2017) and a bdqffdq:Validation (Need layer, see Figure 3 in Veiga et al., 2017). Parallel concepts are bdqffdq:forAmendment, bdqffdq:forMeasure, and bdqffdq:forIssue.

********************

#### hasActedUponInformationElement

- Name: bdqffdq:hasActedUponInformationElement
- Preferred Label: has Acted Upon Information Element
- Definition: Describes the bdqffdq:ActedUpon bdqffdq:InformationElements assessed by a bdqffdq:DataQualityNeed about which bdqffdq:Assertions arising from the bdqffdq:DataQualityNeed would apply.
- SubClass Of: hasInformationElement
- Comments: Provides a relationship between bdqffdq concepts and the bdqffdq:InformationElements that are bdqffdq:ActedUpon in a Test.

********************

#### hasArgument

- Name: bdqffdq:hasArgument
- Preferred Label: has Argument
- Definition: Relates a bdqffdq:Specification to a bdqffdq:Argument
- Range bdqffdq:Argument
- Comments: Expected to be a relationship between a bdqffdq:Specification and a bdqffdq:Argument, where the bdqffdq:Argument provides a value for a bdqffdq:Parameter (e.g., bdq:sourceAuthority), and a bdqffdq:hasAuthoritiesDefaults for the bdqffdq:Specification may provide a default value for the bdqffdq:Parameter under that bdqffdq:Specification.

********************

#### hasConsultedInformationElement

- Name: bdqffdq:hasConsultedInformationElement
- Preferred Label: has Consulted Information Element
- Definition: Describes the bdqffdq:InformationElements assessed by a bdqffdq:DataQualityNeed in order to make bdqffdq:Assertions concerning bdqffdq:ActedUpon bdqffdq:InformationElements.
- SubClass Of: hasInformationElement
- Comments: Provides a relationship between bdqffdq concepts and the bdqffdq:InformationElements that are bdqffdq:Consulted, but not bdqffdq:ActedUpon in a Test.

********************

#### hasCriterion

- Name: bdqffdq:hasCriterion
- Preferred Label: has Criterion
- Definition: The bdqffdq:Criterion under which a bdqffdq:Validation or bdqffdq:Issue assesses for data quality.
- SubClass Of: issueProperty; validationProperty
- Range [ owl:someValuesFrom bdqffdq:hasCriterion ]
- Comments: Used to link the derived concept of a bdqffdq:Validation to the bdqffdq:FundamentalConcept of a bdqffdq:Criterion.

********************

#### hasDataQualityDimension

- Name: bdqffdq:hasDataQualityDimension
- Preferred Label: has Data Quality Dimension
- Definition: The bdqffdq:DataQualityDimension to which a bdqffdq:DataQualityNeed applies.
- SubClass Of: amendmentProperty; issueProperty; measurementProperty; validationProperty
- Range [ owl:someValuesFrom bdqffdq:hasDataQualityDimension ]
- Comments: Used to link a derived concept of a bdqffdq:DataQualityNeed (a Test, whether rdf:type Validation, Issue, Measure, or Amendment) to the bdqffdq:FundamentalConcept of a bdqffdq:DataQualityDimension. For a bdqffdq:Validation or bdqffdq:Issue, the bdqffdq:Dimension of data quality assessed. For a bdqffdq:Measure, the bdqffdq:Dimension of data quality measured. For a bdqffdq:Amendment, the bdqffdq:Dimension of data quality to be improved.  
Under the original formulation of the Framework, only Measures have Dimensions.

********************

#### hasEnhancement

- Name: bdqffdq:hasEnhancement
- Preferred Label: has Enhancement
- Definition: The bdqffdq:Enhancement that describes how a bdqffdq:Amendment may propose changes to improve data quality.
- SubClass Of: amendmentProperty
- Range [ owl:someValuesFrom bdqffdq:hasEnhancement ]
- Comments: Used to link the derived property of a bdqffdq:Amendment to the bdqffdq:FundamentalConcept of a bdqffdq:Enhancement.

********************

#### hasInformationElement

- Name: bdqffdq:hasInformationElement
- Preferred Label: has Information Element
- Definition: Describes the bdqffdq:InformationElements assessed by a bdqffdq:DataQualityNeed.
- SubClass Of: amendmentProperty; issueProperty; measurementProperty; validationProperty
- Range bdqffdq:InformationElement
- Comments: Provides a relationship between bdqffdq:DataQualityNeed concepts and bdqffdq:InformationElements. For example, bdqffdq:Validation uses this property with bdqffdq:hasResourceType to define a bdqffdq:Criterion in the context of related bdqffdq:InformationElements.  
Subtypes bdqffdq:hasActedUponInformationElement and bdqffdq:hasConsultedInformationElement allow a bdqffdq:DataQualityNeed to be related to specific bdqffdq:InformationElement terms in a way that allows bdqffdq:DataQualityReports to distinguish for consumers which bdqffdq:InformationElements a Test makes bdqffdq:Assertions about (and which only informed that bdqffdq:Assertion).

********************

#### hasParameter

- Name: bdqffdq:hasParameter
- Preferred Label: has Parameter
- Definition: Relates a bdqffdq:Argument to a bdqffdq:Parameter.
- Range bdqffdq:Parameter
- Comments: The bdqffdq:hasParameter property is expected to describe the Formal Parameter for which a bdqffdq:hasArgumentValue of the same bdqffdq:Argument provides the Actual Parameter. The bdqffdq:Argument is also expected to be the bdqffdq:hasArgument for a bdqffdq:Specification that provides the default value for the bdqffdq:hasArgumentValue and bdqffdq:hasParameter within a bdqffdq:hasAuthoritiesDefaults.

********************

#### hasResourceType

- Name: bdqffdq:hasResourceType
- Preferred Label: has Resource Type
- Definition: The bdqffdq:ResourceType to which a bdqffdq:DataQualityNeed applies.
- Comments: Provides additional metadata, with the bdqffdq:InformationElements, that describe the bdqffdq:ResourceType (bdqffdq:SingleRecord or bdqffdq:MultiRecord) on which the bdqffdq concept operates. For example, a bdqffdq:Amendment with bdqffdq:ResourceType bdqffdq:MultiRecord defines that bdqffdq:Amendment as operating on a data set.

********************

#### hasResponseQualifier

- Name: bdqffdq:hasResponseQualifier
- Preferred Label: has Response Qualifier
- Definition: ResponseQualifier object asserted by an Assertion.
- SubClass Of: reportProperty
- Comments: Optional extension point, could be used to add structured information about uncertainty.

********************

#### hasResponseResult

- Name: bdqffdq:hasResponseResult
- Preferred Label: has Response Result
- Definition: The bdqffdq:ResponseResult object asserted by a bdqffdq:Assertion.
- SubClass Of: reportProperty
- Comments: Used in a bdqffdq:DataQualityReport to describe bdqffdq:ResponseResult objects. For example, values could be bdqffdq:COMPLIANT or bdqffdq:NOT_COMPLIANT for bdqffdq:ValidationAssertions. Both bdqffdq:ValidationAssertions and bdqffdq:IssueAssertions have bdqffdq:ResponseResults as objects. The bdqffdq:AmendmentAssertions have bdqffdq:ResponseResults that are data properties, so they are not expected to use this object property. The bdqffdq:MeasurementAssertion bdqffdq:ResponseResults may be objects or data.  
If bdqffdq:ResponseResults are not objects, use the datatype property bdqffdq:hasResponseResultValue.

********************

#### hasResponseStatus

- Name: bdqffdq:hasResponseStatus
- Preferred Label: has Response Status
- Definition: The bdqffdq:ResponseStatus object asserted by a bdqffdq:Assertion.
- SubClass Of: reportProperty
- Comments: Used in a bdqffdq:DataQualityReport to describe bdqffdq:ResponseStatus. For example, in the case of a bdqffdq:ValidationAssertion, bdqffdq:ResponseStatus values could be bdqffdq:RUN_HAS_RESULT, bdqffdq:INTERNAL_PREREQUISITES_NOT_MET, or bdqffdq:EXTERNAL_PREREQISITES_NOT_MET. Similarly, bdqffdq:AmendmentAssertions can assert bdqffdq:ResponesStatus objects including bdqffdq:AMENDED or bdqffdq:FILLED_IN.  
The bdqffdq:ResponseStatus is always an object, unlike bdqffdq:ResponseResult, where either the object property bdqffdq:hasResponseResult or the data property bdqffdq:hasResponseResultValue may apply.

********************

#### hasSpecification

- Name: bdqffdq:hasSpecification
- Preferred Label: has Specification
- Definition: Relates a bdqffdq:Method to a bdqffdq:Specification.
- Range [ owl:someValuesFrom bdqffdq:hasSpecification ]
- Comments: Describes the relationship between a derived bdqffdq concept that is a bdqffdq:Method and the bdqffdq:FundamentalConcept of a bdqffdq:Specification (technical description of a Test).

********************

#### hasUseCase

- Name: bdqffdq:hasUseCase
- Preferred Label: has Use Case
- Definition: Relates a bdqffdq:Policy to a bdqffdq:UseCase.
- Range [ owl:someValuesFrom bdqffdq:hasUseCase ]
- Comments: Used by concepts in the bdqffdq:DataQualityNeed category to describe the relationship between bdqffdq:Policies (bdqffdq:ValidationPolicy, bdqffdq:MeasurementPolicy, bdqffdq:AmendmentPolicy) and an instance of a bdqffdq:UseCase.

********************

#### implementedBy

- Name: bdqffdq:implementedBy
- Preferred Label: implemented By
- Definition: The bdqffdq:Mechanism that provides a bdqffdq:Implementation
- Range [ owl:someValuesFrom bdqffdq:implementedBy ]
- Comments: Describes the link between a bdqffdq:Implementation and a bdqffdq:Mechanism.

********************

#### improvedBy

- Name: bdqffdq:improvedBy
- Preferred Label: improved By
- Definition: The bdqffdq:ImprovementTarget that would have data quality improved by bdqffdq:Assertions resulting from a bdqffdq:Amendment.
- Range [ owl:someValuesFrom bdqffdq:improvedBy ]
- Comments: Originally had Domain: Amendment and Range: ImprovementTarget. Asserts that a bdqffdq:ImprovementTarget could be improved by the bdqffdq:Amendment.  
Object property that describes a bdqffdq:Amendment, as part of the bdqffdq:ImprovementTarget, that would improve data bdqffdq:ActedUpon by a set of bdqffdq:Measures or bdqffdq:Validations. This can be used to determine which bdqffdq:Measures and bdqffdq:Validations are improved upon by a given bdqffdq:Amendment.

********************

#### includedInPolicy

- Name: bdqffdq:includedInPolicy
- Preferred Label: included In Policy
- Definition: Assserts that a bdqffdq:DataQualityNeed is part of a bdqffdq:Policy.
- Comments: Relates bdqffdq:Policies to Tests (bdqffdq:DataQualityNeed).

********************

#### issueProperty

- Name: bdqffdq:issueProperty
- Preferred Label: issue Property
- Definition: Category of object properties that apply to bdqffdq:Issues.
- Comments: Properties that relate bdqffdq:Issues to bdqffdq:IssueMethods, bdqffdq:Criteria, and bdqffdq:DataQualityDimensions.

********************

#### measurementProperty

- Name: bdqffdq:measurementProperty
- Preferred Label: measurement Property
- Definition: Category of object properties that apply to bdqffdq:Measures.
- Comments: Subproperties of this type group object properties that apply to bdqffdq:MeasurementConcepts such as bdqffdq:MeasurementPolicy (bdqffdq:DataQualityNeed), bdqffdq:MeasurementMethod (bdqffdq:DataQualityMethod) and bdqffdq:Measure (bdqffdq:DataQualityReport).

********************

#### producesAssertion

- Name: bdqffdq:producesAssertion
- Preferred Label: produces Assertion
- Definition: Connects an entity with a bdqffdq:Assertion that the entity created.
- Comments: Connects bdqffdq:Implementations (Solutions layer, see Figure 3 in Veiga et al., 2017) with the bdqffdq:Assertions (Reports layer, see Figure 3 in Veiga et al., 2017) that they produce from the execution of a bdqffdq:Specification.

********************

#### reportProperty

- Name: bdqffdq:reportProperty
- Preferred Label: report Property
- Definition: Category of object properties that apply to bdqffdq:Assertions.
- Comments: Category of properties used in reports (object properties associated with response objects (bdqffdq:Assertions)). See also the data properties bdqffdq:hasResponseComment and bdqffdq:hasResponseResultValue.

********************

#### targetedIssue

- Name: bdqffdq:targetedIssue
- Preferred Label: targeted Issue
- Definition: A bdqffdq:Issue for which the data conformance with a bdqffdq:NeedConcept may be improved by accepting proposals from a bdqffdq:Amendment via a bdqffdq:ImprovementTarget.
- Range [ owl:someValuesFrom bdqffdq:targetedIssue ]
- Comments: The bdqffdq:Issue targeted by a problem via the bdqffdq:ImprovementTarget object. Describes the relationship between a bdqffdq:ImprovementTarget and a bdqffdq:Issue.

********************

#### targetedMeasure

- Name: bdqffdq:targetedMeasure
- Preferred Label: targeted Measure
- Definition: A bdqffdq:Measure for which the data conformance with a bdqffdq:NeedConcept may be improved by accepting proposals from a bdqffdq:Amendment via a bdqffdq:ImprovementTarget.
- Range [ owl:someValuesFrom bdqffdq:targetedMeasure ]
- Comments: Describes the relationship between a bdqffdq:ImprovementTarget and a bdqffdq:Measure.

********************

#### targetedValidation

- Name: bdqffdq:targetedValidation
- Preferred Label: targeted Validation
- Definition: A bdqffdq:Validation for which the data conformance with a bdqffdq:NeedConcept may be improved by accepting proposals from a bdqffdq:Amendment via a bdqffdq:ImprovementTarget.
- SubClass Of: http://www.w3.org/2002/07/owl#topObjectProperty
- Range [ owl:someValuesFrom bdqffdq:targetedValidation ]
- Comments: Relates a bdqffdq:ImprovementTarget to a bdqffdq:Validation. Describes the relationship between a bdqffdq:ImprovementTarget and a bdqffdq:Validation.

********************

#### usesSpecification

- Name: bdqffdq:usesSpecification
- Preferred Label: uses Specification
- Definition: The bdqffdq:Specification that a bdqffdq:Implementation implements.
- Range [ owl:someValuesFrom bdqffdq:usesSpecification ]
- Comments: Relates a bdqffdq:Implementation to the bdqffdq:Specification that the bdqffdq:Implementation implements.

********************

#### validationProperty

- Name: bdqffdq:validationProperty
- Preferred Label: validation Property
- Definition: Category of object properties that apply to bdqffdq:Validations.
- Comments: Subproperties of this type group object properties that apply to bdqffdq:ValidationConcepts such as bdqffdq:ValidationPolicy (bdqffdq:DataQualityNeed), bdqffdq:ValidationMethod (bdqffdq:DataQualityMethod) and bdqffdq:Validation (bdqffdq:DataQualityReport).

********************

### 4.3 DataProperty terms
#### hasAuthoritiesDefaults

- Name: bdqffdq:hasAuthoritiesDefaults
- Preferred Label: has Authorities and Defaults
- Definition: Text describing bdq:sourceAuthorities and bdqffdq:Parameters with their default values to attach to a bdqffdq:Specification to further specify the behavior described in the bdqffdq:hasExpectedResponse.
- Range xsd:string
- Comments: Details of the bdq:sourceAuthority listed in a bdqffdq:Specification, with bdqffdq:Parameters that may affect the bdqffdq:hasExpectedResponse, and with their default values.

********************

#### hasDateLastUpdated

- Name: bdqffdq:hasDateLastUpdated
- Preferred Label: has Date Last Updated
- Definition: Date of the most recent dcterms:issued for this class with a change that would be pertinent to a bdqffdq:Implementation.
- Range xsd:date
- Comments: While a new instance of a resource with a new dcterms:issued is required for any change to that resource, not all changes would be pertinent to implementers, (i.e., that would required implementers to evaluate their code for changes needed to comply with the update). The bdqffdq:hasDateLastUpdated allows implementers to identify which new changes to the definition of a Test would entail changes to code, and which would not. For example, a change to the logic of a bdqffdq:Specification in the text of bdqffdq:hasExpectedResponse would imply needed changes to the logic of code implementing that bdqffdq:Specification, but a correction of a spelling mistake within the text of a bdqffdq:hasExpectedResponse would not.

********************

#### hasExpectedResponse

- Name: bdqffdq:hasExpectedResponse
- Preferred Label: has Expected Response
- Definition: Text describing the logic to be followed by a bdqffdq:Implementation of a bdqffdq:Specification specifying the values of bdqffdq:ResponseStatus and bdqffdq:ResponseResults that should be produced from the evaluation of input bdqffdq:InformationElements.
- Range xsd:string
- Comments: The description of the logic of a Test Specification. A bdqffdq:hasExpectedResponse is expected to be a data property of a Specification.

********************

#### hasResponseComment

- Name: bdqffdq:hasResponseComment
- Preferred Label: has Response Comment
- Definition: Free text describing the bdqffdq:Assertion made in the response and why that conclusion was reached.
- Range xsd:string
- Comments: Intended for consumption by human readers of bdqffdq:DataQualityReports to understand why particular bdqffdq:Assertions were made.

********************

#### hasResponseResultValue

- Name: bdqffdq:hasResponseResultValue
- Preferred Label: has response result value
- Definition: Data property carrying the value of a bdqffdq:Assertion when the value is not an object.
- Comments: Applies to bdqffdq:AmendmentAssertions. To support bdqcore: Tests, bdqffdq:hasResponseResultValue is expected to carry a key:value list where the keys are the names of bdqffdq:ActedUpon bdqffdq:InformationElements, and the values are the proposed new values (filling in or replacing the values of those terms in the input). Applies to bdqffdq:MeasureAssertions that assert a numeric value.

********************

### 4.4 NamedIndividual terms
#### MultiRecord

- Name: bdqffdq:MultiRecord
- Type: bdqffdq:ResourceType
- Preferred Label: Multi Record
- Definition: A set of one or more bdqffdq:SingleRecords.
- Comments: A data set. Encoded data with a defined structure that can be described as dcmitype:Dataset.

********************

#### SingleRecord

- Name: bdqffdq:SingleRecord
- Type: bdqffdq:ResourceType
- Preferred Label: Single Record
- Definition: A single entity comprised of encoded data with a defined structure that contains one instance of a core concept from the perspective of bdqffdq:InformationElements assessed for a bdqffdq:DataQualityNeed.
- Comments: A record from a dcmitype:Dataset. May be a database tuple, in the strict sense (i.e, a single row in a table) or may be rows related across several tables, or a graph of data. A bdqffdq:SingleRecord is single in that it has one instance of a core concept from the perspective of bdqffdq:InformationElements assessed for a bdqffdq:UseCase. For example, in a bdqffdq:UseCase where dwc:Occurences are central, a bdqffdq:SingleRecord would represent a single dwc:Occurrence, but could have multiple dwc:Identifications and multiple dwc:Taxa related to it in a graph or data structure. However, in a bdqffdq:UseCase where dwc:Taxa are central, a bdqffdq:SingleRecord would represent a single dwc:Taxon entity (and might have multiple dwc:Occurrences related to it as part of the bdqffdq:SingleRecord, so long as the graph was limited before reaching other dwc:Taxon entities).  
A bdqffdq:SingleRecord, like a bdqffdq:MultiRecord, consists of data with a defined structure that can be described as dcmitype:Dataset

********************

#### COMPLETE

- Name: bdqffdq:COMPLETE
- Type: bdqffdq:ResponseResult
- Preferred Label: COMPLETE
- DifferentFrom: bdqffdq:NOT_COMPLETE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Measure that asserts that data are present and sufficiently comprehensive for use.
- Comments: This value can be used to filter data for Quality Assurance. This value can be asserted, for example, by bdqffdq:Measures of bdqffdq:MultiRecords where all the bdqffdq:Validation bdqffdq:ResponseResults from all included records in the dataset are bdqffdq:COMPLIANT.

********************

#### IS_ISSUE

- Name: bdqffdq:IS_ISSUE
- Type: bdqffdq:ResponseResult
- Preferred Label: IS_ISSUE
- DifferentFrom: bdqffdq:NOT_ISSUE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue indicating that the data do not have sufficient quality for a use.
- Comments: This is a parallel bdqffdq:ResponseResult to bdqffdq:NOT_COMPLIANT

********************

#### IS_ISSUE

- Name: bdqffdq:IS_ISSUE
- Type: bdqffdq:ResponseResult
- Preferred Label: IS_ISSUE
- DifferentFrom: bdqffdq:POTENTIAL_ISSUE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue indicating that the data do not have sufficient quality for a use.
- Comments: This is a parallel bdqffdq:ResponseResult to bdqffdq:NOT_COMPLIANT

********************

#### NOT_COMPLETE

- Name: bdqffdq:NOT_COMPLETE
- Type: bdqffdq:ResponseResult
- Preferred Label: NOT_COMPLETE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Measure which asserts that data are not present or are not sufficiently comprehensive for a use.
- Comments: This value can be used to exclude data for Quality Assurance. This value can be asserted, for example, by bdqffdq:Measures of bdqffdq:MultiRecords where not all the bdqffdq:Validation bdqffdq:ResponseResult from all included records in the dataset have a bdqffdq:ResponseResult of bdqffdq:COMPLIANT.

********************

#### NOT_ISSUE

- Name: bdqffdq:NOT_ISSUE
- Type: bdqffdq:ResponseResult
- Preferred Label: NOT_ISSUE
- DifferentFrom: bdqffdq:POTENTIAL_ISSUE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue where no potential problems were detected.
- Comments: This is similar to, but has different semantics to, bdqffdq:COMPLIANT for a bdqffdq:Validation. The value bdqffdq:COMPLIANT means that the data were evaluated as having quality according to a bdqffdq:Criterion. The value bdqffdq:NOT_ISSUE means that no bdqffdq:Issue with data quality was found under a bdqffdq:Criterion for identifying the absence of quality.

********************

#### POTENTIAL_ISSUE

- Name: bdqffdq:POTENTIAL_ISSUE
- Type: bdqffdq:ResponseResult
- Preferred Label: POTENTIAL_ISSUE
- Definition: A bdqffdq:ResponseResult of a bdqffdq:Issue that indicates that the data may not have sufficient quality for a use. The user will need to evaluate if the data are fit for their particular use or not.
- Comments: See also bdqffdq:IS_ISSUE and bdqffdq:NOT_ISSUE. The value bdqffdq:POTENTIAL_ISSUE has no analog in a bdqffdq:Validation.

********************

#### AMENDED

- Name: bdqffdq:AMENDED
- Type: bdqffdq:ResponseStatus
- Preferred Label: AMENDED
- DifferentFrom: bdqffdq:NOT_AMENDED
- Definition: A bdqffdq:ResponseStatus used to indicate that a bdqffdq:hasResponseResultValue from a bdqffdq:Amendment contains a proposed change.
- Comments: The value bdqffdq:AMENDED implies that a change is being proposed to an existing bdq:NotEmpty value. bdqffdq:Amendments do not provide bdqffdq:hasResponseResult object properties. Proposed changes will be in a bdqffdq:hasResponseResultValue data property.

********************

#### NOT_AMENDED

- Name: bdqffdq:NOT_AMENDED
- Type: bdqffdq:ResponseStatus
- Preferred Label: NOT_AMENDED
- Definition: A bdqffdq:ResponseStatus used to indicate that a bdqffdq:Amendment proposed no change.
- Comments: No value will be provided in a bdqfdq:hasResponseResultValue. bdqffdq:Amendments do not provide bdqffdq:hasResponseResult object properties.

********************

#### RUN_HAS_RESULT

- Name: bdqffdq:RUN_HAS_RESULT
- Type: bdqffdq:ResponseStatus
- Preferred Label: RUN_HAS_RESULT
- Definition: A bdqffdq:ResponseStatus used to indicate that that a result was correctly generated.
- Comments: Applies to bdqffdq:Validations, bdqffdq:Issues and bdqfdfq:Measures, but not bdqffdq:Amendments. For a bdqffdq:Validation or a bdqffdq:Issue, the value will be found as a bdqffdq:ResponseResult object by following bdqffdq:hasResponseResult. For a bdqffdq:Measure, the value could be either in the data property bdqffdq:hasResponseResultValue or could be a ResponseResult object.

********************


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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/terms/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


