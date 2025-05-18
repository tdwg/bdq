<!--- Template for header, values provided from yaml configuration --->
# {document_title}

**Title**<br>
{document_title}

**Date version issued**<br>
{ratification_date}

**Date created**<br>
{created_date}

**Part of TDWG Standard**<br>
<{standard_iri}>

<!--
**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}
-->

**This version**<br>
<{current_iri}{ratification_date}>

**Latest version**<br>
<{current_iri}>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
{abstract}

**Authors**<br>
{authors}

**Creator**<br>
{creator}

**Bibliographic citation**<br>
{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

**Status**<br>
{comment}

{toc}

## 1 Introduction

### 1.1 Purpose

The purpose of this document is to define and explain the BDQ Tests — the primary mechanism for evaluating the quality of biodiversity data in the BDQ standard. It describes the structure, types, and formal characteristics of the Tests, providing a clear and consistent specification that can be used by implementers, analysts, and quality assessors.

This document is both normative and explanatory: it defines how each Test is modeled using standard vocabulary terms and how it should behave under various conditions. It also distinguishes among types of Tests (`Validation`, `Issue`, `Measure`, and `Amendment`), outlines the semantics of single- versus multi-record evaluation, and explains how `Parameters` influence Test behavior. The content here provides the foundation for interpreting and using the Tests in software and quality assessment workflows.

### 1.2 Audience

This document is intended for audiences who need a detailed understanding of the BDQ Tests, including:

- Data quality specialists configuring or analyzing BDQ Test outputs
- Software developers and data platform architects implementing BDQ Tests
- Researchers and data managers evaluating dataset readiness for specific uses
- Standards developers integrating BDQ Test logic into broader biodiversity data infrastructures.

While some familiarity with controlled vocabularies and RDF modeling may be useful, the document is designed to be accessible to both technical and semi-technical users who want to apply, understand, or extend BDQ Tests.

### 1.3 Associated Documents

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../index.md).

The set of information most relevant to the Biodiversity Data Quality (BDQ) Tests can be found in the following subset of resources:

- **BDQ Tests and Assertions** Defines how each Test is modeled using standard vocabulary terms and how it should behave under various conditions. This document.
- [**BDQ Tests Quick Reference Guide**](../terms/bdqtest/index.md) Provides a concise, easy-to-read reference about the BDQ Tests.
  - [BDQ Test Index by Use Case](../terms/bdqtest/qrg_index_by_usecase.md)
  - [BDQ Test Index by Information Element Acted Upon](../terms/bdqtest/qrg_index_by_ie_actedupon.md)
  - [BDQ Test Index by Information Element Class](../terms/bdqtest/qrg_index_by_ie_class.md)
  - [BDQ Test Index by Data Quality Dimension](../terms/bdqtest/qrg_index_by_dimension.md)
  - [BDQ Multi Record Measure Test Index](../terms/bdqtest/qrg_multirecord_index.md)
