### 5 Example RDF (non-normative) 

A more complete description of the tests can be found in the RDF representation of this vocabulary.

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

    <rdf:Description rdf:about="https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Validation"/>
    	<skos:prefLabel rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</skos:prefLabel>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord</rdfs:label>
    	<hasActedUponInformationElement xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="urn:uuid:c3620a97-65d6-4f9c-8a03-32e0d240a423"/>
    	<hasCriterion xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqcrit:Standard"/>
    	<hasDataQualityDimension xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqdim:Conformance"/>
    	<hasResourceType xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="bdqffdq:SingleRecord"/>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</rdfs:comment>
    	<skos:historyNote rdf:datatype="http://www.w3.org/2001/XMLSchema#string">https://github.com/tdwg/bdq/issues/20</skos:historyNote>
    	<skos:note rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and suitable for a marker for the high seas.  Also available in the ISO user defined codes is ZZ, used by GBIF to mark unknown countries.  This test should accept both XZ and ZZ as COMPLIANT country codes. This test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.</skos:note>
    	<dcterms:bibliographicCitation rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ISO (n.dat.) ISO 3166 Country Codes. https://www.iso.org/iso-3166-country-codes.html; ISO (n.dat) 3166-1 alpha-2. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2; DataHub (2018) List of all countries with their two digit codes (ISO 3166-1). https://datahub.io/core/country-list; Chapman AD and Wieczorek JR (2020) Georeferencing Best Practices. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-gg7h-s853</dcterms:bibliographicCitation>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:c3620a97-65d6-4f9c-8a03-32e0d240a423">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/ActedUpon"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Information Element ActedUpon dwc:countryCode</rdfs:label>
    	<composedOf xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="http://rs.tdwg.org/dwc/terms/countryCode"/>
    	<prefLabel xmlns="skos:" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Information Element ActedUpon dwc:countryCode</prefLabel>
    </rdf:Description>
    
    <rdf:Description rdf:about="urn:uuid:02f5a440-a473-42cf-a3f1-6c10334d5eb8">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/ValidationMethod"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ValidationMethod: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<skos:prefLabel rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ValidationMethod: Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord with Specification for: VALIDATION_COUNTRYCODE_STANDARD</skos:prefLabel>
    	<forValidation xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
    	<hasSpecification xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:resource="urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047"/>
    </rdf:Description>

    <rdf:Description rdf:about="urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047">
    	<rdf:type rdf:resource="https://rs.tdwg.org/bdqffdq/terms/Specification"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Specification for: VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</rdfs:comment>
    	<skos:example rdf:datatype="http://www.w3.org/2001/XMLSchema#string">dwc:countryCode="GL": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value"</skos:example>
    	<skos:example rdf:datatype="http://www.w3.org/2001/XMLSchema#string">dwc:countryCode="GRL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value"</skos:example>
    	<hasAuthoritiesDefaults xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</hasAuthoritiesDefaults>
    	<hasExpectedResponse xmlns="https://rs.tdwg.org/bdqffdq/terms/" rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT</hasExpectedResponse>
    </rdf:Description>

## Cite BDQ Core

**To cite BDQ Core in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite the standard document upon which this page is built, use
the following:**

BDQ Core Maintenance Group 2024. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/bdq/doc/list/

**To cite this document specifically, use the following:**

{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

**{publisher}**

This content made open by {publisher} is licensed under a [{license_statement}]({license_uri})


