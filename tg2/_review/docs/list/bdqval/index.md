<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Controlled Vocabulary List of Terms

**Title**<br>
BDQ Controlled Vocabulary List of Terms

**Date version issued**<br>
2026-06-03

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqval

**This version**<br>
<http://rs.tdwg.org/bdqval/terms/2026-06-03>

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
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2026. BDQ Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqval/terms/2026-06-03>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
- [1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Data Quality Vocabulary Terms (non-normative)](#13-data-quality-vocabulary-terms-non-normative)
  - [1.4 Associated Documents (non-normative)](#14-associated-documents-non-normative)
  - [1.5 Term List Distributions (non-normative)](#15-term-list-distributions-non-normative)
  - [1.6 Status of the Content of this Document (normative)](#16-status-of-the-content-of-this-document-normative)
  - [1.7 RFC 2119 key words (normative)](#17-rfc-2119-key-words-normative)
  - [1.8 Namespace abbreviations (non-normative)](#18-namespace-abbreviations-non-normative)
  - [1.9 Key to Vocabulary Terms (normative)](#19-key-to-vocabulary-terms-normative)

- [2 Use of Terms (normative)](#2-use-of-terms-normative)

- [3 Term index (non-normative)](#3-term-index-non-normative)
  - [3.1 Index By Term Name (non-normative)](#31-index-by-term-name-non-normative)
  - [3.2 Index By Label (non-normative)](#32-index-by-label-non-normative)

- [4 Vocabulary (normative)](#4-vocabulary-normative)

- [Glossary (non-normative)](#glossary-non-normative)

- [References (non-normative)](#references-non-normative)

- [Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to provide the full term list for the `bdqval:` controlled vocabulary, which supports the specification and use of BDQ Tests. The `bdqval:` vocabulary includes concepts used throughout the BDQ standard to describe Test parameters, data structures, Information Elements, source authorities, and special value cases such as Empty and NotEmpty relevant to the execution and behavior of Tests.

This term list defines the formal structure and meanings of these concepts and provides reference material for implementation and documentation purposes.

### 1.2 Audience (non-normative)

This document is intended for technical users who need a precise understanding of the vocabulary elements used in BDQ Test `Specifications` and reports. It will be particularly useful for:

- Implementers interpreting or extending BDQ Test logic
- Standards developers and data quality modelers working with BDQ vocabularies
- Analysts and system designers configuring parameterized data quality assessments
- Curators needing to understand the conceptual basis for different Test evaluations

Familiarity with RDF vocabularies and the Fitness For Use Framework is recommended for full comprehension, but the document is organized to be accessible for any reader needing detailed term definitions.

### 1.3 Data Quality Vocabulary Terms (non-normative)

The `bdqval:` vocabulary includes three groups of concepts used across the BDQ standard:

- **Test Parameters** (`bdqffdq:Parameter`) – concepts used to configure the behavior of Tests, including named parameters like `bdqval:sourceAuthority`.
- **Information Elements** – used by `Multi Record` `Measure` Tests to refer to aggregated or referenced values.
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
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdquc:       | https://rs.tdwg.org/bdquc/terms/            |
| **bdqval:**  | https://rs.tdwg.org/bdqval/terms/           |
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
| Controlled Value () | normative | A string that is unique within a controlled vocabulary that identifies the concept in the context of a text-based metadata transfer system. The value MUST consist of Unicode characters. | AggregatedTestResponseOutcomes |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:AbstractInformationElement |


## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqval:` namespace MUST use the Term IRI (e.g., `https://rs.tdwg.org/bdqval/terms/NotEmpty`) or Term Qualified name (e.g., `bdqval:NotEmpty`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (local name, e.g., `NotEmpty`) SHOULD be used. In a purely human context a label (e.g., `Not Empty`) MAY be used.

## 3 Term index (non-normative)
### 3.1 Index By Term Name (non-normative)

(See also [3.2 Index By Label (non-normative)](#32-index-by-label-non-normative))

**Data**

[bdqval:Empty](#bdqval_Empty) |
[bdqval:NotEmpty](#bdqval_NotEmpty) 

**bdqffdq:Parameter**

[bdqval:annotationAlertIf](#bdqval_annotationAlertIf) |
[bdqval:annotationSystem](#bdqval_annotationSystem) |
[bdqval:assumptionOnUnknownBiome](#bdqval_assumptionOnUnknownBiome) |
[bdqval:defaultGeodeticDatum](#bdqval_defaultGeodeticDatum) |
[bdqval:defaultOccurrenceStatus](#bdqval_defaultOccurrenceStatus) |
[bdqval:earliestValidDate](#bdqval_earliestValidDate) |
[bdqval:geospatialLand](#bdqval_geospatialLand) |
[bdqval:includeEventDate](#bdqval_includeEventDate) |
[bdqval:latestValidDate](#bdqval_latestValidDate) |
[bdqval:maximumValidDepthInMeters](#bdqval_maximumValidDepthInMeters) |
[bdqval:maximumValidElevationInMeters](#bdqval_maximumValidElevationInMeters) |
[bdqval:minimumValidDepthInMeters](#bdqval_minimumValidDepthInMeters) |
[bdqval:minimumValidElevationInMeters](#bdqval_minimumValidElevationInMeters) |
[bdqval:sourceAuthority](#bdqval_sourceAuthority) |
[bdqval:spatialBufferInMeters](#bdqval_spatialBufferInMeters) |
[bdqval:taxonIsMarine](#bdqval_taxonIsMarine) 

**bdqffdq:AbstractInformationElement**

[bdqval:AggregatedTestResponseOutcomes](#bdqval_AggregatedTestResponseOutcomes) |
[bdqval:AllAmendmentTestsRunOnSingleRecord](#bdqval_AllAmendmentTestsRunOnSingleRecord) |
[bdqval:AllValidationTestsRunOnSingleRecord](#bdqval_AllValidationTestsRunOnSingleRecord) 

### 3.2 Index By Label (non-normative)

(See also [3.1 Index By Term Name (non-normative)](#31-index-by-term-name-non-normative))

**Data**

[Empty](#bdqval_Empty) |
[NotEmpty](#bdqval_NotEmpty) 

**bdqffdq:Parameter**

[annotationAlertIf](#bdqval_annotationAlertIf) |
[annotationSystem](#bdqval_annotationSystem) |
[assumptionOnUnknownBiome](#bdqval_assumptionOnUnknownBiome) |
[defaultGeodeticDatum](#bdqval_defaultGeodeticDatum) |
[defaultOccurrenceStatus](#bdqval_defaultOccurrenceStatus) |
[earliestValidDate](#bdqval_earliestValidDate) |
[geospatialLand](#bdqval_geospatialLand) |
[includeEventDate](#bdqval_includeEventDate) |
[latestValidDate](#bdqval_latestValidDate) |
[maximumValidDepthInMeters](#bdqval_maximumValidDepthInMeters) |
[maximumValidElevationInMeters](#bdqval_maximumValidElevationInMeters) |
[minimumValidDepthInMeters](#bdqval_minimumValidDepthInMeters) |
[minimumValidElevationInMeters](#bdqval_minimumValidElevationInMeters) |
[sourceAuthority](#bdqval_sourceAuthority) |
[spatialBufferInMeters](#bdqval_spatialBufferInMeters) |
[taxonIsMarine](#bdqval_taxonIsMarine) 

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
			<td>An Abstract Information Element composed of the outcomes of a list of bdqffdq:Validation Tests from a single run on a bdqffdq:SingleRecord in a bdqffdq:DataQualityReport.</td>
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
			<td>Optionally establishes if an annotation exists in a bdqval:ParameterizedTest within a bdqval:annotationSystem by describing the criteria for relating annotations in the system to records within the bdqval:ParameterizedTest, by default the presence of an oa:hasTarget with the bdqffdq:SingleRecord under evaluation as its object.  'PREFIX oa: <http://www.w3.org/ns/oa#> SELECT ?annotation WHERE { ?annotation a oa:Annotation ; oa:hasTarget <evaluated_instance_iri> .  }'</td>
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
			<th colspan="2"><a id="bdqval_defaultOccurrenceStatus"></a>Term Name  bdqval:defaultOccurrenceStatus</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/defaultOccurrenceStatus">https://rs.tdwg.org/bdqval/terms/defaultOccurrenceStatus</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-27</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqval/terms/version/defaultOccurrenceStatus-2026-04-27">https://rs.tdwg.org/bdqval/terms/version/defaultOccurrenceStatus-2026-04-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>defaultOccurrenceStatus</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A provided default value for dwc:occurrenceStatus that is used when a required dwc:occurrenceStatus is bdqval:Empty.</td>
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
			<td>defaultOccurrenceStatus</td>
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
			<td>An authority using the "bdqval" namespace that provides a reference for values required for a Test evaluation. Where the Test is a bdqval:ParameterizedTest a bdqval:defaultSourceAuthority ("bdqval:sourceAuthority default = xxx") is specified.</td>
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


## Glossary (non-normative)

A glossary of acronyms and terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2026. BDQ Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqval/terms/2026-06-03>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
