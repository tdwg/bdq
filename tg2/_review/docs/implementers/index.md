# BDQ Core Implementer's Guide

**Date version issued**  (Draft)

**Date created** (Draft)

**Part of TDWG Standard**

**This version**

**Latest version**

**Previous version**

**Contributors**

**Creator**

TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions).

## 1 Introduction (non-normative)

This document provides guidance for those wishing to create sofware implementations (bdqffdq:Mechanism) of BDQ Core tests.

## 1.1 Independence (normative) 

Test implementations SHOULD be independent of how data are stored and transported, data serializations, and the framework or environment in which the tests are being executed.   

## 2 About the Tests 

### 2.1 The Concept of "EMPTY" in BDQ Core (normative)

Empty and NotEmpty are defined as: 

<!--- Load definition of Empty and NotEmpty from bdq vocabulary here into template --->

| term | definition |
| ---  | ---------- |
| bdq:Empty | An evaluation of a value, that in the context of the evaluation, returns true if the value does not contain any characters or values other than those in the range U+0000 to U+0020, otherwise returns false. |
| bdq:NotEmpty |An evaluation of a value, that in the context of the evaluation, returns false if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns true. |

<!--- end load --->

Data that has passed through arbitrary serializations and transformations can contain many anomolies.  Empty is defined to allow tests to clearly separate concerns.  An information Element containing invalid characters, (e.g. letters in an information element that would be expected to contain integers) or values (including string serializations of the NULL value) are NOTEMPTY and are the concern of tests that evaluate bdqdim:Conformance.  Presence or absence of data is a concern for tests evaluating bdqdim:Completeness.  

A bdqffdq:InformationElement containing invalid characters (e.g. letters in an information element that would be expected to contain integers) or values (including string serializations of the NULL value) are NotEmpty, identifying that they are invalid is a concern of other tests evaluating bdqdim:Completeness.

#### 2.1.1 Concerns of Empty (normative)

(1) Spaces, tabs, and other non-printing characters, treated as Empty.

Objects that are null, or null values in a relational database, at the point of test execution, MUST be treated as bdq:Empty.

(2) Serializations of NULL, treated as NotEmpty.

Data serialized from relational database systems may contain string representations of NULL, 
We considered, and explicitly rejected, treating common string serializations of null such as "\N" and "NULL" as empty values.  String serializations of NULL outside of a database, present at the point of evaluation of a test, MUST be treated as bdq:NotEmpty.  A test execution environment MAY deserialize these string serializations of NULL

(3) Data values indicating an unknown, treated as NotEmpty.

The definition of bdq:Empty is not applicable to a discussion of what value to include in a controlled vocabulary to indicate that no meaningful value is present, so no suggestion is made that "EMPTY" should be used as a data value to represent some form of "Null", "Unknown", "Not Recorded", etc. Choices there would fall into the semantics for some set of controlled vocabularies. The relevance to such a discussion is that this definition would treat an empty string as an empty value, with no semantics attached as to why the value is empty.

(4) Independence of tests from the execution framework. 

The evaluation of bdq:Empty MUST be at the point of evaluation of the test.  This allows the tests to be independent of data serializations for transport and the representation of data in test execution environments. 

In BDQ Core, bdq:Empty is used to evaluate bdqffdq:InformationElements within a test specification, it therefore means empty if the data set being evaluated does not contain the term matching the information element, or if the data set contains that term but the value for that term is empty.   This is to allow the application programing interface expressed by  the test bdq:CriterionInContext to be agnostic about the strucuture presented to a framework for executing the tests. 

For csv data a column is either there or not in a data set, but in an rdf representation, some data objects could have relevant properties and others not - and the tests are independent of that.

#### 2.1.2 Example implementation of a function to assess Empty (non-normative)

Here is a java function to evaluate Empty, using trim() to exclude U+0020 (space), U+000A (LF), U+000D (CR) and the other non-printing characters in the unicode range U+0000 to U+0020, and also evaluating null as Empty.  Test implementations can reuse a function like this for tests that evaluate bdq:Empty in their specification.

    public boolean isEmpty(String aString)  {
        boolean result = true;
        if (aString != null && aString.trim().length()>0) { 
            result = false;
        }
        return result;
    }

