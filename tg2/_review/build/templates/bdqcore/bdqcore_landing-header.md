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

Preferred namespace abbreviation
: {pref_namespace_prefix}

This version
: <{current_iri}{ratification_date}>

Latest version
: <{current_iri}>

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

# Table of Contents 
{toc}

## 1 Introduction

This document provides explanatory information and normative guidance for the BDQ Core tests. The document includes terms in several namespaces that contain the recommended terms: `bdq:`, `bdqffdq:`, `bdqdim:`, `bdqenh:`, and `bdqcrit:` as well as the focus of this document the `bdqcore:` terms. For details and rationale, see Chapman et al. (2017).

### 1.1 Purpose

The document provides the context in which the BDQ Core tests exist.

### 1.2 Audience

This document is for Users and Implementors of BDQ Core who require a technical understanding of the Tests.

### 1.3 Associated Documents

The bdqcore: vocabulary includes: 

- A [Quick Reference Guide](../terms/bdqcore/index.md) to the tests.
- A [term-list for the vocabulary](../list/bdqcore/index.md), containing the vocabulary terms and their metadata.
- This landing page document provides Normative guidance on the use of the BDQ Core vocabulary.

In addition, A users guide to the use of the bdqcore tests is provided in the [Users Guide](../guide/users/index.md) and a guide to implemetation of the bdqcore tests is provided in the [Implementers Guide](../guide/implementers/index.md) 

### 1.3.1 Term List Distributions for BDQ Core

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcore/index.md | Complete term list for the bdqcore: vocabulary  | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.xml | An rdf representation of the tests in an RDF/XML serialization | 
| Turtle file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.ttl | An rdf representation of the tests in a Turtle serialization | 
| CSV file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqcore_terms.csv | CSV  filelisting the tests | 

### 1.4 RFC 2119 Key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.5 Status of the Content of this Document

Sections 1 is non-normative.

Portions of section 2 are normative and portions are non-normative.

Section 3 is normative.

Section 4 is non-normative.

Section 5 is non-normative.

### 1.6 Namespace Abbreviations

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
| rdfs         | http://www.w3.org/2000/01/rdf-schema#            |
| owl          | http://www.w3.org/2002/07/owl#                   |


### 2 A Brief Context for the BDQ Core Tests

The Authors acknowledge the centrality of the work of:

- The TDWG Framework on Data Qualilty Task Group (https://tdwg.github.io/bdq/tg1/site/) that provided the Framework for the BDQ Core tests.
- The TDWG Data Quality Use Case Library Task Group (https://github.com/tdwg/bdq/tree/master/tg3) for providing recommendations on use cases.
- The TDWG Annotations Interest Group (https://github.com/tdwg/annotations) as to how the test results may be reported against records. 
  
The terminology of BDQ Core is based primarily on the Fittness for use Framework (Viega 2016, TDWG Task Group 1, and Veiga et al. 2017) expressed as an ontology, but additional vocabularies are required for a complete description of the Tests and how to use them.  See the [list of vocabularies](../vocabularies/index.md).

BDQ Core Tests focus on values of a subset of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) composed as bdqffdq:InformationElements as inputs to the tests. Each Test is independent, to support the mixing and matching of Tests to meet particular data quality needs and not impose a particular model of test execution on implementation frameworks. Tests may execute in parallel, on data records in sequence, as queries on data sets and on unique values. Tests are paired in that all Amendment Tests are matched with a corresponding Validation Test that assesses some aspect of data quality. An Amendment Test may propose improvements to term values but BDQ Core recommends that all improvements be evaluated before application.

Some BDQ Core Tests also require reference to external data such as standard vocabularies of terms or names. 

While the most important BDQ Core Tests apply to a SingleRecord (bdqffdq:SingeRecord), Test results may also be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord.  Tests that accumulate information about results across multiple records are necessary for formal application of Quality Assurance and Quality Control principles.

### 2.1 Characteristics of the Tests (non-normative)

The scope of each test is largely provided by the bdqffdq:Specification. The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) used in the Specification are included in the "Information Elements". The Specification also includes references to external (to the Darwin Core standard: Wieczorek et al. 2012) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource required for the implementation of the test.

Each test is defined to operate on a SingleRecord or a MultiRecord.  The framework allows for MultiRecord tests able to identify outliers within a data set, or other tests that look across data values in a MultiRecord to evaluate data quality.  No BDQ Core tests have been defined to use data in other records within a data set to evaluate the quality of data in a SingleRecord.  The only MultiRecord Tests included in BDQ Core accumulate the outputs of other tests.

### 2.2 Types of Tests (non-normative)

The concept of 'tests' in the context of this standard include four distinct types: Validation (bdqffdq:Validation); Issue (bdqffdq:Issue); Amendment (bdqffdq:Amendment) and Measure (bdqffdq:Measure). 

Each bdqcore: test is an instance of a subclass of bdqffdq:DataQualityNeed (e.g. bdqffdq:Validation) composed with an instance of a subclass of bdqffdq:Method (e.g. bdqffdq:ValidationMethod) composed with an instance of bdqffdq:Specification.  When run by an implementation, each bdqcore: test can produce a data quality report consisting of bdqffdq:Assertions.  See the diagrams and further information in the [bdqffdq: Framework Guide](../guide/bdqffdq/index.md).

#### 2.2.1 Validation Tests (normative)

Each Validation Test is composed of an instance of bdqffdq:Validation (which expresses a data quality need in the abstract) with an instance of bdqffdq:ValidationMethod which links it to an instance of a bdqffdq:Specification (which gives details of how that data quality need is to be concretely assessed).

Validation Tests in BDQ Core evaluate values in one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) for fitness for a particular data quality need. In some cases, Validation Tests check for the presence or the lack of a value. Validation Tests are phrased as positive statements consistent with the Fitness For Use Framework (Veiga et al. 2017). For example, VALIDATION_TAXONRANK_NOTEMPTY will return a Response.status="RUN_HAS_RESULT" and Response.result="COMPLIANT" if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a potential problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result="COMPLIANT". 

