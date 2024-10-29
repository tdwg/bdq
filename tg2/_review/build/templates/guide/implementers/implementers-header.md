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

Authors
: {authors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}


### Table of Contents ###

{toc}

## 1 Introduction (non-normative)

### 1.1 Purpose

This document provides guidance for those wishing to create sofware implementations (bdqffdq:Mechanism) of the BDQ Core Tests.

### 1.2 Audience

This document is for software developers needing a technical understanding of the BDQ Core Tests.

### 1.3 Associated Documents

- [BDQ Core Tests Quick Reference Guide](../../terms/bdqcore/index.md)
- [BDQ Core Vocabularies](../../vocabularies/index.md)
- [BDQ Core User's Guide](../users/index.md)

### 1.4 Status of the Content of this document

Section 1 is non-normative. Other sections are marked as normative or non-normative.

### 1.5 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace Abbreviations

The following namespace abbreviations are used in this document:

| **Prefix**   | **Namespace**                                    |
|--------------|--------------------------------------------------|
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

## 2 About the Tests and their Implementation

### 2.1 Independence (normative) 

Test implementations SHOULD be independent of how data are stored and transported, data serializations, and the framework or environment in which the Tests are being executed.   

### 2.2 The Concept of "EMPTY" in BDQ Core (normative)

Empty and NotEmpty in the context of BDQ Core are defined as follows: 

<!--- Load definition of Empty and NotEmpty from bdq vocabulary here into template --->

| term | definition |
| ---  | ---------- |
| bdq:Empty | An evaluation of a value, that in the context of the evaluation, returns true if the value does not contain any characters or values other than those in the range U+0000 to U+0020, otherwise returns false. |
| bdq:NotEmpty |An evaluation of a value, that in the context of the evaluation, returns false if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns true. |

<!--- end load --->

Data that has passed through arbitrary serializations and transformations can contain anomalies. bdq:Empty is defined to allow Tests to clearly separate concerns.  An Information Element containing invalid characters, (e.g. letters in an information element that would be expected to contain integers) or values (including string serializations of the NULL value) are bdq:NotEmpty and are the concern of Tests that evaluate bdqdim:Conformance.  Presence or absence of data is a concern for Tests evaluating bdqdim:Completeness.  

A bdqffdq:InformationElement containing invalid characters (e.g. letters in an information element that would be expected to contain integers) or values (including string serializations of the NULL value) are bdq:NotEmpty, identifying that they are invalid is a concern of other Tests evaluating bdqdim:Completeness.

#### 2.2.1 The Concept of Empty (normative)

(1) Spaces, tabs, and other non-printing characters, are treated as bdq:Empty.

Objects that are null, or null values in a relational database, at the point of Test execution, MUST be treated as bdq:Empty.

(2) Serializations of NULL, treated as bdq:NotEmpty.

Data serialized from relational database systems may contain string representations of NULL.

We considered, and explicitly rejected, treating common string serializations of null such as "&#92;N" and "NULL" as empty values.  String serializations of NULL outside of a database, present at the point of evaluation of a Test, MUST be treated as bdq:NotEmpty.  A Test execution environment MAY deserialize these string serializations of NULL

(3) Data values indicating an unknown, treated as bdq:NotEmpty.

The definition of bdq:Empty is not applicable to a discussion of what value to include in a controlled vocabulary to indicate that no meaningful value is present, so no suggestion is made that "EMPTY" should be used as a data value to represent some form of "Null", "Unknown", "Not Recorded", etc. Choices there would fall into the semantics for some set of controlled vocabularies. The relevance to such a discussion is that this definition would treat an empty string as an empty value, with no semantics attached as to why the value is empty.

(4) Independence of Tests from the execution framework. 

The evaluation of bdq:Empty MUST be at the point of evaluation of the Test.  This allows the Tests to be independent of data serializations for transport and the representation of data in Test execution environments. 

In BDQ Core, bdq:Empty is used to evaluate bdqffdq:InformationElements within a Test specification, it therefore means empty if the data set being evaluated does not contain the term matching the information element, or if the data set contains that term but the value for that term is empty.   This is to allow the application programing interface expressed by the Test bdqffdq:DataQualityNeed to be agnostic about the strucuture presented to a framework for executing the Tests. 

For csv data, a column is either there or not in a data set, but in an rdf representation, some data objects could have relevant properties and others not - and the Tests are independent of that.

#### 2.2.2 Example implementation of a Function to Assess Empty (non-normative)

Here is a Java function to evaluate Empty, using trim() to exclude U+0020 (space), U+000A (LF), U+000D (CR) and the other non-printing characters in the unicode range U+0000 to U+0020, and also evaluating null as Empty.  Test implementations can reuse a function like this for Tests that evaluate bdq:Empty in their specification.

    public boolean isEmpty(String aString)  {
        boolean result = true;
        if (aString != null && aString.trim().length()>0) { 
            result = false;
        }
        return result;
    }

Here is a MariaDB implementation of a lightweight version of [VALIDATION_KINGDOM_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/36ed36c9-b1a7-40b2-b5e2-0d012e772098) that provides a list of NOT_COMPLIANT records for some flat taxonomy table in a database, again handing off the resposibility for evaluation of non-printing characters to the trim function available in the language.

    SELECT taxonomy_id, kingdom,
         'VALIDATION_KINGDOM_NOTEMPTY' as test, 'NOT_COMPLIANT' as response_result, 'RUN_HAS_RESULT' as response_status,
         'The value of kingdom is Empty.' as response_comment
    FROM taxonomy
    WHERE 
         kingdom is null
         OR
         length(trim(kingdom)) == 0
    ;

### 2.3 Reading Test Descriptors (non-normative)

#### 2.3.1 Key Parts of a Test Descriptor

- termLocalName
- skos:prefLabel
- specification - expected response
- specification - authorities/defaults
- information elements
- parameters

#### 2.3.2 Reading a Specification 

#### 2.3.2.1 Response as Shorthand for a Set of bdqffdq Concepts (non-normative)

We regularly use Response, Response.status, Response.result, and Response.comment as shorthand for a more complicated set of bdqffdq: classes, object properties and datatype properties.  The table below describes how these concepts are related.

| Concept | bdqffdq Term(s) | Description |
| ------- | ------- | ----------- |
| Response | bdqffdq:Assertion | The report from a single execution of a single Test, consisting of a bdq:Response.status, a bdq:Response.result, a bdq:Response.comment, and optionally, a bdq:Response.qualifier.| 
| Response.status | bdqffdq:ResponseStatus, bdqffdq:hasResponseStatus | A metadata element in a bdq:Response indicating whether a particular Test (bdqffdq:Validation, bdqffdq:Amendment, bdqffdq:Measure, or bdqffdq:Issue) was able to be performed or not.| 
| Response.result | bdqffdq:ResponseResult, bdqffdq:hasResponseResult, bdqffdq:hasResponseResultValue | The element in a bdq:Response containing the value returned by a Test (bdqffdq:Validation, bdqffdq:Amendment, bdqffdq:Measure, or bdqffdq:Issue)|
| Response.comment | bdqffdq:hasResponseComment | A human readable interpretation of the results of the Test.|
| Response.qualifier | bdqffdq:ResponseQualifier, bdqffdq:hasResponseQualifier | Additional structured information that qualifies the bdq:Response, intended as an extension point for uncertainty.|

#### 2.3.2.2 Guidance for Reading a Specification (normative)

A bdqffdq:hasExpectedResponse property of a bdqffdq:Specification provides expectations for the behavior of an implemenation of a Test.  A bdqffdq:hasExpectedResponse consists of a sequence of blocks of "RESPONSE, criteria;"   Where a few Amendment Tests can propose values for multiple [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021), the "criteria" is a sequence of options for that RESPONSE.  When reading a Specification, implementers SHOULD read each block in sequence, evaluating each of the criteria in sequence, and returning the first response for which the specified criteria are met.  An exception to this is that the placement of EXTERNAL_PREREQUISITES_NOT_MET as the first RESPONSE in the Specification. This does not imply that the responsiveness of an external resource should be assessed first. Implementers MAY handle failure of an external resource in any appropriate manner, for example, with exception handling.

#### 2.3.2.3 Further Guidance for Reading a Specification (non-normative)

Responses in a Specification are expressed in a concise and abbreviated form for readability by implementers, expanding these to string properties on a Response object gives:

EXTERNAL_PREREQUISITES_NOT_MET means Response.status=EXTERNAL_PREREQUISITES_NOT_MET, Response.result=null, Response.comment={some non-null description of the failure condition}

INTERNAL_PREREQUISITES_NOT_MET means Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.result=null, Response.comment={some non-null description of the failure condition}.

COMPLIANT means Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment={some non-null description of the failure condition}. etc.

Expressed with bdqffdq terms, as would be if Assertions are expressed in RDF, the first of these would be:

EXTERNAL_PREREQUISITES_NOT_MET means some bdqffdq:Assertion bdqffdq:hasResponseStatus bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET, that Assertion bdqffdq:hasResponseResult Response.null,  that Assertion bdqffdq:hasResponseComment "{some non-null description of the failure condition}"

For example, the bdqffdq:hasExpectedResponse for the Specification for: [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe) states:

    EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

To understand the meaning of bdq:sourceAuthority in the expected response, see the the bdqffdq:hasAuthoritiesDefaults for the Specification: 

    bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}

