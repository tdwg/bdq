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

This document provides introductory explanatory information and normative guidance for the BDQ Core tests. The document includes terms in several namespaces that contain the recommended terms: `bdq:`, `bdqffdq:`, `bdqdim:`, `bdqenh:`, and `bdqcrit:` as well as the focus of this document the `bdqcore:` terms. For details and rationale, see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889.

### 1.1 BDQ Core Test Documents

The BDQ Core vocabulary includes the following documents and files

- [BDQ Core Tests Quick Reference Guide](docs/terms/bdqcore/index.md)
- [BDQ Core Vocabularies](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/vocabularies/index.md)
- Normative guidance on the use of the BDQ Core vocabulary is provided in **this document**.
- The BDQ Core Tests have several distribution files:
      - File: [CSV List of Tests](https://github.com/tdwg/bdq/blob/master/tg2/_review/vocabulary/bdqcore_terms.csv "Convenience CSV list of test descriptors.")
      - File: [Tests in RDF/XML](https://github.com/tdwg/bdq/blob/master/tg2/_review/dist/bdqcore.xml "RDF/XML serialization of OWL representation of the tests descriptors.")
      - File: [Tests in Turtle](https://github.com/tdwg/bdq/blob/master/tg2/_review/dist/bdqcore.ttl "Turtle serialization of OWL representation of the tests descriptors.")
- [BDQ Core User's Guide](docs/guide/users/index.md)
- [BDQ Core Implementer's Guide](docs/guide/implementers/index.md)

### 1.1.1 Term List Distributions for BDQ Core

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcore/index.md | Complete term list  | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.xml | RDF/XML  | 
| Turtle file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcore.ttl | Turtle  | 
| CSV file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqcore_terms.csv | CSV list of tests | 

### Text to move or rewrite

<!--- Material here probably goes into the implementers or users guide --->

Tests may require reference to external data such as standard vocabularies of terms or names. While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

(Make sure to establish that the standard does not specify the "format" of the responses (JSON within an Annotation, etc.), but it does specify the required content regardless of serialization format.)

Tests are paired in that all AMENDMENTs require a corresponding VALIDATION that assesses some aspect of data quality. An AMENDMENT may be able to improve the quality of data with respect to that VALIDATION. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values. 

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, repeated in 5.2.3 --->
The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

For a simplied list of current terms, see the BDQ Core Quick Reference Guide {http://..........}.

(Make sure this is addressed in this document) We acknowledge the centrality of the work of the TDWG Annotations Interest Group (https://github.com/tdwg/annotations) as to how the test results are reported against records. Test results structured with these three components can be readily wrapped in the body annotation document that follows the W3C Web Annotation Data Model (Sanderson et al. 2017), along with metadata from the Framework to describe which test is being reported upon, and metadata within the target of the annotation to describe which data resource is being annotated, and the state it was in at the time of annotation.

<!--- end of information that probably goes in the users or implementers guides --->

### 1.2 Characteristics of the tests (non-normative)

Each test is defined as a SingleRecord test. No CORE tests have been defined to use data in other records within a data set to evaluate the quality of data in a SingleRecord. The framework allows for MultiRecord tests able to identify outliers within a data set, or other tests that look across a MultiRecord to evaluate data quality, but we have not specified any such tests here.

The scope of each test is also largely provided by the bdqffdq:Specification. The Darwin Core terms used in the Specification are included in the "Information Elements". The "Specification" also includes references to external (to the Darwin Core standard) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource required for the implementation of the test.

The tests are agnostic about the form in which the data are stored or transported. The test specifications all assume that data are presented to the tests in structured form such as csv or tab delimited text files, with data elements identifiable as Darwin Core terms (Wieczorek et al. 2012). Here, cells contain non-typed data values possibly aggregated from and serialized from multiple sources such as relational databases where Boolean nulls and non-string data types may exist, but the data have been exported into a string serialization that supports neither null nor typed data. 

The tests are also agnostic about uses for quality assurance, where output data are limited to those for which all Validations are Compliant, or for quality control where the results of Validations, Issues, Measures, and Amendments can be used to improve the quality of the data.

The test specifications are agnostic about where in the biodiversity data lifecycle they are used. Implementers can incorporate the tests at any stage to help identify and correct issues. The tests can be applied during data capture in the field, transcription from paper records, data ingestion into databases, integration with collections management systems, data aggregation, and research on aggregated biodiversity data. They are designed to run at any point in the data lifecycle, from initial collection or observation to data transcription, database loading, and preparation for or during data aggregation. [However, the framing of the InformationElements as Darwin Core terms with the CORE Use Case focused on the research needs of downstream users means that competing requirements have led to some different decisions than would have been made if the aim was to solely evaluate data in a database of records and preparing it for aggregation.]   

### 1.3 Types of tests (non-normative)

[!---check out the wording Paul put in the BDQ_Core_Users_Guide.md - that is nice and simple wording---AC]

The concept of 'tests' in the context of this standard include four distinct types: VALIDATION; ISSUE; AMENDMENT and MEASURE.


#### 1.3.1 Validation 

alidation Tests evaluates values in one or more Darwin Core terms (https://dwc.tdwg.org/list/)for fitness for a particular data quality need. In some cases, Validation Tests check for the presence or the lack of a value. Validation Tests are phrased as positive statements consistent with the Fitness For Use Framework (Veiga et al. 2017). For example, VALIDATION_TAXONRANK_NOTEMPTY will return a Response.status="RUN_HAS_RESULT" and Response.result="COMPLIANT" if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a potential problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result="COMPLIANT". The formal response of Validation Tests take one of four forms. 

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service (bdq:sourceAuthority) is unavailable
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the Information Elements are such that the test cannot be meaningfully run
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met
4. When Response.status="RUN_HAS_RESULT", a Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not.

During the development of the tests, there were significant discussions about how tests were to be phrased, for several contributors (and all tests implemented by agencies such as th ALA and GBIF), the most natural form seemed to be to describe assertions in the negative sense, identifying problems. The bdqffdq Framework, however, focused entirely on positive statements, identifying data that have quality and are fit for purpose.  Over the evolution of the description of the tests we conformed the language to the positive sense of the Framework in almost all cases.  Validations are thus phrased in the Framework sense of being COMPLIANT if the data have quality with respect to the test evaluation criteria.  There were, however, a set of cases that didn't fit well into this positive sense, in particular, those where the conclusion of the test was that the data might or might not be fit for purpose and a human would have to evaluate more closely.  In order to accomodate this "there might be a problem" case, we expanded the framework to include the concept of bdqffdq:Issue, where Issues are the converse of Validations and are phrased in a negative sense, identifying problems, see below. 

#### 1.3.2 Issue

Issue Tests are a form of warning flag where the test is drawing attention to potential problem with the value of a Darwin Core term (https://dwc.tdwg.org/list/) for at least one use case. As discussed above, Validations are phrased in the Framework sense of being COMPLIANT if the data have quality with respect to the test evaluation criteria.  There were however, a set of cases that didn't fit well into this positive sense, in particular, those where the conclusion of the test was that the data might or might not be fit for purpose and a human would have to evaluate the results.  In order to accomodate this "there might be a problem" case, we expanded the Framework to include the concept of bdqffdq:Issue, where Issues are the converse of Validations and are phrased in a negative sense of identifying potential problems. 

Issues can result in a Response.status="RUN_HAS_RESULT" accompanied by a Response.result="POTENTIAL_ISSUE" or a Response.result="NOT_ISSUE".  

An ISSUE is the equivalent to a Response.status="NOT_COMPLIANT" from a Validation Test. A Response.result="NOT_ISSUE" is similar to a Response.result="COMPLIANT" from a Validation Test, but with slightly different semantics, "COMPLIANT" means that the data is fit for some use. A Response.result="NOT_ISSUE" means that there was no reason for the data not to be fit for use.  A Response.result="POTENTIAL_ISSUE" is the reason we incorporated Issue type Tests into BDQ Core.  "POTENTIAL_ISSUE" means that the Issue found a concern in the data that might make it unfit for some use, but that human evaluation of the details of the data and the use are needed. Data flagged with potential issues require a human review.  For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result="POTENTIAL_ISSUE" if dwc:dataGeneralizations contains a value. Any value in dwc:dataGeneralizations asserts changes have been made to generalize other Darwin Core terms and requires a human review to determine whether the data are fit for purpose.

#### 1.3.3 Amendment

Amendment Tests may propose a change to one or more Darwin Core term (https://dwc.tdwg.org/list/) values or fill in missing values. Amendments are intended to improve one or more components of the quality of the record.  The Response.result from an Amendment is a proposal for a change, not to be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses may choose to (blindly - not recommended, or after analysis) accept all proposed amendments as part of a pipeline in preparing data for an analysis. We urge that Amendments do not overwrite existing information within a database; that existing information is preserved, as well as potential changes.

The Framework also supports Amendments where the Response.result is a proposal to changes in procedures, such as suggesting that a constraint should be placed on a database field to restrict allowed values, or that a mapping of a data set onto Darwin Core terms has transposed a set of fields.  We have not framed any such tests of this form in BDQ Core, nor have we considered how such assertions should be represented in a Response.result.

When carrying out Amendments where numeric vales are concerned (e.g. feet to meters, etc.), the principle of reversability is paramount, and thus rounding up or down or using approximations should be avoided and only exact values used. In BDQ Core, we have taken an expedient approach in relation to making Amendments: We have used code in our tests to try and parse out likely unambiguous matches. This is far from an ideal solution, but it does provide the potential of Amendments to 'value add' to Darwin Core data records.

#### 1.3.4 Measure 

Most SingleRecord Measure Tests defined in BDQ Core count the number of Validation or Amendment Tests with a specified Response.Result in a bdqffdq:SingleRecord. Measure Tests return a Response.result as either a numeric value or "COMPLETE" or "NOT_COMPLETE".  Measure Tests can also be accumulated across multiple records (bdqffdq:MultiRecord).

Data are found to be fit for some use if all Validation Tests comprising that Use Case have a Response.result="COMPLIANT", and all non-numeric Measure Tests comprising that Use Case have a Response.result="COMPLETE". The majority of BDQ Core Tests are Validations phrased in the positive sense to identify biodiversity data that are fit for the Use Case, as identified in the user scenario analyses performed by BDQ Task Group 3 (https://github.com/tdwg/bdq/tree/master/tg3).   

bdqffdq:SingleRecord MEASUREs within BDQ Core are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS. Of these, MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate and is the only numeric response Test. This Test is intended to provide an estimator for the duration of an event date that can be used as a criterion for Quality Assurance for some use cases. For example, a phenology use may need temporal resolution of records to within about a day, while a use involving long term patterns of spatial change may be satisfied by temporal resolution of a year or better.  Rather than providing specific measures for each possible duration, we chose to provide just this one generic measure that could be used as a filter criterion for any Use Case.  

For each bdqffdq:SingleRecord Validation Test, there is a bdqffdq:MultiRecord Measure Test that returns a Response.result="COMPLETE" when all records in the bdqffdq:MultiRecord have a Response.result="COMPLIANT", and a Response.result="NOT_COMPLETE" when they are not. Under Quality Assurance, these Measure Tests are the key criterion for identifying data which have quality for a Use Case. Under Quality Assurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measure Tests for completeness, such that a filtered bdqffdq:MultiRecord has Response.result="COMPLETE" for all bdqffdq:MultiRecord Measure Tests.

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

### 1.4 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


### 1.5 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4 the values of the rdfs:Label, skos:prefLabel, Versioned IRI, Resource Type, Specification, Information Elements ActedUpon, Information Elements Consulted, and Parameters are normative.  The values of Description, Examples, Use Cases, and Notes are non-normative. 

In Section 4, the values of the `Term IRI` and `Definition` are normative. The values of `Term Name` `skos:pref:Label` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Examples` and `Notes`) are non-normative.

### 1.6 Namespace abbreviations

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

### 1.7 Example RDF (non-normative) 

A more complete description of the tests can be found in the RDF representation of this vocabulary.  Following the bdqffdq: Framework, a test is composed of an instance of a subclass of a bdqffdq:DataQualityNeed (e.g. bdqffdq:Validation), an instance of a bdqffdq:ActedUpon information element, optionally an instance of a bdqffdq:Consulted information element, an instance of a subclass of bdqffdq:Method (e.g. bdqffdq:ValidationMethod), and an instance of a bdqffdq:Specification.  Most of the information associated with a bdqffdq:term is expressed in other vocabularies, in particular bdqffdq:.   This structure and dependence on other vocabularies can be seen in the example below of https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

**TODO: Check kurator-ffdq appears to have label and skos:prefLabel switched**

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

    <rdf:Description rdf:about="https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Validation"/>
    	<skos:prefLabel rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</skos:prefLabel>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord</rdfs:label>
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

## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of classes and object properties in the `bdqffdq:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqdim/terms), resources MUST be used as values of the `bdqdim:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqenh/terms), resources MUST be used as values of the `bdqenh:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdqcrit/terms), resources MUST be used as values of the `bdqcrit:` namespace.

Due to the requirements of [bdq](https://rs.tdwg.org/bdq/terms), resources MUST be used as values of the `bdq:` namespace.

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of the `bdqcore:` namespace.

### 2.1 Structure of Response (normative)

Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags,  The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary (consisting of exactly COMPLIANT or NOT_COMPLIANT) for validations or Issues (NOT_ISSUE, POTENTIAL_ISSUE, ISSUE), either a numeric value or a controlled vocabulary (consisting of exactly COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments. 
2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 
3. Remark supplies human-readable text describing reasons for the test result output.

### 2.2 Resource Types (normative)

Each test (each instance of a bdqffdq:DataQualityNeed) MUST have exactly one bdqffdq:hasResourceType object property that relates the test to a ResouceType of bdqffdq:SingleRecord or bdqffdq:MultiRecord.  

Tests operate on data, the data may be understood as representing a single record or multiple records.  In the bdqcore: tests the single record (bdqffdq:SingleRecord) tests MAY be applied to a single of Flat Darwin Core Record, or to a single instance of a Darwin Core Observation, Taxon, Event, or other class, and MAY extend across one to many relations from that class instance to instances of classes of other types in a structured representation of Darwin Core data (Wieczorek et al 2012).  For example,    A bdqcore: SingleRecord test SHOULD NOT take multiple rows of Flat Darwin core as input.  A bdqcore: SingleRecord test SHOULD NOT 

The bdqcore test ISSUE_ANNOTATION_NOTEMPTY similarly operates on a single Flat Darwin Core record, or a single core Darwin Core class instance, and asks whether annotations exist related to that class, here this standard encourages the implementation of a standard for annotating occurrence records beyond the Darwin Core terms.

Multi record (bdqffdq:MultiRecord) tests operate on a dataset as a whole, the MultiRecord tests in bdqcore: sum up results across all records for each single record test.

### 2.3 Parameterising the tests (normative)

Where a test is parameterized, a parameter (e.g. bdq:sourceAuthority) is specified in the text of the hasExpectedResponse data type property of the instance of the bdqffdq:Specification for the test.  Such a bdqffdq:Specification MUST also have a bdqffdq:hasArgument object property linking it to an instance of a bdqffdq:Argument, which MUST have a bdqffdq:hasArgumentValue data type property carrying the default value for the parameter, and this bdqffdq:Argument MUST have a bdqffdq:hasParameter object property linking it to a bdqffdq:Parameter.  The bdqffdq:Parameter SHOULD be a class instance in the bdq: namespace (e.g. bdq:sourceAuthority).  The instance of the bdqffdq:Specification SHOULD have a bdqffdq:hasAuthoritiesDefaults data type property containing

These elements MUST be understood in concert.

Values of bdqffdq:hasAuthoritiesDefaults SHOULD be a text string listing parameters in the form of a semicolon delimited list of one or more of the following: 
     
- parameter default = "default value" 
- parameter default = "default value" {[resource]}
- parameter default = "default value" {[resource]} {API endpoint [resource]}

Examples:

     bdq:earliestValidDate default ="1582-11-15"

     bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&amp;name=]}

##### Most of this text goes elsewhere 

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. This allows us to define general tests that provide support for non functional requirements that vary within the community. 

For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite. Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 


## 3 Term indices
