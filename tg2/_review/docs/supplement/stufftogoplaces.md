Material from the initial draft of the BDQ Core standard to be moved elsewhere.

Much of this goes in supplementary information or the guides.

Delete from here once moved elsewhere.


## 2 Framework for describing data quality

The specification of the tests within the Framework allows the same set of tests to apply to both Data Quality Control (correcting errors) and Data Quality Assurance (filtering out problematic records to limit data to that with quality for meeting a particular need). The design of the Validations and Measures are intended to be agnostic as to whether their use is for Data Quality Control (finding problematic data), or Data Quality Assurance (filtering out NOT_COMPLIANT records).

### 2.1 Introduction


### 2.2 Data Quality Control, Data Quality Assurance

The framework draws a distinction between Quality Control and Quality Assurance.  Quality Control processes seek to assess the quality of data for some purpose, then identify changes to the data or to processes around the data for improving the quality of the data.  Quality Assurance processes seek to filter some set of data to a subset that is fit for some purpose, that is to assure that data used for some purpose are fit for that purpose.

### 2.3 Data Quality Needs, Data Quality Mechanisms, Data Quality Reports

The framework organizes data quality concepts into three areas: Needs, Mechanisms, and Reports.  Data Quality Needs identify a use to which data may be put, and frame a set of requirements that data needs to meet to be fit for that use, and means by which data not fit for that use may be improved.  The tests described in this standard are formal descriptions of data quality needs for CORE purposes.  Data Quality Mechanisms in the framework are formal descriptions of software and other mechanisms that implement tests described in the Needs area.  Data Quality Reports are the results produced by Mechanisms on some set of data.  The tests described in this standard include specifications of assertions to be made in Data Quality Reports.

The framework has an abstract concept of Information Elements. To frame tests on Darwin Core terms in a usable way, we list specific Darwin Core terms as the information elements in each test.

Formally, in the Data Quality Needs level, the framework starts with a Use Case, a framing of some use to which data may be put.  Use cases are related to the formal description of data quality needs through policies and contexts.  Contexts (ContextualizedCriterion, ContextualizedDimension, ContextualizedEnhancement, ContextualizedIssue) relate the specification of a need, such as a Validation, to the information elements that need to be examined, and to the resource type that is operated on.  Each of the tests described in this standard has a formal specification that includes each of these elements.   A Use Case includes a set of policies, policies relate the use case to contexts, contexts link information elements to needs and to resource types, a need specify what properties data must have to have quality.   

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

	<rdf:Description rdf:about="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/Specification"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code; otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</rdfs:comment>
	</rdf:Description>

	<rdf:Description rdf:about="urn:uuid:54fdf7a8-c1b1-4c21-b0a2-1f5aa86d3461">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ValidationMethod"/>
    	<criterionInContext xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9"/>
	    <hasSpecification xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
	</rdf:Description>

	<rdf:Description rdf:about="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ContextualizedCriterion"/>
    	<hasActedUponInformationElement xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:c8c64b57-6bed-49f0-b273-d6bc95b12916"/>
    	<hasCriterion xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:1f717a19-54b5-4240-a2c8-fff86d237c2e"/>
    	<hasResourceType xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="rt:SingleRecord"/>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</rdfs:comment>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord</rdfs:label>
	</rdf:Description>

The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

## 3 Tests


### 3.3 Tests and Data Dimensions

We identified four fundamental aspects of biodiversity-related data that we needed to cover with the tests: Name (taxonomic information); space (geographic location); time (temporal terms) and other (all other terms such as dwc:basisOfRecord). A record without a taxonomic name, a location or a date has limited value. Three tests in this standard specifically target records with no name, space or time values.

#### 3.4 Types of Test

The concept of 'tests' in this standard include Validation, Issue, Amendment and Measure. Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags. The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary consisting of exactly COMPLIANT or NOT_COMPLIANT for Validations, NOT_ISSUE, POTENTIAL_ISSUE or ISSUE for Issues, either a numeric value or a controlled vocabulary consisting of COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments.

2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 

3. The Remark supplies human-readable text describing reasons for the test result output.

