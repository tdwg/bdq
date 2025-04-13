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

**Comment**<br>
{comment}

### Table of Contents ###

{toc} 

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to introduce the Biodiversity Data Quality Core (BDQ Core) standard—its components, guiding principles, and intended applications. BDQ Core provides a modular, extensible framework for assessing the quality of biodiversity data relative to specific uses, not according to a universal benchmark. It includes:

- Specifications of data quality Tests that produce reproducible outcomes from standardized inputs;
- A formal fitness for use framework (`bdqffdq:`), described in an ontology and used to contextualize Tests;
- Controlled vocabularies that define key concepts such as `DataQualityDimension`, `Enhancement`, and `Criterion`;
- A supporting vocabulary (`bdq:`) used in expressing the Test specifications;
- A validation dataset for confirming the expected behavior of Test implementations;
- Guides for implementing the Tests and interpreting their results;
- A guide to understanding and applying the Framework Ontology.

While not part of the BDQ Core standard, a validated Java® implementation and exemplar datasets demonstrate practical usage and conformance.

This document also explains BDQ Core’s underlying principle: data quality is not an inherent property but is relative to a specific purpose or use case. The concept of ‘fitness for use’ drives how Tests are applied and interpreted. BDQ Core enables users to define, compose, and apply Tests aligned with different uses, recognizing that data quality must be evaluated within context.

### 1.2 Audience

This document is intended for a broad audience, including:

- Practitioners interested in improving or assessing the quality of biodiversity data;
- Developers of tools and pipelines for data validation;
- Researchers and project leads evaluating the suitability of datasets;
- Standards developers seeking formal approaches to fitness-for-use assessment.

No technical or ontological expertise is required to understand this document. It provides a conceptual foundation for exploring the rest of the BDQ Core suite, whether for casual use or deep integration.

### Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality Core](../../index.md) page, which lists the parts of the standard.

### 1.4. Status of the Content of This Document

Section 3 of this document is normative. 

All other sections of this document are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.5 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.6 Namespace Abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |

## 2 Introduction to the BDQ Core Standard 

### 2.1 Parts of the Standard

The full set of documents comprising the BDQ Core standard is listed on the [Biodiversity Data Quality Core](../../index.md) landing page.

### 2.2 Vocabularies

The focus of this standard is on (1) a framework for describing data quality and (2) the description of a set of Tests and assertions using that framework. The framework is instantiated formally as an ontology (namespace abbreviation `bdqffdq:`). The Tests are instantiated formally as a vocabulary (namespace abbreviation `bdqcore:`), with Test names, labels, descriptions, expected responses and other metadata expressed with bdqffdq: and other vocabularies. Four additional vocabularies used in defining the Tests are defined by this standard. Together the vocabularies serve to support the specification of suites of biodiversity data quality assessments and amendments to improve data for particular purposes. Each vocabulary is described in full in its distinct Term List document, linked from and summarized together on the [BDQ Core List of Vocabularies](../vocabularies/index.md). 

### 2.3 Test Guidance

Beyond data availability, data quality is probably the most significant issue for users of biodiversity data. The BDQ Core standard suite of Tests and assertions is meant to be used by data collectors, data providers, and data users to assess and potentially improve data quality.

The Fitness for Use Framework upon which BDQ Core is based allows pipelines of Tests and assertions to have formal dependencies between them, such as a specified order in which they should be run in order to get a deterministic result, or using the results of some Tests as the inputs to other Tests, or building composite Tests from other existing Tests. By design, dependencies are manifest in some of the Tests and assertions that are Measures, while Tests and assertions that are Issues, Validations, and Amendments tend to be independent of each other.

Tests, even Amendments, do not modify original data. Instead, Amendment Test responses contain the information needed to amend original data by providing reproducible interpretations. These interpretations can be as a substitute for the original data downstream in analytical pipelines, or can be used to vet and amend the original data, as appropriate.

