<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

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
- [1.1 Purpose](#11-purpose)
- [1.2 Audience](#12-audience)
- [1.3 Associated Documents](#13-associated-documents)
- [1.3.1 Term List Distributions for BDQ Core](#131-term-list-distributions-for-bdq-core)
- [1.4 Status of the Content of this Document](#14-status-of-the-content-of-this-document)
- [1.5 RFC 2119 key words](#15-rfc-2119-key-words)
- [1.6 Namespace Abbreviations](#16-namespace-abbreviations)
- [2 A Brief Context for the BDQ Core Tests](#2-a-brief-context-for-the-bdq-core-tests)
- [2.1 Characteristics of the Tests (non-normative)](#21-characteristics-of-the-tests-non-normative)
- [2.2 Types of Tests (non-normative)](#22-types-of-tests-non-normative)
- [2.2.1 Validation Tests (normative)](#221-validation-tests-normative)
- [2.2.2 Issue Tests (normative)](#222-issue-tests-normative)
- [2.2.3 Amendment Tests (normative)](#223-amendment-tests-normative)
- [2.2.4 Measure Tests (normative)](#224-measure-tests-normative)
- [2.3 SingleRecord and MultiRecord Tests (non-normative)](#23-singlerecord-and-multirecord-tests-non-normative)
- [2.4 Example RDF (non-normative)](#24-example-rdf-non-normative)
- [3 Use of Terms (normative)](#3-use-of-terms-normative)
- [3.1 Structure of Response (normative)](#31-structure-of-response-normative)
- [3.2 Resource Types (normative)](#32-resource-types-normative)
- [3.3 Parameterising the Tests (normative)](#33-parameterising-the-tests-normative)
- [3.3.1 Parameter Examples (non-normative)](#331-parameter-examples-non-normative)
- [4 Term indices](#4-term-indices)
- [4.1 Index By Test Label](#41-index-by-test-label)
- [5 Vocabulary Summary](#5-vocabulary-summary)


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

### 1.4 Status of the Content of this Document

Sections 1 is non-normative.

Portions of section 2 are normative and portions are non-normative.

Section 3 is normative.

Section 4 is non-normative.

Section 5 is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

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

Validation Tests in BDQ Core evaluate values in one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) for fitness for a particular data quality need. In some cases, Validation Tests check for the presence or the lack of a value. Validation Tests are phrased as positive statements consistent with the Fitness For Use Framework (Veiga et al. 2017). For example, [VALIDATION_TAXONRANK_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/14da5b87-8304-4b2b-911d-117e3c29e890) will return a Response.status="RUN_HAS_RESULT" and Response.result="COMPLIANT" if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a potential problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result="COMPLIANT". 

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

A more complete description of the tests can be found in the RDF representation of this vocabulary.  Following the bdqffdq: Framework, a test is composed of an instance of a subclass of a bdqffdq:DataQualityNeed (e.g. bdqffdq:Validation), an instance of a bdqffdq:ActedUpon information element, optionally an instance of a bdqffdq:Consulted information element, an instance of a subclass of bdqffdq:Method (e.g. bdqffdq:ValidationMethod), and an instance of a bdqffdq:Specification.  Most of the information associated with a bdqffdq:term is expressed in other vocabularies, in particular bdqffdq:.  This structure and dependence on other vocabularies can be seen in the example below of [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe).

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

Example RDF Fragment from Specification for [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe), where bdqffdq:hasAuthoritiesDefaults is present to provide a bdq:sourceAuthority for the Specificaiton, but the test is not parameterized, so no hasArgument properties are present: 

    <hasAuthoritiesDefaults xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</hasAuthoritiesDefaults>
    <hasExpectedResponse xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</hasExpectedResponse


## 4 Term indices


### 4.1 Index By Test Label


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

## 5 Vocabulary Summary
- <a id="bdqcore_07c28ace-561a-476e-a9b9-3d5ad6e35933"></a>AMENDMENT_BASISOFRECORD_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_BASISOFRECORD_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_07c28ace-561a-476e-a9b9-3d5ad6e35933)

- <a id="bdqcore_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e"></a>AMENDMENT_COORDINATES_FROM_VERBATIM
  - Description: Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_COORDINATES_FROM_VERBATIM)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e)

- <a id="bdqcore_f2b4a50a-6b2f-4930-b9df-da87b6a21082"></a>AMENDMENT_COORDINATES_TRANSPOSED
  - Description: Proposes an amendment of the signs of dwc:decimalLatitude and/or dwc:decimalLongitude to align the location with the dwc:countryCode.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_COORDINATES_TRANSPOSED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_f2b4a50a-6b2f-4930-b9df-da87b6a21082)

- <a id="bdqcore_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae"></a>AMENDMENT_COUNTRYCODE_FROM_COORDINATES
  - Description: Proposes an amendment to the value of dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary from the bdq:countryShapes that is attributable to a single valid country code.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_COUNTRYCODE_FROM_COORDINATES)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae)

- <a id="bdqcore_fec5ffe6-3958-4312-82d9-ebcca0efb350"></a>AMENDMENT_COUNTRYCODE_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:countryCode if it can be interpreted as an ISO country code.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_COUNTRYCODE_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_fec5ffe6-3958-4312-82d9-ebcca0efb350)

- <a id="bdqcore_39bb2280-1215-447b-9221-fd13bc990641"></a>AMENDMENT_DATEIDENTIFIED_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:dateIdentified to a valid ISO date.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_DATEIDENTIFIED_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_39bb2280-1215-447b-9221-fd13bc990641)

- <a id="bdqcore_b129fa4d-b25b-43f7-9645-5ed4d44b357b"></a>AMENDMENT_DAY_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:day as an integer between 1 and 31 inclusive.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_DAY_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_b129fa4d-b25b-43f7-9645-5ed4d44b357b)

- <a id="bdqcore_bd385eeb-44a2-464b-a503-7abe407ef904"></a>AMENDMENT_DCTYPE_STANDARDIZED
  - Description: Proposes an amendment to the value of dc:type using the DCMI type vocabulary.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_DCTYPE_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_bd385eeb-44a2-464b-a503-7abe407ef904)

- <a id="bdqcore_74ef1034-e289-4596-b5b0-cde73796697d"></a>AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:degreeOfEstablishment using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_74ef1034-e289-4596-b5b0-cde73796697d)

- <a id="bdqcore_15d15927-7a22-43f8-88d6-298f5eb45c4c"></a>AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:establishmentMeans using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_15d15927-7a22-43f8-88d6-298f5eb45c4c)

- <a id="bdqcore_6d0a0c10-5e4a-4759-b448-88932f399812"></a>AMENDMENT_EVENTDATE_FROM_VERBATIM
  - Description: Proposes an amendment to the value of dwc:eventDate from the content of dwc:verbatimEventDate.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_EVENTDATE_FROM_VERBATIM)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_6d0a0c10-5e4a-4759-b448-88932f399812)

- <a id="bdqcore_3892f432-ddd0-4a0a-b713-f2e2ecbd879d"></a>AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY
  - Description: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:month and dwc:day.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_3892f432-ddd0-4a0a-b713-f2e2ecbd879d)

- <a id="bdqcore_eb0a44fa-241c-4d64-98df-ad4aa837307b"></a>AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR
  - Description: Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_eb0a44fa-241c-4d64-98df-ad4aa837307b)

- <a id="bdqcore_718dfc3c-cb52-4fca-b8e2-0e722f375da7"></a>AMENDMENT_EVENTDATE_STANDARDIZED
  - Description: Proposes an amendment of the value of dwc:eventDate to a valid ISO date.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_EVENTDATE_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_718dfc3c-cb52-4fca-b8e2-0e722f375da7)

- <a id="bdqcore_710fe118-17e1-440f-b428-88ba3f547d6d"></a>AMENDMENT_EVENT_FROM_EVENTDATE
  - Description: Proposes an amendment to values in any of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear or dwc:endDayOfYear from the content of dwc:eventDate.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_EVENT_FROM_EVENTDATE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_710fe118-17e1-440f-b428-88ba3f547d6d)

- <a id="bdqcore_7498ca76-c4d4-42e2-8103-acacccbdffa7"></a>AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT
  - Description: Proposes an amendment to fill in dwc:geodeticDatum using a prameterized value if the dwc:geodeticDatum is empty.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_7498ca76-c4d4-42e2-8103-acacccbdffa7)

- <a id="bdqcore_0345b325-836d-4235-96d0-3b5caf150fc0"></a>AMENDMENT_GEODETICDATUM_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:geodeticDatum using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_GEODETICDATUM_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_0345b325-836d-4235-96d0-3b5caf150fc0)

- <a id="bdqcore_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8"></a>AMENDMENT_LICENSE_STANDARDIZED
  - Description: Proposes an amendment to the value of dcterms:license using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_LICENSE_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8)

- <a id="bdqcore_c5658b83-4471-4f57-9d94-bf7d0a96900c"></a>AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM
  - Description: Proposes amendments of the values of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be interpreted from dwc:verbatimDepth.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_c5658b83-4471-4f57-9d94-bf7d0a96900c)

- <a id="bdqcore_2d638c8b-4c62-44a0-a14d-fa147bf9823d"></a>AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM
  - Description: Proposes an amendment or amendments to the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be interpreted from dwc:verbatimElevation.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_2d638c8b-4c62-44a0-a14d-fa147bf9823d)

