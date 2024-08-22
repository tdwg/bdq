# Title: BDQ Core Introduction

**Date version issued**: (Draft)

**Date created**: (Draft)

**Part of TDWG Standard**: 

**This version**:

**Latest version**:

**Previous version**:

**Abstract**: The **BDQ (Biodiversity Data Quality) Core** is a set of vocabularies designed to represent metadata for biodiversity data quality tests and assertions. These vocabularies aim to represent information that will help to determine whether a particular resource will be fit for use for some particular application from the perspectives of data quality dimensions such as completeness, conformance, consistency, etc.

**Contributors**

Lee Belbin, Arthur D. Chapman, Paul Morris, John R. Wieczorek, Paula Zermoglio, Alex Thompson and Yi Ming Gan.

**Creator**

TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions).

**Bibliographic citation**

BDQ Core Maintenance Group. 2024. BDQ Core Introduction. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/bdq/doc/introduction/2024-08-21

### Table of Contents ###

```
1 Introduction
1.1 Audience
1.2 Status of the content of this document
1.3 RFC 2119 keywords
1.4 Namespace abbreviations
1.5 BDQ Core Tests and Assertions
1.6 Test Specifications
1.7 Framework for describing data quality

2 Guidance for Consumers of Data Quality Reports
2.1 Introduction
2.2 Biodiversity Data Quality Tests
2.2.1 Introduction
2.2.2 Tests
2.2.3 Notes on tests
2.2.3.1 Events and Calendars

3 A Framework for Data Quality
3.1 Introduction
3.2 Framework

4 Vocabularies
4.1 Introduction
4.2 Vocabularies

5 Test specifications
5.1 Introduction
5.1.1 Parameters
5.1.2 Workflows and Sequencing Test
5.1.3 Amendments where order is important
5.2 Implementation
5.3 Extension points
5.4 Core Test Specifications
5.5 Multi-Record Measure Specifications

6 Validating test implementations
6.1 Introduction
6.2 Considerations Concerning Input Data Values for AMENDMENTS
6.3 Test Data Specifications
6.4 Example data for validating tests
6.5 Where to get the Test Data
6.6 Implementation
6.7 Identifying example data

7 Implications for the Darwin Core Standard (John)

8 Acknowledgements

9 Acronyms

10 References

11 Supplement: Rationale Management Documentation
``` 

## 1. Introduction

BDQ (Biodiversity Data Quality) Core is a standard that consists of 1) a generic data quality framework as an ontology that provides terms and semantics, 2) a vocabulary of tests whose specifications can be implemented to provide reproducible results from a given set of input data and consistent test parameters, 3) a vocabulary of terms used in the specification of the previously mentioned tests, 4) a controlled vocabulary for the term bdq:dimension from the previously mentioned test specification terms, 5) an exemplar data set to use as input for implementations of the previously mentioned tests, 6) an exemplar implementation of the tests, in Java(R), which uses the previously mentioned test data set as input and demonstrates the expected responses to each of the tests, 7) a guide to implementation of the tests are included, and 8) a guide to interpretation of the results of the tests. 

### 1.1 Audience
This document is designed for anyone who needs an introduction or orientation to the set of standard specifications to assess or assure fitness for use of biodiversity data, or to improve it.

### 1.2. Status of the content of this document

All sections of this document are non-normative unless explicitly noted as normative.

### 1.3 RFC 2119 keywords

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.4 Namespace abbreviations

The following namespace abbreviations are used in this document:

**CHECK THIS on final draft**

| **Prefix**   | **Namespace**                                    |
|--------------|--------------------------------------------------|
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms                |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms                 |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| owl          | http://www.w3.org/2002/07/owl#                   |

### 1.5 BDQ Core Tests and Assertions

This standard is a specification of tests for the quality of biodiversity data, not a specification of the quality to which biodiversity data are expected to conform. ‘Fitness for use’ of a biodiversity data record will greatly depend on the use to which it is applied: A record that is unsuitable to be used in one application may be suitable for another application (Belbin et al 2013).

The tests are intended for use in quality control and quality assurance of biodiversity data. They serve to assess the fitness for use of biodiversity occurrence data for uses where key components of Darwin Core encoded records are important for an application.

CORE tests are all defined as single record-level (bdqffdq:SingleRecord) tests, applying to a single observation or event structured under Darwin Core terms (Wieczorek et al 2012). The one exception to this is the test ISSUE_ANNOTATION_NOTEMPTY where this standard encourages the implementation of a standard for annotating occurrence records supported by Darwin Core. This test is an example of what the team calls 'aspirational tests', suggesting that supporting infrastructure seems well-justified. 

[!--- suggest "Single record (bdqffdq:SingleRecord) tests apply to a single observation or event structured under Darwin Core terms (Wieczorek et al 2012). The one exception to this is the test ISSUE_ANNOTATION_NOTEMPTY where this standard encourages the implementation of a standard for annotating occurrence records supported by Darwin Core. Multi record (bdqffdq:MultiRecord) tests sum up results across all records for each single record test."   AC - PAUL to check?  ---]

Tests may require reference to external data such as standard vocabularies of terms or names. While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