Validation tests are phrased as positive statements, consistent with the Framework.  Validations evaluate values or in some cases, presence or lack of a value to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT. The formal response of VALIDATIONs can take one of four forms. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable (bdq:sourceAuthority), a Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run, a Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation, a Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 

Issues are a form of warning flag where the test is drawing attention to potential problem with the value of a Darwin Core term for at least one use case. Issues are currently outside the Data Quality Fitness for Use Framework. Issues result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "POTENTIAL_ISSUE" or "NOT_ISSUE". Human evaluation of potential issues require a human review. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POSSIBLE_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.  

An Amendment may propose a change to an exisitng Darwin Core value or fill in a missing value. Amendments  is intended to improve one or more components of the quality of the record.  The Response.result from an Amendment MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  The Framework also supports changes to procedures but we have not framed any such tests in this form.  

A Measure returns a numeric value or INTERNAL_PREREQUISITES_NOT_MET. Most Measures count the number of Validation or Amendment tests that a specifified Response.Result. MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. 

[From QRG]

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

[End QRG addition]

All tests could be accumulated across multiple records (bdqffdq:MultiRecords). For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not.  Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes.  Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.    

### 3.5 Test Descriptors

The Test Descriptors are those terms that are necessary to comprehensively describe the test. Some descriptors such as the GUID are intended for machine consumption, some such as the "Description" are designed to be human-readable' for consumers of biodiversity data quality reports while descriptors such as the "Specification" ensure that implementers have no ambiguity about how the test should be coded.

**"GUID"** [normative]:A machine readable unique identifier for the test. Example: "0493bcfb-652e-4d17-815b-b0cce0742fb" 

**"Label"** [normative]: A human readable label identifying the test.  The labels largely follow the pattern TYPE_INFORMATIONELEMENT_STATUS.. Example: "VALIDATION_COUNTRYCODE_STANDARD" 

**"Description"** [non-normative]: A non-technical description of what the test does, intended for consumers of data quality reports in concert with the Response.comment. Example: "Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?"

**"TestType"** [normative]: The Type of assertion that this test produces, Measure, Validation, Amendment, Issue.. Example: "Validation" 

**"Darwin Core Class"** [non-normative]: The Information Element in the original terms of the framework, the general sort of information this test operates on. . Example: "dwc:Location"  

**"Information Elements ActedUpon"** [normative]:A list of the specific Darwin Core terms that are the focus of the test.. Example: "dwc:countryCode" 

**"Information Elements Consulted"** [normative]:"dwc:scientificName" A list of Darwin Core terms that are consulted in the evaluation of the Information Elements ActedUpon.

**"Specification"** [normative]: The specification for implementors describing the expected behavior of the test. Example: EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is EMPTY; COMPLIANT if the value of dwc:phylum was found as a value at the rank of Phylum by the bdq:sourceAuthority; otherwise NOT_COMPLIANT."  

**"Parameters"** [normative]: Any parameters that change the behavior of the test for a subset of users with special data quality needs within the domain.. Example: "bdq:taxonIsMarine" 

**"Dimension"** [normative]: The [data quality dimension](https://github.com/tdwg/bdq/blob/master/tg2/vocabularies/data_quality_dimensions.csv) for this test. Example: "Conformance"

**"Criterion Label"** [non-normative]:  A label for the Criterion (TODO: Criterion/CriteronInContext applies to Validations, need to clarify for Dimension/DimensionInContext, Enhancement/EnhancementInContext, Issue/IssueInContext). Example: "Conformance: standard"

**"Resource Type"** [normative]: The type of resource on which this test acts, SingleRecord or MultiRecord, the CORE tests include Validations, Measures, and Amendments that operate on SingleRecords and a set of MultiRecord Measures that assess the results of the SingleRecord Validations. Example: "SingleRecord"   

**"Source Authority"** [normative]: A reference to an external (non-Darwin Core) authority required for the test. bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}. The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be exTests may require reference to external data such as standard vocabularies of terms or names. While applying to a single record, the test results may be accumulated across multiple records (bdqffdq:MultiRecord), for example reporting that 75% of the records do not have a valid value for dwc:basisOfRecord. Only a subset of the values of all Darwin Core terms are referenced in the core tests. Each test focuses on a single aspect of data quality, usually a single dimension of a single Darwin Core term or small set of related input Darwin Core terms; the Information Elements which form the input data to the tests.

