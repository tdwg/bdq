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

## 1 Introduction (non-normative)

This document provides guidance for those wishing to create sofware implementations (bdqffdq:Mechanism) of BDQ Core tests.

## 1.1 Independence (normative) 

Test implementations SHOULD be independent of how data are stored and transported, data serializations, and the framework or environment in which the tests are being executed.   

## 2 About the Tests and their Implementation


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

In BDQ Core, bdq:Empty is used to evaluate bdqffdq:InformationElements within a test specification, it therefore means empty if the data set being evaluated does not contain the term matching the information element, or if the data set contains that term but the value for that term is empty.   This is to allow the application programing interface expressed by the test bdqffdq:DataQualityNeed to be agnostic about the strucuture presented to a framework for executing the tests. 

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

#### 2.2.1 Key Parts of a descriptor

- termLocalName
- skos:prefLabel
- specification - expected response
- specification - authorities/defaults
- information elements
- parameters

#### 2.2.2 Reading a Specification

A specification consists of a sequence of RESPONSE, criteria; with a few AMENDMENTS that can propose values for multiple terms having a sequence of options within the criteria.  When reading a Specification, implementors SHOULD read each Response in sequence, evaluating each of the criteria in sequence, and returning the first response that for which the specified criteria are met.  An exception to this is that the placement of EXTERNAL_PREREQUISITES_NOT_MET as the first RESPONSE in the Specification does not imply that the responsiveness of an external resource should be assessed first.  Implementors MAY handle failure of an external resource in any appropriate manner, for example, with exception handling.

Responses in a Specification are expressed in an abbreviated form for readability by implementors.

EXTERNAL_PREREQUISITES_NOT_MET means Response.status=EXTERNAL_PREREQUISITES_NOT_MET, Response.value=null, Response.comment={some non-null description of the failure condition}

INTERNAL_PREREQUISITES_NOT_MET means Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.value=null, Response.comment={some non-null description of the failure condition}.

COMPLIANT means Response.status=RUN_HAS_RESULT, Response.value=COMPLIANT, Response.comment={some non-null description of the failure condition}.

etc.

| Concept | bdqffdq Term(s) | Description |
| ------- | ------- | ----------- |
| Response | bdqffdq:Assertion | The report from a single execution of a single test, consisting of a bdq:Response.status, a bdq:Response.result, a bdq:Response.comment, and optionally, a bdq:Response.qualifier.| 
| Response.status | bdqffdq:ResponseStatus, bdqffdq:hasResponseStatus | A metadata element in a bdq:Response indicating whether a particular test (bdqffdq:Validation, bdqffdq:Amendment, bdqffdq:Measure, or bdqffdq:Issue) was able to be performed or not.| 
| Response.result | bdqffdq:ResponseResult, bdqffdq:hasResponseResult, bdqffdq:hasResponseResultValue | The element in a bdq:Response containing the value returned by a test (bdqffdq:Validation, bdqffdq:Amendment, bdqffdq:Measure, or bdqffdq:Issue)|
| Response.comment | bdqffdq:hasResponseComment | A human readable interpretation of the results of the test.|
| Response.qualifier | bdqffdq:ResponseQualifier, bdqffdq:hasResponseQualifier | Additional structured information that qualifies the bdq:Response, intended as an extension point for uncertainty.|



#### 2.2.3 Interpreted As

In the Specifications the phrase "interpreted as" means for Implementors, (1) where Darwin Core data are serialized as strings, but the test refers to data as numeric or other non-string data type, can the string value be parsed into the target data type in the language of implementation (e.g., "1" as the integer 1), (2) matching a representation of a value unambiguously onto a controlled vocabulary (e.g., ‘WGS84’ to ’EPSG:4326’), or (3) interpreting the representation of a numeric value (e.g., a roman numeral) as a number (e.g., an integer).


## 3 Compliant Implementation (normative)

In order to be considered as compliant with this standard, an implementation MUST meet the requirements of this section.   

We view the most important elements of this standard as being the structure that holds explicit descriptions of what a data quality test is intended to do, along with the consistent structure for reporting the results from the execution of a test upon some data.  We expect that implementors will implement sets of these tests that fit their data quality needs, and will also implement other tests.  The CORE tests provide a coherent library of tests that can be applied to the set of defined UseCases, and considerable thought has gone into describing tests that isolate particular data quality issues, and that work together as a conherent suite.   

An implementation MUST include all bdqcore: SingleRecord Validations, Amendments, and Measures for each implemented UseCase.  An Implementation MUST provide an implementation for at least one UseCase, and MAY provide implementations for more or all of the UseCases.   Implementations MAY include additional tests and additional UseCases.