Here is a MariaDB implementation of a lightweight version of VALIDATION_KINGDOM_NOTEMPTY that provides a list of NOT_COMPLIANT records for some flat taxonomy table in a database, again handing off the resposibility for evaluation of non-printing characters to the trim function available in the language.

    SELECT taxonomy_id, kingdom,
         'VALIDATION_KINGDOM_NOTEMPTY' as test, 'NOT_COMPLIANT' as response_result, 'RUN_HAS_RESULT' as response_status,
         'The value of kingdom is Empty.' as response_comment
    FROM taxonomy
    WHERE 
         kingdom is null
         OR
         length(trim(kingdom)) == 0
    ;

### 2.2 Reading Test Descriptors (non-normative)

## 3 Responses from tests

### 3.1 The Response Object (normative) 

The test types are: Validation, Issue, Amendment and Measure. Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags. The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary consisting of exactly COMPLIANT or NOT_COMPLIANT for Validations, NOT_ISSUE, POTENTIAL_ISSUE or ISSUE for Issues, either a numeric value or a controlled vocabulary consisting of COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments.

2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 

3. The Remark supplies human-readable text describing reasons for the test result output.

### 3.2 Framework elements not included in bdqcore test descriptions (normative)

Implementors SHOULD create an instance of bdqffdq:Mechanism to uniquely identify their suite of test implementations.

Implementations producing data quality reports SHOULD create instances of bdqffdq:Assertions grouped in bdqffdq:DataQualityReports that also specify the bdqffdq:DataResource that the bdqffdq:DataQualityReport concerns.

Implementors MUST provide bdq:Response data in data quality reports consisting of bdq:Response.status, bdq:Response.result, and bdq:Response.comment.  

Implementations MAY perform data Quality Control, data Quality Assurance, or both.  

## 4 Guidelines for Implementers

### Parameters and changing the behavior of a test (normative)

Many tests specify bdqffdq:Parameters in addition to bdqffdq:InformationElements.  Parameters are intended to change the behavior of a test to fit local data quality needs without changing the specification of the test.  

Implementors SHOULD only present non-default parameter values to a test implementation if needed for local data quality needs.

Implemenentors MUST NOT produce test implementations identified by the same identifiers that only implement non-default parameter values.  An implementation of a test MUST support the test execution with the default parameter values, and MAY optionally support other parameter values.   Provided parameters MUST NOT change the behavior of the test to depart from the bdqffdq:Specification.expectedResponse.  Parameters MUST only change the behavior of the test as specified in the bdqffdq:Specification.expectedResponse.

**TODO: The value supplied for the parameter for the test is not an attribute of the data, it is an attribute of the Mechanism (of the system assessing the data quality). If we had included assertions about the validity values of parameters, they should only return external prerequisites not met, as they are assertions about externalities to the data and will change if the same data are run on the same test with a different configuration.**

### Execution Process Agnostic (non-normative)

The test descriptions in bdqcore are designed to be able to be implemented anywhere in the lifecycle of biodiversity data, and are designed to be independent of the environment in which the tests are run.   Tests may be run in the abstract within, for example, relational databases, they may be run individually on single Darwin Core records, or fragments of Darwin Core records within a data capture interface, or may be run in sequence in a processing pipleine of Darwin Core records, or they may be run in paralell in a processing pipeline of Darwin Core records, or they may be run in a workflow environment that produces lists of unique values of Information Elements for each test, executes the test on the unique values, and then maps the results back out onto rows in the data set.  Data may be presented to an execution framework as Flat Darwin Core, or as Structured Darwin Core, or in another structure that can be mapped to the information elements of relevant tests.

The tests are designed to be run at any point in the life cycle of biodiversity data. They may be run at the point of initial collection or observation of organisms. They may be run to support data transcription. They may be run in loading data into databases of records from field or transcription sources. They may be run in preparing data from databases of record for aggregation. They may be run during data aggregation.

### Considerations for execution (normative)

Many tests invoke external bdq:sourceAuthorities, some of these are downloadable vocabulary files, others are webservices over continually changing data.

Implementations SHOULD locally cache the results of calls to remote web services, particularly if they operate on a sequence of SingleRecords instead of operating on distinct values of InformationElements.  Data sets typically contain many repeated values, and remote web services SHOULD NOT be subject to repeated requests asking the same question over and over. 

Some source authorities are highly stable small vocabularies.  Implementors MAY choose to query a local copy of such a vocabulary, even if a remote service is specified in a bdq:sourceAuthority for a test.  Implementors SHOULD monitor for changes to that vocabulary and update if it changes. 

