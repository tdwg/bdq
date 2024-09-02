# Quick Reference Guide to BDQ Core Tests

**Title**: Quick Reference Guide to BDQ Core Tests

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: <{standard_iri}>

**This version**: <{current_iri}{ratification_date}>

**Latest version**: <{current_iri}>

This document is intended to be an easy-to-read quick reference to the currently (as of 2024-xx-xx) BDQ Core Tests maintained as part of the BDQ Core standard.

Need help? Read more about BDQ Core in Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889, the BDQ Core Introduction, BDQ Core Users Guide, BDQ Core Implementers Guide or BDQ Core Vocabularies. Still have questions? Submit a new issue (question/problem) to the Issues form page (link) in GitHub. See the bottom of this document for how to cite BDQ Core.

Want to contribute? For information about how to contribute to the BDQ Core Standard, including how to propose changes, see the BDQ Core Guidelines for contributing.

This page is not part of the standard. It lists the BDQ Core tests by key descriptors defined below. Definitions, comments, and examples may include namespace abbreviations (e.g., “dwc:”). These are included to show that the meaning for the word it is attached to very specifically means the term as defined in that namespace. Thus, dwc:Event means Event as defined by Darwin Core at https://dwc.tdwg.org/terms/#event.

**"skos:prefLabel"** [normative]: A human readable label identifying the test.  These labels largely follow the pattern 
"type of test" "key information element acted upon" " TYPE_INFORMATIONELEMENT_STATUS. For example: "VALIDATION_COUNTRYCODE_STANDARD" [--- This is not the skos:pref format---]

**"IRI"** [normative]:A machine readable unique identifier for the test with a Date Last Updated. Example: "0493bcfb-652e-4d17-815b-b0cce0742fb " 

**"Name"** [normative] https://

**"Description"** [non-normative]: A non-technical description of what the test does, intended for consumers of data quality reports in concert with the Response.comment. Example: "Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?"

**"Darwin Core Class"** [non-normative]: The Information Element in the original terms of the framework, the general sort of information this test operates on. Example: "dwc:Location"  

**"Information Elements ActedUpon"** [normative]:A list of the specific Darwin Core terms that are the focus of the test.. Example: "dwc:countryCode" 

**"Specification"** [normative]: The specification for implementors describing the expected behavior of the test. Example: EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdq:Empty; COMPLIANT if the value of dwc:phylum was found as a value at the rank of Phylum by the bdq:sourceAuthority; otherwise NOT_COMPLIANT."  

**"Data Quality Dimension"** [normative]: The [bdqdim (http://rs.tdwg.org/bdqdim/terms) for this test. Example: "Conformance"

**"Criterion Label"** [non-normative]:  A label for the Criterion (TODO: Criterion/CriteronInContext applies to Validations, need to clarify for Dimension/DimensionInContext, Enhancement/EnhancementInContext, Issue/IssueInContext). Example: "Conformance: standard"

**"Resource Type"** [normative]: The type of resource on which this test acts, SingleRecord or MultiRecord, the CORE tests include Validations, Measures, and Amendments that operate on SingleRecords and a set of MultiRecord Measures that assess the results of the SingleRecord Validations. Example: "bdqffdq:SingleRecord"   

**"Examples"** [non-normative]: Example of inputs for a test and the expected output from an implementation of the test given those outputs.  A ’pass’ and a ‘fail’ example are provided for each test.  All examples listed are also present in the the validation test data. Example: "[dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"]"

**"Notes"** [non-normative]: Additional, guidance that may be necessary for the accurate implementation of the tests. Example: "Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters."  
