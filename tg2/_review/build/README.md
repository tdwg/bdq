# Build Files for BDQ Core
 
This directory contains build files to generate the BDQ Core standard files for submission.

Editable master copies of templates for human readable vocabulary lists and human readable documentation live here.

<pre>
├── make_bdq_tests_vertical.py  builds an artifact containing a list of tests, purpose unclear.
├── README.md this file.
├── templates  for various docs files.
│   ├── list Term lists  files that produce /docs/list/{term}/index.md and /dist/{term}.xml files using draft_build-termlist.py
│   │   ├── bdqcore  **work in progress** uses draft_build-termlist_bdqcore.py for build
│   │   │   ├── bdqcore_termlist-footer.md  
│   │   │   ├── bdqcore_termlist-header.md
│   │   │   └── document_configuration.yaml
│   │   ├── bdq
│   │   │   ├── bdq_termlist-footer.md
│   │   │   ├── bdq_termlist-header.md
│   │   │   └── document_configuration.yaml
│   │   ├── bdqcrit
│   │   │   ├── bdqcrit_termlist-footer.md
│   │   │   ├── bdqcrit_termlist-header.md
│   │   │   └── document_configuration.yaml
│   │   ├── bdqdim
│   │   │   ├── bdqdim_termlist-footer.md
│   │   │   ├── bdqdim_termlist-header.md
│   │   │   └── document_configuration.yaml
│   │   └── bdqenh
│   │       ├── bdqenh_termlist-footer.md
│   │       ├── bdqenh_termlist-header.md
│   │       └── document_configuration.yaml
│   ├── extension  files that produce /docs/extension/{term}/index.md vocabulary extension list files
│   │   └── bdqffdq used by draft_build_bdqffdq.py to build docs/extension/bdqffdq/index.md extension list with additional axioms
│   │       ├── bdqffdq_extension-footer.md
│   │       ├── bdqffdq_extension-header.md
│   │       └── document_configuration.yaml
│   ├── terms  files that produce /docs/terms/{term}/index.md 
│   │   └── bdqcore_qrg to build docs/terms/bdqcore/index.md quick reference guide using draft_build_bdqcore_qrg.py
│   │       ├── document_configuration.yaml
│   │       ├── bdqcore_quickreference-footer.md
│   │       └── bdqcore_quickreference-header.md
│   ├── bdqffdq used by draft_buid_bdqffdq.py to produce landing page for bdqffdq /docs/bdqffdq/index.md
│   │   ├── document_configuration.yaml
│   │   ├── bdqffdq_landing-footer.md **Main text document for landing page**
│   │   └── bdqffdq_landing-header.md **Includes Mathematical Forumulation**
│   ├── bdqcore Landing pad page for bdqcore.
│   │   ├── document_configuration.yaml
│   │   ├── bdqcore_landing-footer.md **Main text document for landing page**
│   │   └── bdqcore_landing-header.md
│   ├── intro templates used by draft_build-docs.py to build docs/intro/
│   │   ├── document_configuration.yaml
│   │   ├── intro-footer.md
│   │   ├── intro-header.md
│   │   ├── workflow_single_iteration.svg
│   │   └── workflow_two_iterations.svg
│   ├── supplement templates used by draft_build-docs.py to build docs/supplement/
│   │   ├── document_configuration.yaml
│   │   ├── stufftogoplaces.md
│   │   ├── supplement-footer.md
│   │   └── supplement-header.md
│   ├── synthetic templates used by draft_build-docs.py to build docs/synthetic/
│   │   ├── document_configuration.yaml
│   │   ├── synthetic-footer.md
│   │   └── synthetic-header.md
│   ├── vocabularies templates used by draft_build-docs.py to build docs/vocabularies/
│   │   ├── document_configuration.yaml
│   │   ├── vocabularies-footer.md
│   │   └── vocabularies-header.md
│   └── guide used by draft_build-docs.py to build docs/guide/ pages
│       ├── bdqffdq
│       │   ├── document_configuration.yaml
│       │   ├── assertions.png
│       │   ├── bdqffdq_class_diagram.png
│       │   ├── bdqffdq_data_quality_layers.svg
│       │   ├── bdqffdq_data_quality_needs_amendment.svg
│       │   ├── bdqffdq_data_quality_needs_measure.svg
│       │   ├── bdqffdq_data_quality_needs_solutions_report_validation.svg
│       │   ├── bdqffdq_data_quality_needs_validation.svg
│       │   ├── dataqualityneeds.png
│       │   ├── bdqffdq-header.md  **Main text document for the bdqffdq guide**
│       │   ├── bdqffdq-footer.md
│       │   └── resource_types.png
│       ├── implementers
│       │   ├── document_configuration.yaml
│       │   ├── implementers-header.md **Main text document for the implementers guide**
│       │   ├── implementers-footer.md
│       │   ├── TG2_test_validation_data.csv
│       │   └── TG2_test_validation_data_nonprintingchars.csv
│       └── users
│           ├── document_configuration.yaml
│           ├── users-footer.md
│           └── users-header.md **Main text document for the users guide**
├── draft_build-termlist.py script to build termlist files for docs/list/ from templates (plus rdf for dist/), draft refers to this being to build a draft standard
├── draft_build-termlist_bdqcore.py script to build bdqcore termlist for docs/list/ from templates, needs more complete input list,  draft refers to this being to build a draft standard
├── draft_build-docs.py script to fill in template information and copy files that don't include terms from build/templates to docs/
├── draft_build_bdqcore_qrg.py to build bdqcore quick reference guide
├── authors_configuration.yaml  list of authors and contributors
├── temp_namespaces.yaml used by draft_build-termlist.py to replace a rs.tdwg.org resource unavailable for a draft standard
└── temp_term-lists.csv used by draft_build-termlist.py to replace a rs.tdwg.org resource unavailable for a draft standard
</pre>

