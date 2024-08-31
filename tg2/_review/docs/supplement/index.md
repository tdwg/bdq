# BDQ Core Supplemental Information

**Date version issued**  (Draft)

**Date created** (Draft)

**Part of TDWG Standard**

**This version**

**Latest version**

**Previous version**

**Contributors**

Lee Belbin, Arthur D. Chapman, Paul J. Morris, John R. Wieczorek, Paula Zermoglio, Alex Thompson and Yi Ming Gan.

**Creator**

TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions).

### Table of Contents ###

```
1 Introduction
1.1 Audience
1.2 Status of the content of this document
1.3 RFC 2119 keywords
1.4 Namespace abbreviations

``` 

## 1. Introduction

This document contains information that is considered supplemental to the normative and non-normative BDQ Core documentation. 

### 1.1 Audience

Supplemental information is included for anyone seeking further historical context or technical details of components of the BDQ Core standard. This information may be relevant for curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners that wish to evaluate and/or improve the quality of the biodiversity data of interest to their domain. 

This document provides practical information to those who wish to implement BDQ Core. It also provides some guidelines based on the knowledge of the authors, for those who may maintain BDQ Core.

### 1.2. Status of the content of this document

This document is non-normative.

### 1.3 RFC 2119 keywords

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.4 Namespace abbreviations

The following namespace abbreviations are used in this document:

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

## Goes in Supplement: 2 Historical Context

An internationally agreed standard suite of core tests and resulting assertions can be used by all data providers, data collectors and data users to improve the quality of the data. This will allow for more appropriate and more accurate use of biodiversity data. Other than data availability, ‘Data Quality’ is probably the most significant issue for users of biodiversity data and this is especially so for the research community. The tests will not correct all issues that exist with the data, but reports from the tests will identify issues that need to be addressed by users of the data. This may require the user to make decisions on the data - i.e., data that may need to be excluded, data that may need examining for possible improvement, and data that can be used as is. It is always the purview of the user to decide what data is of suitable quality for their use.

## Goes in Supplement: 2.1 Definition of CORE

'CORE' in the context of this standard implies that the tests are informative, simple to implement, are mandatory for enhancements/amendments, have ‘power’ in that they will not likely result in 0% or 100% of all records failing or passing, are widely applicable across sub-disciplines within the biodiversity domain, may elevate the significance of an issue (e.g., no value for dcterms:license) or they may be 'aspirational' in the sense of encouraging priority developments in the biodiversity informatics domain (e.g., testing for any annotations against a record). The scope of CORE was also developed from the user needs analysis of BDQ Task Group 3, (Data Quality Use Cases: Rees & Nicholls 2020). The CORE tests largely cover data quality with regards to what organism has occurred where, at what times, and a subset of Darwin Core terms that we consider to be critical metadata about occurrence records.

A number of tests were framed, but considered out of scope for CORE data quality needs ('Supplementary' GitHub tag). Implementers are free to implement a subset of the CORE tests or add additional tests when there is a particular data quality needs within their domain. For example, the testing for a value of sub-genus against a taxonomic name authority or testing for a valid depth against maximum depth around the location of an observation. Over the period of this project, many tests were removed from CORE on the basis that they could not be currently implemented in a manner that would result in predictable results. For example, the test VALIDATION_GEOGRAPHY_CONSISTENT was rejected late in the project because of the complexities in matching terms in the geographic names hierarchy, which is less standardized than the taxonomic names hierarchy.


## 2 Framework for describing data quality

The specification of the tests within the Framework allows the same set of tests to apply to both Data Quality Control (correcting errors) and Data Quality Assurance (filtering out problematic records to limit data to that with quality for meeting a particular need). The design of the Validations and Measures are intended to be agnostic as to whether their use is for Data Quality Control (finding problematic data), or Data Quality Assurance (filtering out NOT_COMPLIANT records).

### 2.1 Introduction

Included in this standard is a specification for a framework for describing data quality. Each of the tests in this standard has been designed within this framework and is framed using the terms and concepts from the framework. The framework provides the context for each test, and has shaped decisions made about each test.

The framework data quality with respect to some specified use.  It provides a means to describe a use of data, and what is needed for some data set to have quality for that use, that is for some data set to be fit for a specified purpose.  The framework explicitly links data quality to use, and allows formal description of means to assure that data are fit for some specified purpose.  

