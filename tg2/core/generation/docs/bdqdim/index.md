# Data Quality Dimension Controlled Vocabulary List of Terms

**Title**: Data Quality Dimension Controlled Vocabulary List of Terms

**Namespace URI**: <http://rs.tdwg.org/bdqdim/values/>

**Preferred namespace abbreviation**: bdqdim:

**Date version issued**: 2024-09-10

**Date created**: 2024-09-10

**Part of TDWG Standard**: <http://www.tdwg.org/standards/[*******]>

**This document version**: <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

**Latest version of document**: <http://rs.tdwg.org/bdq/doc/dim/>

**Abstract**: The BDQ Core term `Dimension` describes the aspect of data quality (accuracy, precision, completeness, etc.) that a test examines. For example, "precision" in "coordinate precision of single records". Includes Completeness, Conformance, Consistency, Likeliness, Reliability, and Resolution. 

**Contributors**: Lee Belbin, Paul Morris, Arthur Chapman, John Wieczorek, Alan Koch Veiga, Paula F Zermoglio, Alex Thompson, Anytonio M Saraiva, Yi Ming Gan

**Creator**: TDWG Biodiversity Data Quality Interest Group: Task Group 1 (Framework on Data Quality) and Task Group 2 (Data Quality Tests and Assertions)

**Bibliographic citation**: TDWG Biodiversity Data Quality Interest Group. 2024. BDQ Dimensions Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqcore/terms/2024-09-10>


## 1 Introduction
[!--- JRW finished first draft to here ---]
This document includes terms intended to be used as a controlled value for BDQ Core tests with local name `Dimension`. For details and rationale, see Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>

#### Data Quality Dimensions 

The scope of the standard is the fundamental information about core tests applied to occurrence type Darwin Core records. These tests evaluate one of Data Quality Dimension of the Fitness for Use Framework (Chapman et al., 2020): Measurable attributes in an Information Element which can be individually assessed, interpreted, and potentially improved. These dimensions are:

* Completeness: The extent to which data are present and sufficiently comprehensive for use.
* Conformance: Conforms to a format, syntax, data type, range, or standard of the Information Element.
* Consistency: Agreement among related Information Elements (q.v.) that are present in the data. Note that missing Information Elements do not make a test Inconsistent.
* Likeliness: The likelihood of Darwin Core Term(s) having true or expected values.
* Reliability: Measure of how the data values agree with an identified source of truth. The degree to which data correctly describes the truth (object, event or any abstract or real 'thing').
* Resolution: Refers to the data having sufficiently detailed information. Measure of the granularity of the data, or the smallest measurable increment.


A "Warning Type" for each test was originally envisioned to provide insight into the nature of the issues, but a review the relationship with "Data Quality Dimension" across the tests suggested such a high degree of correlation that "Warning Type" is effectively redundant. See table xx below. **NEEDS UPDATING**

| Data Quality Dimension/Warning Type | Ambiguous | Amended | Incomplete | Inconsistent | Invalid | Issue | Report | Unlikely | Total |
|-------------------------------------|-----------|---------|------------|--------------|---------|-------|--------|----------|-------|
| Completeness                        |           |   11    |    19      |              |         |   1   |    2   |          |  33   |
| Conformance                         |     2     |   13    |            |       3      |    35   |       |        |          |  53   |
| Consistency                         |           |    1    |            |       5      |         |       |        |          |   6   |
| Likeliness                          |           |         |            |              |         |       |        |     2    |   2   |
| Reliability                         |           |         |            |              |         |   1   |    2   |          |   3   |
| Resolution                          |           |         |            |              |         |   1   |    1   |          |   2   |
| Total                               |     2     |   25    |    19      |       8      |    35   |   3   |    5   |     2    |  99   |

Caption: Data Quality Dimension vs Warning Type with the number of tests as cell values. 

### 1.1 Status of the content of this document

In Section 4, the values of the `Term IRI`, `Definition` and `Controlled value` are normative. The values of `Term Name` and `skos:prefLabel` are non-normative. 

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 2 Use of Terms

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), controlled value strings MUST be used as values of `bdqffdq:dataQualityDimension`.

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

[Completeness](#Completeness) |
[Conformance](#Conformance) |
[Consistency](#Consistency) |
[Likeliness](#Likeliness) |
[Reliability](#Reliability) |
[Resolution](#Resolution) 

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
			<td><a href="http://rs.tdwg.org/bdq/bdqdim/terms/Completeness">http://rs.tdwg.org/bdq/bdqdim/terms/Completeness</a></td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document (Link needed to RDF document  - https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
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
			<td><a href="http://rs.tdwg.org/bdq/bdqdim/terms/Conformance">http://rs.tdwg.org/bdq/bdqdim/terms/Conformance</a></td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document (Link needed to RDF document  - https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
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
			<td><a href="http://rs.tdwg.org/bdq/bdqdim/terms/Consistency">http://rs.tdwg.org/bdq/bdqdim/terms/Consistency</a></td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document (Link needed to RDF document  - https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
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
			<td><a href="http://rs.tdwg.org/bdq/bdqdim/terms/Likeliness">http://rs.tdwg.org/bdq/bdqdim/terms/Likeliness</a></td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document (Link needed to RDF document  - https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
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
			<td><a href="http://rs.tdwg.org/bdq/bdqdim/terms/Reliability">http://rs.tdwg.org/bdq/bdqdim/terms/Reliability</a></td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document (Link needed to RDF document  - https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
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
			<td><a href="http://rs.tdwg.org/bdq/bdqdim/terms/Resolution">http://rs.tdwg.org/bdq/bdqdim/terms/Resolution</a></td>
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
			<td>Definition from the Fitness for Use Framework: Data Quality Dimensions Document (Link needed to RDF document  - https://github.com/tdwg/bdq/wiki/TG2-Data-Quality-Dimension).</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>bdqffdq:DataQualityDimension</td>
		</tr>
	</tbody>
</table>


