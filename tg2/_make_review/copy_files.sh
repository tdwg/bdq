#!/bin/bash
# Shell Script to copy files from their authoritative locations in other parts of directory tree into the _review directory.
#
# Run from within the bdq/tg2/_make_review/ directory of a git checkout of the tdwg/bdq repository.

# bdqffdq files for the framework

# bdqdim vocabulary

cp ../vocabularies/bdqdim_terms.csv ../_review/vocabulary/bdqdim_terms.csv

# bdqcore files containing test descriptions

cp ../core/TG2_tests.csv ../_review/vocabulary/bdqcore_terms.csv
cp ../core/TG2_tests.xml ../_review/vocabulary/bdqcore_terms.xml