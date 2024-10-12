<!--- Template for header, values provided from yaml configuration --->
# {document_title}

Title
: {document_title}

Date version issued
: {ratification_date}

Date created
: {created_date}

Part of TDWG Standard
: <{standard_iri}>

Preferred namespace abbreviation
: {pref_namespace_prefix}

This version
: <{current_iri}{ratification_date}>

Latest version
: <{current_iri}>

{previous_version_slot}

Abstract
: {abstract}

Authors
: {authors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}

### Table of Contents ###

{toc}

## 1 Introduction

The BDQ Conceptual Framework ontology formally describes the terms and relationships between them for evaluating the quality of biodiversity data. Due to the comprehensiveness of the conceptual framework (Veiga et al. 2017), it allows different interpretations and manners of using it according to different stakeholders. The Framework also prodives a base for the bdq: and bdqcore: namespace vocabularies.

The bdqffdq: vocabulary is a specification of a framework for describing data quality.   Each of the tests in the bdqcore: vocabulary in this standard has been designed with this framework and is framed using the terms and concepts from the framework. The framework provides the context for each test, and has shaped decisions made about each test.

The framework considers data to have quality with respect to some specified use.   It provides a means to describe a use of data (bdqffdq:UseCase), and what is needed for some data set to have quality for that use, that is for some data set to be fit for a specified purpose.  The framework explicitly links data quality to use, and allows formal description of means to assure that data are fit for some specified purpose.

This document lists terms used to describe 'data quality' / 'fitness for use' in the context of biodiversity data.  These are based on Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>, with a few changes for increased clarity.

### 1.1 Documents about the bdqffdq: ontology.

The bdqffdq: vocabulary is an ontology, it includes: 

- A [term list](../list/bdqffdq/index.md) for the vocabulary, containing just the vocabulary terms.
- Additional axioms that can be found in the [vocabulary extension list](../extension/bdqffdq/index.md) 
- Normative guidance on the use of this ontology is provided in this landing page document.
- The bdqffdq framework ontology is best technically understood as its [Owl Ontology Distribution](../vocabulary/bdqffdq.owl) 

An illustrated guide to the use of the bdqffdq ontology is provided in the [Guide to the bdqffdq: framework](../guide/bdqffdq/index.md) 

### 1.2 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Prefix**   | **Namespace**                                    | **Note** |
|--------------|--------------------------------------------------|----------|
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                | Framework for Describing Data Quality |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms                | Tests described using the bdqffdq Framework |
| bdq          | https://rs.tdwg.org/bdq/terms/                   | Supporting Vocabulary for Data Quality |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms                 | Data Quality Dimension Vocabulary |
| bdqcrit      | https://rs.tdwg.org/bdqcrit/terms                | Data Quality Criteria Vocabulary | 
| bdqenh       | https://rs.tdwg.org/bdqenh/terms                 | Data Quality Enhancement Vocabulary | 
| dc           | https://purl.org/dc/elements/1.1/                | | 
| dcterms      | https://purl.org/dc/elements/1.1/                | |
| dwc          | http://rs.tdwg.org/dwc/terms/                    | Darwin Core |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      | |
| oa           | https://www.w3.org/TR/annotation-vocab/          | |
| skos         | http://www.w3.org/2004/02/skos/core#             | |
| owl          | http://www.w3.org/2002/07/owl#                   | |

### 1.2 Status of the content of this document

Sections 2 and 5 are normative.

Section 3 is non-normative

Section 3.1 lists which which terms in section 4 have normative values and which non-normative.

Other sections of this document are marked as normative or non-normative.

### 1.3 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.4 Distributions (normative)