### 2.2 Data Quality Control, Data Quality Assurance

The framework draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.

### 2.3 Data Quality Needs, Data Quality Mechanisms, Data Quality Reports

The framework organizes data quality concepts into three areas: Needs, Mechanisms, and Reports.  Data Quality Needs identify a use to which data may be put, and frame a set of requirements that data needs to meet to be fit for that use, and means by which data not fit for that use may be improved.  The tests described in this standard are formal descriptions of data quality needs for CORE purposes.  Data Quality Mechanisms in the framework are formal descriptions of software and other mechanisms that implement tests described in the Needs area.  Data Quality Reports are the results produced by Mechanisms on some set of data.  The tests described in this standard include specifications of assertions to be made in Data Quality Reports.

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

The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

## Goes in Supplement: 3 Developing the Tests

### 3.3 Tests and Data Dimensions

We identified four categories of information elements of biodiversity-related data that we needed to cover with the tests: Name (taxonomic information); space (geographic location); time (temporal terms) and other (all other terms such as dwc:basisOfRecord). A record without a taxonomic name, a location or a date has limited value. Three tests in this standard specifically target records with no name, space or time values.

#### 3.4 Types of Test

The concept of 'tests' in this standard include Validation, Issue, Amendment and Measure. Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags. The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary consisting of exactly COMPLIANT or NOT_COMPLIANT for Validations, NOT_ISSUE, POTENTIAL_ISSUE or ISSUE for Issues, either a numeric value or a controlled vocabulary consisting of COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments.

2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 

3. The Remark supplies human-readable text describing reasons for the test result output.

Validation tests are phrased as positive statements, consistent with the Framework.  Validations evaluate values or in some cases, presence or lack of a value to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT. The formal response of VALIDATIONs can take one of four forms. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable (bdq:sourceAuthority), a Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run, a Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation, a Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 

Issues are a form of warning flag where the test is drawing attention to potential problem with the value of a Darwin Core term for at least one use case. Issues are currently outside the Data Quality Fitness for Use Framework. Issues result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "POTENTIAL_ISSUE" or "NOT_ISSUE". Human evaluation of potential issues require a human review. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POSSIBLE_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.  

An Amendment may propose a change to an exisitng Darwin Core value or fill in a missing value. Amendments  is intended to improve one or more components of the quality of the record.  The Response.result from an Amendment MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  The Framework also supports changes to procedures but we have not framed any such tests in this form.  

A Measure returns a numeric value or INTERNAL_PREREQUISITES_NOT_MET. Most Measures count the number of Validation or Amendment tests that a specifified Response.Result. MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. 

[From QRG]

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

[End QRG addition]

All tests could be accumulated across multiple records (bdqffdq:MultiRecords). For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not.  Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes.  Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.    

### 3.6 Domain Scope of Tests

The domain scope of each test is also largely provided by the bdqffdq:Specification. The Darwin Core terms used in the Specification are included in the "Information Elements". The "Specification" also includes references to external (to the Darwin Core standard) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource required for the implementation of the test.

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values.  This allows us to define general tests that provide support for non functional requirements that vary within the community.  For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite.  Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests.   Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values.

[Text from QRG start]

#### Parameterising the tests

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. This allows us to define general tests that provide support for non functional requirements that vary within the community. 

For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite. Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 

Tests are paired in that all AMENDMENTs require a corresponding VALIDATION that assesses some aspect of data quality. An AMENDMENT may be able to improve the quality of data with respect to that VALIDATION. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values. 

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

[End of QRG Text entry]

### 3.7 Test Parameters

Some tests have been defined as parameterized. A parameterized test will behave differently on the same data when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs.

The existence of national requirements for spatial data to be represented with a particular datum lead us to identify a requirement that some tests be able to be adjusted to the needs of particular communities. An example is AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT, which takes a Parameter bdq:defaultGeodeticDatum, with a default value that fills most users’ needs of “EPSG:4326”, but recognizes that some users may have requirements that for data to have quality, they must associate dwc:decimalLatitude and dwc:decimalLongitude with a different spatial reference system in dwc:geodeticDatum. Other tests related to georeferences are similarly parameterized, with a similar default, understanding that most CORE users will be working with EPSG:4326, but others will have requirements for a different spatial reference system. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Parameters are not intended to relax the definition of data having quality for CORE needs. The specifications deliberately do not include parameters that would relax tests on secondary terms for downstream research users or tighten them for upstream data capture. Some tests which would serve the needs of users engaged in data capture or preparing data for aggregation, but not of downstream aggregators or research users were considered, but deemed non-CORE and are not specified here. We have similarly resisted the temptation to parameterize tests to meet the needs of different portions of the data life cycle.

