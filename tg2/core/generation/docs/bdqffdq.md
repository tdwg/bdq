---
title:  TDWG BDQ Core Framework for data quality
geometry: margin=1cm
titlepage: true
---
#  'Data Quality Dimension'

## Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityDimension

## Type

Class

## Superclass

http://www.w3.org/2002/07/owl#Thing

## Comment

'Describes the aspect of data quality (accuracy, precision, completeness, etc.) that a test examines. For example, 'precision' in 'coordinate percision of single records'.  Includes Completeness (q.v.), Conformance (q.v.), Consistency (q.v.), Likeliness (q.v.), Reliability (q.v.), and Resolution (q.v.).'


********************

#  'Information Element'

## Name

https://rs.tdwg.org/bdqffdq/terms/InformationElement

## Type

Class

## Superclass

http://www.w3.org/2002/07/owl#Thing

## Comment

'An information element identifies a portion of data to which a test pertains.  The information element in FFDQ can be represented as a single or composite element that consists of one or more terms from a controlled vocabulary (fields actedUpon or consulted by an assertion test) that identifies concepts in data relevant to a use case.  An abstraction or a concrete term that represents relevant content (e.g., coordinates; dwc.decimalLatitude, dwc:decimalLongitude).'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Type

Class

## Superclass

http://www.w3.org/2002/07/owl#Thing

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

## Type

Class

## Superclass

http://www.w3.org/2002/07/owl#Thing

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ResourceType

## Type

Class

## Superclass

http://www.w3.org/2002/07/owl#Thing

## Comment

'In FFDQ the concept of ResourceType has instances for SingleRecord or MultiRecord'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/SolutionsConcept

## Type

Class

## Superclass

http://www.w3.org/2002/07/owl#Thing

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/AmendmentAssertion

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/Assertion

## Comment

'The Amendment assertion type is a report level concept that describes a run of a test that proposes changes based on some data quality enhancement. The Amendment concept in FFDQ consists of a run result that includes a status (FILLED_IN, TRANSPOSED, etc) as well as the proposed changes to values from the original data.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/IssueAssertion

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/Assertion

## Comment

'The DQ report concept describing a test for the negative case. If a problem was found the result has a status of HAS_PROBLEM otherwise the status is NO_PROBLEM.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/MeasurementAssertion

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/Assertion

## Comment

'The Measure assertion type is a report level concept that describes a run of a test that performs a measurement according to some data quality dimension. In FFDQ, the Measure concept consists of a run result of COMPLETE or NOT_COMPLETE or a value of the measurement (i.e. a measure of dwc:eventDate duration in seconds).'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ValidationAssertion

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/Assertion

## Comment

'The Validation assertion type is a report level concept that describes a run of a test for validity. The Validation concept in FFDQ consists of a run result of COMPLIANT or NON_COMPLIANT and a criterion that describes the conditions for validity that result in a status of COMPLIANT.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/AmendmentMethod

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityMethod

## Comment

'The AmendmentMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and an enhancement in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/MeasurementMethod

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityMethod

## Comment

'The MeasurementMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and a dimension in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ProblemMethod

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityMethod

## Comment

'The ProblemMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and an issue in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ValidationMethod

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityMethod

## Comment

'The ValidationMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and a criterion in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Amendmenent

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityNeed

## Comment

'Describes a proposal for enhancement of original data, which if accepted, would improve the quality of the data for some use. For example, 'Recommends valid value for taxon name in a single record'.  Amendments may describe proposed changes to data values, or to processes for the production and manipulation of data, for example an Amendment on a SingleRecord may provide criteria for proposing that latitude and longitude are transposed in that record, or a similar Amendment on a MultiRecord may provide critera for proposing that all latitudes and longitudes from some data source have been transposed, and the mapping of data values to transport terms should be changed.  An Amendment is the data quality needs concept that paralells an AmendmentMethod at the solutions level, and an AmmendmentAssertion at the report level.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Issue

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityNeed

