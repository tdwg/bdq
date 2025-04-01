# Terms used in the Quick Reference Guide to BDQ Core Tests

Title
: Terms used in the Quick Reference Guide to BDQ Core Tests

Part of the [BDQ Core Quick Reference Guide](index.md)

<!-- This is the list of descriptions of bdqcore terms included in the Quick Reference Guide. -->

<!-- Generated list, approximates the correct set of term definitions, labels don't fully match and not all items are labeled. -->

{term_key}

<!-- Original separately created list of term definitions TODO: Remove when generated list above is correct -->

**rdfs:label** [normative]: A human-readable label following the pattern `TESTTYPE_INFORMATIONELEMENT_CRITERION`. This can be thought of as the name of the Test. Example: ```VALIDATION_COUNTRYCODE_STANDARD```

**skos:prefLabel** [normative]: The preferred human-readable label following the pattern `Test Type Focus Information Element Criterion`. Example: ```Validation dwc:countryCode Standard```

**Term Version IRI** [normative]: A machine-readable unique identifier with a version in the form of a Date Last Updated appended. Example: ```0493bcfb-652e-4d17-815b-b0cce0742fb 2024-08-30```

**Resource Type** [normative]: The type of record a Test operates on - 'SingleRecord' or 'MultiRecord'. Example: ```bdqffdq:SingleRecord```

**Description** [non-normative]: A non-technical description of what the Test evaluates. Example: ```Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?```

**Specification** [normative]: The concise logic of the Test for implementers. Example:```EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is EMPTY; COMPLIANT if there is a match of the contents of dwc:scientificName with the bdq:sourceAuthority; otherwise NOT_COMPLIANT```

**Information Elements ActedUpon** [normative]: A list of Darwin Core terms that are the focus of the Test. Examples: ```dwc:countryCode```, ```dwc:decimalLatitude, dwc:decimalLongitude```

**Information Elements Consulted** [normative]: A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon. Example: ```dwc:minimumDepthInMeters, dwc:maximumDepthInMeters```, ```dwc:verbatimDepth```

**Parameters** [normative]: Any parameters that change the behavior of the Test for a subset of users with special data quality needs. Example: ```bdq:taxonIsMarine```, ```bdq:earliestValidDate,bdq:latestValidDate```

**Default Parameter Values** [normative]: The default values for any bdq:sourceAuthority and any parameters used in the Specification that define the default behavior of the Test. Example: ```bdq:maximumValidElevationInMeters default = "8850"```

**Examples** [non-normative]: 'Pass' and 'Fail' examples of inputs and outputs for the Test from the Test Validation Data. Example: ```[dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in bdq:sourceAuthority"]
[dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in bdq:sourceAuthority"]```

**Use Cases** [non-normative]: Descriptions of data quality example needs that this Test helps to support. Example: ```bdq:Record-Management, bdq:Alien-Species```

**Notes** [non-normative]: Additional guidance that may be necessary for the accurate implementation of the Tests. Example: ```Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This Test will fail if there is leading or trailing whitespace or if there are leading or trailing non-printing characters.```
