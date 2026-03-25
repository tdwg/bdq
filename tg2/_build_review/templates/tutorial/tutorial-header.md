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

This document is also intended for those interested in describing new tests using the BDQ Fittness for Use Framework.

### 1.3 Associated Documents (non-normative)

For the list and links to all associated documents see [The Biodiversity Data Quality (BDQ) Standard](../../../index.md).

### 1.4 Status of the content of this document (normative)

This document is non-normative.

### 1.6 Namespace abbreviations (non-normative)

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
| xsd:         | http://www.w3.org/2001/XMLSchema#           |

## 2 Overview (non-normative)

This tutorial works through the development of a `Use Case`, then walks through two examples of the development of Tests.  One of the examples of a test is simple, the other is more complex.  This tutorial then comes back to the `Use Case` and describes how Measure Tests can be developed to evaluate the results of the Validation Tests for the purpose of `Quality Control`.  

The simpler of the two Tests examined is VALIDATION_FOOTPRINTWKT_NOTEMPTY, which was considered a ‘[Supplementary test](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md)’ rather than a BDQ \`Core\` test as we considered it of marginal use for the BDQ \`Use Cases\`. As noted in the [BDQ Supplement Information](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md), the test could be useful in certain \`Use Cases\`, as noted below.

**Note** that a proposed **BDQ Maintenance Group** will be established to maintain the BDQ Standard. This group will take responsibility for advising on processes for editing the BDQ standard and evaluating new BDQ \`Tests\`, \`Use Cases\` and other components of the BDQ Standard.

By following this workflow, you move from a human-centric research need to a machine-readable technical standard.

## 3 Tutorial Phase 1: Context and Strategy (The "Problem") (non-normative)

*Before defining a test, we must justify why it exists and how it fits into the broader ecosystem of the standard.*

### 3.1 Define the Use Case and Fitness-for-Use Requirements (non-normative)

**Purpose:** Establish the data user's perspective and fitness-for-use requirements

**The Reasoning:** A test is only as good as the problem it solves. We begin by establishing a clear perspective on who the data user is, what use the data are to be put, what makes the data "fit for use" for that use, and what problems in the data would make it unfit for that use. 

Clearly stating the problem that we are trying to solve ensures that the test is grounded in real-world needs and not just theoretical ideals.

* **User:** A conservation biologist.
* **Context:** We have a data set consisting of "Expert Distributions" of taxa.  We want to validate that this dataset is is usable for identifying outliers in other occurrence data (and for doing other things we may want to do with a set of expert distributions like drawing maps).  The data consist a taxon oriented data set (e.g. one record per taxon) with fields identifying the taxon, providing the expert distribution as geospatial data (vector data providing shapes rather than point occurrences), along with metadata about the source of each record. 
* **What makes data Fit for this Use?**: To be fit for this purpose each record in the data set must have:  A taxonomic name.  This taxonomic name can be found in a relevant authority on taxon names.  The taxon is also represented with a machine readable identifier.  The spatial footprint of the expert distribution of that taxon is provided as a polygon. That polygon is a valid shape.  Each taxon distribution has its source identified (the data set as a whole may have been compiled from multiple sources of taxon distributions.

Now we can define our `UseCase`.  We need to specify three elements, a name for the use case, a description, and a statement of fittness for use requirements.  We want to refine our statement of the problem into concise and clear statements.   (We will also need a unique identifier for the `UseCase` that software can use, but we won't examine these machine readable identifiers at this point).  

* **Name** Validated Distribution Authority
* **Description** Validating that Taxon oriented data can provide an authoritative resource for mapping known distributions of taxa, for identifying occurrence records in other data sets that have coordinates within the known ranges of taxa or are outliers, or for similar purposes.
* **hasFitnessRequirements** Data are fit for the `UseCase` "Validated Distribution Authority" and can provide a resource for validating that occurrence records are in range if they are taxon oriented data with fields identifying the taxon, providing expert validated distributions as geospatial data, along with metadata about the sources of the distributions.  To be fit for this purpose each record in the data set must have:
  * A taxonomic name is present and can be found in GBIF's backbone taxonomy.
  * A well formed machine readable identifier taxonomic name for that taxon is present.
  * A polygon providing the spatial footprint of the expert distribution for that taxon is present and valid.
  * Metadata providing the source for each taxon distribution is present.

It is helpfull, but by no means required, to state the `hasFitnessRequirements` as a brief summary paragraph followed by a set of brief bullet points.  The `UseCase` is describing what we are trying to accomplish at a high level, without getting too far into the details.  

### 3.2 Identify The Information Elements (non-normative)

**Purpose:** Determine which fields (mapped to vocabulary terms like Darwin Core terms) will in the data and are relevant to your use case.

Now let is consider in a little more detail what fields are present in the data that is to be evaluated and how can we map those fields onto terms in vocabularies like Darwin Core.  In the Fittnes for Use Framework, input fields or terms for a Test are generalized as `Information Elements`

We can expand each of the bullet points in the hasFitnessRequirements statement into a set of terms that are likely to map onto the data.  We may understand these well at the start, or as we consider data in the wild and start defining and implementing tests we will very likely need to come back and refine this list.

* A valid taxonomic name: 
  * dwc:scientificName
  * dwc:scientificNameAuthorship
* A machine readable identifier for the taxonomic name:
  *  dwc:scientificNameID
* A polygon of the taxon footprint: 
  * dwc:footprintWKT (the expert distribution)
  * dwc:geodeticDatum (for the footprintWKT)
* Metadata providing source for each taxon distribution: 
  * prov:wasAttributedTo (ORCiD)
  * foaf:name (Author name)
  * dcterms:source (publication or dataset source)  

Now, we want to identify a set of tests to be applied to these `Information Elements` to evaluate whether the data are fit for use.  

There are two key elements to the strategy at this point: (1) we want identify and use existing tests that can be applied before defining new tests and (2) we want each test to be as focused as possible on a single aspect of data quality.

### 3.3 Reuse of Existing Tests and Gap Analysis (non-normative)

**Purpose:** Identify existing tests that can be applied to the `Information Elements` and identify gaps where new tests are needed.

Lets identify which existing BDQ tests might already be able to apply to these `Information Elements` for this `Use Case`.

We can start with a simple presence check for each of these `Information Elements` and then add more complex tests as needed.

We are looking for existing `Validation` Tests, as we are trying to assert whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT).  By convention in BDQ, the names of these tests start with VALODATION_.  Simple presence tests for does an `Information Element` contain a value, by convention have a name that ends with  NOTEMPTY.   Between these two parts, again by convention, the name of the `Information Element` (or the name of a concept (e.g. LOCATION, EVENT) for several `Information Elements`)  being tested is included.

For example, VALIDATION_SCIENTIFICNAME_NOTEMPTY is a test that checks if there is a value in dwc:scientificName.

There are several places we could look for existing tests within BDQ, including the Quick Reference Guide, and the [index](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#31-index-to-validation-tests-non-normative) of the bdqtest: term-list document.  An easy place to look for Tests that operate on particular `Information Elements` is the Quick Reference Guide's [BDQ Test Index by Information Element Acted Upon](../terms/bdqtest/qrg_index_by_ie_actedupon.md#bdq-test-index-by-information-element-acted-upon-non-normative)

Looking here for simple presence checks for the `Information Elements` we can identify the following existing BDQ tests (and gaps):

* A valid taxonomic name is present: 
  * dwc:scientificName VALIDATION_SCIENTIFICNAME_NOTEMPTY
  * dwc:scientificNameAuthorshipa VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
* A machine readable identifier for the taxonomic name is present:
  *  dwc:scientificNameID VALIDATION_SCIENTIFICNAMEID_NOTEMPTY
* A polygon of the taxon footprint is present: 
  * dwc:footprintWKT **Gap**
  * dwc:geodeticDatum VALIDATION_GEODETICDATUM_NOTEMPTY
* Metadata providing source for each taxon distribution is present: 
  * prov:wasAttributedTo (ORCiD) **Gap**
  * foaf:name (Author name) **Gap**
  * dcterms:source (publication or dataset source) **Gap**

Our `Use Case' calls for more than just a presence check for these `Information Elements`, so we would want to fill in in more candiate tests for these `Information Elements`, until we've got tests that cover each of the hasFitnessRequirements we identified for the Use Case.  Filling in, for example, a few more tests:  