- <a id="bdqcore_2e371d57-1eb3-4fe3-8a61-dff43ced50cf"></a>AMENDMENT_MONTH_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:month as an integer between 1 and 12 inclusive.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_MONTH_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_2e371d57-1eb3-4fe3-8a61-dff43ced50cf)

- <a id="bdqcore_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5"></a>AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT
  - Description: Proposes an amendment of the value of dwc:occurrenceStatus to the default parameter value if dwc:occurrenceStatus, dwc:individualCount and dwc:organismQuantity are empty.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5)

- <a id="bdqcore_f8f3a093-042c-47a3-971a-a482aaaf3b75"></a>AMENDMENT_OCCURRENCESTATUS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:occurrenceStatus using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_OCCURRENCESTATUS_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_f8f3a093-042c-47a3-971a-a482aaaf3b75)

- <a id="bdqcore_f9205977-f145-44f5-8cb9-e3e2e35ce908"></a>AMENDMENT_PATHWAY_STANDARDIZED
  - Description: Propose an amendment to the value of dwc:pathway using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_PATHWAY_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_f9205977-f145-44f5-8cb9-e3e2e35ce908)

- <a id="bdqcore_431467d6-9b4b-48fa-a197-cd5379f5e889"></a>AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON
  - Description: Proposes an amendment to the value of dwc:scientificNameID if it can be unambiguously resolved from bdq:sourceAuthority using the available taxon terms.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_431467d6-9b4b-48fa-a197-cd5379f5e889)

