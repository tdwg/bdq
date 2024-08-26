---
title:  TDWG BDQ Core Framework for data quality
geometry: margin=1cm
titlepage: true
---
Ontology Terms forming the BDQ Core Framework For Data Quality.

- [Classes](#Class-terms)
- [Named Individuals](#NamedIndividual-terms)
- [Object Properties](#ObjectProperty-terms)
- [Data Properties](#DataProperty-terms)

Alphabetical Index of classes

- [https://rs.tdwg.org/bdqffdq/terms#Parameter](#https//rs.tdwg.org/bdqffdq/terms#Parameter) 
- [bdqffdq:ActedUpon](#bdqffdqActedUpon) InformationElement
- [bdqffdq:Amendmenent](#bdqffdqAmendmenent) DataQualityNeed
- [bdqffdq:AmendmentAssertion](#bdqffdqAmendmentAssertion) Assertion
- [bdqffdq:AmendmentMethod](#bdqffdqAmendmentMethod) DataQualityMethod
- [bdqffdq:AmendmentPolicy](#bdqffdqAmendmentPolicy) NeedConcept
- [bdqffdq:Assertion](#bdqffdqAssertion) ReportConcept
- [bdqffdq:Consulted](#bdqffdqConsulted) InformationElement
- [bdqffdq:ContextualizedCriterion](#bdqffdqContextualizedCriterion) NeedConcept
- [bdqffdq:ContextualizedDimension](#bdqffdqContextualizedDimension) NeedConcept
- [bdqffdq:ContextualizedEnhancement](#bdqffdqContextualizedEnhancement) NeedConcept
- [bdqffdq:ContextualizedIssue](#bdqffdqContextualizedIssue) NeedConcept
- [bdqffdq:DataQualityDimension](#bdqffdqDataQualityDimension) 
- [bdqffdq:DataQualityMethod](#bdqffdqDataQualityMethod) SolutionsConcept
- [bdqffdq:DataQualityNeed](#bdqffdqDataQualityNeed) NeedConcept
- [bdqffdq:DataQualityReport](#bdqffdqDataQualityReport) ReportConcept
- [bdqffdq:DataResource](#bdqffdqDataResource) ReportConcept
- [bdqffdq:Implementation](#bdqffdqImplementation) SolutionsConcept
- [bdqffdq:ImprovementTarget](#bdqffdqImprovementTarget) NeedConcept
- [bdqffdq:InformationElement](#bdqffdqInformationElement) 
- [bdqffdq:Issue](#bdqffdqIssue) DataQualityNeed
- [bdqffdq:IssueAssertion](#bdqffdqIssueAssertion) Assertion
- [bdqffdq:IssueMethod](#bdqffdqIssueMethod) DataQualityMethod
- [bdqffdq:Measure](#bdqffdqMeasure) DataQualityNeed
- [bdqffdq:MeasurementAssertion](#bdqffdqMeasurementAssertion) Assertion
- [bdqffdq:MeasurementMethod](#bdqffdqMeasurementMethod) DataQualityMethod
- [bdqffdq:MeasurementPolicy](#bdqffdqMeasurementPolicy) NeedConcept
- [bdqffdq:Mechanism](#bdqffdqMechanism) SolutionsConcept
- [bdqffdq:NeedConcept](#bdqffdqNeedConcept) 
- [bdqffdq:ProblemPolicy](#bdqffdqProblemPolicy) NeedConcept
- [bdqffdq:Profile](#bdqffdqProfile) NeedConcept
- [bdqffdq:ReportConcept](#bdqffdqReportConcept) 
- [bdqffdq:ResourceType](#bdqffdqResourceType) 
- [bdqffdq:Result](#bdqffdqResult) ReportConcept
- [bdqffdq:ResultStatus](#bdqffdqResultStatus) ReportConcept
- [bdqffdq:SolutionsConcept](#bdqffdqSolutionsConcept) 
- [bdqffdq:Specification](#bdqffdqSpecification) NeedConcept
- [bdqffdq:UseCase](#bdqffdqUseCase) NeedConcept
- [bdqffdq:Validation](#bdqffdqValidation) DataQualityNeed
- [bdqffdq:ValidationAssertion](#bdqffdqValidationAssertion) Assertion
- [bdqffdq:ValidationMethod](#bdqffdqValidationMethod) DataQualityMethod
- [bdqffdq:ValidationPolicy](#bdqffdqValidationPolicy) NeedConcept
********************

# Class terms

********************

## https://rs.tdwg.org/bdqffdq/terms#Parameter

### Name

https://rs.tdwg.org/bdqffdq/terms#Parameter

### Preferred Label

'Parameter'

### Label

'Parameter'

### Type

Class

### Definition

nan


### Comment

nan


********************

## bdqffdq:DataQualityDimension

### Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityDimension

### Preferred Label

'Data Quality Dimension'

### Label

'Data Quality Dimension'

### Type

Class

### Definition

'The aspects of data quality  that a test examines.'


### Comment

'Describes the aspect of data quality (accuracy, precision, completeness, etc.) that a test examines. For example, 'precision' in 'coordinate precision of single records'.'


********************

## bdqffdq:InformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/InformationElement

### Preferred Label

'Information Element'

### Label

'Information Element'

### Type

Class

### Definition

nan


### Comment

'An information element identifies a portion of data to which a test pertains.  The information element in FFDQ can be represented as a single or composite element that consists of one or more terms from a controlled vocabulary (fields actedUpon or consulted by an assertion test) that identifies concepts in data relevant to a use case.  An abstraction or a concrete term that represents relevant content (e.g., coordinates; dwc.decimalLatitude, dwc:decimalLongitude).'


********************

## bdqffdq:NeedConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

### Preferred Label

'Need Concept'

### Label

'Need Concept'

### Type

Class

### Definition

'Category of concepts forming the Needs layer of the fittness for use framework.'


### Comment

nan


********************

## bdqffdq:ReportConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

### Preferred Label

'Report Concept'

### Label

nan

### Type

Class

### Definition

'Category of concepts forming the Report layer of the fittness for use framework.'


### Comment

nan


********************

## bdqffdq:ResourceType

### Name

https://rs.tdwg.org/bdqffdq/terms/ResourceType

### Preferred Label

'Resource Type'

### Label

'Resource Type'

### Type

Class

### Definition

nan


### Comment

'In bdqffdq the concept of ResourceType has instances for SingleRecord or MultiRecord'


********************

## bdqffdq:SolutionsConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/SolutionsConcept

### Preferred Label

'Solutions Concept'

### Label

'Solutions Concept'

### Type

Class

### Definition

'Category of concepts forming the Solutions layer of the fittness for use framework.'


### Comment

nan


********************

## bdqffdq:AmendmentAssertion

### Name

https://rs.tdwg.org/bdqffdq/terms/AmendmentAssertion

### Preferred Label

'Amendment Assertion'

### Label

'Amendment Assertion'

### Type

Class

## Superclass

bdqffdq:Assertion

### Definition

nan


### Comment

'The Amendment assertion type is a report level concept that describes a run of a test that proposes changes based on some data quality enhancement. The Amendment concept in FFDQ consists of a run result that includes a status (FILLED_IN, TRANSPOSED, etc) as well as the proposed changes to values from the original data.'


********************

## bdqffdq:IssueAssertion

### Name

https://rs.tdwg.org/bdqffdq/terms/IssueAssertion

### Preferred Label

'Issue Assertion'

### Label

'Issue Assertion'

### Type

Class

## Superclass

bdqffdq:Assertion

### Definition

nan


### Comment

'The DQ report concept describing a test for the negative case. If a problem was found the result has a status of HAS_PROBLEM otherwise the status is NO_PROBLEM.'


********************

## bdqffdq:MeasurementAssertion

### Name

https://rs.tdwg.org/bdqffdq/terms/MeasurementAssertion

### Preferred Label

'Measurement Assertion'

### Label

'Measurement Assertion'

### Type

Class

## Superclass

bdqffdq:Assertion

### Definition

nan


### Comment

'The Measure assertion type is a report level concept that describes a run of a test that performs a measurement according to some data quality dimension. In FFDQ, the Measure concept consists of a run result of COMPLETE or NOT_COMPLETE or a value of the measurement (i.e. a measure of dwc:eventDate duration in seconds).'


********************

## bdqffdq:ValidationAssertion

### Name

https://rs.tdwg.org/bdqffdq/terms/ValidationAssertion

### Preferred Label

'Vailidation Assertion'

### Label

'Vailidation Assertion'

### Type

Class

## Superclass

bdqffdq:Assertion

### Definition

nan


### Comment

'The Validation assertion type is a report level concept that describes a run of a test for validity. The Validation concept in FFDQ consists of a run result of COMPLIANT or NON_COMPLIANT and a criterion that describes the conditions for validity that result in a status of COMPLIANT.'


********************

## bdqffdq:AmendmentMethod

### Name

https://rs.tdwg.org/bdqffdq/terms/AmendmentMethod

### Preferred Label

'Amendment Method'

### Label

'Amendment Method'

### Type

Class

## Superclass

bdqffdq:DataQualityMethod

### Definition

nan


### Comment

'The AmendmentMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and an enhancement in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

## bdqffdq:IssueMethod

### Name

https://rs.tdwg.org/bdqffdq/terms/IssueMethod

### Preferred Label

'Issue Method'

### Label

'Issue Method'

### Type

Class

## Superclass

bdqffdq:DataQualityMethod

### Definition

nan


### Comment

'The ProblemMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and an issue in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

## bdqffdq:MeasurementMethod

### Name

https://rs.tdwg.org/bdqffdq/terms/MeasurementMethod

### Preferred Label

'Measurement Method'

### Label

'Measurement Method'

### Type

Class

## Superclass

bdqffdq:DataQualityMethod

### Definition

nan


### Comment

'The MeasurementMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and a dimension in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

## bdqffdq:ValidationMethod

### Name

https://rs.tdwg.org/bdqffdq/terms/ValidationMethod

### Preferred Label

'Validation Method'

### Label

'Validation Method'

### Type

Class

## Superclass

bdqffdq:DataQualityMethod

### Definition

nan


### Comment

'The ValidationMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and a criterion in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

## bdqffdq:Amendmenent

### Name

https://rs.tdwg.org/bdqffdq/terms/Amendmenent

### Preferred Label

'Amendment'

### Label

'Amendment'

### Type

Class

## Superclass

bdqffdq:DataQualityNeed

### Definition

nan


### Comment

'Describes a proposal for enhancement of original data, which if accepted, would improve the quality of the data for some use. For example, 'Recommends valid value for taxon name in a single record'.  Amendments may describe proposed changes to data values, or to processes for the production and manipulation of data, for example an Amendment on a SingleRecord may provide criteria for proposing that latitude and longitude are transposed in that record, or a similar Amendment on a MultiRecord may provide critera for proposing that all latitudes and longitudes from some data source have been transposed, and the mapping of data values to transport terms should be changed.  An Amendment is the data quality needs concept that paralells an AmendmentMethod at the solutions level, and an AmmendmentAssertion at the report level.'


********************

## bdqffdq:Issue

### Name

https://rs.tdwg.org/bdqffdq/terms/Issue

### Preferred Label

'Issue'

### Label

'Issue'

### Type

Class

## Superclass

bdqffdq:DataQualityNeed

### Definition

nan


### Comment

'Describes criteria by which data which lack quality for some purpose may be identified.  An issue is phrased in a negative sense, and approximantes an inverse of a Validation.  An Issue identifies data that lack or may lack quality.  An Issue may flag a POSSIBLE_PROBLEM that would need further review to determine if the data have qulity for some purpose,  If the conditions described by an issue are identified by a test, the Problem Assertion result will be either HAS_PROBLEM or POSSIBLE_PROBLEM, if no issue is found with the data the result will be NO_PROBLEM.  NO_PROBLEM, unlike COMPLIANT for a Validation, does not assert that data are fit for some purpose.    An Issue is the data quality needs concept that paralells a IssueMethod at the solutions level, and a IssieAssertion at the report level.'


********************

## bdqffdq:Measure

### Name

https://rs.tdwg.org/bdqffdq/terms/Measure

### Preferred Label

'Measure'

### Label

'Measure'

### Type

Class

## Superclass

bdqffdq:DataQualityNeed

### Definition

nan


### Comment

'Describes the criteria for measuring an aspect of data quality related to some data quality need.   May be criteria for determining that data are COMPLETE or NOT_COMPLETE, or may be criteria for asserting a numeric measurement.  COMPLETE or NOT_COMPLETE measures are fundamental to data quality control, as set of data are filtered to the subset of data have quality for some need if all records are COMPLETE for all pertenent Measures.  A Measure is the data quality needs concept that paralells a MeasurementMethod at the solutions level, and a MeasurementAssertion at the report level.'


********************

## bdqffdq:Validation

### Name

https://rs.tdwg.org/bdqffdq/terms/Validation

### Preferred Label

'Validation'

### Label

'Validation'

### Type

Class

## Superclass

bdqffdq:DataQualityNeed

### Definition

nan


### Comment

'Describes the criteria for determining compliance of data to fill some data quality need.  Validations are phrased in a positive sense, they identify data which has quality for some need.  For example, 'The value of basisOfRecord of single records must be in the controlled vocabulary'.   A Validation is the data quality needs concept that paralells a ValidationMethod at the solutions level, and a ValidationAssertion at the report level.  ValidationAssertions may specify a result that is COMPLIANT, where the data has quality, or NOT_COMPLIANT, where the data lacks quality.'


********************

## bdqffdq:ActedUpon

### Name

https://rs.tdwg.org/bdqffdq/terms/ActedUpon

### Preferred Label

nan

### Label

'Acted Upon'

### Type

Class

## Superclass

bdqffdq:InformationElement

### Definition

nan


### Comment

'An information element to which a Result applies.'


********************

## bdqffdq:Consulted

### Name

https://rs.tdwg.org/bdqffdq/terms/Consulted

### Preferred Label

nan

### Label

'Consulted'

### Type

Class

## Superclass

bdqffdq:InformationElement

### Definition

nan


### Comment

'An Information Element the content of which is examined to assert a result on one or more other Information Elements'


********************

## bdqffdq:AmendmentPolicy

### Name

https://rs.tdwg.org/bdqffdq/terms/AmendmentPolicy

### Preferred Label

'Amendment Policy'

### Label

'Amendment Policy'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

'The set of Contextualized Enhancements that support a Use Case.'


### Comment

'A Data Quality needs level concept that describes how some bdqffdq:contextualizedEnhancement relates to a bdqffdq:UseCase. This relationship defines which amendments are supported by a given use case.'


********************

## bdqffdq:ContextualizedCriterion

### Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedCriterion

### Preferred Label

'Contextualized Criterion'

### Label

nan

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'Describes an instance of the criterion concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

## bdqffdq:ContextualizedDimension

### Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedDimension

### Preferred Label

'Contextualized Dimension'

### Label

'Contextualized Dimension'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'Describes an instance of the dimension concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

## bdqffdq:ContextualizedEnhancement

### Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedEnhancement

### Preferred Label

'Contextualized Enhancement'

### Label

'Contextualized Enhancement'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'Describes an instance of the enhancement concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

## bdqffdq:ContextualizedIssue

### Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedIssue

### Preferred Label

'Contextualized Issue'

### Label

'Contextualized Issue'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'Describes an instance of the issue concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

## bdqffdq:DataQualityNeed

### Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityNeed

### Preferred Label

'Data Quality Need'

### Label

'Data Quality Need'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

nan


********************

## bdqffdq:ImprovementTarget

### Name

https://rs.tdwg.org/bdqffdq/terms/ImprovementTarget

### Preferred Label

'Improvement Target'

### Label

'Improvement Target'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'The ImprovementTarget concept in FFDQ describes which measures and validations are improved by some amendment. ImprovementTarget includes relationships between a contextualizedEnhancement (for an Amendment) and one or more contextualizedCriterion (link to validations) or contextualizedDimensions (link to measures).'


********************

## bdqffdq:MeasurementPolicy

### Name

https://rs.tdwg.org/bdqffdq/terms/MeasurementPolicy

### Preferred Label

'Measurement Policy'

### Label

'Measurement Policy'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'The MeasurementPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedDimension relates to a use case. This relationship defines which measures are supported by a given use case.'


********************

## bdqffdq:ProblemPolicy

### Name

https://rs.tdwg.org/bdqffdq/terms/ProblemPolicy

### Preferred Label

'Problem Policy'

### Label

'Problem Policy'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'The ProblemPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedIssue relates to a use case. This relationship defines which problems are supported by a given use case.'


********************

## bdqffdq:Profile

### Name

https://rs.tdwg.org/bdqffdq/terms/Profile

### Preferred Label

'Profile'

### Label

'Profile'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'Profile in FFDQ is a DQ Needs level concept describing the UseCases that make up some data quality operation such as the behavior of a single actor or workflow producing the relevant assertions.'


********************

## bdqffdq:Specification

### Name

https://rs.tdwg.org/bdqffdq/terms/Specification

### Preferred Label

'Specification'

### Label

'Specification'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'A specification is a technical desription of an assertion test.

A specification is expected to have the following properies: 

Expected Response

Authorities and Parameters'


********************

## bdqffdq:UseCase

### Name

https://rs.tdwg.org/bdqffdq/terms/UseCase

### Preferred Label

'Use Case'

### Label

'Use Case'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'The UseCase concept in FFDQ describes some data quality control use case. The Amendment, Measurement and Validation policies that make up a use case define which assertions cover a given use case.

An example of a UseCase could be 'Check for internal consistency of dates', with validation policies for checking consistency between atomic date fields and an Amendment such as 'eventDate filled in from verbatim'.

Use Cases in bdqffdq are not the same as Use Cases in the software engineering sense, but  are similar bdqffdq formal statements derived from analyis of user stories.'


********************

## bdqffdq:ValidationPolicy

### Name

https://rs.tdwg.org/bdqffdq/terms/ValidationPolicy

### Preferred Label

'Validation Policy'

### Label

'Validation Policy'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

nan


### Comment

'The ValidationPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedCriterion relates to a use case. This relationship defines which validations are supported by a given use case.'


********************

## bdqffdq:Assertion

### Name

https://rs.tdwg.org/bdqffdq/terms/Assertion

### Preferred Label

'Assertion'

### Label

'Assertion'

### Type

Class

## Superclass

bdqffdq:ReportConcept

### Definition

nan


### Comment

'The Assertion type in FFDQ is the fundamental concept that makes up a data quality report. Assertion can be any one of four types (represented as subClasses), Measure, Validation, Issue, and Amendement.

The assertion concept consists of a specification (the technical description of a performed test), a data resource (initial values of input data expressed in terms of some controlled vocabulary), the mechanism (external service, actor, or code that performs the test), and some form of result.'


********************

## bdqffdq:DataQualityReport

### Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityReport

### Preferred Label

'Data Quality Report'

### Label

'Data Quality Report'

### Type

Class

## Superclass

bdqffdq:ReportConcept

### Definition

nan


### Comment

'The FFDQ Report concept consists of a set of assertions (measures, validations and amendments) that represent the output of a workflow/actor run.  These assertions form an account of the fitness for use of a tested data set for a specified use, as produced by a Mechanism.'


********************

## bdqffdq:DataResource

### Name

https://rs.tdwg.org/bdqffdq/terms/DataResource

### Preferred Label

'Data Resource'

### Label

'Data Resource'

### Type

Class

## Superclass

bdqffdq:ReportConcept

### Definition

nan


### Comment

'Describes a data resource described in terms of a controlled vocabulary such as dwc and represents the original values of the data operated on by an assertion test (i.e. an instance of dwc:Occurrence).'


********************

## bdqffdq:Result

### Name

https://rs.tdwg.org/bdqffdq/terms/Result

### Preferred Label

'Response.result'

### Label

'Response.result'

### Type

Class

## Superclass

bdqffdq:ReportConcept

### Definition

nan


### Comment

'The report result concept in FFDQ is represented as a value or a status for measures, just a result status for validations and a result status as well as values for changes propsed by amendments.'


********************

## bdqffdq:ResultStatus

### Name

https://rs.tdwg.org/bdqffdq/terms/ResultStatus

### Preferred Label

'Response.status'

### Label

'Response.status'

### Type

Class

## Superclass

bdqffdq:ReportConcept

### Definition

nan


### Comment

'Depending on the assertion type would have values of COMPLIANT or NON_COMPLIANT for a Validation, COMPLETE or NOT_COMPLETE for a Measure, CURATED, FILLED_IN,TRANSPOSED, NO_CHANGE for an Amendment and HAS_PROBLEM NO_PROBLEM for a Problem.

A separate concept describes the result state as values of AMBIGIOUS, INTERNAL_PREREQUISITES_NOT_MET and EXTERNAL_PREREQUISITES_NOT_MET.'


********************

## bdqffdq:DataQualityMethod

### Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityMethod

### Preferred Label

'Data Quality Method'

### Label

'Data Quality Method'

### Type

Class

## Superclass

bdqffdq:SolutionsConcept

### Definition

nan


### Comment

nan


********************

## bdqffdq:Implementation

### Name

https://rs.tdwg.org/bdqffdq/terms/Implementation

### Preferred Label

'Implementation'

### Label

'Implementation'

### Type

Class

## Superclass

bdqffdq:SolutionsConcept

### Definition

nan


### Comment

'The FFDQ derived concept of an Implementation describes the relationship between a specification (technical description of a test) and the mechanism that implements it.'


********************

## bdqffdq:Mechanism

### Name

https://rs.tdwg.org/bdqffdq/terms/Mechanism

### Preferred Label

'Mechanism'

### Label

'Mechanism'

### Type

Class

## Superclass

bdqffdq:SolutionsConcept

### Definition

nan


### Comment

'The FFDQ concept of mechanism describes the entity that performs an assertion test (code, external service, actor, etc.). Tied to a specification via the concept of an Implementation.'


********************


# DataProperty terms

********************

## https://rs.tdwg.org/bdqffdq/terms#AuthoritiesDefaults

### Name

https://rs.tdwg.org/bdqffdq/terms#AuthoritiesDefaults

### Preferred Label

nan

### Label

nan

### Type

DataProperty

## Superclass

'Details of the bdq:sourceAuthoritiy listed in a Specification, along with Parameters that may be provided to the expected response along with their default values.'

### Definition

'Authorities and Defaults'


### Comment

'Authorities and Defaults'


********************

## bdqffdq:ExpectedResponse

### Name

https://rs.tdwg.org/bdqffdq/terms/ExpectedResponse

### Preferred Label

nan

### Label

nan

### Type

DataProperty

## Superclass

'The description of the logic of a test specification.  An expected response is expected to be a data property of a Specification'

### Definition

'Expected Response'


### Comment

'Expected Response'


********************

## bdqffdq:hasResponseResultValue

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseResultValue

### Preferred Label

nan

### Label

nan

### Type

DataProperty

### Definition

'has response result value'


### Comment

'has response result value'


********************


# NamedIndividual terms

********************

## bdqffdq:SingleRecord

### Name

https://rs.tdwg.org/bdqffdq/terms/SingleRecord

### Preferred Label

nan

### Label

nan

### Type

NamedIndividual

## Superclass

'A record from a dataset without dependencies on any other record.'

### Definition

nan


### Comment

'Single Record'


********************

## bdqffdq:MultiRecord

### Name

https://rs.tdwg.org/bdqffdq/terms/MultiRecord

### Preferred Label

nan

### Label

nan

### Type

NamedIndividual

### Definition

nan


### Comment

'Multi Record'


********************


# ObjectProperty terms

********************

## bdqffdq:implementedBy

### Name

https://rs.tdwg.org/bdqffdq/terms/implementedBy

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Describes the link between the Implementation concept in FFDQ and the Mechanism that implements some specification (also defined in Implementation).'

### Definition

nan


### Comment

nan


********************

## bdqffdq:composedOf

### Name

https://rs.tdwg.org/bdqffdq/terms/composedOf

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Describes the properties from a controlled vocabulary that compose an InformationElement. For example, an InformationElement may be 'composedOf' properties such as dwc:day, dwc:month and dwc:year.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasSpecification

### Name

https://rs.tdwg.org/bdqffdq/terms/hasSpecification

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Describes the relationship between a derived FFDQ concept and the fundamental concept of a specification (technical description of a test).'

### Definition

nan


### Comment

nan


********************

## bdqffdq:issueInContext

### Name

https://rs.tdwg.org/bdqffdq/terms/issueInContext

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Describes the relationship between a problem concept in FFDQ (needs, solutions, reports) and a ContextualizedIssue.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:criterionInContext

### Name

https://rs.tdwg.org/bdqffdq/terms/criterionInContext

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Describes the relationship between a validation concept in FFDQ (needs, solutions, reports) and a contextualizedCriterion.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:dimensionInContext

### Name

https://rs.tdwg.org/bdqffdq/terms/dimensionInContext

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Describes the relationship between an Amendment concept in FFDQ (needs, solutions, reports) and a ContextualizedDimension.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:enhancementInContext

### Name

https://rs.tdwg.org/bdqffdq/terms/enhancementInContext

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Describes the relationship between an Amendment concept in FFDQ (needs, solutions, reports) and a ContextualizedEnhancement.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:improvedBy

### Name

https://rs.tdwg.org/bdqffdq/terms/improvedBy

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Object property that describes an enhancement, as part of the ImprovementTarget, that would improve data acted upon by some set of measures or validations.  This can be used to determine which measures and validations are improved upon by a given amendment.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasActedUponInformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasActedUponInformationElement

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Provides a relationship between FFDQ concepts and the information elements that are ActedUpon in a test.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasConsultedInformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasConsultedInformationElement

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Provides a relationship between FFDQ concepts and the information elements that are Consulted, but not ActedUpon in a test.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasInformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasInformationElement

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Provides a relationship between FFDQ concepts and the information elements. For example, ContextualizedCriterion uses this property along with hasResourceType to define a criterion in the context of related information elements.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasResourceType

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResourceType

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Provides additional metadata, along with the information elements, that describes the level (SingleRecord or MultiRecord) at which the FFDQ concept operates. For example, an enhancementInContext with resource type of MultiRecord could be used to define an Amendment that applies at the level of multiple record values.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:amendmentProperties

### Name

https://rs.tdwg.org/bdqffdq/terms/amendmentProperties

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to amendment concepts such as AmendmentPolicy (DQ Needs), AmendmentMethod (DQ Solutions) and Amendment (DQ Reports).'

### Definition

nan


### Comment

nan


********************

## bdqffdq:measurementProperties

### Name

https://rs.tdwg.org/bdqffdq/terms/measurementProperties

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to measurement concepts such as MeasurementPolicy (DQ Needs), MeasurementMethod (DQ Solutions) and Measure (DQ Reports).'

### Definition

nan


### Comment

nan


********************

## bdqffdq:problemProperties

### Name

https://rs.tdwg.org/bdqffdq/terms/problemProperties

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to problem concepts such as ProblemPolicy (DQ Needs), ProblemMethod (DQ Solutions) and Issue (DQ Reports).'

### Definition

nan


### Comment

nan


********************

## bdqffdq:validationProperties

### Name

https://rs.tdwg.org/bdqffdq/terms/validationProperties

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to validation concepts such as ValidationPolicy (DQ Needs), ValidationMethod (DQ Solutions) and Validation (DQ Reports).'

### Definition

nan


### Comment

nan


********************

## bdqffdq:targetedCriterion

### Name

https://rs.tdwg.org/bdqffdq/terms/targetedCriterion

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'The criteria targeted by some enhancement via the ImprovementTarget object.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:targetedDimension

### Name

https://rs.tdwg.org/bdqffdq/terms/targetedDimension

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'The dimension targeted by some enhancement via the ImprovementTarget object.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:targetedIssue

### Name

https://rs.tdwg.org/bdqffdq/terms/targetedIssue

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'The issue targeted by some problem via the ImprovementTarget object.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:coversUseCase

### Name

https://rs.tdwg.org/bdqffdq/terms/coversUseCase

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used by concepts in the DQ Needs category to describe the relationship between DQ Policies (ValidationPolicy, AmendmentPolicy, MeasurementPolicy) and an instance of the use case covered by that policy.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasResponseResult

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseResult

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used in the DQ Report concept to describe response result objects. For example, values could be bdq:RUN_HAS_RESULT or bdq:INTERNAL_PREREQUISITES_NOT_MET.   If Response.results are not objects, use the datatype property hasResponseResultValue'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasStatus

### Name

https://rs.tdwg.org/bdqffdq/terms/hasStatus

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used in the DQ Report concept to describe result status. For example, in the case of a Validation result, values could be COMPLIANT or NON_COMPLIANT.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasResponseStatus

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseStatus

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used in the DQ Report concept to describe result status. For example, in the case of a Validation result, values could be bdq:COMPLIANT or bdq:NON_COMPLIANT.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasCriterion

### Name

https://rs.tdwg.org/bdqffdq/terms/hasCriterion

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedCriterion to the fundamental concept of a Criterion.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasDimension

### Name

https://rs.tdwg.org/bdqffdq/terms/hasDimension

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedDimension to the fundamental concept of a Dimension.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasEnhancement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasEnhancement

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedEnhancement to the fundamental concept of an Enhancement.'

### Definition

nan


### Comment

nan


********************

## bdqffdq:hasIssue

### Name

https://rs.tdwg.org/bdqffdq/terms/hasIssue

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedIssue to the fundamental concept of a Problem.'

### Definition

nan


### Comment

nan


********************

## http://www.w3.org/2002/07/owl#topObjectProperty

### Name

http://www.w3.org/2002/07/owl#topObjectProperty

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

### Definition

nan


### Comment

nan


********************

## bdqffdq:reportProperties

### Name

https://rs.tdwg.org/bdqffdq/terms/reportProperties

### Preferred Label

nan

### Label

nan

### Type

ObjectProperty

### Definition

nan


### Comment

nan


********************