### Order of test execution.

#### Phases: Pre-Amendment, Amendment, Post-Amendment.

Recommended process with the current suite of BDQ Core tests is to run all pertinent single record validations and measures, then run all pertinent multirecord measures, from these calculate some measure of quality, then execute all pertinent amendments, then to run all pertinent single record validations and measures again in a post-amendment phase on the data as if the proposed changes from each amendment were accepted, and then run all multirecord meaures.  A comparison of the multirecord measures from the pre-amendment phase with those from the post-amendment phase will quantify how much accepting the proposals from amendments would improve the data, with respect to the aspects measured by the tests.

Under Quality Assurance, MultiRecord measures that return COMPLETE/NOT_COMPLETE MAY be used as filters for quality for purpose, exclude records from the data set untill all MultiRecord measures of this sort are returning COMPLETE, this under the mathematical forumuation of the framework, is the assertion that the data are fit for the purpose of the selected UseCase.

Under Quality Control, MultiRecord measures that return numeric values MAY be used to assess the prevelance of quality issues in the data with respect to the selected UseCase.  

#### Test dependencies

Individual tests are designed to be as indepenent of each other as possible, but given the by design redundancies in Darwin Core, some amendments have potential interactions.

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

BDQ Core does not specify how these ordering of these tests should be accomplished.   This could be done by describing an Amendment with an expected response that specifies the execution of each of these tests in order.  Such a composition of Amendments would be the preferred method of sequencing under the framework, but to keep tests as granular a possible, and to allow the maxiumum flexibility for the composition of tests in Profiles to support UseCases, BDQ Core does not currently provide such tests.   Ordering could also could be done by providing a configuration file for a test execution framework specifying test dependencies.  Ordering could be supported in a workflow environment by composing a workflow to execute these tests in sequence.  

The bdqffdq: ontology does not include a property to describe sequence interdependencies among amendments.  

The bdqffdq: ontology provides terms: bdqffdq:targetedMeasure, bdqffdq:targetedValidation, bdqffdq:TargetedIssue, that could be used, together with bdqffdq:improvedBy to relate Amendments to Validations, Measures, and Issues.  BDQ Core does not, at this time, use these terms to describe test interrelationships.  

#### Implementing a concrete Test 



#### Presenting Darwin Core data to a method that implements a test.

One complexity introduced by the abstraction of tests into essentially APIs that take Darwin Core terms as input, and output Response objects is correctly mapping Darwin Core terms loaded in an execution framework onto the parameters of an implementation method.   Consider an implementation of VALIDATION_ENDDAYOFYEAR_INRANGE that has a method signature: 
    
    public Response validationEnddayofyearInrange(String startDayOfYear, String eventDate) 

If an implementation framework calls this method reversing the binding of dwc:startDayOfYear and dwc:eventDate as present in whatever structure is present in the framework, for example: 

    Response endDayTestResponse = validationEnddayofyearInrange(eventDate, startDayOfYear);

Then the test will not return the desired result, even if the implementation is correct.  Thus correct matching of input terms to the implementation of each test is critical. 

Multiple approaches are possible to correctly matching input Darwin Core terms onto method signatures for methods that implement tests. 

BDQ Core is entirely agnostic as to how this binding is done.  Implementors MAY freely implement in any appropriate way for their environment. However, test implementations MUST return structured Responses containing Response.status, Response.result, and Response.comment.   

