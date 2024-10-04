<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
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
: This document is a reference for the (Draft) BDQ Core Standard, documenting vocabulary values for the BDQ Core term Dimension.  Dimension describes the aspect of data quality (accuracy, precision, completeness, etc.) that a test examines. For example, "precision" in "coordinate precision of single records". Includes Completeness, Conformance, Consistency, Likeliness, Reliability, and Resolution.

Contributors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028)), [Yi-Ming Gan](https://orcid.org/0000-0001-7087-2646) ([Royal Belgian Institute of Natural Sciences](http://www.wikidata.org/entity/Q16665660)), [António Mauro Saraiva](https://orcid.org/0000-0003-2283-1123) ([Universidade de São Paulo](https://www.wikidata.org/wiki/Q835960)), [Alan Koch Veiga](http://orcid.org/0000-0003-2672-8115) (Universidade de São Paulo), [Paula F Zermoglio](https://orcid.org/0000-0002-6056-5084) ([Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN): San Carlos de Bariloche](https://www.irnad.com/)), [Alexander Thompson](https://orcid.org/0000-0002-8981-4048) ([Google](https://www.wikidata.org/wiki/Q95)), David Lowery , [Christian Gendreau](https://orcid.org/000-0003-4898-4291) ([XXXXXXXX](https://www.wikidata.org/wiki/XXXXXXX)), [Tim Roberston](https://orcid.org/0000-0001-6215-3617) ([Global Biodiversity Information Facility](https://www.wikidata.org/wiki/Q1531570)), [Dmitry Schigel](https://orcid.org/0000-0002-2919-1168) ([Global Biodiversity Information Facility](https://www.wikidata.org/wiki/Q1531570)), [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) 

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Data Quality Dimension Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqdim/terms/2024-09-10>

Draft Standard for Submission


## 1 Introduction (non-normative)

This document includes terms intended to be used as a controlled value for BDQ Core tests with local name `Dimension`. For details and rationale, see Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731.

### 1.1 Data Quality Dimensions 

The scope of the standard is the fundamental information about core tests applied to occurrence type Darwin Core records. These tests evaluate one of Data Quality Dimension of the Fitness for Use Framework (Chapman et al., 2020): Measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved.

### 1.2 Status of the content of this document

Section 2 is normative.

In Section 4, the values of the `Term IRI`, `Definition` and `Controlled value` are normative. The values of `Term Name` and `skos:prefLabel` are non-normative. 

### 1.3 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bbqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqdim/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqdim/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqdim.xml | Example for submission, to be generated | 

## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values of `bdqffdq:dataQualityDimension`.

### 2.1 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

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


