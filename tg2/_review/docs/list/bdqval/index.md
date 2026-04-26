<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Controlled Vocabulary List of Terms

**Title**<br>
BDQ Controlled Vocabulary List of Terms

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqval

**This version**<br>
<http://rs.tdwg.org/bdqval/terms/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdqval/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ standard. It covers some terms used in Test Specifications, and especially values used as bdqffdq:Parameters.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqval/terms/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Data Quality Vocabulary Terms (non-normative)](#13-data-quality-vocabulary-terms-non-normative)
  - [1.4 Associated Documents (non-normative)](#14-associated-documents-non-normative)
  - [1.5 Term List Distributions (non-normative)](#15-term-list-distributions-non-normative)
  - [1.6 Status of the Content of this Document (normative)](#16-status-of-the-content-of-this-document-normative)
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

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to provide the full term list for the `bdqval:` controlled vocabulary, which supports the specification and use of BDQ Tests. The `bdqval:` vocabulary includes concepts used throughout the BDQ standard to describe parameters, data structures, source authorities, and special value cases relevant to the execution and behavior of Tests.

This term list defines the formal structure and meanings of these concepts and provides reference material for implementation and documentation purposes.

### 1.2 Audience (non-normative)

This document is intended for technical users who need a precise understanding of the vocabulary elements used in BDQ Test `Specifications` and reports. It will be particularly useful for:

- Implementers interpreting or extending BDQ Test logic
- Standards developers and data quality modelers working with BDQ vocabularies
- Analysts and system designers configuring parameterized data quality assessments
- Curators needing to understand the conceptual basis for different Test evaluations

Familiarity with RDF vocabularies and the Fitness For Use Framework is recommended for full comprehension, but the document is organized to be accessible for any reader needing detailed term definitions.

### 1.3 Data Quality Vocabulary Terms (non-normative)

The `bdqval:` vocabulary includes four groups of concepts used across the BDQ standard:

- **Use Cases** (`bdqffdq:UseCase`) – formal representations of the purposes for which data might be evaluated using BDQ Tests.
- **Test Parameters** (`bdqffdq:Parameter`) – concepts used to configure the behavior of Tests, including named parameters like `bdqval:sourceAuthority`.
- **Information Elements** – used by `MultiRecord` `Measure` Tests to refer to aggregated or referenced values.
- **Empty/NotEmpty Concepts** – `bdqval:Empty` and `bdqval:NotEmpty`, which provide shared semantics for Tests dealing with missing or present values.

These terms ensure consistent representation and enable structured interpretation of Test configurations and outcomes.

### 1.4 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.5 Term List Distributions (non-normative)

| Description | IRI | Download URL |
| ----------- | --- | -----------  |
| HTML file   | http://rs.tdwg.org/bdqval/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdqval/index.md |
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/bdqval.xml |

### 1.6 Status of the Content of this Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

Section [1.9 Key to Vocabulary Terms (normative)](#19-key-to-vocabulary-terms-normative) identifies which values in Section 4 are normative and which are non-normative.

### 1.7 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.8 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdqval:         | https://rs.tdwg.org/bdqval/terms/           |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| dwciri:      | http://rs.tdwg.org/dwc/iri/                 |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.9 Key to Vocabulary Terms (normative)

The terminology used to describe the terms in this vocabulary follows the TDWG [TDWG Standards Documentation Standard (SDS)](https://www.tdwg.org/standards/sds/) (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | AggregatedTestResponseOutcomes |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqval/terms/version/ AggregatedTestResponseOutcomes](https://rs.tdwg.org/bdqval/terms/version/AggregatedTestResponseOutcomes) |
| Modified (dcterms:issued) | normative | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2026-04-23 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqval/terms/version/ AggregatedTestResponseOutcomes-2026-04-23](https://rs.tdwg.org/bdqval/terms/version/AggregatedTestResponseOutcomes-2026-04-23) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | AggregatedTestResponseOutcomes |
| Definition (rdfs:comment) | normative | A description of the subject resource. TDWG SDS: The normative definition of the term, written in English. | An abstract InformationElement representing the set of outcomes (Response instances with their Response.status and Response.result values) produced by running a particular SingleRecord Test across the members of a MultiRecord in a single DataQualityReport. This Information Element is intended for use as a component of a bdqffdq:ActedUpon node for MultiRecord Measures that aggregate Response outcomes from other Tests. |
| Comments (skos:note) | non-normative | A general note, for any purpose. | Used to indicate that a MultiRecord Measure is concerned with Response outcomes (report data) rather than raw source-data terms. Pair with bdqffdq:aggregatesResponsesFrom to identify which Test produced the aggregated Responses. |
| Status (tdwgutility:status) |  | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |
| Controlled Value String () | normative |  | AggregatedTestResponseOutcomes |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:AbstractInformationElement |
| Fitness Requirements (bdqffdq:hasFitnessRequirements) | non-normative | The property of a bdqffdq:UseCase that provides text listing the qualities that data must have to be fit for a given use. | Data are fit for the Use Case bdqval:Alien-Species when occurrence records can be reliably interpreted for alien-species management: the organism identity is usable, occurrence semantics are usable and standardizable, and establishment context (e.g., establishment means, degree of establishment, pathway) is present and standardizable so that interpretation of alien-status is comparable across records and datasets.  <ul><li>Organism identity is usable: Taxon/scientific name terms (e.g., dwc:scientificName, related dwc:Taxon terms, and identifiers where provided) are present, sufficiently resolvable and consistent.  </li><li>Occurrence semantics are usable: dwc:occurrenceStatus is present, valid and  standardizable so records can be interpreted consistently for alien-species analyses and workflows.  </li><li>Alien-species context is usable: Alien-species related terms (e.g., dwc:establishmentMeans, dwc:degreeOfEstablishment, dwc:pathway) are present where expected, valid and standardizable against an appropriate authority so records are comparable.  </li><li>Core record typing supports interpretation: Values such as dwc:basisOfRecord and dc:type are present, valid and standardizable so record meaning is consistent in downstream use.  </li></ul>  |


## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqval:` namespace MUST use the Term IRI (e.g., `https://rs.tdwg.org/bdqval/terms/NotEmpty`) or Term Qualified name (e.g., `bdqval:NotEmpty`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (local name, e.g., `NotEmpty`) SHOULD be used. In a purely human context a label (e.g., `Not Empty`) MAY be used.

## 3 Term index (non-normative)
### 3.1 Index By Term Name (non-normative)

(See also [3.2 Index By Label (non-normative)](#32-index-by-label-non-normative))

**Classes**

**Data**

[bdqval:Empty](#bdqval_Empty) |
[bdqval:NotEmpty](#bdqval_NotEmpty) 

**bdqval:Parameter**

**bdqffdq:UseCase**

[bdqval:Alien-Species](#bdqval_Alien-Species) |
[bdqval:Biotic-Relationships](#bdqval_Biotic-Relationships) |
[bdqval:Record-Management](#bdqval_Record-Management) |
[bdqval:Spatial-Temporal_Patterns](#bdqval_Spatial-Temporal_Patterns) |
[bdqval:Taxon-Management](#bdqval_Taxon-Management) 

**bdqffdq:AbstractInformationElement**

[bdqval:AggregatedTestResponseOutcomes](#bdqval_AggregatedTestResponseOutcomes) |
[bdqval:AllAmendmentTestsRunOnSingleRecord](#bdqval_AllAmendmentTestsRunOnSingleRecord) |
[bdqval:AllValidationTestsRunOnSingleRecord](#bdqval_AllValidationTestsRunOnSingleRecord) 

### 3.2 Index By Label (non-normative)

(See also [3.1 Index By Term Name (non-normative)](#31-index-by-term-name-non-normative))

**Classes**

**Data**

[Empty](#bdqval_Empty) |
[NotEmpty](#bdqval_NotEmpty) 

**bdqval:Parameter**

**bdqffdq:UseCase**

[Alien-Species](#bdqval_Alien-Species) |
[Biotic-Relationships](#bdqval_Biotic-Relationships) |
[Record-Management](#bdqval_Record-Management) |
[Spatial-Temporal Patterns](#bdqval_Spatial-Temporal_Patterns) |
[Taxon-Management](#bdqval_Taxon-Management) 

**bdqffdq:AbstractInformationElement**

[AggregatedTestResponseOutcomes](#bdqval_AggregatedTestResponseOutcomes) |
[AllAmendmentTestsRunOnSingleRecord](#bdqval_AllAmendmentTestsRunOnSingleRecord) |
[AllValidationTestsRunOnSingleRecord](#bdqval_AllValidationTestsRunOnSingleRecord) 

## 4 Vocabulary (normative)
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_AggregatedTestResponseOutcomes"></a>Term Name  bdqval:AggregatedTestResponseOutcomes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/AggregatedTestResponseOutcomes">https://rs.tdwg.org/bdqval/terms/version/AggregatedTestResponseOutcomes</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-23</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/AggregatedTestResponseOutcomes-2026-04-23">https://rs.tdwg.org/bdqval/terms/version/AggregatedTestResponseOutcomes-2026-04-23</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>AggregatedTestResponseOutcomes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An abstract InformationElement representing the set of outcomes (Response instances with their Response.status and Response.result values) produced by running a particular SingleRecord Test across the members of a MultiRecord in a single DataQualityReport. This Information Element is intended for use as a component of a bdqffdq:ActedUpon node for MultiRecord Measures that aggregate Response outcomes from other Tests.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used to indicate that a MultiRecord Measure is concerned with Response outcomes (report data) rather than raw source-data terms. Pair with bdqffdq:aggregatesResponsesFrom to identify which Test produced the aggregated Responses.</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>AggregatedTestResponseOutcomes</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:AbstractInformationElement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_Alien-Species"></a>Term Name  bdqval:Alien-Species</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/Alien-Species">https://rs.tdwg.org/bdqval/terms/Alien-Species</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/Alien-Species-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/Alien-Species-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Alien-Species</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Research uses forming a bdqffdq:UseCase for dwc:Occurrence data of alien species that 1) allows the understanding of the spatial and temporal distribution of an alien species or 2) identifies records that contain valid terms (i.e. name, space, time, other) associated with alien species; i.e.1) where the Information Elements concern what dwc:Organism occurred where and when and the means, degree, and pathways of establishment, and that may used for analysis of spatial and/or temporal patterns of biodiversity (see examples in Groom et al. (2019). Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards, 3: e38084.  https://doi.org/10.3897/biss.3.38084).</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for the Use Case bdqval:Alien-Species when occurrence records can be reliably interpreted for alien-species management: the organism identity is usable, occurrence semantics are usable and standardizable, and establishment context (e.g., establishment means, degree of establishment, pathway) is present and standardizable so that interpretation of alien-status is comparable across records and datasets.  <ul><li>Organism identity is usable: Taxon/scientific name terms (e.g., dwc:scientificName, related dwc:Taxon terms, and identifiers where provided) are present, sufficiently resolvable and consistent.  </li><li>Occurrence semantics are usable: dwc:occurrenceStatus is present, valid and  standardizable so records can be interpreted consistently for alien-species analyses and workflows.  </li><li>Alien-species context is usable: Alien-species related terms (e.g., dwc:establishmentMeans, dwc:degreeOfEstablishment, dwc:pathway) are present where expected, valid and standardizable against an appropriate authority so records are comparable.  </li><li>Core record typing supports interpretation: Values such as dwc:basisOfRecord and dc:type are present, valid and standardizable so record meaning is consistent in downstream use.  </li></ul> </td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Alien-Species</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
		<tr>
			<td>Included SingleRecord Tests</td>
			<td><a href="../../terms/bdqtest/index.md#AMENDMENT_BASISOFRECORD_STANDARDIZED">AMENDMENT_BASISOFRECORD_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DCTYPE_STANDARDIZED">AMENDMENT_DCTYPE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED">AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED">AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT">AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_STANDARDIZED">AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_PATHWAY_STANDARDIZED">AMENDMENT_PATHWAY_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID">AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SEX_STANDARDIZED">AMENDMENT_SEX_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_TYPESTATUS_STANDARDIZED">AMENDMENT_TYPESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#ISSUE_ESTABLISHMENTMEANS_NOTEMPTY">ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_NOTEMPTY">VALIDATION_BASISOFRECORD_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_STANDARD">VALIDATION_BASISOFRECORD_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASSIFICATION_CONSISTENT">VALIDATION_CLASSIFICATION_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASS_FOUND">VALIDATION_CLASS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_NOTEMPTY">VALIDATION_DCTYPE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_STANDARD">VALIDATION_DCTYPE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_INRANGE">VALIDATION_DECIMALLATITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_NOTEMPTY">VALIDATION_DECIMALLATITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_INRANGE">VALIDATION_DECIMALLONGITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_NOTEMPTY">VALIDATION_DECIMALLONGITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DEGREEOFESTABLISHMENT_STANDARD">VALIDATION_DEGREEOFESTABLISHMENT_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ESTABLISHMENTMEANS_STANDARD">VALIDATION_ESTABLISHMENTMEANS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_NOTEMPTY">VALIDATION_EVENTDATE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_STANDARD">VALIDATION_EVENTDATE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENT_CONSISTENT">VALIDATION_EVENT_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GENUS_FOUND">VALIDATION_GENUS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_NOTEMPTY">VALIDATION_OCCURRENCESTATUS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_STANDARD">VALIDATION_OCCURRENCESTATUS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_PATHWAY_STANDARD">VALIDATION_PATHWAY_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY">VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_COMPLETE">VALIDATION_SCIENTIFICNAMEID_COMPLETE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_NOTEMPTY">VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_FOUND">VALIDATION_SCIENTIFICNAME_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY">VALIDATION_SCIENTIFICNAME_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SEX_STANDARD">VALIDATION_SEX_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_STARTDAYOFYEAR_INRANGE">VALIDATION_STARTDAYOFYEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_STATEPROVINCE_FOUND">VALIDATION_STATEPROVINCE_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_NOTEMPTY">VALIDATION_TAXON_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_UNAMBIGUOUS">VALIDATION_TAXON_UNAMBIGUOUS</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TYPESTATUS_STANDARD">VALIDATION_TYPESTATUS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_YEAR_INRANGE">VALIDATION_YEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_YEAR_NOTEMPTY">VALIDATION_YEAR_NOTEMPTY</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_AllAmendmentTestsRunOnSingleRecord"></a>Term Name  bdqval:AllAmendmentTestsRunOnSingleRecord</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/AllAmendmentTestsRunOnSingleRecord">https://rs.tdwg.org/bdqval/terms/AllAmendmentTestsRunOnSingleRecord</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/AllAmendmentTestsRunOnSingleRecord-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/AllAmendmentTestsRunOnSingleRecord-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>AllAmendmentTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An Abstract Information Element composed of the outcomes of a list of bdqffdq:Amendment Tests from a single run on a bdqffdq:SingleRecord in a bdqffdq:DataQualityReport forming the input to another Test.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Measure of Single Record Tests</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>AllAmendmentTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:AbstractInformationElement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_AllValidationTestsRunOnSingleRecord"></a>Term Name  bdqval:AllValidationTestsRunOnSingleRecord</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/AllValidationTestsRunOnSingleRecord">https://rs.tdwg.org/bdqval/terms/AllValidationTestsRunOnSingleRecord</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/AllValidationTestsRunOnSingleRecord-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/AllValidationTestsRunOnSingleRecord-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An Abstract Information Element composed of the outcomes of a list of bdqffdq:Validation Tests from a single run on a bdqffdq:SingleRecord in a bdwffdq:DataQualityReport.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Measure of Single Record Tests</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:AbstractInformationElement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_annotationAlertIf"></a>Term Name  bdqval:annotationAlertIf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/annotationAlertIf">https://rs.tdwg.org/bdqval/terms/annotationAlertIf</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/annotationAlertIf-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/annotationAlertIf-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>annotationAlertIf</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes if an annotation exists in a bdqval:ParameterizedTest within a bdqval:annotationSystem by describing the criteria for relating annotations in the system to records within the bdqval:ParameterizedTest.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Test "ANNOTATION_ISSUE_NOTEMPTY" (bdqtest:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>annotationAlertIf</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_annotationSystem"></a>Term Name  bdqval:annotationSystem</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/annotationSystem">https://rs.tdwg.org/bdqval/terms/annotationSystem</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/annotationSystem-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/annotationSystem-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>annotationSystem</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes a system for annotations in a bdqval:ParameterizedTest, with the default being the W3C Annotations Data Model's "oa:Annotation"</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Test "ANNOTATION_ISSUE_NOTEMPTY" (bdqtest:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>annotationSystem</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_assumptionOnUnknownBiome"></a>Term Name  bdqval:assumptionOnUnknownBiome</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/assumptionOnUnknownBiome">https://rs.tdwg.org/bdqval/terms/assumptionOnUnknownBiome</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/assumptionOnUnknownBiome-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/assumptionOnUnknownBiome-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>assumptionOnUnknownBiome</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Used when a bdqval:taxonomyIsMarine sourceAuthority is unable to assert the marine or non-marine status of a taxon, the biome (either "marine" or "nonmarine") to assume, with the default being "noassumption".</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT (bdqtest:b9c184ce-a859-410c-9d12-71a338200380).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>assumptionOnUnknownBiome</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_Biotic-Relationships"></a>Term Name  bdqval:Biotic-Relationships</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/Biotic-Relationships">https://rs.tdwg.org/bdqval/terms/Biotic-Relationships</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/Biotic-Relationships-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/Biotic-Relationships-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Biotic-Relationships</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Research uses forming a bdqffdq:UseCase for relationships between dwc:Organisms 1) where the bdqffdq:InformationElements concern what dwc:Organisms have a relationship and 2) that are used for analysis of the relationship of one dwc:Organism to another (see examples in: Poelen JH, Simons JD, Mungall CJ. (2014). Global Biotic Interactions: An open infrastructure to share and analyze species-interaction datasets. Ecological Informatics, 24, 148–159. https://doi.org/10.1016/j.ecoinf.2014.08.005). </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for the Use Case bdqval:Biotic-Relationships when occurrence records support consistent interpretation of biotic relationship evidenced by providing a resolvable taxonomic identification, minimally usable spatial and temporal context, and key controlled descriptors that are present and standardizable (e.g., record type, occurrence status, establishment context, pathway, type status).  <ul><li>Organism identity is usable: Taxon and scientific name terms are present and sufficiently resolvable, are internally consistent, and where possible are consistent with an appropriate source authority to support relationship interpretation and grouping.  </li><li>Occurrence semantics are usable: Key status/occurrence terms (e.g., dwc:occurrenceStatus) are present, and valid and standardizable so records are comparable.  </li><li>Location and time are usable: Spatial terms (coordinates and supporting metadata) and temporal terms (e.g., dwc:eventDate and related date terms) are present, valid, and internally consistent so records are comparable, and support consistent interpretation, and downstream use.  </li><li> </li><li>Supporting descriptors are usable: Core typing/descriptor terms (e.g., dwc:basisOfRecord, dc:type) are present, valid/ and standardizable so as to support consistent interpretation across sources.  </li></ul> </td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Biotic-Relationships</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
		<tr>
			<td>Included SingleRecord Tests</td>
			<td><a href="../../terms/bdqtest/index.md#AMENDMENT_DCTYPE_STANDARDIZED">AMENDMENT_DCTYPE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED">AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT">AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_STANDARDIZED">AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_PATHWAY_STANDARDIZED">AMENDMENT_PATHWAY_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID">AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_TYPESTATUS_STANDARDIZED">AMENDMENT_TYPESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#ISSUE_ESTABLISHMENTMEANS_NOTEMPTY">ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_NOTEMPTY">VALIDATION_BASISOFRECORD_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_STANDARD">VALIDATION_BASISOFRECORD_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASSIFICATION_CONSISTENT">VALIDATION_CLASSIFICATION_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASS_FOUND">VALIDATION_CLASS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_NOTEMPTY">VALIDATION_DCTYPE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_STANDARD">VALIDATION_DCTYPE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_INRANGE">VALIDATION_DECIMALLATITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_NOTEMPTY">VALIDATION_DECIMALLATITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_INRANGE">VALIDATION_DECIMALLONGITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_NOTEMPTY">VALIDATION_DECIMALLONGITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ESTABLISHMENTMEANS_STANDARD">VALIDATION_ESTABLISHMENTMEANS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_NOTEMPTY">VALIDATION_EVENTDATE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_STANDARD">VALIDATION_EVENTDATE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENT_CONSISTENT">VALIDATION_EVENT_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GENUS_FOUND">VALIDATION_GENUS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_NOTEMPTY">VALIDATION_OCCURRENCESTATUS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_STANDARD">VALIDATION_OCCURRENCESTATUS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_PATHWAY_STANDARD">VALIDATION_PATHWAY_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_FOUND">VALIDATION_SCIENTIFICNAME_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY">VALIDATION_SCIENTIFICNAME_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_NOTEMPTY">VALIDATION_TAXON_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_UNAMBIGUOUS">VALIDATION_TAXON_UNAMBIGUOUS</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TYPESTATUS_STANDARD">VALIDATION_TYPESTATUS_STANDARD</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_defaultGeodeticDatum"></a>Term Name  bdqval:defaultGeodeticDatum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/defaultGeodeticDatum">https://rs.tdwg.org/bdqval/terms/defaultGeodeticDatum</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/defaultGeodeticDatum-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/defaultGeodeticDatum-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>defaultGeodeticDatum</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the default dwc:geodeticDatum in a bdqval:ParameterizedTest. A default dwc:geodeticDatum is supplied in cases where a bdqval:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See Test AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT (bdqtest:7498ca76-c4d4-42e2-8103-acacccbdffa7).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>defaultGeodeticDatum</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_DefaultSourceAuthority"></a>Term Name  bdqval:DefaultSourceAuthority</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/DefaultSourceAuthority">https://rs.tdwg.org/bdqval/terms/DefaultSourceAuthority</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/DefaultSourceAuthority-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/DefaultSourceAuthority-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>DefaultSourceAuthority</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A provided default bdqval:sourceAuthority that is used when a required bdqval:Parameter specifying a bdqval:sourceAuthority has not been provided at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>DefaultSourceAuthority</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_defaultValue"></a>Term Name  bdqval:defaultValue</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/defaultValue">https://rs.tdwg.org/bdqval/terms/defaultValue</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/defaultValue-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/defaultValue-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>defaultValue</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A preselected value (e.g., year, elevation) to be used where a required bdqval:Parameter value has not been provided at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>defaultValue</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_earliestValidDate"></a>Term Name  bdqval:earliestValidDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/earliestValidDate">https://rs.tdwg.org/bdqval/terms/earliestValidDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/earliestValidDate-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/earliestValidDate-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>earliestValidDate</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the earliest date in a bdqval:ParameterizedTest. A default date is supplied in cases where a bdqval:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>earliestValidDate</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_Empty"></a>Term Name  bdqval:Empty</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/Empty">https://rs.tdwg.org/bdqval/terms/Empty</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/Empty-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/Empty-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Empty</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An evaluation of a value, which in the context of the evaluation, returns false if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns true. </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See also: bdqval:NotEmpty. In the BDQ standard, bdqval:Empty is used to evaluate bdqffdq:InformationElements within a Test specification, it therefore means empty if the dataset being evaluated does not contain the term matching the Information Element, or if the dataset contains that term but the value for that term is empty. The phrasing 'in the context of the evauation' is to allow the Test implementations to be independent of, and agnostic about the data structures presented to a framework for executing the Tests and the framework within which the Tests are run. The term bdqval:Empty is defined to be more broadly usable than just with bdqtest:. Note: A bdqffdq:InformationElement containing invalid characters (e.g., letters in an Information Element that would be expected to contain integers) or values (including string serializations of the NULL value) are bdqval:NotEmpty and their invalidity must be separately detected. The definition of bdqval:Empty is not applicable to a discussion of what value to include in a controlled vocabulary to indicate that no meaningful value is present, so no suggestion is made that bdqval:Empty should be used as a data value to represent some form of 'Null', 'unknown', 'not recorded', etc. Choices there would fall into the semantics for some set of controlled vocabularies. The relevance to such a discussion is that the definition of bdqval:Empty would treat an empty string as an empty value, with no semantics attached as to why the value is empty</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Empty</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>skos:Concept</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_geospatialLand"></a>Term Name  bdqval:geospatialLand</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/geospatialLand">https://rs.tdwg.org/bdqval/terms/geospatialLand</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/geospatialLand-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/geospatialLand-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>geospatialLand</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqval:sourceAuthority consisting of polygons that have been derived from a union of Natural Earth vectors for Land and for Minor Islands at 1:10,000,000 resolution.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT (bdqtest:b9c184ce-a859-410c-9d12-71a338200380)</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>geospatialLand</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_includeEventDate"></a>Term Name  bdqval:includeEventDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/includeEventDate">https://rs.tdwg.org/bdqval/terms/includeEventDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/includeEventDate-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/includeEventDate-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>includeEventDate</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Allows dwc:eventDate to be excluded in a bdqval:ParameterizedTest. The default is to include the dwc:eventDate in the Test, but it may be excluded to allow a dwc:dateIdentified to be prior to the dwc:eventDate.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Test "VALIDATION_DATEIDENTIFIED_INRANGE" (bdqtest:dc8aae4b-134f-4d75-8a71-c4186239178e).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>includeEventDate</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_latestValidDate"></a>Term Name  bdqval:latestValidDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/latestValidDate">https://rs.tdwg.org/bdqval/terms/latestValidDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/latestValidDate-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/latestValidDate-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>latestValidDate</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the latest date in a bdqval:ParameterizedTest. A default date is supplied in cases where a bdqval:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>latestValidDate</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_maximumValidDepthInMeters"></a>Term Name  bdqval:maximumValidDepthInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/maximumValidDepthInMeters">https://rs.tdwg.org/bdqval/terms/maximumValidDepthInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/maximumValidDepthInMeters-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/maximumValidDepthInMeters-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>maximumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the maximum depth in a bdqval:ParameterizedTest. A default depth is supplied in cases where a bdqval:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>maximumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_maximumValidElevationInMeters"></a>Term Name  bdqval:maximumValidElevationInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/maximumValidElevationInMeters">https://rs.tdwg.org/bdqval/terms/maximumValidElevationInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/maximumValidElevationInMeters-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/maximumValidElevationInMeters-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>maximumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the highest elevation in a bdqval:ParameterizedTest. A default elevation is supplied in cases where a bdqval:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>maximumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_minimumValidDepthInMeters"></a>Term Name  bdqval:minimumValidDepthInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/minimumValidDepthInMeters">https://rs.tdwg.org/bdqval/terms/minimumValidDepthInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/minimumValidDepthInMeters-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/minimumValidDepthInMeters-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>minimumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the minimum depth in a bdqval:ParameterizedTest. A default depth is supplied in cases where a bdqval:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>minimumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_minimumValidElevationInMeters"></a>Term Name  bdqval:minimumValidElevationInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/minimumValidElevationInMeters">https://rs.tdwg.org/bdqval/terms/minimumValidElevationInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/minimumValidElevationInMeters-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/minimumValidElevationInMeters-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>minimumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the lowest elevation in a bdqval:ParameterizedTest. A default elevation is supplied in cases where a bdqval:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>minimumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_NotEmpty"></a>Term Name  bdqval:NotEmpty</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/NotEmpty">https://rs.tdwg.org/bdqval/terms/NotEmpty</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/NotEmpty-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/NotEmpty-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An evaluation of a value, which in the context of the evaluation, returns true if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns false. </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See also: bdqval:Empty. In the BDQ standard, bdqval:NotEmpty is used to evaluate bdqffdq:InformationElements within a Test specification. Common string serializations of null such as '\N', 'NA', 'NaN', and NULL are treated as bdqval:NotEmpty. If '\N' is present in a dataset, Tests are expected to explicitly treat that value as bdqval:NotEmpty, and then try to evaluate it against whatever other criteria may apply. The term bdqval:NotEmpty is defined to be more broadly usable than the scope of BDQ Tests. </td>
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
			<td>skos:Concept</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_Record-Management"></a>Term Name  bdqval:Record-Management</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/Record-Management">https://rs.tdwg.org/bdqval/terms/Record-Management</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/Record-Management-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/Record-Management-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Record-Management</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase that documents the management of the quality of biodiversity data records, for example, where an agency wishes to do broad data quality checks across the whole of their database for checking for data errors, and for data cleaning (see examples in Rees ER and Nicholls M (2020) Data Quality Use Case Study Results. Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2). </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for the Use Case bdqval:Record-Management when occurrence records can be reliably managed and curated: Core taxon identifiers and descriptors are present, values are valid and standardizable, spatial and temporal fields are usable and internally consistent, and potential data transformations or special conditions are detectable so records can be prioritized for remediation and maintained with clear semantics.  <ul><li>Core record content is usable: Key fields (e.g., identifiers, dwc:basisOfRecord, dc:type, and other essential descriptors) are present, valid and standardizable for consistent management workflows.  </li><li>Location and time are usable: Spatial terms (coordinates and supporting metadata) and temporal terms (e.g., dwc:eventDate and related date parts) are present, valid, and internally consistent enough to support curation, reporting, and downstream use.  </li><li>Taxon content is manageable: Taxon terms are sufficiently resolvable and consistent to support curation and management tasks (including standardization where applicable).  </li><li>Review triggers are detectable: Reports of generalization and transformations or other potential issues (e.g., generalizations and other warning-type fields) are available so curators can decide how to handle records for management purposes.  </li></ul> </td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Record-Management</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
		<tr>
			<td>Included SingleRecord Tests</td>
			<td><a href="../../terms/bdqtest/index.md#AMENDMENT_BASISOFRECORD_STANDARDIZED">AMENDMENT_BASISOFRECORD_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COORDINATES_FROM_VERBATIM">AMENDMENT_COORDINATES_FROM_VERBATIM</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COORDINATES_TRANSPOSED">AMENDMENT_COORDINATES_TRANSPOSED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_FROM_COORDINATES">AMENDMENT_COUNTRYCODE_FROM_COORDINATES</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_STANDARDIZED">AMENDMENT_COUNTRYCODE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DATEIDENTIFIED_STANDARDIZED">AMENDMENT_DATEIDENTIFIED_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DAY_STANDARDIZED">AMENDMENT_DAY_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DCTYPE_STANDARDIZED">AMENDMENT_DCTYPE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED">AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_VERBATIM">AMENDMENT_EVENTDATE_FROM_VERBATIM</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY">AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR">AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_STANDARDIZED">AMENDMENT_EVENTDATE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_EVENT_FROM_EVENTDATE">AMENDMENT_EVENT_FROM_EVENTDATE</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT">AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_GEODETICDATUM_STANDARDIZED">AMENDMENT_GEODETICDATUM_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_LICENSE_STANDARDIZED">AMENDMENT_LICENSE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM">AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM">AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_MONTH_STANDARDIZED">AMENDMENT_MONTH_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT">AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_STANDARDIZED">AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_PATHWAY_STANDARDIZED">AMENDMENT_PATHWAY_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON">AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID">AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SEX_STANDARDIZED">AMENDMENT_SEX_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_TAXONRANK_STANDARDIZED">AMENDMENT_TAXONRANK_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_TYPESTATUS_STANDARDIZED">AMENDMENT_TYPESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY">ISSUE_DATAGENERALIZATIONS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS">MEASURE_EVENTDATE_DURATIONINSECONDS</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_COMPLIANT">MEASURE_VALIDATIONTESTS_COMPLIANT</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT">MEASURE_VALIDATIONTESTS_NOTCOMPLIANT</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET">MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_NOTEMPTY">VALIDATION_BASISOFRECORD_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_STANDARD">VALIDATION_BASISOFRECORD_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASSIFICATION_CONSISTENT">VALIDATION_CLASSIFICATION_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASS_FOUND">VALIDATION_CLASS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT">VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT">VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATEUNCERTAINTY_INRANGE">VALIDATION_COORDINATEUNCERTAINTY_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_NOTEMPTY">VALIDATION_COUNTRYCODE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD">VALIDATION_COUNTRYCODE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT">VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS">VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRY_FOUND">VALIDATION_COUNTRY_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRY_NOTEMPTY">VALIDATION_COUNTRY_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DATEIDENTIFIED_INRANGE">VALIDATION_DATEIDENTIFIED_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DATEIDENTIFIED_STANDARD">VALIDATION_DATEIDENTIFIED_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DAY_INRANGE">VALIDATION_DAY_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DAY_STANDARD">VALIDATION_DAY_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_NOTEMPTY">VALIDATION_DCTYPE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_STANDARD">VALIDATION_DCTYPE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_INRANGE">VALIDATION_DECIMALLATITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_NOTEMPTY">VALIDATION_DECIMALLATITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_INRANGE">VALIDATION_DECIMALLONGITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_NOTEMPTY">VALIDATION_DECIMALLONGITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ENDDAYOFYEAR_INRANGE">VALIDATION_ENDDAYOFYEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ESTABLISHMENTMEANS_STANDARD">VALIDATION_ESTABLISHMENTMEANS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_INRANGE">VALIDATION_EVENTDATE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_NOTEMPTY">VALIDATION_EVENTDATE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_STANDARD">VALIDATION_EVENTDATE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTTEMPORAL_NOTEMPTY">VALIDATION_EVENTTEMPORAL_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENT_CONSISTENT">VALIDATION_EVENT_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_FAMILY_FOUND">VALIDATION_FAMILY_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GENUS_FOUND">VALIDATION_GENUS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GEODETICDATUM_NOTEMPTY">VALIDATION_GEODETICDATUM_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GEODETICDATUM_STANDARD">VALIDATION_GEODETICDATUM_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_KINGDOM_FOUND">VALIDATION_KINGDOM_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_KINGDOM_NOTEMPTY">VALIDATION_KINGDOM_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_LICENSE_NOTEMPTY">VALIDATION_LICENSE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_LICENSE_STANDARD">VALIDATION_LICENSE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_LOCATION_NOTEMPTY">VALIDATION_LOCATION_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MAXDEPTH_INRANGE">VALIDATION_MAXDEPTH_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MAXELEVATION_INRANGE">VALIDATION_MAXELEVATION_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINDEPTH_INRANGE">VALIDATION_MINDEPTH_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH">VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINELEVATION_INRANGE">VALIDATION_MINELEVATION_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION">VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MONTH_STANDARD">VALIDATION_MONTH_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY">VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCEID_NOTEMPTY">VALIDATION_OCCURRENCEID_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_NOTEMPTY">VALIDATION_OCCURRENCESTATUS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_STANDARD">VALIDATION_OCCURRENCESTATUS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ORDER_FOUND">VALIDATION_ORDER_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_PATHWAY_STANDARD">VALIDATION_PATHWAY_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_PHYLUM_FOUND">VALIDATION_PHYLUM_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_POLYNOMIAL_CONSISTENT">VALIDATION_POLYNOMIAL_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY">VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_COMPLETE">VALIDATION_SCIENTIFICNAMEID_COMPLETE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_NOTEMPTY">VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_FOUND">VALIDATION_SCIENTIFICNAME_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY">VALIDATION_SCIENTIFICNAME_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SEX_STANDARD">VALIDATION_SEX_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_STARTDAYOFYEAR_INRANGE">VALIDATION_STARTDAYOFYEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_STATEPROVINCE_FOUND">VALIDATION_STATEPROVINCE_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXONRANK_NOTEMPTY">VALIDATION_TAXONRANK_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXONRANK_STANDARD">VALIDATION_TAXONRANK_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_NOTEMPTY">VALIDATION_TAXON_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_UNAMBIGUOUS">VALIDATION_TAXON_UNAMBIGUOUS</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TYPESTATUS_STANDARD">VALIDATION_TYPESTATUS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_YEAR_INRANGE">VALIDATION_YEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_YEAR_NOTEMPTY">VALIDATION_YEAR_NOTEMPTY</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_sourceAuthority"></a>Term Name  bdqval:sourceAuthority</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/sourceAuthority">https://rs.tdwg.org/bdqval/terms/sourceAuthority</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/sourceAuthority-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/sourceAuthority-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>sourceAuthority</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An authority using the "bdq" namespace that provides a reference for values required for a Test evaluation. Where the Test is a bdqval:ParameterizedTest a bdqval:defaultSourceAuthority ("bdqval:sourceAuthority default = xxx") is specified.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>sourceAuthority</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_Spatial-Temporal_Patterns"></a>Term Name  bdqval:Spatial-Temporal_Patterns</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/Spatial-Temporal_Patterns">https://rs.tdwg.org/bdqval/terms/Spatial-Temporal_Patterns</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/Spatial-Temporal_Patterns-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/Spatial-Temporal_Patterns-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Spatial-Temporal Patterns</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Research uses forming a bdqffdq:UseCase for dwc:Occurrence data 1) where the Information Elements concern what dwc:Organism occurred where and when and 2) that are used for analysis of spatial and/or temporal patterns of biodiversity or for use in species distribution / niche modeling, etc. (see examples in Rees ER and Nicholls M (2020) Data Quality Use Case Study Results. Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2). </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for the Use Case bdqval:Spatial-Temporal_Patterns when occurrence records can be reliably interpreted as organism occurrences in space and time: the organism identity is usable, the location is usable (with adequate precision and metadata), textual geography data is consistent with the coordinates, the event date is usable and internally consistent, and any generalization (spatial or temporal) is detectable so users can decide whether the record is fit at the intended analysis scale. <ul><li>Organism identity is usable: Taxon and scientific name terms (e.g., dwc:scientificName and related taxon terms) are present and sufficiently resolvable and consistent to support analyses of spatio-temporal patterns of organisms.  </li><li>Location is usable and interpretable (including precision and metadata): Coordinates are present, are in-range, and are accompanied by adequate spatial metadata (e.g., uncertainty and spatial reference such as datum); obvious artifact coordinates (e.g., zeros) are detectable.  </li><li>Textual geography is coherent with coordinates: Textual geography fields (e.g., dwc:countryCode, dwc:country, dwc:stateProvince) are valid and standardizable and consistent with the coordinates.  </li><li>Date is usable and internally consistent: dwc:eventDate is present, valid, in standard form and consistent with other temporal terms (e.g. dwc:year) terms when those are provided. Generalization and low precision are detectable: Any indication that the record has been generalized (via dwc:dataGeneralizations) is available along with coordinate uncertainty, broad and interval event dates, and taxonomic rank so that users can judge whether records are fit for the intended spatial and temporal resolution.  </li></ul></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Spatial-Temporal Patterns</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
		<tr>
			<td>Included SingleRecord Tests</td>
			<td><a href="../../terms/bdqtest/index.md#AMENDMENT_BASISOFRECORD_STANDARDIZED">AMENDMENT_BASISOFRECORD_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COORDINATES_FROM_VERBATIM">AMENDMENT_COORDINATES_FROM_VERBATIM</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COORDINATES_TRANSPOSED">AMENDMENT_COORDINATES_TRANSPOSED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_FROM_COORDINATES">AMENDMENT_COUNTRYCODE_FROM_COORDINATES</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_COUNTRYCODE_STANDARDIZED">AMENDMENT_COUNTRYCODE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DATEIDENTIFIED_STANDARDIZED">AMENDMENT_DATEIDENTIFIED_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DAY_STANDARDIZED">AMENDMENT_DAY_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DCTYPE_STANDARDIZED">AMENDMENT_DCTYPE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED">AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_EVENTDATE_STANDARDIZED">AMENDMENT_EVENTDATE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_EVENT_FROM_EVENTDATE">AMENDMENT_EVENT_FROM_EVENTDATE</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT">AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_GEODETICDATUM_STANDARDIZED">AMENDMENT_GEODETICDATUM_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM">AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM">AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_MONTH_STANDARDIZED">AMENDMENT_MONTH_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT">AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_OCCURRENCESTATUS_STANDARDIZED">AMENDMENT_OCCURRENCESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID">AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</a>, <a href="../../terms/bdqtest/index.md#ISSUE_COORDINATES_CENTEROFCOUNTRY">ISSUE_COORDINATES_CENTEROFCOUNTRY</a>, <a href="../../terms/bdqtest/index.md#ISSUE_DATAGENERALIZATIONS_NOTEMPTY">ISSUE_DATAGENERALIZATIONS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#ISSUE_ESTABLISHMENTMEANS_NOTEMPTY">ISSUE_ESTABLISHMENTMEANS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS">MEASURE_EVENTDATE_DURATIONINSECONDS</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_COMPLIANT">MEASURE_VALIDATIONTESTS_COMPLIANT</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT">MEASURE_VALIDATIONTESTS_NOTCOMPLIANT</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET">MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_NOTEMPTY">VALIDATION_BASISOFRECORD_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_STANDARD">VALIDATION_BASISOFRECORD_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT">VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT">VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT">VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATES_NOTZERO">VALIDATION_COORDINATES_NOTZERO</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COORDINATEUNCERTAINTY_INRANGE">VALIDATION_COORDINATEUNCERTAINTY_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_NOTEMPTY">VALIDATION_COUNTRYCODE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD">VALIDATION_COUNTRYCODE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT">VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS">VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRY_FOUND">VALIDATION_COUNTRY_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_COUNTRY_NOTEMPTY">VALIDATION_COUNTRY_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DATEIDENTIFIED_INRANGE">VALIDATION_DATEIDENTIFIED_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DATEIDENTIFIED_STANDARD">VALIDATION_DATEIDENTIFIED_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DAY_INRANGE">VALIDATION_DAY_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DAY_STANDARD">VALIDATION_DAY_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_NOTEMPTY">VALIDATION_DCTYPE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_STANDARD">VALIDATION_DCTYPE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_INRANGE">VALIDATION_DECIMALLATITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_NOTEMPTY">VALIDATION_DECIMALLATITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_INRANGE">VALIDATION_DECIMALLONGITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_NOTEMPTY">VALIDATION_DECIMALLONGITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ENDDAYOFYEAR_INRANGE">VALIDATION_ENDDAYOFYEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ESTABLISHMENTMEANS_STANDARD">VALIDATION_ESTABLISHMENTMEANS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_INRANGE">VALIDATION_EVENTDATE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_NOTEMPTY">VALIDATION_EVENTDATE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTDATE_STANDARD">VALIDATION_EVENTDATE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_EVENTTEMPORAL_NOTEMPTY">VALIDATION_EVENTTEMPORAL_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GEODETICDATUM_NOTEMPTY">VALIDATION_GEODETICDATUM_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GEODETICDATUM_STANDARD">VALIDATION_GEODETICDATUM_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_LOCATION_NOTEMPTY">VALIDATION_LOCATION_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MAXDEPTH_INRANGE">VALIDATION_MAXDEPTH_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MAXELEVATION_INRANGE">VALIDATION_MAXELEVATION_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINDEPTH_INRANGE">VALIDATION_MINDEPTH_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH">VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINELEVATION_INRANGE">VALIDATION_MINELEVATION_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION">VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_MONTH_STANDARD">VALIDATION_MONTH_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_NOTEMPTY">VALIDATION_OCCURRENCESTATUS_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_OCCURRENCESTATUS_STANDARD">VALIDATION_OCCURRENCESTATUS_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_FOUND">VALIDATION_SCIENTIFICNAME_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY">VALIDATION_SCIENTIFICNAME_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_STARTDAYOFYEAR_INRANGE">VALIDATION_STARTDAYOFYEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_STATEPROVINCE_FOUND">VALIDATION_STATEPROVINCE_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_NOTEMPTY">VALIDATION_TAXON_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_UNAMBIGUOUS">VALIDATION_TAXON_UNAMBIGUOUS</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_YEAR_INRANGE">VALIDATION_YEAR_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_YEAR_NOTEMPTY">VALIDATION_YEAR_NOTEMPTY</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_spatialBufferInMeters"></a>Term Name  bdqval:spatialBufferInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/spatialBufferInMeters">https://rs.tdwg.org/bdqval/terms/spatialBufferInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/spatialBufferInMeters-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/spatialBufferInMeters-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>spatialBufferInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A buffer, in meters, from a polygon (geopolitical boundary, coastline, etc.).</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>spatialBufferInMeters</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_Taxon-Management"></a>Term Name  bdqval:Taxon-Management</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/Taxon-Management">https://rs.tdwg.org/bdqval/terms/Taxon-Management</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/Taxon-Management-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/Taxon-Management-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon-Management</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase that documents the management of the quality of taxonomic names and associated information such as rank, authority, Type status, etc. (see examples in Rees ER and Nicholls M (2020) Data Quality Use Case Study Results Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2).</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for the Use Case bdqval:Taxon-Management when occurrence records support taxon curation: Taxon terms are sufficient to resolve the organism (or flag ambiguity), core name and rank terms (e.g., dwc:scientificName, dwc:taxonRank) are present and align with an appropriate bdqval:sourceAuthority, name strings are consistent with atomized name fields and identifiers or authorship, identification dates are valid and plausible, and key contextual metadata (e.g., dwc:basisOfRecord, and controlled fields such as dwc:typeStatus and dwc:sex where relevant) are usable.  <ul><li>Taxon can be resolved: Taxon terms are present and sufficient to support unambiguous resolution when possible.  </li><li>Names and ranks are authoritative: dwc:scientificName and required rank and classification terms are present, standardizable, and consistent with the bdqval:sourceAuthority.  </li><li>Name fields are consistent: dwc:scientificName agrees with atomized name fields; authorship is provided where needed.  </li><li>Identifiers are usable: Identifiers (e.g., dwc:scientificNameID) are present when available and correctly formed; dwc:taxonRank is present and valid.  </li><li>Identification timing is usable: dwc:dateIdentified is present when needed, ISO-valid, and temporally plausible (and consistent with dwc:eventDate when provided).  </li><li>Supporting context is usable: dwc:basisOfRecord and other relevant controlled and context fields are present and valid; basic space/time fields are in standard form where used to support curation decisions. </li></ul></td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Taxon-Management</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
		<tr>
			<td>Included SingleRecord Tests</td>
			<td><a href="../../terms/bdqtest/index.md#AMENDMENT_BASISOFRECORD_STANDARDIZED">AMENDMENT_BASISOFRECORD_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DATEIDENTIFIED_STANDARDIZED">AMENDMENT_DATEIDENTIFIED_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_DCTYPE_STANDARDIZED">AMENDMENT_DCTYPE_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON">AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID">AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_SEX_STANDARDIZED">AMENDMENT_SEX_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_TAXONRANK_STANDARDIZED">AMENDMENT_TAXONRANK_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#AMENDMENT_TYPESTATUS_STANDARDIZED">AMENDMENT_TYPESTATUS_STANDARDIZED</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_COMPLIANT">MEASURE_VALIDATIONTESTS_COMPLIANT</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT">MEASURE_VALIDATIONTESTS_NOTCOMPLIANT</a>, <a href="../../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET">MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_NOTEMPTY">VALIDATION_BASISOFRECORD_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_BASISOFRECORD_STANDARD">VALIDATION_BASISOFRECORD_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASSIFICATION_CONSISTENT">VALIDATION_CLASSIFICATION_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_CLASS_FOUND">VALIDATION_CLASS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DATEIDENTIFIED_INRANGE">VALIDATION_DATEIDENTIFIED_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DATEIDENTIFIED_STANDARD">VALIDATION_DATEIDENTIFIED_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_NOTEMPTY">VALIDATION_DCTYPE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DCTYPE_STANDARD">VALIDATION_DCTYPE_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_INRANGE">VALIDATION_DECIMALLATITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLATITUDE_NOTEMPTY">VALIDATION_DECIMALLATITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_INRANGE">VALIDATION_DECIMALLONGITUDE_INRANGE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_DECIMALLONGITUDE_NOTEMPTY">VALIDATION_DECIMALLONGITUDE_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_FAMILY_FOUND">VALIDATION_FAMILY_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_GENUS_FOUND">VALIDATION_GENUS_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_KINGDOM_FOUND">VALIDATION_KINGDOM_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_KINGDOM_NOTEMPTY">VALIDATION_KINGDOM_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY">VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_ORDER_FOUND">VALIDATION_ORDER_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_PHYLUM_FOUND">VALIDATION_PHYLUM_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_POLYNOMIAL_CONSISTENT">VALIDATION_POLYNOMIAL_CONSISTENT</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY">VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_COMPLETE">VALIDATION_SCIENTIFICNAMEID_COMPLETE</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_NOTEMPTY">VALIDATION_SCIENTIFICNAMEID_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_FOUND">VALIDATION_SCIENTIFICNAME_FOUND</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY">VALIDATION_SCIENTIFICNAME_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_SEX_STANDARD">VALIDATION_SEX_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXONRANK_NOTEMPTY">VALIDATION_TAXONRANK_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXONRANK_STANDARD">VALIDATION_TAXONRANK_STANDARD</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_NOTEMPTY">VALIDATION_TAXON_NOTEMPTY</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TAXON_UNAMBIGUOUS">VALIDATION_TAXON_UNAMBIGUOUS</a>, <a href="../../terms/bdqtest/index.md#VALIDATION_TYPESTATUS_STANDARD">VALIDATION_TYPESTATUS_STANDARD</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqval_taxonIsMarine"></a>Term Name  bdqval:taxonIsMarine</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/taxonIsMarine">https://rs.tdwg.org/bdqval/terms/taxonIsMarine</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/taxonIsMarine-2026-04-22">https://rs.tdwg.org/bdqval/terms/version/taxonIsMarine-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>taxonIsMarine</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqval:sourceAuthority that uses dwc:scientificName to determine the "marine" or "non-marine" status of a dwc:Taxon using the "Environment" term obtained from the World Register of Marine Species (WORMS) database.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT (bdqtest:b9c184ce-a859-410c-9d12-71a338200380).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>taxonIsMarine</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Parameter, owl:NamedIndividual</td>
		</tr>
	</tbody>
</table>


## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../../index.md#71-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [General Glossary (non-normative)](../../../index.md#73-general-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## References (non-normative)

The references for the BDQ standard can be found in the [References (non-normative)](../../../index.md#8-references-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqval/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
