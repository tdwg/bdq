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

Contributors
: {contributors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}


### Table of Contents ###

{toc}

# 1 Introduction

This users guide describes how consumers of data quality reports can interpret the content of those reports.  

See also the [Implementer's Guide](BDQ_Core_Implementers_guide.md) for those writing sofware to implement the tests.

Each test is intended to examine just one specific aspect of data quality.   Tests are assembled into test suites (profiles) that assess the fitness for use of data for a specific use.

# 2.0 Kinds of Tests and what they do (non-normative)

## 2.1 Validation 

A VALIDATION evaluates the values in one or more Darwin Core terms for fitness for some particular narrow data quality need within CORE. Validations evaluate values or in some cases, presence or lack of a value. Validation tests are phrased as positive statements, consistent with the "Fitness for Use Framework".  A Validation tests to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY, is phrased as "Not Empty", and will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem. The formal response of VALIDATIONs can take one of four forms:

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation.
4. A Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 

## 2.2 Issue

ISSUE is a form of warning flag where the test is drawing attention to a non-empty value of a Darwin Core term. We have used these for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of this case would take human review. For example, ISSUE_ANNOTATION_NOTEMPTY is informing the tester than there is at least one annotation associated with record and this should be evaluated before using the record. Similarly for the other two ISSUE-type tests: ISSUE_DATAGENERALIZATIONS_NOTEMPTY where some form of transformation has occurred, and ISSUE_ESTABLISHMENTMEANS_NOTEMPTY where the value needs to be assessed for utility. ISSUEs are currently outside the Data Quality Fitness for Use Framework. ISSUEs result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "IS_ISSUE", "POTENTIAL_ISSUE" or "NOT_ISSUE". ISSUE is symmetrical to NOT_COMPLIANT, NOT_ISSUE is approximately symmetrical to COMPLIANT, and POTENTIAL_ISSUE does not have an equivalent Validation Response.result. 

## 2.3 Amendment

An AMENDMENT may propose a change or addition to at least one Darwin Core term that is intended to improve one or more components of the quality of the record.  The Response.result from an AMENDMENT MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for QualityControl of an existing database or record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  Amendments, under the framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in these tests.  

## 2.4 Measure 

A MEASURE may return either a Response.result that is a numeric value, or the values COMPLETE or NOT_COMPLETE, or NOT_REPORTED (when the Response.status="INTERNAL_PREREQUISITES_NOTMET").  The principle Measure defined in the core tests is MEASURE_EVENTDATE_DURATIONINSECONDS, it returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the VALIDATIONs and AMENDMENTs and in one case provides an indication of the length of the period of the value of dwc:eventDate.

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

# 3.0 Characteristics of the tests (non-normative)

The tests are agnostic about the form in which the data are stored or transported. The test specifications all assume that data are presented to the tests in structured form such as csv or tab delimited text files, with data elements identifiable as Darwin Core terms (Wieczorek et al. 2012). Here, cells contain non-typed data values possibly aggregated from and serialized from multiple sources such as relational databases where Boolean nulls and non-string data types may exist, but the data have been exported into a string serialization that supports neither null nor typed data. 

The tests are also agnostic about uses for quality assurance, where output data are limited to those for which all Validations are Compliant, or for quality control where the results of Validations, Issues, Measures, and Amendments can be used to improve the quality of the data.

The test specifications are agnostic about where in the biodiversity data lifecycle they are used. Implementers can incorporate the tests at any stage to help identify and correct issues. The tests can be applied during data capture in the field, transcription from paper records, data ingestion into databases, integration with collections management systems, data aggregation, and research on aggregated biodiversity data. They are designed to run at any point in the data lifecycle, from initial collection or observation to data transcription, database loading, and preparation for or during data aggregation. [However, the framing of the InformationElements as Darwin Core terms with the CORE Use Case focused on the research needs of downstream users means that competing requirements have led to some different decisions than would have been made if the aim was to solely evaluate data in a database of records and preparing it for aggregation.]   

**(Make sure to establish that the standard does not specify the "format" of the responses (JSON within an Annotation, etc.), but it does specify the required content regardless of serialization format.)**

**(Make sure this is addressed in this document) We acknowledge the centrality of the work of the TDWG Annotations Interest Group (https://github.com/tdwg/annotations) as to how the test results are reported against records. Test results structured with these three components can be readily wrapped in the body annotation document that follows the W3C Web Annotation Data Model (Sanderson et al. 2017), along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.**

# 4.0 Parameterising the tests

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. This allows us to define general tests that provide support for non functional requirements that vary within the community. 

For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite. Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, repeated in 5.2.3 --->
The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

For a simplied list of current terms, see the BDQ Core Quick Reference Guide {http://..........}.

<!--- end of information that probably goes in the users or implementers guides --->

# 5.0 Inputs to a test 

Each test is defined to take a specific set of input terms (InformationElements, generally Darwin Core terms), and then perform some tightly specified evaluation of those inputs to produce a specific output (the Response, see below). All of the Validations, Amendments, and Issues currently defined in BDQ Core examine a set of Darwin Core terms from a single record, e.g. from a single Occurrence record, rather than looking at the input term(s) over multiple records.  

Consider the test VALIDATION_EVENTDATE_STANDARD, it takes as input the InformationElement dwc:eventDate from a single record, and then asks "Is the value of dwc:eventDate a valid ISO date?".  It will then produce a Response describing the conclusion it reached in asking that question for that record.

# 6.0 Structure of Response (normative)

Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags,  The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary (consisting of exactly COMPLIANT or NOT_COMPLIANT) for validations or Issues (NOT_ISSUE, POTENTIAL_ISSUE, ISSUE), either a numeric value or a controlled vocabulary (consisting of exactly COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments. 
2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 
3. Remark supplies human-readable text describing reasons for the test result output.
   
## 6.1 Parts of a Response from a test. (normative) 

Reports SHOULD identify tests to you using at least the skos:prefLabel for the test class, e.g. VALIDATION_COUNTRY_FOUND.  

Results from each test MUST be delivered in the form of a Response.status, Response.result, and Response.comment.  Each test produces one Response.   A Response.qualifier may also be included.  

- The Response.status tells you if the test was able to run.  
- The Response.result tells you the conclusion of the test if it was able to be run.  Look only to the Response.result to understand if data have quality for some use or not.
- The Response.comment is a brief explanation of why the test reached the conclusion it did, examine the Response comment first to understand why a test provided a particular response.
- The optional Response.qualifier MAY provide additional information.

The Response.status MUST NOT be interpreted as a assertion concerning the quality of the data.  

The Response.result MUST be treated as the sole conclusion about data quality made by the test.  This conclusion MUST be explained in the Response.comment, and MAY be expaned upon in an optional Response.qualifier.

A Response.status of EXTERNAL_PREREQUISITES_NOT_MET tells you that the test was looking information up on some remote resource, such as a web service to look up taxon names, which was not available at the time the test was run.  This Response.status means that if the same test is run again on the same data at a different time, it may have a different result (e.g. if the web service became available and could be queried).

A Response.status of INTERNAL_PREREQUISITES_NOT_MET, however, means that some aspect of the data itself does not meet the prerequisites for running the test, such as an empty dwc:eventDate for a test that evaluates whether the eventDate falls within a particular time span.  If the same test is run again on the same, unmodified data, the same result is expected.  It is all to easy to interpret INTERNAL_PREREQUISITES_NOT_MET as pointing to some quality problem in the data, and while this may seem so, it is is misleading to think so, look instead to some Validation that specifically makes that evaluation and returns a Response.result of COMPLIANT or NOT_COMPLIANT, or some measure that returns a Response.result of COMPLETE or NOT_COMPLETE. 

Validations can also have a Response.status of RUN_HAS_RESULT, this tells you that the test ran, and the result of the test (COMPLIANT or NOT_COMPLIANT) will be found in the Response.result.

Amendments can have a Response.status of either of the prerequisites not met, or FILLED_IN, AMENDED, or NOT_AMENDED.  FILLED_IN tells you that the amendment is proposing that a value that was empty in the data under test can be filled in with a non empty value.  This proposal will be found in the Response.result.  AMENDED tell you that the amendment is proposing a change to an existing value, this proposal will be found in the Response.result.  NOT_AMENDED tells you that the prerequisites for running the amendment were met, but that it did not propose any change to the data.

A Measure returns a numeric value or INTERNAL_PREREQUISITES_NOT_MET. Most Measures count the number of Validation or Amendment tests that a specifified Response.Result. MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. 

Issues result in a Response.status of "RUN_HAS_RESULT" and a Response.status of ISSUE, "POTENTIAL_ISSUE" or "NOT_ISSUE".  Potential issues require a human review. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POSSIBLE_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.   An issue that reports ISSUE is making an assertions that is the same as a Validation reporting a Response.result of NOT_COMPLIANT, in this sense, Issues are the converse of Validations.  The meaning, however, of NOT_ISSUE from an Issue is not the same as COMPLIANT from a Validation.  NOT_ISSUE means that no issue was detected, not that the data comply with any criteria for fitness, while COMPLIANT explicitly means that the data satisify some critierion for fitness for some use.  POTENTIAL_ISSUE has no analog in validations, it marks the presence of something in the data that will need evaluation by a human to determine whether or not the data are fit for their use or not.  One Issue in BDQ Core evaluates whether dwc:dataGeneralizations contains any value, if it does, then it reports POTENTIAL_ISSUE, meaning that a human will need to evaluate whether the information in dwc:dataGeneralizations indicates that the data in that record have been generalized in a way that makes the data unfit for their purpose.  See: [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../bdqcore/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY)  Very few Issues are defined in BDQ Core.

# 7.0 Reading the Quick Reference Guide to the tests (non-normative)

The BDQ Core Quick Reference Guide lists the tests by a subset of Descriptors. This subset provides a summary of the nature of each of the tests, and some Descriptors can be used to filter the tests to those that may be applicable to an application.   An index is provided for each test by UseCase.  Both SingleRecord tests (Validations, Amendments, Issues, Measures) and MultiRecord tests (at this time only Measures that evaluate the output of SingleRecord Validations across a data set) are included.  

For each test, the Quick Reference Guide lists ways to identify the test (Label: the brief human readable means for identifying a test; skos:prefLabel: a human readable label spelled out in words; Versioned IRI: the means for software to identify the test).  It is noted whether a test operates on SingleRecords or a MultiRecord (data set).   A brief description of what the test is intended to do is provided, along with a more detailed description for implementors (consisting of Specification, InformationElements ActedIpon and Consulted, any Paramters that could change the behaviour of the tests, default values for any bdq:sourceAuthority consulted by the test or other parameters).  

Two examples are given, each illustrating opposing behaviors of the test. For Validations, one example provides a Response.result of COMPLIANT, the other of NOT_COMPLIANT.  See the implementation guide for information on a larger set of test validation data.   
A list of UseCases describing data quality needs to which each test is seen to be applicable is provided, along with notes that provide additional guidance for understanding test results and for implementation.  

[Quick Reference Guide to the tests](../bdqcore/index.md)

# 8.0 Amendments only propose changes (normative)

Amendments only propose changes to data.  It is up to the consumers of data quality reports to choose whether or not to accept those changes, particularly into authoritative databases of record.  Consumers of data quality reports MAY choose to change data based on assertions made by Ammendments, or consumers of data quality reports MAY choose to not change their data based on assertions made by Amendments.  Databases of record SHOULD NOT automatically alter data based on assertions made by Amendments without human evaluation.   

# 9.0 Time and TimeZone (non-normative)

Time is not considered in any of the bdqcore: test descriptions.  This means that some cases where time zone data is important, dates within a dataset (bdqffdq:MultiRecord) aggregated from multiple sources may have plus or minus one day errors introduced.  If this would make such data unfit for your purposes, you will need to introduce additional tests. 