The specification is thus to be read as: 

1. Return EXTERNAL_PREREQUISITES_NOT_MET if the ISO Country codes list (https://www.iso.org/iso-3166-country-codes.html, searchable at https://www.iso.org/obp/ui/#search)  is not available; 
2. else Return INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; 
3. else Return COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the ISO Country Codes list; 
4. otherwise NOT_COMPLIANT

This could be implemented with a local copy of the ISO 3166 Country Codes (likely the better choice for this small stable list), or with a web service call. 

Any EXTERNAL_PREREQUISITES_NOT_MET can also be read as exception handling, thus: 

1. Return INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; 
2. else 
  - try :
    - Return COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the ISO Country Codes list (https://www.iso.org/iso-3166-country-codes.html, searchable at https://www.iso.org/obp/ui/#search);
  - catch :   
    - Return EXTERNAL_PREREQUISITES_NOT_MET (as the the ISO Country codes list is not available); 
3. otherwise NOT_COMPLIANT

Where a Test is parameterized or when a source authority (bdq:sourceAuthority) is specified in the text of the expected response the Specification should include a bdqffdq:hasAuthoritiesDefaults data type property containing the parameters, default values, and references to resources, including API enpoints that would provide access to values in authority.   

Values of bdqffdq:hasAuthoritiesDefaults are text strings listing parameters in the form of a semicolon delimited list of one or more of the following: 
     
- parameter default = "default value" 
- parameter default = "default value" {[resource]}
- parameter default = "default value" {[resource]} {API endpoint [resource]}

The bdqffdq:hasAuthoritiesDefaults property may be present in isolation (to make the expected response easier to read) as in the Test [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe) example above when a Test is not parameterized, or when a Test is parameterized, with corresponding bdqffdq:Arguments and bdqffdq:Parameters.  

See section [# 3.3 Parameterising the tests (normative)](../../bdqcore/index.md#33-parameterising-the-tests-normative) of the bdqcore landing page for further guidance on bdq:sourceAuthority values, parameters, and arguments. 

#### 2.3.2.4 Default Value Strings in Parameters (normative)

When a Test is defined as parameterized, implementations SHOULD support the parameter in addition to the information elements.  When a Test is defined as parameterized, implementations MAY choose to only support the default value, and MAY do so internally to the Test, without including the parameter(s) in the test API (note that implementations that choose to do so, will be unable to validate against all of the Test validation data (see [8 Validating Test Implementations](#8-Validating-Test-Implementations-normative))).

When the parameter has a default value and a resource, and an implementation includes the parameter in its API, that implementation MUST support the string literal given as the default value, and internally choose the resource "{[resource]}" or "{API endpoint [resource]}" based on that string literal "default value".  Implementations MAY also accept other values including the "{[resource]}" or "{API endpoint [resource]}" as the value for the parameter in the API for the Test implementation.

#### 2.3.2.5 Example Interpretation of a Parameter String Default Value (non-normative)

The following code snippet in Java from the FilteredPush rec_occur_qc library illustrates interpretation of the default value "Creative Commons" when provided as a parameter to an implementation of [AMENDMENT_LICENSE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8).  The literal "Creative Commons" is accepted as a parameter value.

    @Amendment(label="AMENDMENT_LICENSE_STANDARDIZED", description="Propose amendment to the value of dwc:license using bdq:sourceAuthority.")
    @Provides("dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8/2023-09-18")
    @Specification("EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; AMENDED value of dcterms:license if it could be unambiguously interpreted as a value in bdq:sourceAuthority; otherwise NOT_AMENDED. bdq:sourceAuthority default = 'Creative Commons' {[https://creativecommons.org/]} {Creative Commons licenses [https://creativecommons.org/about/cclicenses/]}")
    public static DQResponse<AmendmentValue> amendmentLicenseStandardized(
        @ActedUpon("dcterms:license") String license,
        @Parameter(name="bdq:sourceAuthority") String sourceAuthority
    ) {
        DQResponse<AmendmentValue> result = new DQResponse<AmendmentValue>();

        if (MetadataUtils.isEmpty(license)) { 
            result.addComment("No Value provided for dcterms:license");
            result.setResultState(ResultState.NOT_AMENDED);
        } else { 
            if (MetadataUtils.isEmpty(sourceAuthority)) { 
                sourceAuthority = "Creative Commons";
            }
            try { 
                MetadataSourceAuthority sourceAuthorityObject = new MetadataSourceAuthority(sourceAuthority);
                if (sourceAuthorityObject.getAuthority().equals(EnumMetadataSourceAuthority.INVALID)) { 
                    result.setResultState(ResultState.EXTERNAL_PREREQUISITES_NOT_MET);
                }
                String pattern = "";
                if (sourceAuthorityObject.getAuthority().equals(EnumMetadataSourceAuthority.CREATIVE_COMMONS)) {
                   ....

This library also includes a method who's signature does not include the parameter, but which runs the implementation of [AMENDMENT_LICENSE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8) with the default parameter.

    @Amendment(label="AMENDMENT_LICENSE_STANDARDIZED", description="Propose amendment to the value of dwc:license using bdq:sourceAuthority.")
    @Provides("dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8/2023-09-18")
    @Specification("EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; AMENDED value of dcterms:license if it could be unambiguously interpreted as a value in bdq:sourceAuthority; otherwise NOT_AMENDED. bdq:sourceAuthority default = 'Creative Commons' {[https://creativecommons.org/]} {Creative Commons licenses [https://creativecommons.org/about/cclicenses/]}")
    public static DQResponse<AmendmentValue> amendmentLicenseStandardized(
        @ActedUpon("dcterms:license") String license
    ) {
        return amendmentLicenseStandardized(license, null);
    }

#### 2.3.3 The Concept of "interpreted as" (normative)

In the Specifications the phrase "interpreted as" SHOULD BE interpreted by Implementers to mean: 

1. where Darwin Core (Wieczorek et al. 2012) data are serialized as strings, but the Test refers to data as numeric or other non-string data type, can the string value be parsed into the target data type in the language of implementation (e.g., "1" as the integer 1), **or**
2. matching a representation of a value unambiguously onto a controlled vocabulary (e.g., ‘WGS84’ to ’EPSG:4326’), **or**
3. interpreting the representation of a numeric value (e.g., a Roman numeral) as a number (e.g., an integer).

When interpretations of strings containing Roman numerals as numbers is intended, guidance associated with the text, usually in the skos:note for the Test, should be explicit about this meaning.  For example, the skos:note for the Test [AMENDMENT_MONTH_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/2e371d57-1eb3-4fe3-8a61-dff43ced50cf) states: "Implementations should translate interpretable Roman numerals in the range I-XII in dwc:month as integer month values 1-12, as some natural science domains use Roman numeral months to avoid language and day/month vs moth/day order." this is explicit guidance for the meaning of "interpeted as" in the Specification for this Test: "AMENDED the value of dwc:month if it can be unambiguously interpreted as an integer between 1 and 12 inclusive;"

#### 2.3.4 Handling Leading and Trailing Whitespace (normative)

<!--- TODO: Rewrite this section as normative guidance for implementers. Lee thinks it reads well and did a few minor edits--->

Whitespace refers to characters such as spaces and tabs that affect rendering of printed or displayed output but which themselves are not printed (see the [Glossary](../../intro/index.md#6-glossary)). A field that only includes whitespace is treated as bdq:Empty. In bdqffdq:Validation Tests that require the lookup of a bdq:sourceAuthority, leading and/or trailing whitespace may cause the test to fail as no preprocessing is performed on the data. Leading and trailing whitespaces may be stripped out in a subsequent bdqffdq:Amendment Tests and thus pass when the same bdqffdq:Validation Test is re-run.

Amendments SHOULD propose changes with leading or trailing whitespace removed.

<!--- TODO: Above needs better phrasing --->

## 3 Compliant Implementation (normative)

In order to be considered as compliant with BDQ Core, an implementation MUST meet the requirements of this section.   

The most important elements of BDQ Core is the structure that holds explicit descriptions of what a data quality Test is intended to do, along with the consistent structure for reporting the results from the execution of a Test upon data.  We expect that implementers will implement sets of these Tests that fit their data quality needs, and may also implement other Tests that are specifically suited for their domain. BDQ Core provides a coherent library of Tests that can be applied to the set of defined bdqffdq:UseCases, and considerable thought has gone into describing Tests that isolate particular data quality issues and work together as a conherent suite.   

An implementation of a Test MUST include all bdqcore:SingleRecord Validation, Amendment, and Measure Tests for each implemented UseCase.  An Implementation MUST provide for at least one bdqffdq:UseCase, and MAY provide implementations for more or all of the bdqffdq:UseCases.  New implementations MAY include additional Tests and additional UseCases.

Results from each Test MUST be produced in the form Response.status, Response.result, and Response.comment, with one Test producing one Response. Results MAY include Response.qualifier (See 4 Extension Points).  The values of Response.status and Response.result MUST be those specified. This standard is agnostic concerning data structures and serializations of a Response. The standard is agnostic concerning internationalization and languages of labels applied to human readable presentations of values within a Response.  See the bdqcore: landing page section on the [Structure of a Response](../../bdqcore/index.md#31-Structure-of-Response-normative) for further normative guidance on Responses as RDF or as data structures.

Additional Tests that conform to BDQ Core MUST describe those Tests using the bdqffdq Framework, those Tests MUST use the same Response structures, and those Tests MUST be related to bdqffdq:UseCases, either those defined in the standard or additional use cases.  

Implementations MUST provide Parameterized Tests that support the default Parameter values. Implementations SHOULD provide for Parameterized Tests to take parameters, but MAY produce an implementation of a Parameterized Test that takes no parameters but only uses a default parameter value applicable within their domain.

How a Test responds when given a parameter value that is not supported by the implementation is not specified. Implementers SHOULD handle this in a manner appropriate for their implementation framework. Unless specified in the Specification, implementations MUST NOT use Response.status="EXTERNAL_PREREQUISITES_NOT_MET" to indicate a non-supported parameter value.

Implementers are encouraged to produce means of testing data quality in bulk in settings such as SQL queries on relational data stores where construction of Response objects is not feasable, but the logic of a Specification can be framed as a question on a data store.  Such non-Framework implementations MUST NOT assert compliance with BDQ Core.

Within the Response.result for an Amendment Test, the order of key-value pairs is not specified and MAY vary.

## 4 Extension Points (normative)

A response MAY include a Response.qualifier (in RDF, a bqqffqd:hasResponseQualifier object property on an instance of a bdqffdq:Assertion). This is intended as a place to include structured assertions concerning uncertainty in a response. This is also intended as a place to include structured assertions about the details of Amendment Tests (e.g. TRANSPOSED MAY be attached to a Response.qualifier for some Amendment Tests).


MultiRecord (bdqffdq:MultiRecord) Measues that return counts where the input InformationElement is Response values from Tests on SingleRecords (bdqffdq:SingleRecord) MUST report only a single count as the Response.result, but can provide a Response.qualifier containing structured data describing additional information such as the total number of SingleRecords evaluated (to calculate percentages), the number of each value of Response.status encountered, and the number of each Response.result encountered.  Measures under the Framework are only allowed to return "COMPLETE", "NOT_COMPLETE", or a single number. If it is desirable for any Measure to return more than a single number, Response.qualifier is the extension point to use. 

## 5 Responses from Tests

### 5.1 The Response Object (normative)

The four Test Types, Validation, Issue, Amendment, and Measure all provide a Response from the execution of the Test. The Response from a Test is an assertion which MAY form part of a data quality report or MAY be wrapped in an annotation. 

Responses from each of the Tests MUST be structured data, and MUST NOT be simple pass fail flags. 

The Response MUST include the following three components: 

1. Response.result is the returned result for the Test, i.e. numeric for Measure Tests, a controlled vocabulary consisting of "COMPLIANT" or "NOT_COMPLIANT" for Validation Tests, "NOT_ISSUE" or "POTENTIAL_ISSUE" for Issue Tests, either a numeric value or a controlled vocabulary consisting of "COMPLETE" or "NOT_COMPLETE" for Measure Tests, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendment Tests.

2. Response.status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the Test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 

3. The Response.comment supplies human-readable text describing reasons for the Test result.

An Amendment Test may propose a change to an exisiting Darwin Core (Wieczorek et al. 2012) value or a set of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) or fill in a missing value. Amendment Tests are intended to improve one or more components of the quality of the record.  The Response.result from an Amendment Test MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  The Framework also supports changes to procedures but we have not framed any such Tests in this form.  

An Amendment Test Response.result SHOULD consist of a set of key:value pairs, where the key is the InformationElement to be modified, and the value is the proposed new value for that InformationElement. The Response.result key:value pairs SHOULD be a JSON serialization of the proposed changes.

Under the Framework (bdqffdq:), amendments may propose changes to processes as well as data, no structure is proposed for such an Amendment Test Response.result, and implementers MAY develop their own structures and serialisations for such Amendment Test Response.results.

Nothing in this section should be taken as a requirement for a particular format or serialization of bdqffdq:Assertions or Responses. Implementations MAY serialize Assertions in any appropriate form. 

Nothing in this section should be taken as a requirement to how bdqffdq:Assertions or Responses are to be presented to consumers of data quality reports.  Implementations MAY present the results of Tests in any form appropriate for their consumers.  

See the bdqcore: landing page section on the [Structure of a Response](../../bdqcore/index.md#31-structure-of-response-normative) for further normative guidance on representing Responses as RDF or in data structures.

### 5.2 Framework Elements Not Included in BDQ Core Test Descriptions (normative)

Implementers SHOULD create an instance of bdqffdq:Mechanism to uniquely identify their suite of Test implementations.

Implementations producing data quality reports SHOULD create instances of bdqffdq:Assertions grouped in bdqffdq:DataQualityReports that also specify the bdqffdq:DataResource that the bdqffdq:DataQualityReport concerns.

Implementers MUST provide bdq:Response data in data quality reports consisting of bdq:Response.status, bdq:Response.result, and bdq:Response.comment.  

Implementations MAY perform data Quality Control, data Quality Assurance, or both.  

## 6 Guidelines for Implementers

### 6.1 Parameters and Changing the Behavior of a Test (normative)

Many Tests specify bdqffdq:Parameters that are intended to change the behavior of a Test to fit local data quality needs without changing the Specification of the Test.  

A Parameterized Test will behave differently on the same data when using different Parameter values. 

Implementers SHOULD only present non-default Parameter values to a Test implementation if needed for local data quality needs. When a test is executed with non-default Arguments specified for Parameters, consumers of Assertions and data quality reports resulting from such MUST be able to tell that non-default Arguments were used, and what the non-default values were.

When a non-default Argument is used, a Response.comment SHOULD include the non-default value.

Implementers MUST NOT produce Test implementations identified by the same identifiers that only implement non-default Parameter values.  An implementation of a Test MUST support the Test execution with the default Parameter values, and MAY optionally support other Parameter values.  Provided Parameters MUST NOT change the behavior of the Test to depart from the bdqffdq:Specification.expectedResponse.  Parameters MUST only change the behavior of the Test as specified in the bdqffdq:Specification.expectedResponse.

<!--- Text to Merge with above 6.1 When a non-default Argument is used, an instance of an  **TODO** Specify how to assert the alternate Argument value in RDF. --->

### 6.2 Execution Process is Agnostic (non-normative)

The Test descriptions in BDQ Core are designed to be able to be used anywhere in the lifecycle of biodiversity data, and are designed to be independent of the environment in which the Tests are run. Tests may be run-

- at the point of initial collection or observation of organisms,
- to support data transcription,
- in loading data into databases of records from field or transcription sources,
- in preparing data from databases of record for aggregation,
- during data aggregation,
- individually on single Darwin Core records,
- or fragments of Darwin Core (Wieczorek et al. 2012) records within a data capture interface,
- in sequence in a processing pipleine of Darwin Core records, or
- in paralell in a processing pipeline of Darwin Core records, or
- in a workflow environment that produces lists of unique values of InformationElements for each Test, executes the Test on the unique values, and then maps the results back out into rows in the data set.

Data may be presented to an execution framework as Flat Darwin Core, or as Structured Darwin Core, or in another structure that can be mapped to the InformationElements of relevant Tests.

### 6.3 Considerations for Test Execution (normative)

Many Tests invoke external bdq:sourceAuthorities, some of these are downloadable vocabulary files, others are webservices with changing data.

Implementation of Tests SHOULD locally cache the results of calls to remote web services, particularly if they operate on a sequence of bdqffdq:SingleRecords instead of operating on distinct values of bdqffdq:InformationElements.  Data sets typically contain many repeated values, and remote web services SHOULD NOT be subject to repeated requests using the same question. 

Some source authorities are highly stable small vocabularies.  Implementers MAY choose to query a local copy of such a vocabulary, even if a remote service is specified in a bdq:sourceAuthority for a Test. Implementers SHOULD monitor for changes to that vocabulary and update local data when changes occur. 

### 6.4 Order of Test Execution.

#### 6.4.1 Phases: Pre-Amendment, Amendment, Post-Amendment

A good practice for executing the Tests is to execute all of the bdqffdq:SingleRecord Validation and Measure Tests in a pre-amendment phase, then to execute all of the Amendment Tests in an amendment phase, then to re-execute all of the Validation Tests on the data with the proposed changes from the amendments applied to the data in a post-amendment phase. Such a sequence of phases allows assertions to be made about the quality of the data as they were initially presented, and how much the quality of the data would be improved if the amendments were accepted. Within pre-amendment and post-amendment phases, the Validation and Measures Tests are agnostic about the order in which they are run, the extent to which they are run in parallel, or the extent to which they are run on single records or on unique values within a data set. One possible workflow for Tests is to aggregate the unique values of applicable InformationElements within a bdqffdq:MultiRecord for each Validation or Measure Test, then to execute the Validation or Measure Test on just the unique values, then de-aggregate the results back to each bdqffdq:SingleRecord. This is analogous to implementing Tests as SQL queries.

Recommended process with the current suite of BDQ Core Tests is to run all pertinent bdqffdq:SingleRecord Validation and Measure Tests, then run all pertinent Under Quality Assurance, MultiRecord measures that return "COMPLETE" or "NOT_COMPLETE" MAY be used as filters for quality for purpose, exclude records from the data set untill all bdqffdq:MultiRecord Measures Tests of this sort are returning "COMPLETE", this under the mathematical forumuation of the Framework, is the assertion that the data are fit for the purpose of the selected UseCase.

Under Quality Control, bdqffdq:MultiRecord Measure Tests that return numeric values MAY be used to assess the prevalence of quality issues in the data with respect to the selected bdqffdq:UseCase.  

#### 6.4.2 Test Dependencies

The BDQ Core Tests are largely agnostic to the extent to which they are run in parallel and the sequence in which particular Tests are run. While the Tests are designed to be as independent as possible, some Amendment Tests have potential interactions given the by-design redundancies in Darwin Core (Wieczorek et al. 2012). The order of execution of some Amendment Tests can affect results. 

When Amendment Tests are executed in a workflow where downstream amendments operate on data with the changes proposed by upstream amendments applied, the following sequences SHOULD be followed. Similarly when Amendment Tests are executed in parallel these sequences SHOULD be applied.

Given that Amendment Tests propose a value to a primary term from secondary terms, priority over those which back fill secondary terms from a primary term, The Test [AMENDMENT_EVENT_FROM_EVENTDATE](https://rs.tdwg.org/bdqcore/terms/710fe118-17e1-440f-b428-88ba3f547d6d) SHOULD be run after the following amendments that propose changes to dwc:eventDate: 

- [AMENDMENT_EVENTDATE_FROM_VERBATIM](https://rs.tdwg.org/bdqcore/terms/6d0a0c10-5e4a-4759-b448-88932f399812),
- [AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY](https://rs.tdwg.org/bdqcore/terms/3892f432-ddd0-4a0a-b713-f2e2ecbd879d),
- [AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR](https://rs.tdwg.org/bdqcore/terms/eb0a44fa-241c-4d64-98df-ad4aa837307b),
- [AMENDMENT_EVENTDATE_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/718dfc3c-cb52-4fca-b8e2-0e722f375da7).

[AMENDMENT_SCIENTIFICNAME_FROM_TAXONID](https://rs.tdwg.org/bdqcore/terms/f01fb3f9-2f7e-418b-9f51-adf50f202aea) SHOULD be run after the Amendment test which proposes changes to dwc:TaxonID: [AMENDMENT_TAXONID_FROM_TAXON](https://rs.tdwg.org/bdqcore/terms/431467d6-9b4b-48fa-a197-cd5379f5e889). 

Where multiple amendments on secondary terms could propose conflicting changes to a primary term, the sequence of Amendment Tests SHOULD be ordered.

The following Amendment Tests SHOULD be composed to run in an ordered sequence:

| order       | Test                                                       |
|-------------|------------------------------------------------------------|
| first       | AMENDMENT_EVENTDATE_FROM_VERBATIM                          | 
| second      | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR    |
| and finally | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY                      |

BDQ Core does not specify how these ordering of these Tests should be accomplished.  This could be done by describing an Amendment Test with an expected response that specifies the execution of each of these Tests in order.  Such a composition of Amendment Tests would be the preferred method of sequencing under the Framework, but to keep Tests as granular a possible, and to allow the maximum flexibility for the composition of Tests in Profiles to support bdqffdq:UseCases, BDQ Core does not provide such requirements. Ordering could also could be done by providing a configuration file for a Test execution framework specifying Test dependencies. Ordering could be supported in a workflow environment by composing a workflow to execute these Tests in sequence.  

The bdqffdq: ontology does not include a property to describe sequence interdependencies among amendments.  

The bdqffdq: ontology provides terms: bdqffdq:targetedMeasure, bdqffdq:targetedValidation, bdqffdq:TargetedIssue, that could be used, together with bdqffdq:improvedBy to relate Amendment Tests to Validation, Measure, and Issue Tests.  BDQ Core does not use these terms to describe Test interrelationships, though they could be used for this purpose. 

#### 6.4.3 Implementing a concrete Test (normative)

Implementations MAY be complete in the scope of the Test as described in [bdqcore:](../../list/bdqcore/index.md) with bdqffdq terms.  Such concrete implementations encompass the elements of the test defined in an instance of bdqffdq:DataQualityNeed, plus its associated bdqffdq:InformationElements, instance of a subclass of bdqffdq:Method, instance of bdqffdq:Specification, any related Arguments and Parameters, and be able to produce instances of bdqffdq:Assertion (carrying Response.status, Response.result, Response.comment).     

#### 6.4.4 Presenting Darwin Core Data to a Method that Implements a Test

One complexity introduced by the abstraction of Tests into essentially APIs that take [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) as input and output, Response objects are correctly mapping Darwin Core terms loaded in an execution framework onto the parameters of an implementation method.   Consider an implementation of the Test [VALIDATION_ENDDAYOFYEAR_INRANGE](https://rs.tdwg.org/bdqcore/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8) that has a method signature: 
    
    public Response validationEnddayofyearInrange(String startDayOfYear, String eventDate) 

If an implementation framework calls this method reversing the binding of dwc:startDayOfYear and dwc:eventDate as present in whatever structure is present in the framework, for example: 

    Response endDayTestResponse = validationEnddayofyearInrange(eventDate, startDayOfYear);

the Test will not return the desired result, even if the implementation is correct.  Thus correct matching of input terms to the implementation of each Test is critical. 

Multiple approaches are possible to correctly match input Darwin Core terms onto method signatures for methods that implement Tests. 

BDQ Core is entirely agnostic as to how this binding is done. Implementers MAY freely implement in any appropriate way for their environment. However, Test implementations MUST return structured Responses containing Response.status, Response.result, and Response.comment.   

In Java, annotating method parameters and using reflection to bind between the execution framework and Test implementations works well, here is a simplified code snippet from the FilteredPush event_date_qc library that uses Java annotations, e.g. @ActedUpon(value="dwc:endDayOfYear") to provide metadata about which parameter goes with which Information Element. 

    public Response validationEnddayofyearInrange(
            @ActedUpon(value="dwc:endDayOfYear") String endDay,
            @Consulted(value="dwc:eventDate") String eventDate) {

An execution framework can use reflection to determine, from the annotations on the parameter, which Darwin Core term to bind to which parameter.

Additional metadata can be added in Java annotations, here, from the FilteredPush event_date_qc library annotations enable an implementation framework to look a Test implementation by the Test GUID, and can provide metadata about the Test to users, and for maintenance, can be used to determine if an implementation is up to date with the latest version of a Test specification.

    @Validation(label="_ENDDAYOFYEAR_INRANGE", description="Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?")
    @Provides("9a39d88c-7eee-46df-b32a-c109f9f81fb8")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8/2023-09-18")
    @Specification("INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is EMPTY or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is EMPTY or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT ")
    public static DQResponse<ComplianceValue> validationEnddayofyearInrange(
            @ActedUpon(value="dwc:endDayOfYear") String endDay,
            @Consulted(value="dwc:eventDate") String eventDate) {
        ....
    } 

This approach will only work with a subset of programming languages.  

In many languages, a domain object can be passed as a method parameter.  
    
    public Response validationEnddayofyearInrange(Event event) { 
        
    }

Here, both the execution framework and the internals of validationEnddayofyearInrange must be able to work with the Event (object or structure) and work with its Event.enddayofyear and Event.eventdate properties.

It is also possible to implement in an object oriented manner as methods on a class: 

    public class Event() { 

        private eventDate;
        private enddayofyear;

        public Response validationEnddayofyearInRange()...

    } 

Other approaches are possible.  Implementers MAY use any approach to passing data into Test implementations appropriate for their language(s) and environment.

#### 6.4.5 Example Test Implementations (non-normative)

#### 6.4.5.1 Example in Pseudocode (non-normative)

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

#### 6.4.5.2 Example in Java (non-normative)

Given the test [VALIDATION_DAY_STANDARD](https://rs.tdwg.org/bdqcore/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498)

Specification
: INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.

Information Elements Acted Upon
: dwc:day

Here is an example implementation from the FilteredPush event_date_qc library.  In this implementation, Java annotations are used to provide metadata that can be used by an implementation framework to pick out a Test to run by its IRI or term_localName and match an input Darwin Core term to a (Java) parameter in the method signature.  The implementation walks through the elements of the specification in sequence, and return the first matching response in a response object (which has Response.state, Response.result (here called value), and Response.comment properties.  

    @Validation(label="VALIDATION_DAY_STANDARD", description="Is the value of dwc:day an integer between 1 and 31 inclusive?")
    @Provides("47ff73ba-0028-4f79-9ce1-ee7008d66498")
    @ProvidesVersion("https://rs.tdwg.org/bdq/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498/2023-09-18")
    @Specification("INTERNAL_PREREQUISITES_NOT_MET if dwc:day is EMPTY; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT. ")
    public static DQResponse<ComplianceValue> validationDayStandard(@ActedUpon("dwc:day") String day) {
        DQResponse<ComplianceValue> result = new DQResponse<ComplianceValue>();

		if (DateUtils.isEmpty(day)) {
			result.addComment("No value provided for day.");
			result.setResultState(ResultState.INTERNAL_PREREQUISITES_NOT_MET);
		} else {
			try {
				int numericDay = Integer.parseInt(day.trim());
				if (DateUtils.isDayInRange(numericDay)) {
					result.setValue(ComplianceValue.COMPLIANT);
					result.addComment("Provided value for day '" + day + "' is an integer in the range 1 to 31.");
				} else {
					result.setValue(ComplianceValue.NOT_COMPLIANT);
					result.addComment("Provided value for day '" + day + "' is not an integer in the range 1 to 31.");
				}
				result.setResultState(ResultState.RUN_HAS_RESULT);
			} catch (NumberFormatException e) {
				logger.debug(e.getMessage());
				result.setValue(ComplianceValue.NOT_COMPLIANT);
				result.setResultState(ResultState.RUN_HAS_RESULT);
				result.addComment(e.getMessage());
			}
		}
		return result;
    }

#### 6.4.6 Implementing an Abstract Test 

In some environments, implementations MAY be a lightweight implementation of an abstract Test. Such abstract implementations MAY encompass only the elements of the Test defined in an instance of bdqffdq:DataQualityNeed, plus its associated bdqffdq:InformationElements, and not be able to produce instances of bdqffdq:Assertion, but SHOULD be able to produce analogs of Response objects (with Response.status, Response.result, and Response.comment properties).     

Consider the Validation Test: [VALIDATION_ENDDAYOFYEAR_INRANGE](https://rs.tdwg.org/bdqcore/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8)

A SQL query that implements this abstract concept, that the dwc:enddayofyear is in range, could take the following form, using available database fields that contain data related to the abstract information element, but are not precicely mapped to the concrete specified ActedUpon and Consulted [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) in the specification.  This query produces a data quality report with: 

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

#### 6.4.7 Implementing a Test in a Specific Environment

Given data stored in a known and controlled environment, Test implementations can be specifically tailored to that environment, both in language and in assumptions about formats and data types. Consider the Validation Test: [VALIDATION_ENDDAYOFYEAR_INRANGE](https://rs.tdwg.org/bdqcore/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8)

With the specification "INTERNAL_PREREQUISITES_NOT_MET if dwc:day is EMPTY; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT."

Given a hypothetical Event table with fields including a primary key event_id and an integer field day, an implementation of [VALIDATION_DAY_STANDARD](https://rs.tdwg.org/bdqcore/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498) in SQL that operates on data in the aggregate might look like:

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

This implementation does not generalize, as for example, day in a numeric data type that supports numbers in addition to integers would return incorrect values (per the Test Specification, which requires day to be an integer), for values of day such as "8.5"

Implementations should carefully consider the assumptions inherent in the environment on which Tests are being run.  For example, the FilteredPush implementations in event_date_qc, sci_name_qc, rec_occur_qc, and geo_ref_qc, expect that all data will be presented to the Test methods as strings.  Therefore each Test implementation that deals with numeric values must convert the input strings to appropriate numeric types for evaluation, and can use the failure to convert the data type as a means to identify INTERNAL_PREREQUISITES_NOT_MET.

## 7 Presentation of Results

We are agnostic about how reports from BDQ Core can be reported, e.g., as aggregated results, on web pages for individual records, as spreadsheets of results with issues for quality control, etc.  

Reports SHOULD identify Tests to consumers of those reports using at least the skos:prefLabel for the Test class, e.g. [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134).  

### 7.1 Data Quality Reports

### 7.1.1 InformationElements ActedUpon and Consulted in Results (normative)

InformationElements (subtypes of bdqffdq:InformationElement) are bdqffdq:ActedUpon or bdqffdq:Consulted. Presentations of data quality results MAY use ActedUpon and Consulted identification of Information Elements to identify to users which specific values assertions are being made about, and what values are being used to support those assertions. ActedUpon InformationElements are those for which a Validation Test is asserting compliance/non-compliance, or an Amendment Test that is proposing an improvement to the data. Consulted InformationElements are those which inform such decisions, but are not themselves the subject of the decision. For example, in the Test [AMENDMENT_EVENTDATE_FROM_VERBATIM](https://rs.tdwg.org/bdqcore/terms/6d0a0c10-5e4a-4759-b448-88932f399812), the InformationElement dwc:eventDate is ActedUpon, while the InformationElement dwc:verbatimEventDate is Consulted.  Implementers may wish to clearly represent to consumers of data quality reports (particularly data quality reports in the form of spreadsheets), which terms are particular Tests are making assertions about.


#### 7.1.2 Example (non-normative)

Below is an example, taken from MCZbase, of a portion of a data quality report, run on demand, for a single specimen using an implementation of BDQ Core Tests integrated into that collection management system.

This example shows Tests that were run, using the rdfs:comment on the bdqffdq:Validation to identify the action taken by the Test to the collection management staff reading the report. Then in columns for a pre-amendment phase, the result (Response.status or Response.result) of the Test, and the Response.comment explaining why the Test returned the result it did.  Below this report are listed any proposed changes from Amendment Tests, then in the table, the result and comment from repeating the Validation Tests in a post-amendment phase, treating the data as if the results of any amendments had been accepted. Amendments are not done automatically applied. Users must explicitly change the data if they want to accept the proposals from the amendments.  In the presentation, COMPLIANT values are styled in green and NOT_COMPLIANT values in red.  A subset of the results are shown here, so compliant result percentages included values not shown.

** QC Taxon Name for MCZ:Herp:R-1440**

Results of the Biodiversity Data Quality (TWDG) IG TG2 Taxon Name related
Tests.

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

### 7.2 Annotations (normative)

The bdqffdq: owl framework, and the framing of the Tests in BDQ Core as rdf using that ontology makes Test results particularly amenable to being wrapped in annotations following the W3C Web Annotation Data Model (Sanderson et al. 2017). Test responses MAY be represented as annotations.

The responses from Tests could be structured as elements that can be wrapped in the body annotation document along with metadata from the Framework to describe which Test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.

When Test responses are being returned as annotations, they SHOULD use the W3C Web Annotation Data Model for the annotations, and SHOULD place Test responses within the body of the annotation.  Such annotations SHOULD include reference to the source Test by the versioned fully qualified name of the Test (e.g. bdqcore:47ff73ba-0028-4f79-9ce1-ee7008d66498/2023-09-18) and the Test skos:prefLabel (e.g. VALIDATION_DAY_STANDARD).  Such annotations SHOULD also provide the bdqffdq:Mechanism that generated the Test response. 

When Test responses are persisted as anotations in association with the annotated data, a means SHOULD be provided to mark annotations as having been evaluated, and to carry the results of such evaluations.  Annotation conversations MAY provide such a means.  Vocabularies related to bug/issue tracking MAY provide such a means.

## 8 Validating Test Implementations (normative)

Implementers of the BDQ Core Tests SHOULD validate the behaviour of the internals of their Test implementations with unit Tests, and MUST validate that each Test implementation is capable of taking relevant input from a set of standard Test validation data, and returning the expected responses.

For synthetic Test validation data that could be conflated with actual data, see: [Identifying Synthetic and Example Data](../../synthetic/index.md)

### 8.1 Introduction (non-normative)

A set of Test validation data accompanying the BDQ Core Test descriptors.  This data is intended for implementers to use to evaluate whether or not their Test implementations produced the expected Response values for a set of cases for each Test.  Each Test specification could be graphed as a flow chart with several paths, the Test validation data are intended to cover each node and each path within each Test specification with at least a single case.  These data are however, not exhaustive unit Tests covering large numbers of edge cases, but rather a minimal set of Tests for expected behaviours.  

The Test validation data are organized as two flat CSV files.  Each row in each file is intended for the single validation of a single Test.  The file has columns identifying the Test, the input data, the expected Response.status, Response.result, an example Response.comment, parameter values (if any), and a set of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021). Most of the terms are empty for a given Test.

The Test validation records are all fragmentary flat Darwin Core (Wieczorek et al. 2012) Occurrence records.  Each row contains values for only those Darwin Core terms that are relevant input to the particular validation.   The validation records are all fragmentary, consisting of a mixture of real and artificial data with most of the records being synthetic.  The validation data are a set of 1191 records, with about 10 validation cases for each Test.  The set of rows for a particular Test are designed to validate that an implementation of that particular Test performs as expected against the specification.  This data set is referred to as the 'Test Validation Data'.  The set of about 10 validation records for each Test are designed to exercise all of the decision pathways in the specification of the Test.  

Additional Test records can be readily generated or adapted from real data using the following template based on the specifications below. In consideration of the community, the DataID values MUST uniquely identify a validation case for each additional Test data record and the resulting data added to the GitHub repository.

### 8.2 Structure of the Validation Data 

<!---Paul - please check meaning in paragraph below --->

The validation test data are intended as input into a testing system that can evaluate the implementations of Tests independently. Each Test data record is contains only the values of REQUIRED Information Elements ([Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021)) as input, and assesses whether the Test Response conforms to the expected responses in the Test data.  The data could be processed as input for unit Tests or it could be used as the basis for presenting synthetic records to a larger test execution system. The test data is designed to be used at a level where individual Tests are being assessed.  The structure of the validation data attempts to be at a level of abstraction above **the method signature specificity needed in unit Tests ??**, but still at a level that is examining individual Test implementations below the level of testing inputs and outputs of a larger data processing system that could take complete Darwin Core records as input and return rich data quality reports as output (to avoid forcing particular formats on data quality reports as a whole).  

The following column header for the data are used for the validation data files.

| header | definition |
| ------ | ---------- |
| Last Updated | The date on which this record was last updated |
| GitHub Issue | The URL of the GitHub issue number where rationale management of the Test under validation is maintained |
| GitHubIssueNo | The last section of the GitHub Issue URL - a number, e.g., 20 can be found at https://github.com/tdwg/bdq/issues/20. |
| GUID | The machine readable identifier for the Test under validation, e.g., 69b2efdc-6269-45a4-aecb-4cb99c2ae134 |
| Test Type | The type of the Test, either Validation, Issue, Amendment or Measure |
| Label | The second two components of the full english Test label, for example COUNTRYCODE_STANDARD |
| Data Dimension | Does the Test apply to data that is essentially NAME, SPACE, TIME or OTHER? |
| dataID | A local to bdq:ValidationData unique integer to indentify each Validation Data record | 
| LineForTest | A local to bdq:ValidationData integer identifier for Test records within one Test. For maintaining the sort order within a test, and with two special cases: "88" when Input.data contains a NULL character and "99" when Input.data contains non-printers characters. | 
| Input.data | Data for the Information Elements that are required by the Specification for unambiguous running of the Test, e.g., for [VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b23110e7-1be7-444a-a677-cdee0cf4330c), dwc:country="México", dwc:countryCode="MX" |
| Output.data | For Amendments only and when Response.status="AMENDED", suggested changes to the Input.data to improve quality, in the same format as Input.data |
| Response.status | The status on applying the Test to the data record. For VALIDATIONS, one of the terms "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET" or "RUN_HAS_RESULT". For AMENDMENTS, one of the terms "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET", "FILLED_IN", "AMENDED" or "NOT_AMENDED". For ISSUE, one of the terms "INTERNAL_PREREQUISITES_NOT_MET" or "RUN_HAS_RESULT". For MEASURES, either "RUN_HAS_RESULT" or "INTERNAL_PREREQUISITES_NOT_MET". |
| Response.result | The result of running the Test on the data record. For VALIDATIONS and AMENDMENTS, "NULL" where the Response.status is either "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET". For VALIDATIONS, either "COMPLIANT" or "NOT_COMPLIANT" where Response.status is "RUN_HAS_RESULT".  For AMENDMENTS where Response.status is either "FILLED_IN" or "AMENDED, the Response.result is a json structure containing a key:value list of Darwin Core terms and values for changes proposed by the AMENDMENT. For MEASURES, a resulting value or "NOT_REPORTED". |
|Response.comment | A human-readable example statement identifying the reason for the Test result given the input data. Implementations are not expected to produce this exact value | IssuesWithThisRow | A working column for recording issues while developing validation data, to be removed. |
| bdq:annotation | A placeholder for an annotation when Testing for their presence. |
| bdq:sourceAuthority | Input parameter for some Parameterized Tests. |
| dwc: (77 columns) |  All of the Darwin Core terms that are in scope for Core.  In each row, only those identified in the Information Elements of the relevant Test and pertinent to the Test case at hand contain values. |

**NOTE:** We have implemented examples of EXTERNAL_PREREQUISITES_NOT_MET using the Input.Data structure of

bdq:sourceAuthority="https://invalid/invalidservice", dwc:inputDataValue1="", dwc:inputDataValue 2... . As an example:

bdq:taxonomyIsMarine="https://invalid/invalidservice", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:scientificName=""

### 8.3 Examples of the Data for Validating Tests (Informative)

The validation files contain one column for each of 77 [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that are referenced as an InformationElement somewhere in Core, but only terms relevant to the particular validation case for the row are populated, therefore the validation files are sparse.  They contain fragments of Flat Darwin Core records. 

The header line for each of the validation files:  

"LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Response.status","Response.result","Response.comment","IssuesWithThisRow","bdq:annotation","bdq:sourceAuthority","dc:type","dcterms:license","dwc:acceptedNameUsageID","dwc:basisOfRecord","dwc:class","dwc:continent","dwc:coordinateUncertaintyInMeters","dwc:country","dwc:countryCode","dwc:county","dwc:dataGeneralizations","dwc:dateIdentified","dwc:day","dwc:decimalLatitude","dwc:decimalLongitude","dwc:endDayOfYear","dwc:establishmentMeans","dwc:eventDate","dwc:family","dwc:genus","dwc:geodeticDatum","dwc:higherClassification","dwc:higherGeography","dwc:higherGeographyID","dwc:infraspecificEpithet","dwc:island","dwc:islandGroup","dwc:kingdom","dwc:locality","dwc:locationID","dwc:maximumDepthInMeters","dwc:maximumElevationInMeters","dwc:minimumDepthInMeters","dwc:minimumElevationInMeters","dwc:month","dwc:municipality","dwc:occurrenceID","dwc:occurrenceStatus","dwc:order","dwc:originalNameUsageID","dwc:parentNameUsageID","dwc:phylum","dwc:scientificName","dwc:scientificNameAuthorship","dwc:scientificNameID","dwc:specificEpithet","dwc:startDayOfYear","dwc:stateProvince","dwc:subgenus","dwc:taxon","dwc:taxonConceptID","dwc:taxonID","dwc:taxonRank","dwc:verbatimCoordinateSystem","dwc:verbatimCoordinates","dwc:verbatimDepth","dwc:verbatimElevation","dwc:verbatimEventDate","dwc:verbatimLatitude","dwc:verbatimLocality","dwc:verbatimLongitude","dwc:verbatimSRS","dwc:vernacularName","dwc:waterBody","dwc:year","dwc:subfamily","dwc:superfamily","dwc:tribe","dwc:subtribe","dwc:genericName","dwc:infragenericEpithet","dwc:cultivarEpithet","dwc:individualCount","dwc:organismQuantity","dwc:footprintWKT","dwc:coordinatePrecision","dwc:namePublishedInYear","dwc:sex","dwc:typeStatus","dwc:pathway","dwc:degreeOfEstablishment","bdq:taxonIsMarine","bdq:geospatialLand","bdq:assumptionOnUnknownBiome","bdq:latestValidDate","bdq:earliestValidDate"

The data are sparse, as most dwc: term columns do not contain a value for each individual case.

A validation Test case evaluating empty, where no dwc: term columns contain a value (dataID=1):  

"2","1","1","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","INTERNAL_PREREQUISITES_NOT_MET","","dwc:countryCode is EMPTY","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation Test case for a validation where the input data result in a Response.result of NOT_COMPLIANT (dataID=7)

"8","7","7","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","NOT_COMPLIANT","dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value ","","","","","","","","","","","","Austria","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation Test case for a validation where the input data result in a Response.result of COMPLIANT (dataID=8)

"9","8","8","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","COMPLIANT","dwc countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value","","","","","","","","","","","","US","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

### 8.4 Where to Get the Validation Data (non-normative)

The validation data is in two files, one containing normal data values, the other containing validation cases using non-printing characters.

1. [TG2_test_validation_data.csv](TG2_test_validation_data.csv)
2. [TG2_test_validation_data_nonprintingchars.csv](TG2_test_validation_data_nonprintingchars.csv)

Validation file containing data values that would be expected to be encountered in the wild: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data.csv

Validation data file containing non-printing characters for testing implementation of EMPTY: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data_nonprintingchars.csv

This file is a csv file with the same set of columns as the above, but with rows that contain input values for selected [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) consisting of either the 0x00 null character (e.g. dwc:scientificName="0x00"), or a pair of ASCII control characters (shift out 0x0E and shift in 0x0F, e.g. dwc:day="0x0E0x0F"). This file is intended to validate that implementations of Tests are consistently evaluating inputs as EMPTY as expected by the definition of EMPTY.  

The non-printing characters file MUST only be edited with a tool that will maintain the non-printing characters.  

Both files have a header line identifying the specifications as defined in Section 8.2.

The expectation for the response that an implementation should produce when executed against the row: "Response.status", "Response.result" and "Response.comment", where an implementation is expected to produce the exact Response.status, the exact Response.result (ignoring order of any key-value pairs for an amendment response), and Response.comment is an example of what an English comment may look like.  

Parameter values are specified in a bdq:sourceAuthority column, when more than one sourceAuthority is involved, then these are given separate names.

Darwin Core term input columns are specified as "dc:type","dcterms:license","dwc:acceptedNameUsageID",...

### 8.5 Implementation and the Validation Data (normative)

Implementations SHOULD provide support for each Parameter value specified in the example data. 

Implementations MUST produce structured Response values with a Response.status, Response.result and Response.comment.  

To be compliant with BDQ Core, an implementation of the Core Tests MUST fulfill all of the REQUIRED elements of this section.

Human readable Data Quality Reports for Quality Control MAY take any appropriate form, they MAY aggregate Response values and comments, they MAY present results organized by Test, or by data record, or by frequency of problem, or any other form suitable for presentation.  Data Quality Reports for Quality Control SHOULD allow users to access individual Response.status, Response.result, Response.comment results.  

Response.comment values SHOULD be internationalized as appropriate for the the consumers of data quality reports.  

Response.status and Response.result constants SHOULD be given internationalized labels as appropriate for the the consumers of data quality reports.  

For each Test in an implementation, that Test MUST produce the same results as are specified in a row of the validation data for that Test, except when a bdq:sourceAuthority parameter specifies a web service other than the default sourceAuthority specified for that Test.

### 8.6 Existing Sofware tools (non-normative) 

### 8.6.1 Tools for Validating Test Implementations with the Validation Data (non-normative) 

The bdqtestrunner tool (Morris, 2024), written in Java, was written to validate the implementations of the BDQ Core Tests in various FilteredPush data quality libraries against the Test validation data, see: [doi:10.5281/zenodo.13932177](https://doi.org/10.5281/zenodo.13932178) and [github.com/FilteredPush/bdqtestrunner/](https://github.com/FilteredPush/bdqtestrunner/).  This tool uses Java annotations on methods that implement Tests in order to match inputs from the validation data to methods under Test that implement individual Tests. The tool could be reused to validate implementations in other Java classes that follow the same use of ffdq-api <!--- (**TODO: Cite**) ---> 

Java annotations can be used to match test implementation methods to tests and information elements to method parameters <!-- TODO: Complete this thought --->

### 8.6.2 Tools to assist with implementations and RDF presentation (non-normative) 

The Test implementations listed below use Java Annotations (as shown in the example in [Section 2.3.2.5](#2325-Example-interpretation-of-a-parameter-string-default-value-non-normative) to carry metadata to identify Tests and to allow binding of Darwin Core terms to Java method parameters.  The Java Annotations are themselves related to bdqffdq Framework concepts and are available in a library ffdq-api.  In addition, a Java library, kurator-ffdq is available for working with Test descriptions as RDF, being an implementation of the bdqffdq: Framework in Java.  The kurator-ffdq library also includes classes for generating stub methods for each Test in either Java or Python.

<!--- TODO: Add citations --->

- [ffdq-api](https://github.com/kurator-org/ffdq-api) Java annotations for decorating Test implementations.
- [kurator-ffdq](https://github.com/kurator-org/kurator-ffdq)  Java classes for bdqffdq: classes, able to produce stub code for Test implementations in Java or Python.

These libraries are available in Maven Central.

## 9 Existing Test Implementations (non-normative) 

A set of open source Java libraries provide classes which implement each of the bdqffdq:SingleRecord Tests that operate directly on data. These librarie are not part of the BDQ Core standard, but have been implemented as part of the process of writing the standard.

<!--- TODO: Add citations --->

- [event_date_qc](https://github.com/filteredpush/event_date_qc) Tests related to spatial terms.
- [sci_name_qc](https://github.com/filteredpush/sci_name_qc) Tests related to taxonomy and identification terms.
- [geo_ref_qc](https://github.com/filteredpush/geo_ref_qc) Tests related to spatial terms.
- [rec_occur_qc](https://github.com/FilteredPush/rec_occur_qc) Tests related to metadata terms.

These libraries are available in Maven Central.