### 3.8 Workflows and Sequencing of Tests

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


### Goes in Supplement: Considerations for use of MultiRecord Measures

MultiRecord tests examine data across a data set.  

The BDQ Core MultiRecord Measures all take the output of other tests as their input rather than data.  The inputs, that is the InformationElements, for these Measures in bdqcore: are the outputs of SingleRecord Validations.  

One subset of these measures simply counts the Responses from a given Validation that have Response.result of COMPLIANT.  For QualityControl, these numbers identify where work is needed to make more of a data set fit for use for a given UseCase.  These MultiRecord Measures that return counts can be run before an amendment step in a data processing pipeline, and run again after applying all of the proposed changes to the data from the Amendments to the data set.  A comparison of these pre-amendment and post-amendment phases will identify how much accepting all of the proposed changes from the amendments will improve the quality of the data for a given UseCase.

The other subset of these measures are intended for QualityAssurance.  These QA measures return a Response.result of COMPLETE if all of a given Validation on SingleRecords in a MultiRecord have a response that indicates that the data are fit for use.  A MultiRecord is fit for use for a given UseCase if each of the MultiRecord QA Measures on that MultiRecord returns COMPLETE.  If this is not the case, SingleRecords where the Validations are other than COMPLIANT are filtered out until all of the MultiRecord QA measures return COMPLETE.  The MultiRecord QA measures are the formal means the Fitness for Use Framework provides for ensuring that a data set is fit for use for a given UseCase.  

Some Validations return Response.status=INTERNAL_PREREQUISITES_NOT_MET when one or more of the input InformationElements contain empty values.  For some UseCases, empty values in some fields make the data not fit for use (these are usually tested directly for with VALIDATION...NOTEMPTY tests), however, some Validations operate on sparse data or other cases where the data is fit for use even without values, but when values are present, they must comply with some restriction.  For example, dwc:minimumDepth and dwc:maximumDepth are not expected to be populated for terrestrial data, but are expected to be within range when values are supplied (for freshwater and marine data).  A subset of the MultiRecord QA Measures accomodate such cases by returning Response.result=COMPLETE for validations that are either Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET.  Thus they can measure that all of the SingleRecords in a MultiRecord either have, for example, no value in dwc:minimumDepth or have an in-range value for dwc:minimumDepth.   

It is possible, but less flexible, to frame Validations to return Result.response=COMPLIANT for either empty values or non-empty values that satisfy other validation criteria.  Concerns are better separated, and individual tests are better composed to fit particular user needs, by having the Validations treat empty data as INTERNAL_PREREQUISITES_NOT_MET, and then framing MultiRecord QA Measures as appropriate for a given UseCase.

MultiRecord measures can also operate directly on the data, for example, a MultiRecord Measure could be framed to measure the average number of individuals reported in dwc:individualCount in a data set.

### Goes in Supplement: Considerations Concerning Input Data Values for AMENDMENTS