## Comment

'Describes criteria by which data which lack quality for some purpose may be identified.  An issue is phrased in a negative sense, and approximantes an inverse of a Validation.  An Issue identifies data that lack or may lack quality.  An Issue may flag a POSSIBLE_PROBLEM that would need further review to determine if the data have qulity for some purpose,  If the conditions described by an issue are identified by a test, the Problem Assertion result will be either HAS_PROBLEM or POSSIBLE_PROBLEM, if no issue is found with the data the result will be NO_PROBLEM.  NO_PROBLEM, unlike COMPLIANT for a Validation, does not assert that data are fit for some purpose.    An Issue is the data quality needs concept that paralells a IssueMethod at the solutions level, and a IssieAssertion at the report level.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Measure

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityNeed

## Comment

'Describes the criteria for measuring an aspect of data quality related to some data quality need.   May be criteria for determining that data are COMPLETE or NOT_COMPLETE, or may be criteria for asserting a numeric measurement.  COMPLETE or NOT_COMPLETE measures are fundamental to data quality control, as set of data are filtered to the subset of data have quality for some need if all records are COMPLETE for all pertenent Measures.  A Measure is the data quality needs concept that paralells a MeasurementMethod at the solutions level, and a MeasurementAssertion at the report level.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Validation

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/DataQualityNeed

## Comment

'Describes the criteria for determining compliance of data to fill some data quality need.  Validations are phrased in a positive sense, they identify data which has quality for some need.  For example, 'The value of basisOfRecord of single records must be in the controlled vocabulary'.   A Validation is the data quality needs concept that paralells a ValidationMethod at the solutions level, and a ValidationAssertion at the report level.  ValidationAssertions may specify a result that is COMPLIANT, where the data has quality, or NOT_COMPLIANT, where the data lacks quality.'


********************

#  'Acted Upon'

## Name

https://rs.tdwg.org/bdqffdq/terms/ActedUpon

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/InformationElement

## Comment

'An information element to which a Result applies.'


********************

#  'Consulted'

## Name

https://rs.tdwg.org/bdqffdq/terms/Consulted

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/InformationElement

## Comment

'An Information Element the content of which is examined to assert a result on one or more other Information Elements'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/AmendmentPolicy

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'The AmendmentPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedEnhancement relates to a use case. This relationship defines which Amendments are supported by a given use case.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedCriterion

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'Describes an instance of the criterion concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedDimension

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'Describes an instance of the dimension concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedEnhancement

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'Describes an instance of the enhancement concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ContextualizedIssue

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'Describes an instance of the issue concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityNeed

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ImprovementTarget

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'The ImprovementTarget concept in FFDQ describes which measures and validations are improved by some amendment. ImprovementTarget includes relationships between a contextualizedEnhancement (for an Amendment) and one or more contextualizedCriterion (link to validations) or contextualizedDimensions (link to measures).'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/MeasurementPolicy

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'The MeasurementPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedDimension relates to a use case. This relationship defines which measures are supported by a given use case.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ProblemPolicy

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'The ProblemPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedIssue relates to a use case. This relationship defines which problems are supported by a given use case.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Profile

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'Profile in FFDQ is a DQ Needs level concept describing the UseCases that make up some data quality operation such as the behavior of a single actor or workflow producing the relevant assertions.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Specification

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'A specification is a technical desription of an assertion test.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/UseCase

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'The UseCase concept in FFDQ describes some data quality control use case. The Amendment, Measurement and Validation policies that make up a use case define which assertions cover a given use case.

An example of a UseCase could be 'Check for internal consistency of dates', with validation policies for checking consistency between atomic date fields and an Amendment such as 'eventDate filled in from verbatim'.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ValidationPolicy

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/NeedConcept

## Comment

'The ValidationPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedCriterion relates to a use case. This relationship defines which validations are supported by a given use case.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Assertion

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

## Comment

