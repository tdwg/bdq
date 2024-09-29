#!/bin/bash
# Shell Script to copy files from their authoritative locations in other parts of directory tree into the _review directory.
#
# Run from within the bdq/tg2/_make_review/ directory of a git checkout of the tdwg/bdq repository.

# bdqffdq files for the framework

cp ../vocabularies/bdqffdq.owl ../_review/vocabulary/bdqffdq.owl

# bdq, bdqdim and related vocabulary

cp ../vocabularies/bdqdim_terms.csv ../_review/vocabulary/bdqdim_term_versions.csv
cp ../vocabularies/bdqenh_terms.csv ../_review/vocabulary/bdqenh_term_versions.csv
cp ../vocabularies/bdqcrit_terms.csv ../_review/vocabulary/bdqcrit_term_versions.csv

cp ../vocabularies/bdq_vocabulary_terms.csv ../_review/vocabulary/bdq_term_versions.csv

# bdqcore files containing test descriptions

cp ../core/TG2_tests.csv ../_review/vocabulary/bdqcore_terms.csv
cp ../core/TG2_tests.xml ../_review/dist/bdqcore.xml
cp ../core/TG2_tests.ttl ../_review/dist/bdqcore.ttl

# append multi-record measures to csv list of core tests
grep -v prefLabel ../core/TG2_multirecord_measure_tests.csv >> ../_review/vocabulary/bdqcore_terms.csv

# CSV files of test validation data

cp ../core/TG2_test_validation_data.csv  ../_review/build/templates/guide/implementers/TG2_test_validation_data.csv 
cp ../core/TG2_test_validation_data_nonprintingchars.csv ../_review/build/templates/guide/implementers/TG2_test_validation_data_nonprintingchars.csv
