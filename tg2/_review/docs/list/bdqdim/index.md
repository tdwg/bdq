<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Data Quality Dimension Controlled Vocabulary List of Terms

**Title**<br>
Data Quality Dimension Controlled Vocabulary List of Terms

**Date version issued**<br>
2025-04-11

**Date created**<br>
2025-04-11

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqdim

**This version**<br>
<http://rs.tdwg.org/bdq/bdqdim/terms/2025-04-11>

**Latest version**<br>
<http://rs.tdwg.org/bdq/bdqdim/terms/>

**Previous version**<br>
**Abstract**<br>
This document is a reference for the BDQ Core Standard. It covers the vocabulary terms that are types of bdqffdq:DataQualityDimension (originally defined in Veiga 2016 and Veiga et al. 2017) and form the controlled vocabulary for bdqffdq:hasDataQualityDimension.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([Rauthiflor LLC](http://www.wikidata.org/entity/Q98382028))

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Dimension Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqdim/terms/2025-04-11>

Draft Standard for Review

## 1 Introduction

This document provides the full details of the controlled vocabulary values (individuals of the type bdqffdq:DataQualityDimension) for the term bdqffdq:hasDataQualityDimension in the BDQ Core Tests.

### 1.1 Purpose

This is the term-list document for the bdqdim: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology, especially with respect to the controlled vocabulary for the term bdqffdq:hasDataQualityDimension.

### 1.3 Data Quality Dimensions 

Data Quality Dimension as used in the context of BDQ Core was originally defined by Veiga 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:DataQualityDimension (Completeness, Conformance, Consistency, Likeliness, Reliability, and Resolution) describes the aspect of data quality that a Test examines to assess 'quality' for a given Use Case.

Data Quality Dimensions are measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved.

Each Test in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) against a single bdqffdq:DataQualityDimension. For example, the Test VALIDATION_COUNTRY_FOUND assesses the value of dwc:country against a source authority for a Use Case, (e.g., bdq:Record-Management). The appropriate type of bdqffq:DataQualityDimension in this case is bdqdim:Conformance, i.e., how well does the country value conform to an appropriate reference standard when evaluating the quality of a Darwin Core record in the context of a Use Case in which VALIDATION_COUNTRY_FOUND is found?

Data Quality Dimension applies to all Test types (all subclasses of bsqffdq:DataQualityNeed: bdqffdq:VALIDATION, bdqffdq:ISSUE, bdqffdq:AMENDMENT and bdqffdq:MEASURE).

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqdim/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/docs/list/bdqdim/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/_review/dist/bdqdim.xml | Example for submission, to be generated | 

### 1.5 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

Section [1.8 Key to Vocabulary Terms](#18-Key-to-Vocabulary-Terms) identifies which values in Section 4 are normative and which are non-normative.

Any sentence or phrase beginning with "For example" or "e.g." is non-normative.

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| bdqcore:     | https://rs.tdwg.org/bdqcore/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms           |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema        |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| tdwgutility: | http://rs.tdwg.org/dwc/terms/attributes/    |

### 1.8 Key to Vocabulary Terms

The terminology used to describe the terms in this vocabulary follows the TDWG Standards Documentation Standard (SDS). Each term definition includes the original RDF definition, and may also provide a TDWG-specific interpretation from the SDS, as well as a definition tailored to this local context.

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | Completeness |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqdim/terms/ Completeness](https://rs.tdwg.org/bdqdim/terms/Completeness) |
| Modified (dcterms:issued) | normative | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2024-09-30 |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqdim/terms/version/ Completeness-2024-09-30](https://rs.tdwg.org/bdqdim/terms/version/Completeness-2024-09-30) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Completeness |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | The extent to which data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use. |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension. |
| Status (tdwgutility:status) |  | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |
| Controlled Value String () | normative |  | Completeness |
| Type (rdf:type) | normative | The subject is an instance of a class. | bdqffdq:DataQualityDimension |


## 2 Use of Terms (normative)

A value for `bdqffdq:hasdataQualityDimension` in an RDF context MUST be a Term IRI (e.g., `https://rs.tdwg.org/bdqdim/terms/Completeness`) or Term Qualified name (e.g., `bdqdim:Completeness`) from the bdqdim: namespace. In a non-RDF context in which resources may be used by software (e.g., a value in a spreadsheet or database table) the Controlled Value String (Local name, e.g., `Completeness`) MAY be used. In a purely human context a Label (e.g., `Completeness`) MAY be used.

Each instance of a Test, regardless of Test type, SHOULD have exactly one bdqffdq:hasdataQualityDimension property relating it to a term in this bdqdim: vocabulary.

## 3 Term index
### 3.1 Index By Term Name

(See also [3.2 Index By Label](#32-index-by-label))

**Classes**

**Vocabulary**

[bdqdim:Completeness](#bdqdim_Completeness) |
[bdqdim:Conformance](#bdqdim_Conformance) |
[bdqdim:Consistency](#bdqdim_Consistency) |
[bdqdim:Likeliness](#bdqdim_Likeliness) |
[bdqdim:Reliability](#bdqdim_Reliability) |
[bdqdim:Resolution](#bdqdim_Resolution) 

### 3.2 Index By Label

(See also [3.1 Index By Term Name](#31-index-by-term-name))

**Classes**

[Completeness](#bdqdim_Completeness) |
[Conformance](#bdqdim_Conformance) |
[Consistency](#bdqdim_Consistency) |
[Likeliness](#bdqdim_Likeliness) |
[Reliability](#bdqdim_Reliability) |
[Resolution](#bdqdim_Resolution) 

## 4 Vocabulary
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
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
			<td>The likelihood of Darwin Core Term(s) having true or expected values.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension.</td>
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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Data Quality Dimension Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqdim/terms/2025-04-11>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


