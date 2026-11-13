# Files describing and supporting the BDQ Tests

## The BDQ Test descriptors

These are copies of the descriptors of the BDQ Tests, originally extracted from GitHub issue markdown tables using [bdq_issue_to_csv](https://github.com/kurator-org/bdq_issue_to_csv); one file contains the SingleRecord Tests, the other file the MultiRecord Measures. They are derived from _review/vocabulary/bdqtest_term_versions.csv by _make_review/copy_files.sh. **As of 2026-11-13 the source of truth for the Tests is tdwg/rs.tdwg.org, branch `bdq-source`**, and `bdqtest_term_versions.csv` and the GUID tables below are copies kept in step with it until the build reads rs.tdwg.org (see [Where the BDQ standard is maintained](../README.md#where-the-bdq-standard-is-maintained-sources-of-truth)). Do not edit these files as the place of record: change the Tests in rs.tdwg.org, then copy the change here.

- TG2_tests.csv
- TG2_multirecord_measure_tests.csv

### Turtle and RDF/XML representations of the Tests

These are produced from the CSV files above using [kurator-ffdq](https://github.com/kurator-org/kurator-ffdq).  See instructions in [this README](https://github.com/kurator-org/bdq_issue_to_csv/blob/master/README.md)

- TG2_tests.ttl (now _review/dist/bdqtests.ttl)
- TG2_tests.xml (now _review/dist/bdqtests.xml)

- TG2_multirecord_measure_tests.ttl
- TG2_multirecord_measure_tests.xml

### Supporting CSV files containing lists of GUIDs

These files allow kurator-ffdq to preserve the identifiers of objects in the RDF when regenerating from the CSV into RDF. rs.tdwg.org keeps its own copies, in `bdqtest-graph-inputs/` of the release directories on `bdq-source` where they change, and generates the served Test graphs from them; changes are made there first.

- information_element_guids.csv
- TG2_tests_additional_guids.csv
- TG2_policy_guids.csv 
- TG2_tests_argument_guids.csv 
- TG2_citation_guids.csv  for dcterms:BibliographciResource objects extracted from "References" columns in the TG2_tests.csv file.

test_label_mappings.csv (?no longer used?)

Deprecated file formerly used for test-usecase mapping, now replaced by the UseCases colunn in the TG2_tests.csv file.

usecase_test_list_deprecated.csv

## Test Validation Data 

These files are for implementers to validate that their implementations of the BDQ Tests produce expected results.  They consist of one line per validation, with columns specifying the Test being validated by that row, one column for each of the inputs for the Information Elements and parameters for a single Test, and columns holding the expected outputs.  Each Test has multiple validation rows.  

TG2_test_validation_data.csv
TG2_test_validation_data_nonprintingchars.csv

### Draft CSV of Test Validation Data 

This file contains a complete synthetic [Simple Darwin Core](https://dwc.tdwg.org/simple/) record.  No specification is provided yet for expected results of execution against an implementation of the Tests.

TG2_test_validation_data_synthetic_occurrence.csv

### Python script to convert one column per information Test validation spreadsheet into one with a single column for all Input.data

Maintenance of validation data is easier in this more compact spreadsheet form, but the one column per Information Element form is more easily consumed by a Test validation framework.

- squish_validation_data.py
- test_validation_maintainer.csv

