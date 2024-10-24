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

{previous_version_slot}

Abstract
: {abstract}

{authors_contributors}
Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}

### Table of Contents ###

{toc} 

## 1 Introduction

Biodiversity Data Quality (BDQ) Core, hereafter referred to as 'BDQ Core', consists of 1) specifications of data quality tests that can be implemented to provide reproducible results from a given set of input data and test parameters, 2) a generic fitness for use framework (bdqffdq:) whose terms and semantics are embodied in an ontology, 3) a set of controlled vocabularies for the terms bdqffdq:DataQualityDimension, bdqffdq:Enhancement, and bdqffdq:Criterion, 4) a supporting vocabulary of terms (bdq:) used in the specification of the previously mentioned tests, 5) an exemplar data set to use as input for validation of the behavior of implementations of the previously mentioned tests, 6) a guide to implementation of the tests,  7) a guide to the interpretation of the results of the tests, and 8) a guide to the bdqffdq: Framework for describing data quality.

Not part of BDQ Core, but dependent on it, is an exemplar implementation of the tests, written in Java(R), the behavior of which has been validated against the uses the previously mentioned validation data set.

BDQ Core covers a specification of tests for the quality of biodiversity data, not a specification of the quality to which biodiversity data are expected to conform. ‘Fitness for use’ of a biodiversity data record depends on the use to which it is applied: a record that is unsuitable to be used in one application may be suitable for another application (Belbin et al 2013).  Data does not have quality in the abstract, it only has quality with respect to some use, within BDQ Core, bdqffdq:UseCases provide a formal representation of uses to which data may be put.  The set of Tests and UseCases defined in BDQ Core are a starting point, not a limitation.  The BDQ Core tests may be composed differently for different uses, and additional tests are expected. 