The response of a Validation Test (an instance of a bdqffdq:ValidationAssertion) MUST take one of three forms. 

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external resource (e.g. a source authority, bdq:sourceAuthority) is unavailable, and running the same test on the same data at a different time may result in a different result.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the Information Elements are such that the test cannot be meaningfully run.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation:
  - A Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not.

#### 2.2.2 Issue Tests (normative)

Each Issue Test is composed of an instance of bdqffdq:Issue (which expresses a data quality need in the abstract) with an instance of bdqffdq:IssueMethod which links it to an instance of a bdqffdq:Specification (which gives details of how that data quality need is to be concretely assessed).

Issue Tests are a form of warning flag where the test is drawing attention to potential problem with the value of an Information Element for at least one use of the data.

We have used Issue Tests for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of this case would take human review. For example, ISSUE_ANNOTATION_NOTEMPTY is informing the tester than there is at least one annotation associated with record and this should be evaluated before using the record. Similarly for the other two ISSUE-type tests: ISSUE_DATAGENERALIZATIONS_NOTEMPTY where some form of transformation has occurred, and ISSUE_ESTABLISHMENTMEANS_NOTEMPTY where the value needs to be assessed for utility.

The response of an Issue Test (an instance of a bdqffdq:IssueAssertion) MUST take one of three forms. 

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external resource (e.g. a source authority, bdq:sourceAuthority) is unavailable, and running the same test on the same data at a different time may result in a different result.  In this case, the Response.result MUST be empty.  
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the Information Elements are such that the test cannot be meaningfully run.  In this case, the Response.result MUST be empty.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this case:
  - A Response.result="POTENTIAL_ISSUE", a Response.result="NOT_ISSUE", or a Response.result="IS_ISSUE".

In each case, a Response.comment MUST be present with text explaining to consumers of the data quality report why the the test produced this response in this case.

None of the currently defined BDQ Core Issue tests return a Response.result of IS_ISSUE

#### 2.2.3 Amendment Tests (normative) 

Each Amendment Test is composed of an instance of bdqffdq:Amendment (which expresses how to improve data to fit a data quality need in the abstract) with an instance of bdqffdq:AmendmentMethod which links it to an instance of a bdqffdq:Specification (which gives details of how proposals could be made to improve data for that need).

An Amendment Test MAY propose a change to one or more Darwin Core Term values, or MAY propose to fill in missing values.  The Assertion produced by an Amendment is intended to improve one or more components of the quality of the record.  The Response.result from an Amendment MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for QualityControl of an existing database or record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  Amendments, under the framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in these tests.

The response of an Amendment Test (an instance of a bdqffdq:AmendmentAssertion) MUST take one of four forms. 

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external resource (e.g. a source authority, bdq:sourceAuthority) is unavailable, and running the same test on the same data at a different time may result in a different result.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the Information Elements are such that the test cannot be meaningfully run.
3. A Response.status of "FILLED_IN" when the prerequisites for running the test have been met and a proposal is made to fill in a value for one or more input terms that were empty, and in this situation:
  - A Response.result containing a list of key-value pairs of the terms for which values are to be filled in, and the proposed new values for those terms.