- <a id="bdqcore_f01fb3f9-2f7e-418b-9f51-adf50f202aea"></a>AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID
  - Description: Proposes an amendment to the value of dwc:scientificName using the dwc:scientificNameID value from the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_f01fb3f9-2f7e-418b-9f51-adf50f202aea)

- <a id="bdqcore_33c45ae1-e2db-462a-a59e-7169bb01c5d6"></a>AMENDMENT_SEX_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:sex using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_SEX_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_33c45ae1-e2db-462a-a59e-7169bb01c5d6)

- <a id="bdqcore_e39098df-ef46-464c-9aef-bcdeee2a88cb"></a>AMENDMENT_TAXONRANK_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:taxonRank using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_TAXONRANK_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_e39098df-ef46-464c-9aef-bcdeee2a88cb)

- <a id="bdqcore_b3471c65-b53e-453b-8282-abfa27bf1805"></a>AMENDMENT_TYPESTATUS_STANDARDIZED
  - Description: Proposes an amendment to the value of dwc:typeStatus using the bdq:sourceAuthority.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#AMENDMENT_TYPESTATUS_STANDARDIZED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_b3471c65-b53e-453b-8282-abfa27bf1805)

- <a id="bdqcore_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1"></a>ISSUE_ANNOTATION_NOTEMPTY
  - Description: Are there any annotations associated with the record?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#ISSUE_ANNOTATION_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1)

- <a id="bdqcore_256e51b3-1e08-4349-bb7e-5186631c3f8e"></a>ISSUE_COORDINATES_CENTEROFCOUNTRY
  - Description: Are the supplied geographic coordinates within a defined buffer of the center of the country?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#ISSUE_COORDINATES_CENTEROFCOUNTRY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_256e51b3-1e08-4349-bb7e-5186631c3f8e)

- <a id="bdqcore_13d5a10e-188e-40fd-a22c-dbaa87b91df2"></a>ISSUE_DATAGENERALIZATIONS_NOTEMPTY
  - Description: Is there a value in dwc:dataGeneralizations?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_13d5a10e-188e-40fd-a22c-dbaa87b91df2)

- <a id="bdqcore_acc8dff2-d8d1-483a-946d-65a02a452700"></a>ISSUE_ESTABLISHMENTMEANS_NOTEMPTY
  - Description: Is there a value in dwc:establishmentMeans?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#ISSUE_ESTABLISHMENTMEANS_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_acc8dff2-d8d1-483a-946d-65a02a452700)

- <a id="bdqcore_03049fe5-a575-404f-b564-ae63f5a1cf8b"></a>MEASURE_AMENDMENTS_PROPOSED
  - Description: A count of the number of distinct AMENDMENT tests that have a Response.status="AMENDED" for a given record.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#MEASURE_AMENDMENTS_PROPOSED)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_03049fe5-a575-404f-b564-ae63f5a1cf8b)

- <a id="bdqcore_56b6c695-adf1-418e-95d2-da04cad7be53"></a>MEASURE_EVENTDATE_DURATIONINSECONDS
  - Description: What is the duration of dwc:eventDate in seconds?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_56b6c695-adf1-418e-95d2-da04cad7be53)

- <a id="bdqcore_45fb49eb-4a1b-4b49-876f-15d5034dfc73"></a>MEASURE_VALIDATIONTESTS_COMPLIANT
  - Description: Measures the number of distinct VALIDATION tests that have a Response.status="COMPLIANT" for a given record.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#MEASURE_VALIDATIONTESTS_COMPLIANT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_45fb49eb-4a1b-4b49-876f-15d5034dfc73)

