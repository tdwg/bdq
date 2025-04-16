<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Data Quality Enhancement Controlled Vocabulary List of Terms

**Title**<br>
Data Quality Enhancement Controlled Vocabulary List of Terms

**Date version issued**<br>
2025-04-11

**Date created**<br>
2025-04-11

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqenh

**This version**<br>
<http://rs.tdwg.org/bdq/bdqenh/terms/2025-04-11>

**Latest version**<br>
<http://rs.tdwg.org/bdq/bdqenh/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ Core Standard. It covers the vocabulary terms that are types of bdqffdq:Enhancement (originally defined in Veiga 2016 and Veiga et al. 2017) and form the controlled vocabulary for bdqffdq:hasEnhancement.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Enhancement Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqenh/terms/2025-04-11>

**Comment**<br>
Draft Standard for Review

## Table of Contents ##
[1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Audience](#12-audience)
  - [1.3 Data Quality Enhancements](#13-data-quality-enhancements)
  - [1.4 Associated Documents](#14-associated-documents)
  - [1.5 Term List Distributions](#15-term-list-distributions)
  - [1.6 Status of the content of this document](#16-status-of-the-content-of-this-document)
  - [1.7 RFC 2119 key words](#17-rfc-2119-key-words)
  - [1.8 Namespace abbreviations](#18-namespace-abbreviations)
  - [1.9 Key to Vocabulary Terms](#19-key-to-vocabulary-terms)

[2 Use of Terms (normative)](#2-use-of-terms-normative)

[3 Term index](#3-term-index)
  - [3.1 Index By Term Name](#31-index-by-term-name)
  - [3.2 Index By Label](#32-index-by-label)

[4 Vocabulary](#4-vocabulary)

[Acronyms](#acronyms)

[Glossary](#glossary)

[References](#references)

[Cite BDQ Core](#cite-bdq-core)

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to provide the full term list for the `bdqenh:` controlled vocabulary, which defines the values of `bdqffdq:Enhancement` used in BDQ Core Amendment Tests. Each Enhancement describes a general strategy by which data may be modified or supplemented to improve its quality in alignment with a specified Use Case.

These terms support the formal description of how Amendments propose changes to data and clarify the intended nature of those proposals.

### 1.2 Audience

This document is intended for users who need a technical understanding of how BDQ Core Amendment Tests describe proposed improvements to data. It will be especially useful for:

- implementers developing systems that generate or evaluate data quality Amendments
- standards developers and data quality modelers working with the BDQ Core Framework Ontology
- analysts and Data Curators reviewing Test results in the context of proposed changes to datasets

Some familiarity with the structure of BDQ Core Tests and the Framework Ontology is recommended.

### 1.3 Data Quality Enhancements

The concept of `bdqffdq:Enhancement`, as defined by Veiga (2016) and Veiga et al. (2017), captures the general nature of a proposed change intended to improve data quality. Examples of Enhancements include `AssumedDefault`, `Converted`, `From`, `Standardized`, and `Transposed`. These represent high-level categories of amendment strategies.

Enhancements describe, in abstract terms, what a `bdqffdq:Specification` expresses concretely. While Enhancements are informally related to Data Quality Dimensions (e.g., a `Standardized` enhancement might relate to `Conformance`), those relationships are not formally encoded.

Each `bdqffdq:Amendment` Test in `bdqcore:` proposes a change to one or more data values (`bdqffdq:InformationElements`) based on a specific Enhancement. For example, the Test [`AMENDMENT_EVENTDATE_STANDARDIZED`](https://rs.tdwg.org/bdqcore/terms/718dfc3c-cb52-4fca-b8e2-0e722f375da7) evaluates the term `dwc:eventDate` and may propose a revised value formatted according to the ISO 8601 standard. The Enhancement in this case is `bdqenh:Standardized`.

Enhancements are only applicable to Tests of type `bdqffdq:Amendment`.

### 1.4 Associated Documents

For the list and links to all associated documents see the [Biodiversity Data Quality (BDQ) Core](../../index.md) page, which lists the parts of the standard.

### 1.5 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | ------------ | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqenh/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdqenh/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/bdqenh.xml | Example for submission, to be generated | 

### 1.6 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.9 Key to Vocabulary Terms](#19-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.7 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.8 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms            |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.9 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | AssumedDefault |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqenh/terms/ AssumedDefault](https://rs.tdwg.org/bdqenh/terms/AssumedDefault) |
| Modified (dcterms:issued) | normative | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2024-09-30 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqenh/terms/ AssumedDefault-2024-09-30](https://rs.tdwg.org/bdqenh/terms/AssumedDefault-2024-09-30) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Assumed Default |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | Data could be improved by setting an empty value to a default value |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in with a default value.  Corresponding dimension is bdqdim:Completeness |
| Status (tdwgutility:status) |  | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |
| Controlled Value String () | normative |  | AssumedDefault |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:Enhancement |


## 2 Use of Terms (normative) 

A value for `bdqffdq:hasEnhancement` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqenh/terms/AssumedDefault`) or Term Qualified name (e.g., `bdqdim:AssumedDefault`) from the bdqenh: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `AssumedDefault`) MAY be used. In a purely human context a Label (e.g., `Assumed Default`) MAY be used.

Each instance of bdqffdq:Amendment SHOULD have exactly one bdqffdq:hasEnhancement property relating it to a term in this bdqenh: vocabulary.

An instance of bdqffdq:Validation, bdqffdq:Issue, or bdqffdq:Measure SHOULD NOT have a bdqffdq:hasEnhancement property relating it to a term in this bdqenh: vocabulary.

## 3 Term index
### 3.1 Index By Term Name

(See also [3.2 Index By Label](#32-index-by-label))

**Classes**

**Vocabulary**

[bdqenh:AssumedDefault](#bdqenh_AssumedDefault) |
[bdqenh:Converted](#bdqenh_Converted) |
[bdqenh:FilledInFrom](#bdqenh_FilledInFrom) |
[bdqenh:Standardized](#bdqenh_Standardized) |
[bdqenh:Transposed](#bdqenh_Transposed) 

### 3.2 Index By Label

(See also [3.1 Index By Term Name](#31-index-by-term-name))

**Classes**

[Assumed Default](#bdqenh_AssumedDefault) |
[Converted](#bdqenh_Converted) |
[Fill In From](#bdqenh_FilledInFrom) |
[Standardized](#bdqenh_Standardized) |
[Transposed](#bdqenh_Transposed) 

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_AssumedDefault"></a>Term Name  bdqenh:AssumedDefault</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/AssumedDefault">https://rs.tdwg.org/bdqenh/terms/AssumedDefault</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/AssumedDefault-2024-09-30">https://rs.tdwg.org/bdqenh/terms/AssumedDefault-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Assumed Default</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by setting an empty value to a default value</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in with a default value.  Corresponding dimension is bdqdim:Completeness</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>AssumedDefault</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_Converted"></a>Term Name  bdqenh:Converted</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Converted">https://rs.tdwg.org/bdqenh/terms/Converted</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Converted-2024-09-30">https://rs.tdwg.org/bdqenh/terms/Converted-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Converted</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by converting from one representation to another</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>As in spatial coordinate transformations.  Data in a bdqffdq:InformationElement that do not conform to some specification may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Converted</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_FilledInFrom"></a>Term Name  bdqenh:FilledInFrom</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/FilledInFrom">https://rs.tdwg.org/bdqenh/terms/FilledInFrom</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/FilledInFrom-2024-09-30">https://rs.tdwg.org/bdqenh/terms/FilledInFrom-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fill In From</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by using one data value to fill in the empty value in another</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>As in filling in from verbatim terms.  Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in by interpretation of values in one or more other terms.  Corresponding dimension is bdqdim:Completeness.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>FilledInFrom</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_Standardized"></a>Term Name  bdqenh:Standardized</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Standardized">https://rs.tdwg.org/bdqenh/terms/Standardized</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Standardized-2024-09-30">https://rs.tdwg.org/bdqenh/terms/Standardized-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by conforming them to a standard representation.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement that do not conform to some format, syntax, data type, or standard may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_Transposed"></a>Term Name  bdqenh:Transposed</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Transposed">https://rs.tdwg.org/bdqenh/terms/Transposed</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Transposed-2024-09-30">https://rs.tdwg.org/bdqenh/terms/Transposed-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Transposed</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by switching values between two or more fields.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a set of at least two bdqffdq:InformationElements that do not conform to expectations may be proposed to have their values switched in order to produce conforming values.  Corresponding dimension is bdqdim:Consistency.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Transposed</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>



## Acronyms

For a list of Acronyms see [Acronyms](../../intro/index.md#5-acronyms) in the Introduction document.

## Glossary

A glossary of terms additional to those in the various namespaces can be found at [Glossary](../../intro/index.md#6-glossary) in the Introduction document.

## References

The bibliography for BDQ Core is in the [References](../../references/index.md#2-references) document.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Enhancement Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqenh/terms/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


