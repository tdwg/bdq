<!--- Template for header, values provided from yaml configuration --->
# {document_title}

**Title**<br>
{document_title}

**Date version issued**<br>
{ratification_date}

**Date created**<br>
{created_date}

**Part of TDWG Standard**<br>
<{standard_iri}>

**Preferred namespace abbreviation**<br>
{pref_namespace_prefix}

**This version**<br>
<{current_iri}{ratification_date}>

**Latest version**<br>
<{current_iri}>

**Previous version**<br>
{previous_version_slot}

**Abstract**<br>
{abstract}

**Authors**<br>
{authors}

**Creator**<br>
{creator}

**Bibliographic citation**<br>
{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

**Status**<br>
{comment}

{toc}

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

The purpose of this document is to facilitate naviation among the various documents related to the Biodiversity Data Quality Fitness for Use Framework (the "Framework"), and to provide an introduction to the formal ontology that underpins the BDQ standard. It serves as a landing page for the `bdqffdq:` vocabulary, which defines the core concepts and relationships used to represent data quality information in the context of biodiversity data, and points to the associated documents that provide normative guidance about the ontology, its terms, and its application.


### 1.2 Audience (non-normative)

This document is intended for technical users who need to interact directly with the BDQ ontology. 

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../index.md) page.

Information about the Fitness for Use ontology, its usage, and its extensions can be found in the following subset of BDQ resources:

- **Fitness For Use Framework Ontology** - Landing page for the bdqffdq: vocabulary. This document.
- [**Fitness For Use Framework Ontology: Concepts and Use**](../guide/bdqffdq/index.md) - Provides normative guidance along with visual and narrative introduction to the concepts and application of the ontology.
- [**Fitness For Use Framework Ontology List of Terms**](../list/bdqffdq/index.md) - The term list document, which enumerates and describes the vocabulary terms.
- [**Fitness For Use Framework Ontology Vocabulary Extension**](../extension/bdqffdq/index.md) - Defines additional axioms extending the core vocabulary.

#### 1.3.1 Distributions (non-normative)

| Description | IRI | Download URL | Notes | 
| ----------- | --- | -----------  | ----- | 
| Owl ontology | TBD | [Biodiversity Data Quality Fitness For Use Framework (Ontology)](../../vocabulary/bdqffdq.owl) | The formal RDF/OWL representation of the vocabulary. |

### 1.4 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
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

