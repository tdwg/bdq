<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Data Quality Criterion Controlled Vocabulary List of Terms

Title
: Data Quality Criterion Controlled Vocabulary List of Terms

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Preferred namespace abbreviation
: bdqcrit

This version
: <http://rs.tdwg.org/bdq/bdqcrit/terms/2024-09-10>

Latest version
: <http://rs.tdwg.org/bdq/bdqcrit/terms/>

Abstract
: This document describes the vocabulary terms used in the (Draft) BDQ Core Standard as values of bdqffdq:Criterion, originally defined in Veiga 2016 and Veiga et al. 2017.

Authors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Data Quality Criterion Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqcrit/terms/2024-09-10>

Draft Standard for Submission

## 1 Introduction

This document includes terms that are individuals of type bdqffdq:Criterion intended to be used as a controlled value for bdqffdq:hasCriterion in the BDQ Core tests.

### 1.1. Purpose

This is the term-list document for the bdqcrit: vocabulary.

### 1.2 Audience

This document is for those needing a technical understanding of the BDQ Core Tests and the application of the Framework Ontology.

### 1.3 Data Quality Criteria

Criterion as used in the context of BDQ Core, was originally defined by Veiga 2016 and Veiga et at. 2017 as a fundamental concept. The concept of bdqffdq:Criterion (Complete, Consistent, Found, InRange, Likely, NotEmpty, Standard, Unambiguous) describes, in abstract terms how data can be evaluated for quality for a given use case.
  
A criterion expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Criteria have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

Each bdqffdq:Validation and bdqffdq:Issue in bdqcore: is expected to evaluate one or more data values (one or more bdqffdq:InformationElements) following a single bdqffdq:Criterion. For example, the test VALIDATION_COUNTRY_FOUND tests the value of dwc:country against a source authority for a use case, (e.g.  bdq:Record-Management).  The appropriate type of bdqffq:Criterion in this case is bdqcrit:Found i.e. does the value of dwc:contry conform to the values in a specfied authority when you are evaluating the quality of a Darwin Core record (in the context of the use case with which VALIDATION_COUNTRY_FOUND is composed)?

Criterion applies only Test Types bdqffdq:Validation and bdqffdq:Issue.

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqcrit/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqcrit/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqcrit.xml | Example for submission, to be generated | 

### 1.5 Status of the content of this document

Section 1 is non-normative.

Section 2 is normative.

In Section 4, the values of the `Term IRI`, `Term Name`, `Type`, `Definition` and `Controlled value` are normative. The values of `Comments`, `Label` and `Preferred Label` are non-normative. 

### 1.6 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.7 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| ------ | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqcrit: | https://rs.tdwg.org/bdqcrit/terms |
| bdqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.8 Key to Vocabulary Terms

| Label (Term) | Definition | Example | Normative | 
| ------------ | ---------- | ------- | --------- |
| Comments (rdfs:comment) | A description of the subject resource. | Data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use.  Corresponding dimension is bdqdim:Completeness | non-normative |
| Controlled Value () | A string that is unique within a controlled vocabulary that identifies the concept in the context of a text-based metadata transfer system. The value MUST consist of Unicode characters. | Complete | normative |
| Definition (skos:definition) | A statement or formal explanation of the meaning of a concept. | Data are present and sufficiently comprehensive for use. | normative |
| Term Version IRI (rdf:about) | The HTTP IRI that identifies the version of the term that is currently in force. | https://rs.tdwg.org/bdqcrit/terms/Complete-2024-09-30 | normative |
| Modified (dcterms:issued) | Date of formal issuance of the resource. TDWG SDS: The date in ISO 8601 Date format on which the most recent version of the term was issued. | 2024-09-30 | normative |
| Label (rdfs:label) | A human-readable name for the subject. | Complete | normative |
| Preferred Label (skos:prefLabel) | The preferred lexical label for a resource, in a given language. | Complete | non-normative |
| Type (rdf:type) | The subject is an instance of a class. | bdqffdq:Criterion | normative |
| Status (tdwgutility:status) | Used to indicate if the term is recommended for use or if it is only of historical significance. | recommended |  |
| Term IRI (dcterms:isVersionOf) | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | https://rs.tdwg.org/bdqcrit/terms/Complete | normative |
| Term Name (rdf:value) | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | Complete | normative |


## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used values of `bdqffdq:Criterion`.

Each bdqffdq:Validation and bdqffdq:Issue SHOULD have exactly one bdqffdq:hasCriterion property relating it to a term in this bdqcrit: vocabulary.

Instances of bdqffdq:Measure and bdqffdq:Amendment SHOULD NOT have bdqffdq:hasCriterion properties relating them to a term in this bdqcrit: vocabulary.

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Data Quality Criterion Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqcrit/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


