# Terms used in the Quick Reference Guide to BDQ Core Tests

Title
: Terms used in the Quick Reference Guide to BDQ Core Tests

Part of the [BDQ Core Tests Quick Reference Guide](index.md)

<!-- This is the list of descriptions of bdqcore terms included in the Quick Reference Guide. -->

<!-- Generated list, TODO: Doesn't include all terms. -->

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Comments (rdfs:comment) | non-normative | A description of the subject resource. | Information elements such as DATE and DAY are abstract, they could reference any representation of those concepts.  In contrast, dwc:eventDate and dwc:day can be linked to concrete Acted Upon or Consulted information elements. |
| Definition (skos:definition) | normative | A statement or formal explanation of the meaning of a concept. TDWG SDS: The normative definition of the term, written in English. | An InformationElement described in abstract terms and not linked with one or more concrete terms. |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. | Abstract Information Element |
| Preferred Label (skos:prefLabel) | normative | The preferred lexical label for a resource, in a given language. | Abstract Information Element |
| Type (rdf:type) | normative | The subject is an instance of a class. | [http://www.w3.org/2002/07/ owl#Class](http://www.w3.org/2002/07/owl#Class) |
| Term IRI (dcterms:isVersionOf) | normative | A related resource of which the described resource is a version, edition, or adaptation. TDWG SDS: The HTTP IRI that uniquely identifies the current term. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |
| Term Name (rdf:value) | normative | Idiomatic property used for structured values. TDWG SDS: The term name is a controlled value that represents the class, property, or concept described by the term definition. | [https://rs.tdwg.org/ bdqffdq/terms/ AbstractInformationElement](https://rs.tdwg.org/bdqffdq/terms/AbstractInformationElement) |


<!-- Original separately created list -->

**rdfs:Label** [normative]: A brief human-readable label for consumers and implementers using the structure TESTTYPE_INFORMATIONELEMENT_CRITERION (e.g., VALIDATION_COUNTRYCODE_STANDARD)

**skos:prefLabel** [normative]: A human readable label that follows the pattern 'Test Type' 'Focus Information Element' 'Criterion'. Example: ```Validation dwc:countryCode Standard```

**Term Version IRI** [normative]: A machine readable unique identifier with a Date Last Updated appended. Example: ```0493bcfb-652e-4d17-815b-b0cce0742fb 2024-08-30```

**Resource Type** [normative]: What record type a test operates on - 'SingleRecord' or 'MultiRecord'. Example: ```bdqffdq:SingleRecord```

**Description** [non-normative]: A non-technical description of what the test does. Example: ```Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?```

**Specification** [normative]: The concise logic of the test for implementers. Example:```EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is EMPTY; COMPLIANT if there is a match of the contents of dwc:scientificName with the bdq:sourceAuthority; otherwise NOT_COMPLIANT```

**Information Elements ActedUpon** [normative]: For implementers and consumers. A list of Darwin Core terms that are the focus of the test. Example: ```dwc:countryCode```

**Information Elements Consulted** [normative]: A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon. Example: ```dwc:country```

**Parameters** [normative]: Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain. Example: ```bdq:taxonIsMarine```

**Default Parameter Values** [normative]: The default values for any bdq:sourceAuthority and any parameters used in the Specification that define the default behavior of the test. Example: ```bdq:maximumValidElevationInMeters default = "8850"```

**Examples** [non-normative]: 'Pass' and 'Fail' examples of inputs and outputs for the test from the Test Validation Data. Example: ```[dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in bdq:sourceAuthority"]
[dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in bdq:sourceAuthority"]```

**Use Cases** [non-normative]: For Consumers and Implementers. Descriptions of data example quality needs that this test helps to support. Example: ```bdq:Record-Management, bdq:Alien-Species```

**Notes** [non-normative]: For implementers and Consumers. Additional guidance that may be necessary for the accurate implementation of the tests. Example: ```Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters.```


## Acronyms

For a list of Acronyms see [Acronyms](../../intro/index.md#5-acronyms) in the Introduction document.

## Glossary

A glossary of terms additional to those in the various namespaces can be found at [Glossary](../../intro/index.md#6-glossary) in the Introduction document.

## References

The bibliography for BDQ Core is in the [References](../../references/index.md#2-references) document.

## Cite BDQ Core

**To cite BDQ Core in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889

**To cite the standard document upon which this page is built, use the following:**

BDQ Core Maintenance Group 2024. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/bdq/doc/list/

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. BDQ Core Quick Reference Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqcore/terms/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)

