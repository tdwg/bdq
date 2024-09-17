#!/bin/bash
# Shell Script to copy files from their authoritative locations in other parts of directory tree into the _review directory.
#
# Run from within the bdq/tg2/_make_review/ directory of a git checkout of the tdwg/bdq repository.

# bdqffdq files for the framework

cp ../vocabularies/bdqffdq.owl ../_review/vocabulary/bdqffdq.owl

# bdqdim and related vocabulary

cp ../vocabularies/bdqdim_terms.csv ../_review/vocabulary/bdqdim_terms.csv
cp ../vocabularies/bdqenh_terms.csv ../_review/vocabulary/bdqenh_terms.csv
cp ../vocabularies/bdqcrit_terms.csv ../_review/vocabulary/bdqcrit_terms.csv

cp ../vocabularies/bdq_vocabulary_terms.csv ../_review/vocabulary/bdq_terms.csv

# bdqcore files containing test descriptions

cp ../core/TG2_tests.csv ../_review/vocabulary/bdqcore_terms.csv
cp ../core/TG2_tests.xml ../_review/vocabulary/bdqcore_terms.xml

# CSV files of test validation data

cp ../core/TG2_test_validation_data.csv  ../_review/docs/implementers/TG2_test_validation_data.csv 
cp ../core/TG2_test_validation_data_nonprintingchars.csv ../_review/docs/implementers/TG2_test_validation_data_nonprintingchars.csv
