<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# BDQ Use Case Controlled Vocabulary

**Title**<br>
BDQ Use Case Controlled Vocabulary

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdquc

**This version**<br>
<http://rs.tdwg.org/bdquc/terms/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdquc/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ standard. It covers named individual Use Cases.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Use Case Controlled Vocabulary. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdquc/terms/2025-05-10>

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

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to provide the full term list for the `bdquc:` controlled vocabulary, which supports the specification and use of BDQ Tests. The `bdquc:` vocabulary provides the 'Use Cases` defined as part of the BDQ Standard.

This term list defines the formal structure and meanings of these concepts and provides reference material for implementation and documentation purposes.

### 1.2 Audience (non-normative)

TODO: Rework for just Use Cases


This document is intended for technical users who need a precise understanding of the vocabulary elements used in BDQ Test `Specifications` and reports. It will be particularly useful for:

- Implementers interpreting or extending BDQ Test logic
- Standards developers and data quality modelers working with BDQ vocabularies
- Analysts and system designers configuring parameterized data quality assessments
- Curators needing to understand the conceptual basis for different Test evaluations

Familiarity with RDF vocabularies and the Fitness For Use Framework is recommended for full comprehension, but the document is organized to be accessible for any reader needing detailed term definitions.

### 1.3 Data Quality Vocabulary Terms (non-normative)

The `bdqval:` vocabulary covers one set of concepts used across the BDQ standard:

- **Use Cases** (`bdqffdq:UseCase`) – formal representations of the purposes for which data might be evaluated using BDQ Tests.

### 1.4 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.5 Term List Distributions (non-normative)