- <a id="bdqcore_453844ae-9df4-439f-8e24-c52498eca84a"></a>MEASURE_VALIDATIONTESTS_NOTCOMPLIANT
  - Description: A count of the number of distinct VALIDATION tests that have a Response.status="NOT_COMPLIANT" for a given record.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_453844ae-9df4-439f-8e24-c52498eca84a)

- <a id="bdqcore_49a94636-a562-4e6b-803c-665c80628a3d"></a>MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET
  - Description: The number of distinct VALIDATION tests that have a Response.status="EXTERNAL_PREREQUISITES_NOT_MET" or "INTERNAL_PREREQUISITES_NOT_MET" for a given record.
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_49a94636-a562-4e6b-803c-665c80628a3d)

- <a id="bdqcore_ac2b7648-d5f9-48ca-9b07-8ad5879a2536"></a>VALIDATION_BASISOFRECORD_NOTEMPTY
  - Description: Is there a value in dwc:basisOfRecord?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_BASISOFRECORD_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_ac2b7648-d5f9-48ca-9b07-8ad5879a2536)

- <a id="bdqcore_42408a00-bf71-4892-a399-4325e2bc1fb8"></a>VALIDATION_BASISOFRECORD_STANDARD
  - Description: Does the value of dwc:basisOfRecord occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_BASISOFRECORD_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_42408a00-bf71-4892-a399-4325e2bc1fb8)

- <a id="bdqcore_2750c040-1d4a-4149-99fe-0512785f2d5f"></a>VALIDATION_CLASSIFICATION_CONSISTENT
  - Description: Is the combination of higher classification taxonomic terms consistent using bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_CLASSIFICATION_CONSISTENT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_2750c040-1d4a-4149-99fe-0512785f2d5f)

- <a id="bdqcore_2cd6884e-3d14-4476-94f7-1191cfff309b"></a>VALIDATION_CLASS_FOUND
  - Description: Does the value of dwc:class occur at rank of Class in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_CLASS_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_2cd6884e-3d14-4476-94f7-1191cfff309b)

- <a id="bdqcore_adb27d29-9f0d-4d52-b760-a77ba57a69c9"></a>VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT
  - Description: Do the geographic coordinates fall on or within the boundaries of the territory given in dwc:countryCode or its Exclusive Economic Zone?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_adb27d29-9f0d-4d52-b760-a77ba57a69c9)

- <a id="bdqcore_f18a470b-3fe1-4aae-9c65-a6d3db6b550c"></a>VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT
  - Description: Do the geographic coordinates fall on or within the boundary from the bdq:sourceAuthority for the given dwc:stateProvince or within the distance given by bdq:spatialBufferInMeters outside that boundary?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_f18a470b-3fe1-4aae-9c65-a6d3db6b550c)

- <a id="bdqcore_b9c184ce-a859-410c-9d12-71a338200380"></a>VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT
  - Description: Does the marine/non-marine biome of a taxon from the bdq:sourceAuthority match the biome at the location given by the coordinates?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_b9c184ce-a859-410c-9d12-71a338200380)

- <a id="bdqcore_1bf0e210-6792-4128-b8cc-ab6828aa4871"></a>VALIDATION_COORDINATES_NOTZERO
  - Description: Are the values of either dwc:decimalLatitude or dwc:decimalLongitude numbers that are not equal to 0?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COORDINATES_NOTZERO)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_1bf0e210-6792-4128-b8cc-ab6828aa4871)

- <a id="bdqcore_c6adf2ea-3051-4498-97f4-4b2f8a105f57"></a>VALIDATION_COORDINATEUNCERTAINTY_INRANGE
  - Description: Is the value of dwc:coordinateUncertaintyInMeters a number between 1 and 20,037,509?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COORDINATEUNCERTAINTY_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_c6adf2ea-3051-4498-97f4-4b2f8a105f57)

- <a id="bdqcore_853b79a2-b314-44a2-ae46-34a1e7ed85e4"></a>VALIDATION_COUNTRYCODE_NOTEMPTY
  - Description: Is there a value in dwc:countryCode?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COUNTRYCODE_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_853b79a2-b314-44a2-ae46-34a1e7ed85e4)

- <a id="bdqcore_0493bcfb-652e-4d17-815b-b0cce0742fbe"></a>VALIDATION_COUNTRYCODE_STANDARD
  - Description: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COUNTRYCODE_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_0493bcfb-652e-4d17-815b-b0cce0742fbe)

- <a id="bdqcore_b23110e7-1be7-444a-a677-cdee0cf4330c"></a>VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT
  - Description: Does the ISO country code, determined from the value of dwc:country, equal the value of dwc:countryCode?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_b23110e7-1be7-444a-a677-cdee0cf4330c)

