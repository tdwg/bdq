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

{authors_contributors}
Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}

### Table of Contents ###

{toc} 

## 1 Introduction

Biodiversity Data Quality (BDQ) Core, hereafter referred to as 'BDQ Core', consists of 1) specifications of data quality tests that can be implemented to provide reproducible results from a given set of input data and test parameters, 2) a vocabulary of terms used in the specification of the previously mentioned tests, 3) a controlled vocabulary for the term bdq:dimension from the previously mentioned test specification terms, 4) a generic fitness for use framework whose terms and semantics are embodied in an ontology, 5) an exemplar data set to use as input for implementations of the previously mentioned tests, 6) an exemplar implementation of the tests, in Java(R), which uses the previously mentioned test data set as input and demonstrates the expected responses to each of the tests, 7) a guide to implementation of the tests are included, and 8) a guide to the interpretation of the results of the tests. 

BDQ Core covers a specification of tests for the quality of biodiversity data, not a specification of the quality to which biodiversity data are expected to conform. ‘Fitness for use’ of a biodiversity data record will greatly depend on the use to which it is applied: a record that is unsuitable to be used in one application may be suitable for another application (Belbin et al 2013). 

The BDQ tests support the determination of whether data resources will be fit for use for some particular purpose from the perspectives of the data quality dimensions `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, and `Resolution`. The tests themselves do not assert data quality, rather, sets of tests can be defined to support the assessment or assurance of data quality for a particular purpose by analyzing their responses to the input data in question against predefined expectations. This standard does not specify a structure to capture 'profiles' - component tests, order of processing, and expected results - for particular cases of fitness for use.

The BDQ tests were initially targeted specifically to [Darwin Core](https://dwc.tdwg.org/terms/) classes and properties against which they operate. This is not a limitation on the scope of the standard, but rather a choice of original scope against which to develop the tests.

### 1.1 Purpose

This document introduces BDQ Core.

### 1.2 Audience

This document is a general introduction to BDQ Core standard designed for anyone interested in specifications for the assessment or assurance of fitness for use of biodiversity data, or to improve it. 

### 1.3 Associated Documents

Those who want  quick view of the Tests should consult the [BDQ Core Tests Quick Reference Guide](../terms/bdqcore/index.md). Those interested in more detail on the interpretation of test results should consult the [BDQ Core User's Guide](../guide/users/index.md "BDQ Core Users Guide"), while those interested in the implementation of tests following the BDQ Core should consult the [BDQ Core Implementer's Guide](../guide/implementation/index.md "BDQ Core Implementation Guide").

### 1.4. Status of the Content of This Document

All sections of this document are non-normative unless explicitly noted as normative.

### 1.5 RFC 2119 Keywords

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
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema             |
| owl          | http://www.w3.org/2002/07/owl#                   |

## 2 Parts of the Standard

### 2.1 Vocabularies

The focus of this standard is on (1) a framework for describing data quality and (2) the description of a set of tests and assertions using that framework.  The framework is instantiated formally as an ontology (namespace abbreviation bdqffdq:).  The tests are instantiated formally as a vocabulary (namespace abbreviation `bdqcore:`), with test names, labels, descriptions, expected responses and other metadata. The tests and assertions specifications make use of additional vocabularies, three of which are defined by this standard. Together the vocabularies serve to support the specification of suites of biodiversity data quality assessments and amendments to improve data for particular purposes. Each vocabulary is described in full in its distinct Term List document, linked from and summarized together on [BDQ Core Vocabularies](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/vocabularies/index.md). 

### 2.2 Test Guidance

Beyond data availability, data quality is probably the most significant issue for users of biodiversity data. The BDQ Core standard suite of tests and assertions is meant to be used by data collectors, data providers, and data users to assess and potentially improve data quality.  

The Fitness for Use Framework upon which BDQ Core is based allows pipelines of tests and assertions to have formal dependencies between them, such as a specified order in which they should be run in order to get a deterministic result, or using the results of some tests as the inputs to other tests, or building composite tests from other existing tests. By design, dependencies are manifest in some of the tests and assertions that are Measures, while tests and assertions that are Issues, Validations, and Amendments tend to be independent of each other.

Tests, even those labeled as Amendments, do not modify original data. Instead, test responses contain the information needed to amend original data by providing reproducible interpretations. These interpretations can be as a substitute for the original data or can be used to vet and amend the original data, as appropriate.

Test specifications consist of the metadata (e.g., identifier, preferred label, description, information elements acted upon, information elements consulted, expected response, data quality dimension, parameters and default behavior, notes) required to understand the test, its context, and its potential uses, and to implement it in a way that is compliant with the standard.

The specifications for expected responses from tests consist of metadata (status, result, and comment) required for a user to interpret and act upon the data (information elements) pertinent to the test that was run, whether the information elements were those consulted or those acted upon.

The [BDQ User's Guide](../guide/users/index.md) is intended to contain everything needed to understand the nature or the tests and the responses from them when they are run. 

The [BDQ Implementer's Guide](../guide/implementers/index.md) is intended to contain everything needed to understand the requirements for compliant implementations of the tests. 

[!--- JRW first pass finished to here ---]

[Synthetic and Modified Data](../synthetic/index.md) Describes how to mark synthetic and altered data that may be used to validate test implementations to distinguish it from real data.


### 2.3 Implementation Validation Data 

See the [BDQ Implementer's Guide](../guide/implementers/index.md) for information on a set of data for validating test implementations.. 

### 2.4 Exemplar Tests Implementation

<!--- PJM: Does section 2.4 belong?  The filteredpush implementations aren't part of the standard --->

### 2.6 Test Lists

The [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md) is a quick reference guide to the tests defined in BDQ Core. 

### 2.7 Test Execution Environments and Workflows

Neither the test descriptions nor the framework impose constraints on workflows for execution.  One possible workflow is to run all validations, then all amendments, then all validations again on a modified copy of the input data to which all proposed amendments have been applied.

A single validation step, with measures evaluating the results of the amendments could look like the diagram below.

![Diagram of workflow through single validation step](workflow_single_iteration.svg)

Expanding on this single validation step, amendments can be run and their results fed back into a second phase of post-amendment validation, with measures again evaluating the results of validation of the input data if all changes proposed by amendments are accepted.

![Diagram of workflow with pre-amendment validation+measure phase, followed by amendment phase, followed by post-amendment validation-measure phase](workflow_two_iterations.svg)

### 2.8 Glossary

**Needs Text**

### 2.9 Bibliography

<!--- PJM: Select list here, or is this where the references go, or just link to References page? --->

[References File](../references/index.md)


## 3 Design of the Tests

<!--- PJM: Section 3 is Important elements to put in the introduction --->

### 3.1 Data Quality Control, Data Quality Assurance

BDQ Core draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.  Implementations of the bdqcore tests MAY be used to perform Quality Control, Quality Assurance, or both.

### 3.2 When are Tests Run 

The bdqcore tests are designed to be run at any point in the life cycle of biodiversity data. They MAY be run at the point of initial collection or observation of organisms. They MAY be run to support data transcription. They MAY be run in loading data into databases of records from field or transcription sources. They MAY be run in preparing data from databases of record for aggregation. They MAY be run during data aggregation and the presentation of aggregated data.  They MAY be run in workflows for analysis of data for research purposes.

### 3.3 Results of Test Executions 

BDQ Core is agnostic about how reports from BDQ Core can be reported.  It does, however, specify that test implementations and presentations MUST return structured data with at least bdq:Response.status, bdq:Response.result, and bdq:Response.  Responses MAY also contain more information in Response.qualifier.

The results of the execution of implementations of the bdqcore: tests MAY be presented as Data Quality reports.  The bdqffdq: framework provides vocabulary and structure that MAY be used for such data quality reports.

The bdqffdq: vocabulary enables the wrapping of the results of bdqcore: tests within annotations.  The bdqffdq: vocabularies in particular are intended to support the framing of assertions from tests within annotations that follow the W3C Web Annotation Data Model (Sanderson et al. 2017), and are suitable for inclusion in semantic data stores.

## 4 Acknowledgements

We acknowldge the financial support of The Atlas of Living Australia and Biodiversity Information Standards (TDWG) for Lee Belbin and Arthur Chapman to attend the two face-to-face meetings for the development of BDQ Core. We also acknowledge the support of Paul Morris by The Museum of Comparative Zoology.

The authors also gratefully acknowledge all those who have commented on the issues during the development of BDQ Core.

### 4.1 Contributor Roles

Many people have contributed to the development of the BDQ Core standard.  

We recognize 4 people as authors of the standard, having contributed consistently over the last decade and having been heavily engaged in writing the core test descriptors and the BDQ core documentation.  

Lee Belbin (Blatant Fabrications)
: Test Descriptions, Test Validation Data, Author of BDQ Core documents. Convenor of Task Group 2: Data Quality Tests and Assertions. 

Arthur D. Chapman (Australian Biodiversity Information Services)
: Test Descriptions, Author of BDQ Core Documents, Vocabulary and definition development, convener of the BDQ Interest group.

Paul J. Morris (Museum of Comparative Zoology, Harvard University), 
: Test Descriptions, bdqffdq ontology, java test implementations in filteredpush packages, Author of BDQ Core Documents.

John Wieczorek (VertNet)
: Test Descriptions, test implementations, Author of BDQ Core Documents.

The following people have also contributed substantally to the development what has become BDQ Core over the last decade.

Yi-Ming Gan (Royal Belgian Institute of Natural Sciences)
: Contributed to finalization of the test descriptors, explanatory workflow diagrams, edits to text of BDQ Core Documents.

António Mauro Saraiva (Universidade de São Paulo)
: Development of the framework, TG1, Facilitated test development workshop, co-convenor of Data Quality Interest Group until 2022.

Alan Koch Veiga (Universidade de São Paulo)
: Developed the framework as his disertation, convenor of Task Group 1: Framework on Data Quality.

Paula F. Zermoglio (Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN): San Carlos de Bariloche), 
: Contributions to multiple test descriptions and vocabulary development, Convenor of Task Group 4: Best Practices for Development of Vocabularies of Value.

Alexander Thompson (iDigBio)
: Key contributions to initial development of test descriptors, migrated test descriptors into markdown tables in github issues.

David Lowery (Museum of Comparative Zoology, Harvard University)
: Initial development of ontology reprentation of the framework, developer of kurator-ffdq java class representation of the framework.

Christian Gendreau (Agriculture and Agri-Food Canada)
: Intitial contribitions to data quality discussions, vocabulary definitions and early test development.

Tim Roberston (Global Biodiversity Information Facility)
: Contributions to test descriptions, clarification of GBIF vocabulary and API resources for the tests.

Dmitry Schigel (Global Biodiversity Information Facility)
: Intitial contribitions to data quality discussions and vocabulary definitions.

Robert A. Morris (late, of UMass Boston)
: Competency Questions for the framework as an ontology, guided intital development of the ontology representation of the framework.

Miles Nicholls (Atlas of Living Australia)
: Use Case analysis, convenor of Task Group 3: Data Quality Use Cases.

Emily Rose Rees (Atlas of Living Australia)
: Use Case analysis in Task Group 3: Data Quality Use cases.

Abigail Benson (U.S. Geological Survey)
: Intitial contribitions to data quality discussions and vocabulary definitions.

## 5 Acronyms
<!--- TODO: Where do the acronyms go? --->

| **Acronym** | **Explanation**                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------|
| ALA         | Atlas of Living Australia                                                                                      | 
| BDQ         | TDWG Biodiversity Data Quality Interest Group                                                                  |
| BISON       | Biodiversity Information Serving Our Nation                                                                    |
| CRIA        | Centro de Referência em Informação Ambiental                                                                   |
| EPSG        | European Petroleum Survey Group                                                                                |
| GBIF        | Global Biodiversity Information Facility                                                                       |
| iDigBio     | Integrated Digitized BioCollections                                                                            |
| IRI         | Internationalized Resource Identifier                                                                          |
| ISO         | International Standards Organization                                                                           |
| TDWG        | Biodiversity Information Standards                                                                             |
| TG1         | Biodiversity Data Quality Interest Group Task Group 1: Framework on Data Quality                               |
| TG2         | Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions                       |
| TG3         | Biodiversity Data Quality Interest Group Task Group 3: Data Quality Use Cases                                  |
| TG4         | Biodiversity Data Quality Interest Group Task Group 4: Best Practices for Development of Vocabularies of Value |

## 6 Audience for Each Document in BDQ Core

- [Introduction](../intro/index.md) This document is a general introduction to BDQ Core standard designed for anyone interested in specifications for the assessment or assurance of fitness for use of biodiversity data, or to improve it. 
- Guides
  - [Quick Reference Guide](../guide/users/index.md) This document is for all users.
  - [Users Guide](../guide/users/index.md) This document is for consumers of data quality reports.
  - [Implementers Guide](../guide/implementers/index.md) This document is for software developers needing a technical understanding of the BDQ Core Tests.
  - [bdqffdq Framework Guide](../guide/bdqffdq/index.md) This document is for those needing a technical understanding of the bdqffdq: Framework vocabulary.
- Vocabularies
  - [Vocabulary Landing page](../vocabularies/index.md) This document is for those needing a technical understanding of BDQ Core and readers seeking to navigate the BDQ Core standard.
    - [bdqcore: Landing page](../bdqcore/index.md) This document is for those needing a technical understanding of the BDQ Core Tests, both Users and Implementors. 
    - [bdqffdq; Landing page](../bdqffdq/index.md) Technical users who need to understand how to describe data quality with the framework.
    - [Term List for bdqffdq:](../list/bdqffdq/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the bdqffdq: Framework vocabulary.
    - [bdqffdq: Vocabulary Extension](../extension/bdqffdq/index.md) This document is for those needing a technical understanding of the bdqffdq Framework. 
    - [Term List for bdqenh:](../list/bdqenh/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and application of the bdqffdq: Framework. 
    - [Term List for bdqdim:](../list/bdqdim/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the bdqffdq: Framework vocabulary.
    - [Term List for bdqcrit:](../list/bdqcrit/index.md) This document is for those needing a technical understanding of the BDQ Core Tests and the application of the bdqffdq: Framework vocabulary.
    - [Term List for bdq:](../list/bdq/index.md) This document is for those needing a technical understanding of the BDQ Core Tests. 
- Additional Documents
  - [Marking Synthetic Data](../synthetic/index.md) This document is designed for creators of data sets for the validation of implementations of BDQ Core tests, to see how to mark their data, and for aggregators and users of biodiversity data, to identify criteria for excluding synthetic or modified data from their pipelines . 
  - [Supplement](../supplement/index.md) This supplementary information may be relevant for curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners that wish to understand, evaluate and/or improve the quality of the biodiversity data within their domain. This document provides some key developmental issues in the building of BDQ Core that are not covered in other documents within this this standard. This document may also be useful to those seeking to evaluate their current tests or generate additional to the existing tests for their domain.
