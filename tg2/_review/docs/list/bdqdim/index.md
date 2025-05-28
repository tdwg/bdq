<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Data Quality Dimension Controlled Vocabulary List of Terms

**Title**<br>
Data Quality Dimension Controlled Vocabulary List of Terms

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqdim

**This version**<br>
<http://rs.tdwg.org/bdq/bdqdim/terms/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdq/bdqdim/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ standard. It covers the vocabulary terms that are types of bdqffdq:DataQualityDimension (originally defined in Veiga 2016 and Veiga et al. 2017) and form the controlled vocabulary for bdqffdq:hasDataQualityDimension.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Dimension Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqdim/terms/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1. Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Data Quality Dimensions (non-normative)](#13-data-quality-dimensions-non-normative)
  - [1.4 Associated Documents (non-normative)](#14-associated-documents-non-normative)
  - [1.5 Term List Distributions (non-normative)](#15-term-list-distributions-non-normative)
  - [1.6 Status of the content of this document (normative)](#16-status-of-the-content-of-this-document-normative)
  - [1.7 RFC 2119 key words (normative)](#17-rfc-2119-key-words-normative)
  - [1.8 Namespace abbreviations (non-normative)](#18-namespace-abbreviations-non-normative)
  - [1.9 Key to Vocabulary Terms (normative)](#19-key-to-vocabulary-terms-normative)

[2 Use of Terms (normative)](#2-use-of-terms-normative)

[3 Term index (non-normative)](#3-term-index-non-normative)
  - [3.1 Index By Term Name (non-normative)](#31-index-by-term-name-non-normative)
  - [3.2 Index By Label (non-normative)](#32-index-by-label-non-normative)

[4 Vocabulary (normative)](#4-vocabulary-normative)

[Acronyms (non-normative)](#acronyms-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1. Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to provide the full term list for the `bdqdim:` controlled vocabulary, which defines the values of `bdqffdq:DataQualityDimension` used in BDQ Tests. Each `Data Quality Dimension` describes a specific aspect of quality that a Test is intended to assess, such as completeness, conformance, or reliability.

These `Dimensions` serve as a semantic anchor for describing the intent of Tests and enable structured classification and interpretation of Test results across diverse `Use Cases`.

### 1.2 Audience (non-normative)

This document is intended for users who need a technical understanding of how BDQ Tests relate to conceptual `Dimensions` of data quality. It will be especially useful for:

- Implementers who need to map Tests to `Dimensions` in automated systems
- Standards developers and data quality modelers applying the Fitness for Use Framework Ontology
- Analysts and curators needing to understand the conceptual basis for different Tests’ evaluation

A working familiarity with the BDQ Test structure and the Fitness for Use Framework Ontology is helpful, though not required to benefit from this document.

### 1.3 Data Quality Dimensions (non-normative)

The concept of `bdqffdq:DataQualityDimension`, originally introduced by Veiga (2016) and Veiga et al. (2017), represents the aspect or attribute of data quality being evaluated. Common `Dimensions` include `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, and `Resolution`. These serve as high-level categories that group Tests according to the type of quality issue they address.

`Dimensions` are measurable characteristics of an `bdqffdq:InformationElement` and provide insight into how quality is defined and assessed for a given `Use Case`.

Each BDQ Test typically evaluates one or more data values (`Information Elements`) with respect to a single `Data Quality Dimension`. For example, the Test VALIDATION_COUNTRY_FOUND assesses the value of `dwc:country` for conformance to a `sourceAuthority`. In this case, the relevant dimension is `bdqdim:Conformance`.

Unlike `Criteria`, which apply only to `Validation` and `Issue` Tests, `Data Quality Dimensions` apply to all BDQ Test types: `bdqffdq:Validation`, `bdqffdq:Issue``bdqffdq:Measure`, and `bdqffdq:Amendment`.

### 1.4 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.5 Term List Distributions (non-normative)

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqdim/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdqdim/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/bdqdim.xml | Example for submission, to be generated | 

### 1.6 Status of the content of this document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Section [1.9 Key to Vocabulary Terms (normative)](#19-key-to-vocabulary-terms-normative) identifies which values in Section 4 are normative and which are non-normative.

### 1.7 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.8 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.9 Key to Vocabulary Terms (normative)

The terminology used to describe the terms in this vocabulary follows the TDWG [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | Completeness |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqdim/terms/ Completeness](https://rs.tdwg.org/bdqdim/terms/Completeness) |
| Modified (dcterms:issued) | normative | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2024-09-30 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqdim/terms/version/ Completeness-2024-09-30](https://rs.tdwg.org/bdqdim/terms/version/Completeness-2024-09-30) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Completeness |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | The extent to which data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use. |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Definition from the Fitness for Use Framework: Data Quality Dimensions Document https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension. |
| Status (tdwgutility:status) |  | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |
| Controlled Value String () | normative |  | Completeness |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:DataQualityDimension |


## 2 Use of Terms (normative)

A value for `bdqffdq:hasdataQualityDimension` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqdim/terms/Completeness`) or Term Qualified name (e.g., `bdqdim:Completeness`) from the `bdqdim:` namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `Completeness`) MAY be used. In a purely human context a abel (e.g., `Completeness`) MAY be used.

Each instance of a Test, regardless of Test type, SHOULD have exactly one `bdqffdq:hasdataQualityDimension` property relating it to a term in this `bdqdim:` vocabulary.

## 3 Term index (non-normative)
### 3.1 Index By Term Name (non-normative)

(See also [3.2 Index By Label (non-normative)](#32-index-by-label-non-normative))

**Classes**

**Vocabulary**

[bdqdim:Completeness](#bdqdim_Completeness) |
[bdqdim:Conformance](#bdqdim_Conformance) |
[bdqdim:Consistency](#bdqdim_Consistency) |
[bdqdim:Likeliness](#bdqdim_Likeliness) |
[bdqdim:Reliability](#bdqdim_Reliability) |
[bdqdim:Resolution](#bdqdim_Resolution) 

### 3.2 Index By Label (non-normative)

(See also [3.1 Index By Term Name (non-normative)](#31-index-by-term-name-non-normative))

**Classes**

[Completeness](#bdqdim_Completeness) |
[Conformance](#bdqdim_Conformance) |
[Consistency](#bdqdim_Consistency) |
[Likeliness](#bdqdim_Likeliness) |
[Reliability](#bdqdim_Reliability) |
[Resolution](#bdqdim_Resolution) 

## 4 Vocabulary (normative)
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqdim_Completeness"></a>Term Name  bdqdim:Completeness</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/Completeness">https://rs.tdwg.org/bdqdim/terms/Completeness</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/version/Completeness-2024-09-30">https://rs.tdwg.org/bdqdim/terms/version/Completeness-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The extent to which data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Completeness</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:DataQualityDimension</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqdim_Conformance"></a>Term Name  bdqdim:Conformance</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/Conformance">https://rs.tdwg.org/bdqdim/terms/Conformance</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/version/Conformance-2024-09-30">https://rs.tdwg.org/bdqdim/terms/version/Conformance-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Where data in a bdqffdq:InformationElement conform to a format, syntax, data type, range, or standard.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Conformance</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:DataQualityDimension</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqdim_Consistency"></a>Term Name  bdqdim:Consistency</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/Consistency">https://rs.tdwg.org/bdqdim/terms/Consistency</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/version/Consistency-2024-09-30">https://rs.tdwg.org/bdqdim/terms/version/Consistency-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Agreement among related bdqffdq:InformationElements that are present in the data. Note that missing bdqffdq:InformationElements do not make a test bdq:Inconsistent.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Consistency</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:DataQualityDimension</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqdim_Likeliness"></a>Term Name  bdqdim:Likeliness</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/Likeliness">https://rs.tdwg.org/bdqdim/terms/Likeliness</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/version/Likeliness-2024-09-30">https://rs.tdwg.org/bdqdim/terms/version/Likeliness-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The likelihood of one or more Darwin Core Terms having a true or expected values.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Likeliness</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:DataQualityDimension</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqdim_Reliability"></a>Term Name  bdqdim:Reliability</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/Reliability">https://rs.tdwg.org/bdqdim/terms/Reliability</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/version/Reliability-2024-09-30">https://rs.tdwg.org/bdqdim/terms/version/Reliability-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A measure of the degree to which data values agree with and describe an identified source of truth (object, event or any abstract or real 'thing').</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Reliability</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:DataQualityDimension</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqdim_Resolution"></a>Term Name  bdqdim:Resolution</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/Resolution">https://rs.tdwg.org/bdqdim/terms/Resolution</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqdim/terms/version/Resolution-2024-09-30">https://rs.tdwg.org/bdqdim/terms/version/Resolution-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Resolution</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The extent to which the data have sufficiently detailed information. A measure of the granularity of the data, or the smallest measurable increment.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Resolution</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:DataQualityDimension</td>
		</tr>
	</tbody>
</table>


## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../../index.md#5-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## References (non-normative)

The references for the BDQ standard can be found in the [References (non-normative)](../../../index.md#7-references-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Dimension Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqdim/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
