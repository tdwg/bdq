<!--- Template for header, values provided from yaml configuration --->
# {document_title}

Title
: {document_title}

Date version issued
: {ratification_date}

Date created
: {created_date}

Part of TDWG Standard
: <{standard_iri}>

{previous_version_slot}

Abstract
: {abstract}

Authors:
: {authors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}


### Table of Contents ###

{toc}

## 1 Introduction

This document contains information that is considered supplemental to the normative and non-normative BDQ Core standard documentation. 

### 1.1 Purpose 

This document provides a historical context and lessons learned during the development of BDQ Core. This document will assist those seeking to evaluate their current tests or generate additional tests specific to their domain. 

### 1.2 Audience

This document is relevant to curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners that wish to understand, evaluate and/or improve the quality of the biodiversity data within their domain. This document also provides some guidelines based on the knowledge of the authors, for those who may wish to maintain BDQ Core.

### 1.3 Associated Documents

This document provides practical information that goes beyond the normative guidance in the [BDQ Core User's Guide](../guide/users/index.md) and [BDQ Core Implementer's Guide](../guide/implementers/index.md) for those who wish to use or implement BDQ Core.

### 1.4 Status of the content of this document

This document is non-normative.

### 1.5 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Prefix**   | **Namespace**                                    |
|--------------|--------------------------------------------------|
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms/               |
| bdqcrit      | https://rs.tdwh.org/bdqcrit/terms/               |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms/                |
| bdqenh       | https://rs.tdwg.org/bdqenh/terms/                |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms/               |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| skos         | http://www.w3.org/2004/02/skos/core#             |
| rdfs         | http://www.w3.org/2000/01/rdf-schema#            |
| owl          | http://www.w3.org/2002/07/owl#                   |
| xsd          | http://www.w3.org/2001/XMLSchema#                |

## 2 Historical Context

An internationally agreed standard suite of core tests and resulting assertions can be used by all data providers, data collectors and data users to improve the quality of biodiversity data. This will facilitate more appropriate and more accurate use of biodiversity data. Other than data availability, ‘Data Quality’ is probably the most significant issue for users of biodiversity data and this is especially so for the research community. The BDQ Core Tests will not correct all issues that exist with the data, but reports from the Tests will hopefully identify issues that need to be addressed by users of the data. Such issues will require the user to make decisions on the data - i.e., data that may need to be excluded, data that may need improvement before use, and data that can be used as is. It is always the purview of the user to decide what data are of suitable quality for their use.

### 2.1 Definition of CORE

'CORE' in the context of BDQ Core implies that the Tests are 

- Informative
- Simple to implement
- Mandatory for enhancements/amendments
- Have ‘power’ in that they will not likely result in 0% or 100% of all records failing or passing
- Widely applicable across sub-disciplines within the biodiversity domain
- Capable of elevating the significance of an issue (e.g., no value for dcterms:license), or
- Aspirational in the sense of encouraging priority developments in the biodiversity informatics domain (e.g., testing for any annotations against a record)

