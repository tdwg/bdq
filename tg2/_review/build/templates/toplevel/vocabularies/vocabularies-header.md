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

Contributors
: {contributors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}


### Table of Contents ###

{toc}

# 1 BDQ Core Vocabularies

This page provides an introduction and index to the six vocabularies introduced by this standard. The vocabularies are distinguished by their roles within applications of the standard to biodiversity data quality (BDQ) use cases. Each vocabulary has its own namespace and term list document. 

## 1.1 Vocabularies central to BDQ Core

- [BDQ Core Tests and Assertions List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqcore_list/index.md) - this vocabulary is likely to be the focus of interest for both implementors and consumers of the outputs of implementations of tests and assertions.  This vocabulary uses the namespace abbreviation `bdqcore:` for the namespace `https://rs.tdwg.org/bdqcore`. The specifications defined in `bdqcore:` make use of terms from the other three vocabularies defined by the standard and listed below.
- [Fitness For Use Framework Ontology](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqffdq/index.md) - this vocabulary, in the form of an ontology, provides the semantics of terms that describe data quality and fitness for use in the namespace `https://rs.tdwg.org/bdqffdq` (abbreviated `bdqffdq:`), these are the terms used to describe the tests in bdqcore:.

## 1.2 Vocabularies supporting to BDQ Core

- [Test Specification Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdq/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdq` (abbreviated `bdq:`), which are to be used within the specifications of the tests covered by `bdqcore:`.  Provides values for bdqffdq:Parameter and bdqffdq:UseCase. 
- [Data Quality Dimension Controlled Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqdim/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqdim` (abbreviated `bdqdim:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:DataQualityDimension`. 
- [Data Quality Criteria Controlled Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqcrit/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqcrit` (abbreviated `bdqcrit:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Criterion`. 
- [Data Quality Enhancement Controlled Vocabulary List of Terms](../docs/list/bdqenh/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqenh` (abbreviated `bdqenh:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Enhancement`. 
