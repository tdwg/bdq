# Build Files for the BDQ standard
 
This directory contains build files to generate files that constitute the proposed BDQ standard.

Editable master copies of templates for human readable vocabulary lists and human readable documentation live here.

README.md  This file.
[**authors_configuration.yaml**](authors_configuration.yaml) Configuration file for the list of authors and contributors.
[**draft_build_bdqtest_qrg.py**](draft_build_bdqtest_qrg.py) Script to build the BDQ Tests Quick Reference Guide.
[**draft_build_bdqffdq.py**](draft_build_bdqffdq.py) Script to build markdown documents for the BDQFFDQ Framework Ontology from the OWL ontology.
[**draft_build-docs.py**](draft_build-docs.py) Script to fill in template information and copy files that don't include terms from build/templates to docs/.
[**draft_build-termlist_bdqtest.py**](draft_build-termlist_bdqtest.py) Script to build bdqtest termlist for docs/list/ from templates, needs more complete input list,  draft refers to this being to build a draft standard.
[**draft_build-termlist.py**](draft_build-termlist.py) Script to build termlist files for docs/list/ from templates (plus RDF for dist/), draft refers to this being to build a draft standard.
[**function_lib.py**](function_lib.py) Shared functions reused across build scripts.
[**make_bdq_tests_vertical.py**](make_bdq_tests_vertical.py) Script to build an artifact containing a list of tests. ** NOTE: purpose unclear.**
[**temp_namespaces.yaml**](temp_namespaces.yaml) Configuration file used by draft_build-termlist.py to replace an rs.tdwg.org resource unavailable for a draft standard.
[**temp_term-lists.csv**](temp_term-lists.csv) CSV file used by draft_build-termlist.py to replace an rs.tdwg.org resource unavailable for a draft standard.
[**vocabulary_configuration.yaml**](vocabulary_configuration.yaml) Configuration file of key to terms used to describe terms in bdq, bdqdim, bdqenh, and bdqcrit.
[**templates/](templates/**) Documents used as templates to generate files for the standard.
