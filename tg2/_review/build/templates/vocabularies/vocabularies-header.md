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

{toc}

## 1 Introduction

### 1.1 Purpose

The purpose of this document is to serve as the central index and orientation point for the vocabularies used in the BDQ Core standard. BDQ Core defines a set of controlled vocabularies to support consistent specification, interpretation, and implementation of data quality Tests. These vocabularies provide the formal terms used to describe aspects such as data quality dimensions, amendment strategies, and evaluation criteria.

This document distinguishes between foundational vocabularies that define the structural logic of BDQ Core and supporting vocabularies that contribute to its descriptive and operational semantics. Each vocabulary is assigned a namespace and is linked to its associated term list and RDF serialization.

### 1.2 Audience

This document is intended for both technical and non-technical readers who need to understand the structure and scope of the vocabularies within BDQ Core. It is especially useful for:

- Implementers and developers working with BDQ Core Tests who need to reference the correct vocabulary namespaces and terms
- Standards developers seeking to align external specifications with BDQ Core vocabulary structures
- Data managers or analysts looking for contextual information about terms used in BDQ Core outputs or configurations.

While the vocabulary content itself may involve semantic modeling, this index is designed to be readable without requiring specialized knowledge of RDF or ontology frameworks.

### 1.3 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality (BDQ) Core](../../index.md) page, which lists the parts of the standard.

The set of information most relevant to the vocabularies of Biodiversity Data Quality (BDQ) Core Tests can be found in the following subset of resources:

- [Biodiversity Data Quality Core](../../index.md) Provides an index to all documents in the standard.
- [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md) Provides a concise, easy-to-read reference about the BDQ Core Tests.
- [BDQ Core List of Vocabularies](../../vocabularies/index.md) A summary of the vocabularies used in the BDQ Core Tests. This document.

### 1.4 Status of the content of this document

This document is non-normative.

## 2 BDQ Core Vocabularies

### 2.1 Vocabularies Foundational to BDQ Core
- [BDQ Core Tests and Assertions](../bdqcore/index.md) - this vocabulary is likely to be the focus of interest for both implementers and consumers of the outputs of implementations of Tests and Assertions. This vocabulary uses the namespace `https://rs.tdwg.org/bdqcore` (abbreviated `bdqcore:`). The specifications defined in `bdqcore:` make use of terms from the other three vocabularies defined by the standard and listed below.
- [Fitness for Use Ontology](../bdqffdq/index.md) - this vocabulary, in the form of an ontology, provides the semantics of terms that describe data quality and fitness for use in the namespace `https://rs.tdwg.org/bdqffdq` (abbreviated `bdqffdq:`), these are the terms used to describe the Tests in bdqcore:.

### 2.2 Vocabularies Supporting BDQ Core

- [BDQ Controlled Vocabulary List of Terms](../list/bdq/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdq` (abbreviated `bdq:`), which are to be used within the specifications of the Tests covered by `bdqcore:`. Provides values for bdqffdq:Parameter and bdqffdq:UseCase. 
- [Data Quality Dimension Controlled Vocabulary List of Terms](../list/bdqdim/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqdim` (abbreviated `bdqdim:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:DataQualityDimension`. 
- [Data Quality Criterion Controlled Vocabulary List of Terms](../list/bdqcrit/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqcrit` (abbreviated `bdqcrit:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Criterion`. 
- [Data Quality Enhancement Controlled Vocabulary List of Terms](../list/bdqenh/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqenh` (abbreviated `bdqenh:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Enhancement`. 

## 3 Namespace Abbreviations

The following namespace abbreviations are used in this document: **CHECK THIS set on final draft, include only those used in this document**

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms            |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| oa:          | https://www.w3.org/TR/annotation-vocab/     |
