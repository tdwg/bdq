<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
# Terms Used in the BDQ Tests Quick Reference Guide

Title
: Terms Used in the BDQ Tests Quick Reference Guide

This document is non-normative and part of the [BDQ Tests Quick Reference Guide](index.md)

<!-- This is the list of descriptions of bdqtest terms included in the Quick Reference Guide. -->

<!-- Generated list, approximates the correct set of term definitions, labels don't fully match and not all items are labeled. -->

| Label (Term) | Normative | Definition | Example |
| ------------ | --------- | ---------- | ------- |
| Label (rdfs:label) | normative | A human-readable name for the subject. TDWG SDS: A a word or short phrase that serves as a human-readable name for the term. In present context: A descriptive label for humans to use to identify the Test. | AMENDMENT_COORDINATES_FROM_VERBATIM |
| Preferred Label (skos:prefLabel) | normative | The preferred lexical label for a resource, in a given language. In present context: An easy to read label for the Test, similar to the Label, but in words. | Amendment Coordinates from Verbatim |
| Term Version IRI (rdf:about) | normative | The HTTP IRI that identifies the version of the term that is currently in force. | [https://rs.tdwg.org/ bdqtest/terms/version/ 3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e-2024-08-20](https://rs.tdwg.org/bdqtest/terms/version/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e-2024-08-20) |
| Description (rdfs:comment) | non-normative | A description of the subject resource. In present context: A brief description of what the Test does. | Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms. |
| Expected Response (bdqffdq:hasExpectedResponse) | normative | Text describing the logic to be followed by a bdqffdq:Implementation of a bdqffdq:Specification specifying the values of bdqffdq:ResponseStatus and bdqffdq:ResponseResults that should be produced from the evaluation of input bdqffdq:InformationElements. In present context: The formal definition of how the Test must be implemented. | INTERNAL_PREREQUISITES_NOT_MET if 1) either dwc:decimalLatitude or dwc:decimalLongitude are bdq:NotEmpty, or 2) dwc:verbatimCoordinates and one of dwc:verbatimLatitude and dwc:verbatimLongitude are bdq:Empty; FILLED_IN the values of dwc:decimalLatitude, dwc:decimalLongitude and dwc:geodeticDatum (provided that the dwc:verbatimCoordinates can be unambiguously interpreted as geographic coordinates) from 1) dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimSRS or 2) dwc:verbatimCoordinates and dwc:verbatimSRS; otherwise NOT_AMENDED. |
| InformationElements ActedUpon (bdqffdq:composedOf) | normative | Specific vocabulary term that comprises a bdqffdq:InformationElement that is not a bdqffdq:AbstractInformationElement. | dwc:decimalLatitude, dwc:decimalLongitude, dwc:geodeticDatum |
| InformationElements Consulted (bdqffdq:composedOf) | normative | Specific vocabulary term that comprises a bdqffdq:InformationElement that is not a bdqffdq:AbstractInformationElement. | dwc:verbatimCoordinates, dwc:verbatimLatitude, dwc:verbatimLongitude, dwc:verbatimCoordinateSystem, dwc:verbatimSRS |
| Parameters (bdqffdq:Parameter) | normative | A placeholder for a value that, when provided to a Test bdqffdq:Specification changes the behavior of the Test in a defined manner. | bdq:sourceAuthority |
| SourceAuthorities/Defaults (bdqffdq:hasAuthoritiesDefaults) | normative | Text describing bdq:sourceAuthorities and bdqffdq:Parameters with their default values to attach to a bdqffdq:Specification to further specify the behavior described in the bdqffdq:hasExpectedResponse. | bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]} |
| Notes (skos:note) | non-normative | A general note, for any purpose. In present context: Additional information to supplement the Specification. | Transformations between coordinate reference systems should not be made as a part of this Test. Though coordinate precision of the verbatim coordinates could also be interpreted during the process of amending decimal coordinates from verbatim coordinates, that amendment is recommended to be an independent Test. Note that dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimCoordinates might all be populated, and they may or not be perfectly consistent with each other. An ideal implementation should check for the consistency of these three fields and not amend them if they are inconsistent. |
| Examples (skos:example) | non-normative | An example of the use of a concept. In present context: Examples of input and output data and Test responses for a pass case and a fail case. | [dwc:verbatimLatitude="-23.712", dwc:verbatimLongitude="139.92", dwc:verbatimCoordinates="", dwc:verbatimSRS="EPSG:4326", dwc:verbatimCoordinateSystem="decimal degrees",dwc:decimalLatitude="", dwc:decimalLongitude="": Response.status=FILLED_IN, Response.result=dwc:decimalLatitude="-23.712", dwc:decimalLongitude="139.92", dwc:geodeticDatum="EPSG:4326", Response.comment="Input fields contain interpretable values"],[dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:verbatimCoordinates="54K 0390210 7377243", dwc:verbatimSRS="EPSG:32754", dwc:verbatimCoordinateSystem="decimal degrees", dwc:decimalLatitude="", dwc:decimalLongitude="":: Response.status=NOT_AMENDED, Response.result="", Response.comment="In the wrong coordinate system"] |
| Type (rdf:type) | normative | The subject is an instance of a class. In present context: The type of the Test, one of the subtypes of DataQualityNeed. | Amendment |


Namespace abbreviations used in the table above are as follows:

| **Abbreviation** | **Namespace** |
| ------------ | -------------                               |
| rdf:         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs:        | http://www.w3.org/2000/01/rdf-schema#       |
| skos:        | http://www.w3.org/2004/02/skos/core#        |
| bdqffdq:     | https://rs.tdwg.org/bdqffdq/terms/          |
| bdq:         | https://rs.tdwg.org/bdq/terms/              |
| dwc:         | http://rs.tdwg.org/dwc/terms/               |


## Acronyms (non-normative)

A list of Acronyms can be found in the [Acronyms (non-normative)](../../../index.md#5-acronyms-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary (non-normative)

A glossary of terms additional to those in the various namespaces can be found in the [Glossary (non-normative)](../../../index.md#6-glossary-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## References (non-normative)

The references for the BDQ standard can be found in the [References (non-normative)](../../../index.md#7-references-non-normative) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ (non-normative)

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Tests Quick Reference Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqtest/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)