| Description | IRI | Download URL |
| ----------- | --- | ------------ |
| Human Readable Term List |  | [https://github.com/tdwg/bdq/blob/master/tg2/\_review/docs/terms/bdqffdq/index.md](../list/bdqffdq/index.md) | 
| Human Readable Vocabulary Extension |  | [https://github.com/tdwg/bdq/blob/master/tg2/\_review/docs/extension/bdqffdq/index.md](../extension/bdqffdq/index.md) | 
| Owl Ontology | | [https://github.com/tdwg/bdq/blob/master/tg2/\_review/vocabulary/bdqffdq.owl](../vocabulary/bdqffdq.owl) |

### 1.5 Diagram of classes and properties (non-normative) 

The diagram below is intended to help understand the normative statements in section 2 below.

![Diagram of Validation, ValidationMethod, and ValidationAssertion with related classes](../guide/bdqffdq/bdqffdq_data_quality_needs_solutions_report_validation.svg "Validation concepts in the Needs, Solutions, and Reports levels.")

The use of classes and properties in [bdqcore:](../../dist/bdqcore.ttl) also follow the normative guidance in section 2 below.

## 2 Use of Terms (normative) 

When not represented as objects, controlled value strings MUST be used as values of bdqffdq:ResponseStatus, and bdqffdq:ResponseResult.

### 2.1 Use of properties (normative) 

This section describes normative expectations for the use of object and datatype properties to related instances of bdqffdq: classes in their intended ways given the open world limited use of domains, ranges, and other axioms in the bdqffdq Framework ontology.  This guidance builds on the normative defintions of bdqffdq: object properties and and datatype properties to describe how bdqffdq terms can be composed in a useful and consistent way.

This guidance describes the use of the bdqffdq: framework terms in an RDF context.  This guidance MAY be used to develop models of the bdqffdq data quality framework in more constrained forms including UML object models, information models, classes in a programing language, or database schemas.  

#### 2.1.1 Properties relating data quality needs

Each description of a data quality test SHOULD include the following properties and related instances.

The bdqffdq:hasUseCase object property SHOULD have an individual with a type that is a subclass of bdqffdq:Policy as its subject.  

The bdqffdq:hasUseCase object property MAY have an individual from the bdq: vocabulary that represents a UseCase as its object.  

An axiom types the range of bdqffdq:hasUseCase as a bdqffdq:UseCase.  

The bdqffdq:includedInPolicy object property SHOULD have an individual that is a subclass of bdqffdq:Policy as its subject.

The bdqffdq:includedInPolicy object property SHOULD have an individual that is a subclass of bdqffdq:DataQualityNeed as its object.

The four subclasses of bdqffdq:DataQualityNeed are bdqffdq:Validation, bdqffdq:Measure, bdqffdq:Amendment, and bdqffdq:Issue.

Each individual that is a subclass of bdqffdq:DataQualityNeed SHOULD have at least one bdqffdq:includedInPolicy relationship to an instance of a subclass of bdqffdq:Policy which is in turn related to an instance of a bdqffdq:UseCase.   

User communites MAY provide new use cases, and MAY compose instances that are subtypes of bdqffdq:DataQualityNeed with instances of bdqffdq:Policy subclasses and instances of bdqffdq:UseCase with the object properties bdqffdq:includesInPolicy and bdqffdq:hasUseCase in new ways.  

Each instance of a subclass of a bdqffdq:DataQualityNeed SHOULD have an rdfs:label in all upper case, with underscores separating components.  Tests that have a bdqffdq:hasResourceType of bdqffdq:SingleRecord SHOULD follow the convention of the subclass of bdqffdq:DataQualityNeed in all upper case as the first word, and a representation of the bdqffdq:AbstractInformationElement as a single word in all upper case as the second word, in the form TESTTYPE_INFORMATIONELEMENT_CRITERIA or TESTTYPE_INFORMATIONELEMENT_ACTION_INFORMATIONELEMENT.  Tests that have a bdqffdq:hasResourceType of bdqffdq:MultiRecord SHOULD have "MULTIRECORD_" as the first element in their rdfs:label, and MAY follow the pattern MULTIRECORD_TESTTYPE_COUNT_RESULT_INFORMATIONELEMENT_CRITERIA, or MULTIRECORD_TESTTYPE_QA_INFORMANTIONELEMENT_CRITERIA.  The rdfs:label of the instance of the subclass of bdqffdq:DataQualityNeed SHOULD be used by humans to identify tests.

Each instance of a subclass of bdqffdq:DataQualityNeed MUST have exactly one bdqffdq:hasResourceType object property linking it to a bdqffdq:SingleRecord or a bsqffdq:MultiRecord.

The bdqffdq:hasCriterion object property SHOULD have an individual with a type that is a bdqffdq:Validation or a bdqffdq:Issue as its subject.

The bdqffdq:hasCriterion object property MAY have an individual from the bdqcrit: vocabulary as its object.

An axiom types the range of bdqffdq:hasCriterion as a bdqffdq:Criterion.

The bdqffdq:hasEnhancement object property SHOULD have an individual with a type that is a bdqffdq:Amendment as its subject.

The bdqffdq:hasEnhancement object property MAY have an individual from the bdqenh: vocabulary as its object.

An axiom types the range of bdqffdq:hasEnhancement as a bdqffdq:Enhancement.

The bdqffdq:hasDataQualityDimension object property SHOULD have an individual with a type that is a subclass of bdqffdq:DataQualityNeed as its subject.

The bdqffdq:hasDataQualityDimension object property MAY have individual in the bdqdim: vocabulary is its object.  

An axiom types the range of bdqffdq:hasDataQualityDimension as a bdqffdq:DataQualityDimension.

Each individual instance of a bbdqffdq:Validation SHOULD have exactly one bdqffdq:hasDataQualityDimension property and exactly one bdffdq:Criterion property.

Each individual instance of a bbdqffdq:Issue SHOULD have exactly one bdqffdq:hasDataQualityDimension property and exactly one bdffdq:Criterion property.

Each individual instance of a bbdqffdq:Amendment SHOULD have exactly one bdqffdq:hasDataQualityDimension property and exactly one bdffdq:Enhancement property.

Each individual instance of a bbdqffdq:Measure SHOULD have exactly one bdqffdq:hasDataQualityDimension property.

A subproperty of the bdqffdq:hasInformationElement object property SHOULD have an individual that is a subclass of bdqffdq:InformationElement as its object.

A subproperty of the bdqffdq:hasInformationElement object property SHOULD have an individual that is a subclass of bdqffdq:DataQualityNeed as its subject.

Each instance of a subclass of bdqffdq:DataQualityNeed SHOULD have exactly one bdqffdq:hasActedUponInformationElement property linking it to a bdqffdq:ActedUpon. 

Each instance of bdqffdq:ActedUpon SHOULD have one to many bdqffdq:composedOf object properties linking it to specific information elements.

Each instance of a subclass of bdqffdq:DataQualityNeed MAY have exactly one bdqffdq:hasConsultedInformationElement property linking it to a bdqffdq:Consulted.

Each instance of bdqffdq:Consulted SHOULD have one to many bdqffdq:composedOf object properties linking it to specific information elements.

Each instance of a subclass of bdqffdq:DataQualityNeed MAY have a bdqffdq:hasInformationElement property linking it to a bdqffdq:AbstractInformationElement.

Each instance of bdqffdq:AbstractInformationElement SHOULD have rdfs:label and rdfs:comment properties describing the scope of the information element with the rdfs:label corresponding to the INFORMATIONELEMENT portion of the rdfs:label for an instance of a subclass of bdqffdq:DataQualityNeed following the convention described in this section.  

#### 2.1.2 Properties relating data quality needs to data quality solutions

Each description of a data quality test SHOULD include the following properties and related instances.

The bdqffdq:forValidation object property SHOULD have have an individual with a type that is a subclass of bdqffdq:ValidationMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forValidation object property as a bdqffdq:Validation

Each bdqffdq:Validation method SHOULD have exactly one bdqffdq:forValidation object property.

The bdqffdq:forAmendment object property SHOULD have have an individual with a type that is a subclass of bdqffdq:AmendmentMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forAmendment object property as a bdqffdq:Amendment

Each bdqffdq:Amendment method SHOULD have exactly one bdqffdq:forAmendment object property.

The bdqffdq:forMeasure object property SHOULD have have an individual with a type that is a subclass of bdqffdq:MeasureMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forMeasure object property as a bdqffdq:Measure

Each bdqffdq:Measure method SHOULD have exactly one bdqffdq:forMeasure object property.

The bdqffdq:forIssue object property SHOULD have have an individual with a type that is a subclass of bdqffdq:IssueMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:forIssue object property as a bdqffdq:Issue

Each bdqffdq:Issue method SHOULD have exactly one bdqffdq:forIssue object property.

#### 2.1.3 Properties relating to data quality solutions provided in a test description

Each description of a data quality test SHOULD include the following properties and related instances.

The bdqffdq:hasSpecification object property SHOULD have an instance of a subclass of bdqffdq:DataQualityMethod as its subject.

An axiom places an owl:restriction on the object of the bdqffdq:hasSpecification object property as a bdqffdq:Specification.

The bdqffdq:hasArgument object property SHOULD have a bdqffdq:Specification as its subject.

An axiom types the object of the bdqffdq:hasArgument object as a bdqffdq:Argument.

An instance of bdqffdq:Argument SHOULD have exactly one bdqffdq:hasArgumentValue data property holding the value of the argument that replaces the bdqffdq:Parameter in the bdqffdq:hasExpectedResponse of the bdqffdq:Specification.  An instance of bdqffdq:Argument SHOULD have exactly one bdqffdq:hasParameter object property that denotes the parameter within the bdqffdq:hasExpectedResponse that is to be replace by the value of the bdqffdq:hasArgumentValue.  An instance of bdqffdq:Argument SHOULD be related to exactly one instance of a bdqffdq:Specification with the bdqffdq:hasArgument object property.

Each instance of a bdqffdq:Specification MAY have zero to many bdqffdq:hasArgument object properties relating it to zero to many bdqffdq:Argument instances.

Each instance of a bdqffdq:Specification with a bdqffdq:hasAuthoritiesDefaults value that references at least one parameter MUST have a corresponding bdqffdq:hasArgument object property.  The related instances bdqffdq:Argument through these bdqffdq:hasArgument object properties SHOULD have appropriate bdqffdq:hasArgumentValue and bdqffdq:hasParameter triples to express the actual and formal parameters for the bdqffdq:Specification instance.

The bdqffdq:hasParameter object property SHOULD have a bdqffdq:Argument as its subject.

An axiom types the object of the bdqffdq:hasParameter object property as a bdqffdq:Parameter.

#### 2.1.4 Properties relating to data quality solutions provided by an implementation

Each data quality mechanism that produces data quality reports using the bdqffdq vocabulary SHOULD include the following properties and related instances.


#### 2.1.5 Properties relating data quality reports

Each data quality mechanism that produces data quality reports using the bdqffdq vocabulary SHOULD include the following properties and related instances.

Nothing in this section is to be construed as relaxing the normative statements in the users guide and implementers guid concering the expression of data quality responses in forms other than RDF.  Each data quality mechanism MUST produce results coresponding to bdqffdq:Assertions with bdqffdq:hasResponseStatus, bdqffdq:hasResponseResult, and bdqffdq:hasResponseComment as specfied in those guides.   

## 3 Term Index

### 3.1 Key to Vocabulary Terms

{term_key}

### 3.2 Indexes
<!--- NOTE: The mathematical forumlation of the framework is in the bdqffdq_landing-footer.md document --->

