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

[AbstractInformationElement](AbstractInformationElement)
[ActedUpon](ActedUpon)
[Amendment](Amendment)
[AmendmentAssertion](AmendmentAssertion)
[AmendmentConcept](AmendmentConcept)
[AmendmentMethod](AmendmentMethod)
[AmendmentPolicy](AmendmentPolicy)
[Assertion](Assertion)
[Consulted](Consulted)
[Criterion](Criterion)
[DataQualityDimension](DataQualityDimension)
[DataQualityMethod](DataQualityMethod)
[DataQualityNeed](DataQualityNeed)
[DataQualityProfile](DataQualityProfile)
[DataQualityReport](DataQualityReport)
[DataResource](DataResource)
[Enhancement](Enhancement)
[FundamentalConcept](FundamentalConcept)
[Implementation](Implementation)
[ImprovementTarget](ImprovementTarget)
[InformationElement](InformationElement)
[Issue](Issue)
[IssueAssertion](IssueAssertion)
[IssueConcept](IssueConcept)
[IssueMethod](IssueMethod)
[IssuePolicy](IssuePolicy)
[Measure](Measure)
[MeasurementAssertion](MeasurementAssertion)
[MeasurementMethod](MeasurementMethod)
[MeasurementPolicy](MeasurementPolicy)
[MeaurementConcept](MeaurementConcept)
[Mechanism](Mechanism)
[NeedConcept](NeedConcept)
[Parameter](Parameter)
[Policy](Policy)
[ReportConcept](ReportConcept)
[ResourceType](ResourceType)
[ResponseQualifier](ResponseQualifier)
[ResponseResult](ResponseResult)
[ResponseStatus](ResponseStatus)
[SolutionsConcept](SolutionsConcept)
[Specification](Specification)
[UseCase](UseCase)
[Validation](Validation)
[ValidationAssertion](ValidationAssertion)
[ValidationConcept](ValidationConcept)
[ValidationMethod](ValidationMethod)
[ValidationPolicy](ValidationPolicy)
## Class terms
###bdqffdq:AbstractInformationElement

- Name: bdqffdq:AbstractInformationElement
- Preferred Label: Abstract Information Element
- Definition: An InformationElement described in abstract terms and not linked with one or more concrete terms.
- SubClass Of: InformationElement

********************

###bdqffdq:ActedUpon

- Name: bdqffdq:ActedUpon
- Preferred Label: Acted Upon
- Definition: An information element, expressed in concrete terms, about which a data quality need expresses assertions about the data quality in that element.
- SubClass Of: InformationElement

********************

###bdqffdq:Amendment

- Name: bdqffdq:Amendment
- Preferred Label: Amendment
- Definition: A data quality need that expresses how proposals may be made to improve the fittnes for use of data.
- SubClass Of: AmendmentConcept; DataQualityNeed

********************

###bdqffdq:AmendmentAssertion

- Name: bdqffdq:AmendmentAssertion
- Preferred Label: Amendment Assertion
- Definition: An assertion expressing the result of an implementation evaluating an amendment supporting a particular data quality need to improve a particular data resource.
- SubClass Of: AmendmentConcept; Assertion

********************

###bdqffdq:AmendmentMethod

- Name: bdqffdq:AmendmentMethod
- Preferred Label: Amendment Method
- Definition: A data quality solution concept that relates an Amendment to its Specifications.
- SubClass Of: AmendmentConcept; DataQualityMethod

********************

###bdqffdq:AmendmentPolicy

- Name: bdqffdq:AmendmentPolicy
- Preferred Label: Amendment Policy
- Definition: A need concept that relates a UseCase to a set of supporting Amendments.
- SubClass Of: AmendmentConcept; Policy

********************

###bdqffdq:Assertion

- Name: bdqffdq:Assertion
- Preferred Label: Assertion
- Definition: A report concept expressing a statement about data quality assertion following some Specification produced by some implementation pertaining to some data resource.
- SubClass Of: ReportConcept

********************

###bdqffdq:Consulted

- Name: bdqffdq:Consulted
- Preferred Label: Acted Upon
- Definition: An information element, expressed in concrete terms, about which a data quality need examines in order to expresses assertions about the data quality in another Information Element.
- SubClass Of: InformationElement

