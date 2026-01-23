<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Tests and Assertions List of Terms

**Title**<br>
BDQ Tests and Assertions List of Terms

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqtest

**This version**<br>
<http://rs.tdwg.org/bdqtest/terms/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdqtest/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ standard, documenting the tests in the bdqtest: vocabulary, using terms from the Fitness For Use Framework ontology.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Tests and Assertions List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqtest/terms/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
  - [1.4 Term List Distributions (non-normative)](#14-term-list-distributions-non-normative)
  - [1.5 Status of the Content of this Document (normative)](#15-status-of-the-content-of-this-document-normative)
  - [1.6 RFC 2119 key words (normative)](#16-rfc-2119-key-words-normative)
  - [1.7 Namespace abbreviations (non-normative)](#17-namespace-abbreviations-non-normative)
  - [1.8 Referring to Terms (normative)](#18-referring-to-terms-normative)
  - [1.9 Test Types (non-normative)](#19-test-types-non-normative)
  - [1.10 Key to Vocabulary Terms (normative)](#110-key-to-vocabulary-terms-normative)

[2 Use of Terms (normative)](#2-use-of-terms-normative)

[3 Term Indices (non-normative)](#3-term-indices-non-normative)
  - [3.1 Index to Validation Tests (non-normative)](#31-index-to-validation-tests-non-normative)
  - [3.2 Index to Issue Tests (non-normative)](#32-index-to-issue-tests-non-normative)
  - [3.3 Index to Measure Tests (non-normative)](#33-index-to-measure-tests-non-normative)
  - [3.4 Index to Amendment Tests (non-normative)](#34-index-to-amendment-tests-non-normative)

[4 Vocabulary (normative)](#4-vocabulary-normative)

[Acronyms (non-normative)](#acronyms-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to list and describe the terms that define the BDQ Tests, each represented as a term in the `bdqtest:` namespace. This document provides normative values and explanations for the properties used to describe each Test, including its label, expected input, outputs, parameters, and relationships to `Use Cases` and quality `Dimensions`.

The Tests defined here are intended to be modular and interoperable. They can be combined into `Profiles` tailored to particular `Data Quality Needs` or assessment goals. Each Test is specified independently to support implementation flexibility, but all Tests are grounded in the principles of fitness for use as described in the Fitness for Use Framework.

### 1.2 Audience (non-normative)

This document is intended for users who need to understand the detailed structure and semantics of the BDQ Tests. It is particularly useful for:

- Software developers implementing or integrating BDQ Test logic into applications
- Data managers and curators reviewing or selecting appropriate Tests for assessing data quality
- Standards developers and information architects building upon the Fitness for Use Framework
- Anyone requiring detailed, machine-readable specifications of the Tests used in the BDQ standard.

Familiarity with RDF vocabularies, Darwin Core, and fitness for use principles will help readers make full use of this document, though the structure and examples are designed to support a broad technical audience.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

The set of information most relevant to the BDQ Tests can be found in the following subset of resources:

- **BDQ Tests and Assertions** - Defines how each Test is modeled using standard vocabulary terms and how it should behave under various conditions. This document.
- [**BDQ Tests Quick Reference Guide**](../../terms/bdqtest/index.md) - Provides a concise, easy-to-read reference about the BDQ Tests.
- **BDQ Tests and Assertions List of Terms** - Provides the complete normative definitions of the BDQ Tests. This document.
  - [**CSV list of BDQ Tests**](../../../dist/bdqtest_singlerecord_tests_current.csv) - A convenience CSV file listing single record Tests.
  - [**CSV term-version file of BDQ Tests**](../../../vocabulary/bdqtest_term_versions.csv) 
  - [**RDF/Turtle Serialization of BDQ Tests**](../../../dist/bdqtest.ttl) 
  - [**RDF/XML Serialization of BDQ Tests**](../../../dist/bdqtest.xml) 
- [**BDQ User's Guide**](../../guide/users/index.md) - For anyone interested in how to use the BDQ Tests in practice.
- [**BDQ Implementer's Guide**](../../guide/implementers/index.md) - For anyone interested in the technical implementation of the BDQ Tests.

### 1.4 Term List Distributions (non-normative)

<!--- This same table appears in bdqtest_landing_header. Edit here, edit there. --->
| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | TBD | [BDQ Tests and Assertions List of Terms](../../list/bdqtest/index.md) | Complete term list for the `bdqtest:` vocabulary as a web page. | 
| RDF/XML file | TBD | [Tests in RDF/XML](../../../dist/bdqtest.xml) | An RDF representation of the Tests in an RDF/XML serialization. | 
| Turtle file | TBD | [Tests in Turtle](../../../dist/bdqtest.ttl) | An RDF representation of the Tests in a Turtle serialization. | 
| JSON-LD file | TBD | [Tests in JSON/LD](../../../dist/bdqtest.json) | An RDF representation of the Tests in a JSON-LD serialization. | 
| CSV file | TBD | [Tests in CSV](../../../vocabulary/bdqtest_term_versions.csv) | CSV file listing all of the Tests. | 
| Single Record Test CSV file | TBD | [Single Record Tests in CSV](../../../dist/bdqtest_singlerecord_tests_current.csv) | CSV file listing just the `Single Record` Tests. |
| Multi Record Test CSV file | TBD | [Multi Record Tests in CSV](../../../dist/bdqtest_multirecord_tests_current.csv) | CSV file listing just the 		`Multi Record` Tests. |

### 1.5 Status of the Content of this Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Section [1.10 Key to Vocabulary Terms (normative)](#110-key-to-vocabulary-terms-normative) identifies which values in Section 4 are normative and which are non-normative.

### 1.6 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| dwciri:      | http://rs.tdwg.org/dwc/iri/                 |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.8 Referring to Terms (normative)
In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., 'https://rs.tdwg.org/bdqffdq/terms/' for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (skos:prefLabel, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. You will find all of these methods of referring to BDQ-related terms throughout the BDQ documentation.

### 1.9 Test Types (non-normative)

There are four types of BDQ Tests: `Validations`, `Issues`, `Measures` and `Amendments`. Each Test is intended to examine just one specific aspect of data quality. Tests are assembled into Test suites (`bdqffdq:Policies`) that assess the fitness for use of data for a specific use (`bdqffdq:UseCase`).

**Validation Tests** can be thought of as fact-checking. They compare the data against known standards or rules. `Validation` Tests examine the values of one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) against a `Criterion` for quality. An example is [VALIDATION_COUNTRYCODE_STANDARD](../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD) where `dwc:countryCode` is checked against a `sourceAuthority` for validity.

**Issue Tests** can be thought of as warning flags. They don't necessarily mean the data are wrong, but they highlight something that might be a problem for some users. For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](../../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY) alerts users to a `NotEmpty` value that should be examined against their `Data Quality Needs`. 

**Measure Tests** can be thought of as metrics. `Measure` Tests either count things, or assert that data evaluate as fit for some use (COMPLETE), or not fit for some use (NOT_COMPLETE). An example is [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT), which returns the number of Tests of Type `Validation` that had a response of "NOT_COMPLIANT" on a record.

**Amendment Tests** can be thought of as suggestions for improvement. `Amendment` Tests examine the values of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and may propose changes or additions to improve the quality. An example is [AMENDMENT_COUNTRYCODE_STANDARDIZED](../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_STANDARDIZED), where a valid ISO country code could be inferred.

### 1.10 Key to Vocabulary Terms (normative)

These "Test Descriptors" are terms that are necessary to comprehensively describe each Test. Some terms, such as those labeled `Term Version IRI` (`rdf:about`), `Term IRI` (`dcterms:isVersionOf`) and `Term Name` (`rdf:value`) are intended for machine consumption. Some terms such as the `Description` (`rdfs:comment`) are designed to be human-readable and to be understood by consumers of biodiversity `Data Quality Reports`. Terms such as the `Specification` (`bdqffdq:Specification`) ensure that implementers have no ambiguity about how the Test should be coded.

The terminology used to describe the terms in this vocabulary follows the TDWG [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/) (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.
See section [2.4.1 Listing Identifiers for Tests (non-normative)](../../supplement/index.md#241-listing-identifiers-for-tests-non-normative) in [BDQ Supplemental Information](../../supplement/index.md) for a competency question clarifying the relationships among `Term Version IRI`, `Term IRI`, `Term Name`, and `Label`.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | 07c28ace-561a-476e-a9b9-3d5ad6e35933 |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. In present context: A descriptive label for humans to use to identify the Test. | AMENDMENT_BASISOFRECORD_STANDARDIZED |
| Preferred Label (skos:prefLabel) | normative | The preferred lexical label for a resource, in a given language. In present context: An easy to read label for the Test, similar to the Label, but in words. | Amendment dwc:basisOfRecord Standardized |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqtest/terms/ 07c28ace-561a-476e-a9b9-3d5ad6e35933](https://rs.tdwg.org/bdqtest/terms/07c28ace-561a-476e-a9b9-3d5ad6e35933) |
| Modified (dcterms:issued) |  | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. In present context: The most recent date for any change to any element of the Test. | 2025-03-07 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqtest/terms/version/ 07c28ace-561a-476e-a9b9-3d5ad6e35933-2024-07-24](https://rs.tdwg.org/bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933-2024-07-24) |
| Description (rdfs:comment) | non-normative | A description of the subject resource. In present context: A brief description of what the Test does. | Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority. |
| Expected Response (bdqffdq:hasExpectedResponse) | normative | Text describing the logic to be followed by a bdqffdq:Implementation of a bdqffdq:Specification specifying the values of bdqffdq:ResponseStatus and bdqffdq:ResponseResults that should be produced from the evaluation of input bdqffdq:InformationElements. In present context: The formal definition of how the Test must be implemented. | EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; AMENDED the value of dwc:basisOfRecord if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED |
| Specification GUID (bdqffdq:Specification) | normative | A specific statement about how to evaluate a bdqffdq:DataQualityNeed. | urn:uuid:76ee10e7-7be9-432b-ad9c-655b127bff27 |
| InformationElements ActedUpon (bdqffdq:composedOf) | normative | Specific vocabulary term that comprises a bdqffdq:InformationElement that is not a bdqffdq:AbstractInformationElement. | dwc:basisOfRecord |
| InformationElements Consulted (bdqffdq:composedOf) | normative | Specific vocabulary term that comprises a bdqffdq:InformationElement that is not a bdqffdq:AbstractInformationElement. | dwc:verbatimCoordinates, dwc:verbatimLatitude, dwc:verbatimLongitude, dwc:verbatimCoordinateSystem, dwc:verbatimSRS |
| Parameters (bdqffdq:Parameter) | normative | A placeholder for a value that, when provided to a Test bdqffdq:Specification changes the behavior of the Test in a defined manner. | bdq:sourceAuthority |
| SourceAuthorities/Defaults (bdqffdq:hasAuthoritiesDefaults) | normative | Text describing bdq:sourceAuthorities and bdqffdq:Parameters with their default values to attach to a bdqffdq:Specification to further specify the behavior described in the bdqffdq:hasExpectedResponse. | bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]} {dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]} |
| Notes (skos:note) | non-normative | A general note, for any purpose. In present context: Additional information to supplement the Specification. | The term dwc:basisOfRecord has the comment "Recommended best practice is to use a controlled vocabulary such as the set of local names of the identifiers for classes in Darwin Core." The list of these values can be determined by searching https://github.com/tdwg/dwc/blob/master/vocabulary/term_versions.csv for rows with status="recommended" and rdf_type="http://www.w3.org/2000/01/rdf-schema#Class". For example, the term http://rs.tdwg.org/dwc/terms/PreservedSpecimen has a local name PreservedSpecimen. For Tests against a dwc:Occurrence record, the set of valid terms is more limited and embodied in the resource found at https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml, which contains the local name for the identifier, as well as preferred and alternate labels from which to standardize values. |
| Examples (skos:example) | non-normative | An example of the use of a concept. In present context: Examples of input and output data and Test responses for a pass case and a fail case. | [dwc:basisOfRecord="Human obs": Response.status=AMENDED, Response.result=dwc:basisOfRecord="HumanObservation", Response.comment="dwc:basisOfRecord contains interpretable value"],[dwc:basisOfRecord="FossilSpecimen": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:basisOfRecord contains match in the bdq:sourceAuthority so NOT_AMENDED"] |
| Type (rdf:type) | normative | The subject is an instance of a class. In present context: The type of the Test, one of the subtypes of DataQualityNeed. | Amendment |
| Resource Type (bdqffdq:ResourceType) | normative | Category of things that are data objects about which data quality bdqffdq:Assertions may be made. | SingleRecord |
| Data Quality Dimension (bdqffdq:DataQualityDimension) | normative | An aspect of data quality. | Conformance |
| Criterion (bdqffdq:Criterion) | normative | Rule against which data are evaluated for conformance to quality bdqffdq:Criteria. | NotEmpty |
| Enhancement (bdqffdq:Enhancement) | normative | Description of a means by which data could be improved. | Standardized |
| Example Implementations (skos:note) | non-normative | A general note, for any purpose. In present context: Name or links to one or more entities that have an implementation of the Test. | Kurator/FilteredPush rec_occur_qc Library (Morris 2025) |
| Example Implementation Source Code (skos:note) | non-normative | A general note, for any purpose. In present context: A link to code that implements the Test. | [https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/ DwCMetadataDQ.java#L834](https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L834) |
| Source (skos:historyNote) | non-normative | A note about the past state/use/meaning of a concept. In present context: The origin of the concept of the Test. | VertNet |
| Developed As GitHub Issue (skos:historyNote) | non-normative | A note about the past state/use/meaning of a concept. In present context: A link to the GitHub issue that provided rationale management, recording a history (changes and comments) of the development of the Test. | [https://github.com/tdwg/bdq/issues/ 63](https://github.com/tdwg/bdq/issues/63) |
| GitHub Issue Labels (skos:note) | non-normative | A general note, for any purpose. In present context: Labels applied to GitHub Issue noted in the skos:historyNote. | TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE |
| Argument GUID (bdqffdq:Argument) | normative | A value that, when provided to a Test bdqffdq:Specification to replace a bdqffdq:Parameter changes the behavior of the Test in a defined manner. | 1b66a16a-5e76-4eca-a400-d097ac136ac1 |


## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqffdq:` namespace MUST use the Term IRI (e.g., `http://rs.tdwg.org/bdq/bdqffdq/InformationElement`) or Term Qualified name (e.g., `bdqffdq:InformationElement`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `InformationElement`) MAY be used. In a purely human context a label (e.g., `Information Element`) MAY be used.

## 3 Term Indices (non-normative)



### 3.1 Index to Validation Tests (non-normative)

[VALIDATION_BASISOFRECORD_NOTEMPTY](#bdqtest_ac2b7648-d5f9-48ca-9b07-8ad5879a2536) |
[VALIDATION_BASISOFRECORD_STANDARD](#bdqtest_42408a00-bf71-4892-a399-4325e2bc1fb8) |
[VALIDATION_CLASSIFICATION_CONSISTENT](#bdqtest_2750c040-1d4a-4149-99fe-0512785f2d5f) |
[VALIDATION_CLASS_FOUND](#bdqtest_2cd6884e-3d14-4476-94f7-1191cfff309b) |
[VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqtest_adb27d29-9f0d-4d52-b760-a77ba57a69c9) |
[VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqtest_f18a470b-3fe1-4aae-9c65-a6d3db6b550c) |
[VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqtest_b9c184ce-a859-410c-9d12-71a338200380) |
[VALIDATION_COORDINATES_NOTZERO](#bdqtest_1bf0e210-6792-4128-b8cc-ab6828aa4871) |
[VALIDATION_COORDINATEUNCERTAINTY_INRANGE](#bdqtest_c6adf2ea-3051-4498-97f4-4b2f8a105f57) |
[VALIDATION_COUNTRYCODE_NOTEMPTY](#bdqtest_853b79a2-b314-44a2-ae46-34a1e7ed85e4) |
[VALIDATION_COUNTRYCODE_STANDARD](#bdqtest_0493bcfb-652e-4d17-815b-b0cce0742fbe) |
[VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqtest_b23110e7-1be7-444a-a677-cdee0cf4330c) |
[VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqtest_d257eb98-27cb-48e5-8d3c-ab9fca4edd11) |
[VALIDATION_COUNTRY_FOUND](#bdqtest_69b2efdc-6269-45a4-aecb-4cb99c2ae134) |
[VALIDATION_COUNTRY_NOTEMPTY](#bdqtest_6ce2b2b4-6afe-4d13-82a0-390d31ade01c) |
[VALIDATION_DATEIDENTIFIED_INRANGE](#bdqtest_dc8aae4b-134f-4d75-8a71-c4186239178e) |
[VALIDATION_DATEIDENTIFIED_STANDARD](#bdqtest_66269bdd-9271-4e76-b25c-7ab81eebe1d8) |
[VALIDATION_DAY_INRANGE](#bdqtest_8d787cb5-73e2-4c39-9cd1-67c7361dc02e) |
[VALIDATION_DAY_STANDARD](#bdqtest_47ff73ba-0028-4f79-9ce1-ee7008d66498) |
[VALIDATION_DCTYPE_NOTEMPTY](#bdqtest_374b091a-fc90-4791-91e5-c1557c649169) |
[VALIDATION_DCTYPE_STANDARD](#bdqtest_cdaabb0d-a863-49d0-bc0f-738d771acba5) |
[VALIDATION_DECIMALLATITUDE_INRANGE](#bdqtest_b6ecda2a-ce36-437a-b515-3ae94948fe83) |
[VALIDATION_DECIMALLATITUDE_NOTEMPTY](#bdqtest_7d2485d5-1ba7-4f25-90cb-f4480ff1a275) |
[VALIDATION_DECIMALLONGITUDE_INRANGE](#bdqtest_0949110d-c06b-450e-9649-7c1374d940d1) |
[VALIDATION_DECIMALLONGITUDE_NOTEMPTY](#bdqtest_9beb9442-d942-4f42-8b6a-fcea01ee086a) |
[VALIDATION_DEGREEOFESTABLISHMENT_STANDARD](#bdqtest_060e7734-607d-4737-8b2c-bfa17788bf1a) |
[VALIDATION_ENDDAYOFYEAR_INRANGE](#bdqtest_9a39d88c-7eee-46df-b32a-c109f9f81fb8) |
[VALIDATION_ESTABLISHMENTMEANS_STANDARD](#bdqtest_4eb48fdf-7299-4d63-9d08-246902e2857f) |
[VALIDATION_EVENTDATE_INRANGE](#bdqtest_3cff4dc4-72e9-4abe-9bf3-8a30f1618432) |
[VALIDATION_EVENTDATE_NOTEMPTY](#bdqtest_f51e15a6-a67d-4729-9c28-3766299d2985) |
[VALIDATION_EVENTDATE_STANDARD](#bdqtest_4f2bf8fd-fc5c-493f-a44c-e7b16153c803) |
[VALIDATION_EVENTTEMPORAL_NOTEMPTY](#bdqtest_41267642-60ff-4116-90eb-499fee2cd83f) |
[VALIDATION_EVENT_CONSISTENT](#bdqtest_5618f083-d55a-4ac2-92b5-b9fb227b832f) |
[VALIDATION_FAMILY_FOUND](#bdqtest_3667556d-d8f5-454c-922b-af8af38f613c) |
[VALIDATION_GENUS_FOUND](#bdqtest_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec) |
[VALIDATION_GEODETICDATUM_NOTEMPTY](#bdqtest_239ec40e-a729-4a8e-ba69-e0bf03ac1c44) |
[VALIDATION_GEODETICDATUM_STANDARD](#bdqtest_7e0c0418-fe16-4a39-98bd-80e19d95b9d1) |
[VALIDATION_KINGDOM_FOUND](#bdqtest_125b5493-052d-4a0d-a3e1-ed5bf792689e) |
[VALIDATION_KINGDOM_NOTEMPTY](#bdqtest_36ed36c9-b1a7-40b2-b5e2-0d012e772098) |
[VALIDATION_LICENSE_NOTEMPTY](#bdqtest_15f78619-811a-4c6f-997a-a4c7888ad849) |
[VALIDATION_LICENSE_STANDARD](#bdqtest_3136236e-04b6-49ea-8b34-a65f25e3aba1) |
[VALIDATION_LOCATION_NOTEMPTY](#bdqtest_58486cb6-1114-4a8a-ba1e-bd89cfe887e9) |
[VALIDATION_MAXDEPTH_INRANGE](#bdqtest_3f1db29a-bfa5-40db-9fd1-fde020d81939) |
[VALIDATION_MAXELEVATION_INRANGE](#bdqtest_c971fe3f-84c1-4636-9f44-b1ec31fd63c7) |
[VALIDATION_MINDEPTH_INRANGE](#bdqtest_04b2c8f3-c71b-4e95-8e43-f70374c5fb92) |
[VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqtest_8f1e6e58-544b-4365-a569-fb781341644e) |
[VALIDATION_MINELEVATION_INRANGE](#bdqtest_0bb8297d-8f8a-42d2-80c1-558f29efe798) |
[VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqtest_d708526b-6561-438e-aa1a-82cd80b06396) |
[VALIDATION_MONTH_STANDARD](#bdqtest_01c6dafa-0886-4b7e-9881-2c3018c98bdc) |
[VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqtest_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70) |
[VALIDATION_OCCURRENCEID_NOTEMPTY](#bdqtest_c486546c-e6e5-48a7-b286-eba7f5ca56c4) |
[VALIDATION_OCCURRENCESTATUS_NOTEMPTY](#bdqtest_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf) |
[VALIDATION_OCCURRENCESTATUS_STANDARD](#bdqtest_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47) |
[VALIDATION_ORDER_FOUND](#bdqtest_81cc974d-43cc-4c0f-a5e0-afa23b455aa3) |
[VALIDATION_PATHWAY_STANDARD](#bdqtest_5424e933-bee7-4125-839e-d8743ea69f93) |
[VALIDATION_PHYLUM_FOUND](#bdqtest_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f) |
[VALIDATION_POLYNOMIAL_CONSISTENT](#bdqtest_17f03f1f-f74d-40c0-8071-2927cfc9487b) |
[VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqtest_49f1d386-5bed-43ae-bd43-deabf7df64fc) |
[VALIDATION_SCIENTIFICNAMEID_COMPLETE](#bdqtest_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8) |
[VALIDATION_SCIENTIFICNAMEID_NOTEMPTY](#bdqtest_401bf207-9a55-4dff-88a5-abcd58ad97fa) |
[VALIDATION_SCIENTIFICNAME_FOUND](#bdqtest_3f335517-f442-4b98-b149-1e87ff16de45) |
[VALIDATION_SCIENTIFICNAME_NOTEMPTY](#bdqtest_7c4b9498-a8d9-4ebb-85f1-9f200c788595) |
[VALIDATION_SEX_STANDARD](#bdqtest_88d8598b-3318-483d-9475-a5acf9887404) |
[VALIDATION_STARTDAYOFYEAR_INRANGE](#bdqtest_85803c7e-2a5a-42e1-b8d3-299a44cafc46) |
[VALIDATION_STATEPROVINCE_FOUND](#bdqtest_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a) |
[VALIDATION_TAXONRANK_NOTEMPTY](#bdqtest_14da5b87-8304-4b2b-911d-117e3c29e890) |
[VALIDATION_TAXONRANK_STANDARD](#bdqtest_7bdb13a4-8a51-4ee5-be7f-20693fdb183e) |
[VALIDATION_TAXON_NOTEMPTY](#bdqtest_06851339-843f-4a43-8422-4e61b9a00e75) |
[VALIDATION_TAXON_UNAMBIGUOUS](#bdqtest_4c09f127-737b-4686-82a0-7c8e30841590) |
[VALIDATION_TYPESTATUS_STANDARD](#bdqtest_4833a522-12eb-4fe0-b4cf-7f7a337a6048) |
[VALIDATION_YEAR_INRANGE](#bdqtest_ad0c8855-de69-4843-a80c-a5387d20fbc8) |
[VALIDATION_YEAR_NOTEMPTY](#bdqtest_c09ecbf9-34e3-4f3e-b74a-8796af15e59f) 

### 3.2 Index to Issue Tests (non-normative)

[ISSUE_ANNOTATION_NOTEMPTY](#bdqtest_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1) |
[ISSUE_COORDINATES_CENTEROFCOUNTRY](#bdqtest_256e51b3-1e08-4349-bb7e-5186631c3f8e) |
[ISSUE_DATAGENERALIZATIONS_NOTEMPTY](#bdqtest_13d5a10e-188e-40fd-a22c-dbaa87b91df2) |
[ISSUE_ESTABLISHMENTMEANS_NOTEMPTY](#bdqtest_acc8dff2-d8d1-483a-946d-65a02a452700) 

### 3.3 Index to Measure Tests (non-normative)

[MEASURE_AMENDMENTS_PROPOSED](#bdqtest_03049fe5-a575-404f-b564-ae63f5a1cf8b) |
[MEASURE_EVENTDATE_DURATIONINSECONDS](#bdqtest_56b6c695-adf1-418e-95d2-da04cad7be53) |
[MEASURE_VALIDATIONTESTS_COMPLIANT](#bdqtest_45fb49eb-4a1b-4b49-876f-15d5034dfc73) |
[MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](#bdqtest_453844ae-9df4-439f-8e24-c52498eca84a) |
[MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](#bdqtest_49a94636-a562-4e6b-803c-665c80628a3d) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY](#bdqtest_b60c8c58-0137-4b6a-97e9-57d8ca5cf248) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD](#bdqtest_f5dd74bd-6a22-4792-b675-c7ccf2a2c103) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT](#bdqtest_a56fb342-c8ee-4611-8aab-e6c6357e8875) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND](#bdqtest_7270a362-5f2e-41f0-955a-d7a8eaaf0f17) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqtest_d68dc111-9704-4fc5-a8eb-5fa084809202) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqtest_c6c998af-6145-4361-b1e6-52c5b790340a) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqtest_b67f41f4-198c-41e9-9419-ba3919c1be8b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO](#bdqtest_0e239a55-0f19-4c68-bdbf-20580f27a647) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE](#bdqtest_2d90d94b-d384-4bac-aa68-c6800d765882) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY](#bdqtest_d71be8d4-1a04-4816-90c5-49808c823651) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD](#bdqtest_38966850-3737-4a67-953c-c231469e0489) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqtest_26b46375-df2b-4677-a2e5-f96f86b8e242) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqtest_8b73f37d-89ed-479a-8389-9e71ad2ac84d) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND](#bdqtest_f15c38c3-d96d-4e9c-982d-410fb71cf2bc) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY](#bdqtest_6887c881-dc52-409b-8979-9c2f05e55569) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE](#bdqtest_c72fda2d-16e1-4ded-91a5-a7094339d603) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD](#bdqtest_49b787eb-7dce-4ace-97f5-7cbb47cd8cb9) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE](#bdqtest_780480ff-8c4a-4276-aaca-cbd1248de9fa) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD](#bdqtest_c3e0100f-dfc3-4379-a855-df878eef295e) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY](#bdqtest_f041ab17-d834-4586-aa6b-090de2e571a8) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD](#bdqtest_fbe47441-500f-44c7-a1bd-1e872edc5266) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE](#bdqtest_f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY](#bdqtest_bceae35a-52ab-4968-846f-069ace766513) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE](#bdqtest_c70c4950-2246-4acc-a59d-81eaa47edf2b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY](#bdqtest_f948a30e-8084-48d5-b1ca-d77c476f181f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD](#bdqtest_1b8ae68e-63f1-41c0-9025-fbe64db38d64) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE](#bdqtest_7775309b-5331-4a65-b839-cbe959948d33) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD](#bdqtest_130bb875-6b7c-4965-b864-d53f9d05b2cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE](#bdqtest_c8250600-de61-4047-9d7c-6e06a38c7994) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY](#bdqtest_3f62eaa2-747f-456b-85e6-1a6e74086a18) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD](#bdqtest_bffd7499-aca3-423f-bb43-f7bdc9260f4f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY](#bdqtest_d3e282a1-3ff3-4ed0-bd08-fa23b6b8c161) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT](#bdqtest_1919f212-b7db-4b6e-9697-41a715001bd6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND](#bdqtest_97928242-11a9-4ab0-9dd7-3f0465834824) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND](#bdqtest_977f7e75-a88e-4e29-a7b1-e8cdd35aa107) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY](#bdqtest_63fbaf3c-3d41-4ab6-bfc0-904f1b26835f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD](#bdqtest_8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND](#bdqtest_012eade5-fc64-458a-a13a-a614491bf4e0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY](#bdqtest_342bd81c-e2b7-41d8-b32b-013992d19f99) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY](#bdqtest_47ee20d9-5087-4f76-a494-6fea05e50b8b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD](#bdqtest_9d5be694-f5da-465d-8c7e-27e6dac69f9f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY](#bdqtest_bac852b5-1ba6-427b-aa8e-02018e99279c) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE](#bdqtest_3de8af03-05d4-4fd8-8e6d-ba886dc5446f) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE](#bdqtest_6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE](#bdqtest_9c66c116-6644-45b4-b4c7-db7a4ee7c500) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqtest_b21256c2-4bb7-4deb-852d-a9eaa05345e7) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE](#bdqtest_071267a0-d993-4961-a3f7-d8210810d167) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqtest_be2eb717-b390-47d1-b7ba-965a1101e215) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD](#bdqtest_c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqtest_36ea0a78-a079-4014-aca3-2f2b3b11e822) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY](#bdqtest_0c9a139e-5d23-44de-a495-14ec08c61a1c) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY](#bdqtest_298db0c9-a85a-41ee-b111-d622fd969d71) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD](#bdqtest_faca6558-dbff-4d26-a5cb-e11cdf632fe7) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND](#bdqtest_f4fa449c-4b74-4dcf-b4cf-0b73e1496375) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD](#bdqtest_15e0da1d-1a43-4075-8454-b2e618cdd25b) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND](#bdqtest_65e66ca0-e9d1-4411-ad26-bb9c43f32afc) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT](#bdqtest_7da5428e-87b2-4ec2-be82-05b9398b7577) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqtest_dbf3cece-1d83-426e-a5e0-8158fcf9c0cd) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE](#bdqtest_f174ad13-3c67-49f9-8d8b-aba4e933d6f6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY](#bdqtest_a9962d33-ad08-453a-8938-2972425034c2) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND](#bdqtest_4e70b0e4-3fd2-4899-802c-439671374eeb) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY](#bdqtest_0f8b30e2-59dc-46ba-8b91-62049cd1a4e2) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD](#bdqtest_e4d35063-2366-4dda-8eaa-326340361da3) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE](#bdqtest_76008c6b-c56a-4233-84e3-8584950037ec) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND](#bdqtest_58fdd5c1-6201-49a1-a7cd-f49c210dc0b6) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY](#bdqtest_de661615-b338-4557-af5b-d44a89de40fa) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD](#bdqtest_602bc457-6b1d-4f24-adef-d0d31bcdf2f0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY](#bdqtest_54d290e8-ac48-4f31-8af3-676363573217) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS](#bdqtest_782773c9-7b37-483d-8ce2-c6683ba81882) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD](#bdqtest_b5a14d76-292e-499b-b80f-9546243311a0) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE](#bdqtest_aee65eb8-8d1e-4b8f-bd37-5822e29f5734) |
[MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY](#bdqtest_687d3ad1-93a3-4a1f-b69f-da5a1eb761a5) |
[MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY](#bdqtest_c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8) |
[MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD](#bdqtest_241a279c-76d5-499b-ab49-a47ad7f8df50) |
[MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT](#bdqtest_a2be4734-0a93-46dc-af4a-e2125b47dbd4) |
[MULTIRECORD_MEASURE_QA_CLASS_FOUND](#bdqtest_21541436-641d-45a9-938c-537484d94eb7) |
[MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT](#bdqtest_86c28d5e-f778-4230-88d8-64cc01478601) |
[MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT](#bdqtest_7a8b0af3-fa7d-416a-921a-8992d56f8233) |
[MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT](#bdqtest_478dee00-98d0-4154-b66c-eca64dbbf86d) |
[MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO](#bdqtest_151b2d29-3460-4ba5-a226-86971dc8ad03) |
[MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE](#bdqtest_d94b0130-7a13-4fa8-955c-eff5c47bd9de) |
[MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY](#bdqtest_942f63bd-d19d-4214-bf8e-cec0055b8909) |
[MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD](#bdqtest_fedf27b2-e01d-459f-98fc-7f0f39e3d4be) |
[MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT](#bdqtest_57b40d9a-67d7-4916-9c27-dbb395c6c27e) |
[MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#bdqtest_23aced89-d613-479c-bc4c-837d74b73be0) |
[MULTIRECORD_MEASURE_QA_COUNTRY_FOUND](#bdqtest_388e74b3-2e18-4d78-8112-3142d1177e25) |
[MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY](#bdqtest_9c8df974-8fba-4537-8c67-31466787f732) |
[MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE](#bdqtest_6354376c-0cf2-435b-be40-850769c5a18a) |
[MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD](#bdqtest_563872eb-f544-45a0-8f91-8098d62768d4) |
[MULTIRECORD_MEASURE_QA_DAY_INRANGE](#bdqtest_85dc5d02-9847-420f-a026-6a0e70962d2a) |
[MULTIRECORD_MEASURE_QA_DAY_STANDARD](#bdqtest_371035f6-42b5-494f-86d9-de2f44a6cdc6) |
[MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY](#bdqtest_4d999a65-a431-4a76-b591-e0d86dcf244b) |
[MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD](#bdqtest_d9493fa0-d90e-41db-95f6-d1c1d243540e) |
[MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE](#bdqtest_3c8bc478-f6b2-4533-b7ce-45bae5d186c2) |
[MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY](#bdqtest_a2535b23-4407-40bd-b23b-30c8185d72a2) |
[MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE](#bdqtest_6f7a9b82-7d34-4111-a2a6-9efe5221fa44) |
[MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY](#bdqtest_a94e986e-dbc8-4147-872d-5f2727945654) |
[MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD](#bdqtest_ba953672-6526-4375-97e8-b4e9d1a7d3a0) |
[MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE](#bdqtest_c04d428a-13d0-4766-9df7-4dfb2ef5d5d8) |
[MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD](#bdqtest_8dfed701-01a9-415d-a9f8-539280b75975) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE](#bdqtest_d41a731b-2e2b-4442-9217-4c375ae92926) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY](#bdqtest_c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365) |
[MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD](#bdqtest_14a1d51f-16ed-4148-9dc8-1e90157a9868) |
[MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY](#bdqtest_f22539ef-029b-4edb-ad17-add4363f7395) |
[MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT](#bdqtest_f375a3fd-4cf5-4ef4-955e-d71762ede2d8) |
[MULTIRECORD_MEASURE_QA_FAMILY_FOUND](#bdqtest_a07d7147-2db8-48ce-81b8-e47595ad5f17) |
[MULTIRECORD_MEASURE_QA_GENUS_FOUND](#bdqtest_c5c8db83-3af0-4215-806f-e2f90574b138) |
[MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY](#bdqtest_488c1dff-21ec-4e68-a00a-7355505e180c) |
[MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD](#bdqtest_cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e) |
[MULTIRECORD_MEASURE_QA_KINGDOM_FOUND](#bdqtest_465d7ac1-d193-46c0-a302-56a9ef99215f) |
[MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY](#bdqtest_3bc9df8b-0f57-4157-9374-b56a99090b22) |
[MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY](#bdqtest_4fccf163-9336-4f48-996c-57f5f66e72db) |
[MULTIRECORD_MEASURE_QA_LICENSE_STANDARD](#bdqtest_acd8d43e-7a2a-4372-b887-fb53a9972dc9) |
[MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY](#bdqtest_3b2e4791-1a5a-4087-9e8d-09c67cf8c816) |
[MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE](#bdqtest_c73d49d1-06e4-4272-8249-6a26e7f8abca) |
[MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE](#bdqtest_7c5a6ba0-399d-4570-878a-4a064e2406fe) |
[MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE](#bdqtest_49d756a8-e654-4267-a290-d1def5d2c5f9) |
[MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH](#bdqtest_fcabd2c9-392c-4841-a5d7-e2680c9587ab) |
[MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE](#bdqtest_1ba18c8b-66a6-47d9-a709-404439332dba) |
[MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION](#bdqtest_44f00697-ca66-43cf-8f16-646b40c0f514) |
[MULTIRECORD_MEASURE_QA_MONTH_STANDARD](#bdqtest_b3c2bb86-e239-4532-ae0c-b121ec1ee025) |
[MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY](#bdqtest_16059801-6adb-4e65-82f4-61eaa70d8df0) |
[MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY](#bdqtest_0028ef9a-6553-467b-a344-90327ed2babf) |
[MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY](#bdqtest_d2922585-2070-4851-a033-15e51977f9dc) |
[MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD](#bdqtest_2fea4571-92d0-48a5-a5ba-6caecd647862) |
[MULTIRECORD_MEASURE_QA_ORDER_FOUND](#bdqtest_773bb288-fef3-4968-a65a-a69c74d6ecb5) |
[MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD](#bdqtest_ef31ba02-cea7-4d76-990f-99ebbd201fb4) |
[MULTIRECORD_MEASURE_QA_PHYLUM_FOUND](#bdqtest_17364d16-37b7-4ccb-9614-bfb95ff1bca9) |
[MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT](#bdqtest_ef05b45b-13b8-4877-9e9d-fa44b332d83c) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#bdqtest_6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE](#bdqtest_a9529e71-5470-4cb1-b04d-aa483926f532) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY](#bdqtest_4cf84216-c8a7-4865-a8e1-3ffd829d5a10) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND](#bdqtest_a8aee02c-cf7c-4104-a601-d8afc4f9cbe2) |
[MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY](#bdqtest_b4d6a61c-64ff-4da0-974c-63a73fd20836) |
[MULTIRECORD_MEASURE_QA_SEX_STANDARD](#bdqtest_1b3bbac4-7c00-46d6-8179-1d57c92374ad) |
[MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE](#bdqtest_8c217eee-9cd0-48c3-aea0-90151c6c5bfd) |
[MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND](#bdqtest_9c1cdf6a-0dbf-4828-a2e3-fb368f74d194) |
[MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY](#bdqtest_e0b8cff1-3322-40d2-b8b2-b99fc9ae130a) |
[MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD](#bdqtest_f320ca83-8487-4011-b1ff-f4b1b4dd86ec) |
[MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY](#bdqtest_2a9d4cfd-815a-46e0-bb51-60724582b762) |
[MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS](#bdqtest_0df03601-3768-4805-906a-bbd0a41b0fda) |
[MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD](#bdqtest_1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88) |
[MULTIRECORD_MEASURE_QA_YEAR_INRANGE](#bdqtest_a0502c5f-608b-4e59-99da-d9490bb4d93b) |
[MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY](#bdqtest_a8fef8a8-e7c7-4a2d-adaf-7da99c896c93) 

### 3.4 Index to Amendment Tests (non-normative)

Including MultiRecord Measures

[AMENDMENT_BASISOFRECORD_STANDARDIZED](#bdqtest_07c28ace-561a-476e-a9b9-3d5ad6e35933) |
[AMENDMENT_COORDINATES_FROM_VERBATIM](#bdqtest_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e) |
[AMENDMENT_COORDINATES_TRANSPOSED](#bdqtest_f2b4a50a-6b2f-4930-b9df-da87b6a21082) |
[AMENDMENT_COUNTRYCODE_FROM_COORDINATES](#bdqtest_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae) |
[AMENDMENT_COUNTRYCODE_STANDARDIZED](#bdqtest_fec5ffe6-3958-4312-82d9-ebcca0efb350) |
[AMENDMENT_DATEIDENTIFIED_STANDARDIZED](#bdqtest_39bb2280-1215-447b-9221-fd13bc990641) |
[AMENDMENT_DAY_STANDARDIZED](#bdqtest_b129fa4d-b25b-43f7-9645-5ed4d44b357b) |
[AMENDMENT_DCTYPE_STANDARDIZED](#bdqtest_bd385eeb-44a2-464b-a503-7abe407ef904) |
[AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED](#bdqtest_74ef1034-e289-4596-b5b0-cde73796697d) |
[AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED](#bdqtest_15d15927-7a22-43f8-88d6-298f5eb45c4c) |
[AMENDMENT_EVENTDATE_FROM_VERBATIM](#bdqtest_6d0a0c10-5e4a-4759-b448-88932f399812) |
[AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY](#bdqtest_3892f432-ddd0-4a0a-b713-f2e2ecbd879d) |
[AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR](#bdqtest_eb0a44fa-241c-4d64-98df-ad4aa837307b) |
[AMENDMENT_EVENTDATE_STANDARDIZED](#bdqtest_718dfc3c-cb52-4fca-b8e2-0e722f375da7) |
[AMENDMENT_EVENT_FROM_EVENTDATE](#bdqtest_710fe118-17e1-440f-b428-88ba3f547d6d) |
[AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](#bdqtest_7498ca76-c4d4-42e2-8103-acacccbdffa7) |
[AMENDMENT_GEODETICDATUM_STANDARDIZED](#bdqtest_0345b325-836d-4235-96d0-3b5caf150fc0) |
[AMENDMENT_LICENSE_STANDARDIZED](#bdqtest_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8) |
[AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM](#bdqtest_c5658b83-4471-4f57-9d94-bf7d0a96900c) |
[AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM](#bdqtest_2d638c8b-4c62-44a0-a14d-fa147bf9823d) |
[AMENDMENT_MONTH_STANDARDIZED](#bdqtest_2e371d57-1eb3-4fe3-8a61-dff43ced50cf) |
[AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT](#bdqtest_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5) |
[AMENDMENT_OCCURRENCESTATUS_STANDARDIZED](#bdqtest_f8f3a093-042c-47a3-971a-a482aaaf3b75) |
[AMENDMENT_PATHWAY_STANDARDIZED](#bdqtest_f9205977-f145-44f5-8cb9-e3e2e35ce908) |
[AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON](#bdqtest_431467d6-9b4b-48fa-a197-cd5379f5e889) |
[AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](#bdqtest_f01fb3f9-2f7e-418b-9f51-adf50f202aea) |
[AMENDMENT_SEX_STANDARDIZED](#bdqtest_33c45ae1-e2db-462a-a59e-7169bb01c5d6) |
[AMENDMENT_TAXONRANK_STANDARDIZED](#bdqtest_e39098df-ef46-464c-9aef-bcdeee2a88cb) |
[AMENDMENT_TYPESTATUS_STANDARDIZED](#bdqtest_b3471c65-b53e-453b-8282-abfa27bf1805) 

## 4 Vocabulary (normative)
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_07c28ace-561a-476e-a9b9-3d5ad6e35933"></a>Term Name  bdqtest:07c28ace-561a-476e-a9b9-3d5ad6e35933</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_BASISOFRECORD_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:basisOfRecord Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/07c28ace-561a-476e-a9b9-3d5ad6e35933</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933-2024-07-24</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; AMENDED the value of dwc:basisOfRecord if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:76ee10e7-7be9-432b-ad9c-655b127bff27</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:basisOfRecord</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]} {dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The term dwc:basisOfRecord has the comment "Recommended best practice is to use a controlled vocabulary such as the set of local names of the identifiers for classes in Darwin Core." The list of these values can be determined by searching https://github.com/tdwg/dwc/blob/master/vocabulary/term_versions.csv for rows with status="recommended" and rdf_type="http://www.w3.org/2000/01/rdf-schema#Class". For example, the term http://rs.tdwg.org/dwc/terms/PreservedSpecimen has a local name PreservedSpecimen. For Tests against a dwc:Occurrence record, the set of valid terms is more limited and embodied in the resource found at https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml, which contains the local name for the identifier, as well as preferred and alternate labels from which to standardize values.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:basisOfRecord="Human obs": Response.status=AMENDED, Response.result=dwc:basisOfRecord="HumanObservation", Response.comment="dwc:basisOfRecord contains interpretable value"],[dwc:basisOfRecord="FossilSpecimen": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:basisOfRecord contains match in the bdq:sourceAuthority so NOT_AMENDED"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L834</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/63</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>1b66a16a-5e76-4eca-a400-d097ac136ac1</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_BASISOFRECORD_STANDARDIZED with Specification Specification for: AMENDMENT_BASISOFRECORD_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_BASISOFRECORD_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e"></a>Term Name  bdqtest:3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COORDINATES_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment Coordinates from Verbatim</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e-2024-08-20</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if 1) either dwc:decimalLatitude or dwc:decimalLongitude are bdq:NotEmpty, or 2) dwc:verbatimCoordinates and one of dwc:verbatimLatitude and dwc:verbatimLongitude are bdq:Empty; FILLED_IN the values of dwc:decimalLatitude, dwc:decimalLongitude and dwc:geodeticDatum (provided that the dwc:verbatimCoordinates can be unambiguously interpreted as geographic coordinates) from 1) dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimSRS or 2) dwc:verbatimCoordinates and dwc:verbatimSRS; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1e16fbb3-0c8d-4f23-bf55-68e159ab2b04</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude,dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:verbatimCoordinates,dwc:verbatimLatitude,dwc:verbatimLongitude,dwc:verbatimCoordinateSystem,dwc:verbatimSRS</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Transformations between coordinate reference systems should not be made as a part of this Test. Though coordinate precision of the verbatim coordinates could also be interpreted during the process of amending decimal coordinates from verbatim coordinates, that amendment is recommended to be an independent Test. Note that dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimCoordinates might all be populated, and they may or not be perfectly consistent with each other. An ideal implementation should check for the consistency of these three fields and not amend them if they are inconsistent.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:verbatimLatitude="-23.712", dwc:verbatimLongitude="139.92", dwc:verbatimCoordinates="", dwc:verbatimSRS="EPSG:4326", dwc:verbatimCoordinateSystem="decimal degrees",dwc:decimalLatitude="", dwc:decimalLongitude="": Response.status=FILLED_IN, Response.result=dwc:decimalLatitude="-23.712", dwc:decimalLongitude="139.92", dwc:geodeticDatum="EPSG:4326", Response.comment="Input fields contain interpretable values"],[dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:verbatimCoordinates="54K 0390210 7377243", dwc:verbatimSRS="EPSG:32754", dwc:verbatimCoordinateSystem="decimal degrees", dwc:decimalLatitude="", dwc:decimalLongitude="":: Response.status=NOT_AMENDED, Response.result="", Response.comment="In the wrong coordinate system"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L402</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/32</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_COORDINATES_FROM_VERBATIM with Specification Specification for: AMENDMENT_COORDINATES_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COORDINATES_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f2b4a50a-6b2f-4930-b9df-da87b6a21082"></a>Term Name  bdqtest:f2b4a50a-6b2f-4930-b9df-da87b6a21082</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COORDINATES_TRANSPOSED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment Coordinates Transposed</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f2b4a50a-6b2f-4930-b9df-da87b6a21082</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f2b4a50a-6b2f-4930-b9df-da87b6a21082-2024-11-11</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment transposing or changing the signs of dwc:decimalLatitude and/or dwc:decimalLongitude to align the location with the dwc:countryCode.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if any of dwc:decimalLatitude or dwc:decimalLongitude or dwc:countryCode are bdq:Empty; AMENDED dwc:decimalLatitude and dwc:decimalLongitude if the coordinates were transposed or one or more of the signs of the coordinates were reversed to align the location with dwc:countryCode according to the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:46caea46-0c94-4efb-9e5f-1b170f2ad54e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The dwc:geodeticDatum is not necessary for this Test. The maximum positional shift between any geographic coordinate reference system and WGS84 is less than 6 km, so any hemisphere Test that relies on a country code for consistency would not be affected by the potential shift. The prior VALIDATION for this Test is VALIDATION_COORDINATE_COUNTRYCODE_CONSISTENT (adb27d29-9f0d-4d52-b760-a77ba57a69c9).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="25.46", dwc:decimalLongitude="135.87", dwc:countryCode="AU": Response.status=AMENDED, Response.result=dwc:decimalLatitude="-25.46", dwc:decimalLongitude="135.87", Response.comment="dwc:decimalLatitude sign reversed to fit dwc:countryCode=AU"],[dwc:decimalLatitude="25.46", dwc:decimalLongitude="135.87", dwc:countryCode="AX": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:countryCode is uninterpretable"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Transposed</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L3473</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio, GBIF, BISON, FP, Kurator, ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/54</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test Consistency CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>95e1332e-eeca-4b41-8698-88ffc33cef3f</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_COORDINATES_TRANSPOSED with Specification Specification for: AMENDMENT_COORDINATES_TRANSPOSED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COORDINATES_TRANSPOSED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae"></a>Term Name  bdqtest:8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COUNTRYCODE_FROM_COORDINATES</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:countryCode from Coordinates</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary from the bdq:countryShapes that is attributable to a single valid ISO 3166-1-alpha-2 country code.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either dwc:decimalLatitude or dwc:decimalLongitude is bdq:Empty, or if dwc:countryCode is bdq:NotEmpty; FILLED_IN dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary in the bdq:sourceAuthority that is attributable to a single valid country code; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:95ac057e-a941-416f-b7dc-ad7aca875cff</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This amendment simply fills dwc:countryCode from a lookup of dwc:decimalLatitude and dwc:decimalLongitude.  If the coordinate falls in the high seas outside any national jurisdiction dwc:countryCode="XZ" should be asserted.  Values in dwc:coordinateUncertaintyInMeters and dwc:coordinatePrecision (if present) imply a buffer around the provided coordinates. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is also justified. Taking spatial buffers into account does, however, greatly complicate the logic and the implementation of this and related Tests. In this Test, a detection of multiple country codes by sampling within the buffer, while possible, is not considered.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="-25.23", dwc:decimalLongitude="135.43", dwc:countryCode="": Response.status=FILLED_IN, Response.result=dwc:countryCode="AU", Response.comment="dwc:decimalLatitude and dwc:decimalLongitude contain interpretable values"],[dwc:decimalLatitude="-38.280937", dwc:decimalLongitude="72.047790", dwc:countryCode="": Response.status=FILLED_IN, Response.result=dwc:countryCode="XZ", Response.comment="Coordinates do not fall in the boundary of any national jurisdiction, using XZ for high seas"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.1.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2019</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, iDigBio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/73</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test VOCABULARY Completeness ISO/DCMI STANDARD Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>82350b56-1855-4b5a-8b44-9040efb0bf05</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_COUNTRYCODE_FROM_COORDINATES with Specification Specification for: AMENDMENT_COUNTRYCODE_FROM_COORDINATES</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COUNTRYCODE_FROM_COORDINATES</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_fec5ffe6-3958-4312-82d9-ebcca0efb350"></a>Term Name  bdqtest:fec5ffe6-3958-4312-82d9-ebcca0efb350</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_COUNTRYCODE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/fec5ffe6-3958-4312-82d9-ebcca0efb350-2024-11-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:countryCode if it can be interpreted as an ISO 3166-1-alpha-2 country code.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISTITES_NOT_MET if the value of dwc:countryCode is bdq:Empty; AMENDED the value of dwc:countryCode if it can be unambiguously interpreted to a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3e076cfa-56ff-4b79-9739-736d062eac5a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "ISO 3166-1-alpha-2" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test supports conformance with the recommendation in the comment on dwc:countryCode: "Recommended best practice is to use an ISO 3166-1-alpha-2 country code." Darwin Core also recommends the use of the XZ for high seas and ZZ for unknown. Three letter codes should be amended to the matching two-letter code.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="Australia": Response.status=AMENDED, Response.result=dwc:countryCode="AU", Response.comment="dwc:countryCode contains an interpretable value"],[dwc:countryCode="Aust.": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:countryCode contains an ambiguous value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L931</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/48</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_COUNTRYCODE_STANDARDIZED with Specification Specification for: AMENDMENT_COUNTRYCODE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_COUNTRYCODE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_39bb2280-1215-447b-9221-fd13bc990641"></a>Term Name  bdqtest:39bb2280-1215-447b-9221-fd13bc990641</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DATEIDENTIFIED_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/39bb2280-1215-447b-9221-fd13bc990641</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/39bb2280-1215-447b-9221-fd13bc990641-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:dateIdentified to a valid ISO date.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; AMENDED if the value of dwc:dateIdentified is not a properly formatted ISO 8601 date but is unambiguous and altered to be a valid ISO 8601 date; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:16e40618-e9bd-479a-b1e8-8aee3467109f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:dateIdentified</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We reference Wikipedia for the ISO standard because the standard documents are not free.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dateIdentified="2021-28-10": Response.status=AMENDED, Response.result=dwc:dateIdentified="2021-10-28", Response.comment="dwc:dateIdentified assuming dwc:year, dwc:day and dwc:month"],[dwc:dateIdentified="21-10-28": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:dateIdentified contains ambiguous values. It could be dd-mm-yy or yy-mm-dd"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCOtherDateDQ.java#L300</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Kurator</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/26</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_DATEIDENTIFIED_STANDARDIZED with Specification Specification for: AMENDMENT_DATEIDENTIFIED_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DATEIDENTIFIED_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b129fa4d-b25b-43f7-9645-5ed4d44b357b"></a>Term Name  bdqtest:b129fa4d-b25b-43f7-9645-5ed4d44b357b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:day Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b129fa4d-b25b-43f7-9645-5ed4d44b357b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b129fa4d-b25b-43f7-9645-5ed4d44b357b-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:day as an integer between 1 and 31 inclusive.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; AMENDED the value of dwc:day if the value is unambiguously interpreted as an integer between 1 and 31 inclusive; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3eae7451-19c6-403c-ba36-29f8204d15ff</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:day</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If dwc:day contains text that may be interpreted as Roman numerals, the result will be NOT_AMENDED as this is not standard. Values such as "3rd" or "12th" can be interpreted as the integers "3" and "12". Text such as "5th Friday" is ambiguous.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="23rd": Response.status=AMENDED, Response.result=dwc:day="23", Response.comment="dwc:day is interpretable as "23""],[dwc:day="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:day is ambiguous, either a "X", "No data" or "10""]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1621</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/127</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_DAY_STANDARDIZED with Specification Specification for: AMENDMENT_DAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DAY_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_bd385eeb-44a2-464b-a503-7abe407ef904"></a>Term Name  bdqtest:bd385eeb-44a2-464b-a503-7abe407ef904</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DCTYPE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dc:type Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/bd385eeb-44a2-464b-a503-7abe407ef904</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/bd385eeb-44a2-464b-a503-7abe407ef904-2024-08-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dc:type using the DCMI type vocabulary.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; AMENDED the value of dc:type if it can be unambiguously interpreted as a term name in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:317e79db-680a-4bbe-8a3e-e805c69514b8</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dc:type</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority is "DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>dc:type holds literals (e.g. PhysicalObject), while dcterms:type holds an IRI for the resource (e.g. http://purl.org/dc/dcmitype/PhysicalObject), see the Darwin Core RDF guide https://dwc.tdwg.org/rdf/#32-imported-dublin-core-terms-for-which-only-literal-objects-are-appropriate-normative. Implementations of this Amendment are expected be able to amend IRI values to the literals, as well as removing leading/trailing whitespace and correcting case errors in the literal.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dc:type="evnt": Response.status=AMENDED, Response.result=dc:type="Event", Response.comment="dc:type contains an interpretable value"],[dc:type="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dc:type contains an uninterpretable value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L724</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/41</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_DCTYPE_STANDARDIZED with Specification Specification for: AMENDMENT_DCTYPE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DCTYPE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_74ef1034-e289-4596-b5b0-cde73796697d"></a>Term Name  bdqtest:74ef1034-e289-4596-b5b0-cde73796697d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:degreeOfEstablishment Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/74ef1034-e289-4596-b5b0-cde73796697d</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/74ef1034-e289-4596-b5b0-cde73796697d-2024-04-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:degreeOfEstablishment using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; AMENDED the value of dwc:degreeOfEstablishment if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:ba1fa532-9612-4944-bfd1-8bd39ab47758</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:degreeOfEstablishment</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, synonyms for values of dwc:degreeOfEstablishment can be found at https://registry.gbif.org/vocabulary/DegreeOfEstablishment/concepts.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:degreeOfEstablishment="capt.": Response.status=AMENDED, Response.result=dwc:degreeOfEstablishment="captive", Response.comment="dwc:degreeOfEstablishment contains an interpretable value in the bdq:sourceAuthority"],[dwc:degreeOfEstablishment="tree": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:degreeOfEstablishment does not contain an interpretable value in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1759</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/276</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>ff9e9459-d1a5-43a6-ada9-8be41772b711</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED with Specification Specification for: AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_15d15927-7a22-43f8-88d6-298f5eb45c4c"></a>Term Name  bdqtest:15d15927-7a22-43f8-88d6-298f5eb45c4c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:establishmentMeans Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/15d15927-7a22-43f8-88d6-298f5eb45c4c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/15d15927-7a22-43f8-88d6-298f5eb45c4c-2024-02-08</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:establishmentMeans using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; AMENDED the value of dwc:establishmentMeans if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fa4e531e-f45e-4dea-8c4b-27d364117808</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:establishmentMeans</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:establishmentMeans="vag.": Response.status=AMENDED, Response.result=dwc:establishmentMeans="vagrant", Response.comment="dwc:establishmentMeans contains an interpretable value in the bdq:sourceAuthority"],[dwc:establishmentMeans="cultivated": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:establishmentMeans is not an interpretable value in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1502</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/269</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>17d785ee-6ac9-4ab4-9806-f4a2b0d8bbf1</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED with Specification Specification for: AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6d0a0c10-5e4a-4759-b448-88932f399812"></a>Term Name  bdqtest:6d0a0c10-5e4a-4759-b448-88932f399812</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:eventDate from dwc:verbatimEventDate</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6d0a0c10-5e4a-4759-b448-88932f399812</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6d0a0c10-5e4a-4759-b448-88932f399812-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:eventDate from the content of dwc:verbatimEventDate.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:NotEmpty or the value of dwc:verbatimEventDate is bdq:Empty; FILLED_IN the value of dwc:eventDate if an unambiguous ISO 8601 date is interpreted from dwc:verbatimEventDate; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b417d971-8b0f-49ab-9431-3364ba8694e2</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:verbatimEventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the proposed eventDate is prior to 1918-02-14, the Response.comment will include a note that the "verbatimDate was assumed to be in the Gregorian calendar". When running the Test, the original precision, e.g. year=1980, month=1 should be retained, e.g. dwc:eventDate should become 1980-01, not 1980-01-01/1980-01-31.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="", dwc:verbatimEventDate="Friday 29th Oct. 2021": Response.status=FILLED_IN, Response.result=dwc:eventDate="2021-10-29", Response.comment="dwc:verbatimEventDate contains an interpretable value (assuming some external lookup thesauri)"],[dwc:eventDate="", dwc:verbatimEventDate="03/04/2020": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:verbatimEventDate is ambiguous - could be either 3rd April or 4th March"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L334. For a minimum set of unit tests see: [DwcEventDQTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L605), see also unit tests for underlying implementation in [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L632) and [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L788)</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet, FP, Kurator</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/86</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_EVENTDATE_FROM_VERBATIM with Specification Specification for: AMENDMENT_EVENTDATE_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3892f432-ddd0-4a0a-b713-f2e2ecbd879d"></a>Term Name  bdqtest:3892f432-ddd0-4a0a-b713-f2e2ecbd879d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:eventDate from dwc:year dwc:month dwc:day</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3892f432-ddd0-4a0a-b713-f2e2ecbd879d</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3892f432-ddd0-4a0a-b713-f2e2ecbd879d-2024-09-15</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:month and dwc:day.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL _PREREQUISITES_NOT_MET if dwc:eventDate is not EMPTY or dwc:year is EMPTY or is not interpretable as an integer; FILLED_IN the value of dwc:eventDate if an ISO 8601 date was interpreted from the values in dwc:year, dwc:month and dwc:day; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:bda7e8a3-3366-43d5-8a8b-e206101dc90d</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:year,dwc:month,dwc:day</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>An attempt to populate dwc:eventDate from dwc:verbatimEventDate and from dwc:startDayOfYear and dwc:endDayOfYear should be made before this Test is run. If dwc:year and dwc:day are present and interpretable, but dwc:month is not supplied or is not interpretable, then just the year should be given as the proposed amendment. This Test assumes that that dwc:year, dwc:month, dwc:day are in a Gregorian calendar, and that only those three pieces of information are needed to produce a dwc:eventDate (explicitly in ISO 8601-1 format, and thus using the Gregorian calendar). When running the Test, the original precision, e.g. dwc:year=1980, dwc:month=1 should be retained, e.g. dwc:eventDate should become 1980-01, not 1980-01-01/1980-01-31.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="", dwc:year="1420", dwc:month="10", dwc:day="29": Response.status=FILLED_IN, Response.result=dwc:eventDate="1420-10-29", Response.comment="dwc:year, dwc:month and dwc:day are interpretable, even if pre-Linnaeus"],[dwc:eventDate="", dwc:year="2024", dwc:month="2", dwc:day="30": Response.status=NOT_AMENDED, Response.result=, Response.comment="Not a valid date"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1395</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/93</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY with Specification Specification for: AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_eb0a44fa-241c-4d64-98df-ad4aa837307b"></a>Term Name  bdqtest:eb0a44fa-241c-4d64-98df-ad4aa837307b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:eventDate from dwc:year dwc:startDayOfYear dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/eb0a44fa-241c-4d64-98df-ad4aa837307b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/eb0a44fa-241c-4d64-98df-ad4aa837307b-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:NotEmpty or any of dwc:year, dwc:startDayOfYear, or dwc:endDayOfYear are bdq:Empty; FILLED_IN the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear if the values in each are independently interpretable and if the value of dwc:startDayOfYear is less than the value of dwc:endDayOfYear; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:647bf697-e432-4b31-9a69-778396e14a82</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:year,dwc:startDayOfYear,dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>An attempt to populate dwc:eventDate from dwc:verbatimEventDate should be made before this Test is run. While year=1999, startDayOfYear=123 could be validly represented as an ISO date as either 1999-123 or 1999-05-03, the latter of these two forms SHOULD be used, thus, do not simply concatenate dwc:year and dwc:startDayOfYear. This Test is only for cases that fall within the one year (as given in dwc:year) and hence dwc:startDayOfYear will always be less than dwc:endDayOfYear.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:year="1901", dwc:startDayOfYear="15", dwc:endDayOfYear="25", dwc:eventDate="": Response.status=FILLED_IN, Response.result=dwc:eventDate="1901-01-15/1901-01-25", Response.comment="dwc:eventDate was interpreted from dwc:year, dwc:startDayOfYear and dwc:endDayOfYear"],[dwc:year="1901", dwc:startDayOfYear="25", dwc:endDayOfYear="15", dwc:eventDate="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:startDayOfYear > dwc:endDayOfyear"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1296</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/132</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR with Specification Specification for: AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_718dfc3c-cb52-4fca-b8e2-0e722f375da7"></a>Term Name  bdqtest:718dfc3c-cb52-4fca-b8e2-0e722f375da7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENTDATE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:eventDate Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/718dfc3c-cb52-4fca-b8e2-0e722f375da7</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/718dfc3c-cb52-4fca-b8e2-0e722f375da7-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment of the value of dwc:eventDate to a valid ISO date.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; AMENDED if the value of dwc:eventDate is not a properly formatted ISO 8601 date but is unambiguous, and altered to be a valid ISO 8601 date; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:6e0e22a1-c233-4c13-baa7-0ab48a4340e4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The intent of the amended range is to capture the original uncertainty where possible. As in the example, we amend "1999-11" instead of "1999-11-01/1999-11-31". An AMBIGUOUS response is possible.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="2021-28-10": Response.status=AMENDED, Response.result=dwc:eventDate="2021-10-28", Response.comment="dwc:eventDate contains an interpretable value. Assuming year-day-month input format"],[dwc:eventDate="10-28": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:eventDate contains an ambiguous value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L559 A minimal set of unit tests is in [DwCEventDQTestDefinitions](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DwCEventDQTestDefinitions.java#L338) unit tests for the underlying verbatim date extraction code are in [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L632) and [DateUtilsTest](https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DateUtilsTest.java#L788)</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paul Morris, Lee Belbin</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/61</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_EVENTDATE_STANDARDIZED with Specification Specification for: AMENDMENT_EVENTDATE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENTDATE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_710fe118-17e1-440f-b428-88ba3f547d6d"></a>Term Name  bdqtest:710fe118-17e1-440f-b428-88ba3f547d6d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_EVENT_FROM_EVENTDATE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:Event from dwc:eventDate</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/710fe118-17e1-440f-b428-88ba3f547d6d</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/710fe118-17e1-440f-b428-88ba3f547d6d-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to values in any of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear or dwc:endDayOfYear from the content of dwc:eventDate.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or contains an invalid value according to ISO 8601; FILLED_IN if any of (1) dwc:day from dwc:eventDate if dwc:day is bdq:Empty and dwc:eventDate has a precision of a day or finer and is within a single day, (2) dwc:month from dwc:eventDate if dwc:month is bdq:Empty and dwc:eventDate has a precision of a single month or finer and is within a single month, (3) dwc:year from dwc:eventDate if dwc:year is bdq:Empty and dwc:eventDate has a precision of a single year or finer and is within a single year, (4) dwc:startDayOfYear and dwc:endDayOfYear if they are bdq:Empty and dwc:eventDate has a precision of a day or better; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:46992280-0ed6-4c42-9e89-ed388ca1d43b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:year,dwc:month,dwc:day,dwc:startDayOfYear,dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Only fields that are empty will be have changes proposed, and only if dwc:eventDate has a valid ISO 8601-1 date. The dwc:eventDate is the canonical form of the event date (it is the first trusted form). If event date does not contain a range,dwc:startDayOfYear = dwc:endDayOfYear. Time (as compared to date) is not deemed a CORE component. Note, see sequencing Tests section of standards documents, run this amendment after any other amendment that may affect dwc:eventDate</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="2023-01-26", dwc:year="2023", dwc:month="", dwc:day="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=FILLED_IN, Response.result=dwc:month="1", dwc:day="26", dwc:startDayOfYear="26", dwc:endDayOfYear="26", Response.comment="dwc:month, dwc:day, dwc:startDayOfyear and dwc:endDayOfYear filled in from dwc:eventDate"],[dwc:eventDate="2023",dwc:year="2023", dwc:month="", dwc:day="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=NOT_AMENDED, Response.result=, Response.comment="No amendments possible"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L2073</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/52</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Completeness ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_EVENT_FROM_EVENTDATE with Specification Specification for: AMENDMENT_EVENT_FROM_EVENTDATE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_EVENT_FROM_EVENTDATE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7498ca76-c4d4-42e2-8103-acacccbdffa7"></a>Term Name  bdqtest:7498ca76-c4d4-42e2-8103-acacccbdffa7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:geodeticDatum Assumed Default</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7498ca76-c4d4-42e2-8103-acacccbdffa7</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7498ca76-c4d4-42e2-8103-acacccbdffa7-2024-11-12</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to fill in dwc:geodeticDatum using a parameterized value if the dwc:geodeticDatum is empty.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>If dwc:geodeticDatum is bdq:Empty, fill in dwc:geodeticDatum using the value of bdq:defaultGeodeticDatum, report FILLED_IN and, if dwc:coordinateUncertaintyInMeters, dwc:decimalLatitude and dwc:decimalLongitude are bdq:NotEmpty, amend the value of dwc:coordinateUncertaintyInMeters by adding the maximum datum shift between the specified bdq:defaultGeodeticDatum and any other datum at the provided dwc:decimalLatitude and dwc:decimalLongitude and instead report AMENDED; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:da49fa95-ce7b-46cf-825a-91d53f21a997</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:geodeticDatum,dwc:coordinateUncertaintyInMeters</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:defaultGeodeticDatum</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:defaultGeodeticDatum default = "EPSG:4326"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The value of dwc:geodeticDatum applies to dwc:decimalLatitude and dwc:decimalLongitude, thus EPSG:4326 (https://epsg.org/crs_4326/WGS-84.html) is the appropriate EPSG code as it applies to the WGS84 datum used with a geographic coordinate system. If the dwc:coordinateUncertaintyInMeters is bdq:Empty, not interpretable, or not valid, this amendment should not provide a dwc:coordinateUncertaintyInMeters. If the dwc:coordinateUncertaintyInMeters is bdq:NotEmpty and is valid, this amendment should add to the dwc:coordinateUncertaintyInMeters the uncertainty contributed by the maximum datum shift at the given coordinates. Since different systems have differing requirements for what the default datum should be, it is left unspecified, but should match whatever the target datum is in AMENDMENT_COORDINATES_CONVERTED (620749b9-7d9c-4890-97d2-be3d1cde6da8). After the amendment is performed, the dwc:geodeticDatum field should be the assumed default datum as parameterized. An example implementation to determine the uncertainty added by asserting a default datum (datum shift) where a known datum is not declared can be found in [datumshiftproj.py](https://github.com/VertNet/georefcalculator/blob/master/source/python/datumshiftproj.py) in the source code for the [Georeferencing Calculator](http://georeferencing.org/georefcalculator/gc.html) (Wieczorek & Wieczorek 2021). Included in the source code is a [5-degree grid](https://github.com/VertNet/georefcalculator/blob/master/datumerrordata.js) of datum shifts from an unknown datum to WGS84.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="[null]", dwc:decimalLatitude="-30.00", dwc:decimalLongitude="130.00", dwc:coordinateUncertaintyInMeters="50": Response.status=AMENDED, Response.result=dwc:geodeticDatum="EPSG:4326", dwc:coordinateUncertaintyInMeters="2836", Response.comment="dwc:godeticDatum is bdq:Empty so filled in with default and dwc:coordinateUncertaintyInMeters amended to maximum possible value"],[dwc:geodeticDatum="WGS84", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:geodeticDatum contains a value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>AssumedDefault</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2349</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/102</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test Completeness Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>7fd3889a-0d1d-4054-8e68-807cfa5410f2</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT with Specification Specification for: AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0345b325-836d-4235-96d0-3b5caf150fc0"></a>Term Name  bdqtest:0345b325-836d-4235-96d0-3b5caf150fc0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_GEODETICDATUM_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:geodeticDatum Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0345b325-836d-4235-96d0-3b5caf150fc0</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0345b325-836d-4235-96d0-3b5caf150fc0-2025-03-03</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:geodeticDatum using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; AMENDED the value of dwc:geodeticDatum if it could be unambiguously interpreted as a valid code from the bdq:sourceAuthority (in the form Authority:Number) for a Datum, Ellipsoid or a CRS appropriate for a 2D geographic coordinate in degrees, or as the value "not recorded"; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:5daf8c2f-50df-423c-a740-55079b625c10</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index#/Datum]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Chapman and Wieczorek (2020) recommend best practice is to use EPSG codes (https://epsg.io/) as a controlled vocabulary. Ideally, amend to the EPSG code for the geographic coordinate reference system (CRS), if known. Otherwise use the EPSG code for the geodetic datum, if known. Otherwise use the EPSG code of the ellipsoid, if known. If none of these is known, use the explicit value "not recorded". The reference vocabularies of values for geodetic datums and ellipsoids needs to be made available and should map alternative representations of dwc:geodeticDatum strings to EPSG codes, such as "WGS84", "WGS_84", "WGS:84", "WGS 84", all with standard value "EPSG:4326". NB. Do NOT change one datum to any other datum no matter how close they are or may appear to be. The same treatment should be given to all datums, which is to use their transformation algorithms to get the equivalent in EPSG:4326. For reference, a vocabulary of synonyms for EPSG codes for values of dwc:geodeticDatum can be found at https://registry.gbif.org/vocabulary/GeodeticDatum/concepts and and for more information on obtaining the EPSG dataset, see https://docs.geotools.org/latest/userguide/library/referencing/epsg.html. For the purposes of this Test "not recorded" is not a value in the bdq:sourceAuthority and should result in NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="WGS84": Response.status=AMENDED, Response.result=dwc:geodeticDatum="EPSG:4326", Response.comment="dwc:geodeticDatum contains a valid code in the bdq:sourceAuthority"],[dwc:geodeticDatum="WGS8": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:geodeticDatum contains an ambiguous value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1568</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paul Morris</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/60</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test VOCABULARY Conformance CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_GEODETICDATUM_STANDARDIZED with Specification Specification for: AMENDMENT_GEODETICDATUM_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_GEODETICDATUM_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8"></a>Term Name  bdqtest:dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_LICENSE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dcterms:license Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dcterms:license using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; AMENDED value of dcterms:license if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:825f551a-2adf-4509-9f95-5a42601a8e88</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dcterms:license</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Creative Commons" {[https://creativecommons.org/]} {Creative Commons licenses [https://creativecommons.org/about/cclicenses/]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The license at the record level might be derived from the license of the dataset from which the record is retrieved.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dcterms:license="CC0": Response.status=AMENDED, Response.result=dcterms:license="https://creativecommons.org/publicdomain/zero/1.0/legalcode", Response.comment="Input field contains interpretable value"],[dcterms:license="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dcterms:license contains uninterpretable value "X""]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1226</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/133</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>7ecc692d-e65f-4ea5-9d54-04421ec96ab4</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_LICENSE_STANDARDIZED with Specification Specification for: AMENDMENT_LICENSE_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_LICENSE_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c5658b83-4471-4f57-9d94-bf7d0a96900c"></a>Term Name  bdqtest:c5658b83-4471-4f57-9d94-bf7d0a96900c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:minimumDepthInMeters dwc:maximumDepthInMeters from dwc:verbatimDepth</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c5658b83-4471-4f57-9d94-bf7d0a96900c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c5658b83-4471-4f57-9d94-bf7d0a96900c-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes amendments of the values of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be interpreted from dwc:verbatimDepth.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters are bdq:NotEmpty or dwc:verbatimDepth is bdq:Empty; FILLED_IN the value of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be unambiguously interpreted from dwc:verbatimDepth; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4db033ea-b0f7-4d01-a5fc-a0459a73a67d</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:minimumDepthInMeters,dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:verbatimDepth</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If dwc:verbatimDepth has a single value rather than a range, the minimum and maximum values should be amended with the same value. When transforming units, the transformation should be reversible, not adjusting the number of significant digits or adjusting the rounding. For example, transform fathoms to meters by multiplying by 1.8288 and retaining added significant digits (verbatim depth of 10 fathoms to minimum and maximum depths in meters of 18.288). Implementations should be capable of interpreting verbatim data in at least meters, fathoms, and feet, in the form of either a single value or a range. The units must be specified in the verbatim data to be interpretable.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumDepthInMeters="", dwc:maximumDepthInMeters="", dwc:verbatimDepth="10 feet": Response.status=FILLED_IN, Response.result=dwc:minimumDepthInMeters="3.048", dwc:maximumDepthInMeters="3.048", Response.comment="dwc:verbatimDepth contains interpretable values"],[ dwc:minimumDepthInMeters="", dwc:maximumDepthInMeters="", dwc:verbatimDepth="x": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:verbatimDepth does not contain an interpretable value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1121</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/55</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM with Specification Specification for: AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_2d638c8b-4c62-44a0-a14d-fa147bf9823d"></a>Term Name  bdqtest:2d638c8b-4c62-44a0-a14d-fa147bf9823d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:minimumElevationInMeters dwc:maximumElevationInMeters from dwc:verbatimElevation</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/2d638c8b-4c62-44a0-a14d-fa147bf9823d</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/2d638c8b-4c62-44a0-a14d-fa147bf9823d-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment or amendments to the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be interpreted from dwc:verbatimElevation.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters or dwc:maximumElevationInMeters are bdq:NotEmpty or dwc:verbatimElevation is bdq:Empty; FILLED_IN the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be unambiguously interpreted from dwc:verbatimElevation; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:84195393-4797-465f-bfc1-b764df67c5c2</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:minimumElevationInMeters,dwc:maximumElevationInMeters</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:verbatimElevation</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the dwc:verbatimElevation as a single value rather than a range, the minimum and maximum values should be amended with the same value. When transforming units, the transformation should be reversible, not adjusting the number of significant digits or adjusting the rounding. For example, transform yards to meters by multiplying by 0.9144 and retaining added significant digits (verbatim elevation of 10 yards to minimum and maximum depths in meters of 9.144). Implementations should be capable of interpreting verbatim data in at least meters,yards, feet, and kilometers in the form of either a single value or a range. The units must be specified in the verbatim data to be interpretable.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:verbatimElevation="100 feet", dwc:minimumElevationInMeters="", dwc:maximumElevationInMeters="": Response.status=FILLED_IN, Response.result=dwc:minimumElevationInMeters="30.48", dwc:maximumElevationInMeters="30.48", Response.comment="dwc:verbatimElevation contains an interpretable value"],[dwc:verbatimElevation="x", dwc:minimumElevationInMeters="", dwc:maximumElevationInMeters="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:verbatimElevation contains an uninterpretable value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1775</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/68</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM with Specification Specification for: AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_2e371d57-1eb3-4fe3-8a61-dff43ced50cf"></a>Term Name  bdqtest:2e371d57-1eb3-4fe3-8a61-dff43ced50cf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_MONTH_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:month Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/2e371d57-1eb3-4fe3-8a61-dff43ced50cf</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/2e371d57-1eb3-4fe3-8a61-dff43ced50cf-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:month as an integer between 1 and 12 inclusive.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; AMENDED the value of dwc:month if it can be unambiguously interpreted as an integer between 1 and 12 inclusive; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4a514adf-766f-46a4-bf16-6febcb594f38</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:month</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Implementations should translate interpretable Roman numerals in the range I-XII in dwc:month as integer month values 1-12, as some natural science domains use roman numeral months to avoid language and day/month vs month/day order. In these cases, the result will be AMENDED numeric equivalents.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:month="IV": Response.status=AMENDED, Response.result=dwc:month="4", Response.comment="dwc:month interpreted as roman numerals "],[dwc:month="October": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:month contains an uninterpretable value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1535 with unit test at https://github.com/FilteredPush/event_date_qc/blob/f224e5a1e6db81bc6ca725f520dd06a71fcfb54e/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L671 Internals of recognized string values (roman numerals, month names and abbreviations in multiple languages) use a combination of event_date_qc's DateUtils.cleanMonth() (see https://github.com/FilteredPush/event_date_qc/blob/23e4139d7f0ef71736f7fc7e984cfd2d0bfea093/src/main/java/org/filteredpush/qc/date/DateUtils.java#L2111 and Joda time's month recognition)</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/128</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment TIME CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_MONTH_STANDARDIZED with Specification Specification for: AMENDMENT_MONTH_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_MONTH_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5"></a>Term Name  bdqtest:96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:occurrenceStatus Assumed Default</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5-2024-11-13</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment of the value of dwc:occurrenceStatus to the default parameter value if dwc:occurrenceStatus, dwc:individualCount and dwc:organismQuantity are empty.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:NotEmpty; FILLED_IN the value of dwc:occurrenceStatus using the bdq:defaultOccurrenceStatus Parameter value if dwc:occurrenceStatus,dwc:individualCount and dwc:organismQuantity are bdq:Empty; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:9c150f88-1fc4-47b7-b826-f6357c104946</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:individualCount,dwc:organismQuantity</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:defaultOccurrenceStatus</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:defaultOccurrenceStatus default = "present"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>There is currently a capitalization mismatch between https://dwc.tdwg.org/terms/#dwc:occurrenceStatus recommended values and the GBIF vocabulary at (https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="", dwc:individualCount="", dwc:organismQuantity="": Response.status=FILLED_IN, Response.result=dwc:occurrenceStatus="present", Response.comment="dwc:occurrenceStatus is bdq:Empty; assumed "present""],[dwc:occurrenceStatus="X", dwc:individualCount="10", dwc:organismQuantity="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:occurrenceStatus is bdq:NotEmpty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>AssumedDefault</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1021</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/75</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Completeness Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>a558165b-7014-4029-839f-33badcb0842f</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT with Specification Specification for: AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f8f3a093-042c-47a3-971a-a482aaaf3b75"></a>Term Name  bdqtest:f8f3a093-042c-47a3-971a-a482aaaf3b75</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:occurrenceStatus Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f8f3a093-042c-47a3-971a-a482aaaf3b75</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f8f3a093-042c-47a3-971a-a482aaaf3b75-2025-03-03</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:occurrenceStatus using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:ocurrenceStatus is bdq:Empty; AMENDED the value of dwc:occurrenceStatus if it can be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fae50773-a832-4e44-87fe-d66a1332c3e7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Regex present/absent" {["^(present\</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The recommended controlled vocabulary for this term consists of "present" and "absent", which are the only two appropriate terms for a Darwin Core Occurrence. This is reflected in the suggested dwc:occurrenceStatus vocabulary for this Test. Other values for dwc:occurrenceStatus should only arise under circumstances that do not refer to an Occurrence. The GBIF API is listed in the sourceAuthority. However, there is currently a mismatch between the lower case recommended values at https://dwc.tdwg.org/terms/#dwc:occurrenceStatus and the GBIF vocabulary at bdq:sourceAuthority that uses an upper case first letter (https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts), thus implementations using the GBIF API should ensure that matches on alternate terms in that vocabulary are converted to the all lower case values in the present/absent vocabulary recommended in Darwin Core. Implementations should interpret the numeric value 1 as present, and the numeric value 0 as absent.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="1": Response.status=AMENDED, Response.result=dwc:occurrenceStatus="present", Response.comment="Input field contains an interpretable value. "],[dwc:occurrenceStatus="X": Response.status=NOT_AMENDED, Response.result=, Response.comment="Input field contains uninterpretable value "X"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1119</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/115</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>59635d6c-f265-45dd-8814-b80a1dc41540</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_OCCURRENCESTATUS_STANDARDIZED with Specification Specification for: AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f9205977-f145-44f5-8cb9-e3e2e35ce908"></a>Term Name  bdqtest:f9205977-f145-44f5-8cb9-e3e2e35ce908</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_PATHWAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:pathway Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f9205977-f145-44f5-8cb9-e3e2e35ce908</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f9205977-f145-44f5-8cb9-e3e2e35ce908-2024-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:pathway using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; AMENDED the value of dwc:pathway if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fef3a7f9-edd8-41c9-9704-4798814077e3</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:pathway</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, synonyms for values of dwc:pathway can be found at https://registry.gbif.org/vocabulary/Pathway/concepts.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:pathway="transportStowaway": Response.status=AMENDED, Response.result=dwc:pathway="transportStowaway", Response.comment="dwc:pathway found in the bdq:sourceAuthority"],[dwc:pathway="escapeee": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:pathway not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1941</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/278</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>0a7b3629-ecd9-47d2-b672-44ef47e03f7b</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_PATHWAY_STANDARDIZED with Specification Specification for: AMENDMENT_PATHWAY_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_PATHWAY_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_431467d6-9b4b-48fa-a197-cd5379f5e889"></a>Term Name  bdqtest:431467d6-9b4b-48fa-a197-cd5379f5e889</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:scientificNameID from dwc:Taxon</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/431467d6-9b4b-48fa-a197-cd5379f5e889</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/431467d6-9b4b-48fa-a197-cd5379f5e889-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:scientificNameID if it can be unambiguously resolved from bdq:sourceAuthority using the available taxon terms.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:NotEmpty, or if all of dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, and dwc:cultivarEpithet are bdq:Empty, FILLED_IN the value of dwc:scientificNameID for an unambiguously resolved single taxon record in the bdq:sourceAuthority through (1) the value of dwc:scientificName or (2) if dwc:scientificName is bdq:Empty through values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship and dwc:cultivarEpithet, or (3) if ambiguity produced by multiple matches in (1) or (2) can be disambiguated to a single Taxon using the values of dwc:subtribe, dwc:tribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID, dwc:taxonomicRank, and dwc:vernacularName; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:566faded-60b6-44bf-a335-dc78d5013582</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:taxonID,dwc:acceptedNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:scientificName,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:cultivarEpithet,dwc:vernacularName,dwc:scientificNameAuthorship,dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Return a result with no value and a Result.status of NOT_AMENDED with a Response.comment of ambiguous if the information provided does not resolve to a unique result (e.g. if homonyms exist and there is insufficient information in the provided data, for example using the lowest ranking taxa in conjunction with dwc:dwc:scientificNameAuthorship, to resolve them). When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Chicoreus palmarosae (Lamarck, 1822)", dwc:higherClassification="", dwc:kingdom="Animalia", dwc:phylum="Mollusca", dwc:class="Gastropoda", dwc:order="", dwc:family="Muricidae", dwc:subfamily="", dwc:genus="Chicoreus", dwc:genericName="Chicoreus", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="palmarosae", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="(Lamarck, 1822)", dwc:taxonRank="", bdq:sourceAuthority=”marinespecies.org”: Response.status=FILLED_IN, Response.result=dwc:scientificNameID="urn:lsid:marinespecies.org:taxname:208134", Response.comment="dwc:scientificName matched to unique taxon record in WoRMS, exact match on name and authorship. Resolvable at https://marinespecies.org/aphia.php?p=taxdetails&id=208134"],[dwc:scientificNameID="", dwc:taxonID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Graphis", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:family="", dwc:subfamily="", dwc:genus="", dwc:genericName="", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="", dwc:taxonRank="": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:scientificName="Graphis" is ambiguous as could be either a lichen or a gastropod."]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025), Arctos, MCZbase, Symbiota</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L393</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>FP-Akka</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/57</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>b1f2699b-3b7e-41a1-9e5c-f670559664ba</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON with Specification Specification for: AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f01fb3f9-2f7e-418b-9f51-adf50f202aea"></a>Term Name  bdqtest:f01fb3f9-2f7e-418b-9f51-adf50f202aea</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:scientificName from dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f01fb3f9-2f7e-418b-9f51-adf50f202aea</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f01fb3f9-2f7e-418b-9f51-adf50f202aea-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:scientificName using the dwc:scientificNameID value from the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty, or dwc:scientificName is bdq:NotEmpty; FILLED_IN the value of dwc:scientificName if the value of dwc: scientificNameID could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:8e8355a6-e5d0-4ad7-9f2c-8a4148bfda57</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The value of dwc:scientificNameID is unambiguous if dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority. When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID. Implementers can be aware of the current GBIF api endpoint that can replace the pseduo-namespace gbif: when looking up the dwc:scientificNameID (taxonID in the gbif document), e.g. `s/gbif:/https:\/\/api.gbif.org\/v1\/species\// ` will transform the value taxonID=gbif:8102122 to the resolvable endpoint https://api.gbif.org/v1/species/8102122. The pseudo-namespace "gbif:" is recommended by GBIF to reference GBIF taxon records. Where resolvable persistent identifiers exist for dwc:scientificNameID values, they should be used in full, but implementers will need to support at least the "gbif:" pseudo-namespace.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameID="gbif:8102122", dwc:scientificName="": Response.status=FILLED_IN, Response.result=dwc:scientificName="Harpullia pendula F.Muell.", Response.comment="dwc:scientificNameID contains an interpretable value"],[dwc:scientificNameID="gbif:8a", dwc:scientificName="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:scientificNameID does not contain an interpretable value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1152</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/71</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment NAME CODED Test VOCABULARY Completeness Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>0127389b-a68d-4393-a84c-aa9c690bd0e7</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID with Specification Specification for: AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_33c45ae1-e2db-462a-a59e-7169bb01c5d6"></a>Term Name  bdqtest:33c45ae1-e2db-462a-a59e-7169bb01c5d6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_SEX_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:sex Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/33c45ae1-e2db-462a-a59e-7169bb01c5d6</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/33c45ae1-e2db-462a-a59e-7169bb01c5d6-2024-03-25</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:sex using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; AMENDED the value of dwc:sex if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:08a4abb0-8977-4805-a4a1-c1a96b532322</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:sex</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, a list of synonyms for dwc:sex values can be found at https://registry.gbif.org/vocabulary/Sex/concepts.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:sex="f": Response.status=AMENDED, Response.result=dwc:sex="Female", Response.comment="dwc:sex found in the bdq:sourceAuthority"],[dwc:sex="x": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:sex not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L2148</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/284</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>e35dd18a-9c69-4aef-9b70-3d36d7eb6bd4</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_SEX_STANDARDIZED with Specification Specification for: AMENDMENT_SEX_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_SEX_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_e39098df-ef46-464c-9aef-bcdeee2a88cb"></a>Term Name  bdqtest:e39098df-ef46-464c-9aef-bcdeee2a88cb</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_TAXONRANK_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:taxonRank Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/e39098df-ef46-464c-9aef-bcdeee2a88cb</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/e39098df-ef46-464c-9aef-bcdeee2a88cb-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:taxonRank using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; AMENDED the value of dwc:taxonRank if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:ca6b9d39-4a1d-4ec5-925a-d1d67f95bea0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For reference, information about possible values of dwc:taxonRank can be found at https://registry.gbif.org/vocabulary/TaxonRank/concepts</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonRank="sp.": Response.status=AMENDED, Response.result=dwc:taxonRank="species", Response.comment="dwc:taxonRank contains an interpretable value in the bdq:sourceAuthority"],[dwc:taxonRank="sic.": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:taxonRank does not contain an interpretable value in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L2272</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/163</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>ef83a8c4-62f3-4e18-b589-07bc6f178cd7</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_TAXONRANK_STANDARDIZED with Specification Specification for: AMENDMENT_TAXONRANK_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_TAXONRANK_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b3471c65-b53e-453b-8282-abfa27bf1805"></a>Term Name  bdqtest:b3471c65-b53e-453b-8282-abfa27bf1805</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>AMENDMENT_TYPESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Amendment dwc:typeStatus Standardized</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b3471c65-b53e-453b-8282-abfa27bf1805</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b3471c65-b53e-453b-8282-abfa27bf1805-2024-11-11</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Proposes an amendment to the value of dwc:typeStatus using the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; AMENDED the value of the first word in each &#124; delimited portion of dwc:typeStatus if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:401e2562-cb26-43a7-8690-b06eabd5982a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:typeStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF TypeStatus Vocabulary" {[https://api.gbif.org/v1/vocabularies/TypeStatus]} {dwc:typeStatus vocabulary API [https://api.gbif.org/v1/vocabularies/TypeStatus/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Valuable for data quality needs related to voucher specimens in natural science collections. Almost all occurrence data will have no value in dwc:typeStatus. For reference, a vocabulary of synonyms can be found for dwc:typeStatus at [https://registry.gbif.org/vocabulary/TypeStatus/concepts].</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:typeStatus="Holo.": Response.status=AMENDED, Response.result=dwc:typeStatus="Holotype", Response.comment="dwc:typeStatus found in the bdq:sourceAuthority"],[dwc:typeStatus="x": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:typeStatus not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Amendment</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Enhancement</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L2338</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/286</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Amendment OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>a10eb348-7fc5-4b96-88e3-619300cb0079</td>
		</tr>
		<tr>
			<td>AmendmentMethod label</td>
			<td>AmendmentMethod: AMENDMENT_TYPESTATUS_STANDARDIZED with Specification Specification for: AMENDMENT_TYPESTATUS_STANDARDIZED</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: AMENDMENT_TYPESTATUS_STANDARDIZED</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1"></a>Term Name  bdqtest:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_ANNOTATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Issue Annotation Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-17</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are there any annotations associated with the record?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:annotationSystem is not available; POTENTIAL_ISSUE if an annotation in the bdq:annotationSystem exists with a matching bdq:annotationAlertIf; otherwise NOT_ISSUE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1999e4e0-ce3a-46e3-b131-24412bd94bd1</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>AllDarwinCoreTerms</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:annotationSystem,bdq:annotationAlertIf</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:annotationSystem default = "W3C Web Annotation" {[https://www.w3.org/annotation/]} {"oa:Annotation vocabulary" {[https://www.w3.org/TR/annotation-vocab/]},bdq:annotationAlertIf default = "oa:Annotation with oa:hasTarget having as object any dwciri:term instance that is part of the SingleRecord under Test." {[https://www.w3.org/TR/annotation-vocab/]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>While there is a W3C standard on 'web annotation', there is no TDWG recommendation on how this standard could be applied to annotating Darwin Core records. While implementation of this Test is currently problematic, TG2 considers annotations attached to any aspect of a Darwin Core record justifies this Test as a placeholder in the hope of future developments.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[bdq:annotationAlertIf="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="bdq:annotationAlertIf is bdq:Empty"],[bdq:annotationAlertIf="?": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="bdq:annotationAlertIf is bdq:NotEmpty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, Lee Belbin</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/29</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Issue OTHER Test CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_256e51b3-1e08-4349-bb7e-5186631c3f8e"></a>Term Name  bdqtest:256e51b3-1e08-4349-bb7e-5186631c3f8e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_COORDINATES_CENTEROFCOUNTRY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Issue Coordinates Center of Country</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/256e51b3-1e08-4349-bb7e-5186631c3f8e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/256e51b3-1e08-4349-bb7e-5186631c3f8e-2024-08-28</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are the supplied geographic coordinates within a defined buffer of the center of the country?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if any of dwc:countryCode, dwc:decimalLatitude, dwc:decimalLongitude are bdq:Empty; POTENTIAL_ISSUE if (1) the geographic coordinates are within the distance given by bdq:spatialBufferInMeters from the center of the supplied dwc:countryCode as represented in the bdq:sourceAuthority (or one of the centers, if the bdq:sourceAuthority provides more than one per country code) and (2) the dwc:coordinateUncertaintyInMeters is bdq:Empty or less than half the square root of the area of the country; otherwise NOT_ISSUE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:693aa9a5-6058-4399-a474-43268a8e503b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:countryCode,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:coordinateUncertaintyInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:spatialBufferInMeters,bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:spatialBufferInMeters default = "5000",bdq:sourceAuthority default = "GBIF Catalogue of Country Centroides" {[https://raw.githubusercontent.com/jhnwllr/catalogue-of-centroids/master/PCLI.tsv]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have increased the buffer to 5000 meters to cater for differences that may have arisen due to the difference in geodetic datums.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="-35.38804", dwc:decimalLongitude="-65.154964", dwc:countryCode="AR": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="coordinates fall within buffered distance in the bdq:sourceAuthority for dwc:countryCode"],[dwc:decimalLatitude="-34.184199", dwc:decimalLongitude="-65.509403", dwc:countryCode="AR": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="coordinates fall outside buffered distance in the bdq:sourceAuthority for dwc:countryCode"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Likely</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L3632</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/287</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Issue SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>9c0a82d5-4b24-4160-a000-ee9429bef8f7,2c441806-b56b-4252-9944-e331f9f3fee6</td>
		</tr>
		<tr>
			<td>IssueMethod label</td>
			<td>IssueMethod: ISSUE_COORDINATES_CENTEROFCOUNTRY with Specification Specification for: ISSUE_COORDINATES_CENTEROFCOUNTRY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: ISSUE_COORDINATES_CENTEROFCOUNTRY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_13d5a10e-188e-40fd-a22c-dbaa87b91df2"></a>Term Name  bdqtest:13d5a10e-188e-40fd-a22c-dbaa87b91df2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_DATAGENERALIZATIONS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Issue dwc:dataGeneralizations Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/13d5a10e-188e-40fd-a22c-dbaa87b91df2-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:dataGeneralizations?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>POTENTIAL_ISSUE if dwc:dataGeneralizations is bdq:NotEmpty; otherwise NOT_ISSUE</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:90618419-452d-4f35-b39a-7c342ca0791b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:dataGeneralizations</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is not specific to spatial data, any value in the dwc:dataGeneralizations field will cause this flag to be raised, but the primary use case is expected to be that dwc:dataGeneralizations demonstrates obfuscated locations.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dataGeneralizations="placed on quarter degree grid": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="dwc:dataGeneralizations is bdq:NotEmpty"],[dwc:dataGeneralizations="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="dwc:dataGeneralizations is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Resolution</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/d742991440f2f5fc6ffc75dfe3b6d2ab5b6826b2/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L138</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/72</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Issue NAME SPACE TIME CODED Test Resolution CORE</td>
		</tr>
		<tr>
			<td>IssueMethod label</td>
			<td>IssueMethod: ISSUE_DATAGENERALIZATIONS_NOTEMPTY with Specification Specification for: ISSUE_DATAGENERALIZATIONS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: ISSUE_DATAGENERALIZATIONS_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_acc8dff2-d8d1-483a-946d-65a02a452700"></a>Term Name  bdqtest:acc8dff2-d8d1-483a-946d-65a02a452700</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Issue dwc:establishmentMeans Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/acc8dff2-d8d1-483a-946d-65a02a452700</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/acc8dff2-d8d1-483a-946d-65a02a452700-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:establishmentMeans?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>POTENTIAL_ISSUE if dwc:establishmentMeans is bdq:NotEmpty; otherwise NOT_ISSUE</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c69007a2-6391-463e-96bc-baa18d24beb7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:establishmentMeans</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:establishmentMeans="?": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="dwc:establishmentMeans is bdq:NotEmpty"],[dwc:establishmentMeans="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="dwc:establishmentMeans is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Issue</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L241</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, CRIA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/94</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Issue OTHER CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>IssueMethod label</td>
			<td>IssueMethod: ISSUE_ESTABLISHMENTMEANS_NOTEMPTY with Specification Specification for: ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_03049fe5-a575-404f-b564-ae63f5a1cf8b"></a>Term Name  bdqtest:03049fe5-a575-404f-b564-ae63f5a1cf8b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_AMENDMENTS_PROPOSED</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measure Amendments Proposed</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/03049fe5-a575-404f-b564-ae63f5a1cf8b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/03049fe5-a575-404f-b564-ae63f5a1cf8b-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>A count of the number of distinct AMENDMENT Tests that have a Response.status="AMENDED" for a given record.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>The number of Tests of output type AMENDMENT that have been run against the record and have proposed changes to the record (Result.status="AMENDED")</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:7e365897-cfc0-413e-a613-99c6050edc4b</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>bdq:AllAmendmentTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="17", Response.comment="17 Tests of TYPE AMENDMENT were run and proposed changes to the record."]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>John Wieczorek</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/65</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Measure NAME SPACE TIME OTHER Test CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_56b6c695-adf1-418e-95d2-da04cad7be53"></a>Term Name  bdqtest:56b6c695-adf1-418e-95d2-da04cad7be53</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_EVENTDATE_DURATIONINSECONDS</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measure dwc:eventDate Duration in Seconds</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/56b6c695-adf1-418e-95d2-da04cad7be53</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/56b6c695-adf1-418e-95d2-da04cad7be53-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>What is the duration of dwc:eventDate in seconds?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; otherwise RUN_HAS_RESULT with the result being the duration (sensu ISO 8601) expressed in the dwc:eventDate, in seconds.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:be93a0ef-9bf7-417f-a26e-daae5d00dabb</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The duration of a day is 86400 seconds. Implementations should treat all days as 86400 seconds, but should include leap days (but not leap seconds) in durations that encompass them. Consumers should treat assertions about event date duration as approximations, see: https://xkcd.com/2867/</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1880-05-08/10": Response.status=RUN_HAS_RESULT, Response.result="259200", Response.comment="dwc:eventDate duration is 3 days = 259,200 seconds"],[dwc:eventDate="95": Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.result=NOT_REPORTED, Response.comment="dwc:eventDate does not contain a valid ISO 8601-1:2019 date"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Resolution</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L120</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Alex Thompson</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/140</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Measure TIME CODED Test CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_45fb49eb-4a1b-4b49-876f-15d5034dfc73"></a>Term Name  bdqtest:45fb49eb-4a1b-4b49-876f-15d5034dfc73</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_VALIDATIONTESTS_COMPLIANT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measure Validation Tests Compliant</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/45fb49eb-4a1b-4b49-876f-15d5034dfc73</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/45fb49eb-4a1b-4b49-876f-15d5034dfc73-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measures the number of distinct VALIDATION Tests that have a Response.status="COMPLIANT" for a given record.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if no Tests of type VALIDATION were attempted to be run; Report the number of Tests of output type VALIDATION run against the record that were COMPLIANT (passed)</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b611e1b1-cbf5-405c-b24d-24e9a649cbf0</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>bdq:AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of Tests that were attempted, add all three measures. To get the total number of Tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="7", Response.comment="7 VALIDATION Tests had Response.status="COMPLIANT" ]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/135</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Measure NAME SPACE OTHER Test CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_453844ae-9df4-439f-8e24-c52498eca84a"></a>Term Name  bdqtest:453844ae-9df4-439f-8e24-c52498eca84a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_VALIDATIONTESTS_NOTCOMPLIANT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measure Validation Tests Not Compliant</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/453844ae-9df4-439f-8e24-c52498eca84a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-24</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/453844ae-9df4-439f-8e24-c52498eca84a-2024-08-22</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>A count of the number of distinct VALIDATION Tests that have a Response.status="NOT_COMPLIANT" for a given record.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if no Tests of type VALIDATION were attempted to be run; REPORT of the number of Tests of output type VALIDATION run against the record that have Response.result="NOT_COMPLIANT"</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1a7adc4a-58ee-480c-9765-3834ea433bf0</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>bdq:AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of Tests that were attempted, add all three measures. To get the total number of Tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="37", Response.comment="37 VALIDATION Tests had Response.status="NOT_COMPLIANT."]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Lee Belbin</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/31</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Measure NAME SPACE TIME OTHER Test CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_49a94636-a562-4e6b-803c-665c80628a3d"></a>Term Name  bdqtest:49a94636-a562-4e6b-803c-665c80628a3d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measure Validation Tests Prerequisites Not Met</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/49a94636-a562-4e6b-803c-665c80628a3d</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-25</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/49a94636-a562-4e6b-803c-665c80628a3d-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>The number of distinct VALIDATION Tests that have a Response.status="EXTERNAL_PREREQUISITES_NOT_MET" or "INTERNAL_PREREQUISITES_NOT_MET" for a given record.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if no Tests of type VALIDATION were run; Report the number of Tests of output type VALIDATION that did not run because prerequisites for those Tests were not met (Result.status="INTERNAL_PREREQUISITES_NOT_MET" or "EXTERNAL_PREREQUISITES_NOT_MET")</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:aefe88ed-6d3a-4824-8c4a-a75714cb0351</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>bdq:AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of Tests that were attempted, add all three measures. To get the total number of Tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[Response.status=RUN_HAS_RESULT, Response.result="27", Response.comment="27 VALIDATION Tests had either INTERNAL_PREREQUISITES_NOT_MET" or "EXTERNAL_PREREQUISITES_NOT_MET"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/134</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Measure NAME SPACE TIME OTHER Test CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b60c8c58-0137-4b6a-97e9-57d8ca5cf248"></a>Term Name  bdqtest:b60c8c58-0137-4b6a-97e9-57d8ca5cf248</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:basisOfRecord Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b60c8c58-0137-4b6a-97e9-57d8ca5cf248</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b60c8c58-0137-4b6a-97e9-57d8ca5cf248-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:5aabe3d4-d2c0-415c-8972-c834b543971a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f5dd74bd-6a22-4792-b675-c7ccf2a2c103"></a>Term Name  bdqtest:f5dd74bd-6a22-4792-b675-c7ccf2a2c103</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:basisOfRecord Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f5dd74bd-6a22-4792-b675-c7ccf2a2c103</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f5dd74bd-6a22-4792-b675-c7ccf2a2c103-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_BASISOFRECORD_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f094b94f-09b6-4fb0-8ba4-24252a2101c4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a56fb342-c8ee-4611-8aab-e6c6357e8875"></a>Term Name  bdqtest:a56fb342-c8ee-4611-8aab-e6c6357e8875</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Classification Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a56fb342-c8ee-4611-8aab-e6c6357e8875</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a56fb342-c8ee-4611-8aab-e6c6357e8875-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_CLASSIFICATION_CONSISTENT in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_CLASSIFICATION_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:21d0b5f6-5b3e-4810-8413-c975b7cf343a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Consistency Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7270a362-5f2e-41f0-955a-d7a8eaaf0f17"></a>Term Name  bdqtest:7270a362-5f2e-41f0-955a-d7a8eaaf0f17</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:class Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7270a362-5f2e-41f0-955a-d7a8eaaf0f17</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7270a362-5f2e-41f0-955a-d7a8eaaf0f17-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_CLASS_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_CLASS_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a2b39526-d08a-4a91-8b6d-aacf73677789</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_CLASS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d68dc111-9704-4fc5-a8eb-5fa084809202"></a>Term Name  bdqtest:d68dc111-9704-4fc5-a8eb-5fa084809202</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d68dc111-9704-4fc5-a8eb-5fa084809202</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d68dc111-9704-4fc5-a8eb-5fa084809202-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4343a7e0-7f0b-434d-99d4-e939ecb16e1f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency ISO/DCMI STANDARD Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c6c998af-6145-4361-b1e6-52c5b790340a"></a>Term Name  bdqtest:c6c998af-6145-4361-b1e6-52c5b790340a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates dwc:stateProvince Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c6c998af-6145-4361-b1e6-52c5b790340a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c6c998af-6145-4361-b1e6-52c5b790340a-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4dd617df-a984-419f-b7b5-098b2023c4ab</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b67f41f4-198c-41e9-9419-ba3919c1be8b"></a>Term Name  bdqtest:b67f41f4-198c-41e9-9419-ba3919c1be8b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates Terrestrial Marine</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b67f41f4-198c-41e9-9419-ba3919c1be8b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b67f41f4-198c-41e9-9419-ba3919c1be8b-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:45cb9e13-7944-4535-a5ef-f6ededb77305</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0e239a55-0f19-4c68-bdbf-20580f27a647"></a>Term Name  bdqtest:0e239a55-0f19-4c68-bdbf-20580f27a647</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Coordinates Not Zero</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0e239a55-0f19-4c68-bdbf-20580f27a647</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0e239a55-0f19-4c68-bdbf-20580f27a647-2023-06-20</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATES_NOTZERO in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COORDINATES_NOTZERO in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b482148e-9ac2-47ad-99b5-462508e9f360</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATES_NOTZERO.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Likeliness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_2d90d94b-d384-4bac-aa68-c6800d765882"></a>Term Name  bdqtest:2d90d94b-d384-4bac-aa68-c6800d765882</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:coordinateUncertaintyInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/2d90d94b-d384-4bac-aa68-c6800d765882</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/2d90d94b-d384-4bac-aa68-c6800d765882-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COORDINATEUNCERTAINTY_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f8dfc3fc-6580-4518-b2b4-595c29e9042e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d71be8d4-1a04-4816-90c5-49808c823651"></a>Term Name  bdqtest:d71be8d4-1a04-4816-90c5-49808c823651</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:countryCode Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d71be8d4-1a04-4816-90c5-49808c823651</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d71be8d4-1a04-4816-90c5-49808c823651-2024-11-10</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d153d4bd-b39d-43b0-b00a-395ff3e2ca62</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_38966850-3737-4a67-953c-c231469e0489"></a>Term Name  bdqtest:38966850-3737-4a67-953c-c231469e0489</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/38966850-3737-4a67-953c-c231469e0489</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/38966850-3737-4a67-953c-c231469e0489-2024-09-19</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COUNTRYCODE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_26b46375-df2b-4677-a2e5-f96f86b8e242"></a>Term Name  bdqtest:26b46375-df2b-4677-a2e5-f96f86b8e242</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/26b46375-df2b-4677-a2e5-f96f86b8e242</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/26b46375-df2b-4677-a2e5-f96f86b8e242-2024-09-25</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:6f1093a0-0da5-4691-a95e-184d6d55eeb0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_8b73f37d-89ed-479a-8389-9e71ad2ac84d"></a>Term Name  bdqtest:8b73f37d-89ed-479a-8389-9e71ad2ac84d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country dwc:stateProvince Unambiguous</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/8b73f37d-89ed-479a-8389-9e71ad2ac84d</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/8b73f37d-89ed-479a-8389-9e71ad2ac84d-2024-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e5efdd20-d1fc-4287-91f9-15b9ce3f3aac</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f15c38c3-d96d-4e9c-982d-410fb71cf2bc"></a>Term Name  bdqtest:f15c38c3-d96d-4e9c-982d-410fb71cf2bc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f15c38c3-d96d-4e9c-982d-410fb71cf2bc</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f15c38c3-d96d-4e9c-982d-410fb71cf2bc-2024-08-19</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRY_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COUNTRY_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6887c881-dc52-409b-8979-9c2f05e55569"></a>Term Name  bdqtest:6887c881-dc52-409b-8979-9c2f05e55569</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:country Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6887c881-dc52-409b-8979-9c2f05e55569</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6887c881-dc52-409b-8979-9c2f05e55569-2024-09-27</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_COUNTRY_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_COUNTRY_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:34ef6ea2-de06-4d2c-88fe-2c779de8f7db</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c72fda2d-16e1-4ded-91a5-a7094339d603"></a>Term Name  bdqtest:c72fda2d-16e1-4ded-91a5-a7094339d603</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:dateIdentified In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c72fda2d-16e1-4ded-91a5-a7094339d603</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c72fda2d-16e1-4ded-91a5-a7094339d603-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a25786df-a624-4ff2-8962-6b23e8b07b0b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Likeliness ISO/DCMI STANDARD Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_49b787eb-7dce-4ace-97f5-7cbb47cd8cb9"></a>Term Name  bdqtest:49b787eb-7dce-4ace-97f5-7cbb47cd8cb9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/49b787eb-7dce-4ace-97f5-7cbb47cd8cb9</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/49b787eb-7dce-4ace-97f5-7cbb47cd8cb9-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DATEIDENTIFIED_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:89f8b2ea-fc35-4941-929a-0e32cfbeb1a6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_780480ff-8c4a-4276-aaca-cbd1248de9fa"></a>Term Name  bdqtest:780480ff-8c4a-4276-aaca-cbd1248de9fa</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:day In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/780480ff-8c4a-4276-aaca-cbd1248de9fa</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/780480ff-8c4a-4276-aaca-cbd1248de9fa-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DAY_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DAY_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2563ae15-a5bf-48fc-91f3-6df869aece2d</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DAY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c3e0100f-dfc3-4379-a855-df878eef295e"></a>Term Name  bdqtest:c3e0100f-dfc3-4379-a855-df878eef295e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:day Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c3e0100f-dfc3-4379-a855-df878eef295e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c3e0100f-dfc3-4379-a855-df878eef295e-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DAY_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DAY_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c0fce1a1-8879-4175-8a71-ce037655c358</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f041ab17-d834-4586-aa6b-090de2e571a8"></a>Term Name  bdqtest:f041ab17-d834-4586-aa6b-090de2e571a8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dc:type Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f041ab17-d834-4586-aa6b-090de2e571a8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f041ab17-d834-4586-aa6b-090de2e571a8-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DCTYPE_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DCTYPE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e1286c46-2a95-480d-89e4-f02681372eb7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_fbe47441-500f-44c7-a1bd-1e872edc5266"></a>Term Name  bdqtest:fbe47441-500f-44c7-a1bd-1e872edc5266</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dc:type Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/fbe47441-500f-44c7-a1bd-1e872edc5266</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/fbe47441-500f-44c7-a1bd-1e872edc5266-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DCTYPE_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DCTYPE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b85129f0-28c2-4ede-aff2-5ce3791c6e86</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26"></a>Term Name  bdqtest:f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLatitude In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a5111c0c-d198-4ecc-af10-809ae2b3ae01</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_bceae35a-52ab-4968-846f-069ace766513"></a>Term Name  bdqtest:bceae35a-52ab-4968-846f-069ace766513</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLatitude Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/bceae35a-52ab-4968-846f-069ace766513</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/bceae35a-52ab-4968-846f-069ace766513-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DECIMALLATITUDE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:0067fa60-5503-490e-8c94-93fb79cc7da2</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c70c4950-2246-4acc-a59d-81eaa47edf2b"></a>Term Name  bdqtest:c70c4950-2246-4acc-a59d-81eaa47edf2b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLongitude In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c70c4950-2246-4acc-a59d-81eaa47edf2b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c70c4950-2246-4acc-a59d-81eaa47edf2b-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1a504f7f-21a7-49e1-a0dc-f51146957fa4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f948a30e-8084-48d5-b1ca-d77c476f181f"></a>Term Name  bdqtest:f948a30e-8084-48d5-b1ca-d77c476f181f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLongitude Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f948a30e-8084-48d5-b1ca-d77c476f181f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f948a30e-8084-48d5-b1ca-d77c476f181f-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DECIMALLONGITUDE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c893ee17-ee8b-43ec-bf17-97ac814ea502</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_1b8ae68e-63f1-41c0-9025-fbe64db38d64"></a>Term Name  bdqtest:1b8ae68e-63f1-41c0-9025-fbe64db38d64</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:degreeofEstablishment Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/1b8ae68e-63f1-41c0-9025-fbe64db38d64</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/1b8ae68e-63f1-41c0-9025-fbe64db38d64-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fec2103b-5d46-4723-b2ec-8c8119b44aaf</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7775309b-5331-4a65-b839-cbe959948d33"></a>Term Name  bdqtest:7775309b-5331-4a65-b839-cbe959948d33</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:endDayOfYear In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7775309b-5331-4a65-b839-cbe959948d33</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7775309b-5331-4a65-b839-cbe959948d33-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_ENDDAYOFYEAR_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_ENDDAYOFYEAR_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:62f754b5-a0a1-4b24-9982-b76e4e169f71</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_130bb875-6b7c-4965-b864-d53f9d05b2cd"></a>Term Name  bdqtest:130bb875-6b7c-4965-b864-d53f9d05b2cd</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:establishmentMeans Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/130bb875-6b7c-4965-b864-d53f9d05b2cd</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/130bb875-6b7c-4965-b864-d53f9d05b2cd-2024-02-08</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_ESTABLISHMENTMEANS_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f1d3bf9c-5558-41dc-8e33-b17c499be016</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c8250600-de61-4047-9d7c-6e06a38c7994"></a>Term Name  bdqtest:c8250600-de61-4047-9d7c-6e06a38c7994</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c8250600-de61-4047-9d7c-6e06a38c7994</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c8250600-de61-4047-9d7c-6e06a38c7994-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTDATE_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_EVENTDATE_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:29a1fdc6-326b-4017-880d-d11ff0225b8f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3f62eaa2-747f-456b-85e6-1a6e74086a18"></a>Term Name  bdqtest:3f62eaa2-747f-456b-85e6-1a6e74086a18</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3f62eaa2-747f-456b-85e6-1a6e74086a18</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3f62eaa2-747f-456b-85e6-1a6e74086a18-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTDATE_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_EVENTDATE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1fae3f77-7fcb-42c6-ab43-1ff28adf4fa4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_bffd7499-aca3-423f-bb43-f7bdc9260f4f"></a>Term Name  bdqtest:bffd7499-aca3-423f-bb43-f7bdc9260f4f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/bffd7499-aca3-423f-bb43-f7bdc9260f4f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/bffd7499-aca3-423f-bb43-f7bdc9260f4f-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTDATE_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_EVENTDATE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:80c8f69b-4ad3-40ee-bccd-de016bfae367</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d3e282a1-3ff3-4ed0-bd08-fa23b6b8c161"></a>Term Name  bdqtest:d3e282a1-3ff3-4ed0-bd08-fa23b6b8c161</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Event Temporal Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d3e282a1-3ff3-4ed0-bd08-fa23b6b8c161</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d3e282a1-3ff3-4ed0-bd08-fa23b6b8c161-2023-09-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_EVENTTEMPORAL_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b57460c4-16e1-4c1d-8a07-a53aee9e8922</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_1919f212-b7db-4b6e-9697-41a715001bd6"></a>Term Name  bdqtest:1919f212-b7db-4b6e-9697-41a715001bd6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Event Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/1919f212-b7db-4b6e-9697-41a715001bd6</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/1919f212-b7db-4b6e-9697-41a715001bd6-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_EVENT_CONSISTENT in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_EVENT_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:83d057ea-a6f6-49e6-ac3c-0c418776a0e0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENT_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Consistency CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_97928242-11a9-4ab0-9dd7-3f0465834824"></a>Term Name  bdqtest:97928242-11a9-4ab0-9dd7-3f0465834824</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:family Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/97928242-11a9-4ab0-9dd7-3f0465834824</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/97928242-11a9-4ab0-9dd7-3f0465834824-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_FAMILY_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_FAMILY_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:16f999d9-1cf5-4208-b2ca-1a93d6700085</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_FAMILY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_977f7e75-a88e-4e29-a7b1-e8cdd35aa107"></a>Term Name  bdqtest:977f7e75-a88e-4e29-a7b1-e8cdd35aa107</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:genus Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/977f7e75-a88e-4e29-a7b1-e8cdd35aa107</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/977f7e75-a88e-4e29-a7b1-e8cdd35aa107-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_GENUS_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_GENUS_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:15bbda19-dd18-471a-a5c3-56c7e543012f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_GENUS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_63fbaf3c-3d41-4ab6-bfc0-904f1b26835f"></a>Term Name  bdqtest:63fbaf3c-3d41-4ab6-bfc0-904f1b26835f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:geodeticDatum Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/63fbaf3c-3d41-4ab6-bfc0-904f1b26835f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/63fbaf3c-3d41-4ab6-bfc0-904f1b26835f-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a3c8b277-15fb-4ae8-afb1-e64fb6eb5241</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63"></a>Term Name  bdqtest:8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Vaildation dwc:geodeticDatum Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63-2025-03-03</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_GEODETICDATUM_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:5cc05662-c029-4ba9-b32e-fb487ccba71c</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_012eade5-fc64-458a-a13a-a614491bf4e0"></a>Term Name  bdqtest:012eade5-fc64-458a-a13a-a614491bf4e0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:kingdom Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/012eade5-fc64-458a-a13a-a614491bf4e0</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/012eade5-fc64-458a-a13a-a614491bf4e0-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_KINGDOM_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_KINGDOM_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a90e100a-3522-4742-aa73-3b98a35ab826</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_342bd81c-e2b7-41d8-b32b-013992d19f99"></a>Term Name  bdqtest:342bd81c-e2b7-41d8-b32b-013992d19f99</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:kingdom Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/342bd81c-e2b7-41d8-b32b-013992d19f99</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/342bd81c-e2b7-41d8-b32b-013992d19f99-2024-01-28</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_KINGDOM_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_KINGDOM_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e6f0a9ce-3e72-40fb-9fad-63cf5962f93e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_47ee20d9-5087-4f76-a494-6fea05e50b8b"></a>Term Name  bdqtest:47ee20d9-5087-4f76-a494-6fea05e50b8b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dcterms:license Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/47ee20d9-5087-4f76-a494-6fea05e50b8b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/47ee20d9-5087-4f76-a494-6fea05e50b8b-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_LICENSE_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_LICENSE_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d8b450af-47e6-4f5c-8154-6d6acbe9efa5</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_9d5be694-f5da-465d-8c7e-27e6dac69f9f"></a>Term Name  bdqtest:9d5be694-f5da-465d-8c7e-27e6dac69f9f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dcterms:license Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/9d5be694-f5da-465d-8c7e-27e6dac69f9f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/9d5be694-f5da-465d-8c7e-27e6dac69f9f-2024-03-21</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_LICENSE_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_LICENSE_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2a9dbd16-d427-471e-8db5-c1de2b2cf030</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_bac852b5-1ba6-427b-aa8e-02018e99279c"></a>Term Name  bdqtest:bac852b5-1ba6-427b-aa8e-02018e99279c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dcterms:Location Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/bac852b5-1ba6-427b-aa8e-02018e99279c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/bac852b5-1ba6-427b-aa8e-02018e99279c-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_LOCATION_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_LOCATION_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:30ed5e2d-ef30-4988-8dbb-12c119e94ac3</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_LOCATION_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3de8af03-05d4-4fd8-8e6d-ba886dc5446f"></a>Term Name  bdqtest:3de8af03-05d4-4fd8-8e6d-ba886dc5446f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:maximumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3de8af03-05d4-4fd8-8e6d-ba886dc5446f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3de8af03-05d4-4fd8-8e6d-ba886dc5446f-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MAXDEPTH_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_MAXDEPTH_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:cebc8ba0-ca02-4f1e-830e-ec693bc628e4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MAXDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5"></a>Term Name  bdqtest:6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:maximumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MAXELEVATION_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_MAXELEVATION_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f9471802-a5f7-4f4e-9810-f3f4f43dad1a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MAXELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Likeliness Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_9c66c116-6644-45b4-b4c7-db7a4ee7c500"></a>Term Name  bdqtest:9c66c116-6644-45b4-b4c7-db7a4ee7c500</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:minimumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/9c66c116-6644-45b4-b4c7-db7a4ee7c500</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/9c66c116-6644-45b4-b4c7-db7a4ee7c500-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINDEPTH_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_MINDEPTH_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b21256c2-4bb7-4deb-852d-a9eaa05345e7"></a>Term Name  bdqtest:b21256c2-4bb7-4deb-852d-a9eaa05345e7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:minimumDepthInMeters less than dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b21256c2-4bb7-4deb-852d-a9eaa05345e7</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b21256c2-4bb7-4deb-852d-a9eaa05345e7-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:12f7f82e-ab1c-4690-92b8-ecc9328256c1</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_071267a0-d993-4961-a3f7-d8210810d167"></a>Term Name  bdqtest:071267a0-d993-4961-a3f7-d8210810d167</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:minimumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/071267a0-d993-4961-a3f7-d8210810d167</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/071267a0-d993-4961-a3f7-d8210810d167-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINELEVATION_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_MINELEVATION_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2bb79221-0312-410a-aef6-f569485df6a6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_be2eb717-b390-47d1-b7ba-965a1101e215"></a>Term Name  bdqtest:be2eb717-b390-47d1-b7ba-965a1101e215</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:minimumElevationInMeters less than dwcmaximumElevationInMeters</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/be2eb717-b390-47d1-b7ba-965a1101e215</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/be2eb717-b390-47d1-b7ba-965a1101e215-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f799fb5c-37e4-46d7-a07e-87eb071df9c6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3"></a>Term Name  bdqtest:c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:month Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_MONTH_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_MONTH_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2c5dbdbb-feab-474c-bcca-bf6d1b90ae66</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MONTH_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_36ea0a78-a079-4014-aca3-2f2b3b11e822"></a>Term Name  bdqtest:36ea0a78-a079-4014-aca3-2f2b3b11e822</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:namePublishedInYear Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/36ea0a78-a079-4014-aca3-2f2b3b11e822</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/36ea0a78-a079-4014-aca3-2f2b3b11e822-2024-02-07</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f09fc9ad-a449-4422-b32f-63d8ccf2501f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0c9a139e-5d23-44de-a495-14ec08c61a1c"></a>Term Name  bdqtest:0c9a139e-5d23-44de-a495-14ec08c61a1c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceID Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0c9a139e-5d23-44de-a495-14ec08c61a1c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0c9a139e-5d23-44de-a495-14ec08c61a1c-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_OCCURRENCEID_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_OCCURRENCEID_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3d9e1339-19d7-47e7-af9e-11905df82b6a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_298db0c9-a85a-41ee-b111-d622fd969d71"></a>Term Name  bdqtest:298db0c9-a85a-41ee-b111-d622fd969d71</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceStatus Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/298db0c9-a85a-41ee-b111-d622fd969d71</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/298db0c9-a85a-41ee-b111-d622fd969d71-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c3a53898-c4ad-40e0-961b-b4ceafea37c7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_faca6558-dbff-4d26-a5cb-e11cdf632fe7"></a>Term Name  bdqtest:faca6558-dbff-4d26-a5cb-e11cdf632fe7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceStatus Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/faca6558-dbff-4d26-a5cb-e11cdf632fe7</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/faca6558-dbff-4d26-a5cb-e11cdf632fe7-2025-02-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_OCCURRENCESTATUS_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fbe854d4-acf3-4c79-a654-81441fed644f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f4fa449c-4b74-4dcf-b4cf-0b73e1496375"></a>Term Name  bdqtest:f4fa449c-4b74-4dcf-b4cf-0b73e1496375</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:order Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f4fa449c-4b74-4dcf-b4cf-0b73e1496375</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f4fa449c-4b74-4dcf-b4cf-0b73e1496375-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_ORDER_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_ORDER_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:ae08b4b4-89ba-4972-b51f-912b132bd006</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_ORDER_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_15e0da1d-1a43-4075-8454-b2e618cdd25b"></a>Term Name  bdqtest:15e0da1d-1a43-4075-8454-b2e618cdd25b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:pathway Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/15e0da1d-1a43-4075-8454-b2e618cdd25b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/15e0da1d-1a43-4075-8454-b2e618cdd25b-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_PATHWAY_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_PATHWAY_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c7c92ef0-284e-4c5d-8fc9-f1480bfe0b8e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_PATHWAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_65e66ca0-e9d1-4411-ad26-bb9c43f32afc"></a>Term Name  bdqtest:65e66ca0-e9d1-4411-ad26-bb9c43f32afc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:phylum Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/65e66ca0-e9d1-4411-ad26-bb9c43f32afc</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/65e66ca0-e9d1-4411-ad26-bb9c43f32afc-2022-03-25</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_PHYLUM_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_PHYLUM_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1193230f-f188-4917-92da-bba3390ed3fa</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_PHYLUM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7da5428e-87b2-4ec2-be82-05b9398b7577"></a>Term Name  bdqtest:7da5428e-87b2-4ec2-be82-05b9398b7577</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation Polynomial Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7da5428e-87b2-4ec2-be82-05b9398b7577</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7da5428e-87b2-4ec2-be82-05b9398b7577-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_POLYNOMIAL_CONSISTENT in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_POLYNOMIAL_CONSISTENT in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d92c5e23-bf6a-483b-86c3-9374e12d01c7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Consistency CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_dbf3cece-1d83-426e-a5e0-8158fcf9c0cd"></a>Term Name  bdqtest:dbf3cece-1d83-426e-a5e0-8158fcf9c0cd</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameAuthorship Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/dbf3cece-1d83-426e-a5e0-8158fcf9c0cd</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/dbf3cece-1d83-426e-a5e0-8158fcf9c0cd-2024-02-04</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e9ffc3b0-0fb8-4a7c-a588-a00085ba980b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f174ad13-3c67-49f9-8d8b-aba4e933d6f6"></a>Term Name  bdqtest:f174ad13-3c67-49f9-8d8b-aba4e933d6f6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameID Complete</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f174ad13-3c67-49f9-8d8b-aba4e933d6f6</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f174ad13-3c67-49f9-8d8b-aba4e933d6f6-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_COMPLETE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e6c02558-8541-4292-9a11-2f4408d69699</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a9962d33-ad08-453a-8938-2972425034c2"></a>Term Name  bdqtest:a9962d33-ad08-453a-8938-2972425034c2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameID Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a9962d33-ad08-453a-8938-2972425034c2</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a9962d33-ad08-453a-8938-2972425034c2-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:02242018-3e73-4e0a-8d6f-d1db06cf81a3</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4e70b0e4-3fd2-4899-802c-439671374eeb"></a>Term Name  bdqtest:4e70b0e4-3fd2-4899-802c-439671374eeb</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificName Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4e70b0e4-3fd2-4899-802c-439671374eeb</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4e70b0e4-3fd2-4899-802c-439671374eeb-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3c2fe7e9-186f-4ceb-8274-8bbcb4a62de4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0f8b30e2-59dc-46ba-8b91-62049cd1a4e2"></a>Term Name  bdqtest:0f8b30e2-59dc-46ba-8b91-62049cd1a4e2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:scientificName Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0f8b30e2-59dc-46ba-8b91-62049cd1a4e2</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0f8b30e2-59dc-46ba-8b91-62049cd1a4e2-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_SCIENTIFICNAME_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a9c18563-f63e-42db-98e5-a3e6079086b7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_e4d35063-2366-4dda-8eaa-326340361da3"></a>Term Name  bdqtest:e4d35063-2366-4dda-8eaa-326340361da3</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:sex Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/e4d35063-2366-4dda-8eaa-326340361da3</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/e4d35063-2366-4dda-8eaa-326340361da3-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_SEX_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_SEX_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:72471db4-226c-454f-bbe8-5c1718e6c834</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SEX_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_76008c6b-c56a-4233-84e3-8584950037ec"></a>Term Name  bdqtest:76008c6b-c56a-4233-84e3-8584950037ec</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:startDayOfYear In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/76008c6b-c56a-4233-84e3-8584950037ec</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/76008c6b-c56a-4233-84e3-8584950037ec-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_STARTDAYOFYEAR_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_STARTDAYOFYEAR_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:53c6af68-6120-4da6-87d8-a3e9551b9671</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_58fdd5c1-6201-49a1-a7cd-f49c210dc0b6"></a>Term Name  bdqtest:58fdd5c1-6201-49a1-a7cd-f49c210dc0b6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:stateProvince Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/58fdd5c1-6201-49a1-a7cd-f49c210dc0b6</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/58fdd5c1-6201-49a1-a7cd-f49c210dc0b6-2024-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_STATEPROVINCE_FOUND in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_STATEPROVINCE_FOUND in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d261fac1-ce61-4879-bc04-870fa885b578</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_STATEPROVINCE_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_de661615-b338-4557-af5b-d44a89de40fa"></a>Term Name  bdqtest:de661615-b338-4557-af5b-d44a89de40fa</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:taxonRank Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/de661615-b338-4557-af5b-d44a89de40fa</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/de661615-b338-4557-af5b-d44a89de40fa-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXONRANK_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_TAXONRANK_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c619ec9b-92ec-4047-a8d3-931e3324bf3e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_602bc457-6b1d-4f24-adef-d0d31bcdf2f0"></a>Term Name  bdqtest:602bc457-6b1d-4f24-adef-d0d31bcdf2f0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:taxonRank Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/602bc457-6b1d-4f24-adef-d0d31bcdf2f0</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/602bc457-6b1d-4f24-adef-d0d31bcdf2f0-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXONRANK_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_TAXONRANK_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c8964200-630e-47c6-baad-7e334fddbbdb</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_54d290e8-ac48-4f31-8af3-676363573217"></a>Term Name  bdqtest:54d290e8-ac48-4f31-8af3-676363573217</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Taxon Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/54d290e8-ac48-4f31-8af3-676363573217</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/54d290e8-ac48-4f31-8af3-676363573217-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXON_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_TAXON_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f38e3644-354d-4180-bc7c-c437cef1d606</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_782773c9-7b37-483d-8ce2-c6683ba81882"></a>Term Name  bdqtest:782773c9-7b37-483d-8ce2-c6683ba81882</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:Taxon Unambiguous</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/782773c9-7b37-483d-8ce2-c6683ba81882</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/782773c9-7b37-483d-8ce2-c6683ba81882-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TAXON_UNAMBIGUOUS in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_TAXON_UNAMBIGUOUS in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:8bd6f6de-49e4-4889-82e0-e4af093981e0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b5a14d76-292e-499b-b80f-9546243311a0"></a>Term Name  bdqtest:b5a14d76-292e-499b-b80f-9546243311a0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:typeStatus Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b5a14d76-292e-499b-b80f-9546243311a0</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b5a14d76-292e-499b-b80f-9546243311a0-2024-11-11</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_TYPESTATUS_STANDARD in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_TYPESTATUS_STANDARD in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e4dbf38d-bdd7-4cf7-8c60-5b3bfc6af4ff</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TYPESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_aee65eb8-8d1e-4b8f-bd37-5822e29f5734"></a>Term Name  bdqtest:aee65eb8-8d1e-4b8f-bd37-5822e29f5734</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:year In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/aee65eb8-8d1e-4b8f-bd37-5822e29f5734</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/aee65eb8-8d1e-4b8f-bd37-5822e29f5734-2024-08-23</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_YEAR_INRANGE in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_YEAR_INRANGE in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:aee43366-0352-448a-a5ea-85ddc8605da1</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_687d3ad1-93a3-4a1f-b69f-da5a1eb761a5"></a>Term Name  bdqtest:687d3ad1-93a3-4a1f-b69f-da5a1eb761a5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord Counting Compliance of Validation dwc:year Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/687d3ad1-93a3-4a1f-b69f-da5a1eb761a5</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/687d3ad1-93a3-4a1f-b69f-da5a1eb761a5-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Count the number of VALIDATION_YEAR_NOTEMPTY in a record set that are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>Count the number of VALIDATION_YEAR_NOTEMPTY in the MultiRecord that have Response.result=COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:42f331f4-a5a8-48b4-a08e-57048d1d1a77</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/296</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8"></a>Term Name  bdqtest:c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:basisOfRecord Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_BASISOFRECORD_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_BASISOFRECORD_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:5aabe3d4-d2c0-415c-8972-c834b543971a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_241a279c-76d5-499b-ab49-a47ad7f8df50"></a>Term Name  bdqtest:241a279c-76d5-499b-ab49-a47ad7f8df50</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:basisOfRecord Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/241a279c-76d5-499b-ab49-a47ad7f8df50</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/241a279c-76d5-499b-ab49-a47ad7f8df50-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_BASISOFRECORD_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_BASISOFRECORD_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f094b94f-09b6-4fb0-8ba4-24252a2101c4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_BASISOFRECORD_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a2be4734-0a93-46dc-af4a-e2125b47dbd4"></a>Term Name  bdqtest:a2be4734-0a93-46dc-af4a-e2125b47dbd4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Classification Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a2be4734-0a93-46dc-af4a-e2125b47dbd4</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a2be4734-0a93-46dc-af4a-e2125b47dbd4-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_CLASSIFICATION_CONSISTENT in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_CLASSIFICATION_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:21d0b5f6-5b3e-4810-8413-c975b7cf343a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Consistency Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_21541436-641d-45a9-938c-537484d94eb7"></a>Term Name  bdqtest:21541436-641d-45a9-938c-537484d94eb7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:class Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/21541436-641d-45a9-938c-537484d94eb7</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/21541436-641d-45a9-938c-537484d94eb7-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_CLASS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_CLASS_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a2b39526-d08a-4a91-8b6d-aacf73677789</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_CLASS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_86c28d5e-f778-4230-88d8-64cc01478601"></a>Term Name  bdqtest:86c28d5e-f778-4230-88d8-64cc01478601</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/86c28d5e-f778-4230-88d8-64cc01478601</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/86c28d5e-f778-4230-88d8-64cc01478601-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4343a7e0-7f0b-434d-99d4-e939ecb16e1f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency ISO/DCMI STANDARD Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7a8b0af3-fa7d-416a-921a-8992d56f8233"></a>Term Name  bdqtest:7a8b0af3-fa7d-416a-921a-8992d56f8233</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates dwc:stateProvince Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7a8b0af3-fa7d-416a-921a-8992d56f8233</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7a8b0af3-fa7d-416a-921a-8992d56f8233-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4dd617df-a984-419f-b7b5-098b2023c4ab</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_478dee00-98d0-4154-b66c-eca64dbbf86d"></a>Term Name  bdqtest:478dee00-98d0-4154-b66c-eca64dbbf86d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates Terrestrial Marine</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/478dee00-98d0-4154-b66c-eca64dbbf86d</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/478dee00-98d0-4154-b66c-eca64dbbf86d-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:45cb9e13-7944-4535-a5ef-f6ededb77305</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_151b2d29-3460-4ba5-a226-86971dc8ad03"></a>Term Name  bdqtest:151b2d29-3460-4ba5-a226-86971dc8ad03</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Coordinates Not Zero</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/151b2d29-3460-4ba5-a226-86971dc8ad03</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/151b2d29-3460-4ba5-a226-86971dc8ad03-2023-06-20</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATES_NOTZERO in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COORDINATES_NOTZERO in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b482148e-9ac2-47ad-99b5-462508e9f360</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATES_NOTZERO.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Likeliness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d94b0130-7a13-4fa8-955c-eff5c47bd9de"></a>Term Name  bdqtest:d94b0130-7a13-4fa8-955c-eff5c47bd9de</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:coordinateUncertaintyInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d94b0130-7a13-4fa8-955c-eff5c47bd9de</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d94b0130-7a13-4fa8-955c-eff5c47bd9de-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COORDINATEUNCERTAINTY_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f8dfc3fc-6580-4518-b2b4-595c29e9042e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_942f63bd-d19d-4214-bf8e-cec0055b8909"></a>Term Name  bdqtest:942f63bd-d19d-4214-bf8e-cec0055b8909</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:countryCode Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/942f63bd-d19d-4214-bf8e-cec0055b8909</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/942f63bd-d19d-4214-bf8e-cec0055b8909-2024-11-10</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYCODE_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COUNTRYCODE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d153d4bd-b39d-43b0-b00a-395ff3e2ca62</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_fedf27b2-e01d-459f-98fc-7f0f39e3d4be"></a>Term Name  bdqtest:fedf27b2-e01d-459f-98fc-7f0f39e3d4be</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/fedf27b2-e01d-459f-98fc-7f0f39e3d4be</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/fedf27b2-e01d-459f-98fc-7f0f39e3d4be-2024-09-19</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYCODE_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COUNTRYCODE_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCODE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_57b40d9a-67d7-4916-9c27-dbb395c6c27e"></a>Term Name  bdqtest:57b40d9a-67d7-4916-9c27-dbb395c6c27e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/57b40d9a-67d7-4916-9c27-dbb395c6c27e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/57b40d9a-67d7-4916-9c27-dbb395c6c27e-2024-09-25</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:6f1093a0-0da5-4691-a95e-184d6d55eeb0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_23aced89-d613-479c-bc4c-837d74b73be0"></a>Term Name  bdqtest:23aced89-d613-479c-bc4c-837d74b73be0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country dwc:stateProvince Unambiguous</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/23aced89-d613-479c-bc4c-837d74b73be0</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/23aced89-d613-479c-bc4c-837d74b73be0-2024-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e5efdd20-d1fc-4287-91f9-15b9ce3f3aac</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_388e74b3-2e18-4d78-8112-3142d1177e25"></a>Term Name  bdqtest:388e74b3-2e18-4d78-8112-3142d1177e25</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/388e74b3-2e18-4d78-8112-3142d1177e25</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/388e74b3-2e18-4d78-8112-3142d1177e25-2024-08-19</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRY_FOUND in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COUNTRY_FOUND in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_9c8df974-8fba-4537-8c67-31466787f732"></a>Term Name  bdqtest:9c8df974-8fba-4537-8c67-31466787f732</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:country Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/9c8df974-8fba-4537-8c67-31466787f732</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/9c8df974-8fba-4537-8c67-31466787f732-2024-09-27</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_COUNTRY_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_COUNTRY_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:34ef6ea2-de06-4d2c-88fe-2c779de8f7db</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_COUNTRY_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6354376c-0cf2-435b-be40-850769c5a18a"></a>Term Name  bdqtest:6354376c-0cf2-435b-be40-850769c5a18a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:dateIdentified In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6354376c-0cf2-435b-be40-850769c5a18a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6354376c-0cf2-435b-be40-850769c5a18a-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DATEIDENTIFIED_INRANGE in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DATEIDENTIFIED_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a25786df-a624-4ff2-8962-6b23e8b07b0b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Likeliness ISO/DCMI STANDARD Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_563872eb-f544-45a0-8f91-8098d62768d4"></a>Term Name  bdqtest:563872eb-f544-45a0-8f91-8098d62768d4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/563872eb-f544-45a0-8f91-8098d62768d4</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/563872eb-f544-45a0-8f91-8098d62768d4-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DATEIDENTIFIED_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DATEIDENTIFIED_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:89f8b2ea-fc35-4941-929a-0e32cfbeb1a6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_85dc5d02-9847-420f-a026-6a0e70962d2a"></a>Term Name  bdqtest:85dc5d02-9847-420f-a026-6a0e70962d2a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:day In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/85dc5d02-9847-420f-a026-6a0e70962d2a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/85dc5d02-9847-420f-a026-6a0e70962d2a-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DAY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DAY_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2563ae15-a5bf-48fc-91f3-6df869aece2d</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DAY_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_371035f6-42b5-494f-86d9-de2f44a6cdc6"></a>Term Name  bdqtest:371035f6-42b5-494f-86d9-de2f44a6cdc6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:day Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/371035f6-42b5-494f-86d9-de2f44a6cdc6</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/371035f6-42b5-494f-86d9-de2f44a6cdc6-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DAY_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c0fce1a1-8879-4175-8a71-ce037655c358</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4d999a65-a431-4a76-b591-e0d86dcf244b"></a>Term Name  bdqtest:4d999a65-a431-4a76-b591-e0d86dcf244b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dc:type Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4d999a65-a431-4a76-b591-e0d86dcf244b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4d999a65-a431-4a76-b591-e0d86dcf244b-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DCTYPE_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DCTYPE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e1286c46-2a95-480d-89e4-f02681372eb7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d9493fa0-d90e-41db-95f6-d1c1d243540e"></a>Term Name  bdqtest:d9493fa0-d90e-41db-95f6-d1c1d243540e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dc:type Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d9493fa0-d90e-41db-95f6-d1c1d243540e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d9493fa0-d90e-41db-95f6-d1c1d243540e-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DCTYPE_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DCTYPE_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b85129f0-28c2-4ede-aff2-5ce3791c6e86</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DCTYPE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3c8bc478-f6b2-4533-b7ce-45bae5d186c2"></a>Term Name  bdqtest:3c8bc478-f6b2-4533-b7ce-45bae5d186c2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLatitude In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3c8bc478-f6b2-4533-b7ce-45bae5d186c2</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3c8bc478-f6b2-4533-b7ce-45bae5d186c2-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLATITUDE_INRANGE in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DECIMALLATITUDE_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a5111c0c-d198-4ecc-af10-809ae2b3ae01</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a2535b23-4407-40bd-b23b-30c8185d72a2"></a>Term Name  bdqtest:a2535b23-4407-40bd-b23b-30c8185d72a2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLatitude Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a2535b23-4407-40bd-b23b-30c8185d72a2</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a2535b23-4407-40bd-b23b-30c8185d72a2-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DECIMALLATITUDE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:0067fa60-5503-490e-8c94-93fb79cc7da2</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6f7a9b82-7d34-4111-a2a6-9efe5221fa44"></a>Term Name  bdqtest:6f7a9b82-7d34-4111-a2a6-9efe5221fa44</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLongitude In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6f7a9b82-7d34-4111-a2a6-9efe5221fa44</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6f7a9b82-7d34-4111-a2a6-9efe5221fa44-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLONGITUDE_INRANGE in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DECIMALLONGITUDE_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1a504f7f-21a7-49e1-a0dc-f51146957fa4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a94e986e-dbc8-4147-872d-5f2727945654"></a>Term Name  bdqtest:a94e986e-dbc8-4147-872d-5f2727945654</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLongitude Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a94e986e-dbc8-4147-872d-5f2727945654</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a94e986e-dbc8-4147-872d-5f2727945654-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DECIMALLONGITUDE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c893ee17-ee8b-43ec-bf17-97ac814ea502</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_ba953672-6526-4375-97e8-b4e9d1a7d3a0"></a>Term Name  bdqtest:ba953672-6526-4375-97e8-b4e9d1a7d3a0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:degreeofEstablishment Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/ba953672-6526-4375-97e8-b4e9d1a7d3a0</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/ba953672-6526-4375-97e8-b4e9d1a7d3a0-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fec2103b-5d46-4723-b2ec-8c8119b44aaf</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c04d428a-13d0-4766-9df7-4dfb2ef5d5d8"></a>Term Name  bdqtest:c04d428a-13d0-4766-9df7-4dfb2ef5d5d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:endDayOfYear In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c04d428a-13d0-4766-9df7-4dfb2ef5d5d8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c04d428a-13d0-4766-9df7-4dfb2ef5d5d8-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_ENDDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_ENDDAYOFYEAR_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:62f754b5-a0a1-4b24-9982-b76e4e169f71</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_8dfed701-01a9-415d-a9f8-539280b75975"></a>Term Name  bdqtest:8dfed701-01a9-415d-a9f8-539280b75975</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:establishmentMeans Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/8dfed701-01a9-415d-a9f8-539280b75975</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/8dfed701-01a9-415d-a9f8-539280b75975-2024-02-08</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_ESTABLISHMENTMEANS_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f1d3bf9c-5558-41dc-8e33-b17c499be016</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d41a731b-2e2b-4442-9217-4c375ae92926"></a>Term Name  bdqtest:d41a731b-2e2b-4442-9217-4c375ae92926</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d41a731b-2e2b-4442-9217-4c375ae92926</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d41a731b-2e2b-4442-9217-4c375ae92926-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTDATE_INRANGE in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_EVENTDATE_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:29a1fdc6-326b-4017-880d-d11ff0225b8f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365"></a>Term Name  bdqtest:c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTDATE_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_EVENTDATE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1fae3f77-7fcb-42c6-ab43-1ff28adf4fa4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_14a1d51f-16ed-4148-9dc8-1e90157a9868"></a>Term Name  bdqtest:14a1d51f-16ed-4148-9dc8-1e90157a9868</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/14a1d51f-16ed-4148-9dc8-1e90157a9868</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/14a1d51f-16ed-4148-9dc8-1e90157a9868-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTDATE_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_EVENTDATE_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:80c8f69b-4ad3-40ee-bccd-de016bfae367</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTDATE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f22539ef-029b-4edb-ad17-add4363f7395"></a>Term Name  bdqtest:f22539ef-029b-4edb-ad17-add4363f7395</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Event Temporal Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f22539ef-029b-4edb-ad17-add4363f7395</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f22539ef-029b-4edb-ad17-add4363f7395-2023-09-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_EVENTTEMPORAL_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b57460c4-16e1-4c1d-8a07-a53aee9e8922</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f375a3fd-4cf5-4ef4-955e-d71762ede2d8"></a>Term Name  bdqtest:f375a3fd-4cf5-4ef4-955e-d71762ede2d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Event Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f375a3fd-4cf5-4ef4-955e-d71762ede2d8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f375a3fd-4cf5-4ef4-955e-d71762ede2d8-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_EVENT_CONSISTENT in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_EVENT_CONSISTENT in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:83d057ea-a6f6-49e6-ac3c-0c418776a0e0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_EVENT_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Consistency CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a07d7147-2db8-48ce-81b8-e47595ad5f17"></a>Term Name  bdqtest:a07d7147-2db8-48ce-81b8-e47595ad5f17</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:family Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a07d7147-2db8-48ce-81b8-e47595ad5f17</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a07d7147-2db8-48ce-81b8-e47595ad5f17-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_FAMILY_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_FAMILY_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:16f999d9-1cf5-4208-b2ca-1a93d6700085</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_FAMILY_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c5c8db83-3af0-4215-806f-e2f90574b138"></a>Term Name  bdqtest:c5c8db83-3af0-4215-806f-e2f90574b138</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:genus Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c5c8db83-3af0-4215-806f-e2f90574b138</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c5c8db83-3af0-4215-806f-e2f90574b138-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_GENUS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_GENUS_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:15bbda19-dd18-471a-a5c3-56c7e543012f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_GENUS_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_488c1dff-21ec-4e68-a00a-7355505e180c"></a>Term Name  bdqtest:488c1dff-21ec-4e68-a00a-7355505e180c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:geodeticDatum Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/488c1dff-21ec-4e68-a00a-7355505e180c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/488c1dff-21ec-4e68-a00a-7355505e180c-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_GEODETICDATUM_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_GEODETICDATUM_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a3c8b277-15fb-4ae8-afb1-e64fb6eb5241</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e"></a>Term Name  bdqtest:cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Vaildation dwc:geodeticDatum Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e-2025-03-03</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_GEODETICDATUM_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_GEODETICDATUM_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:5cc05662-c029-4ba9-b32e-fb487ccba71c</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_GEODETICDATUM_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_465d7ac1-d193-46c0-a302-56a9ef99215f"></a>Term Name  bdqtest:465d7ac1-d193-46c0-a302-56a9ef99215f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:kingdom Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/465d7ac1-d193-46c0-a302-56a9ef99215f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/465d7ac1-d193-46c0-a302-56a9ef99215f-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_KINGDOM_FOUND in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_KINGDOM_FOUND in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a90e100a-3522-4742-aa73-3b98a35ab826</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3bc9df8b-0f57-4157-9374-b56a99090b22"></a>Term Name  bdqtest:3bc9df8b-0f57-4157-9374-b56a99090b22</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:kingdom Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3bc9df8b-0f57-4157-9374-b56a99090b22</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3bc9df8b-0f57-4157-9374-b56a99090b22-2024-01-28</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_KINGDOM_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_KINGDOM_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e6f0a9ce-3e72-40fb-9fad-63cf5962f93e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_KINGDOM_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4fccf163-9336-4f48-996c-57f5f66e72db"></a>Term Name  bdqtest:4fccf163-9336-4f48-996c-57f5f66e72db</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dcterms:license Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4fccf163-9336-4f48-996c-57f5f66e72db</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4fccf163-9336-4f48-996c-57f5f66e72db-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_LICENSE_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_LICENSE_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d8b450af-47e6-4f5c-8154-6d6acbe9efa5</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_acd8d43e-7a2a-4372-b887-fb53a9972dc9"></a>Term Name  bdqtest:acd8d43e-7a2a-4372-b887-fb53a9972dc9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dcterms:license Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/acd8d43e-7a2a-4372-b887-fb53a9972dc9</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/acd8d43e-7a2a-4372-b887-fb53a9972dc9-2024-03-21</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_LICENSE_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_LICENSE_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2a9dbd16-d427-471e-8db5-c1de2b2cf030</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_LICENSE_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3b2e4791-1a5a-4087-9e8d-09c67cf8c816"></a>Term Name  bdqtest:3b2e4791-1a5a-4087-9e8d-09c67cf8c816</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dcterms:Location Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3b2e4791-1a5a-4087-9e8d-09c67cf8c816</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3b2e4791-1a5a-4087-9e8d-09c67cf8c816-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_LOCATION_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_LOCATION_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:30ed5e2d-ef30-4988-8dbb-12c119e94ac3</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_LOCATION_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c73d49d1-06e4-4272-8249-6a26e7f8abca"></a>Term Name  bdqtest:c73d49d1-06e4-4272-8249-6a26e7f8abca</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:maximumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c73d49d1-06e4-4272-8249-6a26e7f8abca</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c73d49d1-06e4-4272-8249-6a26e7f8abca-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MAXDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_MAXDEPTH_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:cebc8ba0-ca02-4f1e-830e-ec693bc628e4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MAXDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7c5a6ba0-399d-4570-878a-4a064e2406fe"></a>Term Name  bdqtest:7c5a6ba0-399d-4570-878a-4a064e2406fe</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:maximumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7c5a6ba0-399d-4570-878a-4a064e2406fe</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7c5a6ba0-399d-4570-878a-4a064e2406fe-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MAXELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_MAXELEVATION_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f9471802-a5f7-4f4e-9810-f3f4f43dad1a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MAXELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Likeliness Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_49d756a8-e654-4267-a290-d1def5d2c5f9"></a>Term Name  bdqtest:49d756a8-e654-4267-a290-d1def5d2c5f9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/49d756a8-e654-4267-a290-d1def5d2c5f9</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/49d756a8-e654-4267-a290-d1def5d2c5f9-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_MINDEPTH_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_fcabd2c9-392c-4841-a5d7-e2680c9587ab"></a>Term Name  bdqtest:fcabd2c9-392c-4841-a5d7-e2680c9587ab</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumDepthInMeters less than dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/fcabd2c9-392c-4841-a5d7-e2680c9587ab</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/fcabd2c9-392c-4841-a5d7-e2680c9587ab-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:12f7f82e-ab1c-4690-92b8-ecc9328256c1</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_1ba18c8b-66a6-47d9-a709-404439332dba"></a>Term Name  bdqtest:1ba18c8b-66a6-47d9-a709-404439332dba</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/1ba18c8b-66a6-47d9-a709-404439332dba</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/1ba18c8b-66a6-47d9-a709-404439332dba-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_MINELEVATION_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2bb79221-0312-410a-aef6-f569485df6a6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_44f00697-ca66-43cf-8f16-646b40c0f514"></a>Term Name  bdqtest:44f00697-ca66-43cf-8f16-646b40c0f514</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumElevationInMeters less than dwcmaximumElevationInMeters</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/44f00697-ca66-43cf-8f16-646b40c0f514</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/44f00697-ca66-43cf-8f16-646b40c0f514-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f799fb5c-37e4-46d7-a07e-87eb071df9c6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b3c2bb86-e239-4532-ae0c-b121ec1ee025"></a>Term Name  bdqtest:b3c2bb86-e239-4532-ae0c-b121ec1ee025</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:month Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b3c2bb86-e239-4532-ae0c-b121ec1ee025</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b3c2bb86-e239-4532-ae0c-b121ec1ee025-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_MONTH_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_MONTH_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2c5dbdbb-feab-474c-bcca-bf6d1b90ae66</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_MONTH_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_16059801-6adb-4e65-82f4-61eaa70d8df0"></a>Term Name  bdqtest:16059801-6adb-4e65-82f4-61eaa70d8df0</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:namePublishedInYear Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/16059801-6adb-4e65-82f4-61eaa70d8df0</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/16059801-6adb-4e65-82f4-61eaa70d8df0-2024-02-07</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f09fc9ad-a449-4422-b32f-63d8ccf2501f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0028ef9a-6553-467b-a344-90327ed2babf"></a>Term Name  bdqtest:0028ef9a-6553-467b-a344-90327ed2babf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceID Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0028ef9a-6553-467b-a344-90327ed2babf</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0028ef9a-6553-467b-a344-90327ed2babf-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_OCCURRENCEID_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_OCCURRENCEID_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3d9e1339-19d7-47e7-af9e-11905df82b6a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d2922585-2070-4851-a033-15e51977f9dc"></a>Term Name  bdqtest:d2922585-2070-4851-a033-15e51977f9dc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceStatus Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d2922585-2070-4851-a033-15e51977f9dc</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d2922585-2070-4851-a033-15e51977f9dc-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_OCCURRENCESTATUS_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c3a53898-c4ad-40e0-961b-b4ceafea37c7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_2fea4571-92d0-48a5-a5ba-6caecd647862"></a>Term Name  bdqtest:2fea4571-92d0-48a5-a5ba-6caecd647862</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceStatus Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/2fea4571-92d0-48a5-a5ba-6caecd647862</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/2fea4571-92d0-48a5-a5ba-6caecd647862-2025-02-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_OCCURRENCESTATUS_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_OCCURRENCESTATUS_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fbe854d4-acf3-4c79-a654-81441fed644f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_773bb288-fef3-4968-a65a-a69c74d6ecb5"></a>Term Name  bdqtest:773bb288-fef3-4968-a65a-a69c74d6ecb5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:order Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/773bb288-fef3-4968-a65a-a69c74d6ecb5</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/773bb288-fef3-4968-a65a-a69c74d6ecb5-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_ORDER_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_ORDER_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:ae08b4b4-89ba-4972-b51f-912b132bd006</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_ORDER_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_ef31ba02-cea7-4d76-990f-99ebbd201fb4"></a>Term Name  bdqtest:ef31ba02-cea7-4d76-990f-99ebbd201fb4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:pathway Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/ef31ba02-cea7-4d76-990f-99ebbd201fb4</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/ef31ba02-cea7-4d76-990f-99ebbd201fb4-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_PATHWAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_PATHWAY_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c7c92ef0-284e-4c5d-8fc9-f1480bfe0b8e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_PATHWAY_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_17364d16-37b7-4ccb-9614-bfb95ff1bca9"></a>Term Name  bdqtest:17364d16-37b7-4ccb-9614-bfb95ff1bca9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:phylum Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/17364d16-37b7-4ccb-9614-bfb95ff1bca9</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/17364d16-37b7-4ccb-9614-bfb95ff1bca9-2022-03-25</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_PHYLUM_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_PHYLUM_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1193230f-f188-4917-92da-bba3390ed3fa</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_PHYLUM_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_ef05b45b-13b8-4877-9e9d-fa44b332d83c"></a>Term Name  bdqtest:ef05b45b-13b8-4877-9e9d-fa44b332d83c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation Polynomial Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/ef05b45b-13b8-4877-9e9d-fa44b332d83c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/ef05b45b-13b8-4877-9e9d-fa44b332d83c-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_POLYNOMIAL_CONSISTENT in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_POLYNOMIAL_CONSISTENT in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d92c5e23-bf6a-483b-86c3-9374e12d01c7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Consistency CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7"></a>Term Name  bdqtest:6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameAuthorship Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7-2024-02-04</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e9ffc3b0-0fb8-4a7c-a588-a00085ba980b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a9529e71-5470-4cb1-b04d-aa483926f532"></a>Term Name  bdqtest:a9529e71-5470-4cb1-b04d-aa483926f532</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameID Complete</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a9529e71-5470-4cb1-b04d-aa483926f532</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a9529e71-5470-4cb1-b04d-aa483926f532-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAMEID_COMPLETE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e6c02558-8541-4292-9a11-2f4408d69699</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4cf84216-c8a7-4865-a8e1-3ffd829d5a10"></a>Term Name  bdqtest:4cf84216-c8a7-4865-a8e1-3ffd829d5a10</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameID Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4cf84216-c8a7-4865-a8e1-3ffd829d5a10</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4cf84216-c8a7-4865-a8e1-3ffd829d5a10-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:02242018-3e73-4e0a-8d6f-d1db06cf81a3</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a8aee02c-cf7c-4104-a601-d8afc4f9cbe2"></a>Term Name  bdqtest:a8aee02c-cf7c-4104-a601-d8afc4f9cbe2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificName Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a8aee02c-cf7c-4104-a601-d8afc4f9cbe2</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a8aee02c-cf7c-4104-a601-d8afc4f9cbe2-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAME_FOUND in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAME_FOUND in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3c2fe7e9-186f-4ceb-8274-8bbcb4a62de4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b4d6a61c-64ff-4da0-974c-63a73fd20836"></a>Term Name  bdqtest:b4d6a61c-64ff-4da0-974c-63a73fd20836</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificName Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b4d6a61c-64ff-4da0-974c-63a73fd20836</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b4d6a61c-64ff-4da0-974c-63a73fd20836-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_SCIENTIFICNAME_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a9c18563-f63e-42db-98e5-a3e6079086b7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_1b3bbac4-7c00-46d6-8179-1d57c92374ad"></a>Term Name  bdqtest:1b3bbac4-7c00-46d6-8179-1d57c92374ad</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:sex Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/1b3bbac4-7c00-46d6-8179-1d57c92374ad</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/1b3bbac4-7c00-46d6-8179-1d57c92374ad-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_SEX_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_SEX_STANDARD in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:72471db4-226c-454f-bbe8-5c1718e6c834</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_SEX_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_8c217eee-9cd0-48c3-aea0-90151c6c5bfd"></a>Term Name  bdqtest:8c217eee-9cd0-48c3-aea0-90151c6c5bfd</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:startDayOfYear In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/8c217eee-9cd0-48c3-aea0-90151c6c5bfd</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/8c217eee-9cd0-48c3-aea0-90151c6c5bfd-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_STARTDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_STARTDAYOFYEAR_INRANGE in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:53c6af68-6120-4da6-87d8-a3e9551b9671</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_9c1cdf6a-0dbf-4828-a2e3-fb368f74d194"></a>Term Name  bdqtest:9c1cdf6a-0dbf-4828-a2e3-fb368f74d194</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:stateProvince Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/9c1cdf6a-0dbf-4828-a2e3-fb368f74d194</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/9c1cdf6a-0dbf-4828-a2e3-fb368f74d194-2024-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_STATEPROVINCE_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_STATEPROVINCE_FOUND in the MultiRecord has Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET, otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d261fac1-ce61-4879-bc04-870fa885b578</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_STATEPROVINCE_FOUND.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/297</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_e0b8cff1-3322-40d2-b8b2-b99fc9ae130a"></a>Term Name  bdqtest:e0b8cff1-3322-40d2-b8b2-b99fc9ae130a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:taxonRank Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/e0b8cff1-3322-40d2-b8b2-b99fc9ae130a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/e0b8cff1-3322-40d2-b8b2-b99fc9ae130a-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXONRANK_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_TAXONRANK_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c619ec9b-92ec-4047-a8d3-931e3324bf3e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f320ca83-8487-4011-b1ff-f4b1b4dd86ec"></a>Term Name  bdqtest:f320ca83-8487-4011-b1ff-f4b1b4dd86ec</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:taxonRank Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f320ca83-8487-4011-b1ff-f4b1b4dd86ec</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f320ca83-8487-4011-b1ff-f4b1b4dd86ec-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXONRANK_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_TAXONRANK_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c8964200-630e-47c6-baad-7e334fddbbdb</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXONRANK_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_2a9d4cfd-815a-46e0-bb51-60724582b762"></a>Term Name  bdqtest:2a9d4cfd-815a-46e0-bb51-60724582b762</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Taxon Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/2a9d4cfd-815a-46e0-bb51-60724582b762</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/2a9d4cfd-815a-46e0-bb51-60724582b762-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXON_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_TAXON_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f38e3644-354d-4180-bc7c-c437cef1d606</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0df03601-3768-4805-906a-bbd0a41b0fda"></a>Term Name  bdqtest:0df03601-3768-4805-906a-bbd0a41b0fda</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:Taxon Unambiguous</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0df03601-3768-4805-906a-bbd0a41b0fda</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0df03601-3768-4805-906a-bbd0a41b0fda-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TAXON_UNAMBIGUOUS in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_TAXON_UNAMBIGUOUS in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:8bd6f6de-49e4-4889-82e0-e4af093981e0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88"></a>Term Name  bdqtest:1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:typeStatus Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88-2024-11-11</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_TYPESTATUS_STANDARD in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_TYPESTATUS_STANDARD in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e4dbf38d-bdd7-4cf7-8c60-5b3bfc6af4ff</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_TYPESTATUS_STANDARD.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a0502c5f-608b-4e59-99da-d9490bb4d93b"></a>Term Name  bdqtest:a0502c5f-608b-4e59-99da-d9490bb4d93b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:year In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a0502c5f-608b-4e59-99da-d9490bb4d93b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a0502c5f-608b-4e59-99da-d9490bb4d93b-2024-08-23</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_YEAR_INRANGE in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_YEAR_INRANGE in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:aee43366-0352-448a-a5ea-85ddc8605da1</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_INRANGE.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance Parameterized CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_a8fef8a8-e7c7-4a2d-adaf-7da99c896c93"></a>Term Name  bdqtest:a8fef8a8-e7c7-4a2d-adaf-7da99c896c93</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Measurement over MultiRecord for QualityAssurance of Validation dwc:year Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/a8fef8a8-e7c7-4a2d-adaf-7da99c896c93</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/a8fef8a8-e7c7-4a2d-adaf-7da99c896c93-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Measure if all VALIDATION_YEAR_NOTEMPTY in a record set are COMPLIANT.</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLETE if every VALIDATION_YEAR_NOTEMPTY in the MultiRecord has Response.result=COMPLIANT; otherwise NOT_COMPLETE.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:42f331f4-a5a8-48b4-a08e-57048d1d1a77</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>bdq:VALIDATION_YEAR_NOTEMPTY.Response</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For Quality Assurance, filter record set until this measure is COMPLETE.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Measure</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>MultiRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/295</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_ac2b7648-d5f9-48ca-9b07-8ad5879a2536"></a>Term Name  bdqtest:ac2b7648-d5f9-48ca-9b07-8ad5879a2536</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:basisOfRecord Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/ac2b7648-d5f9-48ca-9b07-8ad5879a2536</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/ac2b7648-d5f9-48ca-9b07-8ad5879a2536-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:basisOfRecord?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:basisOfRecord is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:5aabe3d4-d2c0-415c-8972-c834b543971a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:basisOfRecord</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:basisOfRecord="PreservedSpecimen": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:basisOfRecord is bdq:NotEmpty"],[dwc:basisOfRecord="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:basisOfRecord is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L207</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/58</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_BASISOFRECORD_NOTEMPTY with Specification for: VALIDATION_BASISOFRECORD_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_BASISOFRECORD_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_42408a00-bf71-4892-a399-4325e2bc1fb8"></a>Term Name  bdqtest:42408a00-bf71-4892-a399-4325e2bc1fb8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:basisOfRecord Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/42408a00-bf71-4892-a399-4325e2bc1fb8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/42408a00-bf71-4892-a399-4325e2bc1fb8-2024-08-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:basisOfRecord occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; COMPLIANT if the value of dwc:basisOfRecord is valid in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f094b94f-09b6-4fb0-8ba4-24252a2101c4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:basisOfRecord</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]}{dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The term dwc:basisOfRecord has the comment "Recommended best practice is to use a controlled vocabulary such as the set of local names of the identifiers for classes in Darwin Core." The list of these values can be determined by searching https://github.com/tdwg/dwc/blob/master/vocabulary/term_versions.csv for rows with status="recommended" and rdf_type="http://www.w3.org/2000/01/rdf-schema#Class". For Tests against a dwc:Occurrence record, the set of valid terms is more limited and embodied in the resource found at https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:basisOfRecord="Taxon": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:basisOfRecord matches a standard label of one of the Darwin Core classes"],[dwc:basisOfRecord="Specimen": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:basisOfRecord does not exactly match a standard label of one of the Darwin Core classes"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L342</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/104</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>a723528a-ee73-44a7-818d-5315323ec4e9</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_BASISOFRECORD_STANDARD with Specification for: VALIDATION_BASISOFRECORD_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_BASISOFRECORD_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_2750c040-1d4a-4149-99fe-0512785f2d5f"></a>Term Name  bdqtest:2750c040-1d4a-4149-99fe-0512785f2d5f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation Classification Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/2750c040-1d4a-4149-99fe-0512785f2d5f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/2750c040-1d4a-4149-99fe-0512785f2d5f-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the combination of higher classification taxonomic terms consistent using bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of the fields dwc:kingdom dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus are bdq:Empty; COMPLIANT if the combination of values of higher classification taxonomic terms (dwc:kingdom, dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus) are consistent with the lowest ranking matched element in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:21d0b5f6-5b3e-4810-8413-c975b7cf343a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>A fail condition may arise either from the taxon terms being internally inconsistent (not all of the information can be true at the same time), or from the vocabulary being incapable of resolving the combination of classification values. Additional Tests could be devised against a taxonomic authority to report the distinct failure conditions. This Test specifically does not consider the content of dwc:higherClassification.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="Myrtales", dwc:superfamily="", dwc:family="Myrtaceae", dwc:subfamily="", dwc:tribe="", dwc:subtribe="",dwc:genus="Punica": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="The combination of values of higher classification taxonomic terms can be unambiguously resolved in the bdq:sourceAuthority"],[dwc:kingdom="", dwc:phylum="Chordata", dwc:class="", dwc:order="Rhopalocera", dwc:superfamly="", dwc:family="Muricidae", dwc:subfamily="", dwc:tribe="", dwc:subtribe="", dwc:genus="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="The combination of values of higher classification taxonomic terms cannot be unambiguously resolved in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L2563</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/123</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Consistency Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>d6bc8db2-014b-47dc-9737-b0ecd98bf5bb</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_CLASSIFICATION_CONSISTENT with Specification for: VALIDATION_CLASSIFICATION_CONSISTENT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_CLASSIFICATION_CONSISTENT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_2cd6884e-3d14-4476-94f7-1191cfff309b"></a>Term Name  bdqtest:2cd6884e-3d14-4476-94f7-1191cfff309b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:class Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/2cd6884e-3d14-4476-94f7-1191cfff309b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/2cd6884e-3d14-4476-94f7-1191cfff309b-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:class occur at the rank of Class in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:class is bdq:Empty; COMPLIANT if the value of dwc:class is found as a value at the rank of Class in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a2b39526-d08a-4a91-8b6d-aacf73677789</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:class</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:class="Insecta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:class has an equivalent at the rank of Class in the bdq:sourceAuthority"],[dwc:class="Magnoleopsida": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT,Response.comment="dwc:class does not have an equivalent at the rank of Class in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1345</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/77</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>cd12d17c-8404-40fa-bc15-5583564ddd14</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_CLASS_FOUND with Specification for: VALIDATION_CLASS_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_CLASS_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_adb27d29-9f0d-4d52-b760-a77ba57a69c9"></a>Term Name  bdqtest:adb27d29-9f0d-4d52-b760-a77ba57a69c9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation Coordinates dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/adb27d29-9f0d-4d52-b760-a77ba57a69c9</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/adb27d29-9f0d-4d52-b760-a77ba57a69c9-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Do the geographic coordinates fall on or within the boundaries of the territory given in dwc:countryCode or its Exclusive Economic Zone?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if one or more of dwc:decimalLatitude, dwc:decimalLongitude, or dwc:countryCode are bdq:Empty or invalid; COMPLIANT if the geographic coordinates fall on or within the boundary defined by the union of the boundary of the country from dwc:countryCode plus it's Exclusive Economic Zone as found in the bdq:sourceAuthority, if any, plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4343a7e0-7f0b-434d-99d4-e939ecb16e1f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:countryCode,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority,bdq:spatialBufferInMeters</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>dwc:coordinatePrecision and dwc:coordinateUncertaintyInMeters (if present) imply a potential displacement of the provided coordinates. These two terms can be considered spatial buffers. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is justified. When dwc:countryCode=XZ (for High Seas), the coordinate should fall into a marine region out side of the EEZ of any country. Taking the spatial buffers into account does however greatly complicate both the logic and the implementation of such Tests. The same applies to potential conversion of the Spatial Reference System (SRS) of dwc:decimalLatitude and dwc:decimalLongitude to the SRS used in the bdq:sourceAuthority.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="AR", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Coordinates match dwc:countryCode"],[dwc:countryCode="CL", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Coordinates are in Argentina, not Chile"],[dwc:countryCode="ZX", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.comment="Input field contains invalid values - ZX is not a valid ISO 3166-1-alpha-2 country code"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1005</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, iDigBio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/50</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency ISO/DCMI STANDARD Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>8a3f5702-a4e5-4b21-acb6-a4eae9a1ae09,972320cd-3ba3-4076-a8eb-f797095509cd</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT with Specification for: VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f18a470b-3fe1-4aae-9c65-a6d3db6b550c"></a>Term Name  bdqtest:f18a470b-3fe1-4aae-9c65-a6d3db6b550c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation Coordinates dwc:stateProvince Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f18a470b-3fe1-4aae-9c65-a6d3db6b550c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f18a470b-3fe1-4aae-9c65-a6d3db6b550c-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Do the geographic coordinates fall on or within the boundary from the bdq:sourceAuthority for the given dwc:stateProvince or within the distance given by bdq:spatialBufferInMeters outside that boundary?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or invalid, or dwc:stateProvince is bdq:Empty or not found in the bdq:sourceAuthority; COMPLIANT if the geographic coordinates fall on or within the boundary in the bdq:sourceAuthority for the given dwc:stateProvince (after coordinate reference system transformations, if any, have been accounted for), or within the distance given by bdq:spatialBufferInMeters outside that boundary; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:4dd617df-a984-419f-b7b5-098b2023c4ab</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:stateProvince,dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority,bdq:spatialBufferInMeters</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "10m-admin-1 boundaries" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/]},bdq:spatialBufferInMeters default = "3000"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The geographic determination service is expected to return a list of names of first-level administrative divisions for geometries that the geographic point falls on or within, including a 3 km buffer around the administrative geometry. A match on any of those names should constitute a consistency, and dwc:countryCode should not be needed to make this determination, that is, this Test does not attempt to disambiguate potential duplicate first-level administrative division names. The level of buffering may be related to the scale of the underlying GIS layer being used. At a global scale, typical map scales used for borders and coastal areas are either 1:3M or 1:1M (Dooley 2005, Chapter 4). Horizontal accuracy at those scales is around 1.5-2.5km and 0.5-0.85 km respectively (Chapman & Wieczorek 2020).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:stateProvince="Tasmania", dwc:decimalLatitude="-42.85", dwc:decimalLongitude="146.75": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Input fields contain interpretable values"],[dwc:stateProvince="Córdoba", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Input fields contain interpretable values but coordinates don't match dwc:stateProvince with buffer"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1378</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/56</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>b7c56646-56f1-4094-b2be-8546c7e18102,cceaf335-6cd3-44a0-9562-6fe8e7743854</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT with Specification for: VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b9c184ce-a859-410c-9d12-71a338200380"></a>Term Name  bdqtest:b9c184ce-a859-410c-9d12-71a338200380</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation Coordinates Terrestrial Marine</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b9c184ce-a859-410c-9d12-71a338200380</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b9c184ce-a859-410c-9d12-71a338200380-2024-08-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the marine/non-marine biome of a taxon from the bdq:sourceAuthority match the biome at the location given by the coordinates?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if either bdq:taxonIsMarine or bdq:geospatialLand are not available; INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:scientificName is bdq:Empty or (2) the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or (3) if bdq:assumptionOnUnknownBiome is noassumption and the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine; COMPLIANT if (1) the taxon marine/nonmarine status from bdq:taxonIsMarine matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters or (2) if the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine and bdq:assumptionOnUnknownBiome matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:45cb9e13-7944-4535-a5ef-f6ededb77305</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:taxonIsMarine,bdq:geospatialLand,bdq:spatialBufferInMeters,bdq:assumptionOnUnknownBiome</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:taxonIsMarine default = "World Register of Marine Species (WoRMS)" {[https://www.marinespecies.org/]} {Web service [https://www.marinespecies.org/aphia.php?p=webservice]},bdq:geospatialLand default = "Union of NaturalEarth 10m-physical-vectors for Land and NaturalEarth Minor Islands" {[https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip], [https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_minor_islands.zip]},bdq:spatialBufferInMeters default = "3000",bdq:assumptionOnUnknownBiome default = "noassumption"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>dwc:coordinatePrecision and dwc:coordinateUncertaintyInMeters (if present) imply a potential displacement of the provided coordinates. These two terms can be considered spatial buffers. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is justified. Taking the spatial buffers into account does however greatly complicate both the logic and the implementation of such Tests. The same applies to potential conversion of the Spatial Reference System (SRS) of dwc:decimalLatitude and dwc:decimalLongitude to the SRS used in the bdq:sourceAuthority. Note that in the current implementation Tests treat "brackish" in WoRMS as both marine and terrestrial. Note that both bdq:taxonIsMarine and bdq:geospatialLand are bdq:sourceAuthorities, but as they form two parameters, distinct names are used for them.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521", dwc:scientificName="Aegla neuquensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="The species is freshwater aquatic and the coordinates fall in a lake and thus COMPLIANT"],[dwc:decimalLatitude="20.0", dwc:decimalLongitude="-30.0", dwc:scientificName="Viviparus contectus (Millet, 1813)": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is non-marine according to dwc:taxonIsMarine but coordinates are marine"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L3198</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, OBIS</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/51</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>3968f8d0-7364-4f3d-9993-96b8678f1653,cbb3483c-2bf7-4b42-9d74-71ddc0e41c5e,b3bf69d3-061c-4e2a-ac53-a73cb51ecbe2,e7012224-eb6d-4bb9-a4ef-2d40fd3b3471</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT with Specification for: VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_1bf0e210-6792-4128-b8cc-ab6828aa4871"></a>Term Name  bdqtest:1bf0e210-6792-4128-b8cc-ab6828aa4871</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation Coordinates Not Zero</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/1bf0e210-6792-4128-b8cc-ab6828aa4871</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/1bf0e210-6792-4128-b8cc-ab6828aa4871-2023-06-20</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are the values of either dwc:decimalLatitude or dwc:decimalLongitude numbers that are not equal to 0?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or is not interpretable as a number, or dwc:decimalLongitude is bdq:Empty or is not interpretable as a number; COMPLIANT if either the value of dwc:decimalLatitude is not = 0 or the value of dwc:decimalLongitude is not = 0; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b482148e-9ac2-47ad-99b5-462508e9f360</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLatitude,dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>A record with 0.0 is interpreted as the string "0".</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="21.0534", dwc:decimalLongitude="81.0554": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatitude and dwc:decimalLongitude are not zero"],[dwc:decimalLatitude="0", dwc:decimalLongitude="0",: Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatitude and dwc:decimalLongitude are zero"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Likely</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2193</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/87</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Likeliness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COORDINATES_NOTZERO with Specification for: VALIDATION_COORDINATES_NOTZERO</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATES_NOTZERO</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c6adf2ea-3051-4498-97f4-4b2f8a105f57"></a>Term Name  bdqtest:c6adf2ea-3051-4498-97f4-4b2f8a105f57</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:coordinateUncertaintyInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c6adf2ea-3051-4498-97f4-4b2f8a105f57</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c6adf2ea-3051-4498-97f4-4b2f8a105f57-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:coordinateUncertaintyInMeters a number between 1 and 20,037,509?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:coordinateUncertaintyInMeters is bdq:Empty; COMPLIANT if the value of dwc:coordinateUncertaintyInMeters is interpreted as a number between 1 and 20037509 inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f8dfc3fc-6580-4518-b2b4-595c29e9042e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:coordinateUncertaintyInMeters</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The upper limit is one half the equatorial circumference of the earth.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:coordinateUncertaintyInMeters="1": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:coordinateUncertaintyInMeters is in range"],[dwc:coordinateUncertaintyInMeters="-1": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:coordinateUncertaintyInMeters is out of range"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2562</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/109</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COORDINATEUNCERTAINTY_INRANGE with Specification for: VALIDATION_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COORDINATEUNCERTAINTY_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_853b79a2-b314-44a2-ae46-34a1e7ed85e4"></a>Term Name  bdqtest:853b79a2-b314-44a2-ae46-34a1e7ed85e4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:countryCode Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/853b79a2-b314-44a2-ae46-34a1e7ed85e4</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/853b79a2-b314-44a2-ae46-34a1e7ed85e4-2024-11-10</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:countryCode?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:countryCode is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d153d4bd-b39d-43b0-b00a-395ff3e2ca62</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Darwin Core recommends that data from the high seas (outside national jurisdictions) use dwc:countryCode = "XZ".</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="Australia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is bdq:NotEmpty"],[dwc:countryCode="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2308</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/98</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COUNTRYCODE_NOTEMPTY with Specification for: VALIDATION_COUNTRYCODE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYCODE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0493bcfb-652e-4d17-815b-b0cce0742fbe"></a>Term Name  bdqtest:0493bcfb-652e-4d17-815b-b0cce0742fbe</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:countryCode Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0493bcfb-652e-4d17-815b-b0cce0742fbe-2024-09-19</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and recommended in Darwin Core to designate the high seas. Also available in the ISO user defined codes is ZZ, used by Darwin Core and GBIF to mark unknown countries. This Test should accept both XZ and ZZ as COMPLIANT country codes. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:countryCode="GL": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value"],[dwc:countryCode="GRL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L99</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/20</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COUNTRYCODE_STANDARD with Specification for: VALIDATION_COUNTRYCODE_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYCODE_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b23110e7-1be7-444a-a677-cdee0cf4330c"></a>Term Name  bdqtest:b23110e7-1be7-444a-a677-cdee0cf4330c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:country dwc:countryCode Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b23110e7-1be7-444a-a677-cdee0cf4330c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b23110e7-1be7-444a-a677-cdee0cf4330c-2024-09-25</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the ISO country code, determined from the value of dwc:country, equal the value of dwc:countryCode?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either of the terms dwc:country or dwc:countryCode are bdq:Empty; COMPLIANT if the values of dwc:country and dwc:countryCode match national-level country name and matching country code respectively in the bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:6f1093a0-0da5-4691-a95e-184d6d55eeb0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:country,dwc:countryCode</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The country code determination service should be able to match the name of a country in the original or any language in the source authority. When dwc:countryCode="XZ" to designate "high seas", dwc:country should be empty. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Australia", dwc:countryCode="AU": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country matches dwc:countryCode"],[dwc:country="United States Minor Outlying Islands", dwc:countryCode="US": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country does not match dwc:countryCode"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1675</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/62</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Consistency ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT with Specification for: VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d257eb98-27cb-48e5-8d3c-ab9fca4edd11"></a>Term Name  bdqtest:d257eb98-27cb-48e5-8d3c-ab9fca4edd11</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:country dwc:stateProvince Unambiguous</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d257eb98-27cb-48e5-8d3c-ab9fca4edd11</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d257eb98-27cb-48e5-8d3c-ab9fca4edd11-2024-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the combination of the values of the terms dwc:country, dwc:stateProvince unique in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the terms dwc:country and dwc:stateProvince are bdq:Empty; COMPLIANT if the combination of values of dwc:country and dwc:stateProvince are unambiguously resolved to a single result with a child-parent relationship in the bdq:sourceAuthority and the entity matching the value of dwc:country in the bdq:sourceAuthority is an ISO 3166 country-like administrative entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e5efdd20-d1fc-4287-91f9-15b9ce3f3aac</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:country,dwc:stateProvince</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See table https://github.com/tdwg/bdq/issues/95#issuecomment-1226450014. A fail condition may arise from the content being internally inconsistent (not all of the information can be true at the same time), or from the vocabulary being incapable of uniquely resolving the combination of term values. This Test specifically does not consider the content of dwc:higherGeography. If dwc:country contains a value and dwc:stateProvince does not, this Test will return NOT_COMPLIANT. Use cases where knowledge to the level of country is adequate for the fitness of the data should not include this Test. @tucotuco: "Of #200 and #201, #201 is the strongest Test. If it passes for a record, #200 must necessarily also pass and doesn't tell you anything. If #201 fails, #200 could still pass and that would tell you that there are multiple matches on the dwc:country/dwc:stateProvince combo: It would tell you the nature of the problem. Along with #42 (dwc:country not empty), #200 would tell you whether there was an ambiguous combination of country (not empty) and dwc:stateProvince, such as would happen with Argentina/Buenos Aires. While if country is empty, then the ambiguity is purely at the dwc:stateProvince level".</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Argentina", dwc:stateProvince="Rio Negro": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country and dwc:stateProvince are unambiguous"],[dwc:country="", dwc:stateProvince="WA": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country and dwc:stateProvince are ambiguous. Matches Western Australia, Washington State (US)"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Unambiguous</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L3020</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet, Kurator</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/201</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>aabaaac7-b26c-478e-9f04-3e2fbdba4a96</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS with Specification for: VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_69b2efdc-6269-45a4-aecb-4cb99c2ae134"></a>Term Name  bdqtest:69b2efdc-6269-45a4-aecb-4cb99c2ae134</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:country Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/69b2efdc-6269-45a4-aecb-4cb99c2ae134-2024-08-19</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:country occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:country is bdq:Empty; COMPLIANT if value of dwc:country is a place type equivalent to administrative entity of "nation" in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:country</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Non-country information such as "high seas" will fail this Test (high seas should use dwc:countryCode = "XZ" and have dwc:country empty). Getty Place Types for administrative level "nation" are 81010 nation, 81011 independent sovereign nation, and 81012 independent nation. Multiple values in the dwc:country field (whether to signify on a border or in a list of possibilities) will fail this Test. Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This Test should find any matches at the Getty "nation" level including internationalized names and historical representations of that nation (where boundaries are same). This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Eswatini": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country is a valid country name in the bdq:sourceAuthority"],[dwc:country="Tasmania": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Tasmania is not found at the level of national in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L158</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/21</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>3e00109a-13d3-416d-9a91-127c99b47473</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COUNTRY_FOUND with Specification for: VALIDATION_COUNTRY_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRY_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6ce2b2b4-6afe-4d13-82a0-390d31ade01c"></a>Term Name  bdqtest:6ce2b2b4-6afe-4d13-82a0-390d31ade01c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:country Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6ce2b2b4-6afe-4d13-82a0-390d31ade01c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6ce2b2b4-6afe-4d13-82a0-390d31ade01c-2024-09-27</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:country?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:country is bdq:NotEmpty or dwc:countryCode has a value of "XZ" and either dwc:country is bdq:Empty or has a value of "High seas"; otherwise NOT_COMPLIANT ?</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:34ef6ea2-de06-4d2c-88fe-2c779de8f7db</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:country</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:countryCode</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Country is expected to be either bdq:Empty or, ideally, have a value of "High seas" or an agreed equivalent if material comes from the high seas, or from those portions of Antarctica outside of any sovereign nation.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:country="Eswatini": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country is bdq:NotEmpty"],[dwc:country="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L747</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/42</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_COUNTRY_NOTEMPTY with Specification for: VALIDATION_COUNTRY_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_COUNTRY_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_dc8aae4b-134f-4d75-8a71-c4186239178e"></a>Term Name  bdqtest:dc8aae4b-134f-4d75-8a71-c4186239178e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:dateIdentified In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/dc8aae4b-134f-4d75-8a71-c4186239178e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/dc8aae4b-134f-4d75-8a71-c4186239178e-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:dateIdentified within Parameters range and does it overlap with or is it later than dwc:eventDate?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:dateIdentified is bdq:Empty, or (2) dwc:dateIdentified contains an invalid value according to ISO 8601, or (3) bdq:includeEventDate=true and dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the value of dwc:dateIdentified is between bdq:earliestValidDate and bdq:latestValidDate inclusive and either (1) dwc:eventDate is bdq:Empty or bdq:includeEventDate=false, or (2) if dwc:eventDate is a valid ISO 8601 date and dwc:dateIdentified overlaps or is later than the dwc:eventDate; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a25786df-a624-4ff2-8962-6b23e8b07b0b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:dateIdentified</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:earliestValidDate,bdq:latestValidDate,bdq:includeEventDate</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:earliestValidDate default = "1753-01-01",bdq:latestValidDate default = "{current day}",bdq:includeEventDate default = "true"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>There may be valid identifications prior to Linnaeus, but this Test will flag these under the default value of bdq:earliestValidDate, as for most biodiversity data, pre-Linnaean identification dates are likely to be errors. If a parameter is not set, then the default is 1753-01-01. This Test will, by design, flag as problematic cases (such as LTER plots and marine mammal sightings) where a known individual organism is identified by a specialist and then subsequently observed without new taxonomic identifications being made.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dateIdentified="1963-03-08T14:07-0600", dwc:eventDate="1962-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:dateIdentified is in range"],[dwc:dateIdentified="1963-03-08T14:07-0600", dwc:eventDate="1964-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:dateIdentified before dwc:eventDate"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCOtherDateDQ.java#L124</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF, ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/76</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Likeliness ISO/DCMI STANDARD Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>13c17157-1714-4f67-848b-9dc031917fee,030797c0-0b00-4272-9219-16d701e9da7c,739faad3-eb8a-4593-af8f-35b22630a920</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DATEIDENTIFIED_INRANGE with Specification for: VALIDATION_DATEIDENTIFIED_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DATEIDENTIFIED_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_66269bdd-9271-4e76-b25c-7ab81eebe1d8"></a>Term Name  bdqtest:66269bdd-9271-4e76-b25c-7ab81eebe1d8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:dateIdentified Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/66269bdd-9271-4e76-b25c-7ab81eebe1d8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/66269bdd-9271-4e76-b25c-7ab81eebe1d8-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:dateIdentified a valid ISO date?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; COMPLIANT if the value of dwc:dateIdentified contains a valid ISO 8601 date; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:89f8b2ea-fc35-4941-929a-0e32cfbeb1a6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:dateIdentified</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:dateIdentified="1963-03-08T14:07": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:dateIdentified is a valid ISO 8601-1:2019 date"],[dwc:dateIdentified="1963-03-08X14:07-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:dateIdentified is not a valid ISO 8601-1:2019 date"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCOtherDateDQ.java#L61</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/69</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DATEIDENTIFIED_STANDARD with Specification for: VALIDATION_DATEIDENTIFIED_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DATEIDENTIFIED_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_8d787cb5-73e2-4c39-9cd1-67c7361dc02e"></a>Term Name  bdqtest:8d787cb5-73e2-4c39-9cd1-67c7361dc02e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:day In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/8d787cb5-73e2-4c39-9cd1-67c7361dc02e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/8d787cb5-73e2-4c39-9cd1-67c7361dc02e-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:day interpretable as a valid integer between 1 and 28 inclusive, or is it validly 29, 30 or 31 given the dwc:month and dwc:year?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:day is bdq:Empty, or (2) dwc:day is not interpretable as an integer, or (3) dwc:day is interpretable as an integer between 29 and 31 inclusive and dwc:month is not interpretable as an integer between 1 and 12, or (4) dwc:month is interpretable as the integer 2 and dwc:day is interpretable as the integer 29 and dwc:year is not interpretable as a valid ISO 8601 year; COMPLIANT if (1) the value of dwc:day is interpretable as an integer between 1 and 28 inclusive, or (2) dwc:day is interpretable as an integer between 29 and 30 and dwc:month is interpretable as an integer in the set (4,6,9,11), or (3) dwc:day is interpretable as an integer between 29 and 31 and dwc:month is interpretable as an integer in the set (1,3,5,7,8,10,12), or (4) dwc:day is interpretable as the integer 29 and dwc:month is interpretable as the integer 2 and dwc:year is interpretable as is a valid leap year (evenly divisible by 400 or (evenly divisible by 4 but not evenly divisible by 100)); otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2563ae15-a5bf-48fc-91f3-6df869aece2d</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:day,dwc:month,dwc:year</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must take into account the given month and year, if present, to account for leap years. This is part of a group of similar Tests (VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e, #VALIDATION_STARTDAYOFYEAR_INRANGE (85803c7e-2a5a-42e1-b8d3-299a44cafc46), VALIDATION_ENDDAYOFYEAR_INRANGE9a39d88c-7eee-46df-b32a-c109f9f81fb8)).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="15", dwc:month="", dwc:year="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day is in range"],[dwc:day="30", dwc:month="2", dwc:year="1952": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day is not in range"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L829</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/125</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DAY_INRANGE with Specification for: VALIDATION_DAY_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DAY_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_47ff73ba-0028-4f79-9ce1-ee7008d66498"></a>Term Name  bdqtest:47ff73ba-0028-4f79-9ce1-ee7008d66498</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:day Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/47ff73ba-0028-4f79-9ce1-ee7008d66498-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:day an integer between 1 and 31 inclusive?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c0fce1a1-8879-4175-8a71-ce037655c358</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:day</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is part of a group of similar Tests (VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e), VALIDATION_STARTDAYOFYEAR_INRANGE (85803c7e-2a5a-42e1-b8d3-299a44cafc46), VALIDATION_ENDDAYOFYEAR_INRANGE (9a39d88c-7eee-46df-b32a-c109f9f81fb8)).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="15": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day is in range"],[dwc:day="32": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day is not in range"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L639</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018 DQIG Meeting; TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/147</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DAY_STANDARD with Specification for: VALIDATION_DAY_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DAY_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_374b091a-fc90-4791-91e5-c1557c649169"></a>Term Name  bdqtest:374b091a-fc90-4791-91e5-c1557c649169</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dc:type Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/374b091a-fc90-4791-91e5-c1557c649169</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/374b091a-fc90-4791-91e5-c1557c649169-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dc:type?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dc:type is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e1286c46-2a95-480d-89e4-f02681372eb7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dc:type</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dc:type="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dc:type is bdq:NotEmpty"],[dc:type=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dc:type is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L308</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/103</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DCTYPE_NOTEMPTY with Specification for: VALIDATION_DCTYPE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DCTYPE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_cdaabb0d-a863-49d0-bc0f-738d771acba5"></a>Term Name  bdqtest:cdaabb0d-a863-49d0-bc0f-738d771acba5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dc:type Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/cdaabb0d-a863-49d0-bc0f-738d771acba5</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/cdaabb0d-a863-49d0-bc0f-738d771acba5-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dc:type occur as a value in the DCMI type vocabulary?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; COMPLIANT if the value of dc:type is a term name in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b85129f0-28c2-4ede-aff2-5ce3791c6e86</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dc:type</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. EXTERNAL_PREREQUISITES_NOT_MET is not a necessary path in the specification, the type literals may be hard coded in a Test implementation without an external call.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dc:type="Event": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dc:type matches a term in DCMI Vocabulary"],[dc:type="StillerImage": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dc:type does not match terms in DCMI Vocabulary"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1070</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/91</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DCTYPE_STANDARD with Specification for: VALIDATION_DCTYPE_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DCTYPE_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_b6ecda2a-ce36-437a-b515-3ae94948fe83"></a>Term Name  bdqtest:b6ecda2a-ce36-437a-b515-3ae94948fe83</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:decimalLatitude In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/b6ecda2a-ce36-437a-b515-3ae94948fe83</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/b6ecda2a-ce36-437a-b515-3ae94948fe83-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:decimalLatitude a number between -90 and 90 inclusive?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or the value is not interpretable as a number; COMPLIANT if the value of dwc:decimalLatitude is between -90 and 90, inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a5111c0c-d198-4ecc-af10-809ae2b3ae01</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLatitude</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="0.0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatitude is in RANGE"],[dwc:decimalLatitude="121.0534": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatitude is in not in RANGE"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2140</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/79</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DECIMALLATITUDE_INRANGE with Specification for: VALIDATION_DECIMALLATITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLATITUDE_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7d2485d5-1ba7-4f25-90cb-f4480ff1a275"></a>Term Name  bdqtest:7d2485d5-1ba7-4f25-90cb-f4480ff1a275</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:decimalLatitude Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7d2485d5-1ba7-4f25-90cb-f4480ff1a275</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7d2485d5-1ba7-4f25-90cb-f4480ff1a275-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:decimalLatitude?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:decimalLatitude is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:0067fa60-5503-490e-8c94-93fb79cc7da2</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLatitude</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLatitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatiitude is bdq:NotEmpty"],[dwc:decimalLatitude="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatiitude is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2688</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/119</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DECIMALLATITUDE_NOTEMPTY with Specification for: VALIDATION_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLATITUDE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0949110d-c06b-450e-9649-7c1374d940d1"></a>Term Name  bdqtest:0949110d-c06b-450e-9649-7c1374d940d1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:decimalLongitude In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0949110d-c06b-450e-9649-7c1374d940d1</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0949110d-c06b-450e-9649-7c1374d940d1-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:decimalLongitude a number between -180 and 180 inclusive?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLongitude is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:decimalLongitude is between -180 and 180 degrees, inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1a504f7f-21a7-49e1-a0dc-f51146957fa4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLongitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLongitude is in range"],[dwc:decimalLongitude="181.0554": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLongitude >180"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L343</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/30</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DECIMALLONGITUDE_INRANGE with Specification for: VALIDATION_DECIMALLONGITUDE_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLONGITUDE_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_9beb9442-d942-4f42-8b6a-fcea01ee086a"></a>Term Name  bdqtest:9beb9442-d942-4f42-8b6a-fcea01ee086a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:decimalLongitude Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/9beb9442-d942-4f42-8b6a-fcea01ee086a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/9beb9442-d942-4f42-8b6a-fcea01ee086a-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:decimalLongitude?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:decimalLongitude is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c893ee17-ee8b-43ec-bf17-97ac814ea502</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:decimalLongitude</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:decimalLongitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLongitude is bdq:NotEmpty"],[dwc:decimalLongitude=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLongitude is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2273</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/96</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DECIMALLONGITUDE_NOTEMPTY with Specification for: VALIDATION_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DECIMALLONGITUDE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_060e7734-607d-4737-8b2c-bfa17788bf1a"></a>Term Name  bdqtest:060e7734-607d-4737-8b2c-bfa17788bf1a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:degreeofEstablishment Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/060e7734-607d-4737-8b2c-bfa17788bf1a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/060e7734-607d-4737-8b2c-bfa17788bf1a-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:degreeOfEstablishment occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; COMPLIANT if the value of dwc:degreeOfEstablishment is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fec2103b-5d46-4723-b2ec-8c8119b44aaf</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:degreeOfEstablishment</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:degreeOfEstablishment="cultivated": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:degreeOfEstablishment found in the bdq:sourceAuthority"],[dwc:degreeOfEstablishment="grown in garden": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:degreeOfEstablishment not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1694</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/275</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>8aac7359-311a-405f-8117-79bb4873011d</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_DEGREEOFESTABLISHMENT_STANDARD with Specification for: VALIDATION_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_DEGREEOFESTABLISHMENT_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_9a39d88c-7eee-46df-b32a-c109f9f81fb8"></a>Term Name  bdqtest:9a39d88c-7eee-46df-b32a-c109f9f81fb8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:endDayOfYear In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/9a39d88c-7eee-46df-b32a-c109f9f81fb8-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is bdq:Empty or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:62f754b5-a0a1-4b24-9982-b76e4e169f71</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See Test VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e). This Test only asks if dwc:endDayOfYear is a valid value for the relevant year, not if it is consistent with the end day of the range specified in dwc:eventDate. In a non-leap year, the valid range is 1-365 inclusive, in a leap year 366 is also valid. This Test should be run after the series of Tests that assure that dwc:eventDate is populated, if possible (i.e., AMENDMENT_EVENTDATE_FROM_VERBATIM (6d0a0c10-5e4a-4759-b448-88932f399812), AMENDMENT_EVENTDATE_STANDARDIZED (718dfc3c-cb52-4fca-b8e2-0e722f375da7), and AMENDMENT_EVENT_DATE_FROM_YEARMONTHDAY (3892f432-ddd0-4a0a-b713-f2e2ecbd879d)).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1949-01-15T12:34/1949-01-20T17:00", dwc:endDayOfYear="20": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:endDayOfYear is in range"],[dwc:eventDate="", dwc:endDayOfYear="x": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:endDayOfYear is ambiguous, either "X" or "No data" or "10"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1189</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/131</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_ENDDAYOFYEAR_INRANGE with Specification for: VALIDATION_ENDDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_ENDDAYOFYEAR_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4eb48fdf-7299-4d63-9d08-246902e2857f"></a>Term Name  bdqtest:4eb48fdf-7299-4d63-9d08-246902e2857f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:establishmentMeans Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4eb48fdf-7299-4d63-9d08-246902e2857f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4eb48fdf-7299-4d63-9d08-246902e2857f-2024-02-08</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:establishmentMeans occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; COMPLIANT if the value of dwc:establishmentMeans is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f1d3bf9c-5558-41dc-8e33-b17c499be016</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:establishmentMeans</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:establishmentMeans="native": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:establishmentMeans found in the bdq:sourceAuthority"],[dwc:establishmentMeans="cultivated": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:establishmentMeans not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1429</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/268</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>0c051c38-621f-4a52-ae92-5077afd46446</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_ESTABLISHMENTMEANS_STANDARD with Specification for: VALIDATION_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_ESTABLISHMENTMEANS_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3cff4dc4-72e9-4abe-9bf3-8a30f1618432"></a>Term Name  bdqtest:3cff4dc4-72e9-4abe-9bf3-8a30f1618432</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:eventDate In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3cff4dc4-72e9-4abe-9bf3-8a30f1618432</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3cff4dc4-72e9-4abe-9bf3-8a30f1618432-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:eventDate entirely with the Parameter range?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the range of dwc:eventDate is entirely within the range bdq:earliestValidDate to bdq:latestValidDate, inclusive, otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:29a1fdc6-326b-4017-880d-d11ff0225b8f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:earliestValidDate,bdq:latestValidDate</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:earliestValidDate default ="1582-11-15",bdq:latestValidDate default = "{current year}"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test provides for a default earliest date, which is 1582-11-15 by convention. That date was chosen because ISO 8601-1 asserts that "the use of proleptic Gregorian calendar dates prior are not allowed in ISO 8601-1 without prior agreement of the parties exchanging data", and Darwin Core does not comment on this. Different calendars have been used at different times in different places, and the transcription of an original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date, and metadata may or not be present to even identify such records. Given the complexity, and ongoing nature of transitions between calendars, we do not advocate using this Test for quality assurance by selecting a transition date and using it as a threshold.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1962-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate is IN_RANGE"],[dwc:eventDate="2300-11-01T10:00": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate is NOT_IN_RANGE"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L2365</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/36</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>8b223050-f314-4601-9e20-d5f3d59d8e79,2e5c3e37-b6a9-4928-8436-0d83bdb3f0fc</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_EVENTDATE_INRANGE with Specification for: VALIDATION_EVENTDATE_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTDATE_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f51e15a6-a67d-4729-9c28-3766299d2985"></a>Term Name  bdqtest:f51e15a6-a67d-4729-9c28-3766299d2985</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:eventDate Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f51e15a6-a67d-4729-9c28-3766299d2985</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f51e15a6-a67d-4729-9c28-3766299d2985-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:eventDate?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:eventDate is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1fae3f77-7fcb-42c6-ab43-1ff28adf4fa4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1964-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventdate is bdq:NotEmpty"],[dwc:eventDate="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L196</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/33</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_EVENTDATE_NOTEMPTY with Specification for: VALIDATION_EVENTDATE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTDATE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4f2bf8fd-fc5c-493f-a44c-e7b16153c803"></a>Term Name  bdqtest:4f2bf8fd-fc5c-493f-a44c-e7b16153c803</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:eventDate Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4f2bf8fd-fc5c-493f-a44c-e7b16153c803</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4f2bf8fd-fc5c-493f-a44c-e7b16153c803-2024-09-16</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:eventDate a valid ISO date?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; COMPLIANT if the value of dwc:eventDate is a valid ISO 8601 date; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:80c8f69b-4ad3-40ee-bccd-de016bfae367</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test should also pick up issues such as 29 Feb in a non-leap year.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="1963-03-08T14": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate contains a valid ISO 8601-1:2019 date"],[dwc:eventDate="1963-03-08T14:67-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate does not contain a valid ISO 8601-1:2019 date"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L507</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paul Morris</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/66</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance ISO/DCMI STANDARD CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_EVENTDATE_STANDARD with Specification for: VALIDATION_EVENTDATE_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTDATE_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_41267642-60ff-4116-90eb-499fee2cd83f"></a>Term Name  bdqtest:41267642-60ff-4116-90eb-499fee2cd83f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:Event Temporal Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/41267642-60ff-4116-90eb-499fee2cd83f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/41267642-60ff-4116-90eb-499fee2cd83f-2023-09-30</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in any of the terms dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if any of dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate are bdq:NotEmpty; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:b57460c4-16e1-4c1d-8a07-a53aee9e8922</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate,dwc:year,dwc:month,dwc:day,dwc:startDayOfYear,dwc:endDayOfYear,dwc:verbatimEventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Only fails if all of the relevant fields of the Darwin Core Event class are bdq:Empty or do not exist. Relevant Darwin Core fields include dwc:eventDate, dwc:verbatimEventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear. The terms dwc:eventID (if populated may or may not point to temporal information accessible to the user of the data) and dwc:eventTime (which is rare) are not included.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="", dwc:month="", dwc:year="", dwc:eventDate="1962-11-01T10:00-0600", dwc:verbatimEventDate="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate is bdq:NotEmpty"],[dwc:dateIdentified="", dwc:day="", dwc:month="", dwc:year="", dwc:eventDate="", dwc:verbatimEventDate="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All input fields bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1968</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>@Tasilee</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/88</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_EVENTTEMPORAL_NOTEMPTY with Specification for: VALIDATION_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENTTEMPORAL_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_5618f083-d55a-4ac2-92b5-b9fb227b832f"></a>Term Name  bdqtest:5618f083-d55a-4ac2-92b5-b9fb227b832f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:Event Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/5618f083-d55a-4ac2-92b5-b9fb227b832f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/5618f083-d55a-4ac2-92b5-b9fb227b832f-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Are the values in dwc:eventDate consistent with the values in dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty, or all of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear are bdq:Empty; COMPLIANT if all of the following conditions are met (1) dwc:year is bdq:Empty or dwc:eventDate has a precision of one year or finer and and is within a single year and the provided value of dwc:year matches the year expressed in dwc:eventDate, and (2) dwc:month is bdq:Empty or dwc:eventDate has a precision of one month or finer and is within a single month and the provided value in dwc:month matches the month represented by dwc:eventDate, and (3) dwc:day is bdq:Empty or dwc:eventDate has a precision of a day or less and is within a single day and the provided value in dwc:day matches the day represented by dwc:eventDate, and (4) dwc:startDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:startDayOfYear matches the start day of the year of the range represented by dwc:eventDate, and (5) dwc:endDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:endDayOfYear matches the end day of the year of the range represented by dwc:eventDate; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:83d057ea-a6f6-49e6-ac3c-0c418776a0e0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:eventDate,dwc:day,dwc:month,dwc:year,dwc:startDayOfYear,dwc:endDayOfYear</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test does not take a position on whether the value in dwc:eventDate, or the values in the atomic terms are correct, it simply points out the presence of inconsistencies. For this Test, dwc:eventTime is explicitly ignored. It may be useful to consider an additional Test that does evaluate dwc:eventTime and dwc:eventDate. In that case, but not in this Test, if the time is present in both dwc:eventDate and dwc:eventTime, and it is inconsistent, it may indicate an error in the dwc:eventDate, thus making it a problem that someone needs to evaluate. This Test will only assert consistency if the data are both internally consistent and are compliant with the term definitions, for example dwc:day, by its definition, can only be the day of an dwc:eventDate that has a precision of a day or better and is not a range that spans more than a single day. A dwc:day that was internally consistent with the first day of the year (that is, 1) of an dwc:eventDate that only had precision to a year would be consistent internally, but not consistent with the Darwin Core term definitions, and would not return COMPLIANT from this Test.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:day="15", dwc:month="9", dwc:year="1949", dwc:eventDate="1949-09-15T12:34", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day, dwc:month and dwc:year match dwc:eventDate"],[dwc:day="15", dwc:month="9", dwc:year="1949", dwc:eventDate="1949-09-16T12:34", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day does not match dwc:eventDate"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1754</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/67</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Consistency CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_EVENT_CONSISTENT with Specification for: VALIDATION_EVENT_CONSISTENT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_EVENT_CONSISTENT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3667556d-d8f5-454c-922b-af8af38f613c"></a>Term Name  bdqtest:3667556d-d8f5-454c-922b-af8af38f613c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:family Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3667556d-d8f5-454c-922b-af8af38f613c</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3667556d-d8f5-454c-922b-af8af38f613c-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:family occur at the rank of Family in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:family is bdq:Empty; COMPLIANT if the value of dwc:family is found as a value at the rank of Family in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:16f999d9-1cf5-4208-b2ca-1a93d6700085</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:family</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:family="Agaricaceae": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="bdq:family has an equivalent at the rank of Family in the bdq:sourceAuthority"],[dwc:family="Agaricacae": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="bdq:family does not have an equivalent at the rank of Family in the Parameterized Source Authority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L171</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/28</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>146784a4-b53c-4245-a813-c41896761279</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_FAMILY_FOUND with Specification for: VALIDATION_FAMILY_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_FAMILY_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_f2ce7d55-5b1d-426a-b00e-6d4efe3058ec"></a>Term Name  bdqtest:f2ce7d55-5b1d-426a-b00e-6d4efe3058ec</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:genus Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/f2ce7d55-5b1d-426a-b00e-6d4efe3058ec</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/f2ce7d55-5b1d-426a-b00e-6d4efe3058ec-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:genus occur at the rank of Genus in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:genus is bdq:Empty; COMPLIANT if the value of dwc:genus is found as a value at the rank of genus in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:15bbda19-dd18-471a-a5c3-56c7e543012f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:genus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:genus="Egernia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:genus has an equivalent at the rank of Genus in the Parameterized Source Authority"],[dwc:genus="Egernea": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:genus does not have an equivalent at the rank of Genus in the bdq:sourceAuthority. This may be fixed using fuzzy matching at the AMENDMENT stage"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1999</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/122</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>6304e753-423d-4188-bba4-0301c1a01769</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_GENUS_FOUND with Specification for: VALIDATION_GENUS_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_GENUS_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_239ec40e-a729-4a8e-ba69-e0bf03ac1c44"></a>Term Name  bdqtest:239ec40e-a729-4a8e-ba69-e0bf03ac1c44</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:geodeticDatum Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/239ec40e-a729-4a8e-ba69-e0bf03ac1c44</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/239ec40e-a729-4a8e-ba69-e0bf03ac1c44-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:geodeticDatum?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:geodeticDatum is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a3c8b277-15fb-4ae8-afb1-e64fb6eb5241</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="UTM": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:geodeticDatum is bdq:NotEmpty"],[dwc:geodeticDatum="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:geodeticDatum is bdq:Empty."]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2105</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/78</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_GEODETICDATUM_NOTEMPTY with Specification for: VALIDATION_GEODETICDATUM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_GEODETICDATUM_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7e0c0418-fe16-4a39-98bd-80e19d95b9d1"></a>Term Name  bdqtest:7e0c0418-fe16-4a39-98bd-80e19d95b9d1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Vaildation dwc:geodeticDatum Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7e0c0418-fe16-4a39-98bd-80e19d95b9d1</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7e0c0418-fe16-4a39-98bd-80e19d95b9d1-2025-03-03</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:geodeticDatum occur as a valid geographic CRS, geodetic Datum or ellipsoid in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available, INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; COMPLIANT if the value of dwc:geodeticDatum is a valid code from the bdq:sourceAuthority (in the form Authority:Number) for a Datum, or ellipsoid, or for a CRS appropriate for a 2D geographic coordinate in degrees, or is the value "not recorded"; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:5cc05662-c029-4ba9-b32e-fb487ccba71c</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:geodeticDatum</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Darwin Core recommends best practice is to use a controlled vocabulary. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. Chapman and Wieczorek (2020) recommend best practice is to use EPSG geographic CRS or Datum codes (https://epsg.io/) as a controlled vocabulary. Ideally, amend to the EPSG code for the geographic coordinate reference system (CRS), if known. Otherwise use the EPSG code for the geodetic datum, if known. Otherwise use the EPSG code of the ellipsoid, if known. If none of these is known, use the explicit value "not recorded". While "not recorded" is not a valid EPSG code, it is a valid value according to Darwin Core. The reference vocabularies of values for geodetic datums and ellipsoids needs to be made available and should map alternative representations of dwc:geodeticDatum strings to EPSG codes, such as "WGS84", "WGS_84", "WGS:84", "WGS 84" all with standard value "EPSG:4326".</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:geodeticDatum="EPSG:4326": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:geodeticDatum matches an unambiguous alphanumeric CRS or datum code value in the bdq:sourceAuthority"],[dwc:geodeticDatum="7030": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:geodeticDatum doesn't match values in the bdq:sourceAuthority, 7030 is a bare number without an authority.]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L1500</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/59</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_GEODETICDATUM_STANDARD with Specification for: VALIDATION_GEODETICDATUM_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_GEODETICDATUM_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_125b5493-052d-4a0d-a3e1-ed5bf792689e"></a>Term Name  bdqtest:125b5493-052d-4a0d-a3e1-ed5bf792689e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:kingdom Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/125b5493-052d-4a0d-a3e1-ed5bf792689e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/125b5493-052d-4a0d-a3e1-ed5bf792689e-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:kingdom occur at the rank of Kingdom in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:kingdom is bdq:Empty; COMPLIANT if the value of dwc:kingdom is found as a value at the rank of kingdom in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a90e100a-3522-4742-aa73-3b98a35ab826</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:kingdom</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:kingdom="Animalia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:kingdom has an equivalent at the rank of Kingdom in the bdq:sourceAuthority"],[dwc:kingdom="Metazoa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:kingdom does not strictly have an equivalent at the rank of Kingdom in the Parameterized Source Authority (Metazoa is synonym of Animalia)"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1386</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/81</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>a5055cb3-b1e5-4070-90df-f875b0d9ae8a</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_KINGDOM_FOUND with Specification for: VALIDATION_KINGDOM_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_KINGDOM_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_36ed36c9-b1a7-40b2-b5e2-0d012e772098"></a>Term Name  bdqtest:36ed36c9-b1a7-40b2-b5e2-0d012e772098</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:kingdom Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/36ed36c9-b1a7-40b2-b5e2-0d012e772098</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/36ed36c9-b1a7-40b2-b5e2-0d012e772098-2024-01-28</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:kingdom?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:kingdom is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e6f0a9ce-3e72-40fb-9fad-63cf5962f93e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:kingdom</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:kingdom="Fungi": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:kingdom is bdq:NotEmpty"],[dwc:kingdom="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:kingdom is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L3021</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/216</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_KINGDOM_NOTEMPTY with Specification for: VALIDATION_KINGDOM_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_KINGDOM_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_15f78619-811a-4c6f-997a-a4c7888ad849"></a>Term Name  bdqtest:15f78619-811a-4c6f-997a-a4c7888ad849</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dcterms:license Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/15f78619-811a-4c6f-997a-a4c7888ad849</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/15f78619-811a-4c6f-997a-a4c7888ad849-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dcterms:license?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dcterms:license is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d8b450af-47e6-4f5c-8154-6d6acbe9efa5</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dcterms:license</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The license at the record level might be derived from the license of the dataset from which the record is retrieved.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dcterms:license="CC0 1.0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dcterms:license is bdq:NotEmpty"],[dcterms:license=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dcterms:license is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L274</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/99</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_LICENSE_NOTEMPTY with Specification for: VALIDATION_LICENSE_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_LICENSE_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3136236e-04b6-49ea-8b34-a65f25e3aba1"></a>Term Name  bdqtest:3136236e-04b6-49ea-8b34-a65f25e3aba1</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dcterms:license Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3136236e-04b6-49ea-8b34-a65f25e3aba1</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3136236e-04b6-49ea-8b34-a65f25e3aba1-2024-03-21</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dcterms:license occur in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dcterms:license is bdq:Empty; COMPLIANT if the value of the term dcterms:license is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2a9dbd16-d427-471e-8db5-c1de2b2cf030</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dcterms:license</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Creative Commons 4.0 Licenses or CC0" {[https://creativecommons.org/]} { Regular Expression ^(http(s){0,1}://creativecommons.org/licenses/(by&#124;by-sa&#124;by-nc&#124;by-nc-sa&#124;by-nd&#124;by-nc-nd)/4.0/((deed&#124;legalcode)(.(id&#124;eu&#124;da&#124;de&#124;en&#124;es&#124;fr&#124;fy&#124;hr&#124;it&#124;lv&#124;lt&#124;mi&#124;ni&#124;no&#124;pl&#124;pt&#124;ro&#124;si&#124;fi&#124;sv&#124;tr&#124;cs&#124;el&#124;ru&#124;uk&#124;ar&#124;jp&#124;zh-hans&#124;zh-hant&#124;ko)){0,1})&#124;(http(s){0,1}://creativecommons.org/publicdomain/zero/1.0/((deed&#124;legalcode)(.(id&#124;eu&#124;da&#124;de&#124;en&#124;es&#124;fr&#124;fy&#124;hr&#124;it&#124;lv&#124;lt&#124;ni&#124;no&#124;pl&#124;pt&#124;ro&#124;si&#124;fi&#124;sv&#124;tr&#124;cs&#124;el&#124;ru&#124;uk&#124;ar&#124;jp&#124;zh-hans&#124;zh-hant&#124;ko)){0,1})))$ }</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The license at the record level might be derived from the license of the dataset from which the record is retrieved. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. The canonical form of the Creative Commons license IRI has nothing after the version (e.g., https://creativecommons.org/licenses/by/4.0/), but may be followed by deed or legalcode e.g. https://creativecommons.org/licenses/by/4.0/deed and this may be followed by a language code. However, only some two-letter language codes have translations, and some translations are identified by a longer string than the two-letter language code. Errors in the language code, or specifying a language code for which a translation doesn't exist returns a 404 error instead of redirecting to the more general license IRI. As of 2024-02-28 deed.mi doesn't exist yet, but legalcode.mi does.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dcterms:license="https://creativecommons.org/licenses/by/4.0/": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT,Response.comment="dcterms:license matches a term in the bdq:sourceAuthority"],[dcterms:license="GPL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dcterms:license does not match a term in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L635</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>John Wieczorek</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/38</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>7308bf21-2648-40d8-bb2c-3f36d2789552</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_LICENSE_STANDARD with Specification for: VALIDATION_LICENSE_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_LICENSE_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_58486cb6-1114-4a8a-ba1e-bd89cfe887e9"></a>Term Name  bdqtest:58486cb6-1114-4a8a-ba1e-bd89cfe887e9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dcterms:Location Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/58486cb6-1114-4a8a-ba1e-bd89cfe887e9</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/58486cb6-1114-4a8a-ba1e-bd89cfe887e9-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in any of the Darwin Core spatial terms that could specify a location?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if at least one term needed to determine the location of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:30ed5e2d-ef30-4988-8dbb-12c119e94ac3</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:higherGeographyID,dwc:higherGeography,dwc:continent,dwc:country,dwc:countryCode,dwc:stateProvince,dwc:county,dwc:municipality,dwc:waterBody,dwc:island,dwc:islandGroup,dwc:locality,dwc:locationID,dwc:verbatimLocality,dwc:decimalLatitude,dwc:decimalLongitude,dwc:verbatimCoordinates,dwc:verbatimLatitude,dwc:verbatimLongitude,dwc:footprintWKT</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Only fails if all of the relevant fields of the Darwin Core Location class are EMPTY or do not exist. Relevant Darwin Core fields include dwc:locationID, dwc:higherGeographyID, dwc:higherGeography, dwc:continent, dwc:waterBody, dwc:islandGroup, dwc:island, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality, dwc:locality, dwc:verbatimLocality, dwc:decimalLatitude, dwc:decimalLongitude, dwc:verbatimCoordinates, dwc:verbatimLatitude, dwc:verbatimLongitude, dwc:footprintWKT. Elevation and/or depth alone are deemed insufficient to meaningfully locate a position on the earth.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:locationID="https://opencontext.org/subjects/e54377f7-4452-4315-b676-40679b10c4d9", dwc:higherGeographyID="", dwc:higherGeography="",dwc:continent="", dwc:waterBody="", dwc:islandGroup="", dwc:island="", dwc:country="", dwc:countryCode="", dwc:stateProvince="", dwc:county="", dwc:municipality="", dwc:locality="", dwc:verbatimLocality="", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="", dwc:geodeticDatum="", dwc:verbatimCoordinates="", dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:footprintWKT="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:LocationID is bdq:NotEmpty"],[dwc:locationID="", dwc:higherGeographyID="", dwc:higherGeography="", dwc:continent="", dwc:waterBody="", dwc:islandGroup="", dwc:island="", dwc:country="", dwc:countryCode="", dwc:stateProvince="", dwc:county="", dwc:municipality="", dwc:locality="", dwc:verbatimLocality="", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="", dwc:geodeticDatum="", dwc:verbatimCoordinates="", dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:footprintWKT="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All location fields are bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L672</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Lee Belbin</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/40</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_LOCATION_NOTEMPTY with Specification for: VALIDATION_LOCATION_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_LOCATION_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3f1db29a-bfa5-40db-9fd1-fde020d81939"></a>Term Name  bdqtest:3f1db29a-bfa5-40db-9fd1-fde020d81939</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:maximumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3f1db29a-bfa5-40db-9fd1-fde020d81939</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3f1db29a-bfa5-40db-9fd1-fde020d81939-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:maximumDepthInMeters within the Parameter range?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumDepthInMeters is bdq:Empty or is not interpretable as a number greater than or equal to zero; COMPLIANT if the value of dwc:maximumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:cebc8ba0-ca02-4f1e-830e-ec693bc628e4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidDepthInMeters,bdq:maximumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The Challenger Deep in the Mariana Trench is the deepest known point in Earth's oceans at 10,994 meters below sea level. We have rounded up bdq:maximumValidDepthInMeters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:maximumDepthInMeters="1200": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:maximumDepthInMeters is in range (<11,000)"],[dwc:maximumDepthInMeters="99999": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:maximumDepthInMeters is not in range (>11,000)"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2726</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/187</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>edf69c59-056d-4c8a-b1fb-647ea684eb18,f41be58e-2e1e-409e-a322-1de95df2ce0b</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_MAXDEPTH_INRANGE with Specification for: VALIDATION_MAXDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MAXDEPTH_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c971fe3f-84c1-4636-9f44-b1ec31fd63c7"></a>Term Name  bdqtest:c971fe3f-84c1-4636-9f44-b1ec31fd63c7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:maximumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c971fe3f-84c1-4636-9f44-b1ec31fd63c7</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c971fe3f-84c1-4636-9f44-b1ec31fd63c7-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:maximumElevationInMeters within the Parameter range?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumElevationInMeters is bdq:Empty or the value cannot be interpreted as a number; COMPLIANT if the value of dwc:maximumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f9471802-a5f7-4f4e-9810-f3f4f43dad1a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:maximumElevationInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidElevationInMeters,bdq:maximumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have rounded up the Parameter values. We are aware of sub-ice elevations in Antarctica to -3,500m and possible sampling in the atmosphere above the elevation of the top of Mt Everest should fail this Test if captured as elevation rather than as distanceAboveSurfaceInMeters. Elevations below the maximum elevation yet above the local surface will be false positives.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:maximumElevation is in is range"],[dwc:maximumElevationInMeters="-500": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:maximumElevation is not in range, i.e. is <-430"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2622</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/112</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Likeliness Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>3ab181c2-a3d8-4317-af4d-f88181e2773a,1766715d-e588-4361-8b27-1c9cc43662ab</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_MAXELEVATION_INRANGE with Specification for: VALIDATION_MAXELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MAXELEVATION_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_04b2c8f3-c71b-4e95-8e43-f70374c5fb92"></a>Term Name  bdqtest:04b2c8f3-c71b-4e95-8e43-f70374c5fb92</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:minimumDepthInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/04b2c8f3-c71b-4e95-8e43-f70374c5fb92</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/04b2c8f3-c71b-4e95-8e43-f70374c5fb92-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumDepthInMeters within the Parameter range?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters is bdq:Empty, or the value is not interpretable as number greater than or equal to zero; COMPLIANT if the value of dwc:minimumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:minimumDepthInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidDepthInMeters,bdq:maximumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The Challenger Deep in the Mariana Trench is the deepest known point in Earth's oceans at 10,994 meters below sea level. We have rounded up bdq:maximumValidDepthInMeters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumDepthInMeters="1": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumDepthInMeters is in range"],[dwc:minimumDepthInMeters="12000": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumDepthInMeters is not in range"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2421</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/107</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>d23e61b3-07b6-4326-bac2-1457b030efef,9f12e2c3-17ac-42c0-91f4-c40a02d3f133</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_MINDEPTH_INRANGE with Specification for: VALIDATION_MINDEPTH_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINDEPTH_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_8f1e6e58-544b-4365-a569-fb781341644e"></a>Term Name  bdqtest:8f1e6e58-544b-4365-a569-fb781341644e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:minimumDepthInMeters less than dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/8f1e6e58-544b-4365-a569-fb781341644e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/8f1e6e58-544b-4365-a569-fb781341644e-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumDepthInMeters a number less than or equal to the value of dwc:maximumDepthInMeters?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters is bdq:Empty, or if either are interpretable as not zero or a positive number; COMPLIANT if the value of dwc:minimumDepthInMeters is less than or equal to the value of dwc:maximumDepthInMeters; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:12f7f82e-ab1c-4690-92b8-ecc9328256c1</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:minimumDepthInMeters,dwc:maximumDepthInMeters</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumDepthInMeters="0", dwc:maximumDepthInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumDepthInMeters = dwc:maximumDepthInMeters"],[dwc:minimumDepthInMeters="1", dwc:maximumDepthInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumDepthInMeters > dwc:maximumDepthInMeters"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L268</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, OBIS</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/24</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH with Specification for: VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_0bb8297d-8f8a-42d2-80c1-558f29efe798"></a>Term Name  bdqtest:0bb8297d-8f8a-42d2-80c1-558f29efe798</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:minimumElevationInMeters In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/0bb8297d-8f8a-42d2-80c1-558f29efe798</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/0bb8297d-8f8a-42d2-80c1-558f29efe798-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumElevationInMeters within the Parameter range?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2bb79221-0312-410a-aef6-f569485df6a6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:minimumElevationInMeters</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:minimumValidElevationInMeters,bdq:maximumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>We have rounded up the Parameter values. We are aware of sub-ice elevations in Antarctica to -3,500m and possible sampling in the atmosphere above the elevation of the top of Mt Everest should fail this Test if captured as elevation rather than as distanceAboveSurfaceInMeters. Elevations below the maximum elevation yet above the local surface will be false positives.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumElevationInMeters is IN_RANGE"],[dwc:minimumElevationInMeters="-500": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumElevationInMeters is NOT_IN_RANGE (<-430)"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L582</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/39</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>6e07e4fe-ce7a-4e5f-9fa3-c26877b273a7,307b78fe-e168-422b-977f-cdb4e1c5e636</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_MINELEVATION_INRANGE with Specification for: VALIDATION_MINELEVATION_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINELEVATION_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_d708526b-6561-438e-aa1a-82cd80b06396"></a>Term Name  bdqtest:d708526b-6561-438e-aa1a-82cd80b06396</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:minimumElevationInMeters less than dwcmaximumElevationInMeters</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/d708526b-6561-438e-aa1a-82cd80b06396</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/d708526b-6561-438e-aa1a-82cd80b06396-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:minimumElevationInMeters a number less than or equal to the value of dwc:maximumElevationInMeters?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumlevationInMeters or dwc:minimumElevationInMeters is bdq:Empty, or if either is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is a number less than or equal to the value of the number dwc:maximumElevationInMeters, otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f799fb5c-37e4-46d7-a07e-87eb071df9c6</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:minimumElevationInMeters,dwc:maximumElevationInMeters</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:minimumElevationInMeters="0", dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumElevationInMeters is equal to dwc: maximumElevationInMeters"],[dwc:minimumElevationInMeters="1", dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumElevationInMeters is greater than dwc:maximumElevationInMeters"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2497</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>@Tasilee</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/108</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION with Specification for: VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_01c6dafa-0886-4b7e-9881-2c3018c98bdc"></a>Term Name  bdqtest:01c6dafa-0886-4b7e-9881-2c3018c98bdc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:month Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/01c6dafa-0886-4b7e-9881-2c3018c98bdc</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/01c6dafa-0886-4b7e-9881-2c3018c98bdc-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:month interpretable as an integer between 1 and 12 inclusive?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; COMPLIANT if the value of dwc:month is interpretable as an integer between 1 and 12 inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:2c5dbdbb-feab-474c-bcca-bf6d1b90ae66</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:month</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:month="10": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:month is in range"],[dwc:month="v": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:month is ambiguous as "v" or "5""]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L690 Unit test in [DwcEventDQTest]{https://github.com/FilteredPush/event_date_qc/blob/v3.0.0/src/test/java/org/filteredpush/qc/date/DwcEventDQTest.java#L242)</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville (MONTH_INVALID/MONTH_IN_RANGE previously in spreadsheet, from ALA?)</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/126</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_MONTH_STANDARD with Specification for: VALIDATION_MONTH_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_MONTH_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_ff59f77d-71e9-4eb1-aac9-8bd05c50ff70"></a>Term Name  bdqtest:ff59f77d-71e9-4eb1-aac9-8bd05c50ff70</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:namePublishedInYear Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/ff59f77d-71e9-4eb1-aac9-8bd05c50ff70</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/ff59f77d-71e9-4eb1-aac9-8bd05c50ff70-2024-02-07</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:namePublishedInYear?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:namePublishedInYear is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f09fc9ad-a449-4422-b32f-63d8ccf2501f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:namePublishedInYear</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:namePublishedInYear="2024": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:namePublishedInYear is bdq:NotEmpty"],[dwc:namePublishedInYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:namePublishedInYear is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L3090</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/259</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY with Specification for: VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c486546c-e6e5-48a7-b286-eba7f5ca56c4"></a>Term Name  bdqtest:c486546c-e6e5-48a7-b286-eba7f5ca56c4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:occurrenceID Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c486546c-e6e5-48a7-b286-eba7f5ca56c4</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c486546c-e6e5-48a7-b286-eba7f5ca56c4-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:occurrenceID?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:occurrenceID is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3d9e1339-19d7-47e7-af9e-11905df82b6a</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:occurrenceID</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceID="https://www.inaturalist.org/observations/43047701": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceID conforms to GUID structure"],[dwc:occurrenceID="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceID is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L173</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/47</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_OCCURRENCEID_NOTEMPTY with Specification for: VALIDATION_OCCURRENCEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_OCCURRENCEID_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf"></a>Term Name  bdqtest:eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:occurrenceStatus Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:occurrenceStatus?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:occurrenceStatus is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c3a53898-c4ad-40e0-961b-b4ceafea37c7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceStatus is bdq:NotEmpty"],[dwc:occurrenceStatus="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceStatus is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L489</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/117</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_OCCURRENCESTATUS_NOTEMPTY with Specification for: VALIDATION_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_OCCURRENCESTATUS_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47"></a>Term Name  bdqtest:7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:occurrenceStatus Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47-2025-02-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:occurrenceStatus occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:Empty; COMPLIANT if the value of dwc:occurrenceStatus is resolved in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:fbe854d4-acf3-4c79-a654-81441fed644f</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:occurrenceStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Regex present/absent" {["^(present\</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The recommended controlled vocabulary for this term consists of "present" and "absent", which are the only two appropriate terms for a Darwin Core Occurrence. This is reflected in the dwc:occurrenceStatus vocabulary for this Test. There is currently a mismatch between the (authoritative) lower case values at https://dwc.tdwg.org/terms/#dwc:occurrenceStatus and the vocabulary at GBIF (https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts), which capitalized the first character. This Test must return NOT_COMPLIANT if there are case differences, leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:occurrenceStatus="present": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceStatus matches a term in the bdq:sourceAuthority"],[dwc:occurrenceStatus="presence": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceStatus does not match a term in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L418</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/116</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>74716bc2-c82e-49f3-938b-2298094554b4</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_OCCURRENCESTATUS_STANDARD with Specification for: VALIDATION_OCCURRENCESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_OCCURRENCESTATUS_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_81cc974d-43cc-4c0f-a5e0-afa23b455aa3"></a>Term Name  bdqtest:81cc974d-43cc-4c0f-a5e0-afa23b455aa3</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:order Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/81cc974d-43cc-4c0f-a5e0-afa23b455aa3</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/81cc974d-43cc-4c0f-a5e0-afa23b455aa3-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:order occur at the rank of Order in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:order is bdq:Empty; COMPLIANT if the value of dwc:order is found as a value at the rank of Order in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:ae08b4b4-89ba-4972-b51f-912b132bd006</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:order</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:order="Lepidoptera": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:order has an equivalent at the rank of Order in the bdq:sourceAuthority"],[dwc:order="Nymphalidae": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:order does not have an equivalent at the rank of Order in the bdq:sourceAuthority. Nymphalidae is a family, not an order"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1459</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/83</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>c169404f-d797-40a1-9c84-3edb2383b759</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_ORDER_FOUND with Specification for: VALIDATION_ORDER_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_ORDER_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_5424e933-bee7-4125-839e-d8743ea69f93"></a>Term Name  bdqtest:5424e933-bee7-4125-839e-d8743ea69f93</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:pathway Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/5424e933-bee7-4125-839e-d8743ea69f93</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/5424e933-bee7-4125-839e-d8743ea69f93-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:pathway occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; COMPLIANT if the value of dwc:pathway is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c7c92ef0-284e-4c5d-8fc9-f1480bfe0b8e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:pathway</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:pathway="transportStowaway": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:pathway found in the bdq:sourceAuthority"],[dwc:pathway="escapee": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:pathway not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L1875</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/277</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>136039c5-6ceb-41ec-90b3-eb1cd37d6eed</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_PATHWAY_STANDARD with Specification for: VALIDATION_PATHWAY_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_PATHWAY_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f"></a>Term Name  bdqtest:eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:phylum Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f-2022-03-25</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:phylum occur at the rank of Phylum in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdq:Empty; COMPLIANT if the value of dwc:phylum is found as a value at the rank of Phylum in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:1193230f-f188-4917-92da-bba3390ed3fa</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:phylum</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"],[dwc:phylum="Trachyophyta": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:phylum does not have an equivalent at the rank of Phylum in the bdq:sourceAuthority."]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L130</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>iDigBio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/22</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>bd91e45d-691a-4d7e-9917-7b6231c05c43</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_PHYLUM_FOUND with Specification for: VALIDATION_PHYLUM_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_PHYLUM_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_17f03f1f-f74d-40c0-8071-2927cfc9487b"></a>Term Name  bdqtest:17f03f1f-f74d-40c0-8071-2927cfc9487b</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation Polynomial Consistent</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/17f03f1f-f74d-40c0-8071-2927cfc9487b</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/17f03f1f-f74d-40c0-8071-2927cfc9487b-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the polynomial represented in dwc:scientificName consistent with the equivalent values in dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty, or all of dwc:genericName, dwc:specificEpithet and dwc:infraspecificEpithet are bdq:Empty; COMPLIANT if the polynomial, as represented in dwc:scientificName, is consistent with bdq:NotEmpty values of dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d92c5e23-bf6a-483b-86c3-9374e12d01c7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificName,dwc:genericName,dwc:specificEpithet,dwc:infraspecificEpithet</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If dwc:specificEpithet is populated then this Test expects that the value dwc:specificEpithet is the name of the second or species epithet of the scientificName. If dwc:genericName is populated, this Test expects that the value of dwc:genus is the first word of the value of dwc:scientificName. If dwc:specificEpithet is populated then this Test expects that the value dwc:specificEpithet is the name of the first or species epithet of the scientificName. If dwc:infraspecificEpithet is populated, then this Test expects that the value of dwc:infraspecificEpithet is the name of the lowest or terminal infraspecific epithet of the scientificName, excluding any rank designation.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificName="Hakea decurrens ssp. physocarpa", dwc:genericName="", dwc:specificEpithet="decurrens", dwc:infraspecificEpithet="physocarpa": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Values of all non-empty atomic terms are found in the polynomial"],[dwc:scientificName="Hakea decurrens", dwc:genericName="Hakea", dwc:specificEpithet="decurrens", dwc:infraspecificEpithet="physocarpa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is inconsistent with atomic parts (dwc:genus, dwc:specificEpithet and dwc:infraspecificEpithet)"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1570</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Paula Zermoglio</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/101</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Consistency CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_POLYNOMIAL_CONSISTENT with Specification for: VALIDATION_POLYNOMIAL_CONSISTENT</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_POLYNOMIAL_CONSISTENT</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_49f1d386-5bed-43ae-bd43-deabf7df64fc"></a>Term Name  bdqtest:49f1d386-5bed-43ae-bd43-deabf7df64fc</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:scientificNameAuthorship Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/49f1d386-5bed-43ae-bd43-deabf7df64fc</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/49f1d386-5bed-43ae-bd43-deabf7df64fc-2024-02-04</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:scientificNameAuthorship?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:scientificNameAuthorship is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e9ffc3b0-0fb8-4a7c-a588-a00085ba980b</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificNameAuthorship</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameAuthorship="(Györfi, 1952)": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameAuthorship is bdq:NotEmpty"],[dwc:scientificNameAuthorship="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameAuthorship is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L3055</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/244</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY with Specification for: VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_6eeac3ed-f691-457f-a42e-eaa9c8a71ce8"></a>Term Name  bdqtest:6eeac3ed-f691-457f-a42e-eaa9c8a71ce8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:scientificNameID Complete</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/6eeac3ed-f691-457f-a42e-eaa9c8a71ce8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/6eeac3ed-f691-457f-a42e-eaa9c8a71ce8-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:scientificNameID contain a complete identifier?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty; COMPLIANT if (1) dwc:scientificNameID is a validly formed LSID, or (2) dwc:scientificNameID is a validly formed URN with at least NID and NSS present, or (3) dwc:scientificNameID is in the form scope:value, or (4) dwc:scientificNameID is a validly formed URI with host and path where path consists of more than just "/"; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e6c02558-8541-4292-9a11-2f4408d69699</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If any single bdq:sourceAuthority such as GBIF is used, a valid and complete dwc:scientificNameID based on an alternative source authority is unlikely to provide a valid match. A text or number string as a namespace indicator without a URI will be ambiguous. As an example, GBIF's backbone taxonomy dataset can be found at https://doi.org/10.15468/39omei. When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID. Note that GBIF currently uses "TaxonID" for this entity. The terms NID, NSS, and URN are all Uniform Resource Identifiers - see the Wikipedia (2024) reference.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameID="urn:lsid:zoobank.org:act:17ADF24F-027F-44F6-9543-D3D0260CE79E": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameID contains a URI and a namespace indicator"],[dwc:scientificNameID="Hakea decurrens ssp. physocarpa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameID does not contain a URI"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Complete</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L2903</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2 December 2023</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/212</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_SCIENTIFICNAMEID_COMPLETE with Specification for: VALIDATION_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAMEID_COMPLETE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_401bf207-9a55-4dff-88a5-abcd58ad97fa"></a>Term Name  bdqtest:401bf207-9a55-4dff-88a5-abcd58ad97fa</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:scientificNameID Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/401bf207-9a55-4dff-88a5-abcd58ad97fa</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/401bf207-9a55-4dff-88a5-abcd58ad97fa-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:scientificNameID?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:scientificNameID is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:02242018-3e73-4e0a-8d6f-d1db06cf81a3</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificNameID</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificNameID="8fa58e08-08de-4ac1-b69c-1235340b7001": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameID is bdq:NotEmpty"],[dwc:scientificNameID=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameID is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1845</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/120</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_SCIENTIFICNAMEID_NOTEMPTY with Specification for: VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_3f335517-f442-4b98-b149-1e87ff16de45"></a>Term Name  bdqtest:3f335517-f442-4b98-b149-1e87ff16de45</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:scientificName Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/3f335517-f442-4b98-b149-1e87ff16de45</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/3f335517-f442-4b98-b149-1e87ff16de45-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a match of the contents of dwc:scientificName with the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty; COMPLIANT if there is a match of the contents of dwc:scientificName in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:3c2fe7e9-186f-4ceb-8274-8bbcb4a62de4</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The purpose of this Test is to detect errors in the scientific name but is dependent on the abilities of the parsing of the bdq:sourceAuthority. For research users of biodiversity data doing quality assurance, VALIDATION_TAXON_UNAMBIGUOUS (4c09f127-737b-4686-82a0-7c8e30841590) handles their needs, but for curators of datasets doing quality control, this Test provides a specific subset of targeted data cleaning, making it a valuable Test to include for the quality control case.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in the bdq:sourceAuthority"],[dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L212</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/46</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>d9dc26f7-6c4e-4647-addc-20197ce50d2b</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_SCIENTIFICNAME_FOUND with Specification for: VALIDATION_SCIENTIFICNAME_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAME_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7c4b9498-a8d9-4ebb-85f1-9f200c788595"></a>Term Name  bdqtest:7c4b9498-a8d9-4ebb-85f1-9f200c788595</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:scientificName Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7c4b9498-a8d9-4ebb-85f1-9f200c788595</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7c4b9498-a8d9-4ebb-85f1-9f200c788595-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:scientificName?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:scientificName is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:a9c18563-f63e-42db-98e5-a3e6079086b7</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:scientificName</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:scientificName="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName is bdq:NotEmpty"],[dwc:scientificName="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1426</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA,GBIF,OBIS</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/82</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_SCIENTIFICNAME_NOTEMPTY with Specification for: VALIDATION_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SCIENTIFICNAME_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_88d8598b-3318-483d-9475-a5acf9887404"></a>Term Name  bdqtest:88d8598b-3318-483d-9475-a5acf9887404</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:sex Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/88d8598b-3318-483d-9475-a5acf9887404</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/88d8598b-3318-483d-9475-a5acf9887404-2024-02-09</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:sex occur in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; COMPLIANT if the value of dwc:sex is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:72471db4-226c-454f-bbe8-5c1718e6c834</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:sex</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. For reference, a list of synonyms for dwc:sex values can be found at https://registry.gbif.org/vocabulary/Sex/concepts.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:sex="Male": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:sex found in the bdq:sourceAuthority"],[dwc:sex="f": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:sex not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L2084</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/283</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>2964d61f-eab0-4a21-9ac6-3f6a7c4fbf86</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_SEX_STANDARD with Specification for: VALIDATION_SEX_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_SEX_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_85803c7e-2a5a-42e1-b8d3-299a44cafc46"></a>Term Name  bdqtest:85803c7e-2a5a-42e1-b8d3-299a44cafc46</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:startDayOfYear In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/85803c7e-2a5a-42e1-b8d3-299a44cafc46</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/85803c7e-2a5a-42e1-b8d3-299a44cafc46-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:startDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:startDayOfYear is bdq:Empty or if the value of dwc:startDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find single year or a start year in a range); COMPLIANT if the value of dwc:startDayOfYear is an integer between 1 and 365, inclusive, or if the value of dwc:startDayOfYear is 366 and the start year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:53c6af68-6120-4da6-87d8-a3e9551b9671</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:startDayOfYear</td>
		</tr>
		<tr>
			<td>InformationElements Consulted</td>
			<td>dwc:eventDate</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See Test VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e). This Test only asks if dwc:startDayOfYear is a valid value for the relevant year, not if it is consistent with the start day of the range specified in dwc:eventDate. In a non-leap year, the valid range is 1-365 inclusive, in a leap year 366 is also valid. This Test should be run after the series of Tests that assure that dwc:eventDate is populated, if possible (i.e., AMENDMENT_EVENTDATE_FROM_VERBATIM (6d0a0c10-5e4a-4759-b448-88932f399812), AMENDMENT_EVENTDATE_STANDARDIZED (718dfc3c-cb52-4fca-b8e2-0e722f375da7), and AMENDMENT_EVENT_DATE_FROM_YEARMONTHDAY (3892f432-ddd0-4a0a-b713-f2e2ecbd879d)).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:eventDate="", dwc:startDayOfYear="15": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:startDayOfYear is in range"],[dwc:eventDate="", dwc:startDayOfYear="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:startDayOfYear is not in range"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L1087</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/130</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_STARTDAYOFYEAR_INRANGE with Specification for: VALIDATION_STARTDAYOFYEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_STARTDAYOFYEAR_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4daa7986-d9b0-4dd5-ad17-2d7a771ea71a"></a>Term Name  bdqtest:4daa7986-d9b0-4dd5-ad17-2d7a771ea71a</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:stateProvince Found</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4daa7986-d9b0-4dd5-ad17-2d7a771ea71a</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4daa7986-d9b0-4dd5-ad17-2d7a771ea71a-2024-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:stateProvince occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:stateProvince is bdq:Empty; COMPLIANT if the value of dwc:stateProvince occurs as an administrative entity that is a child to at least one entity representing an ISO 3166 country-like entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:d261fac1-ce61-4879-bc04-870fa885b578</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:stateProvince</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Multiple values in the dwc:stateProvince field (whether to signify on a border or in a list of possibilities) will fail this Test. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:stateProvince="Florida": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:stateProvince found in bdq:sourceAuthority"],[dwc:stateProvince="Taswegian": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:stateProvince not found in bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush geo_ref_qc Library (Morris & Lowery 2025b)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/geo_ref_qc/blob/v2.0.1/src/main/java/org/filteredpush/qc/georeference/DwCGeoRefDQ.java#L2802</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/199</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation SPACE CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>41461142-2c1e-4fc1-bc97-f83a7b2a893d</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_STATEPROVINCE_FOUND with Specification for: VALIDATION_STATEPROVINCE_FOUND</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_STATEPROVINCE_FOUND</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_14da5b87-8304-4b2b-911d-117e3c29e890"></a>Term Name  bdqtest:14da5b87-8304-4b2b-911d-117e3c29e890</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:taxonRank Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/14da5b87-8304-4b2b-911d-117e3c29e890</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/14da5b87-8304-4b2b-911d-117e3c29e890-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:taxonRank?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:taxonRank is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c619ec9b-92ec-4047-a8d3-931e3324bf3e</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonRank="genus": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:taxonRank is bdq:NotEmpty"],[dwc:taxonRank=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:taxonRank is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L2127</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/161</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_TAXONRANK_NOTEMPTY with Specification for: VALIDATION_TAXONRANK_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXONRANK_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_7bdb13a4-8a51-4ee5-be7f-20693fdb183e"></a>Term Name  bdqtest:7bdb13a4-8a51-4ee5-be7f-20693fdb183e</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:taxonRank Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/7bdb13a4-8a51-4ee5-be7f-20693fdb183e</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/7bdb13a4-8a51-4ee5-be7f-20693fdb183e-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:taxonRank occur in the bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; COMPLIANT if the value of dwc:taxonRank is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:c8964200-630e-47c6-baad-7e334fddbbdb</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonRank="kingdom": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:taxonRank has an equivalent in the bdq:sourceAuthority"],[dwc:taxonRank="sp.": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:taxonRank does not have an equivalent in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L2161</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TDWG2018</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/162</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>da536dda-d467-450e-8b0a-6b6903fd1a1b</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_TAXONRANK_STANDARD with Specification for: VALIDATION_TAXONRANK_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXONRANK_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_06851339-843f-4a43-8422-4e61b9a00e75"></a>Term Name  bdqtest:06851339-843f-4a43-8422-4e61b9a00e75</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:Taxon Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/06851339-843f-4a43-8422-4e61b9a00e75</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/06851339-843f-4a43-8422-4e61b9a00e75-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in any of the terms needed to determine that the taxon exists?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if at least one term needed to determine the taxon of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:f38e3644-354d-4180-bc7c-c437cef1d606</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:taxonID,dwc:scientificNameID,dwc:acceptedNameUsageID,dwc:parentNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:scientificName,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:infragenericEpithet,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:vernacularName,dwc:cultivarEpithet</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This tests for records that have no taxonomic (NAME) information. If there is any value for any of the Information Elements, this may be useful information. See example.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:parentNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Eucalyptus gunnii", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:superfamily="", dwc:tribe="", dwc:subtribe="",dwc:family="", dwc:genus="", dwc:subgenus="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:vernacularName="" : Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="at least enough terms exist that identify that an entity exists"],[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:parentNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:superfamily="", dwc:tribe="", dwc:subtribe="",dwc:family="", dwc:genus="", dwc:subgenus="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:vernacularName="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All input fields are bdq:Empty or missing"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L1761</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>Lee Belbin</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/105</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_TAXON_NOTEMPTY with Specification for: VALIDATION_TAXON_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXON_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4c09f127-737b-4686-82a0-7c8e30841590"></a>Term Name  bdqtest:4c09f127-737b-4686-82a0-7c8e30841590</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:Taxon Unambiguous</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4c09f127-737b-4686-82a0-7c8e30841590</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4c09f127-737b-4686-82a0-7c8e30841590-2023-09-18</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Can the taxon be unambiguously resolved from bdq:sourceAuthority using the available taxon terms?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of dwc:scientificNameID, dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, dwc:cultivarEpithet are bdq:Empty; COMPLIANT if (1) dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority, or (2) dwc:scientificNameID is bdq:Empty and dwc:scientificName references a single taxon record in the bdq:sourceAuthority, or (3) if dwc:scientificName and dwc:scientificNameID are bdq:Empty and if a combination of the values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:cultivarEpithet, dwc:taxonRank, and dwc:scientificNameAuthorship can be unambiguously resolved to a unique taxon in the bdq:sourceAuthority, or (4) if ambiguity produced by multiple matches in (2) or (3) can be disambiguated to a unique Taxon using the values of dwc:tribe, dwc:subtribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID and dwc:vernacularName; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:8bd6f6de-49e4-4889-82e0-e4af093981e0</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:taxonID,dwc:scientificName,dwc:scientificNameID,dwc:acceptedNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:infragenericEpithet,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:cultivarEpithet,dwc:vernacularName,dwc:scientificNameAuthorship,dwc:taxonRank</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>There are any number of potential controlled vocabularies that might be used for this Test, including local vocabularies and taxon specific vocabularies. If dwc:scientificNameID is bdq:Empty, use dwc:scientificName and dwc:CultivarEpithet to search for a unique taxon. If dwc:scientificName is bdq:Empty, check with the terms that form atomic parts of it (dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:taxonRank, dwc:scientificNameAuthorship), and if more than one match is found, use the remaining terms to try to disambiguate to a single Taxon record. The terms dwc:subgenus, dwc:genus, dwc:family, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:scientificNameID,, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID should not be used to make a match if dwc:scientificNameID and dwc:scientificName or dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:taxonRank, dwc:scientificNameAuthorship are bdq:Empty. Note that Test VALIDATION_SCIENTIFICNAME_FOUND (4c09f127-737b-4686-82a0-7c8e30841590) is a more specific Test for a subset of Information Elements from this Test.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Triplex rosaria Perry, 1811", dwc:higherClassification="", dwc:kingdom="Animalia", dwc:phylum="mollusca", dwc:class="Gastropoda", dwc:order="", dwc:family="Muricidae", dwc:subfamily="", dwc:genus="Chicoreus", dwc:genericName="Triplex", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="rosarium", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="Perry, 1811", dwc:taxonRank="",bdq:sourceAuthority=”marinespecies.org”: Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName matched to unique taxon record in WoRMS, unique fuzzy match on name and exact match on authorship. "],[dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Graphis", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:family="", dwc:subfamily="", dwc:genus="", dwc:genericName="", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="", dwc:taxonRank="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName="Graphis" is ambiguous as could be either a lichen or a gastropod."]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Unambiguous</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush sci_name_qc Library (Morris & Dou 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/sci_name_qc/blob/v1.1.2/src/main/java/org/filteredpush/qc/sciname/DwCSciNameDQ.java#L792</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF, CRIA</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/70</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation NAME CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>1f9a778a-7949-4574-8826-55de1e4c1e32</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_TAXON_UNAMBIGUOUS with Specification for: VALIDATION_TAXON_UNAMBIGUOUS</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TAXON_UNAMBIGUOUS</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_4833a522-12eb-4fe0-b4cf-7f7a337a6048"></a>Term Name  bdqtest:4833a522-12eb-4fe0-b4cf-7f7a337a6048</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:typeStatus Standard</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/4833a522-12eb-4fe0-b4cf-7f7a337a6048</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-07</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/4833a522-12eb-4fe0-b4cf-7f7a337a6048-2024-11-11</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Does the value of dwc:typeStatus occur in bdq:sourceAuthority?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; COMPLIANT if the value of the first word in each &#124; delimited portion of dwc:typeStatus is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:e4dbf38d-bdd7-4cf7-8c60-5b3bfc6af4ff</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:typeStatus</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:sourceAuthority</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:sourceAuthority default = "GBIF TypeStatus Vocabulary" {[https://api.gbif.org/v1/vocabularies/TypeStatus]} {dwc:typeStatus vocabulary API [https://api.gbif.org/v1/vocabularies/TypeStatus/concepts]}</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:typeStatus="Holotype": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:typeStatus found in the bdq:sourceAuthority"],[dwc:typeStatus="cleptotype": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:typeStatus not found in the bdq:sourceAuthority"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush rec_occur_qc Library (Morris 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/rec_occur_qc/blob/v1.0.1/src/main/java/org/filteredpush/qc/metadata/DwCMetadataDQ.java#L2246</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>ALA, GBIF</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/285</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation OTHER CODED Test VOCABULARY Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>63b0193f-a8df-4345-8d60-caf667cd62b0</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_TYPESTATUS_STANDARD with Specification for: VALIDATION_TYPESTATUS_STANDARD</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_TYPESTATUS_STANDARD</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_ad0c8855-de69-4843-a80c-a5387d20fbc8"></a>Term Name  bdqtest:ad0c8855-de69-4843-a80c-a5387d20fbc8</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:year In Range</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/ad0c8855-de69-4843-a80c-a5387d20fbc8</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/ad0c8855-de69-4843-a80c-a5387d20fbc8-2024-08-23</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is the value of dwc:year within the Parameter range?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>INTERNAL_PREREQUISITES_NOT_MET if dwc:year is bdq:Empty or cannot be interpreted as an integer; COMPLIANT if the value of dwc:year is within the range bdq:earliestValidDate to bdq:latestValidDate inclusive; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:aee43366-0352-448a-a5ea-85ddc8605da1</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:year</td>
		</tr>
		<tr>
			<td>Parameters</td>
			<td>bdq:earliestValidDate,bdq:latestValidDate</td>
		</tr>
		<tr>
			<td>SourceAuthorities/Defaults</td>
			<td>bdq:earliestValidDate default = "1582",bdq:latestValidDate default = "{current year}"</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The results of this Test are time-dependent. Next year is not valid now. Next year it will be. This Test provides the option to designate lower and upper limits to the year. The upper limit, if not provided, should default to the year when the Test is run. This Test provides for a default earliest date (year), of 1582 by convention. That value was chosen because ISO 8601-1 asserts that "the use of proleptic Gregorian calendar dates prior are not allowed in ISO 8601-1 without prior agreement of the parties exchanging data", and Darwin Core provides no such prior agreement.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:year="1952": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:year is in RANGE"],[dwc:year="9999": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:year is not in RANGE. The value in year has not yet come to pass."]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L2277</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>VertNet</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/84</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Conformance Parameterized CORE</td>
		</tr>
		<tr>
			<td>Argument GUID</td>
			<td>9167035f-14a8-4a0f-81eb-86a5a93bf6d9,fa6e83af-40c3-4330-aca0-937fc22b3a27</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_YEAR_INRANGE with Specification for: VALIDATION_YEAR_INRANGE</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_YEAR_INRANGE</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqtest_c09ecbf9-34e3-4f3e-b74a-8796af15e59f"></a>Term Name  bdqtest:c09ecbf9-34e3-4f3e-b74a-8796af15e59f</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Label</td>
			<td>VALIDATION_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Preferred Label</td>
			<td>Validation dwc:year Not Empty</td>
		</tr>
		<tr>
			<td>Term IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/c09ecbf9-34e3-4f3e-b74a-8796af15e59f</td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-03-06</td>
		</tr>
		<tr>
			<td>Term Version IRI</td>
			<td>https://rs.tdwg.org/bdqtest/terms/version/c09ecbf9-34e3-4f3e-b74a-8796af15e59f-2023-09-17</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Is there a value in dwc:year?</td>
		</tr>
		<tr>
			<td>Expected Response</td>
			<td>COMPLIANT if dwc:year is bdq:NotEmpty; otherwise NOT_COMPLIANT</td>
		</tr>
		<tr>
			<td>Specification GUID</td>
			<td>urn:uuid:42f331f4-a5a8-48b4-a08e-57048d1d1a77</td>
		</tr>
		<tr>
			<td>InformationElements ActedUpon</td>
			<td>dwc:year</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>[dwc:year="1949": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:year is bdq:NotEmpty"],[dwc:year="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:year is bdq:Empty"]</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Validation</td>
		</tr>
		<tr>
			<td>Resource Type</td>
			<td>SingleRecord</td>
		</tr>
		<tr>
			<td>Data Quality Dimension</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Criterion</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Example Implementations</td>
			<td>Kurator/FilteredPush event_date_qc Library (Morris & Lowery 2025)</td>
		</tr>
		<tr>
			<td>Example Implementation Source Code</td>
			<td>https://github.com/FilteredPush/event_date_qc/blob/v3.0.5/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L231</td>
		</tr>
		<tr>
			<td>Source</td>
			<td>TG2-Gainesville</td>
		</tr>
		<tr>
			<td>Developed As GitHub Issue</td>
			<td>https://github.com/tdwg/bdq/issues/49</td>
		</tr>
		<tr>
			<td>GitHub Issue Labels</td>
			<td>TG2 Validation TIME CODED Test Completeness CORE</td>
		</tr>
		<tr>
			<td>ValidationMethod label</td>
			<td>ValidationMethod: VALIDATION_YEAR_NOTEMPTY with Specification for: VALIDATION_YEAR_NOTEMPTY</td>
		</tr>
		<tr>
			<td>Specification label</td>
			<td>Specification for: VALIDATION_YEAR_NOTEMPTY</td>
		</tr>
	</tbody>
</table>
<br>
<a href='#3-Term-Indices'>[🠱]</a>

## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../../index.md#5-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## References (non-normative)

The references for the BDQ standard can be found in the [References (non-normative)](../../../index.md#7-references-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Tests and Assertions List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqtest/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
