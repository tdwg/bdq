# Build Files for the BDQ standard
 
This directory contains build files to generate files that constitute the proposed BDQ standard.

These templates and build scripts generate markdown files in /tg2/_review/ which are then deployed to the bdq.tdwg.org website with a workflow defined in .github/workflow/pages.yml which uses the script and assets in /_site_resources/ to build the website and deploy to GitHub Pages, which the /CNAME file identifies as bdq.tdwg.org.

Some markers that affect how the build scripts process the template files are available and used in some of the files: 

- {toc} is replaced with a table of contents generated from the content of the term list.
- {authors} is replaced with a list of authors from the authors_configuration.yaml file.
- {version} and various other {key}s are replaced with values from an appropriate document_configuration.yaml file.
- <!--- NO LINK LINE ---> and <!--- NO LINK START ---> and <!--- NO LINK END ---> are used to mark sections of text where the _site_resources/ script invoked to deploy to html GitHub pages does not attempt to autolink bare http://example.org/ or https://example.org/ IRIs in the text.  This applies to all templates except for the Quick Reference Guide.
- <!--- START HIDE IN HTML ---> and <!--- END HIDE IN HTML ---> are used to mark sections of text of the template of the Quick Reference guide only that that are hidden in the html version of the documentation but visible in the markdown version.

Editable master copies of templates for human readable vocabulary lists and human readable documentation live here.