A reference to an external (non-Darwin Core) authority required for the test. bdq:sourceAuthority="Normative String Identifier" {"normative resource"} {informative list of api endponts or other resources}. The "Normative String Identifer" is critical when the bdq:sourceAuthority is a parameter, this would be the string that would be expected to be passed in as the parameter value.  Other non-empty strings would select other source authorities. The structure of the information in Source Authority ideally has two components. The first component refers to the standard itself, which may include a vocabulary of accepted values. The second component will, wherever possible (if available), refer to an API that will assist implementers of the tests. In some cases, the API component will refer to a 'third party' site where it is hoped will remain in sync with the standard, for example, a GBIF vocabulary API site would ideally be synced with a Darwin Core site. Example: "bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}"



**"Examples"** [non-normative]: Example of inputs for a test and the expected output from an implementation of the test given those outputs.  A ’pass’ and a ‘fail’ example are provided for each test.  All examples listed are also present in the the validation data suite. Example: "[dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"]"

**"References"** [non-normative]: A list of references that will assist in a thorough understanding of the test. Example: "GBIF Secretariat (2019). GBIF Backbone Taxonomy. Checklist dataset (https://doi.org/10.15468/39omei)"

**"Example Implementations (Mechanisms)"** [non-normative]: nown Mechanisms with implementations of the test.
. Example: "FilteredPush/Kurator: geo_ref_qc"

**"Link to Specification Source Code"** [non-normative]: A link to code that implements the test. Example: https://github.com/FilteredPush/

**"Notes"** [non-normative]: Additional, guidance that may be necessary for the accurate implementation of the tests. Example: "Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This test will fail if there is leading or trailing whitespace or there are leading or trailing non-printing characters."  

### 3.6 Domain Scope of Tests

The domain scope of each test is also largely provided by the bdqffdq:Specification. The Darwin Core terms used in the Specification are included in the "Information Elements". The "Specification" also includes references to external (to the Darwin Core standard) authorities that are required to implement the test, for example, references to an ISO standard. Such authoritative references are listed under "Source Authority" with a link to the authority and optionally, a link to a specific online resource required for the implementation of the test.

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values.  This allows us to define general tests that provide support for non functional requirements that vary within the community.  For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite.  Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests.   Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values.

[Text from QRG start]

#### Parameterising the tests

When we identified that, within Core data quality needs, different portions of the community have different authorities that they are required to adopt for particular terms, we define Parameters for tests, where the Parameter values allow a particular test to behave differently when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs. This allows us to define general tests that provide support for non functional requirements that vary within the community. 

For example, for spatial biodiversity data to have quality for use within some countries, there exist country specific requirement for which geodetic datum is to be used.  A test for fitness for use of biodiversity data for core needs that only allowed the use of EPSG:4326 as the sole COMPLIANT value for dwc:geodeticDatum would not meet the non functional requirements for use in some countries, and thus would not meet the Core purposes for this test suite. Thus, in cases where portions of the community do have clear distinct needs for quality within Core, we provided for the parameterization of tests. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Where there are options available for a resource that supports the test, the test will be designated as "Parameterized" and a default provided, along with a link to an authority if relevant. For example, the "GBIF taxonomic backbone" is suggested as a default for most of the tests related to taxonomic names, but the standard recognizes that other Source Authorities may be required in other circumstances, for example, The World Register of Marine Organisms or a national taxonomic authority.  When a test has a single source authority paramter, bdq:sourceAuthority is used for that parameter, but if a test takes more than one source authority parameter, these are given distinct names, for example, bdq:taxonIsMarine and bdq:geospatialLand are two source authority parameters for the test VALIDATION_COORDINATES_TERRESTRIALMARINE. 

Tests are paired in that all AMENDMENTs require a corresponding VALIDATION that assesses some aspect of data quality. An AMENDMENT may be able to improve the quality of data with respect to that VALIDATION. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values. 

