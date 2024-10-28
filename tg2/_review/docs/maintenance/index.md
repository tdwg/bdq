**NOTE** This is the BDQ Core Maintenance document, it may be edited, it is not built from a template.

# Preliminary Guidance for Maintainers of BDQ Core

## 1 Introduction

Notes for the guidance for maintainers if the BDQ Core standard is ratified.

### 1.1 Purpose
This document is for guidance of the BDQ Core Maintenence Group

### 1.2 Audience
Biodiversity Information Standards (TDWG) BDQ Core Maintenance Interest Group

### 1.3 Associated Documents
- The [BDQ Core Quick Reference Guide](../../terms/bdqcore/index.md) provides a brief summary of the Tests in BDQ Core
- The [BDQ Core Introduction](../../intro/index.md) provides an introduction to the BDQ Core standard and the Tests
- The [BDQ Core Implementer's Guide](../implementers/index.md) provides a more detailed view for those seeking to implement BDQ Core
- 
### 1.4 Status of the content of this document
This document is non-normative.

## 1.5 RFC 2119 key words
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## 2 Proposals for New Issues 

Templates for proposals of new and change issues are available at https://github.com/tdwg/bdq/tree/master/.github/ISSUE_TEMPLATE

**Note** These templates need to be updated to conform with production of term-version file entries (e.g. GUID->term_localName)

### 2.1 Suggested Lifecycle for a Proposal
1. Tag as Proposed
2. Review the proposal, including evaluating that the expected response follows a path an implementor can understand, that the information elements are referenced in the expected response, and whether parameters are present and formatted as desired.
3. Confirm that the proposal is not a duplicate of an existing issue, including both Do Not Implement and Imature/Incomplete issues.
4. Discussion at any point may conclude that the test is not able to be implemented or should not be implemented as results would be misleading or problematic, tag as Do Not Implement, desribe why in comments on the issue, and close the issue.
5. Discussion at any point may conclude that the test is a good one, but can't be implemented at the present time as some needed resource, such a a controlled vocabulary, does not exist (yet), tag as Imature/Incomplete.  Describe why in comments on the issue, leave open or closed as desired.
6. Produce example data covering each path through the expected response, add these to a validation sheet.
7. The markdown table from the test can be exported to a csv list of proposed tests.  This csv list can be used by implementors to generate code stubs for tests to be implemented.
8. Implementors produce at least one implementation of the test, this will provide feedback on the expected response, and whether or not the test is implementable.
9. Implementors run the implementation against the validation data, this will result in idenfification of problems that may be defects in the implementation, errors in the validation data, or problems in the specification.  
10. Confirm that the normative and non-normative elements are filled in as needed, including any references and links to source code for implementations.
11. Confirm that the Proposed test is linked to at least one use case.  
12. Once at least one implementation exists that passes all validation tests (produces exactly the expected Response.status, exactly the expected Response.result, and some Response.comment for each validation case/row), the Proposed test can be evaluated for inclusion in the standard.  
13. At acceptance, tag the issue as CORE, remove the Proposed tab, export the markdown table into the normative term versions csv, generate derivatives as needed, and close the issue.

## 3 Test Validation Data
The Test Validation Data is a file of Darwin Core (Wieczorek et al. 2011) records where each record provides-

- Input.data: The values of bdqffdq:InformationElements (bdq:InformationElementsConsulted and bdq:InformationElementsActedUpon) required as input to the test
- Output.data: For AMENDMENT Type Tests, the output values of amended bdq:InformationElementsActedUpon
- A Response.status that informs the expected status of running the Test on the input data
- A Response.result that informs the expected outcome of running the Test on the input data
- A Response.comment that explains the reasoning for the Response of running the Test on the input data
- Date Last Updated
- Anciliary information that provides a context for generating and maintaining Test Validation Data
  - The URL for the GitHub Issue Test page
  - The Test number (the number on the end of the URL for the GitHub Issue page
  - The Test GUID
  - TestType: Either VALIDATION, ISSUE, MEASURE or AMENDMENT
  - Test Label: The last two components of the full Test Label that enables sorting by the Information Element focus of the Test
  - The Data Dimension: What dimension of the data does the Test focus on, either NAME, SPACE, TIME, or OTHER
  - The record unique identifier
  - The within Test unique identifier (see below on special values)

### 3.1 Edits to Current Test Validation Data
Amend the data record as required, and update the Date Last Updated is REQUIRED

### 3.2 Additions to Test Validation Data
The Test Validation Data provides a minimal suite of Darwin Core records to test the pathways through each Test Specification. The addition of edge cases to the existing Test Validation Data is RECOMMENDED. The addition of Validation Test Data for new Tests is REQUIRED.

The Test Validation Data uses CSV format. There are two versions of the Validation Test Data. The original compressed format version [link] has a single column containing the values for the relevant Information Elements. This file is transformed by xxx into an expanded version [link] where each Information Element forms a separate column. The transfomred version is simpler to use by the testing framework. It is easier to edit the compressed version of the Test Validation Data to change an existing record or add one or more new records. This compressed version of the file contains columns of information for each record (e.g., link to Test, Label, Dimension) that SHOULD be helpful in understanding the context of the focus columns of Input.data, Output.data, Response.status and Response.result. The Response.comment MUST describe the reason for the Response.status. 

Additions to the Test Validation Data are best done by copying and pasting an existing record and editing the content of the new record. Within the (compressed) Test Validation, note that the DataID is unique, so additions MUST NOT re-use an existing DataID value. 

Values in the column **LineForTest** are useful in determining the number of Test Validation records for each Test, but also flag an additional function. A LineForTest value of "88" flags an Input.data value of "[null]" while a value of "99" flags an Input.data value of "[non-printing characters]". Both of these record types are used to separate records of 'normally' expected values from records that require special handing within the testing framework. 

### 3.3 Updating Test Validation Data Due to Changes in Specifications or Terms

If any part of the logic of a test changes, parallel changes must be made to the test data for that test. For example, a change in a tests Expected Response/Specification will very likely to result in the need to amend at least one record within the associated test validation data. For example the Expected Response of the Test [AMENDMENT_EVENT_FROM_EVENTDATE](https://rs.tdwg.org/bdqcore/terms/710fe118-17e1-440f-b428-88ba3f547d6d) to limit amendments to a single year resulted in an amendment to the Response.status of the data record DataID #320 from "FILLED_IN" to "NOT_AMENDED".

A change to a Test data may also precipitate the need to change one or both of the Examples within the Test Specification. As all examples of Tests are based on the associated Test Validation Data records, any such need for changes should be explicit.

Therefore any changes to Test Specifications must trigger the need to check the associated Test Validation Data and examples.

### 3.4 Processing Test Validation Data

<!--- Paul?? **TODO**?--->