Results from each test MUST be produced in the form Response.status, Response.result, and Response.comment, with one test producing one Response.   Results MAY include Response.qualifier (See 4 Extension Points).  The values of Response.status and Response.result MUST be those specified.   This standard is agnostic concerning data structures and serializations of a Response. The standard is agnostic concerning internationalization and languages of labels applied to human readable presentations of values within a Response.

Where implementors add additional tests as part of a test suite compliant with this standard, they MUST describe those tests using the bdqffdq framework, those tests MUST use the same Response structures, and those tests MUST be related to UseCases (either those defined in the standard or additional use cases).  

The standard is agnostic as to how data are presented and piped within some framework to and from test implementations.  An implementation framework MAY present SingleRecords to tests and report results, or an implementation MAY find unique values for InformationElements, execute test implementations on those unique values, and then map the results back onto SingleRecord reports, or an implementation MAY operate on data in other ways.

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, Repeated in 1.7 --->

For each core SingleRecord Validation, an implementation intended for Quality Control SHOULD include a corresponding MultiRecord Measure that counts the number of Response.result values that are COMPLIANT.  An implementation MAY provide similar MultiRecord Measures that report aggregated counts of other Response.status and Response.value values.  

For each core SingleRecord Validation, an implementation intended for Quality Assurance SHOULD include a corresponding MultiRecord Measure that returns COMPLETE when all pertenent Response.result values are COMPLIANT (or for some Measures also INTERNAL_PREREQUSISITES_NOT_MET).

Implementations MUST provide implementations of parameterized tests that support the default parameter values. Implementations SHOULD provide for parameterized tests to take parameters, but MAY produce an implementation of a parameterized test that takes no parameters but only uses the default parameter value.

How a test responds when given a parameter value that is not supported by the implementation is not specified. Implementers SHOULD handle this in a manner appropriate for their implementation framework. Unless specified in the Specification, implementations MUST_NOT use Response.status=EXTERNAL_PREREQUISITES_NOT_MET to indicate a non-supported parameter value.

Implementors are free to, and are encouraged to, in addition to framework compliant implementations, produce means of testing data quality in bulk in settings such as SQL queries on relational data stores where construction of Response objects is not feasable, but the logic of a Specification can be framed as a question on a data store.  Such non-framework implementations MUST NOT assert compliance with this standard.

Within the Response.result for an Amendment, the order of key-value pairs is not specified and MAY vary.

### 4 Extension points (normative)

A response MAY include a Response.qualifier.  This is intended as a place to include structured assertions concerning uncertainty in a response.  This is also intended as a place to include structured assertions about the details of Ammendments (e.g. TRANSPOSED MAY be attached to a Response.qualifier for some Amendments).

<!--- Bit about ActedUpon/Consulted Needs to move, we have added these to the test descriptors and the framework --->

Implementations MAY identify InformationElements as ActedUpon or Consulted. Presentations of data quality results may use ActedUpon and Consulted identification of Information Elements to identify to users which specific values assertions are being made about, and what values are being used to support those assertions. ActedUpon information elements are those for which a Validation is asserting compliance/non-compliance, or an Amendment is proposing a change. Consulted information elements are those which inform such decisions, but are not themselves the subject of the decision. For example, in AMENDMENT_EVENTDATE_FROM_VERBATIM, the InformationElement dwc:eventDate is ActedUpon, while the InformationElement dwc:verbatimEventDate is Consulted. We do not  identify Information Elements as ActedUpon or Consulted here, but implementers may wish to do so to more clearly represent to consumers of data quality reports (particularly data quality reports in the form of spreadsheets), which terms are particular tests are making assertions about.

Tests MAY specify that information elements are ActedUpon or Consulted. We do not do so here, but ActedUpon and Consulted properties of an Information Element are an extension point that may be included when specifying the Information Elements pertinent to a test

MultiRecord Measues that return counts where the input InformationElement is Response values from tests on SingleRecords MUST report only a single count as the Response.value, but can provide a Response.qualifier containing structured data describing additional information such as the total number of SingleRecords evaluated (to calculate percents), the number of each value of Response.status encountered, and the number of each Response.value encountered.  Measures under the framework are only allowed to return COMPLETE/NOT_COMPLETE, or a single number, if it is desirable for any Measure to return more than a single number, Response.qualifier is the extension point to use for this. 

## 3 Responses from tests

### 3.1 The Response Object (normative) 

The four test types, Validation, Issue, Amendment, and Measure all provide a Response from the execution of the test.
The Response from a test is an assertion which MAY form part of a data quality report or MAY be wrapped in an annotation. 

Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags. 

