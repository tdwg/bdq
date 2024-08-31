**NOTE** This is a placeholder for the BDQ Core Maintenance document, which has it's source in tg2/core/generation/Maintainance.md.

# Preliminary suggested guidance for maintainers

Notes on some preliminary guidance for maintainers if the BDQ-Core standard is ratified.

## RFC 2119 keywords
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

# Proposals for New Issues 

Templates for proposals of new and change issues are available at https://github.com/tdwg/bdq/tree/master/.github/ISSUE_TEMPLATE

## Suggested Lifecycle for a proposal,

Tag as Proposed

Review the proposal, including evaluating that the expected response follows a path an implementor can understand, that the information elements are referenced in the expected response, and whether parameters are present and formatted as desired.

Confirm that the proposal is not a duplicate of an existing issue, including both Do Not Implement and Imature/Incomplete issues.

Discussion at any point may conclude that the test is not able to be implemented or should not be implemented as results would be misleading or problematic, tag as Do Not Implement, desribe why in comments on the issue, and close the issue.

Discussion at any point may conclude that the test is a good one, but can't be implemented at the present time as some needed resource, such a a controlled vocabulary, does not exist (yet), tag as Imature/Incomplete.  Describe why in comments on the issue, leave open or closed as desired.

Produce example data covering each path through the expected response, add these to a validation sheet.

The markdown table from the test can be exported to a csv list of proposed tests.  This csv list can be used by implementors to generate code stubs for tests to be implemented.

Implementors produce at least one implementation of the test, this will provide feedback on the expected response, and whether or not the test is implementable.

Implementors run the implementation against the validation data, this will result in idenfification of problems that may be defects in the implementation, errors in the validation data, or problems in the specification.  

Confirm that the normative and non-normative elements are filled in as needed, including any references and links to source code for implementations.

Confirm that the Proposed test is linked to at least one use case.  

Once at least one implementation exists that passes all validation tests (produces exactly the expected Response.status, exactly the expected Response.result, and some Response.comment for each validation case/row), the Proposed test can be evaluated for inclusion in the standard.  

At acceptance, tag the issue as CORE, remove the Proposed tab, export the markdown table into the normative term versions csv, generate derivatives as needed, and close the issue.

## Additions to Test Validation Data

The Test Validation Data provides a minimal suite of Darwin Core records to test the pathways through each Test Specification. The addition of edge cases to the existing Test Validation Data is RECOMMENDED. The addition of Validation Test Data for new Tests is REQUIRED.

The Test Validation Data uses CSV format. There are two versions of the Validation Test Data. The original compressed format version [link] has a single column containing the values for the relevant Information Elements. This file is transformed by xxx into an expanded version [link] where each Information Element forms a separate column. The transfomred version is simpler to use by the Test Validation process.

It is easier to edit the compressed version of the Test Validation Data to change an existing record or add one or more new records. This compressed version of the file contains columns of information for each record (e.g., link to test, Label, Dimension) that SHOULD be helpful in understanding the context of the focus columns of Input.data, Output.data, Response.status and Response.result. The Response.comment MUST describe the reason for the Response.status. 

@paul [Normal and special character file handling].

### Edits to Current Test Validation Data

Amend the data record as required and updating the Date Last Updated is REQUIRED

#### 6.8 Updating test data due to changes in specifications or terms

If any part of the logic of a test changes, parallel changes must be made to the test data for that test. For example, a change in a tests Expected Response will very likely to result in the need to amend at least one record within the associated test data. For example the Expected Response of the test AMENDMENT_EVENT_FROM_EVENTDATE to limit amendments to a single year resulted in an amendment to the Response.status of the data record DataID #320 from "FILLED_IN" to "NOT_AMENDED".

A change to the test data may also precipitate the need to change one or both of the Examples within the test specification. As all examples of tests are based on the associated tests records in the test data, any such need for changes should be explicit.

Similarly, changes to the test specification 'Information Elements ActedUpon' and 'Information Elements Consulted' will may require changes to Input.data, Output.data, Response.result and Response.comment.

Therefore any changes to test specifications must trigger the need to check the associated test data and examples.

### Additions to Test Validation Data

Additions to the Test Validation Data are best done by copying and pasting an existing record and editing the content of the new record. Within the (compressed) Test Validation, note that the DataID is unique, so additions MUST NOT re-use an existing DataID value. 

Values in the column **LineForTest** are useful in determining the number of Test Validation records for each Test, but also flag an additional function. A LineForTest value of "88" flags an Input.data value of "[null]" while a value of "99" flags an Input.data value of "[non-printing characters]". Both of these record types are used to separate records of 'normally' expected values from records that require special handing within the testing framework. 

### Processing Test Validation Data


