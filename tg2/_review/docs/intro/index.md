# Title: Biodiversity Data Quality (BDQ) Core Introduction

**Date version issued**: (Draft)

**Date created**: (Draft)

**Part of TDWG Standard**: 

**This version**:

**Latest version**:

**Previous version**:

**Abstract**: **Biodiversity Data Quality (BDQ)) Core** is a standard designed to facilitate the consistent development and use of a set of biodiversity data quality tests and assertions. The standard consists of vocabularies needed to define the tests, a guide to support the implementation of tests, a guide to support the interpretation of outputs of implemented tests, example data, and expected responses from tests against the example data to support the validation of implemented tests. 

**Contributors**

Lee Belbin, Arthur D. Chapman, Paul J. Morris, John R. Wieczorek, Paula Zermoglio, Alex Thompson and Yi Ming Gan.

**Creator**

TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions).

**Bibliographic citation**

BDQ Core Maintenance Group. 2024. Biodiversity Data Quality (BDQ) Core Introduction. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/bdq/doc/introduction/2024-08-21

### Table of Contents ###

```
1 Introduction
1.1 Audience
1.2 Status of the content of this document
1.3 RFC 2119 keywords
1.4 Namespace abbreviations

2. Parts of the Standard
2.1 Vocabularies
2.2 Test Guidance
2.3 Implementation Validation Data
2.4 Exemplar Implementation of Tests
2.5 Test Lists
2.6 Glossary
2.7 Bibliography

3. Acknowledgements
``` 

## 1. Introduction

Biodiversity Data Quality (BDQ) Core, hereafter referred to as 'BDQ Core', consists of 1) specifications of data quality tests that can be implemented to provide reproducible results from a given set of input data and test parameters, 2) a vocabulary of terms used in the specification of the previously mentioned tests, 3) a controlled vocabulary for the term bdq:dimension from the previously mentioned test specification terms, 4) a generic fitness for use framework whose terms and semantics are embodied in an ontology, 5) an exemplar data set to use as input for implementations of the previously mentioned tests, 6) an exemplar implementation of the tests, in Java(R), which uses the previously mentioned test data set as input and demonstrates the expected responses to each of the tests, 7) a guide to implementation of the tests are included, and 8) a guide to the interpretation of the results of the tests. 

BDQ Core covers a specification of tests for the quality of biodiversity data, not a specification of the quality to which biodiversity data are expected to conform. ‘Fitness for use’ of a biodiversity data record will greatly depend on the use to which it is applied: a record that is unsuitable to be used in one application may be suitable for another application (Belbin et al 2013). 

