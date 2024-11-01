<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Data Quality Dimension Controlled Vocabulary List of Terms

Title
: Data Quality Dimension Controlled Vocabulary List of Terms

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Preferred namespace abbreviation
: bdqdim

This version
: <http://rs.tdwg.org/bdq/bdqdim/terms/2024-09-10>

Latest version
: <http://rs.tdwg.org/bdq/bdqdim/terms/>

Abstract
: This document describes the vocabulary terms used in the (Draft) BDQ Core Standard as values of bdqffdq:DataQualityDimension, originally defined in Veiga 2016 and Veiga et al. 2017.

Authors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Data Quality Dimension Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqdim/terms/2024-09-10>

Draft Standard for Submission


## 1 Introduction

This document includes terms that are individuals of type bdqffdq:DataQualityDimension intended to be used as a controlled value for bdqffdq:hasDataQualityDimension in the BDQ Core tests.

### 1.1 Purpose

This is the term-list document for the bdqdim: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.

### 1.3 Data Quality Dimensions 

DataQualityDimension as used in the context of BDQ Core, was originally defined by Veiga 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:DataQualityDimension (Completeness, Conformance, Consistency, Likeliness, Reliability, and Resolution) describes the aspect of data quality that a test examines to assess 'quality' for a given use case.

DataQualityDimensions are measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved.

Each test in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) against a single bdqffdq:DataQualityDimension. For example, the test VALIDATION_COUNTRY_FOUND tests the value of dwc:country against a source authority for a use case, (e.g.  bdq:Record-Management).  The appropriate type of bdqffq:DataQualityDimension in this case is bdqdim:Conformance: i.e. how well does the country value conform to an appropriate reference standard when you are evaluating the quality of a Darwin Core record (in the context of the use case with which VALIDATION_COUNTRY_FOUND is composed)?

DataQualityDimension applies to all Test Types (all subclasses of bsqffdq:DataQualityNeed that is, bdqffdq:VALIDATION, bdqffdq:ISSUE, bdqffdq:MEASURE and bdqffdq:AMENDMENT).

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqdim/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqdim/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqdim.xml | Example for submission, to be generated | 

### 1.5 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

In Section 4, the values of the `Term IRI`, `Term Name`, `Type`, `Definition` and `Controlled value` are normative. The values of `Comments`, `Label` and `Preferred Label` are non-normative. 

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bdqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |

### 1.8 Key to Vocabulary Terms

| Label (Term) | Definition | Example | Normative | 
| ------------ | ---------- | ------- | --------- |
| Comments (rdfs:comment) | A description of the subject resource. | Definition from the Fitness for Use Framework: Data Quality Dimensions Document  https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension. | non-normative |
| Controlled Value () | A string that is unique within a controlled vocabulary that identifies the concept in the context of a text-based metadata transfer system. The value MUST consist of Unicode characters. | Completeness | normative |
| Definition (skos:definition) | A statement or formal explanation of the meaning of a concept. | The extent to which data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use. | normative |
| Term Version IRI (rdf:about) | The HTTP IRI that identifies the version of the term that is currently in force. | https://rs.tdwg.org/bdqdim/terms/version/Completeness-2024-09-30 | normative |
| Modified (dcterms:issued) | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2024-09-30 | normative |
| Label (rdfs:label) | A human-readable name for the subject. | Completeness | normative |
| Preferred Label (skos:prefLabel) | The preferred lexical label for a resource, in a given language. | Completeness | non-normative |
| Type (rdf:type) | The subject is an instance of a class. | bdqffdq:DataQualityDimension | normative |
| Status (tdwgutility:status) | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |  |
| Term IRI (dcterms:isVersionOf) | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | https://rs.tdwg.org/bdqdim/terms/Completeness | normative |
| Term Name (rdf:value) | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | Completeness | normative |


## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of `bdqffdq:dataQualityDimension`.

Each individual instance of subclasses of bdqffdq:DataQualityNeed SHOULD have exactly one bdqffdq:hasDataQualityDimension property relating it to a term in this bdqdim: vocabulary.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Data Quality Dimension Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqdim/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


