<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

# Tutorial: Creating a New Test using the BDQ Standard

**Title**<br>
Tutorial: Creating a New Test using the BDQ Standard

**Date version issued**<br>
2026-03-20

**Date created**<br>
2026-03-20

**Part of TDWG Standard**<br>
<http://example.org/to_be_determined>

**This version**<br>
<https://bdq.tdwg.org/to_be_determined2026-03-20>

**Latest version**<br>
<https://bdq.tdwg.org/to_be_determined>

**Previous version**<br>

**Abstract**<br>
This document provides information supplementary to the BDQ standard, describing the thought process and procedure for describing a new Test.

**Authors**<br>
[Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur D. Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) (Rauthiflor LLC)

**Creator**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

**Bibliographic citation**<br>
TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2026. Tutorial: Creating a New Test using the BDQ Standard. Biodiversity Information Standards (TDWG). <https://bdq.tdwg.org/to_be_determined2026-03-20>

**Status**<br>
Draft Standard for Review

## Table of Contents ##
[1 Introduction (non-normative)](#1-introduction-non-normative)
  - [1.1 Purpose (non-normative)](#11-purpose-non-normative)
  - [1.2 Audience (non-normative)](#12-audience-non-normative)
  - [1.3 Associated Documents (non-normative)](#13-associated-documents-non-normative)
  - [1.4 Status of the Content of this Document (normative)](#14-status-of-the-content-of-this-document-normative)
  - [1.5 Namespace abbreviations (non-normative)](#15-namespace-abbreviations-non-normative)

[2 Overview (non-normative)](#2-overview-non-normative)
  - [2.1 Best Practices (non-normative)](#21-best-practices-non-normative)

[3 Defining a Use Case (non-normative)](#3-defining-a-use-case-non-normative)
  - [3.1 Define the Use Case and Fitness-for-Use Requirements (non-normative)](#31-define-the-use-case-and-fitness-for-use-requirements-non-normative)
    - [3.1.1 Refine and Formalize the Use Case (non-normative)](#311-refine-and-formalize-the-use-case-non-normative)
  - [3.2 Identify the Information Elements (non-normative)](#32-identify-the-information-elements-non-normative)
  - [3.3 Reuse of Existing Tests and Gap Analysis (non-normative)](#33-reuse-of-existing-tests-and-gap-analysis-non-normative)

[4 Defining a New Test (non-normative)](#4-defining-a-new-test-non-normative)
  - [4.1 A Simple Description of the Test (non-normative)](#41-a-simple-description-of-the-test-non-normative)
  - [4.2 Identify the Information Elements (non-normative)](#42-identify-the-information-elements-non-normative)
  - [4.3 Select the Test Type (non-normative)](#43-select-the-test-type-non-normative)
  - [4.4 Name the Test (non-normative)](#44-name-the-test-non-normative)
    - [4.4.1 Anatomy of a Test Label (non-normative)](#441-anatomy-of-a-test-label-non-normative)
    - [4.4.2 Identifiers supporting software and developers (non-normative)](#442-identifiers-supporting-software-and-developers-non-normative)
  - [4.5 Identify the Data Quality Dimension and Criterion (non-normative)](#45-identify-the-data-quality-dimension-and-criterion-non-normative)
  - [4.6 How many records are we examining at once? (non-normative)](#46-how-many-records-are-we-examining-at-once-non-normative)
  - [4.7 Define the Test Specification (non-normative)](#47-define-the-test-specification-non-normative)
    - [4.7.1 What Isn't Said in the Test Specification (non-normative)](#471-what-isnt-said-in-the-test-specification-non-normative)
  - [4.8 Source Authority? (non-normative)](#48-source-authority-non-normative)
  - [4.9 Generalize the Test? (non-normative)](#49-generalize-the-test-non-normative)
  - [4.10 List the properties of the Test (non-normative)](#410-list-the-properties-of-the-test-non-normative)
    - [4.10.1 Formal RDF Representation of the Test (non-normative)](#4101-formal-rdf-representation-of-the-test-non-normative)
    - [4.10.2 Summary of the Test Definition (non-normative)](#4102-summary-of-the-test-definition-non-normative)

[5 A Test to Fill another Gap (non-normative)](#5-a-test-to-fill-another-gap-non-normative)

[6 Defining a more complicated Test with a Source Authority (non-normative)](#6-defining-a-more-complicated-test-with-a-source-authority-non-normative)
  - [6.1 A Simple Description of the Test (non-normative)](#61-a-simple-description-of-the-test-non-normative)
  - [6.2 Identify the Information Elements (non-normative)](#62-identify-the-information-elements-non-normative)
  - [6.3 Select the Test Type (non-normative)](#63-select-the-test-type-non-normative)
  - [6.4 Name the Test (non-normative)](#64-name-the-test-non-normative)
  - [6.5 Identify the Data Quality Dimension and Criterion (non-normative)](#65-identify-the-data-quality-dimension-and-criterion-non-normative)
  - [6.6 How many records are we examining at once? (non-normative)](#66-how-many-records-are-we-examining-at-once-non-normative)
  - [6.7 Define the Test Specification (non-normative)](#67-define-the-test-specification-non-normative)
    - [6.7.1 Source Authority (non-normative)](#671-source-authority-non-normative)
    - [6.7.2 Generalize, add a parameter (non-normative)](#672-generalize-add-a-parameter-non-normative)
    - [6.7.3  Revisiting the Test Specification (non-normative)](#673--revisiting-the-test-specification-non-normative)
    - [6.7.4 Clarifying Related Concepts (non-normative)](#674-clarifying-related-concepts-non-normative)
  - [6.8 Notes (non-normative)](#68-notes-non-normative)
    - [6.8.1 Example Complex Implementation Notes (non-normative)](#681-example-complex-implementation-notes-non-normative)
  - [6.9 List the properties of the Test (non-normative)](#69-list-the-properties-of-the-test-non-normative)
    - [6.9.1 Summary of the Test Definition (non-normative)](#691-summary-of-the-test-definition-non-normative)
    - [6.9.2 Iterate (non-normative)](#692-iterate-non-normative)

[7 Implementation, Conformance Testing, and Community Feedback (The "real-world") (non-normative)](#7-implementation-conformance-testing-and-community-feedback-the-real-world-non-normative)
  - [7.1 Implementation (non-normative)](#71-implementation-non-normative)
  - [7.2 Conformance Testing Data and exposing Assumptions (non-normative)](#72-conformance-testing-data-and-exposing-assumptions-non-normative)
    - [7.2.1 Unit Tests (non-normative)](#721-unit-tests-non-normative)
    - [7.2.2 Data for Conformance Testing and Edge Cases (non-normative)](#722-data-for-conformance-testing-and-edge-cases-non-normative)
      - [7.2.2.1 Example Conformance Testing Data (non-normative)](#7221-example-conformance-testing-data-non-normative)
      - [7.2.2.2 Conformance testing data for our proposed VALIDATION_WASATTRIBUTEDTO_STANDARD Test (non-normative)](#7222-conformance-testing-data-for-our-proposed-validation_wasattributedto_standard-test-non-normative)
      - [7.2.2.3 Enumerating Test Conformance Data (non-normative)](#7223-enumerating-test-conformance-data-non-normative)
  - [7.4 Execution Frameworks (non-normative)](#74-execution-frameworks-non-normative)
    - [7.4.1 What an execution framework must do between raw data and a Test implementation (non-normative)](#741-what-an-execution-framework-must-do-between-raw-data-and-a-test-implementation-non-normative)

[8 Use an implementation for Quality Control (non-normative)](#8-use-an-implementation-for-quality-control-non-normative)
  - [8.1 MultiRecord Measures for Quality Control (non-normative)](#81-multirecord-measures-for-quality-control-non-normative)
    - [8.1.1 What a MultiRecord Measure takes as input (non-normative)](#811-what-a-multirecord-measure-takes-as-input-non-normative)
    - [8.1.2 Two common patterns of MultiRecord Measures (non-normative)](#812-two-common-patterns-of-multirecord-measures-non-normative)
    - [8.1.3 Interpreting MultiRecord measures under Quality Control (non-normative)](#813-interpreting-multirecord-measures-under-quality-control-non-normative)
    - [8.1.3.1 Contrast with Quality Assurance (non-normative)](#8131-contrast-with-quality-assurance-non-normative)
    - [8.1.4 A worked example (building on VALIDATION_FOOTPRINTWKT_NOTEMPTY) (non-normative)](#814-a-worked-example-building-on-validation_footprintwkt_notempty-non-normative)
    - [8.1.5 Practical note: summary values vs. details (non-normative)](#815-practical-note-summary-values-vs-details-non-normative)
    - [8.1.6 Example Quality Control Measures for the Validated Distribution Authority Use Case (non-normative)](#816-example-quality-control-measures-for-the-validated-distribution-authority-use-case-non-normative)
  - [8.2 Quality Control Workflow (non-normative)](#82-quality-control-workflow-non-normative)
    - [8.2.1 Start with Patterns, Not Individual Records (non-normative)](#821-start-with-patterns-not-individual-records-non-normative)
    - [8.2.2 Look for Point Causes and Systemic Errors (non-normative)](#822-look-for-point-causes-and-systemic-errors-non-normative)
    - [8.2.3 Focus on Results (non-normative)](#823-focus-on-results-non-normative)
    - [8.2.4 Prioritize Work for Greatest Impact (non-normative)](#824-prioritize-work-for-greatest-impact-non-normative)
    - [8.2.5 Close the loop: re-run Tests to confirm improvements (non-normative)](#825-close-the-loop-re-run-tests-to-confirm-improvements-non-normative)
    - [8.2.6 Example Quality Control Workflow Validated Distribution Authority Use Case (non-normative)](#826-example-quality-control-workflow-validated-distribution-authority-use-case-non-normative)
  - [8.3 Quality Assurance Workflow (non-normative)](#83-quality-assurance-workflow-non-normative)

[9 Round-Up (non-normative)](#9-round-up-non-normative)
  - [9.1 Summary of the BDQ Philosophy (non-normative)](#91-summary-of-the-bdq-philosophy-non-normative)

[Glossary (non-normative)](#glossary-non-normative)

[References (non-normative)](#references-non-normative)

[Cite BDQ (non-normative)](#cite-bdq-non-normative)

## 1 Introduction (non-normative)

### 1.1 Purpose (non-normative)

This document provides, in the form of a tutorial, an overview of the concepts, reasoning, technical justifications, and logical choices behind the creation of a new Biodiversity Data Quality (BDQ) Test.  It can be used to understand the components of the BDQ standard and to guide users and implementers in describing new Tests using the BDQ Fitness For Use Framework.  It is also intended to assist the proposed BDQ Maintenance Group in evaluating proposals for new Tests and edits to existing Tests.

### 1.2 Audience (non-normative)

This document is intended for users and implementers seeking to understand the components of the BDQ standard through examining the reasoning and technical justifications behind the creation of a new BDQ Test. 

This document is also intended for those interested in describing new Tests using the BDQ Fitness For Use Framework.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../index.md).

### 1.4 Status of the Content of this Document (normative)

All sections of this document except this one are non-normative.

### 1.5 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdqval:         | https://rs.tdwg.org/bdqval/terms/           |
| bdqtest:     | https://rs.tdwg.org/bdqtest/terms/          |
| bdqcrit:     | https://rs.tdwg.org/bdqcrit/terms/          |
| bdqdim:      | https://rs.tdwg.org/bdqdim/terms/           |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| dcterms:     | http://purl.org/dc/terms/                   |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |
| owl:         | http://www.w3.org/2002/07/owl#              |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| prov:        | http://www.w3.org/ns/prov#                  |
| foaf:        | http://xmlns.com/foaf/0.1/                 |
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

## 2 Overview (non-normative)

This tutorial works through the development of a `Use Case`, then walks through two examples of the development of Tests.  One of the examples of a [Test](<../../index.md#glossary_Test> "A composition of a `bdqffdq:DataQualityNeed` with a `bdqffdq:DataQualityMethod` that links it to an instance of a `bdqffdq:Specification`, these instances being composed of `InformationElements`, `Arguments`, and `Param…") is simple, the other is more complex.  This tutorial then comes back to the `Use Case` and describes how Measure Tests can be developed to evaluate the results of the Validation Tests for the purpose of `Quality Control`.  

The simpler of the two Tests examined is VALIDATION_FOOTPRINTWKT_NOTEMPTY, which was considered a [Supplementary Test](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md) rather than a BDQ "Core" Test as we considered it of marginal use for the BDQ `Use Cases`. As noted in the [BDQ Supplement Information](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md), the Test could be useful in certain `Use Cases`, as noted below.

**Note** that a proposed **BDQ Maintenance Group** will be established to maintain the BDQ Standard. This group will take responsibility for advising on processes for editing the BDQ standard and evaluating new BDQ Tests, `Use Cases` and other components of the BDQ Standard.

By following this workflow, you move from a human-centric research need to a machine-readable technical standard.

See also:
- [BDQ Tests: An Operational Perspective](../guide/bdqtest/index.md#51-bdq-tests-an-operational-perspective-non-normative) in the bdqtest: term-list document.
- [Framework for describing data quality](../guide/bdqffdq/index.md#2-framework-for-describing-data-quality-non-normative) in the bdqffdq: ontology guide.

### 2.1 Best Practices (non-normative)

1. **Atomic Tests**: Make each Test evaluate one single simple aspect of data quality.
1. **Start Simple**: Begin defining basic `Validation` Tests before considering more complex Tests and `Amendments`.
1. **Consider Edge Cases**: Define Tests for empty values, nulls, [whitespace](<../../index.md#glossary_whitespace> "Characters such as spaces and tabs that affect rendering of printed or displayed output, but which themselves are not printed. 1) A field that only includes whitespace is treated as `bdqval:Empty`. 2) In `bdqffdq:Valida…"), and out of range values.
1. **Use Established Authorities**: Reference widely accepted standards when possible.
1. **Generalize Appropriately**: Consider how different parts of the community might want to use a Test in slightly different ways.
1. **Document Assumptions**: Be explicit about why particular choices were made in the development of a Test including choices of default values.
1. **Plan for Evolution**: Consider how Tests might need to change over time.
1. **Iterate**: Refine Tests based on implementation feedback and real-world data.
1. **Conformance Test**: Evaluate whether Test implementations produce the expected outputs for a range of given inputs covering all decision paths in each Test.
1. **Consider Test Interactions**: Consider how multiple Tests might interact on the same data.

## 3 Defining a Use Case (non-normative)

*Before defining a Test, we must justify why it exists and how it fits into the broader ecosystem of the standard.*

### 3.1 Define the Use Case and Fitness-for-Use Requirements (non-normative)

**Purpose:** Establish the data user's perspective and fitness-for-use requirements

**The Reasoning:** A Test is only as good as the problem it solves. We begin by establishing a clear perspective on who the data user is, what use the data are to be put, what makes the data "fit for use" for that use, and what problems in the data would make it unfit for that use. 

Clearly stating the problem that we are trying to solve ensures that the Test is grounded in real-world needs and not just theoretical ideals.

* **User:** A conservation biologist.
* **Context:** We have a dataset consisting of "Expert Distributions" of taxa.  We want to validate that this dataset is usable for identifying outliers in other occurrence data (and for doing other things we may want to do with a set of expert distributions like, mapping distributions of species).  The data consist of a taxon-oriented dataset (e.g. one record per taxon) with fields identifying the taxon, providing the expert distribution as geospatial data (vector data providing shapes rather than point occurrences), along with metadata about the source of each record. 
* **What makes data Fit for this Use?**: To be fit for this purpose each record in the dataset must have:  A taxonomic name.  This taxonomic name can be found in a relevant authority on taxon names.  The taxon is also represented with a machine-readable identifier.  The spatial footprint of the expert distribution of that taxon is provided as a polygon. That polygon is a valid shape.  Each taxon distribution has its source identified as the dataset may have been compiled from multiple sources of taxon distributions.

#### 3.1.1 Refine and Formalize the Use Case (non-normative)

Now we can define our `Use Case`.  We need to specify three elements, a name for the use case, a description, and a statement of fitness for use requirements.  We want to refine our statement of the problem into concise and clear statements.  We will also need a unique identifier for the `Use Case` that software can use, but we won't examine these machine-readable identifiers at this point.  

* **Name** Validated Distribution Authority
* **Description** Validating that Taxon oriented data can provide an authoritative resource for mapping known distributions of taxa, for identifying occurrence records in other datasets that have coordinates within the known ranges of taxa, are outliers, or for similar purposes.
* **hasFitnessRequirements** Data are fit for the `Use Case` "Validated Distribution Authority" and can provide a resource for validating that occurrence records are in range if they are taxon-oriented data with fields that identify the taxon, that provide expert validated distributions as geospatial data, and provide metadata about the sources of the distributions.  To be fit for this purpose each record in the dataset must have the following properties:
  * A taxonomic name is present and can be found in [GBIF](<../../index.md#glossary_GBIF> "[Global Biodiversity Information Facility](https://www.gbif.org/) is an international network and data infrastructure funded by the world’s governments and aimed at providing anyone, anywhere, open access to data about…")'s backbone taxonomy.
  * A well-formed machine-readable taxonomic name identifier for that taxon is present.
  * A polygon providing the spatial footprint of the expert distribution for that taxon is present and valid.
  * Metadata providing the source for each taxon distribution is present.

It is helpful, but by no means required, to state the `hasFitnessRequirements` as a brief summary paragraph followed by a set of brief bullet points.  The `Use Case` is describing what we are trying to accomplish at a high level, without getting too detailed.  

In each of the bullet points, the properties that are needed for fitness are explicitly stated, e.g. "is present", "is valid", "found in an authority", etc.  These properties will be the basis for defining Tests that evaluate whether the data meet these fitness requirements, and being explicit here will help us describe Tests that separate concerns.  We will wish to be clear about fields that must be present for the data to have quality (i.e. "is present") and which fields are optional, but need to have certain properties if populated (e.g. "is valid if present")

Treat this `Use Case` definition (and everything else that follows from it) as a first draft.  We will likely need to come back and refine this `Use Case` definition as we consider the data in the wild and start defining and implementing Tests.  We may find that we need to add additional fitness requirements, or that we need to clarify the existing fitness requirements, or that we need to change the way we have stated the fitness requirements.  That is all part of the process.  It is critically important to be flexible and iterative in this process. 

See also: 
* [Context for Quality, Uses and Purposes](../guide/users/index.md#2-context-for-quality-uses-and-purposes-non-normative) in the User's Guide.
* [Concepts in the Framework (Use Cases, Policies, Contexts)](../guide/bdqffdq/index.md#223-concepts-in-the-framework-test-types-validation-issue-measure-amendment-non-normative) in the bdqffdq: ontology guide.

### 3.2 Identify the Information Elements (non-normative)

**Purpose:** Determine which fields (mapped to vocabulary terms such as [Darwin Core](<../../index.md#glossary_Darwin_Core> "[Darwin Core](https://dwc.tdwg.org/). A Standard intended to facilitate the sharing of information about biological diversity. Host of the dwc:namespace [dwc:](http://rs.tdwg.org/dwc/terms/)") terms) are in the data and are relevant to your use case.

In the Fitness For Use Framework, input fields or terms for a Test are generalized as `Information Elements`.  

We can expand each of the bullet points in the hasFitnessRequirements statement into a set of terms that are likely to map onto the data.  We may understand these well at the start, but as we work with real data and implement Tests, we will very likely need to refine this list.

* A valid taxonomic name: 
  * dwc:scientificName
  * dwc:scientificNameAuthorship
* A machine-readable identifier for the taxonomic name:
  *  dwc:scientificNameID
* A polygon of the taxon footprint: 
  * dwc:footprintWKT (the expert distribution)
  * dwc:geodeticDatum (spatial metadata for the footprintWKT)
* Metadata providing source for each taxon distribution: 
  * prov:wasAttributedTo (letting us ORCID ID to identify the source of the distribution)
  * foaf:name (Author name for a human readable attribution of the source of the distribution)
  * dcterms:source (publication or dataset source for the distribution)

Most of these terms are from Darwin Core, but we have also included some terms from other vocabularies that fit concepts in our data, such as PROV-O for provenance metadata and FOAF for person metadata.  We can use any terms from any vocabularies that are relevant to our `Use Case` and that map onto our data.

Now, we want to identify a set of Tests to be applied to these `Information Elements` to evaluate whether the data are fit for use.  

There are two key elements to the strategy at this point: (1) we want to identify and use existing Tests that can be applied before defining new Tests and (2) we want each Test to be as focused as possible on a single aspect of data quality.


### 3.3 Reuse of Existing Tests and Gap Analysis (non-normative)

**Purpose:** Identify existing BDQ Tests that can be applied to the `Information Elements` and identify gaps where new Tests are needed.

Let's identify which existing BDQ Tests might already be able to be applied to these `Information Elements` for this `Use Case`.

We can start with a simple presence check for each of these `Information Elements` (building on the "is present" statements in the `hasFitnessRequirements`) and then add more complex Tests as needed.

We are looking for existing `Validation` Tests, as we are trying to assert whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT).  By convention in BDQ, the names of these Tests start with VALIDATION_.  Simple presence Tests for "does an `Information Element` contain a value", by convention have a name that ends with  NOTEMPTY.   Between these two parts, again by convention, we use the name of the `Information Element` (or the name of a concept (e.g. LOCATION, EVENT) for several `Information Elements`).

For example, [VALIDATION_SCIENTIFICNAME_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY) is a BDQ Test that checks if there is a value in dwc:scientificName.

There are several places we could look for existing Tests within BDQ, including the [Quick Reference Guide](../terms/bdqtest/index.md), and the [index](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#31-index-to-validation-tests-non-normative) of the bdqtest: term-list document.  An easy place to look for Tests that operate on particular `Information Elements` is the Quick Reference Guide's [BDQ Test Index by Information Element Acted Upon](../terms/bdqtest/qrg_index_by_ie_actedupon.md).  

Looking here for simple presence checks for the `Information Elements` we can identify the following existing BDQ Tests (and gaps):

* A valid taxonomic name is present: 
  * dwc:scientificName [VALIDATION_SCIENTIFICNAME_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY)
  * dwc:scientificNameAuthorship [VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY)
* A machine-readable identifier for the taxonomic name is present:
  *  dwc:scientificNameID [VALIDATION_SCIENTIFICNAMEID_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_NOTEMPTY)
* A polygon of the taxon footprint is present: 
  * dwc:footprintWKT **Gap**
  * dwc:geodeticDatum [VALIDATION_GEODETICDATUM_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_GEODETICDATUM_NOTEMPTY)
* Metadata providing source for each taxon distribution is present: 
  * prov:wasAttributedTo (ORCID ID) **Gap**
  * foaf:name (Author name) **Gap**
  * dcterms:source (publication or dataset source) **Gap**

Our `Use Case` calls for more than just a presence check for these `Information Elements`, so we would want to fill in in more candidate Tests for these `Information Elements`, until we have Tests that cover each of the hasFitnessRequirements we identified for the Use Case.  If there is an existing Test that can be applied to a particular `Information Element` and is relevant our `Use Case`, we should include that Test, and would need strong justification to do otherwise.  Filling in a few more Tests:  

* A taxonomic name is present and can be found in GBIF's backbone taxonomy.
  * dwc:scientificName
    * [VALIDATION_SCIENTIFICNAME_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_NOTEMPTY)
    * [VALIDATION_SCIENTIFICNAME_FOUND](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAME_FOUND) (check if the name can be found in an authority, GBIF's backbone taxonomy by default)
  * dwc:scientificNameAuthorship
    * [VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY)
* A well-formed machine-readable identifier taxonomic name for that taxon is present.
  * dwc:scientificNameID 
    * [VALIDATION_SCIENTIFICNAMEID_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_NOTEMPTY)
    * [VALIDATION_SCIENTIFICNAMEID_COMPLETE](../terms/bdqtest/index.md#VALIDATION_SCIENTIFICNAMEID_COMPLETE) (check if the identifier is well-formed)
* A polygon of the taxon footprint is present and valid: 
  * dwc:footprintWKT 
    * Is present: **Gap**
    * Is valid spatial data in a Well Known Text serialization: **Gap**
  * dwc:geodeticDatum 
    * [VALIDATION_GEODETICDATUM_NOTEMPTY](../terms/bdqtest/index.md#VALIDATION_GEODETICDATUM_NOTEMPTY) 
    * [VALIDATION_GEODETICDATUM_STANDARD](../terms/bdqtest/index.md#VALIDATION_GEODETICDATUM_STANDARD) (check if the value is a valid [geodetic datum](<../../index.md#glossary_geodetic_datum> "A mathematical model that uses a reference ellipsoid to describe the size and shape of the surface of the earth and adds to it the information needed for the origin and orientation of coordinate systems on that surface…"), e.g. by checking if it can be found in an authority like [EPSG](<../../index.md#glossary_EPSG> "European Petroleum Survey Group database contains many definitions of coordinate reference systems and coordinate transformations which may be global, regional, national, or local in application."))
* Metadata providing source for each taxon distribution is present: 
  * prov:wasAttributedTo (ORCID ID) 
    * Is present: **Gap**
    * Conforms to the structure of an ORCID ID identifier: **Gap**
    * Is a valid ORCID ID (e.g. by checking if it can be found in an authority like the ORCID ID registry): **Gap**
  * foaf:name (Author name) 
    * Is present: **Gap**
    * Is consistent with the ORCID ID. **Gap**
  * dcterms:source 
    * Is present: (publication or dataset source) **Gap**


Let's focus on the gaps.  The BDQ Issues in GitHub that define Tests are a good place to start.  These Tests are a superset of the BDQ Tests and have had some level of documentation.

For dwc:footprintWKT, we could guess the name of the Test, following the naming conventions, as VALIDATION_FOOTPRINTWKT_NOTEMPTY, and search the issues for [that name](https://github.com/tdwg/bdq/issues?q=VALIDATION_FOOTPRINTWKT_NOTEMPTY) or [the Information Element part of that name](https://github.com/tdwg/bdq/issues?q=FOOTPRINTWKT).  These searches may return a match, but guessing the name is a fragile strategy, as the desired Test might not have a name exactly matching our guess, so a better broader strategy is to search and scan lists of issues:

* Existing proposals tagged as [SUPPLEMENTARY](https://github.com/tdwg/bdq/issues?q=label%3ASupplementary) that would fill the desired gap.
* Existing proposals tagged as [IMMATURE/INCOMPLETE](https://github.com/tdwg/bdq/issues?q=label%3AImmature%2FIncomplete) that may fill the gap, but are not yet fully developed.
* Existing proposals tagged as [DO NOT IMPLEMENT](https://github.com/tdwg/bdq/issues?q=label%3A%22DO%20NOT%20IMPLEMENT%22) that would fill the desired gap, but have been rejected for implementation.  These Tests should be reconsidered only with great caution.
* **Note that all of these issues in GitHub are Closed, the default issue search which includes is:open will not find them.**

There is an existing definition for a Test, [VALIDATION_FOOTPRINTWKT_NOTEMPTY](https://github.com/tdwg/bdq/issues/226), in the documented [Supplementary](<../../index.md#glossary_Supplementary> "Tests regarded as not [CORE](<../../index.md#glossary_CORE> "Tests for evaluating biodiversity data quality as represented by the values of `Darwin Core` terms. CORE tests address identified user needs, are widely applicable, informative, unambiguous, well defined, and straight f…") because of one or more reasons: Not widely applicable; not clearly matched to an identified data quality need; not informative concerning the 'quality' or lack of quality of the data; likely t…") Tests.

Looking at the description of that Test we see:

* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY
* **Description** Is there a value in dwc:footprintWKT?
* **TestType** Validation
* **Information Elements Acted Upon** dwc:footprintWKT
* **Expected Response** COMPLIANT if dwc:footprintWKT is bdqval:NotEmpty; otherwise NOT_COMPLIANT

This is telling us, much like an entry in the Quick Reference Guide or the more detailed entry in the bdqtest: term-list document, that this Test is a simple presence check for dwc:footprintWKT.

See also: 
* The [Quick Reference Guide](../terms/bdqtest/index.md) to the BDQ Tests.
* The [BDQ Tests Term-List document](../terms/bdqtest/index.md) for more detailed descriptions of each Tests.
* List of [DO_NOT_IMPLEMENT Tests](../supplement/index.md#211-tests-tagged-as-do-not-implement-non-normative) in the Supplement.

## 4 Defining a New Test (non-normative)

Let's walk through the steps and decisions involved in defining a Test, using VALIDATION_FOOTPRINTWKT_NOTEMPTY as an example, and see how the components of the Test are justified and how they fit together.

### 4.1 A Simple Description of the Test (non-normative)

The Description of the Test is an easy-to-understand, concise explanation of what the Test does. It is a human-oriented explanation.  It is a good starting point for defining a Test.

* **Description** “Is there a value in dwc:footprintWKT?”

As descriptions go, it doesn’t get simpler than that.

This description will also be used in Data Quality Reports to explain to users what the Test is doing, so it should be clear and concise.  It should not include details about how the Test might be implemented. The description should provide just enough information for a user to understand what the Test is checking for.

**Reasoning for Simplicity:** In this Test, we are not validating the *contents* or *mathematical structure* of the WKT polygon—only that it contains some data. We could add to a workflow for example, by adding subsequent Tests for validating the contents of dwc:footprintWKT, but focusing on a "limited specific aspect" of data is a core principle of the BDQ standard.

See also [Principles for Defining Tests](../supplement/index.md#3112-principles-non-normative) in the Supplement document.

### 4.2 Identify the Information Elements (non-normative)

**Purpose** Identify the specific fields in the input data (`Information Elements`) that the Test will evaluate.

For this new Test we want to evaluate one `Information Element`, `dwc:footprintWKT`, which is a term in Darwin Core that provides spatial data, in this context, a polygon of the taxon footprint.  The WKT (Well Known Text serialization of spatial data) could be of a point, vector, polygon, or set of polygons, but in this case we are expecting a polygon.  

An `Information Element` is classified as either `ActedUpon` or `Consulted`.  An `Information Element` is `ActedUpon` if it is the primary focus of the Test, and it is `Consulted` if it is supporting information used to run the Test.  In this case, `dwc:footprintWKT` is the primary focus of the Test, so it is an `Information Element` that is `ActedUpon`.  

Briefly consider another Test that might be proposed to evaluate the validity of the WKT polygon in `dwc:footprintWKT`.  This Test might have the same `Information Element` that is `ActedUpon`, `dwc:footprintWKT`, but it might also use the content of `dwc:geodeticDatum` to interpret the value in `dwc:footprintWKT`. In such a Test, the supporting `Information Element` `dwc:geodeticDatum` would be `Consulted`, the Test is making an assertion about the value in `dwc:footprintWKT` and "consulting" the value in `dwc:geodeticDatum` to do so, but not actually making an assertion about the value in `dwc:geodeticDatum` itself.  If a Test asserts compliance about `dwc:footprintWKT` but uses `dwc:geodeticDatum` to interpret it, then `dwc:footprintWKT` is `ActedUpon` and `dwc:geodeticDatum` is `Consulted`.

The Test we are developing does not require any supporting information, so there are no `Information Elements` that are `Consulted`:

* **Information Elements Acted Upon** dwc:footprintWKT
* **Information Elements Consulted** None

See also:
- [Inputs to Tests](../guide/users/index.md#321-inputs-to-tests-non-normative) in the User's Guide.
- [Information Elements](../guide/bdqffdq/index.md#222-information-elements-non-normative) in the bdqffdq: ontology guide.

### 4.3 Select the Test Type (non-normative)

**Purpose**: Determine in what way the Test evaluates data quality.

There are four Test types in BDQ: 

* **Validation** Assess whether data meet quality criteria (COMPLIANT/NOT_COMPLIANT)
* **Amendment** Propose improvements to data quality (AMENDED/NOT_AMENDED)
* **Measure** Quantify an aspect of data quality (numerical result) or measure completeness (COMPLETE/NOT_COMPLETE)
* **Issue** Flag potential problems for human review (POTENTIAL_ISSUE/NOT_ISSUE)  

We choose VALIDATION for this Test because we are asserting whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT).

* **Test Type** Validation

See also: 
* [Test Types](../guide/bdqtest/index.md#3-test-types-non-normative) in the BDQ Tests: Concepts and Use document.
* [Test Types](../guide/users/index.md#31-test-types-non-normative) in the User Guide.

> **Alternative Pattern: metric + analytical threshold**
>
> In some cases, the relationship between the value of an `Information Element` and fitness for use is not well captured as a single `Validation` rule. In those situations a `Single Record` `Measure` can return a numeric metric that consumers of `Data Quality Reports` can interpret using an analytical threshold that is specific to their `Use Case` (for example, using [MEASURE_EVENTDATE_DURATIONINSECONDS](../terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS) and applying a threshold such as “duration ≤ 86401 seconds” to identify records with day-level temporal precision).

### 4.4 Name the Test (non-normative)

**Purpose**: Create human and machine-readable names for the Test.

#### 4.4.1 Anatomy of a Test Label (non-normative)

**The Reasoning:** BDQ uses a convention for the naming pattern so that Test labels are predictable and descriptive: **TESTTYPE_INFORMATIONELEMENTS_EVALUATION**.

The use of all upper case with underscores is a convention inherited from the use of [Java](<../../index.md#glossary_Java> "Java is a registered trademark of Oracle and/or its affiliates.") constants to identify Tests in contributing projects.

The label provides a concise summary of the Test's purpose and logic.  The components of the label are:

* **Test Type** one of VALIDATION, AMENDMENT, MEASURE, or ISSUE, as described above.
* **Information Elements** Expressed as the "simple English term" for the `Information Element` being evaluated, or if multiple `Information Elements` are being evaluated together, a succinct more general concept (like LOCATION or EVENT) that encompasses those `Information Elements`
  * The use of "simple English terms" in the label (e.g., FOOTPRINTWKT) rather than the formal prefixed term (dwc:footprintWKT) to make it more accessible to human readers, and allows the label to be used as a string constant in many programming languages.
* **Evaluation:** What is the Test testing? 
  * Examples of evaluations include "NOTEMPTY" (a value is present), “FOUND” (the value can be found in a source authority), “INRANGE” (the value is within an expected range), etc.  See the [Evaluations](../supplement/index.md#evaluations) table in the [Supplement](../supplement/index.md).

This Test is a Validation, it is evaluating the Information Element `dwc:footprintWKT`, and it is evaluating whether there is a value in `dwc:footprintWKT`, so the label is VALIDATION_FOOTPRINTWKT_NOTEMPTY.  This label is expected to be a constant that does not change, even in translation.

We need to create a Preferred Label for the Test to support accessibility (the ability of screen readers to read the label in a more human friendly way), and to provide for translations of the name of the Test into additional languages.

The Preferred Label for this Test could be "Validation dwc:footprintWKT Not Empty".  This Preferred Label is expected to be translated into different languages (e.g. "Dilysu dwc:footprintWKT Ddim yn Wag"@cy)

This gives us the following names for the Test: 
* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY
* **Preferred Label** Validation dwc:footprintWKT Not Empty 

See also: [Naming Conventions (non-normative)](../supplement/index.md#312-naming-conventions-non-normative) in the [Supplement](../supplement/index.md) document.

#### 4.4.2 Identifiers supporting software and developers (non-normative)

While the label is a human-friendly identifier for the Test, we need a machine-readable identifier that can be used by software to identify the Test.  In BDQ, this is the `Term Name`, which is a UUID.  The `Term Name` allows software to unambiguously identify the Test, and to ensure that in a search through available Tests, this specific Test is located.

We also need to provide a date for the Test definition, and to update that date if the Test definition is modified.

This gives us the following additional properties for the Test:
* **Term Name** c6b705fc-7cf8-4af1-88ab-7a38d85f7109 
* **Modified** 2024-01-29

(Once accepted into BDQ, these properties would be combined to form the fully qualified Term [IRI](<../../index.md#glossary_IRI> "Internationalized Resource Identifier is an internet protocol standard which builds on the Uniform Resource Identifier (URI) protocol by greatly expanding the set of permitted characters.") for the Test (e.g. https://rs.tdwg.org/ bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933) and the Term Version IRI for a particular version of the Test (e.g. https://rs.tdwg.org/ bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933-2024-07-24))

See also: [Key to bdqtest: Vocabulary Terms](../list/bdqtest/index.md#18-key-to-vocabulary-terms-normative) in the bdqtest: term-list document.

### 4.5 Identify the Data Quality Dimension and Criterion (non-normative)

**Purpose**: Classify the Test according to the aspect of data quality it addresses.

All BDQ Tests have a dimension of data quality, formally defined in the [bdqdim:](../list/bdqdim/index.md) vocabulary.

BDQ Data Quality Dimensions include:
* **Completeness**: Are all required data elements present?
* **Conformity**: Do data values conform to format, syntax, or controlled vocabularies?
* **Consistency**: Are data values logically consistent with each other?
* **Likeliness**: Do data values fall within expected ranges or distributions?
* **Resolution**: Is the level of detail appropriate for the intended use?

The question we wish to ask is whether there is a value in `dwc:footprintWKT`.  In this Test we are only asking if any value is present.  We are not asking if it is correctly formatted Well Known Text spatial data, or whether it contains in-range values, or anything else, we are simply asking if any value is present.  So this Test is addressing the Completeness dimension of data quality.

This seems a very trivial Test.  It is.  That is important.  We do not wish to over complicate our Tests.  We want to ask simple questions that are easy to understand and implement, and that address specific aspects of data quality.  We assemble multiple simple atomic Tests to evaluate distinct aspects of data quality in a `Use Case`.

If some data are absent and other data are incorrectly formatted, a more complicated Test that checks for both presence and correct formatting will not be able to distinguish between these two problems, and thus will not be as useful for our `Use Case` as a simple presence check (combined with a separate Test to assess correct formatting).  

BDQ `Validations` also have a `Criterion` property.  Each `Criterion` represents an abstract way of evaluating whether a data value meets expectations for a particular `Use Case`.  These criteria are formally defined in the [bdqcrit:](../list/bdqcrit/index.md) vocabulary.  For example, the Criterion `NotEmpty` is defined as "The data value is not empty (i.e., it contains some data)".  This is exactly the criterion we are applying in this Test, so we will use the `NotEmpty` criterion for this Test.  

This gives us the following additional properties for the Test:
* **Data Quality [Dimension](<../../index.md#glossary_Dimension> "See [bdqffdq:DataQualityDimension.](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqffdq/index.md#dataqualitydimension)")** Completeness
* **Criterion** NotEmpty

All BDQ Test types have a `Data Quality Dimension` (taking values from the [bdqdim:](../list/bdqdim/index.md) vocabulary).  Only `Validations` and `Issues` have a `Criterion` (taking values from the [bdqcrit:](../list/bdqcrit/index.md) vocabulary), while `Amendments` have an `Enhancement` (taking values from the [bdqenh:](../list/bdqenh/index.md) vocabulary).  `Measures` have only the `Data Quality Dimension`.

See also:
* Diagrams of Test Types and their Properties in [Concepts in the Framework](../guide/bdqffdq/index.md#223-concepts-in-the-framework-test-types-validation-issue-measure-amendment-non-normative) in the bdqffdq: guide.
* [bdqdim:](../list/bdqdim/index.md) for the data quality dimension vocabulary.
* [bdqcrit:](../list/bdqcrit/index.md) for the criteria vocabulary.
* [bdqenh:](../list/bdqenh/index.md) for the enhancement vocabulary.

### 4.6 How many records are we examining at once? (non-normative)

**Purpose**: Determine whether the Test is applied to single records or multiple records.

In BDQ, Tests can be applied to single data records or to multiple records.  A Test that is applied to a single record is called a "SingleRecord" Test, and a Test that is applied to multiple records is called a "MultiRecord" Test.  The distinction between these two types of Tests is important because it affects how the Test is implemented and how the results are interpreted.

We wish to step through the input dataset one record at a time and for each record assess whether or not there is a value in dwc:footprintWKT.  Thus we are applying this Test to single records, and thus this is a `Single Record` Test.  

We will come back later and define another Test to measure how much of the dataset is compliant for this Test, and that will be a `Multi Record` Test.

* **Resource Type** SingleRecord

See also: [Resource Types](../guide/bdqtest/index.md#42-resource-types-normative) in the BDQ Tests: Concepts and Use document.

### 4.7 Define the Test Specification (non-normative)

**Purpose**: Provide a clear, unambiguous description of the Test's logic and expected outcomes.

Now we need to provide the unambiguous technical details required for a developer to implement the Test.  

Let's start with the question the Test is asking, very simply phrased:  **Is there a value in dwc:footprintWKT?**

How do we phrase that question in a way that provides clear and unambiguous guidance to a developer who will implement the Test? In the BDQ standard, the phrasing follows a standard structure and terminology. 

Since this is a `Validation`, the Test will return either COMPLIANT or NOT_COMPLIANT.  The Test will return COMPLIANT if there is a value in dwc:footprintWKT, and it will return NOT_COMPLIANT if there is not a value in `dwc:footprintWKT`.  We can phrase this as follows:

**Expected Response** COMPLIANT if dwc:footprintWKT contains some value; otherwise NOT_COMPLIANT

But, "contains some value" might be interpreted in different ways by different developers, so we will use an explicit concept from BDQ that allows developers to look in one place for the meaning of "contains some value", and know that this is a standard concept that gets reused.

The [bdqval:](../list/bdqval/index.md) vocabulary contains a term for just this purpose: [bdqval:NotEmpty](../list/bdqval/index.md#bdqval_NotEmpty), a standard definition of this common concept for reuse in many Tests, preventing ambiguity in implementation. Thus, we can rephrase the expected response to link to this BDQ concept:

**Expected Response** COMPLIANT if dwc:footprintWKT is bdqval:NotEmpty; otherwise NOT_COMPLIANT

This means that implementers should examine the input data, evaluate the statements in order, and return a result from the first statement that is true.
* COMPLIANT if dwc:footprintWKT is bdqval:NotEmpty; 
* otherwise NOT_COMPLIANT

In this simple case, if `dwc:footprintWKT` is `bdqval:NotEmpty` [bdqval:NotEmpty](<../list/bdqval/index.md#bdqval_NotEmpty> "An evaluation of a value, which in the context of the evaluation, returns true if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns false."), the Test should return COMPLIANT and stop there.  If `dwc:footprintWKT` is not `bdqval:NotEmpty` (i.e. is `bdqval:Empty` [bdqval:Empty](<../list/bdqval/index.md#bdqval_Empty> "An evaluation of a value, which in the context of the evaluation, returns false if the value contains any characters or values other than those in the range U+0000 to U+0020, otherwise returns true.")), the Test should return NOT_COMPLIANT.
 
Formally in the bdqffdq: ontology, `Specification` is a class, which has a `bdqffdq:hasExpectedResponse` [bdqffdq:hasExpectedResponse](<../list/bdqffdq/index.md#bdqffdq_hasExpectedResponse> "Text describing the logic to be followed by a bdqffdq:Implementation of a bdqffdq:Specification specifying the values of bdqffdq:ResponseStatus and bdqffdq:ResponseResults that should be produced from the evaluation of…") property (the `Expected Response` text). The Specification can have other properties for source authorities, parameters and default values.  The specification for a simple Test is found in the text of the `hasExpectedResponse`, in a more complex Test, the specification is found split across all these properties of the `Specification` class instance.  When we talk about the specification of a Test, we mean the `Expected Response`, sometimes combined with other properties of a `Specification`.

See also: 
* [Reading a Specification](../guide/implementers/index.md#232-reading-a-specification-non-normative) in the Implementers Guide.
* [The bdqval: vocabulary](../list/bdqval/index.md) for standard concepts that can be used in Test specifications.
* The `Data Quality Solutions` portions of the diagrams in [Concepts in the Framework](../guide/bdqffdq/index.md#223-concepts-in-the-framework-test-types-validation-issue-measure-amendment-non-normative) in the bdqffdq: guide.

#### 4.7.1 What Isn't Said in the Test Specification (non-normative)

For the purposes of simplicity and clarity, the expected response does not include all the details of a `Response` from a Test, just the key elements that implementers need to understand the logic of the Test.  The response from a Test is required to contain metadata (`bdqffdq:hasResponseStatus` [bdqffdq:hasResponseStatus](<../list/bdqffdq/index.md#bdqffdq_hasResponseStatus> "The bdqffdq:ResponseStatus object asserted by a bdqffdq:Response.")), the value of the result of the Test (`bdqffdq:hasResponseResult` [bdqffdq:hasResponseResult](<../list/bdqffdq/index.md#bdqffdq_hasResponseResult> "The bdqffdq:ResponseResult object asserted by a bdqffdq:Response.") or `bdqffdq:hasResponseResultValue` [bdqffdq:hasResponseResultValue](<../list/bdqffdq/index.md#bdqffdq_hasResponseResultValue> "Data property carrying the value of a bdqffdq:Response when the value is not an object.")) and a human readable statement about why the Test reached the conclusion it did in a particular case (`bdqffdq:hasResponseComment` [bdqffdq:hasResponseComment](<../list/bdqffdq/index.md#bdqffdq_hasResponseComment> "Free text describing the bdqffdq:Response made in the response and why that conclusion was reached.")).   

**Expected Response** COMPLIANT if dwc:footprintWKT is bdqval:NotEmpty; otherwise NOT_COMPLIANT

This is shorthand for the explicit, but much harder to read:
* bdqffdq:hasResponseStatus is RUN_HAS_RESULT and bdqffdq:hasResponseResult is COMPLIANT with an explanatory bdqffdq:hasResponseComment that dwc:footprintWKT contains a value if dwc:footprintWKT is bdqval:NotEmpty; 
* otherwise bdqffdq:hasResponseStatus is RUN_HAS_RESULT and bdqffdq:hasResponseResult is NOT_COMPLIANT with an explanatory bdqffdq:hasResponseComment stating that dwc:footprintWKT contains no value.

`Responses` from Tests must have the tripartite status, result, and comment structure, but the `Expected Response` in the Test specification is a concise statement of the logic of the Test, without all of these details (details for which the content is explicit in the BDQ standard, e.g. if the result is COMPLIANT, the status must be RUN_HAS_RESULT, and there must be a comment).

The conventions of evaluating clauses in sequence, returning a result from the first clause that evaluates to true, and highlighting only the key differences in each clause are very important in making complex Expected Responses readable and understandable to implementers.  (see, for example, the Expected Response for [VALIDATION_DATEIDENTIFIED_INRANGE](../terms/bdqtest/index.md#validation_dateidentified_inrange)).

See also:
* [Responses from Tests](../guide/users/index.md#323-outputs-responses-from-tests-normative) in the Users Guide.
* [Reading a Specification](../guide/implementers/index.md#232-reading-a-specification-non-normative) in the Implementers Guide.
* [Responses as a Shorthand](../guide/implementers/index.md#2321-response-as-shorthand-for-a-set-of-bdqffdq-concepts-non-normative) in the Implementers Guide.

### 4.8 Source Authority? (non-normative)

**Purpose**: If the Test references an external authoritative source, specify that source authority in the Test definition.

In BDQ, if a Test references some external authoritative source, e.g. a controlled vocabulary, an authority file, a registry, etc., it is important to specify that source authority in the Test definition.  This allows implementers to know where to look for the authoritative information that they need to run the Test. The source authority also allows users of the Test results to understand the basis for the Test's logic.

The new Test is not referencing any external authoritative source.  We are simply checking for the presence of a value in `dwc:footprintWKT`, so there is no source authority to specify.  Note that the definition of `dwc:footprintWKT` in Darwin Core is authoritative for this Test, but we do not need to specify that as a source authority in the Test definition, as it is implicit in the use of the term `dwc:footprintWKT` itself.

### 4.9 Generalize the Test? (non-normative)

**Purpose**: If different users of the Test might have slightly different data quality needs with regard to that Test, consider generalizing the Test with a parameter.

Different users of a Test might have slightly different data quality needs with regard to that Test.  For example, checking if elevation values are in range within national boundaries for some national dataset, rather than more general global minimum and maximum possible elevations.  In such cases, in BDQ, the Test can be generalized with one or parameters, allowing different users to specify slightly different behaviors for the Test, while retaining the same internal logic.

In this Test, we are simply checking for the presence of a value in `dwc:footprintWKT`, so there is no need to generalize the Test with a parameter.

### 4.10 List the properties of the Test (non-normative)

**Purpose**: Create a human-readable label for the Test and list its properties in a structured format.

Now let's put all of the information about the Test together.  See the [bdqtest: term-list](../list/bdqtest/index.md) document for examples (like the very similar [VALIDATION_COUNTRYCODE_NOTEMPTY](../list/bdqtest/index.md#bdqtest_853b79a2-b314-44a2-ae46-34a1e7ed85e4).  

For our Test, we have:

* **Description** Is there a value in dwc:footprintWKT?
* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY 
* **Preferred Label** Validation dwc:footprintWKT Not Empty 
* **Term Name** c6b705fc-7cf8-4af1-88ab-7a38d85f7109 
* **Modified** 2024-01-29
* **Test Type** Validation
* **Data Quality Dimension** Completeness
* **Resource Type** SingleRecord
* **Criterion** NotEmpty
* **Information Elements Acted Upon** dwc:footprintWKT
* **Expected Response** COMPLIANT if dwc:footprintWKT is bdqval:NotEmpty; otherwise NOT_COMPLIANT

To formally express this Test in [RDF](<../../index.md#glossary_RDF> "Resource Description Framework - a W3C standard for modeling, interchanging, and linking structured data on the web. Hosts the namespace [rdf:](http://www.w3.org/1999/02/22-rdf-syntax-ns#)") we would need to add some more identifiers and structures, but the above are the key properties that define the Test and provide the information needed for an implementer to understand and implement the Test.  See the [Fitness For Use Framework Ontology: Concepts and Use](../guide/bdqffdq/index.md) document for details about the full formal structure.

See also: 
* [Test Types](../guide/users/index.md#31-test-types-non-normative) in the User’s Guide.
* [Reading Test Descriptors](../guide/implementers/index.md#23-reading-test-descriptors-non-normative) in the Implementer’s Guide.
* [Relating Classes and Properties](../guide/bdqffdq/index.md#311-relating-classes-and-properties-non-normative) in the Fitness For Use Framework Ontology: Concepts and Use document.

#### 4.10.1 Formal RDF Representation of the Test (non-normative)

This simple list of properties is sufficient for a human reader to understand the Test and for a developer to implement the Test.  However, to formally express this Test in RDF we would need to add some more identifiers and structures, but the above are the key properties that define the Test and provide the information needed for an implementer to understand and implement the Test.  The [bdqffdq: ontology guide](../guide/bdqffdq/index.md) gives the details about the full formal structure.  We won't go into the details of the RDF representation here.

See also:
* [Diagram of Test Concepts](../guide/implementers/index.md#3-compliant-implementation-normative) in the implementers guide.
* [Example RDF for a Test](../guide/bdqtest/index.md#6-example-rdf-description-of-a-test-non-normative) in the BDQ Tests: Concepts and Use document (VALIDATION_COUNTRYCODE_STANDARD in an RDF/XML serialization).
* [Example RDF for a Test](../guide/bdqffdq/index.md#26-example-representation-of-a-bdq-test-non-normative) in the Fitness For Use Framework Ontology: Concepts and Use (VALIDATION_COUNTRY_FOUND in a Turtle serialization). 

#### 4.10.2 Summary of the Test Definition (non-normative)

VALIDATION_FOOTPRINTWKT_NOTEMPTY is a `Validation` Test that takes `dwc:footprintWKT` as input, and asks a very simple question, "Is there a value in dwc:footprintWKT?", This question is spelled out very clearly for an implementer in the `Expected Response`.  The expected response is COMPLIANT if there is a value in `dwc:footprintWKT`, and NOT_COMPLIANT if there is not.  This is exactly the simple presence check we need for our `Use Case`.

Thus, we could include this Test in our `Use Case`, even though it is not yet accepted into the BDQ standard. We could implement it, Test the implementation, and put it forward to the Maintenance group for consideration for inclusion in the standard. This Test would fill the gap of a simple presence check for `dwc:footprintWKT`.

## 5 A Test to Fill another Gap (non-normative)

Another gap we identified in the `Use Case` was evaluating whether `prov:wasAttributedTo` contains a value, and whether that value is a valid ORCID ID.  Under the principle of keeping Tests focused on a single aspect of data quality, we can break this down into three separate Tests:

* prov:wasAttributedTo (Contains a value) **Gap**
* prov:wasAttributedTo (Conforms to the structure of an ORCID ID) **Gap**
* prov:wasAttributedTo (Is found in an ORCID ID registry) **Gap**

The first of these is a simple presence check for `prov:wasAttributedTo`, which is a term in the PROV ontology that provides metadata, in this case, about the source of each taxon distribution.  We could define a Test for this gap in a similar way to the Test we just defined for dwc:footprintWKT.  The Test would be a `Validation` Test, it would take `prov:wasAttributedTo` as input, and it would ask the question "Is there a value in prov:wasAttributedTo?"  The expected response would be COMPLIANT if there is a value in `prov:wasAttributedTo`, and NOT_COMPLIANT if there is not a value.

* **Description** Is there a value in prov:wasAttributedTo?
* **Label** VALIDATION_WASATTRIBUTEDTO_NOTEMPTY 
* **Preferred Label** Validation prov:wasAttributedTo Not Empty 
* **Term Name** {some UUID}
* **Modified** 2026-03-25
* **Test Type** Validation
* **Data Quality Dimension** Completeness
* **Resource Type** SingleRecord
* **Criterion** NotEmpty
* **Information Elements Acted Upon** prov:wasAttributedTo
* **Expected Response** COMPLIANT if prov:wasAttributedTo is bdqval:NotEmpty; otherwise NOT_COMPLIANT

## 6 Defining a more complicated Test with a Source Authority (non-normative)

The next gap we identified in the `Use Case` was: 

** prov:wasAttributedTo (Conforms to the structure of an ORCID ID) **Gap**

This is a more complex Test, as it requires not simply checking for the presence of a value, but rather checking that a value conforms with the expected structure of an ORCID ID.  

Note than on the principle of one Test evaluates one simple thing, we are asking whether the value has the correct structure for an ORCID ID, but we are not asking whether the value is actually a valid ORCID ID (e.g. by checking if it can be found in an authority like the ORCID ID registry).  We would define a separate Test for that second question, and thus keep each Test focused on a single aspect of data quality.

### 6.1 A Simple Description of the Test (non-normative)

The Description of the Test is an easy-to-understand, concise explanation of what the Test does. It is a human-oriented explanation.  

We could phrase this as "Is there a value in prov:wasAttributedTo, and if so, does the value conform to the expected structure of an ORCID ID?"  This, however, is combining two questions into one.

We want this Test to evaluate a single aspect of data quality, which is whether the value in `prov:wasAttributedTo` has the structure of an ORCID ID, that is, does it have the right format.  Thus we can phrase the description as follows:

* **Description** Does the value in prov:wasAttributedTo conform to the format of an ORCID ID* 

### 6.2 Identify the Information Elements (non-normative)

The `Information Element` that this Test will evaluate is `prov:wasAttributedTo`, which is a term in the [PROV ontology](https://www.w3.org/TR/prov-o/) that provides metadata about the source of each taxon distribution.  This `Information Element` is `ActedUpon`, as it is the primary focus of the Test.  This Test does not require any supporting information, so there are no `Information Elements` that are `Consulted`.

* **Information Elements Acted Upon** prov:wasAttributedTo

### 6.3 Select the Test Type (non-normative)

We are asserting whether the value in `prov:wasAttributedTo` conforms to the structure of an ORCID ID, so we are asserting whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT), thus we choose VALIDATION for this Test.

* **Test Type** Validation

### 6.4 Name the Test (non-normative)

Now we can name the Test, following the naming conventions in BDQ.  The Test is a `Validation`, it is evaluating the `Information Element` `prov:wasAttributedTo`, and it is evaluating whether the value in `prov:wasAttributedTo` has the expected format of an ORCID ID.  So, the label for this Test could be VALIDATION_WASATTRIBUTEDTO_STANDARD.  (In contrast, we could frame another Test to check if the value in `prov:wasAttributedTo` can be found in an authoritative list of ORCID IDs, which could be labeled VALIDATION_WASATTRIBUTEDTO_FOUND.  There is some overlap in the words used for this [evaluation](../supplement/index.md#evaluations) part of the names, typically, _FOUND is used for matches against large and changing authorities, like taxon names, and _STANDARD for correct formatting, as in dates, or matches to short stable controlled vocabularies like taxon rank.)  

* **Label** VALIDATION_WASATTRIBUTEDTO_STANDARD

We will also want to provide a more readable and translatable Preferred Label, and a machine-readable identifier, and a version date for this Test.

* **Preferred Label** "Validation prov:wasAttributedTo Standard".  
* **Term Name** {some UUID}
* **Modified** 2026-03-25

### 6.5 Identify the Data Quality Dimension and Criterion (non-normative)

This Test is a `Validation`, so it will have both a `Data Quality Dimension` and a `Criterion`.  

The `Data Quality Dimension` is the aspect of data quality that this Test is addressing, looking at the bdqdim; vocabulary we find `Conformance` defined as "Where data in a bdqffdq:InformationElement conform to a format, syntax, data type, range, or standard."  We are asking if the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID, so this is a good fit.

Similarly, in the [bdqcrit: vocabulary](../list/bdqcrit/index.md) we find `Standard` defined as "Data in a bdqffdq:InformationElement conform to a format, syntax, data type, or standard. Corresponding dimension is bdqdim:Conformance."  Again, this sounds like a good fit.

* **Data Quality Dimension** Conformance
* **Criterion** Standard

In contrast, in another Test that evaluates whether the ORCID ID is valid by checking if it can be found in an authority like the ORCID ID registry, we would use a `Data Quality Dimension` of `Conformance`, but a `Criterion` of **`Found`**.

### 6.6 How many records are we examining at once? (non-normative)

This Test would evaluate the value of `prov:wasAttributedTo` for each record, so we are applying this Test to single records, and thus this is a `Single Record` Test.

* **Resource Type** SingleRecord

### 6.7 Define the Test Specification (non-normative)

We could make a very simple specification for this Test, such as "COMPLIANT if the value in prov:wasAttributedTo is a valid ORCID ID; otherwise NOT_COMPLIANT".  However, this is not very clear or specific for an implementer.  What does it mean for a value to be a valid ORCID ID?  How would an implementer determine that?  We need to provide more specific guidance in the specification to ensure that different implementers will implement the Test in a consistent way and thus get comparable results.

We are asking not if the value in `prov:wasAttributedTo` is found in some authority, but if it conforms to the expected format for an ORCID ID.  Thus we could phrase the specification as "COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID; otherwise NOT_COMPLIANT".  This is better, but what happens if there is no value in `prov:wasAttributedTo`, if it is `bdqval:Empty`?  That would be NOT_COMPLIANT, but it would not be because the value does not conform to the expected format for an ORCID ID, it would be because there is no value at all, and this Test would overlap in what it is testing with VALIDATION_WASATTRIBUTEDTO_NOTEMPTY, which is our separate Test above that checks for the presence of a value in `prov:wasAttributedTo`.  We want to keep these two Tests separate and focused on different aspects of data quality, so we need to make sure the specification for this Test is clear that it is only evaluating whether a value that is present conforms to the expected format for an ORCID ID, and it is not evaluating whether a value is present at all. We accomplish this by asserting that the presence of some value in `prov:wasAttributedTo` is a prerequisite for this Test, and if that prerequisite is not met, then this Test cannot return a result.

So, we could phrase our Test specification (our `Expected Response`) as a sequence of:
* INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty;
* COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID; 
* otherwise NOT_COMPLIANT

This could work for our `Use Case`, but what does it mean for a value to conform to the expected format for an ORCID ID?  We need to provide more specific guidance on what we mean by that.  We could be more explicit in the specification: 

* INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty;
* COMPLIANT if the value in prov:wasAttributedTo conforms to the regular expression "^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"
* otherwise NOT_COMPLIANT

But, where did that regular expression "^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$" come from?  It isn't inherent in the definition of `prov:wasAttributedTo`, it is something specific to some external authority.  In bdqffdq: is a means for us to separate out these specifics, the `Source Authority` (which will then set the stage for making this Test more generally applicable).

#### 6.7.1 Source Authority (non-normative)

When a Test references some external authoritative source, e.g. a controlled vocabulary, an authority file, a registry, etc., outside of the BDQ namespaces (the ontology or vocabularies that form the BDQ standard), or the definition of terms used as `Information Elements`, we must specify that external dependency, that Source Authority in the Test definition.  

As noted in the BDQ documentation, many aspects of "data quality" or "fitness for use" cannot be evaluated IF no authority exists to which to evaluate data values.  For example, we cannot evaluate whether a value is a valid ORCID ID if we do not have an authority that defines what a valid ORCID ID looks like.  In this case, the authority is the ORCID organization itself, which provides documentation on the expected format for ORCID IDs.  We can reference this authority in our Test definition, and then use the information from that authority to define the expected format for ORCID IDs in our Test specification.  This is an externality we must reference in our Test definition, and thus we need to specify the source authority for this Test.

In bdqffdq:, a `Specification` has a `hasExpectedResponse` property that contains the text of the Expected Response, and it can also have a `hasAuthoritiesDefaults` property.  The `hasAuthoritiesDefaults` property provides information on source authorities (and defaults for parameterized Tests).

BDQ details a convention for the structure and format of source authorities (in `bdqffdq:hasAuthoritiesDefaults` [bdqffdq:hasAuthoritiesDefaults](<../list/bdqffdq/index.md#bdqffdq_hasAuthoritiesDefaults> "Text describing bdqval:sourceAuthorities and bdqffdq:Parameters with their default values to attach to a bdqffdq:Specification to further specify the behavior described in the bdqffdq:hasExpectedResponse.")) as follows:

* **Convention One**: An authority with a URI providing information about the authority.
  * `“Fixed String Identifier” {\[URL\]}`

* Example: bdqval:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}
  * Fixed string identifier:  "The Getty Thesaurus of Geographic Names (TGN)" 
  * URI: {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}

* **Convention Two**: An authority with a URI providing information about the authority, and an API endpoint for checking values against the authority.
  * `“Fixed String Identifier” {\[URL\]}{API name\[URL of the API\]}`

* Example: bdqval:sourceAuthority default = "[ISO](<../../index.md#glossary_ISO> "[International Organization for Standarization.](https://www.iso.org/home.html)") 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}
  * Fixed string Identifier: "ISO 3166 Country Codes" (the name of the authority)
  * URI: {[https://www.iso.org/iso-3166-country-codes.html]}
  * API: {ISO 3166-1-alpha-2 Country Code search \[https://www.iso.org/obp/ui/#search\]}
    * A label for the API: "ISO 3166-1-alpha-2 Country Code search" 
    * An API endpoint: [https://www.iso.org/obp/ui/#search]

* **Convention Three**: An authority that is defined using a regular expression pattern.
  * `“Fixed String Identifier” {\[Regular Expression Pattern\]}`

* Example: bdqval:sourceAuthority default = "Regex present/absent" {["^(present|absent)$"]}
  * Fixed string identifier: "Regex present/absent" 
  * Regular Expression Pattern: "^(present|absent)$" (matches only the strings "present" or "absent" (the leading and trailing [{ enclose the pattern, but aren't part of it))

Regular expressions are a tool used in multiple programming languages. A regular expression is sequence of characters that defines a search pattern, often used for string matching, and thus can be used to evaluate whether a value conforms to a particular format.  

The source authority allows implementers to know where to look for the authoritative information that they need to run the Test. The source authority also allows users of the Test results to understand the basis for the Test's logic.  Critical to all three of these is the "Fixed String Identifier", this is a string that identifies the source authority, and will be expected to be embedded in code that implements Tests that take Parameters (which we will come back to shortly).  

For this Test, we can use the regular expression pattern for a resolvable ORCID ID as the source authority.

An ORCID ID is a unique identifier for researchers, and it has a specific format that can be expressed as a regular expression.  The expected format for an ORCID ID is a resolvable URL that starts with "http://orcid.org/" or "https://orcid.org/", followed by four groups of four digits, separated by hyphens, and ending with a single digit or the letter 'X'.  This can be expressed as the following regular expression: "^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$".  This regular expression matches strings that start with "http://" or "https://", followed by "orcid.org/", then four groups of four digits separated by hyphens, and ending with a single digit or 'X'.

Thus we could specify the source authority as follows:

* **hasAuthoritiesDefaults** bdqval:sourceAuthority default = "Resolvable ORCID ID regex" `{["^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"]}`
* **Expected Response**  INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of bdqval:sourceAuthority; otherwise NOT_COMPLIANT.

Which, combining the Expected Response with the default sourceAuthority, could be read by an implementer as: 
* INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty; 
* COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of "^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"
* otherwise NOT_COMPLIANT.

#### 6.7.2 Generalize, add a parameter (non-normative)

Some Tests have `Parameters`.  A Test with a `Parameter` will produce different results for the same input `Information Element` values, depending on the value of the parameter.  This allows for a single Test to be used in different contexts, with different expectations for how it will respond in certain conditions.  Parameters allow a Test to be generalized to serve a broader range of use cases, while still maintaining a clear and specific Test specification that can be implemented in a consistent way across different implementations.

We could make this Test more general by allowing for alternative authorities, and thus more broadly applicable, by adding a parameter to the Test that allows an implementer to specify which authority to use for evaluating whether the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID.  This would allow the Test to be used not just for ORCID IDs, but also for other types of identifiers that have a well-defined format and an authority that can be referenced for that format.

Parameters can include:

- Date ranges (e.g., bdqval:earliestValidDate)
- Thresholds (e.g., dwc:minimumElevationInMeters)
- Alternative source authorities
  * Alternative source authority vocabularies (e.g., taxonomic name authorities)
  * Alternative regular expression patterns for evaluating the format of identifiers.

BDQ allows for parameters where an local variant on a `Use Case` requires some locally accepted authority, distinct from a globally accepted authority that would apply to most applications of that `Use Case`.  This may be the case, for example, when legislation requires taxonomic names to be checked against a national names list, rather than a global names list.  In such cases, we can use parameters on a Test to allow for these variations in local needs, while still retaining the same overall logic and structure of the Test.

Note that IF there is only one source authority that everyone would use, such as an ISO format specified in a term definition, the source authority would not be accompanied by a parameter value, as there is no local need to generalize to. 

Some users may wish to store ORCID ID values with an ORCID: prefix, instead of the canonical https://orcid.org/ resolvable form, and thus we might want to allow for a parameter that allows for this variation in format.  This would be a parameter that allows for an alternative regex pattern to be used for evaluating the format of the ORCID ID, and when used, would change the behavior of the Test such that https://orcid.org/0000-0002-1825-0097 would be NOT_COMPLIANT while ORCID:0000-0002-1825-0097 would be COMPLIANT.  This would allow the Test to be used for datasets that use this alternative format for ORCID IDs, while still allowing the Test to be used for datasets that use the canonical resolvable form of ORCID IDs, without any change to the specification of the Test itself. 

* "Bare ORCID ID regex" `{[^ORCID:\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`

Other users might wish to allow for VIAF or other identifiers in wasAttributedTo, thus they could use the same Test, but with an implementation that supports a parameter value that encompasses their needs (e.g. "VIAF ID regex" `{[^https?://viaf\.org/viaf/\d+$]}`, or "VIAF or ORCID ID regex" `{[^https?://viaf\.org/viaf/\d+$|^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`), and thus they could use the same Test for their needs without any change to the specification of the Test itself.

Now the purpose of the “Fixed String Identifier” in the  source authority becomes clear.  These values are expected to to be embedded in code that implements parameterized Test, and that the presentation of these "Fixed String Identifier" values will allow different implementations of the same Test to recognize which parameter  to use.  For example, if an implementation of this Test is designed to allow for both the default regex for resolvable ORCID IDs and an alternative regex for ORCID IDs with the ORCID: prefix, then the implementation would look for the "Fixed String Identifier" in the source authority to determine which regex pattern to use for evaluating the format of the value in `prov:wasAttributedTo`.  If the "Fixed String Identifier" is "Resolvable ORCID ID regex", then the implementation would use the default regex pattern for resolvable ORCID IDs.  If the "Fixed String Identifier" is "Bare ORCID ID regex", then the implementation would use the alternative regex pattern for ORCID IDs with the ORCID: prefix.

We can make the bdqval:sourceAuthority as a parameter for this Test, meaning that users could supply different sourceAuthority values as parameters to change the behavior of a Test implementation to fit their specific local needs, while retaining the overall meaning and purpose of the Test.  Under the expectations of BDQ, all implementations must support the default parameter value.  A caveat, a brand new parameter value for a Test must be accompanied by implementation supporting that value, and not every implementation of the Test may support every proposed parameter.

* **Parameter** bdqval:sourceAuthority

See also:
- [Parameterizing the Tests](../guide/bdqtest/index.md#43-parameterizing-the-tests-normative) in the bdqtest: landing page.
- [Test Parameters](../guide/users/index.md#34-test-parameters-non-normative) in the Users Guide.
- [Test Parameters in Reports](../guide/users/index.md#341-test-parameters-in-reports-normative) in the Users Guide.

#### 6.7.3  Revisiting the Test Specification (non-normative)

Having asserted that a `bdqval:sourceAuthority` [bdqval:sourceAuthority](<../list/bdqval/index.md#bdqval_sourceAuthority> "An authority using the 'bdqval' namespace that provides a reference for values required for a Test evaluation. Where the Test is a bdqval:ParameterizedTest a bdqval:defaultSourceAuthority ('bdqval:sourceAuthority defaul…") is needed in the Test definition (and that the Test can take this as a parameter to allow for different implementations to use different authorities), we now need to revisit the `Description` and `Expected Response` to make sure that we have included this generalization.

* **Description** Does value in prov:wasAttributedTo conform to the format of the bdqval:sourceAuthority?
* **Expected Response**  INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of bdqval:sourceAuthority; otherwise NOT_COMPLIANT.

#### 6.7.4 Clarifying Related Concepts (non-normative)

The concept of `Source Authority` can blur several related ideas including the authority itself (e.g. ORCID documentation/registry) an implementation strategy (e.g. regex validation of a resolvable ORCID URL) and a fixed string identifier (e.g. "Resolvable ORCID ID regex") that is used to identify the authority and implementation strategy in code.  It is important to be clear about these related concepts when defining a Test with a `Source Authority`.  The values in `Source Authority` should distinguish between "what is authoritative" from "how you check it." from "what you call it in code".  For example, for this Test, we have:  

* **hasAuthoritiesDefaults** bdqval:sourceAuthority default = "Resolvable ORCID ID regex" `{["^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"]}`
* **Parameter** bdqval:sourceAuthority

* Authority: ORCID documentation 
* Fixed string identifier: "Resolvable ORCID ID regex"
* Default checking mechanism: regex for resolvable form of ORCID IDs
* Parameterization: allowing alternative acceptable forms
  * Alternative checking mechanism: regex for non resolvable form of ORCID IDs

Some Tests specify a `Source Authority` that is a controlled vocabulary which has a defined set of acceptable values and is also available at an API endpoint.

For example [VALIDATION_PHYLUM_FOUND](../terms/bdqtest/index.md#VALIDATION_PHYLUM_FOUND):

* **Expected Response** EXTERNAL_PREREQUISITES_NOT_MET if the bdqval:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdqval:Empty; COMPLIANT if the value of dwc:phylum is found as a value at the rank of Phylum in the bdqval:sourceAuthority; otherwise NOT_COMPLIANT
* **hasAuthoritiesDefaults** bdqval:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}
* **Parameters** bdqval:sourceAuthority

* Authority: GBIF Backbone Taxonomy
* Fixed string identifier: "GBIF Backbone Taxonomy"
* Default checking mechanism: API endpoint: [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]
* Parameterization: allowing alternative acceptable forms
  * Alternative checking mechanism: API endpoint for another taxonomic authority

### 6.8 Notes (non-normative)

Notes are present when some aspects of a Test may not be obvious to the casual user or implementer, or if we want to describe aspects of the behavior of the Test in a non-normative way. 
Notes might want to comment on variations in the expected structure of an ORCID ID, for example, the expected format of an ORCID ID is https://orcid.org/0000-0002-1825-0097, which can be tested for with this regular expression pattern: ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$

But we might or might not want to allow for http:// as well as https:// and allow a case error where x is used instead of X, and comment on the rationale for these decisions in the Notes. For example: 

* **Notes** The expected format of an ORCID ID is ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$, but we allow for protocol variants of http:// as well as https:// in the identifier and relax to the regex ^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$.  We expect the ORCID ID to be in resolvable form, not the bare identifier.  ORCID IDs are a subset of ISNI in the range 0000-0001-5000-0007 to 0000-0003-5000-0001, but this Test only evaluates the format, not the range.  The form ORCID:0000-0001-5000-0007 should be treated as NOT_COMPLIANT by this Test.

#### 6.8.1 Example Complex Implementation Notes (non-normative)

Notes are present when some aspects of a Test may not be obvious to the casual user or implementer. In some cases, Notes are not required, but Notes can be very helpful as in the example of the BDQ Test [VALIDATION_COUNTRYCODE_STANDARD](../list/bdqtest/index.md#bdqtest_0493bcfb-652e-4d17-815b-b0cce0742fbe):

> “Locations outside of a jurisdiction covered by a country code may
> have a value in the field dwc:countryCode, the ISO user defined codes
> include XZ used by the UN for installations on the high seas and
> suitable for a marker for the high seas. Also available in the ISO
> user defined codes is ZZ, used by GBIF to mark unknown countries. This
> test should accept both XZ and ZZ as COMPLIANT country codes. This
> test must return NOT_COMPLIANT if there is leading or trailing
> whitespace or there are leading or trailing [non-printing characters](<../../index.md#glossary_nonprinting_characters> "ASCII 0-32 and 127 decimal. Non-printing characters or formatting marks that are not displayed when printing. These may include pilcrow, space, non-breaking space, tab character, etc. For the purposes of the Tests they…").”

### 6.9 List the properties of the Test (non-normative)

So, our set of Test descriptors (the values of various bdqffdq: properties attached to instances of `Data Quality Need` subclasses, `Data Quality Method` subclasses, and `Specifications`) for this Test would be as follows:

* **Label** VALIDATION_WASATTRIBUTEDTO_STANDARD
* **Description** Does value in prov:wasAttributedTo conform to the format of the bdqval:sourceAuthority?
* **Preferred Label** "Validation prov:wasAttributedTo Standard".  
* **Term Name** {some UUID}
* **Modified** 2026-03-25
* **Test Type** Validation
* **Information Elements Acted Upon** prov:wasAttributedTo
* **Expected Response**  INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of the bdqval:sourceAuthority; otherwise NOT_COMPLIANT.
* **hasAuthoritiesDefaults** bdqval:sourceAuthority default = "Resolvable ORCID ID regex" `{[^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`
* **Parameter** bdqval:sourceAuthority
* **Notes** The expected format of an ORCID ID is ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$, but we allow for protocol variants of http:// as well as https:// in the identifier and relax to the regex ^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$.  We expect the ORCID ID to be in resolvable form, not the bare identifier.  ORCID IDs are a subset of ISNI in the range 0000-0001-5000-0007 to 0000-0003-5000-0001, but this test only evaluates the format, not the range.  The form ORCID:0000-0001-5000-0007 should be treated as NOT_COMPLIANT by this test.

#### 6.9.1 Summary of the Test Definition (non-normative)

VALIDATION_WASATTRIBUTEDTO_STANDARD is a `Validation` Test, that takes prov:wasAttributedTo as input, and asks the question "Does the value in prov:wasAttributedTo conform to the format of [a specified authority]?"  The expected response is COMPLIANT if there is a value in prov:wasAttributedTo and that value conforms to the expected format for an ORCID ID as defined by the default source authority; otherwise NOT_COMPLIANT.  If there is no value in prov:wasAttributedTo, then this Test cannot return a Response.result, and thus returns the Response.status INTERNAL_PREREQUISITES_NOT_MET.  This Test has a parameter for the source authority, allowing for different implementations to use different authorities for evaluating whether the value in prov:wasAttributedTo conforms to the expected format for different identifiers, while still retaining the same overall logic and purpose of the Test.

#### 6.9.2 Iterate (non-normative)

Earlier we said _"Treat this `Use Case` definition (and everything else that follows from it) as a first draft."_

This is a critical point in the process. We have now defined Tests that fill gaps in our `Use Case`, and we have defined these Tests in a way that is consistent with the principles of BDQ, and we have provided detailed specifications for these Tests.  However, we have not yet implemented these Tests, or thrown any real data at these Tests to see how they respond.  Thus, we should treat this as a first draft of the `Use Case` and Test definitions, and be prepared to iterate on these definitions based on implementation feedback and real-world data.

## 7 Implementation, Conformance Testing, and Community Feedback (The "real-world") (non-normative)

*No Test is final until it is implemented and thrown at actual data to confirm it responds correctly.*

### 7.1 Implementation (non-normative)

A Test specification may sound perfectly clear and straightforward to its writers, but it may not be clear to developers who are trying to implement the Test based on the specification.  In BDQ, the decision logic of a Test is expressed in the `hasExpectedResponse` and `hasAuthoritiesDefaults` properties of its `Specification`.  The only way to confirm that a Test specification is clear and can be implemented correctly is to actually implement the Test based on the specification, and then throw real data at that implementation to see if it responds correctly.  Expect that an initial Test specification will need revision based on questions raised in implementation and on testing the behavior of the implementation against real world data.

BDQ is deliberately agnostic about programming languages and execution frameworks for Test implementations.

A BDQ Test implementation is expected to have a consistent scope and API shape across languages:

* Inputs: the `Information Element(s)` `Acted Upon` (and any `Consulted` values if needed), plus optional `Parameter(s)` (e.g., `bdqval:sourceAuthority`).
* Logic (decision rules): evaluate the clauses in the specification (`hasExpectedResponse`) in order, returning the first matching outcome (handling EXTERNAL_PREREQUISITES_NOT_MET via exception/error handling where appropriate).  
* Output: exactly one structured Response per run, always providing a `Response.status` and a `Response.comment`, and providing a `Response.result` only when `Response.status` indicates a result (typically RUN_HAS_RESULT).

We use a shorthand for the set of properties associated with a `Response` that are produced by running a Test.  A `Response` carries `Response.status`, `Response.result`, and `Response.comment` properties (see [Structure of Response](../guide/bdqtest/index.md#41-structure-of-response-normative) in the bdqtest: landing page).

BDQ keeps Tests portable by standardizing semantics (inputs, decision rules, outputs), but it leaves binding of raw data inputs to `Information Elements` and execution mechanics (orchestration of test execution) to whatever framework fits the implementer's environment.  This means that the behavior of the implementation of an individual Test should be tested in isolation, presenting the Test with known inputs, and confirming that the Test produces the expected outputs based on the logic of the decision rules in the specification.  This means that Test conformance testing is expected to be performed on the level of individual Test implementations.

See also: 
* [Responsibilities of a Test](../guide/implementers/index.md#651-responsibilities-of-a-test-non-normative) in the implementers guide.
* [Responsibilities of a Test Execution Framework](../guide/implementers/index.md#66-responsibilities-of-a-test-execution-framework-non-normative) in the implementers guide.

### 7.2 Conformance Testing Data and exposing Assumptions (non-normative)

Conformance testing data that provides the expected outputs from a Test for a variety of inputs, including edge cases is an integral part of the process of confirming that a Test implementation is correct and behaves as expected, but also in developing a clear and unambiguous Test specification.

The description and specification of a Test may involve hidden assumptions by those who defined the Test.  Conformance testing data provided by more than one person, especially if those people have different perspectives and examples of the data being evaluated by the Test can help to expose these assumptions.  For example, if the Test specification includes a clause that says "COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID", there may be a hidden assumption that the expected format for an ORCID ID is only the canonical resolvable form of ORCID IDs (e.g. https://orcid.org/0000-0002-1825-0097), but some users may have data with ORCID IDs in a different format (e.g. ORCID:0000-0002-1825-0097), and they may have an assumption that this the expected format for an ORCID ID.  If multiple people provide conformance testing data, it is likely to includes examples of both formats.  Testing can thus expose these assumptions and feedback to clarification of the Test specification to make it clear which formats are expected to be COMPLIANT and which are expected to be NOT_COMPLIANT.  Expect that the Test specification will need revision based on questions raised in implementation and on testing the behavior of the implementation against real world data, and that this process will be iterative until the Test specification is clear and unambiguous, and Test implementations behave as expected when presented with a variety of test cases, including edge cases.

See also: 
* [Conformance Testing Implementations](../guide/implementers/index.md#8-conformance-testing-implementations-normative) in the implementers guide.
* [Structure of Response](../guide/bdqtest/index.md#41-structure-of-response-normative) in the bdqtest: landing page.

#### 7.2.1 Unit Tests (non-normative)

When implementing a Test, implementors are encouraged to use a test-driven development approach, where they first create unit tests for a Test implementation covering each expected path in the specification, as well as edge cases, and then implement the Test internals to pass those unit tests.  This strategy helps ensures that the Test is implemented correctly and that it responds correctly to a variety of test cases, including edge cases.  

Unit tests, however, are integral parts of the code base for a test implementation and thus do not provide a basis for confirming that different test implementations in different languages behave in the same ways when presented with identical inputs.  An implementation independent conformation testing dataset is needed for this purpose.

#### 7.2.2 Data for Conformance Testing and Edge Cases (non-normative)

The documentation of a Test should include conformance testing data.  Such conformance testing data should provide inputs for a Test, and for each input, the expected outputs.  Such a conformance testing dataset can be used to validate that any implementation of the Test is responding as expected. 

An implementation of a Test then needs to be connected to a conformance testing harness that can read the example data for each Test, present the Test with the specified inputs, and confirm that the outputs from the Test match the expected outputs for those inputs.  This is a critical step in confirming that a Test implementation is correct and behaves as expected, and it is also a critical step in confirming that different implementations of the same Test in different languages behave in the same way when presented with identical inputs.  It would also be possible to frame conformance testing data that has the same structure as the expected inputs for a `Use Case`, but such data are much harder to produce in a way that evaluates conformance of individual decision paths within individual Tests in isolation, and thus it is more difficult to use such data to confirm that individual Tests are behaving as expected.  If such integration test data include synthetic values, they should be marked so as to be clearly distinguishable from actual data. 

See also: [Guide to Marking and Identifying Synthetic and Modified Data](../guide/synthetic/index.md)

##### 7.2.2.1 Example Conformance Testing Data (non-normative)

Consider the Test [VALIDATION_COUNTRYCODE_STANDARD](../terms/bdqtest/index.md#VALIDATION_COUNTRYCODE_STANDARD), which evaluates whether the value in dwc:countryCode is a valid ISO 3166-1-alpha-2 country code.  

* **Expected Response**  EXTERNAL_PREREQUISITES_NOT_MET if the bdqval:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdqval:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdqval:sourceAuthority; otherwise NOT_COMPLIANT
* **Source Authority** bdqval:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}
* **Notes** Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and recommended in Darwin Core to designate the high seas. Also available in the ISO user defined codes is ZZ, used by Darwin Core and GBIF to mark unknown countries. This Test should accept both XZ and ZZ as COMPLIANT country codes. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

The conformance testing dataset that accompanies the BDQ implementer's guide includes these following (and other) rows for this Test:

| Label | dwc:countryCode | Response.status | Response.result | Response.comment |
| --- | --- | --- | --- | --- | --- |
| VALIDATION_COUNTRYCODE_STANDARD |  | INTERNAL_PREREQUISITES_NOT_MET |  | dwc:countryCode is bdqval:Empty | 
| VALIDATION_COUNTRYCODE_STANDARD | GL | RUN_HAS_RESULT | COMPLIANT | dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value | 
| VALIDATION_COUNTRYCODE_STANDARD | GRL | RUN_HAS_RESULT | NOT_COMPLIANT | dwc:countryCode is not a valid ISO (ISO 3166-1-alpha-2 country codes) value | 
| VALIDATION_COUNTRYCODE_STANDARD | XZ | RUN_HAS_RESULT | COMPLIANT | dwc:countryCode is a valid code for high seas taken from UN/Locode | 
| VALIDATION_COUNTRYCODE_STANDARD | Austria | RUN_HAS_RESULT | NOT_COMPLIANT | dwc:countryCode is not a valid ISO (ISO 3166-1-alpha-2 country codes) value  | 
| VALIDATION_COUNTRYCODE_STANDARD | ZZ | RUN_HAS_RESULT | COMPLIANT | dwc countryCode is a user- defined ISO 2-letter country code | 

The columns shown here are the human readable identifier (Label) for the Test, the input value for the Information Element being evaluated (dwc:countryCode), and the expected outputs for the Test for that input value (`Response.status`, `Response.result`, and `Response.comment`).  Not shown here, but quite important, are columns for the machine readable identifier for a Test (Term Name) to allow a conformance testing harness to connect the test data to the correct Test implementation, and the DataID column identifying a particular conformance test case to facilitate discussion of specific conformance failure cases.

This conformance testing data includes edge cases such as an empty value for dwc:countryCode, a valid ISO 3166-1-alpha-2 country code, some cases that are not 2 letter country codes, and edge cases taken from the notes: a valid code for high seas taken from UN/Locode, and the user-defined ISO 2-letter country code ZZ.  

See also: 
[VALIDATION_COUNTRYCODE_STANDARD](../list/bdqtest/index.md#bdqtest_0493bcfb-652e-4d17-815b-b0cce0742fbe) in the bdqtest: term-list document.
[High Seas](../supplement/index.md#394-high-seas-non-normative) in the Supplement.

##### 7.2.2.2 Conformance testing data for our proposed VALIDATION_WASATTRIBUTEDTO_STANDARD Test (non-normative)

A possible set of conformance testing data for our proposed `VALIDATION_WASATTRIBUTEDTO_STANDARD` Test are below: 

* **Expected Response**  INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of the bdqval:sourceAuthority; otherwise NOT_COMPLIANT.
* **hasAuthoritiesDefaults** bdqval:sourceAuthority default = "Resolvable ORCID ID regex" `{[^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`

| Label | prov:wasAttributedTo | Response.status | Response.result | Response.comment |
| --- | --- | --- | --- | --- |
| VALIDATION_WASATTRIBUTEDTO_STANDARD |  | INTERNAL_PREREQUISITES_NOT_MET |  | prov:wasAttributedTo is bdqval:Empty |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | `   ` | INTERNAL_PREREQUISITES_NOT_MET |  | prov:wasAttributedTo is bdqval:Empty (whitespace only) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-0007 | RUN_HAS_RESULT | COMPLIANT | prov:wasAttributedTo matches expected resolvable ORCID ID format (^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | http://orcid.org/0000-0001-5000-0007 | RUN_HAS_RESULT | COMPLIANT | prov:wasAttributedTo matches expected resolvable ORCID ID format allowing http:// as well as https:// |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0002-1825-0097 | RUN_HAS_RESULT | COMPLIANT | prov:wasAttributedTo matches expected resolvable ORCID ID format (format only; range not evaluated) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | ORCID:0000-0001-5000-0007 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo is not in resolvable URL form (expected http(s)://orcid.org/...) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | 0000-0001-5000-0007 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo is not in resolvable URL form (bare identifier not allowed) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-0007/ | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (trailing slash not allowed by regex) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-0007?foo=bar | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (query string not allowed by regex) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-00070 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (extra digit at end) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-000X | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (final group must be 3 digits plus [0-9X]) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-0007X | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (unexpected extra character) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-0007  | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (trailing whitespace not allowed) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD |  https://orcid.org/0000-0001-5000-0007 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (leading whitespace not allowed) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | HTTPS://orcid.org/0000-0001-5000-0007 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (scheme is case-sensitive in this regex) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://ORCID.org/0000-0001-5000-0007 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (host is case-sensitive in this regex) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-0007#fragment | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (fragment not allowed by regex) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://orcid.org/0000-0001-5000-000 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (too short) |
| VALIDATION_WASATTRIBUTEDTO_STANDARD | https://example.org/0000-0001-5000-0007 | RUN_HAS_RESULT | NOT_COMPLIANT | prov:wasAttributedTo does not match expected format (wrong domain; expected orcid.org) |

Some of these test cases are "edge cases" that might not be immediately obvious to an implementer or the person who defined a test, such as:
* The value in prov:wasAttributedTo is whitespace only.
* There is a trailing slash at the end of the ORCID ID.
* There is a query string at the end of the ORCID ID.
* There is an extra digit at the end of the ORCID ID.
* The scheme for the ORCID ID is http instead of https.
* There is an unexpected extra character at the end of the ORCID ID.
* There is leading or trailing whitespace around the ORCID ID.
* There is a fragment at the end of the ORCID ID.

These edge cases are important to include in the conformance testing dataset because they help ensure that an implementation of this Test will produce the expected outputs for these cases and not produce false positives or false negatives.  

Some of these test cases also highlight hidden assumptions in our Test specification, in particular, the assumption that the scheme in the ORCID ID is case-sensitive and the assumption that the host in the ORCID ID is case-sensitive.  By including these edge cases in our conformance testing dataset, we can confirm that our Test specification is clear about these assumptions and that implementations of this Test will correctly handle these cases.

Since the scheme (https) and host (orcid.org) in the ORCID ID are technically case-insensitive according to the URI specification, but our regex pattern is case-sensitive, we need to be clear in our Test specification and in our conformance testing data that we are expecting the scheme and host to be in lowercase, and that if they are not, then the Test should return NOT_COMPLIANT.  The case insensitivity scheme and host in the URI specification may well also mean that we want to revisit our regex pattern to allow for case-insensitivity in the scheme and host.  This is an example of a "pitfall for the naive" when defining a Test.

So, we might want to relax the default regex pattern to allow for case-insensitivity in the scheme and host, and thus we might want to change our default `Source Authority`:

* From: **hasAuthoritiesDefaults** bdqval:sourceAuthority default = "Resolvable ORCID ID regex" `{[^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`
* To: **hasAuthoritiesDefaults** bdqval:sourceAuthority default = "Resolvable ORCID ID regex" `{[^(?i:http(s){0,1}://orcid\.org/)\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`

And then change the conformance testing data accordingly to reflect this change in the expected format for a compliant ORCID ID (so that the "HTTPS://orcid.org" and "https://ORCID.org" would be COMPLIANT).  Similarly, two resolvable identifiers with different schemes (e.g. http://orcid.org/0000-0001-5000-0007 and https://orcid.org/0000-0001-5000-0007) are technically identifiers for different resources, and careful consideration of whether the the regex should allow for either http or https may be needed.

Note, that when evaluating whether a Test implementation responds as expected to a given input, the `Response.status` and `Response.result` must be exact matches, but the `Response.comment` in the response needs to be bdqval:NotEmpty.  The `Response.comment` in the conformance testing data provides a general guide to implementers for what the comment could say for a given input, but more importantly provides documentation and explanation for that particular case.

##### 7.2.2.3 Enumerating Test Conformance Data (non-normative)

**Purpose**: Ensure that a Test can be correctly implemented, and that the Test specification is clear, unambiguous, and has logic that handles real world data and edge cases.

The only way to validate a Test is to implement it and then throw sufficient examples of data at that Test to confirm that it responds as expected, and that the Test specification is a good fit to real world data.

**Minimal Starting point:** One validation case for each clause in the `Expected Response`.

The `Expected Response` "INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of bdqval:sourceAuthority; otherwise NOT_COMPLIANT." can be read as the following three clauses, to be evaluated in order:

1. INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty; 
1. COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of "^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"
1. otherwise NOT_COMPLIANT.

For clause 1, we would want to include at least one test case where prov:wasAttributedTo is bdqval:Empty, and the expected response is INTERNAL_PREREQUISITES_NOT_MET.  For clause 2, we would want to include at least one test case where prov:wasAttributedTo conforms to the expected format for an ORCID ID, and the expected response is COMPLIANT.  For clause 3, we would want to include at least one test case where prov:wasAttributedTo does not conform to the expected format for an ORCID ID, and the expected response is NOT_COMPLIANT.

* A test case for clause 1 `INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdqval:Empty;`:
  * Test Label: VALIDATION_WASATTRIBUTEDTO_STANDARD
  * prov:wasAttributedTo: 
  * Response.status: INTERNAL_PREREQUISITES_NOT_MET
  * Response.result:  
  * Response.comment: prov:wasAttributedTo is bdqval:Empty, so its format cannot be evaluated.

* A test cases for clause 2 `COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of "^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"`:
  * Test Label: VALIDATION_WASATTRIBUTEDTO_STANDARD
  * prov:wasAttributedTo: https://orcid.org/0000-0001-5000-0007 
  * Response.status: RUN_HAS_RESULT
  * Response.result: COMPLIANT 
  * Response.comment: prov:wasAttributedTo matches expected resolvable ORCID ID format (^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$)

* A test case for clause 3 `otherwise NOT_COMPLIANT`:
  * Test Label: VALIDATION_WASATTRIBUTEDTO_STANDARD 
  * prov:wasAttributedTo: https://orcid.org/0000-0001-5000-0007/ 
  * Response.status: RUN_HAS_RESULT
  * Response.result: NOT_COMPLIANT
  * Response.comment: prov:wasAttributedTo does not match expected format (trailing slash not allowed) 

That is just a starting point, to create comprehensive test data covering all decision paths in the `Expected Response` split the `Expected Response` into separate clauses, then: 

* Add a pass and fail test case for each clause.
* Examine the Test notes for any discussion of special cases and add test cases for each of those.
* Look at a the distribution of real values of data in the wild and add additional test cases, particularly for unusual values.
  * Valid compliant data.
  * Malformed data.
  * Missing or empty values.
  * Edge cases (leading or trailing whitespace on data, very large numbers, very small numbers, zero, etc)
  * Boundary conditions (e.g., for a test that evaluates whether a number is between 1 and 10, include test cases for 1, 10, and values just outside the boundaries like 0.999 and 10.001)
* Optionally include cases for non-default parameter values if the Test has parameters.

Consideration of all of these will help ensure comprehensive coverage of the Test decision path for both inputs that are likely to be encountered and edge cases.

**Critical Thinking:** Both those defining a Test and those implementing it must consider "pitfalls for the naive".  The domain experts defining a Test are likely to perceive a different set of pitfalls from developers implementing a Test.  Multiple iterations and a conversation mediated by Test conformance Testing data is necessary for developing a robust Test description and specification (`Description`, `Information Elements`, `hasAuthoritiesDefaults`, `hasSourceAuthority`, and `Parameters`) 

See also: 
* [Conformance Testing Implementations](../guide/implementers/index.md#8-conformance-testing-implementations-normative) in the BDQ Implementer's Guide.

### 7.4 Execution Frameworks (non-normative)

The BDQ Test specifications (the Specification text in bdqffdq:hasExpectedResponse, plus any Parameters/defaults) are execution framework agnostic because they define only:

* What inputs are required (the `Information Elements` `Acted Upon` and `Consulted`, and any `Parameter` values),
* What outputs must be produced (a structured `Response` with `Response.status`, `Response.result`, `Response.comment`), and
* What decision logic must be followed (evaluate the criteria blocks in the `hasExpectedResponse` in order and return the first applicable response),

…but they do not constrain:

* How data are stored (RDBMS, CSV, JSON, RDF, objects) or accessed.
* How records are streamed/batched/parallelized in a workflow.
* What programming language(s) are used.
* How methods are discovered/invoked (reflection, registry, function pointers, workflow nodes).
* How Responses are serialized/persisted (objects, rows, RDF `bdqffdq:Response` [bdqffdq:Response](<../list/bdqffdq/index.md#bdqffdq_Response> "A bdqffdq:ReportConcept produced by a bdqffdq:Implementation expressing a statement about data quality resulting from the application of the logic of a bdqffdq:Specification to a bdqffdq:DataResource."), annotations).
* How Responses are presented to users or downstream processes (logs, dashboards, annotations).

#### 7.4.1 What an execution framework must do between raw data and a Test implementation (non-normative)

A framework’s job is to act as the “adapter layer” that turns heterogeneous input into the canonical inputs/outputs implied by the ontology and the Test descriptors:

* Select the scope / unit of execution
  * Decide what constitutes a `Single Record` (e.g., one Simple Darwin Core row; one `dwc:Occurrence` graph root) or a `Multi Record` (a dataset), and iterate accordingly.

* Bind raw data to the Test API
  * Map raw fields/properties onto the Test’s `Information Elements`:
    * provide the value(s) for the `Acted Upon` term(s),
    * provide any `Consulted` term(s),
    * supply `Parameter` argument values (or omit them and let defaults apply).
  * This is the core “plumbing” step: e.g. ensure `dwc:countryCode` actually lands in the method parameter that represents `dwc:countryCode`, etc. 
	* This mapping could be via annotations, configuration, naming conventions, or explicit mapping code.
	* The FilteredPush implementations use Java Annotations for this purpose, but other frameworks are free to use different approaches.

* Invoke the correct implementation
  * Locate the right Implementation for a given Test (e.g., by Label, [GUID](<../../index.md#glossary_GUID> "Globally Unique Identifier. In this document, the GUID for a Test is a UUID (128-bit universally unique identifier) which identifies the Test.")/Term Name, or versioned IRI), then call it with the bound inputs.

* Capture and normalize outputs into a `Response`
  * Ensure every execution yields exactly one structured `Response` with:
    * `Response.status` from the controlled vocabulary (e.g. RUN_HAS_RESULT, EXTERNAL_PREREQUISITES_NOT_MET),
    * `Response.result` as required by status and `Test Type`, and
    * a `Response.comment` that is `bdqval:NotEmpty`.
  * Optionally wrap/serialize as RDF assertions (`bdqffdq:Response`) or as W3C Annotations, as that representation choice is outside the Test itself.

* Present results to users and/or downstream processes
  * This could be as simple as logging, or as complex as a dashboard or API response (e.g., BDQEmail). 
  * BDQ is explicitly agnostic about this presentation layer.

* Manage common cross-cutting concerns
  * caching and retry for external authorities.
  * concurrency/parallel execution.
  * attaching Responses back to records.

In short: BDQ keeps Tests portable by standardizing semantics (inputs, decision rules, outputs), while leaving execution mechanics (binding, orchestration, serialization) to whatever framework fits the implementer’s environment.

See also: 
* [Responsibilities of a Test](../guide/implementers/index.md#651-responsibilities-of-a-test-non-normative) in the implementers guide.
* [Responsibilities of a Test Execution Framework](../guide/implementers/index.md#66-responsibilities-of-a-test-execution-framework-non-normative) in the implementers guide.

## 8 Use an implementation for Quality Control (non-normative)

So, for our `Use Case` **Validated Distribution Authority** we have identified a set of specific Tests to evaluate whether some dataset is fit for the purpose of being used as a "validated distribution authority" for biodiversity science.  

The Fitness For Use Framework is designed to support two different but related purposes: `Quality Control` and `Quality Assurance`.  `Quality Control` is the process of finding and fixing errors in a dataset, while `Quality Assurance` is the process of filtering a dataset down to a subset of records that are fit for some purpose.  

Implicit in our `Use Case`, and we will want to spell this out explicitly (again, iterate), is that, in this **Validated Distribution Authority** `Use Case`, we want to use the results of Tests to find and fix errors in a dataset, thus improving the quality of the dataset for this purpose, that is, our `Use Case` is focused on `Quality Control`. 

The formal mechanism that the Fitness For Use Framework provides to support both `Quality Control` and `Quality Assurance` is the use of `Multi Record` `Measures`.  These `Multi Record` `Measures`  take as input the output results from `Single Record` Tests over multiple records, and combine those results in some way to produce a measure of the quality of the dataset as a whole for some purpose.  For example, we could have a `Multi Record` `Measure` that takes the results of the VALIDATION_FOOTPRINTWKT_NOTEMPTY Test for all records in a dataset, and counts the number of records that are NOT_COMPLIANT with that Test, combining this count with the number of records in the dataset gives us a measure of how many records are missing values in the `dwc:footprintWKT` field in that dataset.  

Both `Quality Control` and `Quality Assurance` rely on an examination of the results of `Single Record` Tests, but they use those results in different ways.

It is important to recognize that BDQ does not standardize full `Quality Control` or `Quality Assurance` workflows; it standardizes the semantics of Tests and their Responses and provides `Measure` patterns to support `Quality Control` and `Quality Assurance` workflows.  

In listing a set of `Validations` for our `Use Case`, we are setting a `ValidationPolicy` for the `Use Case`.  A `ValidationPolicy` is the set of `Validations` that are relevant to a particular `Use Case`.   A `Use Case` also has an `AmendmentPolicy` (the set of `Amendments` that are relevant to that `Use Case`) and a `MeasurementPolicy` (the set of `Measures` that are relevant to that `Use Case`), and an `IssuePolicy` (the set of `Issues` that are relevant to that `Use Case`).  The set of Tests associated with a `Use Case` in its `Policies` can be referred to as a Test suite.

Informally, to perform `Quality Control` we could run the set of `Validation` Tests in the `ValidationPolicy` for our `Use Case`, and simply examine the outputs for NOT_COMPLIANT `Response.result` values, and then locate and fix those problems in the dataset.  BDQ does not constrain how we do that examination and remediation, but it does provide a standard way to report the results of those `Validations` (the `Data Quality Report`), and it provides a standard way to summarize those results across records in the dataset (the `Multi Record` `Measures`) to help us prioritize and track our `Quality Control` efforts. 

For our **Validated Distribution Authority** `Use Case` we would likely wish to define one or more `Amendment` Tests to propose changes to fix problems identified by the `Validations` that are relevant to that `Use Case`, but we won't explore these here.  Instead, we will focus on the `Multi Record` `Measures` that we would want to use to evaluate the quality of a dataset for this `Use Case`, and to track improvements in that quality as we find and fix errors in the dataset.

See also:
- [Quality Control and Quality Assurance](../guide/users/index.md#21-quality-control-and-quality-assurance-non-normative) in the User's Guide.
- [Single Record and MultiRecord Tests](../guide/bdqtest/index.md#35-single-record-and-multi-record-tests-non-normative) in the BDQ Tests: Concepts and Use document.
- [Data Quality Control and Data Quality Assurance](../guide/bdqffdq/index.md#221-data-quality-control-and-data-quality-assurance-non-normative) in the Fitness For Use Framework Ontology: Concepts and Use document.

### 8.1 MultiRecord Measures for Quality Control (non-normative)

The `Use Case` we have been working with in this tutorial is focused on `Quality Control` (we want to fix problems in a dataset of distributions that would itself be used to evaluate other datasets), so we will examine how the Fitness For Use Framework supports using the results of `Single Record` Tests for that purpose.

This tutorial has focused on defining `Single Record` Tests (primarily `Validations`) that evaluate one record at a time. In practice, `Quality Control` almost always requires a dataset-level view: curators, data managers, and developers need to know **how prevalent** a particular problem is, **where** it occurs, and **whether** proposed changes would measurably improve fitness for a `Use Case`.

In the BDQ Fitness For Use Framework, that dataset-level view is provided by `Multi Record` `Measures` (`bdqffdq:Measure` [bdqffdq:Measure](<../list/bdqffdq/index.md#bdqffdq_Measure> "A bdqffdq:DataQualityNeed that expresses how the fitness of data for some use may be measured.") with resource type `bdqffdq:MultiRecord` [bdqffdq:MultiRecord](<../list/bdqffdq/index.md#bdqffdq_MultiRecord> "A set of one or more bdqffdq:SingleRecords.")). These `Measures` operate over the collection of `Responses` produced by running one or more `Single Record` Tests across all records in a dataset, and they return a **single summary value** in `Response.result` (either a single number, or one of `COMPLETE`/`NOT_COMPLETE`).

Before we focus on `Multi Record` `Measures`, it is helpful to distinguish three common patterns of `Measures` in BDQ:

- `Single Record` `Measures` that directly measure an `Information Element` value and return a metric (e.g., [MEASURE_EVENTDATE_DURATIONINSECONDS](../terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS)).
- `Single Record` `Measures` that summarize outcomes of other `Single Record` Tests on the same `Single Record` (e.g., `MEASURE_AMENDMENTS_PROPOSED`).
- `Multi Record` `Measures` that take the outputs of `Single Record` Tests as their inputs and return metrics or filters across a dataset (e.g., [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](../terms/bdqtest/index.md#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT)).

The remainder of this section focuses on `Multi Record` `Measures` that take the output of other Tests as their input, because such `Measures` are central to practical `Quality Control` workflows on datasets.

#### 8.1.1 What a MultiRecord Measure takes as input (non-normative)

A `Multi Record` `Measure` does not typically examine raw input (e.g. Darwin Core) values directly. Instead, it uses as input the outputs of `Single Record` Tests — the set of Responses with their `Response.status`, `Response.result`, and `Response.comment`.   `Multi Record` `Measures` can also be defined to take raw data as input, for example, a `Multi Record` `Measure` could be defined to calculate the average dwc:individualCount across all records in a dataset, but we won't consider that use of `Multi Record` `Measures` here.

Conceptually what we want to do with `Multi Record` `Measures` is:

1. Choose a `Use Case` (e.g., "Validated Distribution Authority"), and from the `ValidationPolicy` that relates the `Use Case` to `Validations`, identify the `Single Record` `Validation` Tests for that `Use Case`.
2. Run the relevant `Single Record` `Validation` Tests over all records in the dataset.
3. Collect the resulting `Responses`.
4. Run one or more `Multi Record` `Measures` that take these `Responses` as input to summarize how many quality issues exist where in the dataset.
   * If there are only a small number of problems, we can fix them, and repeat the process to confirm that the fixes worked.
   * If there are a large number of problems, we can use the `Multi Record` `Measures` to prioritize which problems to fix first, that is identify where to focus effort for improving the data quality for the `Use Case`.
5. Act upon the results of those `Multi Record` `Measures` to prioritize and direct `Quality Control` efforts (or filter records for `Quality Assurance`).

This separation on `Resource Type` (`Single Record` or `Multi Record`) is important: it keeps each `Single Record` Test atomic and easy to implement, while providing a consistent, standards-aligned way to summarize results for dataset-level decision making.

See also [Framework Competency Questions](../supplement/index.md#24-framework-competency-questions-non-normative) in the Supplement for examples of sparql queries that select the set of `Single Record` `Validations` associated by `Policy` with a `Use Case`.

#### 8.1.2 Two common patterns of MultiRecord Measures (non-normative)

BDQ includes (and encourages) two practical patterns of `Multi Record` `Measures`:

**(A) Counts / prevalence measures (numeric results)**  
These return a single number, such as the count of records that are `COMPLIANT`, `NOT_COMPLIANT`, or have `INTERNAL_PREREQUISITES_NOT_MET` for a particular `Single Record` Test.

These are particularly useful for `Quality Control` because they let you:

- quantify the scale of a problem (e.g., “how many records are missing `dwc:footprintWKT`?”)
- prioritize work (fix the highest-impact problems first)
- track improvement over time (before/after a cleanup project, or between data releases)

**(B) Completeness-as-fitness measures (`COMPLETE` / `NOT_COMPLETE`)**  
These return `COMPLETE` if the dataset meets a dataset-level requirement derived from `Single Record` Test outcomes, and `NOT_COMPLETE` otherwise.

While these measures are central to formal `Quality Assurance` filtering, they can also support `Quality Control` by providing a clear “done/not done” indicator for a dataset with respect to a selected `Use Case` and its included Tests.

#### 8.1.3 Interpreting MultiRecord measures under Quality Control (non-normative)

A key idea in `Quality Control` is that dataset-level metrics should be interpreted in the context of the `Use Case`:

- A low count of `COMPLIANT` outcomes for a critical `Validation` indicates a major barrier to fitness for that `Use Case`.
- A high count of `INTERNAL_PREREQUISITES_NOT_MET` often points to upstream data capture or mapping gaps (e.g., a term not supplied at all, or supplied inconsistently).
- Changes in counts between a “pre-amendment” and “post-amendment” phase provide an estimate of how much quality could improve if proposed `Amendments` were accepted (or implemented by a curator).

Because `Multi Record` `Measures` return only a single value, they are often paired with reporting or visualization outside of the Framework (e.g., spreadsheets, dashboards, or issue lists) that link summary counts back to the specific records needing attention.

See also: [Phases: Pre-Amendment, Amendment, Post-Amendment](../guide/implementers/index.md#641-phases-pre-amendment-amendment-post-amendment-normative) in the implementers guide for a discussion of "pre-amendment" and "post-amendment" phases in a `Quality Control` workflow.

#### 8.1.3.1 Contrast with Quality Assurance (non-normative)

In contrast, in `Quality Assurance`, the focus is on filtering records based on `Single Record` Test outcomes.  The mechanism for this in the Fitness For Use Framework is to define a `Multi Record` `Measure` that returns `COMPLETE` if the dataset meets a dataset-level requirement derived from `Single Record` Test outcomes, and `NOT_COMPLETE` otherwise, and if `NOT_COMPLETE`.  This `Multi Record` `Measure` can be used as a completeness condition.  A `Quality Assurance` workflow may filter records until the remaining dataset satisfies that condition (the `Measure` returns `COMPLETE`).  When all the `Multi Record` `Measures` of this sort for a `Use Case` (as specified by `Policy`) are `COMPLETE`, the (filtered) dataset is fit for use with respect to the selected `Use Case`.  Alternately, remediation could be applied (as in applying `Amendments` to fix problems identified by `Validations`) and filtering such that the `Multi Record` `Measures` return `COMPLETE`, at which point the dataset is fit for use with respect to the selected `Use Case`.  BDQ does not specify a workflow, it fundamentally supports the representation of completeness conditions via `Multi Record` `Measures`, and it is up to implementers to decide how to use those `Measures` in a workflow, whether for `Quality Control` or `Quality Assurance`.  BDQ defines how to represent `Quality Assurance` conditions and outcomes. A filtering or remediation strategy is outside the scope of BDQ and would be up to an implementation.

A related pattern occurs at the `Single Record` level: when fitness depends on a user-defined analytical threshold rather than a single universal rule, a `Single Record` `Measure` may return a numeric metric that consumers interpret relative to their `Use Case`. For example, [MEASURE_EVENTDATE_DURATIONINSECONDS](../terms/bdqtest/index.md#MEASURE_EVENTDATE_DURATIONINSECONDS) returns the duration (in seconds) of the time interval represented by `dwc:eventDate`; consumers can then apply a threshold (e.g., “duration ≤ 86401 seconds” for day-level precision) to decide whether an individual `Single Record` has sufficient temporal precision for their `Use Case`.

#### 8.1.4 A worked example (building on VALIDATION_FOOTPRINTWKT_NOTEMPTY) (non-normative)

Suppose we run the `Validation` Test `VALIDATION_FOOTPRINTWKT_NOTEMPTY` on a dataset (`Multi Record`) of 10,000 records.

A `Quality Control` workflow commonly uses `Multi Record` `Measures` to summarize how often the underlying `Single Record` `Validation` produced each outcome. For a simple NotEmpty `Validation`, two prevalence-style measures are typically sufficient:

- A `Multi Record` `Measure` that counts records where `Response.status=RUN_HAS_RESULT` and `Response.result=COMPLIANT` for `VALIDATION_FOOTPRINTWKT_NOTEMPTY` (records where `dwc:footprintWKT` is present).
- A `Multi Record` `Measure` that counts records where `Response.status=RUN_HAS_RESULT` and `Response.result=NOT_COMPLIANT` for `VALIDATION_FOOTPRINTWKT_NOTEMPTY` (records where `dwc:footprintWKT` is empty).

These summary counts are useful in `Quality Control` because they quickly show the *prevalence* of a specific quality issue (here: missing spatial footprints), and they support prioritization and tracking of improvements over time (for example, comparing a baseline run to a run after a targeted data cleanup or a mapping fix).  Values like percentages would be computed outside the Framework (unless you define separate Measures for them).

Depending on how your Test suite is designed, `Multi Record` `Measures` that count `Validations` with `Response.status=INTERNAL_PREREQUISITES_NOT_MET` may be less informative than counts of `COMPLIANT` and `NOT_COMPLIANT` results from other (e.g. `NotEmpty`, `Standard`, or `InRange`) `Validations` because missing, incorrectly formatted, or uninterpretable values may be directly identified by those other `Validations` Tests.  Thus, separate counts of missing prerequisites may be less actionable than counts of compliance or non-compliance, depending on the design of a Test suite.  

A `Multi Record` `Measure` that counts records where `Response.status=EXTERNAL_PREREQUISITES_NOT_MET` may be informative in some workflow settings to identify cases where Tests may need to be run again later due to some problem connecting to some external source authority at run time.

**`Use Case` and `Policy` design note**: In practice, the utility of counting  INTERNAL_PREREQUISITES_NOT_MET outcomes depends on how your specification (`Expected Response`) clauses are written across a suite of Tests.  Suites that include explicit prerequisite checks (e.g., “INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdqval:Empty”) will surface more of these statuses, while suites that instead express missingness and non-interpretability as direct NOT_COMPLIANT outcomes in focused Validation Tests (e.g., separate ...\_NOTEMPTY and ...\_STANDARD Tests) will enable clearly identifying those cases in more actionable compliance/non-compliance counts.  Again, iterate in `Use Case` and Test design.

#### 8.1.5 Practical note: summary values vs. details (non-normative)

`Multi Record` `Measures` are intentionally constrained to produce a single value in `Response.result`. If you need more detail than one number (for example, mean and standard deviation), implementations may place additional structured detail in `Response.qualifier` (as an extension point), while keeping `Response.result` to a single number as required for the BDQ `Measure` outputs, but your preference should be to define additional `Multi Record` `Measures` if you need multiple summary values, rather than overloading a single `Measure`, such as one `Measure` that counts Response.status `INTERNAL_PREREQUISITES_NOT_MET` and another that counts Response.result `NOT_COMPLIANT` outcomes.  Separating these into separate `Measures` keeps each `Measure` focused and easier to interpret and allows for more flexible reporting and visualization of the results to answer particular `Quality Control` questions.

In other words for a `Measure`:

- `Response.status` answers “was the metric calculated?”
- `Response.result` answers “what is the one metric?”
- `Response.qualifier` (optional) can answer “what else helps interpret that metric?”

This pattern supports interoperability while still enabling rich `Quality Control` reporting in practical systems.

#### 8.1.6 Example Quality Control Measures for the Validated Distribution Authority Use Case (non-normative)

For our **Validated Distribution Authority** `Use Case`, we might define the following `Multi Record` `Measures` to summarize the results of the `Single Record` `Validations` in the `ValidationPolicy` for that `Use Case`, framing a separate `Measure` to count COMPLIANT results for each `Validation` Test (and one `Measure` to summarize overall compliance across all `Validations` (that is, a policy-level completeness measure)):

* MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY 
  * Count of records where VALIDATION_SCIENTIFICNAME_NOTEMPTY is COMPLIANT (i.e., has dwc:scientificName) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND 
  * Count of records where VALIDATION_SCIENTIFICNAME_FOUND is COMPLIANT (i.e., has a resolvable scientific name) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY 
  * Count of records where VALIDATION_SCIENTIFICNAMEID_NOTEMPTY is COMPLIANT (i.e., has dwc:scientificNameID) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE 
  * Count of records where VALIDATION_SCIENTIFICNAMEID_COMPLETE is COMPLIANT (i.e., has a complete scientificNameID) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY 
  * Count of records where VALIDATION_GEODETICDATUM_NOTEMPTY is COMPLIANT (i.e., has dwc:geodeticDatum) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD 
  * Count of records where VALIDATION_GEODETICDATUM_STANDARD is COMPLIANT (i.e., has a standard geodeticDatum) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_FOOTPRINTWKT_NOTEMPTY 
  * Count of records where VALIDATION_FOOTPRINTWKT_NOTEMPTY is COMPLIANT (i.e., has dwc:footprintWKT) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_FOOTPRINTWKT_VALID 
  * Count of records where VALIDATION_FOOTPRINTWKT_VALID is COMPLIANT (i.e., has a valid dwc:footprintWKT)
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_WASATTRIBUTEDTO_NOTEMPTY 
  * Count of records where VALIDATION_WASATTRIBUTEDTO_NOTEMPTY is COMPLIANT (i.e., has prov:wasAttributedTo) 
* MULTIRECORD_MEASURE_COUNT_COMPLIANT_WASATTRIBUTEDTO_STANDARD 
  * Count of records where VALIDATION_WASATTRIBUTEDTO_STANDARD is COMPLIANT (i.e., has a standard prov:wasAttributedTo)
* MULTIRECORD_MEASURE_QA_VALIDATIONPOLICY_COMPLIANT
  * COMPLETE if all `Validations` in the `ValidationPolicy` for the `Use Case` are COMPLIANT (i.e., has all required values and those values are valid)
  * This is a dataset-level and policy-level completeness measure across multiple Validations.

These Tests follow a naming convention of MULTIRECORD_MEASURE_COUNT_COMPLIANT_{validation_label} for the individual counts, and MULTIRECORD_MEASURE_QA_{condition} for `Measures` that return COMPLETE/NOT_COMPLETE.  

### 8.2 Quality Control Workflow (non-normative)

In contrast to `Quality Assurance`, which focuses on filtering a dataset down to records that are fit for a stated purpose, `Quality Control` focuses on *understanding* why data are not fit, and on identifying tractable actions that can improve quality over time. In practice, `Quality Control` is often iterative: run a suite of Tests, interpret the resulting `Data Quality Reports`, make targeted changes (to data, mappings, or workflows), and then re-run the Tests to confirm improvement.

#### 8.2.1 Start with Patterns, Not Individual Records (non-normative)

For real-world datasets, the number of `NOT_COMPLIANT` results can be large. A productive first step in a practical workflow is to summarize results in ways that reveal patterns:

- **By Test (`Validation`)**: Which Tests fail most often? Which failures are most likely to affect your intended `Use Case`?
- **By `Information Element`**: Are failures concentrated in a small set of terms (e.g., `dwc:countryCode`, `dwc:eventDate`, `dwc:scientificName`)?
- **By source / provider / collection / pipeline stage**: Are failures clustered by dataset subset, indicating differences in upstream practices?
- **By repeated value**: Do many failures share the same few problematic values (e.g., a common misspelling, code system mismatch, or placeholder value)?

These summaries help distinguish “many unique problems” from “one recurring problem”, and they help avoid spending time reviewing records one-by-one when the underlying cause is systematic.

In addition to dataset-level summaries, some `Single Record` `Measures` (e.g., `MEASURE_AMENDMENTS_PROPOSED`) can be useful for triage by identifying individual records that have many proposed changes and therefore may benefit from focused review.

#### 8.2.2 Look for Point Causes and Systemic Errors (non-normative)

Many record-level problems that appear as widespread in a dataset have *point causes*: a single upstream issue that propagates broadly when data are transformed, denormalized, or aggregated. Examples include:

- a mapping error that swaps fields or applies the wrong delimiter,
- characters set transformations that corrupted values (e.g., UTF-8 vs Latin-1 issues),
- an export rule that adds leading/trailing whitespace,
- an error in an authority table (such as a taxon name table) that propagates to many related records in denormalized exports (e.g. identifications),
- a controlled vocabulary change that was not reflected in a pick-list,
- a missing join key that causes large-scale loss of related values.

A key Quality Control technique is therefore to ask: “Could these many failures be explained by a small number of causes?” Investigating this can have high leverage: fixing a single cause can remediate thousands of records (or prevent future errors at ingestion).

#### 8.2.3 Focus on Results (non-normative)

`Response.status` values are useful for triage.  Look first to `RUN_HAS_RESULT` with `Response.result` = `NOT_COMPLIANT` for specific non-conformances that can be fixed.  In contrast, `INTERNAL_PREREQUISITES_NOT_MET` may be harder to interpret, they may come from a mixture of missing and uninterpretable values, and very likely (if you have designed the test suite well) are covered by `Validations` that test for empty and incorrectly formatted values.  

- `RUN_HAS_RESULT` with `Response.result` = `NOT_COMPLIANT` indicates the Test ran and found a specific non-conformance. This often points to easily identifiable *fixable* issues such as:
  - Mismatch of values with a controlled vocabulary (e.g., 3 letter country codes used where 2 letter codes are required)
  - Formatting problems (e.g., date formats, coordinate formats)

- `INTERNAL_PREREQUISITES_NOT_MET` can indicate some combination of *missing, incomplete, or uninterpretable* inputs. This may reflect:
  - legitimate unknowns (e.g., historical records with incomplete labels),
  - missing values that could be filled in,
  - values that could be standardized or corrected (e.g., “USA” instead of “US” for country code),
  - errors in transformation on export (e.g., incorrect format of database date fields into string literal dates),
  - data entry constraints not enforced at capture time,
  - schema or mapping gaps (values exist upstream but are not being exported).

Treating these categories differently and focusing on `RUN_HAS_RESULT` helps focus effort to specific known problem types, e.g. “fill in missing values” and “standardize or correct values” are distinct work types with different feasibility and risk profiles, and they are often easier to interpret and act upon from Tests targeted to identify them than the more ambiguous `INTERNAL_PREREQUISITES_NOT_MET` category.

#### 8.2.4 Prioritize Work for Greatest Impact (non-normative)

`Quality Control` can require substantial human effort, so prioritization matters. A practical prioritization approach is to consider:

- **Impact on the target `Use Case`**: failures in core requirements (e.g., location, time, taxon) may matter more than peripheral metadata.
- **Fixability at scale**: problems that can be corrected via deterministic rules, controlled vocabularies, or workflow changes typically yield high return.
- **Risk of introducing error**: changes that require interpretation or could introduce false precision should be deferred, flagged for careful review.
- **Prevention vs remediation**: improving upstream capture/validation rules prevents future errors and is often more cost-effective than repeatedly cleaning exports.

These may be coupled.  For example, in some institution, an uncontrolled database field that maps onto a Darwin Core term for which there is a controlled vocabulary may be identified as a high-impact, fixable problem.  Then a remediation strategy may involve a large scale data cleanup project within some institution where existing values are mapped onto the controlled vocabulary, some of which are straightforward and done at scale, others of which may need careful case by case examination in context.  Then, in parallel, to reduce the introduction of new inconsistencies, user interface elements may be added to restrict users to only enter allowed values in that field.  Then, when the cleanup project is complete use of the controlled vocabulary may be enforced at the database level, preventing the introduction of new problems in that field.  In this example, the combination of a large scale cleanup project and prevention measures may be more effective than repeated cleanup of exports with no prevention measures. 

Summaries from `Multi Record` `Measures` (particularly count outcomes) are particularly helpful for setting priorities for institutional data cleanup projects: they provide quick indicators of where quality improvement will most increase fitness for purpose, and they support tracking progress over time.

#### 8.2.5 Close the loop: re-run Tests to confirm improvements (non-normative)

Quality Control actions should be followed by re-running the same Test suite (and regenerating `Data Quality Reports`) to verify that:

- Targeted corrections had the intended effect.
- Improvements did not create new failures elsewhere.
- Quality has improved with respect to the selected `Use Case`.

This “run → analyze patterns → fix causes → re-run” loop is a Quality Control workflow pattern supported by the BDQ Tests and the Fitness For Use Framework.

#### 8.2.6 Example Quality Control Workflow Validated Distribution Authority Use Case (non-normative)

Let's assume that we've got a set of distribution data, and that we can map that data onto the `Information Elements` required by the `Single Record` `Validations` in our `ValidationPolicy` for the **Validated Distribution Authority** `Use Case`, and that we have implemented those `Validations` in some execution framework.

Our dataset would include the following `Information Elements` `scientificName, scientificNameAuthorship, scientificNameID, geodeticDatum, footprintWKT, wasAttributedTo`.

Now we could run the set of Tests against our dataset (of, say, 10000 records).  The workflow may include taking the resulting `Responses`, and using them as input for the `Multi Record` `Measures` listed above to get counts of compliant records for each of those `Validations`.  We could then use those counts to prioritize our `Quality Control` efforts.

We might find:
| Test | Count of COMPLIANT records | Calculated percentage of all records |
| ---- | -------------------------- | ------------------------------------ |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY | 9950 | 99.5% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND | 9000 | 90% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY | 0 | 0% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE | 0 | 0% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY | 10000 | 100% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD | 9980 | 99.8% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_FOOTPRINTWKT_NOTEMPTY | 9500 | 95% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_FOOTPRINTWKT_VALID | 9400 | 94% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_WASATTRIBUTEDTO_NOTEMPTY | 9900 | 99% |
| MULTIRECORD_MEASURE_COUNT_COMPLIANT_WASATTRIBUTEDTO_STANDARD | 0 | 0% |

And:
* MULTIRECORD_MEASURE_QA_VALIDATIONPOLICY_COMPLIANT = NOT_COMPLETE because not all the `Validations` are COMPLIANT.

We can quickly see two large gaps in the data: the `scientificNameID` field is completely empty, and the `prov:wasAttributedTo` field is present but does not conform to the expected standard.  These might be good targets for automated `Quality Control` efforts.  An examination of the data values or the `Response.comment` values from the underlying `Single Record` `Validations` may help identify specific problems and potential fixes.  For example, if the comment indicates that `prov:wasAttributedTo` values are present but do not match the expected ORCID format, we could look for common patterns in those values to design a mapping or transformation to fix them at scale.  We can see that 90% of records have a resolvable scientific name, so for that 90% it should be very straightforward to look up a corresponding `scientificNameID` value, so that might be a good target for an automated lookup (e.g. including [AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON](../terms/bdqtest/index.md#AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON) in the `Use Case` and workflow) to fix that problem at scale. 

The 10% of records with an unresolvable scientific name likely require manual review and a focused data cleaning project by a domain specialist with an understanding of the taxonomy involved in order to identify why these records are not matched to the taxonomic source authority, to resolve any problems, and to, in the process, find the correct `scientificNameID` value for these records.  This focused manual review should be carried out on distinct values of `dwc:scientificName` that are not resolvable, rather than on individual records. On examination of distinct values, these 1000 records might be a single typo in a single name, or they might involve many distinct names and many distinct problems.

The 5% of records missing `dwc:footprintWKT` are a core manual task for the domain specialist curators this data set.  They will need to find the distributions for taxa that don't have them.  

The 6% of records with invalid `dwc:footprintWKT` likely need to be addressed by a GIS specialist. 

Thus, these measure results not only provide a picture of the quality of the dataset, but also provide a starting point for a roadmap for how to improve the quality of the dataset for the `Use Case` of being a "validated distribution authority" for biodiversity science, with different types of problems that require different types of expertise to fix, and different types of fixes, some of which can be automated at scale, others of which will require manual evaluation.

Once these problems are fixed, we can re-run the same Test suite to confirm that the fixes had the intended effect, and to confirm that the quality of the dataset has improved with respect to the selected `Use Case`.  We can also track improvement over time by comparing the results of these `Multi Record` `Measures` before and after the fixes.  This iterative process of running Tests, interpreting results, fixing problems, and re-running Tests is a common `Quality Control` workflow pattern supported by the BDQ Tests and the Fitness For Use Framework.  

When all the problems have been fixed and the entire dataset is fit for this `Use Case`, the MULTIRECORD_MEASURE_QA_VALIDATIONPOLICY_COMPLIANT will return COMPLETE, and the dataset will be fit for use as a "validated distribution authority" for biodiversity science.

### 8.3 Quality Assurance Workflow (non-normative)

`Quality Assurance` is about filtering a dataset down to a subset of records that are fit for some purpose.  The mechanism to support this provided by the Fitness For Use Framework is the use of a set of `Multi Record` `Measures` that return `COMPLETE` if the dataset meets a dataset-level requirement derived from `Single Record` Test outcomes, and `NOT_COMPLETE` otherwise.  Then, if some set of `Measures` in the `MeasurementPolicy` of the `Use Case` are `NOT_COMPLETE`, data may be filtered out of the dataset based on underlying `Validation` problems (or remediated with `Amendment` results) such that the  `Measures` all return `COMPLETE`.   When all the `Multi Record` `Measures` of this sort for a `Use Case` (as specified by `Policy`) are `COMPLETE`, the filtered dataset is fit for use with respect to the selected `Use Case`.   

BDQ does not constrain how workflows may perform `Quality Assurance`, but it does provide a standard means for defining dataset-level requirements where `Single Record` Test outcomes, potentially modified by adopting proposals for improving the fitness of data from `Amendments` can be aggregated and measured for formal filtering of the data (using the `Multi Record` `Measures`) to provide formal  `Quality Assurance` of a dataset for a `Use Case`.

## 9 Round-Up (non-normative)

Our eleven year journey with the development of BDQ illustrates that there are many pitfalls in defining Tests.  Make sure that the `Expected Response` doesn’t hide any edge cases, and that is often easier said than done.  The development of the BDQ standard often surprised us with "emergent properties" and differing assumptions.  There are pitfalls in defining Tests for both the experienced and the inexperienced.  

Critical to the process of defining a new Test is to iterate.  Start with a draft definition, create one or more independent implementations, have someone who isn't writing the implementation produce conformance testing data (including looking at values found in the wild), validate the implementation(s) against this data, and discuss any discrepancies between the expected and actual results.  It will usually be necessary to iterate and refine the Test specifications, Test implementations, and the Test conformance testing data.  This process of iteration is critical for producing a robust Test specification that is clear, unambiguous, and has logic that handles real world data and edge cases. 

### 9.1 Summary of the BDQ Philosophy (non-normative)

Through these steps, the BDQ standard aims to be "comprehensive but not exhaustive". By providing clear rationale, identifying abstract `Information Elements`, and anchoring Tests in community-vetted `Use Cases`, the standard creates a stable framework for evaluating data quality. The emphasis on iteration, conformance testing, and real-world edge cases helps ensure that Tests are not only theoretically sound but also practically effective in improving data fitness for biodiversity data science.


## Glossary (non-normative)

A glossary of acronyms and terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

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

[TDWG](<../../index.md#glossary_TDWG> "[Biodiversity Information Standards](https://www.tdwg.org/standards/sds/)") Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2026. Tutorial: Creating a New Test using the BDQ Standard. Biodiversity Information Standards (TDWG). <https://bdq.tdwg.org/to_be_determined2026-03-20>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