**Document metadata** (titles, abstracts, authors and contributors with their roles, licence, dates, versions) come from tdwg/rs.tdwg.org (branch `bdq`, `docs/docs.csv` and `docs/docs-authors.csv`; the landing page from `standards/standards.csv`), read by `function_lib.rs_document_metadata` and `rs_document_version`. Change them there, in the `documents` of a release `config.yaml` on branch `bdq-source`. The `document_configuration.yaml` files and `authors_configuration.yaml` here are fallbacks, used only for documents or values that rs.tdwg.org does not hold (such as the Quick Reference Guide's maintainer). See [Where the BDQ standard is maintained](../README.md#where-the-bdq-standard-is-maintained-sources-of-truth).

README.md  This file.
- [**authors_configuration.yaml**](authors_configuration.yaml) - Configuration file for the list of authors and contributors.
- [**draft_build_bdqtest_qrg.py**](draft_build_bdqtest_qrg.py) - Script to build the BDQ Tests Quick Reference Guide.
- [**draft_build_bdqffdq.py**](draft_build_bdqffdq.py) - Script to build markdown documents for the BDQFFDQ Framework Ontology from the OWL ontology.
- [**draft_build-docs.py**](draft_build-docs.py) - Script to fill in template information and copy files that don't include terms from build/templates to docs/.
- [**draft_build-termlist_bdqtest.py**](draft_build-termlist_bdqtest.py) - Script to build bdqtest: termlist for docs/list/ from templates, needs more complete input list, draft refers to this being to build a draft standard.
- [**draft_build-termlist.py**](draft_build-termlist.py) - Script to build termlist files for docs/list/ from templates (plus RDF for dist/), draft refers to this being to build a draft standard.
- [**function_lib.py**](function_lib.py) - Shared functions reused across build scripts.
- [**make_bdq_tests_vertical.py**](make_bdq_tests_vertical.py) - Script to build `dist/bdqtest_tests_vertical.csv`, a list of the Tests' labels, prefLabels, and fully qualified names, from bdqtest_term_versions.csv.
- [**draft_build_bdqtest_singlerecord_tests_current.py**](draft_build_bdqtest_singlerecord_tests_current.py) - Script to write a CSV of the current version of each SingleRecord Test from bdqtest_term_versions.csv.
- [**postprocess_autolink_terms.py**](postprocess_autolink_terms.py) - Script run after the builders to link qualified vocabulary terms (e.g. `bdqffdq:InformationElement`) and the first occurrence of glossary terms in the generated Markdown.
- [**draft_generate_normative_index.py**](draft_generate_normative_index.py) - Script to build `docs/normative_index.md`, an index of the normative sections of the documents, with a topical index from [normative_topics.yaml](normative_topics.yaml).
- [**generate_bdq_qrg_filtering.py**](generate_bdq_qrg_filtering.py) - Script to build the interactive HTML Quick Reference Guide, `docs/terms/bdqtest/index.html`.
- [**glossary_and_vocabulary_terms.csv**](glossary_and_vocabulary_terms.csv) - A reference list of the glossary and vocabulary terms with their namespaces; not read by the build scripts.
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
- [**build_bdqtest_rdf.py**](build_bdqtest_rdf.py) - Script to generate the three bdqtest RDF serializations (Turtle, RDF/XML, JSON-LD) from the bdqtest_term_versions.csv term-version file and associated GUID mapping files. Python replacement for the kurator-ffdq / test-util.sh Java-based workflow. Since 2026-11-14 it is not used by the build: `dist/bdqtest.*` is generated from rs.tdwg.org by `_make_review/export_rs_baseline.py`, with rs.tdwg.org's Test-graph builder (`process/bdq-revisions/bdqtest_rdf.py`).
- [**compare_bdqtest_rdf.py**](compare_bdqtest_rdf.py) - Validation harness that compares generated bdqtest RDF outputs against baseline files in `tg2/_review/dist/`, reporting byte equality (informational) and graph isomorphism (authoritative pass/fail).
- [**tools/**](tools/) - Directory for tools used for quality control of the BDQ documentation; see [tools/README.md](tools/README.md).

The directory structure of the templates is as follows, with the files listed in each directory:

    templates/
    ├── bdqffdq
    │   ├── bdqffdq_landing-footer.md
    │   ├── bdqffdq_landing-header.md
    │   ├── document_configuration.yaml
    │   └── vocabulary_configuration.yaml
    ├── extension
    │   └── bdqffdq
    │       ├── bdqffdq_extension-footer.md
    │       ├── bdqffdq_extension-header.md
    │       ├── document_configuration.yaml
    │       └── vocabulary_configuration.yaml
    ├── guide
    │   ├── bdqffdq
    │   │   ├── assertions.png
    │   │   ├── bdqffdq-footer.md
    │   │   ├── bdqffdq-header.md
    │   │   ├── bdqffdq_class_diagram.png
    │   │   ├── bdqffdq_class_diagram_1_main.png
    │   │   ├── bdqffdq_class_diagram_2_horizontal.png
    │   │   ├── bdqffdq_data_quality_layers.svg
    │   │   ├── bdqffdq_data_quality_needs_amendment.svg
    │   │   ├── bdqffdq_data_quality_needs_measure.svg
    │   │   ├── bdqffdq_data_quality_needs_solutions_report_validation.svg
    │   │   ├── bdqffdq_data_quality_needs_validation.svg
    │   │   ├── dataqualityneeds.png
    │   │   ├── document_configuration.yaml
    │   │   └── resource_types.png
    │   ├── bdqtest
    │   │   ├── bdqtest-footer.md
    │   │   ├── bdqtest-header.md
    │   │   ├── document_configuration.yaml
    │   │   ├── workflow_single_iteration.svg
    │   │   └── workflow_two_iterations.svg
    │   ├── implementers
    │   │   ├── bdqffdq_overview_diagram.svg
    │   │   ├── document_configuration.yaml
    │   │   ├── implementers-footer.md
    │   │   ├── implementers-header.md
    │   │   ├── TG2_test_validation_data.csv
    │   │   ├── TG2_test_validation_data_nonprintingchars.csv
    │   │   └── validation_actedupon_cell_red.png
    │   ├── synthetic
    │   │   ├── document_configuration.yaml
    │   │   ├── synthetic-footer.md
    │   │   └── synthetic-header.md
    │   └── users
    │       ├── document_configuration.yaml
    │       ├── users-footer.md
    │       └── users-header.md
    ├── list
    │   ├── bdqcrit
    │   │   ├── bdqcrit_termlist-footer.md
    │   │   ├── bdqcrit_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqdim
    │   │   ├── bdqdim_termlist-footer.md
    │   │   ├── bdqdim_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqenh
    │   │   ├── bdqenh_termlist-footer.md
    │   │   ├── bdqenh_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqffdq
    │   │   ├── bdqffdq_termlist-footer.md
    │   │   ├── bdqffdq_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqtest
    │   │   ├── bdqtest_termlist-footer.md
    │   │   ├── bdqtest_termlist-header.md
    │   │   ├── document_configuration.yaml
    │   │   └── vocabulary_configuration.yaml
    │   ├── bdquc
    │   │   ├── bdquc_termlist-footer.md
    │   │   ├── bdquc_termlist-header.md
    │   │   └── document_configuration.yaml
    │   └── bdqval
    │       ├── bdqval_termlist-footer.md
    │       ├── bdqval_termlist-header.md
    │       └── document_configuration.yaml
    ├── standard_landing
    │   ├── document_configuration.yaml
    │   ├── overview_diagram.svg
    │   ├── overview_diagram_use_organized.svg
    │   ├── standard_landing-footer.md
    │   └── standard_landing-header.md
    ├── supplement
    │   ├── document_configuration.yaml
    │   ├── supplement-footer.md
    │   ├── supplement-header.md
    │   ├── TestsName.png
    │   ├── TestsOther.png
    │   ├── TestsSpace.png
    │   └── TestsTime.png
    ├── terms
    │   └── bdqtest_qrg
    │       ├── bdqtest_qrg_term_descriptions-header.md
    │       ├── bdqtest_quickreference-footer.md
    │       ├── bdqtest_quickreference-header.md
    │       └── document_configuration.yaml
    └── tutorial
        ├── document_configuration.yaml
        ├── tutorial-footer.md
        └── tutorial-header.md