* A taxonomic name is present and can be found in GBIF's backbone taxonomy.
  * dwc:scientificName
    * VALIDATION_SCIENTIFICNAME_NOTEMPTY
    * VALIDATION_SCIENTIFICNAME_FOUND (check if the name can be found in an authority, GBIF's backbone taxonomy by default)
  * dwc:scientificNameAuthorship
    * VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY
* A well formed machine readable identifier taxonomic name for that taxon is present.
  * dwc:scientificNameID 
    * VALIDATION_SCIENTIFICNAMEID_NOTEMPTY
    * VALIDATION_SCIENTIFICNAMEID_COMPLETE (check if the identifier is well formed)

But, let's focus on the gaps.  There is somewhere else we want to check for potential tests that aren't already defined in BDQ, and that's the BDQ Issues in GitHub.

For dwc:footprintWKT, we could guess the name of the test, following the naming conventions, as VALIDATION_FOOTPRINTWKT_NOTEMPTY, and search the issues for [that name](https://github.com/tdwg/bdq/issues?q=VALIDATION_FOOTPRINTWKT_NOTEMPTY).  That does return a match, but it is a bit fragile, as the desired test might not have a name exactly matching that, and GitHub issue searches don't have good substring search support, so a better broader strategy is to search for: 

* Are there existing proposals tagged as [SUPPLEMENTARY](https://github.com/tdwg/bdq/issues?q=label%3ASupplementary) that would fill the desired gap.
* Are there existing proposals tagged as [DO NOT IMPLEMENT](https://github.com/tdwg/bdq/issues?q=label%3A%22DO%20NOT%20IMPLEMENT%22) that would fill the desired gap, but have been rejected for implementation, and should be reconsidered only with great caution.
* **Note that all of these issues in GitHub are Closed, the default issue search which includes is:open will not find them.**

So there is an existing definition for a test VALIDATION_FOOTPRINTWKT_NOTEMPTY, in the documented Supplementary tests.  

Looking at the description of that test we see:

* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY
* **Description** Is there a value in dwc:footprintWKT?
* **TestType** Validation
* **Information Elements Acted Upon** dwc:footprintWKT
* **Expected Response** COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

This is telling us, much like an entry in the Quick Reference Guide or the more detailed entry in the bdqtest: term-list document, that this test is a simple presence check for dwc:footprintWKT.

# 4 Defining a New Test (non-normative)

Let's walk through the steps and decisions involved in defining a test, using VALIDATION_FOOTPRINTWKT_NOTEMPTY as an example, and see how the components of the test are justified and how they fit together.

## 4.1 A Simple Description of the Test (non-normative)

The Description of the test is an easy-to-understand, concise explanation of what the test does. It is a human-oriented explanation.  It is a good starting point for defining a Test.

* **Description** “Is there a value in dwc:footprintWKT?”

As descriptions go, it doesn’t get simpler than that.

This description will also be used in Data Quality Reports to explain to users what the test is doing, so it should be clear and concise.  It should not include details about how the test might implemented, but it should provide just enough information for a user to understand what the test is checking for.

## 4.2 Identify the Information Elements (non-normative)

**Purpose** Identify the specific fields in the input data (Information Elements) that the test will evaluate.

For this test we want to evaluate one `Information Element`, dwc:footprintWKT, which is a term in Darwin Core that provides a polygon of the taxon footprint.  

An `Information Element` is classified as either `ActedUpon` or `Consulted`.  An `Information Element` is `ActedUpon` if it is the primary focus of the test, and it is `Consulted` if it is supporting information used to run the test.  In this case, dwc:footprintWKT is the primary focus of the test, so it is an `Information Element` that is `ActedUpon`.  This test does not require any supporting information, so there are no `Information Elements` that are `Consulted`.

## 4.3 Select the Test Type (non-normative)

**Purpose**: Determine in what way the test evaluates data quality.

There are four test types in BDQ: 

* **Validation** Assess whether data meet quality criteria (COMPLIANT/NOT_COMPLIANT)
* **Amendment** Propose improvements to data quality (AMENDED/NOT_AMENDED)
* **Measure** Quantify an aspect of data quality (numerical result) or measure completeness (COMPLTE/NOT_COMPLETE)
* **Issue** Flag potential problems for human review (POTENTIAL_ISSUE/NOT_ISSUE)  

We choose VALIDATION for this test because we are asserting whether data meets specific criteria (COMPLIANT vs. NOT_COMPLIANT).

## 4.4 Name The Test (non-normative)

**Purpose**: Create human and machine readable names for the test.

### 4.4.1 Anatomy of a Test Label (non-normative)

**The Reasoning:** BDQ uses a standardized naming pattern to ensure labels are predictable and descriptive: **TESTTYPE_INFORMATIONELEMENTS_EVALUATION**.

The use of all upper case with underscores is a convention inherited from the use of Java constants to identify tests in some early contributing projects.

The label provides a concise summary of the test's purpose and logic.  The components of the label are:

* **Test Type** one of VALIDATION, AMENDMENT, MEASURE, or ISSUE, as described above.
* **Information Elements** Expressed as the "simple English term" for the `Information Element` being evaluated, or if multiple `Information Elements` are being evaluated together, a suscinct more general concept (like LOCATION or EVENT) that encompasses those `Information Elements`
  * The use of "simple English terms" in the label (e.g., FOOTPRINTWKT) rather than the formal prefixed term (dwc:footprintWKT) to make it more accessible to human readers., and allows the label to be used as a string constant in many programming languages.
* **Evaluation:** What is the test testing? 
  * Examples of evaluations include "NOTEMPTY" (a value is present), “FOUND” (the value can be found in an authority), “INRANGE” (the value is within an expected range), etc.  See the bdq: vocabulary for a list of standard criteria,

This test is a Validation, it is evaluating the Information Element dwc:footprintWKT, and it is evaluating whether there is a value in dwc:footprintWKT, so the label is VALIDATION_FOOTPRINTWKT_NOTEMPTY.  This label is expected to be a constant that does not change, even in translation.

In order to support accessibility (the ability of screen readers to read the label in a more human friendly way), and to provide for translations of the name of the test into additional languages we will also want to create a Preferred Label for the test.

The Preferred Label for this test could be "Validation dwc:footprintWKT Not Empty".  This Preferred Label is expected to be translated into different languages.

This gives us the following names for the test: 
* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY
* **Preferred Label** Validation dwc:footprintWKT Not Empty 

### 4.4.2 Identifiers supporting software and developers (non-normative)

While the label is a human-friendly identifier for the test, we need a machine-readable identifier that can be used by software to identify the test.  In BDQ, this is the `Term Name`, which is a UUID.  This allows software to unambiguously identify the test, and to ensure that a search for the test results in only this specific test being identified/located.

We also need to provide a date for the test definition, and to update that date if the test definition is modified.

This gives us the following additional properties for the test:
* **Term Name** c6b705fc-7cf8-4af1-88ab-7a38d85f7109 
* **Modified** 2024-01-29

(Once accepted into BDQ, these properties would be combined to form the fully qualified Term IRI for the test (e.g. https://rs.tdwg.org/ bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933) and the Term Version IRI for a particular version of the test (e.g. https://rs.tdwg.org/ bdqtest/terms/version/07c28ace-561a-476e-a9b9-3d5ad6e35933-2024-07-24))

## 4.5 Identify the Data Quality Dimension and Criterion (non-normative)

**Purpose**: Classify the test according to the aspect of data quality it addresses.

All BDQ Tests are related to some dimension of data quality.  These are formally defined in the bdqdim: vocabulary.

BDQ Data Quality Dimensions include:
* **Completeness**: Are all required data elements present?
* **Conformity**: Do data values conform to format, syntax, or controlled vocabularies?
* **Consistency**: Are data values logically consistent with each other?
* **Likeliness**: Do data values fall within expected ranges or distributions?
* **Resolution**: Is the level of detail appropriate for the intended use?

The question we wish to ask is whether there is a value in dwc:footprintWKT.  In this test we are only asking if any value is present, we are not asking if it is correctly formatted Well Known Text spatial data, or whether it contains in range values, or anything else, we are simply asking if any value is present.  So this test is addressing the Completeness dimension of data quality.

This seems a very trivial test.  It is.  That is important.  We do not wish to overcomplicate our tests.  We want to ask simple questions that are easy to understand and implement, and that address specific aspects of data quality.  This test is a simple presence check for dwc:footprintWKT, and it is exactly the simple presence check we need for our `Use Case`.  If some data are absent and other data are incorrectly formatted, a more complicated test that checks for both presence and correct formatting will not be able to distinguish between these two problems, and thus will not be as useful for our `Use Case` as a simple presence check (combined with a separate test to assess correct formatting).

BDQ `Validations` also have a `Criterion` property.  Each Criterion represents an abstract way of evaluating whether a data value meets expectations for a particular Use Case.  These are formally defined int he bdqcrit: vocabulary.  For example, the Criterion `NotEmpty` is defined as "The data value is not empty (i.e., it contains some data)".  This is exactly the criterion we are applying in this test, so we will use the `NotEmpty` criterion for this test.  

## 4.6 How many records are we examining at once? (non-normative)

**Purpose**: Determine whether the test is applied to single records or multiple records.

In BDQ, tests can be applied to single records or to multiple records.  A test that is applied to a single record is called a "SingleRecord" test, and a test that is applied to multiple records is called a "MultiRecord" test.  The distinction between these two types of tests is important because it affects how the test is implemented and how the results are interpreted.

We wish to step through the input data set one record at a time and for each record assess whether or not there is a value in dwc:footprintWKT.  Thus we are applying this test to single records, and thus this is a "SingleRecord" test.  

We will come back later and define another test to measure how much of the data set is compliant for this test, and that will be a "MultiRecord" test, but for now we are just defining a simple presence check for dwc:footprintWKT that is applied to single records.

## 4.7 Define the Test Specification (non-normative)

**Purpose**: Provide a clear, unambiguous description of the test's logic and expected outcomes.

Let's start with the question the test is asking, very simply phrased:  **Is there a value in dwc:footprintWKT?**

Now, lets phrase that question in a way that provides clear and unambigouus guidance to a developer who will implement the test.  The phrasing follows a standard structure and terminology in the BDQ standard (TODO: See ****).   

Since this is a `Validation`, the test will return either COMPLIANT or NOT_COMPLIANT.  The test will return COMPLIANT if there is a value in dwc:footprintWKT, and it will return NOT_COMPLIANT if there is not a value in dwc:footprintWKT.  We can phrase this as follows:

**Expected Response** COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

## 4.8 List the properties of the Test (non-normative)

**Purpose**: Create a human-readable label for the test and list its properties in a structured format.

Now let's put all of this together into a structured format that lists the properties of the test, including its label, description, test type, information elements acted upon, and expected response.  See the bdqtest: term-list document for examples (like the very similar [VALIDATION_COUNTRYCODE_NOTEMPTY](../list/bdqtest/index.md#bdqtest_853b79a2-b314-44a2-ae46-34a1e7ed85e4).  For our test, we have:

* **Description** Is there a value in dwc:footprintWKT?
* **Label** VALIDATION_FOOTPRINTWKT_NOTEMPTY 
* **Preferred Label** Validation dwc:footprintWLT Not Empty 
* **Term Name** c6b705fc-7cf8-4af1-88ab-7a38d85f7109 
* **Modified** 2024-01-29
* **Test Type** Validation
* **Data Quality Dimension** Completeness
* **Resource Type** SingleRecord
* **Criterion** NotEmpty
* **Information Elements Acted Upon** dwc:footprintWKT
* **Expected Response** COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

To formally express this test in RDF we would need to add some more identifiers and structures, but the above are the key properties that define the test and provide the information needed for an implementer to understand and implement the test.  See the bdqffdq: ontology guide for details about the full formal structure.

### 4.6.1 Summary of the Test Definition

So, VALIDATION_FOOTPRINTWKT_NOTEMPTY is is a `Validation` test, that takes dwc:footprintWKT as input, and askes a very simple question, "Is there a value in dwc:footprintWKT?", This question is spelled out very clearly for an implementer in the `Expected Response`.  The expected response is COMPLIANT if there is a value in dwc:footprintWKT, and NOT_COMPLIANT if there is not a value.  This is exactly the simple presence check we need for our `Use Case`.

Thus we could include this test in our `Use Case`, even though it is not yet accepted into the BDQ standard (and we could implement it, test the implementation, and put it forward to the Maintinence group for consideration for inclusion in the standard). This test would fill the gap of a simple presence check for dwc:footprintWKT.

# 5 Defining a more complicated Test (non-normative)

The next gap we identified in the 'Use Case'  

** prov:wasAttributedTo (ORCiD is present) **Gap**

TODO: describe this test briefly.

Then: Next Gap: 

** prov:wasAttributedTo (ORCiD is valid) **Gap**

TODO: Repeate the logic, but here add in source authority, and then recongnise that a parameter is needed to allow for alternative authorities like VIAF, as the test can be more general than just ORCiD, and thus more broadly applicable.

TODO: Then return to UseCase->Policy->Test, and purpose of the use case being Quality Control (we want to find and fix errrors), thus develop/explain the multi-record measures needed for that purpose.

---------

**TODO: Work the correct parts of the following text from Lee into section 4 above.**

### 5. Selecting the Test Mechanism
**??? Mechanism?  That is software that implements Tests, what is described here is the Data Quality Need** 

The test type is the first part of the test label

**The Choice:** Why VALIDATION? The choices we have are

-   **VALIDATION**: Asserts whether data meets quality criteria
    (COMPLIANT/NOT_COMPLIANT)

-   AMENDMENT: Proposes improvements to data quality
    (AMENDED/NOT_AMENDED)

-   MEASURE: Quantifies an aspect of data quality (numerical result)

-   ISSUE: Flags potential problems for human review
    (POTENTIAL_ISSUE/NOT_ISSUE)

We chose a **Validation** test (\`Mechanism\`) because we are asserting
whether data meets a specific \`Criterion\` (\`COMPLIANT\` vs.
NOT_COMPLIANT).

**Reasoning for Simplicity:** At this stage, we are not validating the
*contents* or *mathematical structure* of the WKT polygon—only that it
contains some data. We could add to a workflow for example, by adding
subsequent tests for validating the contents of dwc:footprintWKT, but
focusing on a "limited specific aspect" of data is a core principle of
the standard.

## Phase 3: Formal Specification (The "Blueprint")

*This phase provides the unambiguous technical details required for a
developer to implement the test.*

### 6. Technical Identity (ActedUpon vs. Consulted)

**??This is is about information elements, not about the specification???**

This component of the \`Specification\` focuses on the terms that the
test requires to run. BDQ calls all the terms \`Information Elements\`
and generally assumes that these are predominantly [Darwin Core
terms](https://dwc.tdwg.org/list/). There are two of \`Information
Elements\`-

**The Distinction:**

-   **ActedUpon:** The primary focus (in this case, dwc:footprintWKT).

-   **Consulted:** Supporting information used to run the test (none
    required for this simple presence check).

### 7. Expected Response and Namespaces

The *phrasing* of the \`Specification\` should follow the structure and
terminology in the BDQ standard, see the BDQ Tests and Assertions
document. In our new test, we could use the following phrase-

> COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise NOT_COMPLIANT

**The Technical Logic:**

-   **Status (RUN_HAS_RESULT):** Indicates the test executed
    successfully.

-   **Result (COMPLIANT vs. NOT_COMPLIANT):** Follows the formula:
    *"COMPLIANT if dwc:footprintWKT is bdq:NotEmpty; otherwise
    NOT_COMPLIANT"*.

-   **Justification for bdq: Prefix:** We prefix NotEmpty with bdq: to
    ensure the test uses the standard's explicit definition of
    "\`Empty\`", preventing ambiguity during implementation.

**TODO: Work this into section 5**

### **8.** Defining Prerequisites and Authorities

This component of a test is required IF it must reference some
authorities outside the BDQ namespaces (the ontology or vocabularies
that form the BDQ standard). These are external dependencies and
therefore are outside the domain and responsibility of BDQ.

As noted in the BDQ documentation, many aspects of ‘data quality’ or
‘fitness for use’ cannot be evaluated IF no authority exists to which to
evaluate data values.

BDQ details the structure and format of source authorities as follows

> bdq:sourceAuthority default = “Name of Authority” {\[URL\]}{optional
> API name if available\[URL of the API\]}

And here are two examples:

-   bdq:sourceAuthority default = "ISO 3166 Country Codes"
    {\[https://www.iso.org/iso-3166-country-codes.html\]} {ISO
    3166-1-alpha-2 Country Code search
    \[https://www.iso.org/obp/ui/#search\]}

-   bdq:sourceAuthority default = "The Getty Thesaurus of Geographic
    Names (TGN)"
    {\[https://www.getty.edu/research/tools/vocabularies/tgn/index.html\]}

In our \`Use Case\`, we are only referring to the presence of ANY value
in one Darwin Core term: dwc:footprintWKT, so no bdq:sourceAuthority is
required.

**Prerequisites**: This test does not require external authorities (like
\`ISO\` codes) or internal prerequisites (like a latitude being a
number).

**Justification**: Because we are only checking for the presence of
*any* value, it is a self-contained check.


**TODO: Work this into section 5**

### 9. Parameters

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

**TODO: Work this into section 4** 

## Phase 4: Validation and Community (The "Real-World")

*No test is final until it is implemented and thrown at actual data to
confirm it responds correctly.*

### 10. Test Data and Edge Cases

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
often surprised by ‘emergent properties’

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

### 13. Best Practices

1.  **Start Simple**: Begin with basic validation tests before complex
    amendments

2.  **Consider Edge Cases**: Include tests for empty values, nulls, and
    whitespace

3.  **Use Established Authorities**: Reference widely accepted standards
    when possible

4.  **Document Assumptions**: Be explicit about interpretations and
    defaults

5.  **Plan for Evolution**: Consider how tests might need to change over
    time

6.  **Test Interactions**: Consider how multiple tests might interact on
    the same data

**TODO: Section on MultiRecord Measures and Quality Control goes here**


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
