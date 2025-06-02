# Build Files for the BDQ standard
 
This directory contains build files to generate files that constitute the proposed BDQ standard.

Editable master copies of templates for human readable vocabulary lists and human readable documentation live here.

README.md  This file.
- [**authors_configuration.yaml**](authors_configuration.yaml) - Configuration file for the list of authors and contributors.
- [**draft_build_bdqtest_qrg.py**](draft_build_bdqtest_qrg.py) - Script to build the BDQ Tests Quick Reference Guide.
- [**draft_build_bdqffdq.py**](draft_build_bdqffdq.py) - Script to build markdown documents for the BDQFFDQ Framework Ontology from the OWL ontology.
- [**draft_build-docs.py**](draft_build-docs.py) - Script to fill in template information and copy files that don't include terms from build/templates to docs/.
- [**draft_build-termlist_bdqtest.py**](draft_build-termlist_bdqtest.py) - Script to build bdqtest: termlist for docs/list/ from templates, needs more complete input list, draft refers to this being to build a draft standard.
- [**draft_build-termlist.py**](draft_build-termlist.py) - Script to build termlist files for docs/list/ from templates (plus RDF for dist/), draft refers to this being to build a draft standard.
- [**function_lib.py**](function_lib.py) - Shared functions reused across build scripts.
- [**make_bdq_tests_vertical.py**](make_bdq_tests_vertical.py) - Script to build an artifact containing a list of tests. ** NOTE: purpose unclear.**
- [**temp_namespaces.yaml**](temp_namespaces.yaml) - Configuration file used by draft_build-termlist.py to replace an rs.tdwg.org resource unavailable for a draft standard.
- [**temp_term-lists.csv**](temp_term-lists.csv) - CSV file used by draft_build-termlist.py to replace an rs.tdwg.org resource unavailable for a draft standard.
- [**vocabulary_configuration.yaml**](vocabulary_configuration.yaml) - Configuration file of key to terms used to describe terms in bdq, bdqdim, bdqenh, and bdqcrit.
- [**templates/**](templates/) - Documents used as templates to generate files for the standard.
 - templates/ directories contain files in a directory structure matching the target build structure and each directory can contain:
   - {term}\_landing-header.md  A header and descriptive text content appended before content generated from a term list, contains markers such as {toc} that are replaced with content when a build script runs.
   - {term}\_landing-footer.md A standard short footer appended after content generated from a term list.
   - document_configuration.yaml Configuration file for the document, used to fill in template information.
   - vocabulary_configuration.yaml Configuration file for a key to terms used to describe terms in the document.
   - image and graphics files linked to in the generated document (and copied by the build script to a target directory).
 - templates/guide/implementers also contains the master copy of the test validation data files:
   - TG2_test_validation_data.csv and TG2_test_validation_data_nonprintingchars.csv 

The directory structure of the templates is as follows, with the files listed in each directory:

    templates/
    ├── bdqffdq
    │   ├── bdqffdq_landing-footer.md
    │   ├── bdqffdq_landing-header.md
    │   ├── document_configuration.yaml
    │   └── vocabulary_configuration.yaml
    ├── bdqtest
    │   ├── bdqtest_landing-footer.md
    │   ├── bdqtest_landing-header.md
    │   └── document_configuration.yaml
    ├── extension
    │   └── bdqffdq
    │       ├── bdqffdq_extension-footer.md
    │       ├── bdqffdq_extension-header.md
    │       ├── document_configuration.yaml
    │       └── vocabulary_configuration.yaml
    ├── guide
    │   ├── bdqffdq
    │   │   ├── assertions.png
    │   │   ├── bdqffdq_class_diagram.png
    │   │   ├── bdqffdq_data_quality_layers.svg
    │   │   ├── bdqffdq_data_quality_needs_amendment.svg
    │   │   ├── bdqffdq_data_quality_needs_measure.svg
    │   │   ├── bdqffdq_data_quality_needs_solutions_report_validation.svg
    │   │   ├── bdqffdq_data_quality_needs_validation.svg
    │   │   ├── bdqffdq-footer.md
    │   │   ├── bdqffdq-header.md
    │   │   ├── dataqualityneeds.png
    │   │   ├── document_configuration.yaml
    │   │   └── resource_types.png
    │   ├── implementers
    │   │   ├── document_configuration.yaml
    │   │   ├── implementers-footer.md
    │   │   ├── implementers-header.md
    │   │   ├── TG2_test_validation_data.csv
    │   │   └── TG2_test_validation_data_nonprintingchars.csv
    │   ├── synthetic
    │   │   ├── document_configuration.yaml
    │   │   ├── synthetic-footer.md
    │   │   └── synthetic-header.md
    │   └── users
    │       ├── document_configuration.yaml
    │       ├── users-footer.md
    │       └── users-header.md
    ├── list
    │   ├── bdq
    │   │   ├── bdq_termlist-footer.md
    │   │   ├── bdq_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqcrit
    │   │   ├── bdqcrit_termlist-footer.md
    │   │   ├── bdqcrit_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqdim
    │   │   ├── bdqdim_termlist-footer.md
    │   │   ├── bdqdim_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqenh
    │   │   ├── bdqenh_termlist-footer.md
    │   │   ├── bdqenh_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqffdq
    │   │   ├── bdqffdq_termlist-footer.md
    │   │   ├── bdqffdq_termlist-header.md
    │   │   └── document_configuration.yaml
    │   └── bdqtest
    │       ├── bdqtest_termlist-footer.md
    │       ├── bdqtest_termlist-header.md
    │       ├── document_configuration.yaml
    │       └── vocabulary_configuration.yaml
    ├── supplement
    │   ├── document_configuration.yaml
    │   ├── supplement-footer.md
    │   ├── supplement-header.md
    │   ├── TestsName.png
    │   ├── TestsOther.png
    │   ├── TestsSpace.png
    │   └── TestsTime.png
    └── terms
        └── bdqtest_qrg
            ├── bdqtest_qrg_term_descriptions-header.md
            ├── bdqtest_quickreference-footer.md
            ├── bdqtest_quickreference-header.md
            └── document_configuration.yaml
