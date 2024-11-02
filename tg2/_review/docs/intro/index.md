<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Biodiversity Data Quality Core Introduction

Title
: Biodiversity Data Quality Core Introduction

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Abstract
: **Biodiversity Data Quality (BDQ)) Core** is a standard designed to facilitate the consistent development and use of a set of biodiversity data quality tests and assertions. The standard consists of vocabularies needed to define the tests, a guide to support the implementation of tests, a guide to support the interpretation of outputs of implemented tests, example data, and expected responses from tests against the example data to support the validation of implemented tests.

Authors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Contributors
: [Yi-Ming Gan](https://orcid.org/0000-0001-7087-2646) ([Royal Belgian Institute of Natural Sciences](http://www.wikidata.org/entity/Q16665660)), [António Mauro Saraiva](https://orcid.org/0000-0003-2283-1123) ([Universidade de São Paulo](https://www.wikidata.org/wiki/Q835960)), [Alan Koch Veiga](http://orcid.org/0000-0003-2672-8115) ([Universidade de São Paulo](https://www.wikidata.org/wiki/Q835960)), [Paula F Zermoglio](https://orcid.org/0000-0002-6056-5084) ([Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN): San Carlos de Bariloche](https://www.irnad.com/)), [Alexander Thompson](https://orcid.org/0000-0002-8981-4048) ([Google](https://www.wikidata.org/wiki/Q95)), [David Lowery](https://github.com/lowery) , [Christian Gendreau](https://orcid.org/0000-0003-4898-4291) ([Agriculture and Agri-Food Canada](http://www.wikidata.org/entity/Q1046164)), [Tim Roberston](https://orcid.org/0000-0001-6215-3617) ([Global Biodiversity Information Facility](https://www.wikidata.org/wiki/Q1531570)), [Dmitry Schigel](https://orcid.org/0000-0002-2919-1168) ([Global Biodiversity Information Facility](https://www.wikidata.org/wiki/Q1531570)), [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) , [Miles Nicholls](https://orcid.org/0000-0002-3302-0070) ([Atlas of Living Australia](https://www.wikidata.org/wiki/Q16335177)), [Emily Rose Rees](https://orcid.org/0000-0003-0112-6716) ([Atlas of Living Australia](https://www.wikidata.org/wiki/Q16335177)), [Abigail Benson](https://orcid.org/0000-0002-4391-107X) ([U.S. Geological Survey](https://www.wikidata.org/wiki/Q193755))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Biodiversity Data Quality Core Introduction. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2024-09-10>

Draft Standard for Submission

### Table of Contents ###

- [1 Introduction](#1-introduction)
- [1.1 Purpose](#11-purpose)
- [1.2 Audience](#12-audience)
- [1.3 Associated Documents](#13-associated-documents)
- [1.4. Status of the Content of This Document](#14-status-of-the-content-of-this-document)
- [1.5 RFC 2119 key words](#15-rfc-2119-key-words)
- [1.6 Namespace Abbreviations](#16-namespace-abbreviations)
- [2 Introduction to the BDQ Core Standard](#2-introduction-to-the-bdq-core-standard)
- [2.1 Parts of the Standard](#21-parts-of-the-standard)
- [2.1 Vocabularies](#21-vocabularies)
- [2.2 Test Guidance](#22-test-guidance)
- [2.3 Test Lists](#23-test-lists)
- [2.4 Guides and other documents.](#24-guides-and-other-documents)
- [2.5 Implementation Validation Data](#25-implementation-validation-data)
- [2.6 Test Execution Environments and Workflows](#26-test-execution-environments-and-workflows)
- [2.7 Implementations of Tests 'In the Wild'](#27-implementations-of-tests-'in-the-wild')
- [3 Design of the Tests (normative)](#3-design-of-the-tests-normative)
- [3.1 Data Quality Control, Data Quality Assurance (normative)](#31-data-quality-control,-data-quality-assurance-normative)
- [3.2 When are Tests Run (normative)](#32-when-are-tests-run-normative)
- [3.3 Results of Test Executions (normative)](#33-results-of-test-executions-normative)
- [4 Contributions and Acknowledgments](#4-contributions-and-acknowledgments)
- [4.1 Acknowledgments](#41-acknowledgments)
- [4.1.1 Funding and Support for Meetings](#411-funding-and-support-for-meetings)
- [4.2 Contributions](#42-contributions)
- [4.2.1 Authors](#421-authors)
- [4.2.2 Contributors](#422-contributors)
- [5 Acronyms](#5-acronyms)
- [6 Glossary](#6-glossary)
- [6.1 Term-Action](#61-term-action)
- [6.2 General Glossary](#62-general-glossary)
- [7 References](#7-references)
- [8 Audience for Each Document in BDQ Core](#8-audience-for-each-document-in-bdq-core)
 

## 1 Introduction

Biodiversity Data Quality (BDQ) Core, hereafter referred to as 'BDQ Core', consists of 1) specifications of data quality tests that can be implemented to provide reproducible results from a given set of input data and test parameters, 2) a generic fitness for use framework (bdqffdq:) whose terms and semantics are embodied in the Framework Ontology, 3) a set of controlled vocabularies for the terms bdqffdq:DataQualityDimension, bdqffdq:Enhancement, and bdqffdq:Criterion, 4) a supporting vocabulary of terms (bdq:) used in the specification of the previously mentioned tests, 5) an exemplar data set to use as input for validation of the behavior of implementations of the previously mentioned tests, 6) a guide to implementation of the tests,  7) a guide to the interpretation of the results of the tests, and 8) a guide to the Framework Ontology for describing data quality.

Not part of BDQ Core, but dependent on it, is an exemplar implementation of the tests, written in Java&#174;, the behavior of which has been validated against the uses the previously mentioned validation data set.

BDQ Core covers a specification of tests for the quality of biodiversity data, not a specification of the quality to which biodiversity data are expected to conform. ‘Fitness for use’ of a biodiversity data record depends on the use to which it is applied: a record that is unsuitable to be used in one application may be suitable for another application (Belbin et al. 2013).  Data does not have quality in the abstract, it only has quality with respect to some use, within BDQ Core, bdqffdq:UseCases provide a formal representation of uses to which data may be put.  The set of Tests and UseCases defined in BDQ Core are a starting point, not a limitation.  The BDQ Core tests may be composed differently for different uses, and additional tests are expected. 

The BDQ tests support the determination of whether data resources will be fit for use for some particular purpose from the perspectives of the data quality dimensions `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, and `Resolution`. The tests themselves do not assert data quality, rather, sets of tests can be defined to support the assessment or assurance of data quality for a particular purpose by analyzing their responses to the input data in question against predefined expectations.  This standard also specifies a structure to capture Profiles of tests for particular cases of fitness for use, and identifies a set of Profiles and uses they apply to for the included tests.  This standard does not specify execution order or other aspects of frameworks within which tests may be run.  Users are free to add new tests and compose tests differently for different uses.

The BDQ tests were initially targeted specifically to [Darwin Core](https://dwc.tdwg.org/terms/) classes and properties against which they operate. This is not a limitation on the scope of the standard, but rather a choice of original scope against which to develop the tests.

### 1.1 Purpose

This document introduces BDQ Core.

### 1.2 Audience

This document is a general introduction to BDQ Core standard designed for anyone interested in specifications for the assessment or assurance of fitness for use of biodiversity data, or to improve it. 

### 1.3 Associated Documents

Those who want a quick view of the Tests should consult the [BDQ Core Tests Quick Reference Guide](../terms/bdqcore/index.md).  Those interested in more detail on the interpretation of test results should consult the [BDQ Core User's Guide](../guide/users/index.md "BDQ Core Users Guide"), while those interested in the implementation of tests following the BDQ Core should consult the [BDQ Core Implementer's Guide](../guide/implementers/index.md "BDQ Core Implementation Guide").  Those interested in composing new tests, or seeking to represent test results as linked open data should consult the [Framework Ontology guide](../guide/bdqffdq/index.md).

### 1.4. Status of the Content of This Document

Section 3 of this document is normative. 

All other sections of this document are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace Abbreviations

The following namespace abbreviations are used in this document:

**CHECK THIS set on final draft, include only those used in this document**

| **Prefix**   | **Namespace**                                    |
|--------------|--------------------------------------------------|
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms/               |
| bdqcrit      | https://rs.tdwh.org/bdqcrit/terms/               |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms/                |
| bdqenh       | https://rs.tdwg.org/bdqenh/terms/                |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms/               |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema#            |
| owl          | http://www.w3.org/2002/07/owl#                   |
| xsd          | http://www.w3.org/2001/XMLSchema#                |

## 2 Introduction to the BDQ Core Standard 

### 2.1 Parts of the Standard

The full set of documents comprising the BDQ Core standard is listed on the [BDQ Core landing page](../index.md).

### 2.1 Vocabularies

The focus of this standard is on (1) a framework for describing data quality and (2) the description of a set of tests and assertions using that framework.  The framework is instantiated formally as an ontology (namespace abbreviation bdqffdq:).  The tests are instantiated formally as a vocabulary (namespace abbreviation `bdqcore:`), with test names, labels, descriptions, expected responses and other metadata expressed with bdqffdq: and other vocabularies.  Four additional vocabularies used in defining the tests are defined by this standard. Together the vocabularies serve to support the specification of suites of biodiversity data quality assessments and amendments to improve data for particular purposes. Each vocabulary is described in full in its distinct Term List document, linked from and summarized together on [BDQ Core Vocabularies](../vocabularies/index.md). 

### 2.2 Test Guidance

Beyond data availability, data quality is probably the most significant issue for users of biodiversity data. The BDQ Core standard suite of tests and assertions is meant to be used by data collectors, data providers, and data users to assess and potentially improve data quality.  

The Fitness for Use Framework upon which BDQ Core is based allows pipelines of tests and assertions to have formal dependencies between them, such as a specified order in which they should be run in order to get a deterministic result, or using the results of some tests as the inputs to other tests, or building composite tests from other existing tests. By design, dependencies are manifest in some of the tests and assertions that are Measures, while tests and assertions that are Issues, Validations, and Amendments tend to be independent of each other.

Tests, even Amendments, do not modify original data. Instead, Amendment Test responses contain the information needed to amend original data by providing reproducible interpretations. These interpretations can be as a substitute for the original data downstream in analytical pipelines, or can be used to vet and amend the original data, as appropriate.

Test specifications _sensu latu_ consist of the metadata (e.g., identifier, preferred label, description, information elements acted upon, information elements consulted, expected response, data quality dimension, parameters and default behavior, notes) required to understand the test, its context, and its potential uses, and to implement it in a way that is compliant with the standard.

The specifications _sensu strictu_ for tests include expected responses from tests consist of metadata (status, result, and comment) required for a user to interpret and act upon the data (information elements) pertinent to the test that was run, whether the information elements were those consulted or those acted upon.

### 2.3 Test Lists

The [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md) is a quick reference guide to the tests defined in BDQ Core. 

### 2.4 Guides and other documents. 

The [BDQ User's Guide](../guide/users/index.md) is intended to contain everything needed to understand the nature or the tests and the responses from them when they are run.  It is intended to be read with the quick reference guide to the tests.

The [BDQ Implementer's Guide](../guide/implementers/index.md) is intended to contain everything needed to understand the requirements for compliant implementations of the tests. 

The [Framework Ontology guide](../guide/bdqffdq/index.md) describes how the Framework Ontology (bdqffdq:) is used to describe the BDQ Core Tests, and can be used to describe new tests or new compositions of tests for new uses.  The ontology is also intended to allow test results to be represented as linked open data or in W3C oa:Annotations. 

[Synthetic and Modified Data](../synthetic/index.md) Describes how to mark synthetic and altered data that may be used to validate test implementations to distinguish it from real data.

### 2.5 Implementation Validation Data 

See the [BDQ Implementer's Guide](../guide/implementers/index.md) for information on a set of data for validating test implementations.. 

### 2.6 Test Execution Environments and Workflows

Neither the test descriptions nor the framework impose constraints on environments or workflows for execution.  One possible workflow is to run all validations, then all amendments, then all validations again on a modified copy of the input data to which all proposed amendments have been applied.

A single validation step, with measures evaluating the results of the amendments could look like the diagram below.

![Diagram of workflow through single validation step](workflow_single_iteration.svg)

Expanding on this single validation step, amendments can be run and their results fed back into a second phase of post-amendment validation, with measures again evaluating the results of validation of the input data if all changes proposed by amendments are accepted.  Presentation of a data quality report would be an expected result from this workflow for Quality Control purposes, while using the Measures in the second step to filter data in a processing pipeline to just that fit for purpose for a particular use would be expected for Quality Assurance purposes.

![Diagram of workflow with pre-amendment validation+measure phase, followed by amendment phase, followed by post-amendment validation-measure phase](workflow_two_iterations.svg)

### 2.7 Implementations of Tests 'In the Wild'

Not part of the BDQ Core standard, but implemented as part of the process of writing the standard, are a set of Java implementations of the BDQ Core tests which pass against the validation data.  See [9 Existing Test Implementations](../guide/implementers/index.md/#9-Existing-Test-Implementations-non-normative) in the implementer's guide for details.  

Additional code is available to help support implementation of tests and the use of bdqcore, dwc, and bdqffdq terms in rdf.  See the discussion in [section 8.6 Existing Software tools](#86-Existing-Sofware-tools-non-normative) of the BDQ Core Implementer's Guide.

<!--- TODO: note partial implementations in iDigBio, ALA, OBIS, GBIF, and R packages --->

## 3 Design of the Tests (normative)

<!--- PJM: Section 3 is Important (largely permissive) elements that are needed in the introduction --->

### 3.1 Data Quality Control, Data Quality Assurance (normative)

BDQ Core draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.  Implementations of the bdqcore tests MAY be used to perform Quality Control, Quality Assurance, or both.  The [mathematical formalization](..//bdqffdq/index.md#5-fitness-for-use-framework-summary-of-mathematical-formalization-normative) of the bdqffdq Framework provides a formal definition of Quality Control and Quality Assurance, and how Test Assertions SHOULD be used for each.

### 3.2 When are Tests Run (normative)

The bdqcore tests are designed to be run at any point in the life cycle of biodiversity data. They MAY be run at the point of initial collection or observation of organisms. They MAY be run to support data transcription. They MAY be run in loading data into databases of record from field or transcription sources. They MAY be run in preparing data from databases of record for aggregation. They MAY be run during data aggregation and the presentation of aggregated data.  They MAY be run in workflows for analysis of data for research purposes.

### 3.3 Results of Test Executions (normative)

BDQ Core is agnostic about the format of presentation of results from BDQ Core Tests.  BDQ Core does, however, specify that test implementations and presentations MUST return structured data with at least bdq:Response.status, bdq:Response.result, and bdq:Response.comment  Responses MAY also contain more information in Response.qualifier.  See the implementer's guide section on [Presentation of Results](../guide/implementers/index.md#7-Presentation-of-Results) for further normative and non-normative guidance about result presentation See the bdqcore: landing page section on the [Structure of a Response](../bdqcore/index.md#31-Structure-of-Response-normative) for normative guidance on Responses as RDF or as data structures.

The results of the execution of implementations of the bdqcore: tests MAY be presented as Data Quality reports.  The Framework Ontology provides vocabulary and structure that MAY be used for such data quality reports.

The bdqffdq: vocabulary enables the wrapping of the results of bdqcore: tests within annotations.  The bdqffdq: vocabularies in particular are intended to support the framing of assertions from tests within annotations that follow the W3C Web Annotation Data Model (Sanderson et al. 2017), and are suitable for inclusion in semantic data stores.  See the section on [Annotations](../guide/implementers/index.md#72-Annotations-normative) in the implementer's guide for more guidance.

## 4 Contributions and Acknowledgments

### 4.1 Acknowledgments

The Authors gratefully acknowledge all those who have commented on the GitHub issues during the development of BDQ Core, and all those who have contributed to discussions at various workshops in São Paulo, Brazil; Canberra, Australia; Monash, Australia; Leiden, The Netherlands; Gainesville, USA; and Seattle, USA) and at Biodiversity Information Standards (TDWG) annual meetings (in Jönköping, Sweden; Santa Clara de San Carlos, Costa Rica; Ottawa, Canada; Dunedin, New Zealand; Leiden, The Netherlands; Sofia, Bulgaria; Hobart, Australia; and Ginowa, Japan; and the various Virtual meetings). The Authors are also grateful for all those who responded to our email questions.

We'd also gratefully acknowledge the continued support of the Biodiversity Information Standards (TDWG) Executive over the 10 years of this project.

#### 4.1.1 Funding and Support for Meetings

We acknowledge the financial support of The Atlas of Living Australia and Biodiversity Information Standards (TDWG) for Lee Belbin and Arthur Chapman to attend two face-to-face meetings for the development of BDQ Core, and the Atlas of Living Australia for support of John Wieczorek to attend meetings in Canberra Australia. The Museum of Comparative Zoology provided support for Paul Morris; VertNet, Kurator, and Rauthflor LLC provided support of John Wieczorek. The United States National Science Foundation through funding of the Kurator project, provided time for Paul Morris, Robert Morris and David Lowery for early work on the project.

The São Paulo Research Foundation (FAPESP), the Universidade de São Paulo (USP) provided facilities, and with the Global Biodiversity Information Facility and others, supported participants to attend the meeting in São Paulo, Brazil. The US National Science Foundation through iDigBio provided support for the meeting in Gainesville, Florida.

### 4.2 Contributions

Many people have contributed valuable comments through the development of the BDQ Core standard.  

#### 4.2.1 Authors 

We recognize four people as authors of the standard, having contributed consistently over the last decade and having been heavily engaged in writing the core test descriptors and the BDQ core documentation. 

- **Lee Belbin (Blatant Fabrications Pty Ltd)**: Convener of TDWG Data Quality Task Group 2 (Data Quality Tests and Assertions); test descriptions; author of BDQ Core documents; test validation data.
- **Arthur D Chapman (Australian Biodiversity Information Services)**: Co-convener of the TDWG Data Quality Interest Group; test descriptions; author of BDQ Core documents; vocabularies. 
- **Paul J Morris (Museum of Comparative Zoology, Harvard University)**: Test descriptions; bdqffdq ontology; Java test implementations in filteredpush packages; author of BDQ Core documents; test validation data. 
- **John Wieczorek (VertNet)**: Test descriptions; test implementations; author of BDQ Core documents; Darwin Core liaison.

#### 4.2.2 Contributors

There were many people who have made notable contributions at various times during the development of BDQ Core.
 
- **Paula F. Zermoglio (Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN), San Carlos de Bariloche)**: Convener of TDWG Data Quality Task Group 4 (Best Practices for Development of Vocabularies of Value); test descriptions; vocabulary development.
- **Alexander Thompson (iDigBio)**: Key contributions to initial development of test descriptors; migrated test descriptors into markdown tables in GitHub issues.
- **Yi-Ming Gan (Royal Belgian Institute of Natural Sciences)**: Contributed to test evaluation; explanatory workflow diagrams; editing BDQ Core documents.
- **António Mauro Saraiva (Universidade de São Paulo)**: Co-convenor of the TDWG Data Quality Interest Group; development of the Framework for Data Quality (TDWG Data Quality Task Group 1); facilitated test development workshop.
- **Allan Koch Veiga (Universidade de São Paulo)**: Developed the Framework on Data Quality as his dissertation (Veiga 2016), Convener of the TDWG Data Quality Task Group 1 (Framework for Data Quality).
- **David Lowery (Museum of Comparative Zoology, Harvard University)**: Initial development of ontology representation of Framework on Data Quality; developer of kurator-ffdq Java class representation of the Framework.
- **Christian Gendreau (Agriculture and Agri-Food Canada)**: Initial contribitions to data quality discussions; vocabulary definitions and early test development.
- **Tim Roberston (Global Biodiversity Information Facility)**: Contributions to test descriptions; clarification of GBIF vocabulary and API resources for the BDQ Core Tests.
- **Dmitry Schigel (Global Biodiversity Information Facility)**: Initial contributions to data quality discussions and vocabulary definitions; GBIF Representative to the Data Quality Interest Group in early years.
- **Robert A. Morris (late, of UMass Boston)**: Competency questions for the ontology of the Data Quality Framework; guided initial development of the ontology representation of the Framework.
- **Miles Nicholls (Atlas of Living Australia)**: Convener of TDWG Data Quality Task Group 3 (Data Quality Use Cases); Use Case analysis.
- **Emily Rose Rees (Atlas of Living Australia)**: Use Case analysis in TDWG Data Quality Task Group 3 (Data Quality Use Cases).
- **Abigail Benson (U.S. Geological Survey)**: Initial contributions to data quality discussions and vocabulary definitions.

## 5 Acronyms

| **Acronym** | **Explanation**                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------|
| ALA         | [Atlas of Living Australia](https://ala.org.au)                             | 
| BDQ         | [TDWG Biodiversity Data Quality](https://github.com/tdwg/bdq)                       |
| BISON       | [Biodiversity Information Serving Our Nation](https://www.gbif.us/about/)           |
| CRIA        | [Centro de Referência em Informação Ambiental](https://www.cria.org.br/)          |
| EPSG        | [European Petroleum Survey Group](https://epsg.org/home.html)                     |
| GBIF        | [Global Biodiversity Information Facility](https://gbif.org)             |
| iDigBio     | [Integrated Digitized BioCollections](https://www.idigbio.org/)                   |
| IRI         | [Internationalized Resource Identifier](https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier)                 |
| ISO         | [International Standards Organization](https://www.iso.org/home.html)                  |
| QA          | [Quality Assurance](https://en.wikipedia.org/wiki/Quality_assurance)                                     |
| QC          | [Quality Control](https://en.wikipedia.org/wiki/Quality_control)                                       |
| SDS         | [TDWG Standards Documentation Standard](https://www.tdwg.org/standards/sds/)                 |
| TDWG        | [Biodiversity Information Standards](https://tdwg.org)                    |
| TG1         | [Biodiversity Data Quality Interest Group - Task Group 1: Framework on Data Quality](https://github.com/tdwg/bdq/tree/master/tg1) |
| TG2         | [Biodiversity Data Quality Interest Group - Task Group 2: Data Quality Tests and Assertions](https://github.com/tdwg/bdq/tree/master/tg2) |
| TG3         | [Biodiversity Data Quality Interest Group - Task Group 3: Data Quality Use Cases](https://github.com/tdwg/bdq/tree/master/tg3)     |
| TG4         | [Biodiversity Data Quality Interest Group - Task Group 4: Best Practices for Development of Vocabularies of Value](https://github.com/tdwg/bdq/tree/master/tg4) |

## 6 Glossary

### 6.1 Term-Action

Glossary of Term-Actions - i.e. the last two components of the Title (the focus bdqffdq:InformationElement), and the evaluation focus. Useful in filtering Tests in CSV files, for example: "COUNTRYCODE_STANDARD".

| Label | Definition | Comment |
| ---- | ---- | ---- |
| ASSUMEDDEFAULT | A bdqffdq:Amendment that replaces a bdq:EMPTY term with a predefined default bdq:Parameter value. | This action is used in Tests and in bdq:Response.comments. bdq:Response.status value for this case is bdq:AMENDED. For example, the Test [AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](https://rs.tdwg.org/bdqcore/terms/7498ca76-c4d4-42e2-8103-acacccbdffa7). |
| CENTREOFCOUNTRY | Testing if bdqffdq:EnformationElements COORDINATES identify the center of the dwc:country, allowing for a spatial buffer. | For example, the Test [ISSUE_COORDINATES_CENTEROFCOUNTRY](https://rs.tdwg.org/bdqcore/terms/256e51b3-1e08-4349-bb7e-5186631c3f8e). |
| COMPLETE | Testing if the bdqffdq:InformationElement dwc:scientificNameId forms a valid and complete identifier. | Testing for bdqdim:Completeness, for example, the Test [VALIDATION_SCIENTIFICNAMEID_COMPLETE](https://rs.tdwg.org/bdqcore/terms/6eeac3ed-f691-457f-a42e-eaa9c8a71ce8). |
| CONSISTENT | Identifies consistency among values between bdqffdq:InformationElements. | Testing for bdqdim:Consistency. For example, the Test [VALIDATION_CLASSIFICATION_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/2750c040-1d4a-4149-99fe-0512785f2d5f). |
| COORDINATESTERRESTRIALMARINE | A terrestrial taxon that has geographic coordinates that fall within terrestrial boundaries, or a marine taxon that has geographic coordinates that fall within marine boundaries. | Use bdq:AMENDED as the bdq:Response.status, report bdq:COORDINATESTERRESTRIALMARINE in a bdq:Response.qualifier or in a bdq:Response.comment. See the Test [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b9c184ce-a859-410c-9d12-71a338200380). |
| DURATIONINSECONDS | The duration in seconds of the bdq:InformationElement dwc:eventDate. | See the Test [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53). |
| FOUND | The value in a bdqffdq:InformationElement that matched a value in a bdq:sourceAuthority. | Use bdq:COMPLIANT for bdq:Response.result, and include this in bdq:Response.comments or bdq:Response.qualifier. For example, the Test [VALIDATION_STATEPROVINCE_FOUND](https://rs.tdwg.org/bdqcore/terms/4daa7986-d9b0-4dd5-ad17-2d7a771ea71a). |
| FROM | An Output bdqffdqInformationElement is being populated from a more primary Input bdqffdq:InformationElement. | Populates dwc:scienticName from dwc:scientificNameId. See, for example, Test [AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](https://rs.tdwg.org/bdqcore/terms/f01fb3f9-2f7e-418b-9f51-adf50f202aea). |
| INRANGE | The value of bdqffdq:InformationElements that are within an acceptable range. | Use in bdq:Response.qualifier or bdq:Response.comment. For example, the test [VALIDATION_MAXDEPTH_INRANGE](3f1db29a-bfa5-40db-9fd1-fde020d81939). |
| LESSTHAN | A Term-Action indicating that the value in one bdq:InformationElement is less than the value in another bdq:InformationElement. | Used in tests for Depth and Elevation, for example, the Test [VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH](https://rs.tdwg.org/bdqcore/terms/8f1e6e58-544b-4365-a569-fb781341644e). |
| NOTEMPTY | An bdqffdq:InformationElement contains a non-empty value | For example, the Test [VALIDATION_EVENTDATE_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/f51e15a6-a67d-4729-9c28-3766299d2985). |
| PREREQUISITESNOTMET | A Test of type bdqffdq:Measure that counts the number of Tests of type bdqffdq:Validation that did not run due to one or more prerequisites not being met (bdq:INTERNAL_PREREQUISITES_NOT_MET or EXTERNAL_PREREQUISITES_NOT_MET). | See the Test [MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](https://rs.tdwg.org/bdqcore/terms/49a94636-a562-4e6b-803c-665c80628a3d). |
| PROPOSED | A test of type bdqffdq:Measure that counts the number of bdqffdq:Amendments where an action to modify a value in some way through a change or addition is proposed. | See the Test [MEASURE_AMENDMENTS_PROPOSED](https://rs.tdwg.org/bdqcore/terms/03049fe5-a575-404f-b564-ae63f5a1cf8b). |
| STANDARD | A bdqffdq:Validation Test where a value in a bdqffdq:InformationElement matches a bdq:STANDARD value in a bdq:sourceAuthority. | Use in bdq:Response.qualifier or bdq:Response.comment. For example, the Test [VALIDATION_TAXONRANK_STANDARD](https://rs.tdwg.org/bdqcore/terms/7bdb13a4-8a51-4ee5-be7f-20693fdb183e). |
| STANDARDIZED | A bdqffdq:Amendment where a bdq:STANDARD value for a bdqffdq:InformationElement is proposed. | Use bdq:AMENDED as the bdq:Response.status, report bdq:STANDARDIZED in a bdq:Response.qualifier or in a bdq:Response.comment. For example see Test [AMENDMENT_TAXONRANK_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/e39098df-ef46-464c-9aef-bcdeee2a88cb). |
| TRANSPOSED | A bdqffdq:Amendment where the sign and/or value of one or more bdqffdq:InformationElements were proposed to be swapped. | Use bdq:AMENDED as the bdq:Response.status, report bdq:TRANSPOSED in a bdq:Response.qualifier or in a bdq:Response.comment. See the Test [AMENDMENT_COORDINATES_TRANSPOSED](https://rs.tdwg.org/bdqcore/terms/f2b4a50a-6b2f-4930-b9df-da87b6a21082). |
| UNAMBIGUOUS | A combination of bdqffdq:InformationElements is unambiguous in that they align to a unique result given a reference or a Source Authority (bdq:sourceAuthority). | For example, the Test [VALIDATION_TAXON_UNAMBIGUOUS](https://rs.tdwg.org/bdqcore/terms/4c09f127-737b-4686-82a0-7c8e30841590).	|
| VERBATIM | Refers to bdqffdq:Amendment Tests that attempt to extract explicit Darwin Core bdq:InformationElements values from Darwin Core verbatim term bdq:InformationElements. | For example, the Test [AMENDMENT_EVENTDATE_FROM_VERBATIM](https://rs.tdwg.org/bdqcore/terms/6d0a0c10-5e4a-4759-b448-88932f399812) attempts to extract dwc:eventDate from dwc:verbatimEventDate. |

### 6.2 General Glossary

Glossary of terms used in BDQ Core that are additional to those included in the various Namespace: vocabularies and Term-Actions. Note: Usage of 'Darwin Core term(s)' below refer to  [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021).

| Label | Definition | Context |
| ---- | ---- | ---- |
| COORDINATES | A general category of specific bdq:InformationElements that represents the combination of the Darwin Core terms dwc:decimalLatitude and dwc:decimalLongitude and may include metadata terms including dwc:geodeticDatum. | bdqffdq:InformationElement |
| CRS | Coordinate Reference System - (also referred to as 'spatial reference system'). A coordinate system defined in relation to a standard reference or datum (Chapman & Wieczorek 2020). | Test |
| Database of record | An information system which holds an authoritative or master record of some data.  Records in a database of record are held to be correct over different values for the same records that might be found in other data sets.  This is in distinction from aggregated data sets, derived research data set, data sets for portals and other holders of non authoritative copies of the data. | BDQ Core |
| geodetic coordinate reference system | A coordinate reference system based on a geodetic datum, used to describe positions on the surface of the earth (Chapman and Wieczorek 2020). | Test |
| geodetic datum | A mathematical model that uses a reference ellipsoid to describe the size and shape of the surface of the earth and adds to it the information needed for the origin and orientation of coordinate systems on that surface (Chapman and Wieczorek 2000). | Test |
| Framework | The Fitness for Use Framework, the body of work that provides a fundamental structure for the BDQ Core Tests.  The Fitness for Use Framework is derived from (Veiga 2016) and is the outcome of the TDWG Data Quality Task Group 1: Framework on Data Quality (Veiga et al. 2017). | bdqffdq: |
| Framework Ontology | A model of the Framework (Veiga 2016, Veiga et al. 2017) as an owl ontology, present as the bdqffdq: vocabulary in BDQ Core. | bdqffdq: |
| GEOGRAPHY | A general category of specific bdq:InformationElements that represents a combination of Darwin Core administrative geography terms dwc:continent, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality. | bdqffdq:InformationElement |
| Java | Java is a registered trademark of Oracle and/or its affiliates. | BDQ Core |
| [NAME](../supplement/index.md#NAME) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Taxon Class. | bdqffdq:InformationElement |
| non-printing characters | ASCII 0-32 and 127 decimal. Non printing characters or formatting marks that are not displayed at printing. These may include pilcrow, space, non-breaking space, tab character. etc. For the purposes of the tests they are treated as bdq:Empty. | Data |
| null | A value that is used in some databases to signify that a value is unknown or missing. It may be represented in serializations of data outside of database environments by strings such as "NULL", "Null", "null". "/n", "9999", etc. These serializations should be treated as bdq:NotEmpty. | Data |
| [OTHER](../supplement/index.md#OTHER) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms other than Classes dwc:Taxon, dwc:Location or dwc:Event. | bdqffdq:InformationElement |
| POLYNOMIAL | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet. See the test [VALIDATION_POLYNOMIAL_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/17f03f1f-f74d-40c0-8071-2927cfc9487b). | bdqffdq:InformationElement |
| Roman numerals | Numbers written with the characters I, V, X, L, C, D, and M in the latin alphabet, each letter representing an integer and combined to form arbitrary integers. Roman numerals are interpreted as the equivalent integer for months (e.g. "X" as "10") in certain tests. Roman numerals may not be unambiguously interpreted for other Darwin Core terms such as dwc:day or in text fields as they may mean unknown or something else entirely. | Data | 
| [SPACE](../supplement/index.md#SPACE) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Location Class. | bdqffdq:InformationElement |
| SRS | spatial reference system - see CRS (Chapman and Wieczorek 2020). | Test |
| Test | An individual consideration of a DataQualityNeed with a Method which links it to an instance of a Specification, these instances being composed of InformationElements, Arguments, and Parameters. | BDQ Core | 
|  | Technical: A composition of an instance of a subclass of bdqffdq:DataQualityNeed (which expresses a data quality need in the abstract) with an instance of a subclass of bdqffdq:DataQualityMethod which links it to an instance of a bdqffdq:Specification (which spells out how to concretely evaluate the need), these class instances being composed with bdqffdq:InformationElements, bdqffdq:Arguments, and bdqffdq:Parameters. For example, the Test [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134).| BDQ Core | 
| TestField | Column heading in the markdown of the tests in the [tdwg/bdq GitHub](https://github.com/tdwg/bdq/issues) that list all the normative and informative metadata elements that describe a Data Quality Test. | Test |
| Test Type | There are four types of tests, viz. Validation (bdqffdq:Validation), Amendment (bdqffdq:Amendment), Issue (bdqffdq:Issue), and Measure (bdqffdq:Measure). | Test |
| [TIME](../supplement/index.md#TIME) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Event Class. | bdqffdq:InformationElement |
| VERBATIM | A general category of specific bdq:InformationElements that represents a term containing an original value. | bdqffdq:InformationElement |
| whitespace | Characters such as spaces and tabs that affect rendering of printed or displayed output but which themselves are not printed.   1) A field that only includes whitespace is treated as bdq:Empty. 2) In bdqffdq:Validation tests that require the looking up of a bdq:sourceAuthority, leading and/or trailing whitespace will cause the test to fail as no pre-processing is carried out on the data. These leading and trailing whitespaces may be stripped out in a subsequent bdqffdq:Amendment and thus pass when the bdqffdq:Validation test is run again. | Data |
| YEARMONTHDAY | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:month, dwc:day. | bdqffdq:InformationElement |
| YEARSTARTDAYOFYEARENDDAYOFYEAR | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:startDayOfYear, dwc:endDayofYear. | bdqffdq:InformationElement |

## 7 References

Date Last Updated 2024-08-24

The following references have been extracted from the "References" descriptor on the BDQ Core tests and supporting documents. We have used the formatting as used by Pensoft, see https://checklist.pensoft.net/about#AuthorsGuidelines. 

<ul>
<li>ALA (2013) Data Processing. https://www.ala.org.au/blogs-news/data-processing/</li>
<li>ALA (2020) Locations - Species distributions as areas. https://support.ala.org.au/support/solutions/articles/6000234834-locations-species-distributions-as-areas</li>
<li>Belbin L, Daly J, Hirsch T, Hobern D, Salle JL (2013) A specialist’s audit of aggregated occurrence records: An ‘aggregator’s’ perspective. ZooKeys 305: 67–76. doi: 10.3897/zookeys.305.5438</li>
<li>Biodiversity Information Standards (TDWG) (2010) TDWG GUID Applicability Statement. https://github.com/tdwg/guid-as/blob/master/guid/tdwg_guid_applicability_statement.pdf</li>
<li>Biodiversity Information Standards (TDWG) (n.dat) Annotations Interest Group. https://www.tdwg.org/community/annotations/</li>
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
<li>Leiba B (2017) IETF Key words for use in RFCs to Indicate Requirement Levels (RFC 8174). https://tools.ietf.org/html/rfc8174</li>
<li>Library of Congress (2019) Extended Date/Time Format (EDTF). https://www.loc.gov/standards/datetime/</li>
<li>Lowery D, Morris PJ, Morris RA (2024) kurator-org/kurator-ffdq: Release of Kurator-FFDQ library version v3.0.0 (v3.0.0). Zenodo. https://doi.org/10.5281/zenodo.14026643</li>
<li>Maptiler (2019) EPSG.io. https://epsg.io</li>
<li>Morris PJ (2023) FilteredPush/sci_name_qc: Release vesion 1.0.1 of the sci_name_qc library implementing TG2 core NAME tests. (v1.0.1). Zenodo. https://doi.org/10.5281/zenodo.8165105</li>
<li>Morris PJ (2024) kurator-org/bdq_issue_to_csv: Initial release of bdq_issue_to_csv utility (v0.0.5). Zenodo. https://doi.org/10.5281/zenodo.13937571</li>
<li>Morris PJ, Lowery D (2018) kurator-org/ffdq-api: Release of Kurator's FFDQ-API library version 1.0.4 (v1.0.4). Zenodo. https://doi.org/10.5281/zenodo.1253052</li>
<li>Morris PJ, Lowery D (2023) FilteredPush/event_date_qc: Release version 3.0.2 of the event_date_qc library, compliant implementation of all the TG2 Core Time Tests. (v3.0.2). Zenodo. https://doi.org/10.5281/zenodo.8136725</li>
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



## 8 Audience for Each Document in BDQ Core

- [Introduction](../intro/index.md) This document is a general introduction to BDQ Core standard designed for anyone interested in specifications for the assessment or assurance of fitness for use of biodiversity data, or to improve it. 
- Guides
  - [Quick Reference Guide](../guide/users/index.md) This document is for all users.
  - [BDQ Core User's Guide](../guide/users/index.md) This document is for consumers of data quality reports.
  - [BDQ Core Implementer's Guide](../guide/implementers/index.md) This document is for software developers needing a technical understanding of the BDQ Core Tests.
  - [bdqffdq Framework Guide](../guide/bdqffdq/index.md) This document is for those needing a technical understanding of the Framework Ontology (the bdqffdq: vocabulary).
- Vocabularies
  - [Vocabulary Landing page](../vocabularies/index.md) This document is for those needing a technical understanding of BDQ Core and readers seeking to navigate the BDQ Core standard.
    - [bdqcore: Landing page](../bdqcore/index.md) This document is for those needing a technical understanding of the BDQ Core Tests, both Users and Implementers. 
    - [bdqffdq; Landing page](../bdqffdq/index.md) Technical users who need to understand how to describe data quality with the framework.
    - [Term List for bdqffdq:](../list/bdqffdq/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology (the bdqffdq: vocabulary).
    - [bdqffdq: Vocabulary Extension](../extension/bdqffdq/index.md) This document is for those needing a technical understanding of the bdqffdq Framework. 
    - [Term List for bdqenh:](../list/bdqenh/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and application of the Framework Ontology. 
    - [Term List for bdqdim:](../list/bdqdim/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.
    - [Term List for bdqcrit:](../list/bdqcrit/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.
    - [Term List for bdq:](../list/bdq/index.md) This document is for those needing a technical understanding of the BDQ Core Tests. 
- Additional Documents
  - [Marking Synthetic Data](../synthetic/index.md) This document is designed for creators of data sets for the validation of implementations of BDQ Core tests, to see how to mark their data, and for aggregators and users of biodiversity data, to identify criteria for excluding synthetic or modified data from their pipelines . 
  - [Supplement](../supplement/index.md) This supplementary information may be relevant for curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners that wish to understand, evaluate and/or improve the quality of the biodiversity data within their domain. This document provides some key developmental issues in the building of BDQ Core that are not covered in other documents within this this standard. This document may also be useful to those seeking to evaluate their current tests or generate additional to the existing tests for their domain.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Biodiversity Data Quality Core Introduction. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


