<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
# BDQ Core Tests and Assertions Landing Page

Title
: BDQ Core Tests and Assertions Landing Page

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Preferred namespace abbreviation
: {pref_namespace_prefix}

This version
: <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

Latest version
: <http://rs.tdwg.org/bdqcore/terms/>

Abstract
: This document is a reference for the (Draft) BDQ Core Standard, documenting the tests in the bdqcore: vocabulary, using terms from the bdqffdq ontology.

Authors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core Tests and Assertions Landing Page. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

Draft Standard for Submission

# Table of Contents 

- [1 Introduction](#1-introduction)
- [1.1 Documents about the bdqcore: test descriptions.](#11-documents-about-the-bdqcore-test-descriptions)
- [1.1.1 Term List Distributions for bdqcore:](#111-term-list-distributions-for-bdqcore)
- [1.2 Characteristics of the tests (non-normative)](#12-characteristics-of-the-tests-(non-normative))
- [1.3 Types of tests (non-normative)](#13-types-of-tests-(non-normative))
- [1.3.1 Validation](#131-validation-)
- [1.3.2 Issue](#132-issue)
- [1.3.3 Amendment](#133-amendment)
- [1.3.4 Measure](#134-measure-)
- [1.4 RFC 2119 key words (normative)](#14-rfc-2119-key-words-(normative))
- [1.5 Status of the content of this document](#15-status-of-the-content-of-this-document)
- [1.6 Namespace abbreviations](#16-namespace-abbreviations)
- [2 Use of Terms (normative)](#2-use-of-terms-(normative))
- [2.1 Structure of Response (normative)](#21-structure-of-response-(normative))
- [2.2 Resource Types (normative)](#22-resource-types-(normative))
- [2.3 Parameterising the tests (normative)](#23-parameterising-the-tests-(normative))
- [3 Term indices](#3-term-indices)



## 1 Introduction

This document provides introductory explanatory information and normative guidance for the BDQ Core tests. The document includes terms in several namespaces that contain the recommended terms: `bdq:`, `bdqffdq:`, `bdqdim:`, bdqenh:, and bdqcrit as well as the focus of this document the `bdqcore` terms. For details and rationale, see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889.

### 1.1 Documents about the bdqcore: test descriptions.

The bdqcore: vocabulary includes: 

- A [Quick Reference Guide](../terms/bdqcore/index.md) to the tests.
- A [term list](../list/bdqffdq/index.md) for the vocabulary, containing the vocabulary terms and their metadata.
- Normative guidance on the use of the bdqcore vocabulary is provided in this landing page document.
- The bdqcore tests have several distribution files:
  - A csv file listing the tests  [CSV list of tests](../vocabulary/bdqcore_terms.csv) 
  - An rdf representation of the tests in a [Turtle Serialization of bdqcore](../dist/bdqcore.ttl) 
  - An rdf representation of the tests in an [RDF/XML Serialization of bdqcore](../dist/bdqcore.xml) 

An users guide to the use of the bdqcore tests is provided in the [Users Guide](../guide/users/index.md) 

An guide to implemetation of the bdqcore tests is provided in the [Implementers Guide](../guide/implementers/index.md) 

### 1.1.1 Term List Distributions for bdqcore:

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcore/index.md | Complete term list  | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.xml | RDF/XML  | 
| Turtle file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.ttl | Turtle  | 
| CSV file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqcore_terms.csv | CSV list of tests | 

### Text to move or rewrite

<!--- Material here probably goes into the implementers or users guide --->

Tests may require reference to external data such as standard vocabularies of terms or names. While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

(Make sure to establish that the standard does not specify the "format" of the responses (JSON within an Annotation, etc.), but it does specify the required content regardless of serialization format.)

Tests are paired in that all AMENDMENTs require a corresponding VALIDATION that assesses some aspect of data quality. An AMENDMENT may be able to improve the quality of data with respect to that VALIDATION. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values. 

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, repeated in 5.2.3 --->
The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

For a simplied list of current terms, see the BDQ Core Quick Reference Guide {http://..........}.

(Make sure this is addressed in this document) We acknowledge the centrality of the work of the TDWG Annotations Interest Group (https://github.com/tdwg/annotations) as to how the test results are reported against records. Test results structured with these three components can be readily wrapped in the body annotation document that follows the W3C Web Annotation Data Model (Sanderson et al. 2017), along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.

<!--- end of information that probably goes in the users or implementers guides --->

### 1.2 Characteristics of the tests (non-normative)

Each test is defined as a SingleRecord test. No CORE tests have been defined to use data in other records within a data set to evaluate the quality of data in a SingleRecord. The framework allows for MultiRecord tests able to identify outliers within a data set, or other tests that look across a MultiRecord to evaluate data quality, but we have not specified any such tests here.

The scope of each test is also largely provided by the bdqffdq:Specification. The Darwin Core terms used in the Specification are included in the "Information Elements". The "Specification" also includes references to external (to the Darwin Core standard) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource required for the implementation of the test.

The tests are agnostic about the form in which the data are stored or transported. The test specifications all assume that data are presented to the tests in structured form such as csv or tab delimited text files, with data elements identifiable as Darwin Core terms (Wieczorek et al. 2012). Here, cells contain non-typed data values possibly aggregated from and serialized from multiple sources such as relational databases where Boolean nulls and non-string data types may exist, but the data have been exported into a string serialization that supports neither null nor typed data. 

The tests are also agnostic about uses for quality assurance, where output data are limited to those for which all Validations are Compliant, or for quality control where the results of Validations, Issues, Measures, and Amendments can be used to improve the quality of the data.

The test specifications are agnostic about where in the biodiversity data lifecycle they are used. Implementers can incorporate the tests at any stage to help identify and correct issues. The tests can be applied during data capture in the field, transcription from paper records, data ingestion into databases, integration with collections management systems, data aggregation, and research on aggregated biodiversity data. They are designed to run at any point in the data lifecycle, from initial collection or observation to data transcription, database loading, and preparation for or during data aggregation. [However, the framing of the InformationElements as Darwin Core terms with the CORE Use Case focused on the research needs of downstream users means that competing requirements have led to some different decisions than would have been made if the aim was to solely evaluate data in a database of records and preparing it for aggregation.]   

### 1.3 Types of tests (non-normative)

[!---check out the wording Paul put in the BDQ_Core_Users_Guide.md - that is nice and simple wording---AC]

The concept of 'tests' in the context of this standard include four distinct types: VALIDATION; ISSUE; AMENDMENT and MEASURE.


#### 1.3.1 Validation 

Each bdqcore:Validation evaluates the values in one or more Darwin Core terms for fitness for some particular narrow data quality need within CORE. Validations evaluate values or in some cases, presence or lack of a value. Validation tests are phrased as positive statements, consistent with the "Fitness for Use Framework".  A Validation tests to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY, is phrased as "Not Empty", and will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem. The formal response of VALIDATIONs can take one of four forms:

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable, and running the same test on the same data at a different time may result in a different result.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation.
4. A Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 

#### 1.3.2 Issue

ISSUE is a form of warning flag where the test is drawing attention to a non-empty value of a Darwin Core term. We have used these for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of this case would take human review. For example, ISSUE_ANNOTATION_NOTEMPTY is informing the tester than there is at least one annotation associated with record and this should be evaluated before using the record. Similarly for the other two ISSUE-type tests: ISSUE_DATAGENERALIZATIONS_NOTEMPTY where some form of transformation has occurred, and ISSUE_ESTABLISHMENTMEANS_NOTEMPTY where the value needs to be assessed for utility. ISSUEs are currently outside the Data Quality Fitness for Use Framework. ISSUEs result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "IS_ISSUE", "POTENTIAL_ISSUE" or "NOT_ISSUE". ISSUE is symmetrical to NOT_COMPLIANT, NOT_ISSUE is approximately symmetrical to COMPLIANT, and POTENTIAL_ISSUE does not have an equivalent Validation Response.result. 

#### 1.3.3 Amendment

An AMENDMENT may propose a change or addition to at least one Darwin Core term that is intended to improve one or more components of the quality of the record.  The Response.result from an AMENDMENT MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for QualityControl of an existing database or record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  Amendments, under the framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in these tests.  

#### 1.3.4 Measure 

A MEASURE may return either a Response.result that is a numeric value, or the values COMPLETE or NOT_COMPLETE, or NOT_REPORTED (when the Response.status="INTERNAL_PREREQUISITES_NOTMET").  The principle Measure defined in the core tests is MEASURE_EVENTDATE_DURATIONINSECONDS, it returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the VALIDATIONs and AMENDMENTs and in one case provides an indication of the length of the period of the value of dwc:eventDate.

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

### 1.4 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


### 1.5 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4 the values of the rdfs:Label, skos:prefLabel, Versioned IRI, Resource Type, Specification, Information Elements ActedUpon, Information Elements Consulted, and Parameters are normative.  The values of Description, Examples, Use Cases, and Notes are non-normative. 

In Section 4, the values of the `Term IRI` and `Definition` are normative. The values of `Term Name` `skos:pref:Label` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Examples` and `Notes`) are non-normative.

### 1.6 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix |  IRI |
| ------ |  --- |
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms/               |
| bdqcrit      | https://rs.tdwh.org/bdqcrit/terms/               |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms/                |
| bdqenh       | https://rs.tdwg.org/bdqenh/terms/                |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema             |
| owl          | http://www.w3.org/2002/07/owl#                   |

## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of classes and object properties in the `bdqffdq:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqdim/terms), resources MUST be used as values of the `bdqdim:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqenh/terms), resources MUST be used as values of the `bdqenh:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqcrit/terms), resources MUST be used as values of the `bdqcrit:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdq/terms), resources MUST be used as values of the `bdq:` namespace.

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of the `bdqcore:` namespace.

### 2.1 Structure of Response (normative)

Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags,  The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary (consisting of exactly COMPLIANT or NOT_COMPLIANT) for validations or Issues (NOT_ISSUE, POTENTIAL_ISSUE, ISSUE), either a numeric value or a controlled vocabulary (consisting of exactly COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments. 
2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 
3. Remark supplies human-readable text describing reasons for the test result output.

### 2.2 Resource Types (normative)

Each test (each instance of a bdqffdq:DataQualityNeed) MUST have exactly one bdqffdq:hasResourceType object property that relates the test to a ResouceType of bdqffdq:SingleRecord or bdqffdq:MultiRecord.  

Tests operate on data, the data may be understood as representing a single record or multiple records.  In the bdqcore: tests the single record (bdqffdq:SingleRecord) tests MAY be applied to a single of Flat Darwin Core Record, or to a single instance of a Darwin Core Observation, Taxon, Event, or other class, and MAY extend across one to many relations from that class instance to instances of classes of other types in a structured representation of Darwin Core data (Wieczorek et al 2012).  For example,    A bdqcore: SingleRecord test SHOULD NOT take multiple rows of Flat Darwin core as input.  A bdqcore: SingleRecord test SHOULD NOT 

The bdqcore test ISSUE_ANNOTATION_NOTEMPTY similarly operates on a single Flat Darwin Core record, or a single core Darwin Core class instance, and asks whether annotations exist related to that class, here this standard encourages the implementation of a standard for annotating occurrence records beyond the Darwin Core terms.

Multi record (bdqffdq:MultiRecord) tests operate on a dataset as a whole, the MultiRecord tests in bdqcore: sum up results across all records for each single record test.

### 2.3 Parameterising the tests (normative)

Where a test is parameterized, a parameter (e.g. bdq:sourceAuthority) is specified in the text of the hasExpectedResponse data type property of the instance of the bdqffdq:Specification for the test.  Such a bdqffdq:Specification MUST also have a bdqffdq:hasArgument object property linking it to an instance of a bdqffdq:Argument, which MUST have a bdqffdq:hasArgumentValue data type property carrying the default value for the parameter, and this bdqffdq:Argument MUST have a bdqffdq:hasParameter object property linking it to a bdqffdq:Parameter.  The bdqffdq:Parameter SHOULD be a class instance in the bdq: namespace (e.g. bdq:sourceAuthority).  The instance of the bdqffdq:Specification SHOULD have a bdqffdq:hasAuthoritiesDefaults data type property containing

These elements MUST be understood in concert.

Values of bdqffdq:hasAuthoritiesDefaults SHOULD be a text string listing parameters in the form of a semicolon delimited list of one or more of the following: 
     
- parameter default = "default value" 
- parameter default = "default value" {[resource]}
- parameter default = "default value" {[resource]} {API endpoint [resource]}

Examples:

     bdq:earliestValidDate default ="1582-11-15"

     bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&amp;name=]}

##### Most of this text goes elsewhere 

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. This allows us to define general tests that provide support for non functional requirements that vary within the community. 

For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite. Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 


## 3 Term indices

### 3.1 Index By Test Label


[AMENDMENT_BASISOFRECORD_STANDARDIZED](#bdqcore_07c28ace-561a-476e-a9b9-3d5ad6e35933) |
[AMENDMENT_COORDINATES_FROM_VERBATIM](#bdqcore_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e) |
[AMENDMENT_COORDINATES_TRANSPOSED](#bdqcore_f2b4a50a-6b2f-4930-b9df-da87b6a21082) |
[AMENDMENT_COUNTRYCODE_FROM_COORDINATES](#bdqcore_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae) |
[AMENDMENT_COUNTRYCODE_STANDARDIZED](#bdqcore_fec5ffe6-3958-4312-82d9-ebcca0efb350) |
[AMENDMENT_DATEIDENTIFIED_STANDARDIZED](#bdqcore_39bb2280-1215-447b-9221-fd13bc990641) |
[AMENDMENT_DAY_STANDARDIZED](#bdqcore_b129fa4d-b25b-43f7-9645-5ed4d44b357b) |
[AMENDMENT_DCTYPE_STANDARDIZED](#bdqcore_bd385eeb-44a2-464b-a503-7abe407ef904) |
[AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED](#bdqcore_74ef1034-e289-4596-b5b0-cde73796697d) |
[AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED](#bdqcore_15d15927-7a22-43f8-88d6-298f5eb45c4c) |
[AMENDMENT_EVENTDATE_FROM_VERBATIM](#bdqcore_6d0a0c10-5e4a-4759-b448-88932f399812) |
[AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY](#bdqcore_3892f432-ddd0-4a0a-b713-f2e2ecbd879d) |
[AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR](#bdqcore_eb0a44fa-241c-4d64-98df-ad4aa837307b) |
[AMENDMENT_EVENTDATE_STANDARDIZED](#bdqcore_718dfc3c-cb52-4fca-b8e2-0e722f375da7) |
[AMENDMENT_EVENT_FROM_EVENTDATE](#bdqcore_710fe118-17e1-440f-b428-88ba3f547d6d) |
[AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](#bdqcore_7498ca76-c4d4-42e2-8103-acacccbdffa7) |
[AMENDMENT_GEODETICDATUM_STANDARDIZED](#bdqcore_0345b325-836d-4235-96d0-3b5caf150fc0) |
[AMENDMENT_LICENSE_STANDARDIZED](#bdqcore_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8) |
[AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM](#bdqcore_c5658b83-4471-4f57-9d94-bf7d0a96900c) |
[AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM](#bdqcore_2d638c8b-4c62-44a0-a14d-fa147bf9823d) |
[AMENDMENT_MONTH_STANDARDIZED](#bdqcore_2e371d57-1eb3-4fe3-8a61-dff43ced50cf) |
[AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT](#bdqcore_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5) |
[AMENDMENT_OCCURRENCESTATUS_STANDARDIZED](#bdqcore_f8f3a093-042c-47a3-971a-a482aaaf3b75) |
[AMENDMENT_PATHWAY_STANDARDIZED](#bdqcore_f9205977-f145-44f5-8cb9-e3e2e35ce908) |
[AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON](#bdqcore_431467d6-9b4b-48fa-a197-cd5379f5e889) |
[AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](#bdqcore_f01fb3f9-2f7e-418b-9f51-adf50f202aea) |
[AMENDMENT_SEX_STANDARDIZED](#bdqcore_33c45ae1-e2db-462a-a59e-7169bb01c5d6) |
[AMENDMENT_TAXONRANK_STANDARDIZED](#bdqcore_e39098df-ef46-464c-9aef-bcdeee2a88cb) |
[AMENDMENT_TYPESTATUS_STANDARDIZED](#bdqcore_b3471c65-b53e-453b-8282-abfa27bf1805) |
[ISSUE_ANNOTATION_NOTEMPTY](#bdqcore_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1) |
[ISSUE_COORDINATES_CENTEROFCOUNTRY](#bdqcore_256e51b3-1e08-4349-bb7e-5186631c3f8e) |
[ISSUE_DATAGENERALIZATIONS_NOTEMPTY](#bdqcore_13d5a10e-188e-40fd-a22c-dbaa87b91df2) |
[ISSUE_ESTABLISHMENTMEANS_NOTEMPTY](#bdqcore_acc8dff2-d8d1-483a-946d-65a02a452700) |
[MEASURE_AMENDMENTS_PROPOSED](#bdqcore_03049fe5-a575-404f-b564-ae63f5a1cf8b) |
[MEASURE_EVENTDATE_DURATIONINSECONDS](#bdqcore_56b6c695-adf1-418e-95d2-da04cad7be53) |
[MEASURE_VALIDATIONTESTS_COMPLIANT](#bdqcore_45fb49eb-4a1b-4b49-876f-15d5034dfc73) |
[MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](#bdqcore_453844ae-9df4-439f-8e24-c52498eca84a) |
[MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](#bdqcore_49a94636-a562-4e6b-803c-665c80628a3d) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY](#bdqcore_b60c8c58-0137-4b6a-97e9-57d8ca5cf248) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD](#bdqcore_f5dd74bd-6a22-4792-b675-c7ccf2a2c103) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT](#bdqcore_a56fb342-c8ee-4611-8aab-e6c6357e8875) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND](#bdqcore_7270a362-5f2e-41f0-955a-d7a8eaaf0f17) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqcore_c439952b-fb00-4902-90b3-a9d477c11a0b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqcore_b89b8424-91eb-4fd1-a6c3-1b0bc92120d0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqcore_25b5d4bf-c871-4485-a457-68021dce0367) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO](#bdqcore_0e239a55-0f19-4c68-bdbf-20580f27a647) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE](#bdqcore_2d90d94b-d384-4bac-aa68-c6800d765882) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY](#bdqcore_d71be8d4-1a04-4816-90c5-49808c823651) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD](#bdqcore_38966850-3737-4a67-953c-c231469e0489) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqcore_18b9d086-29ae-42a5-8f0a-4bc86f4e87ad) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqcore_8b73f37d-89ed-479a-8389-9e71ad2ac84d) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND](#bdqcore_f15c38c3-d96d-4e9c-982d-410fb71cf2bc) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY](#bdqcore_6887c881-dc52-409b-8979-9c2f05e55569) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE](#bdqcore_c72fda2d-16e1-4ded-91a5-a7094339d603) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD](#bdqcore_49b787eb-7dce-4ace-97f5-7cbb47cd8cb9) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE](#bdqcore_780480ff-8c4a-4276-aaca-cbd1248de9fa) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD](#bdqcore_c3e0100f-dfc3-4379-a855-df878eef295e) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY](#bdqcore_f041ab17-d834-4586-aa6b-090de2e571a8) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD](#bdqcore_fbe47441-500f-44c7-a1bd-1e872edc5266) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE](#bdqcore_f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY](#bdqcore_bceae35a-52ab-4968-846f-069ace766513) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE](#bdqcore_c70c4950-2246-4acc-a59d-81eaa47edf2b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY](#bdqcore_f948a30e-8084-48d5-b1ca-d77c476f181f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD](#bdqcore_1b8ae68e-63f1-41c0-9025-fbe64db38d64) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE](#bdqcore_7775309b-5331-4a65-b839-cbe959948d33) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD](#bdqcore_130bb875-6b7c-4965-b864-d53f9d05b2cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE](#bdqcore_c8250600-de61-4047-9d7c-6e06a38c7994) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY](#bdqcore_3f62eaa2-747f-456b-85e6-1a6e74086a18) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD](#bdqcore_bffd7499-aca3-423f-bb43-f7bdc9260f4f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY](#bdqcore_4a1fa336-dd47-4b60-a7b0-c958e2dc72cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT](#bdqcore_1919f212-b7db-4b6e-9697-41a715001bd6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND](#bdqcore_97928242-11a9-4ab0-9dd7-3f0465834824) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND](#bdqcore_977f7e75-a88e-4e29-a7b1-e8cdd35aa107) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY](#bdqcore_63fbaf3c-3d41-4ab6-bfc0-904f1b26835f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD](#bdqcore_8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND](#bdqcore_012eade5-fc64-458a-a13a-a614491bf4e0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY](#bdqcore_342bd81c-e2b7-41d8-b32b-013992d19f99) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY](#bdqcore_47ee20d9-5087-4f76-a494-6fea05e50b8b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD](#bdqcore_9d5be694-f5da-465d-8c7e-27e6dac69f9f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY](#bdqcore_bac852b5-1ba6-427b-aa8e-02018e99279c) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE](#bdqcore_3de8af03-05d4-4fd8-8e6d-ba886dc5446f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE](#bdqcore_6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE](#bdqcore_9c66c116-6644-45b4-b4c7-db7a4ee7c500) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqcore_b21256c2-4bb7-4deb-852d-a9eaa05345e7) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE](#bdqcore_071267a0-d993-4961-a3f7-d8210810d167) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqcore_be2eb717-b390-47d1-b7ba-965a1101e215) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD](#bdqcore_c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqcore_36ea0a78-a079-4014-aca3-2f2b3b11e822) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY](#bdqcore_0c9a139e-5d23-44de-a495-14ec08c61a1c) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY](#bdqcore_298db0c9-a85a-41ee-b111-d622fd969d71) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD](#bdqcore_faca6558-dbff-4d26-a5cb-e11cdf632fe7) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND](#bdqcore_f4fa449c-4b74-4dcf-b4cf-0b73e1496375) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD](#bdqcore_15e0da1d-1a43-4075-8454-b2e618cdd25b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND](#bdqcore_65e66ca0-e9d1-4411-ad26-bb9c43f32afc) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT](#bdqcore_7da5428e-87b2-4ec2-be82-05b9398b7577) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqcore_dbf3cece-1d83-426e-a5e0-8158fcf9c0cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE](#bdqcore_f174ad13-3c67-49f9-8d8b-aba4e933d6f6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY](#bdqcore_a9962d33-ad08-453a-8938-2972425034c2) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND](#bdqcore_4e70b0e4-3fd2-4899-802c-439671374eeb) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY](#bdqcore_0f8b30e2-59dc-46ba-8b91-62049cd1a4e2) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD](#bdqcore_e4d35063-2366-4dda-8eaa-326340361da3) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE](#bdqcore_76008c6b-c56a-4233-84e3-8584950037ec) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND](#bdqcore_58fdd5c1-6201-49a1-a7cd-f49c210dc0b6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY](#bdqcore_de661615-b338-4557-af5b-d44a89de40fa) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD](#bdqcore_602bc457-6b1d-4f24-adef-d0d31bcdf2f0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY](#bdqcore_54d290e8-ac48-4f31-8af3-676363573217) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS](#bdqcore_782773c9-7b37-483d-8ce2-c6683ba81882) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD](#bdqcore_b5a14d76-292e-499b-b80f-9546243311a0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE](#bdqcore_aee65eb8-8d1e-4b8f-bd37-5822e29f5734) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY](#bdqcore_687d3ad1-93a3-4a1f-b69f-da5a1eb761a5) |
[MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY](#bdqcore_c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8) |
[MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD](#bdqcore_241a279c-76d5-499b-ab49-a47ad7f8df50) |
[MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT](#bdqcore_a2be4734-0a93-46dc-af4a-e2125b47dbd4) |
[MULTIRECORD_MEASURE_QA_CLASS_FOUND](#bdqcore_21541436-641d-45a9-938c-537484d94eb7) |
[MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqcore_1ede76d0-c096-465c-8bbb-08c53bf7e367) |
[MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqcore_9ff65ace-9d16-4393-b90f-9150d9628371) |
[MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqcore_fb3732c6-4199-4767-a263-0363a1fe1766) |
[MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO](#bdqcore_151b2d29-3460-4ba5-a226-86971dc8ad03) |
[MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE](#bdqcore_d94b0130-7a13-4fa8-955c-eff5c47bd9de) |
[MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY](#bdqcore_942f63bd-d19d-4214-bf8e-cec0055b8909) |
[MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD](#bdqcore_fedf27b2-e01d-459f-98fc-7f0f39e3d4be) |
[MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqcore_c6a62914-f42e-442a-9e2b-38ccff594070) |
[MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqcore_23aced89-d613-479c-bc4c-837d74b73be0) |
[MULTIRECORD_MEASURE_QA_COUNTRY_FOUND](#bdqcore_388e74b3-2e18-4d78-8112-3142d1177e25) |
[MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY](#bdqcore_9c8df974-8fba-4537-8c67-31466787f732) |
[MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE](#bdqcore_6354376c-0cf2-435b-be40-850769c5a18a) |
[MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD](#bdqcore_563872eb-f544-45a0-8f91-8098d62768d4) |
[MULTIRECORD_MEASURE_QA_DAY_INRANGE](#bdqcore_85dc5d02-9847-420f-a026-6a0e70962d2a) |
[MULTIRECORD_MEASURE_QA_DAY_STANDARD](#bdqcore_371035f6-42b5-494f-86d9-de2f44a6cdc6) |
[MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY](#bdqcore_4d999a65-a431-4a76-b591-e0d86dcf244b) |
[MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD](#bdqcore_d9493fa0-d90e-41db-95f6-d1c1d243540e) |
[MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE](#bdqcore_3c8bc478-f6b2-4533-b7ce-45bae5d186c2) |
[MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY](#bdqcore_a2535b23-4407-40bd-b23b-30c8185d72a2) |
[MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE](#bdqcore_6f7a9b82-7d34-4111-a2a6-9efe5221fa44) |
[MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY](#bdqcore_a94e986e-dbc8-4147-872d-5f2727945654) |
[MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD](#bdqcore_ba953672-6526-4375-97e8-b4e9d1a7d3a0) |
[MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE](#bdqcore_c04d428a-13d0-4766-9df7-4dfb2ef5d5d8) |
[MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD](#bdqcore_8dfed701-01a9-415d-a9f8-539280b75975) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE](#bdqcore_d41a731b-2e2b-4442-9217-4c375ae92926) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY](#bdqcore_c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD](#bdqcore_14a1d51f-16ed-4148-9dc8-1e90157a9868) |
[MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY](#bdqcore_4cf4fe57-6736-443b-afda-f7ce8ce25471) |
[MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT](#bdqcore_f375a3fd-4cf5-4ef4-955e-d71762ede2d8) |
[MULTIRECORD_MEASURE_QA_FAMILY_FOUND](#bdqcore_a07d7147-2db8-48ce-81b8-e47595ad5f17) |
[MULTIRECORD_MEASURE_QA_GENUS_FOUND](#bdqcore_c5c8db83-3af0-4215-806f-e2f90574b138) |
[MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY](#bdqcore_488c1dff-21ec-4e68-a00a-7355505e180c) |
[MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD](#bdqcore_cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e) |
[MULTIRECORD_MEASURE_QA_KINGDOM_FOUND](#bdqcore_465d7ac1-d193-46c0-a302-56a9ef99215f) |
[MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY](#bdqcore_3bc9df8b-0f57-4157-9374-b56a99090b22) |
[MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY](#bdqcore_4fccf163-9336-4f48-996c-57f5f66e72db) |
[MULTIRECORD_MEASURE_QA_LICENSE_STANDARD](#bdqcore_acd8d43e-7a2a-4372-b887-fb53a9972dc9) |
[MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY](#bdqcore_3b2e4791-1a5a-4087-9e8d-09c67cf8c816) |
[MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE](#bdqcore_c73d49d1-06e4-4272-8249-6a26e7f8abca) |
[MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE](#bdqcore_7c5a6ba0-399d-4570-878a-4a064e2406fe) |
[MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE](#bdqcore_49d756a8-e654-4267-a290-d1def5d2c5f9) |
[MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqcore_fcabd2c9-392c-4841-a5d7-e2680c9587ab) |
[MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE](#bdqcore_1ba18c8b-66a6-47d9-a709-404439332dba) |
[MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqcore_44f00697-ca66-43cf-8f16-646b40c0f514) |
[MULTIRECORD_MEASURE_QA_MONTH_STANDARD](#bdqcore_b3c2bb86-e239-4532-ae0c-b121ec1ee025) |
[MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqcore_16059801-6adb-4e65-82f4-61eaa70d8df0) |
[MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY](#bdqcore_0028ef9a-6553-467b-a344-90327ed2babf) |
[MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY](#bdqcore_d2922585-2070-4851-a033-15e51977f9dc) |
[MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD](#bdqcore_2fea4571-92d0-48a5-a5ba-6caecd647862) |
[MULTIRECORD_MEASURE_QA_ORDER_FOUND](#bdqcore_773bb288-fef3-4968-a65a-a69c74d6ecb5) |
[MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD](#bdqcore_ef31ba02-cea7-4d76-990f-99ebbd201fb4) |
[MULTIRECORD_MEASURE_QA_PHYLUM_FOUND](#bdqcore_17364d16-37b7-4ccb-9614-bfb95ff1bca9) |
[MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT](#bdqcore_ef05b45b-13b8-4877-9e9d-fa44b332d83c) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqcore_6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE](#bdqcore_a9529e71-5470-4cb1-b04d-aa483926f532) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY](#bdqcore_4cf84216-c8a7-4865-a8e1-3ffd829d5a10) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND](#bdqcore_a8aee02c-cf7c-4104-a601-d8afc4f9cbe2) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY](#bdqcore_b4d6a61c-64ff-4da0-974c-63a73fd20836) |
[MULTIRECORD_MEASURE_QA_SEX_STANDARD](#bdqcore_1b3bbac4-7c00-46d6-8179-1d57c92374ad) |
[MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE](#bdqcore_8c217eee-9cd0-48c3-aea0-90151c6c5bfd) |
[MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND](#bdqcore_9c1cdf6a-0dbf-4828-a2e3-fb368f74d194) |
[MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY](#bdqcore_e0b8cff1-3322-40d2-b8b2-b99fc9ae130a) |
[MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD](#bdqcore_f320ca83-8487-4011-b1ff-f4b1b4dd86ec) |
[MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY](#bdqcore_2a9d4cfd-815a-46e0-bb51-60724582b762) |
[MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS](#bdqcore_0df03601-3768-4805-906a-bbd0a41b0fda) |
[MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD](#bdqcore_1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88) |
[MULTIRECORD_MEASURE_QA_YEAR_INRANGE](#bdqcore_a0502c5f-608b-4e59-99da-d9490bb4d93b) |
[MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY](#bdqcore_a8fef8a8-e7c7-4a2d-adaf-7da99c896c93) |
[VALIDATION_BASISOFRECORD_NOTEMPTY](#bdqcore_ac2b7648-d5f9-48ca-9b07-8ad5879a2536) |
[VALIDATION_BASISOFRECORD_STANDARD](#bdqcore_42408a00-bf71-4892-a399-4325e2bc1fb8) |
[VALIDATION_CLASSIFICATION_CONSISTENT](#bdqcore_2750c040-1d4a-4149-99fe-0512785f2d5f) |
[VALIDATION_CLASS_FOUND](#bdqcore_2cd6884e-3d14-4476-94f7-1191cfff309b) |
[VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqcore_adb27d29-9f0d-4d52-b760-a77ba57a69c9) |
[VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqcore_f18a470b-3fe1-4aae-9c65-a6d3db6b550c) |
[VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqcore_b9c184ce-a859-410c-9d12-71a338200380) |
[VALIDATION_COORDINATES_NOTZERO](#bdqcore_1bf0e210-6792-4128-b8cc-ab6828aa4871) |
[VALIDATION_COORDINATEUNCERTAINTY_INRANGE](#bdqcore_c6adf2ea-3051-4498-97f4-4b2f8a105f57) |
[VALIDATION_COUNTRYCODE_NOTEMPTY](#bdqcore_853b79a2-b314-44a2-ae46-34a1e7ed85e4) |
[VALIDATION_COUNTRYCODE_STANDARD](#bdqcore_0493bcfb-652e-4d17-815b-b0cce0742fbe) |
[VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqcore_b23110e7-1be7-444a-a677-cdee0cf4330c) |
[VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqcore_d257eb98-27cb-48e5-8d3c-ab9fca4edd11) |
[VALIDATION_COUNTRY_FOUND](#bdqcore_69b2efdc-6269-45a4-aecb-4cb99c2ae134) |
[VALIDATION_COUNTRY_NOTEMPTY](#bdqcore_6ce2b2b4-6afe-4d13-82a0-390d31ade01c) |
[VALIDATION_DATEIDENTIFIED_INRANGE](#bdqcore_dc8aae4b-134f-4d75-8a71-c4186239178e) |
[VALIDATION_DATEIDENTIFIED_STANDARD](#bdqcore_66269bdd-9271-4e76-b25c-7ab81eebe1d8) |
[VALIDATION_DAY_INRANGE](#bdqcore_8d787cb5-73e2-4c39-9cd1-67c7361dc02e) |
[VALIDATION_DAY_STANDARD](#bdqcore_47ff73ba-0028-4f79-9ce1-ee7008d66498) |
[VALIDATION_DCTYPE_NOTEMPTY](#bdqcore_374b091a-fc90-4791-91e5-c1557c649169) |
[VALIDATION_DCTYPE_STANDARD](#bdqcore_cdaabb0d-a863-49d0-bc0f-738d771acba5) |
[VALIDATION_DECIMALLATITUDE_INRANGE](#bdqcore_b6ecda2a-ce36-437a-b515-3ae94948fe83) |
[VALIDATION_DECIMALLATITUDE_NOTEMPTY](#bdqcore_7d2485d5-1ba7-4f25-90cb-f4480ff1a275) |
[VALIDATION_DECIMALLONGITUDE_INRANGE](#bdqcore_0949110d-c06b-450e-9649-7c1374d940d1) |
[VALIDATION_DECIMALLONGITUDE_NOTEMPTY](#bdqcore_9beb9442-d942-4f42-8b6a-fcea01ee086a) |
[VALIDATION_DEGREEOFESTABLISHMENT_STANDARD](#bdqcore_060e7734-607d-4737-8b2c-bfa17788bf1a) |
[VALIDATION_ENDDAYOFYEAR_INRANGE](#bdqcore_9a39d88c-7eee-46df-b32a-c109f9f81fb8) |
[VALIDATION_ESTABLISHMENTMEANS_STANDARD](#bdqcore_4eb48fdf-7299-4d63-9d08-246902e2857f) |
[VALIDATION_EVENTDATE_INRANGE](#bdqcore_3cff4dc4-72e9-4abe-9bf3-8a30f1618432) |
[VALIDATION_EVENTDATE_NOTEMPTY](#bdqcore_f51e15a6-a67d-4729-9c28-3766299d2985) |
[VALIDATION_EVENTDATE_STANDARD](#bdqcore_4f2bf8fd-fc5c-493f-a44c-e7b16153c803) |
[VALIDATION_EVENTTEMPORAL_NOTEMPTY](#bdqcore_41267642-60ff-4116-90eb-499fee2cd83f) |
[VALIDATION_EVENT_CONSISTENT](#bdqcore_5618f083-d55a-4ac2-92b5-b9fb227b832f) |
[VALIDATION_FAMILY_FOUND](#bdqcore_3667556d-d8f5-454c-922b-af8af38f613c) |
[VALIDATION_GENUS_FOUND](#bdqcore_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec) |
[VALIDATION_GEODETICDATUM_NOTEMPTY](#bdqcore_239ec40e-a729-4a8e-ba69-e0bf03ac1c44) |
[VALIDATION_GEODETICDATUM_STANDARD](#bdqcore_7e0c0418-fe16-4a39-98bd-80e19d95b9d1) |
[VALIDATION_KINGDOM_FOUND](#bdqcore_125b5493-052d-4a0d-a3e1-ed5bf792689e) |
[VALIDATION_KINGDOM_NOTEMPTY](#bdqcore_36ed36c9-b1a7-40b2-b5e2-0d012e772098) |
[VALIDATION_LICENSE_NOTEMPTY](#bdqcore_15f78619-811a-4c6f-997a-a4c7888ad849) |
[VALIDATION_LICENSE_STANDARD](#bdqcore_3136236e-04b6-49ea-8b34-a65f25e3aba1) |
[VALIDATION_LOCATION_NOTEMPTY](#bdqcore_58486cb6-1114-4a8a-ba1e-bd89cfe887e9) |
[VALIDATION_MAXDEPTH_INRANGE](#bdqcore_3f1db29a-bfa5-40db-9fd1-fde020d81939) |
[VALIDATION_MAXELEVATION_INRANGE](#bdqcore_c971fe3f-84c1-4636-9f44-b1ec31fd63c7) |
[VALIDATION_MINDEPTH_INRANGE](#bdqcore_04b2c8f3-c71b-4e95-8e43-f70374c5fb92) |
[VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqcore_8f1e6e58-544b-4365-a569-fb781341644e) |
[VALIDATION_MINELEVATION_INRANGE](#bdqcore_0bb8297d-8f8a-42d2-80c1-558f29efe798) |
[VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqcore_d708526b-6561-438e-aa1a-82cd80b06396) |
[VALIDATION_MONTH_STANDARD](#bdqcore_01c6dafa-0886-4b7e-9881-2c3018c98bdc) |
[VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqcore_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70) |
[VALIDATION_OCCURRENCEID_NOTEMPTY](#bdqcore_c486546c-e6e5-48a7-b286-eba7f5ca56c4) |
[VALIDATION_OCCURRENCESTATUS_NOTEMPTY](#bdqcore_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf) |
[VALIDATION_OCCURRENCESTATUS_STANDARD](#bdqcore_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47) |
[VALIDATION_ORDER_FOUND](#bdqcore_81cc974d-43cc-4c0f-a5e0-afa23b455aa3) |
[VALIDATION_PATHWAY_STANDARD](#bdqcore_5424e933-bee7-4125-839e-d8743ea69f93) |
[VALIDATION_PHYLUM_FOUND](#bdqcore_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f) |
[VALIDATION_POLYNOMIAL_CONSISTENT](#bdqcore_17f03f1f-f74d-40c0-8071-2927cfc9487b) |
[VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqcore_49f1d386-5bed-43ae-bd43-deabf7df64fc) |
[VALIDATION_SCIENTIFICNAMEID_COMPLETE](#bdqcore_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8) |
[VALIDATION_SCIENTIFICNAMEID_NOTEMPTY](#bdqcore_401bf207-9a55-4dff-88a5-abcd58ad97fa) |
[VALIDATION_SCIENTIFICNAME_FOUND](#bdqcore_3f335517-f442-4b98-b149-1e87ff16de45) |
[VALIDATION_SCIENTIFICNAME_NOTEMPTY](#bdqcore_7c4b9498-a8d9-4ebb-85f1-9f200c788595) |
[VALIDATION_SEX_STANDARD](#bdqcore_88d8598b-3318-483d-9475-a5acf9887404) |
[VALIDATION_STARTDAYOFYEAR_INRANGE](#bdqcore_85803c7e-2a5a-42e1-b8d3-299a44cafc46) |
[VALIDATION_STATEPROVINCE_FOUND](#bdqcore_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a) |
[VALIDATION_TAXONRANK_NOTEMPTY](#bdqcore_14da5b87-8304-4b2b-911d-117e3c29e890) |
[VALIDATION_TAXONRANK_STANDARD](#bdqcore_7bdb13a4-8a51-4ee5-be7f-20693fdb183e) |
[VALIDATION_TAXON_NOTEMPTY](#bdqcore_06851339-843f-4a43-8422-4e61b9a00e75) |
[VALIDATION_TAXON_UNAMBIGUOUS](#bdqcore_4c09f127-737b-4686-82a0-7c8e30841590) |
[VALIDATION_TYPESTATUS_STANDARD](#bdqcore_4833a522-12eb-4fe0-b4cf-7f7a337a6048) |
[VALIDATION_YEAR_INRANGE](#bdqcore_ad0c8855-de69-4843-a80c-a5387d20fbc8) |
[VALIDATION_YEAR_NOTEMPTY](#bdqcore_c09ecbf9-34e3-4f3e-b74a-8796af15e59f) 
## 4 Vocabulary Summary
- <a id="bdqcore_07c28ace-561a-476e-a9b9-3d5ad6e35933"></a>AMENDMENT_BASISOFRECORD_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:07c28ace-561a-476e-a9b9-3d5ad6e35933)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:07c28ace-561a-476e-a9b9-3d5ad6e35933)

- <a id="bdqcore_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e"></a>AMENDMENT_COORDINATES_FROM_VERBATIM
  - Description: Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e)

- <a id="bdqcore_f2b4a50a-6b2f-4930-b9df-da87b6a21082"></a>AMENDMENT_COORDINATES_TRANSPOSED
  - Description: Proposes an amendment of the signs of dwc:decimalLatitude and/or dwc:decimalLongitude to align the location with the dwc:countryCode.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f2b4a50a-6b2f-4930-b9df-da87b6a21082)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f2b4a50a-6b2f-4930-b9df-da87b6a21082)

- <a id="bdqcore_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae"></a>AMENDMENT_COUNTRYCODE_FROM_COORDINATES
  - Description: Proposes an amendment to the value of dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary from the bdq:countryShapes that is attributable to a single valid country code.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae)

- <a id="bdqcore_fec5ffe6-3958-4312-82d9-ebcca0efb350"></a>AMENDMENT_COUNTRYCODE_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:countryCode if it can be interpreted as an ISO country code.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fec5ffe6-3958-4312-82d9-ebcca0efb350)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fec5ffe6-3958-4312-82d9-ebcca0efb350)

- <a id="bdqcore_39bb2280-1215-447b-9221-fd13bc990641"></a>AMENDMENT_DATEIDENTIFIED_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:dateIdentified to a valid ISO date.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:39bb2280-1215-447b-9221-fd13bc990641)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:39bb2280-1215-447b-9221-fd13bc990641)

- <a id="bdqcore_b129fa4d-b25b-43f7-9645-5ed4d44b357b"></a>AMENDMENT_DAY_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:day as an integer between 1 and 31 inclusive.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b129fa4d-b25b-43f7-9645-5ed4d44b357b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b129fa4d-b25b-43f7-9645-5ed4d44b357b)

- <a id="bdqcore_bd385eeb-44a2-464b-a503-7abe407ef904"></a>AMENDMENT_DCTYPE_STANDARDIZED
  - Description: Proposes an amendment to the value of dc:type using the DCMI type vocabulary.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bd385eeb-44a2-464b-a503-7abe407ef904)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bd385eeb-44a2-464b-a503-7abe407ef904)

- <a id="bdqcore_74ef1034-e289-4596-b5b0-cde73796697d"></a>AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:degreeOfEstablishment using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:74ef1034-e289-4596-b5b0-cde73796697d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:74ef1034-e289-4596-b5b0-cde73796697d)

- <a id="bdqcore_15d15927-7a22-43f8-88d6-298f5eb45c4c"></a>AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:establishmentMeans using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:15d15927-7a22-43f8-88d6-298f5eb45c4c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:15d15927-7a22-43f8-88d6-298f5eb45c4c)

- <a id="bdqcore_6d0a0c10-5e4a-4759-b448-88932f399812"></a>AMENDMENT_EVENTDATE_FROM_VERBATIM
  - Description: Proposes an amendment to the value of dwc:eventDate from the content of dwc:verbatimEventDate.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6d0a0c10-5e4a-4759-b448-88932f399812)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6d0a0c10-5e4a-4759-b448-88932f399812)

- <a id="bdqcore_3892f432-ddd0-4a0a-b713-f2e2ecbd879d"></a>AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY
  - Description: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:month and dwc:day.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3892f432-ddd0-4a0a-b713-f2e2ecbd879d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3892f432-ddd0-4a0a-b713-f2e2ecbd879d)

- <a id="bdqcore_eb0a44fa-241c-4d64-98df-ad4aa837307b"></a>AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR
  - Description: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:eb0a44fa-241c-4d64-98df-ad4aa837307b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:eb0a44fa-241c-4d64-98df-ad4aa837307b)

- <a id="bdqcore_718dfc3c-cb52-4fca-b8e2-0e722f375da7"></a>AMENDMENT_EVENTDATE_STANDARDIZED
  - Description: Proposes an amendment of the value of dwc:eventDate to a valid ISO date.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:718dfc3c-cb52-4fca-b8e2-0e722f375da7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:718dfc3c-cb52-4fca-b8e2-0e722f375da7)

- <a id="bdqcore_710fe118-17e1-440f-b428-88ba3f547d6d"></a>AMENDMENT_EVENT_FROM_EVENTDATE
  - Description: Proposes an amendment to values in any of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear or dwc:endDayOfYear from the content of dwc:eventDate.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:710fe118-17e1-440f-b428-88ba3f547d6d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:710fe118-17e1-440f-b428-88ba3f547d6d)

- <a id="bdqcore_7498ca76-c4d4-42e2-8103-acacccbdffa7"></a>AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT
  - Description: Proposes an amendment to fill in dwc:geodeticDatum using a prameterized value if the dwc:geodeticDatum is empty.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7498ca76-c4d4-42e2-8103-acacccbdffa7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7498ca76-c4d4-42e2-8103-acacccbdffa7)

- <a id="bdqcore_0345b325-836d-4235-96d0-3b5caf150fc0"></a>AMENDMENT_GEODETICDATUM_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:geodeticDatum using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0345b325-836d-4235-96d0-3b5caf150fc0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0345b325-836d-4235-96d0-3b5caf150fc0)

- <a id="bdqcore_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8"></a>AMENDMENT_LICENSE_STANDARDIZED
  - Description: Proposes an amendment to the value of dcterms:license using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8)

- <a id="bdqcore_c5658b83-4471-4f57-9d94-bf7d0a96900c"></a>AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM
  - Description: Proposes amendments of the values of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be interpreted from dwc:verbatimDepth.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c5658b83-4471-4f57-9d94-bf7d0a96900c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c5658b83-4471-4f57-9d94-bf7d0a96900c)

- <a id="bdqcore_2d638c8b-4c62-44a0-a14d-fa147bf9823d"></a>AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM
  - Description: Proposes an amendment or amendments to the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be interpreted from dwc:verbatimElevation.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2d638c8b-4c62-44a0-a14d-fa147bf9823d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2d638c8b-4c62-44a0-a14d-fa147bf9823d)

- <a id="bdqcore_2e371d57-1eb3-4fe3-8a61-dff43ced50cf"></a>AMENDMENT_MONTH_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:month as an integer between 1 and 12 inclusive.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2e371d57-1eb3-4fe3-8a61-dff43ced50cf)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2e371d57-1eb3-4fe3-8a61-dff43ced50cf)

- <a id="bdqcore_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5"></a>AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT
  - Description: Proposes an amendment of the value of dwc:occurrenceStatus to the default parameter value if dwc:occurrenceStatus, dwc:individualCount and dwc:organismQuantity are empty.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5)

- <a id="bdqcore_f8f3a093-042c-47a3-971a-a482aaaf3b75"></a>AMENDMENT_OCCURRENCESTATUS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:occurrenceStatus using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f8f3a093-042c-47a3-971a-a482aaaf3b75)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f8f3a093-042c-47a3-971a-a482aaaf3b75)

- <a id="bdqcore_f9205977-f145-44f5-8cb9-e3e2e35ce908"></a>AMENDMENT_PATHWAY_STANDARDIZED
  - Description: Propose an amendment to the value of dwc:pathway using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f9205977-f145-44f5-8cb9-e3e2e35ce908)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f9205977-f145-44f5-8cb9-e3e2e35ce908)

- <a id="bdqcore_431467d6-9b4b-48fa-a197-cd5379f5e889"></a>AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON
  - Description: Proposes an amendment to the value of dwc:scientificNameID if it can be unambiguously resolved from bdq:sourceAuthority using the available taxon terms.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:431467d6-9b4b-48fa-a197-cd5379f5e889)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:431467d6-9b4b-48fa-a197-cd5379f5e889)

- <a id="bdqcore_f01fb3f9-2f7e-418b-9f51-adf50f202aea"></a>AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID
  - Description: Proposes an amendment to the value of dwc:scientificName using the dwc:scientificNameID value from the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f01fb3f9-2f7e-418b-9f51-adf50f202aea)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f01fb3f9-2f7e-418b-9f51-adf50f202aea)

- <a id="bdqcore_33c45ae1-e2db-462a-a59e-7169bb01c5d6"></a>AMENDMENT_SEX_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:sex using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:33c45ae1-e2db-462a-a59e-7169bb01c5d6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:33c45ae1-e2db-462a-a59e-7169bb01c5d6)

- <a id="bdqcore_e39098df-ef46-464c-9aef-bcdeee2a88cb"></a>AMENDMENT_TAXONRANK_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:taxonRank using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:e39098df-ef46-464c-9aef-bcdeee2a88cb)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:e39098df-ef46-464c-9aef-bcdeee2a88cb)

- <a id="bdqcore_b3471c65-b53e-453b-8282-abfa27bf1805"></a>AMENDMENT_TYPESTATUS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:typeStatus using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b3471c65-b53e-453b-8282-abfa27bf1805)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b3471c65-b53e-453b-8282-abfa27bf1805)

- <a id="bdqcore_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1"></a>ISSUE_ANNOTATION_NOTEMPTY
  - Description: Are there any annotations associated with the record?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1)

- <a id="bdqcore_256e51b3-1e08-4349-bb7e-5186631c3f8e"></a>ISSUE_COORDINATES_CENTEROFCOUNTRY
  - Description: Are the supplied geographic coordinates within a defined buffer of the center of the country?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:256e51b3-1e08-4349-bb7e-5186631c3f8e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:256e51b3-1e08-4349-bb7e-5186631c3f8e)

- <a id="bdqcore_13d5a10e-188e-40fd-a22c-dbaa87b91df2"></a>ISSUE_DATAGENERALIZATIONS_NOTEMPTY
  - Description: Is there a value in dwc:dataGeneralizations?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:13d5a10e-188e-40fd-a22c-dbaa87b91df2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:13d5a10e-188e-40fd-a22c-dbaa87b91df2)

- <a id="bdqcore_acc8dff2-d8d1-483a-946d-65a02a452700"></a>ISSUE_ESTABLISHMENTMEANS_NOTEMPTY
  - Description: Is there a value in dwc:establishmentMeans?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:acc8dff2-d8d1-483a-946d-65a02a452700)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:acc8dff2-d8d1-483a-946d-65a02a452700)

- <a id="bdqcore_03049fe5-a575-404f-b564-ae63f5a1cf8b"></a>MEASURE_AMENDMENTS_PROPOSED
  - Description: A count of the number of distinct AMENDMENT tests that have a Response.status="AMENDED" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:03049fe5-a575-404f-b564-ae63f5a1cf8b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:03049fe5-a575-404f-b564-ae63f5a1cf8b)

- <a id="bdqcore_56b6c695-adf1-418e-95d2-da04cad7be53"></a>MEASURE_EVENTDATE_DURATIONINSECONDS
  - Description: What is the duration of dwc:eventDate in seconds?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:56b6c695-adf1-418e-95d2-da04cad7be53)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:56b6c695-adf1-418e-95d2-da04cad7be53)

- <a id="bdqcore_45fb49eb-4a1b-4b49-876f-15d5034dfc73"></a>MEASURE_VALIDATIONTESTS_COMPLIANT
  - Description: Measures the number of distinct VALIDATION tests that have a Response.status="COMPLIANT" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:45fb49eb-4a1b-4b49-876f-15d5034dfc73)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:45fb49eb-4a1b-4b49-876f-15d5034dfc73)

- <a id="bdqcore_453844ae-9df4-439f-8e24-c52498eca84a"></a>MEASURE_VALIDATIONTESTS_NOTCOMPLIANT
  - Description: A count of the number of distinct VALIDATION tests that have a Response.status="NOT_COMPLIANT" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:453844ae-9df4-439f-8e24-c52498eca84a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:453844ae-9df4-439f-8e24-c52498eca84a)

- <a id="bdqcore_49a94636-a562-4e6b-803c-665c80628a3d"></a>MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET
  - Description: The number of distinct VALIDATION tests that have a Response.status="EXTERNAL_PREREQUISITES_NOT_MET" or "INTERNAL_PREREQUISITES_NOT_MET" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49a94636-a562-4e6b-803c-665c80628a3d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49a94636-a562-4e6b-803c-665c80628a3d)

- <a id="bdqcore_b60c8c58-0137-4b6a-97e9-57d8ca5cf248"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY
  - Description: Count the number of VALIDATION_BASISOFRECORD_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b60c8c58-0137-4b6a-97e9-57d8ca5cf248)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b60c8c58-0137-4b6a-97e9-57d8ca5cf248)

- <a id="bdqcore_f5dd74bd-6a22-4792-b675-c7ccf2a2c103"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD
  - Description: Count the number of VALIDATION_BASISOFRECORD_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f5dd74bd-6a22-4792-b675-c7ccf2a2c103)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f5dd74bd-6a22-4792-b675-c7ccf2a2c103)

- <a id="bdqcore_a56fb342-c8ee-4611-8aab-e6c6357e8875"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT
  - Description: Count the number of VALIDATION_CLASSIFICATION_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a56fb342-c8ee-4611-8aab-e6c6357e8875)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a56fb342-c8ee-4611-8aab-e6c6357e8875)

- <a id="bdqcore_7270a362-5f2e-41f0-955a-d7a8eaaf0f17"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND
  - Description: Count the number of VALIDATION_CLASS_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7270a362-5f2e-41f0-955a-d7a8eaaf0f17)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7270a362-5f2e-41f0-955a-d7a8eaaf0f17)

- <a id="bdqcore_c439952b-fb00-4902-90b3-a9d477c11a0b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT
  - Description: Count the number of VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c439952b-fb00-4902-90b3-a9d477c11a0b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c439952b-fb00-4902-90b3-a9d477c11a0b)

- <a id="bdqcore_b89b8424-91eb-4fd1-a6c3-1b0bc92120d0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT
  - Description: Count the number of VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b89b8424-91eb-4fd1-a6c3-1b0bc92120d0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b89b8424-91eb-4fd1-a6c3-1b0bc92120d0)

- <a id="bdqcore_25b5d4bf-c871-4485-a457-68021dce0367"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT
  - Description: Count the number of VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:25b5d4bf-c871-4485-a457-68021dce0367)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:25b5d4bf-c871-4485-a457-68021dce0367)

- <a id="bdqcore_0e239a55-0f19-4c68-bdbf-20580f27a647"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO
  - Description: Count the number of VALIDATION_COORDINATES_NOTZERO in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0e239a55-0f19-4c68-bdbf-20580f27a647)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0e239a55-0f19-4c68-bdbf-20580f27a647)

- <a id="bdqcore_2d90d94b-d384-4bac-aa68-c6800d765882"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE
  - Description: Count the number of VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2d90d94b-d384-4bac-aa68-c6800d765882)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2d90d94b-d384-4bac-aa68-c6800d765882)

- <a id="bdqcore_d71be8d4-1a04-4816-90c5-49808c823651"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY
  - Description: Count the number of VALIDATION_COUNTRYCODE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d71be8d4-1a04-4816-90c5-49808c823651)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d71be8d4-1a04-4816-90c5-49808c823651)

- <a id="bdqcore_38966850-3737-4a67-953c-c231469e0489"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD
  - Description: Count the number of VALIDATION_COUNTRYCODE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:38966850-3737-4a67-953c-c231469e0489)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:38966850-3737-4a67-953c-c231469e0489)

- <a id="bdqcore_18b9d086-29ae-42a5-8f0a-4bc86f4e87ad"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT
  - Description: Count the number of VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:18b9d086-29ae-42a5-8f0a-4bc86f4e87ad)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:18b9d086-29ae-42a5-8f0a-4bc86f4e87ad)

- <a id="bdqcore_8b73f37d-89ed-479a-8389-9e71ad2ac84d"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS
  - Description: Count the number of VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8b73f37d-89ed-479a-8389-9e71ad2ac84d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8b73f37d-89ed-479a-8389-9e71ad2ac84d)

- <a id="bdqcore_f15c38c3-d96d-4e9c-982d-410fb71cf2bc"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND
  - Description: Count the number of VALIDATION_COUNTRY_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f15c38c3-d96d-4e9c-982d-410fb71cf2bc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f15c38c3-d96d-4e9c-982d-410fb71cf2bc)

- <a id="bdqcore_6887c881-dc52-409b-8979-9c2f05e55569"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY
  - Description: Count the number of VALIDATION_COUNTRY_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6887c881-dc52-409b-8979-9c2f05e55569)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6887c881-dc52-409b-8979-9c2f05e55569)

- <a id="bdqcore_c72fda2d-16e1-4ded-91a5-a7094339d603"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE
  - Description: Count the number of VALIDATION_DATEIDENTIFIED_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c72fda2d-16e1-4ded-91a5-a7094339d603)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c72fda2d-16e1-4ded-91a5-a7094339d603)

- <a id="bdqcore_49b787eb-7dce-4ace-97f5-7cbb47cd8cb9"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD
  - Description: Count the number of VALIDATION_DATEIDENTIFIED_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49b787eb-7dce-4ace-97f5-7cbb47cd8cb9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49b787eb-7dce-4ace-97f5-7cbb47cd8cb9)

- <a id="bdqcore_780480ff-8c4a-4276-aaca-cbd1248de9fa"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE
  - Description: Count the number of VALIDATION_DAY_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:780480ff-8c4a-4276-aaca-cbd1248de9fa)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:780480ff-8c4a-4276-aaca-cbd1248de9fa)

- <a id="bdqcore_c3e0100f-dfc3-4379-a855-df878eef295e"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD
  - Description: Count the number of VALIDATION_DAY_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c3e0100f-dfc3-4379-a855-df878eef295e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c3e0100f-dfc3-4379-a855-df878eef295e)

- <a id="bdqcore_f041ab17-d834-4586-aa6b-090de2e571a8"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY
  - Description: Count the number of VALIDATION_DCTYPE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f041ab17-d834-4586-aa6b-090de2e571a8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f041ab17-d834-4586-aa6b-090de2e571a8)

- <a id="bdqcore_fbe47441-500f-44c7-a1bd-1e872edc5266"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD
  - Description: Count the number of VALIDATION_DCTYPE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fbe47441-500f-44c7-a1bd-1e872edc5266)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fbe47441-500f-44c7-a1bd-1e872edc5266)

- <a id="bdqcore_f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE
  - Description: Count the number of VALIDATION_DECIMALLATITUDE_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26)

- <a id="bdqcore_bceae35a-52ab-4968-846f-069ace766513"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY
  - Description: Count the number of VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bceae35a-52ab-4968-846f-069ace766513)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bceae35a-52ab-4968-846f-069ace766513)

- <a id="bdqcore_c70c4950-2246-4acc-a59d-81eaa47edf2b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE
  - Description: Count the number of VALIDATION_DECIMALLONGITUDE_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c70c4950-2246-4acc-a59d-81eaa47edf2b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c70c4950-2246-4acc-a59d-81eaa47edf2b)

- <a id="bdqcore_f948a30e-8084-48d5-b1ca-d77c476f181f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY
  - Description: Count the number of VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f948a30e-8084-48d5-b1ca-d77c476f181f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f948a30e-8084-48d5-b1ca-d77c476f181f)

- <a id="bdqcore_1b8ae68e-63f1-41c0-9025-fbe64db38d64"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD
  - Description: Count the number of VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1b8ae68e-63f1-41c0-9025-fbe64db38d64)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1b8ae68e-63f1-41c0-9025-fbe64db38d64)

- <a id="bdqcore_7775309b-5331-4a65-b839-cbe959948d33"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE
  - Description: Count the number of VALIDATION_ENDDAYOFYEAR_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7775309b-5331-4a65-b839-cbe959948d33)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7775309b-5331-4a65-b839-cbe959948d33)

- <a id="bdqcore_130bb875-6b7c-4965-b864-d53f9d05b2cd"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD
  - Description: Count the number of VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:130bb875-6b7c-4965-b864-d53f9d05b2cd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:130bb875-6b7c-4965-b864-d53f9d05b2cd)

- <a id="bdqcore_c8250600-de61-4047-9d7c-6e06a38c7994"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE
  - Description: Count the number of VALIDATION_EVENTDATE_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c8250600-de61-4047-9d7c-6e06a38c7994)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c8250600-de61-4047-9d7c-6e06a38c7994)

- <a id="bdqcore_3f62eaa2-747f-456b-85e6-1a6e74086a18"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY
  - Description: Count the number of VALIDATION_EVENTDATE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3f62eaa2-747f-456b-85e6-1a6e74086a18)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3f62eaa2-747f-456b-85e6-1a6e74086a18)

- <a id="bdqcore_bffd7499-aca3-423f-bb43-f7bdc9260f4f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD
  - Description: Count the number of VALIDATION_EVENTDATE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bffd7499-aca3-423f-bb43-f7bdc9260f4f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bffd7499-aca3-423f-bb43-f7bdc9260f4f)

- <a id="bdqcore_4a1fa336-dd47-4b60-a7b0-c958e2dc72cd"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY
  - Description: Count the number of VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4a1fa336-dd47-4b60-a7b0-c958e2dc72cd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4a1fa336-dd47-4b60-a7b0-c958e2dc72cd)

- <a id="bdqcore_1919f212-b7db-4b6e-9697-41a715001bd6"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT
  - Description: Count the number of VALIDATION_EVENT_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1919f212-b7db-4b6e-9697-41a715001bd6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1919f212-b7db-4b6e-9697-41a715001bd6)

- <a id="bdqcore_97928242-11a9-4ab0-9dd7-3f0465834824"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND
  - Description: Count the number of VALIDATION_FAMILY_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:97928242-11a9-4ab0-9dd7-3f0465834824)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:97928242-11a9-4ab0-9dd7-3f0465834824)

- <a id="bdqcore_977f7e75-a88e-4e29-a7b1-e8cdd35aa107"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND
  - Description: Count the number of VALIDATION_GENUS_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:977f7e75-a88e-4e29-a7b1-e8cdd35aa107)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:977f7e75-a88e-4e29-a7b1-e8cdd35aa107)

- <a id="bdqcore_63fbaf3c-3d41-4ab6-bfc0-904f1b26835f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY
  - Description: Count the number of VALIDATION_GEODETICDATUM_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:63fbaf3c-3d41-4ab6-bfc0-904f1b26835f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:63fbaf3c-3d41-4ab6-bfc0-904f1b26835f)

- <a id="bdqcore_8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD
  - Description: Count the number of VALIDATION_GEODETICDATUM_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63)

- <a id="bdqcore_012eade5-fc64-458a-a13a-a614491bf4e0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND
  - Description: Count the number of VALIDATION_KINGDOM_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:012eade5-fc64-458a-a13a-a614491bf4e0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:012eade5-fc64-458a-a13a-a614491bf4e0)

- <a id="bdqcore_342bd81c-e2b7-41d8-b32b-013992d19f99"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY
  - Description: Count the number of VALIDATION_KINGDOM_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:342bd81c-e2b7-41d8-b32b-013992d19f99)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:342bd81c-e2b7-41d8-b32b-013992d19f99)

- <a id="bdqcore_47ee20d9-5087-4f76-a494-6fea05e50b8b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY
  - Description: Count the number of VALIDATION_LICENSE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:47ee20d9-5087-4f76-a494-6fea05e50b8b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:47ee20d9-5087-4f76-a494-6fea05e50b8b)

- <a id="bdqcore_9d5be694-f5da-465d-8c7e-27e6dac69f9f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD
  - Description: Count the number of VALIDATION_LICENSE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9d5be694-f5da-465d-8c7e-27e6dac69f9f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9d5be694-f5da-465d-8c7e-27e6dac69f9f)

- <a id="bdqcore_bac852b5-1ba6-427b-aa8e-02018e99279c"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY
  - Description: Count the number of VALIDATION_LOCATION_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bac852b5-1ba6-427b-aa8e-02018e99279c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bac852b5-1ba6-427b-aa8e-02018e99279c)

- <a id="bdqcore_3de8af03-05d4-4fd8-8e6d-ba886dc5446f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE
  - Description: Count the number of VALIDATION_MAXDEPTH_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3de8af03-05d4-4fd8-8e6d-ba886dc5446f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3de8af03-05d4-4fd8-8e6d-ba886dc5446f)

- <a id="bdqcore_6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE
  - Description: Count the number of VALIDATION_MAXELEVATION_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5)

- <a id="bdqcore_9c66c116-6644-45b4-b4c7-db7a4ee7c500"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE
  - Description: Count the number of VALIDATION_MINDEPTH_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9c66c116-6644-45b4-b4c7-db7a4ee7c500)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9c66c116-6644-45b4-b4c7-db7a4ee7c500)

- <a id="bdqcore_b21256c2-4bb7-4deb-852d-a9eaa05345e7"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH
  - Description: Count the number of VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b21256c2-4bb7-4deb-852d-a9eaa05345e7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b21256c2-4bb7-4deb-852d-a9eaa05345e7)

- <a id="bdqcore_071267a0-d993-4961-a3f7-d8210810d167"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE
  - Description: Count the number of VALIDATION_MINELEVATION_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:071267a0-d993-4961-a3f7-d8210810d167)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:071267a0-d993-4961-a3f7-d8210810d167)

- <a id="bdqcore_be2eb717-b390-47d1-b7ba-965a1101e215"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION
  - Description: Count the number of VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:be2eb717-b390-47d1-b7ba-965a1101e215)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:be2eb717-b390-47d1-b7ba-965a1101e215)

- <a id="bdqcore_c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD
  - Description: Count the number of VALIDATION_MONTH_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3)

- <a id="bdqcore_36ea0a78-a079-4014-aca3-2f2b3b11e822"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY
  - Description: Count the number of VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:36ea0a78-a079-4014-aca3-2f2b3b11e822)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:36ea0a78-a079-4014-aca3-2f2b3b11e822)

- <a id="bdqcore_0c9a139e-5d23-44de-a495-14ec08c61a1c"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY
  - Description: Count the number of VALIDATION_OCCURRENCEID_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0c9a139e-5d23-44de-a495-14ec08c61a1c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0c9a139e-5d23-44de-a495-14ec08c61a1c)

- <a id="bdqcore_298db0c9-a85a-41ee-b111-d622fd969d71"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY
  - Description: Count the number of VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:298db0c9-a85a-41ee-b111-d622fd969d71)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:298db0c9-a85a-41ee-b111-d622fd969d71)

- <a id="bdqcore_faca6558-dbff-4d26-a5cb-e11cdf632fe7"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD
  - Description: Count the number of VALIDATION_OCCURRENCESTATUS_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:faca6558-dbff-4d26-a5cb-e11cdf632fe7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:faca6558-dbff-4d26-a5cb-e11cdf632fe7)

- <a id="bdqcore_f4fa449c-4b74-4dcf-b4cf-0b73e1496375"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND
  - Description: Count the number of VALIDATION_ORDER_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f4fa449c-4b74-4dcf-b4cf-0b73e1496375)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f4fa449c-4b74-4dcf-b4cf-0b73e1496375)

- <a id="bdqcore_15e0da1d-1a43-4075-8454-b2e618cdd25b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD
  - Description: Count the number of VALIDATION_PATHWAY_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:15e0da1d-1a43-4075-8454-b2e618cdd25b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:15e0da1d-1a43-4075-8454-b2e618cdd25b)

- <a id="bdqcore_65e66ca0-e9d1-4411-ad26-bb9c43f32afc"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND
  - Description: Count the number of VALIDATION_PHYLUM_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:65e66ca0-e9d1-4411-ad26-bb9c43f32afc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:65e66ca0-e9d1-4411-ad26-bb9c43f32afc)

- <a id="bdqcore_7da5428e-87b2-4ec2-be82-05b9398b7577"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT
  - Description: Count the number of VALIDATION_POLYNOMIAL_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7da5428e-87b2-4ec2-be82-05b9398b7577)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7da5428e-87b2-4ec2-be82-05b9398b7577)

- <a id="bdqcore_dbf3cece-1d83-426e-a5e0-8158fcf9c0cd"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
  - Description: Count the number of VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:dbf3cece-1d83-426e-a5e0-8158fcf9c0cd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:dbf3cece-1d83-426e-a5e0-8158fcf9c0cd)

- <a id="bdqcore_f174ad13-3c67-49f9-8d8b-aba4e933d6f6"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE
  - Description: Count the number of VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f174ad13-3c67-49f9-8d8b-aba4e933d6f6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f174ad13-3c67-49f9-8d8b-aba4e933d6f6)

- <a id="bdqcore_a9962d33-ad08-453a-8938-2972425034c2"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY
  - Description: Count the number of VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a9962d33-ad08-453a-8938-2972425034c2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a9962d33-ad08-453a-8938-2972425034c2)

- <a id="bdqcore_4e70b0e4-3fd2-4899-802c-439671374eeb"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND
  - Description: Count the number of VALIDATION_SCIENTIFICNAME_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4e70b0e4-3fd2-4899-802c-439671374eeb)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4e70b0e4-3fd2-4899-802c-439671374eeb)

- <a id="bdqcore_0f8b30e2-59dc-46ba-8b91-62049cd1a4e2"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY
  - Description: Count the number of VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0f8b30e2-59dc-46ba-8b91-62049cd1a4e2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0f8b30e2-59dc-46ba-8b91-62049cd1a4e2)

- <a id="bdqcore_e4d35063-2366-4dda-8eaa-326340361da3"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD
  - Description: Count the number of VALIDATION_SEX_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:e4d35063-2366-4dda-8eaa-326340361da3)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:e4d35063-2366-4dda-8eaa-326340361da3)

- <a id="bdqcore_76008c6b-c56a-4233-84e3-8584950037ec"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE
  - Description: Count the number of VALIDATION_STARTDAYOFYEAR_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:76008c6b-c56a-4233-84e3-8584950037ec)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:76008c6b-c56a-4233-84e3-8584950037ec)

- <a id="bdqcore_58fdd5c1-6201-49a1-a7cd-f49c210dc0b6"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND
  - Description: Count the number of VALIDATION_STATEPROVINCE_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:58fdd5c1-6201-49a1-a7cd-f49c210dc0b6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:58fdd5c1-6201-49a1-a7cd-f49c210dc0b6)

- <a id="bdqcore_de661615-b338-4557-af5b-d44a89de40fa"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY
  - Description: Count the number of VALIDATION_TAXONRANK_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:de661615-b338-4557-af5b-d44a89de40fa)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:de661615-b338-4557-af5b-d44a89de40fa)

- <a id="bdqcore_602bc457-6b1d-4f24-adef-d0d31bcdf2f0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD
  - Description: Count the number of VALIDATION_TAXONRANK_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:602bc457-6b1d-4f24-adef-d0d31bcdf2f0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:602bc457-6b1d-4f24-adef-d0d31bcdf2f0)

- <a id="bdqcore_54d290e8-ac48-4f31-8af3-676363573217"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY
  - Description: Count the number of VALIDATION_TAXON_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:54d290e8-ac48-4f31-8af3-676363573217)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:54d290e8-ac48-4f31-8af3-676363573217)

- <a id="bdqcore_782773c9-7b37-483d-8ce2-c6683ba81882"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS
  - Description: Count the number of VALIDATION_TAXON_UNAMBIGUOUS in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:782773c9-7b37-483d-8ce2-c6683ba81882)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:782773c9-7b37-483d-8ce2-c6683ba81882)

- <a id="bdqcore_b5a14d76-292e-499b-b80f-9546243311a0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD
  - Description: Count the number of VALIDATION_TYPESTATUS_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b5a14d76-292e-499b-b80f-9546243311a0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b5a14d76-292e-499b-b80f-9546243311a0)

- <a id="bdqcore_aee65eb8-8d1e-4b8f-bd37-5822e29f5734"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE
  - Description: Count the number of VALIDATION_YEAR_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:aee65eb8-8d1e-4b8f-bd37-5822e29f5734)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:aee65eb8-8d1e-4b8f-bd37-5822e29f5734)

- <a id="bdqcore_687d3ad1-93a3-4a1f-b69f-da5a1eb761a5"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY
  - Description: Count the number of VALIDATION_YEAR_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:687d3ad1-93a3-4a1f-b69f-da5a1eb761a5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:687d3ad1-93a3-4a1f-b69f-da5a1eb761a5)

- <a id="bdqcore_c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8"></a>MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY
  - Description: Measure if all VALIDATION_BASISOFRECORD_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8)

- <a id="bdqcore_241a279c-76d5-499b-ab49-a47ad7f8df50"></a>MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD
  - Description: Measure if all VALIDATION_BASISOFRECORD_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:241a279c-76d5-499b-ab49-a47ad7f8df50)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:241a279c-76d5-499b-ab49-a47ad7f8df50)

- <a id="bdqcore_a2be4734-0a93-46dc-af4a-e2125b47dbd4"></a>MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT
  - Description: Measure if all VALIDATION_CLASSIFICATION_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a2be4734-0a93-46dc-af4a-e2125b47dbd4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a2be4734-0a93-46dc-af4a-e2125b47dbd4)

- <a id="bdqcore_21541436-641d-45a9-938c-537484d94eb7"></a>MULTIRECORD_MEASURE_QA_CLASS_FOUND
  - Description: Measure if all VALIDATION_CLASS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:21541436-641d-45a9-938c-537484d94eb7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:21541436-641d-45a9-938c-537484d94eb7)

- <a id="bdqcore_1ede76d0-c096-465c-8bbb-08c53bf7e367"></a>MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT
  - Description: Measure if all VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1ede76d0-c096-465c-8bbb-08c53bf7e367)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1ede76d0-c096-465c-8bbb-08c53bf7e367)

- <a id="bdqcore_9ff65ace-9d16-4393-b90f-9150d9628371"></a>MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT
  - Description: Measure if all VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9ff65ace-9d16-4393-b90f-9150d9628371)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9ff65ace-9d16-4393-b90f-9150d9628371)

- <a id="bdqcore_fb3732c6-4199-4767-a263-0363a1fe1766"></a>MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT
  - Description: Measure if all VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fb3732c6-4199-4767-a263-0363a1fe1766)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fb3732c6-4199-4767-a263-0363a1fe1766)

- <a id="bdqcore_151b2d29-3460-4ba5-a226-86971dc8ad03"></a>MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO
  - Description: Measure if all VALIDATION_COORDINATES_NOTZERO in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:151b2d29-3460-4ba5-a226-86971dc8ad03)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:151b2d29-3460-4ba5-a226-86971dc8ad03)

- <a id="bdqcore_d94b0130-7a13-4fa8-955c-eff5c47bd9de"></a>MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE
  - Description: Measure if all VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d94b0130-7a13-4fa8-955c-eff5c47bd9de)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d94b0130-7a13-4fa8-955c-eff5c47bd9de)

- <a id="bdqcore_942f63bd-d19d-4214-bf8e-cec0055b8909"></a>MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY
  - Description: Measure if all VALIDATION_COUNTRYCODE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:942f63bd-d19d-4214-bf8e-cec0055b8909)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:942f63bd-d19d-4214-bf8e-cec0055b8909)

- <a id="bdqcore_fedf27b2-e01d-459f-98fc-7f0f39e3d4be"></a>MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD
  - Description: Measure if all VALIDATION_COUNTRYCODE_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fedf27b2-e01d-459f-98fc-7f0f39e3d4be)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fedf27b2-e01d-459f-98fc-7f0f39e3d4be)

- <a id="bdqcore_c6a62914-f42e-442a-9e2b-38ccff594070"></a>MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT
  - Description: Measure if all VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c6a62914-f42e-442a-9e2b-38ccff594070)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c6a62914-f42e-442a-9e2b-38ccff594070)

- <a id="bdqcore_23aced89-d613-479c-bc4c-837d74b73be0"></a>MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS
  - Description: Measure if all VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:23aced89-d613-479c-bc4c-837d74b73be0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:23aced89-d613-479c-bc4c-837d74b73be0)

- <a id="bdqcore_388e74b3-2e18-4d78-8112-3142d1177e25"></a>MULTIRECORD_MEASURE_QA_COUNTRY_FOUND
  - Description: Measure if all VALIDATION_COUNTRY_FOUND in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:388e74b3-2e18-4d78-8112-3142d1177e25)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:388e74b3-2e18-4d78-8112-3142d1177e25)

- <a id="bdqcore_9c8df974-8fba-4537-8c67-31466787f732"></a>MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY
  - Description: Measure if all VALIDATION_COUNTRY_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9c8df974-8fba-4537-8c67-31466787f732)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9c8df974-8fba-4537-8c67-31466787f732)

- <a id="bdqcore_6354376c-0cf2-435b-be40-850769c5a18a"></a>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE
  - Description: Measure if all VALIDATION_DATEIDENTIFIED_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6354376c-0cf2-435b-be40-850769c5a18a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6354376c-0cf2-435b-be40-850769c5a18a)

- <a id="bdqcore_563872eb-f544-45a0-8f91-8098d62768d4"></a>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD
  - Description: Measure if all VALIDATION_DATEIDENTIFIED_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:563872eb-f544-45a0-8f91-8098d62768d4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:563872eb-f544-45a0-8f91-8098d62768d4)

- <a id="bdqcore_85dc5d02-9847-420f-a026-6a0e70962d2a"></a>MULTIRECORD_MEASURE_QA_DAY_INRANGE
  - Description: Measure if all VALIDATION_DAY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:85dc5d02-9847-420f-a026-6a0e70962d2a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:85dc5d02-9847-420f-a026-6a0e70962d2a)

- <a id="bdqcore_371035f6-42b5-494f-86d9-de2f44a6cdc6"></a>MULTIRECORD_MEASURE_QA_DAY_STANDARD
  - Description: Measure if all VALIDATION_DAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:371035f6-42b5-494f-86d9-de2f44a6cdc6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:371035f6-42b5-494f-86d9-de2f44a6cdc6)

- <a id="bdqcore_4d999a65-a431-4a76-b591-e0d86dcf244b"></a>MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY
  - Description: Measure if all VALIDATION_DCTYPE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4d999a65-a431-4a76-b591-e0d86dcf244b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4d999a65-a431-4a76-b591-e0d86dcf244b)

- <a id="bdqcore_d9493fa0-d90e-41db-95f6-d1c1d243540e"></a>MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD
  - Description: Measure if all VALIDATION_DCTYPE_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d9493fa0-d90e-41db-95f6-d1c1d243540e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d9493fa0-d90e-41db-95f6-d1c1d243540e)

- <a id="bdqcore_3c8bc478-f6b2-4533-b7ce-45bae5d186c2"></a>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE
  - Description: Measure if all VALIDATION_DECIMALLATITUDE_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3c8bc478-f6b2-4533-b7ce-45bae5d186c2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3c8bc478-f6b2-4533-b7ce-45bae5d186c2)

- <a id="bdqcore_a2535b23-4407-40bd-b23b-30c8185d72a2"></a>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY
  - Description: Measure if all VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a2535b23-4407-40bd-b23b-30c8185d72a2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a2535b23-4407-40bd-b23b-30c8185d72a2)

- <a id="bdqcore_6f7a9b82-7d34-4111-a2a6-9efe5221fa44"></a>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE
  - Description: Measure if all VALIDATION_DECIMALLONGITUDE_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6f7a9b82-7d34-4111-a2a6-9efe5221fa44)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6f7a9b82-7d34-4111-a2a6-9efe5221fa44)

- <a id="bdqcore_a94e986e-dbc8-4147-872d-5f2727945654"></a>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY
  - Description: Measure if all VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a94e986e-dbc8-4147-872d-5f2727945654)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a94e986e-dbc8-4147-872d-5f2727945654)

- <a id="bdqcore_ba953672-6526-4375-97e8-b4e9d1a7d3a0"></a>MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD
  - Description: Measure if all VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ba953672-6526-4375-97e8-b4e9d1a7d3a0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ba953672-6526-4375-97e8-b4e9d1a7d3a0)

- <a id="bdqcore_c04d428a-13d0-4766-9df7-4dfb2ef5d5d8"></a>MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE
  - Description: Measure if all VALIDATION_ENDDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c04d428a-13d0-4766-9df7-4dfb2ef5d5d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c04d428a-13d0-4766-9df7-4dfb2ef5d5d8)

- <a id="bdqcore_8dfed701-01a9-415d-a9f8-539280b75975"></a>MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD
  - Description: Measure if all VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8dfed701-01a9-415d-a9f8-539280b75975)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8dfed701-01a9-415d-a9f8-539280b75975)

- <a id="bdqcore_d41a731b-2e2b-4442-9217-4c375ae92926"></a>MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE
  - Description: Measure if all VALIDATION_EVENTDATE_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d41a731b-2e2b-4442-9217-4c375ae92926)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d41a731b-2e2b-4442-9217-4c375ae92926)

- <a id="bdqcore_c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365"></a>MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY
  - Description: Measure if all VALIDATION_EVENTDATE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365)

- <a id="bdqcore_14a1d51f-16ed-4148-9dc8-1e90157a9868"></a>MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD
  - Description: Measure if all VALIDATION_EVENTDATE_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:14a1d51f-16ed-4148-9dc8-1e90157a9868)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:14a1d51f-16ed-4148-9dc8-1e90157a9868)

- <a id="bdqcore_4cf4fe57-6736-443b-afda-f7ce8ce25471"></a>MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY
  - Description: Measure if all VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4cf4fe57-6736-443b-afda-f7ce8ce25471)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4cf4fe57-6736-443b-afda-f7ce8ce25471)

- <a id="bdqcore_f375a3fd-4cf5-4ef4-955e-d71762ede2d8"></a>MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT
  - Description: Measure if all VALIDATION_EVENT_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f375a3fd-4cf5-4ef4-955e-d71762ede2d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f375a3fd-4cf5-4ef4-955e-d71762ede2d8)

- <a id="bdqcore_a07d7147-2db8-48ce-81b8-e47595ad5f17"></a>MULTIRECORD_MEASURE_QA_FAMILY_FOUND
  - Description: Measure if all VALIDATION_FAMILY_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a07d7147-2db8-48ce-81b8-e47595ad5f17)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a07d7147-2db8-48ce-81b8-e47595ad5f17)

- <a id="bdqcore_c5c8db83-3af0-4215-806f-e2f90574b138"></a>MULTIRECORD_MEASURE_QA_GENUS_FOUND
  - Description: Measure if all VALIDATION_GENUS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c5c8db83-3af0-4215-806f-e2f90574b138)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c5c8db83-3af0-4215-806f-e2f90574b138)

- <a id="bdqcore_488c1dff-21ec-4e68-a00a-7355505e180c"></a>MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY
  - Description: Measure if all VALIDATION_GEODETICDATUM_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:488c1dff-21ec-4e68-a00a-7355505e180c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:488c1dff-21ec-4e68-a00a-7355505e180c)

- <a id="bdqcore_cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e"></a>MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD
  - Description: Measure if all VALIDATION_GEODETICDATUM_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e)

- <a id="bdqcore_465d7ac1-d193-46c0-a302-56a9ef99215f"></a>MULTIRECORD_MEASURE_QA_KINGDOM_FOUND
  - Description: Measure if all VALIDATION_KINGDOM_FOUND in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:465d7ac1-d193-46c0-a302-56a9ef99215f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:465d7ac1-d193-46c0-a302-56a9ef99215f)

- <a id="bdqcore_3bc9df8b-0f57-4157-9374-b56a99090b22"></a>MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY
  - Description: Measure if all VALIDATION_KINGDOM_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3bc9df8b-0f57-4157-9374-b56a99090b22)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3bc9df8b-0f57-4157-9374-b56a99090b22)

- <a id="bdqcore_4fccf163-9336-4f48-996c-57f5f66e72db"></a>MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY
  - Description: Measure if all VALIDATION_LICENSE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4fccf163-9336-4f48-996c-57f5f66e72db)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4fccf163-9336-4f48-996c-57f5f66e72db)

- <a id="bdqcore_acd8d43e-7a2a-4372-b887-fb53a9972dc9"></a>MULTIRECORD_MEASURE_QA_LICENSE_STANDARD
  - Description: Measure if all VALIDATION_LICENSE_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:acd8d43e-7a2a-4372-b887-fb53a9972dc9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:acd8d43e-7a2a-4372-b887-fb53a9972dc9)

- <a id="bdqcore_3b2e4791-1a5a-4087-9e8d-09c67cf8c816"></a>MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY
  - Description: Measure if all VALIDATION_LOCATION_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3b2e4791-1a5a-4087-9e8d-09c67cf8c816)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3b2e4791-1a5a-4087-9e8d-09c67cf8c816)

- <a id="bdqcore_c73d49d1-06e4-4272-8249-6a26e7f8abca"></a>MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE
  - Description: Measure if all VALIDATION_MAXDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c73d49d1-06e4-4272-8249-6a26e7f8abca)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c73d49d1-06e4-4272-8249-6a26e7f8abca)

- <a id="bdqcore_7c5a6ba0-399d-4570-878a-4a064e2406fe"></a>MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE
  - Description: Measure if all VALIDATION_MAXELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7c5a6ba0-399d-4570-878a-4a064e2406fe)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7c5a6ba0-399d-4570-878a-4a064e2406fe)

- <a id="bdqcore_49d756a8-e654-4267-a290-d1def5d2c5f9"></a>MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE
  - Description: Measure if all VALIDATION_MINDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49d756a8-e654-4267-a290-d1def5d2c5f9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49d756a8-e654-4267-a290-d1def5d2c5f9)

- <a id="bdqcore_fcabd2c9-392c-4841-a5d7-e2680c9587ab"></a>MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH
  - Description: Measure if all VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fcabd2c9-392c-4841-a5d7-e2680c9587ab)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fcabd2c9-392c-4841-a5d7-e2680c9587ab)

- <a id="bdqcore_1ba18c8b-66a6-47d9-a709-404439332dba"></a>MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE
  - Description: Measure if all VALIDATION_MINELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1ba18c8b-66a6-47d9-a709-404439332dba)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1ba18c8b-66a6-47d9-a709-404439332dba)

- <a id="bdqcore_44f00697-ca66-43cf-8f16-646b40c0f514"></a>MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION
  - Description: Measure if all VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:44f00697-ca66-43cf-8f16-646b40c0f514)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:44f00697-ca66-43cf-8f16-646b40c0f514)

- <a id="bdqcore_b3c2bb86-e239-4532-ae0c-b121ec1ee025"></a>MULTIRECORD_MEASURE_QA_MONTH_STANDARD
  - Description: Measure if all VALIDATION_MONTH_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b3c2bb86-e239-4532-ae0c-b121ec1ee025)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b3c2bb86-e239-4532-ae0c-b121ec1ee025)

- <a id="bdqcore_16059801-6adb-4e65-82f4-61eaa70d8df0"></a>MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY
  - Description: Measure if all VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:16059801-6adb-4e65-82f4-61eaa70d8df0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:16059801-6adb-4e65-82f4-61eaa70d8df0)

- <a id="bdqcore_0028ef9a-6553-467b-a344-90327ed2babf"></a>MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY
  - Description: Measure if all VALIDATION_OCCURRENCEID_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0028ef9a-6553-467b-a344-90327ed2babf)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0028ef9a-6553-467b-a344-90327ed2babf)

- <a id="bdqcore_d2922585-2070-4851-a033-15e51977f9dc"></a>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY
  - Description: Measure if all VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d2922585-2070-4851-a033-15e51977f9dc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d2922585-2070-4851-a033-15e51977f9dc)

- <a id="bdqcore_2fea4571-92d0-48a5-a5ba-6caecd647862"></a>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD
  - Description: Measure if all VALIDATION_OCCURRENCESTATUS_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2fea4571-92d0-48a5-a5ba-6caecd647862)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2fea4571-92d0-48a5-a5ba-6caecd647862)

- <a id="bdqcore_773bb288-fef3-4968-a65a-a69c74d6ecb5"></a>MULTIRECORD_MEASURE_QA_ORDER_FOUND
  - Description: Measure if all VALIDATION_ORDER_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:773bb288-fef3-4968-a65a-a69c74d6ecb5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:773bb288-fef3-4968-a65a-a69c74d6ecb5)

- <a id="bdqcore_ef31ba02-cea7-4d76-990f-99ebbd201fb4"></a>MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD
  - Description: Measure if all VALIDATION_PATHWAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ef31ba02-cea7-4d76-990f-99ebbd201fb4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ef31ba02-cea7-4d76-990f-99ebbd201fb4)

- <a id="bdqcore_17364d16-37b7-4ccb-9614-bfb95ff1bca9"></a>MULTIRECORD_MEASURE_QA_PHYLUM_FOUND
  - Description: Measure if all VALIDATION_PHYLUM_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:17364d16-37b7-4ccb-9614-bfb95ff1bca9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:17364d16-37b7-4ccb-9614-bfb95ff1bca9)

- <a id="bdqcore_ef05b45b-13b8-4877-9e9d-fa44b332d83c"></a>MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT
  - Description: Measure if all VALIDATION_POLYNOMIAL_CONSISTENT in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ef05b45b-13b8-4877-9e9d-fa44b332d83c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ef05b45b-13b8-4877-9e9d-fa44b332d83c)

- <a id="bdqcore_6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
  - Description: Measure if all VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7)

- <a id="bdqcore_a9529e71-5470-4cb1-b04d-aa483926f532"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE
  - Description: Measure if all VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a9529e71-5470-4cb1-b04d-aa483926f532)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a9529e71-5470-4cb1-b04d-aa483926f532)

- <a id="bdqcore_4cf84216-c8a7-4865-a8e1-3ffd829d5a10"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY
  - Description: Measure if all VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4cf84216-c8a7-4865-a8e1-3ffd829d5a10)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4cf84216-c8a7-4865-a8e1-3ffd829d5a10)

- <a id="bdqcore_a8aee02c-cf7c-4104-a601-d8afc4f9cbe2"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND
  - Description: Measure if all VALIDATION_SCIENTIFICNAME_FOUND in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a8aee02c-cf7c-4104-a601-d8afc4f9cbe2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a8aee02c-cf7c-4104-a601-d8afc4f9cbe2)

- <a id="bdqcore_b4d6a61c-64ff-4da0-974c-63a73fd20836"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY
  - Description: Measure if all VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b4d6a61c-64ff-4da0-974c-63a73fd20836)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b4d6a61c-64ff-4da0-974c-63a73fd20836)

- <a id="bdqcore_1b3bbac4-7c00-46d6-8179-1d57c92374ad"></a>MULTIRECORD_MEASURE_QA_SEX_STANDARD
  - Description: Measure if all VALIDATION_SEX_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1b3bbac4-7c00-46d6-8179-1d57c92374ad)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1b3bbac4-7c00-46d6-8179-1d57c92374ad)

- <a id="bdqcore_8c217eee-9cd0-48c3-aea0-90151c6c5bfd"></a>MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE
  - Description: Measure if all VALIDATION_STARTDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8c217eee-9cd0-48c3-aea0-90151c6c5bfd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8c217eee-9cd0-48c3-aea0-90151c6c5bfd)

- <a id="bdqcore_9c1cdf6a-0dbf-4828-a2e3-fb368f74d194"></a>MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND
  - Description: Measure if all VALIDATION_STATEPROVINCE_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9c1cdf6a-0dbf-4828-a2e3-fb368f74d194)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9c1cdf6a-0dbf-4828-a2e3-fb368f74d194)

- <a id="bdqcore_e0b8cff1-3322-40d2-b8b2-b99fc9ae130a"></a>MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY
  - Description: Measure if all VALIDATION_TAXONRANK_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:e0b8cff1-3322-40d2-b8b2-b99fc9ae130a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:e0b8cff1-3322-40d2-b8b2-b99fc9ae130a)

- <a id="bdqcore_f320ca83-8487-4011-b1ff-f4b1b4dd86ec"></a>MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD
  - Description: Measure if all VALIDATION_TAXONRANK_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f320ca83-8487-4011-b1ff-f4b1b4dd86ec)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f320ca83-8487-4011-b1ff-f4b1b4dd86ec)

- <a id="bdqcore_2a9d4cfd-815a-46e0-bb51-60724582b762"></a>MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY
  - Description: Measure if all VALIDATION_TAXON_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2a9d4cfd-815a-46e0-bb51-60724582b762)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2a9d4cfd-815a-46e0-bb51-60724582b762)

- <a id="bdqcore_0df03601-3768-4805-906a-bbd0a41b0fda"></a>MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS
  - Description: Measure if all VALIDATION_TAXON_UNAMBIGUOUS in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0df03601-3768-4805-906a-bbd0a41b0fda)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0df03601-3768-4805-906a-bbd0a41b0fda)

- <a id="bdqcore_1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88"></a>MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD
  - Description: Measure if all VALIDATION_TYPESTATUS_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88)

- <a id="bdqcore_a0502c5f-608b-4e59-99da-d9490bb4d93b"></a>MULTIRECORD_MEASURE_QA_YEAR_INRANGE
  - Description: Measure if all VALIDATION_YEAR_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a0502c5f-608b-4e59-99da-d9490bb4d93b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a0502c5f-608b-4e59-99da-d9490bb4d93b)

- <a id="bdqcore_a8fef8a8-e7c7-4a2d-adaf-7da99c896c93"></a>MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY
  - Description: Measure if all VALIDATION_YEAR_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a8fef8a8-e7c7-4a2d-adaf-7da99c896c93)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a8fef8a8-e7c7-4a2d-adaf-7da99c896c93)

- <a id="bdqcore_ac2b7648-d5f9-48ca-9b07-8ad5879a2536"></a>VALIDATION_BASISOFRECORD_NOTEMPTY
  - Description: Is there a value in dwc:basisOfRecord?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ac2b7648-d5f9-48ca-9b07-8ad5879a2536)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ac2b7648-d5f9-48ca-9b07-8ad5879a2536)

- <a id="bdqcore_42408a00-bf71-4892-a399-4325e2bc1fb8"></a>VALIDATION_BASISOFRECORD_STANDARD
  - Description: Does the value of dwc:basisOfRecord occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:42408a00-bf71-4892-a399-4325e2bc1fb8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:42408a00-bf71-4892-a399-4325e2bc1fb8)

- <a id="bdqcore_2750c040-1d4a-4149-99fe-0512785f2d5f"></a>VALIDATION_CLASSIFICATION_CONSISTENT
  - Description: Is the combination of higher classification taxonomic terms consistent using bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2750c040-1d4a-4149-99fe-0512785f2d5f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2750c040-1d4a-4149-99fe-0512785f2d5f)

- <a id="bdqcore_2cd6884e-3d14-4476-94f7-1191cfff309b"></a>VALIDATION_CLASS_FOUND
  - Description: Does the value of dwc:class occur at rank of Class in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2cd6884e-3d14-4476-94f7-1191cfff309b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2cd6884e-3d14-4476-94f7-1191cfff309b)

- <a id="bdqcore_adb27d29-9f0d-4d52-b760-a77ba57a69c9"></a>VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT
  - Description: Do the geographic coordinates fall on or within the boundaries of the territory given in dwc:countryCode or its Exclusive Economic Zone?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:adb27d29-9f0d-4d52-b760-a77ba57a69c9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:adb27d29-9f0d-4d52-b760-a77ba57a69c9)

- <a id="bdqcore_f18a470b-3fe1-4aae-9c65-a6d3db6b550c"></a>VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT
  - Description: Do the geographic coordinates fall on or within the boundary from the bdq:sourceAuthority for the given dwc:stateProvince or within the distance given by bdq:spatialBufferInMeters outside that boundary?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f18a470b-3fe1-4aae-9c65-a6d3db6b550c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f18a470b-3fe1-4aae-9c65-a6d3db6b550c)

- <a id="bdqcore_b9c184ce-a859-410c-9d12-71a338200380"></a>VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT
  - Description: Does the marine/non-marine biome of a taxon from the bdq:sourceAuthority match the biome at the location given by the coordinates?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b9c184ce-a859-410c-9d12-71a338200380)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b9c184ce-a859-410c-9d12-71a338200380)

- <a id="bdqcore_1bf0e210-6792-4128-b8cc-ab6828aa4871"></a>VALIDATION_COORDINATES_NOTZERO
  - Description: Are the values of either dwc:decimalLatitude or dwc:decimalLongitude numbers that are not equal to 0?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1bf0e210-6792-4128-b8cc-ab6828aa4871)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1bf0e210-6792-4128-b8cc-ab6828aa4871)

- <a id="bdqcore_c6adf2ea-3051-4498-97f4-4b2f8a105f57"></a>VALIDATION_COORDINATEUNCERTAINTY_INRANGE
  - Description: Is the value of dwc:coordinateUncertaintyInMeters a number between 1 and 20,037,509?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c6adf2ea-3051-4498-97f4-4b2f8a105f57)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c6adf2ea-3051-4498-97f4-4b2f8a105f57)

- <a id="bdqcore_853b79a2-b314-44a2-ae46-34a1e7ed85e4"></a>VALIDATION_COUNTRYCODE_NOTEMPTY
  - Description: Is there a value in dwc:countryCode?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:853b79a2-b314-44a2-ae46-34a1e7ed85e4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:853b79a2-b314-44a2-ae46-34a1e7ed85e4)

- <a id="bdqcore_0493bcfb-652e-4d17-815b-b0cce0742fbe"></a>VALIDATION_COUNTRYCODE_STANDARD
  - Description: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0493bcfb-652e-4d17-815b-b0cce0742fbe)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0493bcfb-652e-4d17-815b-b0cce0742fbe)

- <a id="bdqcore_b23110e7-1be7-444a-a677-cdee0cf4330c"></a>VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT
  - Description: Does the ISO country code, determined from the value of dwc:country, equal the value of dwc:countryCode?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b23110e7-1be7-444a-a677-cdee0cf4330c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b23110e7-1be7-444a-a677-cdee0cf4330c)

- <a id="bdqcore_d257eb98-27cb-48e5-8d3c-ab9fca4edd11"></a>VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS
  - Description: Is the combination of the values of the terms dwc:country, dwc:stateProvince unique in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d257eb98-27cb-48e5-8d3c-ab9fca4edd11)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d257eb98-27cb-48e5-8d3c-ab9fca4edd11)

- <a id="bdqcore_69b2efdc-6269-45a4-aecb-4cb99c2ae134"></a>VALIDATION_COUNTRY_FOUND
  - Description: Does the value of dwc:country occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:69b2efdc-6269-45a4-aecb-4cb99c2ae134)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:69b2efdc-6269-45a4-aecb-4cb99c2ae134)

- <a id="bdqcore_6ce2b2b4-6afe-4d13-82a0-390d31ade01c"></a>VALIDATION_COUNTRY_NOTEMPTY
  - Description: Is there a value in dwc:country?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6ce2b2b4-6afe-4d13-82a0-390d31ade01c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6ce2b2b4-6afe-4d13-82a0-390d31ade01c)

- <a id="bdqcore_dc8aae4b-134f-4d75-8a71-c4186239178e"></a>VALIDATION_DATEIDENTIFIED_INRANGE
  - Description: Is the value of dwc:dateIdentified within Parameter ranges and either overlap or is later than dwc:eventDate?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:dc8aae4b-134f-4d75-8a71-c4186239178e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:dc8aae4b-134f-4d75-8a71-c4186239178e)

- <a id="bdqcore_66269bdd-9271-4e76-b25c-7ab81eebe1d8"></a>VALIDATION_DATEIDENTIFIED_STANDARD
  - Description: Is the value of dwc:dateIdentified a valid ISO date?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:66269bdd-9271-4e76-b25c-7ab81eebe1d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:66269bdd-9271-4e76-b25c-7ab81eebe1d8)

- <a id="bdqcore_8d787cb5-73e2-4c39-9cd1-67c7361dc02e"></a>VALIDATION_DAY_INRANGE
  - Description: Is the value of dwc:day interpretable as a valid integer between 1 and 28 inclusive or 29, 30 or 31 given the relative month and year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8d787cb5-73e2-4c39-9cd1-67c7361dc02e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8d787cb5-73e2-4c39-9cd1-67c7361dc02e)

- <a id="bdqcore_47ff73ba-0028-4f79-9ce1-ee7008d66498"></a>VALIDATION_DAY_STANDARD
  - Description: Is the value of dwc:day an integer between 1 and 31 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:47ff73ba-0028-4f79-9ce1-ee7008d66498)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:47ff73ba-0028-4f79-9ce1-ee7008d66498)

- <a id="bdqcore_374b091a-fc90-4791-91e5-c1557c649169"></a>VALIDATION_DCTYPE_NOTEMPTY
  - Description: Is there a value in dc:type?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:374b091a-fc90-4791-91e5-c1557c649169)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:374b091a-fc90-4791-91e5-c1557c649169)

- <a id="bdqcore_cdaabb0d-a863-49d0-bc0f-738d771acba5"></a>VALIDATION_DCTYPE_STANDARD
  - Description: Does the value in dc:type occur as a value in the DCMI type vocabulary?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:cdaabb0d-a863-49d0-bc0f-738d771acba5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:cdaabb0d-a863-49d0-bc0f-738d771acba5)

- <a id="bdqcore_b6ecda2a-ce36-437a-b515-3ae94948fe83"></a>VALIDATION_DECIMALLATITUDE_INRANGE
  - Description: Is the value of dwc:decimalLatitude a number between -90 and 90 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b6ecda2a-ce36-437a-b515-3ae94948fe83)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b6ecda2a-ce36-437a-b515-3ae94948fe83)

- <a id="bdqcore_7d2485d5-1ba7-4f25-90cb-f4480ff1a275"></a>VALIDATION_DECIMALLATITUDE_NOTEMPTY
  - Description: Is there a value in dwc:decimalLatitude?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7d2485d5-1ba7-4f25-90cb-f4480ff1a275)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7d2485d5-1ba7-4f25-90cb-f4480ff1a275)

- <a id="bdqcore_0949110d-c06b-450e-9649-7c1374d940d1"></a>VALIDATION_DECIMALLONGITUDE_INRANGE
  - Description: Is the value of dwc:decimalLongitude a number between -180 and 180 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0949110d-c06b-450e-9649-7c1374d940d1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0949110d-c06b-450e-9649-7c1374d940d1)

- <a id="bdqcore_9beb9442-d942-4f42-8b6a-fcea01ee086a"></a>VALIDATION_DECIMALLONGITUDE_NOTEMPTY
  - Description: Is there a value in dwc:decimalLongitude?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9beb9442-d942-4f42-8b6a-fcea01ee086a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9beb9442-d942-4f42-8b6a-fcea01ee086a)

- <a id="bdqcore_060e7734-607d-4737-8b2c-bfa17788bf1a"></a>VALIDATION_DEGREEOFESTABLISHMENT_STANDARD
  - Description: Does the value of dwc:degreeOfEstablishment occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:060e7734-607d-4737-8b2c-bfa17788bf1a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:060e7734-607d-4737-8b2c-bfa17788bf1a)

- <a id="bdqcore_9a39d88c-7eee-46df-b32a-c109f9f81fb8"></a>VALIDATION_ENDDAYOFYEAR_INRANGE
  - Description: Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9a39d88c-7eee-46df-b32a-c109f9f81fb8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9a39d88c-7eee-46df-b32a-c109f9f81fb8)

- <a id="bdqcore_4eb48fdf-7299-4d63-9d08-246902e2857f"></a>VALIDATION_ESTABLISHMENTMEANS_STANDARD
  - Description: Does the value of dwc:establishmentMeans occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4eb48fdf-7299-4d63-9d08-246902e2857f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4eb48fdf-7299-4d63-9d08-246902e2857f)

- <a id="bdqcore_3cff4dc4-72e9-4abe-9bf3-8a30f1618432"></a>VALIDATION_EVENTDATE_INRANGE
  - Description: Is the value of dwc:eventDate entirely with the Parameter Range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3cff4dc4-72e9-4abe-9bf3-8a30f1618432)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3cff4dc4-72e9-4abe-9bf3-8a30f1618432)

- <a id="bdqcore_f51e15a6-a67d-4729-9c28-3766299d2985"></a>VALIDATION_EVENTDATE_NOTEMPTY
  - Description: Is there a value in dwc:eventDate?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f51e15a6-a67d-4729-9c28-3766299d2985)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f51e15a6-a67d-4729-9c28-3766299d2985)

- <a id="bdqcore_4f2bf8fd-fc5c-493f-a44c-e7b16153c803"></a>VALIDATION_EVENTDATE_STANDARD
  - Description: Is the value of dwc:eventDate a valid ISO date?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4f2bf8fd-fc5c-493f-a44c-e7b16153c803)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4f2bf8fd-fc5c-493f-a44c-e7b16153c803)

- <a id="bdqcore_41267642-60ff-4116-90eb-499fee2cd83f"></a>VALIDATION_EVENTTEMPORAL_NOTEMPTY
  - Description: Is there a value in any of the terms dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:41267642-60ff-4116-90eb-499fee2cd83f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:41267642-60ff-4116-90eb-499fee2cd83f)

- <a id="bdqcore_5618f083-d55a-4ac2-92b5-b9fb227b832f"></a>VALIDATION_EVENT_CONSISTENT
  - Description: Are the values in dwc:eventDate consistent with the values in dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:5618f083-d55a-4ac2-92b5-b9fb227b832f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:5618f083-d55a-4ac2-92b5-b9fb227b832f)

- <a id="bdqcore_3667556d-d8f5-454c-922b-af8af38f613c"></a>VALIDATION_FAMILY_FOUND
  - Description: Does the value of dwc:family occur at rank of Family in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3667556d-d8f5-454c-922b-af8af38f613c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3667556d-d8f5-454c-922b-af8af38f613c)

- <a id="bdqcore_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec"></a>VALIDATION_GENUS_FOUND
  - Description: Does the value of dwc:genus occur at the rank of Genus in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f2ce7d55-5b1d-426a-b00e-6d4efe3058ec)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f2ce7d55-5b1d-426a-b00e-6d4efe3058ec)

- <a id="bdqcore_239ec40e-a729-4a8e-ba69-e0bf03ac1c44"></a>VALIDATION_GEODETICDATUM_NOTEMPTY
  - Description: Is there a value in dwc:geodeticDatum?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:239ec40e-a729-4a8e-ba69-e0bf03ac1c44)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:239ec40e-a729-4a8e-ba69-e0bf03ac1c44)

- <a id="bdqcore_7e0c0418-fe16-4a39-98bd-80e19d95b9d1"></a>VALIDATION_GEODETICDATUM_STANDARD
  - Description: Does the value of dwc:geodeticDatum occur as a valid geographic CRS, geodetic Datum or ellipsoid in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7e0c0418-fe16-4a39-98bd-80e19d95b9d1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7e0c0418-fe16-4a39-98bd-80e19d95b9d1)

- <a id="bdqcore_125b5493-052d-4a0d-a3e1-ed5bf792689e"></a>VALIDATION_KINGDOM_FOUND
  - Description: Does the value of dwc:kingdom occur at rank of Kingdom in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:125b5493-052d-4a0d-a3e1-ed5bf792689e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:125b5493-052d-4a0d-a3e1-ed5bf792689e)

- <a id="bdqcore_36ed36c9-b1a7-40b2-b5e2-0d012e772098"></a>VALIDATION_KINGDOM_NOTEMPTY
  - Description: Is there a value in dwc:kingdom?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:36ed36c9-b1a7-40b2-b5e2-0d012e772098)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:36ed36c9-b1a7-40b2-b5e2-0d012e772098)

- <a id="bdqcore_15f78619-811a-4c6f-997a-a4c7888ad849"></a>VALIDATION_LICENSE_NOTEMPTY
  - Description: Is there a value in dcterms:license?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:15f78619-811a-4c6f-997a-a4c7888ad849)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:15f78619-811a-4c6f-997a-a4c7888ad849)

- <a id="bdqcore_3136236e-04b6-49ea-8b34-a65f25e3aba1"></a>VALIDATION_LICENSE_STANDARD
  - Description: Does the value of dcterms:license occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3136236e-04b6-49ea-8b34-a65f25e3aba1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3136236e-04b6-49ea-8b34-a65f25e3aba1)

- <a id="bdqcore_58486cb6-1114-4a8a-ba1e-bd89cfe887e9"></a>VALIDATION_LOCATION_NOTEMPTY
  - Description: Is there a value in any of the Darwin Core spatial terms that could specify a location?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:58486cb6-1114-4a8a-ba1e-bd89cfe887e9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:58486cb6-1114-4a8a-ba1e-bd89cfe887e9)

- <a id="bdqcore_3f1db29a-bfa5-40db-9fd1-fde020d81939"></a>VALIDATION_MAXDEPTH_INRANGE
  - Description: Is the value of dwc:maximumDepthInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3f1db29a-bfa5-40db-9fd1-fde020d81939)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3f1db29a-bfa5-40db-9fd1-fde020d81939)

- <a id="bdqcore_c971fe3f-84c1-4636-9f44-b1ec31fd63c7"></a>VALIDATION_MAXELEVATION_INRANGE
  - Description: Is the value of dwc:maximumElevationInMeters of a single record within a valid range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c971fe3f-84c1-4636-9f44-b1ec31fd63c7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c971fe3f-84c1-4636-9f44-b1ec31fd63c7)

- <a id="bdqcore_04b2c8f3-c71b-4e95-8e43-f70374c5fb92"></a>VALIDATION_MINDEPTH_INRANGE
  - Description: Is the value of dwc:minimumDepthInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:04b2c8f3-c71b-4e95-8e43-f70374c5fb92)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:04b2c8f3-c71b-4e95-8e43-f70374c5fb92)

- <a id="bdqcore_8f1e6e58-544b-4365-a569-fb781341644e"></a>VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH
  - Description: Is the value of dwc:minimumDepthInMeters a number that is less than or equal to the value of dwc:maximumDepthInMeters?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8f1e6e58-544b-4365-a569-fb781341644e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8f1e6e58-544b-4365-a569-fb781341644e)

- <a id="bdqcore_0bb8297d-8f8a-42d2-80c1-558f29efe798"></a>VALIDATION_MINELEVATION_INRANGE
  - Description: Is the value of dwc:minimumElevationInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0bb8297d-8f8a-42d2-80c1-558f29efe798)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0bb8297d-8f8a-42d2-80c1-558f29efe798)

- <a id="bdqcore_d708526b-6561-438e-aa1a-82cd80b06396"></a>VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION
  - Description: Is the value of dwc:minimumElevationInMeters a number less than or equal to the value of dwc:maximumElevationInMeters?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d708526b-6561-438e-aa1a-82cd80b06396)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d708526b-6561-438e-aa1a-82cd80b06396)

- <a id="bdqcore_01c6dafa-0886-4b7e-9881-2c3018c98bdc"></a>VALIDATION_MONTH_STANDARD
  - Description: Is the value of dwc:month interpretable as an integer between 1 and 12 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:01c6dafa-0886-4b7e-9881-2c3018c98bdc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:01c6dafa-0886-4b7e-9881-2c3018c98bdc)

- <a id="bdqcore_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70"></a>VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY
  - Description: Is there a value in dwc:namePublishedInYear?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ff59f77d-71e9-4eb1-aac9-8bd05c50ff70)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ff59f77d-71e9-4eb1-aac9-8bd05c50ff70)

- <a id="bdqcore_c486546c-e6e5-48a7-b286-eba7f5ca56c4"></a>VALIDATION_OCCURRENCEID_NOTEMPTY
  - Description: Is there a value in dwc:occurrenceID?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c486546c-e6e5-48a7-b286-eba7f5ca56c4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c486546c-e6e5-48a7-b286-eba7f5ca56c4)

- <a id="bdqcore_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf"></a>VALIDATION_OCCURRENCESTATUS_NOTEMPTY
  - Description: Is there a value in dwc:occurrenceStatus?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf)

- <a id="bdqcore_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47"></a>VALIDATION_OCCURRENCESTATUS_STANDARD
  - Description: Does the value of dwc:occurrenceStatus occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47)

- <a id="bdqcore_81cc974d-43cc-4c0f-a5e0-afa23b455aa3"></a>VALIDATION_ORDER_FOUND
  - Description: Does the value of dwc:order occur at rank of Order in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:81cc974d-43cc-4c0f-a5e0-afa23b455aa3)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:81cc974d-43cc-4c0f-a5e0-afa23b455aa3)

- <a id="bdqcore_5424e933-bee7-4125-839e-d8743ea69f93"></a>VALIDATION_PATHWAY_STANDARD
  - Description: Does the value of dwc:pathway occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:5424e933-bee7-4125-839e-d8743ea69f93)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:5424e933-bee7-4125-839e-d8743ea69f93)

- <a id="bdqcore_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f"></a>VALIDATION_PHYLUM_FOUND
  - Description: Does the value of dwc:phylum occur at rank of Phylum in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f)

- <a id="bdqcore_17f03f1f-f74d-40c0-8071-2927cfc9487b"></a>VALIDATION_POLYNOMIAL_CONSISTENT
  - Description: Is the polynomial represented in dwc:scientificName consistent with the equivalent values in dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:17f03f1f-f74d-40c0-8071-2927cfc9487b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:17f03f1f-f74d-40c0-8071-2927cfc9487b)

- <a id="bdqcore_49f1d386-5bed-43ae-bd43-deabf7df64fc"></a>VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
  - Description: Is there a value in dwc:scientificNameAuthorship?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49f1d386-5bed-43ae-bd43-deabf7df64fc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49f1d386-5bed-43ae-bd43-deabf7df64fc)

- <a id="bdqcore_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8"></a>VALIDATION_SCIENTIFICNAMEID_COMPLETE
  - Description: Does the value of dwc:scientificNameID contain a complete identifier?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6eeac3ed-f691-457f-a42e-eaa9c8a71ce8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6eeac3ed-f691-457f-a42e-eaa9c8a71ce8)

- <a id="bdqcore_401bf207-9a55-4dff-88a5-abcd58ad97fa"></a>VALIDATION_SCIENTIFICNAMEID_NOTEMPTY
  - Description: Is there a value in dwc:scientificNameID?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:401bf207-9a55-4dff-88a5-abcd58ad97fa)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:401bf207-9a55-4dff-88a5-abcd58ad97fa)

- <a id="bdqcore_3f335517-f442-4b98-b149-1e87ff16de45"></a>VALIDATION_SCIENTIFICNAME_FOUND
  - Description: Is there a match of the contents of dwc:scientificName with the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3f335517-f442-4b98-b149-1e87ff16de45)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3f335517-f442-4b98-b149-1e87ff16de45)

- <a id="bdqcore_7c4b9498-a8d9-4ebb-85f1-9f200c788595"></a>VALIDATION_SCIENTIFICNAME_NOTEMPTY
  - Description: Is there a value in dwc:scientificName?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7c4b9498-a8d9-4ebb-85f1-9f200c788595)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7c4b9498-a8d9-4ebb-85f1-9f200c788595)

- <a id="bdqcore_88d8598b-3318-483d-9475-a5acf9887404"></a>VALIDATION_SEX_STANDARD
  - Description: Does the value of dwc:sex occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:88d8598b-3318-483d-9475-a5acf9887404)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:88d8598b-3318-483d-9475-a5acf9887404)

- <a id="bdqcore_85803c7e-2a5a-42e1-b8d3-299a44cafc46"></a>VALIDATION_STARTDAYOFYEAR_INRANGE
  - Description: Is the value of dwc:startDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:85803c7e-2a5a-42e1-b8d3-299a44cafc46)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:85803c7e-2a5a-42e1-b8d3-299a44cafc46)

- <a id="bdqcore_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a"></a>VALIDATION_STATEPROVINCE_FOUND
  - Description: Does the value of dwc:stateProvince occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4daa7986-d9b0-4dd5-ad17-2d7a771ea71a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4daa7986-d9b0-4dd5-ad17-2d7a771ea71a)

- <a id="bdqcore_14da5b87-8304-4b2b-911d-117e3c29e890"></a>VALIDATION_TAXONRANK_NOTEMPTY
  - Description: Is there a value in dwc:taxonRank?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:14da5b87-8304-4b2b-911d-117e3c29e890)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:14da5b87-8304-4b2b-911d-117e3c29e890)

- <a id="bdqcore_7bdb13a4-8a51-4ee5-be7f-20693fdb183e"></a>VALIDATION_TAXONRANK_STANDARD
  - Description: Does the value of dwc:taxonRank occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7bdb13a4-8a51-4ee5-be7f-20693fdb183e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7bdb13a4-8a51-4ee5-be7f-20693fdb183e)

- <a id="bdqcore_06851339-843f-4a43-8422-4e61b9a00e75"></a>VALIDATION_TAXON_NOTEMPTY
  - Description: Is there a value in any of the terms needed to determine that the taxon exists?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:06851339-843f-4a43-8422-4e61b9a00e75)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:06851339-843f-4a43-8422-4e61b9a00e75)

- <a id="bdqcore_4c09f127-737b-4686-82a0-7c8e30841590"></a>VALIDATION_TAXON_UNAMBIGUOUS
  - Description: Can the taxon be unambiguously resolved from bdq:sourceAuthority using the available taxon terms?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4c09f127-737b-4686-82a0-7c8e30841590)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4c09f127-737b-4686-82a0-7c8e30841590)

- <a id="bdqcore_4833a522-12eb-4fe0-b4cf-7f7a337a6048"></a>VALIDATION_TYPESTATUS_STANDARD
  - Description: Does the value of dwc:typeStatus occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4833a522-12eb-4fe0-b4cf-7f7a337a6048)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4833a522-12eb-4fe0-b4cf-7f7a337a6048)

- <a id="bdqcore_ad0c8855-de69-4843-a80c-a5387d20fbc8"></a>VALIDATION_YEAR_INRANGE
  - Description: Is the value of dwc:year within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ad0c8855-de69-4843-a80c-a5387d20fbc8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ad0c8855-de69-4843-a80c-a5387d20fbc8)

- <a id="bdqcore_c09ecbf9-34e3-4f3e-b74a-8796af15e59f"></a>VALIDATION_YEAR_NOTEMPTY
  - Description: Is there a value in dwc:year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c09ecbf9-34e3-4f3e-b74a-8796af15e59f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c09ecbf9-34e3-4f3e-b74a-8796af15e59f)

### 3.1 Index By Test Label


[AMENDMENT_BASISOFRECORD_STANDARDIZED](#bdqcore_07c28ace-561a-476e-a9b9-3d5ad6e35933) |
[AMENDMENT_COORDINATES_FROM_VERBATIM](#bdqcore_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e) |
[AMENDMENT_COORDINATES_TRANSPOSED](#bdqcore_f2b4a50a-6b2f-4930-b9df-da87b6a21082) |
[AMENDMENT_COUNTRYCODE_FROM_COORDINATES](#bdqcore_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae) |
[AMENDMENT_COUNTRYCODE_STANDARDIZED](#bdqcore_fec5ffe6-3958-4312-82d9-ebcca0efb350) |
[AMENDMENT_DATEIDENTIFIED_STANDARDIZED](#bdqcore_39bb2280-1215-447b-9221-fd13bc990641) |
[AMENDMENT_DAY_STANDARDIZED](#bdqcore_b129fa4d-b25b-43f7-9645-5ed4d44b357b) |
[AMENDMENT_DCTYPE_STANDARDIZED](#bdqcore_bd385eeb-44a2-464b-a503-7abe407ef904) |
[AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED](#bdqcore_74ef1034-e289-4596-b5b0-cde73796697d) |
[AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED](#bdqcore_15d15927-7a22-43f8-88d6-298f5eb45c4c) |
[AMENDMENT_EVENTDATE_FROM_VERBATIM](#bdqcore_6d0a0c10-5e4a-4759-b448-88932f399812) |
[AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY](#bdqcore_3892f432-ddd0-4a0a-b713-f2e2ecbd879d) |
[AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR](#bdqcore_eb0a44fa-241c-4d64-98df-ad4aa837307b) |
[AMENDMENT_EVENTDATE_STANDARDIZED](#bdqcore_718dfc3c-cb52-4fca-b8e2-0e722f375da7) |
[AMENDMENT_EVENT_FROM_EVENTDATE](#bdqcore_710fe118-17e1-440f-b428-88ba3f547d6d) |
[AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](#bdqcore_7498ca76-c4d4-42e2-8103-acacccbdffa7) |
[AMENDMENT_GEODETICDATUM_STANDARDIZED](#bdqcore_0345b325-836d-4235-96d0-3b5caf150fc0) |
[AMENDMENT_LICENSE_STANDARDIZED](#bdqcore_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8) |
[AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM](#bdqcore_c5658b83-4471-4f57-9d94-bf7d0a96900c) |
[AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM](#bdqcore_2d638c8b-4c62-44a0-a14d-fa147bf9823d) |
[AMENDMENT_MONTH_STANDARDIZED](#bdqcore_2e371d57-1eb3-4fe3-8a61-dff43ced50cf) |
[AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT](#bdqcore_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5) |
[AMENDMENT_OCCURRENCESTATUS_STANDARDIZED](#bdqcore_f8f3a093-042c-47a3-971a-a482aaaf3b75) |
[AMENDMENT_PATHWAY_STANDARDIZED](#bdqcore_f9205977-f145-44f5-8cb9-e3e2e35ce908) |
[AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON](#bdqcore_431467d6-9b4b-48fa-a197-cd5379f5e889) |
[AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](#bdqcore_f01fb3f9-2f7e-418b-9f51-adf50f202aea) |
[AMENDMENT_SEX_STANDARDIZED](#bdqcore_33c45ae1-e2db-462a-a59e-7169bb01c5d6) |
[AMENDMENT_TAXONRANK_STANDARDIZED](#bdqcore_e39098df-ef46-464c-9aef-bcdeee2a88cb) |
[AMENDMENT_TYPESTATUS_STANDARDIZED](#bdqcore_b3471c65-b53e-453b-8282-abfa27bf1805) |
[ISSUE_ANNOTATION_NOTEMPTY](#bdqcore_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1) |
[ISSUE_COORDINATES_CENTEROFCOUNTRY](#bdqcore_256e51b3-1e08-4349-bb7e-5186631c3f8e) |
[ISSUE_DATAGENERALIZATIONS_NOTEMPTY](#bdqcore_13d5a10e-188e-40fd-a22c-dbaa87b91df2) |
[ISSUE_ESTABLISHMENTMEANS_NOTEMPTY](#bdqcore_acc8dff2-d8d1-483a-946d-65a02a452700) |
[MEASURE_AMENDMENTS_PROPOSED](#bdqcore_03049fe5-a575-404f-b564-ae63f5a1cf8b) |
[MEASURE_EVENTDATE_DURATIONINSECONDS](#bdqcore_56b6c695-adf1-418e-95d2-da04cad7be53) |
[MEASURE_VALIDATIONTESTS_COMPLIANT](#bdqcore_45fb49eb-4a1b-4b49-876f-15d5034dfc73) |
[MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](#bdqcore_453844ae-9df4-439f-8e24-c52498eca84a) |
[MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](#bdqcore_49a94636-a562-4e6b-803c-665c80628a3d) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY](#bdqcore_b60c8c58-0137-4b6a-97e9-57d8ca5cf248) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD](#bdqcore_f5dd74bd-6a22-4792-b675-c7ccf2a2c103) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT](#bdqcore_a56fb342-c8ee-4611-8aab-e6c6357e8875) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND](#bdqcore_7270a362-5f2e-41f0-955a-d7a8eaaf0f17) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqcore_c439952b-fb00-4902-90b3-a9d477c11a0b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqcore_b89b8424-91eb-4fd1-a6c3-1b0bc92120d0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqcore_25b5d4bf-c871-4485-a457-68021dce0367) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO](#bdqcore_0e239a55-0f19-4c68-bdbf-20580f27a647) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE](#bdqcore_2d90d94b-d384-4bac-aa68-c6800d765882) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY](#bdqcore_d71be8d4-1a04-4816-90c5-49808c823651) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD](#bdqcore_38966850-3737-4a67-953c-c231469e0489) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqcore_18b9d086-29ae-42a5-8f0a-4bc86f4e87ad) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqcore_8b73f37d-89ed-479a-8389-9e71ad2ac84d) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND](#bdqcore_f15c38c3-d96d-4e9c-982d-410fb71cf2bc) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY](#bdqcore_6887c881-dc52-409b-8979-9c2f05e55569) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE](#bdqcore_c72fda2d-16e1-4ded-91a5-a7094339d603) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD](#bdqcore_49b787eb-7dce-4ace-97f5-7cbb47cd8cb9) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE](#bdqcore_780480ff-8c4a-4276-aaca-cbd1248de9fa) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD](#bdqcore_c3e0100f-dfc3-4379-a855-df878eef295e) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY](#bdqcore_f041ab17-d834-4586-aa6b-090de2e571a8) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD](#bdqcore_fbe47441-500f-44c7-a1bd-1e872edc5266) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE](#bdqcore_f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY](#bdqcore_bceae35a-52ab-4968-846f-069ace766513) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE](#bdqcore_c70c4950-2246-4acc-a59d-81eaa47edf2b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY](#bdqcore_f948a30e-8084-48d5-b1ca-d77c476f181f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD](#bdqcore_1b8ae68e-63f1-41c0-9025-fbe64db38d64) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE](#bdqcore_7775309b-5331-4a65-b839-cbe959948d33) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD](#bdqcore_130bb875-6b7c-4965-b864-d53f9d05b2cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE](#bdqcore_c8250600-de61-4047-9d7c-6e06a38c7994) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY](#bdqcore_3f62eaa2-747f-456b-85e6-1a6e74086a18) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD](#bdqcore_bffd7499-aca3-423f-bb43-f7bdc9260f4f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY](#bdqcore_4a1fa336-dd47-4b60-a7b0-c958e2dc72cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT](#bdqcore_1919f212-b7db-4b6e-9697-41a715001bd6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND](#bdqcore_97928242-11a9-4ab0-9dd7-3f0465834824) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND](#bdqcore_977f7e75-a88e-4e29-a7b1-e8cdd35aa107) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY](#bdqcore_63fbaf3c-3d41-4ab6-bfc0-904f1b26835f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD](#bdqcore_8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND](#bdqcore_012eade5-fc64-458a-a13a-a614491bf4e0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY](#bdqcore_342bd81c-e2b7-41d8-b32b-013992d19f99) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY](#bdqcore_47ee20d9-5087-4f76-a494-6fea05e50b8b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD](#bdqcore_9d5be694-f5da-465d-8c7e-27e6dac69f9f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY](#bdqcore_bac852b5-1ba6-427b-aa8e-02018e99279c) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE](#bdqcore_3de8af03-05d4-4fd8-8e6d-ba886dc5446f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE](#bdqcore_6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE](#bdqcore_9c66c116-6644-45b4-b4c7-db7a4ee7c500) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqcore_b21256c2-4bb7-4deb-852d-a9eaa05345e7) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE](#bdqcore_071267a0-d993-4961-a3f7-d8210810d167) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqcore_be2eb717-b390-47d1-b7ba-965a1101e215) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD](#bdqcore_c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqcore_36ea0a78-a079-4014-aca3-2f2b3b11e822) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY](#bdqcore_0c9a139e-5d23-44de-a495-14ec08c61a1c) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY](#bdqcore_298db0c9-a85a-41ee-b111-d622fd969d71) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD](#bdqcore_faca6558-dbff-4d26-a5cb-e11cdf632fe7) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND](#bdqcore_f4fa449c-4b74-4dcf-b4cf-0b73e1496375) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD](#bdqcore_15e0da1d-1a43-4075-8454-b2e618cdd25b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND](#bdqcore_65e66ca0-e9d1-4411-ad26-bb9c43f32afc) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT](#bdqcore_7da5428e-87b2-4ec2-be82-05b9398b7577) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqcore_dbf3cece-1d83-426e-a5e0-8158fcf9c0cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE](#bdqcore_f174ad13-3c67-49f9-8d8b-aba4e933d6f6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY](#bdqcore_a9962d33-ad08-453a-8938-2972425034c2) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND](#bdqcore_4e70b0e4-3fd2-4899-802c-439671374eeb) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY](#bdqcore_0f8b30e2-59dc-46ba-8b91-62049cd1a4e2) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD](#bdqcore_e4d35063-2366-4dda-8eaa-326340361da3) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE](#bdqcore_76008c6b-c56a-4233-84e3-8584950037ec) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND](#bdqcore_58fdd5c1-6201-49a1-a7cd-f49c210dc0b6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY](#bdqcore_de661615-b338-4557-af5b-d44a89de40fa) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD](#bdqcore_602bc457-6b1d-4f24-adef-d0d31bcdf2f0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY](#bdqcore_54d290e8-ac48-4f31-8af3-676363573217) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS](#bdqcore_782773c9-7b37-483d-8ce2-c6683ba81882) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD](#bdqcore_b5a14d76-292e-499b-b80f-9546243311a0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE](#bdqcore_aee65eb8-8d1e-4b8f-bd37-5822e29f5734) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY](#bdqcore_687d3ad1-93a3-4a1f-b69f-da5a1eb761a5) |
[MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY](#bdqcore_c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8) |
[MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD](#bdqcore_241a279c-76d5-499b-ab49-a47ad7f8df50) |
[MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT](#bdqcore_a2be4734-0a93-46dc-af4a-e2125b47dbd4) |
[MULTIRECORD_MEASURE_QA_CLASS_FOUND](#bdqcore_21541436-641d-45a9-938c-537484d94eb7) |
[MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqcore_1ede76d0-c096-465c-8bbb-08c53bf7e367) |
[MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqcore_9ff65ace-9d16-4393-b90f-9150d9628371) |
[MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqcore_fb3732c6-4199-4767-a263-0363a1fe1766) |
[MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO](#bdqcore_151b2d29-3460-4ba5-a226-86971dc8ad03) |
[MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE](#bdqcore_d94b0130-7a13-4fa8-955c-eff5c47bd9de) |
[MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY](#bdqcore_942f63bd-d19d-4214-bf8e-cec0055b8909) |
[MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD](#bdqcore_fedf27b2-e01d-459f-98fc-7f0f39e3d4be) |
[MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqcore_c6a62914-f42e-442a-9e2b-38ccff594070) |
[MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqcore_23aced89-d613-479c-bc4c-837d74b73be0) |
[MULTIRECORD_MEASURE_QA_COUNTRY_FOUND](#bdqcore_388e74b3-2e18-4d78-8112-3142d1177e25) |
[MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY](#bdqcore_9c8df974-8fba-4537-8c67-31466787f732) |
[MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE](#bdqcore_6354376c-0cf2-435b-be40-850769c5a18a) |
[MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD](#bdqcore_563872eb-f544-45a0-8f91-8098d62768d4) |
[MULTIRECORD_MEASURE_QA_DAY_INRANGE](#bdqcore_85dc5d02-9847-420f-a026-6a0e70962d2a) |
[MULTIRECORD_MEASURE_QA_DAY_STANDARD](#bdqcore_371035f6-42b5-494f-86d9-de2f44a6cdc6) |
[MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY](#bdqcore_4d999a65-a431-4a76-b591-e0d86dcf244b) |
[MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD](#bdqcore_d9493fa0-d90e-41db-95f6-d1c1d243540e) |
[MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE](#bdqcore_3c8bc478-f6b2-4533-b7ce-45bae5d186c2) |
[MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY](#bdqcore_a2535b23-4407-40bd-b23b-30c8185d72a2) |
[MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE](#bdqcore_6f7a9b82-7d34-4111-a2a6-9efe5221fa44) |
[MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY](#bdqcore_a94e986e-dbc8-4147-872d-5f2727945654) |
[MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD](#bdqcore_ba953672-6526-4375-97e8-b4e9d1a7d3a0) |
[MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE](#bdqcore_c04d428a-13d0-4766-9df7-4dfb2ef5d5d8) |
[MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD](#bdqcore_8dfed701-01a9-415d-a9f8-539280b75975) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE](#bdqcore_d41a731b-2e2b-4442-9217-4c375ae92926) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY](#bdqcore_c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD](#bdqcore_14a1d51f-16ed-4148-9dc8-1e90157a9868) |
[MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY](#bdqcore_4cf4fe57-6736-443b-afda-f7ce8ce25471) |
[MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT](#bdqcore_f375a3fd-4cf5-4ef4-955e-d71762ede2d8) |
[MULTIRECORD_MEASURE_QA_FAMILY_FOUND](#bdqcore_a07d7147-2db8-48ce-81b8-e47595ad5f17) |
[MULTIRECORD_MEASURE_QA_GENUS_FOUND](#bdqcore_c5c8db83-3af0-4215-806f-e2f90574b138) |
[MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY](#bdqcore_488c1dff-21ec-4e68-a00a-7355505e180c) |
[MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD](#bdqcore_cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e) |
[MULTIRECORD_MEASURE_QA_KINGDOM_FOUND](#bdqcore_465d7ac1-d193-46c0-a302-56a9ef99215f) |
[MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY](#bdqcore_3bc9df8b-0f57-4157-9374-b56a99090b22) |
[MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY](#bdqcore_4fccf163-9336-4f48-996c-57f5f66e72db) |
[MULTIRECORD_MEASURE_QA_LICENSE_STANDARD](#bdqcore_acd8d43e-7a2a-4372-b887-fb53a9972dc9) |
[MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY](#bdqcore_3b2e4791-1a5a-4087-9e8d-09c67cf8c816) |
[MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE](#bdqcore_c73d49d1-06e4-4272-8249-6a26e7f8abca) |
[MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE](#bdqcore_7c5a6ba0-399d-4570-878a-4a064e2406fe) |
[MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE](#bdqcore_49d756a8-e654-4267-a290-d1def5d2c5f9) |
[MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqcore_fcabd2c9-392c-4841-a5d7-e2680c9587ab) |
[MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE](#bdqcore_1ba18c8b-66a6-47d9-a709-404439332dba) |
[MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqcore_44f00697-ca66-43cf-8f16-646b40c0f514) |
[MULTIRECORD_MEASURE_QA_MONTH_STANDARD](#bdqcore_b3c2bb86-e239-4532-ae0c-b121ec1ee025) |
[MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqcore_16059801-6adb-4e65-82f4-61eaa70d8df0) |
[MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY](#bdqcore_0028ef9a-6553-467b-a344-90327ed2babf) |
[MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY](#bdqcore_d2922585-2070-4851-a033-15e51977f9dc) |
[MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD](#bdqcore_2fea4571-92d0-48a5-a5ba-6caecd647862) |
[MULTIRECORD_MEASURE_QA_ORDER_FOUND](#bdqcore_773bb288-fef3-4968-a65a-a69c74d6ecb5) |
[MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD](#bdqcore_ef31ba02-cea7-4d76-990f-99ebbd201fb4) |
[MULTIRECORD_MEASURE_QA_PHYLUM_FOUND](#bdqcore_17364d16-37b7-4ccb-9614-bfb95ff1bca9) |
[MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT](#bdqcore_ef05b45b-13b8-4877-9e9d-fa44b332d83c) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqcore_6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE](#bdqcore_a9529e71-5470-4cb1-b04d-aa483926f532) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY](#bdqcore_4cf84216-c8a7-4865-a8e1-3ffd829d5a10) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND](#bdqcore_a8aee02c-cf7c-4104-a601-d8afc4f9cbe2) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY](#bdqcore_b4d6a61c-64ff-4da0-974c-63a73fd20836) |
[MULTIRECORD_MEASURE_QA_SEX_STANDARD](#bdqcore_1b3bbac4-7c00-46d6-8179-1d57c92374ad) |
[MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE](#bdqcore_8c217eee-9cd0-48c3-aea0-90151c6c5bfd) |
[MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND](#bdqcore_9c1cdf6a-0dbf-4828-a2e3-fb368f74d194) |
[MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY](#bdqcore_e0b8cff1-3322-40d2-b8b2-b99fc9ae130a) |
[MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD](#bdqcore_f320ca83-8487-4011-b1ff-f4b1b4dd86ec) |
[MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY](#bdqcore_2a9d4cfd-815a-46e0-bb51-60724582b762) |
[MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS](#bdqcore_0df03601-3768-4805-906a-bbd0a41b0fda) |
[MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD](#bdqcore_1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88) |
[MULTIRECORD_MEASURE_QA_YEAR_INRANGE](#bdqcore_a0502c5f-608b-4e59-99da-d9490bb4d93b) |
[MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY](#bdqcore_a8fef8a8-e7c7-4a2d-adaf-7da99c896c93) |
[VALIDATION_BASISOFRECORD_NOTEMPTY](#bdqcore_ac2b7648-d5f9-48ca-9b07-8ad5879a2536) |
[VALIDATION_BASISOFRECORD_STANDARD](#bdqcore_42408a00-bf71-4892-a399-4325e2bc1fb8) |
[VALIDATION_CLASSIFICATION_CONSISTENT](#bdqcore_2750c040-1d4a-4149-99fe-0512785f2d5f) |
[VALIDATION_CLASS_FOUND](#bdqcore_2cd6884e-3d14-4476-94f7-1191cfff309b) |
[VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqcore_adb27d29-9f0d-4d52-b760-a77ba57a69c9) |
[VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqcore_f18a470b-3fe1-4aae-9c65-a6d3db6b550c) |
[VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqcore_b9c184ce-a859-410c-9d12-71a338200380) |
[VALIDATION_COORDINATES_NOTZERO](#bdqcore_1bf0e210-6792-4128-b8cc-ab6828aa4871) |
[VALIDATION_COORDINATEUNCERTAINTY_INRANGE](#bdqcore_c6adf2ea-3051-4498-97f4-4b2f8a105f57) |
[VALIDATION_COUNTRYCODE_NOTEMPTY](#bdqcore_853b79a2-b314-44a2-ae46-34a1e7ed85e4) |
[VALIDATION_COUNTRYCODE_STANDARD](#bdqcore_0493bcfb-652e-4d17-815b-b0cce0742fbe) |
[VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqcore_b23110e7-1be7-444a-a677-cdee0cf4330c) |
[VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqcore_d257eb98-27cb-48e5-8d3c-ab9fca4edd11) |
[VALIDATION_COUNTRY_FOUND](#bdqcore_69b2efdc-6269-45a4-aecb-4cb99c2ae134) |
[VALIDATION_COUNTRY_NOTEMPTY](#bdqcore_6ce2b2b4-6afe-4d13-82a0-390d31ade01c) |
[VALIDATION_DATEIDENTIFIED_INRANGE](#bdqcore_dc8aae4b-134f-4d75-8a71-c4186239178e) |
[VALIDATION_DATEIDENTIFIED_STANDARD](#bdqcore_66269bdd-9271-4e76-b25c-7ab81eebe1d8) |
[VALIDATION_DAY_INRANGE](#bdqcore_8d787cb5-73e2-4c39-9cd1-67c7361dc02e) |
[VALIDATION_DAY_STANDARD](#bdqcore_47ff73ba-0028-4f79-9ce1-ee7008d66498) |
[VALIDATION_DCTYPE_NOTEMPTY](#bdqcore_374b091a-fc90-4791-91e5-c1557c649169) |
[VALIDATION_DCTYPE_STANDARD](#bdqcore_cdaabb0d-a863-49d0-bc0f-738d771acba5) |
[VALIDATION_DECIMALLATITUDE_INRANGE](#bdqcore_b6ecda2a-ce36-437a-b515-3ae94948fe83) |
[VALIDATION_DECIMALLATITUDE_NOTEMPTY](#bdqcore_7d2485d5-1ba7-4f25-90cb-f4480ff1a275) |
[VALIDATION_DECIMALLONGITUDE_INRANGE](#bdqcore_0949110d-c06b-450e-9649-7c1374d940d1) |
[VALIDATION_DECIMALLONGITUDE_NOTEMPTY](#bdqcore_9beb9442-d942-4f42-8b6a-fcea01ee086a) |
[VALIDATION_DEGREEOFESTABLISHMENT_STANDARD](#bdqcore_060e7734-607d-4737-8b2c-bfa17788bf1a) |
[VALIDATION_ENDDAYOFYEAR_INRANGE](#bdqcore_9a39d88c-7eee-46df-b32a-c109f9f81fb8) |
[VALIDATION_ESTABLISHMENTMEANS_STANDARD](#bdqcore_4eb48fdf-7299-4d63-9d08-246902e2857f) |
[VALIDATION_EVENTDATE_INRANGE](#bdqcore_3cff4dc4-72e9-4abe-9bf3-8a30f1618432) |
[VALIDATION_EVENTDATE_NOTEMPTY](#bdqcore_f51e15a6-a67d-4729-9c28-3766299d2985) |
[VALIDATION_EVENTDATE_STANDARD](#bdqcore_4f2bf8fd-fc5c-493f-a44c-e7b16153c803) |
[VALIDATION_EVENTTEMPORAL_NOTEMPTY](#bdqcore_41267642-60ff-4116-90eb-499fee2cd83f) |
[VALIDATION_EVENT_CONSISTENT](#bdqcore_5618f083-d55a-4ac2-92b5-b9fb227b832f) |
[VALIDATION_FAMILY_FOUND](#bdqcore_3667556d-d8f5-454c-922b-af8af38f613c) |
[VALIDATION_GENUS_FOUND](#bdqcore_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec) |
[VALIDATION_GEODETICDATUM_NOTEMPTY](#bdqcore_239ec40e-a729-4a8e-ba69-e0bf03ac1c44) |
[VALIDATION_GEODETICDATUM_STANDARD](#bdqcore_7e0c0418-fe16-4a39-98bd-80e19d95b9d1) |
[VALIDATION_KINGDOM_FOUND](#bdqcore_125b5493-052d-4a0d-a3e1-ed5bf792689e) |
[VALIDATION_KINGDOM_NOTEMPTY](#bdqcore_36ed36c9-b1a7-40b2-b5e2-0d012e772098) |
[VALIDATION_LICENSE_NOTEMPTY](#bdqcore_15f78619-811a-4c6f-997a-a4c7888ad849) |
[VALIDATION_LICENSE_STANDARD](#bdqcore_3136236e-04b6-49ea-8b34-a65f25e3aba1) |
[VALIDATION_LOCATION_NOTEMPTY](#bdqcore_58486cb6-1114-4a8a-ba1e-bd89cfe887e9) |
[VALIDATION_MAXDEPTH_INRANGE](#bdqcore_3f1db29a-bfa5-40db-9fd1-fde020d81939) |
[VALIDATION_MAXELEVATION_INRANGE](#bdqcore_c971fe3f-84c1-4636-9f44-b1ec31fd63c7) |
[VALIDATION_MINDEPTH_INRANGE](#bdqcore_04b2c8f3-c71b-4e95-8e43-f70374c5fb92) |
[VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqcore_8f1e6e58-544b-4365-a569-fb781341644e) |
[VALIDATION_MINELEVATION_INRANGE](#bdqcore_0bb8297d-8f8a-42d2-80c1-558f29efe798) |
[VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqcore_d708526b-6561-438e-aa1a-82cd80b06396) |
[VALIDATION_MONTH_STANDARD](#bdqcore_01c6dafa-0886-4b7e-9881-2c3018c98bdc) |
[VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqcore_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70) |
[VALIDATION_OCCURRENCEID_NOTEMPTY](#bdqcore_c486546c-e6e5-48a7-b286-eba7f5ca56c4) |
[VALIDATION_OCCURRENCESTATUS_NOTEMPTY](#bdqcore_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf) |
[VALIDATION_OCCURRENCESTATUS_STANDARD](#bdqcore_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47) |
[VALIDATION_ORDER_FOUND](#bdqcore_81cc974d-43cc-4c0f-a5e0-afa23b455aa3) |
[VALIDATION_PATHWAY_STANDARD](#bdqcore_5424e933-bee7-4125-839e-d8743ea69f93) |
[VALIDATION_PHYLUM_FOUND](#bdqcore_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f) |
[VALIDATION_POLYNOMIAL_CONSISTENT](#bdqcore_17f03f1f-f74d-40c0-8071-2927cfc9487b) |
[VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqcore_49f1d386-5bed-43ae-bd43-deabf7df64fc) |
[VALIDATION_SCIENTIFICNAMEID_COMPLETE](#bdqcore_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8) |
[VALIDATION_SCIENTIFICNAMEID_NOTEMPTY](#bdqcore_401bf207-9a55-4dff-88a5-abcd58ad97fa) |
[VALIDATION_SCIENTIFICNAME_FOUND](#bdqcore_3f335517-f442-4b98-b149-1e87ff16de45) |
[VALIDATION_SCIENTIFICNAME_NOTEMPTY](#bdqcore_7c4b9498-a8d9-4ebb-85f1-9f200c788595) |
[VALIDATION_SEX_STANDARD](#bdqcore_88d8598b-3318-483d-9475-a5acf9887404) |
[VALIDATION_STARTDAYOFYEAR_INRANGE](#bdqcore_85803c7e-2a5a-42e1-b8d3-299a44cafc46) |
[VALIDATION_STATEPROVINCE_FOUND](#bdqcore_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a) |
[VALIDATION_TAXONRANK_NOTEMPTY](#bdqcore_14da5b87-8304-4b2b-911d-117e3c29e890) |
[VALIDATION_TAXONRANK_STANDARD](#bdqcore_7bdb13a4-8a51-4ee5-be7f-20693fdb183e) |
[VALIDATION_TAXON_NOTEMPTY](#bdqcore_06851339-843f-4a43-8422-4e61b9a00e75) |
[VALIDATION_TAXON_UNAMBIGUOUS](#bdqcore_4c09f127-737b-4686-82a0-7c8e30841590) |
[VALIDATION_TYPESTATUS_STANDARD](#bdqcore_4833a522-12eb-4fe0-b4cf-7f7a337a6048) |
[VALIDATION_YEAR_INRANGE](#bdqcore_ad0c8855-de69-4843-a80c-a5387d20fbc8) |
[VALIDATION_YEAR_NOTEMPTY](#bdqcore_c09ecbf9-34e3-4f3e-b74a-8796af15e59f) 
## 4 Vocabulary Summary
- <a id="bdqcore_07c28ace-561a-476e-a9b9-3d5ad6e35933"></a>AMENDMENT_BASISOFRECORD_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:07c28ace-561a-476e-a9b9-3d5ad6e35933)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:07c28ace-561a-476e-a9b9-3d5ad6e35933)

- <a id="bdqcore_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e"></a>AMENDMENT_COORDINATES_FROM_VERBATIM
  - Description: Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e)

- <a id="bdqcore_f2b4a50a-6b2f-4930-b9df-da87b6a21082"></a>AMENDMENT_COORDINATES_TRANSPOSED
  - Description: Proposes an amendment of the signs of dwc:decimalLatitude and/or dwc:decimalLongitude to align the location with the dwc:countryCode.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f2b4a50a-6b2f-4930-b9df-da87b6a21082)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f2b4a50a-6b2f-4930-b9df-da87b6a21082)

- <a id="bdqcore_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae"></a>AMENDMENT_COUNTRYCODE_FROM_COORDINATES
  - Description: Proposes an amendment to the value of dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary from the bdq:countryShapes that is attributable to a single valid country code.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae)

- <a id="bdqcore_fec5ffe6-3958-4312-82d9-ebcca0efb350"></a>AMENDMENT_COUNTRYCODE_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:countryCode if it can be interpreted as an ISO country code.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fec5ffe6-3958-4312-82d9-ebcca0efb350)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fec5ffe6-3958-4312-82d9-ebcca0efb350)

- <a id="bdqcore_39bb2280-1215-447b-9221-fd13bc990641"></a>AMENDMENT_DATEIDENTIFIED_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:dateIdentified to a valid ISO date.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:39bb2280-1215-447b-9221-fd13bc990641)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:39bb2280-1215-447b-9221-fd13bc990641)

- <a id="bdqcore_b129fa4d-b25b-43f7-9645-5ed4d44b357b"></a>AMENDMENT_DAY_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:day as an integer between 1 and 31 inclusive.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b129fa4d-b25b-43f7-9645-5ed4d44b357b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b129fa4d-b25b-43f7-9645-5ed4d44b357b)

- <a id="bdqcore_bd385eeb-44a2-464b-a503-7abe407ef904"></a>AMENDMENT_DCTYPE_STANDARDIZED
  - Description: Proposes an amendment to the value of dc:type using the DCMI type vocabulary.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bd385eeb-44a2-464b-a503-7abe407ef904)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bd385eeb-44a2-464b-a503-7abe407ef904)

- <a id="bdqcore_74ef1034-e289-4596-b5b0-cde73796697d"></a>AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:degreeOfEstablishment using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:74ef1034-e289-4596-b5b0-cde73796697d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:74ef1034-e289-4596-b5b0-cde73796697d)

- <a id="bdqcore_15d15927-7a22-43f8-88d6-298f5eb45c4c"></a>AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:establishmentMeans using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:15d15927-7a22-43f8-88d6-298f5eb45c4c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:15d15927-7a22-43f8-88d6-298f5eb45c4c)

- <a id="bdqcore_6d0a0c10-5e4a-4759-b448-88932f399812"></a>AMENDMENT_EVENTDATE_FROM_VERBATIM
  - Description: Proposes an amendment to the value of dwc:eventDate from the content of dwc:verbatimEventDate.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6d0a0c10-5e4a-4759-b448-88932f399812)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6d0a0c10-5e4a-4759-b448-88932f399812)

- <a id="bdqcore_3892f432-ddd0-4a0a-b713-f2e2ecbd879d"></a>AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY
  - Description: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:month and dwc:day.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3892f432-ddd0-4a0a-b713-f2e2ecbd879d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3892f432-ddd0-4a0a-b713-f2e2ecbd879d)

- <a id="bdqcore_eb0a44fa-241c-4d64-98df-ad4aa837307b"></a>AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR
  - Description: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:eb0a44fa-241c-4d64-98df-ad4aa837307b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:eb0a44fa-241c-4d64-98df-ad4aa837307b)

- <a id="bdqcore_718dfc3c-cb52-4fca-b8e2-0e722f375da7"></a>AMENDMENT_EVENTDATE_STANDARDIZED
  - Description: Proposes an amendment of the value of dwc:eventDate to a valid ISO date.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:718dfc3c-cb52-4fca-b8e2-0e722f375da7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:718dfc3c-cb52-4fca-b8e2-0e722f375da7)

- <a id="bdqcore_710fe118-17e1-440f-b428-88ba3f547d6d"></a>AMENDMENT_EVENT_FROM_EVENTDATE
  - Description: Proposes an amendment to values in any of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear or dwc:endDayOfYear from the content of dwc:eventDate.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:710fe118-17e1-440f-b428-88ba3f547d6d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:710fe118-17e1-440f-b428-88ba3f547d6d)

- <a id="bdqcore_7498ca76-c4d4-42e2-8103-acacccbdffa7"></a>AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT
  - Description: Proposes an amendment to fill in dwc:geodeticDatum using a prameterized value if the dwc:geodeticDatum is empty.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7498ca76-c4d4-42e2-8103-acacccbdffa7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7498ca76-c4d4-42e2-8103-acacccbdffa7)

- <a id="bdqcore_0345b325-836d-4235-96d0-3b5caf150fc0"></a>AMENDMENT_GEODETICDATUM_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:geodeticDatum using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0345b325-836d-4235-96d0-3b5caf150fc0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0345b325-836d-4235-96d0-3b5caf150fc0)

- <a id="bdqcore_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8"></a>AMENDMENT_LICENSE_STANDARDIZED
  - Description: Proposes an amendment to the value of dcterms:license using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8)

- <a id="bdqcore_c5658b83-4471-4f57-9d94-bf7d0a96900c"></a>AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM
  - Description: Proposes amendments of the values of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be interpreted from dwc:verbatimDepth.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c5658b83-4471-4f57-9d94-bf7d0a96900c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c5658b83-4471-4f57-9d94-bf7d0a96900c)

- <a id="bdqcore_2d638c8b-4c62-44a0-a14d-fa147bf9823d"></a>AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM
  - Description: Proposes an amendment or amendments to the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be interpreted from dwc:verbatimElevation.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2d638c8b-4c62-44a0-a14d-fa147bf9823d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2d638c8b-4c62-44a0-a14d-fa147bf9823d)

- <a id="bdqcore_2e371d57-1eb3-4fe3-8a61-dff43ced50cf"></a>AMENDMENT_MONTH_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:month as an integer between 1 and 12 inclusive.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2e371d57-1eb3-4fe3-8a61-dff43ced50cf)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2e371d57-1eb3-4fe3-8a61-dff43ced50cf)

- <a id="bdqcore_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5"></a>AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT
  - Description: Proposes an amendment of the value of dwc:occurrenceStatus to the default parameter value if dwc:occurrenceStatus, dwc:individualCount and dwc:organismQuantity are empty.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5)

- <a id="bdqcore_f8f3a093-042c-47a3-971a-a482aaaf3b75"></a>AMENDMENT_OCCURRENCESTATUS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:occurrenceStatus using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f8f3a093-042c-47a3-971a-a482aaaf3b75)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f8f3a093-042c-47a3-971a-a482aaaf3b75)

- <a id="bdqcore_f9205977-f145-44f5-8cb9-e3e2e35ce908"></a>AMENDMENT_PATHWAY_STANDARDIZED
  - Description: Propose an amendment to the value of dwc:pathway using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f9205977-f145-44f5-8cb9-e3e2e35ce908)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f9205977-f145-44f5-8cb9-e3e2e35ce908)

- <a id="bdqcore_431467d6-9b4b-48fa-a197-cd5379f5e889"></a>AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON
  - Description: Proposes an amendment to the value of dwc:scientificNameID if it can be unambiguously resolved from bdq:sourceAuthority using the available taxon terms.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:431467d6-9b4b-48fa-a197-cd5379f5e889)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:431467d6-9b4b-48fa-a197-cd5379f5e889)

- <a id="bdqcore_f01fb3f9-2f7e-418b-9f51-adf50f202aea"></a>AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID
  - Description: Proposes an amendment to the value of dwc:scientificName using the dwc:scientificNameID value from the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f01fb3f9-2f7e-418b-9f51-adf50f202aea)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f01fb3f9-2f7e-418b-9f51-adf50f202aea)

- <a id="bdqcore_33c45ae1-e2db-462a-a59e-7169bb01c5d6"></a>AMENDMENT_SEX_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:sex using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:33c45ae1-e2db-462a-a59e-7169bb01c5d6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:33c45ae1-e2db-462a-a59e-7169bb01c5d6)

- <a id="bdqcore_e39098df-ef46-464c-9aef-bcdeee2a88cb"></a>AMENDMENT_TAXONRANK_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:taxonRank using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:e39098df-ef46-464c-9aef-bcdeee2a88cb)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:e39098df-ef46-464c-9aef-bcdeee2a88cb)

- <a id="bdqcore_b3471c65-b53e-453b-8282-abfa27bf1805"></a>AMENDMENT_TYPESTATUS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:typeStatus using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b3471c65-b53e-453b-8282-abfa27bf1805)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b3471c65-b53e-453b-8282-abfa27bf1805)

- <a id="bdqcore_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1"></a>ISSUE_ANNOTATION_NOTEMPTY
  - Description: Are there any annotations associated with the record?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1)

- <a id="bdqcore_256e51b3-1e08-4349-bb7e-5186631c3f8e"></a>ISSUE_COORDINATES_CENTEROFCOUNTRY
  - Description: Are the supplied geographic coordinates within a defined buffer of the center of the country?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:256e51b3-1e08-4349-bb7e-5186631c3f8e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:256e51b3-1e08-4349-bb7e-5186631c3f8e)

- <a id="bdqcore_13d5a10e-188e-40fd-a22c-dbaa87b91df2"></a>ISSUE_DATAGENERALIZATIONS_NOTEMPTY
  - Description: Is there a value in dwc:dataGeneralizations?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:13d5a10e-188e-40fd-a22c-dbaa87b91df2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:13d5a10e-188e-40fd-a22c-dbaa87b91df2)

- <a id="bdqcore_acc8dff2-d8d1-483a-946d-65a02a452700"></a>ISSUE_ESTABLISHMENTMEANS_NOTEMPTY
  - Description: Is there a value in dwc:establishmentMeans?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:acc8dff2-d8d1-483a-946d-65a02a452700)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:acc8dff2-d8d1-483a-946d-65a02a452700)

- <a id="bdqcore_03049fe5-a575-404f-b564-ae63f5a1cf8b"></a>MEASURE_AMENDMENTS_PROPOSED
  - Description: A count of the number of distinct AMENDMENT tests that have a Response.status="AMENDED" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:03049fe5-a575-404f-b564-ae63f5a1cf8b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:03049fe5-a575-404f-b564-ae63f5a1cf8b)

- <a id="bdqcore_56b6c695-adf1-418e-95d2-da04cad7be53"></a>MEASURE_EVENTDATE_DURATIONINSECONDS
  - Description: What is the duration of dwc:eventDate in seconds?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:56b6c695-adf1-418e-95d2-da04cad7be53)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:56b6c695-adf1-418e-95d2-da04cad7be53)

- <a id="bdqcore_45fb49eb-4a1b-4b49-876f-15d5034dfc73"></a>MEASURE_VALIDATIONTESTS_COMPLIANT
  - Description: Measures the number of distinct VALIDATION tests that have a Response.status="COMPLIANT" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:45fb49eb-4a1b-4b49-876f-15d5034dfc73)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:45fb49eb-4a1b-4b49-876f-15d5034dfc73)

- <a id="bdqcore_453844ae-9df4-439f-8e24-c52498eca84a"></a>MEASURE_VALIDATIONTESTS_NOTCOMPLIANT
  - Description: A count of the number of distinct VALIDATION tests that have a Response.status="NOT_COMPLIANT" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:453844ae-9df4-439f-8e24-c52498eca84a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:453844ae-9df4-439f-8e24-c52498eca84a)

- <a id="bdqcore_49a94636-a562-4e6b-803c-665c80628a3d"></a>MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET
  - Description: The number of distinct VALIDATION tests that have a Response.status="EXTERNAL_PREREQUISITES_NOT_MET" or "INTERNAL_PREREQUISITES_NOT_MET" for a given record.
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49a94636-a562-4e6b-803c-665c80628a3d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49a94636-a562-4e6b-803c-665c80628a3d)

- <a id="bdqcore_b60c8c58-0137-4b6a-97e9-57d8ca5cf248"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY
  - Description: Count the number of VALIDATION_BASISOFRECORD_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b60c8c58-0137-4b6a-97e9-57d8ca5cf248)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b60c8c58-0137-4b6a-97e9-57d8ca5cf248)

- <a id="bdqcore_f5dd74bd-6a22-4792-b675-c7ccf2a2c103"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD
  - Description: Count the number of VALIDATION_BASISOFRECORD_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f5dd74bd-6a22-4792-b675-c7ccf2a2c103)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f5dd74bd-6a22-4792-b675-c7ccf2a2c103)

- <a id="bdqcore_a56fb342-c8ee-4611-8aab-e6c6357e8875"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT
  - Description: Count the number of VALIDATION_CLASSIFICATION_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a56fb342-c8ee-4611-8aab-e6c6357e8875)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a56fb342-c8ee-4611-8aab-e6c6357e8875)

- <a id="bdqcore_7270a362-5f2e-41f0-955a-d7a8eaaf0f17"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND
  - Description: Count the number of VALIDATION_CLASS_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7270a362-5f2e-41f0-955a-d7a8eaaf0f17)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7270a362-5f2e-41f0-955a-d7a8eaaf0f17)

- <a id="bdqcore_c439952b-fb00-4902-90b3-a9d477c11a0b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT
  - Description: Count the number of VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c439952b-fb00-4902-90b3-a9d477c11a0b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c439952b-fb00-4902-90b3-a9d477c11a0b)

- <a id="bdqcore_b89b8424-91eb-4fd1-a6c3-1b0bc92120d0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT
  - Description: Count the number of VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b89b8424-91eb-4fd1-a6c3-1b0bc92120d0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b89b8424-91eb-4fd1-a6c3-1b0bc92120d0)

- <a id="bdqcore_25b5d4bf-c871-4485-a457-68021dce0367"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT
  - Description: Count the number of VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:25b5d4bf-c871-4485-a457-68021dce0367)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:25b5d4bf-c871-4485-a457-68021dce0367)

- <a id="bdqcore_0e239a55-0f19-4c68-bdbf-20580f27a647"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO
  - Description: Count the number of VALIDATION_COORDINATES_NOTZERO in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0e239a55-0f19-4c68-bdbf-20580f27a647)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0e239a55-0f19-4c68-bdbf-20580f27a647)

- <a id="bdqcore_2d90d94b-d384-4bac-aa68-c6800d765882"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE
  - Description: Count the number of VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2d90d94b-d384-4bac-aa68-c6800d765882)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2d90d94b-d384-4bac-aa68-c6800d765882)

- <a id="bdqcore_d71be8d4-1a04-4816-90c5-49808c823651"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY
  - Description: Count the number of VALIDATION_COUNTRYCODE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d71be8d4-1a04-4816-90c5-49808c823651)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d71be8d4-1a04-4816-90c5-49808c823651)

- <a id="bdqcore_38966850-3737-4a67-953c-c231469e0489"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD
  - Description: Count the number of VALIDATION_COUNTRYCODE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:38966850-3737-4a67-953c-c231469e0489)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:38966850-3737-4a67-953c-c231469e0489)

- <a id="bdqcore_18b9d086-29ae-42a5-8f0a-4bc86f4e87ad"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT
  - Description: Count the number of VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:18b9d086-29ae-42a5-8f0a-4bc86f4e87ad)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:18b9d086-29ae-42a5-8f0a-4bc86f4e87ad)

- <a id="bdqcore_8b73f37d-89ed-479a-8389-9e71ad2ac84d"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS
  - Description: Count the number of VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8b73f37d-89ed-479a-8389-9e71ad2ac84d)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8b73f37d-89ed-479a-8389-9e71ad2ac84d)

- <a id="bdqcore_f15c38c3-d96d-4e9c-982d-410fb71cf2bc"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND
  - Description: Count the number of VALIDATION_COUNTRY_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f15c38c3-d96d-4e9c-982d-410fb71cf2bc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f15c38c3-d96d-4e9c-982d-410fb71cf2bc)

- <a id="bdqcore_6887c881-dc52-409b-8979-9c2f05e55569"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY
  - Description: Count the number of VALIDATION_COUNTRY_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6887c881-dc52-409b-8979-9c2f05e55569)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6887c881-dc52-409b-8979-9c2f05e55569)

- <a id="bdqcore_c72fda2d-16e1-4ded-91a5-a7094339d603"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE
  - Description: Count the number of VALIDATION_DATEIDENTIFIED_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c72fda2d-16e1-4ded-91a5-a7094339d603)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c72fda2d-16e1-4ded-91a5-a7094339d603)

- <a id="bdqcore_49b787eb-7dce-4ace-97f5-7cbb47cd8cb9"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD
  - Description: Count the number of VALIDATION_DATEIDENTIFIED_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49b787eb-7dce-4ace-97f5-7cbb47cd8cb9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49b787eb-7dce-4ace-97f5-7cbb47cd8cb9)

- <a id="bdqcore_780480ff-8c4a-4276-aaca-cbd1248de9fa"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE
  - Description: Count the number of VALIDATION_DAY_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:780480ff-8c4a-4276-aaca-cbd1248de9fa)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:780480ff-8c4a-4276-aaca-cbd1248de9fa)

- <a id="bdqcore_c3e0100f-dfc3-4379-a855-df878eef295e"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD
  - Description: Count the number of VALIDATION_DAY_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c3e0100f-dfc3-4379-a855-df878eef295e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c3e0100f-dfc3-4379-a855-df878eef295e)

- <a id="bdqcore_f041ab17-d834-4586-aa6b-090de2e571a8"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY
  - Description: Count the number of VALIDATION_DCTYPE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f041ab17-d834-4586-aa6b-090de2e571a8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f041ab17-d834-4586-aa6b-090de2e571a8)

- <a id="bdqcore_fbe47441-500f-44c7-a1bd-1e872edc5266"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD
  - Description: Count the number of VALIDATION_DCTYPE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fbe47441-500f-44c7-a1bd-1e872edc5266)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fbe47441-500f-44c7-a1bd-1e872edc5266)

- <a id="bdqcore_f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE
  - Description: Count the number of VALIDATION_DECIMALLATITUDE_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26)

- <a id="bdqcore_bceae35a-52ab-4968-846f-069ace766513"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY
  - Description: Count the number of VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bceae35a-52ab-4968-846f-069ace766513)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bceae35a-52ab-4968-846f-069ace766513)

- <a id="bdqcore_c70c4950-2246-4acc-a59d-81eaa47edf2b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE
  - Description: Count the number of VALIDATION_DECIMALLONGITUDE_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c70c4950-2246-4acc-a59d-81eaa47edf2b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c70c4950-2246-4acc-a59d-81eaa47edf2b)

- <a id="bdqcore_f948a30e-8084-48d5-b1ca-d77c476f181f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY
  - Description: Count the number of VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f948a30e-8084-48d5-b1ca-d77c476f181f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f948a30e-8084-48d5-b1ca-d77c476f181f)

- <a id="bdqcore_1b8ae68e-63f1-41c0-9025-fbe64db38d64"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD
  - Description: Count the number of VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1b8ae68e-63f1-41c0-9025-fbe64db38d64)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1b8ae68e-63f1-41c0-9025-fbe64db38d64)

- <a id="bdqcore_7775309b-5331-4a65-b839-cbe959948d33"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE
  - Description: Count the number of VALIDATION_ENDDAYOFYEAR_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7775309b-5331-4a65-b839-cbe959948d33)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7775309b-5331-4a65-b839-cbe959948d33)

- <a id="bdqcore_130bb875-6b7c-4965-b864-d53f9d05b2cd"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD
  - Description: Count the number of VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:130bb875-6b7c-4965-b864-d53f9d05b2cd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:130bb875-6b7c-4965-b864-d53f9d05b2cd)

- <a id="bdqcore_c8250600-de61-4047-9d7c-6e06a38c7994"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE
  - Description: Count the number of VALIDATION_EVENTDATE_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c8250600-de61-4047-9d7c-6e06a38c7994)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c8250600-de61-4047-9d7c-6e06a38c7994)

- <a id="bdqcore_3f62eaa2-747f-456b-85e6-1a6e74086a18"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY
  - Description: Count the number of VALIDATION_EVENTDATE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3f62eaa2-747f-456b-85e6-1a6e74086a18)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3f62eaa2-747f-456b-85e6-1a6e74086a18)

- <a id="bdqcore_bffd7499-aca3-423f-bb43-f7bdc9260f4f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD
  - Description: Count the number of VALIDATION_EVENTDATE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bffd7499-aca3-423f-bb43-f7bdc9260f4f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bffd7499-aca3-423f-bb43-f7bdc9260f4f)

- <a id="bdqcore_4a1fa336-dd47-4b60-a7b0-c958e2dc72cd"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY
  - Description: Count the number of VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4a1fa336-dd47-4b60-a7b0-c958e2dc72cd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4a1fa336-dd47-4b60-a7b0-c958e2dc72cd)

- <a id="bdqcore_1919f212-b7db-4b6e-9697-41a715001bd6"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT
  - Description: Count the number of VALIDATION_EVENT_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1919f212-b7db-4b6e-9697-41a715001bd6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1919f212-b7db-4b6e-9697-41a715001bd6)

- <a id="bdqcore_97928242-11a9-4ab0-9dd7-3f0465834824"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND
  - Description: Count the number of VALIDATION_FAMILY_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:97928242-11a9-4ab0-9dd7-3f0465834824)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:97928242-11a9-4ab0-9dd7-3f0465834824)

- <a id="bdqcore_977f7e75-a88e-4e29-a7b1-e8cdd35aa107"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND
  - Description: Count the number of VALIDATION_GENUS_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:977f7e75-a88e-4e29-a7b1-e8cdd35aa107)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:977f7e75-a88e-4e29-a7b1-e8cdd35aa107)

- <a id="bdqcore_63fbaf3c-3d41-4ab6-bfc0-904f1b26835f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY
  - Description: Count the number of VALIDATION_GEODETICDATUM_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:63fbaf3c-3d41-4ab6-bfc0-904f1b26835f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:63fbaf3c-3d41-4ab6-bfc0-904f1b26835f)

- <a id="bdqcore_8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD
  - Description: Count the number of VALIDATION_GEODETICDATUM_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63)

- <a id="bdqcore_012eade5-fc64-458a-a13a-a614491bf4e0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND
  - Description: Count the number of VALIDATION_KINGDOM_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:012eade5-fc64-458a-a13a-a614491bf4e0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:012eade5-fc64-458a-a13a-a614491bf4e0)

- <a id="bdqcore_342bd81c-e2b7-41d8-b32b-013992d19f99"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY
  - Description: Count the number of VALIDATION_KINGDOM_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:342bd81c-e2b7-41d8-b32b-013992d19f99)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:342bd81c-e2b7-41d8-b32b-013992d19f99)

- <a id="bdqcore_47ee20d9-5087-4f76-a494-6fea05e50b8b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY
  - Description: Count the number of VALIDATION_LICENSE_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:47ee20d9-5087-4f76-a494-6fea05e50b8b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:47ee20d9-5087-4f76-a494-6fea05e50b8b)

- <a id="bdqcore_9d5be694-f5da-465d-8c7e-27e6dac69f9f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD
  - Description: Count the number of VALIDATION_LICENSE_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9d5be694-f5da-465d-8c7e-27e6dac69f9f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9d5be694-f5da-465d-8c7e-27e6dac69f9f)

- <a id="bdqcore_bac852b5-1ba6-427b-aa8e-02018e99279c"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY
  - Description: Count the number of VALIDATION_LOCATION_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:bac852b5-1ba6-427b-aa8e-02018e99279c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:bac852b5-1ba6-427b-aa8e-02018e99279c)

- <a id="bdqcore_3de8af03-05d4-4fd8-8e6d-ba886dc5446f"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE
  - Description: Count the number of VALIDATION_MAXDEPTH_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3de8af03-05d4-4fd8-8e6d-ba886dc5446f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3de8af03-05d4-4fd8-8e6d-ba886dc5446f)

- <a id="bdqcore_6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE
  - Description: Count the number of VALIDATION_MAXELEVATION_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5)

- <a id="bdqcore_9c66c116-6644-45b4-b4c7-db7a4ee7c500"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE
  - Description: Count the number of VALIDATION_MINDEPTH_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9c66c116-6644-45b4-b4c7-db7a4ee7c500)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9c66c116-6644-45b4-b4c7-db7a4ee7c500)

- <a id="bdqcore_b21256c2-4bb7-4deb-852d-a9eaa05345e7"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH
  - Description: Count the number of VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b21256c2-4bb7-4deb-852d-a9eaa05345e7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b21256c2-4bb7-4deb-852d-a9eaa05345e7)

- <a id="bdqcore_071267a0-d993-4961-a3f7-d8210810d167"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE
  - Description: Count the number of VALIDATION_MINELEVATION_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:071267a0-d993-4961-a3f7-d8210810d167)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:071267a0-d993-4961-a3f7-d8210810d167)

- <a id="bdqcore_be2eb717-b390-47d1-b7ba-965a1101e215"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION
  - Description: Count the number of VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:be2eb717-b390-47d1-b7ba-965a1101e215)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:be2eb717-b390-47d1-b7ba-965a1101e215)

- <a id="bdqcore_c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD
  - Description: Count the number of VALIDATION_MONTH_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3)

- <a id="bdqcore_36ea0a78-a079-4014-aca3-2f2b3b11e822"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY
  - Description: Count the number of VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:36ea0a78-a079-4014-aca3-2f2b3b11e822)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:36ea0a78-a079-4014-aca3-2f2b3b11e822)

- <a id="bdqcore_0c9a139e-5d23-44de-a495-14ec08c61a1c"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY
  - Description: Count the number of VALIDATION_OCCURRENCEID_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0c9a139e-5d23-44de-a495-14ec08c61a1c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0c9a139e-5d23-44de-a495-14ec08c61a1c)

- <a id="bdqcore_298db0c9-a85a-41ee-b111-d622fd969d71"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY
  - Description: Count the number of VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:298db0c9-a85a-41ee-b111-d622fd969d71)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:298db0c9-a85a-41ee-b111-d622fd969d71)

- <a id="bdqcore_faca6558-dbff-4d26-a5cb-e11cdf632fe7"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD
  - Description: Count the number of VALIDATION_OCCURRENCESTATUS_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:faca6558-dbff-4d26-a5cb-e11cdf632fe7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:faca6558-dbff-4d26-a5cb-e11cdf632fe7)

- <a id="bdqcore_f4fa449c-4b74-4dcf-b4cf-0b73e1496375"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND
  - Description: Count the number of VALIDATION_ORDER_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f4fa449c-4b74-4dcf-b4cf-0b73e1496375)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f4fa449c-4b74-4dcf-b4cf-0b73e1496375)

- <a id="bdqcore_15e0da1d-1a43-4075-8454-b2e618cdd25b"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD
  - Description: Count the number of VALIDATION_PATHWAY_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:15e0da1d-1a43-4075-8454-b2e618cdd25b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:15e0da1d-1a43-4075-8454-b2e618cdd25b)

- <a id="bdqcore_65e66ca0-e9d1-4411-ad26-bb9c43f32afc"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND
  - Description: Count the number of VALIDATION_PHYLUM_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:65e66ca0-e9d1-4411-ad26-bb9c43f32afc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:65e66ca0-e9d1-4411-ad26-bb9c43f32afc)

- <a id="bdqcore_7da5428e-87b2-4ec2-be82-05b9398b7577"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT
  - Description: Count the number of VALIDATION_POLYNOMIAL_CONSISTENT in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7da5428e-87b2-4ec2-be82-05b9398b7577)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7da5428e-87b2-4ec2-be82-05b9398b7577)

- <a id="bdqcore_dbf3cece-1d83-426e-a5e0-8158fcf9c0cd"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
  - Description: Count the number of VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:dbf3cece-1d83-426e-a5e0-8158fcf9c0cd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:dbf3cece-1d83-426e-a5e0-8158fcf9c0cd)

- <a id="bdqcore_f174ad13-3c67-49f9-8d8b-aba4e933d6f6"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE
  - Description: Count the number of VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f174ad13-3c67-49f9-8d8b-aba4e933d6f6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f174ad13-3c67-49f9-8d8b-aba4e933d6f6)

- <a id="bdqcore_a9962d33-ad08-453a-8938-2972425034c2"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY
  - Description: Count the number of VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a9962d33-ad08-453a-8938-2972425034c2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a9962d33-ad08-453a-8938-2972425034c2)

- <a id="bdqcore_4e70b0e4-3fd2-4899-802c-439671374eeb"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND
  - Description: Count the number of VALIDATION_SCIENTIFICNAME_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4e70b0e4-3fd2-4899-802c-439671374eeb)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4e70b0e4-3fd2-4899-802c-439671374eeb)

- <a id="bdqcore_0f8b30e2-59dc-46ba-8b91-62049cd1a4e2"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY
  - Description: Count the number of VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0f8b30e2-59dc-46ba-8b91-62049cd1a4e2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0f8b30e2-59dc-46ba-8b91-62049cd1a4e2)

- <a id="bdqcore_e4d35063-2366-4dda-8eaa-326340361da3"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD
  - Description: Count the number of VALIDATION_SEX_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:e4d35063-2366-4dda-8eaa-326340361da3)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:e4d35063-2366-4dda-8eaa-326340361da3)

- <a id="bdqcore_76008c6b-c56a-4233-84e3-8584950037ec"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE
  - Description: Count the number of VALIDATION_STARTDAYOFYEAR_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:76008c6b-c56a-4233-84e3-8584950037ec)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:76008c6b-c56a-4233-84e3-8584950037ec)

- <a id="bdqcore_58fdd5c1-6201-49a1-a7cd-f49c210dc0b6"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND
  - Description: Count the number of VALIDATION_STATEPROVINCE_FOUND in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:58fdd5c1-6201-49a1-a7cd-f49c210dc0b6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:58fdd5c1-6201-49a1-a7cd-f49c210dc0b6)

- <a id="bdqcore_de661615-b338-4557-af5b-d44a89de40fa"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY
  - Description: Count the number of VALIDATION_TAXONRANK_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:de661615-b338-4557-af5b-d44a89de40fa)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:de661615-b338-4557-af5b-d44a89de40fa)

- <a id="bdqcore_602bc457-6b1d-4f24-adef-d0d31bcdf2f0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD
  - Description: Count the number of VALIDATION_TAXONRANK_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:602bc457-6b1d-4f24-adef-d0d31bcdf2f0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:602bc457-6b1d-4f24-adef-d0d31bcdf2f0)

- <a id="bdqcore_54d290e8-ac48-4f31-8af3-676363573217"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY
  - Description: Count the number of VALIDATION_TAXON_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:54d290e8-ac48-4f31-8af3-676363573217)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:54d290e8-ac48-4f31-8af3-676363573217)

- <a id="bdqcore_782773c9-7b37-483d-8ce2-c6683ba81882"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS
  - Description: Count the number of VALIDATION_TAXON_UNAMBIGUOUS in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:782773c9-7b37-483d-8ce2-c6683ba81882)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:782773c9-7b37-483d-8ce2-c6683ba81882)

- <a id="bdqcore_b5a14d76-292e-499b-b80f-9546243311a0"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD
  - Description: Count the number of VALIDATION_TYPESTATUS_STANDARD in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b5a14d76-292e-499b-b80f-9546243311a0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b5a14d76-292e-499b-b80f-9546243311a0)

- <a id="bdqcore_aee65eb8-8d1e-4b8f-bd37-5822e29f5734"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE
  - Description: Count the number of VALIDATION_YEAR_INRANGE in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:aee65eb8-8d1e-4b8f-bd37-5822e29f5734)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:aee65eb8-8d1e-4b8f-bd37-5822e29f5734)

- <a id="bdqcore_687d3ad1-93a3-4a1f-b69f-da5a1eb761a5"></a>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY
  - Description: Count the number of VALIDATION_YEAR_NOTEMPTY in a record set that are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:687d3ad1-93a3-4a1f-b69f-da5a1eb761a5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:687d3ad1-93a3-4a1f-b69f-da5a1eb761a5)

- <a id="bdqcore_c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8"></a>MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY
  - Description: Measure if all VALIDATION_BASISOFRECORD_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8)

- <a id="bdqcore_241a279c-76d5-499b-ab49-a47ad7f8df50"></a>MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD
  - Description: Measure if all VALIDATION_BASISOFRECORD_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:241a279c-76d5-499b-ab49-a47ad7f8df50)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:241a279c-76d5-499b-ab49-a47ad7f8df50)

- <a id="bdqcore_a2be4734-0a93-46dc-af4a-e2125b47dbd4"></a>MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT
  - Description: Measure if all VALIDATION_CLASSIFICATION_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a2be4734-0a93-46dc-af4a-e2125b47dbd4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a2be4734-0a93-46dc-af4a-e2125b47dbd4)

- <a id="bdqcore_21541436-641d-45a9-938c-537484d94eb7"></a>MULTIRECORD_MEASURE_QA_CLASS_FOUND
  - Description: Measure if all VALIDATION_CLASS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:21541436-641d-45a9-938c-537484d94eb7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:21541436-641d-45a9-938c-537484d94eb7)

- <a id="bdqcore_1ede76d0-c096-465c-8bbb-08c53bf7e367"></a>MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT
  - Description: Measure if all VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1ede76d0-c096-465c-8bbb-08c53bf7e367)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1ede76d0-c096-465c-8bbb-08c53bf7e367)

- <a id="bdqcore_9ff65ace-9d16-4393-b90f-9150d9628371"></a>MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT
  - Description: Measure if all VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9ff65ace-9d16-4393-b90f-9150d9628371)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9ff65ace-9d16-4393-b90f-9150d9628371)

- <a id="bdqcore_fb3732c6-4199-4767-a263-0363a1fe1766"></a>MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT
  - Description: Measure if all VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fb3732c6-4199-4767-a263-0363a1fe1766)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fb3732c6-4199-4767-a263-0363a1fe1766)

- <a id="bdqcore_151b2d29-3460-4ba5-a226-86971dc8ad03"></a>MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO
  - Description: Measure if all VALIDATION_COORDINATES_NOTZERO in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:151b2d29-3460-4ba5-a226-86971dc8ad03)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:151b2d29-3460-4ba5-a226-86971dc8ad03)

- <a id="bdqcore_d94b0130-7a13-4fa8-955c-eff5c47bd9de"></a>MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE
  - Description: Measure if all VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d94b0130-7a13-4fa8-955c-eff5c47bd9de)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d94b0130-7a13-4fa8-955c-eff5c47bd9de)

- <a id="bdqcore_942f63bd-d19d-4214-bf8e-cec0055b8909"></a>MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY
  - Description: Measure if all VALIDATION_COUNTRYCODE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:942f63bd-d19d-4214-bf8e-cec0055b8909)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:942f63bd-d19d-4214-bf8e-cec0055b8909)

- <a id="bdqcore_fedf27b2-e01d-459f-98fc-7f0f39e3d4be"></a>MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD
  - Description: Measure if all VALIDATION_COUNTRYCODE_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fedf27b2-e01d-459f-98fc-7f0f39e3d4be)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fedf27b2-e01d-459f-98fc-7f0f39e3d4be)

- <a id="bdqcore_c6a62914-f42e-442a-9e2b-38ccff594070"></a>MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT
  - Description: Measure if all VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c6a62914-f42e-442a-9e2b-38ccff594070)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c6a62914-f42e-442a-9e2b-38ccff594070)

- <a id="bdqcore_23aced89-d613-479c-bc4c-837d74b73be0"></a>MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS
  - Description: Measure if all VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:23aced89-d613-479c-bc4c-837d74b73be0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:23aced89-d613-479c-bc4c-837d74b73be0)

- <a id="bdqcore_388e74b3-2e18-4d78-8112-3142d1177e25"></a>MULTIRECORD_MEASURE_QA_COUNTRY_FOUND
  - Description: Measure if all VALIDATION_COUNTRY_FOUND in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:388e74b3-2e18-4d78-8112-3142d1177e25)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:388e74b3-2e18-4d78-8112-3142d1177e25)

- <a id="bdqcore_9c8df974-8fba-4537-8c67-31466787f732"></a>MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY
  - Description: Measure if all VALIDATION_COUNTRY_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9c8df974-8fba-4537-8c67-31466787f732)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9c8df974-8fba-4537-8c67-31466787f732)

- <a id="bdqcore_6354376c-0cf2-435b-be40-850769c5a18a"></a>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE
  - Description: Measure if all VALIDATION_DATEIDENTIFIED_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6354376c-0cf2-435b-be40-850769c5a18a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6354376c-0cf2-435b-be40-850769c5a18a)

- <a id="bdqcore_563872eb-f544-45a0-8f91-8098d62768d4"></a>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD
  - Description: Measure if all VALIDATION_DATEIDENTIFIED_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:563872eb-f544-45a0-8f91-8098d62768d4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:563872eb-f544-45a0-8f91-8098d62768d4)

- <a id="bdqcore_85dc5d02-9847-420f-a026-6a0e70962d2a"></a>MULTIRECORD_MEASURE_QA_DAY_INRANGE
  - Description: Measure if all VALIDATION_DAY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:85dc5d02-9847-420f-a026-6a0e70962d2a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:85dc5d02-9847-420f-a026-6a0e70962d2a)

- <a id="bdqcore_371035f6-42b5-494f-86d9-de2f44a6cdc6"></a>MULTIRECORD_MEASURE_QA_DAY_STANDARD
  - Description: Measure if all VALIDATION_DAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:371035f6-42b5-494f-86d9-de2f44a6cdc6)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:371035f6-42b5-494f-86d9-de2f44a6cdc6)

- <a id="bdqcore_4d999a65-a431-4a76-b591-e0d86dcf244b"></a>MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY
  - Description: Measure if all VALIDATION_DCTYPE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4d999a65-a431-4a76-b591-e0d86dcf244b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4d999a65-a431-4a76-b591-e0d86dcf244b)

- <a id="bdqcore_d9493fa0-d90e-41db-95f6-d1c1d243540e"></a>MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD
  - Description: Measure if all VALIDATION_DCTYPE_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d9493fa0-d90e-41db-95f6-d1c1d243540e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d9493fa0-d90e-41db-95f6-d1c1d243540e)

- <a id="bdqcore_3c8bc478-f6b2-4533-b7ce-45bae5d186c2"></a>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE
  - Description: Measure if all VALIDATION_DECIMALLATITUDE_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3c8bc478-f6b2-4533-b7ce-45bae5d186c2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3c8bc478-f6b2-4533-b7ce-45bae5d186c2)

- <a id="bdqcore_a2535b23-4407-40bd-b23b-30c8185d72a2"></a>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY
  - Description: Measure if all VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a2535b23-4407-40bd-b23b-30c8185d72a2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a2535b23-4407-40bd-b23b-30c8185d72a2)

- <a id="bdqcore_6f7a9b82-7d34-4111-a2a6-9efe5221fa44"></a>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE
  - Description: Measure if all VALIDATION_DECIMALLONGITUDE_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6f7a9b82-7d34-4111-a2a6-9efe5221fa44)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6f7a9b82-7d34-4111-a2a6-9efe5221fa44)

- <a id="bdqcore_a94e986e-dbc8-4147-872d-5f2727945654"></a>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY
  - Description: Measure if all VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a94e986e-dbc8-4147-872d-5f2727945654)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a94e986e-dbc8-4147-872d-5f2727945654)

- <a id="bdqcore_ba953672-6526-4375-97e8-b4e9d1a7d3a0"></a>MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD
  - Description: Measure if all VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ba953672-6526-4375-97e8-b4e9d1a7d3a0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ba953672-6526-4375-97e8-b4e9d1a7d3a0)

- <a id="bdqcore_c04d428a-13d0-4766-9df7-4dfb2ef5d5d8"></a>MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE
  - Description: Measure if all VALIDATION_ENDDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c04d428a-13d0-4766-9df7-4dfb2ef5d5d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c04d428a-13d0-4766-9df7-4dfb2ef5d5d8)

- <a id="bdqcore_8dfed701-01a9-415d-a9f8-539280b75975"></a>MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD
  - Description: Measure if all VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8dfed701-01a9-415d-a9f8-539280b75975)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8dfed701-01a9-415d-a9f8-539280b75975)

- <a id="bdqcore_d41a731b-2e2b-4442-9217-4c375ae92926"></a>MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE
  - Description: Measure if all VALIDATION_EVENTDATE_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d41a731b-2e2b-4442-9217-4c375ae92926)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d41a731b-2e2b-4442-9217-4c375ae92926)

- <a id="bdqcore_c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365"></a>MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY
  - Description: Measure if all VALIDATION_EVENTDATE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365)

- <a id="bdqcore_14a1d51f-16ed-4148-9dc8-1e90157a9868"></a>MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD
  - Description: Measure if all VALIDATION_EVENTDATE_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:14a1d51f-16ed-4148-9dc8-1e90157a9868)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:14a1d51f-16ed-4148-9dc8-1e90157a9868)

- <a id="bdqcore_4cf4fe57-6736-443b-afda-f7ce8ce25471"></a>MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY
  - Description: Measure if all VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4cf4fe57-6736-443b-afda-f7ce8ce25471)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4cf4fe57-6736-443b-afda-f7ce8ce25471)

- <a id="bdqcore_f375a3fd-4cf5-4ef4-955e-d71762ede2d8"></a>MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT
  - Description: Measure if all VALIDATION_EVENT_CONSISTENT in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f375a3fd-4cf5-4ef4-955e-d71762ede2d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f375a3fd-4cf5-4ef4-955e-d71762ede2d8)

- <a id="bdqcore_a07d7147-2db8-48ce-81b8-e47595ad5f17"></a>MULTIRECORD_MEASURE_QA_FAMILY_FOUND
  - Description: Measure if all VALIDATION_FAMILY_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a07d7147-2db8-48ce-81b8-e47595ad5f17)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a07d7147-2db8-48ce-81b8-e47595ad5f17)

- <a id="bdqcore_c5c8db83-3af0-4215-806f-e2f90574b138"></a>MULTIRECORD_MEASURE_QA_GENUS_FOUND
  - Description: Measure if all VALIDATION_GENUS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c5c8db83-3af0-4215-806f-e2f90574b138)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c5c8db83-3af0-4215-806f-e2f90574b138)

- <a id="bdqcore_488c1dff-21ec-4e68-a00a-7355505e180c"></a>MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY
  - Description: Measure if all VALIDATION_GEODETICDATUM_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:488c1dff-21ec-4e68-a00a-7355505e180c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:488c1dff-21ec-4e68-a00a-7355505e180c)

- <a id="bdqcore_cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e"></a>MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD
  - Description: Measure if all VALIDATION_GEODETICDATUM_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e)

- <a id="bdqcore_465d7ac1-d193-46c0-a302-56a9ef99215f"></a>MULTIRECORD_MEASURE_QA_KINGDOM_FOUND
  - Description: Measure if all VALIDATION_KINGDOM_FOUND in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:465d7ac1-d193-46c0-a302-56a9ef99215f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:465d7ac1-d193-46c0-a302-56a9ef99215f)

- <a id="bdqcore_3bc9df8b-0f57-4157-9374-b56a99090b22"></a>MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY
  - Description: Measure if all VALIDATION_KINGDOM_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3bc9df8b-0f57-4157-9374-b56a99090b22)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3bc9df8b-0f57-4157-9374-b56a99090b22)

- <a id="bdqcore_4fccf163-9336-4f48-996c-57f5f66e72db"></a>MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY
  - Description: Measure if all VALIDATION_LICENSE_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4fccf163-9336-4f48-996c-57f5f66e72db)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4fccf163-9336-4f48-996c-57f5f66e72db)

- <a id="bdqcore_acd8d43e-7a2a-4372-b887-fb53a9972dc9"></a>MULTIRECORD_MEASURE_QA_LICENSE_STANDARD
  - Description: Measure if all VALIDATION_LICENSE_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:acd8d43e-7a2a-4372-b887-fb53a9972dc9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:acd8d43e-7a2a-4372-b887-fb53a9972dc9)

- <a id="bdqcore_3b2e4791-1a5a-4087-9e8d-09c67cf8c816"></a>MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY
  - Description: Measure if all VALIDATION_LOCATION_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3b2e4791-1a5a-4087-9e8d-09c67cf8c816)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3b2e4791-1a5a-4087-9e8d-09c67cf8c816)

- <a id="bdqcore_c73d49d1-06e4-4272-8249-6a26e7f8abca"></a>MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE
  - Description: Measure if all VALIDATION_MAXDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c73d49d1-06e4-4272-8249-6a26e7f8abca)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c73d49d1-06e4-4272-8249-6a26e7f8abca)

- <a id="bdqcore_7c5a6ba0-399d-4570-878a-4a064e2406fe"></a>MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE
  - Description: Measure if all VALIDATION_MAXELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7c5a6ba0-399d-4570-878a-4a064e2406fe)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7c5a6ba0-399d-4570-878a-4a064e2406fe)

- <a id="bdqcore_49d756a8-e654-4267-a290-d1def5d2c5f9"></a>MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE
  - Description: Measure if all VALIDATION_MINDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49d756a8-e654-4267-a290-d1def5d2c5f9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49d756a8-e654-4267-a290-d1def5d2c5f9)

- <a id="bdqcore_fcabd2c9-392c-4841-a5d7-e2680c9587ab"></a>MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH
  - Description: Measure if all VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:fcabd2c9-392c-4841-a5d7-e2680c9587ab)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:fcabd2c9-392c-4841-a5d7-e2680c9587ab)

- <a id="bdqcore_1ba18c8b-66a6-47d9-a709-404439332dba"></a>MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE
  - Description: Measure if all VALIDATION_MINELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1ba18c8b-66a6-47d9-a709-404439332dba)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1ba18c8b-66a6-47d9-a709-404439332dba)

- <a id="bdqcore_44f00697-ca66-43cf-8f16-646b40c0f514"></a>MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION
  - Description: Measure if all VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:44f00697-ca66-43cf-8f16-646b40c0f514)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:44f00697-ca66-43cf-8f16-646b40c0f514)

- <a id="bdqcore_b3c2bb86-e239-4532-ae0c-b121ec1ee025"></a>MULTIRECORD_MEASURE_QA_MONTH_STANDARD
  - Description: Measure if all VALIDATION_MONTH_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b3c2bb86-e239-4532-ae0c-b121ec1ee025)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b3c2bb86-e239-4532-ae0c-b121ec1ee025)

- <a id="bdqcore_16059801-6adb-4e65-82f4-61eaa70d8df0"></a>MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY
  - Description: Measure if all VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:16059801-6adb-4e65-82f4-61eaa70d8df0)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:16059801-6adb-4e65-82f4-61eaa70d8df0)

- <a id="bdqcore_0028ef9a-6553-467b-a344-90327ed2babf"></a>MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY
  - Description: Measure if all VALIDATION_OCCURRENCEID_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0028ef9a-6553-467b-a344-90327ed2babf)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0028ef9a-6553-467b-a344-90327ed2babf)

- <a id="bdqcore_d2922585-2070-4851-a033-15e51977f9dc"></a>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY
  - Description: Measure if all VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d2922585-2070-4851-a033-15e51977f9dc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d2922585-2070-4851-a033-15e51977f9dc)

- <a id="bdqcore_2fea4571-92d0-48a5-a5ba-6caecd647862"></a>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD
  - Description: Measure if all VALIDATION_OCCURRENCESTATUS_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2fea4571-92d0-48a5-a5ba-6caecd647862)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2fea4571-92d0-48a5-a5ba-6caecd647862)

- <a id="bdqcore_773bb288-fef3-4968-a65a-a69c74d6ecb5"></a>MULTIRECORD_MEASURE_QA_ORDER_FOUND
  - Description: Measure if all VALIDATION_ORDER_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:773bb288-fef3-4968-a65a-a69c74d6ecb5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:773bb288-fef3-4968-a65a-a69c74d6ecb5)

- <a id="bdqcore_ef31ba02-cea7-4d76-990f-99ebbd201fb4"></a>MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD
  - Description: Measure if all VALIDATION_PATHWAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ef31ba02-cea7-4d76-990f-99ebbd201fb4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ef31ba02-cea7-4d76-990f-99ebbd201fb4)

- <a id="bdqcore_17364d16-37b7-4ccb-9614-bfb95ff1bca9"></a>MULTIRECORD_MEASURE_QA_PHYLUM_FOUND
  - Description: Measure if all VALIDATION_PHYLUM_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:17364d16-37b7-4ccb-9614-bfb95ff1bca9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:17364d16-37b7-4ccb-9614-bfb95ff1bca9)

- <a id="bdqcore_ef05b45b-13b8-4877-9e9d-fa44b332d83c"></a>MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT
  - Description: Measure if all VALIDATION_POLYNOMIAL_CONSISTENT in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ef05b45b-13b8-4877-9e9d-fa44b332d83c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ef05b45b-13b8-4877-9e9d-fa44b332d83c)

- <a id="bdqcore_6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
  - Description: Measure if all VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7)

- <a id="bdqcore_a9529e71-5470-4cb1-b04d-aa483926f532"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE
  - Description: Measure if all VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a9529e71-5470-4cb1-b04d-aa483926f532)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a9529e71-5470-4cb1-b04d-aa483926f532)

- <a id="bdqcore_4cf84216-c8a7-4865-a8e1-3ffd829d5a10"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY
  - Description: Measure if all VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4cf84216-c8a7-4865-a8e1-3ffd829d5a10)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4cf84216-c8a7-4865-a8e1-3ffd829d5a10)

- <a id="bdqcore_a8aee02c-cf7c-4104-a601-d8afc4f9cbe2"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND
  - Description: Measure if all VALIDATION_SCIENTIFICNAME_FOUND in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a8aee02c-cf7c-4104-a601-d8afc4f9cbe2)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a8aee02c-cf7c-4104-a601-d8afc4f9cbe2)

- <a id="bdqcore_b4d6a61c-64ff-4da0-974c-63a73fd20836"></a>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY
  - Description: Measure if all VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b4d6a61c-64ff-4da0-974c-63a73fd20836)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b4d6a61c-64ff-4da0-974c-63a73fd20836)

- <a id="bdqcore_1b3bbac4-7c00-46d6-8179-1d57c92374ad"></a>MULTIRECORD_MEASURE_QA_SEX_STANDARD
  - Description: Measure if all VALIDATION_SEX_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1b3bbac4-7c00-46d6-8179-1d57c92374ad)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1b3bbac4-7c00-46d6-8179-1d57c92374ad)

- <a id="bdqcore_8c217eee-9cd0-48c3-aea0-90151c6c5bfd"></a>MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE
  - Description: Measure if all VALIDATION_STARTDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8c217eee-9cd0-48c3-aea0-90151c6c5bfd)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8c217eee-9cd0-48c3-aea0-90151c6c5bfd)

- <a id="bdqcore_9c1cdf6a-0dbf-4828-a2e3-fb368f74d194"></a>MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND
  - Description: Measure if all VALIDATION_STATEPROVINCE_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9c1cdf6a-0dbf-4828-a2e3-fb368f74d194)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9c1cdf6a-0dbf-4828-a2e3-fb368f74d194)

- <a id="bdqcore_e0b8cff1-3322-40d2-b8b2-b99fc9ae130a"></a>MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY
  - Description: Measure if all VALIDATION_TAXONRANK_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:e0b8cff1-3322-40d2-b8b2-b99fc9ae130a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:e0b8cff1-3322-40d2-b8b2-b99fc9ae130a)

- <a id="bdqcore_f320ca83-8487-4011-b1ff-f4b1b4dd86ec"></a>MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD
  - Description: Measure if all VALIDATION_TAXONRANK_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f320ca83-8487-4011-b1ff-f4b1b4dd86ec)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f320ca83-8487-4011-b1ff-f4b1b4dd86ec)

- <a id="bdqcore_2a9d4cfd-815a-46e0-bb51-60724582b762"></a>MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY
  - Description: Measure if all VALIDATION_TAXON_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2a9d4cfd-815a-46e0-bb51-60724582b762)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2a9d4cfd-815a-46e0-bb51-60724582b762)

- <a id="bdqcore_0df03601-3768-4805-906a-bbd0a41b0fda"></a>MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS
  - Description: Measure if all VALIDATION_TAXON_UNAMBIGUOUS in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0df03601-3768-4805-906a-bbd0a41b0fda)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0df03601-3768-4805-906a-bbd0a41b0fda)

- <a id="bdqcore_1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88"></a>MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD
  - Description: Measure if all VALIDATION_TYPESTATUS_STANDARD in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88)

- <a id="bdqcore_a0502c5f-608b-4e59-99da-d9490bb4d93b"></a>MULTIRECORD_MEASURE_QA_YEAR_INRANGE
  - Description: Measure if all VALIDATION_YEAR_INRANGE in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a0502c5f-608b-4e59-99da-d9490bb4d93b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a0502c5f-608b-4e59-99da-d9490bb4d93b)

- <a id="bdqcore_a8fef8a8-e7c7-4a2d-adaf-7da99c896c93"></a>MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY
  - Description: Measure if all VALIDATION_YEAR_NOTEMPTY in a record set are COMPLIANT
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:a8fef8a8-e7c7-4a2d-adaf-7da99c896c93)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:a8fef8a8-e7c7-4a2d-adaf-7da99c896c93)

- <a id="bdqcore_ac2b7648-d5f9-48ca-9b07-8ad5879a2536"></a>VALIDATION_BASISOFRECORD_NOTEMPTY
  - Description: Is there a value in dwc:basisOfRecord?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ac2b7648-d5f9-48ca-9b07-8ad5879a2536)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ac2b7648-d5f9-48ca-9b07-8ad5879a2536)

- <a id="bdqcore_42408a00-bf71-4892-a399-4325e2bc1fb8"></a>VALIDATION_BASISOFRECORD_STANDARD
  - Description: Does the value of dwc:basisOfRecord occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:42408a00-bf71-4892-a399-4325e2bc1fb8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:42408a00-bf71-4892-a399-4325e2bc1fb8)

- <a id="bdqcore_2750c040-1d4a-4149-99fe-0512785f2d5f"></a>VALIDATION_CLASSIFICATION_CONSISTENT
  - Description: Is the combination of higher classification taxonomic terms consistent using bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2750c040-1d4a-4149-99fe-0512785f2d5f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2750c040-1d4a-4149-99fe-0512785f2d5f)

- <a id="bdqcore_2cd6884e-3d14-4476-94f7-1191cfff309b"></a>VALIDATION_CLASS_FOUND
  - Description: Does the value of dwc:class occur at rank of Class in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:2cd6884e-3d14-4476-94f7-1191cfff309b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:2cd6884e-3d14-4476-94f7-1191cfff309b)

- <a id="bdqcore_adb27d29-9f0d-4d52-b760-a77ba57a69c9"></a>VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT
  - Description: Do the geographic coordinates fall on or within the boundaries of the territory given in dwc:countryCode or its Exclusive Economic Zone?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:adb27d29-9f0d-4d52-b760-a77ba57a69c9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:adb27d29-9f0d-4d52-b760-a77ba57a69c9)

- <a id="bdqcore_f18a470b-3fe1-4aae-9c65-a6d3db6b550c"></a>VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT
  - Description: Do the geographic coordinates fall on or within the boundary from the bdq:sourceAuthority for the given dwc:stateProvince or within the distance given by bdq:spatialBufferInMeters outside that boundary?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f18a470b-3fe1-4aae-9c65-a6d3db6b550c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f18a470b-3fe1-4aae-9c65-a6d3db6b550c)

- <a id="bdqcore_b9c184ce-a859-410c-9d12-71a338200380"></a>VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT
  - Description: Does the marine/non-marine biome of a taxon from the bdq:sourceAuthority match the biome at the location given by the coordinates?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b9c184ce-a859-410c-9d12-71a338200380)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b9c184ce-a859-410c-9d12-71a338200380)

- <a id="bdqcore_1bf0e210-6792-4128-b8cc-ab6828aa4871"></a>VALIDATION_COORDINATES_NOTZERO
  - Description: Are the values of either dwc:decimalLatitude or dwc:decimalLongitude numbers that are not equal to 0?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:1bf0e210-6792-4128-b8cc-ab6828aa4871)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:1bf0e210-6792-4128-b8cc-ab6828aa4871)

- <a id="bdqcore_c6adf2ea-3051-4498-97f4-4b2f8a105f57"></a>VALIDATION_COORDINATEUNCERTAINTY_INRANGE
  - Description: Is the value of dwc:coordinateUncertaintyInMeters a number between 1 and 20,037,509?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c6adf2ea-3051-4498-97f4-4b2f8a105f57)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c6adf2ea-3051-4498-97f4-4b2f8a105f57)

- <a id="bdqcore_853b79a2-b314-44a2-ae46-34a1e7ed85e4"></a>VALIDATION_COUNTRYCODE_NOTEMPTY
  - Description: Is there a value in dwc:countryCode?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:853b79a2-b314-44a2-ae46-34a1e7ed85e4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:853b79a2-b314-44a2-ae46-34a1e7ed85e4)

- <a id="bdqcore_0493bcfb-652e-4d17-815b-b0cce0742fbe"></a>VALIDATION_COUNTRYCODE_STANDARD
  - Description: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0493bcfb-652e-4d17-815b-b0cce0742fbe)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0493bcfb-652e-4d17-815b-b0cce0742fbe)

- <a id="bdqcore_b23110e7-1be7-444a-a677-cdee0cf4330c"></a>VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT
  - Description: Does the ISO country code, determined from the value of dwc:country, equal the value of dwc:countryCode?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b23110e7-1be7-444a-a677-cdee0cf4330c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b23110e7-1be7-444a-a677-cdee0cf4330c)

- <a id="bdqcore_d257eb98-27cb-48e5-8d3c-ab9fca4edd11"></a>VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS
  - Description: Is the combination of the values of the terms dwc:country, dwc:stateProvince unique in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d257eb98-27cb-48e5-8d3c-ab9fca4edd11)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d257eb98-27cb-48e5-8d3c-ab9fca4edd11)

- <a id="bdqcore_69b2efdc-6269-45a4-aecb-4cb99c2ae134"></a>VALIDATION_COUNTRY_FOUND
  - Description: Does the value of dwc:country occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:69b2efdc-6269-45a4-aecb-4cb99c2ae134)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:69b2efdc-6269-45a4-aecb-4cb99c2ae134)

- <a id="bdqcore_6ce2b2b4-6afe-4d13-82a0-390d31ade01c"></a>VALIDATION_COUNTRY_NOTEMPTY
  - Description: Is there a value in dwc:country?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6ce2b2b4-6afe-4d13-82a0-390d31ade01c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6ce2b2b4-6afe-4d13-82a0-390d31ade01c)

- <a id="bdqcore_dc8aae4b-134f-4d75-8a71-c4186239178e"></a>VALIDATION_DATEIDENTIFIED_INRANGE
  - Description: Is the value of dwc:dateIdentified within Parameter ranges and either overlap or is later than dwc:eventDate?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:dc8aae4b-134f-4d75-8a71-c4186239178e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:dc8aae4b-134f-4d75-8a71-c4186239178e)

- <a id="bdqcore_66269bdd-9271-4e76-b25c-7ab81eebe1d8"></a>VALIDATION_DATEIDENTIFIED_STANDARD
  - Description: Is the value of dwc:dateIdentified a valid ISO date?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:66269bdd-9271-4e76-b25c-7ab81eebe1d8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:66269bdd-9271-4e76-b25c-7ab81eebe1d8)

- <a id="bdqcore_8d787cb5-73e2-4c39-9cd1-67c7361dc02e"></a>VALIDATION_DAY_INRANGE
  - Description: Is the value of dwc:day interpretable as a valid integer between 1 and 28 inclusive or 29, 30 or 31 given the relative month and year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8d787cb5-73e2-4c39-9cd1-67c7361dc02e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8d787cb5-73e2-4c39-9cd1-67c7361dc02e)

- <a id="bdqcore_47ff73ba-0028-4f79-9ce1-ee7008d66498"></a>VALIDATION_DAY_STANDARD
  - Description: Is the value of dwc:day an integer between 1 and 31 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:47ff73ba-0028-4f79-9ce1-ee7008d66498)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:47ff73ba-0028-4f79-9ce1-ee7008d66498)

- <a id="bdqcore_374b091a-fc90-4791-91e5-c1557c649169"></a>VALIDATION_DCTYPE_NOTEMPTY
  - Description: Is there a value in dc:type?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:374b091a-fc90-4791-91e5-c1557c649169)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:374b091a-fc90-4791-91e5-c1557c649169)

- <a id="bdqcore_cdaabb0d-a863-49d0-bc0f-738d771acba5"></a>VALIDATION_DCTYPE_STANDARD
  - Description: Does the value in dc:type occur as a value in the DCMI type vocabulary?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:cdaabb0d-a863-49d0-bc0f-738d771acba5)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:cdaabb0d-a863-49d0-bc0f-738d771acba5)

- <a id="bdqcore_b6ecda2a-ce36-437a-b515-3ae94948fe83"></a>VALIDATION_DECIMALLATITUDE_INRANGE
  - Description: Is the value of dwc:decimalLatitude a number between -90 and 90 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:b6ecda2a-ce36-437a-b515-3ae94948fe83)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:b6ecda2a-ce36-437a-b515-3ae94948fe83)

- <a id="bdqcore_7d2485d5-1ba7-4f25-90cb-f4480ff1a275"></a>VALIDATION_DECIMALLATITUDE_NOTEMPTY
  - Description: Is there a value in dwc:decimalLatitude?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7d2485d5-1ba7-4f25-90cb-f4480ff1a275)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7d2485d5-1ba7-4f25-90cb-f4480ff1a275)

- <a id="bdqcore_0949110d-c06b-450e-9649-7c1374d940d1"></a>VALIDATION_DECIMALLONGITUDE_INRANGE
  - Description: Is the value of dwc:decimalLongitude a number between -180 and 180 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0949110d-c06b-450e-9649-7c1374d940d1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0949110d-c06b-450e-9649-7c1374d940d1)

- <a id="bdqcore_9beb9442-d942-4f42-8b6a-fcea01ee086a"></a>VALIDATION_DECIMALLONGITUDE_NOTEMPTY
  - Description: Is there a value in dwc:decimalLongitude?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9beb9442-d942-4f42-8b6a-fcea01ee086a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9beb9442-d942-4f42-8b6a-fcea01ee086a)

- <a id="bdqcore_060e7734-607d-4737-8b2c-bfa17788bf1a"></a>VALIDATION_DEGREEOFESTABLISHMENT_STANDARD
  - Description: Does the value of dwc:degreeOfEstablishment occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:060e7734-607d-4737-8b2c-bfa17788bf1a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:060e7734-607d-4737-8b2c-bfa17788bf1a)

- <a id="bdqcore_9a39d88c-7eee-46df-b32a-c109f9f81fb8"></a>VALIDATION_ENDDAYOFYEAR_INRANGE
  - Description: Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:9a39d88c-7eee-46df-b32a-c109f9f81fb8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:9a39d88c-7eee-46df-b32a-c109f9f81fb8)

- <a id="bdqcore_4eb48fdf-7299-4d63-9d08-246902e2857f"></a>VALIDATION_ESTABLISHMENTMEANS_STANDARD
  - Description: Does the value of dwc:establishmentMeans occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4eb48fdf-7299-4d63-9d08-246902e2857f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4eb48fdf-7299-4d63-9d08-246902e2857f)

- <a id="bdqcore_3cff4dc4-72e9-4abe-9bf3-8a30f1618432"></a>VALIDATION_EVENTDATE_INRANGE
  - Description: Is the value of dwc:eventDate entirely with the Parameter Range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3cff4dc4-72e9-4abe-9bf3-8a30f1618432)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3cff4dc4-72e9-4abe-9bf3-8a30f1618432)

- <a id="bdqcore_f51e15a6-a67d-4729-9c28-3766299d2985"></a>VALIDATION_EVENTDATE_NOTEMPTY
  - Description: Is there a value in dwc:eventDate?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f51e15a6-a67d-4729-9c28-3766299d2985)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f51e15a6-a67d-4729-9c28-3766299d2985)

- <a id="bdqcore_4f2bf8fd-fc5c-493f-a44c-e7b16153c803"></a>VALIDATION_EVENTDATE_STANDARD
  - Description: Is the value of dwc:eventDate a valid ISO date?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4f2bf8fd-fc5c-493f-a44c-e7b16153c803)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4f2bf8fd-fc5c-493f-a44c-e7b16153c803)

- <a id="bdqcore_41267642-60ff-4116-90eb-499fee2cd83f"></a>VALIDATION_EVENTTEMPORAL_NOTEMPTY
  - Description: Is there a value in any of the terms dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:41267642-60ff-4116-90eb-499fee2cd83f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:41267642-60ff-4116-90eb-499fee2cd83f)

- <a id="bdqcore_5618f083-d55a-4ac2-92b5-b9fb227b832f"></a>VALIDATION_EVENT_CONSISTENT
  - Description: Are the values in dwc:eventDate consistent with the values in dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:5618f083-d55a-4ac2-92b5-b9fb227b832f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:5618f083-d55a-4ac2-92b5-b9fb227b832f)

- <a id="bdqcore_3667556d-d8f5-454c-922b-af8af38f613c"></a>VALIDATION_FAMILY_FOUND
  - Description: Does the value of dwc:family occur at rank of Family in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3667556d-d8f5-454c-922b-af8af38f613c)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3667556d-d8f5-454c-922b-af8af38f613c)

- <a id="bdqcore_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec"></a>VALIDATION_GENUS_FOUND
  - Description: Does the value of dwc:genus occur at the rank of Genus in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:f2ce7d55-5b1d-426a-b00e-6d4efe3058ec)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:f2ce7d55-5b1d-426a-b00e-6d4efe3058ec)

- <a id="bdqcore_239ec40e-a729-4a8e-ba69-e0bf03ac1c44"></a>VALIDATION_GEODETICDATUM_NOTEMPTY
  - Description: Is there a value in dwc:geodeticDatum?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:239ec40e-a729-4a8e-ba69-e0bf03ac1c44)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:239ec40e-a729-4a8e-ba69-e0bf03ac1c44)

- <a id="bdqcore_7e0c0418-fe16-4a39-98bd-80e19d95b9d1"></a>VALIDATION_GEODETICDATUM_STANDARD
  - Description: Does the value of dwc:geodeticDatum occur as a valid geographic CRS, geodetic Datum or ellipsoid in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7e0c0418-fe16-4a39-98bd-80e19d95b9d1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7e0c0418-fe16-4a39-98bd-80e19d95b9d1)

- <a id="bdqcore_125b5493-052d-4a0d-a3e1-ed5bf792689e"></a>VALIDATION_KINGDOM_FOUND
  - Description: Does the value of dwc:kingdom occur at rank of Kingdom in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:125b5493-052d-4a0d-a3e1-ed5bf792689e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:125b5493-052d-4a0d-a3e1-ed5bf792689e)

- <a id="bdqcore_36ed36c9-b1a7-40b2-b5e2-0d012e772098"></a>VALIDATION_KINGDOM_NOTEMPTY
  - Description: Is there a value in dwc:kingdom?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:36ed36c9-b1a7-40b2-b5e2-0d012e772098)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:36ed36c9-b1a7-40b2-b5e2-0d012e772098)

- <a id="bdqcore_15f78619-811a-4c6f-997a-a4c7888ad849"></a>VALIDATION_LICENSE_NOTEMPTY
  - Description: Is there a value in dcterms:license?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:15f78619-811a-4c6f-997a-a4c7888ad849)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:15f78619-811a-4c6f-997a-a4c7888ad849)

- <a id="bdqcore_3136236e-04b6-49ea-8b34-a65f25e3aba1"></a>VALIDATION_LICENSE_STANDARD
  - Description: Does the value of dcterms:license occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3136236e-04b6-49ea-8b34-a65f25e3aba1)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3136236e-04b6-49ea-8b34-a65f25e3aba1)

- <a id="bdqcore_58486cb6-1114-4a8a-ba1e-bd89cfe887e9"></a>VALIDATION_LOCATION_NOTEMPTY
  - Description: Is there a value in any of the Darwin Core spatial terms that could specify a location?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:58486cb6-1114-4a8a-ba1e-bd89cfe887e9)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:58486cb6-1114-4a8a-ba1e-bd89cfe887e9)

- <a id="bdqcore_3f1db29a-bfa5-40db-9fd1-fde020d81939"></a>VALIDATION_MAXDEPTH_INRANGE
  - Description: Is the value of dwc:maximumDepthInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3f1db29a-bfa5-40db-9fd1-fde020d81939)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3f1db29a-bfa5-40db-9fd1-fde020d81939)

- <a id="bdqcore_c971fe3f-84c1-4636-9f44-b1ec31fd63c7"></a>VALIDATION_MAXELEVATION_INRANGE
  - Description: Is the value of dwc:maximumElevationInMeters of a single record within a valid range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c971fe3f-84c1-4636-9f44-b1ec31fd63c7)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c971fe3f-84c1-4636-9f44-b1ec31fd63c7)

- <a id="bdqcore_04b2c8f3-c71b-4e95-8e43-f70374c5fb92"></a>VALIDATION_MINDEPTH_INRANGE
  - Description: Is the value of dwc:minimumDepthInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:04b2c8f3-c71b-4e95-8e43-f70374c5fb92)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:04b2c8f3-c71b-4e95-8e43-f70374c5fb92)

- <a id="bdqcore_8f1e6e58-544b-4365-a569-fb781341644e"></a>VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH
  - Description: Is the value of dwc:minimumDepthInMeters a number that is less than or equal to the value of dwc:maximumDepthInMeters?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:8f1e6e58-544b-4365-a569-fb781341644e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:8f1e6e58-544b-4365-a569-fb781341644e)

- <a id="bdqcore_0bb8297d-8f8a-42d2-80c1-558f29efe798"></a>VALIDATION_MINELEVATION_INRANGE
  - Description: Is the value of dwc:minimumElevationInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:0bb8297d-8f8a-42d2-80c1-558f29efe798)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:0bb8297d-8f8a-42d2-80c1-558f29efe798)

- <a id="bdqcore_d708526b-6561-438e-aa1a-82cd80b06396"></a>VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION
  - Description: Is the value of dwc:minimumElevationInMeters a number less than or equal to the value of dwc:maximumElevationInMeters?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:d708526b-6561-438e-aa1a-82cd80b06396)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:d708526b-6561-438e-aa1a-82cd80b06396)

- <a id="bdqcore_01c6dafa-0886-4b7e-9881-2c3018c98bdc"></a>VALIDATION_MONTH_STANDARD
  - Description: Is the value of dwc:month interpretable as an integer between 1 and 12 inclusive?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:01c6dafa-0886-4b7e-9881-2c3018c98bdc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:01c6dafa-0886-4b7e-9881-2c3018c98bdc)

- <a id="bdqcore_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70"></a>VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY
  - Description: Is there a value in dwc:namePublishedInYear?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ff59f77d-71e9-4eb1-aac9-8bd05c50ff70)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ff59f77d-71e9-4eb1-aac9-8bd05c50ff70)

- <a id="bdqcore_c486546c-e6e5-48a7-b286-eba7f5ca56c4"></a>VALIDATION_OCCURRENCEID_NOTEMPTY
  - Description: Is there a value in dwc:occurrenceID?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c486546c-e6e5-48a7-b286-eba7f5ca56c4)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c486546c-e6e5-48a7-b286-eba7f5ca56c4)

- <a id="bdqcore_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf"></a>VALIDATION_OCCURRENCESTATUS_NOTEMPTY
  - Description: Is there a value in dwc:occurrenceStatus?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf)

- <a id="bdqcore_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47"></a>VALIDATION_OCCURRENCESTATUS_STANDARD
  - Description: Does the value of dwc:occurrenceStatus occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47)

- <a id="bdqcore_81cc974d-43cc-4c0f-a5e0-afa23b455aa3"></a>VALIDATION_ORDER_FOUND
  - Description: Does the value of dwc:order occur at rank of Order in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:81cc974d-43cc-4c0f-a5e0-afa23b455aa3)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:81cc974d-43cc-4c0f-a5e0-afa23b455aa3)

- <a id="bdqcore_5424e933-bee7-4125-839e-d8743ea69f93"></a>VALIDATION_PATHWAY_STANDARD
  - Description: Does the value of dwc:pathway occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:5424e933-bee7-4125-839e-d8743ea69f93)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:5424e933-bee7-4125-839e-d8743ea69f93)

- <a id="bdqcore_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f"></a>VALIDATION_PHYLUM_FOUND
  - Description: Does the value of dwc:phylum occur at rank of Phylum in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f)

- <a id="bdqcore_17f03f1f-f74d-40c0-8071-2927cfc9487b"></a>VALIDATION_POLYNOMIAL_CONSISTENT
  - Description: Is the polynomial represented in dwc:scientificName consistent with the equivalent values in dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:17f03f1f-f74d-40c0-8071-2927cfc9487b)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:17f03f1f-f74d-40c0-8071-2927cfc9487b)

- <a id="bdqcore_49f1d386-5bed-43ae-bd43-deabf7df64fc"></a>VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
  - Description: Is there a value in dwc:scientificNameAuthorship?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:49f1d386-5bed-43ae-bd43-deabf7df64fc)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:49f1d386-5bed-43ae-bd43-deabf7df64fc)

- <a id="bdqcore_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8"></a>VALIDATION_SCIENTIFICNAMEID_COMPLETE
  - Description: Does the value of dwc:scientificNameID contain a complete identifier?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:6eeac3ed-f691-457f-a42e-eaa9c8a71ce8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:6eeac3ed-f691-457f-a42e-eaa9c8a71ce8)

- <a id="bdqcore_401bf207-9a55-4dff-88a5-abcd58ad97fa"></a>VALIDATION_SCIENTIFICNAMEID_NOTEMPTY
  - Description: Is there a value in dwc:scientificNameID?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:401bf207-9a55-4dff-88a5-abcd58ad97fa)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:401bf207-9a55-4dff-88a5-abcd58ad97fa)

- <a id="bdqcore_3f335517-f442-4b98-b149-1e87ff16de45"></a>VALIDATION_SCIENTIFICNAME_FOUND
  - Description: Is there a match of the contents of dwc:scientificName with the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:3f335517-f442-4b98-b149-1e87ff16de45)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:3f335517-f442-4b98-b149-1e87ff16de45)

- <a id="bdqcore_7c4b9498-a8d9-4ebb-85f1-9f200c788595"></a>VALIDATION_SCIENTIFICNAME_NOTEMPTY
  - Description: Is there a value in dwc:scientificName?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7c4b9498-a8d9-4ebb-85f1-9f200c788595)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7c4b9498-a8d9-4ebb-85f1-9f200c788595)

- <a id="bdqcore_88d8598b-3318-483d-9475-a5acf9887404"></a>VALIDATION_SEX_STANDARD
  - Description: Does the value of dwc:sex occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:88d8598b-3318-483d-9475-a5acf9887404)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:88d8598b-3318-483d-9475-a5acf9887404)

- <a id="bdqcore_85803c7e-2a5a-42e1-b8d3-299a44cafc46"></a>VALIDATION_STARTDAYOFYEAR_INRANGE
  - Description: Is the value of dwc:startDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:85803c7e-2a5a-42e1-b8d3-299a44cafc46)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:85803c7e-2a5a-42e1-b8d3-299a44cafc46)

- <a id="bdqcore_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a"></a>VALIDATION_STATEPROVINCE_FOUND
  - Description: Does the value of dwc:stateProvince occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4daa7986-d9b0-4dd5-ad17-2d7a771ea71a)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4daa7986-d9b0-4dd5-ad17-2d7a771ea71a)

- <a id="bdqcore_14da5b87-8304-4b2b-911d-117e3c29e890"></a>VALIDATION_TAXONRANK_NOTEMPTY
  - Description: Is there a value in dwc:taxonRank?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:14da5b87-8304-4b2b-911d-117e3c29e890)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:14da5b87-8304-4b2b-911d-117e3c29e890)

- <a id="bdqcore_7bdb13a4-8a51-4ee5-be7f-20693fdb183e"></a>VALIDATION_TAXONRANK_STANDARD
  - Description: Does the value of dwc:taxonRank occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:7bdb13a4-8a51-4ee5-be7f-20693fdb183e)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:7bdb13a4-8a51-4ee5-be7f-20693fdb183e)

- <a id="bdqcore_06851339-843f-4a43-8422-4e61b9a00e75"></a>VALIDATION_TAXON_NOTEMPTY
  - Description: Is there a value in any of the terms needed to determine that the taxon exists?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:06851339-843f-4a43-8422-4e61b9a00e75)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:06851339-843f-4a43-8422-4e61b9a00e75)

- <a id="bdqcore_4c09f127-737b-4686-82a0-7c8e30841590"></a>VALIDATION_TAXON_UNAMBIGUOUS
  - Description: Can the taxon be unambiguously resolved from bdq:sourceAuthority using the available taxon terms?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4c09f127-737b-4686-82a0-7c8e30841590)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4c09f127-737b-4686-82a0-7c8e30841590)

- <a id="bdqcore_4833a522-12eb-4fe0-b4cf-7f7a337a6048"></a>VALIDATION_TYPESTATUS_STANDARD
  - Description: Does the value of dwc:typeStatus occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:4833a522-12eb-4fe0-b4cf-7f7a337a6048)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:4833a522-12eb-4fe0-b4cf-7f7a337a6048)

- <a id="bdqcore_ad0c8855-de69-4843-a80c-a5387d20fbc8"></a>VALIDATION_YEAR_INRANGE
  - Description: Is the value of dwc:year within the Parameter range?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:ad0c8855-de69-4843-a80c-a5387d20fbc8)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:ad0c8855-de69-4843-a80c-a5387d20fbc8)

- <a id="bdqcore_c09ecbf9-34e3-4f3e-b74a-8796af15e59f"></a>VALIDATION_YEAR_NOTEMPTY
  - Description: Is there a value in dwc:year?
  - View in Quick Reference Guide: [Link](../guide/bdqcore/index.md#bdqcore:c09ecbf9-34e3-4f3e-b74a-8796af15e59f)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore:c09ecbf9-34e3-4f3e-b74a-8796af15e59f)

### 5 Example RDF (non-normative) 

A more complete description of the tests can be found in the RDF representation of this vocabulary.

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

    <rdf:Description rdf:about="https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Validation"/>
    	<skos:prefLabel rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</skos:prefLabel>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord</rdfs:label>
    	<hasActedUponInformationElement xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="urn:uuid:c3620a97-65d6-4f9c-8a03-32e0d240a423"/>
    	<hasCriterion xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqcrit:Standard"/>
    	<hasDataQualityDimension xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqdim:Conformance"/>
    	<hasResourceType xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqffdq:SingleRecord"/>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</rdfs:comment>
    	<skos:historyNote rdf:datatype="http://www.w3.org/2001/XMLSchema#string">https://github.com/tdwg/bdq/issues/20</skos:historyNote>
    	<skos:note rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and suitable for a marker for the high seas.  Also available in the ISO user defined codes is ZZ, used by GBIF to mark unknown countries.  This test should accept both XZ and ZZ as COMPLIANT country codes. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</skos:note>
    	<dcterms:bibliographicCitation rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html; ISO (n.dat) 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2; DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list; Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</dcterms:bibliographicCitation>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:c3620a97-65d6-4f9c-8a03-32e0d240a423">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/ActedUpon"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Information Element ActedUpon dwc:countryCode</rdfs:label>
    	<composedOf xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="http://rs.tdwg.org/dwc/terms/countryCode"/>
    	<prefLabel xmlns="skos:" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Information Element ActedUpon dwc:countryCode</prefLabel>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:02f5a440-a473-42cf-a3f1-6c10334d5eb8">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/ValidationMethod"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ValidationMethod: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<skos:prefLabel rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ValidationMethod: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYCODE_STANDARD</skos:prefLabel>
    	<forValidation xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
    	<hasSpecification xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047"/>
    </rdf:Description>

    <rdf:Description rdf:about="urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Specification"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Specification for: VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</rdfs:comment>
    	<skos:example rdf:datatype="http://www.w3.org/2001/XMLSchema#string">dwc:countryCode="GL": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value"</skos:example>
    	<skos:example rdf:datatype="http://www.w3.org/2001/XMLSchema#string">dwc:countryCode="GRL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value"</skos:example>
    	<hasAuthoritiesDefaults xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</hasAuthoritiesDefaults>
    	<hasExpectedResponse xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</hasExpectedResponse>
    </rdf:Description>

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core Tests and Assertions Landing Page. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


