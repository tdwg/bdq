# Quick Reference Guide to BDQ Core Tests

**Title**: Quick Reference Guide to BDQ Core Tests

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: <{standard_iri}>

**This version**: <{current_iri}{ratification_date}>

**Latest version**: <{current_iri}>

This document is intended to be an easy-to-read quick reference to the currently (as of 2024-xx-xx) BDQ Core Tests and a subset of associated Descriptors maintained as part of the BDQ Core standard.

**Need help?** Read more about BDQ Core in Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889, the BDQ Core Introduction, BDQ Core Users Guide, BDQ Core Implementers Guide or BDQ Core Vocabularies. Still have questions? Submit a new issue (question/problem) to the Issues form page (link) in GitHub. See the bottom of this document for how to cite BDQ Core.

**Want to contribute?** For information about how to contribute to the BDQ Core Standard, including how to propose changes, see the BDQ Core Guidelines for contributing.

This page is not part of the standard. It lists the BDQ Core tests by key descriptors defined below. Definitions, comments, and examples may include namespace abbreviations (e.g., “dwc:”). These are included to show that the meaning for the word it is attached to very specifically means the term as defined in that namespace. Thus, dwc:Event means Event as defined by Darwin Core at https://dwc.tdwg.org/terms/#event.

---

**rdfs:Label** [normative]: A brief human-readable test label for consumers and implementors and using the structure TESTTYPE_INFORMATIONELEMENT_CRITERION e.g. VALIDATION_COUNTRYCODE_STANDARD.\
**skos:prefLabel** [normative]: A human readable label that follows the pattern 'Test Type' 'Focus Information Element' 'Criterion'. Example: "Validation dwc:countryCode Standard"\
**IRI** [normative]:A machine readable unique identifier with a Date Last Updated appended. Example: "0493bcfb-652e-4d17-815b-b0cce0742fb 2024-08-30"\ 
**Description** [non-normative]: A non-technical description of what the test does. Example: "Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?"\
**Darwin Core Class** [non-normative]: The focus dimension. Example: "dwc:Location"\
**Information Elements** [normative]:The Darwin Core terms that the test is focused on. Example: "dwc:countryCode"\
**Specification** [normative]: The concise logic of the test for implementors. Example: "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is EMPTY; COMPLIANT if there is a match of the contents of dwc:scientificName with the bdq:sourceAuthority; otherwise NOT_COMPLIANT"\
**Criterion Label** [non-normative] for Validations:  A label for the Criterion (TODO: Criterion/CriteronInContext applies to Validations, need to clarify for Dimension/DimensionInContext, Enhancement/EnhancementInContext, Issue/IssueInContext). Example: "Conformance: standard"\
**Resource Type** [normative]: What record type the tests operate on - 'SingleRecord' or 'MultiRecord'. Example: "bdqffdq:SingleRecord"\
**Examples** [non-normative]: 'Pass' and 'Fail' examples of inputs and outputs for the test from the Test Validation Data. Example: "[dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in bdq:sourceAuthority"]
[dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in bdq:sourceAuthority"]"\
**Use Cases** [non-normative]: One for more example use cases for the test. Example: "bdq:Record-Management", "bdq:alien-species"
Use Cases [non-normative] For Consumers and Implementors. Descriptions of data example quality needs that this test helps to support.

From https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqcore/index.md (TBA and some edits done to text, in case added)

ResourceType [normative] For implementors. The Resource Type that the test acts upon, SingleRecords or MultiRecords (data sets).
Information Elements For implementors and consumers, what terms do the test evaluate.
ActedUpon [normative]: A list of the specific Darwin Core terms that are the focus of the test. Example: "dwc:countryCode"
Consulted [normative]: A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon. For example, VALIDATION_ENDDAYOFYEAR_INRANGE tests whether or not dwc:endDayOfYear is in the range 1-365 or 1-366, consulting dwc:eventDate to see if the endDayOfYear falls in a leap year and 366 would be valid. The test makes the assertion of COMPLIANT or NOT_COMPLIANT about the Acted Upon term, and is not evaluating whether the Consulted dwc:eventDate conforms to expectations or not.
Parameters [normative]: Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain. Example: "bdq:taxonIsMarine.
Default Parameter Values [normative]: For Implementors. Default values for parameters to the test, including references to external authorities required for the test. Many parameters are sourceAuthorities, some are simple values.
Source Authority [normative]: An authority required for the test to be evaluated.  bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}.
Implementors Note: The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this exact string MUST be passed in as the parameter value for a test implementation to behave in the default manner. Other non-empty strings would select other source authorities. Implementations MAY regard empty values to be the Normative String Identifier.
Notes [non-normative]: For implementors and Consumers. Additional, guidance that may be necessary for the accurate implementation of the tests. Example: "Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters."