3. A Response.status of "AMENDED" when the prerequisites for running the test have been met and a proposal is made to change a value for one or more input terms that were empty, and in this situation:
  - A Response.result containing a list of key-value pairs of the terms for which new values are proposed, and the proposed new values for those terms.

In each case, a Response.comment MUST be present with text explaining to consumers of the data quality report why the the test produced this response in this case.

#### 2.2.4 Measure Tests (normative) 

Each Measure Test is composed of an instance of bdqffdq:Measure (which expresses how measure fittnes of data for a data quality need in the abstract) with an instance of bdqffdq:MeasurementMethod which links it to an instance of a bdqffdq:Specification (which gives details of how that data quality is to be measured).

Measure Tests return a Response.result of either a numeric value or one of the values "COMPLETE" or "NOT_COMPLETE".  Measure Tests may directly measure properties of data.  Alternatively, Measure Tests may measure the outputs of other tests, for example, a Measure may count the number of Response.results from all Validation run on a single record that are COMPLIANT.

The only Measure defined in BDQ Core that directly examines data is MEASURE_EVENTDATE_DURATIONINSECONDS.  It returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the VALIDATIONs and AMENDMENTs and in one case provides an indication of the length of the period of the value of dwc:eventDate.

Most SingleRecord Measure Tests defined in BDQ Core count the number of Validation or Amendment Tests with a specified Response.Result in a bdqffdq:SingleRecord. 

The response of a Measure Test (an instance of a bdqffdq:MeasureAssertion) MUST take one of three forms. 

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external resource (e.g. a source authority, bdq:sourceAuthority) is unavailable, and running the same test on the same data at a different time may result in a different result.  In this case, the Response.result MUST be empty.  
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the Information Elements are such that the test cannot be meaningfully run.  In this case, the Response.result MUST be empty.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this case either:
  - A Response.result="COMPLETE", or a Response.result="NOT_COMPLETE".
  - or
  - A Response.result containing a single number.

In each case, a Response.comment MUST be present with text explaining to consumers of the data quality report why the the test produced this response in this case.

#### 2.3 SingleRecord and MultiRecord Tests (non-normative) 

Tests may operate on a bdqffdq:SingleRecord (e.g. one row of Flat Darwin Core) or on a bdqffdq:MultiRecord (a data set).  

