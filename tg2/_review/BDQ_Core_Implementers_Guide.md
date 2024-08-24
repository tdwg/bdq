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