- <a id="bdqcore_d257eb98-27cb-48e5-8d3c-ab9fca4edd11"></a>VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS
  - Description: Is the combination of the values of the terms dwc:country, dwc:stateProvince unique in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_d257eb98-27cb-48e5-8d3c-ab9fca4edd11)

- <a id="bdqcore_69b2efdc-6269-45a4-aecb-4cb99c2ae134"></a>VALIDATION_COUNTRY_FOUND
  - Description: Does the value of dwc:country occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COUNTRY_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_69b2efdc-6269-45a4-aecb-4cb99c2ae134)

- <a id="bdqcore_6ce2b2b4-6afe-4d13-82a0-390d31ade01c"></a>VALIDATION_COUNTRY_NOTEMPTY
  - Description: Is there a value in dwc:country?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_COUNTRY_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_6ce2b2b4-6afe-4d13-82a0-390d31ade01c)

- <a id="bdqcore_dc8aae4b-134f-4d75-8a71-c4186239178e"></a>VALIDATION_DATEIDENTIFIED_INRANGE
  - Description: Is the value of dwc:dateIdentified within Parameter ranges and either overlap or is later than dwc:eventDate?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DATEIDENTIFIED_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_dc8aae4b-134f-4d75-8a71-c4186239178e)

- <a id="bdqcore_66269bdd-9271-4e76-b25c-7ab81eebe1d8"></a>VALIDATION_DATEIDENTIFIED_STANDARD
  - Description: Is the value of dwc:dateIdentified a valid ISO date?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DATEIDENTIFIED_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_66269bdd-9271-4e76-b25c-7ab81eebe1d8)

- <a id="bdqcore_8d787cb5-73e2-4c39-9cd1-67c7361dc02e"></a>VALIDATION_DAY_INRANGE
  - Description: Is the value of dwc:day interpretable as a valid integer between 1 and 28 inclusive or 29, 30 or 31 given the relative month and year?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DAY_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_8d787cb5-73e2-4c39-9cd1-67c7361dc02e)

- <a id="bdqcore_47ff73ba-0028-4f79-9ce1-ee7008d66498"></a>VALIDATION_DAY_STANDARD
  - Description: Is the value of dwc:day an integer between 1 and 31 inclusive?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DAY_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_47ff73ba-0028-4f79-9ce1-ee7008d66498)

- <a id="bdqcore_374b091a-fc90-4791-91e5-c1557c649169"></a>VALIDATION_DCTYPE_NOTEMPTY
  - Description: Is there a value in dc:type?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DCTYPE_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_374b091a-fc90-4791-91e5-c1557c649169)

- <a id="bdqcore_cdaabb0d-a863-49d0-bc0f-738d771acba5"></a>VALIDATION_DCTYPE_STANDARD
  - Description: Does the value in dc:type occur as a value in the DCMI type vocabulary?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DCTYPE_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_cdaabb0d-a863-49d0-bc0f-738d771acba5)

- <a id="bdqcore_b6ecda2a-ce36-437a-b515-3ae94948fe83"></a>VALIDATION_DECIMALLATITUDE_INRANGE
  - Description: Is the value of dwc:decimalLatitude a number between -90 and 90 inclusive?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DECIMALLATITUDE_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_b6ecda2a-ce36-437a-b515-3ae94948fe83)

- <a id="bdqcore_7d2485d5-1ba7-4f25-90cb-f4480ff1a275"></a>VALIDATION_DECIMALLATITUDE_NOTEMPTY
  - Description: Is there a value in dwc:decimalLatitude?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DECIMALLATITUDE_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_7d2485d5-1ba7-4f25-90cb-f4480ff1a275)

- <a id="bdqcore_0949110d-c06b-450e-9649-7c1374d940d1"></a>VALIDATION_DECIMALLONGITUDE_INRANGE
  - Description: Is the value of dwc:decimalLongitude a number between -180 and 180 inclusive?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DECIMALLONGITUDE_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_0949110d-c06b-450e-9649-7c1374d940d1)

- <a id="bdqcore_9beb9442-d942-4f42-8b6a-fcea01ee086a"></a>VALIDATION_DECIMALLONGITUDE_NOTEMPTY
  - Description: Is there a value in dwc:decimalLongitude?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DECIMALLONGITUDE_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_9beb9442-d942-4f42-8b6a-fcea01ee086a)

- <a id="bdqcore_060e7734-607d-4737-8b2c-bfa17788bf1a"></a>VALIDATION_DEGREEOFESTABLISHMENT_STANDARD
  - Description: Does the value of dwc:degreeOfEstablishment occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_DEGREEOFESTABLISHMENT_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_060e7734-607d-4737-8b2c-bfa17788bf1a)

