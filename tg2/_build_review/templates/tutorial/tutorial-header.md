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

This document provides, in the form of a tutorial, an overview of the concepts, reasoning, technical justifications, and logical choices behind the creation of a new Biodiversity Data Quality (BDQ) Test.  It can be used to understand the components of the BDQ standard and to guide users and implementers in describing new tests using the BDQ Fitness for Use Framework.  It is also intended to assist the proposed BDQ Maintenance Group in evaluating proposals for new tests and edits to existing tests.

### 1.2 Audience (non-normative)

This document is intended for users and implementers seeking to understand the components of the BDQ standard through examining the reasoning and technical justifications behind the creation of a new BDQ test. 

This document is also intended for those interested in describing new tests using the BDQ Fitness for Use Framework.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.4 Status of the content of this document (normative)

This document is non-normative.

### 1.5 Namespace abbreviations (non-normative)

The following namespace abbreviations are used in this document:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
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

This tutorial works through the development of a `Use Case`, then walks through two examples of the development of Tests.  One of the examples of a test is simple, the other is more complex.  This tutorial then comes back to the `Use Case` and describes how Measure Tests can be developed to evaluate the results of the Validation Tests for the purpose of `Quality Control`.  

The simpler of the two Tests examined is VALIDATION_FOOTPRINTWKT_NOTEMPTY, which was considered a [Supplementary test](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md) rather than a BDQ "Core" test as we considered it of marginal use for the BDQ `Use Cases`. As noted in the [BDQ Supplement Information](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md), the test could be useful in certain `Use Cases`, as noted below.

**Note** that a proposed **BDQ Maintenance Group** will be established to maintain the BDQ Standard. This group will take responsibility for advising on processes for editing the BDQ standard and evaluating new BDQ Tests, `Use Cases` and other components of the BDQ Standard.

By following this workflow, you move from a human-centric research need to a machine-readable technical standard.

## 3 Tutorial Phase 1: Context and Strategy (The "Problem") (non-normative)

*Before defining a test, we must justify why it exists and how it fits into the broader ecosystem of the standard.*

### 3.1 Define the Use Case and Fitness-for-Use Requirements (non-normative)

**Purpose:** Establish the data user's perspective and fitness-for-use requirements

**The Reasoning:** A test is only as good as the problem it solves. We begin by establishing a clear perspective on who the data user is, what use the data are to be put, what makes the data "fit for use" for that use, and what problems in the data would make it unfit for that use. 

Clearly stating the problem that we are trying to solve ensures that the test is grounded in real-world needs and not just theoretical ideals.

* **User:** A conservation biologist.
* **Context:** We have a data set consisting of "Expert Distributions" of taxa.  We want to validate that this dataset is usable for identifying outliers in other occurrence data (and for doing other things we may want to do with a set of expert distributions like drawing maps).  The data consist of a taxon oriented data set (e.g. one record per taxon) with fields identifying the taxon, providing the expert distribution as geospatial data (vector data providing shapes rather than point occurrences), along with metadata about the source of each record. 
* **What makes data Fit for this Use?**: To be fit for this purpose each record in the data set must have:  A taxonomic name.  This taxonomic name can be found in a relevant authority on taxon names.  The taxon is also represented with a machine-readable identifier.  The spatial footprint of the expert distribution of that taxon is provided as a polygon. That polygon is a valid shape.  Each taxon distribution has its source identified (the data set as a whole may have been compiled from multiple sources of taxon distributions).

#### 3.1.1 Refine and Formalize the Use Case (non-normative)

Now we can define our `Use Case`.  We need to specify three elements, a name for the use case, a description, and a statement of fitness for use requirements.  We want to refine our statement of the problem into concise and clear statements.   (We will also need a unique identifier for the `Use Case` that software can use, but we won't examine these machine-readable identifiers at this point).  

* **Name** Validated Distribution Authority
* **Description** Validating that Taxon oriented data can provide an authoritative resource for mapping known distributions of taxa, for identifying occurrence records in other data sets that have coordinates within the known ranges of taxa, are outliers, or for similar purposes.
* **hasFitnessRequirements** Data are fit for the `Use Case` "Validated Distribution Authority" and can provide a resource for validating that occurrence records are in range if they are taxon oriented data with fields that identify the taxon, that provide expert validated distributions as geospatial data, and provide metadata about the sources of the distributions.  To be fit for this purpose each record in the data set must have the following properties:
  * A taxonomic name is present and can be found in GBIF's backbone taxonomy.
  * A well-formed machine-readable taxonomic name identifier for that taxon is present.
  * A polygon providing the spatial footprint of the expert distribution for that taxon is present and valid.
  * Metadata providing the source for each taxon distribution is present.

It is helpful, but by no means required, to state the `hasFitnessRequirements` as a brief summary paragraph followed by a set of brief bullet points.  The `Use Case` is describing what we are trying to accomplish at a high level, without getting too far into the details.  

In each of the bullet points, the properties that are needed for fitness are explicitly stated, e.g. "is present", "is valid", "found in an authority", etc.  These properties will be the basis for defining tests that evaluate whether the data meet these fitness requirements, and being explicit here will help us describe tests that separate concerns.  We will wish to be clear about fields that must be present for the data to have quality (i.e. "is present") and which fields are optional, but need to have certain properties if populated (e.g. "is valid if present")

Treat this `Use Case` definition (and everything else that follows from it) as a first draft.  We will likely need to come back and refine this `Use Case` definition as we consider the data in the wild and start defining and implementing tests.  We may find that we need to add additional fitness requirements, or that we need to clarify the existing fitness requirements, or that we need to change the way we have stated the fitness requirements.  That is all part of the process.  It is critically important to be flexible and iterative in this process. 

### 3.2 Identify the Information Elements (non-normative)

**Purpose:** Determine which fields (mapped to vocabulary terms like Darwin Core terms) are in the data and are relevant to your use case.

Now let us consider in a little more detail what fields are present in the data that is to be evaluated and how can we map those fields onto terms in vocabularies like Darwin Core.  In the Fitness for Use Framework, input fields or terms for a Test are generalized as `Information Elements`

We can expand each of the bullet points in the hasFitnessRequirements statement into a set of terms that are likely to map onto the data.  We may understand these well at the start, or as we consider data in the wild and start defining and implementing tests, we will very likely need to come back and refine this list.

* A valid taxonomic name: 
  * dwc:scientificName
  * dwc:scientificNameAuthorship
* A machine-readable identifier for the taxonomic name:
  *  dwc:scientificNameID
* A polygon of the taxon footprint: 
  * dwc:footprintWKT (the expert distribution)
  * dwc:geodeticDatum (for the footprintWKT)
* Metadata providing source for each taxon distribution: 
  * prov:wasAttributedTo (ORCID ID)
  * foaf:name (Author name)
  * dcterms:source (publication or dataset source)  

Now, we want to identify a set of tests to be applied to these `Information Elements` to evaluate whether the data are fit for use.  

There are two key elements to the strategy at this point: (1) we want to identify and use existing tests that can be applied before defining new tests and (2) we want each test to be as focused as possible on a single aspect of data quality.

### 3.3 Reuse of Existing Tests and Gap Analysis (non-normative)

**Purpose:** Identify existing tests that can be applied to the `Information Elements` and identify gaps where new tests are needed.

Let's identify which existing BDQ tests might already be able to be applied to these `Information Elements` for this `Use Case`.

We can start with a simple presence check for each of these `Information Elements` (building on the "is present" statements in the `hasFitnessRequirements`) and then add more complex tests as needed.

We are looking for existing `Validation` Tests, as we are trying to assert whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT).  By convention in BDQ, the names of these tests start with VALIDATION_.  Simple presence tests for "does an `Information Element` contain a value", by convention have a name that ends with  NOTEMPTY.   Between these two parts, again by convention, the name of the `Information Element` (or the name of a concept (e.g. LOCATION, EVENT) for several `Information Elements`)  being tested is included.

For example, VALIDATION_SCIENTIFICNAME_NOTEMPTY is a test that checks if there is a value in dwc:scientificName.

