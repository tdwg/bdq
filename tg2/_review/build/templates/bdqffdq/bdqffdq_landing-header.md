# Fitness For Use Framework Ontology

**Title**: Fitness For Use Framework Ontology

**Namespace URI**: http://rs.tdwg.org/bdqffdq

**Preferred namespace abbreviation**: bdqffdq:

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: http://www.tdwg.org/standards/[*******]

**This document version**: <{current_iri}{ratification_date}>

**Latest version of document**: http://rs.tdwg.org/bdq/doc/ffdq/

{previous_version_slot}

**Abstract**: The BDQ Conceptual Framework ontology formally describes the terms and relationships between them for evaluating the quality of biodiversity data. Due to the comprehensiveness of the conceptual framework, it allows different interpretations and manners of using it according to different stakeholders. The Framework also prodives a base for the bdq: and bdqcore: namespace vocabularies. 

{authors_contributors}

**Creator**: TDWG Biodiversity Data Quality Interest Group: Task Group 1 (Framework on Data Quality) and Task Group 2 (Data Quality Tests and Assertions)

**Bibliographic citation**: TDWG Biodiversity Data Quality Tests and Assertions Task Group Interest Group. <{current_iri}{ratification_date}>

## 1 Introduction

The bdqffdq: vocabulary is a specification of a framework for describing data quality.   Each of the tests in the bdqcore: vocabulary in this standard has been designed with this framework and is framed using the terms and concepts from the framework. The framework provides the context for each test, and has shaped decisions made about each test.

The framework considers data to have quality with respect to some specified use.   It provides a means to describe a use of data (bdqffdq:UseCase), and what is needed for some data set to have quality for that use, that is for some data set to be fit for a specified purpose.  The framework explicitly links data quality to use, and allows formal description of means to assure that data are fit for some specified purpose.

This document lists terms used to describe 'data quality' / 'fitness for use' in the context of biodiversity data.  These are based on Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>, with a few changes for increased clarity.

For more explanation, see the [Guide to the bdqffdq: framework](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqffdq_guide/index.md)

The bdqffdq: vocabulary is a Vocabulary Extension List, it includes the basic properties listed in this document, and additional axioms that can be found in its [Owl Ontology Distribution](https://github.com/tdwg/bdq/blob/master/tg2/_review/vocabulary/bdqffdq.owl)

### 1.1 Namespace abbreviations

The following namespace abbreviations are used in this document:


| **Prefix**   | **Namespace**                                    | **Note** |
|--------------|--------------------------------------------------|----------|
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                | Framework for Describing Data Quality |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms                | Tests described using the bdqffdq Framework |
| bdq          | https://rs.tdwg.org/bdq/terms/                   | Supporting Vocabulary for Data Quality |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms                 | Data Quality Dimension Vocabulary |
| bdqcrit      | https://rs.tdwg.org/bdqcrit/terms                | Data Quality Criteria Vocabulary | 
| bdqenh       | https://rs.tdwg.org/bdqenh/terms                 | Data Quality Enhancement Vocabulary | 
| dc           | https://purl.org/dc/elements/1.1/                | | 
| dcterms      | https://purl.org/dc/elements/1.1/                | |
| dwc          | http://rs.tdwg.org/dwc/terms/                    | Darwin Core |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      | |
| oa           | https://www.w3.org/TR/annotation-vocab/          | |
| skos         | http://www.w3.org/2004/02/skos/core#             | |
| owl          | http://www.w3.org/2002/07/owl#                   | |

### 1.1 Status of the content of this document

In Section 4, the values of following terms are normative: Term IRI, Name, rdfs:label, skos:prefLabel, Type, Superclass, Definition.

In Section 4, the values of the following term are non-normative: Comment.

Other sections of this document are marked as normative or non-normative.

### 1.2 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.3 Distributions (normative)

| Description | IRI | Download URL |
| ----------- | --- | ------------ |
| Human Readable Term List |  | [https://github.com/tdwg/bdq/blob/master/tg2/\_review/docs/bdqffdq/index.md](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqffdq/index.md) | 
| Owl Ontology | | [https://github.com/tdwg/bdq/blob/master/tg2/\_review/vocabulary/bdqffdq.owl](https://github.com/tdwg/bdq/blob/master/tg2/_review/vocabulary/bdqffdq.owl) |

## 2 Use of Terms (normative) 

When not represented as objects, controlled value strings MUST be used as values of bdqffdq:ResponseStatus, and bdqffdq:ResponseResult.

## 3 Term index

{term_index}

## 4 Terms in the bdqffdq ontology (portions normative, see 2.1)

TODO:  Generate and include here.

[Rough cut at generated list of ontology terms](https://github.com/tdwg/bdq/blob/master/tg2/core/generation/docs/bdqffdq.md)

