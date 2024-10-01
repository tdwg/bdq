<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
# Quick Reference Guide to the bdqffdq Ontology.

Draft Standard for Submission

<!--- Note: This document deliberately diverges from many of the SHOULD expecations of section 3.2.3 Layout and style of the SDS for the express purpose of simplicity.  Some header values have been included in the first paragraph of text, others have been omitted, a table of contents has been omitted, the introduction and abstract are combined, the introduction is not given a heading, and, in consequence, headings are not numbered. --->

This document is intended to be an easy-to-read reference (as of {doc_modified}) of the bdqffdq ontology for describing biodiversity data quality maintained as part of the TDWG standard [BDQ Core]({standard_iri}) produced by the {creator} and is maintained by the {maintainer}. This document lists the terms in the bdqffdq: namespace below. Definitions, comments, and examples may include namespace abbreviations (e.g., "bdq:", “bdffdq:”). These are reequired as the meaning for the word is defined specifically in that namespace.

The quick reference guide to the BDQ Core tests described with the bdqffdq: ontology can be found at [Terms in bdqcore: Quick Reference Guide](../bdqcore/index.md). 

This page is a descriptive document, not the full vocabulary definition document for bdqffdq: terms.   It combines a subset of the normative and non-normative elements of classes and properties found in the [full bdqffdq: ontology](../../vocabulary/bdqffdq.owl), and does not include additional elements such as domains and restrictions found therein. 
Further details are in the overview at [BDQ Core Introduction](../../intro/index.md), and in the [bdqffdq Framework Users Guide](../../guide/bdqffdq/index.md).