These can be considered as the basic principles in the development of the Tests, and are elaborated in [Section 3.11](#311-principles-of-test-design).

The scope of CORE was also developed from the user needs analysis of BDQ Task Group 3, (Data Quality Use Cases: Rees & Nicholls 2020). The CORE Tests largely cover data quality with regards to what organism has occurred where, and at what place and time, and are a subset of [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that we considered to be critical metadata about occurrence records.

A number of Tests were framed, but considered out of scope for CORE data quality needs and were tagged as "Supplementary" in GitHub. These Tests are likely to have a role in specific use cases. Implementers are free to implement a subset of the CORE Tests or Supplementary or new Tests when there is a particular data quality need within their domain. For example, the testing for a value of sub-genus against a taxonomic name authority or testing for a valid depth against maximum depth around the location of an observation. Over the period of this project, many Tests were removed from CORE on the basis that they could not be currently implemented in a manner that would result in predictable results. Be aware, however, that these tests not have gone through the rigorous implimenation testing carried out on the "CORE" tests.

Some Tests were deemed not CORE because they would currently result in the majority of data not having 'quality'. They have been given the GitHub tag "Immature/Incomplete" because it is thought that the Test may have value in the future. An example of such a Test is VALIDATION_REPRODUCTIVECONDITION_NOTEMPTY where we would expect most records to have bdq:Empty for dwc:reproductiveCondition.

#### 2.1.1 Tests tagged as DO NOT IMPLEMENT

Some tests were deemed not CORE because there was a perceived danger in their implementation, even though they appeared superficially implementable. In such cases, we applied the GitHub tag "DO NOT IMPLEMENT" to warn future implementers about the dangers. An example of such as Test is VALIDATION_GEOGRAPHY_CONSISTENT because of the current complexities in matching terms in the geographic names hierarchy.

The following issues describing potential tests were tagged as [DO NOT IMPLEMENT](https://github.com/tdwg/bdq/issues?q=+label%3A%22DO+NOT+IMPLEMENT%22).  The discussion in each issue provides rationale management for why they were tagged as such.

| Issue | Name | Description |
| ----- | ---- | ----------- |
| [53](https://github.com/tdwg/bdq/issues/53) | AMENDMENT_CLASS_STANDARDIZED | Can the value of dwc:class be standardized using the Source Authority? |
| [34](https://github.com/tdwg/bdq/issues/34) | AMENDMENT_DAYMONTH_TRANSPOSED | Swap dwc:month and dwc:day if dwc:month is greater than 12 and dwc:day is less than 12. |
| [27](https://github.com/tdwg/bdq/issues/27) | AMENDMENT_FAMILY_STANDARDIZED | Can the value of dwc:family be standardized using the Source Authority? |
| [118](https://github.com/tdwg/bdq/issues/118) | AMENDMENT_GEOGRAPHY_STANDARDIZED | Propose amendment to one or more of the values dwc:continent, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality using bdq:sourceAuthority. |
| [90](https://github.com/tdwg/bdq/issues/90) | AMENDMENT_KINGDOM_STANDARDIZED | Can the value for kingdom be standardized against the source authority? |
| [100](https://github.com/tdwg/bdq/issues/100) | AMENDMENT_MINDEPTHMAXDEPTH_TRANSPOSED | Attempt to transpose minimum and maximum depth if minimum depth is greater than maximum depth |
| [44](https://github.com/tdwg/bdq/issues/44) | AMENDMENT_MINELEVATIONMAXELEVATION_TRANSPOSED | If \"dwc:minimumElevationInMeters is greater than dwc:maximumElevationInMeters, can they be meaningfully swapped? |
| [25](https://github.com/tdwg/bdq/issues/25) | AMENDMENT_ORDER_STANDARDIZED | Can the value of dwc:order be standardized using the Source Authority? |
| [80](https://github.com/tdwg/bdq/issues/80) | AMENDMENT_PHYLUM_STANDARDIZED | Can the value of dwc:phylum be standardized using the Source Authority? |
| [129](https://github.com/tdwg/bdq/issues/129) | AMENDMENT_YEAR_STANDARDIZED | Attempt to amend the year |
| [37](https://github.com/tdwg/bdq/issues/37) | ISSUE_DAYMONTH_SWAPPED | Is it likely that the day and month have been swapped? |
| [89](https://github.com/tdwg/bdq/issues/89) | ISSUE_DECIMALLATITUDEDECIMALLONGITUDE_CONVERSIONFAILED | Latitude and longitude could not be converted using the default geodetic datum |
| [35](https://github.com/tdwg/bdq/issues/35) | MEASURE_VALIDATIONTESTS_RUN | Total number of tests of output type Validation that have been attempted to have been run against the record |
| [95](https://github.com/tdwg/bdq/issues/95) | VALIDATION_GEOGRAPHY_CONSISTENT | Is the combination of the values of the terms dwc:continent, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality consistent with the bdq:sourceAuthority? |
| [139](https://github.com/tdwg/bdq/issues/139) | VALIDATION_GEOGRAPHY_STANDARD | Can the individual values of the terms dwc:continent, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality be unambiguously resolved from bdq:sourceAuthority? |
| [231](https://github.com/tdwg/bdq/issues/231) | VALIDATION_IDENTIFICATIONQUALIFIER_NOTEMPTY | Is there a value in dwc:identificationQualifier? |
| [274](https://github.com/tdwg/bdq/issues/274) | VALIDATION_MODIFIED_INRANGE | Is the value of dcterms:modified entirely with the Parameter Range? |
| [266](https://github.com/tdwg/bdq/issues/266) | VALIDATION_WATERBODY_NOTEMPTY | Is there a value in dwc:waterbody? |
| [141](https://github.com/tdwg/bdq/issues/141) | VALIDATION_YEAR_STANDARD | Can the value for year be interpreted as a valid year? |

### 2.2 Use Case Development

Biodiversity Data Quality Task Group 3: Data Quality Use Cases (Rees & Nicholls 2020), was established to review what use cases were in common use. This group identified several fundamental use cases, including "bdq:Spatial-Temporal Patterns", "bdq:Record-Management", and "bdq:Taxon-Management". We later added "bdq:Alien-Species" and "bdq:Biotic-Relationships". 

These are only a sample of the many possible use cases used in the biological sciences, but they provide an initial set to which all the BDQ Core Tests have been linked. Note that the relationship between Use Cases and Tests is a many to many relationship - with most tests being relatable to many use cases and vice versa.

Note that the evaluation of a Test can only take place within the context of a specific use case, even if that use is broad. For example, the Test [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134) could test the value of dwc:country against a source authority for the use case bdq:Record-Management, but this Test may not be applicable to a use case related to marine ecology.

### 2.3 Data Quality Control and Data Quality Assurance

The Fitness for Use Framework (Veiga 2016, Veiga et al. 2017) (bdqffdq: namespace) draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose/use case, that is to assure that data used for some purpose are fit for that purpose.

The specification of the BDQ Core Tests within the Framework allows the same set of Tests to apply to both Data Quality Control (detecting and correcting errors) and Data Quality Assurance (filtering out problematic records to limit data to that with quality for meeting a particular need). The design of the Test Types Validations and Measures are intended to be agnostic as to whether their use is for Data Quality Control (finding problematic data), or Data Quality Assurance (filtering out NOT_COMPLIANT records).

### 2.4 Framework Competency Questions

The development of the representation of the Fitness for Use Framework as an owl ontology (bdqffdq:) was influenced by competency questions, shaped by the late Robert A. Morris, and originally written by David Lowery (within the kurator-ffdq codebase (Lowery et al. 2024); see [kurator-ffdq competency questions](https://github.com/kurator-org/kurator-ffdq/tree/53ce808117d83cbe84e6820636c90e404a4c6886/competencyquestions) as part of the Kurator project (Morris et al. 2018)).  The development of the BDQ Core Test descriptors (the terms used to describe our Tests) led to changes in the ontology (largely adopting a consistent naming pattern).  Changes to the specifics of competency questions follow on from that.

Example competency questions that can be asked of the RDF representation of bdqcore: 

    # Given a use case find validation Tests and their specifications

    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    
    SELECT DISTINCT ?useCase ?test ?specification
    
    WHERE {
    
        # Find Validations from the ValidationPolicy
        # for a given use case
    
        ?policy a bdqffdq:ValidationPolicy .
        ?policy bdqffdq:hasUseCase ?uc .
        ?policy bdqffdq:includesInPolicy ?cc .
        ?uc rdfs:label ?useCase .
    
        # Find the specification from the validation method
        # referencing the Validation
    
        ?cc skos:prefLabel ?test .
    
        ?vm a bdqffdq:ValidationMethod .
        ?vm bdqffdq:forValidation ?cc .
        ?vm bdqffdq:hasSpecification ?testSpec .
        ?testSpec bdqffdq:hasExpectedResponse ?specification .

        # Filter by a specific use case
    
         FILTER( ?uc = <https://rs.tdwg.org/bdqffdq/terms/Taxon-Management> )
    }

And another that lists the valuable Information Elements for a use case: 

    # Given a use case find the ActedUpon
    # Information Elements 
    
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    
    SELECT DISTINCT ?useCase ?ie
    
    WHERE {
    
       # Find Validations from the ValidationPolicy
       # for a given use case
    
       ?policy a bdqffdq:ValidationPolicy .
       ?policy bdqffdq:hasUseCase ?uc .
       ?policy bdqffdq:includesInPolicy ?cc .
       ?uc rdfs:label ?useCase .
    
       # Find ActedUpon InformationElements 
       # for the Validations
     
       ?cc bdqffdq:hasActedUponInformationElement ?ieClass .
       ?ieClass bdqffdq:composedOf ?ie
    
       # Filter by a specific use case

       FILTER( ?uc = <https://rs.tdwg.org/bdqffdq/terms/Taxon-Management> )
    
    }

Summary of the distribution of Tests by Data Quality Dimension and specific Darwin Core Terms in InformationElements ActedUpon: 

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    PREFIX bdqcore: <https://rs.tdwg.org/bdqcore/terms/>
    SELECT (count(?test) as ?ct) ?dimension ?sie
    WHERE {
       ?ie bdqffdq:composedOf ?sie .
       ?test bdqffdq:hasActedUponInformationElement ?ie .
       ?test bdqffdq:hasDataQualityDimension ?dimension .
       ?test rdf:type ?testType .
       FILTER (?testType != owl:NamedIndividual)
    }
    GROUP BY ?sie ?dimension
    ORDER BY ?sie ?dimension

Summary of the distribution of Tests by Test Type and specific Darwin Core Terms in InformationElements ActedUpon: 

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    PREFIX bdqcore: <https://rs.tdwg.org/bdqcore/terms/>
    SELECT (count(?test) as ?ct) ?testType ?sie
    WHERE {
        ?ie bdqffdq:composedOf ?sie .
        ?test bdqffdq:hasActedUponInformationElement ?ie .
        ?test rdf:type ?testType .
        FILTER (?testType != owl:NamedIndividual)
    }
    GROUP BY ?sie ?testType
    ORDER BY ?sie ?testType

Given a Specification (as would be known when starting with a bdqffdq:Assertion and following bdqffdq:producesAssertion to a bdqffdq:Implementation then bdqffdq:usesSpecification), what test was run with which argument values for which parameters: 

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT ?test ?label ?description  (GROUP_CONCAT(DISTINCT ?params; separator='; ') as ?parameters) 
    WHERE { 
      ?test rdf:type bdqffdq:Validation . ?test rdfs:label ?label . ?method bdqffdq:forValidation ?test . 
      ?method bdqffdq:hasSpecification ?specification . ?specification rdfs:comment ?description .
      OPTIONAL { 
         ?specification bdqffdq:hasArgument ?argument . ?argument bdqffdq:hasArgumentValue ?argumentValue . ?argument bdqffdq:hasParameter ?parameter . 
         BIND (CONCAT(STR(?parameter), "=" , ?argumentValue ) as ?params )
      } .
      FILTER (STR(?specification) = "urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544")
    }
    GROUP BY ?test ?label ?description

Given an Assertion, what Test was run with which argument values for which parameters by which mechanism to produce it: 

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT ?test ?label ?description  (GROUP_CONCAT(DISTINCT ?params; separator='; ') as ?parameters) ?mechanism
    WHERE { 
      ?test rdf:type bdqffdq:Validation . ?test rdfs:label ?label . ?method bdqffdq:forValidation ?test . 
      ?method bdqffdq:hasSpecification ?specification . ?specification rdfs:comment ?description .
      OPTIONAL { 
         ?specification bdqffdq:hasArgument ?argument . ?argument bdqffdq:hasArgumentValue ?argumentValue . ?argument bdqffdq:hasParameter ?parameter . 
         BIND (CONCAT(STR(?parameter), "=" , ?argumentValue ) as ?params )
      } .
      ?implementation bdqffdq:usesSpecification ?specification . ?implementation bdqffdq:producesAssertion ?assertion .
      ?implementation bdqffdq:implementedBy ?mechanism .
      FILTER (STR(?assertion) = "{id of assertion to look up}")
    }
    GROUP BY ?test ?label ?description ?mechanism

What Validations share the same ActedUpon Information Elements with Amendments:

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT distinct ?vlabel ?term ?alabel
 	WHERE { 
       ?validation a bdqffdq:Validation . ?validation rdfs:label ?vlabel . ?validation bdqffdq:hasActedUponInformationElement ?ie .
       ?ie bdqffdq:composedOf ?term . ?iea bdqffdq:composedOf ?term . ?amendment bdqffdq:hasActedUponInformationElement ?iea . 
        ?amendment a bdqffdq:Amendment . ?amendment rdfs:label ?alabel . 
    }
    ORDER BY ?term

What Information Elements are acted upon by more that one Annotation: 

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT ?term ( count( distinct ?alabel) as ?ct )
    WHERE {
       ?validation a bdqffdq:Validation . ?validation rdfs:label ?vlabel . ?validation bdqffdq:hasActedUponInformationElement ?ie .
       ?ie bdqffdq:composedOf ?term . ?iea bdqffdq:composedOf ?term . ?amendment bdqffdq:hasActedUponInformationElement ?iea .
        ?amendment a bdqffdq:Amendment . ?amendment rdfs:label ?alabel .
    }
    GROUP BY ?term 
    HAVING ( ?ct > 1 )
    ORDER BY ?term

What Amendments act upon Information Elements that are acted upon by more than one Amendment:

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT distinct ?amend ?amendName
    WHERE { 
       ?amend bdqffdq:hasActedUponInformationElement ?iec . ?iec bdqffdq:composedOf ?term .  ?amend a bdqffdq:Amendment . ?amend rdfs:label ?amendName .
       { SELECT ?term (COUNT (distinct ?amendment) as ?ct ) 
            WHERE { 
             ?validation a bdqffdq:Validation . ?validation rdfs:label ?vlabel . ?validation bdqffdq:hasActedUponInformationElement ?ie .
             ?ie bdqffdq:composedOf ?term . ?iea bdqffdq:composedOf ?term . ?amendment bdqffdq:hasActedUponInformationElement ?iea .
             ?amendment a bdqffdq:Amendment . ?amendment rdfs:label ?alabel .
           }
           GROUP BY ?term 
           HAVING ( ?ct > 1 )
       } 
    } 

### 2.4.1 Listing Identifiers for Tests

The following competency question obtains a list of identifiers of Validation Tests: 

    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    SELECT ?label ?term_localName ?iri ?term_iri
    WHERE { 
      ?iri a bdqffdq:Validation . 
      ?iri rdfs:label ?label . 
      ?iri dcterms:isVersionOf ?term_iri . 
      BIND (REPLACE(STR(?term_iri),"https://rs.tdwg.org/bdqcore/terms/","") as ?term_localName ) 
    }

Example results: 

| Label | Term Name | Term Version IRI | Term IRI |
| ----  | --------- | ---------------- | -------- | 
| VALIDATION_MINELEVATION_INRANGE | 0bb8297d-8f8a-42d2-80c1-558f29efe798 | <https://rs.tdwg.org/bdqcore/terms/0bb8297d-8f8a-42d2-80c1-558f29efe798-2024-09-04> | <https://rs.tdwg.org/bdqcore/terms/0bb8297d-8f8a-42d2-80c1-558f29efe798> |
| VALIDATION_MONTH_STANDARD | 01c6dafa-0886-4b7e-9881-2c3018c98bdc | <https://rs.tdwg.org/bdqcore/terms/01c6dafa-0886-4b7e-9881-2c3018c98bdc-2024-09-05> | <https://rs.tdwg.org/bdqcore/terms/01c6dafa-0886-4b7e-9881-2c3018c98bdc> |

The label is intended as the identifier of a Test for humans, the Term Name as a machine readable identifier.

### 2.4.2 Framework Competency Question including an oa:annotation

Given a resource (an occurrence record) list all assertions produced by validations run on that resource where the resource is the target of an annotation and the assertion is the body of the annotation.  Includes the motivation and date generated for the annotation in the response.   

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX oa: <https://www.w3.org/TR/annotation-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    SELECT ?responsestatus ?responseresult ?responsecomment ?test ?label ?description (GROUP_CONCAT(DISTINCT ?params; separator='; ') as ?parameters) ?mechanism ?motivation ?annotationdate 
    WHERE {
      ?test rdf:type bdqffdq:Validation . ?test rdfs:label ?label . ?method bdqffdq:forValidation ?test .
      ?method bdqffdq:hasSpecification ?specification . ?specification rdfs:comment ?description .
      OPTIONAL {
         ?specification bdqffdq:hasArgument ?argument . ?argument bdqffdq:hasArgumentValue ?argumentValue . ?argument bdqffdq:hasParameter ?parameter .
         BIND (CONCAT(STR(?parameter), "=" , ?argumentValue ) as ?params )
      } .
      ?implementation bdqffdq:usesSpecification ?specification . ?implementation bdqffdq:producesAssertion ?assertion .
      ?assertion bdqffdq:hasResponseStatus ?responsestatus .
      ?assertion bdqffdq:hasResponseResult ?responseResult .
      ?assertion bdqffdq:hasResponseComment ?responsecomment .
      ?implementation bdqffdq:implementedBy ?mechanism .
      ?annotation oa:body ?assertion .
      ?annotation oa:target ?target .
      OPTIONAL { ?annotation oa:motivation ?motivation . } .
      OPTIONAL { ?annotation oa:generated ?annotationdate . } .
      FILTER (STR(?target) = "https//mczbase.mcz.harvard.edu/guid/MCZ:Mala:280832")
    }
    GROUP BY ?responsestatus ?responseresult ?responsecomment ?test ?label ?description ?mechanism ?motivation ?annotationdate


## 3 Developing the Tests

Originally, Biodiversity Information Standards (TDWG) Data Quality Task Group 2: Data Quality Tests and Assertions was tasked with finding a fundamental suite of tests and identifying any relevant software associated with testing for 'Data Quality'/'Fitness for Use'. It was quickly realized however, that any software was likely to be far less stable than defining a CORE suite of tests and an associated framework, so the software component was quickly dropped. We also limited the scope of BDQ Core Tests to apply only to data encoded using the Darwin Core standard (Wieczorek et al. 2012). This gave us a specific target, but also associated problems noted below.

Finding out what tests were being used by a range of biodiversity data aggregators was our first step in identifying likely candidates. We identified, aggregated and described 152 unique tests from GBIF, ALA, iDigBio, CRIA and BISON into a consistent structure for comparison and evaluation.  Descriptors at this time included Information Elements (the [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) used by the Tests), Specification (a technical description aimed at implementation), Darwin Core Class, Source of the test and References. We performed a full evaluation of each candidate test using the seven criteria noted in Section 2.1. Tests had to be informative in being able to evaluate or enhance the quality of a data record. Tests had to be relatively simple/straight forward to implement with existing tools. Tests were mandatory for any potential enhancements to record values in that a Validation Test was required before any Amendment Test. Tests required power in that they will not likely result in 0% or 100% of all record passing or failing the test.

BDQ Core Tests were designed to provide an adequate coverage of basic information dimensions of Darwin Core: dwc:Taxon (GitHub tag NAME); dwc:Event (GitHub tag TIME) and dcterms:Location (GitHub tag SPACE), and a category that we called "Other" (GitHub tag OTHER) to cover Tests on dwc terms such as dc:license (see Section 3.1). Tests also had to be widely applicable across a range of use cases. Tests that were identified as useful in a limited context were documented and were (GitHub) tagged as "Supplementary" in that they could be implemented by a community of usage.

We originally rendered the Tests in the form that flagged a **FAIL**, for example a dwc:eventDate that did not conform to ISO 8601-1 date. Our reasoning was this strategy aligned with all of the sources of the Tests in that we all sought to identify **issues** with values in the record that would reduce its quality. However, the Data Quality Framework (Veiga 2016, Veiga et al. 2017) worked in the opposite direction: Identifying values in a record that **PASSED** a Test; increased 'quality'. To align with the Framework, we renamed all BDQ Core Tests from FAIL to PASS type, for example, COUNTRYCODE_NOTSTANDARD became COUNTRYCODE_STANDARD. This reversal of 'fail' to 'pass' was also reflected in the comparison of the Framework's 'Data Quality Dimension' versus our early concept of 'Warning Type' (see Section 3.2).

Second and subsequent evaluations of the candidate BDQ Core Tests reduced the number to about 100 that seemed to fulfill the criteria above. Tests came and went as we provided more consistent and comprehensive documentation against what we called the Test Descriptors. The Tests also changed as we began to implement them. We modified a Test Specification to then find that we would not be able to implement it due to potential ambiguous responses from the Test or that a Test response may be misleading. By far the greatest changes to the candidate tests came about when we implemented them and ran them against the Test Validation Data (see the [Implementer's Guide](../guide/implementers/index.md#81-introduction-non-normative)) (using bdq_issue_to_csv (Morris 2024b) to extract a CSV file of validation data from a working spreadsheet to execute implementations with bdqcoretestrunner (Morris 2024)).

At one point, we aligned the documentation for over sixty tests that were tagged in GitHub as Supplementary, Immature/Incomplete and DO NOT IMPLEMENT. In doing so, we realized that the consistent documentation now provided a more nuanced evaluation and subsequently moved a number of these tests back into BDQ Core. The opposite was also true: The implementation of the Tests and running against the validation test data clearly demonstrated that some Tests were removed from BDQ Core. Where there were recognized nuances with the Tests that may not be obvious from the Specification, we documented the issues in the Test Notes.

The team identified a fundamental problem early in the development of the Tests: Darwin Core lacked a comprehensive suite of controlled vocabularies. Testing for 'quality' or 'fitness for use' was made difficult at best and impossible at worst, when controlled vocabularies were unavailable. We recognized the key issue of openness of the Darwin Core standard, yet the need for controlled vocabularies to evaluate and improve the 'quality' of Darwin Core encoded data was also important. This conclusion effectively initiated Data Quality Task Group 4: Best Practices for Development of Vocabularies of Value (https://www.tdwg.org/community/bdq/tg-4/) to provide a framework for how these vocabularies could be developed for a priority set of Darwin Core Terms. This in turn has resulted in GBIF initiating https://github.com/gbif/vocabulary, and see also https://docs.google.com/viewer?url=https%3A%2F%2Fdev.gbif.org%2Fissues%2Fbrowse%2FGBIF-121%2Fgbif-vocabularies-review_v01.docx.

Over the course of the development of the Tests, we encountered significant difficulties with choices of words.  In the original formulation of the Framework (Veiga 2016), different words were used to describe parallel concepts at the levels of data quality needs, solutions, and reports, and the words used for fundamental concepts overlapped with those for derived concepts.  We have settled on Dimension, Criterion, and Enhancement as the words for fundamental concepts, and variations on Validation (Validation, ValidationMethod, ValidationAssertion), Measure, Amendment, and Issue for derived concepts.  It was very late in development of the Test Specifications that we realized that the heart of what we were terming Validation mapped to the derived concept of CriterionInContext/ContextualizedCriterion in the Framework (Veiga et al. 2017), so we have renamed Framework concepts for clarity.

Early on we recognized that the Data Quality Framework required us to frame MultiRecord measures in order to support the formal requirements in the framework for Quality Control and Quality Assurance (which are defined as only involving Measures).  We recognized that these would be simple, repetitive, formal statements about the results of validations, so we put off defining these until very late in the process.  They proved straightforward to frame and then generated from the set of adopted SingleRecord Tests.

### 3.1 Test Types

Tests are identified by the bdqffdq: namespace classes of Validation, Issue, Amendment and Measure. Each of these types of Tests can be composed with a ResourceType to apply to a single record (bdqffdq:SingleRecord), or to multiple records comprising a dataset (bdqffdq:MultiRecord).  In BDQ Core, we have described a set of SingleRecord Validations, Issues, Amendments, and Measures, and in addition, a set of MultiRecord Measures.  The formal statement of each of these is complex, being a composition of an instance of a subclass of a bdqffdq:DataQualityNeed with an instance of a subclass of a bdqffdq:Method with an instance of a bdqffdq:Specification, but we subsume this complexity with the phrases Validation Test, Issue Test, Amendment Test, and Measure Test. 

#### 3.1.1 Validation

Validation Tests evaluate values in one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) for fitness for a particular data quality need. In some cases, Validation Tests check for the presence or the lack of a value. Validation Tests are phrased as positive statements consistent with the Fitness For Use Framework (Veiga 2016, Veiga et al. 2017). For example, [VALIDATION_TAXONRANK_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/14da5b87-8304-4b2b-911d-117e3c29e890) will return a Response.status="RUN_HAS_RESULT" and Response.result="COMPLIANT" if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e., VALIDATION_TAXONRANK_EMPTY) and flagging a potential problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result="COMPLIANT". The formal response of Validation Tests take one of three forms. 

1. A Response.status of "EXTERNAL_PREQUISITES_NOT_MET" when an external resource (e.g., a source authority, bdq:sourceAuthority) is unavailable, and running the same Test on the same data at a different time may result in a different result.
2. A Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of one or more of the Information Elements are such that the Test cannot be meaningfully run.
3. A Response.status of "RUN_HAS_RESULT" when the prerequisites for running the Test have been met, and in this situation:
  - A Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not.

During the development of BDQ Core, there were significant discussions about how Tests were to be phrased, for several contributors (and all tests implemented by agencies such as the ALA and GBIF), the most natural form seemed to be to describe assertions in the negative sense, identifying problems. The bdqffdq Framework, however, focused entirely on positive statements, identifying data that have quality and are fit for purpose.  Over the evolution of the description of the Tests, we conformed the language to the positive sense of the Framework in almost all cases.  Validations are thus phrased in the Framework sense of being COMPLIANT if the data have quality with respect to the Test evaluation criteria.  There were, however, a set of cases that didn't fit well into this positive sense, in particular, those where the conclusion of the Test was that the data might or might not be fit for purpose and a human would have to evaluate more closely.  In order to accommodate this "there might be a problem" case, we expanded the Framework to include the concept of bdqffdq:Issue, where Issues are the converse of Validations and are phrased in a negative sense, identifying problems, see below. 

#### 3.1.2 Issues

Issue Tests are a form of warning flag where the Test is drawing attention to potential problem with the value of a [Darwin Core Term](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) for at least one use case. As discussed above, Validations are phrased in the Framework sense of being COMPLIANT if the data have quality with respect to the Test evaluation criteria.  There were however, a set of cases that didn't fit well into this positive sense, in particular, those where the conclusion of the Test was that the data might or might not be fit for purpose and a human would have to evaluate the results.  In order to accommodate this "there might be a problem" case, we expanded the Framework to include the concept of bdqffdq:Issue, where Issues are the converse of Validations and are phrased in a negative sense of identifying potential problems. 

Issues can result in a Response.status="RUN_HAS_RESULT" accompanied by a Response.result="POTENTIAL_ISSUE" or "NOT_ISSUE".  

An Issue is the equivalent to a Response.status="NOT_COMPLIANT" from a Validation Test. A Response.result="NOT_ISSUE" is similar to a Response.result="COMPLIANT" from a Validation Test, but with slightly different semantics, "COMPLIANT" means that the data are fit for some use. A Response.result="NOT_ISSUE" means that there was no reason for the data not to be fit for use.  A Response.result="POTENTIAL_ISSUE" is the reason we incorporated Issue type Tests into BDQ Core.  "POTENTIAL_ISSUE" means that the Issue found a concern in the data that might make it unfit for some use, but that human evaluation of the details of the data and the use are needed. Data flagged with potential issues require a human review.  For example, [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/14da5b87-8304-4b2b-911d-117e3c29e890) will return a Response.result="POTENTIAL_ISSUE" if dwc:dataGeneralizations contains a value. Any value in dwc:dataGeneralizations asserts changes have been made to generalize other [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) and requires a human review to determine whether the data are fit for purpose.

#### 3.1.3 Amendments

Amendment Tests may propose a change to one or more [Darwin Core Term](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) values or fill in missing values. Amendments are intended to improve one or more components of the quality of the record.  The Response.result from an Amendment is a proposal for a change, not to be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses may choose to (blindly - not recommended, or after analysis) accept all proposed amendments as part of a pipeline in preparing data for an analysis. We urge that Amendments do not overwrite existing information within a database; that existing information is preserved, as well as potential changes.

The Framework also supports Amendments where the Response.result is a proposal to changes in procedures, such as suggesting that a constraint should be placed on a database field to restrict allowed values, or that a mapping of a dataset onto [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) has transposed a set of fields.  We have not framed any such Tests of this form in BDQ Core, nor have we considered how such assertions should be represented in a Response.result.

When carrying out Amendments where numeric values are concerned (e.g., feet to meters, etc.), the principle of reversibility is paramount, and thus rounding up or down or using approximations should be avoided and only exact values used. In BDQ Core, we have taken an expedient approach in relation to making Amendments: We have used code in our tests to try and parse out likely unambiguous matches. This is far from an ideal solution, but it does provide the potential of Amendments to 'value add' to Darwin Core data records.

#### 3.1.4 Measures

Measures return a Response.result as either a numeric value or "COMPLETE" or "NOT_COMPLETE".

Most SingleRecord Measure Tests defined in BDQ Core count the number of Validation or Amendment Tests with a specified Response.Result in a bdqffdq:SingleRecord.  Measure Tests can also be accumulated across multiple records (bdqffdq:MultiRecord).  See [3.3.2 MultiRecord Measures](#332-MultiRecord-Measures) for further discussion of MultiRecord Measures.

bdqffdq:SingleRecord MEASUREs within BDQ Core are [MEASURE_VALIDATIONTESTS_COMPLIANT](https://rs.tdwg.org/bdqcore/terms/45fb49eb-4a1b-4b49-876f-15d5034dfc73), [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](https://rs.tdwg.org/bdqcore/terms/453844ae-9df4-439f-8e24-c52498eca84a), [MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](https://rs.tdwg.org/bdqcore/terms/49a94636-a562-4e6b-803c-665c80628a3d), [MEASURE_AMENDMENTS_PROPOSED](https://rs.tdwg.org/bdqcore/terms/03049fe5-a575-404f-b564-ae63f5a1cf8b) and [MEASURE_EVENTDATE_DURATIONINSECONDS](https://rs.tdwg.org/bdqcore/terms/56b6c695-adf1-418e-95d2-da04cad7be53). Of these, MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate and is the only numeric response Test. This Test is intended to provide an estimator for the duration of an event date that can be used as a criterion for Quality Assurance for some use cases. For example, a phenology use may need temporal resolution of records to within about a day, while a use involving long term patterns of spatial change may be satisfied by temporal resolution of a year or better.  Rather than providing specific measures for each possible duration, we chose to provide just this one generic measure that could be used as a filter criterion for any Use Case.  

### 3.2 MultiRecord Tests

When defining a Test, the Test Type (Validation, Amendment, Measure, Issue) is composed with a ResourceType (bdqffdq:SingleRecord or bdqffdq:MultiRecord).  This determines if the Test results in assertions about a single record or a dataset as a whole.

#### 3.2.1 MultiRecord Validations, Amendments, Issues

We do not define MultiRecord Validations, Amendments or Issues in BDQ Core, though these are allowed within the namespace bdqffdq.  A MultiRecord Validation, for example, could evaluate all instances of dwc:occurrenceID in a dataset and assert COMPLIANT if they are unique.  A MultiRecord Amendment, could, for example, evaluate all values of dwc:decimalLatitude and dwc:decimalLongitude in a dataset, assert that they are probably transposed, and that the consumer of the data quality report should check that the two terms do not have their values transposed, and if that is the error, switch their values.

#### 3.2.2 MultiRecord Measures

MultiRecord Tests examine data across multiple records - a dataset.

The BDQ Core MultiRecord Measures all take the output of other Tests as their input rather than from the data records. The inputs (Information Elements) for these Measures in bdqcore: are the outputs of SingleRecord Validations. We have defined two sets of MultiRecord Measures in BDQ Core.  One of these sets consists of Measures that return COMPLETE or NOT_COMPLETE, the other set consists of Measures that return numeric values.  These are intended for Quality Control and Quality Assurance (sensu Veiga, et al. 2017).

For each bdqffdq:SingleRecord Validation Test, there is defined a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not.  Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for the relevant UseCase.  Data are found to be fit for some Use if all Validations comprising that Use have a Response.result of COMPLIANT, and if such are included, all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE.  A MultiRecord dataset is fit for use for a given UseCase if each of the MultiRecord Quality Assurance Measures on that MultiRecord returns COMPLETE.  If this is not the case, SingleRecords where the Validations are other than COMPLIANT are filtered out until all of the MultiRecord Quality Assurance measures return COMPLETE. The MultiRecord Quality Assurance Measures are the formal means the Fitness for Use Framework provides for ensuring that a dataset is fit for use for a given Use Case.  Thus, under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the criteria of bdqffdq:MultiRecord Measures for Completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures. 

We have also defined MultiRecord Measures that count the number of instances of some state for the Response objects from some SingleRecord Validation run over all the records in a dataset.  For example, to return a count of Response.result of COMPLIANT for a particular Validation across a dataset, thus providing a numeric measure of how fit a dataset is for some purpose.  This subset of measures in BDQ Core simply counts the Responses from a given Validation that have Response.result of COMPLIANT.  For Quality Control, these numbers identify where (and how much) work is needed to make more of a dataset fit for use for a given Use Case.  These MultiRecord Measures that return counts can also be run before an Amendment step in a data processing pipeline, and then run again after applying all of the proposed changes to the data from the Amendments to the data in the pipeline.  A comparison of these pre-amendment and post-amendment phases will identify how much accepting all of the proposed changes from the amendments will improve the quality of the data for a given Use Case.  We have chosen to phrase these as returning a count of COMPLIANT (but see note in [3.2.3](#333-considerations-for-use-of-multirecord-measures) below), and let consumers calculate percentages of compliant from the number of records in the dataset. Other statistics are possible, but under the constraint of the Framework (bdqffdq:), a Measure may only return a single numeric value or COMPLETE/NOT_COMPLETE.

MultiRecord measures can also operate directly on the data, that is, to use data terms as the input InformationElements. For example, a MultiRecord Measure could be framed to measure the average number of individuals reported in dwc:individualCount in a dataset, or could be framed to report another statistic on that or another term.  We have defined no Measures of this form in BDQ Core.

#### 3.2.3 Considerations for use of MultiRecord Measures

Some Validations return Response.status="INTERNAL_PREREQUISITES_NOT_MET" when one or more of the input InformationElements contain empty values.  For some UseCases, empty values in some fields make the data not fit for use (these are usually tested directly with VALIDATION...NOTEMPTY Tests), however, some Validations operate on sparse data or other cases where the data are fit for use even without values, but when values are present, they must comply with some restriction.  For example, dwc:minimumDepthInMeters and dwc:maximumDepthInMeters are not expected to be populated for terrestrial data, but are expected to be within range when values are supplied for freshwater and marine data.  A subset of the MultiRecord Quality Assurance Measures accommodate such cases by returning a Response.result="COMPLETE" for Validations that are either Response.result="COMPLIANT" or Response.status="INTERNAL_PREREQUISITES_NOT_MET". Thus, they can measure that all of the SingleRecords in a MultiRecord either have, for example, no value in dwc:minimumDepthInMeters or have an in-range value for dwc:minimumDepthInMeters.

It is possible, but less flexible, to frame Validations to return Result.response="COMPLIANT" for either empty values (bdq:Empty) or non-empty values (bdq:NotEmpty) that satisfy other Validation criteria.  Concerns are better separated, and individual Tests are better composed to fit particular user needs, by having the Validations treat empty data with a Response.status="INTERNAL_PREREQUISITES_NOT_MET", and then framing MultiRecord Quality Assurance Measures as appropriate for a given Use Case.

### 3.3 Data Quality Dimension and "Warning Types"

A "Warning Type" for each BDQ Core Test was envisioned to provide insight into the nature of the issues associated the original 'negative-oriented' results of the Tests (see discussion under [3 Developing the tests](#3-developing-the-tests). Initially, we had a concept of 'severity' where a failed Test could be considered either a "Warning" or an "Error". We subsequently elaborated the warnings into "Warning Types" that had a value of "Ambiguous", "Amended", "Incomplete", "Inconsistent", "Invalid", "Issue", "Report" or "Unlikely". In 2023, a cross tabulation of 'Data Quality Dimension' from the Framework (Veiga 2016, Veiga et al. 2017) against 'Warning Type' demonstrated that they were highly correlated (see table below). Subsequently, 'Warning Type' was removed as a Test Descriptor.

| Data Quality Dimension/Warning Type | Ambiguous | Amended | Incomplete | Inconsistent | Invalid | Issue | Report | Unlikely | Total |
|-------------------------------------|-----------|---------|------------|--------------|---------|-------|--------|----------|-------|
| Completeness                        |           |   11    |    22      |              |         |   1   |    5   |          |  39   |
| Conformance                         |     2     |   17    |            |              |    40   |       |        |          |  59   |
| Consistency                         |           |    1    |            |       7      |         |       |        |          |   8   |
| Likeliness                          |           |         |            |              |         |       |        |     2    |   2   |
| Reliability                         |           |         |            |              |         |   1   |    2   |          |   3   |
| Resolution                          |           |         |            |              |         |   1   |    1   |          |   2   |
| Total                               |     2     |   28    |    22      |       7      |    40   |   3   |    8   |     2    | 113   |

Caption: Data Quality Dimension vs Warning Type (as of 2023) with the number of Tests as cell values. 

The following sparql query to count Tests by type and data quality dimension: 
<pre>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdqcore: <https://rs.tdwg.org/bdqcore/terms/>
SELECT (count(?test) as ?ct) ?dimension ?testType
WHERE {
?test bdqffdq:hasDataQualityDimension ?dimension .
?test rdf:type ?testType .
FILTER (?testType != owl:NamedIndividual)
}
GROUP BY ?dimension ?testType
</pre>

Gives the following distribution of Test Types by Dimension:

| Data Quality Dimension | Validation | Amendment | Issue | Measure | 
| ---------------------- | ---------- | --------- | ----- | ------- | 
| Conformance   | 41 | 17 | 1 |   | 
| Consistency   | 7  | 1  |   |   | 
| Completeness  | 22 | 11 | 1 | 1 | 
| Likeliness    | 2  |    |   |   | 
| Resolution    |    |    | 1 | 1 | 
| Reliability    |    |    |   | 2 | 

### 3.4 Domain Scope of Tests

The domain scope of each Test is largely provided by the values of the properties associated with the instance of the subclass of bdqffdq:DataQualityNeed. The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) evaluated by each Test are expressed as specific bdqffdq:InformationElements. The bdqffdq:Specification provides details of how to evaluate values of the InformationElements, but also includes references to external authorities (to the Darwin Core standard) that are required to implement the Test. For example, an external references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and where available, a link to a specific online resource such as an API required for the implementation of the Test.

BDQ Core Tests are agnostic about the form in which the data are stored or transported. The Test Specifications all assume that data are presented to the Tests in structured form such as CSV or tab-delimited text files, with data elements identifiable as [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021). Here, cells contain non-typed data values possibly aggregated from and serialized from multiple sources such as relational databases where Boolean nulls and non-string data types may exist, but the data have been exported into a string serialization that supports neither null nor typed data. 

The Tests are also agnostic about uses for quality assurance, where output data are filtered down to those for which (in effect) all Validations are Compliant, or for quality control where the results of Validations, Issues, Measures, and Amendments can be used to improve the quality of the data.

### 3.5 Parameterizing the Tests

Parameterized Tests are those for which we detected a likelihood of different data quality needs within the community of CORE users and CORE needs. For example, the existence of national requirements for spatial data to be represented with a particular datum. When we identified that within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we defined Parameters for the Tests. The Parameter values allow a particular Test to behave differently when given different parameter values.  This allowed the development of generic Tests that provide support for non functional requirements that vary within the community. An example of such a Test is [AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](https://rs.tdwg.org/bdqcore/terms/7498ca76-c4d4-42e2-8103-acacccbdffa7), which takes the Parameter bdq:defaultGeodeticDatum, with a default value that fills most users’ needs of “EPSG:4326”. But we recognized that some users may have requirements that for data to have quality, they must associate dwc:decimalLatitude and dwc:decimalLongitude with a different spatial reference system in dwc:geodeticDatum. Other Tests related to georeferences are similarly parameterized, with a similar default, understanding that most users will be working with dwc:geodeticDatum="EPSG:4326", but others will have requirements for a different spatial reference system. Similarly, parameters are specified for depth and elevation information based on global maximum values, while user communities may have data that falls entirely within some smaller geographic region and may want to impose tighter constraints on depth and elevation for their data to have quality. For example for quality control, to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the Test, the Test will be designated as "Parameterized" and a default provided, along with a link to an appropriate authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the Tests relating to taxonomic names, but the BDQ Core recognizes that other Source Authorities may be required within other communities, for example, The World Register of Marine Organisms [WORMS](https://www.marinespecies.org/) or a national taxonomic authority.  When a Test has a single source authority Parameter, bdq:sourceAuthority is used for that parameter, but if a Test takes more than one source authority Parameter, each is given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority Parameters for the Test [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b9c184ce-a859-410c-9d12-71a338200380).

Parameters, within the namespace bdqffdq: have been modeled as falling within the realm of data quality solutions, they are not attributes of the data, nor are they attributes of data quality needs.

Since value supplied for a parameter for the Test is an attribute of the Mechanism (of the system assessing the data quality), the Specification of a Test cannot evaluate the validity of Parameter values as a part of the Test logic. Consequences from problems with the validity of values of Parameters (e.g., an incorrect IRI for a source authority API endpoint) may only result in Response.status="EXTERNAL_PREREQUISITES_NOT_MET" values, as Parameters are assertions about externalities to the data and may change if the same data are applied to the same Test with a different Parameter configuration.

Parameters are not intended to relax the definition of data having quality for Core needs. The specifications deliberately do not include Parameters that would relax tests on secondary terms for downstream research users or tighten them for upstream data capture. Tests serving the needs of users engaged in data capture or preparing data for aggregation, but not downstream aggregators or research users were considered, but deemed not CORE. We have similarly resisted the temptation to Parameterize Tests to meet the needs of different portions of the data life cycle.

### 3.6 Independence and Paired Tests

To the best of our abilities, we have designed each BDQ Core Test to stand alone.  This design supports the mixing and matching of tests to meet particular data quality needs. We do not impose any particular model of test execution on implementation frameworks. The specification of any interdependencies among Tests would immediately impose constraints upon test execution frameworks.  Implementations of test execution frameworks may execute tests on data records in parallel, on data records in sequence, as queries on datasets, or on unique values. For a subset of Amendments, we do provide guidance on execution order to produce deterministic results.

BDQ Core Amendment Tests are paired with a corresponding Validation Test that assesses the same aspect of data quality. An Amendment Test may be able to improve the quality of data with respect to that Validation. The Framework contains terms for expressing such formal relationships among Tests, we have chosen not to specify these to allow users to more flexibly to address their data quality needs. What we would recommend however, is that the data evaluation process generally run all Validation Type Tests, then Amendment Type Tests, then re-run the Validation Tests a second time.

### 3.7 Vocabularies and Synonyms

As noted above, one early conclusion to this project was the need for controlled vocabularies and led to an early spin-off of the Data Quality Task Group 4: Best Practice for Development of Vocabularies of Value (https://github.com/tdwg/bdq/tree/master/tg4). Testing the 'quality' or 'fitness for use' of Darwin Core encoded data are made more difficult due to the lack of a comprehensive suite of controlled vocabularies.

Testing Darwin Core values against a known Source Authority using a Validation Type Test is straight forward: A Test is either COMPLIANT or NOT COMPLIANT. The BDQ Core standard also includes Tests of type Amendment, and the mapping of input Darwin Core values to known Vocabulary values is poorly developed. If a Validation Test returns COMPLIANT, no amendment is necessary. For example, if the input value to a Test evaluating sex is dwc:sex="Female", then no amendment is required. If however, the input value is dwc:sex="f.", this can likely be interpreted as "Female"? The same is not true for dwc:sex="M" This value could be interpreted as "Male" or "Mixed" according to https://api.gbif.org/v1/vocabularies/Sex/concepts. GBIF currently treats this as "Male" but without a comprehensive synonymy within the vocabularies, one cannot be certain that this is the case. A key phrase within this standard that particularly relates to many of the Expected Responses of Tests is "dwc:term can be unambiguously interpreted as ...". In the case of dwc:sex="M", the determination is that the value is ambiguous and no amendment can be made.

**We see an urgent need for a comprehensive, internationally agreed list of [Darwin Core Term](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) values that are mapped to standard values**. GBIF has implemented some of the unique values for some Darwin Core terms, for example https://api.gbif.org/v1/vocabularies/Sex/concepts/Female/hiddenLabels, but such lists are not currently comprehensive, and we see this is a severe limitation to the evaluation of 'data quality'/'fitness for use'. While there has been a survey of Darwin Core 'distinct values' for GBIF, ALA, iDigBio and VertNet, these are dated, and have not been mapped to standard values, if they exist.

### 3.8 Amendments and Annotations

The BDQ Core Standard supports the W3C Annotation Data Model (W3C 2017) for reporting the results from tests, including Amendment Type Tests. The bdqffdq:Assertion, with its Response.status, Response.result, and a Response.comment can form the body of an annotation, that is be related to an oa:Annotation through oa:body.  A competency question in [Section 2.4 Framework Competency Questions](#24-Framework-Competency-Questions) illustrates how Assertions made by BDQ Core Tests that are wrapped in oa:Annotations could be retrieved.

BDQ Core Amendment Type Tests **propose** changes: It becomes the responsibility of the consumer of the data quality report under Quality Control to assert when and what changes are made to records. The most consistent path is to allow consumers of data quality reports to extract the metadata about the reasoning for a change from the Response.comment in an Amendment Test, and add that to their representation of the data.

Below is an example of a bdqffdq:Assertion forming the body of an oa:Annotation, with triples indicating the implementation that produced the Assertion and relating it back to a bdqcore:Specification (from which the metadata about the Test that was run can be identified).

    <https://example.org/bdq/assertion/51967574-7be9-4e38-938c-5dfec2d4d61d> a bdqffdq:ValidationAssertion ;
        oa:hasResponseStatus bdqffdq:RUN_HAS_RESULT ;
        oa:hasResponseResult bdqffdq:COMPLIANT ;
        oa:hasResponseComment "Exact Match found for [Chicoreus palmarosae (Lamarck, 1822)] to [https://www.gbif.org/species/4365662] running VALIDATION_SCIENTIFICNAME_FOUND." ;
        bdqffdq:appliesTo <https://mczbase.mcz.harvard.edu/guid/MCZ:Mala:280832>

    <https://example.org/annotation/519ab16d-6c00-4a94-a3bd-5418ad391717> a oa:Annotation ;
        oa:body <https://example.org/bdq/assertion/51967574-7be9-4e38-938c-5dfec2d4d61d> ;
        oa:target <https://mczbase.mcz.harvard.edu/guid/MCZ:Mala:280832> ;
        oa:created "2015-01-28T12:00:00Z" ;
        oa:creator <urn:uuid:90516df7-838c-4d53-81d9-8131be6ac713> ;
        oa:motivation oa:assessing .

    <urn:uuid:90516df7-838c-4d53-81d9-8131be6ac713> a bdqffd:Mechanism ;
        a oa:Software ;
        rdfs:label "Kurator: Scientific Name Validator - DwCSciNameDQ:v1.1.1-SNAPSHOT" .

	<urn:uuid:f3a41284-093c-4b7e-8054-a32456a7a427> a bdqffdq:Implementation ;
        bdqffdq:implementedBy <urn:uuid:90516df7-838c-4d53-81d9-8131be6ac713> ;
        bdqffdq:usesSpecification <urn:uuid:3c2fe7e9-186f-4ceb-8274-8bbcb4a62de4> .

### 3.9 Aspirational Aspects of Some CORE Tests

#### 3.9.1 Vocabularies
The Darwin Core Standard (Wieczorek et al. 2012) is deliberately permissive, and the BDQ Core Tests impose additional expectations on data expressed in [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) in the interest of data quality.  Some Tests assert that data must be in the form described in the normative definition of a Darwin Core term (for example, Tests of dwc:day that evaluate compliance with "The integer day of the month ..." - https://dwc.tdwg.org/terms/#dwc:day).  Some Tests evaluate compliance with expectations imposed by non-normative notes/comments or examples in Darwin Core, often working from the phrase in the comments "Recommended best practice is to use a controlled vocabulary".  In BDQ Core we aspire for the community to adopt common controlled vocabularies to improve the quality of biodiversity data.

The flexibility of Darwin Core (Wieczorek et al. 2012), on which BDQ Core is based, in relation to vocabularies, is a problem when 'data quality'/'fitness for use' of Darwin Core records is attempted. Controlled vocabularies seemed a wise aspirational goal and for this reason, as noted elsewhere, the Biodiversity Information Standards (TDWG) Biodiversity Data Quality Task Group 4: Best Practice for Development of Vocabularies of Value was created (https://github.com/tdwg/bdq/tree/master/tg4). Subsequently, GBIFs vocabulary services supporting Darwin Core and other namespaces (see https://rs.gbif.org/vocabulary/dwc/) were developed and are gradually expanding to cover more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021). We look forward to the uptake of a far more comprehensive suite of controlled vocabularies that include synonyms that will greatly improve the quality of biodiversity-related data and its evaluation. We have been working with GBIF on this.

#### 3.9.2 Georeferencing
Some BDQ Core Tests are aspirational about ways in which the community should express things in order for there to be quality, for example, bringing in an understanding of georeferencing best practices (Chapman & Wieczorek 2020) of the set of metadata concepts that need to have values for there for quality georeferences, for example [VALIDATION_GEODETICDATUM_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/239ec40e-a729-4a8e-ba69-e0bf03ac1c44). Similarly, we have encouraged the use of controlled vocabularies that the community should aspire to using, such as the EPSG codes for datums (https://epsg.org)


#### 3.9.3 Annotations
The authors recognized the significance of an annotation standard to BDQ Core and one Test specifically targets record annotations: [ISSUE_ANNOTATION_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1), even though no Biodiversity Information Standards (TDWG) standard exists. We do however acknowledge the Biodiversity Information Standards (TDWG) Annotations Interest Group (https://github.com/tdwg/annotations) has identified the W3C Web Annotation Data Model (W3C 2017) as the obvious way forward.  We understood that the annotation Test may be difficult for many to implement, but we considered this issue of such significance, that we have included it to promote the use of the W3C web annotation data model by the community. We also acknowledge that data aggregators such as the Atlas of Living Australia (https://ala.org.au) have had an operational annotation service for many years (see https://support.ala.org.au/support/solutions/articles/6000262125-flagging-an-issue-with-a-record) but like other current implementations, this service is a subset of what is required for a comprehensive service (e.g., annotations on annotations for one)

#### 3.9.4 "High Seas"

A number of BDQ Core Tests assert a 'lack of quality' for records representing events on the high seas/international waters (outside national jurisdictions) where Tests will return 'NOT_COMPLIANT' as there is no currently agreed standard for designating 'high seas' records using Darwin Core (https://dwc.tdwg.org/). Examples of such Tests include [VALIDATION_COUNTRY_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/6ce2b2b4-6afe-4d13-82a0-390d31ade01c) and [VALIDATION_COUNTRYCODE_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/(https://rs.tdwg.org/bdqcore/terms/). The authors recognize the significance of this issue to the marine community, and we have retained these Tests to promote an agreement on an international standard. We acknowledge a current user-assigned ISO 3166-alpha-2 country code (dwc:countryCode - https://dwc.tdwg.org/terms/#dwc:countryCode) of "XZ" to infer "international waters" (see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#XZ and https://en.wikipedia.org/wiki/UN/LOCODE). While country code "XZ" looks like a much-needed advance, its use has not be standardized. The situation with populating a country value (dwc:country - https://dwc.tdwg.org/terms/#dwc:country) with "high seas" or "international waters" or something else is less advanced, but we have retained the country Test, aspirational. Related BDQ Core Tests such as [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134), [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b9c184ce-a859-410c-9d12-71a338200380) and [VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b23110e7-1be7-444a-a677-cdee0cf4330c) don't present as much an issue, due to the Specifications including the phrase "INTERNAL_PREREQUISITES_NOT_MET" if dwc:countryCode or dwc:country are bdq:Empty, as would be currently expected for records in international waters. The Specification in effect says "This test can't be run because a vital piece of information required is absent". While currently acceptable, once a standard for international waters/high seas is established, the Tests will need to be revisited.

### 3.10 Tests and Test Vocabularies

The development of the BDQ Core Tests and associated assertions was our core business. To achieve that outcome, we needed to describe the Tests in a comprehensive and consistent manner.  While the Data Quality Framework (Veiga 2016, Veiga et al. 2017) developed a formal model for describing data quality and fitness for use ontology for 'data quality'/'fitness for use', it would be fair to say that while we committed to representing Tests using this model, it initially took an independent, and 'bottom-up' approach.  As noted above, we first examined what tests agencies and others in the community were using to assess data quality and then filled gaps, establishing criteria for test inclusion or exclusion. We then started framing each of the included tests in a common format, which meant the formation of useful descriptive terms.  Both the tests and the vocabulary evolved: The Tests refined our vocabulary and our vocabulary refined our tests.  The single resulting vocabulary, represented as a markdown table in GitHub (https://github.com/tdwg/bdq/issues/152) became a single central place for evaluating and refining terms, scope and definitions.

After some years of work, our vocabularies and Tests were effectively merged with the Framework ontology. A good example of this evolution was reformulating Tests from 'negative' (having issues) to 'Positive' (having quality). Tests like VALIDATION_COUNTRY_NOTFOUND became [VALIDATION_COUNTRY_FOUND](https://rs.tdwg.org/bdqcore/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134). The independence of development of the Tests lead to improvements and clarifications in the Framework ontology.  The BDQ Core Test development process identified very clear needs for tests to be able to be parameterized and for tests to be able to identify elements of the data that might be problematic for some use case.  This lead to the introduction of the concepts of bdqffdq:Parameter and bdqffdq:Issue. The names of some terms in the ontology was very opaque, and names were not entirely consistent, so elements were renamed for clarity (e.g., ContextualizedEnhancement became bdqffdq:Amendment) and to follow consistent naming patterns.  

Once the vocabulary terms and their definitions had become stable, they were assigned to (or ported back into) specific namespaces: 

- bdqffdq	https://rs.tdwg.org/bdqffdq/terms for the ontology that forms the Framework for defining data quality 
- bdqdim	https://rs.tdwg.org/bdqdim/terms/ for the Data Quality Dimension of (Measures and all) the Tests
- bdqcrit	https://rs.tdwh.org/bdqcrit/terms/ for the Criteria of the Validation and Issue Tests
- bdqenh	https://rs.tdwg.org/bdqenh/terms/ for the Enhancements of the Amendment Tests
- bdq	https://rs.tdwg.org/bdq/terms/ for terms used to construct Specifications: source authorities, parameters, Information Elements, and the concepts bdq:Empty and bdq:NotEmpty

These vocabularies all fed into a formal description of the Tests as terms in the bdqcore: namespace (bdqcore: https://rs.tdwg.org/bdqcore/terms/) where the Tests with their descriptions were framed using the other vocabularies.

A few terms in the vocabulary table were seen as glossary terms (e.g., "geodetic datum") for which a formal vocabulary is not required.  These are presented in tables as a glossary in relevant descriptive documents. 

### 3.11 Principles of Test Design

This section provides an elaboration of the summary of the key criteria of the BDQ Core Tests in [Section 2.1](#21-definition-of-core).

The principles of data quality test design emphasize simplicity, clarity, and atomicity in test specifications. Tests should be deterministic, reversible when applicable, and avoid false precision while using realistic benchmarks. They should refrain from validating verbatim terms, and be designed to produce consistent, meaningful results across different implementations and datasets.

#### 3.11.1 General concepts for specifications

The bdqffdq ontology provides a description of the specifications for a test, a standard interface for test invocation, and a description of the content of test results.  Tests are thus all specified following the bdqffdq ontology.  All tests require both a concise description of the specification and a pair of examples, one for a pass scenario and one for a fail. The Specification has been designed to communicate concisely about the nature of the Tests to implementers; where any ambiguity will invalidate a Test.  Each Test Specification follows a standard form.   A consistent concept and definition of EMPTY is used across all Tests, tests must reference this concept rather than test various other concepts of empty values.

Tests should be informative when applied to data found in the wild.  Each Test provides information about some aspect of the 'quality' / 'fitness for use' of the data for some specified purpose.  While the Tests have been developed to address a wide variety of needs, we accept that some tests may of course, not be applicable in some domains; some tests may be irrelevant in some contexts.  A suite of tests assembled for some Use Case should all be informative for that Use Case.  Tests are widely applicable, address quality needs, and must be tied to at least one identified Use Case.  Test development should not start with "here's a term, these are sane values it could hold", but rather with "here is an identified need for quality in the values in this term".  

Given that the Tests are based on Darwin Core terms, we 'piggy-back' on the community acceptance and understanding of Darwin Core.  Tests evaluate values based on the normative definition of terms, and against non-normative guidance provided with each term (the Notes/Comments), and may bring in other concepts from the real world (e.g., practical limits on elevation and depth) or vocabularies.  In general, tests are only possible for terms where the value is bounded by real world extents, or by an agreed vocabulary.

#### 3.11.2 Principles

**Informative**.  In general, Tests have power when they will likely result in neither 0% nor 100% of all record hits.  That is, a Validation should not in general be expected to return NOT_COMPLIANT for almost all data in the wild or COMPLIANT for all wild data.  Tests may however identify non-compliant data in a large portion of cases where we highlight an important point about quality that should be, but is not currently met by the community, e.g., where dcterms:license is EMPTY, that is where a large portion of the community is not providing values for a term important for data quality, or providing values for a term inconsistent with best practices.

**Simple**.  Each Test specification must be as simple as possible. The more complex a Test, the more difficult it will be to implement and to evaluate against real-world data. While the human-readable description of the test may be open to interpretation, Test Specifications were written to allow for no ambiguity. In some cases, this has meant that some Specifications are lengthy, but required if implementation and interpretation are to be accurate.   For example, [VALIDATION_GEOGRAPHY_STANDARD](https://github.com/tdwg/bdq/issues/139) was proposed, but after discussion abandoned and tagged as DO NOT IMPLEMENT as involving too much complexity to be able to phrase a clean and simple specification.  Conversely, [VALIDATION_DAY_STANDARD](https://rs.tdwg.org/bdqcore/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498) asks one simple question: is the value of dwc:day an integer in the range 1 to 31.  

**Atomic**.  Specification should be as atomic as possible, dealing with only a single evaluation.  For example, evaluating dwc:minimumDepthInMeters should involve separate tests to evaluate if a value is present, if the value is numeric, if the value is within a reasonable range, or if the minimumDepthInMeters is smaller or equal to the maximumDepthInMeters.  These should not be combined into a single test, though tests that rely upon an interpretable value may build on a logic that evaluate as INTERNAL_PREREQUISITES_NOT_MET if no value is present or if it is not interpretable before proceeding to the central assertion of the test.  Each test should be designed to independent of other tests.  For example, the test [ISSUE_DAYMONTH_SWAPPED](https://github.com/tdwg/bdq/issues/37) was proposed, but abandoned and tagged as DO NOT IMPLEMENT, in part because of the comment identifying potentially entangled causes and a lack of atomicity: "It would seem this test assumes that there is a transposition as opposed to just an error in the month field. It is risky to assume that, and could lead to other or greater issues." [comment by Paula Zermoglio](https://github.com/tdwg/bdq/issues/37#issuecomment-357280140).   Conversely, [VALIDATION_DAY_STANDARD](https://rs.tdwg.org/bdqcore/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498) and [(VALIDATION_DAY_INRANGE](8d787cb5-73e2-4c39-9cd1-67c7361dc02e) related, but different, questions about the value in dwc:day, each separating out a distinct element of quality.

**Deterministic**.  Tests should be deterministic.  When presented with the same data and the same configuration, different test implementations and different runs of the same test at different times on the same data and configuration should produce the same results.  Each test which references a controlled vocabulary must do so with an explicit statement of what the source authority for that vocabulary is.

**Reversible**.  Amendments which propose conversions or transformations of values should do so in a way that is reversible.  For example in [MINDEPTHMAXDEPTH_FROM_VERBATIM](https://rs.tdwg.org/bdqcore/terms/c5658b83-4471-4f57-9d94-bf7d0a96900c) a verbatim depth of "10 feet" should be converted to 3.048 to fill in the minimum and maximum depths in meters.

**Avoid false precision**.  Except where required for reversibility, tests must not ascribe precision where it is unknown.  For example, in [AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](https://rs.tdwg.org/bdqcore/terms/7498ca76-c4d4-42e2-8103-acacccbdffa7), when the value "EPSG:4326" is assumed to be the datum, the value of coordinateUncertaintyInMeters is increased to reflect the added uncertainty, not left unchanged reflecting a potentially false higher precision.   Spatial buffering is explicitly REQUIRED in the Specification for spatial intersections Tests (e.g., point in polygon). For example, the Test COUNTRYCODE_FROM_COORDINATES.

**Realistic**.  If testing the value of terms that have practical ranges (e.g., dwc:maximumElevationInMeters), real-world values should be used as a limit. For example, the height of Mount Everest: 8848m provides an appropriate value as a limit to the largest valid maximum elevation value. 

**Compare data with data**.  When testing consistency between or among terms, values in one term that is non-EMPTY are not held to be inconsistent with EMPTY terms. For example, in the Test [VALIDATION_EVENT_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/5618f083-d55a-4ac2-92b5-b9fb227b832f), if dwc:eventDate is '2016-12-04' and dwc:day is '4', and the other event terms are empty, the absence of values in dwc:year and dwc:month does not make the values that are present inconsistent.

**Avoid validation of verbatim terms**.  Tests should not attempt to validate the content of literal verbatim terms (e.g., dwc:verbatimLocality), though such terms may be informative for validation or amendment of other terms.

**Proven by implementation, validated with data**.  We repeatedly found that an initial phrasing of the specification of a test did not survive implementation, and subsequent phrasings did not survive exposure to multiple test values.  Test specifications written without implementation and without validation against data from the wild often hide hidden assumptions, missing elements of logic, and incorrect assumptions about how a test implementation might behave.  Actually producing a test implementation, and testing the implementation against input data values and expected response values (with cases provided by more than one person) have proved essential for test specification development.  

**Conflicts between these principles can be expected**.  For example, [AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](https://rc.tdwg.org/bdqcore/7498ca76-c4d4-42e2-8103-acacccbdffa7) and its related validation proved difficult to develop, with conflicts between simplicity and the power of the test, and conflicts between the guidance in the non-normative Darwin Core Notes/Comments for the term and best practices.  Requirements for data quality arising from spatial analysis impose an expectation that dwc:geodeticDatum be explicit about what is being said about the associated dwc:decimalLatitude and dwc:decimalLongitude values, with this best being expressed as EPSG code in the form Authority:Number (e.g., EPSG:4326), while much of the data in the wild is in the form of less explicit text strings (e.g., WGS84), thus these tests are aspirational in seeking to drive the community to best (explicit) practices.  A simple validation could ask if dwc:geodeticDatum matches any EPSG code in the form Authority:Number, but the definition of dwc:geodeticDatum explicitly limits values to those that represent the Coordinate Reference System for the geographic coordinate expressed by dwc:decimalLatitude and dwc:decimalLongitude, or a datum or ellipsoid appropriate for such.  This means only a subset of EPSG codes have quality, adding complexity to the test definition and implementation (with the GBIF vocabulary for Geodetic Datum not helping as it does not assert the authority for the numeric values (with both ESRI and EPSG authorities in use by consumers of spatial data), and it does not provide a means to identify which values are appropriate for dwc:geodeticDatum, given the limitations of the definition to geographic coordinate reference systems).  Furthermore, the [Georeferencing Best Practices](https://docs.gbif.org/georeferencing-best-practices/1.0/en/) guide (Chapman and Wieczorek 2020), specifies the use of "not recorded" for unknown values (under specified conditions), while the Notes/Comments on dwc:geodeticDatum recommend the use of "unknown", here we support the best practice guide, but need to include the explicit value "not recorded" as valid for dwc:geodeticDatum, as well as a specified subset of EPSG codes.  Thus, each test specification must be "as simple as possible", with tradeoffs from other principles likely increasing the minimum complexity.

#### 3.11.3 Consistent behaviors

Amendments must be explicit about whether they propose to fill in EMPTY values, or propose changes to existing values.  

Tests may be parameterized to accommodate national requirements or use case specific variations in quality needs.  For example, “minimum depth in meters is greater than indicated on GEBCO chart”.  Defaults in different Use Cases will need to be accommodated. For example, WGS84 is assumed as a geodetic datum in many cases, but not all, and such cases should be addressed by parameterizing tests to allow for different behaviors of the same test for different data quality needs.

Leading/trailing whitespace or non-printing characters in values shall cause validations against controlled vocabularies to be NOT_COMPLIANT, are proposed to be removed by amendments, and may be ignored when evaluating numeric values.

#### 3.11.4 Avoid test interdependencies

Each test should be able to run without dependencies on other tests.  Sequence of test executions is left to workflows and test execution environments.  

Validations are normally paired with Amendments, with one (or more) validation assessing attributes of quality of some term, paired with an amendment that improves the quality of data in this term.  A workflow may thus assemble tests by running the Validations before running the related Amendments. For example, a Validation of a Darwin Core term such as dwc:occurrenceStatus is first evaluated against a Source Authority before an Amendment that could conform non-standard values to an expected vocabulary is run against that term.  This can be followed by a repetition of the Validation, taking any proposed changes from the amendment as input, in a sequence of VALIDATE-AMEND-VALIDATE, with a comparison of the initial validation results with the final validation results as a measure of ability of the Amendment to improve the data quality.  This is a good practice, and test specifications may assume that tests are intended to be composed in this manner.

Amendments, however, may have complex potential interrelationships, as Darwin Core is by design permissive, with more than one term able to express the same concept (e.g., eventDate, day, month, year, startDayOfYear, endDayOfYear).  To address these potential interrelationships,  for each concept area (e.g., DarwinCore class), a canonical term or set of terms is identified (e.g., eventDate), and tests are structured around improving that canonical concept (thus amendments to fill in eventDate from day, month, and year).   Sequence of operations may be important here, and sets of related amendments need to be designed to avoid overriding information in canonical terms with information from other terms.  That is, Amendments are defined that seek to amend or populate canonical term based on values from other terms, with the canonical term given priority as the term to which consumers of data should look for quality data.  

## 4 Date and Time Issues

BDQ Core avoids analysis of two 'time' and 'date' issues, time zones and geographic and temporal variation in the change from Julian to Gregorian calendars.

### 4.1 Dates and Calendars

Different calendars have been used at different times in different places, and the transcription of an original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date. Metadata may or not be present to even identify such records.

Countries and researchers have changed from the Julian calendar to the Gregorian calendar at different times. For example, Russia adopted the Gregorian Calendar on the ISO date 1918-02-14, the British Empire in 1752-09-14, different regions in France between 1582 and 1760, with France also adopting the French Republican Calendar 1793-1805. The difference between the Gregorian and Julian calendar has typically been around 10 days, but the day that is considered the first day of the year has also changed at different times in different countries. This means that the difference can be as great as 1 year and 10 days. 

Given the complexity and ongoing nature of transitions between calendars, we do not advocate using the Test [VALIDATION_EVENTDATE_INRANGE](https://rs.tdwg.org/bdqcore/terms/3cff4dc4-72e9-4abe-9bf3-8a30f1618432) for quality assurance by selecting a transition date and using it as a threshold. This Test can not assess if a date is actually within a Gregorian date interval, except in special cases where the Julian and Gregorian calendars coincide, and even that is ignoring all other possible calendars. Instead, this Test is able to evaluate a date following the ISO 8601-1 date specification is within a range specified in that context. 

In general, assessing whether a date in biodiversity data was Julian or Gregorian is treated here as an intractable problem, and the problem of correctly determining the Gregorian value for dwc:eventDate is left in the hands of data providers who may have additional knowledge of collectors and their practices to assess how to interpret verbatim date values found in their historical records. For data consumers, this means that historical dates, even into recent times, may have systematic errors in subsets of the data where the date was Julian but has been treated as Gregorian.  This can, in some cases, introduce errors on the scale of one year differences between reported and correct eventDate values. 

### 4.2 Time

If a time zone is not included as a component of date and time, the date and time information is expected to be consistent throughout the event terms

Time is treated as out of scope for BDQ Core Use Cases.  In cases where time zone data are important, dates within a MultiRecord from multiple sources may have multiple plus or minus one day errors introduced. For example, the event_date_qc (Morris & Lowery 2024) implementation of [AMENDMENT_EVENT_FROM_EVENTDATE](https://rs.tdwg.org/bdqcore/terms/710fe118-17e1-440f-b428-88ba3f547d6d) contains the commented out block of code below that is pertinent to time zone issues.   It would populate eventTime from eventDate, converting a local time in eventDate to UTC, where other blocks in the Amendment should, but may not have, taken account of a local time zone in populating dwc:day, dwc:month, dwc:year, dwc:startDayOfYear and dwc:endDayOfYear. (dwc:day, dwc:month, dwc:year, dwc:startDayOfYear, dwc:endDayOfYear and dwc:eventTime should all be consistent, but there aren't unit tests in place to confirm this).

// Time could also be populated, but it isn't in scope for this issue.
// Here is a minimal implementation,
// which illustrates some issues in implementation (using zulu time or not, dealing with time in ranges...)
if (DateUtils.isEmpty(eventTime)) {
        if (DateUtils.containsTime(eventDate)) {
                String newTime = DateUtils.extractZuluTime(eventDate);
                result.addResult("dwc:eventTime", newTime );
                result.setResultState(ResultState.FILLED_IN);
            result.addComment("Added eventTime ["+ newTime +"] from eventDate ["+eventDate+"].");
        }
}

![DateTime](https://imgs.xkcd.com/comics/datetime.png "DateTime")

From [xkcd.com/2867](https://xkcd.com/2867/), by Randall Munroe, xkcd.com.  Licensed under a [Creative Commons Attribution-NonCommercial 2.5 License](https://creativecommons.org/licenses/by-nc/2.5/)


## 5 Rationale Management Documentation

### 5.1 Developing BDQ Core Tests Using Github Issues

The Tests were developed as issues in the tdwg/bdq GitHub environment. The reasoning was that GitHub provided a comprehensive and consistent environment in which to develop, expose, discuss and manage all aspects of the development of BDQ Core. We used a standard template as the first Comment on GitHub Issues pages for documenting all Tests. This immediately exposed all proposed tests to anyone following the work. GitHub then enabled anyone to comment on the Test issues, facilitating discussion. When there was general agreement among the Authors, the values within the template could be easily modified and documented.  The comments in the issues served as a tool for rationale management, documenting why particular decisions were made about the tests during their development.

GitHub's API also provided ample latitude to 'scrape' and filter Issues using GitHub tags (see below) to extract any subset of Tests by Descriptors to CSV files that would be used in the submission and proposed maintenance of the BDQ Core standard.   The [bdq_issue_to_csv](https://github.com/kurator-org/bdq_issue_to_csv) library (Morris 2024) uses GitHub's API to obtain a json representation of the GitHub issues, then parses the agreed upon format for markdown tables for describing issues into a CSV file (destined to become the [term-version CSV](../../vocabulary/bdqcore_term_versions.csv) file for the bdqcore: vocabulary.  The [kurator-ffdq](https://github.com/kurator-org/kurator-ffdq) library (Lowery et al. 2024), which contains a Java representation of bdqffdq: classes is used to process the term-version file into RDF representations of the tests (e.g., [bdqcore.xml](../../dist/bdqcore.xml) (and can also query combined bdqffdq: and bdqcore: rdf, and can generate stub python and java methods for test implementations, and can also execute appropriately annotated Java test implementations and produce data quality reports).  

### 5.2 Github Tags and Categorizing Issues

The development of each Test, with documentation of why particular decisions were made with regard to that test, has been documented in issues in the tdwg/bdq GitHub repository. Each Test issue was tagged with the following GitHub issue labels to assist in finding, evaluating, and asserting conclusions about each Test. 

These tags are retained as the "Github Issue Labels" (a skos:note on each Method instance) in BDQ Core.

| tag | definition | comment |
| --- | ---------- | ------- |
| Amendment | A label to indicate a Test of Type Amendment which may propose a change or addition to at least one [Darwin Core Term](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that is intended to improve one or more components of the quality of the record. | See bdqffdq:Amendment |
| CORE | Conclusion that a Test is useful for evaluating biodiversity data quality as represented by the values of Darwin Core terms. CORE tests address identified user needs, are widely applicable, informative, unambiguous, well defined, and straight forward to implement.  The CORE tests have become the tests defined as part of BDQ Core. |  |
| DO NOT IMPLEMENT | Conclusion that a test is not recommended to be implemented with the current level of understanding for one or more reasons: Available vocabularies are ambiguous; the test is too complex to implement concisely; implementation is expected to lead to ambiguous or inaccurate results. | See Section 2.1.1 |
| Immature/Incomplete | Conclusion that a test requires substantial work needed to develop the specification to the point where the test can be reliably and usefully implemented. This may indicate work that is wholly internal to the test specification such as developing a consistent Expected Response, or may indicate that external work is needed to develop an agreed vocabulary for values of the tested term. An immature/incomplete test may be made CORE, Supplementary, or DO NOT IMPLEMENT when relevant criteria are satisfied. |  |
| ISO/DCMI STANDARD | A reference to either an ISO (International Organization for Standardization) Standard or a DCMI (Dublin Core Metadata Initiative) Standard |  |
| Issue | A label to indicate a test of type ISSUE, where potential problems are flagged and may need examination by the user to determine if data have quality for their use. | see bdqffdq:Issue |
| Measure | A label to indicate a Test of Type Measure that performs a measurement according to some data quality dimension. | See bdqffdq:Measure |
| [NAME](#NAME) | A label to indicate that the Test is related to Darwin Core terms in the dwc:Taxon Class. |  |
| NEEDS WORK | A label that indicates that an issue (Test) requires more work before finalizing. | Supports a workflow of contributors identifying tests needing work with this tag, and review of issues with this tag in task group meetings.  |
| [OTHER](#OTHER) | A label to indicate that the Test is related to Darwin Core terms other than Classes dwc:Taxon, dwc:Location or dwc:Event. |  |
| Parameterized | A label for a Test that a bdq:Parameter may be set prior to a Parameterized Test being run. |  |
| [SPACE](#SPACE) | A label to indicate that the Test is related to Darwin Core terms in the dwc:Location Class. |  |
| Supplementary | Conclusion that a Test is regarded as not CORE (cf. the tag CORE, and BDQ Core) because of one or more reasons: Not widely applicable; not clearly matched to an identified data quality need; not informative concerning the 'quality' or lack of quality of the data; likely to return a high percentage of either bdq:NOT_COMPLIANT or bdq:POTENTIAL_ISSUE records. A Supplementary test MAY be implemented in a local implementation if a suitable use case exists. | A Supplementary test may be made CORE at a later time.  |
| Test | Tests descriptions created by TG2, either CORE, Immature/Incomplete, Supplementary, or DO NOT IMPLEMENT. | Supports workflows for exporting tests from issues to process the markdown into CSV files for review.  |
| TG1 | Issues pertinent to Task Group 1 ([Framework on Data Quality](https://tdwg.github.io/bdq/tg1/site)) of the Biodiversity Information Standards (TDWG) Data Quality Interest Group. |  |
| TG2 | Issues including Tests, developed by, or pertinent to Task Group 2 ([Data Quality Tests and Assertions](https://github.com/tdwg/bdq/blob/master/tg2/README.md)) of the Biodiversity Information Standards (TDWG) Data Quality Interest Group. |  |
| TG3 | Issues pertinent to Task Group 3 ([Data Quality Use Cases](https://github.com/tdwg/bdq/blob/master/tg3/README.md)) of the Biodiversity Information Standards (TDWG) Data Quality Interest Group. |  |
| TG4 | Issues pertinent to Task Group 4 ([Best Practices for Development of Vocabularies of Value](https://github.com/tdwg/bdq/blob/master/tg4/README.md)) of the Biodiversity Information Standards (TDWG) Data Quality Interest Group. |  |
| [TIME](#TIME) | A label to indicate that the Test is related to Darwin Core terms in the dwc:Event Class. |  |
| Validation | A label to indicate a Test of Type Validation that describes a run of a Test for validity against a set of criteria. | See bdqffdq:Validation |
| VOCABULARY | A label to indicate that a Test requires a controlled Vocabulary |  |

The CORE, DO NOT IMPLEMENT, Immature/Incomplete, and Supplementary tags mark conclusions made about each proposed Test.

Supplementary Tests have been exported to a CSV list of tests and have RDF representations generated with the same tools as the BDQ Core Tests, these files are in the [supplement/](../../docs/supplement) directory.

The tag NEEDS WORK was repeatedly added and removed to issues and was a valuable support for the evaluation of tests in repeated feedback loops of: Frame the description of a test, independently produce validation data and an implementation, run the implementation against the validation data, evaluate cases where the expectations in the validation data differ from the Test results (which could be a defect in the implementation, in the validation data, or a problem in the Test Specification), discuss as a group, make changes as needed, and repeat.

#### 5.2.1 Diagram of the NAME-oriented tests and InformationElementsActedUpon
![Diagram of the 'NAME'-oriented tests and InformationElementsActedUpon.](TestsName.png "NAME by InformationElements")

#### 5.2.2 Diagram of the SPACE-oriented tests and InformationElementsActedUpon
![Diagram of the 'SPACE'-oriented tests and InformationElementsActedUpon.](TestsSpace.png "SPACE by InformationElements")

#### 5.2.3 Diagram of the TIME-oriented tests and InformationElementsActedUpon.
![Diagram of the 'TIME'-oriented tests and InformationElementsActedUpon.](TestsTime.png "TIME by InformationElements")

#### 5.2.4 Diagram of the OTHER-oriented tests and InformationElementsActedUpon
![Diagram of the 'OTHER'- oriented tests and InformationElementsActedUpon.](TestsOther.png "OTHER by InformationElements")

### 5.3 Using Markdown Tables in Github Issues to Develop Test Descriptors

Each test issue in GitHub begins with a table in markdown format describing the Test.  The terminology of the Test Descriptors in this markdown table documented below differs slightly from the terms used in the Framework but represent all key aspects of each test. Some Descriptors such as the GUID are intended for machine consumption, some such as the "Description" are designed to be human-readable for consumers of biodiversity data quality reports while Descriptors such as the "Specification" ensure that implementers have no ambiguity about how the test should be coded. 

**Title** [non-normative]: A standardized, human readable name of the Test-assertion based roughly on the template TG2-TESTTYPE_INFORMATIONELEMENT_CRITERIA, for example [TG2-VALIDATION_BASISOFRECORD_STANDARD](https://rs.tdwg.org/bdqcore/terms/42408a00-bf71-4892-a399-4325e2bc1fb8). These names were considered helpful for human-human communication and assisted with code implementation, maintenance and searches. A number of the Tests did however, only loosely conform to this template due to the difficulty of rendering them otherwise, for example [TG2-VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION](https://rs.tdwg.org/bdqcore/terms/d708526b-6561-438e-aa1a-82cd80b06396), but the titles remained obvious and therefore useful.

**GUID** [normative]: A globally unique identifier which allows software to uniquely identify each Test, for example 8f1e6e58-544b-4365-a569-fb781341644e. The GUID in the markdown table becomes the local part of the IRI for the test (for example https://rs.tdwg.org/bdqcore/terms/8f1e6e58-544b-4365-a569-fb781341644e) when translated to RDF.

**Label** [normative]: A human readable label identifying the Test. The labels are TESTTYPE_INFORMATIONELEMENT_CRITERIA part of the Title, for example [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe).  The Label becomes the rdfs:label when translated to RDF.
 
**Description** [non-normative]: A brief English language description of what the Test does, for example "Does the value of dwc:basisOfRecord occur in bdq:sourceAuthority?"  

**Test Type** [non-normative]: Tests have been classified into four Fitness for Use Framework classes. Validation Tests validate values in one or more [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021), for example [VALIDATION_SCIENTIFICNAME_FOUND](https://rs.tdwg.org/bdqcore/terms/3f335517-f442-4b98-b149-1e87ff16de45). Issue flags a potential problem that requires human interpretation, for example [ISSUE_DATAGENERALIZATION_NOTEMPTY](https://rs.tdwg.org/bdqcore/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2). Amendment suggests an improvement that will result in a change or addition to at least one Darwin Core term, for example [AMENDMENT_COORDINATES_FROM_VERBATIM](https://rs.tdwg.org/bdqcore/terms/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e). Measure returns a numeric value, for example [MEASURE_VALIDATIONSTESTS_COMPLIANT](https://rs.tdwg.org/bdqcore/terms/45fb49eb-4a1b-4b49-876f-15d5034dfc73).

**Darwin Core Class** [non-normative]: The Darwin Core class that contains the Information Elements, for example: dwc:Taxon.

**Information Elements Consulted** [normative]: The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that the Test takes as input, for example: dwc:countryCode for the Test  [VALIDATION_COUNTRYCODE_STANDARD](https://rs.tdwg.org/bdqcore/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe)

**Information Elements ActedUpon** [normative]: The [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) that is the focus of the Test, for example:dwc:verbatimCoordinates, dwc:verbatimLatitude, dwc:verbatimLongitude, dwc:verbatimCoordinateSystem, dwc:verbatimSRS for the Test [AMENDMENT_COORDINATES_FROM_VERBATIM](https://rs.tdwg.org/bdqcore/terms/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e).

**Expected Response (Specification)** [normative]: A concise description of the logic of the Test to clarify its implementation. The Expected Response takes the form (for a VALIDATION) of: EXTERNAL_PREREQUISITES_NOT_MET if \<condition\>; INTERNAL_PREREQUESITES_NOT_MET if \<condition\>; COMPLIANT if \<condition\>; otherwise NOT_COMPLIANT. Example: "EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is EMPTY; AMENDED the value of dwc:basisOfRecord if it could be unambiguously interpreted as a value in bdq:sourceAuthority; otherwise NOT_AMENDED".

**Data Quality Dimension** [normative]: A Test will focus on one of the following scenarios based on the Data Quality Framework: "Completeness" (extent to which data elements are present and sufficient); "Conformance" (conforms to a format, syntax, type, range, standard or to the own nature of the Information Element); "Consistency" (agreement among related Information Elements in the data); "Likeliness" (probability that values are real); "Resolution" (is sufficient detail present in the value/s - a measure the granularity of the data). The [data quality dimension](../list/bdqdim/index.md) for this Test. Example: "Conformance"

**Term_Actions** [non-normative]: The last two components of the Label, useful in filtering Tests in CSV files, for example: "COUNTRYCODE_STANDARD"

**Parameter(s)** [normative]: Parameters that modify the behavior of the Test, along with default values or links to Source Authorities (see [3.5 Parameterizing the Tests](#35-parameterizing-the-tests)). A parameter value exists only where there are a number of alternate options for a Source Authority. For example, "bdq:sourceAuthority default = "GBIF Backbone Taxonomy"" is parameterized as it allows for regional taxonomic authorities; whereas "bdq:sourceAuthority is "EPSG:" [https://epsg.io]"" is not parameterized as there is a single Source Authority. Example: bdq:defaultGeodeticDatum.

**Source Authority** [normative]: A reference to an authority required by the Test along with a default value where Tests may require reference to an external reference such as standard vocabularies of terms or names. The structure of the information in Source Authority ideally has two components. The first component refers to the standard itself, which may include a vocabulary of accepted values. The second component will, wherever possible (and if available), refer to an API that will assist implementers of Tests.  For example, bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of API endpoints or other resources}. The "Normative String Identifier" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be the parameter value. In some cases, the API component will refer to a 'third party' site which will hopefully remain in sync with the standard, for example, a GBIF vocabulary API site would ideally be synced with a Darwin Core site. When a Test uses more than one sourceAuthority at the same time, these are given separate names, for example, "bdq:taxonIsMarine" and "bdq:geospatialLand" are the two sourceAuthority Parameters for [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](https://rs.tdwg.org/bdqcore/terms/b9c184ce-a859-410c-9d12-71a338200380).

While applying to a single record (bdqffdq:SingleRecord), the Test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. 

Only a subset of all [Darwin Core Terms](https://dwc.tdwg.org/list/) (Darwin Core Maintenance Group 2021) are referenced in the CORE (or Supplementary) Tests. Each Test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related Darwin Core terms; the Information Elements which form the input data to the Tests. Example: "bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}". 

**Specification Last Updated**: Date of last change to a Normative part of the Test, for example to the wording of an Expected Response/Specification, for example "2023-06-23".

**"Examples"** [non-normative]: Example of inputs and the expected output from an implementation of the Test given those outputs.  ‘Pass’ and ‘Fail’ type examples are provided for clarity of each Test.  All examples listed are also present in the the validation data suite. Example: "[dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"]"

**Source** [non-normative]: The origin of the concept of the Test, for example "The Atlas of Living Australia".

**"References"** [non-normative]: A list of references that will assist in a thorough understanding of the Test, for example: "GBIF Secretariat (2019). GBIF Backbone Taxonomy. Checklist dataset (https://doi.org/10.15468/39omei)"

**Example Implementations (Mechanisms)** [non-normative]: One or more entities that have an implementation of the Test, for example "Kurator/Filtered Push event_date_qc library".

**Link to Specification Source Code** [non-normative]: A link to code that implements the Test, for example "https://github.com/FilteredPush/ event_date_qc/blob/5f2e7b30f8a8076977b2a609e0318068db80599a/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L169".

**Notes** [non-normative]: Additional comments that the Authors believed necessary for an accurate understanding of the Test or issues that implementers needed to be aware of. Example: For [TAXONID_FROM_TAXON](https://rs.tdwg.org/bdqcore/terms/431467d6-9b4b-48fa-a197-cd5379f5e889), “This is the taxonID inferred from the Darwin Core Taxon class, not from any other sense of Taxon. Return a result with no value and a Result.status of NOT_AMENDED with a Response.comment of ambiguous if the information provided does not resolve to a unique result (e.g., if homonyms exist and there is insufficient information in the provided data, for example using the lowest ranking taxa in conjunction with dwc:scientificNameAuthorship, to resolve them).  When referencing a GBIF taxon by GBIF's identifier for that taxon, use the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:taxonID.”.

## 6 Code used to build BDQ Core Components

The specifications for the BDQ Core Tests were developed in Markdown Tables in GitHub issues (initially created by Alex Thompson by using the GitHub API from a spreadsheet of tests developed in the BDQ TG2 Gainesville meeting).  It was recognised early on that these would also need to be serialized to CSV (and later that this CSV would need to become a term-version file), so code was written (python by Lee Belbin, and Java (bdq_issue_to_csv (Morris 2024))) to extract the markdown tables to CSV lists of tests.  The descriptors in the issue markdown tables changed over time, and the columns in the CSV also changed over time (most markedly in late 2024 while preparing BDQ Core for submission), so this code has changed over time.  The kurator-ffdq (Lowery et al. 2024) code developed by David Lowery is capable of loading a CSV list of test descriptors into a set of Java classes that can be serialized as RDF.  This code was maintained and the configuration changed over time to accomodate changes in the test CSV file.  Kurator-ffdq was regularly used to produce RDF representations of the tests.  Kurator-ffdq is also able to generate stub Java (and python) methods, and this functionality was used to add tests to and maintain 4 FilteredPush/Kurator libraries of test implementations.  

BDQ Core `_review` is built with the following three sets of shell scripts:

- bdq_issue_to_csv [make_test_csv.sh](https://github.com/kurator-org/bdq_issue_to_csv/blob/v1.0.0/make_test_csv.sh)
- [bdq/tg2/\_make_review/copy_files.sh](https://github.com/tdwg/bdq/blob/540eae5b1e609025b8dcbf19a7830d5c880aaf20/tg2/_make_review/copy_files.sh)
- [bdq/tg2/\_make_review/do_build.sh](https://github.com/tdwg/bdq/blob/540eae5b1e609025b8dcbf19a7830d5c880aaf20/tg2/_make_review/do_build.sh)

For details on the Test Validation Data see: 

- bdqtestrunner [README](https://github.com/FilteredPush/bdqtestrunner/blob/master/README.md)
- [bdq/tg2/core/squish_validation_data.py](https://github.com/tdwg/bdq/blob/540eae5b1e609025b8dcbf19a7830d5c880aaf20/tg2/core/squish_validation_data.py)

For more information see the following README files: 

- bdq_issue_to_csv [README](https://github.com/kurator-org/bdq_issue_to_csv/blob/master/README.md)
- kurator-ffdq [README](https://github.com/kurator-org/kurator-ffdq/blob/master/README.md)
- event_date_qc/generation [README](https://github.com/FilteredPush/event_date_qc/blob/master/generation/README.md)
- sci_name_qc/generation [README](https://github.com/FilteredPush/sci_name_qc/blob/master/generation/README.md)
- geo_ref_qc/generation [README](https://github.com/FilteredPush/geo_ref_qc/blob/master/generation/README.md)
- rec_occur_qc/generation [README](https://github.com/FilteredPush/rec_occur_qc/blob/master/generation/README.md)