We acknowledge the centrality of the work of the TDWG Annotations Interest Group (https://github.com/tdwg/annotations) as to how the test results are reported against records. Test results structured with these three components can be readily wrapped in the body annotation document that follows the W3C Web Annotation Data Model (Sanderson et al. 2017), along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.

#### Definition of EMPTY

We need a reusable definition for EMPTY that can apply in any test where the concept is relevant. Here we define EMPTY as an information element that is either not present or does not contain any characters or values other than those in the range U+0000 to U+0020. 

An information element containing invalid characters (e.g. letters in an information element that would be expected to contain integers) or values (including string serializations of the NULL value) are NOTEMPTY and may be separately detected. The phrase "not present" is there to cover cases where a test implementation cannot tell if a particular data set under test includes a particular Darwin Core term. This allows the test implementations to be independent of, and agnostic about frameworks within which the tests are run, the nature of the data. For csv data, a column is either there or not in a data set, but in an rdf representation, some data objects could have relevant properties and others not - and the tests are independent of that. We considered, and explicitly rejected, treating common string serializations of null such as \N and NULL as empty values. If "\N" is present in a data set, the tests will explicitly treat that value as NOTEMPTY, and then try to evaluate it against whatever other criteria apply. 

This definition is not applicable to a discussion of what value to include in a controlled vocabulary to indicate that no meaningful value is present, so no suggestion is made that "EMPTY" should be used as a data value to represent some form of "Null", "Unknown", "Not Recorded", etc. Choices there would fall into the semantics for some set of controlled vocabularies. The relevance to such a discussion is that this definition would treat an empty string as an empty value, with no semantics attached as to why the value is empty.

#### Characteristics of the tests

Each test is defined as a SingleRecord test. No CORE tests have been defined to use data in other records within a data set to evaluate the quality of data in a SingleRecord. The framework allows for MultiRecord tests able to identify outliers within a data set, or other tests that look across a MultiRecord to evaluate data quality, but we have not specified any such tests here.

The scope of each test is also largely provided by the bdqffdq:Specification. The Darwin Core terms used in the Specification are included in the "Information Elements". The "Specification" also includes references to external (to the Darwin Core standard) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource required for the implementation of the test.

The tests are agnostic about the form in which the data are stored or transported. The test specifications all assume that data are presented to the tests in structured form such as csv or tab delimited text files, with data elements identifiable as Darwin Core terms (Wieczorek et al. 2012). Here, cells contain non-typed data values possibly aggregated from and serialized from multiple sources such as relational databases where Boolean nulls and non-string data types may exist, but the data have been exported into a string serialization that supports neither null nor typed data. 

The tests are also agnostic about uses for quality assurance, where output data are limited to those for which all Validations are Compliant, or for quality control where the results of Validations, Issues, Measures, and Amendments can be used to improve the quality of the data.

The test specifications are agnostic about where in the biodiversity data lifecycle they are used. Implementers can incorporate the tests at any stage to help identify and correct issues. The tests can be applied during data capture in the field, transcription from paper records, data ingestion into databases, integration with collections management systems, data aggregation, and research on aggregated biodiversity data. They are designed to run at any point in the data lifecycle, from initial collection or observation to data transcription, database loading, and preparation for or during data aggregation. [However, the framing of the InformationElements as Darwin Core terms with the CORE Use Case focused on the research needs of downstream users means that competing requirements have led to some different decisions than would have been made if the aim was to solely evaluate data in a database of records and preparing it for aggregation.]   


#### Types of tests

The concept of 'tests' in the context of this standard include four distinct types: VALIDATION; ISSUE; AMENDMENT and MEASURE.

##### Structure of Response

Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags,  The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary (consisting of exactly COMPLIANT or NOT_COMPLIANT) for validations or Issues (NOT_ISSUE, POTENTIAL_ISSUE, ISSUE), either a numeric value or a controlled vocabulary (consisting of exactly COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments. 
2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 
3. Remark supplies human-readable text describing reasons for the test result output.


##### VALIDATION 

A VALIDATION evaluates the values in one or more Darwin Core terms for fitness for some particular narrow data quality need within CORE. Validations evaluate values or in some cases, presence or lack of a value. Validation tests are phrased as positive statements, consistent with the "Fitness for Use Framework".  A Validation tests to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY, is phrased as "Not Empty", and will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem. The formal response of VALIDATIONs can take one of four forms:

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation.
4. A Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 


##### ISSUE

ISSUE is a form of warning flag where the test is drawing attention to a non-empty value of a Darwin Core term. We have used these for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of this case would take human review. For example, ISSUE_ANNOTATION_NOTEMPTY is informing the tester than there is at least one annotation associated with record and this should be evaluated before using the record. Similarly for the other two ISSUE-type tests: ISSUE_DATAGENERALIZATIONS_NOTEMPTY where some form of transformation has occurred, and ISSUE_ESTABLISHMENTMEANS_NOTEMPTY where the value needs to be assessed for utility. ISSUEs are currently outside the Data Quality Fitness for Use Framework. ISSUEs result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "IS_ISSUE", "POTENTIAL_ISSUE" or "NOT_ISSUE". ISSUE is symmetrical to NOT_COMPLIANT, NOT_ISSUE is approximately symmetrical to COMPLIANT, and POSSIBLE_ISSUE does not have an equivalent Validation Response.result. 

##### AMENDMENT

An AMENDMENT may propose a change or addition to at least one Darwin Core term that is intended to improve one or more components of the quality of the record.  The Response.result from an AMENDMENT MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for QualityControl of an existing database or record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  Amendments, under the framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in these tests.  

##### MEASURE 

A MEASURE may return either a Response.result that is a numeric value, or the values COMPLETE or NOT_COMPLETE, or NOT_REPORTED (when the Response.status="INTERNAL_PREREQUISITES_NOTMET").  The principle Measure defined in the core tests is MEASURE_EVENTDATE_DURATIONINSECONDS, it returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the VALIDATIONs and AMENDMENTs and in one case provides an indication of the length of the period of the value of dwc:eventDate.

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

### 1.6 Test Descriptors (Informative) 

<!--- **TODO: What do we call this as "Specification is being used generally and specifically?** --->
<!--- We can use Descriptor for Specification plus related metadata (the rows in the Markdown tables), Specification for the framework concept. --->

The Test Descriptors are those terms that are necessary to comprehensively describe the test. Some terms, such as the GUID are intended for machine consumption. Some terms such as the "Description" are designed to be human-readable and to be understood by consumers of biodiversity data quality reports. Terms such as the "Specification" ensure that implementers have no ambiguity about how the test should be coded. 

#### Parameterising the tests

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. This allows us to define general tests that provide support for non functional requirements that vary within the community. 

For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite. Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 

#### Data Quality Dimensions 

The scope of the standard is the fundamental information about core tests applied to occurrence type Darwin Core records. These tests evaluate one of Data Quality Dimension of the Fitness for Use Framework (Chapman et al., 2020): Measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved. These dimensions are:

* Completeness: The extent to which data are present and sufficiently comprehensive for use.
* Conformance: Conforms to a format, syntax, data type, range, or standard of the Information Element.
* Consistency: Agreement among related Information Elements (q.v.) that are present in the data. Note that missing Information Elements do not make a test Inconsistent.
* Likeliness: The likelihood of Darwin Core Term(s) having true or expected values.
* Reliability: Measure of how the data values agree with an identified source of truth. The degree to which data correctly describes the truth (object, event or any abstract or real 'thing').
* Resolution: Refers to the data having sufficiently detailed information. Measure of the granularity of the data, or the smallest measurable increment.


A "Warning Type" for each test was originally envisioned to provide insight into the nature of the issues, but a review the relationship with "Data Quality Dimension" across the tests suggested such a high degree of correlation that "Warning Type" is effectively redundant. See table xx below. **NEEDS UPDATING**

| Data Quality Dimension/Warning Type | Ambiguous | Amended | Incomplete | Inconsistent | Invalid | Issue | Report | Unlikely | Total |
|-------------------------------------|-----------|---------|------------|--------------|---------|-------|--------|----------|-------|
| Completeness                        |           |   11    |    19      |              |         |   1   |    2   |          |  33   |
| Conformance                         |     2     |   13    |            |       3      |    35   |       |        |          |  53   |
| Consistency                         |           |    1    |            |       5      |         |       |        |          |   6   |
| Likeliness                          |           |         |            |              |         |       |        |     2    |   2   |
| Reliability                         |           |         |            |              |         |   1   |    2   |          |   3   |
| Resolution                          |           |         |            |              |         |   1   |    1   |          |   2   |
| Total                               |     2     |   25    |    19      |       8      |    35   |   3   |    5   |     2    |  99   |

Caption: Data Quality Dimension vs Warning Type with the number of tests as cell values. 



Tests are paired in that all AMENDMENTs require a corresponding VALIDATION that assesses some aspect of data quality. An AMENDMENT may be able to improve the quality of data with respect to that VALIDATION. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values. 

### 1.7 Framework for describing data quality (Paul) (Informative)
Included in this standard is a specification for a framework for describing data quality. Each of the tests in this standard has been designed within this framework and is framed using the terms and concepts from the framework. The framework provides the context for each test, and has shaped decisions made about each test.

The framework data quality with respect to some specified use.  It provides a means to describe a use of data, and what is needed for some data set to have quality for that use, that is for some data set to be fit for a specified purpose.  The framework explicitly links data quality to use, and allows formal description of means to assure that data are fit for some specified purpose.  

* Data Quality Control, Data Quality Assurance.

The framework draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data. Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.

* Data Quality Needs, Data Quality Mechanisms, Data Quality Reports.

The framework organizes data quality concepts into three areas: Needs, Mechanisms, and Reports. Data Quality Needs identify a use to which data may be put, and frame a set of requirements that data needs to meet to be fit for that use, and means by which data not fit for that use may be improved.  The tests described in this standard are formal descriptions of data quality needs for CORE purposes.  Data Quality Mechanisms in the framework are formal descriptions of software and other mechanisms that implement tests described in the Needs area.  Data Quality Reports are the results produced by Mechanisms on some set of data.  The tests described in this standard include specifications of assertions to be made in Data Quality Reports.

<!--- Ming: Test types: Validation, Amendment, Measure, Issue, repeated in 1.5 --->

* Horizontal: Needs, Reports, Vertical: Test informal, describes both need and reporting.

The framework defines four descriptors of data quality needs: Amendments, Measures, Validations, and Issues.  

Amendments propose changes to data or processes that, if accepted, may improve the fitness of data for a specific use.

Measures measure some specific aspect of data quality.

Validations assess compliance with a need.  Data have quality if they are compliant with the requirements of the validation test.

Issues are the converse of Validations.  Data lack quality if an issue identifies a potential problem in the data that would require further human review to identify if the data have quality for some purpose.  

The framework has an abstract concept of Information Elements. To frame tests on Darwin Core terms in a usable way, we list specific Darwin Core terms as the information elements in each test.

Formally, in the Data Quality Needs level, the framework starts with a Use Case, a framing of some use to which data may be put.  Use cases are related to the formal description of data quality needs through policies and contexts.  Contexts (ContextualizedCriterion, ContextualizedDimension, ContextualizedEnhancement, ContextualizedIssue) relate the specification of a need, such as a Validation, to the information elements that need to be examined, and to the resource type that is operated on.  Each of the tests described in this standard has a formal specification that includes each of these elements.   A Use Case includes a set of policies, policies relate the use case to contexts, contexts link information elements to needs and to resource types, a need specify what properties data must have to have quality.   

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

	<rdf:Description rdf:about="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/Specification"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code; otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</rdfs:comment>
	</rdf:Description>

	<rdf:Description rdf:about="urn:uuid:54fdf7a8-c1b1-4c21-b0a2-1f5aa86d3461">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ValidationMethod"/>
    	<criterionInContext xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9"/>
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

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, repeated in 5.2.3 --->
The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   


## 2. Guidance for Consumers of Data Quality Reports (Informative)

### 2.1 Introduction (Arthur) (Informative)
An internationally agreed standard suite of core tests and resulting assertions can be used by all data providers, data collectors and data users to improve the quality of the data. This will allow for more appropriate and more accurate use of biodiversity data. Other than data availability, ‘Data Quality’ is probably the most significant issue for users of biodiversity data and this is especially so for the research community. The tests will not correct all issues that exist with the data, but reports from the tests will identify issues that need to be addressed by users of the data. This may require the user to make decisions on the data - i.e., data that may need to be excluded, data that may need examining for possible improvement, and data that can be used as is. It is always the purview of the user to decide what data is of suitable quality for their use.

### 2.2 Biodiversity Data Quality Tests (Informative)
What are the important attributes of data quality for biodiversity data?  How are we proposing to assess data quality in the domain?  What is the scope of the tests?   What is out of scope for the tests.  How did we develop the test specifications? 

We identified four fundamental aspects of biodiversity-related data that we needed to cover with the tests: Name (taxonomic information); space (geographic location); time (temporal terms) and other (all other terms such as dwc:basisOfRecord). A record without a taxonomic name, a location or a date has limited value. Three tests in this standard specifically target records with no name, space or time values.

#### **2.2.2 Tests (Informative)**

The intent of the tests...

#### **2.2.3 Notes on Tests (Informative)**

* https://github.com/tdwg/bdq/blob/master/tg2/core/TG2_tests.csv
* https://github.com/tdwg/bdq/blob/master/tg2/core/TG2_tests.xml

## 3. A Framework for Data Quality (Paul)

[need to migrate from https://raw.githubusercontent.com/kurator-org/kurator-ffdq/master/competencyquestions/rdf/ffdq.owl to tdwg repository]

### 3.1 Introduction

### 3.2 Framework (Normative)

[Include generated text]

## 4. Vocabularies (Arthur)

### 4.1 Introduction
The included vocabulary (see Supplement 2) is of terms used for the Data Quality Tests and Assertions. The definitions are a subset of the definitions from the Fitness for Use Framework (Veiga et al. 2017) as documented in <!---OWL DOCUMENT - Paul --->. The definitions used in the tests conform with the Framework definitions, but may be used in a more restricted way than as laid out there. Where this is the case, it is noted in the comments. A column in the Vocabulary indicates the Context in which the terms are used. All terms that are specific to the Tests have a bdq: namespace prefix, those from the Fitness for Use Framework, a bdqffdq: namespace prefix. A separate column provides the name without the prefix. In the GitHub tables, the terms are given without the name space prefix, and the four Test Types (AMENDMENT, ISSUE, MEASURE and VALIDATION) are given in all upper case, even though they are upper/lower case in the vocabulary (e.f. bdqffdq:Amendment)

**Data Quality Dimensions**

Data Quality Dimensions terms, used as values for the Fitness for Use Framework **Data Quality Dimension** are used in the test descriptions and are defined in a [separate document](https://github.com/tdwg/bdq/blob/master/tg2/vocabularies/data_quality_dimensions.csv) TODO: Build RDF and human readable documents from that file, include human readable here.

### 4.2 Vocabularies
1. Framework Glossary - <!---Owl Paul?--->
2. Vocabulary of the terms used within the Tests and Assertions (Currently at #152) SUPP 2
3. List of Namespace terms used in the Tests and Assertions (Currently at #205) SUPP
4. Data Quality Dimension RDF document

[Include generated text]

## 5. Test Specifications (Paul)

### 5.1 Introduction (Informative)

Column headers in https://github.com/tdwg/bdq/blob/master/tg2/core/TG2_tests.csv  TODO: Generate human readable test descriptor document, labels here will apply in that document.  

**TODO: rs.tdwg.org namespace.**

**TODO:VersionDate** The most recent date of update to any element of a test.

**"#"**:"20" The github.com/tdwg/bdq/issues/{number} where documentation of the rationale management conversations for the development of the tests can be found.  See supplement [Section 10](https://github.com/tdwg/bdq/wiki/TG2-Tests-and-Assertions-Standards-Document#10-supplement-rationale-management-documentation) for descriptions of the terminology used in the issues (which do not fully conform to the Framework). 

The number is present in the Markdown document as **Rationale Management** linking to https://github.com/tdwg/bdq/issues/{n}.

<!--- Ming: vocabularies --->

**"GUID"** [Normative]:"0493bcfb-652e-4d17-815b-b0cce0742fb" A machine readable unique identifier for the test 

**"Label"** [Normative]:"VALIDATION_COUNTRYCODE_STANDARD" A human readable label identifying the test.  The labels largely follow the pattern TYPE_INFORMATIONELEMENT_STATUS.

**"Description"** [Informative]:"Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?" A non-technical description of what the test does, intended for consumers of data quality reports in concert with the Response.comment.

**"TestType"** [Normative]:"Validation" The Type of assertion that this test produces, Measure, Validation, Amendment, Issue.

**"Darwin Core Class"** [Informative]:"Location" The Information Element in the original terms of the framework, the general sort of information this test operates on.  

**"Information Elements ActedUpon"** [Normative]:"dwc:countryCode" A list of the specific Darwin Core terms that are the focus of the test.

**"Information Elements Consulted"** [Normative]:"dwc:scientificName" A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon.

**"Specification"** [Normative],"EXTERNAL_PREREQUISITES_NOT_MET if the bdq:SourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if the value of dwc:countryCode is found in bdq:sourceAuthority; otherwise NOT_COMPLIANT bdq:sourceAuthority is ""ISO 3166-1-alpha-2"" [https://restcountries.eu/#api-endpoints-list-of-codes, https://www.iso.org/obp/ui/#search]"  The specification for implementors describing the expected behavior of the test.  

**"DateLastUpdated"** [Normative]:"2022-05-02" The most recent date of update of normative elements of the test specifications or an update to a non-normative section that should trigger a review of the behavior of code by implementors.  

**"Parameters"** [Normative]:"bdq:taxonIsMarine" Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain.

**"Dimension"** [Normative]:"Conformance" The [data quality dimension](https://github.com/tdwg/bdq/blob/master/tg2/vocabularies/data_quality_dimensions.csv) for this test.

**"Criterion Label"** [Informative]:"Conformance: standard" A label for the Criterion (TODO: Criterion/CriteronInContext applies to Validations, need to clarify for Dimension/DimensionInContext, Enhancement/EnhancementInContext, Issue/IssueInContext).    

**"Resource Type"** [Normative]:"SingleRecord"  The type of resource on which this test acts, SingleRecord or MultiRecord, the CORE tests include Validations, Measures, and Amendments that operate on SingleRecords and a set of MultiRecord Measures that assess the results of the SingleRecord Validations. 

**"Source Authority"** [Informative]: A reference to an external (non-Darwin Core) authority required for the test. bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}. The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be expected to be passed in as the parameter value.  Other non-empty strings would select other source authorities. The structure of the information in Source Authority ideally has two components. The first component refers to the standard itself, which may include a vocabulary of accepted values. The second component will, wherever possible (if available), refer to an API that will assist implementers of the tests. In some cases, the API component will refer to a 'third party' site where it is hoped will remain in sync with the standard, for example, a GBIF vocabulary API site would ideally be synced with a Darwin Core site.

**"Example"** [Informative]: Example of inputs for a test and the expected output from an implementation of the test given those outputs.  A ’pass’ and a ‘fail’ example are provided for each test.  All examples listed are also present in the the validation data suite.

**"Source"**:"TG2" [Informative]: The origin of the concept of the test.

**"References"** [Informative]:"ISO (n.dat.). ISO 3166 Country Codes (https://www.iso.org/iso-3166-country-codes.html); Wikipedia (2020). ISO 3166-1 alpha-2 (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2); >DataHub (2018). List of all countries with their two digit codes (ISO 3166-1)(https://datahub.io/core/country-list);Chapman, AD and Wieczorek, JR (2020). Georeferencing Best Practices. Copenhagen: GBIF Secretariat (https://doi.org/10.15468/doc-gg7h-s853)"

**"Example Implementations (Mechanisms)"** [Informative]:"FilteredPush/Kurator: geo_ref_qc"  Known Mechanisms with implementations of the test.

**"Link to Specification Source Code"** [Informative]:"https://github.com/FilteredPush/event_date_qc/blob/1abbd3f02eb6c28129764defab78f72156972864/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L489" A link to code that implements the test.

**"Notes"** [Informative]:"Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters."  Additional, non-normative comments that the Task Group believed necessary for an accurate understanding of the test or issues that implementers needed to be aware of.

<!--- NOTE:  VALIDATION-AMENDMENT-VALIDATION--->

Each concept area within CORE has one or a small set of terms that have the ability to carry by themselves the most important information for CORE purposes, and are treated as the targets for data quality improvement (dwc:taxonID, dwc:eventDate, dwc:decimalLatitude, dwc:decimalLongitude, dwc:geodeticDatum, dwc:coordinateUncertaintyInMeters) while other terms support DarwinCore’s mission of permissive sharing of data from different source formats. The by design redundancy of DarwinCore imposes a conflict between the principle of tests standing in isolation with the principle of some terms having priority. This conflict is most evident in the Amendments related to TIME terms, where dwc:day/dwc:month/dwc:year, dwc:startDayOfYear/dwc:endDayOfYear, and dwc:verbatimDate may all carry information relevant to dwc:eventDate, and have the potential to produce conflicting proposals. 

<!--- NOTE: heirarchy of importance of terms e.g. decimalLat/long+datum+uncertanty then country code, then country, --->

Amendments propose changes to the data (either in the form of AMENDED, proposing a change to the data, or FILLED_IN proposing a value for an empty term).

The specification of the tests within the Framework allows the same set of tests to apply to both Data Quality Control (correcting errors) and Data Quality Assurance (filtering out problematic records to limit data to that with quality for meeting a particular need). The design of the Validations and Measures are intended to be agnostic as to whether their use is for Data Quality Control (finding problematic data), or Data Quality Assurance (filtering out NOT_COMPLIANT records).


**5.1.2 Workflows and Sequencing Tests (Informative)**

<!--- Ming: What the tests are agnostic of, repeated in 1.6, 5.2.3 --->
The test descriptions are agnostic to the framework within which the tests are run. The tests are largely agnostic to the extent to which they are run in parallel and the sequence in which particular tests are run. An exception is certain of the amendments, where the order of execution can be important.

<!--- Ming: Execution sequence of the tests , repeated in 1.6, but more detail than 1.6 --->
A good practice for executing the tests is to execute all of the validations and measures in a pre-amendment phase, then to execute all of the amendments in an amendment phase, then to execute all of the validations again on the data with the proposed changes from the amendments applied to the data in a post-amendment phase. Such a sequence of phases allows assertions to be made about the quality of the data as they were initially presented, and how much the quality of the data would be improved if the amendments were accepted. Within pre-amendment and post-amendment phases, the validations and measures are agnostic about the order in which they are run, the extent to which they are run in parallel, or the extent to which they are run on single records or on unique values within a data set. One possible workflow for tests is to aggregate the unique values of applicable Information Elements within a bdqffdq:MultiRecord for each Validation or Measure, then to execute the Validation or Measure on just the unique values, then de-aggregate the results back to each bdqffdq:SingleRecord. This is analogous to implementing tests as SQL queries.

Given a hypothetical Event table with fields including a primary key event_id and an integer field day, implementation of VALIDATION_DAY_STANDARD in SQL that operates on data in the aggregate might look like:

SELECT
    ‘VALIDATION_DAY_STANDARD’ as test name, event_id,
    ‘INTERNAL_PREREQUISITES_NOT_MET’ as Result_status, null as Result_value,
     ‘No value for dwc:day to evaluate’ as Result_comment 
FROM event
    WHERE day is null
UNION 
SELECT
    ‘VALIDATION_DAY_STANDARD’ as test name, 
    event_id,
    ‘RUN_HAS_RESULT’ as Result_status, 
    ‘COMPLIANT’ as Result_value,
    ‘Value of dwc:day [‘|| day ||’] is in the range 1-31’ as Result_comment 
FROM event
    WHERE day >=1 and day <=31
UNION 
SELECT
    ‘VALIDATION_DAY_STANDARD’ as test name, 
    event_id,
    ‘RUN_HAS_RESULT’ as Result_status, 
    ‘NOT COMPLIANT’ as Result_value,
    ‘Value of dwc:day [‘|| day ||’] is outside the range 1-31’ as Result_comment 
FROM event
    WHERE day < 1 or day > 31

**5.1.3. Amendments where order is important (Normative)**

<!--- Ming: How can user know the order of execution for AMENDMENTS? What are primary term and secondary term? --->

When Amendments are executed in a workflow where downstream Amendments operate on data with the changes proposed by upstream Amendments applied, the following sequences SHOULD be followed. Similarly when Amendments are executed in parallel these sequences SHOULD be applied.

Given amendments propose a value to a primary term from secondary terms priority over those which back fill secondary terms from a primary term, AMENDMENT_EVENT_FROM_EVENTDATE SHOULD be run after the following Amendments that propose changes to dwc:eventDate: 

AMENDMENT_EVENTDATE_FROM_VERBATIM, <!---should we add the GUIDs to these? in this document--->
AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY,
AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR,
AMENDMENT_EVENTDATE_STANDARDIZED.

AMENDMENT_SCIENTIFICNAME_FROM_TAXONID SHOULD be run after the Amendment
which proposes changes to dwc:TaxonID: AMENDMENT_TAXONID_FROM_TAXON. 

Where multiple Amendments on secondary terms could propose conflicting changes to a primary term, the sequence of Amendments SHOULD be ordered.

The following Amendments SHOULD be composed to run in an ordered sequence:

| order       | test                                                       |
|-------------|------------------------------------------------------------|
| first       | AMENDMENT_EVENTDATE_FROM_VERBATIM                          | 
| second      | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR    |
| and finally | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY                      |

### 5.2 Implementation (Normative)

#### 5.2.1 Reading a Specification (Normative)

A specification consists of a sequence of RESPONSE, criteria; with a few AMENDMENTS that can propose values for multiple terms having a sequence of options within the criteria.  When reading a Specification, implementors SHOULD read each Response in sequence, evaluating each of the criteria in sequence, and returning the first response that for which the specified criteria are met.  An exception to this is that the placement of EXTERNAL_PREREQUISITES_NOT_MET as the first RESPONSE in the Specification does not imply that the responsiveness of an external resource should be assessed first.  Implementors MAY handle failure of an external resource in any appropriate manner, for example, with exception handling.

Responses in a Specification are expressed in an abbreviated form for readability by implementors.

EXTERNAL_PREREQUISITES_NOT_MET means Response.status=EXTERNAL_PREREQUISITES_NOT_MET, Response.value=null, Response.comment={some non-null description of the failure condition}

INTERNAL_PREREQUISITES_NOT_MET means Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.value=null, Response.comment={some non-null description of the failure condition}.

COMPLIANT means Response.status=RUN_HAS_RESULT, Response.value=COMPLIANT, Response.comment={some non-null description of the failure condition}.

etc.


#### 5.2.3 Compliant Implementation (Normative)

In order to be considered as compliant with this standard, an implementation MUST meet the requirements of this section.   

We view the most important elements of this standard as being the structure that holds explicit descriptions of what a data quality test is intended to do, along with the consistent structure for reporting the results from the execution of a test upon some data.  We expect that implementors will implement sets of these tests that fit their data quality needs, and will also implement other tests.  The CORE tests provide a coherent library of tests that can be applied to the set of defined UseCases, and considerable thought has gone into describing tests that isolate particular data quality issues, and that work together as a conherent suite.   

An implementation SHOULD include all CORE SingleRecord Validations, Amendments, and Measured for each implemented UseCase.  An Implementation SHOULD provide an implementation for at least one UseCase, and MAY provide implementations for more or all of the UseCases.   Implementations MAY include additional tests and additional UseCases.


Results from each test MUST be produced in the form Response.status, Response.result, and Response.comment, with one test producing one Response.   Results MAY include Response.qualifier (See 5.3).  The values of Response.status and Response.result MUST be those specified.   This standard is agnostic concerning data structures and serializations of a Response. The standard is agnostic concerning internationalization and languages of labels applied to human readable presentations of values within a Response.

Where implementors add additional tests as part of a test suite compliant with this standard, they MUST describe those tests using the bdqffdq framework, those tests MUST use the same Response structures, and those tests MUST be related to UseCases (either those defined in the standard or additional use cases).  

<!--- Ming: Execution sequence of the tests, repeated in 1.6, 5.1.2 --->

Implementations MAY run Validations, Measures, and Issues in a pre-Amendment phase, then run Amendments, then re-run the Validations, Measures, and Issues on the data with the proposed changes from the Amendments applied in a post-Amendment phase. The use of pre-amendment, amendment, and post-amendment phases allows for measurement of how much acceptance of the changes proposed by the amendments would improve the quality of the data for core purposes.  

The standard is agnostic as to how data are presented and piped within some framework to and from test implementations.  An implementation framework MAY present SingleRecords to tests and report results, or an implementation MAY find unique values for InformationElements, execute test implementations on those unique values, and then map the results back onto SingleRecord reports, or an implementation MAY operate on data in other ways.

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, Repeated in 1.7 --->

For each core SingleRecord Validation, an implementation intended for Quality Control SHOULD include a corresponding MultiRecord Measure that counts the number of Response.result values that are COMPLIANT.  An implementation MAY provide similar MultiRecord Measures that report aggregated counts of other Response.status and Response.value values.  

For each core SingleRecord Validation, an implementation intended for Quality Assurance SHOULD include a corresponding MultiRecord Measure that returns COMPLETE when all pertenent Response.result values are COMPLIANT (or for some Measures also INTERNAL_PREREQUSISITES_NOT_MET).

Implementations MUST provide implementations of parameterized tests that support the default parameter values. Implementations SHOULD provide for parameterized tests to take parameters, but MAY produce an implementation of a parameterized test that takes no parameters but only uses the default parameter value.

How a test responds when given a parameter value that is not supported by the implementation is not specified. Implementers SHOULD handle this in a manner appropriate for their implementation framework. Unless specified in the Specification, implementations MUST_NOT use Response.status=EXTERNAL_PREREQUISITES_NOT_MET to indicate a non-supported parameter value.

Implementors are free to, and are encouraged to, in addition to framework compliant implementations, produce means of testing data quality in bulk in settings such as SQL queries on relational data stores where construction of Response objects is not feasable, but the logic of a Specification can be framed as a question on a data store.  Such non-framework implementations MUST NOT assert compliance with this standard.


### 5.3 Extension points (Normative)

A response MAY include a Response.qualifier.  This is intended as a place to include structured assertions concerning uncertainty in a response.  This is also intended as a place to include structured assertions about the details of Ammendments (e.g. TRANSPOSED MAY be attached to a Response.qualifier for some Amendments.

<!--- Bit about ActedUpon/Consulted Needs to move, we have added these to the test descriptors and the framework --->

Implementations MAY identify InformationElements as ActedUpon or Consulted. Presentations of data quality results may use ActedUpon and Consulted identification of Information Elements to identify to users which specific values assertions are being made about, and what values are being used to support those assertions. ActedUpon information elements are those for which a Validation is asserting compliance/non-compliance, or an Amendment is proposing a change. Consulted information elements are those which inform such decisions, but are not themselves the subject of the decision. For example, in AMENDMENT_EVENTDATE_FROM_VERBATIM, the InformationElement dwc:eventDate is ActedUpon, while the InformationElement dwc:verbatimEventDate is Consulted. We do not  identify Information Elements as ActedUpon or Consulted here, but implementers may wish to do so to more clearly represent to consumers of data quality reports (particularly data quality reports in the form of spreadsheets), which terms are particular tests are making assertions about.

Tests MAY specify that information elements are ActedUpon or Consulted. We do not do so here, but ActedUpon and Consulted properties of an Information Element are an extension point that may be included when specifying the Information Elements pertinent to a test

MultiRecord Measues that return counts where the input InformationElement is Response values from tests on SingleRecords MUST report only a single count as the Response.value, but can provide a Response.qualifier containing structured data describing additional information such as the total number of SingleRecords evaluated (to calculate percents), the number of each value of Response.status encountered, and the number of each Response.value encountered.  Measures under the framework are only allowed to return COMPLETE/NOT_COMPLETE, or a single number, if it is desirable for any Measure to return more than a single number, Response.qualifier is the extension point to use for this. 

### 5.4 Core Test Specifications (Normative)

These are the specifications for a set of Validations, Amendments, and Measures, each of which applies to a SingleRecord under one or more UseCases. 

[Generate from https://github.com/tdwg/bdq/blob/master/tg2/core/TG2_tests.csv]

Included Document: 

[CORE SingleRecord Tests](https://github.com/tdwg/bdq/blob/master/tg2/core/generation/docs/core_tests.md)


### 5.5 Core MultiRecord Measure Specifications (Normative)

These are the specifications for a set of Measures each of which applies to a MultiRecord under one or more UseCases.  The inputs, that is the InformationElements, for these Measures are the outputs of SingleRecord validations.  One subset of these measures simply counts the number of Response.result=COMPLIANT for a given Validation in a pass through each of the SingleRecords in a MultiRecord.  The proportion of records that are COMPLIANT is easily calculated and displayed from the measured value over the total number of SingleRecords in the MultiRecord.  For QualityControl, these numbers identify where work is needed to make more of a data set fit for use for a given UseCase.  The other subset of these measures are intended for QualityAssurance.  These QA measures return a Response.result of COMPLETE if all of a given Validation on SingleRecords in a MultiRecord are COMPLIANT.  A MultiRecord is fit for use for a given UseCase if each of the MultiRecord QA Measures on that MultiRecord returns COMPLETE.  If this is not the case, SingleRecords where the Validations are other than COMPLIANT are filtered out until all of the MultiRecord QA measures return COMPLETE.  The MultiRecord QA measures are the formal means the Fitness for Use Framework provides for ensuring that a data set is fit for use for a given UseCase.  

Some Validations return Response.status=INTERNAL_PREREQUISITES_NOT_MET when one or more of the input InformationElements contain empty values.  For some UseCases, empty values in some fields make the data not fit for use (these are usually tested directly for with VALIDATION...NOTEMPTY tests), however, some Validations operate on sparse data or other cases where the data is fit for use even without values, but when values are present, they must comply with some restriction.  For example, dwc:minimumDepth and dwc:maximumDepth are not expected to be populated for terrestrial data, but are expected to be within range when values are supplied (for freshwater and marine data).  A subset of the MultiRecord QA Measures accomodate such cases by returning Response.result=COMPLETE for validations that are either Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET.  Thus they can measure that all of the SingleRecords in a MultiRecord either have, for example, no value in dwc:minimumDepth or have an in-range value for dwc:minimumDepth.   

It is possible, but less flexible, to frame Validations to return Result.response=COMPLIANT for either empty values or non-empty values that satisfy other validation criteria.  Concerns are better separated, and individual tests are better composed to fit particular user needs, by having the Validations treat empty data as INTERNAL_PREREQUISITES_NOT_MET, and then framing MultiRecord QA Measures as appropriate for a given UseCase.

MultiRecord Measures that return counts can be run before an amendment step in a data processing pipeline, and run again after applying all of the proposed changes to the data from the Amendments to the data set.  A comparison of these pre-amendment and post-amendment phases will identify how much accepting all of the proposed changes from the amendments will improve the quality of the data.  

[Generate from https://github.com/tdwg/bdq/blob/master/tg2/core/TG2_multirecord_measure_tests.csv]

Included Document: 

[CORE MultiRecord Measure Tests](https://github.com/tdwg/bdq/blob/master/tg2/core/generation/docs/core_multirecord_measure_tests.md)


## 6. Validating test implementations (Lee)

Implementors of tests SHOULD validate the behaviour of the internals of their test implementations with unit tests, and MUST validate that each test implementation is capable of taking relevant input from a set of standard test validation data, and returning the expected responses.

### 6.1 Introduction

Accompanying the Core test descriptors is a set of test validation data.  This test validation data is intended for implementors to use to evaluate whether or not their test implementations produced the expected Response values for a set of cases for each test.  Each test specification could be graphed as a flow chart with several paths, the test validation data are intended to cover each node and each path within each test specification with at least a single case.  These are not exhaustive unit tests covering large numbers of edge cases, but rather a minimal set of tests for expected behaviour.  

The test validation data are organized as two flat CSV files.  Each row in each file is intended for a single validation of a single test.  The file has columns identifying the validation case, the test that the row is intended to validate, the expected Response.status, Response.value, an example Response.comment, parameter values, if any, and a set of Darwin Core terms (most of which are empty for a given test).   

The test validation records are all fragmentary flat Darwin Core Occurrence records.  Each row contains values for only those Darwin Core terms that are relevant input to the particular validation.   The validation records are all fragmentary, consisting of a mixture of real and artificial data with most of the records being synthetic.  The validation data are a set of 1191 records, with about 10 validation cases for each test.  The set of rows for a particular test are designed to validate that an implementation of that particular test performs as expected against the specifications.   This data set is referred to as the 'Test Validation Data'.   The set of about 10 validation records for each test are designed to exercise all of the decision pathways in the specification of the test.  

This is a minimalist suite of test data. Additional test records can be readily generated or adapted from real data using the following template based on the specifications below. In consideration of the community, the DataID values MUST uniquely identify a validation case for each additional test data record and the resulting data added to the GitHub repository.

### 6.2 Considerations Concerning Input Data Values for AMENDMENTS

One of the early conclusions to this project was the need for controlled vocabularies and an early spin-off of Data Qality Task Group 4 on Vocabularies (https://github.com/tdwg/bdq/tree/master/tg4). Testing the 'quality' or 'fitness for use' of Darwin Core encoded data is made more difficult due to the lack of a comprehensive suite of controlled vocabularies.

Testing Darwin Core values against a known Source Authority using a VALIDATION type test is straight forward: A test is either COMPLIANT or NOT COMPLIANT. This standard includes tests of type AMENDMENT and the mapping of input Darwin Core values to known Vocabulary values is poorly developed. If a VALIDATION returns COMPLIANT, no AMENDMENT is necessary. For example, if the input value to a test is say dwc:sex="Female", then no AMENDMENT is required. If however, the input value is dwc:sex:f., can this be interpreted as "Female"? Probably. What about dwc:sex="M"? This could be "Male" or "Mixed" according to https://api.gbif.org/v1/vocabularies/Sex/concepts. <!--- Ming: I asked GBIF about this specific example and they said that "M" will be matched to Male, but I am not sure how the API works exactly --->

A key phrase within this standard that particularly relates to many of the Expected Responses of tests is " dwc:term can be unambiguously interpreted as ...". In the case above for dwc:sex="M", the determination is that it is ambiguous. In this case, no AMENDMENT can be made.

When carrying out Amendments where numeric vales are concerned (e.g. feet to meters, etc.) the principle of reversability is paramount, and thus rounding up or down or using approximations should be avoided and only exact values used.

We see an urgent need for a comprehensive, internationally agreed list of Darwin Core (https://dwc.tdwg.org/) term values that are mapped to standard values. GBIF has implemented some unique values, for example https://api.gbif.org/v1/vocabularies/Sex/concepts/Female/hiddenLabels, but such lists are not comprehensive. While there has been a survey of Darwin Core 'distinct' values for GBIF, ALA, iDigBio and VertNet, these are both dated, and where possible, have not been mapped to standard values, if they exist.

In this standard, we have taken an expedient approach in relation to making AMENDMENTs. We have used code in our tests to try and parse out likely, unambiguous matches. This is far from an ideal solution, but it does provide the potential of our AMENDMENTs to 'value add' to Darwin Core data records.

### 6.3 Structure of the Validation Data 

The validation data are intended as input into a testing system that can implementations of validation tests independently, presenting them with a validation case for input, and assessing whether the test Response conforms to the expected values in the validation data.  It could be processed as input for unit tests.   It could be used as the basis for presenting synthetic records to a larger test execution system, but is designed to be used at a level where individual tests are being assessed.  This may fit into integration tests of a larger system.  The structure of the validation data attempts to be at a level of abstraction somewhat above the method signature specificity needed in unit tests, but still at a level that is examining individual test implementations, below the level of testing inputs and outputs of a larger data processing system that could take complete Darwin Core records as input and return rich data quality reports as output (to avoid forcing particular formats on data quality reports as a whole).  

The following column header for the data are used for the validation data files.

* Line Number: An integer for maintaining the sort order of the file.
* dataID: A unique identifier (within the validation data) of the validation data record, e.g., "123"
* LineForTest: An integer for maintaining the sort order of the validation case with in the set of validation cases for a particular test,
* GitHubIssueNo: The GitHub issue where rationale management of the test under validation is maintained, can be use to form a link to the discussion history for the development of the relevant test, e.g., 20 can be found at https://github.com/tdwg/bdq/issues/20
* GUID: the machine readable identifier for the test under validation, e.g. 69b2efdc-6269-45a4-aecb-4cb99c2ae134
* Label: The human-readable name of the test, e.g., "VALIDATION	COUNTRY_FOUND"
* Response.status: The status on applying the test to the test data record. For VALIDATIONS, one of the terms "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET" or "RUN_HAS_RESULT". For AMENDMENTS, one of the terms "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET", "FILLED_IN", "AMENDED" or "NOT_AMENDED". For ISSUE, one of the terms "INTERNAL_PREREQUISITES_NOT_MET" or "RUN_HAS_RESULT". For MEASURES, either "RUN_HAS_RESULT" or "INTERNAL_PREREQUISITES_NOT_MET".
* Response.result: The result of running the test on the test data record. For VALIDATIONS and AMENDMENTS, "NULL" where the Response.status is either "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET". For VALIDATIONS, either "COMPLIANT" or "NOT_COMPLIANT" where Response.status is "RUN_HAS_RESULT".  For AMENDMENTS where Response.status is either "FILLED_IN" or "AMENDED, the Response.result is a json structure containing a key:value list of Darwin Core terms and values for changes proposed by the AMENDMENT. For MEASURES, a resulting value or "NOT_REPORTED".
* Response.comment: An example human-readable statement identifying the reason for the test result given the input data, implementations are not expected to produce this exact value, it is given as an example.
* IssuesWithThisRow: Temporary working column for recording problems while developing validation data, to be removed.
* bdq:annotation placeholder for an annotation when testing for their presence.
* bdq:sourceAuthority input parameter for some parameterized tests.
* dwc: (77 columns)  All of the Darwin Core terms that are in scope for Core.  In each row, only those identified in the Information Elements of the relevant test and pertinent to the test case at hand contain values.

NOTE: We have implemented examples of EXTERNAL_PREREQUISITES_NOT_MET using the Input.Data structure of

bdq:sourceAuthority="https://invalid/invalidservice", dwc:inputDataValue1="", dwc:inputDataValue 2... or as an example

bdq:taxonomyIsMarine="https://invalid/invalidservice", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:scientificName=""

See Section on Implementation

### 6.4 Examples of the data for validating tests (Informative)

The validation files contain one column for each of 77 Darwin Core terms that are referenced as an Information Element somewhere in Core, but only terms relevant to the particular validation case for the row are populated, therefore the validation files are sparse.  They contain fragments of Flat Darwin Core records. 

The header line for each of the validation files:  

"LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Response.status","Response.result","Response.comment","IssuesWithThisRow","bdq:annotation","bdq:sourceAuthority","dc:type","dcterms:license","dwc:acceptedNameUsageID","dwc:basisOfRecord","dwc:class","dwc:continent","dwc:coordinateUncertaintyInMeters","dwc:country","dwc:countryCode","dwc:county","dwc:dataGeneralizations","dwc:dateIdentified","dwc:day","dwc:decimalLatitude","dwc:decimalLongitude","dwc:endDayOfYear","dwc:establishmentMeans","dwc:eventDate","dwc:family","dwc:genus","dwc:geodeticDatum","dwc:higherClassification","dwc:higherGeography","dwc:higherGeographyID","dwc:infraspecificEpithet","dwc:island","dwc:islandGroup","dwc:kingdom","dwc:locality","dwc:locationID","dwc:maximumDepthInMeters","dwc:maximumElevationInMeters","dwc:minimumDepthInMeters","dwc:minimumElevationInMeters","dwc:month","dwc:municipality","dwc:occurrenceID","dwc:occurrenceStatus","dwc:order","dwc:originalNameUsageID","dwc:parentNameUsageID","dwc:phylum","dwc:scientificName","dwc:scientificNameAuthorship","dwc:scientificNameID","dwc:specificEpithet","dwc:startDayOfYear","dwc:stateProvince","dwc:subgenus","dwc:taxon","dwc:taxonConceptID","dwc:taxonID","dwc:taxonRank","dwc:verbatimCoordinateSystem","dwc:verbatimCoordinates","dwc:verbatimDepth","dwc:verbatimElevation","dwc:verbatimEventDate","dwc:verbatimLatitude","dwc:verbatimLocality","dwc:verbatimLongitude","dwc:verbatimSRS","dwc:vernacularName","dwc:waterBody","dwc:year","dwc:subfamily","dwc:superfamily","dwc:tribe","dwc:subtribe","dwc:genericName","dwc:infragenericEpithet","dwc:cultivarEpithet","dwc:individualCount","dwc:organismQuantity","dwc:footprintWKT","dwc:coordinatePrecision"

The data are sparse, as most dwc: term columns do not contain a value for each individual case.

A validation test case evaluating empty, where no dwc: term columns contain a value (dataID=1):  

"2","1","1","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","INTERNAL_PREREQUISITES_NOT_MET","","dwc:countryCode is EMPTY","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation test case for a validation where the input data result in a Response.value of NOT_COMPLIANT (dataID=7)

"7","7","7","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","NOT_COMPLIANT","dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value ","","","","","","","","","","","","Austria","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation test case for a validation where the input data result in a Response.value of COMPLIANT (dataID=8)

"8","8","8","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","COMPLIANT","dwc countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value","","","","","","","","","","","","US","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

### 6.5 Where to get the validation data (Informative)

The validation data is in two files, one containing normal data values, the other containing validation cases using non-printing characters.

Validation file containing data values that would be expected to be encountered in the wild: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data.csv

Validation data file containing non-printing characters for testing implementation of EMPTY: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data_nonprintingchars.csv

This file is a csv file with the same set of columns as the above, but with rows that contain input values for selected Darwin Core terms consisting of either the 0x00 null character (e.g. dwc:scientificName="0x00"), or a pair of ASCII control characters (shift out 0x0E and shift in 0x0F, e.g. dwc:day="0x0E0x0F"). This file is intended to validate that implementations of tests are consistently evaluating inputs as EMPTY as expected by the definition of EMPTY.  

The non-printing characters file should only be edited with a tool that will maintain the non-printing characters.  

Both files have a header line identifying the specifications as defined in Section 6.2.

The expectation for the response that an implementation should produce when executed against the row: "Response.status","Response.result","Response.comment", where an implementation is expected to produce the exact Response.status, the exact Response.result (ignoring order of any key-value pairs for an amendment response), and Response.comment is an example of what a comment, in English, might look like.  

Parameter values are specified in a bdq:sourceAuthority column, when more than one sourceAuthority is involved, then these are given separate names.

Darwin Core input columns are specified as "dc:type","dcterms:license","dwc:acceptedNameUsageID",...

### 6.6 Implementation (Normative)

Implementations SHOULD provide support for each parameter value specified in the example data. 

REQUIRED: For each test in an implementation, that test MUST produce the same results as are specified in a row of the validation data for that test, except when a bdq:sourceAuthority parameter specifies a web service other than the default sourceAuthority specified for that test.

REQUIRED: Implementations MUST produce structured Response values with a Response.status, Response.value, and Response.comment.  

In order to be considered as compliant with this standard, an implementation of the Core tests MUST fulfill all of the REQUIRED elements of this section.

Human readable Data Quality Reports for Quality Control MAY take any appropriate form, they MAY aggregate Response values and comments, they MAY present results organized by test, or by data record, or by frequency of problem, or any other form suitable for presentation.  Data Quality Reports for Quality Control SHOULD allow users to access individual Response.status Response.value Response.comment results.  

Response.comment values SHOULD be internationalized as appropriate for the the consumers of data quality reports.  

Response.status and Response.value constants SHOULD be given internationalized labels as appropriate for the the consumers of data quality reports.  

### 6.7 Identifying example data (Normative) (Paul)

Data sets consisting of partly or wholly synthetic data, including data sets into which errors have been deliberately introduced may be used to test, validate, and demonstrate the operation of implementations of data quality tests.  It is important that such synthetic and modified data not become conflated with actual biodiversity data in analyses.  The following processes SHOULD be followed to identify original, modified, and synthetic example biodiversity data.

#### 6.7.1 Data Fragments and Occurrence Data Sets

Inputs to unit tests and testing frameworks for individual test implementations, such as the test validation data in section 6.3 are likely to be organized as fragments of Occurrence data not easily mistaken for actual occurrence data.  A record forming a fragment of an Occurrence record for validating the behaviour of the implementation of a particular test SHOULD only contain the set of terms that form the Information Element for a particular test, along with test parameters, expected outputs, and related metadata, and SHOULD_NOT contain values in other Darwin Core terms not relevant to the test under consideration, except data fragments MAY be marked as synthetic by adding the term values described in 6.6.3 and 6.6.4  Testing frameworks MAY take as input more complete Darwin Core records, and when these are partly or wholly synthetic, they MUST be identified as synthetic, and MUST be treated as synthetic by consumers of Occurrence data.

#### 6.7.2 Real data used as examples.

Use the values in the original source, without modification except:  If no dwc:datasetID is provided, a value for dwc:datasetID MAY be added, this SHOULD be the doi of the source data set in which the example record was found.   

#### 6.7.3  Real data with synthetic modifications used as examples:

A. The data set MUST set values for record level terms to unambiguously mark the record as modified.

The data set SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode =  "Modified Example"
dwc:collectionID = "urn:uuid:1887c794-7291-4005-8eee-1afbe9d7814e"

B. Each modified record MUST provide a new GUID for the modified record distinct from the original GUID.
 			
dwc:occurrenceID = urn:uuid: + a random type 4 UUID.

C. Each Occurrence record SHOULD include resource relationship terms in the modified example pointing at the original source:

dwc:relatedResourceID = the ID (e.g. occurrenceID) for the original source record.

dwc:relationshipOfResource = “source for modified example record”

dwc:relationshipRemarks:  Structured data specifying the original values for institutionID, institutionCode, collectionCode, collectionID, and occurrenceID, the doi for the data set the original example record was found in, a list of the modifications made to the original record, and potentially, a list of standard tests and expected test results that this example illustrates. 

#### 6.7.4 Wholly Synthetic Data MAY be used.  This is not recommended for entire Occurrence records or entire Occurrence data sets.

A. The data set MUST set values for record level terms to unambiguously mark the record as synthetic.

The data set SHOULD use the following values, and consumers of biodiversity data MUST treat these values as not representing actual occurrence data. 

dwc:institutionCode = "example.org"
dwc:institutionID = “http://example.org/"
dwc:collectionCode =  "Synthetic Example"
dwc:collectionID = "urn:uuid:0b1b9546-64aa-446b-bd9c-cbb0eacf4332"

B.  Each modified record MUST provide a GUID for the synthetic record.

dwc:occurrenceID = urn:uuid: + a random type 4 UUID

### 6.8 Updating test data due to changes in specifications or terms

If any part of the logic of a test changes, parallel changes must be made to the test data for that test. For example, a change in a tests Expected Response will very likely to result in the need to amend at least one record within the associated test data. For example the Expected Response of the test AMENDMENT_EVENT_FROM_EVENTDATE to limit amendments to a single year resulted in an amendment to the Response.status of the data record DataID #320 from "FILLED_IN" to "NOT_AMENDED".

A change to the test data may also precipitate the need to change one or both of the Examples within the test specification. As all examples of tests are based on the associated tests records in the test data, any such need for changes should be explicit.

Similarly, changes to the test specification 'Information Elements ActedUpon' and 'Information Elements Consulted' will may require changes to Input.data, Output.data, Response.result and Response.comment.

Therefore any changes to test specifications must trigger the need to check the associated test data and examples.

## 7. Implications for the Darwin Core Standard (John)

Early recognition that estimating 'fitness for use'/'quality was made difficult because of the lack of vocabularies...TG4.

Definitions, uses in the wild, and best practices for Taxon class ..ID terms.

[ Mention of issues arising such as use of dwc:country and dwc:countryCode and "High Seas"]

How to identify the High Seas.

## 8. Acknowledgements
Antonio Mauro Saraiva, Allan Koch Veiga, Tim Robertson, Yi-Min Gan, Ian Engelbrecht, GBIF, IDigBio, ALA, CRIA, TDWG...

## 9. Acronyms

| **Acronym** | **Explanation**                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------|
| ALA         | Atlas of Living Australia                                                                                      | 
| BDQ         | TDWG Biodiversity Data Quality Interest Group                                                                  |
| BISON       | Biodiversity Information Serving Our Nation                                                                    |
| CRIA        | Centro de Referência em Informação Ambiental                                                                   |
| EPSG        | European Petroleum Survey Group                                                                                |
| GBIF        | Global Biodiversity Information Facility                                                                      |
| iDigBio     | Integrated Digitized BioCollections                                                                            |
| IRI         | Internationalized Resource Identifier                                                                          |
| ISO         | International Standards Organization                                                                           |
| TDWG        | Biodiversity Information Standards                                                                             |
| TG1         | Biodiversity Data Quality Interest Group Task Group 1: Framework on Data Quality                               |
| TG2         | Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions                       |
| TG3         | Biodiversity Data Quality Interest Group Task Group 3: Data Quality Use Cases                                  |
| TG4         | Biodiversity Data Quality Interest Group Task Group 4: Best Practices for Development of Vocabularies of Value |


## 10. References

* Belbin L, Daly J, Hirsch T, Hobern D, Salle JL (2013) A specialist’s audit of aggregated occurrence records: An ‘aggregator’s’ perspective. ZooKeys 305: 67–76. doi: 10.3897/zookeys.305.5438
* Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889
* Rees ER, Nicholls M (2020). Suppl. material 2: Data Quality Use Case Study Result. https://biss.pensoft.net/article/download/suppl/5255738/.
* [RFC-2119] http://tools.ietf.org/html/rfc2119 Key words for use in RFCs to Indicate Requirement Levels. 1997. The Internet Engineering Task Force.
Sanderson et al. (2107) see Section 1.5
* Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731
* Wieczorek J, Bloom D, Guralnick R, Blum S, Döring M, Giovanni R, Robertson T, Vieglais D (2012) Darwin Core: An Evolving Community-Developed Biodiversity Data Standard. PLoS ONE 7(1): e29715. https://doi.org/10.1371/journal.pone.0029715

## 11. Supplement: Rationale Management Documentation

TODO: Add preferred labels for tests using the pattern "Validation Day In Range" and "Validation ScientificNameID Complete".

TODO: Create issue templates for new test and test change request. Include Preferred Label in that template.

The development of each test, with documentation of why particular decisions were made with regard to that test, has been documented in issues in the tdwg/bdq github repository. Each issue has table in markdown format in its Issue.  The terminology in this markdown table differs slightly from the Framework, so to support understanding of the rationale management the non-standard terminology used there is documented below:

**Title**: A standardised, human readable name of the test-assertion based roughly on the template OUTPUTTYPE_TERMS_RESPONSE. There are 15 tests that only loosely conform to this template due to the difficulty of rendering them otherwise, for example "VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION". <!---Note that there are 15 tests that don't strictly follow this - e.g. #132, #108, #93, #88, #86, #73, #71, #68, #62, #57, #56, #52, #50, #32, #24 - Should we mention the exception types here?--->. These names were considered helpful for human-human communication and to assist with code implementation, maintenance and searches. Example: VALIDATION_BASISOFRECORD_STANDARD.

**GUID**: A globally unique identifier which allows software to uniquely identify each test (and in combination with parameter values, allows for specification of the expectations for the behaviour of a test implementation). Example: 42408a00-bf71-4892-a399-4325e2bc1fb8. 
 
**Description**: An English language brief description. Example: Does the value of dwc:basisOfRecord occur in bdq:sourceAuthority? 

**Output Type**: Tests have been classified into four Fitness for Use Framework classes; VALIDATION (validates values in one or more Darwin Core terms),  AMENDMENT (an improvement that will result in a change or addition to at least one Darwin Core term); and MEASURE (returns a numeric value, for the tests described here; all values are in the form of the number of tests that conform to a criterion). Three tests are typed as ISSUE (flag a potential problem). Example: POTENTIAL_ISSUE.

**Darwin Core Class**: The Darwin Core class that contains the Information Elements. Example: dwc:Taxon.

**Information Elements**: The Darwin Core terms that the test takes as input. Example: dwc:basisOfRecord.

**Expected Response**: A concise description of the logic of the test to clarify implementation. The Expected Response takes the form (for a VALIDATION) of: EXTERNAL_PREREQUISITES_NOT_MET if <condition>; INTERNAL_PREREQUESITES_NOT_MET if <condition>; COMPLIANT if <condition>; otherwise NOT_COMPLIANT. Example: EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is EMPTY; AMENDED the value of dwc:basisOfRecord if it could be unambiguously interpreted as a value in bdq:sourceAuthority; otherwise NOT_AMENDED.

**Data Quality Dimension**: A test will focus on one of the following scenarios based on the Data Quality Framework: "Completeness" (the extent to which data elements are present and sufficient); "Conformance" (conforms to a format, syntax, type, range, standard or to the own nature of the information element); "Consistency" (agreement among related information elements in the data); "Likeliness" (low probability that values are real); "Resolution" (is sufficient detail present in the value/s - a measure the granularity of the data).

**Warning Type**: The nature of the flag associated with the result of the test. Possible values are "Ambiguous", "Amended", "Incomplete", "Inconsistent", "Invalid", "Notification", "Report" and "Unlikely.

**Parameter(s)**: Parameters that modify the behaviour of the test, along with default values or links to source authorities. A parameter value exists only where there are a number of alternate options. For example, "bdq:sourceAuthority default = "GBIF Backbone Taxonomy"" is parameterised as it allows for regional taxonomic authorities whereas "bdq:sourceAuthority is "EPSG:" [https://epsg.io]"" is not parameterised as there is a single source authority. Example: bdq:defaultGeodeticDatum.	

**Source Authority**: A reference to the authority required by the test and a default value. Example: bdq:sourceAuthority default = {Darwin Core} {Basis of record [https://dwc.tdwg.org/terms/#dwc:basisOfRecord]}.   When a test uses more than one sourceAuthority at the same time, these are given separate names, for example,  bdq:taxonIsMarine,bdq:geospatialLand are the two sourceAuthority Parameters for VALIDATION_COORDINATES_TERRESTRIALMARINE.

**Specification Last Updated**: Date of last change to a Normative part of the test, for example to the wording of an Expected Response. Example 2023-06-23.

**Examples**: A ’pass’ and a ‘fail’ example of test data. All examples have been generated from the test data suite. Example: [dwc:basisOfRecord="Taxon": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:basisOfRecord matches a standard label of one of the Darwin Core classes"]
[dwc:basisOfRecord="Specimen": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:basisOfRecord does not exactly match a standard label of one of the Darwin Core classes"].

**Source**: The origin of the concept of the test. Example: The Atlas of Living Australia.

**References**: One or more publications that relate directly to the test. Example: GBIF Secretariat (2021). GBIF Backbone Taxonomy https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c).

**Example Implementations (Mechanisms)**: A link to one or more agencies that have an implementation of the test. Example: https://github.com/FilteredPush/event_date_qc.

**Link to Specification Source Code**: A link to code that implements the test. Example: https://github.com/FilteredPush/ event_date_qc/blob/5f2e7b30f8a8076977b2a609e0318068db80599a/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L169.

**Notes**: Additional comments that the Task Group believed necessary for an accurate understanding of the test or issues that implementers needed to be aware of. Example: For TAXONID_FROM_TAXON, “This is the taxonID inferred from the Darwin Core Taxon class, not from any other sense of Taxon. Return a result with no value and a Result.status of NOT_AMENDED with a Response.comment of ambiguous if the information provided does not resolve to a unique result (e.g. if homonyms exist and there is insufficient information in the provided data, for example using the lowest ranking taxa in conjunction with dwc:dwc:scientificNameAuthorship, to resolve them).  When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:taxonID.”.

## 1.5 Definition of CORE

'CORE' in the context of this standard implies that the tests are informative, simple to implement, are mandatory for enhancements/amendments, have ‘power’ in that they will not likely result in 0% or 100% of all records failing or passing, are widely applicable across sub-disciplines within the biodiversity domain, may elevate the significance of an issue (e.g., no value for dcterms:license) or they may be 'aspirational' in the sense of encouraging priority developments in the biodiversity informatics domain (e.g., testing for any annotations against a record). The scope of CORE was also developed from the user needs analysis of BDQ Task Group 3, (Data Quality Use Cases: Rees & Nicholls 2020). The CORE tests largely cover data quality with regards to what organism has occurred where, at what times, and a subset of Darwin Core terms that we consider to be critical metadata about occurrence records.

A number of tests were framed, but considered out of scope for CORE data quality needs ('Supplementary' GitHub tag). Implementers are free to implement a subset of the CORE tests or add additional tests when there is a particular data quality needs within their domain. For example, the testing for a value of sub-genus against a taxonomic name authority or testing for a valid depth against maximum depth around the location of an observation. Over the period of this project, many tests were removed from CORE on the basis that they could not be currently implemented in a manner that would result in predictable results. For example, the test VALIDATION_GEOGRAPHY_CONSISTENT was rejected late in the project because of the complexities in matching terms in the geographic names hierarchy, which is less standardized than the taxonomic names hierarchy.

---

## User guide

#### **2.2.3.1 Event and Calendars**

Different calendars have been used at different times in different places, and the transcription of an
original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date, and metadata may or not be present to even identify such records.

Countries and researchers have changed from the Julian calendar to the Gregorian calendar at different times. For example, Russia adopted the Gregorian Calendar on 1918-02-14, the British Empire in 1752-09-14, different regions in France between 1582 and 1760, with France also adopting the French Republican Calendar 1793-1805. The difference between the Gregorian and Julian calendar has typically been around 10 days. But, the day that is considered the first day of the year has also changed at different times in different countries, meaning that the difference can be as great as 1 year and 10 days. Given the complexity, and ongoing nature of transitions between calendars, we do not advocate using VALIDATION_EVENTDATE_INRANGE for quality assurance by selecting a transition date and using it as a threshold.

[John’s statement on calendars as a placeholder (https://github.com/tdwg/bdq/issues/76#issuecomment-1591985055): “I don't think we are in any position to posit a date after which the Gregorian calendar assumption is safe. It is still not safe today, it's just that its use for civil purposes has ever fewer exceptions as time goes on (so far). Making a statement about a particular date (other than the date of its origin) for a date of special mention necessarily has discriminatory implications. We do NOT want that.

In this particular issue, and perhaps in all others where this has come up, I do not see that the uncertainty associated with the date actually has anything to do with what we are testing. This test can't assess if a date is actually within a Gregorian date interval, except in special cases where the Julian and Gregorian calendars coincide, and even that is ignoring all other possible calendars. Instead, it is able to test that a date following the ISO 8601-1 date specification is within a range specified in that context. We can't effectively do anything else because Darwin Core doesn't even provide for stating the original calendar used - it's forcing people to use the Gregorian calendar without describing the responsibility for doing so and the consequences of not doing so. I think the place for awareness of the implications of dates with unknown calendars is in the Darwin Core date terms.]

#### 5.2.2 Example (Informative)

Given the specification: 

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:SourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if the value of dwc:countryCode is found in bdq:sourceAuthority; otherwise NOT_COMPLIANT

Pseudocode for an implementation follows the sequence of RESPONSE,critera; of the specification, with external prerequisites being able to be thrown from anywhere within the logic, but handled within the construct that builds a Result object.

    Function validationCountrycodeNotempty(countryCode) returns Result {
      String sourceAuthority = "ISO 3166-1-alpha-2"
      Result result = new Result()
      try { 
          if (isEmpty(countryCode) { 
              result.setStatus(INTERNAL_PREREQUISTS_NOT_MET) 
              result.setComment("provided countryCode is empty."
          } else {
              result.setStatus(RUN_HAS_RESULT) 
              if (isFoundCountryCode(countryCode,sourceAuthority)) { 
                 result.setValue(COMPLIANT)
                 result.setComment("provided countryCode ["+countryCode+"] is a known "+sourceAuthority+" countryCode ")
              } else { 
                 result.setValue(NOT_COMPLIANT)
                 result.setComment("provided countryCode ["+countryCode+"] is not a known "+sourceAuthority+" countryCode ")
              }
          } 
      } catch NetworkException {
          result.setStatus(EXTERNAL_PREREQUISITES_NOT_MET) 
          result.setComment("Temporary failure looking up countryCode, try later")
      }
      return result;
    }

    Function isfoundCountryCode(countryCode,sourceAuthority) returns boolean throws NetworkException {...}


#### 5.2.4 Guidelines for Implementers (Informative)

**TODO: Mention of the need for local caching of web-site based source authorities.**

Implementors should locally cache the results of calls to remote web services, particularly if they operate on a sequence of SingleRecords instead of operating on distinct values of InformationElements.  Data sets typically contain many repeated values, and remote web services should not be subject to repeated requests asking the same question over and over. 

**TODO: Note that implementors do not need to implement web service calls to source authorities that are highly stable (e.g. DCMI type vocabulary #41).

Some source authorities are highly stable small vocabularies.  Implementors may choose to query a local copy of such a vocabulary, even if a remote service is specified in a bdq:sourceAuthority for a test.  Implementors should monitor for changes to that vocabulary. 

**TODO: The value supplied for the parameter for the test is not an attribute of the data, it is an attribute of the Mechanism (of the system assessing the data quality). If we had included assertions about the validity values of parameters, they should only return external prerequisites not met, as they are assertions about externalities to the data and will change if the same data are run on the same test with a different configuration.**

**If time zone is not included as a component of date and time, the date and time information is expected to be consistent throughout the event terms**

**Placeholder for TIME issue**

See: https://xkcd.com/2867/ and  https://www.xkcd.com/1883/

This standard avoids analysis of two time and date issues, time zones, and geographic and temporal variation in the change from Julian to Gregorian calendars.  

Time is treated as out of scope for CORE Use Cases.  This means that some cases where time zone data is important, dates within a MultiRecord from multiple sources may have multiple plus or minus one day errors introduced.    

The event_date_qc implementation of AMENDMENT_EVENT_FROM_EVENTDATE contains this commented out block of code, pertinent to time zone issues.   It would popluated eventTime from eventDate, converting a local time in eventDate to UTC, where other blocks in the Amendment should but may not have taken account of a local time zone in populating dwc:day/dwc:month/dwc:year/dwc:startDayOfYear/dwc:endDayOfYear (dwc:day/dwc:month/dwc:year/dwc:startDayOfYear/dwc:endDayOfYear/dec:eventTime should all be consistent, but there aren't unit tests in place to confirm this).

// Time could also be populated, but it isn't in scope for this issue.
// Here is a minimal implementation,
// which illustrates some issues in implementation (using zulu time or not, dealing with time in ranges...)
if (DateUtils.isEmpty(eventTime)) {
        if (DateUtils.containsTime(eventDate)) {
                String newTime = DateUtils.extractZuluTime(eventDate);
                result.addResult("dwc:eventTime", newTime );
                result.setResultState(ResultState.FILLED_IN);
            result.addComment("Added eventTime ["+ newTime +"] from eventDate ["+eventDate+"].");
        }
}

In general, assessing whether a date in biodiversity data was Julian or Gregorian is treated here as an intractable problem, and the problem of correctly determining the gregorian value for dwc:eventDates is left in the hands of data providers who may have additional knowledge of collectors and their practices to be able to assess how to interpret verbatim date values found in their historical records.  For consumers, this means that historical dates, even into recent times, may have systematic errors in subsets of the data where the date was julian but has been treated as gregorian.  This can, in some cases, introduce errors on the scale of one year differences between reported and correct eventDate value.     





<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">

<head>

<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 15">
<link id=Main-File rel=Main-File
href="file:///C:/Users/LEEBEL~1/AppData/Local/Temp/msohtmlclip1/01/clip.htm">
<link rel=File-List
href="file:///C:/Users/LEEBEL~1/AppData/Local/Temp/msohtmlclip1/01/clip_filelist.xml">
<!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
x\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]-->
<style>
<!--table
	{mso-displayed-decimal-separator:"\.";
	mso-displayed-thousand-separator:"\,";}
@page
	{margin:.75in .7in .75in .7in;
	mso-header-margin:.51in;
	mso-footer-margin:.51in;}
.font5
	{color:black;
	font-size:9.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Tahoma, sans-serif;
	mso-font-charset:1;}
.font6
	{color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;}
tr
	{mso-height-source:auto;}
col
	{mso-width-source:auto;}
br
	{mso-data-placement:same-cell;}
td
	{padding:0px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri;
	mso-generic-font-family:auto;
	mso-font-charset:1;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;
	mso-protection:locked visible;
	white-space:nowrap;
	mso-rotate:0;}
.xl66
	{color:windowtext;
	font-family:Calibri, sans-serif;
	mso-font-charset:1;}
.xl67
	{color:windowtext;
	font-family:Calibri, sans-serif;
	mso-font-charset:1;}
-->
</style>
</head>

<body link="#0563C1" vlink="#954F72">



</body>

</html>
