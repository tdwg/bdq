# Files describing and supporting the BDQ Core tests

## The BDQ Core test descriptors

These are the authoritative descriptors of the BDQ core tests, extracted from Github issue markdown tables using [bdq_issue_to_csv](https://github.com/kurator-org/bdq_issue_to_csv) one file contains the SingleRecord tests, the other file the MultiRecord Measures.

- TG2_tests.csv
- TG2_multirecord_measure_tests.csv

### Turtle and RDF/XML representations of the tests

These are produced from the csv files above using [kurator-ffdq](https://github.com/kurator-org/kurator-ffdq).  See instructions in [this README](https://github.com/kurator-org/bdq_issue_to_csv/blob/master/README.md)

- TG2_tests.ttl
- TG2_tests.xml
- TG2_multirecord_measure_tests.ttl
- TG2_multirecord_measure_tests.xml

### Supporting csv files containing lists of guids

These files allow kurator-ffdq to preserve the identifiers of objects in the RDF when regenerating from the CSV into RDF.

information_element_guids.csv
usecase_test_list.csv
TG2_tests_additional_guids.csv
test_label_mappings.csv

## Test validation data 

These files are for implementers to validate that their implementations of the BDQ Core tests produce expected results.  They consist of one line per validation, with columns specifying the test being validated by that row, one column for each of the inputs for the information elements and parameters for a single test, and columns holding the expected outputs.  Each test has multiple validation rows.  

TG2_test_validation_data.csv
TG2_test_validation_data_nonprintingchars.csv

### Draft of a test validation data set

This file contains a complete synthetic flat Darwin Core record.  No specification is provided yet for expected results of execution against an implementation of the tests.

TG2_test_validation_data_synthetic_occurrence.csv

### Python script to convert one colums per information test validation spreadsheet into one with a single column for all Input.data

Maintinance of validation data is easier in this more compact spreadsheet form, but the one column per information element form is more easily consumed by a test validation framework.

- squish_validation_data.py
- test_validation_maintainer.csv