The BDQ tests support the determination of whether data resources will be fit for use for some particular purpose from the perspectives of the data quality dimensions `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, and `Resolution`. The tests themselves do not assert data quality, rather, sets of tests can be defined to support the assessment or assurance of data quality for a particular purpose by analyzing their responses to the input data in question against predefined expectations. This standard does not specify a structure to capture 'profiles' - component tests, order of processing, and expected results - for particular cases of fitness for use.

The BDQ tests were initially targeted specifically to [Darwin Core](https://dwc.tdwg.org/terms/) classes and properties against which they operate. This is not a limitation on the scope of the standard, but rather a choice of original scope against which to develop the tests.

### 1.1 Purpose

This document introduces BDQ Core.

### 1.2 Audience

This document is a general introduction to BDQ Core standard designed for anyone interested in specifications for the assessment or assurance of fitness for use of biodiversity data, or to improve it. 

### 1.3 Associated Documents

Those who want  quick view of the Tests should consult the [BDQ Core Tests Quick Reference Guide](../terms/bdqcore/index.md). Those interested in more detail on the interpretation of test results should consult the [BDQ Core User's Guide](../guide/users/index.md "BDQ Core Users Guide"), while those interested in the implementation of tests following the BDQ Core should consult the [BDQ Core Implementer's Guide](../guide/implementers/index.md "BDQ Core Implementation Guide").

### 1.4. Status of the Content of This Document

Section 3 of this document is normative.  

All other sections of this document are non-normative.

### 1.5 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace Abbreviations

The following namespace abbreviations are used in this document:

**CHECK THIS set on final draft, include only those used in this document**

| **Prefix**   | **Namespace**                                    |
|--------------|--------------------------------------------------|
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms/               |
| bdqcrit      | https://rs.tdwh.org/bdqcrit/terms/               |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms/                |
| bdqenh       | https://rs.tdwg.org/bdqenh/terms/                |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms/               |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema#            |
| owl          | http://www.w3.org/2002/07/owl#                   |
| xsd          | http://www.w3.org/2001/XMLSchema#                |

## 2 Parts of the Standard

### 2.1 Vocabularies

The focus of this standard is on (1) a framework for describing data quality and (2) the description of a set of tests and assertions using that framework.  The framework is instantiated formally as an ontology (namespace abbreviation bdqffdq:).  The tests are instantiated formally as a vocabulary (namespace abbreviation `bdqcore:`), with test names, labels, descriptions, expected responses and other metadata. The tests and assertions specifications make use of additional vocabularies, three of which are defined by this standard. Together the vocabularies serve to support the specification of suites of biodiversity data quality assessments and amendments to improve data for particular purposes. Each vocabulary is described in full in its distinct Term List document, linked from and summarized together on [BDQ Core Vocabularies](../vocabularies/index.md). 

### 2.2 Test Guidance

Beyond data availability, data quality is probably the most significant issue for users of biodiversity data. The BDQ Core standard suite of tests and assertions is meant to be used by data collectors, data providers, and data users to assess and potentially improve data quality.  

The Fitness for Use Framework upon which BDQ Core is based allows pipelines of tests and assertions to have formal dependencies between them, such as a specified order in which they should be run in order to get a deterministic result, or using the results of some tests as the inputs to other tests, or building composite tests from other existing tests. By design, dependencies are manifest in some of the tests and assertions that are Measures, while tests and assertions that are Issues, Validations, and Amendments tend to be independent of each other.

Tests, even those labeled as Amendments, do not modify original data. Instead, test responses contain the information needed to amend original data by providing reproducible interpretations. These interpretations can be as a substitute for the original data or can be used to vet and amend the original data, as appropriate.

Test specifications consist of the metadata (e.g., identifier, preferred label, description, information elements acted upon, information elements consulted, expected response, data quality dimension, parameters and default behavior, notes) required to understand the test, its context, and its potential uses, and to implement it in a way that is compliant with the standard.

The specifications for expected responses from tests consist of metadata (status, result, and comment) required for a user to interpret and act upon the data (information elements) pertinent to the test that was run, whether the information elements were those consulted or those acted upon.

The [BDQ User's Guide](../guide/users/index.md) is intended to contain everything needed to understand the nature or the tests and the responses from them when they are run. 

The [BDQ Implementer's Guide](../guide/implementers/index.md) is intended to contain everything needed to understand the requirements for compliant implementations of the tests. 

[!--- JRW first pass finished to here ---]

[Synthetic and Modified Data](../synthetic/index.md) Describes how to mark synthetic and altered data that may be used to validate test implementations to distinguish it from real data.


### 2.3 Implementation Validation Data 

See the [BDQ Implementer's Guide](../guide/implementers/index.md) for information on a set of data for validating test implementations.. 

### 2.4 Exemplar Tests Implementation

<!--- PJM: Does section 2.4 belong?  The filteredpush implementations aren't part of the standard --->

### 2.6 Test Lists

The [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md) is a quick reference guide to the tests defined in BDQ Core. 

### 2.7 Test Execution Environments and Workflows

Neither the test descriptions nor the framework impose constraints on workflows for execution.  One possible workflow is to run all validations, then all amendments, then all validations again on a modified copy of the input data to which all proposed amendments have been applied.

A single validation step, with measures evaluating the results of the amendments could look like the diagram below.

![Diagram of workflow through single validation step](workflow_single_iteration.svg)

Expanding on this single validation step, amendments can be run and their results fed back into a second phase of post-amendment validation, with measures again evaluating the results of validation of the input data if all changes proposed by amendments are accepted.

![Diagram of workflow with pre-amendment validation+measure phase, followed by amendment phase, followed by post-amendment validation-measure phase](workflow_two_iterations.svg)


## 3 Design of the Tests (normative)

<!--- PJM: Section 3 is Important elements to put in the introduction --->

### 3.1 Data Quality Control, Data Quality Assurance (normative)

BDQ Core draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.  Implementations of the bdqcore tests MAY be used to perform Quality Control, Quality Assurance, or both.  The [mathematical formalization](..//bdqffdq/index.md#5-fitness-for-use-framework-summary-of-mathematical-formalization-normative) of the bdqffdq Framework provides a formal definition of Quality Control and Quality Assurance, and how Test Assertions SHOULD be used for each.

### 3.2 When are Tests Run (normative)

The bdqcore tests are designed to be run at any point in the life cycle of biodiversity data. They MAY be run at the point of initial collection or observation of organisms. They MAY be run to support data transcription. They MAY be run in loading data into databases of records from field or transcription sources. They MAY be run in preparing data from databases of record for aggregation. They MAY be run during data aggregation and the presentation of aggregated data.  They MAY be run in workflows for analysis of data for research purposes.

### 3.3 Results of Test Executions (normative)

BDQ Core is agnostic about the format of presentation of results from BDQ Core Tests.  BDQ Core does, however, specify that test implementations and presentations MUST return structured data with at least bdq:Response.status, bdq:Response.result, and bdq:Response.comment  Responses MAY also contain more information in Response.qualifier.  See the implementer's guide section on [Presentation of Results](../guide/implementers/index.md#7-Presentation-of-Results) for further normative and non-normative guidance about result presentation See the bdqcore: landing page section on the [Structure of a Response](../bdqcore/index.md#31-Structure-of-Response-normative) for normative guidance on Responses as RDF or as data structures.

The results of the execution of implementations of the bdqcore: tests MAY be presented as Data Quality reports.  The bdqffdq: framework provides vocabulary and structure that MAY be used for such data quality reports.

The bdqffdq: vocabulary enables the wrapping of the results of bdqcore: tests within annotations.  The bdqffdq: vocabularies in particular are intended to support the framing of assertions from tests within annotations that follow the W3C Web Annotation Data Model (Sanderson et al. 2017), and are suitable for inclusion in semantic data stores.  See the section on [Annotations](../guide/implementers/index.md#72-Annotations-normative) in the implementer's guide for more guidance.

## 4 Contributions and Acknowledgements

### 4.1 Acknowledgements

The Authors gratefully acknowledge all those who have commented on the GitHub issues during the development of BDQ Core, and all those who have contributed to discussions at various workshops in São Paulo, Brazil; Canberra, Australia; Monash, Australia; Leiden, The Netherlands; Gainesville, USA; and Seattle, USA) and at TDWG annual meetings (in Jonkopping, Sweden; Santa Clara de San Carlos, Costa Rica; Ottawa, Canada; Dunedin, New Zealand; Leiden, The Netherlands; Sofia, Bulgaria; Hobart, Australia; and Ginowa, Japan; and the various Virtual meetings. The Authors are also gratefull for all those who responded to our email questions.

We'd also aknowledge the continued support of the TDWG (Biodiversity Information Standards) Executive over the unusual 10 years of the project.

#### 4.1.1 Funding and Support

We acknowledge the financial support of The Atlas of Living Australia and Biodiversity Information Standards (TDWG) for Lee Belbin and Arthur Chapman to attend two face-to-face meetings for the development of BDQ Core, and the Atlas of Living Australia for support of John Wieczorek to attend meetings in Canberra Australia. The Museum of Comparative Zoology provided support for Paul Morris; VertNet, Kurator, and Rauthflor LLC provided support of John Wieczorek. The United States National Science Foundation through funding of the Kurator project, provided time for Paul Morris, Robert Morris and David Lowery for early work on the project.

The São Paulo Research Foundation (FAPESP), the Universidade de São Paulo (USP) provided facilities, and with the Global Biodiversity Information Facility and others, supported participants to attend the meeting in São Paulo, Brazil. The US National Science Foundation through iDigBio provided support for the meeting in Gainesville, Florida.

### 4.2 Contributions

Many people have contributed to the development of the BDQ Core standard.  

#### 4.2.1 Authors 

We recognize four people as authors of the standard, having contributed consistently over the last decade and having been heavily engaged in writing the core test descriptors and the BDQ core documentation. 
 - **Lee Belbin (Blatant Fabrications)**: Test descriptions, test validation data, author of BDQ Core documents, Convenor of Task Group 2; 
- **Arthur D Chapman (Australian Biodiversity Information Services)**: Test descriptions, test validation data, author of BDQ Core documents. Convenor of the TDWG Data Quality Interest Group; 
- **Paul J Morris (Museum of Comparative Zoology, Harvard University)**: Test descriptions, bdqffdq ontology, Java test implementations in filteredpush packages, author of BDQ Core documents; 
- **John Wieczorek (VertNet)**: Test descriptions, test implementations, author of BDQ Core documents, Darwin Core liaison.

#### 4.2.2 Contributors

There were many people who have made notable contributions at various times during the development of BDQ Core. 
- **Yi-Ming Gan (Royal Belgian Institute of Natural Sciences)**: Contributed to finalization of the test descriptors, explanatory workflow diagrams, edits to text of BDQ Core documents;
- **António Mauro Saraiva (Universidade de São Paulo)**: Development of the Fitness for Use Framework (Task Group 1), facilitated test development workshop, Co-convenor of Data Quality Interest Group until 2022;
- **Alan Koch Veiga (Universidade de São Paulo)**: Developed the Fitness for Use Framework as his disertation, Convenor of Task Group 1: Framework on Data Quality;
- **Paula F. Zermoglio (Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN), San Carlos de Bariloche)**: Contributions to multiple test descriptions and vocabulary development, Convenor of Task Group 4: Best Practices for Development of Vocabularies of Value;
- **Alexander Thompson (iDigBio)**: Key contributions to initial development of test descriptors, migrated test descriptors into markdown tables in github issues;
- **David Lowery (Museum of Comparative Zoology, Harvard University)**: Initial development of ontology reprentation of the Fitness for Use Framework, developer of kurator-ffdq Java class representation of the framework;
- **Christian Gendreau (Agriculture and Agri-Food Canada)**: Intitial contribitions to data quality discussions, vocabulary definitions and early test development;
- **Tim Roberston (Global Biodiversity Information Facility)**: Contributions to test descriptions, clarification of GBIF vocabulary and API resources for the tests;
- **Dmitry Schigel (Global Biodiversity Information Facility)**: Intitial contribitions to data quality discussions and vocabulary definitions, GBIF Representative to the Data Quality Interest Group in early years;
- **Robert A. Morris (late, of UMass Boston)**: Competency questions for the Fitness for Use Framework as an ontology, guided intital development of the ontology representation of the framework;
- **Miles Nicholls (Atlas of Living Australia)**: Use Case analysis, Convenor of Task Group 3: Data Quality Use Cases;
- **Emily Rose Rees (Atlas of Living Australia)**: Use Case analysis in Task Group 3: Data Quality Use cases;
- **Abigail Benson (U.S. Geological Survey)**: Intitial contribitions to data quality discussions and vocabulary definitions.

## 5 Acronyms

| **Acronym** | **Explanation**                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------|
| ALA         | Atlas of Living Australia                             | 
| BDQ         | TDWG Biodiversity Data Quality                        |
| BDQIG       | Biodiversity Data Quality Interest Group              |
| BISON       | Biodiversity Information Serving Our Nation           |
| CRIA        | Centro de Referência em Informação Ambiental          |
| EPSG        | European Petroleum Survey Group                       |
| GBIF        | Global Biodiversity Information Facility              |
| iDigBio     | Integrated Digitized BioCollections                   |
| IRI         | Internationalized Resource Identifier                 |
| ISO         | International Standards Organization                  |
| TDWG        | Biodiversity Information Standards                    |
| TG1         | Biodiversity Data Quality Interest Group Task Group 1: Framework on Data Quality |
| TG2         | Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions |
| TG3         | Biodiversity Data Quality Interest Group Task Group 3: Data Quality Use Cases     |
| TG4         | Biodiversity Data Quality Interest Group Task Group 4: Best Practices for Development of Vocabularies of Value |

## 6 Glossary

Glossary of terms used in BDQ Core that are additional to those included in the various Namespace: vocabularies.

| Label | Definition | Context | Comment |
| ---- | ---- | ---- | ---- |
| ASSUMEDDEFAULT | A bdqffdq:Amendment that replaces a bdq:EMPTY term with a predefined default bdq:Parameter value. | Term-Action | Would be used only in an extension or in bdq:Response.comment. bdq:Response.status value for this case is bdq:AMENDED. |
| CENTREOFCOUNTRY | Testing if bdqffdq:EnformationElements COORDINATES identify the centre of the dwc:country, allowing for a spatial buffer. | Term-Action | |
| COMPLETE | Testing if bdqffdq:InformationElement dwc:scientificNameId forms a valid and complete identifier. | Term-Action | Testing for bdqdim:Completeness. |
| CONSISTENT | Identifies consistency among values between bdqffdq:InformationElements. | Term-Action | Testing for bdqdim:Consistency. |
| CONVERTED | A conversion has been proposed to values in the bdqffdq:InformationElements to conform with a targeted geographic reference system. | Term-Action | See Test [AMENDMENT_COORDINATES_CONVERTED](https://rs.tdwg.org/bdqcore/terms/ (620749b9-7d9c-4890-97d2-be3d1cde6da8). |
| COORDINATES | A general category of specific bdq:InformationElements that represents the combination of the Darwin Core terms dwc:decimalLatitude and dwc:decimalLongitude and may include metadata terms including dwc:geodeticDatum. | bdqffdq:InformationElement |  |
| COORDINATESTERRESTRIALMARINE | A terrestrial taxon that has geographic coordinates that fall within terrestrial boundaries; or a marine taxon that has geographic coordinates that fall within marine boundaries. | Term-Action | Use bdq:AMENDED as the bdq:Response.status, report bdq:COORDINATESTERRESTRIALMARINE in a bdq:Response.qualifier or in a bdq:Response.comment. See Test [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b9c184ce-a859-410c-9d12-71a338200380). |
| CRS | Coordinate Reference System - (also spatial reference system). A coordinate system defined in relation to a standard reference or datum (Chapman & Wieczorek 2020). | Test |  |
| DURATIONINSECONDS | The duration in seconds of bdq:InformationElement dwc:eventDate. | Term-Action | See Test [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53). |
| FOUND | The value in a bdqffdq:InformationElement that matched a value in a bdq:sourceAuthority. | Term-Action | Use bdq:COMPLIANT for bdq:Response.result, and include this in bdq:Response.comments or bdq:Response.qualifier. |
| FROM | An Output bdqffdqInformationElement is being populated from a more primary Input bdqffdq:InformationElement. | Term-Action | For example, the Test [AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](https://rs.tdwg.org/bdqcore/terms/f01fb3f9-2f7e-418b-9f51-adf50f202aea) populates dwc:scienticName from dwc:scientificNameId. |
| geodetic coordinate reference system | A coordinate reference system based on a geodetic datum, used to describe positions on the surface of the earth (Chapman and Wieczorek 2020). | Test | |
| geodetic datum | A mathematical model that uses a reference ellipsoid to describe the size and shape of the surface of the earth and adds to it the information needed for the origin and orientation of coordinate systems on that surface (Chapman and Wieczorek 2000). | Test |  |
| GEOGRAPHY | A general category of specific bdq:InformationElements that represents a combination of Darwin Core administrative geography terms dwc:continent, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality. | bdqffdq:InformationElement |  |
| INRANGE | The value of bdqffdq:InformationElements that are within an acceptable range. | Term Action | Use in bdq:Response.qualifier or bdq:Response.comment. |
| Java | Java is a registered trademark of Oracle and/or its affiliates. | BDQ Core |  |
| LESSTHAN | A Term-Action indicating that the value in one bdq:InformationElement is less than the value in another bdq:InformationElement. | Term-Action | Used in tests for Depth and Elevation. |
| non-printing characters | ASCII 0-32 and 127 decimal. Non printing characters or formatting marks that are not displayed at printing. These may include pilcrow, space, non-breaking space, tab character. etc. For the purposes of the tests they are treated as bdq:Empty. | Data |  |
| NOTEMPTY | An bdqffdq:InformationElement contains some non-empty value | Term-Action | For example the Test [VALIDATION_EVENTDATE_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/f51e15a6-a67d-4729-9c28-3766299d2985). |
| null | A value that is used in some databases to signify that a value is unknown or missing. It may be represented in serializations by "NULL", "Null", "null". "/n", "9999", etc. These should be treated as bdq:NotEmpty. | Data |  |
| POLYNOMIAL | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet. | bdqffdq:InformationElement | See test [VALIDATION_POLYNOMIAL_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/17f03f1f-f74d-40c0-8071-2927cfc9487b). |
| PRECISIONINSECONDS | The length of the period of an event in seconds. | Term-Action | This is description of the bdq:Response.result from this bdqffdq:Measure, where the result is a numeric value in seconds. See Test [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53). |
| PREREQUISITESNOTMET | A test of type bdqffdq:Measure that counts the number of tests of type bdqffdq:Validation that did not run due to one or more prerequisites not being met (e.g. bdq:INTERNAL_PREREQUISITES_NOTMET). | Term-Action | See Test [MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](https://rs.tdwg.org/bdqcore/terms/49a94636-a562-4e6b-803c-665c80628a3d). |
| PROPOSED | A test of type bdqffdq:Measure that pertains to a bdqffdq:Amendment where an action to modify a value in some way through a change or addition is recommended. | Term-Action | Example see test [MEASURE_AMENDMENTS_PROPOSED](https://rs.tdwg.org/bdqcore/terms/03049fe5-a575-404f-b564-ae63f5a1cf8b). |
| Roman numerals | Roman numerals are interpreted as the equivalent integer for months (e.g. "X" as "10") in appropriate tests. Roman numerals may not be unambiguously interpreted for other Darwin Core terms such as dwc:day or in text fields as they may mean unknown or something else entirely. | Data |  |
| SRS | spatial reference system - see CRS (Chapman and Wieczorek 2020). | Test |  |
| STANDARD | A bdqffdq:Amendment where a value in a bdqffdq:InformationElement is proposed from a bdq:sourceAuthority. | Term-Action | Use in bdq:Response.qualifier or bdq:Response.comment. |
| STANDARDIZED | A bdqffdq:Amendment where a bdq:STANDARD value for a bdqffdq:InformationElement is proposed. | Term-Action | Use bdq:AMENDED as the bdq:Response.status, report bdq:STANDARDIZED in a bdq:Response.qualifier or in a bdq:Response.comment. |
| Term-Action | The last two components of the Title (the focus bdqffdq:InformationElement), and the evaluation focus), useful in filtering Tests in CSV files, for example: "COUNTRYCODE_STANDARD". | Test |  |
| Test | A composition of an instance of a subclass of bdqffdq:DataQualityNeed (which expresses a data quality need in the abstract) with an instance of a subclass of bdqffdq:DataQualityMethod which links it to an instance of a bdqffdq:Specification (which spells out how to concretely evaluate the need), these class instances being composed with bdqffdq:InformationElements, bdqffdq;Arguments, and bdqffdq:Parameters. | BDQ Core | For example, [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134). | 
| TestField | Column heading in the markdown of the tests in the [tdwg/bdq GitHub](https://github.com/tdwg/bdq/issues) that list all the normative and informative metadata elements that describe a Data Quality Test. | Test |  |
| Test Type | There are four types of tests, viz. bdqffdq:Validation, bdqffdq:Amendment, bdqffdq:Issue, and bdqffdq:Measure. | Test |  |
| TRANSPOSED | The sign and/or value of one or more bdqffdq:InformationElements were swapped. | Term-Action | Use bdq:AMENDED as the bdq:Response.status, report bdq:TRANSPOSED in a bdq:Response.qualifier or in a bdq:Response.comment. See Test [AMENDMENT_COORDINATES_TRANSPOSED](https://rs.tdwg.org/bdqcore/terms/f2b4a50a-6b2f-4930-b9df-da87b6a21082). |
| UNAMBIGUOUS | A combination of bdqffdq:InformationElements is unambiguous in that they align to a unique result given a reference or Source Authority (bdq:sourceAuthority). | Term-Action | For example, the Test [VALIDATION_TAXON_UNAMBIGUOUS](https://rs.tdwg.org/bdqcore/terms/4c09f127-737b-4686-82a0-7c8e30841590)	tests if the combination of taxon terms unambiguously resolves to a unque taxon by the Source Authority. |
| VERBATIM | A general category of specific bdq:InformationElements that represents a term containing an original value. | bdqffdq:InformationElement |  |
| whitespace | 1) A field that only includes whitespace (blanks) is treated as bdq:Empty. 2) In bdqffdq:Validation tests that require the looking up of a bdq:sourceAuthority, leading and/or trailing whitespace will cause the test to fail as no preprocessing is carried out on the data. These leading and trailing whitespaces may be stripped out in a subsequent bdqffdq:Amendment and thus pass when the bdqffdq:Validation test is run again. | Data |  |
| YEARMONTHDAY | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:month, dwc:day. | bdqffdq:InformationElement |  |
| YEARSTARTDAYOFYEARENDDAYOFYEAR | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:startDayOfYear, dwc:endDayofYear. | bdqffdq:InformationElement |  |

## 7 References

{references}

## 8 Audience for Each Document in BDQ Core

- [Introduction](../intro/index.md) This document is a general introduction to BDQ Core standard designed for anyone interested in specifications for the assessment or assurance of fitness for use of biodiversity data, or to improve it. 
- Guides
  - [Quick Reference Guide](../guide/users/index.md) This document is for all users.
  - [Users Guide](../guide/users/index.md) This document is for consumers of data quality reports.
  - [Implementers Guide](../guide/implementers/index.md) This document is for software developers needing a technical understanding of the BDQ Core Tests.
  - [bdqffdq Framework Guide](../guide/bdqffdq/index.md) This document is for those needing a technical understanding of the bdqffdq: Framework vocabulary.
- Vocabularies
  - [Vocabulary Landing page](../vocabularies/index.md) This document is for those needing a technical understanding of BDQ Core and readers seeking to navigate the BDQ Core standard.
    - [bdqcore: Landing page](../bdqcore/index.md) This document is for those needing a technical understanding of the BDQ Core Tests, both Users and Implementors. 
    - [bdqffdq; Landing page](../bdqffdq/index.md) Technical users who need to understand how to describe data quality with the framework.
    - [Term List for bdqffdq:](../list/bdqffdq/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the bdqffdq: Framework vocabulary.
    - [bdqffdq: Vocabulary Extension](../extension/bdqffdq/index.md) This document is for those needing a technical understanding of the bdqffdq Framework. 
    - [Term List for bdqenh:](../list/bdqenh/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and application of the bdqffdq: Framework. 
    - [Term List for bdqdim:](../list/bdqdim/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the bdqffdq: Framework vocabulary.
    - [Term List for bdqcrit:](../list/bdqcrit/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the bdqffdq: Framework vocabulary.
    - [Term List for bdq:](../list/bdq/index.md) This document is for those needing a technical understanding of the BDQ Core Tests. 
- Additional Documents
  - [Marking Synthetic Data](../synthetic/index.md) This document is designed for creators of data sets for the validation of implementations of BDQ Core tests, to see how to mark their data, and for aggregators and users of biodiversity data, to identify criteria for excluding synthetic or modified data from their pipelines . 
  - [Supplement](../supplement/index.md) This supplementary information may be relevant for curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners that wish to understand, evaluate and/or improve the quality of the biodiversity data within their domain. This document provides some key developmental issues in the building of BDQ Core that are not covered in other documents within this this standard. This document may also be useful to those seeking to evaluate their current tests or generate additional to the existing tests for their domain.
