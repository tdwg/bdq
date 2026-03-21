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

## Overview

This tutorial provides the reasoning, technical justifications, and
logical choices behind the creation of a new Biodiversity Data Quality
(BDQ) test, using the specific example VALIDATION_FOOTPRINTWKT_NOTEMPTY.
This test was considered a ‘[Supplementary test](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md)’
rather than a BDQ \`Core\` test as we considered it of marginal use for
the BDQ \`Use Cases\`. As noted in the [BDQ Supplement
Information](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/supplement/index.md),
the test could be useful in certain \`Use Cases\`, as noted below.

**Note** that a proposed **BDQ Maintenance Group** will be established
to maintain the BDQ Standard. This group will take responsibility for
advising on processes for editing the BDQ standard and evaluating new
BDQ \`Tests\`, \`Use Cases\` and likely more.

By following this workflow, you move from a human-centric research need
to a machine-readable technical standard.

## Phase 1: Context and Strategy (The "Problem")

*Before defining a test, we must justify why it exists and how it fits
into the broader ecosystem of the standard.*

### 1. Define the Use Case and Fitness-for-Use

**The Reasoning:** A test is only as good as the problem it solves. We
begin by establishing a clear perspective on who the data user is and
what makes the data "fit for use" for them.

-   **User:** A conservation biologist.

-   **Context:** Identifying candidate data records to validate
    observations for "Expert Distributions" of taxa.

-   **Justification:** For this context, coordinates alone are
    insufficient; a polygonal footprint (dwc:footprintWKT) defining the
    observed area must be present.

<!-- -->

-   **Fitness for Use Requirements**:

    -   A valid taxonomic name (dwc:scientificName)

    -   An observation date (dwc:eventDate)

    -   Geographic coordinates present and accurate to within 100m
        (dwc:decimalLatitude, dwc:decimalLongitude,
        dwc:coordinateUncertaintyInMeters)

    -   A polygon of the taxa footprint (candidate expert distribution)
        must be present (dwc:footprintWKT).

    -   The records have not been annotated

    -   The records have not had their locations generalized to a grid
        or similar

What our \`Use Case\` needs is a validated taxa with ‘accurate’
coordinates and a dwc:footprintWKT (a polygonal footprint) that defines
the area where the taxon was observed. The proposed Test will only need
to confirm the presence of a non-empty dwc:footprintWKT, as existing BDQ
Tests will cover other requirements.

### 2. Gap Analysis and Test Suites

**The Strategy:** Do not attempt to incorporate all criteria into a
single test. Instead, identify which existing BDQ tests already
contribute to the use case.

-   **Existing Support:** Tests for valid coordinates, scientific names,
    and event dates already exist e.g.,

    -   [VALIDATION_COORDINATES_NOTZERO](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_1bf0e210-6792-4128-b8cc-ab6828aa4871) 

    -   [VALIDATION_COORDINATEUNCERTAINTY_INRANGE](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_c6adf2ea-3051-4498-97f4-4b2f8a105f57) 

    -   [VALIDATION_DECIMALLATITUDE_INRANGE](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_b6ecda2a-ce36-437a-b515-3ae94948fe83) 

    -   [VALIDATION_DECIMALLONGITUDE_INRANGE](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_0949110d-c06b-450e-9649-7c1374d940d1)

    -   [VALIDATION_EVENTDATE_STANDARD](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_4f2bf8fd-fc5c-493f-a44c-e7b16153c803) 

    -   [VALIDATION_SCIENTIFICNAME_FOUND](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_3f335517-f442-4b98-b149-1e87ff16de45) 

    -   [ISSUE_ANNOTATION_NOTEMPTY](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1)

    -   [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md#bdqtest_13d5a10e-188e-40fd-a22c-dbaa87b91df2) 

-   **The Gap:** Our proposed test only needs to confirm the presence of
    a non-empty dwc:footprintWKT, filling the specific missing
    requirement for this use case.

## Phase 2: Identity and Logic (The "Naming")

*This phase creates the machine and human-readable identifiers that
allow the test to be discovered and readily understood.*

### 3. A Simple Description of the Test

The Description of the test is an easy-to-understand, concise
explanation of what the test does. It is a human-oriented explanation.

> “Is there a value in dwc:footprintWKT?”

As descriptions go, it doesn’t get simpler than that.

### 4. Anatomy of a Test Label

**The Reasoning:** BDQ uses a standardized naming pattern to ensure
labels are predictable and descriptive:
**TESTTYPE_INFORMATIONELEMENTS_EVALUATION**.

-   **The Choice:** The use of "simple English terms" in the label
    (e.g., FOOTPRINTWKT) rather than the formal prefixed term
    (dwc:footprintWKT) to make it more accessible to human readers.

-   **Globally Unique Identifier:** While the label is human-friendly,
    the \`**GUID\`** is the primary key used by machines to ensure that
    a search results in only this specific test. Note: The GUID
    <u>IS</u> the key identifier for the test. It has to be globally
    unique, in that for example, a Google search will result in ONLY
    this test being identified/located. The test Label uses a
    combination developed by BDQ that follows the pattern.

-   **Evaluation:** What is the test testing? Examples of evaluations
    include “**COMPLETE”, “FOUND”, “INRANGE”, “STANDARD”,** etc

### 5. Selecting the Test Mechanism

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