The Response MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary consisting of exactly COMPLIANT or NOT_COMPLIANT for Validations, NOT_ISSUE, POTENTIAL_ISSUE or ISSUE for Issues, either a numeric value or a controlled vocabulary consisting of COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments.

2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 

3. The Remark supplies human-readable text describing reasons for the test result output.

An Amendment may propose a change to an exisitng Darwin Core value or a set of Darwin Core terms or fill in a missing value. Amendments are intended to improve one or more components of the quality of the record.  The Response.result from an Amendment MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  The Framework also supports changes to procedures but we have not framed any such tests in this form.  

An Amendment Response.result SHOULD consist of a set of key:value pairs, where the key is the information element to be modified, and the value is the proposed new value for that information element.   The Response.result key:value pairs SHOULD be a JSON serialization of the proposed changes.

Under bdqffdq: Amendments may propose changes to processes as well as data, no structure is proposed for such an Amendment Response.result, and implementors MAY develop their own structures and serialisations for such Amendment Response.results.

### 3.2 Framework elements not included in bdqcore test descriptions (normative)

Implementors SHOULD create an instance of bdqffdq:Mechanism to uniquely identify their suite of test implementations.

Implementations producing data quality reports SHOULD create instances of bdqffdq:Assertions grouped in bdqffdq:DataQualityReports that also specify the bdqffdq:DataResource that the bdqffdq:DataQualityReport concerns.

Implementors MUST provide bdq:Response data in data quality reports consisting of bdq:Response.status, bdq:Response.result, and bdq:Response.comment.  

Implementations MAY perform data Quality Control, data Quality Assurance, or both.  

## 4 Guidelines for Implementers

### Parameters and changing the behavior of a test (normative)

Many tests specify bdqffdq:Parameters in addition to bdqffdq:InformationElements.  Parameters are intended to change the behavior of a test to fit local data quality needs without changing the specification of the test.  

A parameterized test will behave differently on the same data when given different parameter values. 

Implementors SHOULD only present non-default parameter values to a test implementation if needed for local data quality needs.

Implemenentors MUST NOT produce test implementations identified by the same identifiers that only implement non-default parameter values.  An implementation of a test MUST support the test execution with the default parameter values, and MAY optionally support other parameter values.   Provided parameters MUST NOT change the behavior of the test to depart from the bdqffdq:Specification.expectedResponse.  Parameters MUST only change the behavior of the test as specified in the bdqffdq:Specification.expectedResponse.

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


<!--- Ming: Execution sequence of the tests , repeated in 1.6, but more detail than 1.6 --->

A good practice for executing the tests is to execute all of the validations and measures in a pre-amendment phase, then to execute all of the amendments in an amendment phase, then to execute all of the validations again on the data with the proposed changes from the amendments applied to the data in a post-amendment phase. Such a sequence of phases allows assertions to be made about the quality of the data as they were initially presented, and how much the quality of the data would be improved if the amendments were accepted. Within pre-amendment and post-amendment phases, the validations and measures are agnostic about the order in which they are run, the extent to which they are run in parallel, or the extent to which they are run on single records or on unique values within a data set. One possible workflow for tests is to aggregate the unique values of applicable Information Elements within a bdqffdq:MultiRecord for each Validation or Measure, then to execute the Validation or Measure on just the unique values, then de-aggregate the results back to each bdqffdq:SingleRecord. This is analogous to implementing tests as SQL queries.

#### Test dependencies

Individual tests are designed to be as indepenent of each other as possible, but given the by design redundancies in Darwin Core, some amendments have potential interactions.

The tests are agnostic to the framework within which they are run. The tests are largely agnostic to the extent to which they are run in parallel and the sequence in which particular tests are run. An exception is certain of the amendments, where the order of execution can be important.

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

#### Example test implementation (non-normative)

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

Note that this implementation will reach the block that can return EXTERNAL_PREREQUISITES_NOT_MET only if the input countryCode contains a value.  This deviation from the logical sequence implied by the Specification (EXTERNAL_PREREQUISITES_NOT_MET if the bdq:SourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY;) is perfectly acceptable, for the case of network resources being evaluated later in the implementation than other conditions.

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

#### Implementing a test in a specific environment

Given data stored in a known and controlled environment, test implementations can be specifically tailored to that environment, both in language and in assumptions about formats and data types. 

Consider the validation: 

VALIDATION_ENDDAYOFYEAR_INRANGE

With the specification "INTERNAL_PREREQUISITES_NOT_MET if dwc:day is EMPTY; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT."

Given a hypothetical Event table with fields including a primary key event_id and an integer field day, an implementation of VALIDATION_DAY_STANDARD in SQL that operates on data in the aggregate might look like:

    SELECT
        ‘VALIDATION_DAY_STANDARD’ as test name, 
        event_id,
        ‘INTERNAL_PREREQUISITES_NOT_MET’ as Result_status, 
        null as Result_value,
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