- <a id="bdqcore_9a39d88c-7eee-46df-b32a-c109f9f81fb8"></a>VALIDATION_ENDDAYOFYEAR_INRANGE
  - Description: Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_ENDDAYOFYEAR_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_9a39d88c-7eee-46df-b32a-c109f9f81fb8)

- <a id="bdqcore_4eb48fdf-7299-4d63-9d08-246902e2857f"></a>VALIDATION_ESTABLISHMENTMEANS_STANDARD
  - Description: Does the value of dwc:establishmentMeans occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_ESTABLISHMENTMEANS_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_4eb48fdf-7299-4d63-9d08-246902e2857f)

- <a id="bdqcore_3cff4dc4-72e9-4abe-9bf3-8a30f1618432"></a>VALIDATION_EVENTDATE_INRANGE
  - Description: Is the value of dwc:eventDate entirely with the Parameter Range?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_EVENTDATE_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_3cff4dc4-72e9-4abe-9bf3-8a30f1618432)

- <a id="bdqcore_f51e15a6-a67d-4729-9c28-3766299d2985"></a>VALIDATION_EVENTDATE_NOTEMPTY
  - Description: Is there a value in dwc:eventDate?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_EVENTDATE_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_f51e15a6-a67d-4729-9c28-3766299d2985)

- <a id="bdqcore_4f2bf8fd-fc5c-493f-a44c-e7b16153c803"></a>VALIDATION_EVENTDATE_STANDARD
  - Description: Is the value of dwc:eventDate a valid ISO date?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_EVENTDATE_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_4f2bf8fd-fc5c-493f-a44c-e7b16153c803)

- <a id="bdqcore_41267642-60ff-4116-90eb-499fee2cd83f"></a>VALIDATION_EVENTTEMPORAL_NOTEMPTY
  - Description: Is there a value in any of the terms dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_EVENTTEMPORAL_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_41267642-60ff-4116-90eb-499fee2cd83f)

- <a id="bdqcore_5618f083-d55a-4ac2-92b5-b9fb227b832f"></a>VALIDATION_EVENT_CONSISTENT
  - Description: Are the values in dwc:eventDate consistent with the values in dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_EVENT_CONSISTENT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_5618f083-d55a-4ac2-92b5-b9fb227b832f)

- <a id="bdqcore_3667556d-d8f5-454c-922b-af8af38f613c"></a>VALIDATION_FAMILY_FOUND
  - Description: Does the value of dwc:family occur at rank of Family in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_FAMILY_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_3667556d-d8f5-454c-922b-af8af38f613c)

- <a id="bdqcore_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec"></a>VALIDATION_GENUS_FOUND
  - Description: Does the value of dwc:genus occur at the rank of Genus in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_GENUS_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec)

- <a id="bdqcore_239ec40e-a729-4a8e-ba69-e0bf03ac1c44"></a>VALIDATION_GEODETICDATUM_NOTEMPTY
  - Description: Is there a value in dwc:geodeticDatum?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_GEODETICDATUM_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_239ec40e-a729-4a8e-ba69-e0bf03ac1c44)

- <a id="bdqcore_7e0c0418-fe16-4a39-98bd-80e19d95b9d1"></a>VALIDATION_GEODETICDATUM_STANDARD
  - Description: Does the value of dwc:geodeticDatum occur as a valid geographic CRS, geodetic Datum or ellipsoid in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_GEODETICDATUM_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_7e0c0418-fe16-4a39-98bd-80e19d95b9d1)

- <a id="bdqcore_125b5493-052d-4a0d-a3e1-ed5bf792689e"></a>VALIDATION_KINGDOM_FOUND
  - Description: Does the value of dwc:kingdom occur at rank of Kingdom in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_KINGDOM_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_125b5493-052d-4a0d-a3e1-ed5bf792689e)

- <a id="bdqcore_36ed36c9-b1a7-40b2-b5e2-0d012e772098"></a>VALIDATION_KINGDOM_NOTEMPTY
  - Description: Is there a value in dwc:kingdom?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_KINGDOM_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_36ed36c9-b1a7-40b2-b5e2-0d012e772098)

- <a id="bdqcore_15f78619-811a-4c6f-997a-a4c7888ad849"></a>VALIDATION_LICENSE_NOTEMPTY
  - Description: Is there a value in dcterms:license?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_LICENSE_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_15f78619-811a-4c6f-997a-a4c7888ad849)

- <a id="bdqcore_3136236e-04b6-49ea-8b34-a65f25e3aba1"></a>VALIDATION_LICENSE_STANDARD
  - Description: Does the value of dcterms:license occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_LICENSE_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_3136236e-04b6-49ea-8b34-a65f25e3aba1)