'The Assertion type in FFDQ is the fundamental concept that makes up a data quality report. Assertion can be any one of four types (represented as subClasses), Measure, Validation, Issue, and Amendement.

The assertion concept consists of a specification (the technical description of a performed test), a data resource (initial values of input data expressed in terms of some controlled vocabulary), the mechanism (external service, actor, or code that performs the test), and some form of result.'


********************

#  'Data Quality Report'

## Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityReport

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

## Comment

'The FFDQ Report concept consists of a set of assertions (measures, validations and amendments) that represent the output of a workflow/actor run.  These assertions form an account of the fitness for use of a tested data set for a specified use, as produced by a Mechanism.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/DataResource

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

## Comment

'Describes a data resource described in terms of a controlled vocabulary such as dwc and represents the original values of the data operated on by an assertion test (i.e. an instance of dwc:Occurrence).'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Result

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

## Comment

'The report result concept in FFDQ is represented as a value or a status for measures, just a result status for validations and a result status as well as values for changes propsed by amendments.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ResultStatus

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

## Comment

'Depending on the assertion type would have values of COMPLIANT or NON_COMPLIANT for a Validation, COMPLETE or NOT_COMPLETE for a Measure, CURATED, FILLED_IN,TRANSPOSED, NO_CHANGE for an Amendment and HAS_PROBLEM NO_PROBLEM for a Problem.

A separate concept describes the result state as values of AMBIGIOUS, INTERNAL_PREREQUISITES_NOT_MET and EXTERNAL_PREREQUISITES_NOT_MET.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/DataQualityMethod

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/SolutionsConcept

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Implementation

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/SolutionsConcept

## Comment

'The FFDQ derived concept of an Implementation describes the relationship between a specification (technical description of a test) and the mechanism that implements it.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Mechanism

## Type

Class

## Superclass

https://rs.tdwg.org/bdqffdq/terms/SolutionsConcept

## Comment

'The FFDQ concept of mechanism describes the entity that performs an assertion test (code, external service, actor, etc.). Tied to a specification via the concept of an Implementation.'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/Parameters

## Type

DataProperty

## Superclass

'Parameters that may be provided with the expected response along with their default values if they are not provided.  Parameters are expected to be data properties of a Specification.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/ExpectedResponse

## Type

DataProperty

## Superclass

'The description of the logic of a test specification.  An expected response is expected to be a data property of a Specification'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseResultValue

## Type

DataProperty

## Superclass

nan

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/SingleRecord

## Type

NamedIndividual

## Superclass

'A record from a dataset without dependencies on any other record.'

## Comment

'Single Record'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/MultiRecord

## Type

NamedIndividual

## Superclass

nan

## Comment

'Multi Record'


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/implementedBy

## Type

ObjectProperty

## Superclass

'Describes the link between the Implementation concept in FFDQ and the Mechanism that implements some specification (also defined in Implementation).'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/composedOf

## Type

ObjectProperty

## Superclass

'Describes the properties from a controlled vocabulary that compose an InformationElement. For example, an InformationElement may be 'composedOf' properties such as dwc:day, dwc:month and dwc:year.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasSpecification

## Type

ObjectProperty

## Superclass

'Describes the relationship between a derived FFDQ concept and the fundamental concept of a specification (technical description of a test).'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/issueInContext

## Type

ObjectProperty

## Superclass

'Describes the relationship between a problem concept in FFDQ (needs, solutions, reports) and a ContextualizedIssue.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/criterionInContext

## Type

ObjectProperty

## Superclass

'Describes the relationship between a validation concept in FFDQ (needs, solutions, reports) and a contextualizedCriterion.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/dimensionInContext

## Type

ObjectProperty

## Superclass

'Describes the relationship between an Amendment concept in FFDQ (needs, solutions, reports) and a ContextualizedDimension.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/enhancementInContext

## Type

ObjectProperty

## Superclass

'Describes the relationship between an Amendment concept in FFDQ (needs, solutions, reports) and a ContextualizedEnhancement.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/improvedBy

