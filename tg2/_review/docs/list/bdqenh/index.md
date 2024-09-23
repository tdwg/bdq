<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
# Data Quality Enhancement Controlled Vocabulary List of Terms

Title
: Data Quality Enhancement Controlled Vocabulary List of Terms

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Preferred namespace abbreviation
: bdqenh

This version
: <http://rs.tdwg.org/bdq/bdqenh/terms/2024-09-10>

Latest version
: <http://rs.tdwg.org/bdq/bdqenh/terms/>

Abstract
: This document is a reference for the (Draft) BDQ Core Standard, documenting vocabulary values for the BDQ Core term Enhancement.

Contributors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028)), [Yi-Ming Gan](https://orcid.org/0000-0001-7087-2646) ([Royal Belgian Institute of Natural Sciences](http://www.wikidata.org/entity/Q16665660)), [Antonio Mauro Saraiva](https://orcid.org/0000-0003-2283-1123) ([University of São Paulo, Research Center on Biodiversity and Computing](https://www.wikidata.org/wiki/Q835960)), [Alan Koch Veiga](http://orcid.org/0000-0003-2672-8115) , [Paula F Zermoglio](https://orcid.org/0000-0002-6056-5084) ([Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN): San Carlos de Bariloche](https://www.irnad.com/)), [Alexander Thompson](https://orcid.org/0000-0002-8981-4048) ([Google](https://www.wikidata.org/wiki/Q95)), David Lowery 

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Data Quality Enhancement Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqenh/terms/2024-09-10>

Draft Standard for Submission

## 1 Introduction
This document includes terms intended to be used as a controlled value for BDQ Core tests with local name `Enhancement`.  For details and rationale, see Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>

### 1.1 Data Quality Criteria

The scope of the standard is the fundamental information about core tests of type bdqffdq:Amendment. The Enhancement describes, in abstract terms, how proposals can modify data to improve fitness.  An enhancement expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Enhancements have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

### 1.2 Data Quality Criteria Vocabulary

<!-- Generated table of terms goes here --->

[CSV File of list of terms to generate content for this section](../../vocabulary/bdqenh_terms.csv "File from which to generate this section")

| term_localName |definition | comments | 
| ------------------ |----------- | ------------- | 
| AssumedDefault |Data could be improved by setting an empty value to a default value | Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in with a default value.  Corresponding dimension is bdqdim:Completeness | 
| Converted |Data could be improved by converting from one representation to another | As in spatial coordinate transformations.  Data in a bdqffdq:InformationElement that do not conform to some specification may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance | 
| FillInFrom |Data could be improved by using one data value to fill in the empty value in another | As in filling in from verbatim terms.  Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in by interpretation of values in one or more other terms.  Corresponding dimension is bdqdim:Completeness. | 
| Standardized |Data could be improved by conforming them to a standard representation. | Data in a bdqffdq:InformationElement that do not conform to some format, syntax, data type, or standard may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance | 
| Transposed |Data could be improved by switching values between two or more fields. | Data in a set of at least two bdqffdq:InformationElements that do not conform to expectations may be proposed to have their values switched in order to produce conforming values.  Corresponding dimension is bdqdim:Consistency. | 


<!-- End generated table of terms --->

## 1.3 Use of Terms

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), controlled values from this vocabulary are REQUIRED values of `bdqffdq:Enhancement`.

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdq/bdqenh/terms/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/list/bdqenh/index.md | This file | 
| RDF/XML file | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/dist/bdqenh.xml | Example for submission, to be generated | 

### 2 Status of the content of this document

In Section 1.2 the values of the `Term IRI`, `Definition` and `Controlled value` are normative. The values of `Term Name`, 'Comments' and `skos:prefLabel` are non-normative. 

### 2.1 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 3.1 Index By Term Name

(See also [3.2 Index By Label](#32-index-by-label))

**Classes**

**Vocabulary**

[bdqenh:AssumedDefault](#bdqenh_AssumedDefault) |
[bdqenh:Converted](#bdqenh_Converted) |
[bdqenh:FillInFrom](#bdqenh_FillInFrom) |
[bdqenh:Standardized](#bdqenh_Standardized) |
[bdqenh:Transposed](#bdqenh_Transposed) 

### 3.2 Index By Label

(See also [3.1 Index By Term Name](#31-index-by-term-name))

**Classes**

[Assumed Default](#bdqenh_AssumedDefault) |
[Converted](#bdqenh_Converted) |
[Fill In From](#bdqenh_FillInFrom) |
[Standardized](#bdqenh_Standardized) |
[Transposed](#bdqenh_Transposed) 

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_AssumedDefault"></a>Term Name  bdqenh:AssumedDefault</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/AssumedDefault">https://rs.tdwg.org/bdqenh/terms/AssumedDefault</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/AssumedDefault-2024-09-30">https://rs.tdwg.org/bdqenh/terms/AssumedDefault-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Assumed Default</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by setting an empty value to a default value</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in with a default value.  Corresponding dimension is bdqdim:Completeness</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>AssumedDefault</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_Converted"></a>Term Name  bdqenh:Converted</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Converted">https://rs.tdwg.org/bdqenh/terms/Converted</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Converted-2024-09-30">https://rs.tdwg.org/bdqenh/terms/Converted-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Converted</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by converting from one representation to another</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>As in spatial coordinate transformations.  Data in a bdqffdq:InformationElement that do not conform to some specification may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Converted</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_FillInFrom"></a>Term Name  bdqenh:FillInFrom</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/FillInFrom">https://rs.tdwg.org/bdqenh/terms/FillInFrom</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/FillInFrom-2024-09-30">https://rs.tdwg.org/bdqenh/terms/FillInFrom-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fill In From</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by using one data value to fill in the empty value in another</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>As in filling in from verbatim terms.  Data in a bdqffdq:InformationElement are absent and may be proposed to be filled in by interpretation of values in one or more other terms.  Corresponding dimension is bdqdim:Completeness.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>FillInFrom</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_Standardized"></a>Term Name  bdqenh:Standardized</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Standardized">https://rs.tdwg.org/bdqenh/terms/Standardized</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Standardized-2024-09-30">https://rs.tdwg.org/bdqenh/terms/Standardized-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by conforming them to a standard representation.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a bdqffdq:InformationElement that do not conform to some format, syntax, data type, or standard may be proposed to be replaced in with a conforming value.  Corresponding dimension is bdqdim:Conformance</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Standardized</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="bdqenh_Transposed"></a>Term Name  bdqenh:Transposed</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Transposed">https://rs.tdwg.org/bdqenh/terms/Transposed</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2024-09-30</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="https://rs.tdwg.org/bdqenh/terms/Transposed-2024-09-30">https://rs.tdwg.org/bdqenh/terms/Transposed-2024-09-30</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Transposed</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Data could be improved by switching values between two or more fields.</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td>Data in a set of at least two bdqffdq:InformationElements that do not conform to expectations may be proposed to have their values switched in order to produce conforming values.  Corresponding dimension is bdqdim:Consistency.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Transposed</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:Enhancement</td>
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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Data Quality Enhancement Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdq/bdqenh/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


