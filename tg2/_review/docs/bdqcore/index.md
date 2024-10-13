<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
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
- [1.1 Documents about the bdqcore: test descriptions.](#11-documents-about-the-bdqcore-test-descriptions)
- [1.1.1 Term List Distributions for bdqcore:](#111-term-list-distributions-for-bdqcore)
- [1.2 Characteristics of the tests (non-normative)](#12-characteristics-of-the-tests-(non-normative))
- [1.3 Types of tests (non-normative)](#13-types-of-tests-(non-normative))
- [1.3.1 Validation](#131-validation-)
- [1.3.2 Issue](#132-issue)
- [1.3.3 Amendment](#133-amendment)
- [1.3.4 Measure](#134-measure-)
- [1.4 RFC 2119 key words (normative)](#14-rfc-2119-key-words-(normative))
- [1.5 Status of the content of this document](#15-status-of-the-content-of-this-document)
- [1.6 Namespace abbreviations](#16-namespace-abbreviations)
- [1.7 Example RDF (non-normative)](#17-example-rdf-(non-normative)-)
- [2 Use of Terms (normative)](#2-use-of-terms-(normative))
- [2.1 Structure of Response (normative)](#21-structure-of-response-(normative))
- [2.2 Resource Types (normative)](#22-resource-types-(normative))
- [2.3 Parameterising the tests (normative)](#23-parameterising-the-tests-(normative))
- [3 Term indices](#3-term-indices)



## 1 Introduction

This document provides introductory explanatory information and normative guidance for the BDQ Core tests. The document includes terms in several namespaces that contain the recommended terms: `bdq:`, `bdqffdq:`, `bdqdim:`, bdqenh:, and bdqcrit as well as the focus of this document the `bdqcore` terms. For details and rationale, see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889.

### 1.1 Documents about the bdqcore: test descriptions.

The bdqcore: vocabulary includes: 

- A [Quick Reference Guide](../terms/bdqcore/index.md) to the tests.
- A [term list](../list/bdqffdq/index.md) for the vocabulary, containing the vocabulary terms and their metadata.
- Normative guidance on the use of the bdqcore vocabulary is provided in this landing page document.
- The bdqcore tests have several distribution files:
  - A csv file listing the tests  [CSV list of tests](../vocabulary/bdqcore_terms.csv) 
  - An rdf representation of the tests in a [Turtle Serialization of bdqcore](../dist/bdqcore.ttl) 
  - An rdf representation of the tests in an [RDF/XML Serialization of bdqcore](../dist/bdqcore.xml) 

An users guide to the use of the bdqcore tests is provided in the [Users Guide](../guide/users/index.md) 

An guide to implemetation of the bdqcore tests is provided in the [Implementers Guide](../guide/implementers/index.md) 

### 1.1.1 Term List Distributions for bdqcore:

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

Each bdqcore:Validation evaluates the values in one or more Darwin Core terms for fitness for some particular narrow data quality need within CORE. Validations evaluate values or in some cases, presence or lack of a value. Validation tests are phrased as positive statements, consistent with the "Fitness for Use Framework".  A Validation tests to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY, is phrased as "Not Empty", and will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem. The formal response of VALIDATIONs can take one of four forms:

1. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable, and running the same test on the same data at a different time may result in a different result.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation.
4. A Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 

#### 1.3.2 Issue

ISSUE is a form of warning flag where the test is drawing attention to a non-empty value of a Darwin Core term. We have used these for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of this case would take human review. For example, ISSUE_ANNOTATION_NOTEMPTY is informing the tester than there is at least one annotation associated with record and this should be evaluated before using the record. Similarly for the other two ISSUE-type tests: ISSUE_DATAGENERALIZATIONS_NOTEMPTY where some form of transformation has occurred, and ISSUE_ESTABLISHMENTMEANS_NOTEMPTY where the value needs to be assessed for utility. ISSUEs are currently outside the Data Quality Fitness for Use Framework. ISSUEs result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "IS_ISSUE", "POTENTIAL_ISSUE" or "NOT_ISSUE". ISSUE is symmetrical to NOT_COMPLIANT, NOT_ISSUE is approximately symmetrical to COMPLIANT, and POTENTIAL_ISSUE does not have an equivalent Validation Response.result. 

#### 1.3.3 Amendment

An AMENDMENT may propose a change or addition to at least one Darwin Core term that is intended to improve one or more components of the quality of the record.  The Response.result from an AMENDMENT MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for QualityControl of an existing database or record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  Amendments, under the framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in these tests.  

#### 1.3.4 Measure 

A MEASURE may return either a Response.result that is a numeric value, or the values COMPLETE or NOT_COMPLETE, or NOT_REPORTED (when the Response.status="INTERNAL_PREREQUISITES_NOTMET").  The principle Measure defined in the core tests is MEASURE_EVENTDATE_DURATIONINSECONDS, it returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the VALIDATIONs and AMENDMENTs and in one case provides an indication of the length of the period of the value of dwc:eventDate.

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

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

### 3.1 Index By Test Label


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
## 4 Vocabulary Summary
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

### 3.1 Index By Test Label


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
## 4 Vocabulary Summary
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


