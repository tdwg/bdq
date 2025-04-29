#!/bin/bash
# Shell Script to copy files from their authoritative locations in other parts of directory tree into the _review directory.
#
# Run from within the bdq/tg2/_make_review/ directory of a git checkout of the tdwg/bdq repository.

# NOTE: CORE tests are no longer maintained from the Markdown tables in the github issues.
# Current master files for the tests are: ../core/TG2_tests.csv and  ../core/TG2_multirecord_measure_tests.csv 
# TODO: Make ../_review/vocabulary/bdqtest_term_versions.csv the master copy.

# bdqtest files containing test descriptions

# TODO: The following term-versions file will become the master copy.
cp ../core/TG2_tests.csv ../_review/vocabulary/bdqtest_term_versions.csv
# TODO: replace the next step with invocation of:
# draft_build_bdqtest_singlerecord_tests_current.py
cp ../core/TG2_tests.csv ../_review/dist/bdqtest_singlerecord_tests_current.csv
# TODO: Replace these steps with creation of these files with kurator-ffdq
cp ../core/TG2_tests.xml ../_review/dist/bdqtest.xml
cp ../core/TG2_tests.ttl ../_review/dist/bdqtest.ttl
cp ../core/TG2_tests.json ../_review/dist/bdqtest.json

# TODO: The above term-versions file will become the master copy, and include the multi-record measures.
# append multi-record measures to csv list of core tests
grep -v prefLabel ../core/TG2_multirecord_measure_tests.csv >> ../_review/vocabulary/bdqtest_term_versions.csv
grep -v SingleRecord ../_review/vocabulary/bdqtest_term_versions.csv > ../_review/dist/bdqtest_multirecord_tests_current.csv

# CSV files of test validation data

cp ../core/TG2_test_validation_data.csv  ../_build_review/templates/guide/implementers/TG2_test_validation_data.csv 
cp ../core/TG2_test_validation_data_nonprintingchars.csv ../_build_review/templates/guide/implementers/TG2_test_validation_data_nonprintingchars.csv