Example: Formal description of 0493bcfb-652e-4d17-815b-b0cce0742fbe VALIDATION_COUNTRYCODE_STANDARD

	<rdf:Description rdf:about="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/Specification"/>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">VALIDATION_COUNTRYCODE_STANDARD</rdfs:label>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">EXTERNAL_PREREQUISITES_NOT_MET if bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code; otherwise NOT_COMPLIANT bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}</rdfs:comment>
	</rdf:Description>

	<rdf:Description rdf:about="urn:uuid:54fdf7a8-c1b1-4c21-b0a2-1f5aa86d3461">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ValidationMethod"/>
    	<criterionInContext xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9"/>
	    <hasSpecification xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:0493bcfb-652e-4d17-815b-b0cce0742fbe"/>
	</rdf:Description>

	<rdf:Description rdf:about="urn:uuid:ad10c2e7-ab24-432f-8b09-c2c73674cce9">
    	<rdf:type rdf:resource="http://rs.tdwg.org/bdq/ffdq/ContextualizedCriterion"/>
    	<hasActedUponInformationElement xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:c8c64b57-6bed-49f0-b273-d6bc95b12916"/>
    	<hasCriterion xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="urn:uuid:1f717a19-54b5-4240-a2c8-fff86d237c2e"/>
    	<hasResourceType xmlns="http://rs.tdwg.org/bdq/ffdq/" rdf:resource="rt:SingleRecord"/>
    	<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?</rdfs:comment>
    	<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code? Validation for SingleRecord</rdfs:label>
	</rdf:Description>

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, repeated in 5.2.3 --->
The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

[End of QRG Text entry]

### 3.7 Test Parameters

Some tests have been defined as parameterized. A parameterized test will behave differently on the same data when given different parameter values. Parameterized tests are those for which we saw the high likelihood of different data quality needs within the community of CORE users and CORE needs.

The existence of national requirements for spatial data to be represented with a particular datum lead us to identify a requirement that some tests be able to be adjusted to the needs of particular communities. An example is AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT, which takes a Parameter bdq:defaultGeodeticDatum, with a default value that fills most users’ needs of “EPSG:4326”, but recognizes that some users may have requirements that for data to have quality, they must associate dwc:decimalLatitude and dwc:decimalLongitude with a different spatial reference system in dwc:geodeticDatum. Other tests related to georeferences are similarly parameterized, with a similar default, understanding that most CORE users will be working with EPSG:4326, but others will have requirements for a different spatial reference system. Similarly, parameters are specified for depth and elevation information based on global maximum values, while users who’s data falls entirely within some smaller geographic region may be able to impose tighter constraints on depth and elevation for their data to have quality, for example for quality control to identify records needing evaluation where the specified elevation is larger than any elevation within the region.

Parameters are not intended to relax the definition of data having quality for CORE needs. The specifications deliberately do not include parameters that would relax tests on secondary terms for downstream research users or tighten them for upstream data capture. Some tests which would serve the needs of users engaged in data capture or preparing data for aggregation, but not of downstream aggregators or research users were considered, but deemed non-CORE and are not specified here. We have similarly resisted the temptation to parameterize tests to meet the needs of different portions of the data life cycle.

### 3.8 Workflows and Sequencing of Tests

<!--- Ming: What the tests are agnostic of, repeated in 1.6, 5.2.3 --->
The test descriptions are agnostic to the framework within which the tests are run. The tests are largely agnostic to the extent to which they are run in parallel and the sequence in which particular tests are run. An exception is certain of the amendments, where the order of execution can be important.

<!--- Ming: Execution sequence of the tests , repeated in 1.6, but more detail than 1.6 --->

A good practice for executing the tests is to execute all of the validations and measures in a pre-amendment phase, then to execute all of the amendments in an amendment phase, then to execute all of the validations again on the data with the proposed changes from the amendments applied to the data in a post-amendment phase. Such a sequence of phases allows assertions to be made about the quality of the data as they were initially presented, and how much the quality of the data would be improved if the amendments were accepted. Within pre-amendment and post-amendment phases, the validations and measures are agnostic about the order in which they are run, the extent to which they are run in parallel, or the extent to which they are run on single records or on unique values within a data set. One possible workflow for tests is to aggregate the unique values of applicable Information Elements within a bdqffdq:MultiRecord for each Validation or Measure, then to execute the Validation or Measure on just the unique values, then de-aggregate the results back to each bdqffdq:SingleRecord. This is analogous to implementing tests as SQL queries.