- [**BDQ Tests and Assertions List of Terms**](../list/bdqtest/index.md) Provides the complete normative definitions of the BDQ Tests.
- [**BDQ User's Guide**](../guide/users/index.md) For anyone interested in how to use the BDQ Tests in practice.
- [**BDQ Implementer's Guide**](../guide/implementers/index.md) For anyone interested in the technical implementation of the BDQ Tests.

#### 1.3.1 Term List Distributions for the BDQ Standard

<!--- This same table appears in bdqtest_termlist_header. Edit here, edit there. --->
| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | TBD | [BDQ Tests and Assertions List of Terms](../list/bdqtest/index.md) | Complete term list for the bdqtest: vocabulary as a web page. | 
| RDF/XML file | TBD | [Tests in RDF/XML](../../dist/bdqtest.xml) | An RDF representation of the Tests in an RDF/XML serialization. | 
| Turtle file | TBD | [Tests in Turtle](../../dist/bdqtest.ttl) | An RDF representation of the Tests in a Turtle serialization. | 
| JSON-LD file | TBD | [Tests in JSON/LD](../../dist/bdqtest.json) | An RDF representation of the Tests in a JSON-LD serialization. | 
| CSV file | TBD | [Tests in CSV](../../vocabulary/bdqtest_term_versions.csv) | CSV file listing all of the Tests. | 
| Single Record Test CSV file | TBD | [Single Record Tests in CSV](../../dist/bdqtest_singlerecord_tests_current.csv) | CSV file listing just the Single Record Tests. |
| Multi Record Test CSV file | TBD | [Multi Record Tests in CSV](../../dist/bdqtest_multirecord_tests_current.csv) | CSV file listing just the Multi Record Tests. |

### 1.4 Status of the Content of this Document

Section 1 is non-normative.

Parts of section 2 are normative.

Section 3 is normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

Section 4 is non-normative.

Section 5 is non-normative.

### 1.5 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace Abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms            |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

### 1.7 Referring to Terms (normative)
In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., 'https://rs.tdwg.org/bdqffdq/terms' for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (skos:prefLabel, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. You will find all of these methods of referring to BDQ-related terms throughout the BDQ documentation.

## 2 A Brief Context for the BDQ Tests

The Authors acknowledge the fundamental importane of the work of:

- The TDWG Data Quality Interest Group - Task Group 1 [BDQFramework](https://tdwg.github.io/bdq/tg1/site/), which provided the Framework for the BDQ Tests.
- The TDWG Data Quality Interest Group - Task Group 3 [Data Quality Use Cases](https://www.tdwg.org/community/bdq/tg-3/) for providing recommendations on Use Cases.
- The TDWG [Annotations Interest Group](https://www.tdwg.org/community/annotations/) as to how the Test results may be reported against records.

The terminology of BDQ is based primarily on the Fitness for use Framework (Veiga 2016, Veiga et al. 2017, Biodiversity Information standards (TDWG) Task Group 1) expressed as an ontology, but additional vocabularies are required for a complete description of the Tests and how to use them. See [2.4 Vocabularies](index.md#24-vocabularies) in [The Biodiversity Data Quality (BDQ) Standard](../../index.md).

BDQ Tests focus on values of a subset of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) composed as `bdqffdq:InformationElements` as inputs to the Tests. Each Test is independent, to support the mixing and matching of Tests to meet particular `Data Quality Needs` and not impose a particular model of Test execution on implementation frameworks. Tests may execute in parallel, on data records in sequence, as queries on datasets and on unique values. Tests are paired in that all `Amendment` Tests are matched with a corresponding `Validation` Test that assesses some aspect of data quality. An `Amendment` Test may propose improvements to term values, but the BDQ standard recommends that all improvements be evaluated before application.

Some BDQ Tests also require reference to external data such as standard vocabularies of terms or names.

While the most important BDQ Tests apply to a `Single Record` (`bdqffdq:SingleRecord`), Test results may also be accumulated across multiple records (`bdqffdq:MultiRecord`), for example reporting that 75% of the records do not have a valid value for `dwc:basisOfRecord`. Tests that accumulate information about results across multiple records are necessary for formal application of Quality Assurance and Quality Control principles.

### 2.1 What is meant by "Test"? (non-normative)

We use the captialized term "Test" to mean something specific in the BDQ Standard. A "Test" is any instance of a subclass of `bdqffdq:DataQualityNeed` (e.g., `bdqffdq:Validation`) composed with an instance of a subclass of `bdqffdq:Method` (e.g., `bdqffdq:ValidationMethod`) composed with an instance of `bdqffdq:Specification`. When run by an `Implementation`, each BDQ Test can produce a `Data Quality Report` consisting of `bdqffdq:Assertions`. See the diagrams and further information in the [Fitness For Use Framework Ontology Guide](../guide/bdqffdq/index.md).

The scope of each BDQ Test is largely provided by the `bdqffdq:Specification`. The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) used in the `Specification` are included in the `Information Elements` (`bdqffdq:InformationElement`). The `Specification` also includes references to external (to the Darwin Core standard, Wieczorek et al. 2012) authorities that are required to implement the Test, for example, references to an ISO standard. Such authoritative references are listed under `sourceAuthority` (`bdq:sourceAuthority`) with a link to the authority and optionally, a link to a specific online resource required for the `Implementation` of the Test.

Each BDQ Test is defined to operate on a `Single Record` or a `Multi Record`. The Framework allows for `Multi Record` Tests able to identify outliers within a dataset, or other Tests that look across data values in a `Multi Record` to evaluate data quality. No BDQ Tests have been defined to use data in other records within a dataset to evaluate the quality of data in a `Single Record`. The only `Multi Record` Tests included in BDQ accumulate the outputs of other Tests.

### 2.2 Test Types (non-normative)

The concept of 'Tests' in the context of BDQ include four distinct types: `Validation` (`bdqffdq:Validation`); `Issue` (`bdqffdq:Issue`); `Amendment` (`bdqffdq:Amendment`) and `Measure` (`bdqffdq:Measure`).

#### 2.2.1 Validation Tests (normative)

Each `Validation` Test is composed of an instance of `bdqffdq:Validation` (which expresses a data quality need in the abstract) with an instance of `bdqffdq:ValidationMethod` linking it to an instance of a `bdqffdq:Specification` (which gives details of how that data quality need is to be concretely assessed).

`Validation` Tests in BDQ evaluate values in one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) for fitness for a particular `Data Quality Need`. In some cases, `Validation` Tests check for the presence or the lack of a value. `Validation` Tests are phrased as positive statements consistent with the Fitness For Use Framework (Veiga 2016, Veiga et al. 2017). For example, [VALIDATION_TAXONRANK_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_TAXONRANK_NOTEMPTY) will return a `Response.status`="RUN_HAS_RESULT" and `Response.result`="COMPLIANT" if a record being tested contains a value in `dwc:taxonRank`, rather than being phrased in the negative (i.e., VALIDATION_TAXONRANK_EMPTY) and flagging a potential problem. Data are found to be fit for some use if all `Validations` comprising a corresponding `Use Case` have a `Response.result`="COMPLIANT".

The response of a `Validation` Test (i.e., an instance of a `bdqffdq:ValidationAssertion`) MUST take one of three forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., a `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` (`bdqffdq:InformationElement`) are such that the Test cannot be meaningfully run.
3. A `Response.status` of "RUN_HAS_RESULT" when the prerequisites for running the Test have been met, and in this situation:
  - A `Response.result` of either "COMPLIANT" if the values of the `Information Elements` (`bdqffdq:InformationElement`) meet the `Criteria`, or "NOT_COMPLIANT" if they do not.

#### 2.2.2 Issue Tests (normative)

Each Issue Test is composed of an instance of `bdqffdq:Issue` (which expresses a data quality need in the abstract) with an instance of `bdqffdq:IssueMethod`, which links it to an instance of a `bdqffdq:Specification` (which gives details of how that data quality need is to be concretely assessed).

`Issue` Tests are a form of warning flag where the Test is drawing attention to potential problem with the value of an `Information Element` for at least one use of the data.

We have used `Issue` Tests for a small number of cases where we wished to flag a value that might indicate a record is not fit for some purpose, but the evaluation of these cases would take human review. For example, the Test [ISSUE_ANNOTATION_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_ANNOTATION_NOTEMPTY) is informing the tester than there is at least one annotation associated with a record and this should be evaluated before using the record. Similarly for the other two `Issue` Tests: [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY) where some form of transformation has occurred, and the Test [ISSUE_ESTABLISHMENTMEANS_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_ESTABLISHMENTMEANS_NOTEMPTY) where the value needs to be assessed for utility.

The response of an `Issue` Test (an instance of a `bdqffdq:IssueAssertion`) MUST take one of three forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., a `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result. In this case, the `Response.result` MUST be empty.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` are such that the Test cannot be meaningfully run. In this case, the `Response.result` MUST be empty.
3. A `Response.status` of "RUN_HAS_RESULT" when the prerequisites for running the Test have been met, and in this case:
  - A `Response.result`="POTENTIAL_ISSUE", a `Response.result`="NOT_ISSUE", or a `Response.result`="IS_ISSUE".

In each case, a `Response.comment` MUST be present with text explaining to consumers of the `Data Quality Report` why the the Test produced this response in this case.

None of the currently defined BDQ Issue Tests return a `Response.result` of IS_ISSUE.

#### 2.2.3 Measure Tests (normative) 

Each `Measure` Test is composed of an instance of `bdqffdq:Measure` (which expresses how to measure fitness of data for a data quality need in the abstract) with an instance of `bdqffdq:MeasurementMethod`, which links it to an instance of a `bdqffdq:Specification` (which gives details of how that data quality is to be measured).

`Measure` Tests return a `Response.result` of either a numeric value or one of the values "COMPLETE" or "NOT_COMPLETE". `Measure` Tests may directly measure properties of data. Alternatively, `Measure` Tests may measure the outputs of other Tests, for example, a `Measure` may count the number of `Response.results` from all COMPLIANT `Validation` Tests run on a `bdqffdq:SingleRecord`.

The only `Measure` defined in the BDQ standard that directly examines data is the Test [MEASURE_EVENTDATE_DURATIONINSECONDS](../terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS). This Test returns a `Response.result` measuring the amount of time represented by the value in `dwc:eventDate`, and can be used in Quality Assurance under specific research `Data Quality Needs` to identify `dwc:Occurrences` where the date observed or collected is known well enough for particular analytical needs (e.g., to at least one day for phenology studies, to at least one year for other purposes). The Test basically interprets the results of running the `Validation` and `Amendment` Tests and provides an indication of the length of the period of the value of `dwc:eventDate`.

Most `Single Record` `Measure` Tests defined in the BDQ standard count the number of `Validation` or `Amendment` Tests with a specified `Response.result` from a `Single Record` Test.

The response of a `Measure` Test (an instance of a `bdqffdq:MeasureAssertion`) MUST take one of three forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., a `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result. In this case, the `Response.result` MUST be empty.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` are such that the Test cannot be meaningfully run. In this case, the `Response.result` MUST be empty.
3. A `Response.status` of "RUN_HAS_RESULT" when the prerequisites for running the Test have been met, and in this case either:
  - a `Response.result`="COMPLETE", or a `Response.result`="NOT_COMPLETE".
or
  - a `Response.result` containing a single number.

In each case, a `Response.comment` MUST be present with text explaining to consumers of the `Data Quality Report` why the the Test produced this response in this case.

#### 2.2.4 Amendment Tests (normative) 

Each `Amendment` Test is composed of an instance of `bdqffdq:Amendment` (which expresses how to improve data to fit a data quality need in the abstract) with an instance of `bdqffdq:AmendmentMethod`, which links it to an instance of a `bdqffdq:Specification` (which gives details of how proposals could be made to improve data for that need).

An `Amendment` Test MAY propose a change to one or more Darwin Core term values, or MAY propose to fill in missing values. The `Assertion` produced by an `Amendment` is intended to improve one or more components of the quality of the record. The `Response.result` from an `Amendment` MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a `Data Quality Report` is used for Quality Control of an existing database or record. Consumers of `Data Quality Reports` under Quality Assurance uses MAY choose to accept all proposed `Amendments` as part of a pipeline in preparing data for an analysis. `Amendments`, under the Fitness For Use Framework, may also propose changes to procedures rather than to data values, we have not framed any in this form in the BDQ Tests at the time of first release.

The response of an `Amendment` Test (an instance of a `bdqffdq:AmendmentAssertion`) MUST take one of four forms.

1. A `Response.status` of "EXTERNAL_PREREQUISITES_NOT_MET" when an external resource (e.g., `bdq:sourceAuthority`) is unavailable. Running the same Test on the same data at a different time may result in a different result.
2. A `Response.status` of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the `Information Elements` are such that the Test cannot be meaningfully run.
3. A `Response.status` of "FILLED_IN" when the prerequisites for running the Test have been met and a proposal is made to fill in a value for one or more input terms that were `Empty`, and in this situation:
  - A `Response.result` containing a list of key-value pairs of the terms for which values are to be filled in, and the proposed new values for those terms.
3. A `Response.status` of "AMENDED" when the prerequisites for running the Test have been met and a proposal is made to change a value for one or more input terms that were Empty, and in this situation:
  - A `Response.result` containing a list of key-value pairs of the terms for which new values are proposed, and the proposed new values for those terms.

In each case, a `Response.comment` MUST be present with text explaining to consumers of the `Data Quality Report` why the the Test produced this response in this case.

### 2.3 Single Record and Multi Record Tests (non-normative) 

Tests may operate on a `Single Record` (e.g., one row of [Simple Darwin Core](https://dwc.tdwg.org/simple/)) or on a `Multi Record` (a dataset).

The BDQ [Fitness for Use Framework](../bdqffdq/index.md) allows for Tests of all types to operate on either (`bdqffdq:hasResourceType`) `Single Record` or `Multi Record`. In the BDQ standard, the only `Multi Record` Tests that have been defined are `Measures`. We refer to these as `Multi Record` `Measures` (instances of `bdqffdq:Measure` that are the subject of a `bdqffdq:hasResourceType` property whose object is `bdqffdq:MultiRecord`).

The focus of the BDQ Tests are the `Single Record` Tests. To allow for standard means for summarizing the results of these Tests, and for filtering data under Quality Assurance, we have also defined two sets of `Multi Record` `Measures`.

In the BDQ standard, for each `Single Record` `Validation` Test, we have defined a `Multi Record` `Measure` Test that returns a `Response.result`="COMPLETE" when all records in the `Multi Record` have a `Response.result`="COMPLIANT", and a `Response.result`="NOT_COMPLETE" when they are not. Under Quality Assurance, these `Measure` Tests are the key criterion for identifying data that have quality for a `Use Case`. Under Quality Assurance, a `Multi Record` is filtered to remove records that do not fit the `Multi Record` `Measure` Tests for completeness, such that a filtered `Multi Record` has `Response.result`="COMPLETE" for all `Multi Record` `Measure` Tests.

In the BDQ standard, for each `Single Record` `Validation` Test, we have also defined a `Multi Record` `Measure` Test that returns a `Response.result` counting the number of `Response.results` from that `Validation` Test that are COMPLIANT (or in a few cases, COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET). Under Quality Control, these `Multi Record` `Measures` allow calculation of how much the quality of a dataset would be improved by accepting changes proposed by `Amendments`, and allow identification of areas in the data where quality improvement is most needed to fit the needs of some `Use Case`.

See the [Fitness For Use Framework Summary of Mathematical Formalization (normative)](../bdqffdq/index.md#3-fitness-for-use-framework-summary-of-mathematical-formalization-normative) for the formal expression of how `Measures` are intended to be used in Quality Control and Quality Assurance.

### 2.4 Example RDF (non-normative) 

A more complete description of BDQ Tests can be found in the RDF representation of this vocabulary. Following the Fitness for Use Framework Ontology (`bdqffdq:`), a Test is composed of an instance of a subclass of a `bdqffdq:DataQualityNeed` (e.g., `bdqffdq:Validation`), an instance of a `bdqffdq:ActedUpon` `Information Element`, optionally an instance of a `bdqffdq:Consulted` `Information Element`, an instance of a subclass of `bdqffdq:Method` (e.g., `bdqffdq:ValidationMethod`), and an instance of a `bdqffdq:Specification`. Most of the information associated with a `bdqtest:` term is expressed in other vocabularies, in particular `bdqffdq:`. This structure and dependence on other vocabularies can be seen in the formal example description of [VALIDATION_COUNTRYCODE_STANDARD](../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD), below.

    <rdf:Description rdf:about="https://rs.tdwg.org/bdqtest/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Validation"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<skos:prefLabel rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Validation dwc:countryCode Standard for SingleRecord</skos:prefLabel
    	<hasActedUponInformationElement xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="urn:uuid:c3620a97-65d6-4f9c-8a03-32e0d240a423"/>
    	<hasCriterion xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqcrit:Standard"/>
    	<hasDataQualityDimension xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqdim:Conformance"/>
    	<hasResourceType xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqffdq:SingleRecord"/>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</rdfs:comment>
    	<skos:historyNote rdf:datatype="http://www.w3.org/2001/XMLSchema#string">https://github.com/tdwg/bdq/issues/20</skos:historyNote>
    	<skos:note rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and suitable for a marker for the high seas. Also available in the ISO user defined codes is ZZ, used by GBIF to mark unknown countries. This Test should accept both XZ and ZZ as COMPLIANT country codes. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</skos:note>
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
    	<forValidation xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="https://rs.tdwg.org/bdqtest/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
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

The technical (normative) details of the BDQ Test terms (those in the `bdqtest:` namespace) are found in the [BDQ Tests and Assertions List of Terms](../list/bdqtest/index.md).

The technical definitions of the `bdqtest:` terms are supported by terms in several additional namespaces in the BDQ standard, namely `bdq:`, `bdqffdq:`, `bdqdim:`, `bdqenh:`, and `bdqcrit:`. For the details and rationale, see Chapman et al. (2017).

| **Abbreviation**  | **Technical List of Terms** |
| -------- | ----------------------- |
| bdq:     | [BDQ Controlled Vocabulary List of Terms](../list/bdq/index.md) |
| bdqtest: | [BDQ Tests and Assertions List of Terms](../list/bdqtest/index.md) |
| bdqcrit: | [Data Quality Criterion Controlled Vocabulary List of Terms](../list/bdqcrit/index.md) |
| bdqdim:  | [Data Quality Dimension Controlled Vocabulary List of Terms](../list/bdqdim/index.md) |
| bdqenh:  | [Data Quality Enhancement Controlled Vocabulary List of Terms](../list/bdqenh/index.md) |
| bdqffdq: | [Fitness For Use Framework Ontology List of Terms](../list/bdqffdq/index.md) |

### 3.1 Structure of Response (normative)

Responses from each of the Tests MUST be structured data, and MUST NOT be simple pass/fail flags. The Response from a Test is an `Assertion`, which can form part of a `Data Quality Report` or be wrapped in an `Annotation`, and MUST include the following three components: 

1. `Response.result` is the returned result for the Test, i.e., a numeric value for `Measure` Tests, a strictly controlled vocabulary value (consisting of "COMPLIANT" or "NOT_COMPLIANT" only) for `Validation` Tests, a strictly controlled vocabulary value ("NOT_ISSUE" or "POTENTIAL_ISSUE" only) for `Issue` Tests, a numeric value or a strictly controlled vocabulary value (consisting of exactly "COMPLETE" or "NOT_COMPLETE" for `Measure` Tests, and a data structure (e.g., a list of key value pairs) for proposed changes for `Amendment` Tests.
2. `Response.status` provides a controlled vocabulary, metadata concerning the success, failure, or problems with the Test. The Status also serves as a link to information about warning type values and where, with future development, probabilistic `Assertions` about the likeliness of the value could be made.
3. `Response.comment` supplies human-readable text describing reasons for the Test result output.

A Response MUST be represented as either RDF or as a data structure.

When responses are in the form of RDF, the RDF MUST meet the following conditions: 

1. The Response MUST be an instance of `bdqffdq:Assertion` or one of its subclasses (`bdqffdq:ValidationAssertion`, `bdqffdq:IssueAssertion`, `bdqffdq:MeasurementAssertion`, `bdqffdq:AmendmentAssertion`). An instance of a subclass of `bdqffdq:Assertion` SHOULD be used.
2. The `Assertion` MUST have exactly one `bdqffdq:hasResponseStatus` object property linking it to one of the named individuals that has type `bdqffdq:ResponseStatus` (`bdqffdq:INTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:NOT_AMENDED`, `bdqffdq:AMENDED`, `bdqffdq:FILLED_IN`, or `bdqffdq:RUN_HAS_RESULT`).
3. The `Assertion` MUST have a `bdqffdq:hasResponseResult` object property or `bdqffdq:hasResponseResultValue` data property, unless the object of the `bdqffdq:hasResponseStatus` indicates that none should be present.
  - If the object of the `bdqffdq:hasResponseStatus` is `bdqffdq:RUN_HAS_RESULT`, then the instance of the `Assertion` MUST have one and only one `bdqffdq:hasResponseResult` object property linking it to one of the named individuals that has type `bdqffdq:ResponseResult` (`bdqffdq:COMPLETE`, `bdqffdq:COMPLIANT`, `bdqffdq:IS_ISSUE`, `bdqffdq:NOT_COMPLETE`, `bdqffdq:NOT_COMPLIANT`, `bdqffdq:NOT_ISSUE`, or `bdqffdq:POTENTIAL_ISSUE`).
  - If the object of the `bdqffdq:hasResponseStatus` is one of `bdqffdq:AMENDED` or `bdqffdq:FILLED_IN`, then the instance of the `Assertion` MUST have one and only one `bdqffdq:hasResponseResultValue` data property linking it to structured data presenting the result of the `Amendment`. The string in the `bdqffdq:hasResponseResultValue` SHOULD be a JSON list of key:value pairs, where the keys are specific `Information Elements` (e.g., `dwc:eventDate`), and the values are the new values proposed by the `Amendment`.
  - If the object of the `bdqffdq:hasResponseStatus` is one of `bdqffdq:INTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:EXTERNAL_PREREQUISITES_NOT_MET`, `bdqffdq:NOT_AMENDED`, then no `bdqffdq:hasResponseResult` SHOULD be present.
4. The `Assertion` MUST have at least one `bdqffdq:hasResponseComment` data property. This `bdqffdq:hasResponseComment` must provide a human readable text explanation of why the conclusion expressed in the `Assertion` was reached. The `bdqffdq:hasResponseComment` MAY be repeated to provide the comment in different languages. Each `bdqffdq:hasResponseComment` SHOULD be a independent and complete explanation.
5. The `Assertion` MAY have a `bdqffdq:hasResponseQualifier` object property.

When the Response is represented as a data structure in a form other than RDF, the data structure MUST:

1. Have properties corresponding to `Response.status`, `Response.result`, and `Response.comment`. These properties SHOULD have these labels.
2. Have one `Response.status` property, containing a string constant that MUST be one of the local names of one of the named individuals in `bdqffdq:` with a type `bdqffdq:ResponseStatus` ("INTERNAL_PREREQUISITES_NOT_MET", "EXTERNAL_PREREQUISITES_NOT_MET", "NOT_AMENDED", "AMENDED", "FILLED_IN", or "RUN_HAS_RESULT"").
3. Have one `Response.result` property.
  - If the `Response.status` is "RUN_HAS_RESULT" then the value of the `Response.result` property MUST be a string constant that is one of the local names of one of the named individuals of type `bdqffdq:ResponseResult` ("COMPLETE", "COMPLIANT", "IS_ISSUE", "NOT_COMPLETE", "NOT_COMPLIANT", "NOT_ISSUE", or "POTENTIAL_ISSUE").
  -  If the `Response.status` is one of  "AMENDED" or "FILLED_IN" then the value of the `Response.result` property MUST be structured data presenting the result of the `Amendment`. The string in the `Response.result` SHOULD be a JSON list of key:value pairs, where the keys are specific `Information Elements` (e.g., `dwc:eventDate`), and the values are the new values proposed by the `Amendment`.
  - If the `Response.status` is one of "INTERNAL_PREREQUISITES_NOT_MET", "EXTERNAL_PREREQUISITES_NOT_MET", or "NOT_AMENDED", then the `Response.result` MUST be empty or null.
4. Have one `Response.comment` property. This `Response.comment` must provide a human readable text explanation of why the conclusion expressed in the `Assertion` was reached. Internationalization of content of the `Response.comment` MAY be provided, nothing in this section should be taken as a constraint on how that may be accomplished.
5. A `Response.qualifier` property may be included to provide additional information.

Nothing in this section should be taken as constraining how `Data Quality Reports` are presented to consumers of those reports, so long as all three elements of `Response.result`, `Response.status`, and `Response.comment` can be accessed.

Nothing in this section should be taken as constraining internationalization and languages of labels applied to human readable presentations of Responses from Tests.

Nothing in this section should be taken as a requirement for a particular format or serialization of `bdqffdq:Assertions` or Responses. `Implementations` MAY serialize `Assertions` in any appropriate form for the context. When `Assertions` are wrapped in `oa:Annotations` or presented as linked open data, an RDF representation SHOULD be used.

Nothing in this section should be taken as a requirement to how `bdqffdq:Assertions` or Responses are to be presented to consumers of `Data Quality Reports`. `Implementations` MAY present the results of Tests in any form appropriate for their consumers, so long as none of the required information is suppressed.

### 3.2 Resource Types (normative)

Each BDQ Test (each instance of a `bdqffdq:DataQualityNeed`) MUST have exactly one `bdqffdq:hasResourceType` object property that relates the Test to a `Resource Type` of `bdqffdq:SingleRecord` or `bdqffdq:MultiRecord`.

Tests operate on data. Data may be understood as representing a single record or multiple records. The `Single Record` (`bdqffdq:SingleRecord`) BDQ Tests MAY be applied to a single [Simple Darwin Core](https://dwc.tdwg.org/simple/)) record, or to a single instance of a Darwin Core `dwc:Occurrence`, `dwc:Taxon`, `dwc:Event`, or other class, and MAY extend across one to many relations from that class instance to instances of classes of other types in a structured representation of Darwin Core data (Wieczorek et al. 2012). For example, a BDQ `Single Record` Test SHOULD NOT take multiple rows of Simple Darwin Core as input. A BDQ `Single Record` Test SHOULD NOT take multiple objects of the same core type in structured Darwin Core as input (for example, input Darwin Core data in RDF should be presented to a BDQ `Single Record` Test one `dwc:Occurrence` at a time, although the `dwc:Occurrence` could be linked to multiple other instances of other classes such as `dwc:Identifications`).

The BDQ Test [ISSUE_ANNOTATION_NOTEMPTY](../terms/bdqtest/index.md#ISSUE_ANNOTATION_NOTEMPTY) similarly operates on a single Simple Darwin Core record, or a single core Darwin Core class instance, and asks whether `Annotations` exist related to that class, here this standard encourages the implementation of a standard for annotating `dwc:Occurrence` records beyond the [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021).

BDQ `Multi Record` (`bdqffdq:MultiRecord`) Tests operate on a dataset as a whole. BDQ `Multi Record` Tests in `bdqtest:` sum up results across all records for each `bdqffdq:SingleRecord` Test.

### 3.3 Parameterizing the Tests (normative)

Where a Test is parameterized, a `Parameter` (e.g., `bdq:sourceAuthority`) is specified in the text of the `bdqffdq:hasExpectedResponse` data type property of the instance of the `bdqffdq:Specification` for the Test. Such a `bdqffdq:Specification` MUST also have a `bdqffdq:hasArgument` object property linking it to an instance of a `bdqffdq:Argument`, which MUST have a `bdqffdq:hasArgumentValue` data type property carrying the default value for the `Parameter`, and this `bdqffdq:Argument` MUST have a `bdqffdq:hasParameter` object property linking it to a `bdqffdq:Parameter`. The `bdqffdq:Parameter` SHOULD be a class instance in the `bdq:` namespace (e.g., `bdq:sourceAuthority`).

An instance of the `bdqffdq:Specification` SHOULD have a `bdqffdq:hasAuthoritiesDefaults` data type property containing the parameters, default values, and references to resources, including API endpoints that would provide access to values in the authority.

These elements MUST be understood in concert.

Values of `bdqffdq:hasAuthoritiesDefaults` SHOULD be a text string listing `Parameters` in the form of a semicolon-delimited list of one or more of the following: 
 
- parameter default = "default value" 
- parameter default = "default value" {[resource]}
- parameter default = "default value" {[resource]} {API endpoint [resource]}

The `bdqffdq:hasAuthoritiesDefaults` data property MAY be used without corresponding `bdqffdq:Arguments` and `bdqffdq:Parameters` when a Test is not parameterized, but a `bdq:sourceAuthority` is mentioned within a `bdqffdq:hasExpectedResponse` for the `bdqffdq:Specification` and the `bdqffdq:hasAuthoritiesDefaults` provides details on this `sourceAuthority`. This usage allows for simpler and easier-to-read expected responses.

Section [2.3.2 Reading a Specification](../guide/implementers/index.md#232-reading-a-specification) of the [BDQ Implementer's Guide](../guide/implementers/index.md) contains additional guidance for handling parameters in BDQ Test `Implementations`.

#### 3.3.1 Parameter Examples (non-normative)

Example values for `bdqffdq:hasAuthoritiesDefaults`: 

     bdq:earliestValidDate default ="1582-11-15"

     bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&amp;name=]}

Example RDF fragment showing use of `Arguments` and `bdqffdq:hasAuthoritiesDefaults`: 

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

Example RDF Fragment from the `Specification` for [VALIDATION_COUNTRYCODE_STANDARD](../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD), where `bdqffdq:hasAuthoritiesDefaults` is present to provide a `bdq:sourceAuthority` for the `Specification`, but the Test is not parameterized, so no `bdqffdq:hasArgument` properties are present: 

    <hasAuthoritiesDefaults xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</hasAuthoritiesDefaults>
    <hasExpectedResponse xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</hasExpectedResponse

<!--
## 4 Term indices
-->