<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Controlled Vocabulary List of Terms

**Title**<br>
BDQ Controlled Vocabulary List of Terms

**Date version issued**<br>
2025-04-11

**Date created**<br>
2025-04-11

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdq

**This version**<br>
<http://rs.tdwg.org/bdq/terms/2025-04-11>

**Latest version**<br>
<http://rs.tdwg.org/bdq/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ Core Standard. It covers some terms used in Test Specifications, and especially values used as bdqffdq:Parameters.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-04-11>

Draft Standard for Review

## 1 Introduction

This document provides the full details of the terms of the bdq: vocabulary (<http://rs.tdwg.org/version/bdq/2025-04-11>). For details and rationale, see Chapman et al. (2020).

### 1.1 Purpose

This is the term-list document for the bdq: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests. 

### 1.3 Data Quality Vocabulary terms.

The bdq: vocabulary inclues four sets of concepts: 
* a list of bdqffdq:UseCases for the bdqcore: Tests
* a list of bdqffdq:Parameters used in the bdqcore: Tests, including the concept of bdq:sourceAuthority and some named sourceAuthority parameters
* a list of named bdqffdq:InformationElements used by MultiRecord Measure Tests
* the concepts bdq:Empty and bdq:NotEmpty.

### 1.4 Term List Distributions

| Description | IRI | Download URL |
| ----------- | --- | -----------  |
| HTML file   | http://rs.tdwg.org/bdq/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdq/index.md |
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/bdq.xml |

### 1.5 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section [1.8 Key to Vocabulary Terms](#18-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dc:          | https://purl.org/dc/elements/1.1/           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| dwciri:      | http://rs.tdwg.org/dwc/iri/                 |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.8 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | Alien-Species |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdq/terms/ Alien-Species](https://rs.tdwg.org/bdq/terms/Alien-Species) |
| Modified (dcterms:issued) | normative | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2024-09-30 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdq/terms/version/ Alien-Species-2024-09-30](https://rs.tdwg.org/bdq/terms/version/Alien-Species-2024-09-30) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Alien-Species |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | Research uses forming a bdqffdq:UseCase for occurrence data of alien species 1) where the Information Elements concern what organism occurred where and when and the means, degree, and pathways of establishment, and 2) that are used for analysis of spatial and/or temporal patterns of biodiversity (see examples in Groom et al. (2019). Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards, 3: e38084. https://doi.org/10.3897/biss.3.38084). |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Used in Measure of Single Record Tests |
| Status (tdwgutility:status) |  | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |
| Controlled Value String () | normative |  | Alien-Species |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:UseCase |


## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdqffdq:` namespace MUST use the Term IRI (e.g., `http://rs.tdwg.org/bdq/bdqffdq/InformationElement`) or Term Qualified name (e.g., `bdqffdq:InformationElement`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `InformationElement`) SHOULD be used. In a purely human context a Label (e.g., `Information Element`) MAY be used.

## 3 Term index (non-normative)
### 3.1 Index By Term Name

(See also [3.2 Index By Label](#32-index-by-label))

**Classes**

**Data**

[bdq:Empty](#bdq_Empty) |
[bdq:NotEmpty](#bdq_NotEmpty) 

**bdq:Parameter**

[bdq:annotationAlertIf](#bdq_annotationAlertIf) |
[bdq:annotationSystem](#bdq_annotationSystem) |
[bdq:assumptionOnUnknownBiome](#bdq_assumptionOnUnknownBiome) |
[bdq:defaultGeodeticDatum](#bdq_defaultGeodeticDatum) |
[bdq:DefaultSourceAuthority](#bdq_DefaultSourceAuthority) |
[bdq:defaultValue](#bdq_defaultValue) |
[bdq:earliestValidDate](#bdq_earliestValidDate) |
[bdq:geospatialLand](#bdq_geospatialLand) |
[bdq:includeEventDate](#bdq_includeEventDate) |
[bdq:latestValidDate](#bdq_latestValidDate) |
[bdq:maximumValidDepthInMeters](#bdq_maximumValidDepthInMeters) |
[bdq:maximumValidElevationInMeters](#bdq_maximumValidElevationInMeters) |
[bdq:minimumValidDepthInMeters](#bdq_minimumValidDepthInMeters) |
[bdq:minimumValidElevationInMeters](#bdq_minimumValidElevationInMeters) |
[bdq:sourceAuthority](#bdq_sourceAuthority) |
[bdq:spatialBufferInMeters](#bdq_spatialBufferInMeters) |
[bdq:taxonIsMarine](#bdq_taxonIsMarine) 

**bdqffdq:UseCase**

[bdq:Alien-Species](#bdq_Alien-Species) |
[bdq:Biotic-Relationships](#bdq_Biotic-Relationships) |
[bdq:Record-Management](#bdq_Record-Management) |
[bdq:Spatial-Temporal_Patterns](#bdq_Spatial-Temporal_Patterns) |
[bdq:Taxon-Management](#bdq_Taxon-Management) 

**bdqffdq:InformationElement**

[bdq:AllAmendmentTestsRunOnSingleRecord](#bdq_AllAmendmentTestsRunOnSingleRecord) |
[bdq:AllValidationTestsRunOnSingleRecord](#bdq_AllValidationTestsRunOnSingleRecord) 

### 3.2 Index By Label

(See also [3.1 Index By Term Name](#31-index-by-term-name))

**Classes**

**Data**

[Empty](#bdq_Empty) |
[NotEmpty](#bdq_NotEmpty) 

**bdq:Parameter**

[DefaultSourceAuthority](#bdq_DefaultSourceAuthority) |
[annotationAlertIf](#bdq_annotationAlertIf) |
[annotationSystem](#bdq_annotationSystem) |
[assumptionOnUnknownBiome](#bdq_assumptionOnUnknownBiome) |
[defaultGeodeticDatum](#bdq_defaultGeodeticDatum) |
[defaultValue](#bdq_defaultValue) |
[earliestValidDate](#bdq_earliestValidDate) |
[geospatialLand](#bdq_geospatialLand) |
[includeEventDate](#bdq_includeEventDate) |
[latestValidDate](#bdq_latestValidDate) |
[maximumValidDepthInMeters](#bdq_maximumValidDepthInMeters) |
[maximumValidElevationInMeters](#bdq_maximumValidElevationInMeters) |
[minimumValidDepthInMeters](#bdq_minimumValidDepthInMeters) |
[minimumValidElevationInMeters](#bdq_minimumValidElevationInMeters) |
[sourceAuthority](#bdq_sourceAuthority) |
[spatialBufferInMeters](#bdq_spatialBufferInMeters) |
[taxonIsMarine](#bdq_taxonIsMarine) 

**bdqffdq:UseCase**

[Alien-Species](#bdq_Alien-Species) |
[Biotic-Relationships](#bdq_Biotic-Relationships) |
[Record-Management](#bdq_Record-Management) |
[Spatial-Temporal Patterns](#bdq_Spatial-Temporal_Patterns) |
[Taxon-Management](#bdq_Taxon-Management) 

**bdqffdq:InformationElement**

[AllAmendmentTestsRunOnSingleRecord](#bdq_AllAmendmentTestsRunOnSingleRecord) |
[AllValidationTestsRunOnSingleRecord](#bdq_AllValidationTestsRunOnSingleRecord) 

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_Alien-Species"></a>Term Name  bdq:Alien-Species</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/Alien-Species">https://rs.tdwg.org/bdq/terms/Alien-Species</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/Alien-Species-2024-09-30">https://rs.tdwg.org/bdq/terms/version/Alien-Species-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Alien-Species</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Research uses forming a bdqffdq:UseCase for occurrence data of alien species 1) where the Information Elements concern what organism occurred where and when and the means, degree, and pathways of establishment, and 2) that are used for analysis of spatial and/or temporal patterns of biodiversity (see examples in Groom et al. (2019). Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards, 3: e38084. https://doi.org/10.3897/biss.3.38084).</td>
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
			<td>Alien-Species</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_AllAmendmentTestsRunOnSingleRecord"></a>Term Name  bdq:AllAmendmentTestsRunOnSingleRecord</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/AllAmendmentTestsRunOnSingleRecord">https://rs.tdwg.org/bdq/terms/AllAmendmentTestsRunOnSingleRecord</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/AllAmendmentTestsRunOnSingleRecord-2024-09-30">https://rs.tdwg.org/bdq/terms/version/AllAmendmentTestsRunOnSingleRecord-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>AllAmendmentTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list of bdqffdq:Amendment Tests that have been run on a bdqffdq:SingleRecord forming the input to another Test.</td>
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
			<td>bdqffdq:InformationElement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_AllValidationTestsRunOnSingleRecord"></a>Term Name  bdq:AllValidationTestsRunOnSingleRecord</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/AllValidationTestsRunOnSingleRecord">https://rs.tdwg.org/bdq/terms/AllValidationTestsRunOnSingleRecord</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/AllValidationTestsRunOnSingleRecord-2024-09-30">https://rs.tdwg.org/bdq/terms/version/AllValidationTestsRunOnSingleRecord-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>AllValidationTestsRunOnSingleRecord</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list of bdqffdq:Validation Tests that have been run on a bdqffdq:SingleRecord.</td>
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
			<td>bdqffdq:InformationElement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_annotationAlertIf"></a>Term Name  bdq:annotationAlertIf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/annotationAlertIf">https://rs.tdwg.org/bdq/terms/annotationAlertIf</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/annotationAlertIf-2024-09-30">https://rs.tdwg.org/bdq/terms/version/annotationAlertIf-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>annotationAlertIf</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes if an annotation exists in a bdq:ParamaterizedTest within a bdq:annotationSystem by describing the criteria for relating annotations in the system to records within the bdq:ParameterizedTest.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Test "ANNOTATION_ISSUE_NOTEMPTY" (bdqcore:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1).</td>
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
			<th colspan="2"><a id="bdq_annotationSystem"></a>Term Name  bdq:annotationSystem</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/annotationSystem">https://rs.tdwg.org/bdq/terms/annotationSystem</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/annotationSystem-2024-09-30">https://rs.tdwg.org/bdq/terms/version/annotationSystem-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>annotationSystem</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes a system for annotations in a bdq:ParamaterizedTest, with the default being the w3c Annotations Data Model's "oa:Annotation"</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Test "ANNOTATION_ISSUE_NOTEMPTY" (bdqcore:fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1).</td>
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
			<th colspan="2"><a id="bdq_assumptionOnUnknownBiome"></a>Term Name  bdq:assumptionOnUnknownBiome</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/assumptionOnUnknownBiome">https://rs.tdwg.org/bdq/terms/assumptionOnUnknownBiome</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/assumptionOnUnknownBiome-2024-09-30">https://rs.tdwg.org/bdq/terms/version/assumptionOnUnknownBiome-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>assumptionOnUnknownBiome</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Used when a bdq:taxonomyIsMarine source authority is unable to assert the marine or non-marine status of a taxon, the biome (either "marine or "nonmarine") to assume, with the default being "noassumption".</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT (bdqcore:b9c184ce-a859-410c-9d12-71a338200380).</td>
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
			<th colspan="2"><a id="bdq_Biotic-Relationships"></a>Term Name  bdq:Biotic-Relationships</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/Biotic-Relationships">https://rs.tdwg.org/bdq/terms/Biotic-Relationships</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/Biotic-Relationships-2024-09-30">https://rs.tdwg.org/bdq/terms/version/Biotic-Relationships-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Biotic-Relationships</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Research uses forming a bdqffdq:UseCase for relationships between organisms 1) where the bdqffdq:InformationElements concern what organisms have a relationship and 2) that are used for analysis of the relationship of one organism to another (see examples in: Poelen JH, Simons JD, Mungall CJ. (2014). Global Biotic Interactions: An open infrastructure to share and analyze species-interaction datasets. Ecological Informatics, 24, 148–159. https://doi.org/10.1016/j.ecoinf.2014.08.005).</td>
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
			<td>Biotic-Relationships</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_defaultGeodeticDatum"></a>Term Name  bdq:defaultGeodeticDatum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/defaultGeodeticDatum">https://rs.tdwg.org/bdq/terms/defaultGeodeticDatum</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/defaultGeodeticDatum-2024-09-30">https://rs.tdwg.org/bdq/terms/version/defaultGeodeticDatum-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>defaultGeodeticDatum</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the default geodetic datum in a bdq:ParamaterizedTest. A default geodetic datum is supplied in cases where a bdq:Parameter is not set at the time the Test is run.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See Test AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT (bdqcore:7498ca76-c4d4-42e2-8103-acacccbdffa7).</td>
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
			<th colspan="2"><a id="bdq_DefaultSourceAuthority"></a>Term Name  bdq:DefaultSourceAuthority</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/DefaultSourceAuthority">https://rs.tdwg.org/bdq/terms/DefaultSourceAuthority</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/DefaultSourceAuthority-2024-09-30">https://rs.tdwg.org/bdq/terms/version/DefaultSourceAuthority-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>DefaultSourceAuthority</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A provided default bdq:SourceAuthority that is used when a required bdq:Parameter specifying a bdq:sourceAuthority has not been provided at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_defaultValue"></a>Term Name  bdq:defaultValue</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/defaultValue">https://rs.tdwg.org/bdq/terms/defaultValue</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/defaultValue-2024-09-30">https://rs.tdwg.org/bdq/terms/version/defaultValue-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>defaultValue</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A preselected value (e.g. year, elevation) to be used where a required bdq:Parameter value has not been provided at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_earliestValidDate"></a>Term Name  bdq:earliestValidDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/earliestValidDate">https://rs.tdwg.org/bdq/terms/earliestValidDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/earliestValidDate-2024-09-30">https://rs.tdwg.org/bdq/terms/version/earliestValidDate-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>earliestValidDate</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the earliest date in a bdq:ParamaterizedTest. A default date is supplied in cases where a bdq:Parameter is not set at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_Empty"></a>Term Name  bdq:Empty</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/Empty">https://rs.tdwg.org/bdq/terms/Empty</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/Empty-2024-09-30">https://rs.tdwg.org/bdq/terms/version/Empty-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Empty</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An evaluation of a value, which in the context of the evaluation, returns true if the value does not contain any characters or values other than those in the range U+0000 to U+0020, otherwise returns false. </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See also: bdq:notEmpty. In BDQ Core, bdq:Empty is used to evaluate bdqffdq:InformationElements within a Test specification, it therefore means empty if the dataset being evaluated does not contain the term matching the Information Element, or if the dataset contains that term but the value for that term is empty. The phrasing 'in the context of the evauation' is to allow the Test implementations to be independent of, and agnostic about the data structures presented to a framework for executing the Tests and the framework within which the Tests are run. The term bdq:Empty is defined to be more broadly usable than just with bdqcore. Note: A bdqffdq:InformationElement containing invalid characters (e.g., letters in an Information Element that would be expected to contain integers) or values (including string serializations of the NULL value) are bdq:notEmpty and their invalidity must be separately detected. The definition of bdq:empty is not applicable to a discussion of what value to include in a controlled vocabulary to indicate that no meaningful value is present, so no suggestion is made that bdq:empty should be used as a data value to represent some form of 'Null', 'unknown', 'not recorded', etc. Choices there would fall into the semantics for some set of controlled vocabularies. The relevance to such a discussion is that the definition of bdq:empty would treat an empty string as an empty value, with no semantics attached as to why the value is empty</td>
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
			<th colspan="2"><a id="bdq_geospatialLand"></a>Term Name  bdq:geospatialLand</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/geospatialLand">https://rs.tdwg.org/bdq/terms/geospatialLand</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/geospatialLand-2024-09-30">https://rs.tdwg.org/bdq/terms/version/geospatialLand-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>geospatialLand</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdq:sourceAuthority consisting of polygons that have been derived from a union of Natural Earth vectors for Land and for Minor Islands at 1:10,000,000 resolution.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT (bdqcore:b9c184ce-a859-410c-9d12-71a338200380)</td>
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
			<th colspan="2"><a id="bdq_includeEventDate"></a>Term Name  bdq:includeEventDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/bdq:includeEventDate">https://rs.tdwg.org/bdq/terms/bdq:includeEventDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/bdq:includeEventDate-2024-09-30">https://rs.tdwg.org/bdq/terms/version/bdq:includeEventDate-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>includeEventDate</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Allows dwc:eventDate to be excluded in a bdq:ParameterizedTest. The default is to include the event date in the Test, but it may be excluded to allow an identification to be prior to the dwc:eventDate.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Used in Test "VALIDATION_DATEIDENTIFIED_INRANGE" (bdqcore:dc8aae4b-134f-4d75-8a71-c4186239178e).</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>bdq:includeEventDate</td>
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
			<th colspan="2"><a id="bdq_latestValidDate"></a>Term Name  bdq:latestValidDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/latestValidDate">https://rs.tdwg.org/bdq/terms/latestValidDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/latestValidDate-2024-09-30">https://rs.tdwg.org/bdq/terms/version/latestValidDate-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>latestValidDate</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the latest date in a bdq:ParameterizedTest. A default date is supplied in cases where a bdq:Parameter is not set at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_maximumValidDepthInMeters"></a>Term Name  bdq:maximumValidDepthInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/maximumValidDepthInMeters">https://rs.tdwg.org/bdq/terms/maximumValidDepthInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/maximumValidDepthInMeters-2024-09-30">https://rs.tdwg.org/bdq/terms/version/maximumValidDepthInMeters-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>maximumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the maximum depth in a bdq:ParameterizedTest. A default depth is supplied in cases where a bdq:Parameter is not set at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_maximumValidElevationInMeters"></a>Term Name  bdq:maximumValidElevationInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/maximumValidElevationInMeters">https://rs.tdwg.org/bdq/terms/maximumValidElevationInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/maximumValidElevationInMeters-2024-09-30">https://rs.tdwg.org/bdq/terms/version/maximumValidElevationInMeters-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>maximumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the highest elevation in a bdq:ParameterizedTest. A default elevation is supplied in cases where a bdq:Parameter is not set at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_minimumValidDepthInMeters"></a>Term Name  bdq:minimumValidDepthInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/minimumValidDepthInMeters">https://rs.tdwg.org/bdq/terms/minimumValidDepthInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/minimumValidDepthInMeters-2024-09-30">https://rs.tdwg.org/bdq/terms/version/minimumValidDepthInMeters-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>minimumValidDepthInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the minimum depth in a bdq:ParameterizedTest. A default depth is supplied in cases where a bdq:Parameter is not set at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_minimumValidElevationInMeters"></a>Term Name  bdq:minimumValidElevationInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/minimumValidElevationInMeters">https://rs.tdwg.org/bdq/terms/minimumValidElevationInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/minimumValidElevationInMeters-2024-09-30">https://rs.tdwg.org/bdq/terms/version/minimumValidElevationInMeters-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>minimumValidElevationInMeters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Optionally establishes the lowest elevation in a bdq:ParameterizedTest. A default elevation is supplied in cases where a bdq:Parameter is not set at the time the Test is run.</td>
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
			<th colspan="2"><a id="bdq_NotEmpty"></a>Term Name  bdq:NotEmpty</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/NotEmpty">https://rs.tdwg.org/bdq/terms/NotEmpty</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/NotEmpty-2024-09-30">https://rs.tdwg.org/bdq/terms/version/NotEmpty-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>NotEmpty</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An evaluation of a value, which in the context of the evaluation, returns false if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns true. </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See also: bdq:empty. In BDQ Core, bdq:NotEmpty is used to evaluate bdqffdq:InformationElements within a Test specification. Common string serializations of null such as '\N', 'NA', 'NaN', and NULL are treated as bdq:notEmpty. If '\N' is present in a dataset, Tests are expected to explicitly treat that value as bdq:notEmpty, and then try to evaluate it against whatever other criteria may apply. The term bdq:NotEmpty is defined to be more broadly usable than the scope of BDQ Tests. </td>
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
			<th colspan="2"><a id="bdq_Record-Management"></a>Term Name  bdq:Record-Management</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/Record-Management">https://rs.tdwg.org/bdq/terms/Record-Management</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/Record-Management-2024-09-30">https://rs.tdwg.org/bdq/terms/version/Record-Management-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Record-Management</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase that documents the management of the quality of biodiversity data records (see examples in Rees ER & Nicholls M (2020) Data Quality Use Case Study Results. Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2).</td>
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
			<td>Record-Management</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_sourceAuthority"></a>Term Name  bdq:sourceAuthority</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/sourceAuthority">https://rs.tdwg.org/bdq/terms/sourceAuthority</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/sourceAuthority-2024-09-30">https://rs.tdwg.org/bdq/terms/version/sourceAuthority-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>sourceAuthority</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An authority using the "bdq" namespace that provides a reference for values required for a Test evaluation. Where the Test is a bdq:ParameterizedTest a bdq:defaultSourceAuthority ("bdq:sourceAuthority default = xxx") is specified.</td>
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
			<th colspan="2"><a id="bdq_Spatial-Temporal_Patterns"></a>Term Name  bdq:Spatial-Temporal_Patterns</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/Spatial-Temporal_Patterns">https://rs.tdwg.org/bdq/terms/Spatial-Temporal_Patterns</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/Spatial-Temporal_Patterns-2024-09-30">https://rs.tdwg.org/bdq/terms/version/Spatial-Temporal_Patterns-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Spatial-Temporal Patterns</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Research uses forming a bdqffdq:UseCase for biodiversity occurrence data 1) where the Information Elements concern what organism occurred where and when and 2) that are used for analysis of spatial and/or temporal patterns of biodiversity (see examples in Rees ER & Nicholls M (2020) Data Quality Use Case Study Results. Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2).</td>
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
			<td>Spatial-Temporal Patterns</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_spatialBufferInMeters"></a>Term Name  bdq:spatialBufferInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/spatialBufferInMeters">https://rs.tdwg.org/bdq/terms/spatialBufferInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/spatialBufferInMeters-2024-09-30">https://rs.tdwg.org/bdq/terms/version/spatialBufferInMeters-2024-09-30</a></td>
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
			<th colspan="2"><a id="bdq_Taxon-Management"></a>Term Name  bdq:Taxon-Management</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/Taxon-Management">https://rs.tdwg.org/bdq/terms/Taxon-Management</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/Taxon-Management-2024-09-30">https://rs.tdwg.org/bdq/terms/version/Taxon-Management-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon-Management</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase that documents the management of the quality of taxonomic names (see examples in Rees ER & Nicholls M (2020) Data Quality Use Case Study Results Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2).</td>
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
			<td>Taxon-Management</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:UseCase</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdq_taxonIsMarine"></a>Term Name  bdq:taxonIsMarine</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/taxonIsMarine">https://rs.tdwg.org/bdq/terms/taxonIsMarine</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdq/terms/version/taxonIsMarine-2024-09-30">https://rs.tdwg.org/bdq/terms/version/taxonIsMarine-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>taxonIsMarine</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdq:sourceAuthority that uses dwc:scientificName to deterrmine the "marine" or "non-marine" status of a taxon using the "Environment" term obtained from the World Register of Marine Species (WORMS) database.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT (bdqcore:b9c184ce-a859-410c-9d12-71a338200380).</td>
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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/terms/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


