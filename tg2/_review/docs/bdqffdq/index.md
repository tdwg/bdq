<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Fitness For Use Framework Ontology

**Title**<br>
Fitness For Use Framework Ontology

**Date version issued**<br>
2025-05-10

**Date created**<br>
2025-05-10

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**Preferred namespace abbreviation**<br>
bdqffdq

**This version**<br>
<http://rs.tdwg.org/bdqffdq/2025-05-10>

**Latest version**<br>
<http://rs.tdwg.org/bdqffdq/>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
This document is a reference for the BDQ standard, linking to the Fitness For Use Framework ontology documents that cover its uses, its vocabulary, and its vocabulary extension.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/2025-05-10>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
    - [1.3.1 Distributions (non-normative)](#131-distributions-non-normative)
  - [1.4 Namespace abbreviations (non-normative)](#14-namespace-abbreviations-non-normative)
  - [1.5 Status of the Content of this Document (normative)](#15-status-of-the-content-of-this-document-normative)
  - [1.6 RFC 2119 key words (normative)](#16-rfc-2119-key-words-normative)
  - [1.7 Referring to Terms (normative)](#17-referring-to-terms-normative)

[Acronyms (non-normative)](#acronyms-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to serve as the landing page for the `bdqffdq:` vocabulary within the BDQ standard. It provides navigation to the primary resources for the Fitness For Use Framework, including the human-readable guide, the term list, the vocabulary extension, and the OWL ontology distribution.

### 1.2 Audience (non-normative)

This document is intended for technical users who need to understand or reference the BDQ Fittnes For Use Framework Ontology. 

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../index.md).

Information about the Fitness For Use Framework Ontology, its usage, and its extensions can be found in the following subset of BDQ resources:

- **Fitness For Use Framework Ontology** - Landing page for the `bdqffdq:` vocabulary *(this document)*.
- [**Fitness For Use Framework Ontology: Concepts and Use**](../guide/bdqffdq/index.md) - Provides normative guidance along with visual and narrative introduction to the concepts and application of the ontology.
- [**Fitness For Use Framework Ontology List of Terms**](../list/bdqffdq/index.md) - The term list document, which enumerates and describes the vocabulary terms.
- [**Fitness For Use Framework Ontology Vocabulary Extension**](../extension/bdqffdq/index.md) - Defines additional axioms extending the core vocabulary.

#### 1.3.1 Distributions (non-normative)

| Description | IRI | Download URL | Notes | 
| ----------- | --- | -----------  | ----- | 
| OWL ontology | TBD | [Biodiversity Data Quality Fitness For Use Framework (Ontology)](../../vocabulary/bdqffdq.owl) | The formal RDF/OWL representation of the vocabulary. |

### 1.4 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this and related documents:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdqval:      | https://rs.tdwg.org/bdqval/terms/           |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqenh:      | https://rs.tdwg.org/bdqenh/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| oa:          | http://www.w3.org/ns/oa#                    |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

### 1.5 Status of the Content of this Document (normative)

Sections may be either normative (defines what is required to comply with the standard) or non-normative (supports understanding but is not binding) and are marked as such. 

Any sentence or phrase beginning with "For example" or "e.g.", whether in a normative section or a non-normative section, is non-normative.

### 1.6 RFC 2119 key words (normative)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.7 Referring to Terms (normative)

In any technical treatment of the BDQ standard, a precise reference to a class or property term SHOULD be made using its qualified name (the namespace prefix followed by the term local name; e.g., `bdqffdq:InformationElement`) and the namespace IRI corresponding to the namespace prefix (e.g., `https://rs.tdwg.org/bdqffdq/terms/` for `bdqffdq:`) MUST be provided. In less formal descriptions where the technical precision is not needed, the preferred label (`skos:prefLabel`, e.g., `Information Element`) or the term local name (e.g., `InformationElement`) MAY be used. The BDQ documents use all these methods.

## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../index.md#61-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [General Glossary (non-normative)](../../index.md#63-general-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## References (non-normative)

The references for the BDQ standard can be found in the [References (non-normative)](../../index.md#7-references-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. Fitness For Use Framework Ontology. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqffdq/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