********************

###bdqffdq:Criterion

- Name: bdqffdq:Criterion
- Preferred Label: Criterion
- Definition: Rule against which data are evaluated for conformance to quality criteria.
- SubClass Of: FundamentalConcept; NeedConcept

********************

###bdqffdq:DataQualityDimension

- Name: bdqffdq:DataQualityDimension
- Preferred Label: Data Quality Dimension
- Definition: An aspect of data quality.
- SubClass Of: FundamentalConcept; NeedConcept

********************

###bdqffdq:DataQualityMethod

- Name: bdqffdq:DataQualityMethod
- Preferred Label: Data Quality Method
- Definition: A solutions concept that relates a data quality need to a Specification.
- SubClass Of: SolutionsConcept

********************

###bdqffdq:DataQualityNeed

- Name: bdqffdq:DataQualityNeed
- Preferred Label: Data Quality Need
- Definition: A data quality need concept that expresses what assertions may be made about data with respect to fitness for use.
- SubClass Of: NeedConcept

********************

###bdqffdq:DataQualityProfile

- Name: bdqffdq:DataQualityProfile
- Preferred Label: Data Quality Profile
- Definition: A needs concept expressing the composition of Policies to satisfy a UseCase.
- SubClass Of: NeedConcept

********************

###bdqffdq:DataQualityReport

- Name: bdqffdq:DataQualityReport
- Preferred Label: Data Quality Report
- Definition: A report concept comprising a set of data quality assertions.
- SubClass Of: ReportConcept

********************

###bdqffdq:DataResource

- Name: bdqffdq:DataResource
- Preferred Label: Data Resource
- Definition: A thing to whch a data quality assertion applies.
- SubClass Of: ReportConcept

********************

###bdqffdq:Enhancement

- Name: bdqffdq:Enhancement
- Preferred Label: Enhancement
- Definition: Description of a means by which data could be improved.
- SubClass Of: AmendmentConcept; FundamentalConcept; NeedConcept

********************

###bdqffdq:Implementation

- Name: bdqffdq:Implementation
- Preferred Label: Implementation
- Definition: A solutions concept that describes the portion of a Mechanism that carries out the proccess described in a particular Specification.
- SubClass Of: SolutionsConcept

********************

###bdqffdq:ImprovementTarget

- Name: bdqffdq:ImprovementTarget
- Preferred Label: Improvement Target
- Definition: A specific data quality need for which a specific Amendment is intended to improve.
- SubClass Of: NeedConcept

********************

###bdqffdq:InformationElement

- Name: bdqffdq:InformationElement
- Preferred Label: Information Element
- Definition: A portion of data with which a Data Quality Need is concerned.
- SubClass Of: FundamentalConcept

********************

###bdqffdq:Issue

- Name: bdqffdq:Issue
- Preferred Label: Issue
- Definition: A data quality need that expresses how quality problems may be identified in data.
- SubClass Of: DataQualityNeed; IssueConcept

********************

###bdqffdq:IssueAssertion

- Name: bdqffdq:IssueAssertion
- Preferred Label: Issue Assertion
- Definition: An assertion expressing the result of an implementation evaluating an issue for a particular data quality need in a particular data resource.
- SubClass Of: Assertion; IssueConcept

********************

###bdqffdq:IssueMethod

- Name: bdqffdq:IssueMethod
- Preferred Label: Issue Method
- Definition: A data quality solution concept that relates an Issue to its Specifications.
- SubClass Of: DataQualityMethod; IssueConcept

********************

###bdqffdq:IssuePolicy

- Name: bdqffdq:IssuePolicy
- Preferred Label: Issue Policy
- Definition: A need concept that relates a UseCase to a set of supporting Issues.
- SubClass Of: IssueConcept; Policy

********************

###bdqffdq:Measure

- Name: bdqffdq:Measure
- Preferred Label: Measure
- Definition: A data quality need that expresses how the fitness of data for some use may be measured.
- SubClass Of: DataQualityNeed; MeaurementConcept

********************

###bdqffdq:MeasurementAssertion

