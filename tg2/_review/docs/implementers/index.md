# BDQ Core Implementer's Guide

**Date version issued**  (Draft)

**Date created** (Draft)

**Part of TDWG Standard**

**This version**

**Latest version**

**Previous version**

**Contributors**

**Creator**

TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions).

## Introduction

#### 5.2.4 Guidelines for Implementers (non normative)

**TODO: Mention of the need for local caching of web-site based source authorities.**

Implementors should locally cache the results of calls to remote web services, particularly if they operate on a sequence of SingleRecords instead of operating on distinct values of InformationElements.  Data sets typically contain many repeated values, and remote web services should not be subject to repeated requests asking the same question over and over. 

**TODO: Note that implementors do not need to implement web service calls to source authorities that are highly stable (e.g. DCMI type vocabulary #41).

Some source authorities are highly stable small vocabularies.  Implementors may choose to query a local copy of such a vocabulary, even if a remote service is specified in a bdq:sourceAuthority for a test.  Implementors should monitor for changes to that vocabulary. 

**TODO: The value supplied for the parameter for the test is not an attribute of the data, it is an attribute of the Mechanism (of the system assessing the data quality). If we had included assertions about the validity values of parameters, they should only return external prerequisites not met, as they are assertions about externalities to the data and will change if the same data are run on the same test with a different configuration.**


#### Example (non normative)

Given the specification: 

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:SourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode was EMPTY; COMPLIANT if the value of dwc:countryCode is found in bdq:sourceAuthority; otherwise NOT_COMPLIANT

Pseudocode for an implementation follows the sequence of RESPONSE,critera; of the specification, with external prerequisites being able to be thrown from anywhere within the logic, but handled within the construct that builds a Result object.

    Function validationCountrycodeNotempty(countryCode) returns Result {
      String sourceAuthority = "ISO 3166-1-alpha-2"
      Result result = new Result()
      try { 
          if (isEmpty(countryCode) { 
              result.setStatus(INTERNAL_PREREQUISITES_NOT_MET) 
              result.setComment("provided countryCode is empty."
          } else {
              result.setStatus(RUN_HAS_RESULT) 
              if (isFoundCountryCode(countryCode,sourceAuthority)) { 
                 result.setValue(COMPLIANT)
                 result.setComment("provided countryCode ["+countryCode+"] is a known "+sourceAuthority+" countryCode ")
              } else { 
                 result.setValue(NOT_COMPLIANT)
                 result.setComment("provided countryCode ["+countryCode+"] is not a known "+sourceAuthority+" countryCode ")
              }
          } 
      } catch NetworkException {
          result.setStatus(EXTERNAL_PREREQUISITES_NOT_MET) 
          result.setComment("Temporary failure looking up countryCode, try later")
      }
      return result;
    }

    Function isfoundCountryCode(countryCode,sourceAuthority) returns boolean throws NetworkException {...}



## Validating Test Implementations

Implementors of tests SHOULD validate the behaviour of the internals of their test implementations with unit tests, and MUST validate that each test implementation is capable of taking relevant input from a set of standard test validation data, and returning the expected responses.

### Introduction

Accompanying the Core test descriptors is a set of test validation data.  This test validation data is intended for implementors to use to evaluate whether or not their test implementations produced the expected Response values for a set of cases for each test.  Each test specification could be graphed as a flow chart with several paths, the test validation data are intended to cover each node and each path within each test specification with at least a single case.  These are not exhaustive unit tests covering large numbers of edge cases, but rather a minimal set of tests for expected behaviour.  

The test validation data are organized as two flat CSV files.  Each row in each file is intended for a single validation of a single test.  The file has columns identifying the validation case, the test that the row is intended to validate, the expected Response.status, Response.value, an example Response.comment, parameter values, if any, and a set of Darwin Core terms (most of which are empty for a given test).   

The test validation records are all fragmentary flat Darwin Core Occurrence records.  Each row contains values for only those Darwin Core terms that are relevant input to the particular validation.   The validation records are all fragmentary, consisting of a mixture of real and artificial data with most of the records being synthetic.  The validation data are a set of 1191 records, with about 10 validation cases for each test.  The set of rows for a particular test are designed to validate that an implementation of that particular test performs as expected against the specifications.   This data set is referred to as the 'Test Validation Data'.   The set of about 10 validation records for each test are designed to exercise all of the decision pathways in the specification of the test.  

This is a minimalist suite of test data. Additional test records can be readily generated or adapted from real data using the following template based on the specifications below. In consideration of the community, the DataID values MUST uniquely identify a validation case for each additional test data record and the resulting data added to the GitHub repository.

### Considerations Concerning Input Data Values for AMENDMENTS

One of the early conclusions to this project was the need for controlled vocabularies and an early spin-off of Data Qality Task Group 4 on Vocabularies (https://github.com/tdwg/bdq/tree/master/tg4). Testing the 'quality' or 'fitness for use' of Darwin Core encoded data is made more difficult due to the lack of a comprehensive suite of controlled vocabularies.

Testing Darwin Core values against a known Source Authority using a VALIDATION type test is straight forward: A test is either COMPLIANT or NOT COMPLIANT. This standard includes tests of type AMENDMENT and the mapping of input Darwin Core values to known Vocabulary values is poorly developed. If a VALIDATION returns COMPLIANT, no AMENDMENT is necessary. For example, if the input value to a test is say dwc:sex="Female", then no AMENDMENT is required. If however, the input value is dwc:sex:f., can this be interpreted as "Female"? Probably. What about dwc:sex="M"? This could be "Male" or "Mixed" according to https://api.gbif.org/v1/vocabularies/Sex/concepts. <!--- Ming: I asked GBIF about this specific example and they said that "M" will be matched to Male, but I am not sure how the API works exactly ---><!--- PJM: the rec_occur_qc implementation uses the vocabulary directly, finds, ^M matches male and mixed, so asserts that it can't make the amendment, I can't speak about the (by our test specification, incorrect) actions that gbif is taking on their vocabulary, their API delivers the vocabulary, but doesn't do this sort of matching, so what they are describing is some internal that uses the vocabulary --->

A key phrase within this standard that particularly relates to many of the Expected Responses of tests is " dwc:term can be unambiguously interpreted as ...". In the case above for dwc:sex="M", the determination is that it is ambiguous. In this case, no AMENDMENT can be made.

When carrying out Amendments where numeric vales are concerned (e.g. feet to meters, etc.) the principle of reversability is paramount, and thus rounding up or down or using approximations should be avoided and only exact values used.

We see an urgent need for a comprehensive, internationally agreed list of Darwin Core (https://dwc.tdwg.org/) term values that are mapped to standard values. GBIF has implemented some unique values, for example https://api.gbif.org/v1/vocabularies/Sex/concepts/Female/hiddenLabels, but such lists are not comprehensive. While there has been a survey of Darwin Core 'distinct' values for GBIF, ALA, iDigBio and VertNet, these are both dated, and where possible, have not been mapped to standard values, if they exist.

In this standard, we have taken an expedient approach in relation to making AMENDMENTs. We have used code in our tests to try and parse out likely, unambiguous matches. This is far from an ideal solution, but it does provide the potential of our AMENDMENTs to 'value add' to Darwin Core data records.

### Structure of the Validation Data 

The validation data are intended as input into a testing system that can implementations of validation tests independently, presenting them with a validation case for input, and assessing whether the test Response conforms to the expected values in the validation data.  It could be processed as input for unit tests.   It could be used as the basis for presenting synthetic records to a larger test execution system, but is designed to be used at a level where individual tests are being assessed.  This may fit into integration tests of a larger system.  The structure of the validation data attempts to be at a level of abstraction somewhat above the method signature specificity needed in unit tests, but still at a level that is examining individual test implementations, below the level of testing inputs and outputs of a larger data processing system that could take complete Darwin Core records as input and return rich data quality reports as output (to avoid forcing particular formats on data quality reports as a whole).  

The following column header for the data are used for the validation data files.

<!-- vocabulary terms that apply only to the validation data files wth their current definitions --->

| header | definition |
| ------ | ---------- |
| dataID | The local (to bdq:ValidationData) integer indentifier for the Validation Data record | 
| LineForTest | A local to bdq:ValidationData identifier for test records within one test | 
| LineNumber | The sequence number of the data record in the bdq:ValidationData |


* Line Number: An integer for maintaining the sort order of the file.
* dataID: A unique identifier (within the validation data) of the validation data record, e.g., "123"
* LineForTest: An integer for maintaining the sort order of the validation case with in the set of validation cases for a particular test,
* GitHubIssueNo: The GitHub issue where rationale management of the test under validation is maintained, can be use to form a link to the discussion history for the development of the relevant test, e.g., 20 can be found at https://github.com/tdwg/bdq/issues/20
* GUID: the machine readable identifier for the test under validation, e.g. 69b2efdc-6269-45a4-aecb-4cb99c2ae134
* Label: The human-readable name of the test, e.g., "VALIDATION	COUNTRY_FOUND"
* Response.status: The status on applying the test to the test data record. For VALIDATIONS, one of the terms "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET" or "RUN_HAS_RESULT". For AMENDMENTS, one of the terms "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET", "FILLED_IN", "AMENDED" or "NOT_AMENDED". For ISSUE, one of the terms "INTERNAL_PREREQUISITES_NOT_MET" or "RUN_HAS_RESULT". For MEASURES, either "RUN_HAS_RESULT" or "INTERNAL_PREREQUISITES_NOT_MET".
* Response.result: The result of running the test on the test data record. For VALIDATIONS and AMENDMENTS, "NULL" where the Response.status is either "EXTERNAL_PREREQUISITES_NOT_MET", "INTERNAL_PREREQUISITES_NOT_MET". For VALIDATIONS, either "COMPLIANT" or "NOT_COMPLIANT" where Response.status is "RUN_HAS_RESULT".  For AMENDMENTS where Response.status is either "FILLED_IN" or "AMENDED, the Response.result is a json structure containing a key:value list of Darwin Core terms and values for changes proposed by the AMENDMENT. For MEASURES, a resulting value or "NOT_REPORTED".
* Response.comment: An example human-readable statement identifying the reason for the test result given the input data, implementations are not expected to produce this exact value, it is given as an example.
* IssuesWithThisRow: Temporary working column for recording problems while developing validation data, to be removed.
* bdq:annotation placeholder for an annotation when testing for their presence.
* bdq:sourceAuthority input parameter for some parameterized tests.
* dwc: (77 columns)  All of the Darwin Core terms that are in scope for Core.  In each row, only those identified in the Information Elements of the relevant test and pertinent to the test case at hand contain values.

NOTE: We have implemented examples of EXTERNAL_PREREQUISITES_NOT_MET using the Input.Data structure of

bdq:sourceAuthority="https://invalid/invalidservice", dwc:inputDataValue1="", dwc:inputDataValue 2... or as an example

bdq:taxonomyIsMarine="https://invalid/invalidservice", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:scientificName=""

See Section on Implementation

### Examples of the data for validating tests (Informative)

The validation files contain one column for each of 77 Darwin Core terms that are referenced as an Information Element somewhere in Core, but only terms relevant to the particular validation case for the row are populated, therefore the validation files are sparse.  They contain fragments of Flat Darwin Core records. 

The header line for each of the validation files:  

"LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Response.status","Response.result","Response.comment","IssuesWithThisRow","bdq:annotation","bdq:sourceAuthority","dc:type","dcterms:license","dwc:acceptedNameUsageID","dwc:basisOfRecord","dwc:class","dwc:continent","dwc:coordinateUncertaintyInMeters","dwc:country","dwc:countryCode","dwc:county","dwc:dataGeneralizations","dwc:dateIdentified","dwc:day","dwc:decimalLatitude","dwc:decimalLongitude","dwc:endDayOfYear","dwc:establishmentMeans","dwc:eventDate","dwc:family","dwc:genus","dwc:geodeticDatum","dwc:higherClassification","dwc:higherGeography","dwc:higherGeographyID","dwc:infraspecificEpithet","dwc:island","dwc:islandGroup","dwc:kingdom","dwc:locality","dwc:locationID","dwc:maximumDepthInMeters","dwc:maximumElevationInMeters","dwc:minimumDepthInMeters","dwc:minimumElevationInMeters","dwc:month","dwc:municipality","dwc:occurrenceID","dwc:occurrenceStatus","dwc:order","dwc:originalNameUsageID","dwc:parentNameUsageID","dwc:phylum","dwc:scientificName","dwc:scientificNameAuthorship","dwc:scientificNameID","dwc:specificEpithet","dwc:startDayOfYear","dwc:stateProvince","dwc:subgenus","dwc:taxon","dwc:taxonConceptID","dwc:taxonID","dwc:taxonRank","dwc:verbatimCoordinateSystem","dwc:verbatimCoordinates","dwc:verbatimDepth","dwc:verbatimElevation","dwc:verbatimEventDate","dwc:verbatimLatitude","dwc:verbatimLocality","dwc:verbatimLongitude","dwc:verbatimSRS","dwc:vernacularName","dwc:waterBody","dwc:year","dwc:subfamily","dwc:superfamily","dwc:tribe","dwc:subtribe","dwc:genericName","dwc:infragenericEpithet","dwc:cultivarEpithet","dwc:individualCount","dwc:organismQuantity","dwc:footprintWKT","dwc:coordinatePrecision","dwc:namePublishedInYear","dwc:sex","dwc:typeStatus","dwc:pathway","dwc:degreeOfEstablishment","bdq:taxonIsMarine","bdq:geospatialLand","bdq:assumptionOnUnknownBiome","bdq:latestValidDate","bdq:earliestValidDate"

The data are sparse, as most dwc: term columns do not contain a value for each individual case.

A validation test case evaluating empty, where no dwc: term columns contain a value (dataID=1):  

"2","1","1","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","INTERNAL_PREREQUISITES_NOT_MET","","dwc:countryCode is EMPTY","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation test case for a validation where the input data result in a Response.value of NOT_COMPLIANT (dataID=7)

"8","7","7","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","NOT_COMPLIANT","dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value ","","","","","","","","","","","","Austria","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

A validation test case for a validation where the input data result in a Response.value of COMPLIANT (dataID=8)

"9","8","8","20","0493bcfb-652e-4d17-815b-b0cce0742fbe","VALIDATION_COUNTRYCODE_STANDARD","RUN_HAS_RESULT","COMPLIANT","dwc countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value","","","","","","","","","","","","US","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""

### Where to get the validation data (Informative)

The validation data is in two files, one containing normal data values, the other containing validation cases using non-printing characters.

1. [TG2_test_validation_data.csv](TG2_test_validation_data.csv)
2. [TG2_test_validation_data_nonprintingchars.csv](TG2_test_validation_data_nonprintingchars.csv)

Validation file containing data values that would be expected to be encountered in the wild: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data.csv

Validation data file containing non-printing characters for testing implementation of EMPTY: 
 https://raw.githubusercontent.com/tdwg/bdq/master/tg2/core/TG2_test_validation_data_nonprintingchars.csv

This file is a csv file with the same set of columns as the above, but with rows that contain input values for selected Darwin Core terms consisting of either the 0x00 null character (e.g. dwc:scientificName="0x00"), or a pair of ASCII control characters (shift out 0x0E and shift in 0x0F, e.g. dwc:day="0x0E0x0F"). This file is intended to validate that implementations of tests are consistently evaluating inputs as EMPTY as expected by the definition of EMPTY.  

The non-printing characters file MUST only be edited with a tool that will maintain the non-printing characters.  

Both files have a header line identifying the specifications as defined in Section 6.2.

The expectation for the response that an implementation should produce when executed against the row: "Response.status","Response.result","Response.comment", where an implementation is expected to produce the exact Response.status, the exact Response.result (ignoring order of any key-value pairs for an amendment response), and Response.comment is an example of what a comment, in English, might look like.  

Parameter values are specified in a bdq:sourceAuthority column, when more than one sourceAuthority is involved, then these are given separate names.

Darwin Core input columns are specified as "dc:type","dcterms:license","dwc:acceptedNameUsageID",...
