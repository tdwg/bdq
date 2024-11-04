#!/bin/bash
# Shell Script to copy files from their authoritative locations in other parts of directory tree into the _review directory.
#
# Run from within the bdq/tg2/_make_review/ directory of a git checkout of the tdwg/bdq repository.

# bdqcore files containing test descriptions

cp ../core/TG2_tests.csv ../_review/vocabulary/bdqcore_term_versions.csv
cp ../core/TG2_tests.csv ../_review/dist/bdqcore_singlerecord_tests_current.csv
cp ../core/TG2_tests.xml ../_review/dist/bdqcore.xml
cp ../core/TG2_tests.ttl ../_review/dist/bdqcore.ttl
cp ../core/TG2_tests.json ../_review/dist/bdqcore.json

# append multi-record measures to csv list of core tests
grep -v prefLabel ../core/TG2_multirecord_measure_tests.csv >> ../_review/vocabulary/bdqcore_term_versions.csv

# CSV files of test validation data

cp ../core/TG2_test_validation_data.csv  ../_review/build/templates/guide/implementers/TG2_test_validation_data.csv 
cp ../core/TG2_test_validation_data_nonprintingchars.csv ../_review/build/templates/guide/implementers/TG2_test_validation_data_nonprintingchars.csv
