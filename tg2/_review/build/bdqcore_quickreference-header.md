# Quick Reference Guide to BDQ Core Tests

**Title**: Quick Reference Guide to BDQ Core Tests

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: <{standard_iri}>

**This version**: <{current_iri}{ratification_date}>

**Latest version**: <{current_iri}>

---

This document is intended to be an easy-to-read quick reference to the currently (as of 2024-xx-xx) BDQ Core Tests maintained as part of the BDQ Core standard.

Need help? Read more about BDQ Core in Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889, the BDQ Core Introduction, BDQ Core Users Guide, BDQ Core Implementers Guide or BDQ Core Vocabularies. Still have questions? Submit a new issue (question/problem) to the Issues form page (link) in GitHub. See the bottom of this document for how to cite BDQ Core.

Want to contribute? For information about how to contribute to the BDQ Core Standard, including how to propose changes, see the BDQ Core Guidelines for contributing.

This page is not part of the standard. It lists the BDQ Core tests by key descriptors defined below. Definitions, comments, and examples may include namespace abbreviations (e.g., “dwc:”). These are included to show that the meaning for the word it is attached to very specifically means the term as defined in that namespace. Thus, dwc:Event means Event as defined by Darwin Core at https://dwc.tdwg.org/terms/#event.

---

**IRI** [normative]:A machine readable unique identifier with a Date Last Updated appended. Example: "0493bcfb-652e-4d17-815b-b0cce0742fb 2024-08-30" 
**skos:prefLabel** [normative]: A human readable label that follows the pattern 'Test Type' 'Focus Information Element' 'Criterion'. Example: "Validation dwc:countryCode Standard"
**Description** [non-normative]: A non-technical description of what the test does. Example: "Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?"
**Darwin Core Class** [non-normative]: The focus area. Example: "dwc:Location"  
**Information Elements ActedUpon** [normative]:The Darwin Core terms focused on. Example: "dwc:countryCode" 
**Specification** [normative]: The concise logic of the test for implementors. Example: "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is EMPTY; COMPLIANT if there is a match of the contents of dwc:scientificName with the bdq:sourceAuthority; otherwise NOT_COMPLIANT"  
**Criterion Label** [non-normative] for Validations:  A label for the Criterion (TODO: Criterion/CriteronInContext applies to Validations, need to clarify for Dimension/DimensionInContext, Enhancement/EnhancementInContext, Issue/IssueInContext). Example: "Conformance: standard"
**Resource Type** [normative]: What record type the tests operate on - 'SingleRecord' or 'MultiRecord'. Example: "bdqffdq:SingleRecord"   
**Examples** [non-normative]: 'Pass' and 'Fail' examples of inputs and outputs for the test from the Test Validation Data. Example: "[dwc:countryCode="GL": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value"]
[dwc:countryCode="GRL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value"]"