This implementation is dependent on the schema the data is stored in, in particular, the definition of event.day as a field holding integers.  

This implementation does not generalize, as for example, day in a numeric data type that supports numbers in addition to integers would return incorrect values (per the test specification, which requires day to be an integer), for values of day such as "8.5"

Implementations should carefully consider the assumptions inherent in the environment on which tests are being run.  For example, the FilteredPush implementations in event_date_qc, sci_name_qc, rec_occur_qc, and geo_ref_qc, expect that all data will be presented to the test methods as strings.  Therefore each test implementation that deals with numeric values must convert the input strings to appropriate numeric types for evaluation (and can use the failure to convert the data type as a means to identify internal prerequisites not met).

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


### Annotations (normative)

The bdqffdq: owl framework, and the framing of the tests in bdqcore: as rdf using that ontology makes, by design, tests results particularly amenable to being wrapped in annotations following the W3C Web Annotation Data Model (Sanderson et al. 2017). 

Test responses MAY be represented as annotations.

The responses from tests could be structured as elements that can be wrapped in the body annotation document along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.

When test responses are being returned as annotations, they SHOULD use the W3C Web Annotation Data Model for the annotations, and SHOULD place test responses within the body of the annotation.  Such annotations SHOULD include reference to the source test by the versioned fully qualified name of the test (e.g. bdqcore:47ff73ba-0028-4f79-9ce1-ee7008d66498/2023-09-18) and the test skos:prefLabel (e.g. VALIDATION_DAY_STANDARD).  Such annotations SHOULD also provide the bdqffdq:Mechanism that generated the test response. 

## 5 Validating Test Implementations (normative)

Implementors of tests SHOULD validate the behaviour of the internals of their test implementations with unit tests, and MUST validate that each test implementation is capable of taking relevant input from a set of standard test validation data, and returning the expected responses.

If validation data could be conflated with actual data, see: [Identifying Synthetic and Example Data](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/synthetic/index.md)

### 5.1 Introduction (non-normative)

Accompanying the Core test descriptors is a set of test validation data.  This test validation data is intended for implementors to use to evaluate whether or not their test implementations produced the expected Response values for a set of cases for each test.  Each test specification could be graphed as a flow chart with several paths, the test validation data are intended to cover each node and each path within each test specification with at least a single case.  These are not exhaustive unit tests covering large numbers of edge cases, but rather a minimal set of tests for expected behaviour.  

The test validation data are organized as two flat CSV files.  Each row in each file is intended for a single validation of a single test.  The file has columns identifying the validation case, the test that the row is intended to validate, the expected Response.status, Response.value, an example Response.comment, parameter values, if any, and a set of Darwin Core terms (most of which are empty for a given test).   

The test validation records are all fragmentary flat Darwin Core Occurrence records.  Each row contains values for only those Darwin Core terms that are relevant input to the particular validation.   The validation records are all fragmentary, consisting of a mixture of real and artificial data with most of the records being synthetic.  The validation data are a set of 1191 records, with about 10 validation cases for each test.  The set of rows for a particular test are designed to validate that an implementation of that particular test performs as expected against the specifications.   This data set is referred to as the 'Test Validation Data'.   The set of about 10 validation records for each test are designed to exercise all of the decision pathways in the specification of the test.  

This is a minimalist suite of test data. Additional test records can be readily generated or adapted from real data using the following template based on the specifications below. In consideration of the community, the DataID values MUST uniquely identify a validation case for each additional test data record and the resulting data added to the GitHub repository.

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

### Implementation and the validation data (normative)

Implementations SHOULD provide support for each parameter value specified in the example data. 

Implementations MUST produce structured Response values with a Response.status, Response.value, and Response.comment.  

In order to be considered as compliant with this standard, an implementation of the Core tests MUST fulfill all of the REQUIRED elements of this section.

Human readable Data Quality Reports for Quality Control MAY take any appropriate form, they MAY aggregate Response values and comments, they MAY present results organized by test, or by data record, or by frequency of problem, or any other form suitable for presentation.  Data Quality Reports for Quality Control SHOULD allow users to access individual Response.status Response.value Response.comment results.  

Response.comment values SHOULD be internationalized as appropriate for the the consumers of data quality reports.  

Response.status and Response.value constants SHOULD be given internationalized labels as appropriate for the the consumers of data quality reports.  

For each test in an implementation, that test MUST produce the same results as are specified in a row of the validation data for that test, except when a bdq:sourceAuthority parameter specifies a web service other than the default sourceAuthority specified for that test.