One of the early conclusions to this project was the need for controlled vocabularies and an early spin-off of Data Qality Task Group 4 on Vocabularies (https://github.com/tdwg/bdq/tree/master/tg4). Testing the 'quality' or 'fitness for use' of Darwin Core encoded data is made more difficult due to the lack of a comprehensive suite of controlled vocabularies.

Testing Darwin Core values against a known Source Authority using a VALIDATION type test is straight forward: A test is either COMPLIANT or NOT COMPLIANT. This standard includes tests of type AMENDMENT and the mapping of input Darwin Core values to known Vocabulary values is poorly developed. If a VALIDATION returns COMPLIANT, no AMENDMENT is necessary. For example, if the input value to a test is say dwc:sex="Female", then no AMENDMENT is required. If however, the input value is dwc:sex:f., can this be interpreted as "Female"? Probably. What about dwc:sex="M"? This could be "Male" or "Mixed" according to https://api.gbif.org/v1/vocabularies/Sex/concepts. <!--- Ming: I asked GBIF about this specific example and they said that "M" will be matched to Male, but I am not sure how the API works exactly ---><!--- PJM: the rec_occur_qc implementation uses the vocabulary directly, finds, ^M matches male and mixed, so asserts that it can't make the amendment, I can't speak about the (by our test specification, incorrect) actions that gbif is taking on their vocabulary, their API delivers the vocabulary, but doesn't do this sort of matching, so what they are describing is some internal that uses the vocabulary --->

A key phrase within this standard that particularly relates to many of the Expected Responses of tests is " dwc:term can be unambiguously interpreted as ...". In the case above for dwc:sex="M", the determination is that it is ambiguous. In this case, no AMENDMENT can be made.

When carrying out Amendments where numeric vales are concerned (e.g. feet to meters, etc.) the principle of reversability is paramount, and thus rounding up or down or using approximations should be avoided and only exact values used.

We see an urgent need for a comprehensive, internationally agreed list of Darwin Core (https://dwc.tdwg.org/) term values that are mapped to standard values. GBIF has implemented some unique values, for example https://api.gbif.org/v1/vocabularies/Sex/concepts/Female/hiddenLabels, but such lists are not comprehensive. While there has been a survey of Darwin Core 'distinct' values for GBIF, ALA, iDigBio and VertNet, these are both dated, and where possible, have not been mapped to standard values, if they exist.

In this standard, we have taken an expedient approach in relation to making AMENDMENTs. We have used code in our tests to try and parse out likely, unambiguous matches. This is far from an ideal solution, but it does provide the potential of our AMENDMENTs to 'value add' to Darwin Core data records.


## Goes in Supplement? Implications for the Darwin Core Standard (John)

Early recognition that estimating 'fitness for use'/'quality was made difficult because of the lack of vocabularies...TG4.

Definitions, uses in the wild, and best practices for Taxon class ..ID terms.

[ Mention of issues arising such as use of dwc:country and dwc:countryCode and "High Seas"]

How to identify the High Seas.


## Goes in Supplement? Acronyms

| **Acronym** | **Explanation**                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------|
| ALA         | Atlas of Living Australia                                                                                      | 
| BDQ         | TDWG Biodiversity Data Quality Interest Group                                                                  |
| BISON       | Biodiversity Information Serving Our Nation                                                                    |
| CRIA        | Centro de Referência em Informação Ambiental                                                                   |
| EPSG        | European Petroleum Survey Group                                                                                |
| GBIF        | Global Biodiversity Information Facility                                                                       |
| iDigBio     | Integrated Digitized BioCollections                                                                            |
| IRI         | Internationalized Resource Identifier                                                                          |
| ISO         | International Standards Organization                                                                           |
| TDWG        | Biodiversity Information Standards                                                                             |
| TG1         | Biodiversity Data Quality Interest Group Task Group 1: Framework on Data Quality                               |
| TG2         | Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions                       |
| TG3         | Biodiversity Data Quality Interest Group Task Group 3: Data Quality Use Cases                                  |
| TG4         | Biodiversity Data Quality Interest Group Task Group 4: Best Practices for Development of Vocabularies of Value |

## Goes in Supplement: Rationale Management Documentation

### Goes in Supplement: Developing tests with Github Issues

The bdqcore: tests were developed in issues in the tdwg/bdq github space  

### Goes in Supplement: Tags and Categorizing Issues

The development of each test, with documentation of why particular decisions were made with regard to that test, has been documented in issues in the tdwg/bdq github repository. Each issue has table in markdown format in its Issue.  Each issue was tagged with the following GitHub issue tags to assist in finding, evaluating, and asserting conclusions about each test. 

<!--- Start: PJM Added the terms from "bdqtag" glossary terms 2024 Aug 24 --->

The following list of Tags is used on issues: 

| tag | definition | comment |
| --- | ---------- | ------- |
| Amendment | A label to indicate a test of type AMENDMENT which may propose a change or addition to at least one Darwin Core term that is intended to improve one or more components of the quality of the record. | See bdqffdq:Amendment |
| CORE | Conclusion that a test belongs in the set of tests for evaluating biodiversity data quality as represented by the values of Darwin Core terms. CORE tests address identified user needs, are widely applicable, informative, unambiguous, well defined, and straight forward to implement. |  |
| DO NOT IMPLEMENT | Conclusion that a test is not recommended to be implemented with the current level of understanding for one or more reasons: Available vocabularies are ambiguous; the test is too complex to implement concisely; implementation is expected to lead to ambiguous or inaccurate results. |  |
| Immature/Incomplete | Conclusion that a test requires substantial work is still needed to develop the specification to the point where the test can be reliably and usefully implemented. This may indicate work that is wholly internal to the test specification such as developing a consistent Expected Response, or may indicate that external work is needed to develop an agreed vocabulary for values of the tested term. An immature/incomplete test may be made CORE, Supplementary, or DO NOT IMPLEMENT when relevant criteria are satisfied. |  |
| ISO/DCMI STANDARD | A reference to either an ISO (International Organization for Standardization) Standard or a DCMI (Dublin Core Metadata Initiative) Standard |  |
| Issue | A label to indicate a test of type ISSUE, where potential problems are flagged and may need examination by the user to determine if data have quality for their use. | see bdqffdq:Issue |
| Measure | A label to indicate a test of type MEASURE that performs a measurement according to some data quality dimension. | See bdqffdq:Measure |
| NAME | A label to indicate that the test is related to Darwin Core terms in the dwc:Taxon Class. |  |
| NEEDS WORK | A label that indicates that an issue (Test) requires more work before finalising. | Supports a workflow of contributors identifying tests needing work with this tag, and review of issues with this tag in task group meetings.  |
| OTHER | A label to indicate that the test is related to Darwin Core terms other than Classes dwc:Taxon, dwc:Location or dwc:Event. |  |
| Parameterized | A label for a test that requires a bdq:Parameter to be set prior to a bdq:parameterizedTest being run. |  |
| SPACE | A label to indicate that the test is related to Darwin Core terms in the dwc:Location Class. |  |
| Supplementary | Conclusion that a test is regarded as not CORE (cf. the tag CORE) because of one or more reasons: Not widely applicable; not clearly matched to an identified data quality need; not informative concerning the 'quality' or lack of quality of the data; likely to return a high percentage of either bdq:NOT_COMPLIANT or bdq:POTENTIAL_ISSUE records. A Supplementary test MAY be implemented in a local implementation if a suitable use case exists. | A Supplementary test may be made CORE at a later time. |
| Test | Tests descriptions created by TG2, either CORE, Immature/Incomplete, Supplementary, or DO NOT IMPLEMENT. | Supports workflows for exporting tests from issues to process the markdown into csv files for review.  |
| TG1 | Issues pertinent to Task Group 1 ([Framework on Data Quality](https://tdwg.github.io/bdq/tg1/site)) of the TDWG Data Quality Interest Group. |  |
| TG2 | Issues including Tests, developed by, or pertinent to Task Group 2 ([Data Quality Tests and Assertions](https://github.com/tdwg/bdq/blob/master/tg2/README.md)) of the TDWG Data Quality Interest Group. |  |
| TG3 | Issues pertinent to Task Group 3 ([Data Quality Use Cases](https://github.com/tdwg/bdq/blob/master/tg3/README.md)) of the TDWG Data Quality Interest Group. |  |
| TG4 | Issues pertinent to Task Group 4 ([Best Practices for Development of Vocabularies of Value](https://github.com/tdwg/bdq/blob/master/tg4/README.md)) of the TDWG Data Quality Interest Group. |  |
| TIME | A label to indicate that the test is related to Darwin Core terms in the dwc:Event Class. |  |
| Validation | A label to indicate a test of type VALIDATION that describes a run of a test for validity against a set of criteria. | See bdqffdq:Validation |
| VOCABULARY | A label to indicate that a Test requires a controlled Vocabulary |  |

<!--- End: PJM Added the terms from "bdqtag" glossary terms 2024 Aug 24 --->

Four tags: CORE, DO NOT IMPLEMENT, Immature/Incomplete, and Supplementary mark conclusions made about tests.

The tag NEEDS WORK was repeatedly added and removed to issues and was a valuable support for the evaluation of tests in repeated feedback loops of: Frame the description of a test, idependently produce validation data and an implementation, run the implementation against the validation data, evaluate cases where the expectations in the validation data differ from the test results (which could be a defect in the implementation, in the validation data, or a problem in the test specification), discuss as a group, make changes as needed, and repeat.


### Goes in Supplement: Using Markdown Tables in Github Issues to develop test descriptors

The development of each test, with documentation of why particular decisions were made with regard to that test, has been documented in issues in the tdwg/bdq github repository. Each issue has table in markdown format in its Issue.  The terminology in this markdown table differs slightly from the Framework, so to support understanding of the rationale management the non-standard terminology used there is documented below:

<!--- three duplicative sets of information, two blocks of test here, then rows in glossary file... --->

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

### Duplicate of above? 

The Test Descriptors are a simplified set of the bdqffdq: terms to describe a test. Some descriptors such as the GUID are intended for machine consumption, some such as the "Description" are designed to be human-readable' for consumers of biodiversity data quality reports while descriptors such as the "Specification" ensure that implementers have no ambiguity about how the test should be coded.

**"GUID"** [normative]:A machine readable unique identifier for the test. Example: "0493bcfb-652e-4d17-815b-b0cce0742fb" 

**"Label"** [normative]: A human readable label identifying the test.  The labels largely follow the pattern TYPE_INFORMATIONELEMENT_STATUS.. Example: "VALIDATION_COUNTRYCODE_STANDARD" 

**"Description"** [non-normative]: A non-technical description of what the test does, intended for consumers of data quality reports in concert with the Response.comment. Example: "Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?"

**"TestType"** [normative]: The Type of assertion that this test produces, Measure, Validation, Amendment, Issue.. Example: "Validation" 

**"Darwin Core Class"** [non-normative]: The Information Element in the original terms of the framework, the general sort of information this test operates on. . Example: "dwc:Location"  

**"Information Elements ActedUpon"** [normative]:A list of the specific Darwin Core terms that are the focus of the test.. Example: "dwc:countryCode" 

**"Information Elements Consulted"** [normative]:"dwc:scientificName" A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon.

**"Specification"** [normative]: The specification for implementors describing the expected behavior of the test. Example: EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is EMPTY; COMPLIANT if the value of dwc:phylum was found as a value at the rank of Phylum by the bdq:sourceAuthority; otherwise NOT_COMPLIANT."  

**"Parameters"** [normative]: Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain.. Example: "bdq:taxonIsMarine" 

**"Dimension"** [normative]: The [data quality dimension](https://github.com/tdwg/bdq/blob/master/tg2/vocabularies/data_quality_dimensions.csv) for this test. Example: "Conformance"

**"Criterion Label"** [non-normative]:  A label for the Criterion (TODO: Criterion/CriteronInContext applies to Validations, need to clarify for Dimension/DimensionInContext, Enhancement/EnhancementInContext, Issue/IssueInContext). Example: "Conformance: standard"

**"Resource Type"** [normative]: The type of resource on which this test acts, SingleRecord or MultiRecord, the CORE tests include Validations, Measures, and Amendments that operate on SingleRecords and a set of MultiRecord Measures that assess the results of the SingleRecord Validations. Example: "SingleRecord"   

**"Source Authority"** [normative]: A reference to an external (non-Darwin Core) authority required for the test. bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}. The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be exTests may require reference to external data such as standard vocabularies of terms or names. While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

A reference to an external (non-Darwin Core) authority required for the test. bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}. The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be expected to be passed in as the parameter value.  Other non-empty strings would select other source authorities. The structure of the information in Source Authority ideally has two components. The first component refers to the standard itself, which may include a vocabulary of accepted values. The second component will, wherever possible (if available), refer to an API that will assist implementers of the tests. In some cases, the API component will refer to a 'third party' site where it is hoped will remain in sync with the standard, for example, a GBIF vocabulary API site would ideally be synced with a Darwin Core site. Example: "bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}"

**"Examples"** [non-normative]: Example of inputs for a test and the expected output from an implementation of the test given those outputs.  A ’pass’ and a ‘fail’ example are provided for each test.  All examples listed are also present in the the validation data suite. Example: "[dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"]"

**"References"** [non-normative]: A list of references that will assist in a thorough understanding of the test. Example: "GBIF Secretariat (2019). GBIF Backbone Taxonomy. Checklist dataset (https://doi.org/10.15468/39omei)"

**"Example Implementations (Mechanisms)"** [non-normative]: nown Mechanisms with implementations of the test.
. Example: "FilteredPush/Kurator: geo_ref_qc"

**"Link to Specification Source Code"** [non-normative]: A link to code that implements the test. Example: https://github.com/FilteredPush/

**"Notes"** [non-normative]: Additional, guidance that may be necessary for the accurate implementation of the tests. Example: "Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters."  

### And again duplicative Test Field vocabulary from the glossary

| Test Field | Definition | 
| Darwin Core Class | "The Information Element in the original terms of the framework, the general sort of information this test operates on. |
| Data Quality Dimension | "The data quality dimension for this test. See bbqffdq:DataQualityDimension. |
| Description | "A non-technical description of what the test does, intended for consumers of data quality reports in concert with the bdq:Response.comment. |
| Example Implementations (Mechanisms) | "Known Mechanisms with implementations of the test. |
| Examples | "A ’pass’ and a ‘fail’ example of test data. All examples listed are present in the the validation data suite. |
| Examples | 
| Expected Response | "The specification for implementors describing the expected behavior of the test. See bdqffdq:Specification |
| GUID | "see bdq:GUID |
| Information Elements Acted Upon | "A list of the specific Darwin Core terms that are the focus of a test. |
| Information Elements Consulted | "AA list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon. |
| Label | "A human readable label identifying the test. The labels largely follow the pattern TYPE_INFORMATIONELEMENT_STATUS. |"cf. rdfs:label"
| Link to Specification Source Code | "A link to code that implements the test. |
| Notes | "Additional, non-normative comments that the Task Group believed necessary for an accurate understanding of the test or issues that implementers needed to be aware of. |
| Parameter(s) | "Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain. |
| References | "A list of references pertinent to the test. |
| Source | "The origin of the concept of the test. |
| Source Authority | "A reference to an external (non-Darwin Core) authority required for the test.  See bdq:sourceAuthority |
| Specification Last Updated | "The last date a change was made to a test that affects the operation of the test. |
| Term-Actions | "Equivalent to the bdqTestField:Label without the leading Test Type. |
| Test Type | The Type of assertion that the test produces, Measure, Validation, Amendment, Issue. |

---

## Goes in Supplement: Time and Date Issues

### Goes in Supplement: Event and Calendars

Different calendars have been used at different times in different places, and the transcription of an
original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date, and metadata may or not be present to even identify such records.

Countries and researchers have changed from the Julian calendar to the Gregorian calendar at different times. For example, Russia adopted the Gregorian Calendar on 1918-02-14, the British Empire in 1752-09-14, different regions in France between 1582 and 1760, with France also adopting the French Republican Calendar 1793-1805. The difference between the Gregorian and Julian calendar has typically been around 10 days. But, the day that is considered the first day of the year has also changed at different times in different countries, meaning that the difference can be as great as 1 year and 10 days. Given the complexity, and ongoing nature of transitions between calendars, we do not advocate using VALIDATION_EVENTDATE_INRANGE for quality assurance by selecting a transition date and using it as a threshold.

[John’s statement on calendars as a placeholder (https://github.com/tdwg/bdq/issues/76#issuecomment-1591985055): “I don't think we are in any position to posit a date after which the Gregorian calendar assumption is safe. It is still not safe today, it's just that its use for civil purposes has ever fewer exceptions as time goes on (so far). Making a statement about a particular date (other than the date of its origin) for a date of special mention necessarily has discriminatory implications. We do NOT want that.

In this particular issue, and perhaps in all others where this has come up, I do not see that the uncertainty associated with the date actually has anything to do with what we are testing. This test can't assess if a date is actually within a Gregorian date interval, except in special cases where the Julian and Gregorian calendars coincide, and even that is ignoring all other possible calendars. Instead, it is able to test that a date following the ISO 8601-1 date specification is within a range specified in that context. We can't effectively do anything else because Darwin Core doesn't even provide for stating the original calendar used - it's forcing people to use the Gregorian calendar without describing the responsibility for doing so and the consequences of not doing so. I think the place for awareness of the implications of dates with unknown calendars is in the Darwin Core date terms.]

## Goes in Supplement: Time

See: https://xkcd.com/2867/ and  https://www.xkcd.com/1883/

**If time zone is not included as a component of date and time, the date and time information is expected to be consistent throughout the event terms**

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