## Type

ObjectProperty

## Superclass

'Object property that describes an enhancement, as part of the ImprovementTarget, that would improve data acted upon by some set of measures or validations.  This can be used to determine which measures and validations are improved upon by a given amendment.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasActedUponInformationElement

## Type

ObjectProperty

## Superclass

'Provides a relationship between FFDQ concepts and the information elements that are ActedUpon in a test.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasConsultedInformationElement

## Type

ObjectProperty

## Superclass

'Provides a relationship between FFDQ concepts and the information elements that are Consulted, but not ActedUpon in a test.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasInformationElement

## Type

ObjectProperty

## Superclass

'Provides a relationship between FFDQ concepts and the information elements. For example, ContextualizedCriterion uses this property along with hasResourceType to define a criterion in the context of related information elements.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasResourceType

## Type

ObjectProperty

## Superclass

'Provides additional metadata, along with the information elements, that describes the level (SingleRecord or MultiRecord) at which the FFDQ concept operates. For example, an enhancementInContext with resource type of MultiRecord could be used to define an Amendment that applies at the level of multiple record values.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/amendmentProperties

## Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to amendment concepts such as AmendmentPolicy (DQ Needs), AmendmentMethod (DQ Solutions) and Amendment (DQ Reports).'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/measurementProperties

## Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to measurement concepts such as MeasurementPolicy (DQ Needs), MeasurementMethod (DQ Solutions) and Measure (DQ Reports).'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/problemProperties

## Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to problem concepts such as ProblemPolicy (DQ Needs), ProblemMethod (DQ Solutions) and Issue (DQ Reports).'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/validationProperties

## Type

ObjectProperty

## Superclass

'Sub properties of this type group object properties that apply to validation concepts such as ValidationPolicy (DQ Needs), ValidationMethod (DQ Solutions) and Validation (DQ Reports).'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/targetedCriterion

## Type

ObjectProperty

## Superclass

'The criteria targeted by some enhancement via the ImprovementTarget object.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/targetedDimension

## Type

ObjectProperty

## Superclass

'The dimension targeted by some enhancement via the ImprovementTarget object.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/targetedIssue

## Type

ObjectProperty

## Superclass

'The issue targeted by some problem via the ImprovementTarget object.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/coversUseCase

## Type

ObjectProperty

## Superclass

'Used by concepts in the DQ Needs category to describe the relationship between DQ Policies (ValidationPolicy, AmendmentPolicy, MeasurementPolicy) and an instance of the use case covered by that policy.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseResult

## Type

ObjectProperty

## Superclass

'Used in the DQ Report concept to describe response result objects. For example, values could be bdq:RUN_HAS_RESULT or bdq:INTERNAL_PREREQUISITES_NOT_MET.   If Response.results are not objects, use the datatype property hasResponseResultValue'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasStatus

## Type

ObjectProperty

## Superclass

'Used in the DQ Report concept to describe result status. For example, in the case of a Validation result, values could be COMPLIANT or NON_COMPLIANT.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseStatus

## Type

ObjectProperty

## Superclass

'Used in the DQ Report concept to describe result status. For example, in the case of a Validation result, values could be bdq:COMPLIANT or bdq:NON_COMPLIANT.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasCriterion

## Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedCriterion to the fundamental concept of a Criterion.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasDimension

## Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedDimension to the fundamental concept of a Dimension.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasEnhancement

## Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedEnhancement to the fundamental concept of an Enhancement.'

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/hasIssue

## Type

ObjectProperty

## Superclass

'Used to link the derived concept of a ContextualizedIssue to the fundamental concept of a Problem.'

## Comment

nan


********************

#  nan

## Name

http://www.w3.org/2002/07/owl#topObjectProperty

## Type

ObjectProperty

## Superclass

nan

## Comment

nan


********************

#  nan

## Name

https://rs.tdwg.org/bdqffdq/terms/reportProperties

## Type

ObjectProperty

## Superclass

nan

## Comment

nan


********************
