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

- [bdqffdq:AbstractInformationElement](#bdqffdqAbstractInformationElement) InformationElement
- [bdqffdq:ActedUpon](#bdqffdqActedUpon) InformationElement
- [bdqffdq:Amendment](#bdqffdqAmendment) AmendmentConcept|DataQualityNeed
- [bdqffdq:AmendmentAssertion](#bdqffdqAmendmentAssertion) AmendmentConcept|Assertion
- [bdqffdq:AmendmentConcept](#bdqffdqAmendmentConcept) 
- [bdqffdq:AmendmentMethod](#bdqffdqAmendmentMethod) AmendmentConcept|DataQualityMethod
- [bdqffdq:AmendmentPolicy](#bdqffdqAmendmentPolicy) AmendmentConcept|Policy
- [bdqffdq:Assertion](#bdqffdqAssertion) ReportConcept
- [bdqffdq:Consulted](#bdqffdqConsulted) InformationElement
- [bdqffdq:Criterion](#bdqffdqCriterion) NeedConcept|FundamentalConcept
- [bdqffdq:DataQualityDimension](#bdqffdqDataQualityDimension) NeedConcept|FundamentalConcept
- [bdqffdq:DataQualityMethod](#bdqffdqDataQualityMethod) SolutionsConcept
- [bdqffdq:DataQualityNeed](#bdqffdqDataQualityNeed) NeedConcept
- [bdqffdq:DataQualityReport](#bdqffdqDataQualityReport) ReportConcept
- [bdqffdq:DataResource](#bdqffdqDataResource) ReportConcept
- [bdqffdq:Enhancement](#bdqffdqEnhancement) AmendmentConcept|NeedConcept|FundamentalConcept
- [bdqffdq:FundamentalConcept](#bdqffdqFundamentalConcept) 
- [bdqffdq:Implementation](#bdqffdqImplementation) SolutionsConcept
- [bdqffdq:ImprovementTarget](#bdqffdqImprovementTarget) NeedConcept
- [bdqffdq:InformationElement](#bdqffdqInformationElement) FundamentalConcept
- [bdqffdq:Issue](#bdqffdqIssue) DataQualityNeed|IssueConcept
- [bdqffdq:IssueAssertion](#bdqffdqIssueAssertion) Assertion|IssueConcept
- [bdqffdq:IssueConcept](#bdqffdqIssueConcept) 
- [bdqffdq:IssueMethod](#bdqffdqIssueMethod) DataQualityMethod|IssueConcept
- [bdqffdq:IssuePolicy](#bdqffdqIssuePolicy) Policy|IssueConcept
- [bdqffdq:Measure](#bdqffdqMeasure) DataQualityNeed|MeaurementConcept
- [bdqffdq:MeasurementAssertion](#bdqffdqMeasurementAssertion) MeaurementConcept|Assertion
- [bdqffdq:MeasurementMethod](#bdqffdqMeasurementMethod) MeaurementConcept|DataQualityMethod
- [bdqffdq:MeasurementPolicy](#bdqffdqMeasurementPolicy) Policy|MeaurementConcept
- [bdqffdq:MeaurementConcept](#bdqffdqMeaurementConcept) 
- [bdqffdq:Mechanism](#bdqffdqMechanism) FundamentalConcept|SolutionsConcept
- [bdqffdq:NeedConcept](#bdqffdqNeedConcept) 
- [bdqffdq:Parameter](#bdqffdqParameter) SolutionsConcept
- [bdqffdq:Policy](#bdqffdqPolicy) NeedConcept
- [bdqffdq:Profile](#bdqffdqProfile) NeedConcept
- [bdqffdq:ReportConcept](#bdqffdqReportConcept) 
- [bdqffdq:ResourceType](#bdqffdqResourceType) FundamentalConcept
- [bdqffdq:ResponseResult](#bdqffdqResponseResult) ReportConcept
- [bdqffdq:ResponseStatus](#bdqffdqResponseStatus) ReportConcept
- [bdqffdq:SolutionsConcept](#bdqffdqSolutionsConcept) 
- [bdqffdq:Specification](#bdqffdqSpecification) FundamentalConcept|SolutionsConcept
- [bdqffdq:UseCase](#bdqffdqUseCase) NeedConcept|FundamentalConcept
- [bdqffdq:Validation](#bdqffdqValidation) DataQualityNeed|ValidationConcept
- [bdqffdq:ValidationAssertion](#bdqffdqValidationAssertion) ValidationConcept|Assertion
- [bdqffdq:ValidationConcept](#bdqffdqValidationConcept) 
- [bdqffdq:ValidationMethod](#bdqffdqValidationMethod) ValidationConcept|DataQualityMethod
- [bdqffdq:ValidationPolicy](#bdqffdqValidationPolicy) Policy|ValidationConcept
********************

# Class terms

********************

## bdqffdq:AmendmentConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/AmendmentConcept

### Preferred Label

'Amendment Concept'

### Label

'Amendment Concept'

### Type

Class

### Definition

'A term involved in proposals of changes to data or process to improve data quallity to fit expressed data quality needs.'


********************

## bdqffdq:FundamentalConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/FundamentalConcept

### Preferred Label

'Fundamental Concept'

### Label

'Fundamental Concept'

### Type

Class

### Definition

'Category of Fittness for use concepts that are not derived by composition with other concepts.'

### Comment

'Contrast with derived concepts, which are compositions of two or more fundamental concepts.  See Veiga et al., 2017.   Derived concepts can be organized by test type into Amendment Concept, Validation Concept, Measurment concept or Issue concept.  Derived concepts can also be organized by framework layer into Needs Concept, Solutions Concept, and Report Concept.'


********************

## bdqffdq:IssueConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/IssueConcept

### Preferred Label

'Issue Concept'

### Label

'Issue Concept'

### Type

Class

### Definition

'A term involved in flagging problems or potential problems in assessment of data quality that would or might prevent the data from meeting expressed data quality needs..'

### Comment

'Issue terms are expressed in a negative sense, they identify data that do not or may not conform to quality needs.'


********************

## bdqffdq:MeaurementConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/MeaurementConcept

### Preferred Label

'Measurement Concept'

### Label

'Measurement Concept'

### Type

Class

### Definition

'A term involved in measurement of data quality with regards to expressed data quality needs.'


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

'A concept that expresses an aspect of a data quality need.'

### Comment

'Category of concepts forming the Needs layer of the fittness for use framework.'


********************

## bdqffdq:ReportConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/ReportConcept

### Preferred Label

'Report Concept'

### Label

'Report Concept'

### Type

Class

### Definition

'A concept concerning data quality expressed in a data quality report.'

### Comment

'Category of concepts forming the Report layer of the fittness for use framework.'


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

'A concept that expresses an aspect of a data quality solution.'

### Comment

'Category of concepts forming the Solutions layer of the fittness for use framework.  Solutions are tools that evaluate data against needs and express conclusions in data quality reports.'


********************

## bdqffdq:ValidationConcept

### Name

https://rs.tdwg.org/bdqffdq/terms/ValidationConcept

### Preferred Label

'Validation Concept'

### Label

'Validation Concept'

### Type

Class

### Definition

'A term involved in statements about the conformance of data to expressed quality needs.'

### Comment

'Validation terms are expressed in a positive sense, they identify data that conform to needs.'


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

bdqffdq:AmendmentConcept|bdqffdq:Assertion

### Definition

'An assertion expressing the result of an implementation evaluating an amendment supporting a particular data quality need to improve a particular data resource.'

### Comment

'The Amendment assertion type is a report level concept that describes a run of a test that proposes changes based on some data quality enhancement. The Amendment concept in FFDQ consists of a run result that includes a status (FILLED_IN, TRANSPOSED, etc) as well as the proposed changes to values from the original data.'


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

bdqffdq:AmendmentConcept|bdqffdq:DataQualityMethod

### Definition

'A data quality solution concept that relates an Amendment to its Specifications.'

### Comment

'The AmendmentMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and an enhancement in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************

## bdqffdq:Amendment

### Name

https://rs.tdwg.org/bdqffdq/terms/Amendment

### Preferred Label

'Amendment'

### Label

'Amendment'

### Type

Class

## Superclass

bdqffdq:AmendmentConcept|bdqffdq:DataQualityNeed

### Definition

'A data quality need that expresses how proposals may be made to improve the fittnes for use of data.'

### Comment

'ContextualizedEnhacement in the original framework.   Describes an instance of the enhancement concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.  Describes a proposal for enhancement of original data, which if accepted, would improve the quality of the data for some use. For example: Recommends valid value for taxon name in a single record.  Amendments may describe proposed changes to data values, or to processes for the production and manipulation of data, for example an Amendment on a SingleRecord may provide criteria for proposing that latitude and longitude are transposed in that record, or a similar Amendment on a MultiRecord may provide critera for proposing that all latitudes and longitudes from some data source have been transposed, and the mapping of data values to transport terms should be changed.  An Amendment is the data quality needs concept that paralells an AmendmentMethod at the solutions level, and an AmmendmentAssertion at the report level.   A = { a | a = < ie, e, rt >, ie ∈ IE, e ∈ E ⋀ rt ∈ RT }'


********************

## bdqffdq:Enhancement

### Name

https://rs.tdwg.org/bdqffdq/terms/Enhancement

### Preferred Label

'Enhancement'

### Label

'Enhancement'

### Type

Class

## Superclass

bdqffdq:AmendmentConcept|bdqffdq:NeedConcept|bdqffdq:FundamentalConcept

### Definition

'Description of a means by which data could be improved.'

### Comment

'General statement, for example: Recomend replacement value from a controlled vocabulary'


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

bdqffdq:AmendmentConcept|bdqffdq:Policy

### Definition

'A need concept that relates a Use Case to a set of supporting Amendments.'

### Comment

'A Data Quality needs level concept that describes how some bdqffdq:contextualizedEnhancement relates to a bdqffdq:UseCase. This relationship defines which amendments are supported by a given use case.'


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

bdqffdq:Assertion|bdqffdq:IssueConcept

### Definition

'An assertion expressing the result of an implementation evaluating an issue for a particular data quality need in a particular data resource.'

### Comment

'The DQ report concept describing a test for the negative case. If a problem was found the result has a status of HAS_PROBLEM otherwise the status is NO_PROBLEM.'


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

bdqffdq:DataQualityMethod|bdqffdq:IssueConcept

### Definition

'A data quality solution concept that relates an Issue to its Specifications.'

### Comment

'The ProblemMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and an issue in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


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

bdqffdq:DataQualityNeed|bdqffdq:IssueConcept

### Definition

'A data quality need that expresses how quality problems may be identified in data.'

### Comment

'Added to the original framework.  Inverse of Contextualized Criterion in the original framework.  Describes an instance of the issue concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.  Describes criteria by which data which lack quality for some purpose may be identified.  An issue is phrased in a negative sense, and approximates an inverse of a Validation.  An Issue identifies data that lack or may lack quality.  An Issue may flag a POSSIBLE_PROBLEM that would need further review to determine if the data have qulity for some purpose,  If the conditions described by an issue are identified by a test, the Problem Assertion result will be either HAS_PROBLEM or POSSIBLE_PROBLEM, if no issue is found with the data the result will be NO_PROBLEM.  NO_PROBLEM, unlike COMPLIANT for a Validation, does not assert that data are fit for some purpose.    An Issue is the data quality needs concept that paralells a IssueMethod at the solutions level, and a IssieAssertion at the report level.   I = { i | i = < ie, c, rt >, ie ∈ IE, c ∈ ∁C ⋀ rt ∈ RT }'


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

bdqffdq:DataQualityNeed|bdqffdq:MeaurementConcept

### Definition

'A data quality need that expressed how the fittness of data for some use may be measured.'

### Comment

'Contextualized Dimension in the original framework  Describes an instance of the measure concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.  Describes the criteria for measuring an aspect of data quality related to some data quality need.   May be criteria for determining that data are COMPLETE or NOT_COMPLETE, or may be criteria for asserting a numeric measurement.  COMPLETE or NOT_COMPLETE measures are fundamental to data quality control, as set of data are filtered to the subset of data have quality for some need if all records are COMPLETE for all pertenent Measures.  A Measure is the data quality needs concept that paralells a MeasurementMethod at the solutions level, and a MeasurementAssertion at the report level.'


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

bdqffdq:DataQualityNeed|bdqffdq:ValidationConcept

### Definition

'A data quality need that expreses how data may be evaluated for fittness for use.'

### Comment

'ContextualizedCriterion in the original framework.  Describes the criteria for determining compliance of data to fill some data quality need.  A description of a criterion applied to an information element for some resource type.  Validations are phrased in a positive sense, they identify data which has quality for some need.  For example: The value of basisOfRecord of single records must be in the controlled vocabulary.   A Validation is the data quality needs concept that paralells a ValidationMethod at the solutions level, and a ValidationAssertion at the report level.  ValidationAssertions may specify a result that is COMPLIANT, where the data has quality, or NOT_COMPLIANT, where the data lacks quality.  Describes an instance of the criterion concept in terms of the associated information elements from some controlled vocabulary (fields actedUpon or consulted), and a resource type of SingleRecord or MultiRecord.   V = { v | v = < ie, c, rt >, ie ∈ IE, c ∈ C ⋀ rt ∈ RT }'


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

## Superclass

bdqffdq:FundamentalConcept

### Definition

'A portion of data with which a Data Quality Need is concerned.'

### Comment

'An information element identifies a portion of data to which a test pertains.  The information element in FFDQ can be represented as a single or composite element that consists of one or more terms from a controlled vocabulary (fields actedUpon or consulted by an assertion test) that identifies concepts in data relevant to a use case.  An abstraction or a concrete term that represents relevant content (e.g., coordinates; dwc.decimalLatitude, dwc:decimalLongitude).'


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

## Superclass

bdqffdq:FundamentalConcept

### Definition

'Category of things that are data objects about which data quality assertions may be made.'

### Comment

'In bdqffdq the concept of ResourceType has instances for SingleRecord or MultiRecord'


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

bdqffdq:FundamentalConcept|bdqffdq:SolutionsConcept

### Definition

'An entity that can execute data quality methods.'

### Comment

'Mechanisms may produce data quality reports as products.    

The FFDQ concept of mechanism describes the entity that performs an assertion test (code, external service, actor, etc.). Tied to a specification via the concept of an Implementation.'


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

bdqffdq:FundamentalConcept|bdqffdq:SolutionsConcept

### Definition

'A specific statement about how to evaluate a data quality need.'

### Comment

'A specification is a technical desription of an assertion test.  A specification is expected to have the following properies:  (1) Expected Response, (2) Authorities and Parameters.'


********************

## bdqffdq:AbstractInformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement

### Preferred Label

'Abstract Information Element'

### Label

'Abstract Information Element'

### Type

Class

## Superclass

bdqffdq:InformationElement

### Definition

'An InformationElement described in abstract terms and not linked with one or concrete terms.'

### Comment

'Information elements such as DATE and DAY are abstract, they could reference any representation of those concepts.  In contrast, dwc:eventDate and dwc:day can be linked to concrete Acted Upon or Consulted information elements.'


********************

## bdqffdq:ActedUpon

### Name

https://rs.tdwg.org/bdqffdq/terms/ActedUpon

### Preferred Label

'Acted Upon'

### Label

'Acted Upon'

### Type

Class

## Superclass

bdqffdq:InformationElement

### Definition

'An information element, expressed in concrete terms, about which a data quality need expresses assertions about the data quality in that element.'

### Comment

'An information element to which a Result applies.'


********************

## bdqffdq:Consulted

### Name

https://rs.tdwg.org/bdqffdq/terms/Consulted

### Preferred Label

'Acted Upon'

### Label

'Consulted'

### Type

Class

## Superclass

bdqffdq:InformationElement

### Definition

'An information element, expressed in concrete terms, about which a data quality need examines in order to expresses assertions about the data quality in another Information Element.'

### Comment

'An Information Element the content of which is examined to assert a result on one or more other Information Elements'


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

bdqffdq:MeaurementConcept|bdqffdq:Assertion

### Definition

'An assertion expressing the result of an implementation measuring a particular data quality need in a particular data resource.'

### Comment

'The Measure assertion type is a report level concept that describes a run of a test that performs a measurement according to some data quality dimension. In FFDQ, the Measure concept consists of a run result of COMPLETE or NOT_COMPLETE or a value of the measurement (i.e. a measure of dwc:eventDate duration in seconds).'


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

bdqffdq:MeaurementConcept|bdqffdq:DataQualityMethod

### Definition

'A data quality solution concept that relates a Measure to its Specifications.'

### Comment

'The MeasurementMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and a dimension in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


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

'A data quality need concept that expresses what assertions may be made about data with respect to fittness for use.'

### Comment

'Subtypes of DataQualityNeed are the Test Types.  Data Quality Need appoximates the informal concept of Test as used in BDQ Core.'


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

'A specific data quality need for which a specific Amendment is intended to improve.'

### Comment

'The ImprovementTarget concept in FFDQ describes which measures, issues, and validations are improved by some amendment. ImprovementTarget includes relationships between a contextualizedEnhancement (for an Amendment) and one or more contextualizedCriterion (link to validations) or contextualizedDimensions (link to measures).'


********************

## bdqffdq:Policy

### Name

https://rs.tdwg.org/bdqffdq/terms/Policy

### Preferred Label

'Policy'

### Label

'Policy'

### Type

Class

## Superclass

bdqffdq:NeedConcept

### Definition

'The set of Data Quality Needs for a Use Case'

### Comment

'Composition of Data Quality Needs into Use Cases'


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

'A needs concept expressing the composition of Policies to satisfy a Use Case.'

### Comment

'Profile in FFDQ is a DQ Needs level concept describing the UseCases that make up some data quality operation such as the behavior of a single actor or workflow producing the relevant assertions.   DQP (u) = {dqp | dqp = mp(u) ⋃ vp(u) ⋃ ip(u), mp ∈ MP , vp ∈ VP , ip ∈ IP ⋀ u ∈ U }'


********************

## bdqffdq:Criterion

### Name

https://rs.tdwg.org/bdqffdq/terms/Criterion

### Preferred Label

'Criterion'

### Label

'Criterion'

### Type

Class

## Superclass

bdqffdq:NeedConcept|bdqffdq:FundamentalConcept

### Definition

'Rule against which data are evaluated for conformance to quality criteria.'

### Comment

'General statement, for example: In a controlled vocabulary.  Composed with both Validations and Issues.'


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

## Superclass

bdqffdq:NeedConcept|bdqffdq:FundamentalConcept

### Definition

'An aspect of data quality.'

### Comment

'Describes the aspect of data quality (accuracy, precision, completeness, etc.) that a test examines. For example, [precision] in [coordinate precision of single records].'


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

bdqffdq:NeedConcept|bdqffdq:FundamentalConcept

### Definition

'A needs concept expressing a purpose to which data are put for which the data must have quality for the result of the purpose to have meaning and reliability.'

### Comment

'The UseCase concept in FFDQ describes some data quality control use case. The Amendment, Measurement and Validation policies that make up a use case define which assertions cover a given use case.  An example of a UseCase could be 'Check for internal consistency of dates', with validation policies for checking consistency between atomic date fields and an Amendment such as 'eventDate filled in from verbatim'.  Use Cases in bdqffdq are not the same as Use Cases in the software engineering sense, but  are similar bdqffdq formal statements derived from analyis of user stories.'


********************

## bdqffdq:IssuePolicy

### Name

https://rs.tdwg.org/bdqffdq/terms/IssuePolicy

### Preferred Label

'Issue Policy'

### Label

'Issue Policy'

### Type

Class

## Superclass

bdqffdq:Policy|bdqffdq:IssueConcept

### Definition

'A need concept that relates a Use Case to a set of supporting Issues.'

### Comment

'The ProblemPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedIssue relates to a use case. This relationship defines which problems are supported by a given use case.'


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

bdqffdq:Policy|bdqffdq:MeaurementConcept

### Definition

'A need concept that relates a Use Case to a set of supporting Measures.'

### Comment

'The MeasurementPolicy in FFDQ is a DQ Needs level concept that describes how some contextualizedDimension relates to a use case. This relationship defines which measures are supported by a given use case.'


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

bdqffdq:Policy|bdqffdq:ValidationConcept

### Definition

'A need concept that relates a Use Case to a set of supporting Validations.'

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

'A report concept expressing a statement about data quality assertion following some specification produced by some implementation pertaining to some data resource.'

### Comment

'The Assertion type in FFDQ is the fundamental concept that makes up a data quality report. Assertion can be any one of four types (represented as subClasses), Measure, Validation, Issue, and Amendement.  The assertion concept consists of a specification (the technical description of a performed test), a data resource (initial values of input data expressed in terms of some controlled vocabulary), the mechanism (external service, actor, or code that performs the test), and some form of result.'


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

'A report concept comprising a set of data quality assertions.'

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

'A thing to whch a data quality assertion applies.'

### Comment

'Describes a data resource described in terms of a controlled vocabulary such as dwc and represents the original values of the data operated on by an assertion test (i.e. an instance of dwc:Occurrence).'


********************

## bdqffdq:ResponseResult

### Name

https://rs.tdwg.org/bdqffdq/terms/ResponseResult

### Preferred Label

'Response.result'

### Label

'Response.result'

### Type

Class

## Superclass

bdqffdq:ReportConcept

### Definition

'A report concept to which a controlled vocabulary assertions about the result of the execution of the specification of a data quality need are attached.'

### Comment

'For Validations, response results may be COMPLIANT, or NOT_COMPLIANT.  For Measures, response result objects may be COMPLETE or NOT_COMPLETE.  For Issues, Response results may be PROBLEM, POSSIBLE_PROBLEM, or NOT_PROBLEM.  See the bdq: vocabulary.  Measures may also use a numeric data property.  Amendments assert a string data property.

The report result concept in FFDQ is represented as a value or a status for measures, just a result status for validations and a result status as well as values for changes propsed by amendments.'


********************

## bdqffdq:ResponseStatus

### Name

https://rs.tdwg.org/bdqffdq/terms/ResponseStatus

### Preferred Label

'Response.status'

### Label

'Response.status'

### Type

Class

## Superclass

bdqffdq:ReportConcept

### Definition

'A report concept expressing controlled vocabulary values about the exit state of an execution process of a data quality specification by an implementation.'

### Comment

'The ResponseStatus is metadata, indicating if data should be present in a ResponseResult.  

Depending on the assertion type would have values of COMPLIANT or NON_COMPLIANT for a Validation, COMPLETE or NOT_COMPLETE for a Measure, CURATED, FILLED_IN,TRANSPOSED, NO_CHANGE for an Amendment and HAS_PROBLEM NO_PROBLEM for a Problem.  A separate concept describes the result state as values of AMBIGIOUS, INTERNAL_PREREQUISITES_NOT_MET and EXTERNAL_PREREQUISITES_NOT_MET.'


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

'A solutions concept that relates a data quality need to a specification.'

### Comment

'DataQualityMethods are associative entities that allow specifications or data quality tests to be reused by supporting a many to many relationship between the two.'


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

'A solutions concept that describes the portion of a Mechanism that carries out the proccess described in a particular Specification.'

### Comment

'The FFDQ derived concept of an Implementation describes the relationship between a specification (technical description of a test) and the mechanism that implements it.'


********************

## bdqffdq:Parameter

### Name

https://rs.tdwg.org/bdqffdq/terms/Parameter

### Preferred Label

'Parameter'

### Label

'Parameter'

### Type

Class

## Superclass

bdqffdq:SolutionsConcept

### Definition

'A value that, when provided to a test Specification changes the behavior of the test in a defined manner.'


********************

## bdqffdq:ValidationAssertion

### Name

https://rs.tdwg.org/bdqffdq/terms/ValidationAssertion

### Preferred Label

'Validation Assertion'

### Label

'Validation Assertion'

### Type

Class

## Superclass

bdqffdq:ValidationConcept|bdqffdq:Assertion

### Definition

'An assertion expressing the result of an implementation validating compliance with a a particular data quality need in a particular data resource.'

### Comment

'The Validation assertion type is a report level concept that describes a run of a test for validity. The Validation concept in FFDQ consists of a run result of COMPLIANT or NON_COMPLIANT and a criterion that describes the conditions for validity that result in a status of COMPLIANT.'


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

bdqffdq:ValidationConcept|bdqffdq:DataQualityMethod

### Definition

'A data quality solution concept that relates an Validation to its Specifications.'

### Comment

'The ValidationMethod in FFDQ is a DQ Solutions level concept describing the relationship between a specification (technical description of a test) and a criterion in the context of resource type (SingleRecord or MultiRecord) and associated information elements.'


********************


# DataProperty terms

********************

## bdqffdq:hasAuthoritiesDefaults

### Name

https://rs.tdwg.org/bdqffdq/terms/hasAuthoritiesDefaults

### Preferred Label

'has Authorities and Defaults'

### Label

'has Authorities and Defaults'

### Type

DataProperty

### Definition

nan

### Comment

'Details of the bdq:sourceAuthoritiy listed in a Specification, along with Parameters that may be provided to the expected response along with their default values.'


********************

## bdqffdq:hasExpectedResponse

### Name

https://rs.tdwg.org/bdqffdq/terms/hasExpectedResponse

### Preferred Label

'has Expected Response'

### Label

'has Expected Response'

### Type

DataProperty

### Definition

nan

### Comment

'The description of the logic of a test specification.  An expected response is expected to be a data property of a Specification'


********************

## bdqffdq:hasResponseComment

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseComment

### Preferred Label

'has Response Comment'

### Label

'has Response Comment'

### Type

DataProperty

### Definition

'Free text describing the assertion made in the response and why that conclusion was reached.'

### Comment

'Intended for consumption by human readers of data qualiy reports to understand why particular assertions were made.'


********************

## bdqffdq:hasResponseResultValue

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseResultValue

### Preferred Label

'has response result value'

### Label

'has response result value'

### Type

DataProperty

### Definition

nan

### Comment

'Applies to AmendmentAssertions.   To support bdqcore: tests, is expected to carry a key:value list where the keys are the names of ActedUpon Information Elements, and the values are the proposed new values (filling in or replacing the values of those terms in the input).'


********************


# NamedIndividual terms

********************

## bdqffdq:MultiRecord

### Name

https://rs.tdwg.org/bdqffdq/terms/MultiRecord

### Preferred Label

nan

### Label

'Multi Record'

### Type

NamedIndividual

### Definition

nan


********************

## bdqffdq:SingleRecord

### Name

https://rs.tdwg.org/bdqffdq/terms/SingleRecord

### Preferred Label

nan

### Label

'Single Record'

### Type

NamedIndividual

### Definition

nan

### Comment

'A record from a dataset without dependencies on any other record.'


********************


# ObjectProperty terms

********************

## bdqffdq:amendmentProperty

### Name

https://rs.tdwg.org/bdqffdq/terms/amendmentProperty

### Preferred Label

'amendment Property'

### Label

'amendment  Property'

### Type

ObjectProperty

### Definition

nan

### Comment

'Sub properties of this type group object properties that apply to amendment concepts such as AmendmentPolicy (DQ Needs), AmendmentMethod (DQ Solutions) and Amendment (DQ Reports).'


********************

## bdqffdq:appliesTo

### Name

https://rs.tdwg.org/bdqffdq/terms/appliesTo

### Preferred Label

'applies To'

### Label

'applies To'

### Type

ObjectProperty

### Definition

'Describes the DataResource about which an Assertion is made.'

### Comment

'If an Assertion forms the oa:body of an oa:Annotation, the appliesTo DataResource would be the oa:target of the Annotation.'


********************

## bdqffdq:composedOf

### Name

https://rs.tdwg.org/bdqffdq/terms/composedOf

### Preferred Label

'composed of'

### Label

'composed of'

### Type

ObjectProperty

### Definition

nan

### Comment

'Describes the properties from a controlled vocabulary that compose an InformationElement. For example, an InformationElement may be 'composedOf' properties such as dwc:day, dwc:month and dwc:year.'


********************

## bdqffdq:forAmendment

### Name

https://rs.tdwg.org/bdqffdq/terms/forAmendment

### Preferred Label

'for Amendment'

### Label

'for Amendment'

### Type

ObjectProperty

### Definition

nan

### Comment

'Use to link AmendmentMethods to Amendments.  Describes the relationship between an Amendment concept in FFDQ (needs, solutions, reports) and a ContextualizedEnhancement.'


********************

## bdqffdq:forIssue

### Name

https://rs.tdwg.org/bdqffdq/terms/forIssue

### Preferred Label

'for Issue'

### Label

'for Issue'

### Type

ObjectProperty

### Definition

nan

### Comment

'Use to link IssueMethods to Issues.  Describes the relationship between a problem concept in FFDQ (needs, solutions, reports) and a ContextualizedIssue.'


********************

## bdqffdq:forMeasure

### Name

https://rs.tdwg.org/bdqffdq/terms/forMeasure

### Preferred Label

'for Measure'

### Label

'for Measure'

### Type

ObjectProperty

### Definition

nan

### Comment

'Use to link MeasurementMethods to Measures.'


********************

## bdqffdq:hasActedUponInformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasActedUponInformationElement

### Preferred Label

'has Acted Upon Information Element'

### Label

'has Acted Upon Information Element'

### Type

ObjectProperty

### Definition

nan

### Comment

'Provides a relationship between FFDQ concepts and the information elements that are ActedUpon in a test.'


********************

## bdqffdq:hasConsultedInformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasConsultedInformationElement

### Preferred Label

'has Consulted Information Element'

### Label

'has Consulted Information Element'

### Type

ObjectProperty

### Definition

nan

### Comment

'Provides a relationship between FFDQ concepts and the information elements that are Consulted, but not ActedUpon in a test.'


********************

## bdqffdq:hasCriterion

### Name

https://rs.tdwg.org/bdqffdq/terms/hasCriterion

### Preferred Label

'has Criterion'

### Label

'has Criterion'

### Type

ObjectProperty

### Definition

nan

### Comment

'Used to link the derived concept of a Validation to the fundamental concept of a Criterion.'


********************

## bdqffdq:hasDataQualityDimension

### Name

https://rs.tdwg.org/bdqffdq/terms/hasDataQualityDimension

### Preferred Label

'has Data Quality Dimension'

### Label

'has Data Quality Dimension'

### Type

ObjectProperty

### Definition

'The DataQualityDimension to which a DataQualityNeed Applies.'

### Comment

'Used to link a derived concept of a DataQualityNeed (Measure, Validation, Amendment, or Issue) to the fundamental concept of a DataQualityDimension.  For a Measure, the dimension of data quality measured.   For a Validation or Issue, the dimension of data quality assessed.  For an Amendment, the dimension of data quality to be improved.  Under the original formulation of the Framework, only Measures have Dimensions.'


********************

## bdqffdq:hasEnhancement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasEnhancement

### Preferred Label

'has Enhancement'

### Label

'has Enhancement'

### Type

ObjectProperty

### Definition

nan

### Comment

'Used to link the derived property of an Amendment to the Fundamental property of an Enhancement.'


********************

## bdqffdq:hasInformationElement

### Name

https://rs.tdwg.org/bdqffdq/terms/hasInformationElement

### Preferred Label

'has Information Element'

### Label

'has Information Element'

### Type

ObjectProperty

### Definition

nan

### Comment

'Provides a relationship between FFDQ concepts and the information elements. For example, ContextualizedCriterion uses this property along with hasResourceType to define a criterion in the context of related information elements.'


********************

## bdqffdq:hasParameter

### Name

https://rs.tdwg.org/bdqffdq/terms/hasParameter

### Preferred Label

'has Parameter'

### Label

'has Parameter'

### Type

ObjectProperty

### Definition

'A relationship between a test class and a Parameter'

### Comment

'Expected to be a relationship between a Specification and a Parameter'


********************

## bdqffdq:hasResourceType

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResourceType

### Preferred Label

'has Resource Type'

### Label

'has Resource Type'

### Type

ObjectProperty

### Definition

nan

### Comment

'Provides additional metadata, along with the information elements, that describes the level (SingleRecord or MultiRecord) at which the FFDQ concept operates. For example, an enhancementInContext with resource type of MultiRecord could be used to define an Amendment that applies at the level of multiple record values.'


********************

## bdqffdq:hasResponseResult

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseResult

### Preferred Label

'has Response Result'

### Label

'has Response Result'

### Type

ObjectProperty

### Definition

nan

### Comment

'Used in the DQ Report concept to describe response result objects. For example, values could be bdq:RUN_HAS_RESULT or bdq:INTERNAL_PREREQUISITES_NOT_MET.   If Response.results are not objects, use the datatype property hasResponseResultValue'


********************

## bdqffdq:hasResponseStatus

### Name

https://rs.tdwg.org/bdqffdq/terms/hasResponseStatus

### Preferred Label

'has Response Status'

### Label

'hase Response Status'

### Type

ObjectProperty

### Definition

nan

### Comment

'Used in the DQ Report concept to describe result status. For example, in the case of a Validation result, values could be bdq:COMPLIANT or bdq:NON_COMPLIANT.'


********************

## bdqffdq:hasSpecification

### Name

https://rs.tdwg.org/bdqffdq/terms/hasSpecification

### Preferred Label

'has Specification'

### Label

'has Specification'

### Type

ObjectProperty

### Definition

nan

### Comment

'Describes the relationship between a derived FFDQ concept and the fundamental concept of a specification (technical description of a test).'


********************

## bdqffdq:hasUseCase

### Name

https://rs.tdwg.org/bdqffdq/terms/hasUseCase

### Preferred Label

'has Use Case'

### Label

'has Use Case'

### Type

ObjectProperty

### Definition

nan

### Comment

'Used by concepts in the DQ Needs category to describe the relationship between DQ Policies (ValidationPolicy, AmendmentPolicy, MeasurementPolicy) and an instance of the use case covered by that policy.'


********************

## bdqffdq:hasValidation

### Name

https://rs.tdwg.org/bdqffdq/terms/hasValidation

### Preferred Label

'has Validation'

### Label

'has Validation'

### Type

ObjectProperty

### Definition

nan

### Comment

'Use to link ValidationPolicies and ValidationMethods to Validations.  Describes the relationship between a validation concept in FFDQ (needs, solutions, reports) and a contextualizedCriterion.'


********************

## bdqffdq:implementedBy

### Name

https://rs.tdwg.org/bdqffdq/terms/implementedBy

### Preferred Label

'implemented By'

### Label

'implemented By'

### Type

ObjectProperty

### Definition

nan

### Comment

'Describes the link between the Implementation concept in FFDQ and the Mechanism that implements some specification (also defined in Implementation).'


********************

## bdqffdq:improvedBy

### Name

https://rs.tdwg.org/bdqffdq/terms/improvedBy

### Preferred Label

'improved By'

### Label

'improved By'

### Type

ObjectProperty

### Definition

nan

### Comment

'Had Domain: Amendment, Range Improvement Target.   Asserting improvement target could be improved by the Amendment.  Object property that describes an enhancement, as part of the ImprovementTarget, that would improve data acted upon by some set of measures or validations.  This can be used to determine which measures and validations are improved upon by a given amendment.'


********************

## bdqffdq:includedInPolicy

### Name

https://rs.tdwg.org/bdqffdq/terms/includedInPolicy

### Preferred Label

'included In Policy'

### Label

'included in Policy'

### Type

ObjectProperty

### Definition

'Assserts that a Data Quality Need is part of a Policy'


********************

## bdqffdq:issueProperty

### Name

https://rs.tdwg.org/bdqffdq/terms/issueProperty

### Preferred Label

'issue Property'

### Label

'issue Property'

### Type

ObjectProperty

### Definition

nan

### Comment

'Category of properties that apply to Issues.'


********************

## bdqffdq:measurementProperty

### Name

https://rs.tdwg.org/bdqffdq/terms/measurementProperty

### Preferred Label

'measurement Property'

### Label

'measurement Property'

### Type

ObjectProperty

### Definition

nan

### Comment

'Sub properties of this type group object properties that apply to measurement concepts such as MeasurementPolicy (DQ Needs), MeasurementMethod (DQ Solutions) and Measure (DQ Reports).'


********************

## bdqffdq:producesAssertion

### Name

https://rs.tdwg.org/bdqffdq/terms/producesAssertion

### Preferred Label

'produces Assertion'

### Label

'produces Assertion'

### Type

ObjectProperty

### Definition

'Connects an entity that creates an assertion with the assertion.'

### Comment

'Connects Implementations with Assertions'


********************

## bdqffdq:reportProperty

### Name

https://rs.tdwg.org/bdqffdq/terms/reportProperty

### Preferred Label

'report Property'

### Label

'report Property'

### Type

ObjectProperty

### Definition

nan

### Comment

'Category of properties used in reports.'


********************

## bdqffdq:targetedIssue

### Name

https://rs.tdwg.org/bdqffdq/terms/targetedIssue

### Preferred Label

'targeted Issue'

### Label

'targeted Issue'

### Type

ObjectProperty

### Definition

'Issue where the data conformance with needs may be improved by accepting proposals from an Amendment via an ImprovementTarget.'

### Comment

'The issue targeted by some problem via the ImprovementTarget object.'


********************

## bdqffdq:targetedMeasure

### Name

https://rs.tdwg.org/bdqffdq/terms/targetedMeasure

### Preferred Label

'targeted Measure'

### Label

'targeted Measure'

### Type

ObjectProperty

### Definition

'Measure where the data conformance with needs may be improved by accepting proposals from an Amendment via an ImprovementTarget.'

### Comment

'Describes the relationship between an improvement target and a Measure.  Was, but dimension is too abstract: The dimension targeted by some enhancement via the ImprovementTarget object.'


********************

## bdqffdq:targetedValidation

### Name

https://rs.tdwg.org/bdqffdq/terms/targetedValidation

### Preferred Label

'targeted Validation'

### Label

'targeted Validatiohn'

### Type

ObjectProperty

### Definition

'Validation where the data conformance with needs may be improved by accepting proposals from an Amendment via an ImprovementTarget.'

### Comment

'Relates an improvement target to a Validation.  Was: The criteria targeted by some enhancement via the ImprovementTarget object.  But, too abstract.'


********************

## bdqffdq:validationProperty

### Name

https://rs.tdwg.org/bdqffdq/terms/validationProperty

### Preferred Label

'validation Property'

### Label

'validation Property'

### Type

ObjectProperty

### Definition

nan

### Comment

'Sub properties of this type group object properties that apply to validation concepts such as ValidationPolicy (DQ Needs), ValidationMethod (DQ Solutions) and Validation (DQ Reports).'


********************

