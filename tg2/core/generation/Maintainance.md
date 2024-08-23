# Preliminary suggested guidance for maintainers

Notes on some preliminary guidance for maintainers if the BDQ-Core standard is ratified.

# Proposals for New Issues 

Templates for proposals of new issues are available

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

Confirm that the normative and non normative elements are filled in as needed, including any references and links to source code for implementations.

Confirm that the Proposed test is linked to at least one use case.  

Once at least one implementation exists that passes all validation tests (produces exactly the expected Response.status, exactly the expected Response.result, and some Response.comment for each validation case/row), the Proposed test can be evaluated for inclusion in the standard.  

At acceptance, tag the issue as CORE, remove the Proposed tab, export the markdown table into the normative term versions csv, generate derivatives as needed, and close the issue.
