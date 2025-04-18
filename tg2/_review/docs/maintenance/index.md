# BDQ Core Maintenance Guide

## Table of Contents ##
[1 Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Audience](#12-audience)
  - [1.3 Associated Documents](#13-associated-documents)
  - [1.4 Status of the content of this document](#14-status-of-the-content-of-this-document)
  - [1.5 RFC 2119 key words](#15-rfc-2119-key-words)

[2 Proposals for New Issues](#2-proposals-for-new-issues)
  - [2.1 Suggested Lifecycle for a Proposal](#21-suggested-lifecycle-for-a-proposal)
  - [2.2 Software Tools for Working with Test Descriptions](#22-software-tools-for-working-with-test-descriptions)
    - [2.2.1 Tools used to build the BDQ Core submission, and related code](#221-tools-used-to-build-the-bdq-core-submission-and-related-code)

[3 Test Validation Data](#3-test-validation-data)
  - [3.1 Edits to Current Test Validation Data](#31-edits-to-current-test-validation-data)
  - [3.2 Additions to Test Validation Data](#32-additions-to-test-validation-data)
  - [3.3 Updating Test Validation Data Due to Changes in Specifications or Terms](#33-updating-test-validation-data-due-to-changes-in-specifications-or-terms)
  - [3.4 Processing Test Validation Data](#34-processing-test-validation-data)
  - [3.5 Tools for validating implementations against the validation data](#35-tools-for-validating-implementations-against-the-validation-data)

[4 Proposals for Changes to existing Tests](#4-proposals-for-changes-to-existing-tests)

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to provide guidance for the ongoing maintenance of the Biodiversity Data Quality (BDQ) Core standard. In accordance with TDWG policies, ratified standards must be supported by a designated Maintenance Interest Group. This guide outlines the responsibilities of the group and describes recommended processes for managing changes, evaluating new or revised Tests, maintaining validation data, and ensuring the integrity of BDQ Core components over time.

It also documents the software tools and structured workflows that support the lifecycle of Test definitions, from proposal to validation, implementation, and inclusion in the standard.

### 1.2 Audience

This document is intended for members of the TDWG BDQ Core Maintenance Interest Group and others tasked with the stewardship and curation of the standard. It is also relevant to:

- Contributors proposing changes or new Tests
- Implementers maintaining software tools that use BDQ Core Test specifications
- Standards developers interested in understanding the governance and maintenance model used by BDQ Core.

Readers should be familiar with the structure of the BDQ Core standard and its supporting tools and vocabularies.

### 1.3 Associated Documents

This document is not part of the BDQ Core standard, and as such it has no formally associated documents within the standard itself.

However, additional background information and development context for BDQ Core may be found in the [BDQ Core Supplemental Information](docs/supplement/index.md).

### 1.4 Status of the content of this document

This document is non-normative.

This document is not part of the BDQ Core standard. 

### 1.5 RFC 2119 key words
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## 2 Proposals for New Issues 

<!--- TODO: These templates should get moved to a new maintinance repository for BDQ Core and should be removed from tdq/bdq --->

Templates for proposals of new and change issues are available at https://github.com/tdwg/bdq/issues/templates/edit.

<!--- TODO: Update templates to fit term-version files --->

**Note** These templates need to be updated to conform with production of term-version file entries (e.g., GUID->term_localName)

### 2.1 Suggested Lifecycle for a Proposal
1. Make sure a proposal is complete, clear, and follows the appropriate template.
2. Label the issue as 'Proposed'.
3. Review the proposal, including evaluating that the expected response follows a path an implementer can understand, that the Information Elements are referenced in the expected response, and whether parameters are present and formatted as desired.
4. Confirm that the proposal is not a duplicate of an existing issue, including both those with the label 'Do Not Implement' and the label 'Immature/Incomplete'.
5. Discussion at any point may conclude that the Test is not able to be implemented or should not be implemented as results would be misleading or problematic, label as 'DO NOT IMPLEMENT', describe why in comments on the issue, and close the issue.
6. Discussion at any point may conclude that the Test is reasonable, but can't be implemented as some needed resource, such a a controlled vocabulary, does not yet exist. Label as 'Immature/Incomplete'. Describe why in comments on the issue, leave open.
7. Produce example data covering each path through the expected response, add these to a validation sheet.
8. The Markdown table from the Test can be exported to a list of proposed Tests in a CSV file. This CSV-based list can be used by implementers to generate code stubs for Tests to be implemented.
9. Implementers produce at least one implementation of the Test, this will provide feedback on the expected response, and whether or not the Test is implementable.
10. Implementers run the implementation against the validation data, this will result in identification of problems that may be defects in the implementation, errors in the validation data, or problems in the Specification.
11. Confirm that the normative and non-normative elements are filled in as needed, including any references and links to source code for implementations.
12. Confirm that the Proposed Test is linked to at least one Use Case.
13. Once at least one implementation exists that passes all Validation Tests (produces exactly the expected Response.status, exactly the expected Response.result, and some Response.comment for each Validation case/row), the proposed Test can be evaluated for inclusion in the standard.
14. If ratified, label the issue as CORE, remove the 'Proposed' label, export the Markdown table into the normative term-versions CSV file, generate derivatives as needed, and close the issue.

### 2.2 Software Tools for Working with Test Descriptions

The bdq_issue_to_csv utility (Morris 2024) is available ([Zenodo](https://doi.org/10.5281/zenodo.13937570), [GitHub](https://github.com/kurator-org/bdq_issue_to_csv)) for converting Markdown tables in issues into lines of CSV (ready for use as a term-version file). See the bdq_issue_to_csv README and the [make_test_csv.sh](https://github.com/kurator-org/bdq_issue_to_csv/blob/master/make_test_csv.sh) shell script for details, including working with kurator-ffdq (Lowery et al. 2024; [Zenodo](https://doi.org/10.5281/zenodo.14026643), [GitHub](https://github.com/kurator-org/kurator-ffdq)) for generation of RDF serializations from the term-version CSV file.

#### 2.2.1 Tools used to build the BDQ Core submission, and related code

BDQ Core `_review` is built with the following three sets of shell scripts:

- bdq_issue_to_csv [make_test_csv.sh](https://github.com/kurator-org/bdq_issue_to_csv/blob/v1.0.0/make_test_csv.sh)
- [bdq/tg2/\_make_review/copy_files.sh](https://github.com/tdwg/bdq/blob/540eae5b1e609025b8dcbf19a7830d5c880aaf20/tg2/_make_review/copy_files.sh)
- [bdq/tg2/\_make_review/do_build.sh](https://github.com/tdwg/bdq/blob/540eae5b1e609025b8dcbf19a7830d5c880aaf20/tg2/_make_review/do_build.sh)

It is expected that supplementary Tests and proposed Tests under development will be maintained from issues, and the full process described in bdq_issue_to_csv [make_test_csv.sh](https://github.com/kurator-org/bdq_issue_to_csv/blob/v1.0.0/make_test_csv.sh) will be needed to produce CSV and RDF from Markdown tables in GitHub issues. This is expected to be different from the process for working with Tests that have been accepted into BDQ Core, where the GitHub issues are historical rationale management only. The authoritative file for Tests that are part of BDQ Core is a term-version file from which the build process will need to extract only the latest versions of Test records.

The bdqcore term-version file does not contain all of the UUIDs needed to produce stable RDF - the following additional files are used for that: 

- tg2/core/TG2_tests_additional_guids.csv (which should all be included in the term-version file for bdqcore, kurator-ffdq may still be reading from this file instead)
- tg2/core/information_element_guids.csv
- tg2/core/TG2_tests_argument_guids.csv
- tg1/supplementary/TG2_supplementary_additional_guids.csv

These files are a workaround and need better engineering. A tool to confirm that UUIDs are not accidentally duplicated would also be valuable.

For details on the Test Validation Data see: 

- bdqtestrunner [README](https://github.com/FilteredPush/bdqtestrunner/blob/master/README.md) used in the BDQ Core development process.
- [bdq/tg2/core/squish_validation_data.py](https://github.com/tdwg/bdq/blob/540eae5b1e609025b8dcbf19a7830d5c880aaf20/tg2/core/squish_validation_data.py) expected to be a needed tool for maintenance of the Test Validation Data in the future (as of the 540eae5b1 commit, this does not round trip between the single column Input.data column for human maintenance and the one column per input Darwin Core term version consumed by bdqtestrunner as empty terms are not correctly handled).

For more information see the following README files: 

- bdq_issue_to_csv [README](https://github.com/kurator-org/bdq_issue_to_csv/blob/master/README.md)
- kurator-ffdq [README](https://github.com/kurator-org/kurator-ffdq/blob/master/README.md) 

## 3 Test Validation Data

The Test Validation Data is a file of Darwin Core (Wieczorek et al. 2012) records where each record provides:

- Input.data: The values of bdqffdq:InformationElements (bdq:InformationElementsConsulted and bdq:InformationElementsActedUpon) required as input to the Test
- Output.data: For Amendment Type Tests, the output values of amended bdq:InformationElementsActedUpon
- A Response.status that informs the expected status of running the Test on the input data
- A Response.result that informs the expected outcome of running the Test on the input data
- A Response.comment that explains the reasoning for the Response of running the Test on the input data
- Date Last Updated
- Ancillary information that provides a context for generating and maintaining Test Validation Data
  - URL for the GitHub Issue Test page
  - Test number (the number on the end of the URL for the GitHub Issue page)
  - Test GUID
  - TestType: Either Validation, Issue, Measure or Amendment
  - Test Label: The last two components of the full Test Label that enables sorting by the Information Element focus of the Test
  - Data Dimension: What dimension of the data (what general category of Information Element) does the Test focus on, either NAME, SPACE, TIME, or OTHER (for definitions - see the [Glossary](docs/intro/index.md#6-glossary) in the [BDQ Core Introduction](docs/intro/index.md))
  - Record unique identifier
  - Unique identifier within the Test (see below on special values)

### 3.1 Edits to Current Test Validation Data
Amend the data record as required, and update the Date Last Updated is REQUIRED.

### 3.2 Additions to Test Validation Data
The Test Validation Data provides a minimal suite of Darwin Core records to Test the pathways through each Test Specification. The addition of edge cases to the existing Test Validation Data is RECOMMENDED. The addition of Validation Test Data for new Tests is REQUIRED.

The Test Validation Data uses the CSV format. There are two versions of the Validation Test Data. One is easier to maintain, the other is easier for Test validation frameworks to consume. See section [3.4 Processing Test Validation Data](#34-Processing-Test-Validation-Data) for details.

Both forms of the validation data contain columns of information for each record (e.g., link to Test, Label, Dimension) that SHOULD be helpful in understanding the context of the focus columns of Input.data, Output.data, Response.status and Response.result. The Response.comment MUST describe the reason for the Response.status. 

Additions to the Test Validation Data are best done by copying and pasting an existing record and editing the content of the new record. Within the (compressed) Test Validation, note that the DataID is unique, so additions MUST NOT re-use an existing DataID value. 

Values in the column **LineForTest** are useful in determining the number of Test Validation records for each Test, but also flag an additional function. A LineForTest value of "88" flags an Input.data value of "[NULL]" while a value of "99" flags an Input.data value in the set of "[non-printing characters]". Both of these record types are used to separate records of 'normally' expected values from records that require special handling within the testing framework. These rows SHOULD not be present in either form of the validation data set.

Validation data containing non-printing characters and NULLs SHOULD only be edited in the separate file of validation data containing non-printing characters. This file MUST only be edited by software able to correctly handle the non-printing characters. This file MUST NOT be edited with a spreadsheet application. The text editors vim or emacs are recommended.

### 3.3 Updating Test Validation Data Due to Changes in Specifications or Terms

Any change to a Test Specification MUST trigger the need to check the associated Test Validation Data and examples. If any part of the logic of a Test changes, parallel changes MUST be made to the Test data for that Test. For example, a change in a Test's Expected Response/Specification will very likely to result in the need to amend at least one record within the associated Test Validation Data. For example, the Expected Response of the Test [AMENDMENT_EVENT_FROM_EVENTDATE](https://rs.tdwg.org/bdqcore/terms/710fe118-17e1-440f-b428-88ba3f547d6d) to limit amendments to a single year resulted in an amendment to the Response.status of the data record DataID #320 from 'FILLED_IN' to 'NOT_AMENDED'.

A change to Test data may also precipitate the need to change one or both of the Examples within the Test Specification. As all examples of Tests are based on the associated Test Validation Data records, any such need for changes should be explicit.

### 3.4 Processing Test Validation Data

Test Validation Data is most easily input into validation frameworks when presented in a CSV file with one column per Information Element (e.g., Darwin Core term). However, such sparse data are very difficult for humans to edit and maintain with spreadsheet software. It is much easier to maintain is a sheet where all the input Information Elements for a validation row are concatenated as a list of key-value pairs in one spreadsheet column. 

The original Test Validation Data was developed in an Excel spreadsheet by Lee Belbin in a compressed format that has columns to identify Test rows, which Test a row pertains to, inputs and expected outputs. Exports of just the validation data sheet can be found in bdqtestrunner (Morris 2024b) (e.g., [Test_data_98_2025_03_05.csv](https://github.com/FilteredPush/bdqtestrunner/blob/master/src/main/resources/Test_data_98_2025_03_05.csv). In this format, a single column contains a list of Darwin Core terms as keys paired with values providing the relevant Information Elements for the given Test. This file was transformed by bdqtestrunner into an [expanded version](../guide/implementers/TG2_test_validation_data.csv) where each Information Element forms a separate column (then split into a file containing normal characters and a second file where particular text strings were changed to null and other non-printing characters). The transformed version is simpler to use as input for a testing framework (and was used by bdqtestrunner for validation of the Kurator/FilteredPush Test implementations) that can take [Simple Darwin Core](https://dwc.tdwg.org/simple/) as input (and doesn't need special case parsing of key:value pairs of Darwin Core terms from one column in the CSV file. It is, however is easier to edit the compressed version of the Test Validation Data to change an existing record or add one or more new records. Thus, two versions of the Test Validation Data are provided for maintenance, and maintainers are encouraged to use the compressed version for maintenance and the expanded version for testing.

A pair of tools are provided to move between the two representations. To compress sparse Information Element columns into a single column use [squish_validation_data.py]( https://github.com/tdwg/bdq/blob/master/tg2/core/squish_validation_data.py). To expand the single input Information Elements column into multiple columns one for each Information Element use [TestOfTestSpreasheetUtility.java](https://github.com/FilteredPush/bdqtestrunner/blob/master/src/main/java/org/filteredpush/qc/bdqtestrunner/TestOfTestSpreasheetUtility.java).

These tools SHOULD NOT be used on the validation data file containing non-printing characters.

Changes to squish_validation_data.py may be provided that would allow round tripping of the non-printing characters file between forms (with the replacement of non-printing characters and NULLs with specified string markers in a squished file editable in a spreadsheet application. This would allow a compressed non-printing characters file to be used for maintenance and the expanded file to be used for testing. Currently, only the expanded non-printing characters file is provided for both maintinance and testing.

### 3.5 Tools for validating implementations against the validation data

The bdqtestrunner utility is available for running Java implementations of Tests that use the ffdq-api Java annotations to annotate method signatures against validation data. See the [bdqtestrunner README](https://github.com/FilteredPush/bdqtestrunner).

## 4 Proposals for Changes to existing Tests 

<!--- TODO: Once in maintenance mode, add a template for proposals of changes to the maintenance repository. It may be possible to reuse the change template from https://github.com/tdwg/bdq/tree/master/.github/ISSUE_TEMPLATE --->

Accepted changes will need to be added as new rows to the bdqcore term-version file.

Note the distinction between the 'issued' date and 'DateLastUpdated'. 'DateLastUpdated' SHOULD only be changed if the changes are substantive to implementers (would cause them to change their code). The purpose of 'DateLastUpdated' is to allow implementers to not have to review their code when changes wouldn't affect that code. Implementers who note the 'DateLastUpdated' for each Test within their implementations can run software checks on their code to see if new changes require examination of their code. Non-substantive changes (such as addition of more non-normative known implementations) to the metadata about a Test can be distinguished by only updating the (required) value of 'issued' in the term-version file without a change to the 'DateLastUpdated'. 

Proposed substantive changes SHOULD have a software implementation.

Proposed substantive changes SHOULD have data validation rows or have proposed changes to existing data validation rows.