The BDQ tests support the determination of whether data resources will be fit for use for some particular purpose from the perspectives of the data quality dimensions `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, and `Resolution`. The tests themselves do not assert data quality, rather, sets of tests can be defined to support the assessment or assurance of data quality for a particular purpose by analyzing their responses to the input data in question against predefined expectations. This standard does not specify a structure to capture 'profiles' - component tests, order of processing, and expected results - for particular cases of fitness for use.

The BDQ tests were initially targeted specifically to [Darwin Core](https://dwc.tdwg.org/terms/) classes and properties against which they operate. This is not a limitation on the scope of the standard, but rather a choice of original scope against which to develop the tests.

### 1.1 Audience
This document is designed for anyone who needs an orientation to the BDQ Core set of standard specifications for the assessment or assurance of fitness for use of biodiversity data, or to improve it. Those interested in more detail on the interpretation of test results should consult the [BDQ Core User Guide](../users/index.md "BDQ Core Users Guide"), while those interested in the implementation of tests following the BDQ Core should consult the [BDQ Core Implementer's Guide](../implementation/index.md "BDQ Core Implementation Guide").

### 1.2. Status of the content of this document

All sections of this document are non-normative unless explicitly noted as normative.

### 1.3 RFC 2119 keywords

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.4 Namespace abbreviations

The following namespace abbreviations are used in this document:

**CHECK THIS set on final draft, include only those used in this document**

| **Prefix**   | **Namespace**                                    |
|--------------|--------------------------------------------------|
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms                |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms                 |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema             |
| owl          | http://www.w3.org/2002/07/owl#                   |

## 2. Parts of the Standard

### 2.1 Vocabularies

The focus of this standard is on a framework for describing data quality and the description of a set of tests and assertions using that framework.  The framework is instantiated formally as an ontology (namespace abbreviation bdqffdq:).  The tests are instantiated formally as a vocabulary (namespace abbreviation `bdqcore:`), with test names, labels, descriptions, expected responses and other metadata. The tests and assertions specifications make use of additional vocabularies, three of which are defined by this standard. Together the vocabularies serve to support the specification of suites of biodiversity data quality assessments and amendments to improve data for particular purposes. Each vocabulary is described in full in its distinct Term List document, linked from and summarized together on [BDQ Core Vocabularies](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/vocabularies/index.md). 

### 2.2 Test Guidance

Beyond data availability, data quality is probably the most significant issue for users of biodiversity data. The BDQ Core standard suite of tests and assertions is meant to be used by data collectors, data providers, and data users to assess and potentially improve data quality.  

The Fitness for Use Framework upon which BDQ Core is based allows pipelines of tests and assertions to have formal dependencies between them, such as a specified order in which they should be run in order to get a deterministic result, or using the results of some tests as the inputs to other tests, or building composite tests from other existing tests. By design, dependencies are manifest in some of the tests and assertions that are Measures, while tests and assertions that are Issues, Validations, and Amendments tend to be independent of each other.

Tests, even those labeled as Amendments, do not modify original data. Instead, test responses contain the information needed to amend original data by providing reproducible interpretations. These interpretations can be as a substitute for the original data or can be used to vet and amend the original data, as appropriate.

Test specifications consist of the metadata (e.g., identifier, preferred label, description, information elements acted upon, information elements consulted, expected response, data quality dimension, parameters and default behavior, notes) required to understand the test, its context, and its potential uses, and to implement it in a way that is compliant with the standard.

The specifications for expected responses from tests consist of metadata (status, result, and comment) required for a user to interpret and act upon the data (information elements) pertinent to the test that was run, whether the information elements were those consulted or those acted upon.

The [BDQ User's Guide](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/users/index.md) is intended to contain everything needed to understand the nature or the tests and the responses from them when they are run. 

The [BDQ Implementer's Guide](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/implementers/index.md) is intended to contain everything needed to understand the requirements for compliant implementations of the tests. 

[!--- JRW first pass finished to here ---]



### 2.3 Implementation Validation Data

### 2.4 Exemplar Tests Implementation

### 2.6 Test Lists

### 2.5 Test Execution Environments and Workflows

Neither the test descriptions nor the framework impose constraints on workflows for execution.  One possible workflow is to run all validations, then all amendments, then all validations again on a modified copy of the input data to which all proposed amendments have been applied.

A single validation step, with measures evaluating the results of the amendments could look like the diagram below.

![Diagram of workflow through single validation step](workflow_single_iteration.svg)

Expanding on this single validation step, amendments can be run and their results fed back into a second phase of post-amendment validation, with measures again evaluating the results of validation of the input data if all changes proposed by amendments are accepted.

![Diagram of workflow with pre-amendment validation+measure phase, followed by amendment phase, followed by post-amendment validation-measure phase](workflow_two_iterations.svg)

### 2.7 Glossary

### 2.8 Bibliography

## 3 Design of the Tests

<!--- PJM: Section 3 is Important elements to put in the introduction --->

### 3.1 Data Quality Control, Data Quality Assurance

BDQ Core draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.  Implementations of the bdqcore tests MAY be used to perform Quality Control, Quality Assurance, or both.

### 3.2 When are tests run 

The bdqcore tests are designed to be run at any point in the life cycle of biodiversity data. They MAY be run at the point of initial collection or observation of organisms. They MAY be run to support data transcription. They MAY be run in loading data into databases of records from field or transcription sources. They MAY be run in preparing data from databases of record for aggregation. They MAY be run during data aggregation and the presentation of aggregated data.  They MAY be run in workflows for analysis of data for research purposes.

### 3.3 Results of test executions 

BDQ Core is agnostic about how reports from BDQ Core can be reported.  It does, however, specify that test implementations and presentations MUST return structured data with at least bdq:Response.status, bdq:Response.result, and bdq:Response.  Responses MAY also contain more information in Response.qualifier.

The results of the execution of implementations of the bdqcore: tests MAY be presented as Data Quality reports.  The bdqffdq: framework provides vocabulary and structure that MAY be used for such data quality reports.

The bdqffdq: vocabulary enables the wrapping of the results of bdqcore: tests within annotations.  The bdqffdq: vocabularies in particular are intended to support the framing of assertions from tests within annotations that follow the W3C Web Annotation Data Model (Sanderson et al. 2017), and are suitable for inclusion in semantic data stores.

## 4. Acknowledgements

Antonio Mauro Saraiva, Allan Koch Veiga, Tim Robertson, Ian Engelbrecht, GBIF, IDigBio, ALA, CRIA, TDWG...

<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">

<head>

<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 15">
<link id=Main-File rel=Main-File
href="file:///C:/Users/LEEBEL~1/AppData/Local/Temp/msohtmlclip1/01/clip.htm">
<link rel=File-List
href="file:///C:/Users/LEEBEL~1/AppData/Local/Temp/msohtmlclip1/01/clip_filelist.xml">
<!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
x\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]-->
<style>
<!--table
	{mso-displayed-decimal-separator:"\.";
	mso-displayed-thousand-separator:"\,";}
@page
	{margin:.75in .7in .75in .7in;
	mso-header-margin:.51in;
	mso-footer-margin:.51in;}
.font5
	{color:black;
	font-size:9.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Tahoma, sans-serif;
	mso-font-charset:1;}
.font6
	{color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;}
tr
	{mso-height-source:auto;}
col
	{mso-width-source:auto;}
br
	{mso-data-placement:same-cell;}
td
	{padding:0px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri;
	mso-generic-font-family:auto;
	mso-font-charset:1;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;
	mso-protection:locked visible;
	white-space:nowrap;
	mso-rotate:0;}
.xl66
	{color:windowtext;
	font-family:Calibri, sans-serif;
	mso-font-charset:1;}
.xl67
	{color:windowtext;
	font-family:Calibri, sans-serif;
	mso-font-charset:1;}
-->
</style>
</head>

<body link="#0563C1" vlink="#954F72">
</body>
</html>