In java, annotating method parameters and using reflection to bind between the execution framework and test implementations works well, here is a simplified code snippet from the FilteredPush event_date_qc library that uses java annotations, e.g. @ActedUpon(value="dwc:endDayOfYear") to provide metadata about which parameter goes with which Information Element. 

    public Response validationEnddayofyearInrange(
            @ActedUpon(value="dwc:endDayOfYear") String endDay,
            @Consulted(value="dwc:eventDate") String eventDate) {

An execution framework can use reflection to determine, from the annotations on the parameter, which Darwin Core term to bind to which parameter.

Additional metadata can be added in java annotations, here, from the FilteredPush event_date_qc library annotations enable an implementation framework to look a test implemenation by the test GUID, and can provide metadata about the test to users, and for maintinance, can be used to determine if an implementation is up to date with the latest version of a test specification.

    @Validation(label="VALIDATION_ENDDAYOFYEAR_INRANGE", description="Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?")
    @Provides("9a39d88c-7eee-46df-b32a-c109f9f81fb8")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8/2023-09-18")
    @Specification("INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is EMPTY or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is EMPTY or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT ")
    public static DQResponse<ComplianceValue> validationEnddayofyearInrange(
            @ActedUpon(value="dwc:endDayOfYear") String endDay,
            @Consulted(value="dwc:eventDate") String eventDate) {
        ....
    } 

This approach will only work with a subset of programming languages.  

In many languages, an domain object can be passed as a method parameter.  
    
    public Response validationEnddayofyearInrange(Event event) { 
        
    }

Here, both the execution framework and the internals of validationEnddayofyearInrange must be able to work with the Event (object or structure) and work with its Event.enddayofyear and Event.eventdate properties.

It is also possible to implement in an object oriented manner as methods on a class: 

    public class Event() { 

        private eventDate;
        private enddayofyear;

        public Response validationEnddayofyearInRange()...

    } 

Other approaches are possible.  Implementors MAY use any approach to passing data into test implementations appropriate for their language(s) and environment.

#### Implementing an abstract Test 

In some environments, implementations MAY be lightweight implementations of an abstract test.

Consider the validation: 

VALIDATION_ENDDAYOFYEAR_INRANGE

A SQL query that implements this abstract concept, that the enddayofyear is in range, could take the following form, using available database fields that contain data related to the abstract information element, but are not precicely mapped to the concrete specfied ActedUpon and Consulted Darwin Core terms in the specification.  This query produces a data quality report with: 

    SELECT collecting_event_id, enddayofyear,
         'VALIDATION_ENDDAYOFYEAR_INRANGE' as test, 'NOT_COMPLIANT' as response_result, 'RUN_HAS_RESULT' as response_status, 
         'The value of enddayofyear [' || enddayofyear ||'] is not an integer between 1 and 365 inclusive, or 366 if ended_date falls in a leap year.' as response_comment
    FROM collecting_event
    WHERE NOT ( 
          enddayofyear BETWEEN 1 AND 365
          OR (
             enddayofyear = 366
             AND 
             (
                 ( 
                   MOD(EXTRACT (year from TO_DATE(ended_date, 'yyyy-mm-dd')),4) = 0
                   AND
                   MOD(EXTRACT (year from TO_DATE(ended_date, 'yyyy-mm-dd')),100) != 0
                 )
                 OR
                 MOD(EXTRACT (year from TO_DATE(ended_date, 'yyyy-mm-dd')),400) = 0
             )
          )
        );


#### Example (non-normative)

Given the specification: 

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:SourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if the value of dwc:countryCode is found in bdq:sourceAuthority; otherwise NOT_COMPLIANT

Pseudocode for an implementation follows the sequence of RESPONSE,critera; of the specification, with external prerequisites being able to be thrown from anywhere within the logic, but handled within the construct that builds a Result object.

    Function validationCountrycodeNotempty(countryCode) returns Result {
      String sourceAuthority = "ISO 3166-1-alpha-2"
      Result result = new Result()
      try { 
          if (isEmpty(countryCode) { 
              result.setStatus(INTERNAL_PREREQUISITES_NOT_MET) 
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

## Presentation of Results

We are agnostic about how reports from BDQ Core can be reported, e.g. as aggregated results, on web pages for individual records, as spreadsheets of results with issues for quality control, etc.  

Reports SHOULD identify tests to consumers of those reports using at least the skos:prefLabel for the test class, e.g. VALIDATION_COUNTRY_FOUND.  

### Data Quality Reports

#### Example (non-normative)

Below is an example, taken from MCZbase, of a portion of a data quality report, run on demand, for a single specimen using an implementation of bdqcore tests integrated into that collection management system.

This example shows tests that were run, using the rdfs:comment on the bdqffdq:Validation to identify the action taken by the test to the collection management staff reading the report. Then in columsn for a pre-amendment phase, the result (Response.status or Response.result) of the test, and the Response.comment explaining why the test returned the result it did.  Below this report are listed any proposed changes from Amendments, then in the table, the result and comment from repeating the Validations in a post-amendment phase, treating the data as if the results of any amendments had been accepted (which is not done automatically, users must explicitly change the data if they want to accept the proposals from the Amendments).   In the presentation, COMPLIANT values are styled in green and NOT_COMPLIANT values in red.  A subset of the results are shown here (so compliant result percentages included values not shown).

** QC Taxon Name for MCZ:Herp:R-1440**

Results of the TDWG Biodiversity Data Quality IG TG2 Taxon Name related
tests.

Tests run using (mechanism): Kurator: Scientific Name Validator -
DwCSciNameDQ:v1.0.1.

Compliant Results Pre-amendment: 75%; Post-amendment: 94%

|                                                                                                                                                              |                                |                                                                                                                                                                                                                     |                       |                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Test                                                                                                                                                         | Pre-amendment Result           | Comment                                                                                                                                                                                                             | Post-Amendment Result | Comment                                                                                                                                                                                                                                                                                      |
| Is there a value in dwc:taxonRank?                                                                                                                           | **COMPLIANT**                  | Some value provided for taxonRank.                                                                                                                                                                                  | **COMPLIANT**         | Some value provided for taxonRank.                                                                                                                                                                                                                                                           |
| Is the combination of higher classification taxonomic terms consistent using GBIF?                                                                           | **COMPLIANT**                  | Genus Chelydra found in GBIF_BACKBONE_TAXONOMY\|Matches to higher ranks found in GBIF_BACKBONE_TAXONOMY\|No more higher ranks found to compare                                                                      | **COMPLIANT**         | Genus Chelydra found in GBIF_BACKBONE_TAXONOMY\|Matches to higher ranks found in GBIF_BACKBONE_TAXONOMY\|No more higher ranks found to compare                                                                                                                                               |
| Does the value of dwc:taxonRank occur in bdq:sourceAuthority?                                                                                                | **COMPLIANT**                  | Provided value for taxonRank \[species\] found in the GBIF taxon rank vocabulary.                                                                                                                                   | **COMPLIANT**         | Provided value for taxonRank \[species\] found in the GBIF taxon rank vocabulary.                                                                                                                                                                                                            |
| Is there a value in dwc:taxonID?                                                                                                                             | **NOT_COMPLIANT**              | No value provided for taxonID.                                                                                                                                                                                      | **COMPLIANT**         | Some value provided for taxonID.                                                                                                                                                                                                                                                             |
| dwc:scientificName contains a value                                                                                                                          | **COMPLIANT**                  | Some value provided for scientificName.                                                                                                                                                                             | **COMPLIANT**         | Some value provided for scientificName.                                                                                                                                                                                                                                                      |
| dwc:family is known to GBIF                                                                                                                                  | **COMPLIANT**                  | Exact match to provided Family found in GBIF backbone taxonomy at rank Family.                                                                                                                                      | **COMPLIANT**         | Exact match to provided Family found in GBIF backbone taxonomy at rank Family.                                                                                                                                                                                                               |
| dwc:genus is known to GBIF                                                                                                                                   | **COMPLIANT**                  | Exact match to provided genus found in GBIF backbone taxonomy as a genus.                                                                                                                                           | **COMPLIANT**         | Exact match to provided genus found in GBIF backbone taxonomy as a genus.                                                                                                                                                                                                                    |
| dwc:scientificName is known to GBIF                                                                                                                          | **COMPLIANT**                  | Exact Match found for \[Chelydra serpentina (Linnaeus, 1758)\] to \[https://www.gbif.org/species/2441905\]                                                                                                          | **COMPLIANT**         | Exact Match found for \[Chelydra serpentina (Linnaeus, 1758)\] to \[https://www.gbif.org/species/2441905\]                                                                                                                                                                                   |
| Can the taxon be unambiguously resolved from GBIF using the available taxon terms?                                                                           | **NOT_COMPLIANT**              | Provided taxon \[:Animalia:Chordata:Reptilia:Testudinata:Chelydridae:Chelydra:Chelydra serpentina (Linnaeus, 1758):(Linnaeus, 1758):Chelydra:\]\|No exact match found for provided taxon in GBIF_BACKBONE_TAXONOMY. | **COMPLIANT**         | Provided taxon \[urn:lsid:marinespecies.org:taxname:1378193:Animalia:Chordata:Reptilia:Testudinata:Chelydridae:Chelydra:Chelydra serpentina (Linnaeus, 1758):(Linnaeus, 1758):Chelydra:\]\|Exact match to provided taxonID found in WORMS, matching the provided value of dwc:scientificName |
| Does the value of dwc:taxonID contain a complete identifier?                                                                                                 | INTERNAL_PREREQUISITES_NOT_MET | No value provided for taxonId.                                                                                                                                                                                      | **COMPLIANT**         | Provided taxonID recognized as an LSID.                                                                                                                                                                                                                                                      |

** Proposed Amendments **

-   lookup taxonID for taxon FILLED_IN
    > **{dwc:taxonID=urn:lsid:marinespecies.org:taxname:1378193}**
    > Provided taxon
    > \[:Animalia:Chordata:Reptilia:Testudinata:Chelydridae:Chelydra:Chelydra
    > serpentina (Linnaeus, 1758):(Linnaeus, 1758):Chelydra:\]\|1
    > potential matches returned from authority.\|Match for provided
    > taxon in WORMS with exact match on authorship. \|Exact match to
    > provided taxon found in WORMS.


### Annotations

The bdqffdq: owl framework, and the framing of the tests in bdqcore: as rdf using that ontology makes, by design, tests results particularly amenable to being wrapped in annotations following the W3C Web Annotation Data Model (Sanderson et al. 2017). 

The results could be structured as components that can be wrapped in the body annotation document along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.


## 5 Validating Test Implementations (normative)

Implementors of tests SHOULD validate the behaviour of the internals of their test implementations with unit tests, and MUST validate that each test implementation is capable of taking relevant input from a set of standard test validation data, and returning the expected responses.

If validation data could be conflated with actual data, see: [Identifying Synthetic and Example Data](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/synthetic/index.md)

### 5.1 Introduction (non-normative)

Accompanying the Core test descriptors is a set of test validation data.  This test validation data is intended for implementors to use to evaluate whether or not their test implementations produced the expected Response values for a set of cases for each test.  Each test specification could be graphed as a flow chart with several paths, the test validation data are intended to cover each node and each path within each test specification with at least a single case.  These are not exhaustive unit tests covering large numbers of edge cases, but rather a minimal set of tests for expected behaviour.  

The test validation data are organized as two flat CSV files.  Each row in each file is intended for a single validation of a single test.  The file has columns identifying the validation case, the test that the row is intended to validate, the expected Response.status, Response.value, an example Response.comment, parameter values, if any, and a set of Darwin Core terms (most of which are empty for a given test).   

The test validation records are all fragmentary flat Darwin Core Occurrence records.  Each row contains values for only those Darwin Core terms that are relevant input to the particular validation.   The validation records are all fragmentary, consisting of a mixture of real and artificial data with most of the records being synthetic.  The validation data are a set of 1191 records, with about 10 validation cases for each test.  The set of rows for a particular test are designed to validate that an implementation of that particular test performs as expected against the specifications.   This data set is referred to as the 'Test Validation Data'.   The set of about 10 validation records for each test are designed to exercise all of the decision pathways in the specification of the test.  

This is a minimalist suite of test data. Additional test records can be readily generated or adapted from real data using the following template based on the specifications below. In consideration of the community, the DataID values MUST uniquely identify a validation case for each additional test data record and the resulting data added to the GitHub repository.

###  Considerations Concerning Input Data Values for AMENDMENTS

TODO: Move this section to supplementary.

One of the early conclusions to this project was the need for controlled vocabularies and an early spin-off of Data Qality Task Group 4 on Vocabularies (https://github.com/tdwg/bdq/tree/master/tg4). Testing the 'quality' or 'fitness for use' of Darwin Core encoded data is made more difficult due to the lack of a comprehensive suite of controlled vocabularies.

Testing Darwin Core values against a known Source Authority using a VALIDATION type test is straight forward: A test is either COMPLIANT or NOT COMPLIANT. This standard includes tests of type AMENDMENT and the mapping of input Darwin Core values to known Vocabulary values is poorly developed. If a VALIDATION returns COMPLIANT, no AMENDMENT is necessary. For example, if the input value to a test is say dwc:sex="Female", then no AMENDMENT is required. If however, the input value is dwc:sex:f., can this be interpreted as "Female"? Probably. What about dwc:sex="M"? This could be "Male" or "Mixed" according to https://api.gbif.org/v1/vocabularies/Sex/concepts. <!--- Ming: I asked GBIF about this specific example and they said that "M" will be matched to Male, but I am not sure how the API works exactly ---><!--- PJM: the rec_occur_qc implementation uses the vocabulary directly, finds, ^M matches male and mixed, so asserts that it can't make the amendment, I can't speak about the (by our test specification, incorrect) actions that gbif is taking on their vocabulary, their API delivers the vocabulary, but doesn't do this sort of matching, so what they are describing is some internal that uses the vocabulary --->

A key phrase within this standard that particularly relates to many of the Expected Responses of tests is " dwc:term can be unambiguously interpreted as ...". In the case above for dwc:sex="M", the determination is that it is ambiguous. In this case, no AMENDMENT can be made.

When carrying out Amendments where numeric vales are concerned (e.g. feet to meters, etc.) the principle of reversability is paramount, and thus rounding up or down or using approximations should be avoided and only exact values used.

We see an urgent need for a comprehensive, internationally agreed list of Darwin Core (https://dwc.tdwg.org/) term values that are mapped to standard values. GBIF has implemented some unique values, for example https://api.gbif.org/v1/vocabularies/Sex/concepts/Female/hiddenLabels, but such lists are not comprehensive. While there has been a survey of Darwin Core 'distinct' values for GBIF, ALA, iDigBio and VertNet, these are both dated, and where possible, have not been mapped to standard values, if they exist.

In this standard, we have taken an expedient approach in relation to making AMENDMENTs. We have used code in our tests to try and parse out likely, unambiguous matches. This is far from an ideal solution, but it does provide the potential of our AMENDMENTs to 'value add' to Darwin Core data records.

### Structure of the Validation Data 

The validation data are intended as input into a testing system that can implementations of validation tests independently, presenting them with a validation case for input, and assessing whether the test Response conforms to the expected values in the validation data.  It could be processed as input for unit tests.   It could be used as the basis for presenting synthetic records to a larger test execution system, but is designed to be used at a level where individual tests are being assessed.  This may fit into integration tests of a larger system.  The structure of the validation data attempts to be at a level of abstraction somewhat above the method signature specificity needed in unit tests, but still at a level that is examining individual test implementations, below the level of testing inputs and outputs of a larger data processing system that could take complete Darwin Core records as input and return rich data quality reports as output (to avoid forcing particular formats on data quality reports as a whole).  

<!--- Start: PJM Added the terms from "bdqValidationData" glossary terms 2024 Aug 24 --->

The following column header for the data are used for the validation data files.

| header | definition |
| ------ | ---------- |
| dataID | A local to the validation data unique integer to indentify each Validation Data record | 
| LineForTest | A local to bdq:ValidationData identifier for test records within one test. An integer for maintaining the sort order of the validation case with in the set of validation cases for a particular test. | 
| LineNumber | The sequence number of the data record in the bdq:ValidationData. An integer for maintaining the sort order of the file. |

<!--- End: PJM Added the terms from "bdqValidationData" glossary terms 2024 Aug 24 --->

<!--- TODO: consistent format with list below, which describes each header and is what is needed here --->

* Line Number: An integer for maintaining the sort order of the file.
* dataID: A unique identifier (within the validation data) of the validation data record, e.g., "123"
* LineForTest: An integer for maintaining the sort order of the validation case with in the set of validation cases for a particular test,
* GitHubIssueNo: The GitHub issue where rationale management of the test under validation is maintained, can be use to form a link to the discussion history for the development of the relevant test, e.g., 20 can be found at https://github.com/tdwg/bdq/issues/20
* GUID: the machine readable identifier for the test under validation, e.g. 69b2efdc-6269-45a4-aecb-4cb99c2ae134
* Label: The human-readable name of the test, e.g., "VALIDATION_COUNTRY_FOUND"
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


### Examples of the data for validating tests (Informative)

The validation files contain one column for each of 77 Darwin Core terms that are referenced as an Information Element somewhere in Core, but only terms relevant to the particular validation case for the row are populated, therefore the validation files are sparse.  They contain fragments of Flat Darwin Core records. 

The header line for each of the validation files:  

"LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Response.status","Response.result","Response.comment","IssuesWithThisRow","bdq:annotation","bdq:sourceAuthority","dc:type","dcterms:license","dwc:acceptedNameUsageID","dwc:basisOfRecord","dwc:class","dwc:continent","dwc:coordinateUncertaintyInMeters","dwc:country","dwc:countryCode","dwc:county","dwc:dataGeneralizations","dwc:dateIdentified","dwc:day","dwc:decimalLatitude","dwc:decimalLongitude","dwc:endDayOfYear","dwc:establishmentMeans","dwc:eventDate","dwc:family","dwc:genus","dwc:geodeticDatum","dwc:higherClassification","dwc:higherGeography","dwc:higherGeographyID","dwc:infraspecificEpithet","dwc:island","dwc:islandGroup","dwc:kingdom","dwc:locality","dwc:locationID","dwc:maximumDepthInMeters","dwc:maximumElevationInMeters","dwc:minimumDepthInMeters","dwc:minimumElevationInMeters","dwc:month","dwc:municipality","dwc:occurrenceID","dwc:occurrenceStatus","dwc:order","dwc:originalNameUsageID","dwc:parentNameUsageID","dwc:phylum","dwc:scientificName","dwc:scientificNameAuthorship","dwc:scientificNameID","dwc:specificEpithet","dwc:startDayOfYear","dwc:stateProvince","dwc:subgenus","dwc:taxon","dwc:taxonConceptID","dwc:taxonID","dwc:taxonRank","dwc:verbatimCoordinateSystem","dwc:verbatimCoordinates","dwc:verbatimDepth","dwc:verbatimElevation","dwc:verbatimEventDate","dwc:verbatimLatitude","dwc:verbatimLocality","dwc:verbatimLongitude","dwc:verbatimSRS","dwc:vernacularName","dwc:waterBody","dwc:year","dwc:subfamily","dwc:superfamily","dwc:tribe","dwc:subtribe","dwc:genericName","dwc:infragenericEpithet","dwc:cultivarEpithet","dwc:individualCount","dwc:organismQuantity","dwc:footprintWKT","dwc:coordinatePrecision","dwc:namePublishedInYear","dwc:sex","dwc:typeStatus","dwc:pathway","dwc:degreeOfEstablishment","bdq:taxonIsMarine","bdq:geospatialLand","bdq:assumptionOnUnknownBiome","bdq:latestValidDate","bdq:earliestValidDate"

The data are sparse, as most dwc: term columns do not contain a value for each individual case.

A validation test case evaluating empty, where no dwc: term columns contain a value (dataID=1):  

"2","1","1","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","INTERNAL_PREREQUISITES_NOT_MET","","dwc:countryCode is EMPTY","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation test case for a validation where the input data result in a Response.value of NOT_COMPLIANT (dataID=7)

"8","7","7","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","NOT_COMPLIANT","dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value ","","","","","","","","","","","","Austria","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation test case for a validation where the input data result in a Response.value of COMPLIANT (dataID=8)

"9","8","8","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","COMPLIANT","dwc countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value","","","","","","","","","","","","US","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

### Where to get the validation data (non-normative)

The validation data is in two files, one containing normal data values, the other containing validation cases using non-printing characters.

1. [TG2_test_validation_data.csv](TG2_test_validation_data.csv)
2. [TG2_test_validation_data_nonprintingchars.csv](TG2_test_validation_data_nonprintingchars.csv)

Validation file containing data values that would be expected to be encountered in the wild: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data.csv

Validation data file containing non-printing characters for testing implementation of EMPTY: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data_nonprintingchars.csv

This file is a csv file with the same set of columns as the above, but with rows that contain input values for selected Darwin Core terms consisting of either the 0x00 null character (e.g. dwc:scientificName="0x00"), or a pair of ASCII control characters (shift out 0x0E and shift in 0x0F, e.g. dwc:day="0x0E0x0F"). This file is intended to validate that implementations of tests are consistently evaluating inputs as EMPTY as expected by the definition of EMPTY.  

The non-printing characters file MUST only be edited with a tool that will maintain the non-printing characters.  

Both files have a header line identifying the specifications as defined in Section 6.2.

The expectation for the response that an implementation should produce when executed against the row: "Response.status","Response.result","Response.comment", where an implementation is expected to produce the exact Response.status, the exact Response.result (ignoring order of any key-value pairs for an amendment response), and Response.comment is an example of what a comment, in English, might look like.  

Parameter values are specified in a bdq:sourceAuthority column, when more than one sourceAuthority is involved, then these are given separate names.

Darwin Core input columns are specified as "dc:type","dcterms:license","dwc:acceptedNameUsageID",...
