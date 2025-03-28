<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Core List of Vocabularies

Title
: BDQ Core List of Vocabularies

Date version issued
: 2025-03-26

Date created
: 2025-03-26

Part of TDWG Standard
: <http://example.org/to_be_determined>

Abstract
: This document is a reference for the BDQ Core Standard, listing the vocabularies included in the BDQ Core Standard.

Authors:
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Core List of Vocabularies. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2025-03-26>

Draft Standard for Submission

### Table of Contents ###

- [1 Introduction](#1-introduction)
- [1.1 Purpose](#11-purpose)
- [1.2 Audience](#12-audience)
- [1.3 Associated Documents](#13-associated-documents)
- [1.4 Status of the content of this document](#14-status-of-the-content-of-this-document)
- [2 BDQ Core Vocabularies](#2-bdq-core-vocabularies)
- [2.1 Vocabularies Foundational to BDQ Core](#21-vocabularies-foundational-to-bdq-core)
- [2.2 Vocabularies Supporting BDQ Core](#22-vocabularies-supporting-bdq-core)
- [3 Namespace Abbreviations](#3-namespace-abbreviations)


## 1 Introduction

This page provides an introduction and index to the six vocabularies introduced in BDQ Core. The vocabularies are distinguished by their roles within applications of the standard to biodiversity data quality (BDQ) use cases. Each vocabulary has its own namespace and term list document. 

### 1.1 Purpose

This document is an index to all the vocabularies in BDQ Core.

### 1.2 Audience

This document is for those needing a general contextual, or a technical understanding of the BDQ Core vocabularies.

### 1.3 Associated Documents

- [Landing page for BDQ Core](../../../index.md) provides an index to all documents in the standard.
- [BDQ Core Tests and Assertions Quick Reference Guide](../terms/bdqcore/index.md) provides an easy to read guide to the Tests (a descriptive document, not the full vocabulary definition document found in the BDQ Core Tests And Assertions List of Terms).

### 1.4 Status of the content of this document

This document is non-normative.

## 2 BDQ Core Vocabularies

### 2.1 Vocabularies Foundational to BDQ Core
- [BDQ Core Tests and Assertions Vocabulary](../bdqcore/index.md) - this vocabulary is likely to be the focus of interest for both implementers and consumers of the outputs of implementations of tests and assertions.  This vocabulary uses the namespace abbreviation `bdqcore:` for the namespace `https://rs.tdwg.org/bdqcore`. The specifications defined in `bdqcore:` make use of terms from the other three vocabularies defined by the standard and listed below.
- [Fitness For Use Framework Ontology](../bdqffdq/index.md) - this vocabulary, in the form of an ontology, provides the semantics of terms that describe data quality and fitness for use in the namespace `https://rs.tdwg.org/bdqffdq` (abbreviated `bdqffdq:`), these are the terms used to describe the tests in bdqcore:.

### 2.2 Vocabularies Supporting BDQ Core

- [Test Specification Controlled Vocabulary List of Terms](../list/bdq/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdq` (abbreviated `bdq:`), which are to be used within the specifications of the tests covered by `bdqcore:`.  Provides values for bdqffdq:Parameter and bdqffdq:UseCase. 
- [Data Quality Dimension Controlled Vocabulary List of Terms](../list/bdqdim/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqdim` (abbreviated `bdqdim:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:DataQualityDimension`. 
- [Data Quality Criteria Controlled Vocabulary List of Terms](../list/bdqcrit/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqcrit` (abbreviated `bdqcrit:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Criterion`. 
- [Data Quality Enhancement Controlled Vocabulary List of Terms](../list/bdqenh/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqenh` (abbreviated `bdqenh:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Enhancement`. 

## 3 Namespace Abbreviations

The following namespace abbreviations are used in this document: **CHECK THIS set on final draft, include only those used in this document**

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
| rdfs         | http://www.w3.org/2000/01/rdf-schema/            |
| owl          | http://www.w3.org/2002/07/owl#                   |

## Acronyms

For a list of Acronyms see [5. Acronyms](../intro/index.md#5-acronyms) in the Introduction document.

## Bibliography

The bibliography for BDQ Core is in the [Bibliography](../references/index.md#2-bibliography) document.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Core List of Vocabularies. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2025-03-26>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