If you have questions or suggestions, submit these to the [BDQ Core Issues](https://github.com/tdwg/bdq/issues) page in GitHub. See the bottom of this document for how to cite BDQ Core.

# Indexes 

- [Classes](#Class-terms)
- [Named Individuals](#NamedIndividual-terms)
- [Object Properties](#ObjectProperty-terms)
- [Data Properties](#DataProperty-terms)

## Alphabetical Index of classes]

[AbstractInformationElement](#AbstractInformationElement)
[ActedUpon](#ActedUpon)
[Amendment](#Amendment)
[AmendmentAssertion](#AmendmentAssertion)
[AmendmentConcept](#AmendmentConcept)
[AmendmentMethod](#AmendmentMethod)
[AmendmentPolicy](#AmendmentPolicy)
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
[MeasurementMethod](#MeasurementMethod)
[MeasurementPolicy](#MeasurementPolicy)
[MeaurementConcept](#MeaurementConcept)
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

## Class terms
### AbstractInformationElement

- Name: bdqffdq:AbstractInformationElement
- Preferred Label: Abstract Information Element
- Definition: An InformationElement described in abstract terms and not linked with one or more concrete terms.
- SubClass Of: InformationElement
- Notes:
Information elements such as DATE and DAY are abstract, they could reference any representation of those concepts.  In contrast, dwc:eventDate and dwc:day can be linked to concrete Acted Upon or Consulted information elements.

********************

### ActedUpon

- Name: bdqffdq:ActedUpon
- Preferred Label: Acted Upon
- Definition: An information element, expressed in concrete terms, about which a data quality need expresses assertions about the data quality in that element.
- SubClass Of: InformationElement
- Notes:
An information element to which a Result applies.

********************

### Amendment

- Name: bdqffdq:Amendment
- Preferred Label: Amendment
- Definition: A data quality need that expresses how proposals may be made to improve the fittnes for use of data.
- SubClass Of: AmendmentConcept; DataQualityNeed
- Notes:
ContextualizedEnhacement in the original framework.   Describes an instance of the enhancement concept in the context of the associated information elements from some controlled vocabulary (fields ActedUpon or Consulted), and a ResourceType of SingleRecord or MultiRecord.  

Describes a proposal for enhancement of original data, which if accepted, would improve the quality of the data for some use. For example: Recommends valid value for taxon name in a single record.  

Amendments may describe proposed changes to data values, or proposed changes to processes for the production and manipulation of data, for example an Amendment on a SingleRecord may provide criteria for proposing that latitude and longitude are transposed in that record, or a similar Amendment on a MultiRecord may provide critera for proposing that all latitudes and longitudes from some data source have been transposed, and the mapping of data values to transport terms should be changed.  

An Amendment is the data quality needs concept that parallels an AmendmentMethod at the solutions level, and an AmmendmentAssertion at the report level.   

AM = { am | am = < ie, e, rt >, ie ∈ IE, e ∈ E ⋀ rt ∈ RT }

********************

### AmendmentAssertion

- Name: bdqffdq:AmendmentAssertion
- Preferred Label: Amendment Assertion
- Definition: An assertion expressing the result of an implementation evaluating an amendment supporting a particular data quality need to improve a particular data resource.
- SubClass Of: AmendmentConcept; Assertion
- Notes:
The Amendment assertion type is a report level concept that describes the results of the execution of of a test that performs an AmendmentMethod following some Specification to propose changes based on some Amendment. 

An Amendment concept in bdqffdq is expected to carry a ResponseStatus result that includes a status FILLED_IN, AMENDED, as well as a ResponseResult that asserts proposed changes to values from the original data.

DQA(dr) = {dqa | dqa = < am, s, m, r >, am ∈ AM, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

********************

### AmendmentMethod

- Name: bdqffdq:AmendmentMethod
- Preferred Label: Amendment Method
- Definition: A data quality solution concept that relates an Amendment to its Specifications.
- SubClass Of: AmendmentConcept; DataQualityMethod
- Notes:
The AmendmentMethod in bdqffdq is a DQ Solutions level concept describing the relationship between a Specification (technical description of a test) and an Amendment (an enhancement in the context of resource type (SingleRecord or MultiRecord) and associated information elements).

EM(am) = {s | s ⊂ S ⋀ am ∈ AM}

********************

### AmendmentPolicy

- Name: bdqffdq:AmendmentPolicy
- Preferred Label: Amendment Policy
- Definition: A need concept that relates a UseCase to a set of supporting Amendments.
- SubClass Of: AmendmentConcept; Policy
- Notes:
A Data Quality needs level concept that describes how some Amendment relates to a UseCase. This relationship defines which amendments are supported by a given UseCase.

EP(u) = {am | am ⊂ AM ⋀ u ∈ U }

********************

### Assertion

- Name: bdqffdq:Assertion
- Preferred Label: Assertion
- Definition: A report concept expressing a statement about data quality assertion following some Specification produced by some implementation pertaining to some data resource.
- SubClass Of: ReportConcept
- Notes:
The Assertion type in bdqffdq is the fundamental concept that makes up a data quality report. Assertion can be any one of four types (represented as subClasses), Measure, Validation, Issue, and Amendement.  The assertion concept consists of a Specification (the technical description of a performed test), a data resource (initial values of input data expressed in terms of some controlled vocabulary), the mechanism (external service, actor, or code that performs the test), and some form of result.

********************

### Consulted

- Name: bdqffdq:Consulted
- Preferred Label: Acted Upon
- Definition: An information element, expressed in concrete terms, about which a data quality need examines in order to expresses assertions about the data quality in another Information Element.
- SubClass Of: InformationElement
- Notes:
An Information Element the content of which is examined to assert a result on one or more other Information Elements

********************

### Criterion

- Name: bdqffdq:Criterion
- Preferred Label: Criterion
- Definition: Rule against which data are evaluated for conformance to quality criteria.
- SubClass Of: FundamentalConcept; NeedConcept
- Notes:
General statement, for example: In a controlled vocabulary.  Composed with both Validations and Issues.

********************

### DataQualityDimension

- Name: bdqffdq:DataQualityDimension
- Preferred Label: Data Quality Dimension
- Definition: An aspect of data quality.
- SubClass Of: FundamentalConcept; NeedConcept
- Notes:
Describes the aspect of data quality (accuracy, precision, completeness, etc.) that a test examines. For example, [precision] in [coordinate precision of single records].  In the original framework only related to Measures, here may be related to any DataQualityNeed.

********************

### DataQualityMethod

- Name: bdqffdq:DataQualityMethod
- Preferred Label: Data Quality Method
- Definition: A solutions concept that relates a data quality need to a Specification.
- SubClass Of: SolutionsConcept
- Notes:
DataQualityMethods are associative entities that allow Specifications or data quality tests to be reused by supporting a many to many relationship between the two.

********************

### DataQualityNeed

- Name: bdqffdq:DataQualityNeed
- Preferred Label: Data Quality Need
- Definition: A data quality need concept that expresses what assertions may be made about data with respect to fitness for use.
- SubClass Of: NeedConcept
- Notes:
Subtypes of DataQualityNeed are the Test Types.  Data Quality Need appoximates the informal concept of Test as used in BDQ Core.

********************

### DataQualityProfile

- Name: bdqffdq:DataQualityProfile
- Preferred Label: Data Quality Profile
- Definition: A needs concept expressing the composition of Policies to satisfy a UseCase.
- SubClass Of: NeedConcept
- Notes:
Profile in bdqffdq is a data quality Needs level concept describing the UseCases that make up some data quality operation such as the behavior of a single actor or workflow producing the relevant assertions.  

DQP (u) = {dqp | dqp = mp(u) ⋃ vp(u) ⋃ ep(u), mp ∈ MP , vp ∈ VP , ep ∈ EP ⋀ u ∈ U }

********************

### DataQualityReport

- Name: bdqffdq:DataQualityReport
- Preferred Label: Data Quality Report
- Definition: A report concept comprising a set of data quality assertions.
- SubClass Of: ReportConcept
- Notes:
The DataQualityReport concept consists of a set of assertions (MeasureAssertions, ValidationAssertions, IssueAssertions and AmendmentAssertions) that represent the output of a workflow/actor run.  These assertions form an account of the fitness for use of a tested data set for a specified use, as produced by a Mechanism.

********************

### DataResource

- Name: bdqffdq:DataResource
- Preferred Label: Data Resource
- Definition: A thing to whch a data quality assertion applies.
- SubClass Of: ReportConcept
- Notes:
Describes a data resource containing terms from a controlled vocabulary such as (dwc) that can be related to information elements and represents the original values of the data operated on by an assertion test (i.e. an instance of dwc:Occurrence).  Ideally, DataResources have persistent GUIDs.

A data resource could be the oa:target of a oa:Annotation of which an Assertion is the oa:body.

DR = { dr | dr = < id, rt, v >, id ∈ I D, rt ∈ RT , (rt = sr ⋁ rt = ds) ⋀ v ∈ V }

********************

### Enhancement

- Name: bdqffdq:Enhancement
- Preferred Label: Enhancement
- Definition: Description of a means by which data could be improved.
- SubClass Of: AmendmentConcept; FundamentalConcept; NeedConcept
- Notes:
General statement, for example: Recommend replacement value from a controlled vocabulary

********************

### Implementation

- Name: bdqffdq:Implementation
- Preferred Label: Implementation
- Definition: A solutions concept that describes the portion of a Mechanism that carries out the proccess described in a particular Specification.
- SubClass Of: SolutionsConcept
- Notes:
The bdqffdq derived concept of an Implementation describes the relationship between a Specification (technical description of a test) and the mechanism that implements it.

I (s) = {m | m ⊂ M ⋀ s ∈ S}

********************

### ImprovementTarget

- Name: bdqffdq:ImprovementTarget
- Preferred Label: Improvement Target
- Definition: A specific data quality need for which a specific Amendment is intended to improve.
- SubClass Of: NeedConcept
- Notes:
The ImprovementTarget concept in bdqffdq describes which measures, issues, and validations are improved by some amendment. ImprovementTarget includes relationships between an Amendment and one or more Validations or Measures.

IT(am) = {me ⋃ va | me ∈ ME, va ∈ VA ⋀ am ∈ AM}

********************

### InformationElement

- Name: bdqffdq:InformationElement
- Preferred Label: Information Element
- Definition: A portion of data with which a Data Quality Need is concerned.
- SubClass Of: FundamentalConcept
- Notes:
An information element identifies a portion of data to which a test pertains.  The information element in bdqffdq can be represented as a single or composite element that consists of one or more terms from a controlled vocabulary (fields actedUpon or consulted by an assertion test) that identifies concepts in data relevant to a UseCase.  An abstraction or a concrete term that represents relevant content (e.g., coordinates; dwc.decimalLatitude, dwc:decimalLongitude).

********************

### Issue

- Name: bdqffdq:Issue
- Preferred Label: Issue
- Definition: A data quality need that expresses how quality problems may be identified in data.
- SubClass Of: DataQualityNeed; IssueConcept
- Notes:
Added to the original framework.  Inverse of Contextualized Criterion in the original framework.  Describes an instance of the issue concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.  Describes criteria by which data which lack quality for some purpose may be identified.  An issue is phrased in a negative sense, and approximates an inverse of a Validation.  An Issue identifies data that lack or may lack quality.  An Issue may flag a POTENTIAL_ISSUE that would need further review to determine if the data have quality for some purpose,  If the conditions described by an issue are identified by a test, the Problem Assertion result will be either IS_ISSUE or POTENTIAL_ISSUE, if no issue is found with the data the result will be NOT_ISSUE.  NOT_ISSUE, unlike COMPLIANT for a Validation, does not assert that data are fit for some purpose.    An Issue is the data quality needs concept that parallels a IssueMethod at the solutions level, and a IssueAssertion at the report level.   

IS = { is | is = < ie, c, rt >, ie ∈ IE, c ∈ ∁C ⋀ rt ∈ RT }

********************

### IssueAssertion

- Name: bdqffdq:IssueAssertion
- Preferred Label: Issue Assertion
- Definition: An assertion expressing the result of an implementation evaluating an issue for a particular data quality need in a particular data resource.
- SubClass Of: Assertion; IssueConcept
- Notes:
The data quality report concept describing a the result of a test in the negative, that is identifying the potential absence of data quality. 

If a problem was found the ResponseResult is expected to carry a a value of IS_ISSUE, if a potential problem was found that needs human review the ResponseResult is expected to be of POTENTIAL_ISSUE, otherwise if the ResponseStatus is RUN_HAS_RESULT,  the ResponseResult is expected to be NOT_ISSUE.

********************

### IssueMethod

- Name: bdqffdq:IssueMethod
- Preferred Label: Issue Method
- Definition: A data quality solution concept that relates an Issue to its Specifications.
- SubClass Of: DataQualityMethod; IssueConcept
- Notes:
The IssueMethod in bdqffdq is a data quality Solutions level concept describing the relationship between a Specification (technical description of a test) and an Issue (a Criterion in the context of resource type (SingleRecord or MultiRecord) and associated information elements).

********************

### IssuePolicy

- Name: bdqffdq:IssuePolicy
- Preferred Label: Issue Policy
- Definition: A need concept that relates a UseCase to a set of supporting Issues.
- SubClass Of: IssueConcept; Policy
- Notes:
The IssuePolicy in bdqffdq is a data quality Needs level concept that describes how some Issue relates to a UseCase. This relationship defines which Issues are supported by a given UseCase.

********************

### Measure

- Name: bdqffdq:Measure
- Preferred Label: Measure
- Definition: A data quality need that expresses how the fitness of data for some use may be measured.
- SubClass Of: DataQualityNeed; MeaurementConcept
- Notes:
Contextualized Dimension in the original framework Describes an instance of the measure concept in terms of the associated information elements from some controlled vocabulary (fields ActedUpon or Consulted), and a ResourceType of SingleRecord or MultiRecord. 

Describes the criteria for measuring an aspect of data quality related to some data quality need.   May be criteria for determining that data are COMPLETE or NOT_COMPLETE, or may be criteria for asserting a numeric measurement.  COMPLETE or NOT_COMPLETE measures are fundamental to data quality control, as set of data are filtered to the subset of data that have quality for some need if all records are COMPLETE for all pertenent Measures. 

A Measure is the data quality needs concept that parallels a MeasurementMethod at the solutions level, and a MeasurementAssertion at the report level.

ME = { me | me =< ie, d, rt >, ie ∈ IE, d ∈ D ⋀ rt ∈ RT }
also acceptable measure
AM(me) = {va | me ∈ C D ⋀ va ⊂ C C}

********************

### MeasurementAssertion

- Name: bdqffdq:MeasurementAssertion
- Preferred Label: Measurement Assertion
- Definition: An assertion expressing the result of an implementation measuring a particular data quality need in a particular data resource.
- SubClass Of: Assertion; MeaurementConcept
- Notes:
The MeasurementAssertion is a report level concept that describes the results of the execution of of a test that performs a MeasurementMethod following some Specification to assess some data quality Measurement. 

In bdqffdq, the MeasurementAssertion is expected to carry a ResponseResult of COMPLETE or NOT_COMPLETE or a numeric measured value value (e.g. a measure of dwc:eventDate duration in seconds).

DQM(dr) = {dqm | dqm =< me, s, m, r >, me ∈ ME, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

********************

### MeasurementMethod

- Name: bdqffdq:MeasurementMethod
- Preferred Label: Measurement Method
- Definition: A data quality solution concept that relates a Measure to its Specifications.
- SubClass Of: DataQualityMethod; MeaurementConcept
- Notes:
The MeasurementMethod in bdqffdq is a data quality Solutions level concept describing the relationship between a Specification (technical description of a test) and a Measurement (a dimension in the context of resource type (SingleRecord or MultiRecord) and associated information elements).

MM(me) = {s | s ⊂ S ⋀ me ∈ ME}

********************

### MeasurementPolicy

- Name: bdqffdq:MeasurementPolicy
- Preferred Label: Measurement Policy
- Definition: A need concept that relates a UseCase to a set of supporting Measures.
- SubClass Of: MeaurementConcept; Policy
- Notes:
The MeasurementPolicy in bdqffdq is a data quality Needs level concept that describes how some Measurement relates to a UseCase. This relationship defines which measures are supported by a given UseCase.

MP(u) = {me | me ⊂ ME ⋀ u ∈ U }

********************

### Mechanism

- Name: bdqffdq:Mechanism
- Preferred Label: Mechanism
- Definition: An entity that can execute data quality methods.
- SubClass Of: FundamentalConcept; SolutionsConcept
- Notes:
Mechanisms may produce data quality reports as products.    

The bdqffdq concept of mechanism describes the entity that performs an assertion test (code, external service, actor, etc.). Tied to a Specification via the concept of an Implementation.

********************

### Parameter

- Name: bdqffdq:Parameter
- Preferred Label: Parameter
- Definition: A value that, when provided to a test Specification changes the behavior of the test in a defined manner.
- SubClass Of: SolutionsConcept
- Notes:
An extension to the original fitness for use framework as described in Veiga et al., 2017.

********************

### Policy

- Name: bdqffdq:Policy
- Preferred Label: Policy
- Definition: The set of data quality Needs for a UseCase
- SubClass Of: NeedConcept
- Notes:
Composition of data quality Needs into UseCases

********************

### ResourceType

- Name: bdqffdq:ResourceType
- Preferred Label: Resource Type
- Definition: Category of things that are data objects about which data quality assertions may be made.
- SubClass Of: FundamentalConcept
- Notes:
In bdqffdq the concept of ResourceType has instances for SingleRecord or MultiRecord

********************

### ResponseQualifier

- Name: bdqffdq:ResponseQualifier
- Preferred Label: Response Qualifier
- Definition: A report concept to which additional assertions providing additional information beyond that of ResponseResult from the result of the execution of the Specification of a data quality need are attached.
- SubClass Of: ReportConcept
- Notes:
Intended as an extension point for qualifying information about uncertainty or ambiguity.

********************

### ResponseResult

- Name: bdqffdq:ResponseResult
- Preferred Label: Response.result
- Definition: A report concept to which a controlled vocabulary assertions about the result of the execution of the Specification of a data quality need are attached.
- SubClass Of: ReportConcept
- Notes:
For Validations, response results may be COMPLIANT, or NOT_COMPLIANT.  For Measures, response result objects may be COMPLETE or NOT_COMPLETE.  For Issues, Response results may be IS_ISSUE, POTENTIAL_ISSUE, or NOT_ISSUE.  See the bdq: vocabulary.  Measures may also use a numeric data property.  Amendments assert a string data property.

The report ResponseResult in bdqffdq is represented as a value or a result object for MeasureAsssertions, just a result object for ValidationAssertions and values for changes propsed in AmendmentAssertions.

********************

### ResponseStatus

- Name: bdqffdq:ResponseStatus
- Preferred Label: Response.status
- Definition: A report concept expressing controlled vocabulary values about the exit state of an execution process of a data quality Specification by an implementation.
- SubClass Of: ReportConcept
- Notes:
The ResponseStatus is metadata, indicating if data should be present in a ResponseResult.   Any assertion may have the values INTERNAL_PREREQUISITES_NOT_MET of EXTERNAL_PREREQUISITES_NOT_MET, indicating that no value would be present in the accompanying ResponseResult.  Other values depend on the Assertion type.  Thes would be RUN_HAS_RESULT for a Validation, Measure, or Isssue, and, FILLED_IN, AMENDED, or NOT_AMENDED for an Amendment.  Additional metadata qualifying the assertion in a ReqponseResult, such as statements of uncertainy or ambiguity may be placed in the ResponseQualifier

********************

### Specification

- Name: bdqffdq:Specification
- Preferred Label: Specification
- Definition: A specific statement about how to evaluate a data quality need.
- SubClass Of: FundamentalConcept; SolutionsConcept
- Notes:
A Specification is a technical desription of an assertion test.  A Specification is expected to have the following properies:  (1) Expected Response, (2) Authorities and Parameters.

********************

### UseCase

- Name: bdqffdq:UseCase
- Preferred Label: Use Case
- Definition: A needs concept expressing a purpose to which data are put for which the data must have quality for the result to have meaning and reliability.
- SubClass Of: FundamentalConcept; NeedConcept
- Notes:
The UseCase concept in bdqffdq describes some data quality control UseCase. The Amendment, Measurement and Validation policies that make up a UseCase define which assertions cover a given UseCase.  An example of a UseCase could be "Check for internal consistency of dates", with validation policies for checking consistency between atomic date fields and an Amendment such as "eventDate filled in from verbatim".  UseCases in bdqffdq are not the same as UseCases in the software engineering sense, but are similar bdqffdq formal statements derived from analyis of user stories.

********************

### Validation

- Name: bdqffdq:Validation
- Preferred Label: Validation
- Definition: A data quality need that expreses how data may be evaluated for fitness for use.
- SubClass Of: DataQualityNeed; ValidationConcept
- Notes:
ContextualizedCriterion in the original framework.  Describes the criteria for determining compliance of data to fill some data quality need.  A description of a criterion applied to an information element for some resource type.   Describes an instance of the criterion concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.  

Validations are phrased in a positive sense, they identify data which has quality for some need.  For example: The value of basisOfRecord of single records must be in the controlled vocabulary.   

A Validation is the data quality needs concept that parallels a ValidationMethod at the solutions level, and a ValidationAssertion at the report level.  ValidationAssertions may specify a result that is COMPLIANT, where the data has quality, or NOT_COMPLIANT, where the data lacks quality for some use.  

VA = { va | va = < ie, c, rt >, ie ∈ IE, c ∈ C ⋀ rt ∈ RT }

********************

### ValidationAssertion

- Name: bdqffdq:ValidationAssertion
- Preferred Label: Validation Assertion
- Definition: An assertion expressing the result of an implementation validating compliance with a a particular data quality need in a particular data resource.
- SubClass Of: Assertion; ValidationConcept
- Notes:
The ValidationAssertion is a report level concept that describes the results of the execution of of a test that performs a ValidationMethod following some Specification to assess the validity of some data with respect to the Criteria of some Validation. 

The ValidationAssertion concept in bdqffdq is expected to carry a a ResponseResult of COMPLIANT or NON_COMPLIANT.

DQV(dr) = {dqv | dqv = < va, s, m, r >, va ∈ VA, s ∈ S, m ∈ M , r ∈ R ⋀ dr ∈ DR}

********************

### ValidationMethod

- Name: bdqffdq:ValidationMethod
- Preferred Label: Validation Method
- Definition: A data quality solution concept that relates an Validation to its Specifications.
- SubClass Of: DataQualityMethod; ValidationConcept
- Notes:
The ValidationMethod in bdqffdq is a data quality Solutions level concept describing the relationship between a Specification (technical description of a test) and a Validation (a Criterion in the context of resource type (SingleRecord or MultiRecord) and associated information elements).

VM(va) = {s | s ⊂ S ⋀ va ∈ VA}

********************

### ValidationPolicy

- Name: bdqffdq:ValidationPolicy
- Preferred Label: Validation Policy
- Definition: A need concept that relates a UseCase to a set of supporting Validations.
- SubClass Of: Policy; ValidationConcept
- Notes:
The ValidationPolicy in bdqffdq is a data quality Needs level concept that describes how some Validation relates to a UseCase. This relationship defines which Validations are needed to identify quality in a given UseCase.

VP (u) = {va | va ⊂ VA ⋀ u ∈ U }

********************

## ObjectProperty terms
### forAmendment

- Name: bdqffdq:forAmendment
- Preferred Label: for Amendment
- Definition: Relates an AmendmentMethod to an Amendment.
- SubClass Of: amendmentProperty; forDataQualityNeed
- Notes:
Use to link AmendmentMethods to Amendments.  Describes the relationship between an AmendmentMethod (solutions) and an Amendment (needs).

********************

### forIssue

- Name: bdqffdq:forIssue
- Preferred Label: for Issue
- Definition: Relates an IssuetMethod to an Issue.
- SubClass Of: forDataQualityNeed; issueProperty
- Notes:
Use to link IssueMethods to Issues.  Describes the relationship between a IssueMethod (solutions) in bdqffdq and an Issue (needs).  Paralell concepts are forAmendment, forValidation, forMeasure.

********************

### forMeasure

- Name: bdqffdq:forMeasure
- Preferred Label: for Measure
- Definition: Relates an MeasurementMethod to a Measure.
- SubClass Of: forDataQualityNeed; measurementProperty
- Notes:
Use to link MeasurementMethods (solutions) to Measures (needs).   Paralell concepts are forAmendment, forValidation, forIssue.

********************

### forValidation

- Name: bdqffdq:forValidation
- Preferred Label: for Validation
- Definition: Relates an ValidationMethod to a Validation.
- SubClass Of: forDataQualityNeed; validationProperty
- Notes:
Use to link ValidationMethods to Validations.  Describes the relationship between a ValidationMethod (solutions) and a Validation (needs).   Paralell concepts are forAmendment, forMeasure, and forIssue.

********************

### hasActedUponInformationElement

- Name: bdqffdq:hasActedUponInformationElement
- Preferred Label: has Acted Upon Information Element
- Definition: Describes the ActedUpon InformationElements assessed by a DataQualityNeed about which Assertions arising from the DataQualityNeed would apply.
- SubClass Of: hasInformationElement
- Notes:
Provides a relationship between bdqffdq concepts and the information elements that are ActedUpon in a test.

********************

### hasConsultedInformationElement

- Name: bdqffdq:hasConsultedInformationElement
- Preferred Label: has Consulted Information Element
- Definition: Describes the InformationElements assessed by a DataQualityNeed in order to make Assertions concerning ActedUpon InformationElements.
- SubClass Of: hasInformationElement
- Notes:
Provides a relationship between bdqffdq concepts and the information elements that are Consulted, but not ActedUpon in a test.

********************

### hasCriterion

- Name: bdqffdq:hasCriterion
- Preferred Label: has Criterion
- Definition: The Criterion under which a Validation or Issue assesses for data quality.
- SubClass Of: issueProperty; validationProperty
- Notes:
Used to link the derived concept of a Validation to the fundamental concept of a Criterion.

********************

### hasDataQualityDimension

- Name: bdqffdq:hasDataQualityDimension
- Preferred Label: has Data Quality Dimension
- Definition: The DataQualityDimension to which a DataQualityNeed Applies.
- SubClass Of: amendmentProperty; issueProperty; measurementProperty; validationProperty
- Notes:
Used to link a derived concept of a DataQualityNeed (a test, that is a Measure, Validation, Amendment, or Issue) to the fundamental concept of a DataQualityDimension.  For a Measure, the dimension of data quality measured.   For a Validation or Issue, the dimension of data quality assessed.  For an Amendment, the dimension of data quality to be improved.  

Under the original formulation of the Framework, only Measures have Dimensions.

********************

### hasEnhancement

- Name: bdqffdq:hasEnhancement
- Preferred Label: has Enhancement
- Definition: The Enhancement that describes how an Amendment may propose changes to improve data quality.
- SubClass Of: amendmentProperty
- Notes:
Used to link the derived property of an Amendment to the Fundamental property of an Enhancement.

********************

### hasInformationElement

- Name: bdqffdq:hasInformationElement
- Preferred Label: has Information Element
- Definition: Describes the InformationElements assessed by a DataQualityNeed.
- SubClass Of: amendmentProperty; issueProperty; measurementProperty; validationProperty
- Notes:
Provides a relationship between DataQualityNeeds concepts and Information elements. For example, Validation uses this property along with hasResourceType to define a criterion in the context of related information elements.

Subtypes hasActedUponInformationElement and hasConsultedInformationElement allow data quality needs to be related to specific information element terms in a way that allows data quality reports to distinguish for consumers which information elements a test makes assertions about (and which only informed that assertion).

********************

### hasResponseQualifier

- Name: bdqffdq:hasResponseQualifier
- Preferred Label: has Response Qualifier
- Definition: ResponseQualifier object asserted by an Assertion.
- SubClass Of: reportProperty
- Notes:
Optional extension point, could be used to add structured information about uncertainty.

********************

### hasResponseResult

- Name: bdqffdq:hasResponseResult
- Preferred Label: has Response Result
- Definition: ResponseResult object asserted by an Assertion.
- SubClass Of: reportProperty
- Notes:
Used in the DQ Report concept to describe response result objects. For example, values could be bdqffdq:COMPLIANT or bdqffdq:NOT_COMPLIANT for ValidationAssertions.   ValidationAssertions and IssueAssertions have ResponseResults as objects.  AmendmentAssertions have ResponseResults that are data properties, so they are not expected to use this object property.  MeasurementAssertion ResponseResults may be objects or data.  

 If Response.results are not objects, use the datatype property hasResponseResultValue

********************

### hasResponseStatus

- Name: bdqffdq:hasResponseStatus
- Preferred Label: has Response Status
- Definition: ResponseStatus object asserted by an Assertion.
- SubClass Of: reportProperty
- Notes:
Used in the DQ Report concept to describe response status.  For example, in the case of a ValidationAssertion ResponseStatus values could be bdqffdq:RUN_HAS_RESULT or bdqffdq:INTERNAL_PREREQUISITES_NOT_MET, or bdqffdq:EXTERNAL_PREREQISITES_NOT_MET.   Similarly, AmendmentAssertions can assert ResponesStatus objects including bdqffdq:AMENDED or bdqffdq:FILLED_IN.  

ResponseStatus is always an object, unlike ResponseResult, where either the object property hasResponseResult or the data property hasResponseResultValue may apply.

********************

### targetedValidation

- Name: bdqffdq:targetedValidation
- Preferred Label: targeted Validation
- Definition: Validation where the data conformance with needs may be improved by accepting proposals from an Amendment via an ImprovementTarget.
- SubClass Of: http://www.w3.org/2002/07/owl#topObjectProperty
- Notes:
Relates an improvement target to a Validation.  Describes the relationship between an improvement target and a Validation.

********************

## Cite BDQ Core

**To cite BDQ Core in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889

**To cite the standard document upon which this page is built, use the following:**

BDQ Core Maintenance Group 2024. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/bdq/doc/list/

**To cite this document specifically, use the following:**
<!--- TODO: move citation elements to document_configuration.yaml --->
BDQ Core Maintenance Group. 2024. BDQ Core Quick Reference Guide. Biodiversity Information Standards (TDWG). https://bdq.tdwg.org/terms/

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Quick Reference Guide to the bdqffdq Ontology.. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)

