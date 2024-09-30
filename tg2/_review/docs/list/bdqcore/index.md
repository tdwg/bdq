<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
# BDQ Core Tests and Assertions List of Terms

Title
: BDQ Core Tests and Assertions List of Terms

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Preferred namespace abbreviation
: bdqcore

This version
: <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

Latest version
: <http://rs.tdwg.org/bdqcore/terms/>

Abstract
: This document is a reference for the (Draft) BDQ Core Standard, documenting the tests in the bdqcore: vocabulary, using terms from the bdqffdq ontology.

Contributors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028)), [Yi-Ming Gan](https://orcid.org/0000-0001-7087-2646) ([Royal Belgian Institute of Natural Sciences](http://www.wikidata.org/entity/Q16665660)), [António Mauro Saraiva](https://orcid.org/0000-0003-2283-1123) ([Universidade de São Paulo](https://www.wikidata.org/wiki/Q835960)), [Alan Koch Veiga](http://orcid.org/0000-0003-2672-8115) (Universidade de São Paulo), [Paula F Zermoglio](https://orcid.org/0000-0002-6056-5084) ([Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN): San Carlos de Bariloche](https://www.irnad.com/)), [Alexander Thompson](https://orcid.org/0000-0002-8981-4048) ([Google](https://www.wikidata.org/wiki/Q95)), David Lowery 

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core Tests and Assertions List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

Draft Standard for Submission

# Table of Contents 
{toc}

## 1 Introduction

This document lists the BDQ Core tests. The document includes terms in several namespaces that contain the recommended terms: `bdq:`, `bdqffdq:`, `bdqdim:`, bdqenh:, and bdqcrit as well as the focus of this document the `bdqcore` terms. For details and rationale, see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889.

<!--- start of information that probably goes in the users or implementers guides --->
### 1.1 Introductory

[!--- suggest "Single record (bdqffdq:SingleRecord) tests apply to a single observation or event structured under Darwin Core terms (Wieczorek et al 2012). The one exception to this is the test ISSUE_ANNOTATION_NOTEMPTY where this standard encourages the implementation of a standard for annotating occurrence records supported by Darwin Core. Multi record (bdqffdq:MultiRecord) tests sum up results across all records for each single record test."   AC - PAUL to check?  ---]

Tests may require reference to external data such as standard vocabularies of terms or names. While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

(Make sure to establish that the standard does not specify the "format" of the responses (JSON within an Annotation, etc.), but it does specify the required content regardless of serialization format.)

(Make sure this is addressed in this document) We acknowledge the centrality of the work of the TDWG Annotations Interest Group (https://github.com/tdwg/annotations) as to how the test results are reported against records. Test results structured with these three components can be readily wrapped in the body annotation document that follows the W3C Web Annotation Data Model (Sanderson et al. 2017), along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.

### 1.1 Characteristics of the tests (non-normative)

Each test is defined as a SingleRecord test. No CORE tests have been defined to use data in other records within a data set to evaluate the quality of data in a SingleRecord. The framework allows for MultiRecord tests able to identify outliers within a data set, or other tests that look across a MultiRecord to evaluate data quality, but we have not specified any such tests here.

The scope of each test is also largely provided by the bdqffdq:Specification. The Darwin Core terms used in the Specification are included in the "Information Elements". The "Specification" also includes references to external (to the Darwin Core standard) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource required for the implementation of the test.

The tests are agnostic about the form in which the data are stored or transported. The test specifications all assume that data are presented to the tests in structured form such as csv or tab delimited text files, with data elements identifiable as Darwin Core terms (Wieczorek et al. 2012). Here, cells contain non-typed data values possibly aggregated from and serialized from multiple sources such as relational databases where Boolean nulls and non-string data types may exist, but the data have been exported into a string serialization that supports neither null nor typed data. 

The tests are also agnostic about uses for quality assurance, where output data are limited to those for which all Validations are Compliant, or for quality control where the results of Validations, Issues, Measures, and Amendments can be used to improve the quality of the data.

The test specifications are agnostic about where in the biodiversity data lifecycle they are used. Implementers can incorporate the tests at any stage to help identify and correct issues. The tests can be applied during data capture in the field, transcription from paper records, data ingestion into databases, integration with collections management systems, data aggregation, and research on aggregated biodiversity data. They are designed to run at any point in the data lifecycle, from initial collection or observation to data transcription, database loading, and preparation for or during data aggregation. [However, the framing of the InformationElements as Darwin Core terms with the CORE Use Case focused on the research needs of downstream users means that competing requirements have led to some different decisions than would have been made if the aim was to solely evaluate data in a database of records and preparing it for aggregation.]   

### 1.2 Structure of Response (normative)

Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags,  The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary (consisting of exactly COMPLIANT or NOT_COMPLIANT) for validations or Issues (NOT_ISSUE, POTENTIAL_ISSUE, ISSUE), either a numeric value or a controlled vocabulary (consisting of exactly COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments. 
2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 
3. Remark supplies human-readable text describing reasons for the test result output.

### 1.3 Types of tests (non-normative)

[!---check out the wording Paul put in the BDQ_Core_Users_Guide.md - that is nice and simple wording---AC]

The concept of 'tests' in the context of this standard include four distinct types: VALIDATION; ISSUE; AMENDMENT and MEASURE.


#### 1.3.1 Validation 

A VALIDATION evaluates the values in one or more Darwin Core terms for fitness for some particular narrow data quality need within CORE. Validations evaluate values or in some cases, presence or lack of a value. Validation tests are phrased as positive statements, consistent with the "Fitness for Use Framework".  A Validation tests to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY, is phrased as "Not Empty", and will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem. The formal response of VALIDATIONs can take one of four forms:

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation.
4. A Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 


#### 1.3.2 Issue

ISSUE is a form of warning flag where the test is drawing attention to a non-empty value of a Darwin Core term. We have used these for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of this case would take human review. For example, ISSUE_ANNOTATION_NOTEMPTY is informing the tester than there is at least one annotation associated with record and this should be evaluated before using the record. Similarly for the other two ISSUE-type tests: ISSUE_DATAGENERALIZATIONS_NOTEMPTY where some form of transformation has occurred, and ISSUE_ESTABLISHMENTMEANS_NOTEMPTY where the value needs to be assessed for utility. ISSUEs are currently outside the Data Quality Fitness for Use Framework. ISSUEs result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "IS_ISSUE", "POTENTIAL_ISSUE" or "NOT_ISSUE". ISSUE is symmetrical to NOT_COMPLIANT, NOT_ISSUE is approximately symmetrical to COMPLIANT, and POSSIBLE_ISSUE does not have an equivalent Validation Response.result. 

#### 1.3.3 Amendment

An AMENDMENT may propose a change or addition to at least one Darwin Core term that is intended to improve one or more components of the quality of the record.  The Response.result from an AMENDMENT MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for QualityControl of an existing database or record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  Amendments, under the framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in these tests.  

#### 1.3.4 Measure 

A MEASURE may return either a Response.result that is a numeric value, or the values COMPLETE or NOT_COMPLETE, or NOT_REPORTED (when the Response.status="INTERNAL_PREREQUISITES_NOTMET").  The principle Measure defined in the core tests is MEASURE_EVENTDATE_DURATIONINSECONDS, it returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the VALIDATIONs and AMENDMENTs and in one case provides an indication of the length of the period of the value of dwc:eventDate.

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

### 1.4 Test Descriptors

<!--- **TODO: What do we call this as "Specification is being used generally and specifically?** --->
<!--- We can use Descriptor for Specification plus related metadata (the rows in the Markdown tables), Specification for the framework concept. --->

The Test Descriptors are those terms that are necessary to comprehensively describe the test. Some terms, such as the GUID are intended for machine consumption. Some terms such as the "Description" are designed to be human-readable and to be understood by consumers of biodiversity data quality reports. Terms such as the "Specification" ensure that implementers have no ambiguity about how the test should be coded. 

### 1.5 Parameterising the tests

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. This allows us to define general tests that provide support for non functional requirements that vary within the community. 

For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite. Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 

Tests are paired in that all AMENDMENTs require a corresponding VALIDATION that assesses some aspect of data quality. An AMENDMENT may be able to improve the quality of data with respect to that VALIDATION. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values. 

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, repeated in 5.2.3 --->
The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

For a simplied list of current terms, see the BDQ Core Quick Reference Guide {http://..........}.

<!--- end of information that probably goes in the users or implementers guides --->

### 1.6 Example RDF (non-normative) 

A more complete description of the tests can be found in the RDF representation of this vocabulary.

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

	<rdf:Description rdf:about="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/Specification"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code; otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</rdfs:comment>
	</rdf:Description>

	<rdf:Description rdf:about="urn:uuid:54fdf7a8-c1b1-4c21-b0a2-1f5aa86d3461">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ValidationMethod"/>
    	<hasValidation xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9"/>
	    <hasSpecification xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
	</rdf:Description>

	<rdf:Description rdf:about="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ContextualizedCriterion"/>
    	<hasActedUponInformationElement xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:c8c64b57-6bed-49f0-b273-d6bc95b12916"/>
    	<hasCriterion xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:1f717a19-54b5-4240-a2c8-fff86d237c2e"/>
    	<hasResourceType xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="rt:SingleRecord"/>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</rdfs:comment>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord</rdfs:label>
	</rdf:Description>


### 1.7 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4 the values of the rdfs:Label, skos:prefLabel, Versioned IRI, Resource Type, Specification, Information Elements ActedUpon, Information Elements Consulted, and Parameters are normative.  The values of Description, Examples, Use Cases, and Notes are non-normative. 

In Section 4, the values of the `Term IRI` and `Definition` are normative. The values of `Term Name` `skos:pref:Label` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Examples` and `Notes`) are non-normative.

### 1.8 Term List Distributions for bdqcore:

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcore/index.md | Complete term list  | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.xml | RDF/XML  | 
| Turtle file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.ttl | Turtle  | 
| CSV file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqcore_terms.csv | CSV list of tests | 

### 1.9 Namespace abbreviations

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

### 2.1 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 3 Term indices
### 3.1 Index By Term Name

(See also [3.2 Index By Label](#32-index-by-label))

**Classes**

**Type**

### 3.2 Index By Label

(See also [3.1 Index By Term Name](#31-index-by-term-name))

**Tests**

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

**Type**

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e"></a>Term Name  bdqcore:3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COORDINATES_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e-2024-08-20</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-20</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment Coordinates From Verbatim</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude,dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:verbatimCoordinates,dwc:verbatimLatitude,dwc:verbatimLongitude,dwc:verbatimCoordinateSystem,dwc:verbatimSRS</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if 1) either dwc:decimalLatitude or dwc:decimalLongitude are bdq:NotEmpty, or 2) dwc:verbatimCoordinates and one of dwc:verbatimLatitude and dwc:verbatimLongitude are bdq:Empty; FILLED_IN the values of dwc:decimalLatitude, dwc:decimalLongitude and dwc:geodeticDatum (provided that the dwc:verbatimCoordinates can be unambiguously interpreted as geographic coordinates) from 1) dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimSRS or 2) dwc:verbatimCoordinates and dwc:verbatimSRS; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: verbatim</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:verbatimLatitude="-23.712", dwc:verbatimLongitude="139.92", dwc:verbatimCoordinates="", dwc:verbatimSRS="EPSG:4326", dwc:verbatimCoordinateSystem="decimal degrees",  dwc:decimalLatitude="", dwc:decimalLongitude="": Response.status=FILLED_IN, Response.result=dwc:decimalLatitude="-23.712", dwc:decimalLongitude="139.92", dwc:geodeticDatum="EPSG:4326", Response.comment="Input fields contain interpretable values"],[dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:verbatimCoordinates="54K 0390210 7377243", dwc:verbatimSRS="EPSG:32754", dwc:verbatimCoordinateSystem="decimal degrees", dwc:decimalLatitude="", dwc:decimalLongitude="":: Response.status=NOT_AMENDED, Response.result="", Response.comment="In the wrong coordinate system"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek, JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Transformations between coordinate reference systems should not be made as a part of this test. Though coordinate precision of the verbatim coordinates could also be interpreted during the process of amending decimal coordinates from verbatim coordinates, that amendment is recommended to be an independent test. Note that dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimCoordinates might all be populated, and they may or not be perfectly consistent with each other. An ideal implementation should check for the consistency of these three fields and not amend them if they are inconsistent.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/32</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:10ad79a1-c93f-4ab2-accf-780867f93957</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms.Amedment for SingleRecord with Specification Specification for: AMENDMENT_COORDINATES_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:1e16fbb3-0c8d-4f23-bf55-68e159ab2b04</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COORDINATES_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f2b4a50a-6b2f-4930-b9df-da87b6a21082"></a>Term Name  bdqcore:f2b4a50a-6b2f-4930-b9df-da87b6a21082</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COORDINATES_TRANSPOSED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f2b4a50a-6b2f-4930-b9df-da87b6a21082-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f2b4a50a-6b2f-4930-b9df-da87b6a21082</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment Coordinates Transposed</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if any of dwc:decimalLatitude or dwc:decimalLongitude or dwc:countryCode are bdq:Empty; AMENDED dwc:decimalLatitude and dwc:decimalLongitude if the coordinates were transposed or one or more of the signs of the coordinates were reversed to align the location with dwc:countryCode; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment of the signs of dwc:decimalLatitude and/or dwc:decimalLongitude to align the location with the dwc:countryCode.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: transposed</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Transposed</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="25.46", dwc:decimalLongitude="135.87", dwc:countryCode="AU": Response.status=AMENDED, Response.result=dwc:decimalLatitude="-25.46", dwc:decimalLongitude="135.87", Response.comment="dwc:decimalLatitude sign reversed to fit dwc:countryCode=AU"],[dwc:decimalLatitude="25.46", dwc:decimalLongitude="135.87", dwc:countryCode="AX": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:countryCode is uninterpretable"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio, GBIF, BISON, FP, Kurator, ALA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/master/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L324</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The dwc:geodeticDatum is not necessary for this test. The maximum positional shift between any geographic coordinate reference system and WGS84 is less than 6 km, so any hemisphere test that relies on a country code for consistency would not be affected by the potential shift.  The prior VALIDATION for this test is VALIDATION_COORDINATE_COUNTRYCODE_CONSISTENT (adb27d29-9f0d-4d52-b760-a77ba57a69c9).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/54</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:2f59ef74-5439-44db-8d5a-85c9773c0cef</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment of the signs of dwc:decimalLatitude and/or dwc:decimalLongitude to align the location with the dwc:countryCode.Amedment for SingleRecord with Specification Specification for: AMENDMENT_COORDINATES_TRANSPOSED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:46caea46-0c94-4efb-9e5f-1b170f2ad54e</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COORDINATES_TRANSPOSED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_bd385eeb-44a2-464b-a503-7abe407ef904"></a>Term Name  bdqcore:bd385eeb-44a2-464b-a503-7abe407ef904</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DCTYPE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/bd385eeb-44a2-464b-a503-7abe407ef904-2024-08-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/bd385eeb-44a2-464b-a503-7abe407ef904</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dc:type Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dc:type</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; AMENDED the value of dc:type if it can be unambiguously interpreted as a term name in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority is "DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List Of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dc:type using the DCMI type vocabulary.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dc:type="evnt": Response.status=AMENDED, Response.result=dc:type="Event", Response.comment="dc:type contains an interpretable value"],[dc:type="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dc:type contains an uninterpretable value"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Dublin Core (2012) DCMI Type Vocabulary. https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>dc:type holds literals (e.g. PhysicalObject), while dcterms:type holds an IRI for the resource (e.g. http://purl.org/dc/dcmitype/PhysicalObject), see the Darwin Core RDF guide https://dwc.tdwg.org/rdf/#32-imported-dublin-core-terms-for-which-only-literal-objects-are-appropriate-normative.   Implementations of this Amendment are expected be able to amend IRI values to the literals, as well as removing leading/trailing whitespace and correcting case errors in the literal.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/41</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:1f38a0bc-4e1f-47a4-bd4a-b6be1c9a456a</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dc:type using the DCMI type vocabulary.Amedment for SingleRecord with Specification Specification for: AMENDMENT_DCTYPE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:317e79db-680a-4bbe-8a3e-e805c69514b8</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DCTYPE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8"></a>Term Name  bdqcore:dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_LICENSE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dcterms:license Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dcterms:license</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; AMENDED value of dcterms:license if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Creative Commons" {[https://creativecommons.org/]} {Creative Commons licenses [https://creativecommons.org/about/cclicenses/]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dcterms:license using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dcterms:license="CC0": Response.status=AMENDED, Response.result=dcterms:license="https://creativecommons.org/publicdomain/zero/1.0/legalcode", Response.comment="Input field contains interpretable value"],[dcterms:license="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dcterms:license contains uninterpretable value "X""]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Dublin Core (2020) Dublin Core Metadata Initiative. License Document. https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/LicenseDocument/</li><li>Creative Commons (n.dat.) About the Licenses. https://creativecommons.org/licenses/</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The license at the record level might be derived from the license of the data set from which the record is retrieved.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/133</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:d040474f-edc7-47b8-80a0-3a3859359897</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dcterms:license using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_LICENSE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:825f551a-2adf-4509-9f95-5a42601a8e88</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_LICENSE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_07c28ace-561a-476e-a9b9-3d5ad6e35933"></a>Term Name  bdqcore:07c28ace-561a-476e-a9b9-3d5ad6e35933</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_BASISOFRECORD_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933-2024-07-24</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/07c28ace-561a-476e-a9b9-3d5ad6e35933</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-07-24</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:basisOfRecord Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:basisOfRecord</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>dwc:basisOfRecord vocabulary</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; AMENDED the value of dwc:basisOfRecord if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]} {dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:basisOfRecord="Human obs": Response.status=AMENDED, Response.result=dwc:basisOfRecord="HumanObservation", Response.comment="dwc:basisOfRecord contains interpretable value"],[dwc:basisOfRecord="FossilSpecimen": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:basisOfRecord contains match in the bdq:sourceAuthority so NOT_AMENDED"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The term dwc:basisOfRecord has the comment "Recommended best practice is to use a controlled vocabulary such as the set of local names of the identifiers for classes in Darwin Core." The list of these values can be determined by searching https://github.com/tdwg/dwc/blob/master/vocabulary/term_versions.csv for rows with status="recommended" and rdf_type="http://www.w3.org/2000/01/rdf-schema#Class". For example, the term http://rs.tdwg.org/dwc/terms/PreservedSpecimen has a local name PreservedSpecimen.  For tests against a dwc:Occurrence record, the set of valid terms is more limited and embodied in the resource found at https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml, which contains the local name for the identifier, as well as preferred and alternate labels from which to standardize values.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/63</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:3c402f21-5347-419c-a720-8bbad7c38577</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_BASISOFRECORD_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:76ee10e7-7be9-432b-ad9c-655b127bff27</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_BASISOFRECORD_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae"></a>Term Name  bdqcore:8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COUNTRYCODE_FROM_COORDINATES</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:countryCode from Coordinates</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:countryCode,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either dwc:decimalLatitude or dwc:decimalLongitude is bdq:Empty, or if dwc:countryCode is bdq:NotEmpty; FILLED_IN dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary in the bdq:sourceAuthority that is attributable to a single valid country code; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary from the bdq:countryShapes that is attributable to a single valid country code.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: coordinates</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="-25.23", dwc:decimalLongitude="135.43", dwc:countryCode="": Response.status=FILLED_IN, Response.result=dwc:countryCode="AU", Response.comment="dwc:decimalLatitude and dwc:decimalLongitude contain interpretable values"],[dwc:decimalLatitude="-38.280937", dwc:decimalLongitude="72.047790", dwc:countryCode="": Response.status=NOT_AMENDED, Response.result="", Response.comment="Coordinates do not fall in the boundary of any country"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, iDigBio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li><li>VLIZ (2023). Marineregions.org. https://www.marineregions.org/downloads.php#marbound</li><li>Dooley, JF Jnr. (2005) An inventory and comparison of globally consistent geospatial databases and libraries. Rome: FAO. http://www.fao.org/3/a0118e/a0118e00.htm#Contents</li><li>Wikipedia (2020) ISO 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li><li>DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list</li><li>Kelso NV and Patterson T (2010) Introducing Natural Earth data—Naturalearthdata.com. Geographica Technica. Special issue, 2010 pp 82–89. https://technicalgeography.org/pdf/sp_i_2010/12_introducing_natural_earth_data__naturaleart.pdf</li><li>Natural Earth (2022) Admin 1 – States, provinces. v5.1.1 2022-05-12. https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/</li><li>Natural Earth (2022) Natural Earth Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales. v5.1.2. https://www.naturalearthdata.com/,  https://github.com/nvkelso/natural-earth-vector/releases/tag/v5.1.2.</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This amendment simply fills dwc:countryCode from a lookup of dwc:decimalLatitude and dwc:decimalLongitude. dwc:coordinateUncertaintyInMeters and dwc:coordinatePrecicision (if present) imply a buffer around the provided coordinates. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is also justified. Taking spatial buffers into account does however greatly complicate the logic and the implementation of this and related tests. In this test, a detection of multiple country codes by sampling within the buffer while possible, is not considered.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/73</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:5e55d983-5667-438c-9754-a71dfe2472af</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary from the bdq:countryShapes that is attributable to a single valid country code.Amedment for SingleRecord with Specification Specification for: AMENDMENT_COUNTRYCODE_FROM_COORDINATES</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:95ac057e-a941-416f-b7dc-ad7aca875cff</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COUNTRYCODE_FROM_COORDINATES</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_fec5ffe6-3958-4312-82d9-ebcca0efb350"></a>Term Name  bdqcore:fec5ffe6-3958-4312-82d9-ebcca0efb350</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COUNTRYCODE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/fec5ffe6-3958-4312-82d9-ebcca0efb350-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISTITES_NOT_MET if the value of dwc:countryCode is bdq:Empty; AMENDED the value of dwc:countryCode if it can be unambiguously interpreted in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:countryCode if it can be interpreted as an ISO country code.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="Australia": Response.status=AMENDED, Response.result=dwc:countryCode="AU", Response.comment="dwc:countryCode contains an interpretable value"],[dwc:countryCode="Aust.": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:countryCode contains an ambiguous value"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li><li>Wikipedia (2020) ISO 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li><li>DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list</li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853.</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/48</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:29b2e2ac-9667-4774-ac06-45333555c620</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:countryCode if it can be interpreted as an ISO country code.Amedment for SingleRecord with Specification Specification for: AMENDMENT_COUNTRYCODE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:3e076cfa-56ff-4b79-9739-736d062eac5a</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COUNTRYCODE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_39bb2280-1215-447b-9221-fd13bc990641"></a>Term Name  bdqcore:39bb2280-1215-447b-9221-fd13bc990641</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DATEIDENTIFIED_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/39bb2280-1215-447b-9221-fd13bc990641-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/39bb2280-1215-447b-9221-fd13bc990641</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Identification</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:dateIdentified</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; AMENDED if the value of dwc:dateIdentified is not a properly formatted ISO 8601 date but is unambiguous and altered to be a valid ISO 8601 date; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:dateIdentified to a valid ISO date.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dateIdentified="2021-28-10": Response.status=AMENDED, Response.result=dwc:dateIdentified="2021-10-28", Response.comment="dwc:dateIdentified assuming dwc:year, dwc:day and dwc:month"],[dwc:dateIdentified="21-10-28": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:dateIdentified contains ambiguous values. It could be dd-mm-yy or yy-mm-dd"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Kurator</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/1abbd3f02eb6c28129764defab78f72156972864/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L489</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We reference Wikipedia for the ISO standard because the standard documents are not free.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/26</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:0836e914-75d8-4cda-a39f-f21a08382732</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:dateIdentified to a valid ISO date.Amedment for SingleRecord with Specification Specification for: AMENDMENT_DATEIDENTIFIED_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:16e40618-e9bd-479a-b1e8-8aee3467109f</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DATEIDENTIFIED_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b129fa4d-b25b-43f7-9645-5ed4d44b357b"></a>Term Name  bdqcore:b129fa4d-b25b-43f7-9645-5ed4d44b357b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b129fa4d-b25b-43f7-9645-5ed4d44b357b-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b129fa4d-b25b-43f7-9645-5ed4d44b357b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:day Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:day</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; AMENDED the value of dwc:day if the value is unambiguously interpreted as an integer between 1 and 31 inclusive; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:day as an integer between 1 and 31 inclusive.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="23rd": Response.status=AMENDED, Response.result=dwc:day="23", Response.comment="dwc:day is interpretable as "23""],[dwc:day="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:day is ambiguous, either a "X", "No data" or "10""]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>A potential minimal implementation is at: https://github.com/FilteredPush/event_date_qc/blob/238f234a4947b3c2820fb2fe3987326f9ead5e54/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1114 unit test at  https://github.com/FilteredPush/event_date_qc/blob/238f234a4947b3c2820fb2fe3987326f9ead5e54/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L824</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If dwc:day contains text that may be interpreted as Roman numerals, the result will be NOT_AMENDED as this is not standard. Values such as "3rd" or "12th" can be interpreted as the integers "3" and "12".  Text such as "5th Friday" is ambiguous.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/127</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:c15d57ce-301c-4db0-8146-399cd59382ad</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:day as an integer between 1 and 31 inclusive.Amedment for SingleRecord with Specification Specification for: AMENDMENT_DAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:3eae7451-19c6-403c-ba36-29f8204d15ff</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DAY_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_74ef1034-e289-4596-b5b0-cde73796697d"></a>Term Name  bdqcore:74ef1034-e289-4596-b5b0-cde73796697d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/74ef1034-e289-4596-b5b0-cde73796697d-2024-04-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/74ef1034-e289-4596-b5b0-cde73796697d</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-04-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:degreeOfEstablishment Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:degreeOfEstablishment</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; AMENDED the value of dwc:degreeOfEstablishment if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:degreeOfEstablishment using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:degreeOfEstablishment="capt.": Response.status=AMENDED, Response.result=dwc:degreeOfEstablishment="captive", Response.comment="dwc:degreeOfEstablishment contains an interpretable value in the bdq:sourceAuthority"],[dwc:degreeOfEstablishment="tree": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:degreeOfEstablishment does not contain an interpretable value in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Darwin Core Maintenance Group (2021) Degree Of Establishment Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/doe/</li> <li>Groom et al. (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Services 3: e38084. https://doi.org/10.3897/biss.3.38084</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, synonyms for values of dwc:degreeOfEstablishment can be found at https://registry.gbif.org/vocabulary/DegreeOfEstablishment/concepts.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/276</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:fda457b6-f844-49ca-aee5-1b99968cf7ea</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:degreeOfEstablishment using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:ba1fa532-9612-4944-bfd1-8bd39ab47758</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_15d15927-7a22-43f8-88d6-298f5eb45c4c"></a>Term Name  bdqcore:15d15927-7a22-43f8-88d6-298f5eb45c4c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/15d15927-7a22-43f8-88d6-298f5eb45c4c-2024-02-08</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/15d15927-7a22-43f8-88d6-298f5eb45c4c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-08</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-08</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:establishmentMeans Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:establishmentMeans</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; AMENDED the value of dwc:establishmentMeans if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:establishmentMeans using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:establishmentMeans="vag.": Response.status=AMENDED, Response.result=dwc:establishmentMeans="vagrant", Response.comment="dwc:establishmentMeans contains an interpretable value in the bdq:sourceAuthority"],[dwc:establishmentMeans="cultivated": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:establishmentMeans is not an interpretable value in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Darwin Core Maintenance Group (2021) Establishment Means Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/em/</li> <li>Groom et al. (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Services 3: e38084. https://doi.org/10.3897/biss.3.38084</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/269</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:fcd9e46a-a31e-47f5-a18a-bb7ee5d1394a</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:establishmentMeans using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:fa4e531e-f45e-4dea-8c4b-27d364117808</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_710fe118-17e1-440f-b428-88ba3f547d6d"></a>Term Name  bdqcore:710fe118-17e1-440f-b428-88ba3f547d6d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENT_FROM_EVENTDATE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/710fe118-17e1-440f-b428-88ba3f547d6d-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/710fe118-17e1-440f-b428-88ba3f547d6d</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:Event from dwc:eventDate</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:year,dwc:month,dwc:day,dwc:startDayOfYear,dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or contains an invalid value according to ISO 8601; FILLED_IN if any of (1) dwc:day from dwc:eventDate if dwc:day is bdq:Empty and dwc:eventDate has a precision of a day or finer and is within a single day, (2) dwc:month from dwc:eventDate if dwc:month is bdq:Empty and dwc:eventDate has a precision of a single month or finer and is within a single month, (3) dwc:year from dwc:eventDate if dwc:year is bdq:Empty and dwc:eventDate has a precision of a single year or finer and is within a single year, (4) dwc:startDayOfYear and dwc:endDayOfYear if they are bdq:Empty and dwc:eventDate has a precision of a day or better; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to values in any of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear or dwc:endDayOfYear from the content of dwc:eventDate.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: eventdate</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="2023-01-26", dwc:year="2023", dwc:month="", dwc:day="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=FILLED_IN, Response.result=dwc:month="1", dwc:day="26", dwc:startDayOfYear="26", dwc:endDayOfYear="26", Response.comment="dwc:month, dwc:day, dwc:startDayOfyear and dwc:endDayOfYear filled in from dwc:eventDate"],[dwc:eventDate="2023",  dwc:year="2023", dwc:month="", dwc:day="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=NOT_AMENDED, Response.result=, Response.comment="No amendments possible"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>FilteredPush event_date_qc [DwCEventDQ.amendmentEventFromEventdate()](https://github.com/FilteredPush/event_date_qc/blob/89436b476975fb40ab2883c4e48717bdf957c0a8/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L2010) unit test in [DwcEventDQTest](https://github.com/FilteredPush/event_date_qc/blob/89436b476975fb40ab2883c4e48717bdf957c0a8/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L1569)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Only fields that are empty will be have changes proposed, and only if dwc:eventDate has a valid ISO 8601-1 date. The dwc:eventDate is the canonical form of the event date (it is the first trusted form). If event date does not contain a range,  dwc:startDayOfYear = dwc:endDayOfYear. Time (as compared to date) is not deemed a CORE component.  Note, see sequencing tests section of standards document, run this amendment after any other amendment which may affect dwc:eventDate</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/52</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:2bc15408-d0d0-4166-b6a6-6fdba5704379</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to values in any of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear or dwc:endDayOfYear from the content of dwc:eventDate.Amedment for SingleRecord with Specification Specification for: AMENDMENT_EVENT_FROM_EVENTDATE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:46992280-0ed6-4c42-9e89-ed388ca1d43b</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENT_FROM_EVENTDATE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6d0a0c10-5e4a-4759-b448-88932f399812"></a>Term Name  bdqcore:6d0a0c10-5e4a-4759-b448-88932f399812</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6d0a0c10-5e4a-4759-b448-88932f399812-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6d0a0c10-5e4a-4759-b448-88932f399812</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:eventDate From dwc:verbatimEventDate</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:verbatimEventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:NotEmpty or the value of dwc:verbatimEventDate is bdq:Empty; FILLED_IN the value of dwc:eventDate if an unambiguous ISO 8601 date is interpreted from dwc:verbatimEventDate; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:eventDate from the content of dwc:verbatimEventDate.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: verbatim</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="", dwc:verbatimEventDate="Friday 29th Oct. 2021": Response.status=FILLED_IN, Response.result=dwc:eventDate="2021-10-29", Response.comment="dwc:verbatimEventDate contains an interpretable value (assuming some external lookup thesauri)"],[dwc:eventDate="", dwc:verbatimEventDate="03/04/2020": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:verbatimEventDate is ambiguous - could be either 3rd April or 4th March"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet, FP, Kurator</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795).</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc [DwCEventDQ.amendmentEventdateFromVerbatim()](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L320) For a minimum set of unit tests see: [DwcEventDQTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L441), see also unit tests for underlying implementation in [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L632) and [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L788)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the proposed eventDate is prior to 1918-02-14, the Response.comment will include a note that the "verbatimDate was assumed to be in the Gregorian calendar". When running the test, the original precision, e.g. year=1980, month=1 should be retained, e.g. dwc:eventDate should become 1980-01, not 1980-01-01/1980-01-31.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/86</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:7c915d24-1fda-4d72-97d4-8bd5e2136c97</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:eventDate from the content of dwc:verbatimEventDate.Amedment for SingleRecord with Specification Specification for: AMENDMENT_EVENTDATE_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:b417d971-8b0f-49ab-9431-3364ba8694e2</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3892f432-ddd0-4a0a-b713-f2e2ecbd879d"></a>Term Name  bdqcore:3892f432-ddd0-4a0a-b713-f2e2ecbd879d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3892f432-ddd0-4a0a-b713-f2e2ecbd879d-2024-09-15</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3892f432-ddd0-4a0a-b713-f2e2ecbd879d</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-15</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:eventDate from dwc:year dwc:month dwc:day</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:year,dwc:month,dwc:day</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL _PREREQUISITES_NOT_MET if dwc:eventDate is not EMPTY or dwc:year is EMPTY or is not interpretable as an integer; FILLED_IN the value of dwc:eventDate if an ISO 8601 date was interpreted from the values in dwc:year, dwc:month and dwc:day; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:month and dwc:day.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: yearmonthday</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="", dwc:year="1420", dwc:month="10", dwc:day="29": Response.status=FILLED_IN, Response.result=dwc:eventDate="1420-10-29", Response.comment="dwc:year, dwc:month and dwc:day are interpretable, even if pre-Linnaeus"],[dwc:eventDate="", dwc:year="2024", dwc:month="2", dwc:day="30": Response.status=NOT_AMENDED, Response.result=, Response.comment="Not a valid date"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/5f2e7b30f8a8076977b2a609e0318068db80599a/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1003 unit tests at https://github.com/FilteredPush/event_date_qc/blob/5f2e7b30f8a8076977b2a609e0318068db80599a/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L493</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>An attempt to populate dwc:eventDate from dwc:verbatimEventDate and from dwc:startDayOfYear and dwc:endDayOfYear should be made before this test is run. If dwc:year and dwc:day are present and interpretable, but dwc:month is not supplied or is not interpretable, then just the year should be given as the proposed amendment.   This test assumes that that dwc:year, dwc:month, dwc:day are in a Gregorian calendar, and that only those three pieces of information are needed to produce a dwc:eventDate (explicitly in ISO 8601-1 format, and thus using the Gregorian calendar). When running the test, the original precision, e.g. dwc:year=1980, dwc:month=1 should be retained, e.g. dwc:eventDate should become 1980-01, not 1980-01-01/1980-01-3.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/93</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:8ca96a50-f1f5-4a4e-853e-755cc5aa82a7</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:month and dwc:day.Amedment for SingleRecord with Specification Specification for: AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:bda7e8a3-3366-43d5-8a8b-e206101dc90d</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_eb0a44fa-241c-4d64-98df-ad4aa837307b"></a>Term Name  bdqcore:eb0a44fa-241c-4d64-98df-ad4aa837307b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/eb0a44fa-241c-4d64-98df-ad4aa837307b-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/eb0a44fa-241c-4d64-98df-ad4aa837307b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-12</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:eventDate from dwc:year dwc:startDayOfYear dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:year,dwc:startDayOfYear,dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:NotEmpty or any of dwc:year, dwc:startDayOfYear, or dwc:endDayOfYear are bdq:Empty; FILLED_IN the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear if the values in each are independently interpretable and if the value of dwc:startDayOfYear is less than the value of dwc:endDayOfYear; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: yearstartdayofyearenddayofyear</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:year="1901", dwc:startDayOfYear="15", dwc:endDayOfYear="25", dwc:eventDate="": Response.status=FILLED_IN, Response.result=dwc:eventDate="1901-01-15/1901-01-25", Response.comment="dwc:eventDate was interpreted from dwc:year, dwc:startDayOfYear and dwc:endDayOfYear"],[dwc:year="1901", dwc:startDayOfYear="25", dwc:endDayOfYear="15", dwc:eventDate="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:startDayOfYear > dwc:endDayOfyear"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/4665e4d3b43ce7ddf319b3d7a5d3dbfee1411250/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L828   Unit Test at:  https://github.com/FilteredPush/event_date_qc/blob/96a8981d997cceb2f39ba47d63f0b98c1b56680c/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L402</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>An attempt to populate dwc:eventDate from dwc:verbatimEventDate should be made before this test is run.   While year=1999, startDayOfYear=123  could be validly represented as an ISO date as either 1999-123 or 1999-05-03, the latter of these two forms SHOULD be used, thus, do not simply concatenate dwc:year and dwc:startDayOfYear. This test is only for cases that fall within the one year (as given in dwc:year) and hence "dwc:startDayOfYear will always be less than dwc:endDayOfYear". [or do we just leave this as being obvious from the Expected Response.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/132</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:cca7732f-c336-47b0-9d69-4514d39f5950</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear.Amedment for SingleRecord with Specification Specification for: AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:647bf697-e432-4b31-9a69-778396e14a82</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_718dfc3c-cb52-4fca-b8e2-0e722f375da7"></a>Term Name  bdqcore:718dfc3c-cb52-4fca-b8e2-0e722f375da7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/718dfc3c-cb52-4fca-b8e2-0e722f375da7-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/718dfc3c-cb52-4fca-b8e2-0e722f375da7</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:eventDate Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; AMENDED if the value of dwc:eventDate is not a properly formatted ISO 8601 date but is unambiguous, and altered to be a valid ISO 8601 date; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment of the value of dwc:eventDate to a valid ISO date.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="2021-28-10": Response.status=AMENDED, Response.result=dwc:eventDate="2021-10-28", Response.comment="dwc:eventDate contains an interpretable value. Assuming year-day-month input format"],[dwc:eventDate="10-28": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:eventDate contains an ambiguous value"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paul Morris, Lee Belbin</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795).</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc [DwCEventDQ.amendmentEventdateStandardized()](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L545) A minimal set of unit tests is in [DwCEventDQTestDefinitions](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DwCEventDQTestDefinitions.java#L338)  unit tests for the underlying verbatim date extraction code are in [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L632) and [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L788)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The intent of the amended range is to capture the original uncertainty where possible. As in the example, we amend "1999-11" instead of "1999-11-01/1999-11-31".  An AMBIGUOUS response is possible.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/61</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:381b0edb-0fb4-4a8e-a77b-badcfa286961</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment of the value of dwc:eventDate to a valid ISO date.Amedment for SingleRecord with Specification Specification for: AMENDMENT_EVENTDATE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:6e0e22a1-c233-4c13-baa7-0ab48a4340e4</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7498ca76-c4d4-42e2-8103-acacccbdffa7"></a>Term Name  bdqcore:7498ca76-c4d4-42e2-8103-acacccbdffa7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7498ca76-c4d4-42e2-8103-acacccbdffa7-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7498ca76-c4d4-42e2-8103-acacccbdffa7</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-08</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:geodeticDatum Assumed Default</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:geodeticDatum,dwc:coordinateUncertaintyInMeters,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:defaultGeodeticDatum</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:NotEmpty; FILLED_IN dwc:geodeticDatum using the value of bdq:defaultGeodeticDatum, report FILLED_IN and, if dwc:coordinateUncertaintyInMeters, dwc:decimalLatitude and dwc:decimalLongitude are bdq:NotEmpty, amend the value of dwc:coordinateUncertaintyInMeters by adding the maximum datum shift between the specified bdq:defaultGeodeticDatum and any other datum at the provided dwc:decimalLatitude and dwc:decimalLongitude and instead report AMENDED; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:defaultGeodeticDatum = "EPSG:4326" {[https://epsg.org/crs_4326/WGS-84.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to fill in dwc:geodeticDatum using a prameterized value if the dwc:geodeticDatum is empty.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: assumeddefault</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>AssumedDefault</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="[null]", dwc:decimalLatitude="-30.00", dwc:decimalLongitude="130.00", dwc:coordinateUncertaintyInMeters="50": Response.status=AMENDED, Response.result=dwc:geodeticDatum="EPSG:4326", dwc:coordinateUncertaintyInMeters="2836", Response.comment="dwc:godeticDatum is bdq:Empty so filled in with default and dwc:coordinateUncertaintyInMeters amended to maximum possible value"],[dwc:geodeticDatum="WGS84", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:geodeticDatum contains an interpretable value"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Maptiler (2019) EPSG.io. https://epsg.io/</li> <li>EPSG (2024) About the EPSG Dataset. https://epsg.org/</li> <li>Spatial Reference (2024) What is SpatialReference.org. https://spatialreference.org/</li> <li>Geomatic Solutions (2018) Georepository. Version 9.0.0.1062. https://georepository.com/</li> <li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li> <li>Wieczorek C and Wieczorek J (2021) Georeferencing Calculator. http://georeferencing.org/georefcalculator/gc.html</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the dwc:coordinateUncertaintyInMeters is bdq:Empty, not interpretable, or not valid, this amendment should not provide a dwc:coordinateUncertaintyInMeters. If the dwc:coordinateUncertaintyInMeters is bdqNotEmpty and is valid, this amendment should add to the dwc:coordinateUncertaintyInMeters the uncertainty contributed by the maximum datum shift at the given coordinates. Since different systems have differing requirements for what the default datum should be, it is left unspecified, but should match whatever the target datum is in AMENDMENT_COORDINATES_CONVERTED (620749b9-7d9c-4890-97d2-be3d1cde6da8). After the amendment is performed, the dwc:geodeticDatum field should be the assumed default datum as parameterized. An example implementation to determine the uncertainty added by asserting a default datum (datum shift) where a known datum is not declared can be found in [datumshiftproj.py](https://github.com/VertNet/georefcalculator/blob/master/source/python/datumshiftproj.py) in the source code for the [Georeferencing Calculator](http://georeferencing.org/georefcalculator/gc.html) (Wieczorek & Wieczorek 2021). Included in the source code is a [5-degree grid](https://github.com/VertNet/georefcalculator/blob/master/datumerrordata.js) of datum shifts from an unknown datum to WGS84.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/102</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:95627fe5-326a-4468-b220-82af19a6ce98</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to fill in dwc:geodeticDatum using a prameterized value if the dwc:geodeticDatum is empty.Amedment for SingleRecord with Specification Specification for: AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:da49fa95-ce7b-46cf-825a-91d53f21a997</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0345b325-836d-4235-96d0-3b5caf150fc0"></a>Term Name  bdqcore:0345b325-836d-4235-96d0-3b5caf150fc0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_GEODETICDATUM_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0345b325-836d-4235-96d0-3b5caf150fc0-2024-09-06</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0345b325-836d-4235-96d0-3b5caf150fc0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-7-24</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:geodeticDatum Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; AMENDED the value of dwc:geodeticDatum if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index#/Datum]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:geodeticDatum using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="WGS84": Response.status=AMENDED, Response.result=dwc:geodeticDatum="EPSG:4326", Response.comment="dwc:geodeticDatum contains a valid code in the bdq:sourceAuthority"],[dwc:geodeticDatum="WGS8": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:geodeticDatum contains an ambiguous value"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paul Morris</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Maptiler (2019) EPSG.io. https://epsg.io/</li> <li>EPSG (2024) About the EPSG Dataset. https://epsg.org/</li> <li>Spatial Reference (2024) What is SpatialReference.org. https://spatialreference.org/</li> <li>Geomatic Solutions (2018) Georepository. Version 9.0.0.1062. https://georepository.com/</li> <li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li> <li>Wieczorek C and Wieczorek J (2021) Georeferencing Calculator. http://georeferencing.org/georefcalculator/gc.html</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Chapman and Wieczorek (2020) recommend best practice is to use EPSG codes (https://epsg.io) as a controlled vocabulary. Ideally, amend to the EPSG code for the geographic coordinate reference system (CRS), if known. Otherwise use the EPSG code for the geodetic datum, if known. Otherwise use the EPSG code of the ellipsoid, if known. If none of these is known, use the explicit value "not recorded". The reference vocabularies of values for geodetic datums and ellipsoids needs to be made available should map alternative representations of dwc:geodeticDatum strings to EPSG codes, such as "WGS84", "WGS_84", "WGS:84", "WGS 84" all with standard value "epsg:4326". NB. Do NOT change one datum to any other datum no matter how close they are or may appear to be. The same treatment should be given to all datums, which is to use their transformation algorithms to get the equivalent in epsg:4326. For reference, a vocabulary of synonyms for EPSG codes for values of dwc:geodeticDatum can be found at https://registry.gbif.org/vocabulary/GeodeticDatum/concepts.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/60</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:35ac2bb4-d1f8-4a32-a591-32f614d97429</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:geodeticDatum using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_GEODETICDATUM_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:5daf8c2f-50df-423c-a740-55079b625c10</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_GEODETICDATUM_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c5658b83-4471-4f57-9d94-bf7d0a96900c"></a>Term Name  bdqcore:c5658b83-4471-4f57-9d94-bf7d0a96900c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c5658b83-4471-4f57-9d94-bf7d0a96900c-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c5658b83-4471-4f57-9d94-bf7d0a96900c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-24</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:minimumDepthInMeters dwc:maximumDepthInMeters From dwc:verbatimDepth</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:minimumDepthInMeters,dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:verbatimDepth</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters are bdq:NotEmpty or dwc:verbatimDepth is bdq:Empty; FILLED_IN the value of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be unambiguously interpreted from dwc:verbatimDepth; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes amendments of the values of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be interpreted from dwc:verbatimDepth.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: verbatim</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumDepthInMeters="", dwc:maximumDepthInMeters="", dwc:verbatimDepth="10 feet": Response.status=FILLED_IN, Response.result=dwc:minimumDepthInMeters="3.048", dwc:maximumDepthInMeters="3.048", Response.comment="dwc:verbatimDepth contains interpretable values"],[ dwc:minimumDepthInMeters="", dwc:maximumDepthInMeters="", dwc:verbatimDepth="x": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:verbatimDepth does not contain an interpretable value"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If dwc:verbatimDepth has a single value rather than a range, the minimum and maximum values should be amended with the same value. When transforming units, the transformation should be reversible, not adjusting the number of significant digits or adjusting the rounding. For example, transform fathoms to meters by multiplying by 1.8288 and retaining added significant digits (verbatim depth of 10 fathoms to minimum and maximum depths in meters of 18.288). Implementations should be capable of interpreting verbatim data in at least meters, fathoms, and feet, in the form of either a single value or a range. The units must be specified in the verbatim data to be interpretable.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/55</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:2f73a662-b833-44ad-942c-a87f82262b7c</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes amendments of the values of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be interpreted from dwc:verbatimDepth.Amedment for SingleRecord with Specification Specification for: AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:4db033ea-b0f7-4d01-a5fc-a0459a73a67d</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_2d638c8b-4c62-44a0-a14d-fa147bf9823d"></a>Term Name  bdqcore:2d638c8b-4c62-44a0-a14d-fa147bf9823d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/2d638c8b-4c62-44a0-a14d-fa147bf9823d-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/2d638c8b-4c62-44a0-a14d-fa147bf9823d</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:minimumElevationInMeters dwc:maximumElevationInMeters From dwc:verbatimElevation</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:minimumElevationInMeters,dwc:maximumElevationInMeters</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:verbatimElevation</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters or dwc:maximumElevationInMeters are bdq:NotEmpty or dwc:verbatimElevation is bdq:Empty; FILLED_IN the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be unambiguously interpreted from dwc:verbatimElevation; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment or amendments to the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be interpreted from dwc:verbatimElevation.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: verbatim</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:verbatimElevation="100 feet", dwc:minimumElevationInMeters="", dwc:maximumElevationInMeters="": Response.status=FILLED_IN, Response.result=dwc:minimumElevationInMeters="30.48", dwc:maximumElevationInMeters="30.48", Response.comment="dwc:verbatimElevation contains an interpretable value"],[dwc:verbatimElevation="x", dwc:minimumElevationInMeters="", dwc:maximumElevationInMeters="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:verbatimElevation contains an uninterpretable value"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the dwc:verbatimElevation as a single value rather than a range, the minimum and maximum values should be amended with the same value. When transforming units, the transformation should be reversible, not adjusting the number of significant digits or adjusting the rounding. For example, transform yards to meters by multiplying by 0.9144 and retaining added significant digits (verbatim elevation of 10 yards to minimum and maximum depths in meters of 9.144). Implementations should be capable of interpreting verbatim data in at least meters,  yards, feet, and kilometers in the form of either a single value or a range. The units must be specified in the verbatim data to be interpretable.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/68</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:47bdaece-0c20-4ba3-b453-4c78b92b4c94</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment or amendments to the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be interpreted from dwc:verbatimElevation.Amedment for SingleRecord with Specification Specification for: AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:84195393-4797-465f-bfc1-b764df67c5c2</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_2e371d57-1eb3-4fe3-8a61-dff43ced50cf"></a>Term Name  bdqcore:2e371d57-1eb3-4fe3-8a61-dff43ced50cf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_MONTH_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/2e371d57-1eb3-4fe3-8a61-dff43ced50cf-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/2e371d57-1eb3-4fe3-8a61-dff43ced50cf</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:month Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:month</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; AMENDED the value of dwc:month if it can be unambiguously interpreted as an integer between 1 and 12 inclusive; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:month as an integer between 1 and 12 inclusive.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:month="IV": Response.status=AMENDED, Response.result=dwc:month="4", Response.comment="dwc:month interpreted as roman numerals "],[dwc:month="October": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:month contains an uninterpretable value"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/f224e5a1e6db81bc6ca725f520dd06a71fcfb54e/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1055 with unit test at https://github.com/FilteredPush/event_date_qc/blob/f224e5a1e6db81bc6ca725f520dd06a71fcfb54e/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L671 Internals of recognized string values (roman numerals, month names and abbreviations in multiple languages) use a combination of event_date_qc's DateUtils.cleanMonth() (see https://github.com/FilteredPush/event_date_qc/blob/23e4139d7f0ef71736f7fc7e984cfd2d0bfea093/src/main/java/org/filteredpush/qc/date/DateUtils.java#L2111  and Joda time's month recognition)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Implementations should translate interpretable Roman numerals in the range I-XII in dwc:month as integer month values 1-12, as some natural science domains use roman numeral months to avoid language and day/month vs moth/day order. In these cases, the result will be AMENDED numeric equivalents.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/128</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:c1af0cfd-311e-4982-922a-dc67e0c2c975</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:month as an integer between 1 and 12 inclusive.Amedment for SingleRecord with Specification Specification for: AMENDMENT_MONTH_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:4a514adf-766f-46a4-bf16-6febcb594f38</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_MONTH_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5"></a>Term Name  bdqcore:96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5-2024-08-23</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-23</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:occurrenceStatus Assumed Default</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:individualCount,dwc:organismQuantity</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>dwc:defaultOccurrenceStatus</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:NotEmpty; FILLED_IN the value of dwc:occurrenceStatus using the Parameter value if dwc:occurrenceStatus,  dwc:individualCount and dwc:organismQuantity are bdq:Empty; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>dwc:defaultOccurrenceStatus default = "present"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment of the value of dwc:occurrenceStatus to the default parameter value if dwc:occurrenceStatus, dwc:individualCount and dwc:organismQuantity are empty.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: assumeddefault</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>AssumedDefault</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="", dwc:individualCount="", dwc:organismQuantity="": Response.status=FILLED_IN, Response.result=dwc:occurrenceStatus="present", Response.comment="dwc:occurrenceStatus is bdq:Empty; assumed "present""],[dwc:occurrenceStatus="X", dwc:individualCount="10", dwc:organismQuantity="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:occurrenceStatus is bdq:NotEmpty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/75</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:637f7b40-1bdc-4ecc-a6ae-bb9b366da3fd</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment of the value of dwc:occurrenceStatus to the default parameter value if dwc:occurrenceStatus, dwc:individualCount and dwc:organismQuantity are empty.Amedment for SingleRecord with Specification Specification for: AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:9c150f88-1fc4-47b7-b826-f6357c104946</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f8f3a093-042c-47a3-971a-a482aaaf3b75"></a>Term Name  bdqcore:f8f3a093-042c-47a3-971a-a482aaaf3b75</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f8f3a093-042c-47a3-971a-a482aaaf3b75-2024-07-26</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f8f3a093-042c-47a3-971a-a482aaaf3b75</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-07-26</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:occurrenceStatus Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:ocurrenceStatus is bdq:Empty; AMENDED the value of dwc:occurrenceStatus if it can be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF OccurrenceStatus Vocabulary" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus]} {"dwc:occurrenceStatus vocabulary API" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:occurrenceStatus using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="1": Response.status=AMENDED, Response.result=dwc:occurrenceStatus="present", Response.comment="Input field contains interpretable value. This may be pushing it a little, but I would have interpreted 1/0 as present/absent"],[dwc:occurrenceStatus="X": Response.status=NOT_AMENDED, Response.result=, Response.comment="Input field contains uninterpretable value "X"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The original recommended controlled vocabulary for this term consisted of "present" and "absent", which are the only two appropriate terms for a Darwin Core Occurrence. This is reflected in the suggested dwc:occurrenceStatus vocabulary for this test. Other values for dwc:occurrenceStatus should only arise under circumstances that do not refer to an Occurrence.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/115</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:abdca718-5564-4dbd-9d98-0a1707d6ecf2</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:occurrenceStatus using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:fae50773-a832-4e44-87fe-d66a1332c3e7</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f9205977-f145-44f5-8cb9-e3e2e35ce908"></a>Term Name  bdqcore:f9205977-f145-44f5-8cb9-e3e2e35ce908</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_PATHWAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f9205977-f145-44f5-8cb9-e3e2e35ce908-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f9205977-f145-44f5-8cb9-e3e2e35ce908</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:pathway Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:pathway</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; AMENDED the value of dwc:pathway if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Propose an amendment to the value of dwc:pathway using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:pathway="transportStowaway": Response.status=AMENDED, Response.result=dwc:pathway="transportStowaway", Response.comment="dwc:pathway found in the bdq:sourceAuthority"],[dwc:pathway="escapeee": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:pathway not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Darwin Core Maintenance Group (2021) Pathway Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). https://dwc.tdwg.org/pw/</li> <li>Groom et al. (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Services 3: e38084. https://doi.org/10.3897/biss.3.38084</i></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, synonyms for values of dwc:pathway can be found at https://registry.gbif.org/vocabulary/Pathway/concepts.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/278</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:5e1ab035-a79f-4048-9330-e073d4b6c2c9</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Propose an amendment to the value of dwc:pathway using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_PATHWAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:fef3a7f9-edd8-41c9-9704-4798814077e3</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_PATHWAY_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f01fb3f9-2f7e-418b-9f51-adf50f202aea"></a>Term Name  bdqcore:f01fb3f9-2f7e-418b-9f51-adf50f202aea</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f01fb3f9-2f7e-418b-9f51-adf50f202aea-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f01fb3f9-2f7e-418b-9f51-adf50f202aea</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:scientificName from dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty, or dwc:scientificName is bdq:NotEmpty; FILLED_IN the value of dwc:scientificName if the value of dwc: scientificNameID could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:scientificName using the dwc:scientificNameID value from the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: scientificnameid</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameID="gbif:8102122", dwc:scientificName="": Response.status=FILLED_IN, Response.result=dwc:scientificName="Harpullia pendula F.Muell.", Response.comment="dwc:scientificNameID contains an interpretable value"],[dwc:scientificNameID="gbif:8a", dwc:scientificName="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:scientificNameID does not contain an interpretable value"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The value of dwc:scientificNameID is unambiguous if dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority.   When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID.   Implementors can be aware of the current  GBIF api endpoint that can replace the pseduo-namespace gbif: when looking up the dwc:scientificNameID (taxonID in the gbif document), e.g. `s/gbif:/https:\/\/api.gbif.org\/v1\/species\// ` will transform the value taxonID=gbif:8102122 to the resolvable endpoint https://api.gbif.org/v1/species/8102122  The pseudo-namespace "gbif:" is recommended by GBIF to reference GBIF taxon records.   Where resolvable persistent identifiers exist for dwc:scientificNameID values, they should be used in full, but implementors will need to support at least the "gbif:" pseudo-namespace.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/71</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:5a6eaed2-00bd-41ce-9531-ebeb986a3517</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:scientificName using the dwc:scientificNameID value from the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:8e8355a6-e5d0-4ad7-9f2c-8a4148bfda57</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_431467d6-9b4b-48fa-a197-cd5379f5e889"></a>Term Name  bdqcore:431467d6-9b4b-48fa-a197-cd5379f5e889</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/431467d6-9b4b-48fa-a197-cd5379f5e889-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/431467d6-9b4b-48fa-a197-cd5379f5e889</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:scientificNameID from dwc:Taxon</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:taxonID,dwc:acceptedNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:scientificName,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:cultivarEpithet,dwc:vernacularName,dwc:scientificNameAuthorship,dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available;  INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:NotEmpty, or if all of dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, and dwc:cultivarEpithet are bdq:Empty, FILLED_IN the value of dwc:scientificNameID for an unambiguously resolved single taxon record in the bdq:sourceAuthority through (1) the value of dwc:scientificName or (2) if dwc:scientificName is bdq:Empty through values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship and dwc:cultivarEpithet, or (3) if ambiguity produced by multiple matches in (1) or (2) can be disambiguated to a single Taxon using the values of dwc:subtribe, dwc:tribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID, dwc:taxonomicRank, and dwc:vernacularName; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:scientificNameID if it can be unambiguously resolved from bdq:sourceAuthority using the available taxon terms.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: taxon</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Chicoreus palmarosae (Lamarck, 1822)", dwc:higherClassification="", dwc:kingdom="Animalia", dwc:phylum="Mollusca", dwc:class="Gastropoda", dwc:order="", dwc:family="Muricidae", dwc:subfamily="", dwc:genus="Chicoreus", dwc:genericName="Chicoreus", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="palmarosae", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="(Lamarck, 1822)", dwc:taxonRank="", bdq:sourceAuthority=”marinespecies.org”: Response.status=FILLED_IN, Response.result=dwc:scientificNameID="urn:lsid:marinespecies.org:taxname:208134", Response.comment="dwc:scientificName matched to unique taxon record in WoRMS, exact match on name and authorship.  Resolvable at https://marinespecies.org/aphia.php?p=taxdetails&id=208134"],[dwc:scientificNameID="", dwc:taxonID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Graphis", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:family="", dwc:subfamily="", dwc:genus="", dwc:genericName="", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="", dwc:taxonRank="": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:scientificName="Graphis" is ambiguous as could be either a lichen or a gastropod."]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>FP-Akka</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FP-KurationServices, Arctos, MCZbase, Symbiota</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Return a result with no value and a Result.status of NOT_AMENDED with a Response.comment of ambiguous if the information provided does not resolve to a unique result (e.g. if homonyms exist and there is insufficient information in the provided data, for example using the lowest ranking taxa in conjunction with dwc:dwc:scientificNameAuthorship, to resolve them).  When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/57</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:316da14e-9477-4319-bd2c-c201f3b0f461</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:scientificNameID if it can be unambiguously resolved from bdq:sourceAuthority using the available taxon terms.Amedment for SingleRecord with Specification Specification for: AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:566faded-60b6-44bf-a335-dc78d5013582</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_33c45ae1-e2db-462a-a59e-7169bb01c5d6"></a>Term Name  bdqcore:33c45ae1-e2db-462a-a59e-7169bb01c5d6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_SEX_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/33c45ae1-e2db-462a-a59e-7169bb01c5d6-2024-03-25</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/33c45ae1-e2db-462a-a59e-7169bb01c5d6</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-03-25</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:sex Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:sex</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; AMENDED the value of dwc:sex if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:sex using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:sex="f": Response.status=AMENDED, Response.result=dwc:sex="Female", Response.comment="dwc:sex found in the bdq:sourceAuthority"],[dwc:sex="x": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:sex not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul> <li>GBIF (2015) Darwin Core Vocabulary: Sex GBIF Vocabulary. https://rs.gbif.org/vocabulary/gbif/sex.xml</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, a list of synonyms for dwc:sex values can be found at https://registry.gbif.org/vocabulary/Sex/concepts.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/284</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:97fb9cdf-68c2-4b0b-8b1d-351435d30722</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:sex using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_SEX_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:08a4abb0-8977-4805-a4a1-c1a96b532322</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_SEX_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_e39098df-ef46-464c-9aef-bcdeee2a88cb"></a>Term Name  bdqcore:e39098df-ef46-464c-9aef-bcdeee2a88cb</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_TAXONRANK_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/e39098df-ef46-464c-9aef-bcdeee2a88cb-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/e39098df-ef46-464c-9aef-bcdeee2a88cb</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:taxonRank Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; AMENDED the value of dwc:taxonRank if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:taxonRank using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonRank="sp.": Response.status=AMENDED, Response.result=dwc:taxonRank="species", Response.comment="dwc:taxonRank contains an interpretable value in the bdq:sourceAuthority"],[dwc:taxonRank="sic.": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:taxonRank does not contain an interpretable value in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Registry (2023) GBIF Vocabulary: Taxonomic Rank. https://registry.gbif.org/vocabulary/TaxonRank/concepts</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, information about possible values of dwc:taxonRank can be found at https://registry.gbif.org/vocabulary/TaxonRank/concepts</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/163</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:e9b8e041-3579-483a-a6aa-74bea442f6bd</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:taxonRank using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_TAXONRANK_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:ca6b9d39-4a1d-4ec5-925a-d1d67f95bea0</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_TAXONRANK_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b3471c65-b53e-453b-8282-abfa27bf1805"></a>Term Name  bdqcore:b3471c65-b53e-453b-8282-abfa27bf1805</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_TYPESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b3471c65-b53e-453b-8282-abfa27bf1805-2024-08-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b3471c65-b53e-453b-8282-abfa27bf1805</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Amendment dwc:typeStatus Standardized</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:typeStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; AMENDED the value of the first word in each \</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core typeStatus" {[https://dwc.tdwg.org/list/#dwc_typeStatus]} {dwc:typeStatus vocabulary API [https://gbif.github.io/parsers/apidocs/org/gbif/api/vocabulary/TypeStatus.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:typeStatus using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:typeStatus="Holo.": Response.status=AMENDED, Response.result=dwc:typeStatus="Holotype", Response.comment="dwc:typeStatus found in the bdq:sourceAuthority"],[dwc:typeStatus="x": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:typeStatus not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul> <li> GBIF (2021) Darwin Core Vocabulary: Nomenclatural Type Status Vocabulary. http://rs.gbif.org/vocabulary/gbif/type_status </li> </ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Valuable for data quality needs related to voucher specimens in natural science collections.   Almost all occurrence data will have no value in dwc:typeStatus.  For reference, a vocabulary of synonyms can be found for dwc:typeStatus at [https://registry.gbif.org/vocabulary/TypeStatus/concepts.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/286</td>
		</tr>
		<tr>
			<td>bdqffdq:AmendmentMethod</td>
			<td>urn:uuid:05104b96-267c-432a-9f30-88552404763e</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: Proposes an amendment to the value of dwc:typeStatus using the bdq:sourceAuthority.Amedment for SingleRecord with Specification Specification for: AMENDMENT_TYPESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:401e2562-cb26-43a7-8690-b06eabd5982a</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_TYPESTATUS_STANDARDIZED</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1"></a>Term Name  bdqcore:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_ANNOTATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-17</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Issue Annotation Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>oa:target</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>AllDarwinCoreTerms</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:annotationSystem,bdq:annotationAlertIf</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:annotationSystem is not available; POTENTIAL_ISSUE if an annotation in the bdq:annotationSystem exists with a matching bdq:annotationAlertIf; otherwise NOT_ISSUE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:annotationSystem default = "W3C Web Annotation" {[https://www.w3.org/annotation/]} {"oa:Annotation vocabulary" {[https://www.w3.org/TR/annotation-vocab/]},bdq:annotationAlertIf default = "oa:Annotation with oa:hasTarget having as object any dwciri:term instance that is part of the SingleRecord under test." {[https://www.w3.org/TR/annotation-vocab/]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are there any annotations associated with the record?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Reliability: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[bdq:annotationAlertIf="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="bdq:annotationAlertIf is bdq:Empty"],[bdq:annotationAlertIf="?": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="bdq:annotationAlertIf is bdq:NotEmpty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, Lee Belbin</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>W3C (2017) Web Annotation Data Model. https://www.w3.org/TR/annotation-model/</li><li>W3C (2017) Web Annotation Data Model: Annotation. https://www.w3.org/TR/annotation-vocab/#annotation</li><li>Biodiversity Information Standards (TDWG) (n.dat) Annotations Interest Group. https://www.tdwg.org/community/annotations/</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>While there is a W3C standard on 'web annotation', there is no TDWG recommendation on how this standard could be applied to annotating Darwin Core records.  While implementation of this test is currently problematic, TG2 considers annotations attached to any aspect of a Darwin Core record justifies this test as a placeholder in the hope of future developments.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/29</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_256e51b3-1e08-4349-bb7e-5186631c3f8e"></a>Term Name  bdqcore:256e51b3-1e08-4349-bb7e-5186631c3f8e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_COORDINATES_CENTEROFCOUNTRY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/256e51b3-1e08-4349-bb7e-5186631c3f8e-2024-08-28</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/256e51b3-1e08-4349-bb7e-5186631c3f8e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-28</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Issue Coordinates Center Of Country</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:countryCode,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:coordinateUncertaintyInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:spatialBufferInMeters,bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if any of dwc:countryCode, dwc:decimalLatitude, dwc:decimalLongitude are bdq:Empty; POTENTIAL_ISSUE if (1) the geographic coordinates are within the distance given by bdq:spatialBufferInMeters from the center of the supplied dwc:countryCode as represented in the bdq:sourceAuthority (or one of the centers, if the bdq:sourceAuthority provides more than one per country code) and (2) the dwc:coordinateUncertaintyInMeters is bdq:Empty or less than half the square root of the area of the country; otherwise NOT_ISSUE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:spatialBufferInMeters default = "5000",bdq:sourceAuthority default = "GBIF Catalogue of Country Centroides" {[https://raw.githubusercontent.com/jhnwllr/catalogue-of-centroids/master/PCLI.tsv]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are the supplied geographic coordinates within a defined buffer of the center of the country?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: centerofcountry</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Likely</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="-35.38804", dwc:decimalLongitude="-65.154964", dwc:countryCode="AR": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="coordinates fall within buffered distance in the bdq:sourceAuthority for dwc:countryCode"],[dwc:decimalLatitude="-34.184199", dwc:decimalLongitude="-65.509403", dwc:countryCode="AR": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="coordinates fall outside buffered distance in the bdq:sourceAuthority for dwc:countryCode"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul> <li> Waller JT (2023) Processing Country Centroids at the Global Biodiversity Information Facility. Biodiversity Information Science and Standards 7: e110728. https://doi.org/10.3897/biss.7.110728</li> </ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have increased the buffer to 5000 meters to cater for differences that may have arisen due to the difference in geodetic datums</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/287</td>
		</tr>
		<tr>
			<td>bdqffdq:IssueMethod</td>
			<td>urn:uuid:0239b59b-db0e-4e6a-8ba8-2f89abf9e78e</td>
		</tr>
		<tr>
			<td>IssueMethod label</td>
			<td>IssueMethod: Are the supplied geographic coordinates within a defined buffer of the center of the country? Criterion for SingleRecord with Specification Specification for: ISSUE_COORDINATES_CENTEROFCOUNTRY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:693aa9a5-6058-4399-a474-43268a8e503b</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: ISSUE_COORDINATES_CENTEROFCOUNTRY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_13d5a10e-188e-40fd-a22c-dbaa87b91df2"></a>Term Name  bdqcore:13d5a10e-188e-40fd-a22c-dbaa87b91df2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_DATAGENERALIZATIONS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/13d5a10e-188e-40fd-a22c-dbaa87b91df2-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Issue dwc:dataGeneralizations Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:dataGeneralizations</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>POTENTIAL_ISSUE if dwc:dataGeneralizations is bdq:NotEmpty; otherwise NOT_ISSUE</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:dataGeneralizations?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Resolution: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Resolution</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dataGeneralizations="placed on quarter degree grid": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="dwc:dataGeneralizations is bdq:NotEmpty"],[dwc:dataGeneralizations="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="dwc:dataGeneralizations is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD (2020) Current Best Practices for Generalizing Sensitive Species Occurrence Data. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-5jp4-5g10.</li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is not specific to spatial data, any value in the dwc:dataGeneralizations field will cause this flag to be raised, but the primary use case is expected to be that dwc:dataGeneralizations demonstrates obfuscated locations.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/72</td>
		</tr>
		<tr>
			<td>bdqffdq:IssueMethod</td>
			<td>urn:uuid:5daad04c-fd7c-4972-ac3a-66f149170bf3</td>
		</tr>
		<tr>
			<td>IssueMethod label</td>
			<td>IssueMethod: Is there a value in dwc:dataGeneralizations? Criterion for SingleRecord with Specification Specification for: ISSUE_DATAGENERALIZATIONS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:90618419-452d-4f35-b39a-7c342ca0791b</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: ISSUE_DATAGENERALIZATIONS_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_acc8dff2-d8d1-483a-946d-65a02a452700"></a>Term Name  bdqcore:acc8dff2-d8d1-483a-946d-65a02a452700</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/acc8dff2-d8d1-483a-946d-65a02a452700-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/acc8dff2-d8d1-483a-946d-65a02a452700</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Issue dwc:establishmentMeans Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:establishmentMeans</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>POTENTIAL_ISSUE if dwc:establishmentMeans is bdq:NotEmpty; otherwise NOT_ISSUE</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:establishmentMeans?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:establishmentMeans="?": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="dwc:establishmentMeans is bdq:NotEmpty"],[dwc:establishmentMeans="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="dwc:establishmentMeans is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, CRIA</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/94</td>
		</tr>
		<tr>
			<td>bdqffdq:IssueMethod</td>
			<td>urn:uuid:8fc9b64a-557b-46ee-aa51-d23b6cf26d75</td>
		</tr>
		<tr>
			<td>IssueMethod label</td>
			<td>IssueMethod: Is there a value in dwc:establishmentMeans? Criterion for SingleRecord with Specification Specification for: ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:c69007a2-6391-463e-96bc-baa18d24beb7</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_03049fe5-a575-404f-b564-ae63f5a1cf8b"></a>Term Name  bdqcore:03049fe5-a575-404f-b564-ae63f5a1cf8b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_AMENDMENTS_PROPOSED</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/03049fe5-a575-404f-b564-ae63f5a1cf8b-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/03049fe5-a575-404f-b564-ae63f5a1cf8b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measure Amendments Proposed</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>bdq:Amendment</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>bdq:AllAmendmentTestsRunOnSingleRecord"</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>The number of tests of output type AMENDMENT that have been run against the record and have proposed changes to the record (Result.status="AMENDED")</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>A count of the number of distinct AMENDMENT tests that have a Response.status="AMENDED" for a given record.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: proposed</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="17", Response.comment="17 tests of TYPE AMENDMENT were run and proposed changes to the record."]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>John Wieczorek</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/65</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_56b6c695-adf1-418e-95d2-da04cad7be53"></a>Term Name  bdqcore:56b6c695-adf1-418e-95d2-da04cad7be53</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_EVENTDATE_DURATIONINSECONDS</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/56b6c695-adf1-418e-95d2-da04cad7be53-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measure dwc:eventDate Duration In Seconds</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; otherwise RUN_HAS_RESULT with the result being the duration (sensu ISO 8601) expressed in the dwc:eventDate, in seconds.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>What is the duration of dwc:eventDate in seconds?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Resolution: durationinseconds</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Resolution</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1880-05-08/10": Response.status=RUN_HAS_RESULT, Response.result="259200", Response.comment="dwc:eventDate duration is 3 days = 259,200 seconds"],[dwc:eventDate="95": Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.result=NOT_REPORTED, Response.comment="dwc:eventDate does not contain a valid ISO 8601-1:2019 date"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Alex Thompson</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795).</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc v3.0.0 [DwCEventDQ.measureEventdateDurationinseconds()](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L109)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The duration of a day is 86400 seconds. Implementations should treat all days as 86400 seconds, but should include leap days (but not leap seconds) in durations that encompass them.  Consumers should treat assertions about event date duration as approximations, see: https://xkcd.com/2867/</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/140</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_45fb49eb-4a1b-4b49-876f-15d5034dfc73"></a>Term Name  bdqcore:45fb49eb-4a1b-4b49-876f-15d5034dfc73</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_VALIDATIONTESTS_COMPLIANT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/45fb49eb-4a1b-4b49-876f-15d5034dfc73-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/45fb49eb-4a1b-4b49-876f-15d5034dfc73</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measure Validation Tests Compliant</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>bdq:Validation</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>bdq:AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if no tests of type VALIDATION were attempted to be run; Report the number of tests of output type VALIDATION run against the record that were COMPLIANT (passed)</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measures the number of distinct VALIDATION tests that have a Response.status="COMPLIANT" for a given record.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Reliability: compliant</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="7", Response.comment="7 VALIDATION tests had Response.status="COMPLIANT" ]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of tests that were attempted, add all three measures. To get the total number of tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/135</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_453844ae-9df4-439f-8e24-c52498eca84a"></a>Term Name  bdqcore:453844ae-9df4-439f-8e24-c52498eca84a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_VALIDATIONTESTS_NOTCOMPLIANT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/453844ae-9df4-439f-8e24-c52498eca84a-2024-08-22</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/453844ae-9df4-439f-8e24-c52498eca84a</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-24</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-22</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measure Validation Tests Not Compliant</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>bdq:Validation</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>bdq:AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if no tests of type VALIDATION were attempted to be run; REPORT of the number of tests of output type VALIDATION run against the record that have Response.result="NOT_COMPLIANT"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>A count of the number of distinct VALIDATION tests that have a Response.status="NOT_COMPLIANT" for a given record.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Reliability: notcompliant</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="37", Response.comment="37 VALIDATION tests had Response.status="NOT_COMPLIANT."]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Lee Belbin</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of tests that were attempted, add all three measures. To get the total number of tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/31</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_49a94636-a562-4e6b-803c-665c80628a3d"></a>Term Name  bdqcore:49a94636-a562-4e6b-803c-665c80628a3d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/49a94636-a562-4e6b-803c-665c80628a3d-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/49a94636-a562-4e6b-803c-665c80628a3d</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measure Validation Tests Prerequisites Not Met</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>bdq:Validation</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>bdq:AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if no tests of type VALIDATION were run; Report the number of tests of output type VALIDATION that did not run because prerequisites for those tests were not met (Result.status="INTERNAL_PREREQUISITES_NOT_MET" or "EXTERNAL_PREREQUISITES_NOT_MET")</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>The number of distinct VALIDATION tests that have a Response.status="EXTERNAL_PREREQUISITES_NOT_MET" or "INTERNAL_PREREQUISITES_NOT_MET" for a given record.</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: prerequisitesnotmet</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="27", Response.comment="27 VALIDATION tests had either INTERNAL_PREREQUISITES_NOT_MET" or "EXTERNAL_PREREQUISITES_NOT_MET"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of tests that were attempted, add all three measures. To get the total number of tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/134</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63"></a>Term Name  bdqcore:8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Vaildation dwc:geodeticDatum Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index#/Datum]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b21256c2-4bb7-4deb-852d-a9eaa05345e7"></a>Term Name  bdqcore:b21256c2-4bb7-4deb-852d-a9eaa05345e7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b21256c2-4bb7-4deb-852d-a9eaa05345e7-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b21256c2-4bb7-4deb-852d-a9eaa05345e7</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation  dwc:minimumDepthInMeters Less Than dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: maxdepth</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a56fb342-c8ee-4611-8aab-e6c6357e8875"></a>Term Name  bdqcore:a56fb342-c8ee-4611-8aab-e6c6357e8875</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a56fb342-c8ee-4611-8aab-e6c6357e8875-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a56fb342-c8ee-4611-8aab-e6c6357e8875</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Classification Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_CLASSIFICATION_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_CLASSIFICATION_CONSISTENT in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c439952b-fb00-4902-90b3-a9d477c11a0b"></a>Term Name  bdqcore:c439952b-fb00-4902-90b3-a9d477c11a0b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c439952b-fb00-4902-90b3-a9d477c11a0b-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c439952b-fb00-4902-90b3-a9d477c11a0b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-26</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b89b8424-91eb-4fd1-a6c3-1b0bc92120d0"></a>Term Name  bdqcore:b89b8424-91eb-4fd1-a6c3-1b0bc92120d0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b89b8424-91eb-4fd1-a6c3-1b0bc92120d0-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b89b8424-91eb-4fd1-a6c3-1b0bc92120d0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates dwc:stateProvince Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0e239a55-0f19-4c68-bdbf-20580f27a647"></a>Term Name  bdqcore:0e239a55-0f19-4c68-bdbf-20580f27a647</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0e239a55-0f19-4c68-bdbf-20580f27a647-2023-06-20</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0e239a55-0f19-4c68-bdbf-20580f27a647</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-06-20</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates Not Zero</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATES_NOTZERO.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COORDINATES_NOTZERO in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATES_NOTZERO in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Likeliness: notzero</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_25b5d4bf-c871-4485-a457-68021dce0367"></a>Term Name  bdqcore:25b5d4bf-c871-4485-a457-68021dce0367</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/25b5d4bf-c871-4485-a457-68021dce0367-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/25b5d4bf-c871-4485-a457-68021dce0367</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates Terrestrial Marine</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:taxonIsMarine default = "World Register of Marine Species (WoRMS)" {[https://www.marinespecies.org/]} {Web service [https://www.marinespecies.org/aphia.php?p=webservice]},bdq:geospatialLand default = "Union of NaturalEarth 10m-physical-vectors for Land and NaturalEarth Minor Islands" {[https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip], [https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_minor_islands.zip]},bdq:spatialBufferInMeters default = "3000",bdq:assumptionOnUnknownBiome default = "noassumption"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f041ab17-d834-4586-aa6b-090de2e571a8"></a>Term Name  bdqcore:f041ab17-d834-4586-aa6b-090de2e571a8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f041ab17-d834-4586-aa6b-090de2e571a8-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f041ab17-d834-4586-aa6b-090de2e571a8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dc:type Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DCTYPE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DCTYPE_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_fbe47441-500f-44c7-a1bd-1e872edc5266"></a>Term Name  bdqcore:fbe47441-500f-44c7-a1bd-1e872edc5266</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/fbe47441-500f-44c7-a1bd-1e872edc5266-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/fbe47441-500f-44c7-a1bd-1e872edc5266</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dc:type Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DCTYPE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List Of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DCTYPE_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_47ee20d9-5087-4f76-a494-6fea05e50b8b"></a>Term Name  bdqcore:47ee20d9-5087-4f76-a494-6fea05e50b8b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/47ee20d9-5087-4f76-a494-6fea05e50b8b-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/47ee20d9-5087-4f76-a494-6fea05e50b8b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dcterms:license Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_LICENSE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_LICENSE_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_9d5be694-f5da-465d-8c7e-27e6dac69f9f"></a>Term Name  bdqcore:9d5be694-f5da-465d-8c7e-27e6dac69f9f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/9d5be694-f5da-465d-8c7e-27e6dac69f9f-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/9d5be694-f5da-465d-8c7e-27e6dac69f9f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dcterms:license Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_LICENSE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Creative Commons 4.0 Licenses or CC0 {[https://creativecommons.org/]} { Regular Expression [((http(s){0,1}://creativecommons.org/licenses/(by\</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_LICENSE_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_bac852b5-1ba6-427b-aa8e-02018e99279c"></a>Term Name  bdqcore:bac852b5-1ba6-427b-aa8e-02018e99279c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/bac852b5-1ba6-427b-aa8e-02018e99279c-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/bac852b5-1ba6-427b-aa8e-02018e99279c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dcterms:Location Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_LOCATION_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_LOCATION_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_LOCATION_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b60c8c58-0137-4b6a-97e9-57d8ca5cf248"></a>Term Name  bdqcore:b60c8c58-0137-4b6a-97e9-57d8ca5cf248</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b60c8c58-0137-4b6a-97e9-57d8ca5cf248-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b60c8c58-0137-4b6a-97e9-57d8ca5cf248</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:basisOfRecord Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f5dd74bd-6a22-4792-b675-c7ccf2a2c103"></a>Term Name  bdqcore:f5dd74bd-6a22-4792-b675-c7ccf2a2c103</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f5dd74bd-6a22-4792-b675-c7ccf2a2c103-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f5dd74bd-6a22-4792-b675-c7ccf2a2c103</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:basisOfRecord Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]}{dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7270a362-5f2e-41f0-955a-d7a8eaaf0f17"></a>Term Name  bdqcore:7270a362-5f2e-41f0-955a-d7a8eaaf0f17</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7270a362-5f2e-41f0-955a-d7a8eaaf0f17-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7270a362-5f2e-41f0-955a-d7a8eaaf0f17</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:class Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_CLASS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_CLASS_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_CLASS_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_2d90d94b-d384-4bac-aa68-c6800d765882"></a>Term Name  bdqcore:2d90d94b-d384-4bac-aa68-c6800d765882</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/2d90d94b-d384-4bac-aa68-c6800d765882-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/2d90d94b-d384-4bac-aa68-c6800d765882</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:coordinateUncertaintyInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COORDINATEUNCERTAINTY_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_18b9d086-29ae-42a5-8f0a-4bc86f4e87ad"></a>Term Name  bdqcore:18b9d086-29ae-42a5-8f0a-4bc86f4e87ad</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/18b9d086-29ae-42a5-8f0a-4bc86f4e87ad-2024-09-25</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/18b9d086-29ae-42a5-8f0a-4bc86f4e87ad</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_8b73f37d-89ed-479a-8389-9e71ad2ac84d"></a>Term Name  bdqcore:8b73f37d-89ed-479a-8389-9e71ad2ac84d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/8b73f37d-89ed-479a-8389-9e71ad2ac84d-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/8b73f37d-89ed-479a-8389-9e71ad2ac84d</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country dwc:stateProvince Unambiguous</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: unambiguous</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f15c38c3-d96d-4e9c-982d-410fb71cf2bc"></a>Term Name  bdqcore:f15c38c3-d96d-4e9c-982d-410fb71cf2bc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f15c38c3-d96d-4e9c-982d-410fb71cf2bc-2024-08-19</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f15c38c3-d96d-4e9c-982d-410fb71cf2bc</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-24</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-19</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COUNTRY_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRY_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6887c881-dc52-409b-8979-9c2f05e55569"></a>Term Name  bdqcore:6887c881-dc52-409b-8979-9c2f05e55569</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6887c881-dc52-409b-8979-9c2f05e55569-2024-09-27</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6887c881-dc52-409b-8979-9c2f05e55569</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COUNTRY_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRY_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_d71be8d4-1a04-4816-90c5-49808c823651"></a>Term Name  bdqcore:d71be8d4-1a04-4816-90c5-49808c823651</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/d71be8d4-1a04-4816-90c5-49808c823651-2024-09-27</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/d71be8d4-1a04-4816-90c5-49808c823651</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:countryCode Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_38966850-3737-4a67-953c-c231469e0489"></a>Term Name  bdqcore:38966850-3737-4a67-953c-c231469e0489</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/38966850-3737-4a67-953c-c231469e0489-2024-09-19</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/38966850-3737-4a67-953c-c231469e0489</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-19</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c72fda2d-16e1-4ded-91a5-a7094339d603"></a>Term Name  bdqcore:c72fda2d-16e1-4ded-91a5-a7094339d603</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c72fda2d-16e1-4ded-91a5-a7094339d603-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c72fda2d-16e1-4ded-91a5-a7094339d603</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:dateIdentified In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Identification</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>,bdq:earliestValidDate default="1753-01-01",bdq:latestValidDate default=[current day],bdq:includeEventDate default=true</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Likeliness: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_49b787eb-7dce-4ace-97f5-7cbb47cd8cb9"></a>Term Name  bdqcore:49b787eb-7dce-4ace-97f5-7cbb47cd8cb9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/49b787eb-7dce-4ace-97f5-7cbb47cd8cb9-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/49b787eb-7dce-4ace-97f5-7cbb47cd8cb9</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Identification</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_780480ff-8c4a-4276-aaca-cbd1248de9fa"></a>Term Name  bdqcore:780480ff-8c4a-4276-aaca-cbd1248de9fa</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/780480ff-8c4a-4276-aaca-cbd1248de9fa-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/780480ff-8c4a-4276-aaca-cbd1248de9fa</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:day In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DAY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DAY_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DAY_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c3e0100f-dfc3-4379-a855-df878eef295e"></a>Term Name  bdqcore:c3e0100f-dfc3-4379-a855-df878eef295e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c3e0100f-dfc3-4379-a855-df878eef295e-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c3e0100f-dfc3-4379-a855-df878eef295e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:day Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DAY_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DAY_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26"></a>Term Name  bdqcore:f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLatitude In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_bceae35a-52ab-4968-846f-069ace766513"></a>Term Name  bdqcore:bceae35a-52ab-4968-846f-069ace766513</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/bceae35a-52ab-4968-846f-069ace766513-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/bceae35a-52ab-4968-846f-069ace766513</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLatitude Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c70c4950-2246-4acc-a59d-81eaa47edf2b"></a>Term Name  bdqcore:c70c4950-2246-4acc-a59d-81eaa47edf2b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c70c4950-2246-4acc-a59d-81eaa47edf2b-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c70c4950-2246-4acc-a59d-81eaa47edf2b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLongitude In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f948a30e-8084-48d5-b1ca-d77c476f181f"></a>Term Name  bdqcore:f948a30e-8084-48d5-b1ca-d77c476f181f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f948a30e-8084-48d5-b1ca-d77c476f181f-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f948a30e-8084-48d5-b1ca-d77c476f181f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLongitude Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_1b8ae68e-63f1-41c0-9025-fbe64db38d64"></a>Term Name  bdqcore:1b8ae68e-63f1-41c0-9025-fbe64db38d64</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/1b8ae68e-63f1-41c0-9025-fbe64db38d64-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/1b8ae68e-63f1-41c0-9025-fbe64db38d64</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:degreeofEstablishment Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7775309b-5331-4a65-b839-cbe959948d33"></a>Term Name  bdqcore:7775309b-5331-4a65-b839-cbe959948d33</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7775309b-5331-4a65-b839-cbe959948d33-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7775309b-5331-4a65-b839-cbe959948d33</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:endDayOfYear In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_ENDDAYOFYEAR_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_ENDDAYOFYEAR_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_130bb875-6b7c-4965-b864-d53f9d05b2cd"></a>Term Name  bdqcore:130bb875-6b7c-4965-b864-d53f9d05b2cd</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/130bb875-6b7c-4965-b864-d53f9d05b2cd-2024-02-08</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/130bb875-6b7c-4965-b864-d53f9d05b2cd</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-08</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:establishmentMeans Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_ESTABLISHMENTMEANS_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_1919f212-b7db-4b6e-9697-41a715001bd6"></a>Term Name  bdqcore:1919f212-b7db-4b6e-9697-41a715001bd6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/1919f212-b7db-4b6e-9697-41a715001bd6-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/1919f212-b7db-4b6e-9697-41a715001bd6</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Event Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENT_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_EVENT_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENT_CONSISTENT in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4a1fa336-dd47-4b60-a7b0-c958e2dc72cd"></a>Term Name  bdqcore:4a1fa336-dd47-4b60-a7b0-c958e2dc72cd</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4a1fa336-dd47-4b60-a7b0-c958e2dc72cd-2023-09-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4a1fa336-dd47-4b60-a7b0-c958e2dc72cd</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Event Temporal Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_EVENTTEMPORAL_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c8250600-de61-4047-9d7c-6e06a38c7994"></a>Term Name  bdqcore:c8250600-de61-4047-9d7c-6e06a38c7994</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c8250600-de61-4047-9d7c-6e06a38c7994-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c8250600-de61-4047-9d7c-6e06a38c7994</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_EVENTDATE_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:earliestValidDate default ="1582-11-15",bdq:latestValidDate default = current year</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTDATE_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3f62eaa2-747f-456b-85e6-1a6e74086a18"></a>Term Name  bdqcore:3f62eaa2-747f-456b-85e6-1a6e74086a18</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3f62eaa2-747f-456b-85e6-1a6e74086a18-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3f62eaa2-747f-456b-85e6-1a6e74086a18</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_EVENTDATE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTDATE_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_bffd7499-aca3-423f-bb43-f7bdc9260f4f"></a>Term Name  bdqcore:bffd7499-aca3-423f-bb43-f7bdc9260f4f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/bffd7499-aca3-423f-bb43-f7bdc9260f4f-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/bffd7499-aca3-423f-bb43-f7bdc9260f4f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_EVENTDATE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTDATE_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_97928242-11a9-4ab0-9dd7-3f0465834824"></a>Term Name  bdqcore:97928242-11a9-4ab0-9dd7-3f0465834824</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/97928242-11a9-4ab0-9dd7-3f0465834824-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/97928242-11a9-4ab0-9dd7-3f0465834824</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-17</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:family Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_FAMILY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_FAMILY_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_FAMILY_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_977f7e75-a88e-4e29-a7b1-e8cdd35aa107"></a>Term Name  bdqcore:977f7e75-a88e-4e29-a7b1-e8cdd35aa107</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/977f7e75-a88e-4e29-a7b1-e8cdd35aa107-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/977f7e75-a88e-4e29-a7b1-e8cdd35aa107</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:genus Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_GENUS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_GENUS_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_GENUS_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_63fbaf3c-3d41-4ab6-bfc0-904f1b26835f"></a>Term Name  bdqcore:63fbaf3c-3d41-4ab6-bfc0-904f1b26835f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/63fbaf3c-3d41-4ab6-bfc0-904f1b26835f-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/63fbaf3c-3d41-4ab6-bfc0-904f1b26835f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:geodeticDatum Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_012eade5-fc64-458a-a13a-a614491bf4e0"></a>Term Name  bdqcore:012eade5-fc64-458a-a13a-a614491bf4e0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/012eade5-fc64-458a-a13a-a614491bf4e0-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/012eade5-fc64-458a-a13a-a614491bf4e0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:kingdom Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_KINGDOM_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_KINGDOM_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_342bd81c-e2b7-41d8-b32b-013992d19f99"></a>Term Name  bdqcore:342bd81c-e2b7-41d8-b32b-013992d19f99</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/342bd81c-e2b7-41d8-b32b-013992d19f99-2024-01-28</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/342bd81c-e2b7-41d8-b32b-013992d19f99</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-01-28</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:kingdom Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_KINGDOM_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_KINGDOM_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3de8af03-05d4-4fd8-8e6d-ba886dc5446f"></a>Term Name  bdqcore:3de8af03-05d4-4fd8-8e6d-ba886dc5446f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3de8af03-05d4-4fd8-8e6d-ba886dc5446f-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3de8af03-05d4-4fd8-8e6d-ba886dc5446f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:maximumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MAXDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_MAXDEPTH_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MAXDEPTH_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5"></a>Term Name  bdqcore:6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:maximumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MAXELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_MAXELEVATION_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MAXELEVATION_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_9c66c116-6644-45b4-b4c7-db7a4ee7c500"></a>Term Name  bdqcore:9c66c116-6644-45b4-b4c7-db7a4ee7c500</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/9c66c116-6644-45b4-b4c7-db7a4ee7c500-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/9c66c116-6644-45b4-b4c7-db7a4ee7c500</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:minimumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_MINDEPTH_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINDEPTH_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_071267a0-d993-4961-a3f7-d8210810d167"></a>Term Name  bdqcore:071267a0-d993-4961-a3f7-d8210810d167</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/071267a0-d993-4961-a3f7-d8210810d167-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/071267a0-d993-4961-a3f7-d8210810d167</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:minimumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_MINELEVATION_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINELEVATION_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_be2eb717-b390-47d1-b7ba-965a1101e215"></a>Term Name  bdqcore:be2eb717-b390-47d1-b7ba-965a1101e215</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/be2eb717-b390-47d1-b7ba-965a1101e215-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/be2eb717-b390-47d1-b7ba-965a1101e215</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:minimumElevationInMeters Less Than dwcmaximumElevationInMeters</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: maxelevation</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3"></a>Term Name  bdqcore:c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:month Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MONTH_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_MONTH_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MONTH_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_36ea0a78-a079-4014-aca3-2f2b3b11e822"></a>Term Name  bdqcore:36ea0a78-a079-4014-aca3-2f2b3b11e822</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/36ea0a78-a079-4014-aca3-2f2b3b11e822-2024-02-07</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/36ea0a78-a079-4014-aca3-2f2b3b11e822</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-07</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:namePublishedInYear Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0c9a139e-5d23-44de-a495-14ec08c61a1c"></a>Term Name  bdqcore:0c9a139e-5d23-44de-a495-14ec08c61a1c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0c9a139e-5d23-44de-a495-14ec08c61a1c-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0c9a139e-5d23-44de-a495-14ec08c61a1c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceID Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_OCCURRENCEID_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_OCCURRENCEID_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_298db0c9-a85a-41ee-b111-d622fd969d71"></a>Term Name  bdqcore:298db0c9-a85a-41ee-b111-d622fd969d71</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/298db0c9-a85a-41ee-b111-d622fd969d71-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/298db0c9-a85a-41ee-b111-d622fd969d71</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceStatus Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_faca6558-dbff-4d26-a5cb-e11cdf632fe7"></a>Term Name  bdqcore:faca6558-dbff-4d26-a5cb-e11cdf632fe7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/faca6558-dbff-4d26-a5cb-e11cdf632fe7-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/faca6558-dbff-4d26-a5cb-e11cdf632fe7</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceStatus Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF OccurrenceStatus Vocabulary" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus]} {"dwc:occurrenceStatus vocabulary API" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f4fa449c-4b74-4dcf-b4cf-0b73e1496375"></a>Term Name  bdqcore:f4fa449c-4b74-4dcf-b4cf-0b73e1496375</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f4fa449c-4b74-4dcf-b4cf-0b73e1496375-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f4fa449c-4b74-4dcf-b4cf-0b73e1496375</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:order Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_ORDER_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_ORDER_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_ORDER_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_15e0da1d-1a43-4075-8454-b2e618cdd25b"></a>Term Name  bdqcore:15e0da1d-1a43-4075-8454-b2e618cdd25b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/15e0da1d-1a43-4075-8454-b2e618cdd25b-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/15e0da1d-1a43-4075-8454-b2e618cdd25b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:pathway Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_PATHWAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_PATHWAY_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_PATHWAY_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_65e66ca0-e9d1-4411-ad26-bb9c43f32afc"></a>Term Name  bdqcore:65e66ca0-e9d1-4411-ad26-bb9c43f32afc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/65e66ca0-e9d1-4411-ad26-bb9c43f32afc-2022-03-25</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/65e66ca0-e9d1-4411-ad26-bb9c43f32afc</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2022-03-25</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:phylum Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_PHYLUM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_PHYLUM_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_PHYLUM_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4e70b0e4-3fd2-4899-802c-439671374eeb"></a>Term Name  bdqcore:4e70b0e4-3fd2-4899-802c-439671374eeb</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4e70b0e4-3fd2-4899-802c-439671374eeb-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4e70b0e4-3fd2-4899-802c-439671374eeb</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificName Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0f8b30e2-59dc-46ba-8b91-62049cd1a4e2"></a>Term Name  bdqcore:0f8b30e2-59dc-46ba-8b91-62049cd1a4e2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0f8b30e2-59dc-46ba-8b91-62049cd1a4e2-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0f8b30e2-59dc-46ba-8b91-62049cd1a4e2</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificName Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_dbf3cece-1d83-426e-a5e0-8158fcf9c0cd"></a>Term Name  bdqcore:dbf3cece-1d83-426e-a5e0-8158fcf9c0cd</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/dbf3cece-1d83-426e-a5e0-8158fcf9c0cd-2024-02-04</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/dbf3cece-1d83-426e-a5e0-8158fcf9c0cd</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-04</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameAuthorship Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f174ad13-3c67-49f9-8d8b-aba4e933d6f6"></a>Term Name  bdqcore:f174ad13-3c67-49f9-8d8b-aba4e933d6f6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f174ad13-3c67-49f9-8d8b-aba4e933d6f6-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f174ad13-3c67-49f9-8d8b-aba4e933d6f6</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameID Complete</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_COMPLETE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: complete</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a9962d33-ad08-453a-8938-2972425034c2"></a>Term Name  bdqcore:a9962d33-ad08-453a-8938-2972425034c2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a9962d33-ad08-453a-8938-2972425034c2-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a9962d33-ad08-453a-8938-2972425034c2</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameID Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_e4d35063-2366-4dda-8eaa-326340361da3"></a>Term Name  bdqcore:e4d35063-2366-4dda-8eaa-326340361da3</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/e4d35063-2366-4dda-8eaa-326340361da3-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/e4d35063-2366-4dda-8eaa-326340361da3</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:sex Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SEX_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_SEX_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SEX_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_76008c6b-c56a-4233-84e3-8584950037ec"></a>Term Name  bdqcore:76008c6b-c56a-4233-84e3-8584950037ec</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/76008c6b-c56a-4233-84e3-8584950037ec-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/76008c6b-c56a-4233-84e3-8584950037ec</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:startDayOfYear In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_STARTDAYOFYEAR_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_STARTDAYOFYEAR_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_58fdd5c1-6201-49a1-a7cd-f49c210dc0b6"></a>Term Name  bdqcore:58fdd5c1-6201-49a1-a7cd-f49c210dc0b6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/58fdd5c1-6201-49a1-a7cd-f49c210dc0b6-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/58fdd5c1-6201-49a1-a7cd-f49c210dc0b6</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:stateProvince Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_STATEPROVINCE_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_STATEPROVINCE_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_STATEPROVINCE_FOUND in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_54d290e8-ac48-4f31-8af3-676363573217"></a>Term Name  bdqcore:54d290e8-ac48-4f31-8af3-676363573217</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/54d290e8-ac48-4f31-8af3-676363573217-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/54d290e8-ac48-4f31-8af3-676363573217</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Taxon Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_TAXON_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXON_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_782773c9-7b37-483d-8ce2-c6683ba81882"></a>Term Name  bdqcore:782773c9-7b37-483d-8ce2-c6683ba81882</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/782773c9-7b37-483d-8ce2-c6683ba81882-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/782773c9-7b37-483d-8ce2-c6683ba81882</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Taxon Unambiguous</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_TAXON_UNAMBIGUOUS in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXON_UNAMBIGUOUS in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: unambiguous</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_de661615-b338-4557-af5b-d44a89de40fa"></a>Term Name  bdqcore:de661615-b338-4557-af5b-d44a89de40fa</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/de661615-b338-4557-af5b-d44a89de40fa-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/de661615-b338-4557-af5b-d44a89de40fa</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:taxonRank Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_TAXONRANK_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXONRANK_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_602bc457-6b1d-4f24-adef-d0d31bcdf2f0"></a>Term Name  bdqcore:602bc457-6b1d-4f24-adef-d0d31bcdf2f0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/602bc457-6b1d-4f24-adef-d0d31bcdf2f0-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/602bc457-6b1d-4f24-adef-d0d31bcdf2f0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:taxonRank Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_TAXONRANK_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXONRANK_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b5a14d76-292e-499b-b80f-9546243311a0"></a>Term Name  bdqcore:b5a14d76-292e-499b-b80f-9546243311a0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b5a14d76-292e-499b-b80f-9546243311a0-2024-08-03</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b5a14d76-292e-499b-b80f-9546243311a0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-03</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:typeStatus Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TYPESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_TYPESTATUS_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core typeStatus" {[https://dwc.tdwg.org/list/#dwc_typeStatus]} {dwc:typeStatus vocabulary API [https://gbif.github.io/parsers/apidocs/org/gbif/api/vocabulary/TypeStatus.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TYPESTATUS_STANDARD in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_aee65eb8-8d1e-4b8f-bd37-5822e29f5734"></a>Term Name  bdqcore:aee65eb8-8d1e-4b8f-bd37-5822e29f5734</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/aee65eb8-8d1e-4b8f-bd37-5822e29f5734-2024-08-23</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/aee65eb8-8d1e-4b8f-bd37-5822e29f5734</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-23</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:year In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_YEAR_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:earliestValidDate="1582",bdq:latestValidDate=current year</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_YEAR_INRANGE in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_687d3ad1-93a3-4a1f-b69f-da5a1eb761a5"></a>Term Name  bdqcore:687d3ad1-93a3-4a1f-b69f-da5a1eb761a5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/687d3ad1-93a3-4a1f-b69f-da5a1eb761a5-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/687d3ad1-93a3-4a1f-b69f-da5a1eb761a5</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:year Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_YEAR_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_YEAR_NOTEMPTY in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7da5428e-87b2-4ec2-be82-05b9398b7577"></a>Term Name  bdqcore:7da5428e-87b2-4ec2-be82-05b9398b7577</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7da5428e-87b2-4ec2-be82-05b9398b7577-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7da5428e-87b2-4ec2-be82-05b9398b7577</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Polynomial Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>Count the number of VALIDATION_POLYNOMIAL_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_POLYNOMIAL_CONSISTENT in a record set that are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e"></a>Term Name  bdqcore:cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Vaildation dwc:geodeticDatum Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_GEODETICDATUM_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index#/Datum]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_GEODETICDATUM_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_fcabd2c9-392c-4841-a5d7-e2680c9587ab"></a>Term Name  bdqcore:fcabd2c9-392c-4841-a5d7-e2680c9587ab</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/fcabd2c9-392c-4841-a5d7-e2680c9587ab-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/fcabd2c9-392c-4841-a5d7-e2680c9587ab</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation  dwc:minimumDepthInMeters Less Than dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: maxdepth</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a2be4734-0a93-46dc-af4a-e2125b47dbd4"></a>Term Name  bdqcore:a2be4734-0a93-46dc-af4a-e2125b47dbd4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a2be4734-0a93-46dc-af4a-e2125b47dbd4-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a2be4734-0a93-46dc-af4a-e2125b47dbd4</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Classification Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_CLASSIFICATION_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_CLASSIFICATION_CONSISTENT in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_1ede76d0-c096-465c-8bbb-08c53bf7e367"></a>Term Name  bdqcore:1ede76d0-c096-465c-8bbb-08c53bf7e367</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/1ede76d0-c096-465c-8bbb-08c53bf7e367-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/1ede76d0-c096-465c-8bbb-08c53bf7e367</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-26</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_9ff65ace-9d16-4393-b90f-9150d9628371"></a>Term Name  bdqcore:9ff65ace-9d16-4393-b90f-9150d9628371</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/9ff65ace-9d16-4393-b90f-9150d9628371-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/9ff65ace-9d16-4393-b90f-9150d9628371</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates dwc:stateProvince Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_151b2d29-3460-4ba5-a226-86971dc8ad03"></a>Term Name  bdqcore:151b2d29-3460-4ba5-a226-86971dc8ad03</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/151b2d29-3460-4ba5-a226-86971dc8ad03-2023-06-20</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/151b2d29-3460-4ba5-a226-86971dc8ad03</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-06-20</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates Not Zero</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATES_NOTZERO.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COORDINATES_NOTZERO in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATES_NOTZERO in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Likeliness: notzero</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_fb3732c6-4199-4767-a263-0363a1fe1766"></a>Term Name  bdqcore:fb3732c6-4199-4767-a263-0363a1fe1766</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/fb3732c6-4199-4767-a263-0363a1fe1766-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/fb3732c6-4199-4767-a263-0363a1fe1766</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates Terrestrial Marine</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:taxonIsMarine default = "World Register of Marine Species (WoRMS)" {[https://www.marinespecies.org/]} {Web service [https://www.marinespecies.org/aphia.php?p=webservice]},bdq:geospatialLand default = "Union of NaturalEarth 10m-physical-vectors for Land and NaturalEarth Minor Islands" {[https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip], [https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_minor_islands.zip]},bdq:spatialBufferInMeters default = "3000",bdq:assumptionOnUnknownBiome default = "noassumption"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4d999a65-a431-4a76-b591-e0d86dcf244b"></a>Term Name  bdqcore:4d999a65-a431-4a76-b591-e0d86dcf244b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4d999a65-a431-4a76-b591-e0d86dcf244b-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4d999a65-a431-4a76-b591-e0d86dcf244b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dc:type Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DCTYPE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DCTYPE_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_d9493fa0-d90e-41db-95f6-d1c1d243540e"></a>Term Name  bdqcore:d9493fa0-d90e-41db-95f6-d1c1d243540e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/d9493fa0-d90e-41db-95f6-d1c1d243540e-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/d9493fa0-d90e-41db-95f6-d1c1d243540e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dc:type Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DCTYPE_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List Of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DCTYPE_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4fccf163-9336-4f48-996c-57f5f66e72db"></a>Term Name  bdqcore:4fccf163-9336-4f48-996c-57f5f66e72db</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4fccf163-9336-4f48-996c-57f5f66e72db-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4fccf163-9336-4f48-996c-57f5f66e72db</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dcterms:license Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_LICENSE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_LICENSE_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_acd8d43e-7a2a-4372-b887-fb53a9972dc9"></a>Term Name  bdqcore:acd8d43e-7a2a-4372-b887-fb53a9972dc9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/acd8d43e-7a2a-4372-b887-fb53a9972dc9-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/acd8d43e-7a2a-4372-b887-fb53a9972dc9</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dcterms:license Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_LICENSE_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Creative Commons 4.0 Licenses or CC0 {[https://creativecommons.org/]} { Regular Expression [((http(s){0,1}://creativecommons.org/licenses/(by\</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_LICENSE_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3b2e4791-1a5a-4087-9e8d-09c67cf8c816"></a>Term Name  bdqcore:3b2e4791-1a5a-4087-9e8d-09c67cf8c816</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3b2e4791-1a5a-4087-9e8d-09c67cf8c816-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3b2e4791-1a5a-4087-9e8d-09c67cf8c816</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dcterms:Location Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_LOCATION_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_LOCATION_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_LOCATION_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8"></a>Term Name  bdqcore:c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:basisOfRecord Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_BASISOFRECORD_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_BASISOFRECORD_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_241a279c-76d5-499b-ab49-a47ad7f8df50"></a>Term Name  bdqcore:241a279c-76d5-499b-ab49-a47ad7f8df50</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/241a279c-76d5-499b-ab49-a47ad7f8df50-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/241a279c-76d5-499b-ab49-a47ad7f8df50</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:basisOfRecord Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_BASISOFRECORD_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]}{dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_BASISOFRECORD_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_21541436-641d-45a9-938c-537484d94eb7"></a>Term Name  bdqcore:21541436-641d-45a9-938c-537484d94eb7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/21541436-641d-45a9-938c-537484d94eb7-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/21541436-641d-45a9-938c-537484d94eb7</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:class Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_CLASS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_CLASS_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_CLASS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_d94b0130-7a13-4fa8-955c-eff5c47bd9de"></a>Term Name  bdqcore:d94b0130-7a13-4fa8-955c-eff5c47bd9de</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/d94b0130-7a13-4fa8-955c-eff5c47bd9de-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/d94b0130-7a13-4fa8-955c-eff5c47bd9de</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:coordinateUncertaintyInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COORDINATEUNCERTAINTY_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c6a62914-f42e-442a-9e2b-38ccff594070"></a>Term Name  bdqcore:c6a62914-f42e-442a-9e2b-38ccff594070</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c6a62914-f42e-442a-9e2b-38ccff594070-2024-09-25</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c6a62914-f42e-442a-9e2b-38ccff594070</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_23aced89-d613-479c-bc4c-837d74b73be0"></a>Term Name  bdqcore:23aced89-d613-479c-bc4c-837d74b73be0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/23aced89-d613-479c-bc4c-837d74b73be0-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/23aced89-d613-479c-bc4c-837d74b73be0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country dwc:stateProvince Unambiguous</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: unambiguous</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_388e74b3-2e18-4d78-8112-3142d1177e25"></a>Term Name  bdqcore:388e74b3-2e18-4d78-8112-3142d1177e25</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/388e74b3-2e18-4d78-8112-3142d1177e25-2024-08-19</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/388e74b3-2e18-4d78-8112-3142d1177e25</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-24</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-19</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COUNTRY_FOUND in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRY_FOUND in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_9c8df974-8fba-4537-8c67-31466787f732"></a>Term Name  bdqcore:9c8df974-8fba-4537-8c67-31466787f732</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/9c8df974-8fba-4537-8c67-31466787f732-2024-09-27</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/9c8df974-8fba-4537-8c67-31466787f732</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COUNTRY_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRY_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_942f63bd-d19d-4214-bf8e-cec0055b8909"></a>Term Name  bdqcore:942f63bd-d19d-4214-bf8e-cec0055b8909</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/942f63bd-d19d-4214-bf8e-cec0055b8909-2024-09-27</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/942f63bd-d19d-4214-bf8e-cec0055b8909</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:countryCode Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COUNTRYCODE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYCODE_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_fedf27b2-e01d-459f-98fc-7f0f39e3d4be"></a>Term Name  bdqcore:fedf27b2-e01d-459f-98fc-7f0f39e3d4be</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/fedf27b2-e01d-459f-98fc-7f0f39e3d4be-2024-09-19</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/fedf27b2-e01d-459f-98fc-7f0f39e3d4be</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-19</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_COUNTRYCODE_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYCODE_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6354376c-0cf2-435b-be40-850769c5a18a"></a>Term Name  bdqcore:6354376c-0cf2-435b-be40-850769c5a18a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6354376c-0cf2-435b-be40-850769c5a18a-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6354376c-0cf2-435b-be40-850769c5a18a</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:dateIdentified In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Identification</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DATEIDENTIFIED_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>,bdq:earliestValidDate default="1753-01-01",bdq:latestValidDate default=[current day],bdq:includeEventDate default=true</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DATEIDENTIFIED_INRANGE in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Likeliness: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_563872eb-f544-45a0-8f91-8098d62768d4"></a>Term Name  bdqcore:563872eb-f544-45a0-8f91-8098d62768d4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/563872eb-f544-45a0-8f91-8098d62768d4-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/563872eb-f544-45a0-8f91-8098d62768d4</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Identification</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DATEIDENTIFIED_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DATEIDENTIFIED_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_85dc5d02-9847-420f-a026-6a0e70962d2a"></a>Term Name  bdqcore:85dc5d02-9847-420f-a026-6a0e70962d2a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/85dc5d02-9847-420f-a026-6a0e70962d2a-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/85dc5d02-9847-420f-a026-6a0e70962d2a</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:day In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DAY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DAY_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DAY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_371035f6-42b5-494f-86d9-de2f44a6cdc6"></a>Term Name  bdqcore:371035f6-42b5-494f-86d9-de2f44a6cdc6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/371035f6-42b5-494f-86d9-de2f44a6cdc6-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/371035f6-42b5-494f-86d9-de2f44a6cdc6</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:day Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DAY_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3c8bc478-f6b2-4533-b7ce-45bae5d186c2"></a>Term Name  bdqcore:3c8bc478-f6b2-4533-b7ce-45bae5d186c2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3c8bc478-f6b2-4533-b7ce-45bae5d186c2-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3c8bc478-f6b2-4533-b7ce-45bae5d186c2</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLatitude In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DECIMALLATITUDE_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLATITUDE_INRANGE in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a2535b23-4407-40bd-b23b-30c8185d72a2"></a>Term Name  bdqcore:a2535b23-4407-40bd-b23b-30c8185d72a2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a2535b23-4407-40bd-b23b-30c8185d72a2-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a2535b23-4407-40bd-b23b-30c8185d72a2</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLatitude Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DECIMALLATITUDE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6f7a9b82-7d34-4111-a2a6-9efe5221fa44"></a>Term Name  bdqcore:6f7a9b82-7d34-4111-a2a6-9efe5221fa44</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6f7a9b82-7d34-4111-a2a6-9efe5221fa44-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6f7a9b82-7d34-4111-a2a6-9efe5221fa44</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLongitude In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DECIMALLONGITUDE_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLONGITUDE_INRANGE in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a94e986e-dbc8-4147-872d-5f2727945654"></a>Term Name  bdqcore:a94e986e-dbc8-4147-872d-5f2727945654</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a94e986e-dbc8-4147-872d-5f2727945654-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a94e986e-dbc8-4147-872d-5f2727945654</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLongitude Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DECIMALLONGITUDE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_ba953672-6526-4375-97e8-b4e9d1a7d3a0"></a>Term Name  bdqcore:ba953672-6526-4375-97e8-b4e9d1a7d3a0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/ba953672-6526-4375-97e8-b4e9d1a7d3a0-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/ba953672-6526-4375-97e8-b4e9d1a7d3a0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:degreeofEstablishment Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c04d428a-13d0-4766-9df7-4dfb2ef5d5d8"></a>Term Name  bdqcore:c04d428a-13d0-4766-9df7-4dfb2ef5d5d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c04d428a-13d0-4766-9df7-4dfb2ef5d5d8-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c04d428a-13d0-4766-9df7-4dfb2ef5d5d8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:endDayOfYear In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_ENDDAYOFYEAR_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_ENDDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_8dfed701-01a9-415d-a9f8-539280b75975"></a>Term Name  bdqcore:8dfed701-01a9-415d-a9f8-539280b75975</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/8dfed701-01a9-415d-a9f8-539280b75975-2024-02-08</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/8dfed701-01a9-415d-a9f8-539280b75975</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-08</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:establishmentMeans Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_ESTABLISHMENTMEANS_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f375a3fd-4cf5-4ef4-955e-d71762ede2d8"></a>Term Name  bdqcore:f375a3fd-4cf5-4ef4-955e-d71762ede2d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f375a3fd-4cf5-4ef4-955e-d71762ede2d8-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f375a3fd-4cf5-4ef4-955e-d71762ede2d8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Event Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENT_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_EVENT_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENT_CONSISTENT in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4cf4fe57-6736-443b-afda-f7ce8ce25471"></a>Term Name  bdqcore:4cf4fe57-6736-443b-afda-f7ce8ce25471</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4cf4fe57-6736-443b-afda-f7ce8ce25471-2023-09-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4cf4fe57-6736-443b-afda-f7ce8ce25471</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Event Temporal Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_EVENTTEMPORAL_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_d41a731b-2e2b-4442-9217-4c375ae92926"></a>Term Name  bdqcore:d41a731b-2e2b-4442-9217-4c375ae92926</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/d41a731b-2e2b-4442-9217-4c375ae92926-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/d41a731b-2e2b-4442-9217-4c375ae92926</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_EVENTDATE_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:earliestValidDate default ="1582-11-15",bdq:latestValidDate default = current year</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTDATE_INRANGE in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365"></a>Term Name  bdqcore:c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_EVENTDATE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTDATE_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_14a1d51f-16ed-4148-9dc8-1e90157a9868"></a>Term Name  bdqcore:14a1d51f-16ed-4148-9dc8-1e90157a9868</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/14a1d51f-16ed-4148-9dc8-1e90157a9868-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/14a1d51f-16ed-4148-9dc8-1e90157a9868</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_EVENTDATE_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTDATE_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a07d7147-2db8-48ce-81b8-e47595ad5f17"></a>Term Name  bdqcore:a07d7147-2db8-48ce-81b8-e47595ad5f17</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a07d7147-2db8-48ce-81b8-e47595ad5f17-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a07d7147-2db8-48ce-81b8-e47595ad5f17</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-17</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:family Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_FAMILY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_FAMILY_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_FAMILY_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c5c8db83-3af0-4215-806f-e2f90574b138"></a>Term Name  bdqcore:c5c8db83-3af0-4215-806f-e2f90574b138</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c5c8db83-3af0-4215-806f-e2f90574b138-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c5c8db83-3af0-4215-806f-e2f90574b138</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:genus Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_GENUS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_GENUS_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_GENUS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_488c1dff-21ec-4e68-a00a-7355505e180c"></a>Term Name  bdqcore:488c1dff-21ec-4e68-a00a-7355505e180c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/488c1dff-21ec-4e68-a00a-7355505e180c-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/488c1dff-21ec-4e68-a00a-7355505e180c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:geodeticDatum Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_GEODETICDATUM_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_GEODETICDATUM_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_465d7ac1-d193-46c0-a302-56a9ef99215f"></a>Term Name  bdqcore:465d7ac1-d193-46c0-a302-56a9ef99215f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/465d7ac1-d193-46c0-a302-56a9ef99215f-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/465d7ac1-d193-46c0-a302-56a9ef99215f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:kingdom Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_KINGDOM_FOUND in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_KINGDOM_FOUND in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3bc9df8b-0f57-4157-9374-b56a99090b22"></a>Term Name  bdqcore:3bc9df8b-0f57-4157-9374-b56a99090b22</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3bc9df8b-0f57-4157-9374-b56a99090b22-2024-01-28</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3bc9df8b-0f57-4157-9374-b56a99090b22</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-01-28</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:kingdom Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_KINGDOM_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_KINGDOM_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c73d49d1-06e4-4272-8249-6a26e7f8abca"></a>Term Name  bdqcore:c73d49d1-06e4-4272-8249-6a26e7f8abca</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c73d49d1-06e4-4272-8249-6a26e7f8abca-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c73d49d1-06e4-4272-8249-6a26e7f8abca</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:maximumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MAXDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_MAXDEPTH_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MAXDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7c5a6ba0-399d-4570-878a-4a064e2406fe"></a>Term Name  bdqcore:7c5a6ba0-399d-4570-878a-4a064e2406fe</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7c5a6ba0-399d-4570-878a-4a064e2406fe-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7c5a6ba0-399d-4570-878a-4a064e2406fe</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:maximumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MAXELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_MAXELEVATION_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MAXELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_49d756a8-e654-4267-a290-d1def5d2c5f9"></a>Term Name  bdqcore:49d756a8-e654-4267-a290-d1def5d2c5f9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/49d756a8-e654-4267-a290-d1def5d2c5f9-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/49d756a8-e654-4267-a290-d1def5d2c5f9</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_MINDEPTH_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_1ba18c8b-66a6-47d9-a709-404439332dba"></a>Term Name  bdqcore:1ba18c8b-66a6-47d9-a709-404439332dba</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/1ba18c8b-66a6-47d9-a709-404439332dba-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/1ba18c8b-66a6-47d9-a709-404439332dba</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_MINELEVATION_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_44f00697-ca66-43cf-8f16-646b40c0f514"></a>Term Name  bdqcore:44f00697-ca66-43cf-8f16-646b40c0f514</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/44f00697-ca66-43cf-8f16-646b40c0f514-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/44f00697-ca66-43cf-8f16-646b40c0f514</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumElevationInMeters Less Than dwcmaximumElevationInMeters</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: maxelevation</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b3c2bb86-e239-4532-ae0c-b121ec1ee025"></a>Term Name  bdqcore:b3c2bb86-e239-4532-ae0c-b121ec1ee025</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b3c2bb86-e239-4532-ae0c-b121ec1ee025-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b3c2bb86-e239-4532-ae0c-b121ec1ee025</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:month Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_MONTH_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_MONTH_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MONTH_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_16059801-6adb-4e65-82f4-61eaa70d8df0"></a>Term Name  bdqcore:16059801-6adb-4e65-82f4-61eaa70d8df0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/16059801-6adb-4e65-82f4-61eaa70d8df0-2024-02-07</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/16059801-6adb-4e65-82f4-61eaa70d8df0</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-07</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:namePublishedInYear Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0028ef9a-6553-467b-a344-90327ed2babf"></a>Term Name  bdqcore:0028ef9a-6553-467b-a344-90327ed2babf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0028ef9a-6553-467b-a344-90327ed2babf-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0028ef9a-6553-467b-a344-90327ed2babf</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceID Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_OCCURRENCEID_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_OCCURRENCEID_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_d2922585-2070-4851-a033-15e51977f9dc"></a>Term Name  bdqcore:d2922585-2070-4851-a033-15e51977f9dc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/d2922585-2070-4851-a033-15e51977f9dc-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/d2922585-2070-4851-a033-15e51977f9dc</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceStatus Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_OCCURRENCESTATUS_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_2fea4571-92d0-48a5-a5ba-6caecd647862"></a>Term Name  bdqcore:2fea4571-92d0-48a5-a5ba-6caecd647862</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/2fea4571-92d0-48a5-a5ba-6caecd647862-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/2fea4571-92d0-48a5-a5ba-6caecd647862</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceStatus Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_OCCURRENCESTATUS_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF OccurrenceStatus Vocabulary" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus]} {"dwc:occurrenceStatus vocabulary API" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_OCCURRENCESTATUS_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_773bb288-fef3-4968-a65a-a69c74d6ecb5"></a>Term Name  bdqcore:773bb288-fef3-4968-a65a-a69c74d6ecb5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/773bb288-fef3-4968-a65a-a69c74d6ecb5-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/773bb288-fef3-4968-a65a-a69c74d6ecb5</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:order Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_ORDER_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_ORDER_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_ORDER_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_ef31ba02-cea7-4d76-990f-99ebbd201fb4"></a>Term Name  bdqcore:ef31ba02-cea7-4d76-990f-99ebbd201fb4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/ef31ba02-cea7-4d76-990f-99ebbd201fb4-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/ef31ba02-cea7-4d76-990f-99ebbd201fb4</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:pathway Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_PATHWAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_PATHWAY_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_PATHWAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_17364d16-37b7-4ccb-9614-bfb95ff1bca9"></a>Term Name  bdqcore:17364d16-37b7-4ccb-9614-bfb95ff1bca9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/17364d16-37b7-4ccb-9614-bfb95ff1bca9-2022-03-25</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/17364d16-37b7-4ccb-9614-bfb95ff1bca9</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2022-03-25</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:phylum Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_PHYLUM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_PHYLUM_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_PHYLUM_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a8aee02c-cf7c-4104-a601-d8afc4f9cbe2"></a>Term Name  bdqcore:a8aee02c-cf7c-4104-a601-d8afc4f9cbe2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a8aee02c-cf7c-4104-a601-d8afc4f9cbe2-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a8aee02c-cf7c-4104-a601-d8afc4f9cbe2</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificName Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAME_FOUND in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAME_FOUND in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b4d6a61c-64ff-4da0-974c-63a73fd20836"></a>Term Name  bdqcore:b4d6a61c-64ff-4da0-974c-63a73fd20836</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b4d6a61c-64ff-4da0-974c-63a73fd20836-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b4d6a61c-64ff-4da0-974c-63a73fd20836</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificName Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAME_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7"></a>Term Name  bdqcore:6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7-2024-02-04</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-04</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameAuthorship Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a9529e71-5470-4cb1-b04d-aa483926f532"></a>Term Name  bdqcore:a9529e71-5470-4cb1-b04d-aa483926f532</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a9529e71-5470-4cb1-b04d-aa483926f532-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a9529e71-5470-4cb1-b04d-aa483926f532</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameID Complete</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAMEID_COMPLETE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: complete</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4cf84216-c8a7-4865-a8e1-3ffd829d5a10"></a>Term Name  bdqcore:4cf84216-c8a7-4865-a8e1-3ffd829d5a10</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4cf84216-c8a7-4865-a8e1-3ffd829d5a10-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4cf84216-c8a7-4865-a8e1-3ffd829d5a10</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameID Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_1b3bbac4-7c00-46d6-8179-1d57c92374ad"></a>Term Name  bdqcore:1b3bbac4-7c00-46d6-8179-1d57c92374ad</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/1b3bbac4-7c00-46d6-8179-1d57c92374ad-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/1b3bbac4-7c00-46d6-8179-1d57c92374ad</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:sex Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_SEX_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_SEX_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SEX_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_8c217eee-9cd0-48c3-aea0-90151c6c5bfd"></a>Term Name  bdqcore:8c217eee-9cd0-48c3-aea0-90151c6c5bfd</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/8c217eee-9cd0-48c3-aea0-90151c6c5bfd-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/8c217eee-9cd0-48c3-aea0-90151c6c5bfd</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:startDayOfYear In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_STARTDAYOFYEAR_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_STARTDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_9c1cdf6a-0dbf-4828-a2e3-fb368f74d194"></a>Term Name  bdqcore:9c1cdf6a-0dbf-4828-a2e3-fb368f74d194</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/9c1cdf6a-0dbf-4828-a2e3-fb368f74d194-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/9c1cdf6a-0dbf-4828-a2e3-fb368f74d194</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:stateProvince Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_STATEPROVINCE_FOUND.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_STATEPROVINCE_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_STATEPROVINCE_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_2a9d4cfd-815a-46e0-bb51-60724582b762"></a>Term Name  bdqcore:2a9d4cfd-815a-46e0-bb51-60724582b762</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/2a9d4cfd-815a-46e0-bb51-60724582b762-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/2a9d4cfd-815a-46e0-bb51-60724582b762</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Taxon Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_TAXON_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXON_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0df03601-3768-4805-906a-bbd0a41b0fda"></a>Term Name  bdqcore:0df03601-3768-4805-906a-bbd0a41b0fda</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0df03601-3768-4805-906a-bbd0a41b0fda-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0df03601-3768-4805-906a-bbd0a41b0fda</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Taxon Unambiguous</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_TAXON_UNAMBIGUOUS in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXON_UNAMBIGUOUS in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: unambiguous</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_e0b8cff1-3322-40d2-b8b2-b99fc9ae130a"></a>Term Name  bdqcore:e0b8cff1-3322-40d2-b8b2-b99fc9ae130a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/e0b8cff1-3322-40d2-b8b2-b99fc9ae130a-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/e0b8cff1-3322-40d2-b8b2-b99fc9ae130a</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:taxonRank Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_TAXONRANK_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXONRANK_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f320ca83-8487-4011-b1ff-f4b1b4dd86ec"></a>Term Name  bdqcore:f320ca83-8487-4011-b1ff-f4b1b4dd86ec</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f320ca83-8487-4011-b1ff-f4b1b4dd86ec-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f320ca83-8487-4011-b1ff-f4b1b4dd86ec</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:taxonRank Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_TAXONRANK_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXONRANK_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88"></a>Term Name  bdqcore:1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88-2024-08-03</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-03</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:typeStatus Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_TYPESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_TYPESTATUS_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core typeStatus" {[https://dwc.tdwg.org/list/#dwc_typeStatus]} {dwc:typeStatus vocabulary API [https://gbif.github.io/parsers/apidocs/org/gbif/api/vocabulary/TypeStatus.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TYPESTATUS_STANDARD in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a0502c5f-608b-4e59-99da-d9490bb4d93b"></a>Term Name  bdqcore:a0502c5f-608b-4e59-99da-d9490bb4d93b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a0502c5f-608b-4e59-99da-d9490bb4d93b-2024-08-23</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a0502c5f-608b-4e59-99da-d9490bb4d93b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-23</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:year In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_YEAR_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:earliestValidDate="1582",bdq:latestValidDate=current year</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_YEAR_INRANGE in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_a8fef8a8-e7c7-4a2d-adaf-7da99c896c93"></a>Term Name  bdqcore:a8fef8a8-e7c7-4a2d-adaf-7da99c896c93</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/a8fef8a8-e7c7-4a2d-adaf-7da99c896c93-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/a8fef8a8-e7c7-4a2d-adaf-7da99c896c93</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:year Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_YEAR_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_YEAR_NOTEMPTY in a record set are COMPLIANT</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_ef05b45b-13b8-4877-9e9d-fa44b332d83c"></a>Term Name  bdqcore:ef05b45b-13b8-4877-9e9d-fa44b332d83c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/ef05b45b-13b8-4877-9e9d-fa44b332d83c-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/ef05b45b-13b8-4877-9e9d-fa44b332d83c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Polynomial Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLETE if every VALIDATION_POLYNOMIAL_CONSISTENT in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_POLYNOMIAL_CONSISTENT in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value)</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7e0c0418-fe16-4a39-98bd-80e19d95b9d1"></a>Term Name  bdqcore:7e0c0418-fe16-4a39-98bd-80e19d95b9d1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7e0c0418-fe16-4a39-98bd-80e19d95b9d1-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7e0c0418-fe16-4a39-98bd-80e19d95b9d1</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Vaildation dwc:geodeticDatum Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available, INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; COMPLIANT if the value of dwc:geodeticDatum is (1) "not recorded" or (2) a valid geographic EPSG code for a CRS, Datum, or ellipsoid in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index#/Datum]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:geodeticDatum occur as a valid geographic CRS, geodetic Datum or ellipsoid in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="epsg:4326": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:geodeticDatum matches an unambiguous alphanumeric CRS or datum code value in the bdq:sourceAuthority"],[dwc:geodeticDatum="7030": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:geodeticDatum doesn't match values in the bdq:sourceAuthority, 1730 (EPSG:1730) is an ellipsoid not a datum"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Maptiler (2019) EPSG.io. https://epsg.io/</li> <li>EPSG (2024) About the EPSG Dataset. https://epsg.org/</li> <li>Spatial Reference (2024) What is SpatialReference.org. https://spatialreference.org/</li> <li>Geomatic Solutions (2018) Georepository. Version 9.0.0.1062. https://georepository.com/</li> <li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li> <li>Wieczorek C and Wieczorek J (2021) Georeferencing Calculator. http://georeferencing.org/georefcalculator/gc.html</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Darwin Core recommends best practice is to use a controlled vocabulary. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.  Chapman and Wieczorek (2020) recommend best practice is to use EPSG geographic CRS or Datum codes (https://epsg.io/) as a controlled vocabulary. Ideally, amend to the EPSG code for the geographic coordinate reference system (CRS), if known. Otherwise use the EPSG code for the geodetic datum, if known. Otherwise use the EPSG code of the ellipsoid, if known. If none of these is known, use the explicit value "not recorded". The reference vocabularies of values for geodetic datums and ellipsoids needs to be made available should map alternative representations of dwc:geodeticDatum strings to EPSG codes, such as "WGS84", "WGS_84", "WGS:84", "WGS 84" all with standard value "epsg:4326".</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/59</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:344cb9f6-68e1-4d7c-a976-7edcd9f20935</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:geodeticDatum occur as a valid geographic CRS, geodetic Datum or ellipsoid in bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:5cc05662-c029-4ba9-b32e-fb487ccba71c</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_GEODETICDATUM_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_8f1e6e58-544b-4365-a569-fb781341644e"></a>Term Name  bdqcore:8f1e6e58-544b-4365-a569-fb781341644e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/8f1e6e58-544b-4365-a569-fb781341644e-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/8f1e6e58-544b-4365-a569-fb781341644e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation  dwc:minimumDepthInMeters Less Than dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:minimumDepthInMeters,dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters is bdq:Empty, or if either are interpretable as not zero or a positive number; COMPLIANT if the value of dwc:minimumDepthInMeters is less than or equal to the value of dwc:maximumDepthInMeters; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumDepthInMeters a number that is less than or equal to the value of dwc:maximumDepthInMeters?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: maxdepth</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumDepthInMeters="0", dwc:maximumDepthInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumDepthInMeters = dwc:maximumDepthInMeters"],[dwc:minimumDepthInMeters="1", dwc:maximumDepthInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumDepthInMeters > dwc:maximumDepthInMeters"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/24</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:07e4c491-0d13-409d-b966-fbb9721e81cf</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:minimumDepthInMeters a number that is less than or equal to the value of dwc:maximumDepthInMeters? Validation for SingleRecord with Specification for: VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:12f7f82e-ab1c-4690-92b8-ecc9328256c1</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_2750c040-1d4a-4149-99fe-0512785f2d5f"></a>Term Name  bdqcore:2750c040-1d4a-4149-99fe-0512785f2d5f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/2750c040-1d4a-4149-99fe-0512785f2d5f-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/2750c040-1d4a-4149-99fe-0512785f2d5f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation Classification Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of the fields dwc:kingdom dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus are bdq:Empty; COMPLIANT if the combination of values of higher classification taxonomic terms (dwc:kingdom, dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus) are consistent with the lowest ranking matched element in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the combination of higher classification taxonomic terms consistent using bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="Myrtales", dwc:superfamily="", dwc:family="Myrtaceae", dwc:subfamily="", dwc:tribe="", dwc:subtribe="",  dwc:genus="Punica": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="The combination of values of higher classification taxonomic terms can be unambiguously resolved in the bdq:sourceAuthority"],[dwc:kingdom="", dwc:phylum="Chordata", dwc:class="", dwc:order="Rhopalocera", dwc:superfamly="", dwc:family="Muricidae", dwc:subfamily="", dwc:tribe="", dwc:subtribe="", dwc:genus="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="The combination of values of higher classification taxonomic terms cannot be unambiguously resolved in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>A fail condition may arise either from the taxon terms being internally inconsistent (not all of the information can be true at the same time), or from the vocabulary being incapable of resolving the combination of classification values. Additional tests could be devised against a taxonomic authority to report the distinct failure conditions. This test specifically does not consider the content of dwc:higherClassification.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/123</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:b751c2ed-11a5-4bff-9c37-1eccc8138191</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the combination of higher classification taxonomic terms consistent using bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:21d0b5f6-5b3e-4810-8413-c975b7cf343a</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_CLASSIFICATION_CONSISTENT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_adb27d29-9f0d-4d52-b760-a77ba57a69c9"></a>Term Name  bdqcore:adb27d29-9f0d-4d52-b760-a77ba57a69c9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/adb27d29-9f0d-4d52-b760-a77ba57a69c9-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/adb27d29-9f0d-4d52-b760-a77ba57a69c9</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-26</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation Coordinates dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:countryCode,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority,bdq:spatialBufferInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if one or more of dwc:decimalLatitude, dwc:decimalLongitude, or dwc:countryCode are bdq:Empty or invalid; COMPLIANT if the geographic coordinates fall on or within the boundary defined by the union of the boundary of the country from dwc:countryCode plus it's Exclusive Economic Zone as found in the bdq:sourceAuthority, if any, plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Do the geographic coordinates fall on or within the boundaries of the territory given in dwc:countryCode or its Exclusive Economic Zone?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="AR", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Coordinates match dwc:countryCode"],[dwc:countryCode="CL", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Coordinates are in Argentina, not Chile"],[dwc:countryCode="ZX", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=INTERNAL_PREREQUISTES_NOT_MET, Response.comment="Input field contains invalid values - ZX is not a valid ISO 3166-1-alpha-2 country code"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, iDigBio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li><li>Wikipedia (2020) ISO 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li><li>Flanders Marine Institute (2023) Maritime Boundaries Geodatabase, version 12. Available online at https://www.marineregions.org/. https://doi.org/10.14284/628</li><li>Kelso NV and Patterson T (2010) Introducing Natural Earth data—Naturalearthdata.com. Geographica Technica. Special issue, 2010 pp 82–89. https://technicalgeography.org/pdf/sp_i_2010/12_introducing_natural_earth_data__naturaleart.pdf</li><li>Natural Earth (2022) Natural Earth Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales. v5.1.2. https://www.naturalearthdata.com/,  https://github.com/nvkelso/natural-earth-vector/releases/tag/v5.1.2.</li><li>Natural Earth (2022) Admin 1 – States, provinces. v5.1.1 2022-05-12. https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/</li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li><li>Dooley, JF Jnr. (2005) An inventory and comparison of globally consistent geospatial databases and libraries. Rome: FAO. http://www.fao.org/3/a0118e/a0118e00.htm#Contents</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:geo_ref_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/master/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L80</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>dwc:coordinatePrecicision and dwc:coordinateUncertaintyInMeters (if present) imply a potential displacement of the provided coordinates. These two terms can be considered spatial buffers. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is justified. When dwc:countryCode=XZ (for High Seas), the coordinate should fall into a marine region out side of the EEZ of any country.  Taking the spatial buffers into account does however greatly complicate both the logic and the implementation of such tests. The same applies to potential conversion of the Spatial Reference System (SRS) of dwc:decimalLatitude and dwc:decimalLongitude to the SRS used in the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/50</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:2afcbce1-7cf8-4c5c-9df4-d267dc2df704</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Do the geographic coordinates fall on or within the boundaries of the territory given in dwc:countryCode or its Exclusive Economic Zone? Validation for SingleRecord with Specification for: VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:4343a7e0-7f0b-434d-99d4-e939ecb16e1f</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f18a470b-3fe1-4aae-9c65-a6d3db6b550c"></a>Term Name  bdqcore:f18a470b-3fe1-4aae-9c65-a6d3db6b550c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f18a470b-3fe1-4aae-9c65-a6d3db6b550c-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f18a470b-3fe1-4aae-9c65-a6d3db6b550c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation Coordinates dwc:stateProvince Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:stateProvince,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority,bdq:spatialBufferInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or invalid, or dwc:stateProvince is bdq:Empty or not found in the bdq:sourceAuthority; COMPLIANT if the geographic coordinates fall on or within the boundary in the bdq:sourceAuthority for the given dwc:stateProvince (after coordinate reference system transformations, if any, have been accounted for), or within the distance given by bdq:spatialBufferInMeters outside that boundary; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Do the geographic coordinates fall on or within the boundary from the bdq:sourceAuthority for the given dwc:stateProvince or within the distance given by bdq:spatialBufferInMeters outside that boundary?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:stateProvince="Tasmania", dwc:decimalLatitude="-42.85", dwc:decimalLongitude="146.75": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Input fields contain interpretable values"],[dwc:stateProvince="Córdoba", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Input fields contain interpretable values but coordinates don't match dwc:stateProvince with buffer"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853.</li><li>Dooley, JF Jnr. (2005) An inventory and comparison of globally consistent geospatial databases and libraries. Rome: FAO. http://www.fao.org/3/a0118e/a0118e00.htm#Contents </li><li>Google Maps Platform (2020) Reverse Geocoding API. https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse</li><li>Kelso NV and Patterson T (2010) Introducing Natural Earth data—Naturalearthdata.com. Geographica Technica. Special issue, 2010 pp 82–89. https://technicalgeography.org/pdf/sp_i_2010/12_introducing_natural_earth_data__naturaleart.pdf</li><li>Natural Earth (2022) Admin 1 – States, provinces. v5.1.1 2022-05-12. https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/</li><li>Natural Earth (2022) Natural Earth Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales. v5.1.2. https://www.naturalearthdata.com/,  https://github.com/nvkelso/natural-earth-vector/releases/tag/v5.1.2.</li><li>ESRI (2020) World Administrative Divisions. https://www.arcgis.com/home/item.html?id=f0ceb8af000a4ffbae75d742538c548b</li><li>ProgrammableWeb (2006) GeoNames API. https://www.programmableweb.com/api/geonames</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The geographic determination service is expected to return a list of names of first-level administrative divisions for geometries that the geographic point falls on or within, including a 3 km buffer around the administrative geometry. A match on any of those names should constitute a consistency, and dwc:countryCode should not be needed to make this determination, that is, this test does not attempt to disambiguate potential duplicate first-level administrative division names. The level of buffering may be related to the scale of the underlying GIS layer being used. At a global scale, typical map scales used for borders and coastal areas are either 1:3M or 1:1M (Dooley 2005, Chapter 4). Horizontal accuracy at those scales is around 1.5-2.5km and 0.5-0.85 km respectively (Chapman & Wieczorek 2020).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/56</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:315a198d-3811-40dd-918a-756f598f3294</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Do the geographic coordinates fall on or within the boundary from the bdq:sourceAuthority for the given dwc:stateProvince or within the distance given by bdq:spatialBufferInMeters outside that boundary? Validation for SingleRecord with Specification for: VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:4dd617df-a984-419f-b7b5-098b2023c4ab</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_1bf0e210-6792-4128-b8cc-ab6828aa4871"></a>Term Name  bdqcore:1bf0e210-6792-4128-b8cc-ab6828aa4871</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/1bf0e210-6792-4128-b8cc-ab6828aa4871-2023-06-20</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/1bf0e210-6792-4128-b8cc-ab6828aa4871</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-06-20</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation Coordinates Not Zero</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or is not interpretable as a number, or dwc:decimalLongitude is bdq:Empty or is not interpretable as a number; COMPLIANT if either the value of dwc:decimalLatitude is not = 0 or the value of dwc:decimalLongitude is not = 0; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are the values of either dwc:decimalLatitude or dwc:decimalLongitude numbers that are not equal to 0?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Likeliness: notzero</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Likely</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="21.0534", dwc:decimalLongitude="81.0554": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatitude and dwc:decimalLongitude are not zero"],[dwc:decimalLatitude="0", dwc:decimalLongitude="0",: Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatitude and dwc:decimalLongitude are zero"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li> </ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>A record with 0.0 is interpreted as the string "0"</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/87</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:8454615d-9cd4-49af-8fd3-c67e6be9c777</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Are the values of either dwc:decimalLatitude or dwc:decimalLongitude numbers that are not equal to 0? Validation for SingleRecord with Specification for: VALIDATION_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:b482148e-9ac2-47ad-99b5-462508e9f360</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATES_NOTZERO</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b9c184ce-a859-410c-9d12-71a338200380"></a>Term Name  bdqcore:b9c184ce-a859-410c-9d12-71a338200380</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b9c184ce-a859-410c-9d12-71a338200380-2024-08-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b9c184ce-a859-410c-9d12-71a338200380</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation Coordinates Terrestrial Marine</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:taxonIsMarine,bdq:geospatialLand,bdq:spatialBufferInMeters,bdq:assumptionOnUnknownBiome</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if either bdq:taxonIsMarine or bdq:geospatialLand are not available; INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:scientificName is bdq:Empty or (2)  the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or (3) if bdq:assumptionOnUnknownBiome is noassumption and the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine; COMPLIANT if (1) the taxon marine/nonmarine status from bdq:taxonIsMarine matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters or (2)  if the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine and bdq:assumptionOnUnknownBiome matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:taxonIsMarine default = "World Register of Marine Species (WoRMS)" {[https://www.marinespecies.org/]} {Web service [https://www.marinespecies.org/aphia.php?p=webservice]},bdq:geospatialLand default = "Union of NaturalEarth 10m-physical-vectors for Land and NaturalEarth Minor Islands" {[https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip], [https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_minor_islands.zip]},bdq:spatialBufferInMeters default = "3000",bdq:assumptionOnUnknownBiome default = "noassumption"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the marine/non-marine biome of a taxon from the bdq:sourceAuthority match the biome at the location given by the coordinates?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521", dwc:scientificName="Aegla neuquensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="The species is freshwater aquatic and the coordinates fall in a lake and thus COMPLIANT"],[dwc:decimalLatitude="20.0", dwc:decimalLongitude="-30.0", dwc:scientificName="Viviparus contectus (Millet, 1813)": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is non-marine according to dwc:taxonIsMarine but coordinates are marine"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, OBIS</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>WoRMS (2019) WoRMS - World Register of Marine Species. https://www.marinespecies.org/</li> <li>Rees T (compiler) (2024) Interim Register of Marine and Nonmarine Genera (IRMNG) VLIZ, Belgium. https://www.irmng.org/</li><li>Kelso NV and Patterson T (2010) Introducing Natural Earth data—Naturalearthdata.com. Geographica Technica. Special issue, 2010 pp 82–89. https://technicalgeography.org/pdf/sp_i_2010/12_introducing_natural_earth_data__naturaleart.pdf</li><li>OBIS (2024) Ocean Biodiversity Information System (OBIS). https://obis.org/ </li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li><li>Dooley, JF Jnr. (2005) An inventory and comparison of globally consistent geospatial databases and libraries. Rome: FAO. http://www.fao.org/3/a0118e/a0118e00.htm#Contents</li><li>Natural Earth (2022) Admin 1 – States, provinces. v5.1.1 2022-05-12. https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/</li><li>Natural Earth (2022) Natural Earth Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales. v5.1.2. https://github.com/nvkelso/natural-earth-vector/releases/tag/v5.1.2.</li><li>Natural Earth (2009) Minor Islands. https//www.naturalearthdata.com/download/10m/physical/ne_10m_minor_islands.zip</li><li>Google Maps Platform (2020) Reverse Geocoding API. https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>dwc:coordinatePrecicision and dwc:coordinateUncertaintyInMeters (if present) imply a potential displacement of the provided coordinates. These two terms can be considered spatial buffers. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is justified. Taking the spatial buffers into account does however greatly complicate both the logic and the implementation of such tests. The same applies to potential conversion of the Spatial Reference System (SRS) of dwc:decimalLatitude and dwc:decimalLongitude to the SRS used in the bdq:sourceAuthority. Note that in the current implementation tests treat "brackish" in WoRMS as both marine and terrestrial.   Note that both bdq:taxonIsMarine and bdq:geospatialLand are bdq:sourceAuthorities, but as they form two parameters, distinct names are used for them.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/51</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:2bb364f7-118b-4258-8afe-978901e5cf67</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the marine/non-marine biome of a taxon from the bdq:sourceAuthority match the biome at the location given by the coordinates? Validation for SingleRecord with Specification for: VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:45cb9e13-7944-4535-a5ef-f6ededb77305</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_374b091a-fc90-4791-91e5-c1557c649169"></a>Term Name  bdqcore:374b091a-fc90-4791-91e5-c1557c649169</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/374b091a-fc90-4791-91e5-c1557c649169-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/374b091a-fc90-4791-91e5-c1557c649169</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dc:type Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dc:type</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dc:type is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dc:type?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dc:type="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dc:type is bdq:NotEmpty"],[dc:type=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dc:type is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Dublin Core (2012) DCMI Type Vocabulary. https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/103</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:95c2e363-5a99-4276-937d-98008ca893f9</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dc:type? Validation for SingleRecord with Specification for: VALIDATION_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:e1286c46-2a95-480d-89e4-f02681372eb7</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DCTYPE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_cdaabb0d-a863-49d0-bc0f-738d771acba5"></a>Term Name  bdqcore:cdaabb0d-a863-49d0-bc0f-738d771acba5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/cdaabb0d-a863-49d0-bc0f-738d771acba5-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/cdaabb0d-a863-49d0-bc0f-738d771acba5</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dc:type Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dc:type</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; COMPLIANT if the value of dc:type is a term name in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List Of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value in dc:type occur as a value in the DCMI type vocabulary?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dc:type="Event": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dc:type matches a term in DCMI Vocabulary"],[dc:type="StillerImage": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dc:type does not match terms in DCMI Vocabulary"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Dublin Core (2012) DCMI Type Vocabulary. https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush rec_occur_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/bef180191258796f777ece7e267040d2cb2b609d/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L630</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.   EXTERNAL_PREREQUISITES_NOT_MET is not a necessary path in the specification, the type literals may be hard coded in a test implementation without an external call</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/91</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:8b06bef9-7fd4-4020-b08c-a07a1bf695b6</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value in dc:type occur as a value in the DCMI type vocabulary? Validation for SingleRecord with Specification for: VALIDATION_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:b85129f0-28c2-4ede-aff2-5ce3791c6e86</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DCTYPE_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_15f78619-811a-4c6f-997a-a4c7888ad849"></a>Term Name  bdqcore:15f78619-811a-4c6f-997a-a4c7888ad849</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/15f78619-811a-4c6f-997a-a4c7888ad849-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/15f78619-811a-4c6f-997a-a4c7888ad849</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dcterms:license Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dcterms:license</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dcterms:license is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dcterms:license?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dcterms:license="CC0 1.0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dcterms:license is bdq:NotEmpty"],[dcterms:license=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dcterms:license is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Dublin Core (2020) License Document. https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/LicenseDocument/</li><li>Creative Commons (n.dat.) About the Licenses. https://creativecommons.org/licenses/</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The license at the record level might be derived from the license of the data set from which the record is retrieved</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/99</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:940621f5-4f24-48de-8b36-256101ca4987</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dcterms:license? Validation for SingleRecord with Specification for: VALIDATION_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:d8b450af-47e6-4f5c-8154-6d6acbe9efa5</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_LICENSE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3136236e-04b6-49ea-8b34-a65f25e3aba1"></a>Term Name  bdqcore:3136236e-04b6-49ea-8b34-a65f25e3aba1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3136236e-04b6-49ea-8b34-a65f25e3aba1-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3136236e-04b6-49ea-8b34-a65f25e3aba1</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dcterms:license Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dcterms:license</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dcterms:license is bdq:Empty; COMPLIANT if the value of the term dcterms:license is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Creative Commons 4.0 Licenses or CC0 {[https://creativecommons.org/]} { Regular Expression [((http(s){0,1}://creativecommons.org/licenses/(by\</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dcterms:license occur in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dcterms:license="https://creativecommons.org/licenses/by/4.0/": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT,  Response.comment="dcterms:license matches a term in the bdq:sourceAuthority"],[dcterms:license="GPL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dcterms:license does not match a term in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>John Wieczorek</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Dublin Core (2020) License Document. https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/LicenseDocument/</li><li>Creative Commons (n.dat.) About the Licenses. https://creativecommons.org/licenses/</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The license at the record level might be derived from the license of the data set from which the record is retrieved. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.   The  canonical form of the Creative Commons license IRI has nothing after the version  e.g. https://creativecommons.org/licenses/by/4.0/, but may be followed by deed or legalcode e.g. https://creativecommons.org/licenses/by/4.0/deed and this may be followed by a language code.   However, only some two letter language codes have translations, and some translations are identified by a longer string than the two letter language code. Errors in the language code, or specifying a language code for which a translation doesn't exist returns a 404 error instead of redirecting to the more general license IRI.  As of 2024-02-28 deed.mi doesn't exist yet, but legalcode.mi does.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/38</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:180c1a90-94c3-48b5-a9fe-4223d6f2bd60</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dcterms:license occur in bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:2a9dbd16-d427-471e-8db5-c1de2b2cf030</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_LICENSE_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_58486cb6-1114-4a8a-ba1e-bd89cfe887e9"></a>Term Name  bdqcore:58486cb6-1114-4a8a-ba1e-bd89cfe887e9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/58486cb6-1114-4a8a-ba1e-bd89cfe887e9-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/58486cb6-1114-4a8a-ba1e-bd89cfe887e9</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dcterms:Location Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:higherGeographyID,dwc:higherGeography,dwc:continent,dwc:country,dwc:countryCode,dwc:stateProvince,dwc:county,dwc:municipality,dwc:waterBody,dwc:island,dwc:islandGroup,dwc:locality,dwc:locationID,dwc:verbatimLocality,dwc:decimalLatitude,dwc:decimalLongitude,dwc:verbatimCoordinates,dwc:verbatimLatitude,dwc:verbatimLongitude,dwc:footprintWKT</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if at least one term needed to determine the location of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in any of the Darwin Core spatial terms that could specify a location?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:locationID="https://opencontext.org/subjects/e54377f7-4452-4315-b676-40679b10c4d9", dwc:higherGeographyID="", dwc:higherGeography="",  dwc:continent="", dwc:waterBody="", dwc:islandGroup="", dwc:island="", dwc:country="", dwc:countryCode="", dwc:stateProvince="", dwc:county="", dwc:municipality="", dwc:locality="", dwc:verbatimLocality="", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="", dwc:geodeticDatum="", dwc:verbatimCoordinates="", dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:footprintWKT="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:LocationID is bdq:NotEmpty"],[dwc:locationID="", dwc:higherGeographyID="", dwc:higherGeography="", dwc:continent="", dwc:waterBody="", dwc:islandGroup="", dwc:island="", dwc:country="", dwc:countryCode="", dwc:stateProvince="", dwc:county="", dwc:municipality="", dwc:locality="", dwc:verbatimLocality="", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="", dwc:geodeticDatum="", dwc:verbatimCoordinates="", dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:footprintWKT="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All location fields are bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Lee Belbin</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Only fails if all of the relevant fields of the Darwin Core Location class are EMPTY or do not exist.  Relevant Darwin Core fields include dwc:locationID, dwc:higherGeographyID, dwc:higherGeography, dwc:continent, dwc:waterBody, dwc:islandGroup, dwc:island, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality, dwc:locality, dwc:verbatimLocality, dwc:decimalLatitude, dwc:decimalLongitude, dwc:verbatimCoordinates, dwc:verbatimLatitude, dwc:verbatimLongitude, dwc:footprintWKT. Elevation and/or depth alone are deemed insufficient to meaningfully locate a position on the earth.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/40</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:1f014694-573d-46e0-b38a-2acf71b32071</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in any of the Darwin Core spatial terms that could specify a location? Validation for SingleRecord with Specification for: VALIDATION_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:30ed5e2d-ef30-4988-8dbb-12c119e94ac3</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_LOCATION_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_ac2b7648-d5f9-48ca-9b07-8ad5879a2536"></a>Term Name  bdqcore:ac2b7648-d5f9-48ca-9b07-8ad5879a2536</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/ac2b7648-d5f9-48ca-9b07-8ad5879a2536-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/ac2b7648-d5f9-48ca-9b07-8ad5879a2536</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:basisOfRecord Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:basisOfRecord</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:basisOfRecord is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:basisOfRecord?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:basisOfRecord="PreservedSpecimen": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:basisOfRecord is bdq:NotEmpty"],[dwc:basisOfRecord="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:basisOfRecord is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/58</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:31c40ce6-eecd-4304-bda7-0234993b079d</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:basisOfRecord? Validation for SingleRecord with Specification for: VALIDATION_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:5aabe3d4-d2c0-415c-8972-c834b543971a</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_BASISOFRECORD_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_42408a00-bf71-4892-a399-4325e2bc1fb8"></a>Term Name  bdqcore:42408a00-bf71-4892-a399-4325e2bc1fb8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/42408a00-bf71-4892-a399-4325e2bc1fb8-2024-08-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/42408a00-bf71-4892-a399-4325e2bc1fb8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:basisOfRecord Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>Record-level</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:basisOfRecord</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>dwc:basisOfRecord vocabulary</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; COMPLIANT if the value of dwc:basisOfRecord is valid in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]}{dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:basisOfRecord occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:basisOfRecord="Taxon": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:basisOfRecord matches a standard label of one of the Darwin Core classes"],[dwc:basisOfRecord="Specimen": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:basisOfRecord does not exactly match a standard label of one of the Darwin Core classes"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The term dwc:basisOfRecord has the comment "Recommended best practice is to use a controlled vocabulary such as the set of local names of the identifiers for classes in Darwin Core." The list of these values can be determined by searching https://github.com/tdwg/dwc/blob/master/vocabulary/term_versions.csv for rows with status="recommended" and rdf_type="http://www.w3.org/2000/01/rdf-schema#Class". For tests against a dwc:Occurrence record, the set of valid terms is more limited and embodied in the resource found at https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/104</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:99103239-1019-4d2e-b435-ecb28c190a3c</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:basisOfRecord occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f094b94f-09b6-4fb0-8ba4-24252a2101c4</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_BASISOFRECORD_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_2cd6884e-3d14-4476-94f7-1191cfff309b"></a>Term Name  bdqcore:2cd6884e-3d14-4476-94f7-1191cfff309b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/2cd6884e-3d14-4476-94f7-1191cfff309b-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/2cd6884e-3d14-4476-94f7-1191cfff309b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:class Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:class</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:class is bdq:Empty; COMPLIANT if the value of dwc:class is found as a value at the rank of Class in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:class occur at rank of Class in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:class="Insecta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:class has an equivalent at the rank of Class in the bdq:sourceAuthority"],[dwc:class="Magnoleopsida": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT,  Response.comment="dwc:class does not have an equivalent at the rank of Class in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the test will designate the source authority against to check. The same test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/77</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:6d096b24-0eb1-4e6e-804f-6810e781d16f</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:class occur at rank of Class in bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:a2b39526-d08a-4a91-8b6d-aacf73677789</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_CLASS_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c6adf2ea-3051-4498-97f4-4b2f8a105f57"></a>Term Name  bdqcore:c6adf2ea-3051-4498-97f4-4b2f8a105f57</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c6adf2ea-3051-4498-97f4-4b2f8a105f57-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c6adf2ea-3051-4498-97f4-4b2f8a105f57</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:coordinateUncertaintyInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:coordinateUncertaintyInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:coordinateUncertaintyInMeters is bdq:Empty; COMPLIANT if the value of  dwc:coordinateUncertaintyInMeters is interpreted as a number between 1 and 20037509 inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:coordinateUncertaintyInMeters a number between 1 and 20,037,509?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:coordinateUncertaintyInMeters="1": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:coordinateUncertaintyInMeters is in range"],[dwc:coordinateUncertaintyInMeters="-1": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:coordinateUncertaintyInMeters is out of range"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Wikipedia (2020) Great-circle distance. https://en.wikipedia.org/wiki/Great-circle_distance</li> <li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The upper limit is one half the equatorial circumference of the earth.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/109</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:a5bbeae3-9dc8-4a0c-9f68-58526e5d6a76</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:coordinateUncertaintyInMeters a number between 1 and 20,037,509? Validation for SingleRecord with Specification for: VALIDATION_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f8dfc3fc-6580-4518-b2b4-595c29e9042e</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b23110e7-1be7-444a-a677-cdee0cf4330c"></a>Term Name  bdqcore:b23110e7-1be7-444a-a677-cdee0cf4330c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b23110e7-1be7-444a-a677-cdee0cf4330c-2024-09-25</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b23110e7-1be7-444a-a677-cdee0cf4330c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:country dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:country,dwc:countryCode</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either of the terms dwc:country or dwc:countryCode are bdq:Empty; COMPLIANT if the values of dwc:country and dwc:countryCode match national-level country name and matching country code respectively in the bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the ISO country code, determined from the value of dwc:country, equal the value of dwc:countryCode?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Australia", dwc:countryCode="AU": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country matches dwc:countryCode"],[dwc:country="United States Minor Outlying Islands", dwc:countryCode="US": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country does not match dwc:countryCode"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html/li><li>DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list</li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The country code determination service should be able to match the name of a country in the original or any language in the source authority.   When dwc:countryCode="XZ" to mark the high seas, country should be empty until a time when a dwc:country="High seas" or similar is adopted.  This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/62</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:3925c15a-2795-4cef-8a30-6e6e5e480eae</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the ISO country code, determined from the value of dwc:country, equal the value of dwc:countryCode? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:6f1093a0-0da5-4691-a95e-184d6d55eeb0</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_d257eb98-27cb-48e5-8d3c-ab9fca4edd11"></a>Term Name  bdqcore:d257eb98-27cb-48e5-8d3c-ab9fca4edd11</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/d257eb98-27cb-48e5-8d3c-ab9fca4edd11-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/d257eb98-27cb-48e5-8d3c-ab9fca4edd11</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:country dwc:stateProvince Unambiguous</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:country,dwc:stateProvince</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the terms dwc:country and dwc:stateProvince are bdq:Empty; COMPLIANT if the combination of values of dwc:country and dwc:stateProvince are unambiguously resolved to a single result with a child-parent relationship in the bdq:sourceAuthority and the entity matching the value of dwc:country in the bdq:sourceAuthority is an ISO 3166 country-like administrative entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the combination of the values of the terms dwc:country, dwc:stateProvince unique in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: unambiguous</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Unambiguous</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Argentina", dwc:stateProvince="Rio Negro": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country and dwc:stateProvince are unambiguous"],[dwc:country="", dwc:stateProvince="WA": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country and dwc:stateProvince are ambiguous. Matches Western Australia, Washington State (US)"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet, Kurator</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li> <li>Vertnet (2022) DwC Vocabs. https://github.com/VertNet/DwCVocabs/tree/master/vocabs</li> <li>Getty Research Institute (2017) Getty Thesaurus of Geographic Names Online. https://www.getty.edu/research/tools/vocabularies/tgn/index.html</li><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li><li>ISO (n.dat) 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/kurator-org/kurator-validation/blob/master/packages/kurator_dwca/workflows/dwca_geography_assessor.yaml</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See table https://github.com/tdwg/bdq/issues/95#issuecomment-1226450014. A fail condition may arise from the content being internally inconsistent (not all of the information can be true at the same time), or from the vocabulary being incapable of uniquely resolving the combination of term values.  This test specifically does not consider the content of dwc:higherGeography. If dwc:country contains a value and dwc:stateProvince does not, this test will return NOT_COMPLIANT. Use cases where knowledge to the level of country is adequate for the fitness of the data should not include this test. @tucotuco: "Of #200 and #201, #201 is the strongest test. If it passes for a record, #200 must necessarily also pass and doesn't tell you anything. If #201 fails,#200 could still pass and that would tell you that there are multiple matches on the dwc:country/dwc:stateProvince combo: It would tell you the nature of the problem. Along with #42 (dwc:country not empty), #200 would tell you whether there was an ambiguous combination of country (not empty) and dwc:stateProvince, such as would happen with Argentina/Buenos Aires. While if country is empty, then the ambiguity is purely at the dwc:stateProvince level".</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/201</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:f1a7f272-9040-42da-9b64-62abedefb1b0</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the combination of the values of the terms dwc:country, dwc:stateProvince unique in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:e5efdd20-d1fc-4287-91f9-15b9ce3f3aac</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_69b2efdc-6269-45a4-aecb-4cb99c2ae134"></a>Term Name  bdqcore:69b2efdc-6269-45a4-aecb-4cb99c2ae134</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/69b2efdc-6269-45a4-aecb-4cb99c2ae134-2024-08-19</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-24</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-19</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:country Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:country</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:country is bdq:Empty; COMPLIANT if value of dwc:country is a place type equivalent to administrative entity of "nation" in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:country occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Eswatini": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country is a valid country name in the bdq:sourceAuthority"],[dwc:country="Tasmania": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Tasmania is not found at the level of national in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Getty Research Institute (2017) Getty Thesaurus of Geographic Names Online. https://www.getty.edu/research/tools/vocabularies/tgn/index.html</li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Non-country information such as "high seas" will fail this test (High Seas should use dwc:countryCode = "XZ" and have dwc:country empty).  Getty Place Types for administrative level "nation"  are 81010 nation, 81011 independent sovereign nation, and 81012 independent nation.  Multiple values in the dwc:country field (whether to signify on a border or in a list of possibilities) will fail this test. Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test should find any matches at the Getty "nation" level including internationalized names and historical representations of that nation (where boundaries are  same). This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/21</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:04cee4e0-0c83-40cc-8de2-e7391f0a97a9</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:country occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRY_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6ce2b2b4-6afe-4d13-82a0-390d31ade01c"></a>Term Name  bdqcore:6ce2b2b4-6afe-4d13-82a0-390d31ade01c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6ce2b2b4-6afe-4d13-82a0-390d31ade01c-2024-09-27</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6ce2b2b4-6afe-4d13-82a0-390d31ade01c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:country Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:country</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:country is bdq:NotEmpty or dwc:countryCode has a value of "XZ" and either dwc:country is bdq:Empty or has a value of "High seas"; otherwise NOT_COMPLIANT ?</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:country?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Eswatini": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country is bdq:NotEmpty"],[dwc:country="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush: geo_ref_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>[geo_ref_qc DwCGeoRefDQ.validationCountryNotEmpty](https://github.com/FilteredPush/geo_ref_qc/blob/fcad4a3757db9bd6ba36fe41064ce015eeede2e3/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L478)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Country is expected to be either bdq:Empty or ideally have a value of "High seas" or an agreed equivalent if material comes from the high seas, or from those portions of Antarctica outside of any sovereign nation.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/42</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:23e9d641-1349-4998-bdff-117e32c30eff</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:country? Validation for SingleRecord with Specification for: VALIDATION_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:34ef6ea2-de06-4d2c-88fe-2c779de8f7db</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRY_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_853b79a2-b314-44a2-ae46-34a1e7ed85e4"></a>Term Name  bdqcore:853b79a2-b314-44a2-ae46-34a1e7ed85e4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/853b79a2-b314-44a2-ae46-34a1e7ed85e4-2024-09-27</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/853b79a2-b314-44a2-ae46-34a1e7ed85e4</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-27</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:countryCode Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:countryCode is bdq:NotEmpty or has a value "XZ"; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:countryCode?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="Australia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is bdq:NotEmpty"],[dwc:countryCode="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li><li>Wikipedia (2020) ISO 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li><li>DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush:geo_ref_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>[geo_ref_qc DwCGeoRefDQ,validationCountrycodeNotempty()](https://github.com/FilteredPush/geo_ref_qc/blob/78afb5f2c8b8e2ebede1de48cb7a40fd1503748f/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1060)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test will return 'NOT_COMPLIANT' for records on the "High seas" where dwc:countryCode is bdq:Empty. We recommend that data from the high seas (outside national jurisdictions) use dwc:countryCode = "XZ" and dwc:country = "High seas" until an agreement has been made.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/98</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:930eb72e-fe83-48ae-9698-ca46713721a3</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:countryCode? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:d153d4bd-b39d-43b0-b00a-395ff3e2ca62</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYCODE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0493bcfb-652e-4d17-815b-b0cce0742fbe"></a>Term Name  bdqcore:0493bcfb-652e-4d17-815b-b0cce0742fbe</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0493bcfb-652e-4d17-815b-b0cce0742fbe-2024-09-19</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-19</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="GL": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value"],[dwc:countryCode="GRL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li><li>ISO (n.dat) 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li><li>DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list</li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and suitable for a marker for the high seas.  Also available in the ISO user defined codes is ZZ, used by GBIF to mark unknown countries.  This test should accept both XZ and ZZ as COMPLIANT country codes. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/20</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:02f5a440-a473-42cf-a3f1-6c10334d5eb8</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYCODE_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_dc8aae4b-134f-4d75-8a71-c4186239178e"></a>Term Name  bdqcore:dc8aae4b-134f-4d75-8a71-c4186239178e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/dc8aae4b-134f-4d75-8a71-c4186239178e-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/dc8aae4b-134f-4d75-8a71-c4186239178e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:dateIdentified In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Identification</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:dateIdentified</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:earliestValidDate,bdq:latestValidDate,bdq:includeEventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:dateIdentified is bdq:Empty, or (2) dwc:dateIdentified contains an invalid value according to ISO 8601, or (3) bdq:includeEventDate=true and dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the value of dwc:dateIdentified is between bdq:earliestValidDate and bdq:latestValidDate inclusive and either (1) dwc:eventDate is bdq:Empty or bdq:includeEventDate=false, or (2) if dwc:eventDate is a valid ISO 8601 date and dwc:dateIdentified overlaps or is later than the dwc:eventDate; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>,bdq:earliestValidDate default="1753-01-01",bdq:latestValidDate default=[current day],bdq:includeEventDate default=true</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:dateIdentified within Parameter ranges and either overlap or is later than dwc:eventDate?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Likeliness: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dateIdentified="1963-03-08T14:07-0600", dwc:eventDate="1962-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:dateIdentified is in range"],[dwc:dateIdentified="1963-03-08T14:07-0600", dwc:eventDate="1964-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:dateIdentified before dwc:eventDate"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF, ALA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/37d349b79f05a76eeb264bafe2315ce88493ecb7/src/main/java/org/filteredpush/qc/date/DwCOtherDateDQ.java#L181</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>There may be valid identifications prior to Linnaeus, but this test will flag these under the default value of bdq:earliestValidDate, as for most biodiversity data, pre-linnaean identification dates are likely to be errors. If a parameter is not set, then the default is 1753-01-01. This test will, by design, flag as problematic cases (such as LTER plots and marine mammal sightings) where a known individual organism is identified by a specialist and then subsequently observed without new taxonomic identifications being made.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/76</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:67ddf706-c8ee-4cf2-a9d0-d161fc6b7d69</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:dateIdentified within Parameter ranges and either overlap or is later than dwc:eventDate? Validation for SingleRecord with Specification for: VALIDATION_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:a25786df-a624-4ff2-8962-6b23e8b07b0b</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DATEIDENTIFIED_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_66269bdd-9271-4e76-b25c-7ab81eebe1d8"></a>Term Name  bdqcore:66269bdd-9271-4e76-b25c-7ab81eebe1d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/66269bdd-9271-4e76-b25c-7ab81eebe1d8-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/66269bdd-9271-4e76-b25c-7ab81eebe1d8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Identification</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:dateIdentified</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; COMPLIANT if the value of dwc:dateIdentified contains a valid ISO 8601 date; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:dateIdentified a valid ISO date?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dateIdentified="1963-03-08T14:07": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:dateIdentified is a valid ISO 8601-1:2019 date"],[dwc:dateIdentified="1963-03-08X14:07-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:dateIdentified is not a valid ISO 8601-1:2019 date"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>[event_date_qc  DwCOtherDateDQ.validationDateidentifiedStandard()](https://github.com/FilteredPush/event_date_qc/blob/be60f348609363d560fe16552bca4cc2975c0766/src/main/java/org/filteredpush/qc/date/DwCOtherDateDQ.java#L58)</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/69</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:4c6a5522-ae8c-42d3-a396-8fc3aee49ef9</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:dateIdentified a valid ISO date? Validation for SingleRecord with Specification for: VALIDATION_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:89f8b2ea-fc35-4941-929a-0e32cfbeb1a6</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DATEIDENTIFIED_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_8d787cb5-73e2-4c39-9cd1-67c7361dc02e"></a>Term Name  bdqcore:8d787cb5-73e2-4c39-9cd1-67c7361dc02e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/8d787cb5-73e2-4c39-9cd1-67c7361dc02e-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/8d787cb5-73e2-4c39-9cd1-67c7361dc02e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:day In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:day,dwc:month,dwc:year</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:day is bdq:Empty, or (2) dwc:day is not interpretable as an integer, or (3) dwc:day is interpretable as an integer between 29 and 31 inclusive and dwc:month is not interpretable as an integer between 1 and 12, or (4) dwc:month is interpretable as the integer 2 and dwc:day is interpretable as the integer 29 and dwc:year is not interpretable as a valid ISO 8601 year; COMPLIANT if (1) the value of dwc:day is interpretable as an integer between 1 and 28 inclusive, or (2) dwc:day is interpretable as an integer between 29 and 30 and dwc:month is interpretable as an integer in the set (4,6,9,11), or (3) dwc:day is interpretable as an integer between 29 and 31 and dwc:month is interpretable as an integer in the set (1,3,5,7,8,10,12), or (4) dwc:day is interpretable as the integer 29 and dwc:month is interpretable as the integer 2 and dwc:year is interpretable as is a valid leap year (evenly divisible by 400 or (evenly divisible by 4 but not evenly divisible by 100)); otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:day interpretable as a valid integer between 1 and 28 inclusive or 29, 30 or 31 given the relative month and year?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="15", dwc:month="", dwc:year="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day is in range"],[dwc:day="30", dwc:month="2", dwc:year="1952": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day is not in range"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>[event_date_qc DwCEventDQ.validationDayInrange()](https://github.com/FilteredPush/event_date_qc/blob/ddbc25e6a12e4cb1c3898cebc36a4225d2945296/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L809)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must take into account the given month and year, if present, to account for leap years. This is part of a group of similar tests (VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e, #VALIDATION_STARTDAYOFYEAR_INRANGE (85803c7e-2a5a-42e1-b8d3-299a44cafc46), VALIDATION_ENDDAYOFYEAR_INRANGE9a39d88c-7eee-46df-b32a-c109f9f81fb8)).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/125</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:bb12babf-ca13-4289-9a3d-dde52bb8aff8</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:day interpretable as a valid integer between 1 and 28 inclusive or 29, 30 or 31 given the relative month and year? Validation for SingleRecord with Specification for: VALIDATION_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:2563ae15-a5bf-48fc-91f3-6df869aece2d</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DAY_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_47ff73ba-0028-4f79-9ce1-ee7008d66498"></a>Term Name  bdqcore:47ff73ba-0028-4f79-9ce1-ee7008d66498</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/47ff73ba-0028-4f79-9ce1-ee7008d66498-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:day Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:day</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:day an integer between 1 and 31 inclusive?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="15": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day is in range"],[dwc:day="32": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day is not in range"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018 DQIG Meeting; TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795).</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc [DwCEventDQ.validationDayStandard()](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L622)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is part of a group of similar tests (VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e), VALIDATION_STARTDAYOFYEAR_INRANGE (85803c7e-2a5a-42e1-b8d3-299a44cafc46), VALIDATION_ENDDAYOFYEAR_INRANGE (9a39d88c-7eee-46df-b32a-c109f9f81fb8)).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/147</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:d9bfd4f7-e158-43ee-8ac4-1bc51bf33307</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:day an integer between 1 and 31 inclusive? Validation for SingleRecord with Specification for: VALIDATION_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:c0fce1a1-8879-4175-8a71-ce037655c358</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DAY_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_b6ecda2a-ce36-437a-b515-3ae94948fe83"></a>Term Name  bdqcore:b6ecda2a-ce36-437a-b515-3ae94948fe83</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/b6ecda2a-ce36-437a-b515-3ae94948fe83-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/b6ecda2a-ce36-437a-b515-3ae94948fe83</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:decimalLatitude In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLatitude</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or the value is not interpretable as a number; COMPLIANT if the value of dwc:decimalLatitude is between -90 and 90, inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:decimalLatitude a number between -90 and 90 inclusive?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="0.0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatitude is in RANGE"],[dwc:decimalLatitude="121.0534": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatitude is in not in RANGE"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/79</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:6f3a7ebb-e857-42e0-8051-4d06feeb4ab2</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:decimalLatitude a number between -90 and 90 inclusive? Validation for SingleRecord with Specification for: VALIDATION_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:a5111c0c-d198-4ecc-af10-809ae2b3ae01</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLATITUDE_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7d2485d5-1ba7-4f25-90cb-f4480ff1a275"></a>Term Name  bdqcore:7d2485d5-1ba7-4f25-90cb-f4480ff1a275</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7d2485d5-1ba7-4f25-90cb-f4480ff1a275-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7d2485d5-1ba7-4f25-90cb-f4480ff1a275</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:decimalLatitude Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLatitude</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:decimalLatitude is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:decimalLatitude?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatiitude is bdq:NotEmpty"],[dwc:decimalLatitude="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatiitude is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020). Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/119</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:b12c8663-25e8-4c8a-abfc-edf4334d1aef</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:decimalLatitude? Validation for SingleRecord with Specification for: VALIDATION_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:0067fa60-5503-490e-8c94-93fb79cc7da2</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0949110d-c06b-450e-9649-7c1374d940d1"></a>Term Name  bdqcore:0949110d-c06b-450e-9649-7c1374d940d1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0949110d-c06b-450e-9649-7c1374d940d1-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0949110d-c06b-450e-9649-7c1374d940d1</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:decimalLongitude In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLongitude is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:decimalLongitude is between -180 and 180 degrees, inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:decimalLongitude a number between -180 and 180 inclusive?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLongitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLongitude is in range"],[dwc:decimalLongitude="181.0554": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLongitude >180"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/30</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:0ff56b48-f00e-45bd-822e-e04afbcef3e1</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:decimalLongitude a number between -180 and 180 inclusive? Validation for SingleRecord with Specification for: VALIDATION_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:1a504f7f-21a7-49e1-a0dc-f51146957fa4</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLONGITUDE_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_9beb9442-d942-4f42-8b6a-fcea01ee086a"></a>Term Name  bdqcore:9beb9442-d942-4f42-8b6a-fcea01ee086a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/9beb9442-d942-4f42-8b6a-fcea01ee086a-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/9beb9442-d942-4f42-8b6a-fcea01ee086a</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:decimalLongitude Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:decimalLongitude is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:decimalLongitude?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLongitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLongitude is bdq:NotEmpty"],[dwc:decimalLongitude=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLongitude is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/96</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:908fc823-75a9-437e-be7c-5c72cd6b149e</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:decimalLongitude? Validation for SingleRecord with Specification for: VALIDATION_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:c893ee17-ee8b-43ec-bf17-97ac814ea502</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_060e7734-607d-4737-8b2c-bfa17788bf1a"></a>Term Name  bdqcore:060e7734-607d-4737-8b2c-bfa17788bf1a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/060e7734-607d-4737-8b2c-bfa17788bf1a-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/060e7734-607d-4737-8b2c-bfa17788bf1a</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:degreeofEstablishment Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:degreeOfEstablishment</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; COMPLIANT if the value of dwc:degreeOfEstablishment is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:degreeOfEstablishment occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:degreeOfEstablishment="cultivated": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:degreeOfEstablishment found in the bdq:sourceAuthority"],[dwc:degreeOfEstablishment="grown in garden": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:degreeOfEstablishment not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Darwin Core Maintenance Group (2021) Degree Of Establishment Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://dwc.tdwg.org/dwc/doc/doe/</li> <li>Groom et al. (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards 3: e38084. https://doi.org/10.3897/biss.3.38084</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/275</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:fd15e0a4-f49d-4566-b700-a9b46c284e68</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:degreeOfEstablishment occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:fec2103b-5d46-4723-b2ec-8c8119b44aaf</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_9a39d88c-7eee-46df-b32a-c109f9f81fb8"></a>Term Name  bdqcore:9a39d88c-7eee-46df-b32a-c109f9f81fb8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/9a39d88c-7eee-46df-b32a-c109f9f81fb8-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:endDayOfYear In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is bdq:Empty or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1949-01-15T12:34/1949-01-20T17:00", dwc:endDayOfYear="20": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:endDayOfYear is in range"],[dwc:eventDate="", dwc:endDayOfYear="x": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:endDayOfYear is ambiguous, either "X" or "No data" or "10"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/23e4139d7f0ef71736f7fc7e984cfd2d0bfea093/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L888  Unit test at https://github.com/FilteredPush/event_date_qc/blob/5f2e7b30f8a8076977b2a609e0318068db80599a/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L609</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See test VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e). This test only asks if dwc:endDayOfYear is a valid value for the relevant year, not if it is consistent with the end day of the range specified in dwc:eventDate. In a non-leap year, the valid range is 1-365 inclusive, in a leap year 366 is also valid. This test should be run after the series of tests that assure that dwc:eventDate is populated, if possible (i.e., AMENDMENT_EVENTDATE_FROM_VERBATIM (6d0a0c10-5e4a-4759-b448-88932f399812), AMENDMENT_EVENTDATE_STANDARDIZED (718dfc3c-cb52-4fca-b8e2-0e722f375da7), and AMENDMENT_EVENT_DATE_FROM_YEARMONTHDAY (3892f432-ddd0-4a0a-b713-f2e2ecbd879d)).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/131</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:ca1bc131-fa85-4fdf-902d-ad20bd4ba0f4</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year? Validation for SingleRecord with Specification for: VALIDATION_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:62f754b5-a0a1-4b24-9982-b76e4e169f71</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_ENDDAYOFYEAR_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4eb48fdf-7299-4d63-9d08-246902e2857f"></a>Term Name  bdqcore:4eb48fdf-7299-4d63-9d08-246902e2857f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4eb48fdf-7299-4d63-9d08-246902e2857f-2024-02-08</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4eb48fdf-7299-4d63-9d08-246902e2857f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-08</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:establishmentMeans Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:establishmentMeans</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; COMPLIANT if the value of dwc:establishmentMeans is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:establishmentMeans occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:establishmentMeans="native": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:establishmentMeans found in the bdq:sourceAuthority"],[dwc:establishmentMeans="cultivated": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:establishmentMeans not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Darwin Core Maintenance Group (2021) Establishment Means Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/em/</li> <li>Groom et al. (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Services 3: e38084. https://doi.org/10.3897/biss.3.38084</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/268</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:f89147ba-03e5-432b-8040-0a2a4921d676</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:establishmentMeans occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f1d3bf9c-5558-41dc-8e33-b17c499be016</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_5618f083-d55a-4ac2-92b5-b9fb227b832f"></a>Term Name  bdqcore:5618f083-d55a-4ac2-92b5-b9fb227b832f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/5618f083-d55a-4ac2-92b5-b9fb227b832f-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/5618f083-d55a-4ac2-92b5-b9fb227b832f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:Event Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate,dwc:day,dwc:month,dwc:year,dwc:startDayOfYear,dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty, or all of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear are bdq:Empty; COMPLIANT if all of the following conditions are met (1) dwc:year is bdq:Empty or dwc:eventDate has a precision of one year or finer and and is within a single year and the provided value of dwc:year matches the year expressed in dwc:eventDate, and (2) dwc:month is bdq:Empty or dwc:eventDate has a precision of one month or finer and is within a single month and the provided value in dwc:month matches the month represented by dwc:eventDate, and (3) dwc:day is bdq:Empty or dwc:eventDate has a precision of a day or less and is within a single day and the provided value in dwc:day matches the day represented by dwc:eventDate, and (4) dwc:startDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:startDayOfYear matches the start day of the year of the range represented by dwc:eventDate, and (5) dwc:endDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:endDayOfYear matches the end day of the year of the range represented by dwc:eventDate; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are the values in dwc:eventDate consistent with the values in dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="15", dwc:month="9", dwc:year="1949", dwc:eventDate="1949-09-15T12:34", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day, dwc:month and dwc:year match dwc:eventDate"],[dwc:day="15", dwc:month="9", dwc:year="1949", dwc:eventDate="1949-09-16T12:34", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day does not match dwc:eventDate"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/029466e0dc5ef649e7768ab19f75c86094023fce/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1179 minimal set of unit tests at https://github.com/FilteredPush/event_date_qc/blob/029466e0dc5ef649e7768ab19f75c86094023fce/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L1149</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test does not take a position on whether the value in dwc:eventDate, or the values in the atomic terms are correct, it simply points out the presence of inconsistencies.  For this test, dwc:eventTime is explicitly ignored. It may be useful to consider an additional test that does evaluate dwc:eventTime and dwc:eventDate. In that case, but not in this test, if the time is present in both dwc:eventDate and dwc:eventTime, and it is inconsistent, it may indicate an error in the dwc:eventDate, thus making it a problem that someone needs to evaluate.   This test will only assert consistency if the data are both internally consistent and are compliant with the term definitions, for example dwc:day, by its definition, can only be the day  of an dwc:eventDate that has a precision of a day or better and is not a range that spans more than a single day.   A dwc:day that was internally consistent with the first day of the year (that is, 1) of an dwc:eventDate that only had precision to a year would be consistent internally, but not consistent with the Darwin Core term definitions, and would not return COMPLIANT from this test.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/67</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:449f44fe-0fef-42ff-a446-d693653b55d4</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Are the values in dwc:eventDate consistent with the values in dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear? Validation for SingleRecord with Specification for: VALIDATION_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:83d057ea-a6f6-49e6-ac3c-0c418776a0e0</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENT_CONSISTENT</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_41267642-60ff-4116-90eb-499fee2cd83f"></a>Term Name  bdqcore:41267642-60ff-4116-90eb-499fee2cd83f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/41267642-60ff-4116-90eb-499fee2cd83f-2023-09-30</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/41267642-60ff-4116-90eb-499fee2cd83f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-30</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:Event Temporal Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate,dwc:year,dwc:month,dwc:day,dwc:startDayOfYear,dwc:endDayOfYear,dwc:verbatimEventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if any of dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate are bdq:NotEmpty; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in any of the terms dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="", dwc:month="", dwc:year="", dwc:eventDate="1962-11-01T10:00-0600", dwc:verbatimEventDate="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate is bdq:NotEmpty"],[dwc:dateIdentified="", dwc:day="", dwc:month="", dwc:year="", dwc:eventDate="", dwc:verbatimEventDate="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All input fields bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>@Tasilee</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/8740a00b52ef41cdda5fc7fa1689e5d95a23a94b/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1207 Unit test at  https://github.com/FilteredPush/event_date_qc/blob/8740a00b52ef41cdda5fc7fa1689e5d95a23a94b/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L881</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Only fails if all of the relevant fields of the Darwin Core Event class are bdq:Empty or do not exist. Relevant Darwin Core fields include dwc:eventDate, dwc:verbatimEventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear.  The terms dwc:eventID (if populated may or may not point to temporal information accessible to user of the data) and dwc:eventTime (which is rare) are not included.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/88</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:87d34104-0a79-4f51-aeeb-1115ec56e237</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in any of the terms dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate? Validation for SingleRecord with Specification for: VALIDATION_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:b57460c4-16e1-4c1d-8a07-a53aee9e8922</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3cff4dc4-72e9-4abe-9bf3-8a30f1618432"></a>Term Name  bdqcore:3cff4dc4-72e9-4abe-9bf3-8a30f1618432</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3cff4dc4-72e9-4abe-9bf3-8a30f1618432-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3cff4dc4-72e9-4abe-9bf3-8a30f1618432</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:eventDate In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:earliestValidDate,bdq:latestValidDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the range of dwc:eventDate is entirely within the range bdq:earliestValidDate to bdq:latestValidDate, inclusive, otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:earliestValidDate default ="1582-11-15",bdq:latestValidDate default = current year</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:eventDate entirely with the Parameter Range?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1962-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate is IN_RANGE"],[dwc:eventDate="2300-11-01T10:00": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate is NOT_IN_RANGE"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>FilteredPush event_date_qc [DwCEventDQ.validationEventdateInrange()](https://github.com/FilteredPush/event_date_qc/blob/c17d6e8340f7dd5dfa63a761d4e1cb66c126980a/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L2229)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test provides for a default earliest date, which is 1582-11-15 by convention. That date was chosen because ISO 8601-1 asserts that "the use of proleptic Gregorian calendar dates prior are not allowed in ISO 8601-1 without prior agreement of the parties exchanging data", and Darwin Core does not comment on this.  Different calendars have been used at different times in different places, and the transcription of an original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date, and metadata may or not be present to even identify such records. Given the complexity, and ongoing nature of transitions between calendars, we do not advocate using this test for quality assurance by selecting a transition date and using it as a threshold.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/36</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:17f89e32-0174-4bf9-805e-ba7aec59477b</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:eventDate entirely with the Parameter Range? Validation for SingleRecord with Specification for: VALIDATION_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:29a1fdc6-326b-4017-880d-d11ff0225b8f</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTDATE_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f51e15a6-a67d-4729-9c28-3766299d2985"></a>Term Name  bdqcore:f51e15a6-a67d-4729-9c28-3766299d2985</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f51e15a6-a67d-4729-9c28-3766299d2985-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f51e15a6-a67d-4729-9c28-3766299d2985</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:eventDate Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:eventDate is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:eventDate?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1964-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventdate is bdq:NotEmpty"],[dwc:eventDate="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795).</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc v3.0.0 [DwCEventDQ.validationEventdateNotEmpty()](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L182)</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/33</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:12499336-882b-4186-b5a2-4a806af2e35b</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:eventDate? Validation for SingleRecord with Specification for: VALIDATION_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:1fae3f77-7fcb-42c6-ab43-1ff28adf4fa4</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTDATE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4f2bf8fd-fc5c-493f-a44c-e7b16153c803"></a>Term Name  bdqcore:4f2bf8fd-fc5c-493f-a44c-e7b16153c803</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4f2bf8fd-fc5c-493f-a44c-e7b16153c803-2024-09-16</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4f2bf8fd-fc5c-493f-a44c-e7b16153c803</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-16</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:eventDate Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; COMPLIANT if the value of dwc:eventDate is a valid ISO 8601 date; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:eventDate a valid ISO date?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1963-03-08T14": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate contains a valid ISO 8601-1:2019 date"],[dwc:eventDate="1963-03-08T14:67-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate does not contain a valid ISO 8601-1:2019 date"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paul Morris</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li><li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li><li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795)</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc [DwCEventDQ.validationEventdateStandard() ](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L494)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test should also pick up issues such as 29 Feb in a non leap year.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/66</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:3f868855-cc39-4a1b-8050-bfa246416a47</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:eventDate a valid ISO date? Validation for SingleRecord with Specification for: VALIDATION_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:80c8f69b-4ad3-40ee-bccd-de016bfae367</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTDATE_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3667556d-d8f5-454c-922b-af8af38f613c"></a>Term Name  bdqcore:3667556d-d8f5-454c-922b-af8af38f613c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3667556d-d8f5-454c-922b-af8af38f613c-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3667556d-d8f5-454c-922b-af8af38f613c</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-17</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:family Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:family</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:family is bdq:Empty; COMPLIANT if the value of dwc:family is found as a value at the rank of Family in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:family occur at rank of Family in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:family="Agaricaceae": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="bdq:family has an equivalent at the rank of Family in the bdq:sourceAuthority"],[dwc:family="Agaricacae": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="bdq:family does not have an equivalent at the rank of Family in the Parameterized Source Authority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the test will designate the source authority against to check. The same test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/28</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:0997d841-9db9-40a8-b6ec-5867e9091532</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:family occur at rank of Family in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:16f999d9-1cf5-4208-b2ca-1a93d6700085</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_FAMILY_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec"></a>Term Name  bdqcore:f2ce7d55-5b1d-426a-b00e-6d4efe3058ec</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/f2ce7d55-5b1d-426a-b00e-6d4efe3058ec-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/f2ce7d55-5b1d-426a-b00e-6d4efe3058ec</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:genus Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:genus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available;  INTERNAL_PREREQUISITES_NOT_MET if dwc:genus is bdq:Empty; COMPLIANT if the value of dwc:genus is found as a value at the rank of genus in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:genus occur at the rank of Genus in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:genus="Egernia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:genus has an equivalent at the rank of Genus in the Parameterized Source Authority"],[dwc:genus="Egernea": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:genus does not have an equivalent at the rank of Genus in the bdq:sourceAuthority. This may be fixed using fuzzy matching at the AMENDMENT stage"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the test will designate the source authority against which to check. The same test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/122</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:b6cb27ac-e9b8-4a0c-b986-3e34069d8449</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:genus occur at the rank of Genus in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:15bbda19-dd18-471a-a5c3-56c7e543012f</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_GENUS_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_239ec40e-a729-4a8e-ba69-e0bf03ac1c44"></a>Term Name  bdqcore:239ec40e-a729-4a8e-ba69-e0bf03ac1c44</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/239ec40e-a729-4a8e-ba69-e0bf03ac1c44-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/239ec40e-a729-4a8e-ba69-e0bf03ac1c44</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:geodeticDatum Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:geodeticDatum is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:geodeticDatum?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="UTM": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:geodeticDatum is bdq:NotEmpty"],[dwc:geodeticDatum="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:geodeticDatum is bdq:Empty."]</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li>  </ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/78</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:6d1f3f11-98d9-4b26-a8e7-56fbc066c705</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:geodeticDatum? Validation for SingleRecord with Specification for: VALIDATION_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:a3c8b277-15fb-4ae8-afb1-e64fb6eb5241</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_GEODETICDATUM_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_125b5493-052d-4a0d-a3e1-ed5bf792689e"></a>Term Name  bdqcore:125b5493-052d-4a0d-a3e1-ed5bf792689e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/125b5493-052d-4a0d-a3e1-ed5bf792689e-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/125b5493-052d-4a0d-a3e1-ed5bf792689e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:kingdom Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:kingdom</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:kingdom is bdq:Empty; COMPLIANT if the value of dwc:kingdom is found as a value at the rank of kingdom in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:kingdom occur at rank of Kingdom in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:kingdom="Animalia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:kingdom has an equivalent at the rank of Kingdom in the bdq:sourceAuthority"],[dwc:kingdom="Metazoa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:kingdom does not strictly have an equivalent at the rank of Kingdom in the Parameterized Source Authority (Metazoa is synonym of Animalia)"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the test will designate the source authority against to check. The same test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/81</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:7072bf93-bffc-4d83-ad51-b351c6e53260</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:kingdom occur at rank of Kingdom in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:a90e100a-3522-4742-aa73-3b98a35ab826</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_KINGDOM_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_36ed36c9-b1a7-40b2-b5e2-0d012e772098"></a>Term Name  bdqcore:36ed36c9-b1a7-40b2-b5e2-0d012e772098</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/36ed36c9-b1a7-40b2-b5e2-0d012e772098-2024-01-28</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/36ed36c9-b1a7-40b2-b5e2-0d012e772098</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-01-28</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:kingdom Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:kingdom</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:kingdom is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:kingdom?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:kingdom="Fungi": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:kingdom is bdq:NotEmpty"],[dwc:kingdom="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:kingdom is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/216</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:f5bd0eee-4cdf-4455-876d-a46d92373a4e</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:kingdom? Validation for SingleRecord with Specification for: VALIDATION_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:e6f0a9ce-3e72-40fb-9fad-63cf5962f93e</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_KINGDOM_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3f1db29a-bfa5-40db-9fd1-fde020d81939"></a>Term Name  bdqcore:3f1db29a-bfa5-40db-9fd1-fde020d81939</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3f1db29a-bfa5-40db-9fd1-fde020d81939-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3f1db29a-bfa5-40db-9fd1-fde020d81939</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:maximumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidDepthInMeters,bdq:maximumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumDepthInMeters is bdq:Empty or is not interpretable as a number greater than or equal to zero; COMPLIANT if the value of dwc:maximumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:maximumDepthInMeters within the Parameter range?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:maximumDepthInMeters="1200": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:maximumDepthInMeters is in range (<11,000)"],[dwc:maximumDepthInMeters="99999": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:maximumDepthInMeters is not in range (>11,000)"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Wikipedia (2024) Extreme points on Earth. https://en.wikipedia.org/wiki/Extreme_points_of_Earth</li> <li>Chapman AD and Wieczorek JR (2020). Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The Challenger Deep in the Mariana Trench is the deepest known point in Earth's oceans at 10,994 meters.  We have rounded up bdq:maximumValidDepthInMeters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/187</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:ed60f87e-7ab7-446a-8565-903dbe6408d2</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:maximumDepthInMeters within the Parameter range? Validation for SingleRecord with Specification for: VALIDATION_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:cebc8ba0-ca02-4f1e-830e-ec693bc628e4</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MAXDEPTH_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c971fe3f-84c1-4636-9f44-b1ec31fd63c7"></a>Term Name  bdqcore:c971fe3f-84c1-4636-9f44-b1ec31fd63c7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c971fe3f-84c1-4636-9f44-b1ec31fd63c7-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c971fe3f-84c1-4636-9f44-b1ec31fd63c7</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:maximumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:maximumElevationInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidElevationInMeters,bdq:maximumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumElevationInMeters is bdq:Empty or the value cannot be interpreted as a number; COMPLIANT if the value of dwc:maximumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:maximumElevationInMeters of a single record within a valid range?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:maximumElevation is in is range"],[dwc:maximumElevationInMeters="-500": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:maximumElevation is not in range, i.e. is <-430"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Wikipedia (2020) List of elevations extremes by country. https://en.wikipedia.org/wiki/List_of_elevation_extremes_by_country_</li> <li>Wikipedia (2020) Extreme points of Antarctica. https://en.wikipedia.org/wiki/Extreme_points_of_Antarctica </li> <li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have rounded up the Parameter values. We are aware of sub-ice elevations in Antarctica to -3,500m and possible sampling in the atmosphere above the elevation of the top of Mt Everest that would fail this test but we support the odd false positive.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/112</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:a6035033-0779-4a75-99ea-f7112c1dde2b</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:maximumElevationInMeters of a single record within a valid range? Validation for SingleRecord with Specification for: VALIDATION_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f9471802-a5f7-4f4e-9810-f3f4f43dad1a</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MAXELEVATION_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_04b2c8f3-c71b-4e95-8e43-f70374c5fb92"></a>Term Name  bdqcore:04b2c8f3-c71b-4e95-8e43-f70374c5fb92</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/04b2c8f3-c71b-4e95-8e43-f70374c5fb92-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/04b2c8f3-c71b-4e95-8e43-f70374c5fb92</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:minimumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:minimumDepthInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidDepthInMeters,bdq:maximumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters is bdq:Empty, or the value is not interpretable as number greater than or equal to zero; COMPLIANT if the value of dwc:minimumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumDepthInMeters within the Parameter range?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumDepthInMeters="1": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumDepthInMeters is in range"],[dwc:minimumDepthInMeters="12000": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumDepthInMeters is not in range"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Wikipedia (2020). Extreme points on Earth (https://en.wikipedia.org/wiki/Extreme_points_of_Earth</li> <li>Chapman, AD and Wieczorek, JR (2020). Georeferencing Best Practices. Copenhagen: GBIF Secretariat (https://doi.org/10.15468/doc-gg7h-s853)</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The Challenger Deep in the Mariana Trench is the deepest known point in Earth's oceans at 10,994 meters.  We have rounded up bdq:maximumValidDepthInMeters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/107</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:9cc301b1-e303-4abb-9d24-d31506de9436</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:minimumDepthInMeters within the Parameter range? Validation for SingleRecord with Specification for: VALIDATION_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINDEPTH_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_0bb8297d-8f8a-42d2-80c1-558f29efe798"></a>Term Name  bdqcore:0bb8297d-8f8a-42d2-80c1-558f29efe798</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/0bb8297d-8f8a-42d2-80c1-558f29efe798-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/0bb8297d-8f8a-42d2-80c1-558f29efe798</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:minimumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:minimumElevationInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidElevationInMeters,bdq:maximumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumElevationInMeters within the Parameter range?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumElevationInMeters is IN_RANGE"],[dwc:minimumElevationInMeters="-500": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumElevationInMeters is NOT_IN_RANGE (<-430)"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Wikipedia (2020) List of elevations extremes by country. https://en.wikipedia.org/wiki/List_of_elevation_extremes_by_country_</li><li>Wikipedia (2020) Extreme points of Antarctica. https://en.wikipedia.org/wiki/Extreme_points_of_Antarctica</li><li>Chapman AD and Wieczorek, JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have rounded up the Parameter values. We are aware of sub-ice elevations in Antarctica to -3,500m and possible sampling in the atmosphere above the elevation of the top of Mt Everest that would fail this test but we support the odd false positive.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/39</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:1aa9c50e-7e8a-445f-9cf3-12af51a9ec10</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:minimumElevationInMeters within the Parameter range? Validation for SingleRecord with Specification for: VALIDATION_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:2bb79221-0312-410a-aef6-f569485df6a6</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINELEVATION_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_d708526b-6561-438e-aa1a-82cd80b06396"></a>Term Name  bdqcore:d708526b-6561-438e-aa1a-82cd80b06396</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/d708526b-6561-438e-aa1a-82cd80b06396-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/d708526b-6561-438e-aa1a-82cd80b06396</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:minimumElevationInMeters Less Than dwcmaximumElevationInMeters</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:minimumElevationInMeters,dwc:maximumElevationInMeters</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumlevationInMeters or dwc:minimumElevationInMeters is bdq:Empty, or if either is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is a number less than or equal to the value of the number dwc:maximumElevationInMeters, otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumElevationInMeters a number less than or equal to the value of dwc:maximumElevationInMeters?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: maxelevation</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumElevationInMeters="0", dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumElevationInMeters is equal to dwc: maximumElevationInMeters"],[dwc:minimumElevationInMeters="1", dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumElevationInMeters is greater than dwc:maximumElevationInMeters"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>@Tasilee</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/108</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:a0486e4f-210d-4143-ae5a-f320bebc2cb5</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:minimumElevationInMeters a number less than or equal to the value of dwc:maximumElevationInMeters? Validation for SingleRecord with Specification for: VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f799fb5c-37e4-46d7-a07e-87eb071df9c6</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_01c6dafa-0886-4b7e-9881-2c3018c98bdc"></a>Term Name  bdqcore:01c6dafa-0886-4b7e-9881-2c3018c98bdc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/01c6dafa-0886-4b7e-9881-2c3018c98bdc-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/01c6dafa-0886-4b7e-9881-2c3018c98bdc</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:month Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:month</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; COMPLIANT if the value of dwc:month is interpretable as an integer between 1 and 12 inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:month interpretable as an integer between 1 and 12 inclusive?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:month="10": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:month is in range"],[dwc:month="v": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:month is ambiguous as "v" or "5""]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville (MONTH_INVALID/MONTH_IN_RANGE previously in spreadsheet, from ALA?)</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795).</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc [DwCEventDQ.validationMonthStandard()](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L673) Unit test in [DwcEventDQTest]{https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L242)</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/126</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:bb630881-2a79-4750-ae0f-36d0df2191f7</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:month interpretable as an integer between 1 and 12 inclusive? Validation for SingleRecord with Specification for: VALIDATION_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:2c5dbdbb-feab-474c-bcca-bf6d1b90ae66</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MONTH_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70"></a>Term Name  bdqcore:ff59f77d-71e9-4eb1-aac9-8bd05c50ff70</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/ff59f77d-71e9-4eb1-aac9-8bd05c50ff70-2024-02-07</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/ff59f77d-71e9-4eb1-aac9-8bd05c50ff70</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-07</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:namePublishedInYear Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:namePublishedInYear</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:namePublishedInYear is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:namePublishedInYear?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:namePublishedInYear="2024": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:namePublishedInYear is bdq:NotEmpty"],[dwc:namePublishedInYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:namePublishedInYear is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/259</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:f8024a02-76c0-482a-b805-097d0cdc82e2</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:namePublishedInYear? Validation for SingleRecord with Specification for: VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f09fc9ad-a449-4422-b32f-63d8ccf2501f</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c486546c-e6e5-48a7-b286-eba7f5ca56c4"></a>Term Name  bdqcore:c486546c-e6e5-48a7-b286-eba7f5ca56c4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c486546c-e6e5-48a7-b286-eba7f5ca56c4-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c486546c-e6e5-48a7-b286-eba7f5ca56c4</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:occurrenceID Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:occurrenceID</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:occurrenceID is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:occurrenceID?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceID="https://www.inaturalist.org/observations/43047701": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceID conforms to GUID structure"],[dwc:occurrenceID="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceID is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/47</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:296e08b2-c044-4cef-930e-8d29c579c8d6</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:occurrenceID? Validation for SingleRecord with Specification for: VALIDATION_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:3d9e1339-19d7-47e7-af9e-11905df82b6a</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_OCCURRENCEID_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf"></a>Term Name  bdqcore:eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:occurrenceStatus Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:occurrenceStatus is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:occurrenceStatus?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceStatus is bdq:NotEmpty"],[dwc:occurrenceStatus="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceStatus is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/117</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:af9591f4-d0ee-4301-bc59-d6a68d1d6813</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:occurrenceStatus? Validation for SingleRecord with Specification for: VALIDATION_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:c3a53898-c4ad-40e0-961b-b4ceafea37c7</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47"></a>Term Name  bdqcore:7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:occurrenceStatus Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>dwc:occurrenceStatus vocabulary</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:Empty; COMPLIANT if the value of dwc:occurrenceStatus is resolved in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF OccurrenceStatus Vocabulary" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus]} {"dwc:occurrenceStatus vocabulary API" [https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:occurrenceStatus occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="present": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceStatus matches a term in the bdq:sourceAuthority"],[dwc:occurrenceStatus="presence": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceStatus does not match a term in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/rec_occur_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/86d413c2b193bb6983e0ad07b3dc0084de118af5/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L479</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The original recommended controlled vocabulary for this term consisted of "present" and "absent", which are the only two appropriate terms for a Darwin Core Occurrence. This is reflected in the suggested dwc:occurrenceStatus vocabulary for this test. Other values for dwc:occurrenceStatus should only arise under circumstances that do not refer to an Occurrence. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/116</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:acc05ff6-b1c8-4001-8aad-930a9b9ccaf8</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:occurrenceStatus occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:fbe854d4-acf3-4c79-a654-81441fed644f</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_OCCURRENCESTATUS_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_81cc974d-43cc-4c0f-a5e0-afa23b455aa3"></a>Term Name  bdqcore:81cc974d-43cc-4c0f-a5e0-afa23b455aa3</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/81cc974d-43cc-4c0f-a5e0-afa23b455aa3-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/81cc974d-43cc-4c0f-a5e0-afa23b455aa3</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:order Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:order</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:order is bdq:Empty; COMPLIANT if the value of dwc:order is found as a value at the rank of Order in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:order occur at rank of Order in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:order="Lepidoptera": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:order has an equivalent at the rank of Order in the bdq:sourceAuthority"],[dwc:order="Nymphalidae": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:order does not have an equivalent at the rank of Order in the bdq:sourceAuthority. Nymphalidae is a family, not an order"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the test will designate the source authority against to check. The same test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/83</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:79096434-5b55-40e1-9afb-e138a11f82ba</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:order occur at rank of Order in bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:ae08b4b4-89ba-4972-b51f-912b132bd006</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_ORDER_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_5424e933-bee7-4125-839e-d8743ea69f93"></a>Term Name  bdqcore:5424e933-bee7-4125-839e-d8743ea69f93</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/5424e933-bee7-4125-839e-d8743ea69f93-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/5424e933-bee7-4125-839e-d8743ea69f93</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:pathway Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:pathway</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; COMPLIANT if the value of dwc:pathway is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:pathway occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:pathway="transportStowaway": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:pathway found in the bdq:sourceAuthority"],[dwc:pathway="escapee": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:pathway not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Darwin Core Maintenance Group (2021) Pathway Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). https://dwc.tdwg.org/pw/</li> <li>Groom et al. (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Services 3: e38084 h.ttps://doi.org/10.3897/biss.3.38084</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/277</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:ffae8e47-2181-4a83-b1c7-d0a893e79b67</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:pathway occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:c7c92ef0-284e-4c5d-8fc9-f1480bfe0b8e</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_PATHWAY_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f"></a>Term Name  bdqcore:eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f-2022-03-25</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2022-03-25</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:phylum Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:phylum</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdq:Empty; COMPLIANT if the value of dwc:phylum is found as a value at the rank of Phylum in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:phylum occur at rank of Phylum in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"],[dwc:phylum="Trachyophyta": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:phylum does not have an equivalent at the rank of Phylum in the bdq:sourceAuthority."]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the test will designate the source authority against to check. The same test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/22</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:06f9faab-102a-452a-b6e0-4eafd8d7e71d</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:phylum occur at rank of Phylum in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:1193230f-f188-4917-92da-bba3390ed3fa</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_PHYLUM_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_3f335517-f442-4b98-b149-1e87ff16de45"></a>Term Name  bdqcore:3f335517-f442-4b98-b149-1e87ff16de45</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/3f335517-f442-4b98-b149-1e87ff16de45-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/3f335517-f442-4b98-b149-1e87ff16de45</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:scientificName Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty; COMPLIANT if there is a match of the contents of dwc:scientificName in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a match of the contents of dwc:scientificName with the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in the bdq:sourceAuthority"],[dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2019). GBIF Backbone Taxonomy. Checklist dataset (https://doi.org/10.15468/39omei)</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FP-Akka</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this test is to detect errors in the scientific name but is dependent on the abilities of the parsing of the bdq:sourceAuthority. For research users of biodiversity data doing quality assurance, VALIDATION_TAXON_UNAMBIGUOUS (4c09f127-737b-4686-82a0-7c8e30841590) handles their needs, but for curators of data sets doing quality control, this test provides a specific subset of targeted data cleaning, making it a valuable test to include for the quality control case.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/46</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:275ae9b2-4085-4946-9580-6a63844174cd</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a match of the contents of dwc:scientificName with the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:3c2fe7e9-186f-4ceb-8274-8bbcb4a62de4</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAME_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7c4b9498-a8d9-4ebb-85f1-9f200c788595"></a>Term Name  bdqcore:7c4b9498-a8d9-4ebb-85f1-9f200c788595</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7c4b9498-a8d9-4ebb-85f1-9f200c788595-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7c4b9498-a8d9-4ebb-85f1-9f200c788595</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:scientificName Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:scientificName is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:scientificName?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificName="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName is bdq:NotEmpty"],[dwc:scientificName="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA,GBIF,OBIS</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/82</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:74259ddf-188c-4e6f-96f2-9ed3a8adfbf7</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:scientificName? Validation for SingleRecord with Specification for: VALIDATION_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:a9c18563-f63e-42db-98e5-a3e6079086b7</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_49f1d386-5bed-43ae-bd43-deabf7df64fc"></a>Term Name  bdqcore:49f1d386-5bed-43ae-bd43-deabf7df64fc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/49f1d386-5bed-43ae-bd43-deabf7df64fc-2024-02-04</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/49f1d386-5bed-43ae-bd43-deabf7df64fc</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-04</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:scientificNameAuthorship Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificNameAuthorship</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:scientificNameAuthorship is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:scientificNameAuthorship?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameAuthorship="(Györfi, 1952)": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameAuthorship is bdq:NotEmpty"],[dwc:scientificNameAuthorship="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameAuthorship is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/244</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:f6c58791-279d-458b-b4ee-058a73a002ee</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:scientificNameAuthorship? Validation for SingleRecord with Specification for: VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:e9ffc3b0-0fb8-4a7c-a588-a00085ba980b</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8"></a>Term Name  bdqcore:6eeac3ed-f691-457f-a42e-eaa9c8a71ce8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/6eeac3ed-f691-457f-a42e-eaa9c8a71ce8-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/6eeac3ed-f691-457f-a42e-eaa9c8a71ce8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:scientificNameID Complete</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty; COMPLIANT if (1) dwc:scientificNameID is a validly formed LSID, or (2) dwc:scientificNameID is a validly formed URN with at least NID and NSS present, or (3) dwc:scientificNameID is in the form scope:value, or (4) dwc:scientificNameID is a validly formed URI with host and path where path consists of more than just "/"; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:scientificNameID contain a complete identifier?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: complete</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Complete</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameID="urn:lsid:zoobank.org:act:17ADF24F-027F-44F6-9543-D3D0260CE79E": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameID contains a URI and a namespace indicator"],[dwc:scientificNameID="Hakea decurrens ssp. physocarpa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameID does not contain a URI"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2 December 2023</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li><li>Wikipedia (2024) LSID (Life Science Identifier). https://en.wikipedia.org/wiki/LSID</li><li>Wikipedia (2024) Uniform Resource Name (URN). https://en.wikipedia.org/wiki/Uniform_Resource_Name</ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If any single bdq:sourceAuthority such as GBIF is used, a valid and complete dwc:scientificNameID based on an alternative source authority is unlikely to provide a valid match. A text or number string as a namespace indicator without a URI will be ambiguous. As an example, GBIF's backbone taxonomy dataset can be found at https://doi.org/10.15468/39omei. When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID.  Note that GBIF currently uses "TaxonID" for this entity. The terms NID, NSS, and URN are all Uniform Resource Identifiers - see the Wikipedia (2024) reference.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/212</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:f2f40350-4081-4402-8b2b-95f9ad8893a7</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:scientificNameID contain a complete identifier? Validation for SingleRecord with Specification for: VALIDATION_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:e6c02558-8541-4292-9a11-2f4408d69699</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_401bf207-9a55-4dff-88a5-abcd58ad97fa"></a>Term Name  bdqcore:401bf207-9a55-4dff-88a5-abcd58ad97fa</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/401bf207-9a55-4dff-88a5-abcd58ad97fa-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/401bf207-9a55-4dff-88a5-abcd58ad97fa</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:scientificNameID Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:scientificNameID is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:scientificNameID?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameID="8fa58e08-08de-4ac1-b69c-1235340b7001": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameID is bdq:NotEmpty"],[dwc:scientificNameID=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameID is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/120</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:b1b04dc2-e74b-43f3-9f48-60ac08afcadb</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:scientificNameID? Validation for SingleRecord with Specification for: VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:02242018-3e73-4e0a-8d6f-d1db06cf81a3</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_88d8598b-3318-483d-9475-a5acf9887404"></a>Term Name  bdqcore:88d8598b-3318-483d-9475-a5acf9887404</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/88d8598b-3318-483d-9475-a5acf9887404-2024-02-09</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/88d8598b-3318-483d-9475-a5acf9887404</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-02-09</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:sex Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:sex</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; COMPLIANT if the value of dwc:sex is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:sex occur in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:sex="Male": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:sex found in the bdq:sourceAuthority"],[dwc:sex="f": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:sex not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul> <li>GBIF (2015) Darwin Core Vocabulary: Sex GBIF Vocabulary. https://rs.gbif.org/vocabulary/gbif/sex.xml</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. For reference, a list of synonyms for dwc:sex values can be found at https://registry.gbif.org/vocabulary/Sex/concepts.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/283</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:a0c48217-97a2-41e2-9540-61939f2628c5</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:sex occur in bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:72471db4-226c-454f-bbe8-5c1718e6c834</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SEX_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_85803c7e-2a5a-42e1-b8d3-299a44cafc46"></a>Term Name  bdqcore:85803c7e-2a5a-42e1-b8d3-299a44cafc46</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/85803c7e-2a5a-42e1-b8d3-299a44cafc46-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/85803c7e-2a5a-42e1-b8d3-299a44cafc46</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:startDayOfYear In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:startDayOfYear</td>
		</tr>
		<tr>
			<td>InformationElement:Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:startDayOfYear is bdq:Empty or if the value of dwc:startDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find single year or a start year in a range); COMPLIANT if the value of dwc:startDayOfYear is an integer between 1 and 365, inclusive, or if the value of dwc:startDayOfYear is 366 and the start year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:startDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="", dwc:startDayOfYear="15": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:startDayOfYear is in range"],[dwc:eventDate="", dwc:startDayOfYear="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:startDayOfYear is not in range"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>Kurator:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/23e4139d7f0ef71736f7fc7e984cfd2d0bfea093/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L832 Unit test at https://github.com/FilteredPush/event_date_qc/blob/5f2e7b30f8a8076977b2a609e0318068db80599a/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L609</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See test VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e).  This test only asks if dwc:startDayOfYear is a valid value for the relevant year, not if it is consistent with the start day of the range specified in dwc:eventDate. In a non-leap year, the valid range is 1-365 inclusive, in a leap year 366 is also valid. This test should be run after the series of tests that assure that dwc:eventDate is populated, if possible (i.e., AMENDMENT_EVENTDATE_FROM_VERBATIM (6d0a0c10-5e4a-4759-b448-88932f399812), AMENDMENT_EVENTDATE_STANDARDIZED (718dfc3c-cb52-4fca-b8e2-0e722f375da7), and AMENDMENT_EVENT_DATE_FROM_YEARMONTHDAY (3892f432-ddd0-4a0a-b713-f2e2ecbd879d)).</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/130</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:c3d0ce9b-2f40-4cd7-8e67-085b137e8e89</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:startDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year? Validation for SingleRecord with Specification for: VALIDATION_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:53c6af68-6120-4da6-87d8-a3e9551b9671</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_STARTDAYOFYEAR_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a"></a>Term Name  bdqcore:4daa7986-d9b0-4dd5-ad17-2d7a771ea71a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4daa7986-d9b0-4dd5-ad17-2d7a771ea71a-2024-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4daa7986-d9b0-4dd5-ad17-2d7a771ea71a</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:stateProvince Found</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dcterms:Location</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:stateProvince</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:stateProvince is bdq:Empty; COMPLIANT if the value of dwc:stateProvince occurs as an administrative entity that is a child to at least one entity representing an ISO 3166 country-like entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:stateProvince occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:stateProvince="Florida": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:stateProvince found in bdq:sourceAuthority"],[dwc:stateProvince="Taswegian": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:stateProvince not found in bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>Getty Research Institute (2017) Getty Thesaurus of Geographic Names Online. https://www.getty.edu/research/tools/vocabularies/tgn/index.html</li><li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li><li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li><li>ISO (n.dat) 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Multiple values in the dwc:stateProvince field (whether to signify on a border or in a list of possibilities) will fail this test. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/199</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:eebb4a3c-30e8-43e5-96f5-eded890dd174</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:stateProvince occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:d261fac1-ce61-4879-bc04-870fa885b578</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_STATEPROVINCE_FOUND</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_06851339-843f-4a43-8422-4e61b9a00e75"></a>Term Name  bdqcore:06851339-843f-4a43-8422-4e61b9a00e75</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/06851339-843f-4a43-8422-4e61b9a00e75-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/06851339-843f-4a43-8422-4e61b9a00e75</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-06</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:Taxon Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:taxonID,dwc:scientificNameID,dwc:acceptedNameUsageID,dwc:parentNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:scientificName,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:infragenericEpithet,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:vernacularName,dwc:cultivarEpithet</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if at least one term needed to determine the taxon of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in any of the terms needed to determine that the taxon exists?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:parentNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Eucalyptus gunnii", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:superfamily="", dwc:tribe="", dwc:subtribe="",  dwc:family="", dwc:genus="", dwc:subgenus="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:vernacularName="" : Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="at least enough terms exist that identify that an entity exists"],[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:parentNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:superfamily="", dwc:tribe="", dwc:subtribe="",  dwc:family="", dwc:genus="", dwc:subgenus="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:vernacularName="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All input fields are bdq:Empty or missing"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Lee Belbin</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This tests for records that have no taxonomic (NAME) information. If there is any value for any of the Information Elements, this may be useful information. See example.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/105</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:9c5798cd-6176-41ed-8e91-35e3df1fa6d4</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in any of the terms needed to determine that the taxon exists? Validation for SingleRecord with Specification for: VALIDATION_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:f38e3644-354d-4180-bc7c-c437cef1d606</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXON_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4c09f127-737b-4686-82a0-7c8e30841590"></a>Term Name  bdqcore:4c09f127-737b-4686-82a0-7c8e30841590</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4c09f127-737b-4686-82a0-7c8e30841590-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4c09f127-737b-4686-82a0-7c8e30841590</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:Taxon Unambiguous</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:taxonID,dwc:scientificName,dwc:scientificNameID,dwc:acceptedNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:infragenericEpithet,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:cultivarEpithet,dwc:vernacularName,dwc:scientificNameAuthorship,dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of dwc:scientificNameID, dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, dwc:cultivarEpithet are bdq:Empty; COMPLIANT if (1) dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority, or (2) dwc:scientificNameID is bdq:Empty and dwc:scientificName references a single taxon record in the bdq:sourceAuthority, or (3) if dwc:scientificName and dwc:scientificNameID are bdq:Empty and if a combination of the values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:cultivarEpithet, dwc:taxonRank, and dwc:scientificNameAuthorship can be unambiguously resolved to a unique taxon in the bdq:sourceAuthority, or (4) if ambiguity produced by multiple matches in (2) or (3) can be disambiguated to a unique Taxon using the values of dwc:tribe, dwc:subtribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID and dwc:vernacularName; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Can the taxon be unambiguously resolved from bdq:sourceAuthority using the available taxon terms?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: unambiguous</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Unambiguous</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Triplex rosaria Perry, 1811", dwc:higherClassification="", dwc:kingdom="Animalia", dwc:phylum="mollusca", dwc:class="Gastropoda", dwc:order="", dwc:family="Muricidae", dwc:subfamily="", dwc:genus="Chicoreus", dwc:genericName="Triplex", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="rosarium", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="Perry, 1811", dwc:taxonRank="",bdq:sourceAuthority=”marinespecies.org”: Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName matched to unique taxon record in WoRMS, unique fuzzy match on name and exact match on authorship.  "],[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Graphis", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:family="", dwc:subfamily="", dwc:genus="", dwc:genericName="", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="", dwc:taxonRank="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName="Graphis" is ambiguous as could be either a lichen or a gastropod."]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, CRIA</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>There are any number of potential controlled vocabularies that might be used for this test, including local vocabularies and taxon specific vocabularies. If dwc:scientificNameID is empty, use dwc:scientificName and dwc:CultivarEpithet to search for a unique taxon.  If dwc:scientificName is bdq:Empty, check with the terms that form atomic parts of it (dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:taxonRank, dwc:scientificNameAuthorship), and if more than one match is found, use the remaining terms to try to disambiguate to a single Taxon record.   The terms dwc:subgenus, dwc:genus, dwc:family, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:scientificNameID,, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID should not be used to make a match if dwc:scientificNameID and dwc:scientificName or dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:taxonRank, dwc:scientificNameAuthorship are bdq:Empty.  Note that test VALIDATION_SCIENTIFICNAME_FOUND (4c09f127-737b-4686-82a0-7c8e30841590) is a more specific test for a subset of Information Elements from this test.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/70</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:55b60dd8-7054-4736-b9ac-88bef8967fb2</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Can the taxon be unambiguously resolved from bdq:sourceAuthority using the available taxon terms? Validation for SingleRecord with Specification for: VALIDATION_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:8bd6f6de-49e4-4889-82e0-e4af093981e0</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXON_UNAMBIGUOUS</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_14da5b87-8304-4b2b-911d-117e3c29e890"></a>Term Name  bdqcore:14da5b87-8304-4b2b-911d-117e3c29e890</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/14da5b87-8304-4b2b-911d-117e3c29e890-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/14da5b87-8304-4b2b-911d-117e3c29e890</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:taxonRank Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:taxonRank is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:taxonRank?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonRank="genus": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:taxonRank is bdq:NotEmpty"],[dwc:taxonRank=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:taxonRank is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF (2015) Taxonomic Rank GBIF Vocabulary. https://rs.gbif.org/vocabulary/gbif/rank.xml</li></ul></td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/161</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:dbb803cb-8b37-4db3-a562-b4f6036f9d17</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:taxonRank? Validation for SingleRecord with Specification for: VALIDATION_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:c619ec9b-92ec-4047-a8d3-931e3324bf3e</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXONRANK_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_7bdb13a4-8a51-4ee5-be7f-20693fdb183e"></a>Term Name  bdqcore:7bdb13a4-8a51-4ee5-be7f-20693fdb183e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/7bdb13a4-8a51-4ee5-be7f-20693fdb183e-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/7bdb13a4-8a51-4ee5-be7f-20693fdb183e</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:taxonRank Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; COMPLIANT if the value of dwc:taxonRank is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:taxonRank occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonRank="kingdom": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:taxonRank has an equivalent in the bdq:sourceAuthority"],[dwc:taxonRank="sp.": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:taxonRank does not have an equivalent in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Registry (2023) GBIF Vocabulary: Taxonomic Rank. https://registry.gbif.org/vocabulary/TaxonRank/concepts</li></ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/162</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:e95df0f4-b6b6-4e04-ad00-95eef6e8d993</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:taxonRank occur in the bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:c8964200-630e-47c6-baad-7e334fddbbdb</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXONRANK_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_4833a522-12eb-4fe0-b4cf-7f7a337a6048"></a>Term Name  bdqcore:4833a522-12eb-4fe0-b4cf-7f7a337a6048</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/4833a522-12eb-4fe0-b4cf-7f7a337a6048-2024-08-03</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/4833a522-12eb-4fe0-b4cf-7f7a337a6048</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-07</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-03</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:typeStatus Standard</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Occurrence</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:typeStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; COMPLIANT if the value of the first word in each \</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core typeStatus" {[https://dwc.tdwg.org/list/#dwc_typeStatus]} {dwc:typeStatus vocabulary API [https://gbif.github.io/parsers/apidocs/org/gbif/api/vocabulary/TypeStatus.html]}</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:typeStatus occur in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:typeStatus="Holotype": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:typeStatus found in the bdq:sourceAuthority"],[dwc:typeStatus="cleptotype": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:typeStatus not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul> <li> GBIF (2021) Darwin Core Vocabulary: Nomenclatural Type Status Vocabulary. http://rs.gbif.org/vocabulary/gbif/type_status </li> </ul></td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/285</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:f84d0f30-9c93-43a4-8f75-8c853fc18fb5</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Does the value of dwc:typeStatus occur in bdq:sourceAuthority? Validation for SingleRecord with Specification for: VALIDATION_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:e4dbf38d-bdd7-4cf7-8c60-5b3bfc6af4ff</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TYPESTATUS_STANDARD</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_ad0c8855-de69-4843-a80c-a5387d20fbc8"></a>Term Name  bdqcore:ad0c8855-de69-4843-a80c-a5387d20fbc8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/ad0c8855-de69-4843-a80c-a5387d20fbc8-2024-08-23</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/ad0c8855-de69-4843-a80c-a5387d20fbc8</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2024-08-23</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:year In Range</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:year</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:earliestValidDate,bdq:latestValidDate</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:year is bdq:Empty or cannot be interpreted as an integer; COMPLIANT if the value of dwc:year is within the range bdq:earliestValidDate to bdq:latestValidDate inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>AuthoritiesDefaults</td>
			<td>bdq:earliestValidDate="1582",bdq:latestValidDate=current year</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:year within the Parameter range?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Conformance: inrange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:year="1952": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:year is in RANGE"],[dwc:year="9999": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:year is not in RANGE. The value in year has not yet come to pass."]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush:event_date_qc</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc [DwCEventDQ.validationYearInrange()]( https://github.com/FilteredPush/event_date_qc/blob/07f5a338c595c345cd6a0243df511cc752386d99/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L2163)  [unit test](https://github.com/FilteredPush/event_date_qc/blob/07f5a338c595c345cd6a0243df511cc752386d99/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L1945)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The results of this test are time-dependent. Next year is not valid now. Next year it will be. This test provides the option to designate lower and upper limits to the year. The upper limit, if not provided, should default to the year when the test is run. This test provides for a default earliest date (year), of 1582 by convention. That value was chosen because ISO 8601-1 asserts that "the use of proleptic Gregorian calendar dates prior are not allowed in ISO 8601-1 without prior agreement of the parties exchanging data", and Darwin Core provides no such prior agreement.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/84</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:7922ab56-6eae-4257-9691-d55d24842274</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the value of dwc:year within the Parameter range? Validation for SingleRecord with Specification for: VALIDATION_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:aee43366-0352-448a-a5ea-85ddc8605da1</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_YEAR_INRANGE</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_c09ecbf9-34e3-4f3e-b74a-8796af15e59f"></a>Term Name  bdqcore:c09ecbf9-34e3-4f3e-b74a-8796af15e59f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/c09ecbf9-34e3-4f3e-b74a-8796af15e59f-2023-09-17</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/c09ecbf9-34e3-4f3e-b74a-8796af15e59f</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-04</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-17</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation dwc:year Not Empty</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Event</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:year</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>COMPLIANT if dwc:year is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:year?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Completeness: notempty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:year="1949": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:year is bdq:NotEmpty"],[dwc:year="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:year is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FilteredPush/Kurator:event_date_qc [10.5281/zenodo.596795](https://doi.org/10.5281/zenodo.596795).</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>event_date_qc v3.0.0 [DwCEventDQ.validationYearNotEmpty()](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L217)</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/49</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:2a0843de-32f9-473e-984a-619dace9ee66</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is there a value in dwc:year? Validation for SingleRecord with Specification for: VALIDATION_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:42f331f4-a5a8-48b4-a08e-57048d1d1a77</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_YEAR_NOTEMPTY</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcore_17f03f1f-f74d-40c0-8071-2927cfc9487b"></a>Term Name  bdqcore:17f03f1f-f74d-40c0-8071-2927cfc9487b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/version/17f03f1f-f74d-40c0-8071-2927cfc9487b-2023-09-18</td>
		</tr>
		<tr>
			<td>term_iri</td>
			<td>https://rs.tdwg.org/bdqcore/terms/17f03f1f-f74d-40c0-8071-2927cfc9487b</td>
		</tr>
		<tr>
			<td>issued</td>
			<td>2024-09-05</td>
		</tr>
		<tr>
			<td>DateLastUpdated</td>
			<td>2023-09-18</td>
		</tr>
		<tr>
			<td>prefLabel</td>
			<td>Validation Polynomial Consistent</td>
		</tr>
		<tr>
			<td>IE Class</td>
			<td>dwc:Taxon</td>
		</tr>
		<tr>
			<td>InformationElement:ActedUpon</td>
			<td>dwc:scientificName,dwc:genericName,dwc:specificEpithet,dwc:infraspecificEpithet</td>
		</tr>
		<tr>
			<td>Specification</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty, or all of dwc:genericName, dwc:specificEpithet and dwc:infraspecificEpithet are bdq:Empty; COMPLIANT if the polynomial, as represented in dwc:scientificName, is consistent with bdq:NotEmpty values of dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the polynomial represented in dwc:scientificName consistent with the equivalent values in dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet?</td>
		</tr>
		<tr>
			<td>Criterion Label</td>
			<td>Consistency: consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificName="Hakea decurrens ssp. physocarpa", dwc:genericName="", dwc:specificEpithet="decurrens", dwc:infraspecificEpithet="physocarpa": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Values of all non-empty atomic terms are found in the polynomial"],[dwc:scientificName="Hakea decurrens", dwc:genericName="Hakea", dwc:specificEpithet="decurrens", dwc:infraspecificEpithet="physocarpa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is inconsistent with atomic parts (dwc:genus, dwc:specificEpithet and dwc:infraspecificEpithet)"]</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paula Zermoglio</td>
		</tr>
		<tr>
			<td>References</td>
			<td><ul><li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li></ul></td>
		</tr>
		<tr>
			<td>Example Implementations (Mechanisms)</td>
			<td>FP-Akka</td>
		</tr>
		<tr>
			<td>Link to Specification Source Code</td>
			<td>https://github.com/FilteredPush/FP-KurationServices/blob/master/src/main/java/org/filteredpush/kuration/util/SciNameServiceUtil.java#L97</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If dwc:specificEpithet is populated then this test expects that the value dwc:specificEpithet is the name of the second or species epithet of the scientificName.  If dwc:genericName is populated, this test expects that the value of dwc:genus is the first word of the value of dwc:scientificName.  If dwc:specificEpithet is populated then this test expects that the value dwc:specificEpithet is the name of the first or species epithet of the scientificName.  If dwc:infraspecificEpithet is populated, then this test expects that the value of dwc:infraspecificEpithet is the name of the lowest or terminal infraspecific epithet of the scientificName, excluding any rank designation.</td>
		</tr>
		<tr>
			<td>UseCases</td>
			<td>bdq:Record-Management, bdq:Taxon-Management</td>
		</tr>
		<tr>
			<td>skos:historyNote</td>
			<td>https://github.com/tdwg/bdq/issues/101</td>
		</tr>
		<tr>
			<td>bdqffdq:ValidationMethod</td>
			<td>urn:uuid:94510668-a59f-41d3-84bb-30cd9715cb62</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: Is the polynomial represented in dwc:scientificName consistent with the equivalent values in dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet? Validation for SingleRecord with Specification for: VALIDATION_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>bdqffdq:Specification</td>
			<td>urn:uuid:d92c5e23-bf6a-483b-86c3-9374e12d01c7</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_POLYNOMIAL_CONSISTENT</td>
		</tr>
	</tbody>
</table>



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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core Tests and Assertions List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


