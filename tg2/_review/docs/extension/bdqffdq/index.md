<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
# Fitness For Use Framework Ontology Vocabulary Extension

Title
: Fitness For Use Framework Ontology Vocabulary Extension

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Preferred namespace abbreviation
: RUN_HAS_RESULT

This version
: <http://rs.tdwg.org/bdqffdq/extension/2024-09-10>

Latest version
: <http://rs.tdwg.org/bdqffdq/extension/>

{previous_version_slot}

Abstract
: This document is a reference for the (Draft) BDQ Core Standard, documenting additional axioms that extend the basic vocabulary of the Fittness For Use Framework Ontology.

Authors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028))

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/extension/2024-09-10>

Draft Standard for Submission

### Table of Contents ###

- [ 1 Introduction (non-normative)](#1-introduction-(non-normative))
- [ 1.1 Fittness for Use Framework Vocabulary terms.](#11-fittness-for-use-framework-vocabulary-terms)
- [ 1.2 Status of the content of this document](#12-status-of-the-content-of-this-document)
- [ 1.3 Namespace abbreviations](#13-namespace-abbreviations)
- [ 1.4 Term List Distributions](#14-term-list-distributions)
- [ 1.5 Key to Vocabulary Terms](#15-key-to-vocabulary-terms)
- [ 2 Use of Terms (normative)](#2-use-of-terms-(normative))
- [ 2.1 RFC 2119 key words (normative)](#21-rfc-2119-key-words-(normative))
- [ 3 Term index (non-normative)](#3-term-index-(non-normative))


## 1 Introduction (non-normative)

This document includes terms that extend the basic bdqffdq vocabulary and are integral to bdqffdq as an ontology..

### 1.1 Fittness for Use Framework Vocabulary terms.

The bdqffdq framework is represented as an owl ontology.  The basic terms for that framework are in the
[basic bdqffdq vocabulary](../../list/bdqffdq/index.md).  The TDWG Standards Documentation Specification requires
that the human readable documentation for ontologies be presented as a term list with additional axioms included
in a vocabulary extension.  This file documents the additional axioms in isolation.  

See the [landing page for bdqffdq:](../../bdqffdq/index.md) for normative guidance on the bdqffdq: framework 
ontology, and the [guide to bdqffdq:](../../guide/bdqffdq/index.md) page for a guide to the ontology.

The bdqffdq ontology includes few restrictions, this is by design.  Domain and range restrictions do not limit
what is in the domain or range of a property, but add assertions about the types of objects that are the subjects
or objects of predicates bearing the restrictions.  Some types of restrictions limit which owl profiles are
available to tools that reason on the ontology and on data stores that include the ontology.

### 1.2 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

Section 1.5 lists which values in Section 4 are normative and which are non-normative.

### 1.3 Namespace abbreviations

The following namespace abbreviations are used in this document:

| Prefix | IRI |
| --- | --- |
| bdq:     | https://rs.tdwg.org/bdq/terms/   |
| bdqdim:  | https://rs.tdwg.org/bdqdim/terms |
| bbqffdq: | http://rs.tdwg.org/bdq/bdqffdq/  |
| bbdcore: | http://rs.tdwg.org/bdq/bdqcore/  |

### 1.4 Term List Distributions

| Description | IRI | Download URL | Note | 
| ----------- | --- | -----------  | ---- | 
| HTML file   | http://rs.tdwg.org/bdqffdq/extension/ | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/docs/extension/RUN_HAS_RESULT/index.md | This file | 
| Owl Ontology | TBD | https://raw.githubusercontent.com/tdwg/bdq/master/tg2/\_review/vocabulary/bdqffdq.owl | Turtle Serialization of the full ontology, including additional axioms | 

### 1.5 Key to Vocabulary Terms

| Label | Term | Definition | Example | Normative | 
| ----- | ---- | ---------- | ------- | --------- |
| Term Version IRI | rdf:about |  | https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement | normative |
| Term IRI | dcterms:isVersionOf |  | https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement | normative |
| Term Name | rdf:value |  | https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement | normative |
| Preferred Label | skos:prefLabel | The preferred lexical label for a resource, in a given language. | Abstract Information Element | non-normative |
| Label | rdfs:label |  | Abstract Information Element | normative |
| Comments | rdfs:comment |  | Information elements such as DATE and DAY are abstract, they could reference any representation of those concepts.  In contrast, dwc:eventDate and dwc:day can be linked to concrete Acted Upon or Consulted information elements. | non-normative |
| Definition | skos:definition | A statement or formal explanation of the meaning of a concept. | An InformationElement described in abstract terms and not linked with one or more concrete terms. | normative |
| Type | rdf:type |  | http://www.w3.org/2002/07/owl#Class | normative |
| Superclass | rdfs:subClassOf |  | https://rs.tdwg.org/bdqffdq/terms/InformationElement | normative |


## 2 Use of Terms (normative)

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), resources MUST be used as values from the `bdq:` namespace, except for bdq:empty and bdq:notEmpty, where controlled value strings MUST be used.

### 2.1 RFC 2119 key words (normative)
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

## 3 Term index (non-normative)

TODO: SPARQL Query for additional axioms, output as table

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

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Fitness For Use Framework Ontology Vocabulary Extension. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/extension/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