Given a hypothetical Event table with fields including a primary key event_id and an integer field day, implementation of VALIDATION_DAY_STANDARD in SQL that operates on data in the aggregate might look like:

SELECT
    ‘VALIDATION_DAY_STANDARD’ as test name, event_id,
    ‘INTERNAL_PREREQUISITES_NOT_MET’ as Result_status, null as Result_value,
     ‘No value for dwc:day to evaluate’ as Result_comment 
FROM event
    WHERE day is null
UNION 
SELECT
    ‘VALIDATION_DAY_STANDARD’ as test name, 
    event_id,
    ‘RUN_HAS_RESULT’ as Result_status, 
    ‘COMPLIANT’ as Result_value,
    ‘Value of dwc:day [‘|| day ||’] is in the range 1-31’ as Result_comment 
FROM event
    WHERE day >=1 and day <=31
UNION 
SELECT
    ‘VALIDATION_DAY_STANDARD’ as test name, 
    event_id,
    ‘RUN_HAS_RESULT’ as Result_status, 
    ‘NOT COMPLIANT’ as Result_value,
    ‘Value of dwc:day [‘|| day ||’] is outside the range 1-31’ as Result_comment 
FROM event
    WHERE day < 1 or day > 31



## 7. Implications for the Darwin Core Standard (John)

Early recognition that estimating 'fitness for use'/'quality was made difficult because of the lack of vocabularies...TG4.

Definitions, uses in the wild, and best practices for Taxon class ..ID terms.

[ Mention of issues arising such as use of dwc:country and dwc:countryCode and "High Seas"]

How to identify the High Seas.

## 9. Acronyms

| **Acronym** | **Explanation**                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------|
| ALA         | Atlas of Living Australia                                                                                      | 
| BDQ         | TDWG Biodiversity Data Quality Interest Group                                                                  |
| BISON       | Biodiversity Information Serving Our Nation                                                                    |
| CRIA        | Centro de Referência em Informação Ambiental                                                                   |
| EPSG        | European Petroleum Survey Group                                                                                |
| GBIF        | Global Biodiversity Information Facility                                                                       |
| iDigBio     | Integrated Digitized BioCollections                                                                            |
| IRI         | Internationalized Resource Identifier                                                                          |
| ISO         | International Standards Organization                                                                           |
| TDWG        | Biodiversity Information Standards                                                                             |
| TG1         | Biodiversity Data Quality Interest Group Task Group 1: Framework on Data Quality                               |
| TG2         | Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions                       |
| TG3         | Biodiversity Data Quality Interest Group Task Group 3: Data Quality Use Cases                                  |
| TG4         | Biodiversity Data Quality Interest Group Task Group 4: Best Practices for Development of Vocabularies of Value |


## 10. References

* Belbin L, Daly J, Hirsch T, Hobern D, Salle JL (2013) A specialist’s audit of aggregated occurrence records: An ‘aggregator’s’ perspective. ZooKeys 305: 67–76. doi: 10.3897/zookeys.305.5438
* Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889
* Rees ER, Nicholls M (2020). Suppl. material 2: Data Quality Use Case Study Result. https://biss.pensoft.net/article/download/suppl/5255738/.
* [RFC-2119] http://tools.ietf.org/html/rfc2119 Key words for use in RFCs to Indicate Requirement Levels. 1997. The Internet Engineering Task Force.
Sanderson et al. (2107) see Section 1.5
* Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731
* Wieczorek J, Bloom D, Guralnick R, Blum S, Döring M, Giovanni R, Robertson T, Vieglais D (2012) Darwin Core: An Evolving Community-Developed Biodiversity Data Standard. PLoS ONE 7(1): e29715. https://doi.org/10.1371/journal.pone.0029715


---

## User guide



