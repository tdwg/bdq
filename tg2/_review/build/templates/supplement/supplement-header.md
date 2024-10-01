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

Contributors
: {contributors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

{comment}


### Table of Contents ###

{toc}


## 1. Introduction

This document contains information that is considered supplemental to the normative and non-normative BDQ Core documentation. 

### 1.1 Audience

Supplemental information is included for anyone seeking further historical context or technical details of components of the BDQ Core standard. This information may be relevant for curators, aggregators, data publishers, data analysts, programmers/developers and other practitioners that wish to evaluate and/or improve the quality of the biodiversity data of interest to their domain. 

This document provides practical information to those who wish to implement BDQ Core. It also provides some guidelines based on the knowledge of the authors, for those who may maintain BDQ Core.

### 1.2. Status of the content of this document

This document is non-normative.

### 1.3 RFC 2119 keywords

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## 1.4 Namespace abbreviations

The following namespace abbreviations are used in this document:

| **Prefix**   | **Namespace**                                    |
|--------------|--------------------------------------------------|
| bdq          | https://rs.tdwg.org/bdq/terms/                   |
| bdqcore      | https://rs.tdwg.org/bdqcore/terms                |
| bdqcrit      | https://rs.tdwg.org/bdqcrit/terms                |
| bdqdim       | https://rs.tdwg.org/bdqdim/terms                 |
| bdqenh       | https://rs.tdwg.org/bdqenh/terms                 |
| bdqffdq      | https://rs.tdwg.org/bdqffdq/terms                |
| dc           | https://purl.org/dc/elements/1.1/                |
| dcterms      | https://purl.org/dc/elements/1.1/                |
| dwc          | http://rs.tdwg.org/dwc/terms/                    |
| dwciri       | http://rs.tdwg.org/dwc/iri/                      |
| oa           | https://www.w3.org/TR/annotation-vocab/          |
| owl          | http://www.w3.org/2002/07/owl#                   |

## 2.0 Historical Context

An internationally agreed standard suite of core tests and resulting assertions can be used by all data providers, data collectors and data users to improve the quality of the data. This will allow for more appropriate and more accurate use of biodiversity data. Other than data availability, ‘Data Quality’ is probably the most significant issue for users of biodiversity data and this is especially so for the research community. The tests will not correct all issues that exist with the data, but reports from the tests will identify issues that need to be addressed by users of the data. This may require the user to make decisions on the data - i.e., data that may need to be excluded, data that may need examining for possible improvement, and data that can be used as is. It is always the purview of the user to decide what data is of suitable quality for their use.

### 2.1 Definition of CORE

**Rewrite to cover initial product of TG3 shaping what became Temporal-Spatial use case, then expansion to other use cases**

'CORE' in the context of this standard implies that the tests are informative, simple to implement, are mandatory for enhancements/amendments, have ‘power’ in that they will not likely result in 0% or 100% of all records failing or passing, are widely applicable across sub-disciplines within the biodiversity domain, may elevate the significance of an issue (e.g., no value for dcterms:license) or they may be 'aspirational' in the sense of encouraging priority developments in the biodiversity informatics domain (e.g., testing for any annotations against a record). 

The scope of CORE was also developed from the user needs analysis of BDQ Task Group 3, (Data Quality Use Cases: Rees & Nicholls 2020). The CORE tests largely cover data quality with regards to what organism has occurred where, at what place and time, and a subset of Darwin Core terms that we considered to be critical metadata about occurrence records.

A number of tests were framed, but considered out of scope for CORE data quality needs ('Supplementary' GitHub tag). Implementers are free to implement a subset of the CORE tests or add additional tests when there is a particular data quality needs within their domain. For example, the testing for a value of sub-genus against a taxonomic name authority or testing for a valid depth against maximum depth around the location of an observation. Over the period of this project, many tests were removed from CORE on the basis that they could not be currently implemented in a manner that would result in predictable results. For example, the test VALIDATION_GEOGRAPHY_CONSISTENT was rejected late in the project because of the complexities in matching terms in the geographic names hierarchy, which is less standardized than the taxonomic names hierarchy.

### 2.2 Use case development

A Task Group, the Biodiversity Data Quality Task Group 3: Data Quality Use Cases (Rees & Nicholls 2020), was established early to look at what use cases were in use. From the use cases in use, they identified several fundamental use case, including "bdq:Spatial-Temporal Patterns", "bdq:Record-Management", and "bdq:Taxon-Management". We later added "bdq:Alien-Species" and "bdq:Biotic-Relationships".

These are only a sample of the many possible use cases used in the biological sciences, but they provide an initial set to which all the tests have been linked.

### 2.3 Data Quality Control and Data Quality Assurance

The framework (bdqffdq:) draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.

The specification of the tests within the Framework allows the same set of tests to apply to both Data Quality Control (correcting errors) and Data Quality Assurance (filtering out problematic records to limit data to that with quality for meeting a particular need). The design of the Validations and Measures are intended to be agnostic as to whether their use is for Data Quality Control (finding problematic data), or Data Quality Assurance (filtering out NOT_COMPLIANT records).

### 2.4 Framework Competency Questions

The development of the representation of the Fittness for Use Framework as an owl ontology (bdqffdq:) was influenced by competency questions, shaped by the late Robert A. Morris, and originally written by David Lowery (within in the kurator-ffdq codebase).  The development of the test descriptors led to changes in the ontology (largely adopting a consistent naming pattern).  Changes to the specifics of competency questions follow on that.  

Example comptency questions that can be asked of the RDF representation of bdqcore: 

    # Given a use case find validation tests and their specifications

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

And another that lists the valuable information elements for a use case: 

    # Given a use case find the ActedUpon
    # information elements 
    
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

Summary of the distribution of tests by Data Quality Dimension and specific Darwin Core Terms in InformationElements ActedUpon: 

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

Summary of the distribution of tests by test Type and specific Darwin Core Terms in InformationElements ActedUpon: 

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

## 3 Developing the Tests

Originally, TDWG Data Quality Task Group 2 was tasked with finding a fundamental suite of tests and identifying any relevant software asociated with testing for 'Data Quality'/'Fitness for Use'. It was quickly realized that any software was likely to be far less stable than defining a core suite of tests, so the software component was dropped.

Finding out what tests were being used by a range of aggregators was the first step in identifying candidate tests. We aggregated all 152 unique tests from GBIF, ALA, iDigBio, CRIA, BISON and elsewhere. We then identified a common set of Descriptors of these tests. Descriptors at this time included Information Elements (ref), Specification (Technical Description), Darwin Core Class, Source and References. We peformed a full evaluation of each candidate test using six critera. Tests had to be informative in being able to evaluate or enhance the quality of a data record. Tests had to be relatively simple/straight forward to implement with existing tools. Tests were mandatory for any potential enhancements to record values in that a VALIDATION was required before any AMENDMENT. Tests required power in that they will not likely result in 0% or 100% of all record hits. The suite of tests were designed to provide an adequate coverage of basic information dimensions of Darwin Core: dwc:Taxon; dwc:Event and dcterms:Location, and a category that we called "Other" to cover tests on dwc terms such as dc:license (see Section 3.1). Tests also had to be widely applicable across a range of use cases. Tests that were identified as useful in a limited context were documented  as core tests but tagged as "Supplementary" in that they could be implemented by a community of usage.

We originally documeted the tests in the form of flagging a **FAIL**, for example dwc:eventDate did not conform to ISO 8601-1 date. Our reasoning was this strategy aligned with all of the sources of the tests in that we all sought to identify **issues** with values in the record that would reduce the quality. However, the Data Quality Framework (Veiga et al. 2017) worked in the opposite direction: Identifying values in a record that **PASSED** a test. To align with the Framework, we renamed all tests from FAIL to PASS type, for example, COUNTRYCODE_NOTSTANDARD became COUNTRYCODE_STANDARD. This reversal of 'fail' to 'pass' was also reflected in the comparison of the Framework's 'Data Quality Dimension' versus our early concept of 'Warning Type' (see Section 3.2).

Second and subsequent evaluations of the candidate core tests reduced the number to about 100 that seemed to fulfil the criteria above. The Tests came and went as we provided more consistent and compehensive documentation against what we now called the Descriptors. The tests also changed as we began to implement them. We modified a Test Specification to then find that we would not be able to implement it due to potential ambiguous responses from the test or that a test response may be misleading. By far the greatest changes to the candidate tests came about when we implemented them and ran them against the Test Data (ref).

At one point, we aligned the documetation for over sixty tests that were tagged as Supplementary, Immature/Incomplete and DO NOT IMPLEMENT. In doing so, we realized that the consistent documentation now provided a more nuanced evaluation and subsequently moved a number of these tests back into the core set. The opposite was also true: The implementation of the tests clearly demonstrated that some tests were moved out of the core test suite. Where there were recognized nuances with the tests that may not be obvious from the Specification, we documented the issues in the Notes descriptor.

The team identified a fundamental problem early in the development of the tests: Darwin Core lacked a comprehensive suite of controlled vocabularies. Testing for 'quality' or 'fitness for use' was made difficult at best and impossible at worst, when controlled vocabularies were unavailable. We recognized the key issue of openness of the Darwin Core standard, yet the need for controlled vocabularies to evaluate and improve the 'quality' of Darwin Core encoded data was also important. This conclusion effectively initiated Data Quality Task Group 4: Vocabularies Gro(https://www.tdwg.org/community/bdq/tg-4/) to start to provide a framework for how these vocabularies could be developed for a priority set of Darwin Core Terms. This in turn has resulted in GBIF initiating https://github.com/gbif/vocabulary and https://docs.google.com/viewer?url=https%3A%2F%2Fdev.gbif.org%2Fissues%2Fbrowse%2FGBIF-121%2Fgbif-vocabularies-review_v01.docx.

Over the course of the development of the tests, we encountered significant difficulties with choices of words.  In the original formulation of the framework (Viega 2016 - Thesis), different words were used to describe parallel concepts at the levels of data quality needs, solutions, and reports, and the words used for fundamental concepts overlapped with those for derived concepts.  We have settled on Dimension, Criterion, and Enhancement as the words for fundamental concepts, and variations on Validation (Validation, ValidationMethod, ValidationAssertion), Measure, Amendment, and Issue for derived concepts.  It was very late in development of the test specifications that we realised that the heart of what we were terming Validation mapped to the derived concept of CriterionInContext/ContextualizedCriterion in the framework, so we have renamed framework concepts for clarity.

### 3.1 Tests and Data Dimensions

We identified four categories of information elements of biodiversity-related data that we needed to cover with the tests: Name (taxonomic information); space (geographic location); time (temporal terms) and other (all other terms such as dwc:basisOfRecord).  A record without a taxonomic name, a location or a date has limited value for many research uses (but may be fit for use for others).

Three tests in this standard specifically target records with no name information, no spatial information or no temporal information.

### 3.2 Data Quality Dimension and 'Warning Types'

A "Warning Type" for each test was originally envisioned to provide insight into the nature of the issues associated the negative results of tests. Initially, we had a concept of 'severity' where a failed test could be considered either a "Warning" or an "Error". We subsequently elaborated the warnings into "Warning Types" that had a value of "Ambiguous", "Amended", "Incomplete", "Inconsistent", "Invalid", "Issue", "Report" or "Unlikely". In 2023, a cross tabulation of 'Data Quality Dimension' from the Framework (Veiga et al. 2017) against 'Warning Type' demonstrated that they were highly correlated (see table below). Subsequently, 'Warning Type' was removed as a test Descriptor.

| Data Quality Dimension/Warning Type | Ambiguous | Amended | Incomplete | Inconsistent | Invalid | Issue | Report | Unlikely | Total |
|-------------------------------------|-----------|---------|------------|--------------|---------|-------|--------|----------|-------|
| Completeness                        |           |   11    |    22      |              |         |   1   |    5   |          |  39   |
| Conformance                         |     2     |   17    |            |              |    40   |       |        |          |  59   |
| Consistency                         |           |    1    |            |       7      |         |       |        |          |   8   |
| Likeliness                          |           |         |            |              |         |       |        |     2    |   2   |
| Reliability                         |           |         |            |              |         |   1   |    2   |          |   3   |
| Resolution                          |           |         |            |              |         |   1   |    1   |          |   2   |
| Total                               |     2     |   28    |    22      |       7      |    40   |   3   |    8   |     2    | 113   |

Caption: Data Quality Dimension vs Warning Type (as of 2023) with the number of tests as cell values. 

The following sparql query to count tests by type and data quality dimension: 
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

Gives the following distribution of test types by Dimension:

| Data Quality Dimension | Validation | Amendment | Issue | Measure | 
| ---------------------- | ---------- | --------- | ----- | ------- | 
| Conformance   | 41 | 17 | 1 |   | 
| Consistency   | 7  | 1  |   |   | 
| Completeness  | 22 | 11 | 1 | 1 | 
| Likeliness    | 2  |    |   |   | 
| Resolution    |    |    | 1 | 1 | 
| Reliability    |    |    |   | 2 | 

### 3.2 Types of Test

The types of test in bdqcore are identified by the bdqffdq classes of Validation, Issue, Amendment and Measure. 

**Validation** tests are phrased as positive statements, consistent with the Framework.  Validations evaluate values or in some cases, presence or lack of a value to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT. The formal response of VALIDATIONs can take one of four forms. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable (bdq:sourceAuthority), a Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run, a Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation, a Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 

During the development of the tests, there were significant discussions about how tests were to be phrased, for several contributors, the most natural form seemed to be to describe assertions in the negative sense, identifying problems.  The bdqffdq framework, however, focused entirely on positive statements, identifying data that have quality and are fit for purpose.  Over the evolution of the description of the tests we conformed the language to the positive sense of the framework in almost all cases.  Validations are thus phrased in the framework sense of being COMPLIANT if the data have quality with respect to the test evaluation criteria.  There were, however, a set of cases that didn't fit well into this positive sense, in particular, those where the conclusion of the test was that the data might or might not be fit for purpose and a human would have to evaluate more closely.  In order to accomodate this "there might be a problem" case, we expanded the framework to include the concept of bdqffdq:Issue, where Issues are the converse of Validations and are phrased in a negative sense, identifying problems. 

**Issues** are a form of warning flag where the test is drawing attention to potential problem with the value of a Darwin Core term for at least one use case. Issues can result in a Response.status of "RUN_HAS_RESULT" accompanied by a Response.result of IS_ISSUE, "POTENTIAL_ISSUE" or "NOT_ISSUE".  ISSUE is the equivalent to NOT_COMPLIANT from a Validation.  NOT_ISSUE is similar to COMPLIANT from a Validation, but with slightly different semantics, COMPLIANT means that the data is fit for some use, NOT_ISSUE means that no reason was found for the data not to be fit for use.  POTENTIAL_ISSUE is the reason we incorporated Issues into bdqffdq.   POTENTIAL_ISSUE means that the Issue found a concern in the data that might make it unfit for some use, but that human evaluation of the details of the data and the use are needed.  Data flagged with potential issues require a human review.  For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POTENTIAL_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.

**Amendments** may propose a change to an existing Darwin Core value or fill in a missing value. Amendments are intended to improve one or more components of the quality of the record.  The Response.result from an Amendment is a proposal for a change, not to be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses may choose to (blindly - not recommended, or after analysis) accept all proposed amendments as part of a pipeline in preparing data for an analysis. We urge that Amendments not overwrite existing information within a database but to preserve the old information as well as the new.

The Framework also supports Amendments where the Response.result is a proposal to changes in procedures, such as suggesting that a constraint should be placed on a database field to restrict allowed values, or that a mapping of a data set onto Darwin Core terms has transposed a set of fields, or some other process related change.   We have not framed any such tests in this form, nor have we considered how such assertions should be represented in a Response.result. 

**Placeholder for link to annotations as related to AMENDMENTS?**

 **Measures** may apply to a single record (bdqffdq:SingleRecord), or can be accumulated across multiple records (bdqffdq:MultiRecords). A Measure returns a numeric value of COMPLETE or NOT_COMPLETE as the Response.result. Most SingleRecord Measures defined here count the number of Validation or Amendment tests with a specifified Response.Result in a SingleRecord.  
 
SingleRecord MEASUREs within bdqcore: are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.  Of these, MEASURE_EVENTDATE_DURATIONINSECONDS is intended to provide an estimator for the duration of an event date that can be used as a criterion for Quality Assurance for some use cases, for example, a phenology use may need temporal resolution of records to within about a day, while a use involving long term patterns of spatial change may be satisfied by temoral resolution of about a year or better.  Rather than providing specific measures for each possible duration, we chose to provide just this one generic measure that could be used as a filter criterion for any Use Case.  The other SingleRecord measures in bdqcore take the Responses from other tests as their input and are intended for Quality Control uses to group records by number of data quality concerns present.   

All tests could be accumulated across multiple records (bdqffdq:MultiRecords). For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not.  Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes.  Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.  

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. 

**Placeholder to add information on MultiRecord Measure Count Tests**

### 3.3 Domain Scope of Tests

The domain scope of each test is also largely provided by the bdqffdq:DataQualityNeed. The Darwin Core terms evaluated by each test are expressed as specific bdqffdq:InformationElements. The bdqffdq:Specification provides details of how to evaluate values of the information elements, but also includes references to external (to the Darwin Core standard) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource (e.g. API) required for the implementation of the test.

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not to impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests on data records in parallel, on data records in sequence, as queries on data sets, or on unique values.

### 3.4 Parameterising the tests

Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. The existence of national requirements for spatial data to be represented with a particular datum lead us to identify a requirement for tests to be adjusted to the needs of particular communities. When we identified that within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values.  This allows us to define general tests that provide support for non functional requirements that vary within the community. 

An example is AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT, which takes a Parameter bdq:defaultGeodeticDatum, with a default value that fills most users’ needs of “EPSG:4326”, but recognizes that some users may have requirements that for data to have quality, they must associate dwc:decimalLatitude and dwc:decimalLongitude with a different spatial reference system in dwc:geodeticDatum. Other tests related to georeferences are similarly parameterized, with a similar default, understanding that most CORE users will be working with EPSG:4326, but others will have requirements for a different spatial reference system. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests.   Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority parameter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT. 

Parameters, within bdqffdq: have been modeled as falling within the realm of data quality solutions, they are not attributes of the data, nor are they attributes of data quality needs.

Since value supplied for a parameter for the test is an attribute of the Mechanism (of the system assessing the data quality), the specification of a test cannot evaluate the validity of parameter values as part of the test logic.   Consequences from problems with the validity of values of parameters (e.g. an incorrect IRI for a source authority API endpoint) may only result in Response.status=EXTERNAL_PREREQUISITES_NOT_MET values, as parameters are assertions about externalities to the data and will change if the same data are run on the same test with a different configuration.

Parameters are not intended to relax the definition of data having quality for Core needs. The specifications deliberately do not include parameters that would relax tests on secondary terms for downstream research users or tighten them for upstream data capture. Some tests which would serve the needs of users engaged in data capture or preparing data for aggregation, but not of downstream aggregators or research users were considered, but deemed non-Core and are not specified here. We have similarly resisted the temptation to parameterize tests to meet the needs of different portions of the data life cycle.

### 3.5 Independence and Paired tests

To the best of our abilities, we have designed each test to stand alone.  This is by design to support the mixing and matching of these and other tests to meet particular data quality needs, and not impose any particular model of test execution on implementation frameworks.  The specification of interdependencies among tests would impose constraints upon test execution frameworks.  Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values.  For a subset of amendments, we do provide guidance on execution order to produce deterministic results.

Tests in bdqcore: are paired in that Amendments have a corresponding Validation that assesses the same aspect of data quality. An Amendment may be able to improve the quality of data with respect to that Validation. The bdqffdq: framework contains terms for expressing such formal relationships among tests, we have chosen not to specify these to allow users to more flexibly mix and match tests to their own data quality needs.  

We have also defined MultiRecord Measures that take the Response objects from other tests as their input information elements, for example, to to return a count of Response.value of COMPLIANT for a Validation across a data set, and thus provide a measure of how fit a data set is for some purpose.  Other than specifying the InformationElements, we do not provide another formal description of how pairs of such tests are related.   

### 3.6 Considerations for use of MultiRecord Measures

MultiRecord tests examine data across multiple records, a data set. The BDQ Core MultiRecord Measures all take the output of other tests as their input rather than data.  The inputs, that is the InformationElements, for these Measures in bdqcore: are the outputs of SingleRecord Validations.  

One subset of these measures simply counts the Responses from a given Validation that have Response.result of COMPLIANT.  For QualityControl, these numbers identify where work is needed to make more of a data set fit for use for a given UseCase.  These MultiRecord Measures that return counts can be run before an amendment step in a data processing pipeline, and run again after applying all of the proposed changes to the data from the Amendments to the data set.  A comparison of these pre-amendment and post-amendment phases will identify how much accepting all of the proposed changes from the amendments will improve the quality of the data for a given UseCase.

The other subset of these measures are intended for QualityAssurance.  These QA measures return a Response.result of COMPLETE if all of a given Validation on SingleRecords in a MultiRecord have a response that indicates that the data are fit for use.  A MultiRecord is fit for use for a given UseCase if each of the MultiRecord QA Measures on that MultiRecord returns COMPLETE.  If this is not the case, SingleRecords where the Validations are other than COMPLIANT are filtered out until all of the MultiRecord QA measures return COMPLETE.  The MultiRecord QA measures are the formal means the Fitness for Use Framework provides for ensuring that a data set is fit for use for a given UseCase.  

Some Validations return Response.status=INTERNAL_PREREQUISITES_NOT_MET when one or more of the input InformationElements contain empty values.  For some UseCases, empty values in some fields make the data not fit for use (these are usually tested directly for with VALIDATION...NOTEMPTY tests), however, some Validations operate on sparse data or other cases where the data is fit for use even without values, but when values are present, they must comply with some restriction.  For example, dwc:minimumDepth and dwc:maximumDepth are not expected to be populated for terrestrial data, but are expected to be within range when values are supplied (for freshwater and marine data).  A subset of the MultiRecord QA Measures accomodate such cases by returning Response.result=COMPLETE for validations that are either Response.result=COMPLIANT or Response.status=INTERNAL_PREREQUISITES_NOT_MET.  Thus they can measure that all of the SingleRecords in a MultiRecord either have, for example, no value in dwc:minimumDepth or have an in-range value for dwc:minimumDepth.   

It is possible, but less flexible, to frame Validations to return Result.response=COMPLIANT for either empty values or non-empty values that satisfy other validation criteria.  Concerns are better separated, and individual tests are better composed to fit particular user needs, by having the Validations treat empty data as INTERNAL_PREREQUISITES_NOT_MET, and then framing MultiRecord QA Measures as appropriate for a given UseCase.

MultiRecord measures can also operate directly on the data, for example, a MultiRecord Measure could be framed to measure the average number of individuals reported in dwc:individualCount in a data set.

### 3.7 Input Data Values for AMENDMENTS

One of the early conclusions to this project was the need for controlled vocabularies and an early spin-off of Data Qality Task Group 4 on Vocabularies (https://github.com/tdwg/bdq/tree/master/tg4). Testing the 'quality' or 'fitness for use' of Darwin Core encoded data is made more difficult due to the lack of a comprehensive suite of controlled vocabularies.

Testing Darwin Core values against a known Source Authority using a VALIDATION type test is straight forward: A test is either COMPLIANT or NOT COMPLIANT. This standard includes tests of type AMENDMENT and the mapping of input Darwin Core values to known Vocabulary values is poorly developed. If a VALIDATION returns COMPLIANT, no AMENDMENT is necessary. For example, if the input value to a test is say dwc:sex="Female", then no AMENDMENT is required. If however, the input value is dwc:sex:f., can this be interpreted as "Female"? Probably. What about dwc:sex="M"? This could be "Male" or "Mixed" according to https://api.gbif.org/v1/vocabularies/Sex/concepts. <!--- Ming: I asked GBIF about this specific example and they said that "M" will be matched to Male, but I am not sure how the API works exactly ---><!--- PJM: the rec_occur_qc implementation uses the vocabulary directly, finds, ^M matches male and mixed, so asserts that it can't make the amendment, I can't speak about the (by our test specification, incorrect) actions that gbif is taking on their vocabulary, their API delivers the vocabulary, but doesn't do this sort of matching, so what they are describing is some internal that uses the vocabulary --->

A key phrase within this standard that particularly relates to many of the Expected Responses of tests is " dwc:term can be unambiguously interpreted as ...". In the case above for dwc:sex="M", the determination is that it is ambiguous. In this case, no AMENDMENT can be made.

When carrying out Amendments where numeric vales are concerned (e.g. feet to meters, etc.) the principle of reversability is paramount, and thus rounding up or down or using approximations should be avoided and only exact values used.

We see an urgent need for a comprehensive, internationally agreed list of Darwin Core (https://dwc.tdwg.org/) term values that are mapped to standard values. GBIF has implemented some unique values, for example https://api.gbif.org/v1/vocabularies/Sex/concepts/Female/hiddenLabels, but such lists are not comprehensive. While there has been a survey of Darwin Core 'distinct' values for GBIF, ALA, iDigBio and VertNet, these are both dated, and where possible, have not been mapped to standard values, if they exist.

In this standard, we have taken an expedient approach in relation to making AMENDMENTs. We have used code in our tests to try and parse out likely, unambiguous matches. This is far from an ideal solution, but it does provide the potential of our AMENDMENTs to 'value add' to Darwin Core data records.

### 3.8 Amendments and Annotations

This is from @chicoreus last comment on https://github.com/tdwg/bdq/issues/113 and is placed here for completeness and discussion.

"An approach to this is to assert that Amendments only propose changes, and then it becomes the responsibility of the consumer of the data quality report under Quality Control to assert when changes are made into a database of record, the Response.comment from the Amendment is available for them to add to the modified record when they accept the amendment.

This approach is probably broader than appending values into Remarks terms as part of the proposed change, as such metadata in the Response.result would duplicate the metadata found in the Response.comment, but only in a small number of cases where Remarks terms are available, and raising the concerns of order of actions noted above.

Thus most consistent path is to allow consumers of data quality reports to extract the metadata about the reasoning for a change from the Response.comment in an amendment, and add that as desired to their representation of the data".

This is from https://github.com/tdwg/bdq/issues/149 last comment by @ymgan as it seems related and, as noted, needs some text...

"Thanks @ArthurChapman ! I think it could helpful to be documented somewhere. We got the same question in the OBIS community and it was also asked during the panel session in TDWG conference last year.

I did got confuse a little whether this is something that the TDWG Annotations IG is working on and whether there is something concrete that people can already do. I remember @chicoreus mentioned about the use of W3C annotation data model about this."

### 3.9 Aspirational Aspects of some Tests

Darwin Core is deliberately permissive, and the BDQ Core tests impose additional expectations on data expressed in Darwin Core terms in the interest of data quality.  Some tests assert that data must be in the form described in the normative definition of a Darwin Core term (for example, tests of dwc:day that evaluate compliance with "The integer day of the month" from the definition).  Some tests evaluate compliance with expectations imposed by non-normative notes/comments or examples in Darwin Core (often working from the phrase in comments "Recommended best practice is to use a controlled vocabulary").  Here we are aspiring to the community to adopt common controlled vocabularies to improve the quality of biodiversity data. 

In some cases, the tests are more aspirational about ways in which the community should express things in order for there to be quality, for example, bringing in an understanding from the geofererencing guide of the set of metadata concepts that need to have values for there to be quality in georeferences, or in pointing at particular controlled vocabularies that the community should aspire to using (such as the EPSG codes).

As noted above, the authors recognized that the flexibility of Darwin Core (on which BDQ Core is based) in relation to vocabularies, is a problem when 'data quality' or 'fitness for use' of Darwin Core records is attempted. Controlled vocabularies seemed a wise aspirational goal and thankfully, the the TDWG Data Quality Task Group 4 Vocabularies Task Group was created (https://github.com/tdwg/bdq/tree/master/tg4) and subsequently, GBIFs vocabulary services supporting Darwin Core and other namespaces (see https://rs.gbif.org/vocabulary/dwc/). We look forward to the uptake of a far more comprehensive suite of controlled vocabularies that will greatly improve the 'quality' of biodiversity-related data and its evaluation.

Similarly, the authors valued the the significance of an annotation standard to BDQ Core and have one test specifically targeting record annoations: ISSUE_ANNOTATION_NOTEMPTY, even though no TDWG standard exists. We do however acknowledge the TDWG Annotations Interest Group (https://github.com/tdwg/annotations) which has identified the W3C Annotation Model (https://www.w3.org/TR/annotation-model/) as the likely way forward.  We understood that the annototation test will be difficult, if not impossible for many to implement, but we considered this issue of such significance, it is included to promote the use of the W3C web annotation data model by the international biodiversity community. We also acknowledge that data aggregators such as the Atlas of Living Australia (https://ala.org.au) have had an operational annotation service for many years (see https://support.ala.org.au/support/solutions/articles/6000262125-flagging-an-issue-with-a-record) but like other implementations, this service is a subset of what is required for a comprehensive service (e.g., annotations on annoations for one).

It was also recognized that a number of BDQ Core tests would assert a 'lack of quality' for records representing events on the high seas/international waters (outside national jurisdictions) where tests will return 'NOT_COMPLIANT' as there is no agreed standard for designating 'high seas' records using Darwin Core (https://dwc.tdwg.org/). Examples of such tests include VALIDATION_COUNTRY_NOTEMPTY and VALIDATION_COUNTRYCODE_NOTEMPTY. The authors recognize the significance of this issue to the marine community, but we have retained these tests to promote an agreement on an international standard. We acknowledge a current user-assigned ISO 3166-alpha-2 country code (dwc:countryCode - https://dwc.tdwg.org/terms/#dwc:countryCode) "XZ" to infer "international waters" (see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#XZ and https://en.wikipedia.org/wiki/UN/LOCODE). While country code "XZ" looks like a much-needed advance, its use has not be standardized. The situation with populating a country value (dwc:country - https://dwc.tdwg.org/terms/#dwc:country) with "high seas" or "international waters" or something else is less advanced, but we have retained the country test, aspirationally. Related tests such as VALIDATION_COUNTRY_FOUND, VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT and VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT don't present as much an issue, due to the Specifications including the phrase "INTERNAL_PREREQUISITES_NOT_MET" if dwc:countryCode or dwc:country are bdq:Empty, as would be currently expected for records in international waters. The Specification says "This test can't be done because a vital piece of information to run this test is absent". While currently acceptable, once a standard for international waters/high seas is established, the tests will need to be revisited.

## 4 Rationale Management Documentation

### 4.1 Developing tests with Github Issues

The bdqcore: tests were developed in issues in the tdwg/bdq github space. The reasoning was that github provided a comprehensive and consistent environment in which to develop, expose, discuss and manage all aspects of the development of BDQ Core. We used a standard template as the first Comment on github Issues pages for documenting all Tests. This immediately exposed all proposed tests to anyone following the work. Github then enabled anyone (with access?) to comment on the Test issues, facilitating discussion. When there was general agreement among the core team, generally by emojis such as 'thumbs up', the values within the template could be easily modified.

Github's API also provided ample latitude to 'scrape' and filter Issues by github tags (see below) to extract any subset of Tests by Descriptors to CSV files that would be used in the submission and proposed maintenance of the BDQ Core standard.

### 4.2 Github Tags and Categorizing Issues

The development of each test, with documentation of why particular decisions were made with regard to that test, has been documented in issues in the tdwg/bdq github repository. Each issue has table in markdown format in its Issue.  Each issue was tagged with the following GitHub issue tags to assist in finding, evaluating, and asserting conclusions about each test. 

The following list of github Tags were used on all Test Issues: 

| tag | definition | comment |
| --- | ---------- | ------- |
| Amendment | A label to indicate a test of type AMENDMENT which may propose a change or addition to at least one Darwin Core term that is intended to improve one or more components of the quality of the record. | See bdqffdq:Amendment |
| CORE | Conclusion that a test belongs in the set of tests for evaluating biodiversity data quality as represented by the values of Darwin Core terms. CORE tests address identified user needs, are widely applicable, informative, unambiguous, well defined, and straight forward to implement. |  |
| DO NOT IMPLEMENT | Conclusion that a test is not recommended to be implemented with the current level of understanding for one or more reasons: Available vocabularies are ambiguous; the test is too complex to implement concisely; implementation is expected to lead to ambiguous or inaccurate results. |  |
| Immature/Incomplete | Conclusion that a test requires substantial work is still needed to develop the specification to the point where the test can be reliably and usefully implemented. This may indicate work that is wholly internal to the test specification such as developing a consistent Expected Response, or may indicate that external work is needed to develop an agreed vocabulary for values of the tested term. An immature/incomplete test may be made CORE, Supplementary, or DO NOT IMPLEMENT when relevant criteria are satisfied. |  |
| ISO/DCMI STANDARD | A reference to either an ISO (International Organization for Standardization) Standard or a DCMI (Dublin Core Metadata Initiative) Standard |  |
| Issue | A label to indicate a test of type ISSUE, where potential problems are flagged and may need examination by the user to determine if data have quality for their use. | see bdqffdq:Issue |
| Measure | A label to indicate a test of type MEASURE that performs a measurement according to some data quality dimension. | See bdqffdq:Measure |
| NAME | A label to indicate that the test is related to Darwin Core terms in the dwc:Taxon Class. |  |
| NEEDS WORK | A label that indicates that an issue (Test) requires more work before finalising. | Supports a workflow of contributors identifying tests needing work with this tag, and review of issues with this tag in task group meetings.  |
| OTHER | A label to indicate that the test is related to Darwin Core terms other than Classes dwc:Taxon, dwc:Location or dwc:Event. |  |
| Parameterized | A label for a test that requires a bdq:Parameter to be set prior to a bdq:parameterizedTest being run. |  |
| SPACE | A label to indicate that the test is related to Darwin Core terms in the dwc:Location Class. |  |
| Supplementary | Conclusion that a test is regarded as not CORE (cf. the tag CORE) because of one or more reasons: Not widely applicable; not clearly matched to an identified data quality need; not informative concerning the 'quality' or lack of quality of the data; likely to return a high percentage of either bdq:NOT_COMPLIANT or bdq:POTENTIAL_ISSUE records. A Supplementary test MAY be implemented in a local implementation if a suitable use case exists. | A Supplementary test may be made CORE at a later time. |
| Test | Tests descriptions created by TG2, either CORE, Immature/Incomplete, Supplementary, or DO NOT IMPLEMENT. | Supports workflows for exporting tests from issues to process the markdown into csv files for review.  |
| TG1 | Issues pertinent to Task Group 1 ([Framework on Data Quality](https://tdwg.github.io/bdq/tg1/site)) of the TDWG Data Quality Interest Group. |  |
| TG2 | Issues including Tests, developed by, or pertinent to Task Group 2 ([Data Quality Tests and Assertions](https://github.com/tdwg/bdq/blob/master/tg2/README.md)) of the TDWG Data Quality Interest Group. |  |
| TG3 | Issues pertinent to Task Group 3 ([Data Quality Use Cases](https://github.com/tdwg/bdq/blob/master/tg3/README.md)) of the TDWG Data Quality Interest Group. |  |
| TG4 | Issues pertinent to Task Group 4 ([Best Practices for Development of Vocabularies of Value](https://github.com/tdwg/bdq/blob/master/tg4/README.md)) of the TDWG Data Quality Interest Group. |  |
| TIME | A label to indicate that the test is related to Darwin Core terms in the dwc:Event Class. |  |
| Validation | A label to indicate a test of type VALIDATION that describes a run of a test for validity against a set of criteria. | See bdqffdq:Validation |
| VOCABULARY | A label to indicate that a Test requires a controlled Vocabulary |  |

The CORE, DO NOT IMPLEMENT, Immature/Incomplete, and Supplementary tags mark conclusions made about each proposed test.

The tag NEEDS WORK was repeatedly added and removed to issues and was a valuable support for the evaluation of tests in repeated feedback loops of: Frame the description of a test, idependently produce validation data and an implementation, run the implementation against the validation data, evaluate cases where the expectations in the validation data differ from the test results (which could be a defect in the implementation, in the validation data, or a problem in the test specification), discuss as a group, make changes as needed, and repeat.

### 4.3 Using Markdown Tables in Github Issues to Develop Test Descriptors

The development of each test, with documentation of why particular decisions were made with regard to that test, has been documented in issues in the tdwg/bdq github repository. Each issue has table in markdown format in its Issue.  The terminology in this markdown table differs slightly from the Framework, so to support understanding of the rationale management the non-standard terminology used there is documented below. The Test Descriptors are a simplified set of the bdqffdq: terms to describe a test. Some descriptors such as the GUID are intended for machine consumption, some such as the "Description" are designed to be human-readable' for consumers of biodiversity data quality reports while descriptors such as the "Specification" ensure that implementers have no ambiguity about how the test should be coded.

**Title** [non-normative]: A standardised, human readable name of the test-assertion based roughly on the template OUTPUTTYPE_TERMS_RESPONSE. There are 15 tests that only loosely conform to this template due to the difficulty of rendering them otherwise, for example "VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION". <!---Note that there are 15 tests that don't strictly follow this - e.g. #132, #108, #93, #88, #86, #73, #71, #68, #62, #57, #56, #52, #50, #32, #24 - Should we mention the exception types here?--->. These names were considered helpful for human-human communication and to assist with code implementation, maintenance and searches. Example: VALIDATION_BASISOFRECORD_STANDARD.  

**GUID** [normative]: A globally unique identifier which allows software to uniquely identify each test (and in combination with parameter values, allows for specification of the expectations for the behaviour of a test implementation). Example: 8f1e6e58-544b-4365-a569-fb781341644e.   The GUID in the markdown table becomes the local part of the IRI for the test (for example https://rs.tdwg.org/bdqcore/terms/8f1e6e58-544b-4365-a569-fb781341644e) when translated to RDF.

**Label** [normative]: A human readable label identifying the test.  The labels largely follow the pattern TYPE_INFORMATIONELEMENT_STATUS.. Example: "VALIDATION_COUNTRYCODE_STANDARD"  The Label becomes the skos:prefLabel when translated to RDF.
 
**Description** [non-normative]: An English language brief description. Example: Does the value of dwc:basisOfRecord occur in bdq:sourceAuthority?  

**Test Type** [non-normative]: Tests have been classified into four Fitness for Use Framework classes; VALIDATION (validates values in one or more Darwin Core terms),  AMENDMENT (an improvement that will result in a change or addition to at least one Darwin Core term); and MEASURE (returns a numeric value, for the tests described here; all values are in the form of the number of tests that conform to a criterion). Three tests are typed as ISSUE (flag a potential problem). Example: POTENTIAL_ISSUE.

**Darwin Core Class** [non-normative]: The Darwin Core class that contains the Information Elements. Example: dwc:Taxon.

**Information Elements Consulted** [normative]: The Darwin Core terms that the test takes as input. Example: dwc:basisOfRecord.

**Information Elements ActedUpon** [normative]: The Darwin Core terms that is the focus of the test. Example: dwc:basisOfRecord.

**Expected Response (Specification)** [normative]: A concise description of the logic of the test to clarify implementation. The Expected Response takes the form (for a VALIDATION) of: EXTERNAL_PREREQUISITES_NOT_MET if <condition>; INTERNAL_PREREQUESITES_NOT_MET if <condition>; COMPLIANT if <condition>; otherwise NOT_COMPLIANT. Example: EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is EMPTY; AMENDED the value of dwc:basisOfRecord if it could be unambiguously interpreted as a value in bdq:sourceAuthority; otherwise NOT_AMENDED.

**Data Quality Dimension** [normative]: A test will focus on one of the following scenarios based on the Data Quality Framework: "Completeness" (the extent to which data elements are present and sufficient); "Conformance" (conforms to a format, syntax, type, range, standard or to the own nature of the information element); "Consistency" (agreement among related information elements in the data); "Likeliness" (low probability that values are real); "Resolution" (is sufficient detail present in the value/s - a measure the granularity of the data). The [data quality dimension](https://github.com/tdwg/bdq/blob/master/tg2/vocabularies/data_quality_dimensions.csv) for this test. Example: "Conformance"

**Term_Actions** [non-normative]: The last two components of the Title, useful in filtering Tests in CSV files. Example: "COUNTRYCODE_STANDARD"

**Parameter(s)** [normative]: Parameters that modify the behaviour of the test, along with default values or links to source authorities. A parameter value exists only where there are a number of alternate options. For example, "bdq:sourceAuthority default = "GBIF Backbone Taxonomy"" is parameterised as it allows for regional taxonomic authorities whereas "bdq:sourceAuthority is "EPSG:" [https://epsg.io]"" is not parameterised as there is a single source authority. Example: bdq:defaultGeodeticDatum.	

**Source Authority** [normative]: A reference to an authority required by the test and a default value. bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}. The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be exTests may require reference to external data such as standard vocabularies of terms or names.   When a test uses more than one sourceAuthority at the same time, these are given separate names, for example,  bdq:taxonIsMarine,bdq:geospatialLand are the two sourceAuthority Parameters for VALIDATION_COORDINATES_TERRESTRIALMARINE. A reference to an external (non-Darwin Core) authority required for the test. bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}. The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be expected to be passed in as the parameter value.  Other non-empty strings would select other source authorities. The structure of the information in Source Authority ideally has two components. The first component refers to the standard itself, which may include a vocabulary of accepted values. The second component will, wherever possible (if available), refer to an API that will assist implementers of the tests. In some cases, the API component will refer to a 'third party' site where it is hoped will remain in sync with the standard, for example, a GBIF vocabulary API site would ideally be synced with a Darwin Core site. Example: "bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}". While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

**Specification Last Updated**: Date of last change to a Normative part of the test, for example to the wording of an Expected Response/Specification. Example 2023-06-23.

**"Examples"** [non-normative]: Example of inputs and the expected output from an implementation of the test given those outputs.  A ’pass’ and a ‘fail’ example are provided for each test.  All examples listed are also present in the the validation data suite. Example: "[dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"]"

**Source** [non-normative]: The origin of the concept of the test. Example: The Atlas of Living Australia.

**"References"** [non-normative]: A list of references that will assist in a thorough understanding of the test. Example: "GBIF Secretariat (2019). GBIF Backbone Taxonomy. Checklist dataset (https://doi.org/10.15468/39omei)"

**Example Implementations (Mechanisms)** [non-normative]: A link to one or more agencies that have an implementation of the test. Example: https://github.com/FilteredPush/event_date_qc.

**Link to Specification Source Code** [non-normative]: A link to code that implements the test. Example: https://github.com/FilteredPush/ event_date_qc/blob/5f2e7b30f8a8076977b2a609e0318068db80599a/src/main/java/org/filteredpush/qc/date/DwCEventDQ.java#L169.

**Notes** [non-normative]: Additional comments that the Task Group believed necessary for an accurate understanding of the test or issues that implementers needed to be aware of. Example: For TAXONID_FROM_TAXON, “This is the taxonID inferred from the Darwin Core Taxon class, not from any other sense of Taxon. Return a result with no value and a Result.status of NOT_AMENDED with a Response.comment of ambiguous if the information provided does not resolve to a unique result (e.g. if homonyms exist and there is insufficient information in the provided data, for example using the lowest ranking taxa in conjunction with dwc:dwc:scientificNameAuthorship, to resolve them).  When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:taxonID.”.

## 5 Date and Time Issues

### 5.1 Events and Calendars

Different calendars have been used at different times in different places, and the transcription of an
original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date, and metadata may or not be present to even identify such records.

Countries and researchers have changed from the Julian calendar to the Gregorian calendar at different times. For example, Russia adopted the Gregorian Calendar on 1918-02-14, the British Empire in 1752-09-14, different regions in France between 1582 and 1760, with France also adopting the French Republican Calendar 1793-1805. The difference between the Gregorian and Julian calendar has typically been around 10 days. But, the day that is considered the first day of the year has also changed at different times in different countries, meaning that the difference can be as great as 1 year and 10 days. Given the complexity, and ongoing nature of transitions between calendars, we do not advocate using VALIDATION_EVENTDATE_INRANGE for quality assurance by selecting a transition date and using it as a threshold.

[John’s statement on calendars as a placeholder (https://github.com/tdwg/bdq/issues/76#issuecomment-1591985055): “I don't think we are in any position to posit a date after which the Gregorian calendar assumption is safe. It is still not safe today, it's just that its use for civil purposes has ever fewer exceptions as time goes on (so far). Making a statement about a particular date (other than the date of its origin) for a date of special mention necessarily has discriminatory implications. We do NOT want that.

In this particular issue, and perhaps in all others where this has come up, I do not see that the uncertainty associated with the date actually has anything to do with what we are testing. This test can't assess if a date is actually within a Gregorian date interval, except in special cases where the Julian and Gregorian calendars coincide, and even that is ignoring all other possible calendars. Instead, it is able to test that a date following the ISO 8601-1 date specification is within a range specified in that context. We can't effectively do anything else because Darwin Core doesn't even provide for stating the original calendar used - it's forcing people to use the Gregorian calendar without describing the responsibility for doing so and the consequences of not doing so. I think the place for awareness of the implications of dates with unknown calendars is in the Darwin Core date terms.]

### 5.2 Time

See: https://xkcd.com/2867/ and  https://www.xkcd.com/1883/

**If time zone is not included as a component of date and time, the date and time information is expected to be consistent throughout the event terms**

This standard avoids analysis of two time and date issues, time zones, and geographic and temporal variation in the change from Julian to Gregorian calendars.  

Time is treated as out of scope for CORE Use Cases.  This means that some cases where time zone data is important, dates within a MultiRecord from multiple sources may have multiple plus or minus one day errors introduced.    

The event_date_qc implementation of AMENDMENT_EVENT_FROM_EVENTDATE contains this commented out block of code, pertinent to time zone issues.   It would popluated eventTime from eventDate, converting a local time in eventDate to UTC, where other blocks in the Amendment should but may not have taken account of a local time zone in populating dwc:day/dwc:month/dwc:year/dwc:startDayOfYear/dwc:endDayOfYear (dwc:day/dwc:month/dwc:year/dwc:startDayOfYear/dwc:endDayOfYear/dec:eventTime should all be consistent, but there aren't unit tests in place to confirm this).

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

In general, assessing whether a date in biodiversity data was Julian or Gregorian is treated here as an intractable problem, and the problem of correctly determining the gregorian value for dwc:eventDates is left in the hands of data providers who may have additional knowledge of collectors and their practices to be able to assess how to interpret verbatim date values found in their historical records.  For consumers, this means that historical dates, even into recent times, may have systematic errors in subsets of the data where the date was julian but has been treated as gregorian.  This can, in some cases, introduce errors on the scale of one year differences between reported and correct eventDate value.     
