<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Data Quality Criterion Controlled Vocabulary List of Terms

**Title**<br>
Data Quality Criterion Controlled Vocabulary List of Terms

**Date version issued**<br>
2025-04-11

**Date created**<br>
2025-04-11

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqcrit

**This version**<br>
<http://rs.tdwg.org/bdq/bdqcrit/terms/2025-04-11>

**Latest version**<br>
<http://rs.tdwg.org/bdq/bdqcrit/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ standard. It covers the vocabulary terms that are types of bdqffdq:Criterion (originally defined in Veiga 2016 and Veiga et al. 2017) and form the controlled vocabulary for bdqffdq:hasCriterion.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Criterion Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqcrit/terms/2025-04-11>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Audience](#12-audience)
  - [1.3 Data Quality Criteria](#13-data-quality-criteria)
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

[Cite BDQ](#cite-bdq)

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to provide the full term list for the `bdqcrit:` controlled vocabulary, which defines the values of `bdqffdq:Criterion` used in BDQ Tests. Each `Criterion` represents an abstract way of evaluating whether a data value meets expectations for a particular `Use Case`.

These terms are central to describing the logic of BDQ `Validation` and `Issue` Tests. They express the general kind of judgment being applied to a data value (e.g., whether it is complete, found, or unambiguous), helping users understand what each Test is assessing in a formalized way.

### 1.2 Audience

This document is intended for users who need a technical understanding of how BDQ Tests apply evaluation logic through the use of `Criteria`. It is especially useful for:

- Implementers interpreting or building Tests that rely on data quality criteria
- Standards developers and data quality modelers applying the Fitness for Use Framework Ontology
- Analysts and curators needing to understand the conceptual basis for Test evaluations

A working familiarity with the BDQ Test structure and the Fitness for Use Framework Ontology is helpful, though not required to benefit from this document.

### 1.3 Data Quality Criteria

The concept of `bdqffdq:Criterion` — originally defined by Veiga (2016) and Veiga et al. (2017) — describes, in abstract terms, how a data value may be evaluated with respect to a particular `Use Case`. `Criteria` such as `Found`, `InRange`, `NotEmpty`, `Unambiguous`, and others express broad evaluation patterns that BDQ `Validation` and `Issue` Tests apply to one or more `bdqffdq:InformationElements`.

While related informally to `bdqffdq:Dimensions`, `Criteria` serve a distinct purpose. A `bdqffdq:Criterion` articulates the *type of judgment* applied to data, whereas a `bdqffdq:Specification` captures the *specific logic* used to make that judgment.

Each `bdqtest:` `Validation` or `Issue` Test references a `Criterion` to clarify what kind of quality is being assessed. For example, the Test VALIDATION_COUNTRY_FOUND evaluates the value of `dwc:country` against a specified `sourceAuthority`, using the `Criterion` `bdqcrit:Found` to indicate that the key  quality concern is whether the value exists in the authority’s domain.

### 1.4 Associated Documents

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.5 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqcrit/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdqcrit/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/bdqcrit.xml | Example for submission, to be generated | 

### 1.6 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

Section [1.9 Key to Vocabulary Terms](#19-key-to-vocabulary-terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.7 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.8 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.9 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/) (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | Complete |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqcrit/terms/ Complete](https://rs.tdwg.org/bdqcrit/terms/Complete) |
| Modified (dcterms:issued) | normative | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2024-09-30 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqcrit/terms/ Complete-2024-09-30](https://rs.tdwg.org/bdqcrit/terms/Complete-2024-09-30) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Complete |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | Data are present and sufficiently comprehensive for use. |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use.  Corresponding dimension is bdqdim:Completeness |
| Status (tdwgutility:status) |  | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |
| Controlled Value String () | normative |  | Complete |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:Criterion |


## 2 Use of Terms (normative)

A value for `bdqffdq:hasCriterion` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqcrit/terms/NotEmpty`) or Term Qualified name (e.g., `bdqcrit:NotEmpty`) from the `bdqcrit:` namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `NotEmpty`) MAY be used. In a purely human context a label (e.g., `Not Empty`) MAY be used.

Each instance of `bdqffdq:Validation` and `bdqffdq:Issue` SHOULD have exactly one `bdqffdq:hasCriterion` property relating it to a term in this `bdqcrit:` vocabulary.

An instance of `bdqffdq:Measure` or `bdqffdq:Amendment` SHOULD NOT have a `bdqffdq:hasCriterion` property relating it to a term in this `bdqcrit: vocabulary`.

## 3 Term index
### 3.1 Index By Term Name

(See also [3.2 Index By Label](#32-index-by-label))

**Classes**

**Vocabulary**

[bdqcrit:Complete](#bdqcrit_Complete) |
[bdqcrit:Consistent](#bdqcrit_Consistent) |
[bdqcrit:Found](#bdqcrit_Found) |
[bdqcrit:InRange](#bdqcrit_InRange) |
[bdqcrit:Likely](#bdqcrit_Likely) |
[bdqcrit:NotEmpty](#bdqcrit_NotEmpty) |
[bdqcrit:Standard](#bdqcrit_Standard) |
[bdqcrit:Unambiguous](#bdqcrit_Unambiguous) 

### 3.2 Index By Label

(See also [3.1 Index By Term Name](#31-index-by-term-name))

**Classes**

[Complete](#bdqcrit_Complete) |
[Consistent](#bdqcrit_Consistent) |
[Found](#bdqcrit_Found) |
[In Range](#bdqcrit_InRange) |
[Likely](#bdqcrit_Likely) |
[Not Empty](#bdqcrit_NotEmpty) |
[Standard](#bdqcrit_Standard) |
[Unambiguous](#bdqcrit_Unambiguous) 

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_Complete"></a>Term Name  bdqcrit:Complete</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Complete">https://rs.tdwg.org/bdqcrit/terms/Complete</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Complete-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/Complete-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Complete</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data are present and sufficiently comprehensive for use.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use.  Corresponding dimension is bdqdim:Completeness</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Complete</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_Consistent"></a>Term Name  bdqcrit:Consistent</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Consistent">https://rs.tdwg.org/bdqcrit/terms/Consistent</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Consistent-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/Consistent-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data are internally consistent and consistent with any authorities consulted. </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>A set of bdqffdq:InformationElements and bdq:sourceAuthorities are consistent.   Corresponding dimension is bdqdim:Consistency</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Consistent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_Found"></a>Term Name  bdqcrit:Found</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Found">https://rs.tdwg.org/bdqcrit/terms/Found</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Found-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/Found-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data conform to the values in an authority.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement conform to a bdq:sourceAuthority.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Found</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_InRange"></a>Term Name  bdqcrit:InRange</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/InRange">https://rs.tdwg.org/bdqcrit/terms/InRange</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/InRange-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/InRange-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>In Range</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data conform to an expected range of values.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement conform to an expected range of values.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>InRange</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_Likely"></a>Term Name  bdqcrit:Likely</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Likely">https://rs.tdwg.org/bdqcrit/terms/Likely</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Likely-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/Likely-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Likely</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data are likely to be true or expected values.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement is likely to be true or expected values.  Corresponding dimension is bdqdim:Likeliness</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Likely</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_NotEmpty"></a>Term Name  bdqcrit:NotEmpty</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/NotEmpty">https://rs.tdwg.org/bdqcrit/terms/NotEmpty</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/NotEmpty-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/NotEmpty-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Not Empty</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Some data value is present.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Some value is present in a bdqffdq:InformationElement.  Corresponding dimension is bdqdim:Completeness.   See also bdq:EMPTY and bdq:NOT_EMPTY</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_Standard"></a>Term Name  bdqcrit:Standard</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Standard">https://rs.tdwg.org/bdqcrit/terms/Standard</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Standard-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/Standard-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data conform to a format, syntax, data type, or standard.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement conform to a format, syntax, data type, or standard.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Standard</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqcrit_Unambiguous"></a>Term Name  bdqcrit:Unambiguous</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Unambiguous">https://rs.tdwg.org/bdqcrit/terms/Unambiguous</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqcrit/terms/Unambiguous-2024-09-30">https://rs.tdwg.org/bdqcrit/terms/Unambiguous-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Unambiguous</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data adequately identify a unique entity.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement adequately identifies a unique entity.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Unambiguous</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Criterion</td>
		</tr>
	</tbody>
</table>


## Acronyms

A list of Acronyms can be found in the [Acronyms](../../index.md#5-acronyms) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary

A glossary of terms additional to those in the various namespaces can be found in the [Glossary](../../index.md#6-glossary) section of the Biodiversity Data Quality (BDQ) landing page.

## References

The references for the BDQ standard can be found in the [References](../../index.md#7-references) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Criterion Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqcrit/terms/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