- <a id="bdqcore_58486cb6-1114-4a8a-ba1e-bd89cfe887e9"></a>VALIDATION_LOCATION_NOTEMPTY
  - Description: Is there a value in any of the Darwin Core spatial terms that could specify a location?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_LOCATION_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_58486cb6-1114-4a8a-ba1e-bd89cfe887e9)

- <a id="bdqcore_3f1db29a-bfa5-40db-9fd1-fde020d81939"></a>VALIDATION_MAXDEPTH_INRANGE
  - Description: Is the value of dwc:maximumDepthInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_MAXDEPTH_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_3f1db29a-bfa5-40db-9fd1-fde020d81939)

- <a id="bdqcore_c971fe3f-84c1-4636-9f44-b1ec31fd63c7"></a>VALIDATION_MAXELEVATION_INRANGE
  - Description: Is the value of dwc:maximumElevationInMeters of a single record within a valid range?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_MAXELEVATION_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_c971fe3f-84c1-4636-9f44-b1ec31fd63c7)

- <a id="bdqcore_04b2c8f3-c71b-4e95-8e43-f70374c5fb92"></a>VALIDATION_MINDEPTH_INRANGE
  - Description: Is the value of dwc:minimumDepthInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_MINDEPTH_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_04b2c8f3-c71b-4e95-8e43-f70374c5fb92)

- <a id="bdqcore_8f1e6e58-544b-4365-a569-fb781341644e"></a>VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH
  - Description: Is the value of dwc:minimumDepthInMeters a number that is less than or equal to the value of dwc:maximumDepthInMeters?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_8f1e6e58-544b-4365-a569-fb781341644e)

- <a id="bdqcore_0bb8297d-8f8a-42d2-80c1-558f29efe798"></a>VALIDATION_MINELEVATION_INRANGE
  - Description: Is the value of dwc:minimumElevationInMeters within the Parameter range?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_MINELEVATION_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_0bb8297d-8f8a-42d2-80c1-558f29efe798)

- <a id="bdqcore_d708526b-6561-438e-aa1a-82cd80b06396"></a>VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION
  - Description: Is the value of dwc:minimumElevationInMeters a number less than or equal to the value of dwc:maximumElevationInMeters?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_d708526b-6561-438e-aa1a-82cd80b06396)

- <a id="bdqcore_01c6dafa-0886-4b7e-9881-2c3018c98bdc"></a>VALIDATION_MONTH_STANDARD
  - Description: Is the value of dwc:month interpretable as an integer between 1 and 12 inclusive?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_MONTH_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_01c6dafa-0886-4b7e-9881-2c3018c98bdc)

- <a id="bdqcore_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70"></a>VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY
  - Description: Is there a value in dwc:namePublishedInYear?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70)

- <a id="bdqcore_c486546c-e6e5-48a7-b286-eba7f5ca56c4"></a>VALIDATION_OCCURRENCEID_NOTEMPTY
  - Description: Is there a value in dwc:occurrenceID?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_OCCURRENCEID_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_c486546c-e6e5-48a7-b286-eba7f5ca56c4)

- <a id="bdqcore_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf"></a>VALIDATION_OCCURRENCESTATUS_NOTEMPTY
  - Description: Is there a value in dwc:occurrenceStatus?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_OCCURRENCESTATUS_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf)

- <a id="bdqcore_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47"></a>VALIDATION_OCCURRENCESTATUS_STANDARD
  - Description: Does the value of dwc:occurrenceStatus occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_OCCURRENCESTATUS_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47)

- <a id="bdqcore_81cc974d-43cc-4c0f-a5e0-afa23b455aa3"></a>VALIDATION_ORDER_FOUND
  - Description: Does the value of dwc:order occur at rank of Order in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_ORDER_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_81cc974d-43cc-4c0f-a5e0-afa23b455aa3)

- <a id="bdqcore_5424e933-bee7-4125-839e-d8743ea69f93"></a>VALIDATION_PATHWAY_STANDARD
  - Description: Does the value of dwc:pathway occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_PATHWAY_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_5424e933-bee7-4125-839e-d8743ea69f93)

- <a id="bdqcore_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f"></a>VALIDATION_PHYLUM_FOUND
  - Description: Does the value of dwc:phylum occur at rank of Phylum in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_PHYLUM_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f)

- <a id="bdqcore_17f03f1f-f74d-40c0-8071-2927cfc9487b"></a>VALIDATION_POLYNOMIAL_CONSISTENT
  - Description: Is the polynomial represented in dwc:scientificName consistent with the equivalent values in dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_POLYNOMIAL_CONSISTENT)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_17f03f1f-f74d-40c0-8071-2927cfc9487b)

- <a id="bdqcore_49f1d386-5bed-43ae-bd43-deabf7df64fc"></a>VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
  - Description: Is there a value in dwc:scientificNameAuthorship?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_49f1d386-5bed-43ae-bd43-deabf7df64fc)

