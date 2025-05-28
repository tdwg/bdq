<!--- layout: home --->
# The Biodiversity Data Quality (BDQ) Standard
<!--- {:.lead} --->

**Title**<br>
The Biodiversity Data Quality (BDQ) Standard

**Permanent IRI (for citations and links)**<br>
[https://www.tdwg.org/standards/bdq](https://www.tdwg.org/standards/bdq)

**Publisher**<br>
[Biodiversity Information Standards (TDWG)](https://www.tdwg.org/)

**Status**<br>
Draft Standard for Review

**Category**<br>
Technical Specification

**Abstract**<br>
**Biodiversity Data Quality (BDQ)** is a standard maintained by the Biodiversity Data Quality Maintenance Interest Group (to be constituted) and designed to facilitate the consistent development and use of a set of biodiversity data quality tests and assertions. The standard consists of vocabularies needed to define the tests, a guide to support the implementation of tests, a guide to support the interpretation of outputs of implemented tests, example data, and expected responses from tests against the example data to support the validation of implemented tests.

**Preferred Citation**<br>
Biodiversity Data Quality Maintenance Group. 2025. The Biodiversity Data Quality (BDQ) Standard. https://www.tdwg.org/standards/bdq

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://www.tdwg.org/standards/to_be_determined>

<!--
**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}
-->

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)),
[Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)),
[John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

# Table of Contents
[1. Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
  - [1.4. Status of the Content of This Document (normative)](#14-status-of-the-content-of-this-document-normative)
  - [1.5 RFC 2119 key words (normative)](#15-rfc-2119-key-words-normative)
  - [1.6 Namespace Abbreviations (non-normative)](#16-namespace-abbreviations-non-normative)
  - [1.7 Referring to Terms (normative)](#17-referring-to-terms-normative)
  
[2. Parts of the Standard (non-normative)](#2-parts-of-the-standard-non-normative)
  - [2.1 BDQ Tests Quick Reference Guide (non-normative)](#21-quick-reference-guide-non-normative)
  - [2.2 Landing Pages (non-normative)](#22-landing-pages-non-normative)
  - [2.3 Guides (non-normative)](#23-guides-non-normative)
  - [2.4 Vocabularies (non-normative)](#24-vocabularies-non-normative)
    - [2.4.1 Foundational Vocabularies (non-normative)](#241-foundational-vocabularies-non-normative)
    - [2.4.2 Supporting Vocabularies (non-normative)](#242-supporting-vocabularies-non-normative)
  - [2.5 Supplemental Information (non-normative)](#25-supplemental-information-non-normative)
  - [2.6 Distribution Files (non-normative)](#26-distribution-files-non-normative)
    - [2.6.1 Tests (non-normative)](#261-tests-non-normative)
    - [2.6.2 Test Validation Data (non-normative)](#262-test-validation-data-non-normative)
    - [2.6.3 Fitness For Use Framework (non-normative)](#263-fitness-for-use-framework-non-normative)
    - [2.6.4 RDF Serializations of Controlled Vocabularies (non-normative)](#264-rdf-serializations-of-controlled-vocabularies-non-normative)
    - [2.6.5 Java Implementation (non-normative)](#265-java-implementation-non-normative)

[3. Design of the Tests (normative)](#3-design-of-the-tests-normative)
  - [3.1 Data Quality Control, Data Quality Assurance (normative)](#31-data-quality-control-data-quality-assurance-normative)
  - [3.2 When to Run Tests (normative)](#32-when-to-run-tests-normative)
  - [3.3 Results of Test Executions (normative)](#33-results-of-test-executions-normative)
  - [3.4 Test Execution Environments and Workflows (non-normative)](#34-test-execution-environments-and-workflows-non-normative)
  
[4. Contributions and Acknowledgments (non-normative)](#4-contributions-and-acknowledgments-non-normative)<br>
[5. Acronyms (non-normative)](#5-acronyms-non-normative)<br>
[6. Glossary (non-normative)](#6-glossary-non-normative)
  - [6.1 Term-Actions (non-normative)](#61-term-actions-non-normative)
  - [6.2 General Glossary (non-normative)](#62-general-glossary-non-normative)
  
[7. References (non-normative)](#7-references-non-normative)<br>
[8. Cite BDQ (non-normative)](#8-cite-bdq-non-normative)

## 1. Introduction (non_normative)

### 1.1 Purpose (non_normative)

Beyond data availability, data quality is probably the most significant issue for users of biodiversity data. Data quality is treated as fitness for a particular use, not as an inherent characteristic of data as described in detail in [3. Context for Quality, Uses and Purposes](docs/guide/users/index.md#3-context-for-quality-uses-and-purposes-non-normative) in the [BDQ User's Guide](docs/guide/users/index.md). The Biodiversity Data Quality (BDQ) standard is meant to provide a modular, extensible framework for assessing the quality of biodiversity data relative to specific uses.

### 1.2 Audience (non_normative)

Intended for:
- Practitioners and data curators
- Software developers implementing Tests
- Researchers evaluating dataset suitability
- Standards developers aligning their work with the BDQ standard
- Data managers interpreting outputs of Test runs

No technical background in ontology is required.

### 1.3 Associated Documents (non_normative)

See all documents listed in [2. Parts of the Standard (non-normative)](#2-parts-of-the-standard-non-normative).

### 1.4 Status of the Content of This Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

### 1.5 RFC 2119 key words (normative)
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html).

### 1.6 Namespace Abbreviations (non_normative)

| Abbreviation | Namespace |
|--------------|-----------|
| bdq:         | https://rs.tdwg.org/bdq/terms/ |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/ |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/ |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/ |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms/ |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/ |
| oa:          | https://www.w3.org/TR/annotation-vocab/ |
| dwc:         | http://rs.tdwg.org/dwc/terms/ |

### 1.7 Referring to Terms (normative)
In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., 'https://rs.tdwg.org/bdqffdq/terms' for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (skos:prefLabel, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. You will find all of these methods of referring to BDQ-related terms throughout the BDQ documentation.

## 2. Parts of the Standard (non-normative)
This standard is comprised of the following documents and artifacts:

### 2.1 BDQ Tests Quick Reference Guide (non-normative)

The Quick Reference Guide is a simple, informative reference and the first place to look for the most commonly used information about the Tests.

[**BDQ Tests Quick Reference Guide**](docs/terms/bdqtest/index.md)

### 2.2 Landing Pages (non-normative)

The landing pages provide overviews of the subjects they cover and refer to more detailed information in associated documents. The details of the individual terms are provided in the corresponding term list documents. The controlled vocabulary term list documents also act as the landing pages for those vocabularies.

- **The Biodiversity Data Quality (BDQ) Standard** - Overview of the BDQ standard. This page.
- [**BDQ Tests and Assertions**](docs/bdqtest/index.md) - Overview of the Tests.
- [**Fitness For Use Ontology**](docs/bdqffdq/index.md) - Overview of the Fitness for Use Framework.
- [**BDQ Controlled Vocabulary List of Terms (bdq:)**](docs/list/bdq/index.md) (will be: https://bdq.tdwg.org/bdq)
- [**Data Quality Criterion Controlled Vocabulary List of Terms (bdqcrit:)**](docs/list/bdqcrit/index.md) (will be: https://bdq.tdwg.org/bdqcrit)
- [**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.md) (will be: https://bdq.tdwg.org/bdqdim)
- [**Data Quality Enhancement Controlled Vocabulary List of Terms (bdqenh:)**](docs/list/bdqdim/index.md) (will be: https://bdq.tdwg.org/bdqenh)

### 2.3 Guides (non-normative)

The Guides are explanatory documents targeting particular perspectives on the standard for particular audiences.

- [**BDQ User's Guide**](docs/guide/users/index.md)
- [**BDQ Implementer's Guide**](docs/guide/implementers/index.md)
- [**Guide to Marking and Identifying Synthetic and Modified Data**](docs/guide/synthetic/index.md)
- [**Fitness For Use Framework Ontology Guide**](docs/guide/bdqffdq/index.md)

### 2.4 Vocabularies (non-normative)
#### 2.4.1 Foundational Vocabularies (non-normative)

The Foundational Vocabularies cover the two main parts of the standard - the practical (the Tests) and the theoretical (the Framework).

- [**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.md) - The definitions of terms in the bdqffdq: vocabulary.
- [**Fitness For Use Framework Ontology Vocabulary Extension**](docs/extension/bdqffdq/index.md) - The axioms that extend the logic of the basic the bdqffdq: vocabulary.
- [**BDQ Tests and Assertions List of Terms (bdqtest:)**](docs/list/bdqtest/index.md) - The complete list of terms that define the BDQ Tests.

#### 2.4.2 Supporting Vocabularies (non-normative)

The Supporting Vocabularies are controlled vocabularies used in the technical definitions of the Tests.

- [**BDQ Controlled Vocabulary List of Terms (bdq:)**](docs/list/bdq/index.md)
- [**Data Quality Criterion Controlled Vocabulary List of Terms (bdqcrit:)**](docs/list/bdqcrit/index.md)
- [**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.md)
- [**Data Quality Enhancement Controlled Vocabulary List of Terms (bdqenh:)**](docs/list/bdqenh/index.md)

### 2.5 Supplemental Information (non-normative)

Supplemental Information includes the rationale for, the history of, and the challenges met while describing the Tests.

- [**BDQ Supplemental Information**](docs/supplement/index.md)

### 2.6 Distribution Files (non-normative)

#### 2.6.1 Tests (non-normative)

The Test definitions are provided in various serializations. Of these, the bdqtest_term_versions.csv is the canonical archive of all Tests versions, both recommended and historical. The documentation about the details of Tests for this standard are generated from this file.  CSV files listing just the current test versions are also provided,

- [**CSV List of all Tests (bdqtest_term_versions.csv)**](vocabulary/bdqtest_term_versions.csv)
- [**CSV List of (current) Single Record Tests**](dist/bdqtest_singlerecord_tests_current.csv)
- [**CSV List of (current) Multi Record Tests**](dist/bdqtest_multirecord_tests_current.csv)
- [**Tests in RDF/XML**](dist/bdqtest.xml)
- [**Tests in Turtle**](dist/bdqtest.ttl)
- [**Tests in JSON-LD**](dist/bdqtest.json)

#### 2.6.2 Test Validation Data (non-normative)

Test Validation Data are intended for implementers to use to evaluate whether Test Implementations produce the Expected Responses.

- [**Test Validation Data**](docs/guide/implementers/TG2_test_validation_data.csv)
- [**Test Validation Data for non-printing characters**](docs/guide/implementers/TG2_test_validation_data_nonprintingchars.csv)

#### 2.6.3 Fitness For Use Framework (non-normative)

The Fittness For Use Framework is provided as an OWL ontology.

- [**Biodiversity Data Quality Fitness for Use Framework (Ontology)**](vocabulary/bdqffdq.owl)

#### 2.6.4 RDF Serializations of Controlled Vocabularies (non-normative)

- [**RDF/XML serialization of the bdq: terms**](dist/bdq.xml)
- [**RDF/XML serialization of the bdqcrit: terms**](dist/bdqcrit.xml)
- [**RDF/XML serialization of the bdqdim: terms**](dist/bdqdim.xml)
- [**RDF/XML serialization of the bdqenh: terms**](dist/bdqenh.xml)

#### 2.6.5 Java Implementation (non-normative)

While not part of the BDQ standard, a validated Java® implementation of the tests is provided in the [event_date_qc](https://github.com/FilteredPush/event_date_qc), [sci_name_qc](https://github.com/FilteredPush/sci_name_qc), [geo_ref_qc](https://github.com/FilteredPush/geo_ref_qc) and [rec_occur_qc](https://github.com/FilteredPush/rec_occur_qc) libraries.  Also see [bdqtestrunner](https://github.com/FilteredPush/bdqtestrunner/), which demonstrates conformance of these libraries with the provided [Test Validation Data](#262-test-validation-data-non-normative).      

## 3 Design of the Tests (normative)

### 3.1 Data Quality Control, Data Quality Assurance (normative)

The BDQ standard draws a distinction between Quality Control and Quality Assurance. Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data. Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose. Implementations of the BDQ Tests MAY be used to perform Quality Control, Quality Assurance, or both. The [mathematical formalization](docs/bdqffdq/index.md#3-fitness-for-use-framework-summary-of-mathematical-formalization-normative) of the [Fitness for Use Ontology](docs/bdqffdq/index.md) provides a formal definition of Quality Control and Quality Assurance, and how Test Assertions SHOULD be used for each.

### 3.2 When to Run Tests (normative)

The BDQ Tests are designed to be run at any point in the life cycle of biodiversity data. They MAY be run at the point of initial collection or observation of organisms. They MAY be run to support data transcription. They MAY be run in loading data into databases of record from field or transcription sources. They MAY be run in preparing data from databases of record for aggregation. They MAY be run during data aggregation and the presentation of aggregated data. They MAY be run in workflows for analysis of data for research purposes.

### 3.3 Results of Test Executions (normative)

The BDQ standard is agnostic about the format of presentation of results from BDQ Tests. BDQ does, however, specify that Test implementations and presentations MUST return structured data with at least bdq:Response.status, bdq:Response.result, and bdq:Response.comment. Responses MAY also contain more information in Response.qualifier.
See the [Implementer's Guide](docs/guide/implementers/index.md) section on [Presentation of Results](docs/guide/implementers/index.md#7-presentation-of-results-normative) for further normative and non-normative guidance about result presentation. See [Structure of a Response](docs/bdqtest/index.md#31-structure-of-response-normative) in the [BDQ Tests and Assertions](docs/bdqtest/index.md) document for normative guidance on Responses as RDF or as data structures.

The results of the execution of implementations of the BDQ Tests MAY be presented as Data Quality reports. The Framework Ontology provides vocabulary and structure that MAY be used for such data quality reports.

The bdqffdq: vocabulary enables the wrapping of the results of BDQ Tests within annotations. The bdqffdq: vocabularies in particular are intended to support the framing of Assertions from Tests within annotations that follow the W3C Web Annotation Data Model (Sanderson et al. 2017), and are suitable for inclusion in semantic data stores. See the [Implementer's Guide](docs/guide/implementers/index.md) section on [Annotations](docs/guide/implementers/index.md#72-annotations-normative) for more guidance.

### 3.4 Test Execution Environments and Workflows (non-normative)

Neither the Test descriptions nor the framework impose constraints on environments or workflows for execution. One possible workflow is to run all validations, then all amendments, then all validations again on a modified copy of the input data to which all proposed amendments have been applied.

A single validation step, with measures evaluating the results of the amendments could look like the diagram below.

![Diagram of workflow through single validation step](workflow_single_iteration.svg)

Expanding on this single validation step, amendments can be run and their results fed back into a second phase of post-amendment validation, with measures again evaluating the results of validation of the input data if all changes proposed by amendments are accepted. Presentation of a data quality report would be an expected result from this workflow for Quality Control purposes, while using the Measures in the second step to filter data in a processing pipeline to just those that are fit for purpose for a particular use would be expected for Quality Assurance purposes.

![Diagram of workflow with pre-amendment validation+measure phase, followed by amendment phase, followed by post-amendment validation-measure phase](workflow_two_iterations.svg)

## 4 Acknowledgments and Contributions (non-normative)

### 4.1 Acknowledgments (non-normative)

The Authors gratefully acknowledge all those who have commented on the GitHub issues during the development of the BDQ standard, and all those who have contributed to discussions at various workshops in São Paulo, Brazil; Canberra, Australia; Monash, Australia; Leiden, The Netherlands; Gainesville, USA; and Seattle, USA, and at Biodiversity Information Standards (TDWG) annual meetings (in Jönköping, Sweden; Santa Clara de San Carlos, Costa Rica; Ottawa, Canada; Dunedin, New Zealand; Leiden, The Netherlands; Sofia, Bulgaria; Hobart, Australia; and Ginowa, Japan; and the various virtual meetings). The Authors are also grateful for all those who responded to our email questions.

We'd also gratefully acknowledge the continued support of the Biodiversity Information Standards (TDWG) Executive over the 10 years of this project.

#### 4.1.1 Funding and Support for Meetings (non-normative)

We acknowledge the financial support of The Atlas of Living Australia and Biodiversity Information Standards (TDWG) for Lee Belbin and Arthur Chapman to attend two face-to-face meetings for the development of the BDQ standard, and the Atlas of Living Australia for support of John Wieczorek to attend meetings in Canberra Australia. The Museum of Comparative Zoology provided support for Paul Morris; VertNet, Kurator, and Rauthflor LLC provided support for John Wieczorek. The United States National Science Foundation through funding of the Kurator project, provided time for Paul Morris, Robert Morris and David Lowery for early work on the project.

The São Paulo Research Foundation (FAPESP), the Universidade de São Paulo (USP) provided facilities, and with the Global Biodiversity Information Facility and others, supported participants to attend the meeting in São Paulo, Brazil. The US National Science Foundation through iDigBio provided support for the meeting in Gainesville, Florida.

### 4.2 Contributions (non-normative)

#### 4.2.1 Authors (non-normative)

We recognize four people as authors of the standard, having contributed consistently over the last decade and having been heavily engaged in writing the BDQ Test Descriptions and the documentation for the BDQ standard.

- **Lee Belbin (Blatant Fabrications Pty Ltd)**: Convener of TDWG Data Quality Task Group 2 (Data Quality Tests and Assertions); Test descriptions; author of the BDQ standard documents; Test Validation Data.
- **Arthur D Chapman (Australian Biodiversity Information Services)**: Co-convener of the TDWG Data Quality Interest Group; Test descriptions; author of the BDQ standard documents; vocabularies. 
- **Paul J Morris (Museum of Comparative Zoology, Harvard University)**: Test descriptions; Fitness For Use Framework ontology; Java Test implementations in filteredpush packages; author of the BDQ standard documents; Test Validation Data. 
- **John Wieczorek (Rauthiflor LLC)**: Test descriptions; Test implementations; author of the BDQ standard documents; Darwin Core liaison.

#### 4.2.2 Contributors (non-normative)

There were many people who have made notable contributions at various times during the development of the BDQ standard.
 
- **Paula F. Zermoglio (Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN), San Carlos de Bariloche)**: Convener of TDWG Data Quality Task Group 4 (Best Practices for Development of Vocabularies of Value); Test descriptions; vocabulary development.
- **Alexander Thompson (iDigBio)**: Key contributions to initial development of Test descriptions; migrated Test descriptions into Markdown tables in GitHub issues.
- **Yi-Ming Gan (Royal Belgian Institute of Natural Sciences)**: Contributed to Test evaluation; explanatory workflow diagrams; editing the documents of the BDQ standard.
- **António Mauro Saraiva (Universidade de São Paulo)**: Co-convenor of the TDWG Data Quality Interest Group; development of the Framework for Data Quality (TDWG Data Quality Task Group 1); facilitated Test development workshop.
- **Allan Koch Veiga (Universidade de São Paulo)**: Developed the Framework on Data Quality as his doctoral dissertation (Veiga 2016), Convener of the TDWG Data Quality Task Group 1 (Framework for Data Quality).
- **David Lowery (Museum of Comparative Zoology, Harvard University)**: Initial development of ontology representation of Framework on Data Quality; developer of kurator-ffdq Java class representation of the Framework.
- **Christian Gendreau (Agriculture and Agri-Food Canada)**: Initial contributions to data quality discussions; vocabulary definitions and early Test development.
- **Tim Robertson (Global Biodiversity Information Facility)**: Contributions to Test descriptions; clarification of GBIF vocabulary and API resources for the BDQ Tests.
- **Dmitry Schigel (Global Biodiversity Information Facility)**: Initial contributions to data quality discussions and vocabulary definitions; GBIF Representative to the Data Quality Interest Group in early years.
- **Robert A. Morris (late, of UMass Boston)**: Competency questions for the ontology of the Data Quality Framework; guided initial development of the ontology representation of the Framework.
- **Miles Nicholls (Atlas of Living Australia)**: Convener of TDWG Data Quality Task Group 3 (Data Quality Use Cases); Use Case analysis.
- **Emily Rose Rees (Atlas of Living Australia)**: Use Case analysis in TDWG Data Quality Task Group 3 (Data Quality Use Cases).
- **Abigail Benson (U.S. Geological Survey)**: Initial contributions to data quality discussions and vocabulary definitions.

## 5 Acronyms (non-normative)

| **Acronym** | **Explanation** |
|-------------|-----------------|
| ALA         | [Atlas of Living Australia](https://ala.org.au) | 
| BDQ         | [TDWG Biodiversity Data Quality](https://github.com/tdwg/bdq) |
| BISON       | Biodiversity Information Serving Our Nation |
| CRIA        | [Centro de Referência em Informação Ambiental](https://www.cria.org.br/) |
| EPSG        | [European Petroleum Survey Group](https://epsg.org/home.html) |
| GBIF        | [Global Biodiversity Information Facility](https://gbif.org) |
| iDigBio     | [Integrated Digitized BioCollections](https://www.idigbio.org/) |
| IRI         | [Internationalized Resource Identifier](https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier) |
| ISO         | [International Standards Organization](https://www.iso.org/home.html) |
| QA          | [Quality Assurance](docs/bdqffdq/index.md#3447-quality-assurance-normative) |
| QC          | [Quality Control](docs/bdqffdq/index.md#3446-quality-control-normative) |
| SDS         | [TDWG Standards Documentation Standard](https://www.tdwg.org/standards/sds/) |
| TDWG        | [Biodiversity Information Standards](https://tdwg.org) |
| TG1         | [Biodiversity Data Quality Interest Group - Task Group 1: Framework on Data Quality](https://github.com/tdwg/bdq/tree/master/tg1) |
| TG2         | [Biodiversity Data Quality Interest Group - Task Group 2: Data Quality Tests and Assertions](https://github.com/tdwg/bdq/tree/master/tg2) |
| TG3         | [Biodiversity Data Quality Interest Group - Task Group 3: Data Quality Use Cases](https://github.com/tdwg/bdq/tree/master/tg3) |
| TG4         | [Biodiversity Data Quality Interest Group - Task Group 4: Best Practices for Development of Vocabularies of Values](https://github.com/tdwg/bdq/tree/master/tg4) |

## 6 Glossary (non-normative)

### 6.1 Term-Actions

A Test label reflects its Test type, the `bdqffdq:InformationElement` the Test acts upon, and the nature of the evaluation that is being done. The Test type is one of `Validation`, `Issue`, `Measure` or `Amendment`. The term-action is the combination of the `bdqffdq:InformationElement` and the nature of the evaluation. For example, the Test with the label "VALIDATION_COUNTRYCODE_STANDARD" has the type `Validation`, the `bdqffdq:InformationElement` `dwc:countryCode` and the nature of the evaluation "STANDARD". Following is a table of distinct values for the nature of the evaluation part of the term-action, along with a definition and a usage comment with examples.

| Label | Comment | Example |
| ----- | ------- | ------- |
| ASSUMEDDEFAULT | A bdqffdq:Amendment that replaces a bdq:EMPTY term with a predefined default bdq:Parameter value. | [AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](docs/terms/bdqtest/index.md#AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT) |
| CENTREOFCOUNTRY | Testing if bdqffdq:EnformationElements COORDINATES identify the center of the dwc:country, allowing for a spatial buffer. | [ISSUE_COORDINATES_CENTEROFCOUNTRY](docs/terms/bdqtest/index.md#ISSUE_COORDINATES_CENTEROFCOUNTRY) |
| COMPLETE | Testing if the bdqffdq:InformationElement dwc:scientificNameId forms a valid and complete identifier. | [VALIDATION_SCIENTIFICNAMEID_COMPLETE](docs/terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_COMPLETE) |
| CONSISTENT | Identifies consistency among values between bdqffdq:InformationElements. | [VALIDATION_CLASSIFICATION_CONSISTENT](docs/terms/bdqtest/index.md#VALIDATION_CLASSIFICATION_CONSISTENT) |
| COORDINATESTERRESTRIALMARINE | A terrestrial taxon that has geographic coordinates that fall within terrestrial boundaries, or a marine taxon that has geographic coordinates that fall within marine boundaries. | [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](docs/terms/bdqtest/index.md#VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT) |
| DURATIONINSECONDS | The duration in seconds of the bdq:InformationElement dwc:eventDate. | | [MEASURE_EVENTDATE_DURATIONINSECONDS](docs/terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS) |
| FOUND | The value in a bdqffdq:InformationElement that matched a value in a bdq:sourceAuthority. | [VALIDATION_STATEPROVINCE_FOUND](docs/terms/bdqtest/index.md#VALIDATION_STATEPROVINCE_FOUND) |
| FROM | An Output bdqffdq:InformationElement is being populated from a more primary Input bdqffdq:InformationElement. | [AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](docs/terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID) |
| INRANGE | The value of bdqffdq:InformationElements that are within an acceptable range. | [VALIDATION_MAXDEPTH_INRANGE](docs/terms/bdqtest/index.md#VALIDATION_MAXDEPTH_INRANGE) |
| LESSTHAN | A Term-Action indicating that the value in one bdq:InformationElement is less than the value in another bdq:InformationElement. | [VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH](docs/terms/bdqtest/index.md#VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH) |
| NOTEMPTY | An bdqffdq:InformationElement contains a value that is bdq:NotEmpty. | | [VALIDATION_EVENTDATE_NOTEMPTY](docs/terms/bdqtest/index.md#VALIDATION_EVENTDATE_NOTEMPTY) |
| PREREQUISITESNOTMET | A Test of type bdqffdq:Measure that counts the number of Tests of type bdqffdq:Validation that did not run due to one or more prerequisites not being met (bdq:INTERNAL_PREREQUISITES_NOT_MET or EXTERNAL_PREREQUISITES_NOT_MET). | | [MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](docs/terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET) |
| PROPOSED | A Test of type bdqffdq:Measure that counts the number of bdqffdq:Amendments where an action to modify a value in some way through a change or addition is proposed. | | [MEASURE_AMENDMENTS_PROPOSED](docs/terms/bdqtest/index.md#MEASURE_AMENDMENTS_PROPOSED) |
| STANDARD | A bdqffdq:Validation Test where a value in a bdqffdq:InformationElement matches a bdq:STANDARD value in a bdq:sourceAuthority. | [VALIDATION_TAXONRANK_STANDARD](docs/terms/bdqtest/index.md#VALIDATION_TAXONRANK_STANDARD) |
| STANDARDIZED | A bdqffdq:Amendment where a bdq:STANDARD value for a bdqffdq:InformationElement is proposed. | [AMENDMENT_TAXONRANK_STANDARDIZED](docs/terms/bdqtest/index.md#AMENDMENT_TAXONRANK_STANDARDIZED) |
| TRANSPOSED | A bdqffdq:Amendment where the sign and/or value of one or more bdqffdq:InformationElements were proposed to be swapped. | [AMENDMENT_COORDINATES_TRANSPOSED](docs/terms/bdqtest/index.md#AMENDMENT_COORDINATES_TRANSPOSED) |
| UNAMBIGUOUS | A combination of bdqffdq:InformationElements is unambiguous in that they align to a unique result given a reference or a Source Authority (bdq:sourceAuthority). | | [VALIDATION_TAXON_UNAMBIGUOUS](docs/terms/bdqtest/index.md#VALIDATION_TAXON_UNAMBIGUOUS) |
| VERBATIM | Refers to bdqffdq:Amendment Tests that attempt to extract explicit Darwin Core bdq:InformationElements values from Darwin Core verbatim term bdq:InformationElements. | | [AMENDMENT_EVENTDATE_FROM_VERBATIM](docs/terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_VERBATIM) |

### 6.2 General Glossary (non-normative)

Glossary of terms used in the BDQ standard that are in addition to those included in the various Namespace: vocabularies and Term-Actions. Note: Usage of 'Darwin Core term(s)' below refer to [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021).

| Label | Definition | Context |
| ---- | ---- | ---- |
| Actual Parameter | The value that is provided when a function or method is called. Actual parameters are the real data that are passed to a function to replace the formal parameters. In the function f(x) = x^2, x is a formal parameter that can be replaced by the actual parameter value 4, and thus be evaluated as f(4) = 4^2 = 16. In VALIDATION_GENUS_FOUND, the formal parameter bdq:sourceAuthority may take the actual parameter "GBIF Backbone Taxonomy". | bdqffdq: |
| COORDINATES | A general category of specific bdq:InformationElements that represents the combination of the Darwin Core terms dwc:decimalLatitude and dwc:decimalLongitude and may include metadata terms including dwc:geodeticDatum. | bdqffdq:InformationElement |
| CRS | Coordinate Reference System - (also referred to as 'spatial reference system'). A coordinate system defined in relation to a standard reference or datum (Chapman & Wieczorek 2020). | Test |
| Database of record | An information system which holds an authoritative or master record of some data. Records in a database of record are held to be correct over different values for the same records that might be found in other datasets. This is in distinction from aggregated datasets, derived research dataset, datasets for portals and other holders of non-authoritative copies of the data. | BDQ standard |
| geodetic coordinate reference system | A coordinate reference system based on a geodetic datum, used to describe positions on the surface of the earth (Chapman and Wieczorek 2020). | Test |
| geodetic datum | A mathematical model that uses a reference ellipsoid to describe the size and shape of the surface of the earth and adds to it the information needed for the origin and orientation of coordinate systems on that surface (Chapman and Wieczorek 2000). | Test |
| Formal Parameter | A placeholder defined in the function or method signature. It represents the input that the function expects. In the function f(x) = x^2, x is a formal parameter of the function f. In VALIDATION_GENUS_FOUND, bdq:sourceAuthority is a formal parameter. | bdqffdq: |
| Framework | The Fitness for Use Framework, the body of work that provides a fundamental structure for the BDQ Tests. The Fitness for Use Framework is derived from (Veiga 2016) and is the outcome of the TDWG Data Quality Task Group 1: Framework on Data Quality (Veiga et al. 2017). | bdqffdq: |
| Framework Ontology | A model of the Framework (Veiga 2016, Veiga et al. 2017) as an OWL ontology, present as the bdqffdq: vocabulary in the BDQ standard. | bdqffdq: |
| GEOGRAPHY | A general category of specific bdq:InformationElements that represents a combination of Darwin Core administrative geography terms dwc:continent, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality. | bdqffdq:InformationElement |
| Java | Java is a registered trademark of Oracle and/or its affiliates. | BDQ standard |
| NAME | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Taxon Class. | bdqffdq:InformationElement |
| non-printing characters | ASCII 0-32 and 127 decimal. Non-printing characters or formatting marks that are not displayed when printing. These may include pilcrow, space, non-breaking space, tab character, etc. For the purposes of the Tests they are treated as bdq:Empty. | Data |
| null | A value that is used in some databases to signify that a value is unknown or missing. It may be represented in serializations of data outside of database environments by strings such as "NULL", "Null", "null". "/n", "9999", "NA", etc. These serializations should be treated as bdq:NotEmpty. | Data |
| OTHER | A bdq GitHub label to indicate that the Test is related to Darwin Core terms other than Classes dwc:Taxon, dwc:Location or dwc:Event. | bdqffdq:InformationElement |
| POLYNOMIAL | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet. See the Test [VALIDATION_POLYNOMIAL_CONSISTENT](docs/terms/bdqtest/index.md#VALIDATION_POLYNOMIAL_CONSISTENT). | bdqffdq:InformationElement |
| Roman numerals | Numbers written with the characters I, V, X, L, C, D, and M in the latin alphabet, each letter representing an integer and combined to form arbitrary integers. Roman numerals are interpreted as the equivalent integer for months (e.g., "X" as "10") in certain Tests. Roman numerals may not be unambiguously interpreted for other Darwin Core terms such as dwc:day or in text fields as they may mean unknown or something else entirely. | Data | 
| SPACE | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Location Class. | bdqffdq:InformationElement |
| SRS | spatial reference system - see CRS (Chapman and Wieczorek 2020). | Test |
| Test | An individual consideration of a DataQualityNeed with a Method that links it to an instance of a Specification, these instances being composed of InformationElements, Arguments, and Parameters. | BDQ standard | 
| Test (technical) | A composition of an instance of a subclass of bdqffdq:DataQualityNeed (which expresses a data quality need in the abstract) with an instance of a subclass of bdqffdq:DataQualityMethod, which links it to an instance of a bdqffdq:Specification (which spells out how to concretely evaluate the need). These class instances are composed with bdqffdq:InformationElements, bdqffdq:Arguments, and bdqffdq:Parameters. For example, the Test [VALIDATION_COUNTRY_FOUND](docs/terms/bdqtest/index.md#VALIDATION_COUNTRY_FOUND).| BDQ standard | 
| TestField | Column heading in the Markdown of the Tests in the [tdwg/bdq GitHub](https://github.com/tdwg/bdq/issues) that list all the normative and informative metadata elements that describe a Data Quality Test. | Test |
| Test Type | There are four types of Tests: Validation (bdqffdq:Validation), Amendment (bdqffdq:Amendment), Issue (bdqffdq:Issue), and Measure (bdqffdq:Measure). | Test |
| TIME | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Event Class. | bdqffdq:InformationElement |
| VERBATIM | A general category of specific bdq:InformationElements that represents a term containing an original value. | bdqffdq:InformationElement |
| whitespace | Characters such as spaces and tabs that affect rendering of printed or displayed output, but which themselves are not printed. 1) A field that only includes whitespace is treated as bdq:Empty. 2) In bdqffdq:Validation Tests that require the look up of a bdq:sourceAuthority, leading and/or trailing whitespace will cause the Test to fail as no pre-processing is carried out on the data. These leading and trailing whitespaces may be stripped out in a subsequent bdqffdq:Amendment and thus pass when the bdqffdq:Validation Test is run again. | Data |
| YEARMONTHDAY | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:month, dwc:day. | bdqffdq:InformationElement |
| YEARSTARTDAYOFYEARENDDAYOFYEAR | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:startDayOfYear, dwc:endDayofYear. | bdqffdq:InformationElement |

## 7. References (non-normative)

We have used the formatting recommended by Pensoft, see https://checklist.pensoft.net/about#AuthorsGuidelines. 

<ul>
<li>ALA (2013) Data Processing. https://www.ala.org.au/blogs-news/data-processing/</li>
<li>ALA (2020) Locations - Species distributions as areas. https://support.ala.org.au/support/solutions/articles/6000234834-locations-species-distributions-as-areas</li>
<li>Belbin L, Daly J, Hirsch T, Hobern D, Salle JL (2013) A specialist’s audit of aggregated occurrence records: An ‘aggregator’s’ perspective. ZooKeys 305: 67–76. doi: 10.3897/zookeys.305.5438</li>
<li>Biodiversity Information Standards (TDWG) (2010) TDWG GUID Applicability Statement. https://github.com/tdwg/guid-as/blob/master/guid/tdwg_guid_applicability_statement.pdf</li>
<li>Biodiversity Information Standards (TDWG) (n.dat) Annotations Interest Group. https://www.tdwg.org/community/annotations/</li>
<li>Biodiversity Information Standards (TDWG) (2021) Biodiversity Information Standards (TDWG) Standards Metadata http://rs.tdwg.org/index</li>
<li>Bradner, S (1997) IETF Key words for use in RFCs to Indicate Requirement Levels (RFC 2119). https://datatracker.ietf.org/doc/html/rfc2119</li>
<li>Chapman AD (1992) Quality control and validation of environmental resource data in Quality control and validation of environmental resource data Canberra: Commonwealth Land Information Forum pp. 1-16 [also published electronically at: https://www.researchgate.net/publication/332537824]</li> 
<li>Chapman AD (1999) Quality control and validation of point-sourced environmental resource data pp. 409-418 in Lowell, K. and Jaton, A. (eds) Spatial Accuracy Assessment: Land Information Uncertainty in Natural Resources. Chelsea, Michigan: Ann Arbor Press. 455pp</li> 
<li>Chapman AD (2005) Principles and Methods of Data Cleaning Primary Species Occurrence Data. Copenhagen: GBIF Secretariat. https://www.gbif.org/document/80528</li>
<li>Chapman AD (2020) Current Best Practices for Generalizing Sensitive Species Occurrence Data. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-5jp4-5g10</li>
<li>Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</li>
<li>Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020) Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889</li>
<li>Chapman AD, Hijmans R, Marino A, De Giovanni R and de Souza S (2006) Using the concept of “Outlierness” to identify suspect records in Primary Species Occurrence Data p. 39 in The Road to Productive Partnerships. The 21st Annual Meeting of the Society for the Preservation of Natural History Collections and the Natural Science Collections Alliance 2006 Annual Meeting. Program & Abstracts. Albuquerque, New Mexico 23-27.  May 2006. https://www.researchgate.net/publication/333198103_Using_the_concept_of_Outlierness_to_identify_suspect_records_in_Primary_Species_Occurrence_Data </li> 
<li>Creative Commons (n.dat.) About the Licenses. https://creativecommons.org/licenses/</li>
<li>Darwin Core and RDF/OWL Task Groups (2021) Darwin Core RDF guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/guides/rdf/2021-07-15</li>
<li>Darwin Core Maintenance Group (2021) Degree Of Establishment Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/doe/</li>
<li>Darwin Core Maintenance Group (2021) Establishment Means Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/em/</li>
<li>Darwin Core Maintenance Group (2021) List of Darwin Core terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/list/</li>
<li>Darwin Core Maintenance Group (2021) Pathway Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). https://dwc.tdwg.org/pw/</li> 
<li>Darwin Core Maintenance Group (2021) Preparations Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/preparations</li> 
<li>Darwin Core Maintenance Group (2021) Reproductive Condition Vocabulary List of Terms. Biodiversity Information Standards (TDWG). https://dwc.tdwg.org/list/#dwc_reproductiveCondition</li> 
<li>Darwin Core Maintenance Group (2021) Year. Biodiversity Information Standards (TDWG) http://rs.tdwg.org/dwc/terms/index.htm#year</li>
<li>DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list</li>
<li>Dooley JF Jnr. (2005) An inventory and comparison of globally consistent geospatial databases and libraries. Rome: FAO. http://www.fao.org/3/a0118e/a0118e00.htm#Contents </li>
<li>Dublin Core (2012) DCMI Type Vocabulary. https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/</li>
<li>Dublin Core (2020) DCMI Metadata Terms. https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#modified</li>
<li>Dublin Core (2020) License Document. https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/LicenseDocument/</li>
<li>EPSG (2024) About the EPSG Dataset. https://epsg.org/home.html</li>
<li>EPSG.io (2024) Transform coordinates. https://epsg.io/transform</li>
<li>ESRI (2020) World Administrative Divisions. https://www.arcgis.com/home/item.html?id=f0ceb8af000a4ffbae75d742538c548b</li> 
<li>Flanders Marine Institute (2023) Maritime Boundaries Geodatabase, version 12. Available online at https://www.marineregions.org/. https://doi.org/10.14284/628</li><li>Kelso NV and Patterson T (2010) Introducing Natural Earth data—Naturalearthdata.com. Geographica Technica. Special issue, 2010 pp 82–89. https://technicalgeography.org/pdf/sp_i_2010/12_introducing_natural_earth_data__naturaleart.pdf</li><li>Natural Earth (2022) Natural Earth Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales. v5.1.2. https://www.naturalearthdata.com/,  https://github.com/nvkelso/natural-earth-vector/releases/tag/v5.1.2.</li><li>Natural Earth (2022) Admin 1 – States, Provinces. v5.1.1 2022-05-12. https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/</li>
<li>GADM (2018) GADM Maps and Data. http://gadm.org/about.html</li>
<li>GBIF (2015) Darwin Core Vocabulary: Sex GBIF Vocabulary. https://rs.gbif.org/vocabulary/gbif/sex.xml</li>
<li>GBIF (2015) Taxonomic Rank GBIF Vocabulary. https://rs.gbif.org/vocabulary/gbif/rank.xml</li>
<li>GBIF (2021) Darwin Core Vocabulary: Nomenclatural Type Status Vocabulary. http://rs.gbif.org/vocabulary/gbif/type_status</li> 
<li>GBIF Registry (2023) GBIF Vocabulary: Taxonomic Rank. https://registry.gbif.org/vocabulary/TaxonRank/concepts</li>
<li>GBIF Secretariat (2023) GBIF Backbone Taxonomy. Checklist dataset. https://doi.org/10.15468/39omei</li>
<li>Geomatic Solutions (2018) Georepository. Version 9.0.0.1062. https://georepository.com</li> 
<li>Getty Research Institute (2017) Getty Thesaurus of Geographic Names Online. https://www.getty.edu/research/tools/vocabularies/tgn/index.html</li>
<li>Google Maps Platform (2020) Reverse Geocoding API. https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse</li>
<li>Groom Q, Desmet P, Reyserhove L, Adriaens T, Oldoni D, Vanderhoeven S, Baskauf SJ, Chapman A, McGeoch M, Walls R, Wieczorek J, Wilson JR.U, Zermoglio PFF, Simpson A (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards 3: e38084. https://doi.org/10.3897/biss.3.38084</li>
<li>ISO (2019) ISO 8601-1:2019(en) Date and time — Representations for information interchange — Part 1: Basic rules. https://www.iso.org/obp/ui/</li>
<li>ISO (n.dat) 3166 code search. https://www.iso.org/obp/ui/#search</li>
<li>ISO (n.dat) 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li>
<li>ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html</li>
<li>Kelso NV and Patterson T (2010) Introducing Natural Earth data—Naturalearthdata.com. Geographica Technica. Special issue, 2010 pp 82–89. https://technicalgeography.org/pdf/sp_i_2010/12_introducing_natural_earth_data__naturaleart.pdf</li>
<li>Kennedy M, Morris PJ, Haley B, McDonald D (2024) MCZbase/MCZbase MCZbase version as of v2024Apr04 commit 53ec47f2 [Computer Software] https://doi.org/10.5281/zenodo.10929079</li>
<li>Leiba B (2017) IETF Key words for use in RFCs to Indicate Requirement Levels (RFC 8174). https://tools.ietf.org/html/rfc8174</li>
<li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li>
<li>Lowery D, Morris PJ (2024) kurator-org/ffdq-api: Release of ffdq-api version 2.0.2 (v2.0.2). Zenodo. https://doi.org/10.5281/zenodo.14031588</li>
<li>Lowery D, Morris PJ, Morris RA (2025) kurator-org/kurator-ffdq: Release of Kurator-FFDQ library version v3.2.0 (v3.2.0). Zenodo. https://doi.org/10.5281/zenodo.15375151</li>
<li>Maptiler (2019) EPSG.io. https://epsg.io</li>
<li>Morris P, Hanken J, Lowery D, Ludäscher B, Macklin J, McPhillips T, Wieczorek J, Zhang Q (2018) Kurator: Tools for Improving Fitness for Use of Biodiversity Data. Biodiversity Information Science and Standards 2: e26539. https://doi.org/10.3897/biss.2.26539</li>
<li>Morris PJ (2024) FilteredPush/bdqtestrunner: Release of bdqtestrunner version v1.0.0 (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.13932178</li>
<li>Morris PJ (2025) kurator-org/bdq_issue_to_csv: Version 1.2.0 release of bdq_issue_to_csv utility for creating bdqtest: term-version file (v1.2.0). Zenodo. https://doi.org/10.5281/zenodo.15375006</li>
<li>Morris PJ, Dou L (2025) FilteredPush/sci_name_qc: Release version 1.2.0 of the sci_name_qc library compliant implementation of all the BDQ Standard NAME Tests (v1.2.0). Zenodo. https://doi.org/10.5281/zenodo.15374172</li>
<li>Morris PJ (2025) FilteredPush/rec_occur_qc: Release version 1.1.0 of the rec_occur_qc library, compliant implementation of all the BDQ Standard OTHER (metadata) Tests (v1.1.0). Zenodo. https://doi.org/10.5281/zenodo.15374776</li>
<li>Morris PJ, Lowery D (2025) FilteredPush/event_date_qc: Release version 3.1.0 of the event_date_qc library, compliant implementation of all the BDQ Standard Time Tests (v3.1.0). Zenodo. https://doi.org/10.5281/zenodo.15373615</li>
<li>Morris PJ, Lowery D (2025b). FilteredPush/geo_ref_qc: Release version 2.1.0 of the geo_ref_qc library, compliant implementation of all the BDQ Standard Space Tests (v2.1.0). Zenodo. https://doi.org/10.5281/zenodo.15374533</li>
<li>Natural Earth (2009)  Land 10m. https//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip</li>
<li>Natural Earth (2009)  Minor Islands. https//www.naturalearthdata.com/download/10m/physical/ne_10m_minor_islands.zip</li>
<li>Natural Earth (2022) Admin 1 – States, provinces. v5.1.1 2022-05-12. https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/</li>
<li>Natural Earth (2022) Natural Earth Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales. v5.1.2. https://www.naturalearthdata.com/,  https://github.com/nvkelso/natural-earth-vector/releases/tag/v5.1.2.</li>
<li>OBIS (2024) Ocean Biodiversity Information System (OBIS). https://obis.org</li>
<li>ProgrammableWeb (2006) GeoNames API. https://www.programmableweb.com/api/geonames</li>
<li>Rees ER, Nicholls M (2020) Suppl. material 2: Data Quality Use Case Study Result. https://biss.pensoft.net/article/download/suppl/5255738/</li>
<li>Rees T (compiler) (2024) Interim Register of Marine and Nonmarine Genera (IRMNG) VLIZ, Belgium. https://www.irmng.org</li>
<li>Sanderson R, Ciccarese P and Young B (2017) Web Annotation Data Model. https://www.w3.org/TR/annotation-model/</li>
<li>Spatial Reference (2024) What is SpatialReference.org. https://spatialreference.org</li>
<li>Veiga AK (2016). A conceptual framework on biodiversity data quality. São Paulo : Escola Politécnica, University of São Paulo. Doctoral Thesis in Sistemas Digitais. http://www.teses.usp.br/teses/disponiveis/3/3141/tde-17032017-085248/</li>
<li>Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017) A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731</li>
<li>Vertnet (2022) DwC Vocabs. https://github.com/VertNet/DwCVocabs/tree/master/vocabs</li>
<li>VLIZ (2023). Marineregions.org. https://www.marineregions.org/downloads.php#marbound</li>
<li>Vocabulary Maintenance Specification Task Group (2017). Standards Documentation Standard. Biodiversity Information Standards (TDWG) http://www.tdwg.org/standards/147</li>
<li>W3C (2017) Web Annotation Data Model. https://www.w3.org/TR/annotation-model/</li>
<li>W3C (2017) Web Annotation Data Model: Annotation. https://www.w3.org/TR/annotation-vocab/#annotation</li>
<li>Waller JT (2023) Processing Country Centroids at the Global Biodiversity Information Facility. Biodiversity Information Science and Standards 7: e110728. https://doi.org/10.3897/biss.7.110728</li> 
<li>Wieczorek C and Wieczorek J (2021) Georeferencing Calculator. http://georeferencing.org/georefcalculator/gc.html</li>
<li>Wieczorek J, Bloom D, Guralnick R, Blum S, Döring M, Giovanni R, Robertson T, Vieglais D (2012) Darwin Core: An Evolving Community-Developed Biodiversity Data Standard. PLoS ONE 7(1): e29715. https://doi.org/10.1371/journal.pone.0029715</li>
<li>Wikipedia (2020) Extreme points of Antarctica. https://en.wikipedia.org/wiki/Extreme_points_of_Antarctica</li>
<li>Wikipedia (2020) Great-circle distance. https://en.wikipedia.org/wiki/Great-circle_distance</li>
<li>Wikipedia (2020) ISO 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</li>
<li>Wikipedia (2020) ISO 8601. https://en.wikipedia.org/wiki/ISO_8601</li>
<li>Wikipedia (2020) List of elevations extremes by country. https://en.wikipedia.org/wiki/List_of_elevation_extremes_by_country_</li>
<li>Wikipedia (2024) Extreme points on Earth. https://en.wikipedia.org/wiki/Extreme_points_of_Earth</li> 
<li>Wikipedia (2024) LSID (Life Science Identifier). https://en.wikipedia.org/wiki/LSID</li>
<li>Wikipedia (2024) Uniform Resource Name (URN). https://en.wikipedia.org/wiki/Uniform_Resource_Name</li>
<li>WoRMS (2019) WoRMS - World Register of Marine Species. https://www.marinespecies.org</li> 
</ul>

## 8. Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. The Biodiversity Data Quality (BDQ) Standard. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
