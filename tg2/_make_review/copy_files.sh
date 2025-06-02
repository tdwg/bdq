#!/bin/bash
# Shell Script to copy files from their authoritative locations in other parts of directory tree into the _review directory.
#
# Run from within the bdq/tg2/_make_review/ directory of a git checkout of the tdwg/bdq repository.

# NOTE: CORE tests are no longer maintained from the Markdown tables in the github issues.
# Current master files for the tests are: ../core/TG2_tests.csv and  ../core/TG2_multirecord_measure_tests.csv 

# bdqtest files containing test descriptions

# The file ../_review/vocabulary/bdqtest_term_versions.csv is now the canonical version
# of all test descriptions.
cp ../core/TG2_tests.csv ../_review/vocabulary/bdqtest_term_versions.csv

# TODO: replace the next step with invocation of:
# draft_build_bdqtest_singlerecord_tests_current.py
cp ../core/TG2_tests.csv ../_review/dist/bdqtest_singlerecord_tests_current.csv

# Replace these steps with creation of these files with kurator-ffdq below
# cp ../core/TG2_tests.xml ../_review/dist/bdqtest.xml
# cp ../core/TG2_tests.ttl ../_review/dist/bdqtest.ttl
# cp ../core/TG2_tests.json ../_review/dist/bdqtest.json

# TODO: The above term-versions file will become the master copy, and include the multi-record measures.
# append multi-record measures to csv list of core tests
grep -v prefLabel ../core/TG2_multirecord_measure_tests.csv >> ../_review/vocabulary/bdqtest_term_versions.csv
grep -v SingleRecord ../_review/vocabulary/bdqtest_term_versions.csv > ../_review/dist/bdqtest_multirecord_tests_current.csv

# CSV files of test validation data

# The copies in ../_build_review/templates/guide/implementers/ are now the canonical 
# versions.
#cp ../core/TG2_test_validation_data.csv  ../_build_review/templates/guide/implementers/TG2_test_validation_data.csv 
#cp ../core/TG2_test_validation_data_nonprintingchars.csv ../_build_review/templates/guide/implementers/TG2_test_validation_data_nonprintingchars.csv

# Assuming that bdq/tg2/_make_review/ is at the same level as kurator-ffdq/ (e.g. in a ~/git/ directory)
# move up to the shared (e.g. ~/git/) directory
cd ../../../
# moved down into kurator-ffdq/ directory
cd kurator-ffdq/
# copy tests into the kurator-ffdq data directory from the bdq project
grep -v "AllAmendmentTestsRunOnSingleRecord" ../bdq/tg2/_review/vocabulary/bdqtest_term_versions.csv  | grep -v "AllDarwin" > data/TG2_tests.csv
# to build rdf files with just the single record tests, copy just those into the kurator-ffdq data directory
#grep -v "AllAmendmentTestsRunOnSingleRecord" ../bdq/tg2/core/TG2_tests.csv  | grep -v "AllDarwin" > data/TG2_tests.csv
# run test-util.sh to generate various RDF serializations of the tests.
./test-util.sh -config data/tg2_tests.properties -format RDFXML -out ../bdq/tg2/_review/dist/bdqtest.xml -in  data/TG2_tests.csv -guidFile ../bdq/tg2/core/TG2_tests_additional_guids.csv -useCaseFile ../bdq/tg2/core/usecase_test_list.csv -ieGuidFile ../bdq/tg2/core/information_element_guids.csv
./test-util.sh -config data/tg2_tests.properties -format TURTLE -out ../bdq/tg2/_review/dist/bdqtest.ttl -in  data/TG2_tests.csv -guidFile ../bdq/tg2/core/TG2_tests_additional_guids.csv -useCaseFile ../bdq/tg2/core/usecase_test_list.csv -ieGuidFile ../bdq/tg2/core/information_element_guids.csv
./test-util.sh -config data/tg2_tests.properties -format JSON-LD -out ../bdq/tg2/_review/dist/bdqtest.json -in  data/TG2_tests.csv -guidFile ../bdq/tg2/core/TG2_tests_additional_guids.csv -useCaseFile ../bdq/tg2/core/usecase_test_list.csv -ieGuidFile ../bdq/tg2/core/information_element_guids.csv
# to build separate RDF files for the multi-record measure tests copy the csv file with just those tests and execute kurator-ffdq on it
#cp ../bdq/tg2/core/TG2_multirecord_measure_tests.csv data/TG2_multirecord_measure_tests.csv
#./test-util.sh -config data/tg2_tests.properties -format RDFXML -out ../bdq/tg2/core/TG2_multirecord_measure_tests.xml -in  data/TG2_multirecord_measure_tests.csv -guidFile ../bdq/tg2/core/TG2_tests_additional_guids.csv -useCaseFile ../bdq/tg2/core/usecase_test_list.csv -ieGuidFile ../bdq/tg2/core/information_element_guids.csv
#./test-util.sh -config data/tg2_tests.properties -format TURTLE -out ../bdq/tg2/core/TG2_multirecord_measure_tests.ttl -in  data/TG2_multirecord_measure_tests.csv -guidFile ../bdq/tg2/core/TG2_tests_additional_guids.csv -useCaseFile ../bdq/tg2/core/usecase_test_list.csv -ieGuidFile ../bdq/tg2/core/information_element_guids.csv