There are several places we could look for existing tests within BDQ, including the Quick Reference Guide, and the [index](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#31-index-to-validation-tests-non-normative) of the bdqtest: term-list document.  An easy place to look for Tests that operate on particular `Information Elements` is the Quick Reference Guide's [BDQ Test Index by Information Element Acted Upon](../terms/bdqtest/qrg_index_by_ie_actedupon.md#bdq-test-index-by-information-element-acted-upon-non-normative)

Looking here for simple presence checks for the `Information Elements` we can identify the following existing BDQ tests (and gaps):

* A valid taxonomic name is present: 
  * dwc:scientificName VALIDATION_SCIENTIFICNAME_NOTEMPTY
  * dwc:scientificNameAuthorship VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
* A machine-readable identifier for the taxonomic name is present:
  *  dwc:scientificNameID VALIDATION_SCIENTIFICNAMEID_NOTEMPTY
* A polygon of the taxon footprint is present: 
  * dwc:footprintWKT **Gap**
  * dwc:geodeticDatum VALIDATION_GEODETICDATUM_NOTEMPTY
* Metadata providing source for each taxon distribution is present: 
  * prov:wasAttributedTo (ORCID ID) **Gap**
  * foaf:name (Author name) **Gap**
  * dcterms:source (publication or dataset source) **Gap**

Our `Use Case` calls for more than just a presence check for these `Information Elements`, so we would want to fill in in more candidate tests for these `Information Elements`, until we've got tests that cover each of the hasFitnessRequirements we identified for the Use Case.  Filling in a few more tests:  

* A taxonomic name is present and can be found in GBIF's backbone taxonomy.
  * dwc:scientificName
    * VALIDATION_SCIENTIFICNAME_NOTEMPTY
    * VALIDATION_SCIENTIFICNAME_FOUND (check if the name can be found in an authority, GBIF's backbone taxonomy by default)
  * dwc:scientificNameAuthorship
    * VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
* A well-formed machine-readable identifier taxonomic name for that taxon is present.
  * dwc:scientificNameID 
    * VALIDATION_SCIENTIFICNAMEID_NOTEMPTY
    * VALIDATION_SCIENTIFICNAMEID_COMPLETE (check if the identifier is well-formed)
* A polygon of the taxon footprint is present and valid: 
  * dwc:footprintWKT 
    * Is present: **Gap**
    * Is valid spatial data in a Well Known Text serialization: **Gap**
  * dwc:geodeticDatum 
    * VALIDATION_GEODETICDATUM_NOTEMPTY
    * VALIDATION_GEODETICDATUM_STANDARD (check if the value is a valid geodetic datum, e.g. by checking if it can be found in an authority like EPSG)
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

Let's focus on the gaps.  There is somewhere else we want to check for potential tests that aren't already defined in BDQ, but have had some level of documentation,  and that's the BDQ Issues in GitHub.

For dwc:footprintWKT, we could guess the name of the test, following the naming conventions, as VALIDATION_FOOTPRINTWKT_NOTEMPTY, and search the issues for [that name](https://github.com/tdwg/bdq/issues?q=VALIDATION_FOOTPRINTWKT_NOTEMPTY).  This particular search does return a match, but guessing the name is a fragile strategy, as the desired test might not have a name exactly matching that, and GitHub issue searches don't have good substring search support, so a better broader strategy is to search for: 

* Are there existing proposals tagged as [SUPPLEMENTARY](https://github.com/tdwg/bdq/issues?q=label%3ASupplementary) that would fill the desired gap.
* Are there existing proposals tagged as [DO NOT IMPLEMENT](https://github.com/tdwg/bdq/issues?q=label%3A%22DO%20NOT%20IMPLEMENT%22) that would fill the desired gap, but have been rejected for implementation, and should be reconsidered only with great caution.
* **Note that all of these issues in GitHub are Closed, the default issue search which includes is:open will not find them.**

So there is an existing definition for a test, VALIDATION_FOOTPRINTWKT_NOTEMPTY, in the documented Supplementary tests.

Looking at the description of that test we see:

* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY
* **Description** Is there a value in dwc:footprintWKT?
* **TestType** Validation
* **Information Elements Acted Upon** dwc:footprintWKT
* **Expected Response** COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

This is telling us, much like an entry in the Quick Reference Guide or the more detailed entry in the bdqtest: term-list document, that this test is a simple presence check for dwc:footprintWKT.

## 4 Defining a New Test (non-normative)

Let's walk through the steps and decisions involved in defining a test, using VALIDATION_FOOTPRINTWKT_NOTEMPTY as an example, and see how the components of the test are justified and how they fit together.

### 4.1 A Simple Description of the Test (non-normative)

The Description of the test is an easy-to-understand, concise explanation of what the test does. It is a human-oriented explanation.  It is a good starting point for defining a Test.

* **Description** “Is there a value in dwc:footprintWKT?”

As descriptions go, it doesn’t get simpler than that.

This description will also be used in Data Quality Reports to explain to users what the test is doing, so it should be clear and concise.  It should not include details about how the test might be implemented, but it should provide just enough information for a user to understand what the test is checking for.

**Reasoning for Simplicity:** In this test, we are not validating the *contents* or *mathematical structure* of the WKT polygon—only that it contains some data. We could add to a workflow for example, by adding subsequent tests for validating the contents of dwc:footprintWKT, but focusing on a "limited specific aspect" of data is a core principle of the standard.

See also [Principles for Defining Tests](../supplement/index.md#3112-principles-non-normative) in the Supplement.

### 4.2 Identify the Information Elements (non-normative)

**Purpose** Identify the specific fields in the input data (Information Elements) that the test will evaluate.

For this test we want to evaluate one `Information Element`, dwc:footprintWKT, which is a term in Darwin Core that provides a polygon of the taxon footprint.  

An `Information Element` is classified as either `ActedUpon` or `Consulted`.  An `Information Element` is `ActedUpon` if it is the primary focus of the test, and it is `Consulted` if it is supporting information used to run the test.  In this case, dwc:footprintWKT is the primary focus of the test, so it is an `Information Element` that is `ActedUpon`.  

Briefly consider another test that might be proposed to evaluate the validity of the WKT polygon in dwc:footprintWKT.  This test might have the same `Information Element` that is `ActedUpon`, dwc:footprintWKT, but it might also use the content of dwc:geodeticDatum to interpret the value in dwc:footprintWKT. In such a Test, the supporting `Information Element` dwc:geodeticDatum would be `Consulted`, the Test is making an assertion about the value in dwc:footprintWKT and "consulting" the value in dwc:geodeticDatum to do so, but not actually making an assertion about the value in dwc:geodeticDatum itself.  If a test asserts compliance about dwc:footprintWKT but uses dwc:geodeticDatum to interpret it, then dwc:footprintWKT is `ActedUpon` and dwc:geodeticDatum is `Consulted`.

The Test we are developing does not require any supporting information, so there are no `Information Elements` that are `Consulted`.

* **Information Elements Acted Upon** dwc:footprintWKT
* **Information Elements Consulted** None

### 4.3 Select the Test Type (non-normative)

**Purpose**: Determine in what way the test evaluates data quality.

There are four test types in BDQ: 

* **Validation** Assess whether data meet quality criteria (COMPLIANT/NOT_COMPLIANT)
* **Amendment** Propose improvements to data quality (AMENDED/NOT_AMENDED)
* **Measure** Quantify an aspect of data quality (numerical result) or measure completeness (COMPLETE/NOT_COMPLETE)
* **Issue** Flag potential problems for human review (POTENTIAL_ISSUE/NOT_ISSUE)  

We choose VALIDATION for this test because we are asserting whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT).

* **Test Type** Validation

See Also: 
* [Test Types](../bdqtest/index.md#22-test-types-non-normative) in the bdqtest: term-list document.
* [Test Types](../guide/users/index.md#31-test-types-non-normative) in the User Guide.

### 4.4 Name the Test (non-normative)

**Purpose**: Create human and machine-readable names for the test.

#### 4.4.1 Anatomy of a Test Label (non-normative)

**The Reasoning:** BDQ uses a convention for the naming pattern so that Test labels are predictable and descriptive: **TESTTYPE_INFORMATIONELEMENTS_EVALUATION**.

The use of all upper case with underscores is a convention inherited from the use of Java constants to identify tests in some early contributing projects.

The label provides a concise summary of the Test's purpose and logic.  The components of the label are:

* **Test Type** one of VALIDATION, AMENDMENT, MEASURE, or ISSUE, as described above.
* **Information Elements** Expressed as the "simple English term" for the `Information Element` being evaluated, or if multiple `Information Elements` are being evaluated together, a succinct more general concept (like LOCATION or EVENT) that encompasses those `Information Elements`
  * The use of "simple English terms" in the label (e.g., FOOTPRINTWKT) rather than the formal prefixed term (dwc:footprintWKT) to make it more accessible to human readers., and allows the label to be used as a string constant in many programming languages.
* **Evaluation:** What is the test testing? 
  * Examples of evaluations include "NOTEMPTY" (a value is present), “FOUND” (the value can be found in an authority), “INRANGE” (the value is within an expected range), etc.  See the [Evaluations](../../index.md#62-evaluations-in-test-labels-non-normative) list in the landing page for the BDQ standard.

This test is a Validation, it is evaluating the Information Element dwc:footprintWKT, and it is evaluating whether there is a value in dwc:footprintWKT, so the label is VALIDATION_FOOTPRINTWKT_NOTEMPTY.  This label is expected to be a constant that does not change, even in translation.

In order to support accessibility (the ability of screen readers to read the label in a more human friendly way), and to provide for translations of the name of the test into additional languages we will also want to create a Preferred Label for the test.

The Preferred Label for this test could be "Validation dwc:footprintWKT Not Empty".  This Preferred Label is expected to be translated into different languages.

This gives us the following names for the test: 
* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY
* **Preferred Label** Validation dwc:footprintWKT Not Empty 

See Also: the [Evaluations](../../index.md#62-evaluations-in-test-labels-non-normative) list in the landing page for the BDQ standard.

#### 4.4.2 Identifiers supporting software and developers (non-normative)

While the label is a human-friendly identifier for the test, we need a machine-readable identifier that can be used by software to identify the test.  In BDQ, this is the `Term Name`, which is a UUID.  This allows software to unambiguously identify the test, and to ensure that a search for the test results in only this specific test being identified/located.

We also need to provide a date for the test definition, and to update that date if the test definition is modified.

This gives us the following additional properties for the test:
* **Term Name** c6b705fc-7cf8-4af1-88ab-7a38d85f7109 
* **Modified** 2024-01-29

(Once accepted into BDQ, these properties would be combined to form the fully qualified Term IRI for the test (e.g. https://rs.tdwg.org/ bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933) and the Term Version IRI for a particular version of the test (e.g. https://rs.tdwg.org/ bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933-2024-07-24))

See Also: [Key to bdqtest: Vocabulary Terms](../list/bdqtest/index.md#110-key-to-vocabulary-terms-normative) in the bdqtest: term-list document.

### 4.5 Identify the Data Quality Dimension and Criterion (non-normative)

**Purpose**: Classify the test according to the aspect of data quality it addresses.

All BDQ Tests are related to some dimension of data quality.  These are formally defined in the bdqdim: vocabulary.

BDQ Data Quality Dimensions include:
* **Completeness**: Are all required data elements present?
* **Conformity**: Do data values conform to format, syntax, or controlled vocabularies?
* **Consistency**: Are data values logically consistent with each other?
* **Likeliness**: Do data values fall within expected ranges or distributions?
* **Resolution**: Is the level of detail appropriate for the intended use?

The question we wish to ask is whether there is a value in dwc:footprintWKT.  In this test we are only asking if any value is present, we are not asking if it is correctly formatted Well Known Text spatial data, or whether it contains in-range values, or anything else, we are simply asking if any value is present.  So this test is addressing the Completeness dimension of data quality.

This seems a very trivial test.  It is.  That is important.  We do not wish to overcomplicate our tests.  We want to ask simple questions that are easy to understand and implement, and that address specific aspects of data quality.  

This test is a simple presence check for dwc:footprintWKT, and it is exactly the simple presence check we need for our `Use Case`.  If some data are absent and other data are incorrectly formatted, a more complicated test that checks for both presence and correct formatting will not be able to distinguish between these two problems, and thus will not be as useful for our `Use Case` as a simple presence check (combined with a separate test to assess correct formatting).

BDQ `Validations` also have a `Criterion` property.  Each Criterion represents an abstract way of evaluating whether a data value meets expectations for a particular Use Case.  These are formally defined in the bdqcrit: vocabulary.  For example, the Criterion `NotEmpty` is defined as "The data value is not empty (i.e., it contains some data)".  This is exactly the criterion we are applying in this test, so we will use the `NotEmpty` criterion for this test.  

This gives us the following additional properties for the test:
* **Data Quality Dimension** Completeness
* **Criterion** NotEmpty

All BDQ Test types have a `Data Quality Dimension` (taking values from the bdqdim: vocabulary).  Only `Validations` and `Issues` have a `Criterion` (taking values from the bdqcrit: vocabulary), while `Amendments` have a `Enhancement` (taking values from the bdqenh: vocabulary).  `Measures` have only the `Data Quality Dimension`.

See also:
* [bdqdim:](../list/bdqdim/index.md) for the data quality dimension vocabulary.
* [bdqcrit:](../list/bdqcrit/index.md) for the criteria vocabulary.
* [bdqenh:](../list/bdqenh/index.md) for the enhancement vocabulary.

### 4.6 How many records are we examining at once? (non-normative)

**Purpose**: Determine whether the test is applied to single records or multiple records.

In BDQ, tests can be applied to single records or to multiple records.  A test that is applied to a single record is called a "SingleRecord" test, and a test that is applied to multiple records is called a "MultiRecord" test.  The distinction between these two types of tests is important because it affects how the test is implemented and how the results are interpreted.

We wish to step through the input data set one record at a time and for each record assess whether or not there is a value in dwc:footprintWKT.  Thus we are applying this test to single records, and thus this is a "SingleRecord" test.  

We will come back later and define another test to measure how much of the data set is compliant for this test, and that will be a "MultiRecord" test, but for now we are just defining a simple presence check for dwc:footprintWKT that is applied to single records.

* **Resource Type** SingleRecord

See also: [Resource Types](../bdqtest/index.md#32-resource-types-normative) in the bdqtest: term-list document.

### 4.7 Define the Test Specification (non-normative)

**Purpose**: Provide a clear, unambiguous description of the test's logic and expected outcomes.

Now we need to provide the unambiguous technical details required for a developer to implement the test.

Let's start with the question the test is asking, very simply phrased:  **Is there a value in dwc:footprintWKT?**

Now, let's phrase that question in a way that provides clear and unambiguous guidance to a developer who will implement the test.  The phrasing follows a standard structure and terminology in the BDQ standard. 

Since this is a `Validation`, the test will return either COMPLIANT or NOT_COMPLIANT.  The test will return COMPLIANT if there is a value in dwc:footprintWKT, and it will return NOT_COMPLIANT if there is not a value in dwc:footprintWKT.  We can phrase this as follows:

**Expected Response** COMPLIANT if dwc:footprintWKT contains some value; otherwise NOT_COMPLIANT

But, "contains no value" might be interpreted in different ways by different developers, so we want to use an explicit concept from BDQ that allows developers to look in one place for the meaning of "contains some value", and know that this is a standard concept that gets reused.

The bdq: vocabulary contains a term for just this purpose: [bdq:NotEmpty](../list/bdq/index.md#bdq_NotEmpty), it provides a standard definition of this common concept for reuse in many tests, preventing ambiguity in implementation. Thus, we can rephrase the expected response to link to this standard concept:

**Expected Response** COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

This means that implementers should examine the input data, evaluate the statements in order, and return a result from the first statement that is true.
* COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; 
* otherwise NOT_COMPLIANT

In this simple case, if dwc:footprintWKT is bdq:NotEmpty, the test should return COMPLIANT and stop there.  If dwc:footprintWKT is not bdq:NotEmpty, the test should return NOT_COMPLIANT.
 
See also: 
* [Reading a Specification](../guide/implementers/index.md#232-reading-a-specification-non-normative) in the Implementers Guide.

#### 4.7.1 What Isn't Said in the Test Specification (non-normative)

For the purposes of simplicity and clarity, the expected response does not include all of the details of a Response from a test, just the key elements that implementers need to understand the logic of the Test.  The response from a Test is required to contain metadata (`bdqffdq:hasResponseStatus`), the value of the result of the test (`bdqffdq:hasResponseResult` or `bdqffdq:hasResponseResultValue`) and a human readable statement about why the test reached the conclusion it did in a particular case (`bdqffdq:hasResponseComment`).   

**Expected Response** COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

Is shorthand for the the explicit, but much harder to read:
* bdqffdq:hasResponseStatus is RUN_HAS_RESULT and bdqffdq:hasResponseResult is COMPLIANT with an explanatory bdqffdq:hasResponseComment that dwc:footprintWKT contains a value if dwc:footprintWKT is bdq:NotEmpty; 
* otherwise bdqffdq:hasResponseStatus is RUN_HAS_RESULT and bdqffdq:hasResponseResult is NOT_COMPLIANT with an explanatory bdqffdq:hasResponseComment stating that dwc:footprintWKT contains no value.

Responses from Tests must have the tripartite status, result, and comment structure, but the Expected Response in the test specification is a concise statement of the logic of the test, without all of these details (details for which the content is explicit in the BDQ standard, e.g. if the result is COMPLIANT, the status must be RUN_HAS_RESULT, and there must be a comment).

The conventions of evaluating clauses in sequence, returning a result from the first clause that evaluates to true, and highlighting only the key differences in each clause are very important in making complex Expected Responses readable and understandable to implementers.  (see, for example, the Expected Response for [VALIDATION_DATEIDENTIFIED_INRANGE](../terms/bdqtest/index.md#validation_dateidentified_inrange)).

See also:
* [Responses from Tests](../guide/users/index.md#323-outputs-responses-from-tests-normative) in the Users Guide.
* [Reading a Specification](../guide/implementers/index.md#232-reading-a-specification-non-normative) in the Implementers Guide.
* [Responses as a Shorthand](../guide/implementers/index.md#2321-response-as-shorthand-for-a-set-of-bdqffdq-concepts-non-normative) in the Implementers Guide.

### 4.8 Source Authority? (non-normative)

**Purpose**: If the test references an external authoritative source, specify that source authority in the test definition.

In BDQ, if a test references some external authoritative source, e.g. a controlled vocabulary, an authority file, a registry, etc., it is important to specify that source authority in the test definition.  This allows implementers to know where to look for the authoritative information that they need to run the test, and it allows users of the test results to understand the basis for the test's logic.

In this test, we are not referencing any external authoritative source, we are simply checking for the presence of a value in dwc:footprintWKT, so there is no source authority to specify.

### 4.9 Generalize the Test? (non-normative)

**Purpose**: If different users of the test might have slightly different data quality needs with regard to that test, consider generalizing the test with a parameter.

In BDQ, if different users of a Test might have slightly different data quality needs with regard to that test, (such as checking if elevation values are in range within national boundaries for some national data set, rather than more general global minimum and maximum possible elevations), the Test can be generalized with a parameter, allowing different users to specify slightly different behaviors for the test, while retaining the same internal logic.

In this test, we are simply checking for the presence of a value in dwc:footprintWKT, so there is no need to generalize the test with a parameter.

### 4.10 List the properties of the Test (non-normative)

**Purpose**: Create a human-readable label for the test and list its properties in a structured format.

Now let's put all of this together into a structured format that lists the properties of the test, including its label, description, test type, information elements acted upon, and expected response.  See the bdqtest: term-list document for examples (like the very similar [VALIDATION_COUNTRYCODE_NOTEMPTY](../list/bdqtest/index.md#bdqtest_853b79a2-b314-44a2-ae46-34a1e7ed85e4).  For our test, we have:

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
* **Expected Response** COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

To formally express this test in RDF we would need to add some more identifiers and structures, but the above are the key properties that define the test and provide the information needed for an implementer to understand and implement the test.  See the bdqffdq: ontology guide for details about the full formal structure.

See also: 
* [Reading Test Descriptors](../guide/users/index.md#31-test-types-non-normative) in the Implementer’s Guide.

#### 4.10.1 Formal RDF Representation of the Test (non-normative)

This simple list of properties is sufficient for a human reader to understand the test and for a developer to implement the test.  However, to formally express this test in RDF we would need to add some more identifiers and structures, but the above are the key properties that define the test and provide the information needed for an implementer to understand and implement the test.  The bdqffdq: ontology guide gives the details about the full formal structure.  We won't go into the details of the RDF representation here.

See Also:
* [Diagram of Test Concepts](../guide/implementers/index.md#3-compliant-implementation-normative) in the implementers guide.
* [Example RDF for a test](../bdqtest/index.md#24-example-rdf-non-normative) in the bdqtest: landing page (VALIDATION_COUNTRYCODE_STANDARD in an RDF/XML serialization).
* [Example RDF for a test](../guide/bdqffdq/index.md#36-example-representation-of-a-bdq-test-non-normative) in the bdqffdq: ontology guide (VALIDATION_COUNTRY_FOUND in a Turtle serialization). 

#### 4.10.2 Summary of the Test Definition

So, VALIDATION_FOOTPRINTWKT_NOTEMPTY is a `Validation` test, that takes dwc:footprintWKT as input, and asks a very simple question, "Is there a value in dwc:footprintWKT?", This question is spelled out very clearly for an implementer in the `Expected Response`.  The expected response is COMPLIANT if there is a value in dwc:footprintWKT, and NOT_COMPLIANT if there is not a value.  This is exactly the simple presence check we need for our `Use Case`.

Thus, we could include this test in our `Use Case`, even though it is not yet accepted into the BDQ standard (and we could implement it, test the implementation, and put it forward to the Maintenance group for consideration for inclusion in the standard). This test would fill the gap of a simple presence check for dwc:footprintWKT.

## 5 Test for another Gap (non-normative)

Another gap we identified in the `Use Case` was evaluating whether prof:wasAttributedTo contains a value, and whether that value is a valid ORCID ID.  Under the principle of keeping tests focused on a single aspect of data quality, we can break this down into two separate tests:

* prov:wasAttributedTo (contains a value) **Gap**
* prov:wasAttributedTo (ORCID ID is valid) **Gap**

The first of these is a simple presence check for prov:wasAttributedTo, which is a term in the PROV ontology that provides metadata, in this case, about the source of each taxon distribution.  We could define a test for this gap in a similar way to the test we just defined for dwc:footprintWKT.  The test would be a `Validation` test, it would take prov:wasAttributedTo as input, and it would ask the question "Is there a value in prov:wasAttributedTo?"  The expected response would be COMPLIANT if there is a value in prov:wasAttributedTo, and NOT_COMPLIANT if there is not a value.

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
* **Expected Response** COMPLIANT if prov:wasAttributedTo is bdq:NotEmpty; otherwise NOT_COMPLIANT

## 6 Defining a more complicated Test (non-normative)

The next gap we identified in the `Use Case` was: 

** prov:wasAttributedTo (Conforms to the structure of an ORCID ID identifier) **Gap**

This is a more complicated test, as it requires not just checking for the presence of a value, but also checking that the value conforms with the expected structure of an ORCID ID.  

Note than on the principle of one Test evaluates one simple thing, we are asking whether the value has the correct structure for an ORCID ID, but we are not asking whether the value is actually a valid ORCID ID (e.g. by checking if it can be found in an authority like the ORCID ID registry).  We would define a separate test for that second question, and thus keep each test focused on a single aspect of data quality.

### 6.1 A Simple Description of the Test (non-normative)

The Description of the test is an easy-to-understand, concise explanation of what the test does. It is a human-oriented explanation.  

We could phrase this as "Is there a value in prov:wasAttributedTo, and if so, is it a valid ORCID ID?"  This, however, is combining two questions into one.

We want this test to evaluate a single aspect of data quality, which is whether the value in prov:wasAttributedTo is a valid ORCID ID.  Thus we can phrase the description as follows:

* **Description** Is the value in prov:wasAttributedTo a valid ORCID ID?

### 6.2 Identify the Information Elements (non-normative)

The `Information Element` that this test will evaluate is prov:wasAttributedTo, which is a term in the PROV ontology that provides metadata about the source of each taxon distribution.  This `Information Element` is `ActedUpon`, as it is the primary focus of the test.  This test does not require any supporting information, so there are no `Information Elements` that are `Consulted`.

* **Information Elements Acted Upon** prov:wasAttributedTo

### 6.3 Select the Test Type (non-normative)

We are asserting whether the value in prov:wasAttributedTo is a valid ORCID ID, so we are asserting whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT), thus we choose VALIDATION for this test.

* **Test Type** Validation

### 6.4 Name The Test (non-normative)

Now we can name the test, following the naming conventions in BDQ.  The test is a Validation, it is evaluating the Information Element prov:wasAttributedTo, and it is evaluating whether the value in prov:wasAttributedTo is a valid ORCID ID, that is whether it can be found in an authoritative list of ORCID IDs.  So the label for this test could be VALIDATION_WASATTRIBUTEDTO_STANDARD.  

* **Label** VALIDATION_WASATTRIBUTEDTO_STANDARD

We will also want to provide a more readable and translatable Preferred Label, and a machine-readable identifier, and a version date for this test.

* **Preferred Label** "Validation prov:wasAttributedTo Standard".  
* **Term Name** {some UUID}
* **Modified** 2026-03-25

### 6.5 Identify the Data Quality Dimension and Criterion (non-normative)

This Test is a `Validation`, so it will have both a `Data Quality Dimension` and Criterion.  

The `Data Quality Dimension` is the aspect of data quality that this test is addressing, looking at the bdqdim; vocabulary we find 'Conformance` defined as "Where data in a bdqffdq:InformationElement conform to a format, syntax, data type, range, or standard."  We are asking if the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID, so this is a good fit.

Similarly in the bdqcrit: vocabulary we find 'Standard' defined as "Data in a bdqffdq:InformationElement conform to a format, syntax, data type, or standard. Corresponding dimension is bdqdim:Conformance."  Again, this sounds like a good fit.

* **Data Quality Dimension** Conformance
* **Criterion** Standard

In contrast, in another test that evaluates whether the ORCID ID is valid by checking if it can be found in an authority like the ORCID ID registry, we would use a `Data Quality Dimension` of `Conformance`, but a `Criterion` of **`Found`**.

### 6.6 How many records are we examining at once? (non-normative)

This test would evaluate the value of prov:wasAttributedTo for each record, so we are applying this test to single records, and thus this is a "SingleRecord" test.

* **Resource Type** SingleRecord

### 6.7 Define the Test Specification (non-normative)

We could make a very simple specification for this test, such as "COMPLIANT if the value in prov:wasAttributedTo is a valid ORCID ID; otherwise NOT_COMPLIANT".  However, this is not very clear or specific for an implementer.  What does it mean for a value to be a valid ORCID ID?  How would an implementer determine that?  We need to provide more specific guidance in the specification to ensure that different implementers will implement the test in a consistent way and thus get comparable results.

We are asking not if the the value in prov:wasAttributedTo is Found in some authority, but if it Conforms to the expected format for an ORCID ID.  Thus we could phrase the specification as "COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID; otherwise NOT_COMPLIANT".  This is better, but what happens if the value in prov:wasAttributedTo is empty?  That would be NOT_COMPLIANT, but it would not be because the value does not conform to the expected format for an ORCID ID, it would be because there is no value at all, and this Test would overlap in what it is testing with VALIDATION_WASATTRIBUTEDTO_NOTEMPTY, which is our separate test above that checks for the presence of a value in prov:wasAttributedTo.  We want to keep these two tests separate and focused on different aspects of data quality, so we need to make sure the specification for this test is clear that it is only evaluating whether a value that is present conforms to the expected format for an ORCID ID, and it is not evaluating whether a value is present at all. We accomplish this by asserting that the presence of some value in prov:wasAttributedTo is a prerequisite for this test, and if that prerequisite is not met, then this test cannot return a result.

So we could phrase our test specification as a sequence of:
* INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdq:Empty;
* COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID; 
* otherwise NOT_COMPLIANT

This could work for our `Use Case`, but what does it mean for a value to conform to the expected format for an ORCID ID?  We need to provide more specific guidance on what we mean by that.  We could be more explicit in the Specification, but bdqffdq: provides a means for us to separate out these specifics, the `Source Authority` (which will then set the stage for making this test more generally applicable).

#### 6.7.1 Source Authority (non-normative)

TODO: Repeat the logic, but here add in source authority, and then recognize that a parameter is needed to allow for alternative authorities like VIAF, as the test can be more general than just ORCID ID, and thus more broadly applicable.

**TODO: Check Lee's Text** 

This component of a test is required IF it must reference some
authorities outside the BDQ namespaces (the ontology or vocabularies
that form the BDQ standard). These are external dependencies and
therefore are outside the domain and responsibility of BDQ.

As noted in the BDQ documentation, many aspects of 'data quality’ or
'fitness for use’ cannot be evaluated IF no authority exists to which to
evaluate data values.

BDQ details the structure and format of source authorities as follows

**TODO: Clarify this is a convention, not controled by normative statement**
**TODO: Fix error, "Name of Authority" is a fixed text string identifier for implementers to embed in code, not the name of the authority**
> bdq:sourceAuthority default = “Name of Authority” {\[URL\]}{optional
> API name if available\[URL of the API\]}

Alternative: "Fixed identifier" {["regular expression pattern"]}

Here are three examples, each divided into its component parts:

* bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}
  * Fixed string Identifier: "ISO 3166 Country Codes" (the name of the authority)
  * URI: {[https://www.iso.org/iso-3166-country-codes.html]}
  * API: {ISO 3166-1-alpha-2 Country Code search \[https://www.iso.org/obp/ui/#search\]}
    * A label for the API: "ISO 3166-1-alpha-2 Country Code search" 
    * An API endpoint: [https://www.iso.org/obp/ui/#search]

* bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}
  * Fixed string identifier:  "The Getty Thesaurus of Geographic Names (TGN)" 
  * URI: {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}

* bdq:sourceAuthority default = "Regex present/absent" {["^(present|absent)$"]}
  * Fixed string identifier: "Regex present/absent" 
  * Regular Expression Pattern: "^(present|absent)$" (matches only the strings "present" or "absent" (the leading and trailing [{ enclose the pattern, but aren't part of it))

For this test, we can use the regular expression pattern for a resolvable ORCID ID as the source authority, thus we could specify the source authority as follows:

* **hasAuthoritiesDefaults** bdq:sourceAuthority default = "Resolvable ORCID ID regex" `{["^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"]}`
* **Expected Response**  INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdq:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of bdq:sourceAuthority; otherwise NOT_COMPLIANT.

Which, combining the Expected Response with the default sourceAuthority, could be read by an implementer as: 
* INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdq:Empty; 
* COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of "^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"
* otherwise NOT_COMPLIANT.

#### 6.7.2 Generalize, add a parameter (non-normative)

We could make this test more general by allowing for alternative authorities, and thus more broadly applicable, by adding a parameter to the test that allows an implementer to specify which authority to use for evaluating whether the value in prov:wasAttributedTo conforms to the expected format for an ORCID ID.  This would allow the test to be used not just for ORCID IDs, but also for other types of identifiers that have a well-defined format and an authority that can be referenced for that format.

**TODO: Evaluate Lee's Text:**

Some tests have \`parameters\` that can be edited to change how the test
will respond in certain conditions. Parameters can be one of three
types:

-   Date ranges (e.g., bdq:earliestValidDate)

-   Thresholds (e.g., dwc:minimumLEveationInMeters)

-   Alternative authorities or vocabularies (e.g., taxonomic names
    authorities)

Note that IF there is only one source authority, such as \`ISO\`, there
is no parameter value as no other source has the authority. As noted in
the example above, BDQ allows for parameters where an implementation of
BDQ requires a unique, non-globally accepted authority, as may be the
case for example when legislation or tradition requires taxonomic names
to be checked against a national names list.

Some users may wish to store ORCID ID values with an ORCID: prefix, instead of the canonical https://orcid.org/ resolvable form, and thus we might want to allow for a parameter that allows for this variation in format.  This would be a parameter that allows for an alternative regex pattern to be used for evaluating the format of the ORCID ID, and when used, would change the behavior of the Test such that https://orcid.org/0000-0002-1825-0097 would be NOT_COMPLIANT while ORCID:0000-0002-1825-0097 would be COMPLIANT.  This would allow the test to be used for data sets that use this alternative format for ORCID IDs, while still allowing the test to be used for data sets that use the canonical resolvable form of ORCID IDs, without any change to the specifiction of the test itself. 

* "Bare ORCID ID regex" `{[^ORCID:\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`

Other users might wish to allow for VIAF or other identifiers in wasAttributedTo, thus they could use the same test, but with an implementation that supports a parameter value that encompasses their needs (e.g. "VIAF ID regex" `{[^https?://viaf\.org/viaf/\d+$]}`, or "VIAF or ORCID ID regex" `{[^https?://viaf\.org/viaf/\d+$|^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`), and thus they could use the same test for their needs without any change to the specifiction of the test itself.

Parameters allow a test to be generalized to serve a broader range of use cases, while still maintaining a clear and specific test specification that can be implemented in a consistent way across different implementations.

We can make the bdq:sourceAuthority as a parameter for this test, meaning that users could supply different sourceAuthority values as parameters to change the behavior of a test implementation to fit their specific local needs, while retaining the overall meaning and purpose of the test.  Under the expectations of BDQ, all implementations must support the default parameter value.  A caveat, a brand new parameter value for a test must be accompanied by implementation supporting that value, and not every implementation of the test may support every proposed parameter.

* **Parameter** bdq:sourceAuthority

#### 6.7.3  Revisiting the Test Specification (non-normative)

Having asserted that a bdq:sourceAuthority is needed in the test definition (and that the test can take this as a parameter to allow for different implementations to use different authorities), we now need to revisit the Description and Expected Response to make sure that we have included this generalization.

* **Description** Does value in prov:wasAttributedTo conform to the format of the bdq:sourceAuthority?
* **Expected Response**  INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdq:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of bdq:sourceAuthority; otherwise NOT_COMPLIANT.

### 6.8 Notes (non-normative)

Notes are present when some aspects of a test may not be obvious to the casual user or implementer, or if we want to describe aspects of the behaivior of the test in a non-normative way. 
Notes might want to comment on variations in the expected structure of an ORCID ID, for example, the expected format of an ORCID ID is https://orcid.org/0000-0002-1825-0097, which can be tested for with this regular expression pattern: ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$

But we might or might not want to allow for http:// as well as https:// and allow a case error where x is used instead of X, and comment on the rationalle for these decisions in the Notes. For example: 

* **Notes** The expected format of an ORCID ID is ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$, but we allow for protocol variants of http:// as well as https:// in the identifier and relax to the regex ^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$.  We expect the ORCID ID to be in resolvable form, not the bare identifier.  ORCID IDs are a subset of ISNI in the range 0000-0001-5000-0007 to 0000-0003-5000-0001, but this test only evaluates the format, not the range.  The form ORCID:0000-0001-5000-0007 should be treated as NOT_COMPLIANT by this test.

### 6.9 List the properties of the Test (non-normative)

* **Label** VALIDATION_WASATTRIBUTEDTO_STANDARD
* **Description** Does value in prov:wasAttributedTo conform to the format of the bdq:sourceAuthority?
* **Preferred Label** "Validation prov:wasAttributedTo Standard".  
* **Term Name** {some UUID}
* **Modified** 2026-03-25
* **Test Type** Validation
* **Information Elements Acted Upon** prov:wasAttributedTo
* **Expected Response**  INTERNAL_PREREQUISITES_NOT_MET if prov:wasAttributedTo is bdq:Empty; COMPLIANT if the value in prov:wasAttributedTo conforms to the expected format of the bdq:sourceAuthority; otherwise NOT_COMPLIANT.
* **hasAuthoritiesDefaults** bdq:sourceAuthority default = "Resolvable ORCID ID regex" `{[^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$]}`
* **Parameter** bdq:sourceAuthority
* **Notes** The expected format of an ORCID ID is ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$, but we allow for protocol variants of http:// as well as https:// in the identifier and relax to the regex ^http(s){0,1}://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$.  We expect the ORCID ID to be in resolvable form, not the bare identifier.  ORCID IDs are a subset of ISNI in the range 0000-0001-5000-0007 to 0000-0003-5000-0001, but this test only evaluates the format, not the range.  The form ORCID:0000-0001-5000-0007 should be treated as NOT_COMPLIANT by this test.

#### 6.9.1 Summary of the Test Definition

VALIDATION_WASATTRIBUTEDTO_STANDARD is a `Validation` test, that takes prov:wasAttributedTo as input, and asks the question "Does the value in prov:wasAttributedTo conform to the format of [a specified authority]?"  The expected response is COMPLIANT if there is a value in prov:wasAttributedTo and that value conforms to the expected format for an ORCID ID as defined by the default source authority; otherwise NOT_COMPLIANT.  If there is no value in prov:wasAttributedTo, then this test cannot return a result, and thus returns INTERNAL_PREREQUISITES_NOT_MET.  This test has a parameter for the source authority, allowing for different implementations to use different authorities for evaluating whether the value in prov:wasAttributedTo conforms to the expected format for different identifiers, while still retaining the same overall logic and purpose of the test.

#### 6.9.2 Iterate

Earlier we said _"Treat this `Use Case` definition (and everything else that follows from it) as a first draft."_

This is a critical point in the process, as we have now defined tests that fill gaps in our `Use Case`, and we have defined these tests in a way that is consistent with the principles of BDQ, and we have provided detailed specifications for these tests.  However, we have not yet implemented these tests, and we have not yet thrown any real data at these tests to see how they respond.  Thus, we should treat this as a first draft of the `Use Case` and Test definitions, and be prepared to iterate on these definitions based on implementation feedback and real-world data.

## 7 Validation and Community (The "Real-World")

*No test is final until it is implemented and thrown at actual data to confirm it responds correctly.*

### 7.1 Implementation (non-normative)

A Test specification may sound perfectly clear and straightforward to its writers, but it may not be clear to developers who are trying to implement the test based on the specification.  Thus, the only way to confirm that a Test specification is clear and can be implemented correctly is to actually implement the Test based on the specification, and then throw real data at that implementation to see if it responds correctly.  Expect that an initial Test specification will need revision based on questions raised in implementation and on testing the behavior of the implementation against real world data.

BDQ is deliberately agnostic about programing languages and execution frameworks for Test implementations.

A BDQ Test implementation has a consistent scope and API shape across languages:

* Inputs: the Information Element(s) Acted Upon (and any Consulted values if needed), plus optional Parameter(s) (e.g., bdq:sourceAuthority) where implementations MUST support the default parameter string literal if the parameter is exposed.
* Logic (decision rules): evaluate the clauses in the Specification (hasExpectedResponse) in order, returning the first matching outcome (handling EXTERNAL_PREREQUISITES_NOT_MET via exception/error handling where appropriate).
Output: exactly one structured Response per run, always providing Response.status + Response.comment, and providing Response.result only when Response.status indicates a result (typically RUN_HAS_RESULT).

BDQ keeps Tests portable by standardizing semantics (inputs, decision rules, outputs), but it leaves execution mechanics (binding to input data, orchestration of test execution) to whatever framework fits the implementer’s environment.  This means that the behavior of the implementation of an individual test should be tested in isolation, presenting the test with known inputs, and confirming that the test produces the expected outputs based on the logic of the decision rules in the specification.  This means that test validation is expected to be performed on the level of individual test implementations.


### 7.2 Unit Tests (non-normative)

When implementing a Test, implementors are encouraged to use a test driven development approach, where they first create unit tests for a Test implementation covering each expected path in the specification, as well as edge cases, and then implement the Test internals to pass those unit tests.  This helps ensures that the Test is implemented correctly and that it responds correctly to a variety of test cases, including edge cases.

### 7.3 Test Validation Data and Edge Cases (non-normative)

**TODO: Check Lee's Text**

The only way to validate a test is to implement it and then throw
sufficient examples of data at that test to confirm that it responds
correctly. Always start with the two examples as noted above, then add
any additional data to ensure comprehensive coverage.

**Purpose**: Ensure that a test can be correctly implemented

**Validation Process**:

-   Create comprehensive test data covering all scenarios

-   Include edge cases and boundary conditions

-   Test with different data encodings and formats

-   Validate against expected responses

**Test Data Categories**:

-   Valid compliant data

-   Valid non-compliant data

-   Missing/empty data

-   Malformed data

-   Edge cases (nulls, whitespace, non-printing characters)

**Our Test:** Provide a "pass" and "fail" example to aid developer
understanding.

-   **Compliant Example:** A valid polygon string.

-   **Non-Compliant Example:** An empty string ("").

-   **Critical Thinking:** Implementers must also consider "pitfalls for
    the naive," such as leading/trailing whitespace or non-printing
    characters, which should typically fail validation.

### 7.4 Execution Frameworks (non-normative)

The BDQ Test specifications (the Specification text in bdqffdq:hasExpectedResponse, plus any Parameters/defaults) are framework agnostic because they define only:

* What inputs are required (the `Information Elements` `Acted Upon` and `Consulted`, and any `Parameter` values),
* What outputs must be produced (a structured Response with Response.status, Response.result, Response.comment), and
* What decision logic must be followed (evaluate the criteria blocks in order and return the first applicable response),

…but they do not constrain:

* How data are stored (RDBMS, CSV, JSON, RDF, objects) or accessed.
* How records are streamed/batched/parallelized in a workflow.
* What programming language(s) are used.
* How methods are discovered/invoked (reflection, registry, function pointers, workflow nodes).
* How Responses are serialized/persisted (objects, rows, RDF bdqffdq:Assertion, annotations).

#### 7.4.1 What an execution framework must do between raw data and a Test implementation (non-normative)

A framework’s job is to act as the “adapter layer” that turns heterogeneous input into the canonical inputs/outputs implied by the ontology and the Test descriptors:

* Select the scope / unit of execution
  * Decide what constitutes a bdqffdq:SingleRecord (e.g., one Simple Darwin Core row; one dwc:Occurrence graph root) or a bdqffdq:MultiRecord (a dataset), and iterate accordingly.

* Bind raw data to the Test API
  * Map raw fields/properties onto the Test’s Information Elements:
    * provide the value(s) for the Acted Upon term(s),
    * provide any Consulted term(s),
    * supply Parameter argument values (or omit them and let defaults apply).
  * This is the core “plumbing” step: e.g. ensure dwc:countryCode actually lands in the method parameter that represents dwc:countryCode, etc. 
	* This could be via annotations, configuration, naming conventions, or explicit mapping code.
	* The FilteredPush implementations use Java Annotations for this purpose, but other frameworks could use different approaches.

* Invoke the correct implementation
  * Locate the right Implementation for a given Test (e.g., by Label, GUID/Term Name, or versioned IRI), then call it with the bound inputs.

* Capture and normalize outputs into a Response
  * Ensure every execution yields exactly one structured Response with:
    * Response.status from the controlled vocabulary,
    * Response.result present/absent as required by status and Test Type,
    * a Response.comment that is bdq:NotEmpty.
  * Optionally wrap/serialize as RDF assertions (bdqffdq:Assertion) or as W3C Annotations, as that representation choice is outside the Test itself.

* Present results to users and/or downstream processes
  * This could be as simple as logging, or as complex as a dashboard or API response.
  * BDQ is explicitly agnostic about this presentation layer.

* Manage common cross-cutting concerns
  * caching and retry for external authorities.
  * concurrency/parallel execution.
  * attaching Responses back to records.

In short: BDQ keeps Tests portable by standardizing semantics (inputs, decision rules, outputs), while leaving execution mechanics (binding, orchestration, serialization) to whatever framework fits the implementer’s environment.

## 8 Best Practices

1. **Atomic Tests**: Make each Test evaluate one single simple aspect of data quality.
1. **Start Simple**: Begin defining basic validation tests before considering more complex tests and amendments.
1. **Consider Edge Cases**: Include tests for empty values, nulls, and whitespace.
1. **Iterate**: Refine tests based on implementation feedback and real-world data.
1. **Use Established Authorities**: Reference widely accepted standards when possible.
1. **Generalize Appropriately**: Consider how different parts of the community might want to use a test in slightly different ways.
1. **Document Assumptions**: Be explicit about why paricular choices were made in the development of a test including choices of default values.
1. **Plan for Evolution**: Consider how tests might need to change over time.
1. **Consider Test Interactions**: Consider how multiple tests might interact on the same data.

## 9 Use an implementation for Quality Control (non-normative)

So, for our `Use Case` **Validated Distribution Authority** we have identified a set of specific tests to evaluate whether some data set is fit for the purpose of being used as a "validated distribution authority" for biodiversity science.  

Implicit in our `Use Case`, and we will want to spell this out explicitly, is that we want to use the results of these tests to find and fix errors in a data set, thus improving the quality of the data set for this purpose.  

The Fitness for Use Framework enables Tests to be used for either `Quality Control` (finding and fixing errors), or `Quality Assurance` (filtering a data set down to a subset of records that are fit for some purpose).

The mechanism that the Fitness for Use Framework uses for both of these is `MultiRecord` `Measures`, which are measures that take the results of multiple records from one or more tests, and combine those results in some way to produce a measure of the quality of the data set as a whole for some purpose.  For example, we could have a `MultiRecord Measure` that takes the results of the VALIDATION_FOOTPRINTWKT_NOTEMPTY test for all records in a data set, and counts the number of records that are COMPLIANT with that test, combining this count with the number of records in the data set gives us a measure of how many records are missing values in the dwc:footprintWKT field in that data set.  

**TODO: Return to UseCase->Policy->Test, and purpose of the use case being Quality Control (we want to find and fix errrors), thus develop/explain the multi-record measures needed for that purpose.**

### 9.1 MultiRecord Measures for Quality Control (non-normative)

The Fittness For Use Framework is intended to support two different but related purposes: `Quality Control` and `Quality Assurance`.  `Quality Control` is the process of finding and fixing errors in a data set, while `Quality Assurance` is the process of filtering a data set down to a subset of records that are fit for some purpose.  Both of these processes rely on an examination of the the results of `SingleRecord` Tests, but they use those results in different ways.  The `Use Case` we have been working with in this tutorial is focused on `Quality Control` (we want to fix problems in a dataset of distributions that would itself be used to evaluate other datasets), so we will examine on how to use the results of `SingleRecord` Tests for that purpose.

This tutorial has focused on defining `SingleRecord` Tests (primarily `Validations`) that evaluate one record at a time. In practice, `Quality Control` almost always requires a dataset-level view: curators, data managers, and developers need to know **how prevalent** a particular problem is, **where** it occurs, and **whether** proposed changes would measurably improve fitness for a `Use Case`.

In the BDQ Fitness for Use Framework, that dataset-level view is provided by `MultiRecord` `Measures` (`bdqffdq:Measure` with resource type `bdqffdq:MultiRecord`). These `Measures` operate over the collection of Responses (i.e., `Assertions`) produced by running one or more `SingleRecord` Tests across all records in a dataset, and they return a **single summary value** in `Response.result` (either a single number, or one of `COMPLETE`/`NOT_COMPLETE`).

#### 9.1.1 What a MultiRecord Measure takes as input (non-normative)

A `MultiRecord` `Measure` does not typically examine raw input (e.g. Darwin Core) values directly. Instead, it uses as input the outputs of `SingleRecord` Tests — the set of Responses with their `Response.status`, `Response.result`, and `Response.comment`.   `MultiRecord` `Measures` can also be defined to take raw data as input, for example, a `MultiRecord` `Measure` could be defined to calculate the average dwc:individualCount across all records in a dataset, but we won't conider that use of `MultiRecord` `Measures` here.

Conceptually what we want to do with `MultiRecord` `Measures` is:

1. Choose a `Use Case` (e.g., "Validated Distribution Authority"), and from the `ValidationPolicy` that relates the `Use Case' to `Validations`, the `SingleRecord` `Validation` Tests for that `Use Case`.
2. Run the relevant `SingleRecord` `Validation` Tests over all records in the dataset.
3. Collect the resulting Responses (`Assertions`).
4. Run one or more `MultiRecord` `Measures` that take these `Assertions` as input to summarize.
5. Act upon the results of those `MultiRecord` `Measures` to prioritize and direct `Quality Control` efforts (or filter records for `Quality Assurance`).

This separation on `Resource Type` (`SingleRecord` or `MultiRecord`) is important: it keeps each `SingleRecord` Test atomic and easy to implement, while providing a consistent, standards-aligned way to summarize results for dataset-level decision making.

#### 9.1.2 Two common patterns of MultiRecord Measures

BDQ includes (and encourages) two practical patterns of `MultiRecord` `Measures`:

**(A) Counts / prevalence measures (numeric results)**  
These return a single number, such as the count of records that are `COMPLIANT`, `NOT_COMPLIANT`, or have `INTERNAL_PREREQUISITES_NOT_MET` for a particular `SingleRecord` Test.

These are particularly useful for `Quality Control` because they let you:

- quantify the scale of a problem (e.g., “how many records are missing `dwc:footprintWKT`?”)
- prioritize work (fix the highest-impact problems first)
- track improvement over time (before/after a cleanup project, or between data releases)

**(B) Completeness-as-fitness measures (`COMPLETE` / `NOT_COMPLETE`)**  
These return `COMPLETE` if the dataset meets a dataset-level requirement derived from `SingleRecord` Test outcomes, and `NOT_COMPLETE` otherwise.

While these measures are central to formal `Quality Assurance` filtering, they can also support `Quality Control` by providing a clear “done/not done” indicator for a dataset with respect to a selected `Use Case` and its included Tests.

#### 9.1.3 Interpreting MultiRecord measures under Quality Control

A key idea in `Quality Control` is that dataset-level metrics should be interpreted in the context of the `Use Case`:

- A low count of `COMPLIANT` outcomes for a critical `Validation` indicates a major barrier to fitness for that `Use Case`.
- A high count of `INTERNAL_PREREQUISITES_NOT_MET` often points to upstream data capture or mapping gaps (e.g., a term not supplied at all, or supplied inconsistently).
- Changes in counts between a “pre-amendment” and “post-amendment” phase provide an estimate of how much quality could improve if proposed `Amendments` were accepted (or implemented by a curator).

Because `MultiRecord` `Measures` return only a single value, they are often paired with reporting or visualization outside of the Framework (e.g., spreadsheets, dashboards, or issue lists) that link summary counts back to the specific records needing attention.

#### 9.1.3.1 Constrast with Quality Assurance.

In contrast, in `Quality Assurance`, the focus is on filtering records based on `SingleRecord` Test outcomes.  The mechanism for this in the Fittness for Use Framework is to define a `MultiRecord` `Measure` that returns `COMPLETE` if the dataset meets a dataset-level requirement derived from `SingleRecord` Test outcomes, and `NOT_COMPLETE` otherwise, and if `NOT_COMPLETE`, filter out records until the `Measure` returns `COMPLETE`.   When all the `MultiRecord` `Measures` of this sort for a `Use Case` (as specified by `Policy`) are 'COMPLETE`, the filtered data set is fit for use with respect to the selected `Use Case`.

#### 9.1.4 A worked example (building on VALIDATION_FOOTPRINTWKT_NOTEMPTY)

Suppose we run `VALIDATION_FOOTPRINTWKT_NOTEMPTY` on a dataset of 10,000 records.

A `Quality Control` workflow commonly includes at least these dataset-level measures:

- A `MultiRecord` `Measure` that counts records where `Response.status=RUN_HAS_RESULT` and `Response.result=COMPLIANT` for `VALIDATION_FOOTPRINTWKT_NOTEMPTY`.
- A `MultiRecord` `Measure` that counts records where `Response.status=RUN_HAS_RESULT` and `Response.result=NOT_COMPLIANT` for the same `Validation`.
- Optionally, a `MultiRecord` `Measure` that counts `INTERNAL_PREREQUISITES_NOT_MET` outcomes (useful when prerequisites exist).

These counts tell you, at a glance, whether the dataset is close to meeting the needs of the `Use Case`, and whether effort should be directed toward data completion, remediation, or improved ingestion/mapping.

#### 9.1.5 Practical note: summary values vs. details

`MultiRecord` `Measures` are intentionally constrained to produce a single value in `Response.result`. If you need more detail than one number (for example, mean and standard deviation), implementations may place additional structured detail in `Response.qualifier` (as an extension point), while keeping `Response.result` to a single number as required for `Measure` outputs, but your preference should be to define additional `MultiRecord` `Measures` if you need multiple summary values, rather than overloading a single `Measure`, such as one `Measure` that counts Response.status `INTERNAL_PREREQUISITES_NOT_MET` and another that counts Response.result `NOT_COMPLIANT` outcomes.  Separating these into separate `Measures` keeps each `Measure` focused and easier to interpret and allows for more flexible reporting and visualization of the results to answer particular `Quality Control` questions.


In other words:

- `Response.result` answers “what is the one metric?”
- `Response.qualifier` (optional) can answer “what else helps interpret that metric?”

This pattern supports interoperability while still enabling rich `Quality Control` reporting in practical systems.


### 9.2 Quality Control Workflow

****************************

**TODO** Rework from here on, below not integrated yet.



### 11. Implementation Notes

Notes are present when some aspects of a test may not be obvious to the
casual user or implementer. In our case, no notes should be required,
but notes can be very helpful as in the example of the BDQ Test
[VALIDATION_COUNTRYCODE_STANDARD](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_0493bcfb-652e-4d17-815b-b0cce0742fbe):

> “Locations outside of a jurisdiction covered by a country code may
> have a value in the field dwc:countryCode, the ISO user defined codes
> include XZ used by the UN for installations on the high seas and
> suitable for a marker for the high seas. Also available in the ISO
> user defined codes is ZZ, used by GBIF to mark unknown countries. This
> test should accept both XZ and ZZ as COMPLIANT country codes. This
> test must return NOT_COMPLIANT if there is leading or trailing
> whitespace or there are leading or trailing non-printing characters.”

When a test provides an AMENDMENT (a proposed fix), it **MUST NOT** be
blindly applied to a "database of record" without human review, as
automated changes can have unintended consequences on sensitive data.

You can see that there are pitfalls for the naive. Just make sure that
the \`Expected Response\` doesn’t hide any edge cases. Easier said than
done sometimes: 11 years work went into the BDQ standard, and we were
often surprised by 'emergent properties’

## Round-Up

### 12. Documentation and Review

**Purpose**: Complete test specification for community review. Community
Review will be determined and managed by the BDQ Maintenance Group.

**Documentation Requirements**:

-   Clear rationale for test necessity

-   Examples of real-world data quality issues addressed

-   Implementation notes and warnings

-   Performance considerations

-   Relationship with other BDQ \`Tests\`




### 14. Framework Integration

This workflow integrates with the broader BDQ framework by:

-   **Connecting to Use Cases**: Tests are grounded in real user needs

-   **Supporting Fitness for Use**: Tests directly address data user
    requirements

-   **Enabling Quality Reports**: Standardized responses support
    automated reporting

-   **Facilitating Comparison**: Common structure allows comparison
    across implementations

### 15. Next Steps

After completing this workflow:

1.  The BDQ Maintenance Group will determine how new tests are proposed
    from time to time – this may include templates for new Tests and
    existing Test editing

2.  Implement test in your chosen programming language

3.  Validate implementation against test data

4.  Integrate into data quality assessment pipeline

5.  Contribute results back to the TDWG community

## Summary of the BDQ Philosophy

Through these steps, the BDQ standard aims to be **comprehensive but not
exhaustive**. By providing clear rationale, identifying abstract
**Information Elements**, and anchoring tests in community-vetted **Use
Cases**, the standard creates a stable framework for biodiversity
science.