- <a id="bdqcore_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8"></a>VALIDATION_SCIENTIFICNAMEID_COMPLETE
  - Description: Does the value of dwc:scientificNameID contain a complete identifier?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_SCIENTIFICNAMEID_COMPLETE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8)

- <a id="bdqcore_401bf207-9a55-4dff-88a5-abcd58ad97fa"></a>VALIDATION_SCIENTIFICNAMEID_NOTEMPTY
  - Description: Is there a value in dwc:scientificNameID?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_SCIENTIFICNAMEID_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_401bf207-9a55-4dff-88a5-abcd58ad97fa)

- <a id="bdqcore_3f335517-f442-4b98-b149-1e87ff16de45"></a>VALIDATION_SCIENTIFICNAME_FOUND
  - Description: Is there a match of the contents of dwc:scientificName with the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_SCIENTIFICNAME_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_3f335517-f442-4b98-b149-1e87ff16de45)

- <a id="bdqcore_7c4b9498-a8d9-4ebb-85f1-9f200c788595"></a>VALIDATION_SCIENTIFICNAME_NOTEMPTY
  - Description: Is there a value in dwc:scientificName?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_7c4b9498-a8d9-4ebb-85f1-9f200c788595)

- <a id="bdqcore_88d8598b-3318-483d-9475-a5acf9887404"></a>VALIDATION_SEX_STANDARD
  - Description: Does the value of dwc:sex occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_SEX_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_88d8598b-3318-483d-9475-a5acf9887404)

- <a id="bdqcore_85803c7e-2a5a-42e1-b8d3-299a44cafc46"></a>VALIDATION_STARTDAYOFYEAR_INRANGE
  - Description: Is the value of dwc:startDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_STARTDAYOFYEAR_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_85803c7e-2a5a-42e1-b8d3-299a44cafc46)

- <a id="bdqcore_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a"></a>VALIDATION_STATEPROVINCE_FOUND
  - Description: Does the value of dwc:stateProvince occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_STATEPROVINCE_FOUND)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a)

- <a id="bdqcore_14da5b87-8304-4b2b-911d-117e3c29e890"></a>VALIDATION_TAXONRANK_NOTEMPTY
  - Description: Is there a value in dwc:taxonRank?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_TAXONRANK_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_14da5b87-8304-4b2b-911d-117e3c29e890)

- <a id="bdqcore_7bdb13a4-8a51-4ee5-be7f-20693fdb183e"></a>VALIDATION_TAXONRANK_STANDARD
  - Description: Does the value of dwc:taxonRank occur in the bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_TAXONRANK_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_7bdb13a4-8a51-4ee5-be7f-20693fdb183e)

- <a id="bdqcore_06851339-843f-4a43-8422-4e61b9a00e75"></a>VALIDATION_TAXON_NOTEMPTY
  - Description: Is there a value in any of the terms needed to determine that the taxon exists?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_TAXON_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_06851339-843f-4a43-8422-4e61b9a00e75)

- <a id="bdqcore_4c09f127-737b-4686-82a0-7c8e30841590"></a>VALIDATION_TAXON_UNAMBIGUOUS
  - Description: Can the taxon be unambiguously resolved from bdq:sourceAuthority using the available taxon terms?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_TAXON_UNAMBIGUOUS)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_4c09f127-737b-4686-82a0-7c8e30841590)

- <a id="bdqcore_4833a522-12eb-4fe0-b4cf-7f7a337a6048"></a>VALIDATION_TYPESTATUS_STANDARD
  - Description: Does the value of dwc:typeStatus occur in bdq:sourceAuthority?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_TYPESTATUS_STANDARD)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_4833a522-12eb-4fe0-b4cf-7f7a337a6048)

- <a id="bdqcore_ad0c8855-de69-4843-a80c-a5387d20fbc8"></a>VALIDATION_YEAR_INRANGE
  - Description: Is the value of dwc:year within the Parameter range?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_YEAR_INRANGE)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_ad0c8855-de69-4843-a80c-a5387d20fbc8)

- <a id="bdqcore_c09ecbf9-34e3-4f3e-b74a-8796af15e59f"></a>VALIDATION_YEAR_NOTEMPTY
  - Description: Is there a value in dwc:year?
  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#VALIDATION_YEAR_NOTEMPTY)
  - View in Term-List: [Link](../list/bdqcore/index.md#bdqcore_c09ecbf9-34e3-4f3e-b74a-8796af15e59f)


## Acronyms

For a list of Acronyms see [Acronyms](../intro/index.md#5-acronyms) in the Introduction document.

## Glossary

A glossary of terms additional to those in the various namespaces can be found at [Glossary](../intro/index.md#6-glossary) in the Introduction document.

## References

The bibliography for BDQ Core is in the [References](../references/index.md#2-references) document.

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


