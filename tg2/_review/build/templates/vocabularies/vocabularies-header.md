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

Authors:
: {authors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}

### Table of Contents ###

{toc}

## 1 Introduction

This page provides an introduction and index to the six vocabularies introduced in BDQ Core. The vocabularies are distinguished by their roles within applications of the standard to biodiversity data quality (BDQ) use cases. Each vocabulary has its own namespace and term list document. 

### 1.1 Purpose

This document is an index to all the vocabularies in BDQ Core.

### 1.2 Audience

This document is for those needing a general or technical contextual overview of the BDQ Core vocabularies.

### 1.3 Associated Documents

- [Biodiversity Data Quality Core](../../index.md) provides an index to all documents in the standard.
- [BDQ Core Quick Reference Guide](../terms/bdqcore/index.md) provides an easy-to-read guide to the Tests. It is a descriptive document, not the full vocabulary definition document found in the [BDQ Core Tests and Assertions List of Terms](../list/bdqcore/index.md).

### 1.4 Status of the content of this document

This document is non-normative.

## 2 BDQ Core Vocabularies

### 2.1 Vocabularies Foundational to BDQ Core
- [BDQ Core Tests and Assertions](../bdqcore/index.md) - this vocabulary is likely to be the focus of interest for both implementers and consumers of the outputs of implementations of Tests and Assertions.  This vocabulary uses the namespace `https://rs.tdwg.org/bdqcore` (abbreviated `bdqcore:`). The specifications defined in `bdqcore:` make use of terms from the other three vocabularies defined by the standard and listed below.
- [Fitness for Use Ontology](../bdqffdq/index.md) - this vocabulary, in the form of an ontology, provides the semantics of terms that describe data quality and fitness for use in the namespace `https://rs.tdwg.org/bdqffdq` (abbreviated `bdqffdq:`), these are the terms used to describe the Tests in bdqcore:.

### 2.2 Vocabularies Supporting BDQ Core

- [BDQ Controlled Vocabulary List of Terms](../list/bdq/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdq` (abbreviated `bdq:`), which are to be used within the specifications of the Tests covered by `bdqcore:`.  Provides values for bdqffdq:Parameter and bdqffdq:UseCase. 
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