Test specifications for Tests, _sensu latu_, consist of the metadata (e.g., identifier, preferred label, description, Information Elements acted upon, Information Elements consulted, expected response, data quality dimension, parameters and default behavior, and notes) required to understand the Test, its context, and its potential uses, and to implement it in a way that is compliant with the standard.

The specifications for Tests, _sensu strictu_, include expected responses from Tests that consist of metadata (status, result, and comment) required for a user to interpret and act upon the data (Information Elements) pertinent to the Test that was run, whether the Information Elements were those consulted or those acted upon.

### 2.4 Test Lists

The [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md) is an simple, easy-to-read reference to the Tests defined in BDQ Core. The fully detailed normative term lists can be found in the following documents:
[BDQ Core Tests and Assertions List of Terms](../list/bdqcore/index.md)
[Biodiversity Data Quality Controlled Vocabulary List of Terms](../list/bdq/index.md)
[Data Quality Dimension Controlled Vocabulary List of Terms](../list/bdqdim/index.md)
[Data Quality Criterion Controlled Vocabulary List of Terms](..list/bdqcrit/index.md)
[Data Quality Enhancement Controlled Vocabulary List of Terms](../list/bdqenh/index.md)
[Fitness For Use Framework Ontology List of Terms](../list/bdqffdq/index.md)

### 2.5 Guides and other documents. 