The bdqffdq Framework allows for tests of all types to operate on (bdqffdq:hasResourceType) either SingleRecords or MultiRecords.  In BDQ Core, the only MultiRecord tests that have been defined are Measures.  We refer to these as MultiRecord Measures (instances of bdqffdq:Measure that are the subject of a bdqffdq:hasResourceType property who's object is bdqffdq:MultiRecord).   

The focus of the BDQ Core tests are the SingleRecord tests.  To allow for standard means for sumarizing the results of these tests, and for filtering data under Quality Assurance, we have also defined two sets of MultiRecord Measures. 

In BDQ Core, for each SingleRecord Validation Test, we have defined a MultiRecord Measure Test that returns a Response.result="COMPLETE" when all records in the MultiRecord have a Response.result="COMPLIANT", and a Response.result="NOT_COMPLETE" when they are not. Under Quality Assurance, these Measure Tests are the key criterion for identifying data which have quality for a Use Case. Under Quality Assurance, a MultiRecord is filtered to remove records that do not fit the MultiRecord Measure Tests for completeness, such that a filtered MultiRecord has Response.result="COMPLETE" for all MultiRecord Measure Tests.

In BDQ Core, for each SingleRecord Validation Test, we have also defined a MultiRecord Measure Test that returns a Response.result counting the number of Response.results from that Validation Test that are COMPLIANT (or in a few cases, COMPLIANT or INTERNAL_PREREQUSIITES_NOT_MET).  Under Quality Control, these MultiRecord Measures allow calculation of how much the quality of a data set would be improved by accepting changes proposed by Amendments, and allow identification of areas in the data where quality improvement is most needed to fit the needs of some Use Case.

See the [bdqcore mathematical formulation](../bdqffdq/index.md#5-fitness-for-use-framework-summary-of-mathematical-formalization-normative) for the formal expression of how measures are intended to be used used in Quality Control and Quality Assurance.

### 2.4 Example RDF (non-normative) 

A more complete description of the tests can be found in the RDF representation of this vocabulary.  Following the bdqffdq: Framework, a test is composed of an instance of a subclass of a bdqffdq:DataQualityNeed (e.g. bdqffdq:Validation), an instance of a bdqffdq:ActedUpon information element, optionally an instance of a bdqffdq:Consulted information element, an instance of a subclass of bdqffdq:Method (e.g. bdqffdq:ValidationMethod), and an instance of a bdqffdq:Specification.  Most of the information associated with a bdqffdq:term is expressed in other vocabularies, in particular bdqffdq:.   This structure and dependence on other vocabularies can be seen in the example below of https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

    <rdf:Description rdf:about="https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Validation"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<skos:prefLabel rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Validation dwc:countryCode Standard for SingleRecord</skos:prefLabel
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

## 3 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of classes and object properties in the `bdqffdq:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqdim/terms), resources MUST be used as values of the `bdqdim:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqenh/terms), resources MUST be used as values of the `bdqenh:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqcrit/terms), resources MUST be used as values of the `bdqcrit:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdq/terms), resources MUST be used as values of the `bdq:` namespace.

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of the `bdqcore:` namespace.

### 3.1 Structure of Response (normative)

Responses from each of the Tests MUST be structured data, and MUST NOT be simple pass fail flags,  The Response from a Test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Response.result is the returned result for the Test, i.e. numeric for Measure Tests, a controlled vocabulary (consisting of exactly "COMPLIANT" or "NOT_COMPLIANT") for Validation Tests or for Issue Tests ("NOT_ISSUE" and "POTENTIAL_ISSUE"), either a numeric value or a controlled vocabulary (consisting of exactly "COMPLETE" or "NOT_COMPLETE" for Measure Tests, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendment Tests. 
2. Response.status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the Test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 
3. Response.comment supplies human-readable text describing reasons for the Test result output.

A Response MUST be represented as either RDF or as a data structure.  

When responses are in the form of RDF, the RDF MUST meet the following conditions: 

1. The response MUST be an instance of bdqffdq:Assertion or one of its subclasses (bdqffdq:IssueAssertion, bdqffdq:MeasurementAssertion, bdqffdq:AmendmentAssertion, bdqffdq:IssueAssertion).  An instance of a subclass of bdqffdq:Assertion SHOULD be used.  
2. The Assertion MUST have exactly one bdqffdq:hasResponseStatus object property linking it to one of the named individuals that has type bdqffdq:ResponseStatus (bdqffdq:INTERNAL_PREREQUISITES_NOT_MET, bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET, bdqffdq:NOT_AMENDED, bdqffdq:AMENDED, bdqffdq:FILLED_IN, or bdqffdq:RUN_HAS_RESULT).
3. The Assertion MUST have a bdqffdq:hasResponseResult object property or bdqffdq:hasResponseResultValue data property, unless the object of the bdqffdq:hasResponseStatus indicates that none should be present.
  - If the object of the bdqffdq:hasResponseStatus is bdqffdq:RUN_HAS_RESULT, then the instance of the Assertion MUST have one and only one bdqffdq:hasResponseResult object property linking it to one of the named individuals that has type bdqffdq:ResponseResult (bdqffdq:COMPLETE, bdqffdq:COMPLIANT, bdqffdq:IS_ISSUE, bdqffdq:NOT_COMPLETE, bdqffdq:NOT_COMLIANT, bdqffdq:NOT_ISSUE, or bdqffdq:POTENTIAL_ISSUE).
  - If the object of the bdqffdq:hasResponseStatus is one of bdqffdq:AMENDED or bdqffdq:FILLED_IN, then the instance of the Assertion MUST have one and only one bdqffdq:hasResponseResultValue data property linking it to structured data presenting the result of the Amendment.  The string in the bdqffdq:hasResponseResultValue SHOULD be a json list of key:value pairs, where the keys are specific information elements (e.g. dwc:eventDate), and the values are the new values proposed by the amendment.
  - If the object of the bdqffdq:hasResponseStatus is one of bdqffdq:INTERNAL_PREREQUISITES_NOT_MET, bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET, bdqffdq:NOT_AMENDED, then no bdqffdq:hasResponseResult SHOULD be present.
4. The Assertion MUST have at least one bdqffdq:hasResponseComment data property.  This bdqffdq:hasResponseComment must provide a human readable text explanation of why the conclusion expressed in the assertion was reached.  The bdqffdq:hasResponseComment MAY be repeated to provide the comment in different languages.  Each bdqffdq:hasResponseComment SHOULD be a self standing and complete explanation.
5. The Assertion MAY have a bdqffdq:hasResponseQualifier object property.

When the Response is represented as a data structure in a form other than RDF, the data structure MUST:

1. Have properties corresponding to Response.status, Response.result, and Response.comment.  These properties SHOULD have these names.
2. Have one Response.status property, containing a string constant that MUST be one of the local names of one of the named individuals in bdqffdq with a type bdqffdq:ResponseStatus ( "INTERNAL_PREREQUISITES_NOT_MET", "EXTERNAL_PREREQUISITES_NOT_MET", "NOT_AMENDED", "AMENDED", "FILLED_IN", or "RUN_HAS_RESULT").
3. Have one Response.result property.
  - If the Response.status is "RUN_HAS_RESULT" then the value of the Response.result property MUST be a string constant that is one of the local names of one of the named individuals of type bdqffdq:ResponseResult ("COMPLETE", "COMPLIANT", "IS_ISSUE", "NOT_COMPLETE", "NOT_COMLIANT", "NOT_ISSUE", or "POTENTIAL_ISSUE").
  -  If the Response.status is one of  "AMENDED" or "FILLED_IN" then the value of the Response.result property MUST be structured data presenting the result of the Amendment.  The string in the Response.result SHOULD be a json list of key:value pairs, where the keys are specific information elements (e.g. dwc:eventDate), and the values are the new values proposed by the amendment.
  - If the Response.status is one of "INTERNAL_PREREQUISITES_NOT_MET", "EXTERNAL_PREREQUISITES_NOT_MET", or "NOT_AMENDED", then the Response.result MUST be empty or null.
4. Have one Response.comment property.  This Response.comment must provide a human readable text explanation of why the conclusion expressed in the assertion was reached.  Internationalization of the Response.comment MAY be provided, nothing in this section should be taken as a constraint on how that may be accomplished.
5. A Response.qualifier property may be included.

Nothing in this section should be taken as constraining how data quality reports are presented to consumers of those reports, so long as all three elements of Response.result, Response.status, and Response.comment can be accessed by consumers.

Nothing in this section should be taken as constraining internationalization and languages of labels applied to human readable presentations of Responses from Tests.  

Nothing in this section should be taken as a requirement for a particular format or serialization of bdqffdq:Assertions or Responses. Implementations MAY serialize Assertions in any appropriate form for the context.  When assertions are wrapped in oa:Annotations or presented as linked open data, an RDF representation SHOULD be used.

Nothing in this section should be taken as a requirement to how bdqffdq:Assertions or Responses are to be presented to consumers of data quality reports.  Implementations MAY present the results of Tests in any form appropriate for their consumers.  

### 3.2 Resource Types (normative)

Each Test (each instance of a bdqffdq:DataQualityNeed) MUST have exactly one bdqffdq:hasResourceType object property that relates the test to a ResouceType of bdqffdq:SingleRecord or bdqffdq:MultiRecord.  

Tests operate on data, the data may be understood as representing a single record or multiple records.  In the bdqcore: tests the single record (bdqffdq:SingleRecord) tests MAY be applied to a single of Flat Darwin Core Record, or to a single instance of a Darwin Core Observation, Taxon, Event, or other class, and MAY extend across one to many relations from that class instance to instances of classes of other types in a structured representation of Darwin Core data (Wieczorek et al 2012).  For example,    A bdqcore: SingleRecord test SHOULD NOT take multiple rows of Flat Darwin core as input.  A bdqcore: SingleRecord test SHOULD NOT take multiple objects of the same core type as input when taking structured Darwin Core as input (for example, input data Darwin Core data in RDF should be presented to a SingleRecord test one dwc:Occurrence at a time, although the Occurrence could be linked to multiple other instances of other classes such as identifications).

The bdqcore test ISSUE_ANNOTATION_NOTEMPTY similarly operates on a single Flat Darwin Core record, or a single core Darwin Core class instance, and asks whether annotations exist related to that class, here this standard encourages the implementation of a standard for annotating occurrence records beyond the [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021).

Multi record (bdqffdq:MultiRecord) tests operate on a dataset as a whole, the MultiRecord tests in bdqcore: sum up results across all records for each single record test.

### 3.3 Parameterising the Tests (normative)

Where a Test is parameterized, a parameter (e.g. bdq:sourceAuthority) is specified in the text of the hasExpectedResponse data type property of the instance of the bdqffdq:Specification for the test.  Such a bdqffdq:Specification MUST also have a bdqffdq:hasArgument object property linking it to an instance of a bdqffdq:Argument, which MUST have a bdqffdq:hasArgumentValue data type property carrying the default value for the parameter, and this bdqffdq:Argument MUST have a bdqffdq:hasParameter object property linking it to a bdqffdq:Parameter.  The bdqffdq:Parameter SHOULD be a class instance in the bdq: namespace (e.g. bdq:sourceAuthority).  

The instance of the bdqffdq:Specification SHOULD have a bdqffdq:hasAuthoritiesDefaults data type property containing the parameters, default values, and references to resources, including API enpoints that would provide access to values in authority.   

These elements MUST be understood in concert.

Values of bdqffdq:hasAuthoritiesDefaults SHOULD be a text string listing parameters in the form of a semicolon delimited list of one or more of the following: 
     
- parameter default = "default value" 
- parameter default = "default value" {[resource]}
- parameter default = "default value" {[resource]} {API endpoint [resource]}

The bdqffdq:hasAuthoritiesDefaults data property MAY be used without corresponding bdqffdq:Arguments and bdqffdq:Parameters when a test is not parameterized, but a bdq:sourceAuthority is mentioned within a bdqffdq:hasExpectedResponse for the bdqffdq:Specification and the bdqffdq:hasAuthoritiesDefaults provides details on this source authority.  This usage allows for simpler and easier to read expected responses.

Section [2.3.2 Reading a Specification](../guide/implementers/index.md#232-Reading-a-Specification) of the implementers guide contains additional guidance for handling parameters in test implementations.

#### 3.3.1 Parameter Examples (non-normative)

Examples values for bdqffdq:hasAuthoritiesDefaults: 

     bdq:earliestValidDate default ="1582-11-15"

     bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&amp;name=]}

Example RDF fragment showing use of Arguments and hasAuthoritiesDefaults: 

    <rdf:Description rdf:about="urn:uuid:9f12e2c3-17ac-42c0-91f4-c40a02d3f133">
        <rdf:type rdf:resource="bdqffdq:Argument"/>
        <rdfs:label rdf:datatype="xsd:string">Default value for bdq:maximumValidDepthInMeters:"11000"</rdfs:label>
        <hasArgumentValue xmlns="bdqffdq:" rdf:datatype="xsd:string">11000</hasArgumentValue>
        <hasParameter xmlns="bdqffdq:" rdf:resource="bdq:maximumValidDepthInMeters"/>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:d23e61b3-07b6-4326-bac2-1457b030efef">
        <rdf:type rdf:resource="bdqffdq:Argument"/>
        <rdfs:label rdf:datatype="xsd:string">Default value for bdq:minimumValidDepthInMeters:"0"</rdfs:label>
        <hasArgumentValue xmlns="bdqffdq:" rdf:datatype="xsd:string">0</hasArgumentValue>
        <hasParameter xmlns="bdqffdq:" rdf:resource="bdq:minimumValidDepthInMeters"/>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544">
        <rdf:type rdf:resource="bdqffdq:Specification"/>
        <rdfs:label rdf:datatype="xsd:string">Specification for: VALIDATION_MINDEPTH_INRANGE</rdfs:label>
        <hasArgument xmlns="bdqffdq:" rdf:resource="urn:uuid:9f12e2c3-17ac-42c0-91f4-c40a02d3f133"/>
        <hasArgument xmlns="bdqffdq:" rdf:resource="urn:uuid:d23e61b3-07b6-4326-bac2-1457b030efef"/>
        <hasAuthoritiesDefaults xmlns="bdqffdq:" rdf:datatype="xsd:string">bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</hasAuthoritiesDefaults>
        <hasExpectedResponse xmlns="bdqffdq:" rdf:datatype="xsd:string">INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters is bdq:Empty, or the value is not interpretable as number greater than or equal to zero; COMPLIANT if the value of dwc:minimumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT</hasExpectedResponse>
        ...
    </rdf:Description>

Example RDF Fragment from Specification for VALIDATION_COUNTRYCODE_STANDARD, where bdqffdq:hasAuthoritiesDefaults is present to provide a bdq:sourceAuthority for the Specificaiton, but the test is not parameterized, so no hasArgument properties are present: 

    <hasAuthoritiesDefaults xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</hasAuthoritiesDefaults>
    <hasExpectedResponse xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</hasExpectedResponse


## 4 Term indices
