# List of BDQ Core Tests and Assertions

**Title**: List of BDQ Core Tests and Assertions

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: <{standard_iri}>

**This version**: <{current_iri}{ratification_date}>

**Latest version**: <{current_iri}>

{previous_version_slot}

**Abstract**: The BDQ Core list of data quality tests. Test Types, Descriptors, 

**Contributors**: Lee Belbin, Paul Morris, Arthur Chapman, John Wieczorek, Alan Koch Veiga, Paula F Zermoglio, Antonio M Saraiva, Alex Thompson, Miles Nicholls, Emily R Rees, Christian Gendreau, Dmitry Schigel, Yi Ming Gan

**Creator**: TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions)

**Bibliographic citation**: TDWG Biodiversity Data Quality Interest Group. 2024. BDQ Dimensions Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <{current_iri}{ratification_date}>

## 1 Introduction (non-normative)

This document lists the BDQ Core tests. The document includes terms in three namespaces that contain the recommended terms: `bdq:`, `bdqffdq:` and `bdq:core`. For details and rationale, see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889.

CORE tests are all defined as single record-level (bdqffdq:SingleRecord) tests, applying to a single observation or event structured under Darwin Core terms (Wieczorek et al 2012). The one exception to this is the test ISSUE_ANNOTATION_NOTEMPTY where this standard encourages the implementation of a standard for annotating occurrence records supported by Darwin Core. This test is an example of what the team calls 'aspirational tests', suggesting that supporting infrastructure seems well-justified. 

[!--- suggest "Single record (bdqffdq:SingleRecord) tests apply to a single observation or event structured under Darwin Core terms (Wieczorek et al 2012). The one exception to this is the test ISSUE_ANNOTATION_NOTEMPTY where this standard encourages the implementation of a standard for annotating occurrence records supported by Darwin Core. Multi record (bdqffdq:MultiRecord) tests sum up results across all records for each single record test."   AC - PAUL to check?  ---]

Tests may require reference to external data such as standard vocabularies of terms or names. While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

(Make sure to establish that the standard does not specify the "format" of the responses (JSON within an Annotation, etc.), but it does specify the required content regardless of serialization format.)

(Make sure this is addressed in this document) We acknowledge the centrality of the work of the TDWG Annotations Interest Group (https://github.com/tdwg/annotations) as to how the test results are reported against records. Test results structured with these three components can be readily wrapped in the body annotation document that follows the W3C Web Annotation Data Model (Sanderson et al. 2017), along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.

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

For a simplied list of current terms, see the BDQ Core Quick Reference Guide {http://..........}.

Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4, the values of the `Term IRI` and `Definition` are normative. The values of `Term Name` `skos:pref:Label` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Examples` and `Notes`) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.3 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdq: | http://rs.tdwg.org/bdq/terms/ |
| bbqffdq: | http://rs.tdwg.org/bdq/bdqffdq/ |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/ |

## 2 Use of Terms
Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), controlled value strings MUST be used as values of the `bdqffdq:` namespace.
Due to the requirements of [bdq](https://rs.tdwg.org/bdq/terms), controlled value strings MUST be used as values of the `bdq:` namespace.
Due to the requirements of [bdq](https://rs.tdwg.org/bdqcore/terms), controlled value strings MUST be used as values of the `bdqcore:` namespace.

## 3 Term indices