- Name: bdqffdq:MeasurementAssertion
- Preferred Label: Measurement Assertion
- Definition: An assertion expressing the result of an implementation measuring a particular data quality need in a particular data resource.
- SubClass Of: Assertion; MeaurementConcept

********************

###bdqffdq:MeasurementMethod

- Name: bdqffdq:MeasurementMethod
- Preferred Label: Measurement Method
- Definition: A data quality solution concept that relates a Measure to its Specifications.
- SubClass Of: DataQualityMethod; MeaurementConcept

********************

###bdqffdq:MeasurementPolicy

- Name: bdqffdq:MeasurementPolicy
- Preferred Label: Measurement Policy
- Definition: A need concept that relates a UseCase to a set of supporting Measures.
- SubClass Of: MeaurementConcept; Policy

********************

###bdqffdq:Mechanism

- Name: bdqffdq:Mechanism
- Preferred Label: Mechanism
- Definition: An entity that can execute data quality methods.
- SubClass Of: FundamentalConcept; SolutionsConcept

********************

###bdqffdq:Parameter

- Name: bdqffdq:Parameter
- Preferred Label: Parameter
- Definition: A value that, when provided to a test Specification changes the behavior of the test in a defined manner.
- SubClass Of: SolutionsConcept

********************

###bdqffdq:Policy

- Name: bdqffdq:Policy
- Preferred Label: Policy
- Definition: The set of data quality Needs for a UseCase
- SubClass Of: NeedConcept

********************

###bdqffdq:ResourceType

- Name: bdqffdq:ResourceType
- Preferred Label: Resource Type
- Definition: Category of things that are data objects about which data quality assertions may be made.
- SubClass Of: FundamentalConcept

********************

###bdqffdq:ResponseQualifier

- Name: bdqffdq:ResponseQualifier
- Preferred Label: Response Qualifier
- Definition: A report concept to which additional assertions providing additional information beyond that of ResponseResult from the result of the execution of the Specification of a data quality need are attached.
- SubClass Of: ReportConcept

********************

###bdqffdq:ResponseResult

- Name: bdqffdq:ResponseResult
- Preferred Label: Response.result
- Definition: A report concept to which a controlled vocabulary assertions about the result of the execution of the Specification of a data quality need are attached.
- SubClass Of: ReportConcept

********************

###bdqffdq:ResponseStatus

- Name: bdqffdq:ResponseStatus
- Preferred Label: Response.status
- Definition: A report concept expressing controlled vocabulary values about the exit state of an execution process of a data quality Specification by an implementation.
- SubClass Of: ReportConcept

********************

###bdqffdq:Specification

- Name: bdqffdq:Specification
- Preferred Label: Specification
- Definition: A specific statement about how to evaluate a data quality need.
- SubClass Of: FundamentalConcept; SolutionsConcept

********************

###bdqffdq:UseCase

- Name: bdqffdq:UseCase
- Preferred Label: Use Case
- Definition: A needs concept expressing a purpose to which data are put for which the data must have quality for the result to have meaning and reliability.
- SubClass Of: FundamentalConcept; NeedConcept

********************

###bdqffdq:Validation

- Name: bdqffdq:Validation
- Preferred Label: Validation
- Definition: A data quality need that expreses how data may be evaluated for fitness for use.
- SubClass Of: DataQualityNeed; ValidationConcept

********************

###bdqffdq:ValidationAssertion

- Name: bdqffdq:ValidationAssertion
- Preferred Label: Validation Assertion
- Definition: An assertion expressing the result of an implementation validating compliance with a a particular data quality need in a particular data resource.
- SubClass Of: Assertion; ValidationConcept

********************

###bdqffdq:ValidationMethod

- Name: bdqffdq:ValidationMethod
- Preferred Label: Validation Method
- Definition: A data quality solution concept that relates an Validation to its Specifications.
- SubClass Of: DataQualityMethod; ValidationConcept

********************

###bdqffdq:ValidationPolicy

- Name: bdqffdq:ValidationPolicy
- Preferred Label: Validation Policy
- Definition: A need concept that relates a UseCase to a set of supporting Validations.
- SubClass Of: Policy; ValidationConcept

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