The [BDQ User's Guide](../guide/users/index.md) is intended to contain everything needed to understand the nature or the Tests and the responses from them when they are run. It is intended to be accompanied by the [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md).

The [BDQ Implementer's Guide](../guide/implementers/index.md) is intended to contain everything needed to understand the requirements for compliant implementations of the Tests. 

The [Fitness For Use Framework Ontology Guide](../guide/bdqffdq/index.md) describes how the Framework Ontology (bdqffdq:) is used to describe the BDQ Core Tests, and can be used to describe new Tests or new compositions of Tests for new uses. The ontology is also intended to allow Test results to be represented as linked open data or in W3C oa:Annotations. 

The document [BDQ Core: Identifying Synthetic and Modified Data](../synthetic/index.md) describes how to mark synthetic and altered data that may be used to validate Test implementations to distinguish it from real data.

### 2.6 Implementation Validation Data 

See the [BDQ Implementer's Guide](../guide/implementers/index.md) for information on a set of data for validating Test implementations.

### 2.7 Test Execution Environments and Workflows

Neither the Test descriptions nor the framework impose constraints on environments or workflows for execution. One possible workflow is to run all validations, then all amendments, then all validations again on a modified copy of the input data to which all proposed amendments have been applied.

A single validation step, with measures evaluating the results of the amendments could look like the diagram below.

![Diagram of workflow through single validation step](workflow_single_iteration.svg)

Expanding on this single validation step, amendments can be run and their results fed back into a second phase of post-amendment validation, with measures again evaluating the results of validation of the input data if all changes proposed by amendments are accepted. Presentation of a data quality report would be an expected result from this workflow for Quality Control purposes, while using the Measures in the second step to filter data in a processing pipeline to just those that are fit for purpose for a particular use would be expected for Quality Assurance purposes.

![Diagram of workflow with pre-amendment validation+measure phase, followed by amendment phase, followed by post-amendment validation-measure phase](workflow_two_iterations.svg)

### 2.8 Implementations of Tests "In the Wild"

Not part of the BDQ Core standard, but implemented as part of the process of writing the standard, are a set of Java implementations of the BDQ Core Tests that pass when Tested with the validation data. See [9 Existing Test Implementations](../guide/implementers/index.md/#9-Existing-Test-Implementations-non-normative) in the [BDQ Implementer's Guide](../guide/implementers/index.md) for details.

Additional code is available to help support the implementation of Tests and the use of bdqcore, dwc, and bdqffdq terms in rdf. See the discussion in section [8.6 Existing Software tools](../guide/implementers/index.md/#86-existing-software-tools-non-normative) of the [BDQ Implementer's Guide](../guide/implementers/index.md).

<!--- TODO: note partial implementations in iDigBio, ALA, OBIS, GBIF, and R packages --->

## 3 Design of the Tests (normative)

<!--- PJM: Section 3 is Important (largely permissive) elements that are needed in the introduction --->

### 3.1 Data Quality Control, Data Quality Assurance (normative)

BDQ Core draws a distinction between Quality Control and Quality Assurance. Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data. Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose. Implementations of the bdqcore Tests MAY be used to perform Quality Control, Quality Assurance, or both. The [mathematical formalization](..//bdqffdq/index.md#5-fitness-for-use-framework-summary-of-mathematical-formalization-normative) of the bdqffdq Framework provides a formal definition of Quality Control and Quality Assurance, and how Test Assertions SHOULD be used for each.

### 3.2 When are Tests Run (normative)

The bdqcore Tests are designed to be run at any point in the life cycle of biodiversity data. They MAY be run at the point of initial collection or observation of organisms. They MAY be run to support data transcription. They MAY be run in loading data into databases of record from field or transcription sources. They MAY be run in preparing data from databases of record for aggregation. They MAY be run during data aggregation and the presentation of aggregated data. They MAY be run in workflows for analysis of data for research purposes.

### 3.3 Results of Test Executions (normative)

BDQ Core is agnostic about the format of presentation of results from BDQ Core Tests. BDQ Core does, however, specify that Test implementations and presentations MUST return structured data with at least bdq:Response.status, bdq:Response.result, and bdq:Response.comment. Responses MAY also contain more information in Response.qualifier.
See the [Implementer's Guide](../guide/implementers/index.md) section on [Presentation of Results](../guide/implementers/index.md#7-Presentation-of-Results) for further normative and non-normative guidance about result presentation. See the [BDQ Core Tests and Assertions](../bdqcore/index.md) landing page section on the [Structure of a Response](../bdqcore/index.md#31-Structure-of-Response-normative) for normative guidance on Responses as RDF or as data structures.

The results of the execution of implementations of the bdqcore: Tests MAY be presented as Data Quality reports. The Framework Ontology provides vocabulary and structure that MAY be used for such data quality reports.

The bdqffdq: vocabulary enables the wrapping of the results of bdqcore: Tests within annotations. The bdqffdq: vocabularies in particular are intended to support the framing of assertions from Tests within annotations that follow the W3C Web Annotation Data Model (Sanderson et al. 2017), and are suitable for inclusion in semantic data stores. See the [Implementer's Guide](../guide/implementers/index.md) section on [Annotations](../guide/implementers/index.md#72-Annotations-normative) for more guidance.

## 4 Contributions and Acknowledgments

### 4.1 Acknowledgments

The Authors gratefully acknowledge all those who have commented on the GitHub issues during the development of BDQ Core, and all those who have contributed to discussions at various workshops in São Paulo, Brazil; Canberra, Australia; Monash, Australia; Leiden, The Netherlands; Gainesville, USA; and Seattle, USA, and at Biodiversity Information Standards (TDWG) annual meetings (in Jönköping, Sweden; Santa Clara de San Carlos, Costa Rica; Ottawa, Canada; Dunedin, New Zealand; Leiden, The Netherlands; Sofia, Bulgaria; Hobart, Australia; and Ginowa, Japan; and the various virtual meetings). The Authors are also grateful for all those who responded to our email questions.

We'd also gratefully acknowledge the continued support of the Biodiversity Information Standards (TDWG) Executive over the 10 years of this project.

#### 4.1.1 Funding and Support for Meetings

We acknowledge the financial support of The Atlas of Living Australia and Biodiversity Information Standards (TDWG) for Lee Belbin and Arthur Chapman to attend two face-to-face meetings for the development of BDQ Core, and the Atlas of Living Australia for support of John Wieczorek to attend meetings in Canberra Australia. The Museum of Comparative Zoology provided support for Paul Morris; VertNet, Kurator, and Rauthflor LLC provided support for John Wieczorek. The United States National Science Foundation through funding of the Kurator project, provided time for Paul Morris, Robert Morris and David Lowery for early work on the project.

The São Paulo Research Foundation (FAPESP), the Universidade de São Paulo (USP) provided facilities, and with the Global Biodiversity Information Facility and others, supported participants to attend the meeting in São Paulo, Brazil. The US National Science Foundation through iDigBio provided support for the meeting in Gainesville, Florida.

### 4.2 Contributions

Many people have contributed valuable comments through the development of the BDQ Core standard.

#### 4.2.1 Authors 

We recognize four people as authors of the standard, having contributed consistently over the last decade and having been heavily engaged in writing the core Test Descriptors and the BDQ Core documentation. 

- **Lee Belbin (Blatant Fabrications Pty Ltd)**: Convener of TDWG Data Quality Task Group 2 (Data Quality Tests and Assertions); Test descriptions; author of BDQ Core documents; Test Validation Data.
- **Arthur D Chapman (Australian Biodiversity Information Services)**: Co-convener of the TDWG Data Quality Interest Group; Test descriptions; author of BDQ Core documents; vocabularies. 
- **Paul J Morris (Museum of Comparative Zoology, Harvard University)**: Test descriptions; bdqffdq ontology; Java Test implementations in filteredpush packages; author of BDQ Core documents; Test Validation Data. 
- **John Wieczorek (Rauthiflor LLC)**: Test descriptions; Test implementations; author of BDQ Core documents; Darwin Core liaison.

#### 4.2.2 Contributors

There were many people who have made notable contributions at various times during the development of BDQ Core.
 
- **Paula F. Zermoglio (Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN), San Carlos de Bariloche)**: Convener of TDWG Data Quality Task Group 4 (Best Practices for Development of Vocabularies of Value); Test descriptions; vocabulary development.
- **Alexander Thompson (iDigBio)**: Key contributions to initial development of Test descriptors; migrated Test descriptors into markdown tables in GitHub issues.
- **Yi-Ming Gan (Royal Belgian Institute of Natural Sciences)**: Contributed to Test evaluation; explanatory workflow diagrams; editing BDQ Core documents.
- **António Mauro Saraiva (Universidade de São Paulo)**: Co-convenor of the TDWG Data Quality Interest Group; development of the Framework for Data Quality (TDWG Data Quality Task Group 1); facilitated Test development workshop.
- **Allan Koch Veiga (Universidade de São Paulo)**: Developed the Framework on Data Quality as his doctoral dissertation (Veiga 2016), Convener of the TDWG Data Quality Task Group 1 (Framework for Data Quality).
- **David Lowery (Museum of Comparative Zoology, Harvard University)**: Initial development of ontology representation of Framework on Data Quality; developer of kurator-ffdq Java class representation of the Framework.
- **Christian Gendreau (Agriculture and Agri-Food Canada)**: Initial contributions to data quality discussions; vocabulary definitions and early Test development.
- **Tim Robertson (Global Biodiversity Information Facility)**: Contributions to Test descriptions; clarification of GBIF vocabulary and API resources for the BDQ Core Tests.
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
| TG4         | [Biodiversity Data Quality Interest Group - Task Group 4: Best Practices for Development of Vocabularies of Values](https://github.com/tdwg/bdq/tree/master/tg4) |

## 6 Glossary

### 6.1 Term-Action

A Test label reflects its Test type, the bdqffdq:InformationElement the Test acts upon, and the nature of the evaluation that is being done. The Test type is one of Validation, Issue, Amendment or Measure. The term action is the combination of the bdqffdq:InformationElement and the nature of the evaluation. For example, the Test with the label "VALIDATION_COUNTRYCODE_STANDARD" has the type "Validation"", the bdqffdq:InformationElement "dwc:countryCode" and the nature of the evaluation "STANDARD". Following is a table of distinct values for the nature of the evaluation part of the term-action, along with a definition and a usage comment with examples.

| Label | Definition | Comment | Example |
| ---- | ---- | ---- | ---- |
| ASSUMEDDEFAULT | A bdqffdq:Amendment that replaces a bdq:EMPTY term with a predefined default bdq:Parameter value. | This action is used in Tests and in bdq:Response.comments. bdq:Response.status value for this case is bdq:AMENDED. | [AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](https://rs.tdwg.org/bdqcore/terms/7498ca76-c4d4-42e2-8103-acacccbdffa7) |
| CENTREOFCOUNTRY | Testing if bdqffdq:EnformationElements COORDINATES identify the center of the dwc:country, allowing for a spatial buffer. | | [ISSUE_COORDINATES_CENTEROFCOUNTRY](https://rs.tdwg.org/bdqcore/terms/256e51b3-1e08-4349-bb7e-5186631c3f8e) |
| COMPLETE | Testing if the bdqffdq:InformationElement dwc:scientificNameId forms a valid and complete identifier. | Testing for bdqdim:Completeness. | [VALIDATION_SCIENTIFICNAMEID_COMPLETE](https://rs.tdwg.org/bdqcore/terms/6eeac3ed-f691-457f-a42e-eaa9c8a71ce8) |
| CONSISTENT | Identifies consistency among values between bdqffdq:InformationElements. | Testing for bdqdim:Consistency. | [VALIDATION_CLASSIFICATION_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/2750c040-1d4a-4149-99fe-0512785f2d5f) |
| COORDINATESTERRESTRIALMARINE | A terrestrial taxon that has geographic coordinates that fall within terrestrial boundaries, or a marine taxon that has geographic coordinates that fall within marine boundaries. | Use bdq:AMENDED as the bdq:Response.status, report bdq:COORDINATESTERRESTRIALMARINE in a bdq:Response.qualifier or in a bdq:Response.comment. | [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b9c184ce-a859-410c-9d12-71a338200380) |
| DURATIONINSECONDS | The duration in seconds of the bdq:InformationElement dwc:eventDate. | | [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53) |
| FOUND | The value in a bdqffdq:InformationElement that matched a value in a bdq:sourceAuthority. | Use bdq:COMPLIANT for bdq:Response.result, and include this in bdq:Response.comments or bdq:Response.qualifier. | [VALIDATION_STATEPROVINCE_FOUND](https://rs.tdwg.org/bdqcore/terms/4daa7986-d9b0-4dd5-ad17-2d7a771ea71a) |
| FROM | An Output bdqffdq:InformationElement is being populated from a more primary Input bdqffdq:InformationElement. | Populates dwc:scientificName from dwc:scientificNameId. | [AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](https://rs.tdwg.org/bdqcore/terms/f01fb3f9-2f7e-418b-9f51-adf50f202aea) |
| INRANGE | The value of bdqffdq:InformationElements that are within an acceptable range. | Use in bdq:Response.qualifier or bdq:Response.comment. | [VALIDATION_MAXDEPTH_INRANGE](https://rs.tdwg.org/bdqcore/terms/3f1db29a-bfa5-40db-9fd1-fde020d81939) |
| LESSTHAN | A Term-Action indicating that the value in one bdq:InformationElement is less than the value in another bdq:InformationElement. | Used in Tests for Depth and Elevation. | [VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH](https://rs.tdwg.org/bdqcore/terms/8f1e6e58-544b-4365-a569-fb781341644e) |
| NOTEMPTY | An bdqffdq:InformationElement contains a non-empty value | | [VALIDATION_EVENTDATE_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/f51e15a6-a67d-4729-9c28-3766299d2985) |
| PREREQUISITESNOTMET | A Test of type bdqffdq:Measure that counts the number of Tests of type bdqffdq:Validation that did not run due to one or more prerequisites not being met (bdq:INTERNAL_PREREQUISITES_NOT_MET or EXTERNAL_PREREQUISITES_NOT_MET). | | [MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](https://rs.tdwg.org/bdqcore/terms/49a94636-a562-4e6b-803c-665c80628a3d) |
| PROPOSED | A Test of type bdqffdq:Measure that counts the number of bdqffdq:Amendments where an action to modify a value in some way through a change or addition is proposed. | | [MEASURE_AMENDMENTS_PROPOSED](https://rs.tdwg.org/bdqcore/terms/03049fe5-a575-404f-b564-ae63f5a1cf8b) |
| STANDARD | A bdqffdq:Validation Test where a value in a bdqffdq:InformationElement matches a bdq:STANDARD value in a bdq:sourceAuthority. | Use in bdq:Response.qualifier or bdq:Response.comment. | [VALIDATION_TAXONRANK_STANDARD](https://rs.tdwg.org/bdqcore/terms/7bdb13a4-8a51-4ee5-be7f-20693fdb183e) |
| STANDARDIZED | A bdqffdq:Amendment where a bdq:STANDARD value for a bdqffdq:InformationElement is proposed. | Use bdq:AMENDED as the bdq:Response.status, report bdq:STANDARDIZED in a bdq:Response.qualifier or in a bdq:Response.comment. | [AMENDMENT_TAXONRANK_STANDARDIZED](https://rs.tdwg.org/bdqcore/terms/e39098df-ef46-464c-9aef-bcdeee2a88cb) |
| TRANSPOSED | A bdqffdq:Amendment where the sign and/or value of one or more bdqffdq:InformationElements were proposed to be swapped. | Use bdq:AMENDED as the bdq:Response.status, report bdq:TRANSPOSED in a bdq:Response.qualifier or in a bdq:Response.comment. | [AMENDMENT_COORDINATES_TRANSPOSED](https://rs.tdwg.org/bdqcore/terms/f2b4a50a-6b2f-4930-b9df-da87b6a21082) |
| UNAMBIGUOUS | A combination of bdqffdq:InformationElements is unambiguous in that they align to a unique result given a reference or a Source Authority (bdq:sourceAuthority). | | [VALIDATION_TAXON_UNAMBIGUOUS](https://rs.tdwg.org/bdqcore/terms/4c09f127-737b-4686-82a0-7c8e30841590) |
| VERBATIM | Refers to bdqffdq:Amendment Tests that attempt to extract explicit Darwin Core bdq:InformationElements values from Darwin Core verbatim term bdq:InformationElements. | | [AMENDMENT_EVENTDATE_FROM_VERBATIM](https://rs.tdwg.org/bdqcore/terms/6d0a0c10-5e4a-4759-b448-88932f399812) |

### 6.2 General Glossary

Glossary of terms used in BDQ Core that are in addition to those included in the various Namespace: vocabularies and Term-Actions. Note: Usage of 'Darwin Core term(s)' below refer to [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021).

| Label | Definition | Context |
| ---- | ---- | ---- |
| COORDINATES | A general category of specific bdq:InformationElements that represents the combination of the Darwin Core terms dwc:decimalLatitude and dwc:decimalLongitude and may include metadata terms including dwc:geodeticDatum. | bdqffdq:InformationElement |
| CRS | Coordinate Reference System - (also referred to as 'spatial reference system'). A coordinate system defined in relation to a standard reference or datum (Chapman & Wieczorek 2020). | Test |
| Database of record | An information system which holds an authoritative or master record of some data. Records in a database of record are held to be correct over different values for the same records that might be found in other datasets. This is in distinction from aggregated datasets, derived research dataset, datasets for portals and other holders of non-authoritative copies of the data. | BDQ Core |
| geodetic coordinate reference system | A coordinate reference system based on a geodetic datum, used to describe positions on the surface of the earth (Chapman and Wieczorek 2020). | Test |
| geodetic datum | A mathematical model that uses a reference ellipsoid to describe the size and shape of the surface of the earth and adds to it the information needed for the origin and orientation of coordinate systems on that surface (Chapman and Wieczorek 2000). | Test |
| Framework | The Fitness for Use Framework, the body of work that provides a fundamental structure for the BDQ Core Tests. The Fitness for Use Framework is derived from (Veiga 2016) and is the outcome of the TDWG Data Quality Task Group 1: Framework on Data Quality (Veiga et al. 2017). | bdqffdq: |
| Framework Ontology | A model of the Framework (Veiga 2016, Veiga et al. 2017) as an owl ontology, present as the bdqffdq: vocabulary in BDQ Core. | bdqffdq: |
| GEOGRAPHY | A general category of specific bdq:InformationElements that represents a combination of Darwin Core administrative geography terms dwc:continent, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality. | bdqffdq:InformationElement |
| Java | Java is a registered trademark of Oracle and/or its affiliates. | BDQ Core |
| [NAME](../supplement/index.md#NAME) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Taxon Class. | bdqffdq:InformationElement |
| non-printing characters | ASCII 0-32 and 127 decimal. Non-printing characters or formatting marks that are not displayed when printing. These may include pilcrow, space, non-breaking space, tab character, etc. For the purposes of the Tests they are treated as bdq:Empty. | Data |
| null | A value that is used in some databases to signify that a value is unknown or missing. It may be represented in serializations of data outside of database environments by strings such as "NULL", "Null", "null". "/n", "9999", "NA", etc. These serializations should be treated as bdq:NotEmpty. | Data |
| [OTHER](../supplement/index.md#OTHER) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms other than Classes dwc:Taxon, dwc:Location or dwc:Event. | bdqffdq:InformationElement |
| POLYNOMIAL | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet. See the Test [VALIDATION_POLYNOMIAL_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/17f03f1f-f74d-40c0-8071-2927cfc9487b). | bdqffdq:InformationElement |
| Roman numerals | Numbers written with the characters I, V, X, L, C, D, and M in the latin alphabet, each letter representing an integer and combined to form arbitrary integers. Roman numerals are interpreted as the equivalent integer for months (e.g., "X" as "10") in certain Tests. Roman numerals may not be unambiguously interpreted for other Darwin Core terms such as dwc:day or in text fields as they may mean unknown or something else entirely. | Data | 
| [SPACE](../supplement/index.md#SPACE) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Location Class. | bdqffdq:InformationElement |
| SRS | spatial reference system - see CRS (Chapman and Wieczorek 2020). | Test |
| Test | An individual consideration of a DataQualityNeed with a Method that links it to an instance of a Specification, these instances being composed of InformationElements, Arguments, and Parameters. | BDQ Core | 
| Test (technical) | A composition of an instance of a subclass of bdqffdq:DataQualityNeed (which expresses a data quality need in the abstract) with an instance of a subclass of bdqffdq:DataQualityMethod, which links it to an instance of a bdqffdq:Specification (which spells out how to concretely evaluate the need). These class instances are composed with bdqffdq:InformationElements, bdqffdq:Arguments, and bdqffdq:Parameters. For example, the Test [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134).| BDQ Core | 
| TestField | Column heading in the markdown of the Tests in the [tdwg/bdq GitHub](https://github.com/tdwg/bdq/issues) that list all the normative and informative metadata elements that describe a Data Quality Test. | Test |
| Test Type | There are four types of Tests: Validation (bdqffdq:Validation), Amendment (bdqffdq:Amendment), Issue (bdqffdq:Issue), and Measure (bdqffdq:Measure). | Test |
| [TIME](../supplement/index.md#TIME) | A bdq GitHub label to indicate that the Test is related to Darwin Core terms in the dwc:Event Class. | bdqffdq:InformationElement |
| VERBATIM | A general category of specific bdq:InformationElements that represents a term containing an original value. | bdqffdq:InformationElement |
| whitespace | Characters such as spaces and tabs that affect rendering of printed or displayed output, but which themselves are not printed. 1) A field that only includes whitespace is treated as bdq:Empty. 2) In bdqffdq:Validation Tests that require the look up of a bdq:sourceAuthority, leading and/or trailing whitespace will cause the Test to fail as no pre-processing is carried out on the data. These leading and trailing whitespaces may be stripped out in a subsequent bdqffdq:Amendment and thus pass when the bdqffdq:Validation Test is run again. | Data |
| YEARMONTHDAY | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:month, dwc:day. | bdqffdq:InformationElement |
| YEARSTARTDAYOFYEARENDDAYOFYEAR | A general category of specific bdq:InformationElements that represents a combination of the Darwin Core terms dwc:year, dwc:startDayOfYear, dwc:endDayofYear. | bdqffdq:InformationElement |

## 7 References

{references}