| Description | IRI | Download URL |
| ----------- | --- | -----------  |
| HTML file   | http://rs.tdwg.org/bdquc/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdquc/index.md |
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/bdquc.xml |

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
| bdqval:      | https://rs.tdwg.org/bdqval/terms/           |
| bdquc:       | https://rs.tdwg.org/bdquc/terms/            |
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
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | Alien-Species |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdquc/terms/ Alien-Species](https://rs.tdwg.org/bdquc/terms/Alien-Species) |
| Modified (dcterms:issued) | normative | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2026-04-22 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdquc/terms/version/ Alien-Species-2026-04-22](https://rs.tdwg.org/bdquc/terms/version/Alien-Species-2026-04-22) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Alien-Species |
| Definition (rdfs:comment) | normative | A description of the subject resource. TDWG SDS: The normative definition of the term, written in English. | A bdqffdq:UseCase that involves the identification and analysis of whether the occurrence of a taxon is native to a location or not, how it got there and to what extent the taxon has become a permanent feature of the location in order to improve the management and reduce the spread of alien species. |
| Comments (skos:note) | non-normative | A general note, for any purpose. | See Groom et al. (2019). Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards, 3: e38084. https://doi.org/10.3897/biss.3.38084. |
| Status (tdwgutility:status) |  | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |
| Controlled Value String () | normative |  | Alien-Species |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:UseCase |
| Fitness Requirements (bdqffdq:hasFitnessRequirements) | non-normative | The property of a bdqffdq:UseCase that provides text listing the qualities that data must have to be fit for a given use. | Data are fit for this use when occurrence records can be reliably interpreted for alien-species management: the organism identity, observation status, and establishment context are present and standard.  <ul><li>Organism identity is usable: Taxon/scientific name terms (e.g., dwc:scientificName, related dwc:Taxon terms, and identifiers where provided) are present, resolvable to a taxonomic authority, and consistent.  </li><li>Establishment context is usable: Terms defining the invasion status (dwc:establishmentMeans, dwc:degreeOfEstablishment, dwc:pathway) are present when relevant, valid and standard.  </li><li>Observation Status is present in valid form to reliably distinguish between presence and absence records; dwc:occurrenceStatus is present, valid and  standardizable.  </li><li>Metadata context (dwc:basisOfRecord and dc:type) is present, valid, and standard so record meaning is consistent in downstream use.  </li></ul>  |
| Scope Note (skos:scopeNote) | non-normative | A note that helps to clarify the meaning and/or the use of a concept. | Darwin Core Occurrences |


## 2 Use of Terms (normative)

In an RDF context, a reference to a term in the `bdquc:` namespace MUST use the Term IRI (e.g., `https://rs.tdwg.org/bdquc/terms/NotEmpty`) or Term Qualified name (e.g., `bdquc:NotEmpty`). In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (local name, e.g., `NotEmpty`) SHOULD be used. In a purely human context a label (e.g., `Not Empty`) MAY be used.

## 3 Term index (non-normative)
### 3.1 Index By Term Name (non-normative)

(See also [3.2 Index By Label (non-normative)](#32-index-by-label-non-normative))

**Vocabulary**

[bdquc:Alien-Species](#bdquc_Alien-Species) |
[bdquc:SDM-Trees](#bdquc_SDM-Trees) |
[bdquc:Spatial-Temporal_Patterns](#bdquc_Spatial-Temporal_Patterns) |
[bdquc:Taxon-Management](#bdquc_Taxon-Management) 

### 3.2 Index By Label (non-normative)

(See also [3.1 Index By Term Name (non-normative)](#31-index-by-term-name-non-normative))

[Alien-Species](#bdquc_Alien-Species) |
[Spatial-Temporal Patterns](#bdquc_Spatial-Temporal_Patterns) |
[Taxon-Management](#bdquc_Taxon-Management) 

## 4 Vocabulary (normative)
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdquc_Alien-Species"></a>Term Name  bdquc:Alien-Species</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/Alien-Species">https://rs.tdwg.org/bdquc/terms/Alien-Species</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/version/Alien-Species-2026-04-22">https://rs.tdwg.org/bdquc/terms/version/Alien-Species-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Alien-Species</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase that involves the identification and analysis of whether the occurrence of a taxon is native to a location or not, how it got there and to what extent the taxon has become a permanent feature of the location in order to improve the management and reduce the spread of alien species.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See Groom et al. (2019). Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards, 3: e38084. https://doi.org/10.3897/biss.3.38084.</td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for this use when occurrence records can be reliably interpreted for alien-species management: the organism identity, observation status, and establishment context are present and standard.  <ul><li>Organism identity is usable: Taxon/scientific name terms (e.g., dwc:scientificName, related dwc:Taxon terms, and identifiers where provided) are present, resolvable to a taxonomic authority, and consistent.  </li><li>Establishment context is usable: Terms defining the invasion status (dwc:establishmentMeans, dwc:degreeOfEstablishment, dwc:pathway) are present when relevant, valid and standard.  </li><li>Observation Status is present in valid form to reliably distinguish between presence and absence records; dwc:occurrenceStatus is present, valid and  standardizable.  </li><li>Metadata context (dwc:basisOfRecord and dc:type) is present, valid, and standard so record meaning is consistent in downstream use.  </li></ul> </td>
		</tr>
		<tr>
			<td>Scope note</td>
			<td>Darwin Core Occurrences</td>
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
			<th colspan="2"><a id="bdquc_SDM-Trees"></a>Term Name  bdquc:SDM-Trees</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/version/SDM-Trees">https://rs.tdwg.org/bdquc/terms/version/SDM-Trees</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/version/SDM-Trees-2026-04-26">https://rs.tdwg.org/bdquc/terms/version/SDM-Trees-2026-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Species-Distribution-Modeling-Trees</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase for improving the quality of, and selecting dwc:Occurrence records suitable for predicting the spatial distribution of tree species. This Use Case filters for occurrence records that meet criteria for a known species at a known location and date.  Records can be further filtered to meet the requirements of the predictive modeling of specific tree species distributions (e.g., Eucalypts) using high-precision occurrence data and environmental variables to evaluate modeling methodologies and refine expert distribution envelopes. </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>References: <ul><li>Gill, A.M., Belbin, L. and Chippendale, G.M. (1985). Phytogeography of EUCALYPTUS in Australia. Bureau of Flora and Fauna, Australian Flora and Fauna Series, 3. Canberra. 53p. ISBN:  0644040815. </li><li>Phillips, S. J., Anderson, R. P., and Schapire, R. E. (2006). Maximum entropy modeling of species geographic distributions. Ecological Modeling, 190(3-4), 231-259.  </li><li>Guisan, A. Edwards, T.C. and Hastie, T. (2002). Generalized linear and generalized additive models in studies of species distributions: setting the scene. Ecological Modeling 157, 89-100.</li></ul></td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for the use case bdquc:Species-Distribution-Modeling-Trees when records have valid:  <ul><li>dwc:scientificName identified to species level.  </li><li>dwc:basisOfRecord = "Occurrence".   </li><li>dwc:occurrenceStatus = "present".  </li><li>dwc:decimalLatitude and dwc:decimalLongitude.  </li><li>dwc:coordinateUncertaintyInMeters less than 500.  </li><li>dwc:dataGeneralizations = bdqval:empty.  </li><li>dwc:year or dwc:eventDate within provided temporal limits. </li></ul></td>
		</tr>
		<tr>
			<td>Scope note</td>
			<td>Darwin Core Occurrences</td>
		</tr>
		<tr>
			<td>Status</td>
			<td>recommended</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Species-Distribution-Modeling-Trees</td>
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
			<th colspan="2"><a id="bdquc_Spatial-Temporal_Patterns"></a>Term Name  bdquc:Spatial-Temporal_Patterns</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/Spatial-Temporal_Patterns">https://rs.tdwg.org/bdquc/terms/Spatial-Temporal_Patterns</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/version/Spatial-Temporal_Patterns-2026-04-22">https://rs.tdwg.org/bdquc/terms/version/Spatial-Temporal_Patterns-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Spatial-Temporal Patterns</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase that pertains to dwc:Occurrence data where the Information Elements concerning what dwc:Organism occurred when at what location are used for analysies such as of taxon distributions across space and time to quantify biodiversity patterns, identify range shifts, or modeling of ecological niches. </td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See Rees ER and Nicholls M (2020) Data Quality Use Case Study Results. Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2.</td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for the Use Case bdquc:Spatial-Temporal_Patterns when occurrence records can be reliably interpreted as organism occurrences in space and time: the organism identity is usable, the location is usable (with adequate precision and metadata), textual geography data is consistent with the coordinates, the event date is usable and internally consistent, and any generalization (spatial or temporal) is detectable so users can decide whether the record is fit at the intended analysis scale. <ul><li>Organism identity is usable: Taxon and scientific name terms (e.g., dwc:scientificName and related taxon terms) are present and sufficiently resolvable and consistent to support analyses of spatio-temporal patterns of organisms.  </li><li>Location is usable and interpretable (including precision and metadata): Coordinates are present, are in-range, and are accompanied by adequate spatial metadata (e.g., uncertainty and spatial reference such as datum); obvious artifact coordinates (e.g., zeros) are detectable.  </li><li>Textual geography is coherent with coordinates: Textual geography fields (e.g., dwc:countryCode, dwc:country, dwc:stateProvince) are valid and standardizable and consistent with the coordinates.  </li><li>Date is usable and internally consistent: dwc:eventDate is present, valid, in standard form and consistent with other temporal terms (e.g. dwc:year) terms when those are provided. Generalization and low precision are detectable: Any indication that the record has been generalized (via dwc:dataGeneralizations) is available along with coordinate uncertainty, broad and interval event dates, and taxonomic rank so that users can judge whether records are fit for the intended spatial and temporal resolution.  </li></ul></td>
		</tr>
		<tr>
			<td>Scope note</td>
			<td>Darwin Core Occurrences</td>
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
			<th colspan="2"><a id="bdquc_Taxon-Management"></a>Term Name  bdquc:Taxon-Management</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/Taxon-Management">https://rs.tdwg.org/bdquc/terms/Taxon-Management</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2026-04-22</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdquc/terms/version/Taxon-Management-2026-04-22">https://rs.tdwg.org/bdquc/terms/version/Taxon-Management-2026-04-22</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon-Management</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A bdqffdq:UseCase that involves the nomenclatural audit, taxonomic verification, and systematic organization of taxon names and associated metadata to ensure identification stability and compliance with global taxonomic standards.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>See Rees ER and Nicholls M (2020) Data Quality Use Case Study Results. Biodiversity Information Science and Standards 4: e50889, suppl. 2. https://doi.org/10.3897/biss.4.50889.suppl2.</td>
		</tr>
		<tr>
			<td>Fitness requirements</td>
			<td>Data are fit for this use when when taxonomic information is sufficient to unambiguously resolve organism identity and position within a nomenclatural hierarchy. Taxon terms are sufficient to resolve the organism (or flag ambiguity), core name and rank terms (e.g., dwc:scientificName, dwc:taxonRank) are present and align with an appropriate bdqval:sourceAuthority, name strings are consistent with atomized name fields and identifiers or authorship, identification dates are valid and plausible, and key contextual metadata (e.g., dwc:basisOfRecord, and controlled fields such as dwc:typeStatus and dwc:sex where relevant) are usable.  <ul><li>Taxon can be resolved: Taxon terms are present and sufficient to support unambiguous resolution (dwc:scientificName, dwc:scientificNameAuthorship, dwc:scientificNameID).  </li><li>Names and ranks are authoritative: dwc:scientificName and required rank and classification terms are present, standardizable, and consistent with the bdqval:sourceAuthority.  </li><li>Name fields are consistent: dwc:scientificName agrees with atomized name fields; authorship is provided where needed.  </li><li>Identifiers are usable: Identifiers (e.g., dwc:scientificNameID) are present when available and correctly formed; dwc:taxonRank is present and valid.  </li><li>Identification timing is usable: dwc:dateIdentified is present when needed, ISO-valid, and temporally plausible (and consistent with dwc:eventDate when provided).  </li><li>Supporting context is usable: dwc:basisOfRecord and other relevant controlled and context fields are present and valid; basic space/time fields are in standard form where used to support curation decisions. </li></ul></td>
		</tr>
		<tr>
			<td>Scope note</td>
			<td>Darwin Core dwc:Taxon terms.</td>
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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Use Case Controlled Vocabulary. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdquc/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
