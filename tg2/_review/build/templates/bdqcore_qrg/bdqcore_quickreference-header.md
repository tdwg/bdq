# Quick Reference Guide to BDQ Core Tests

**Title**: Quick Reference Guide to BDQ Core Tests

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: <{standard_iri}>

**This version**: <{current_iri}{ratification_date}>

**Latest version**: <{current_iri}>

**Audience** This document is intended to be an easy-to-read quick reference to the current BDQ Core Tests using a subset of Descriptors maintained as part of the BDQ Core standard.

**Need help?** See "Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889", the BDQ Core Introduction (link), BDQ Core Users Guide (link), BDQ Core Implementers Guide (link) and BDQ Core Vocabularies (link). Still have questions? Submit a new issue to the Issues form page (link) in GitHub. See the bottom of this document for how to cite BDQ Core.

**Want to contribute?** For information about how to contribute to the BDQ Core Standard, including how to propose changes, see the BDQ Core Guidelines for contributing.

This page lists the BDQ Core tests by key descriptors defined below. Definitions, comments, and examples may include namespace abbreviations (e.g., “dwc:”). These are included to show that the meaning for the word it is attached to, specifically means the term as defined in that namespace. Thus, dwc:Event means Event as defined by Darwin Core at https://dwc.tdwg.org/terms/#event.

---

**rdfs:Label** [normative]: A brief human-readable label for consumers and implementors using the structure TESTTYPE_INFORMATIONELEMENT_CRITERION e.g. VALIDATION_COUNTRYCODE_STANDARD\
**skos:prefLabel** [normative]: A human readable label that follows the pattern 'Test Type' 'Focus Information Element' 'Criterion'. Example: "Validation dwc:countryCode Standard"\
**Versioned IRI** [normative]:A machine readable unique identifier with a Date Last Updated appended. Example: "0493bcfb-652e-4d17-815b-b0cce0742fb 2024-08-30"\
**Resource Type** [normative]: What record type the tests operate on - 'SingleRecord' or 'MultiRecord'. Example: "bdqffdq:SingleRecord"\
**Description** [non-normative]: A non-technical description of what the test does. Example: "Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?"\
<!--- Darwin Core Class isn't present in the RDF, part of rationale management, not terms --->
<!--- **Information Element Class** [non-normative]: The focus Darwin Core Class. Example: "dwc:Location"\--->
**Specification** [normative]: The concise logic of the test for implementors. Example: "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is EMPTY; COMPLIANT if there is a match of the contents of dwc:scientificName with the bdq:sourceAuthority; otherwise NOT_COMPLIANT"\
**Information Elements ActedUpon** [normative]: For implementors and consumers. A list of Darwin Core terms that are the focus of the test. Example: "dwc:countryCode"\
**Information Elements Consulted** [normative]: A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon. Example: "dwc:country"\
**Parameters** [normative]: Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain. Example: "bdq:taxonIsMarine.\
**Default Parameter Values** [normative]: The default values for any bdq:sourceAuthority and any paramters used in the Specification that define the default behavior of the test. Example: bdq:maximumValidElevationInMeters default = "8850" .\
**Examples** [non-normative]: 'Pass' and 'Fail' examples of inputs and outputs for the test from the Test Validation Data. Example: "[dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in bdq:sourceAuthority"]
[dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in bdq:sourceAuthority"]"\
**Use Cases** [non-normative]: For Consumers and Implementors. Descriptions of data example quality needs that this test helps to support. Example: "bdq:Record-Management", "bdq:alien-species"
**Notes** [non-normative]: For implementors and Consumers. Additional, guidance that may be necessary for the accurate implementation of the tests. Example: "Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters."\

## The Tests (normative)

TODO: When this becomes template, product will embed quick reference guide here instead of linking.

[List of Tests to go in Quick Reference Guide](https://github.com/tdwg/bdq/blob/master/tg2/core/generation/docs/core_tests_quick_reference.md)