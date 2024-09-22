# Build Files for BDQ Core
 
This directory contains build files to generate the BDQ Core standard files for submission.

Editable master copies of templates for human readable vocabulary lists and human readable documentation live here.

<pre>
├── make_bdq_tests_vertical.py
├── README.md
├── templates
│   ├── bdq for docs/terms/bdq 
│   │   ├── bdq_termlist-footer.md
│   │   ├── bdq_termlist-header.md
│   │   └── document_configuration.yaml
│   ├── bdqdim for docs/terms/bdqdim
│   │   ├── bdqdim_termlist-footer.md
│   │   ├── bdqdim_termlist-header.md
│   │   └── document_configuration.yaml
│   ├── bdqcore  work in progress
│   │   ├── bdqcore_termlist-footer.md
│   │   └── bdqcore_termlist-header.md
│   ├── bdqcore_qrg  work in progress  to build docs/terms/bdqcore/index.md quick reference guide.
│   │   ├── bdqcore_quickreference-footer.md
│   │   └── bdqcore_quickreference-header.md
│   ├── bdqcrit work in progress
│   │   └── bdqcrit_termlist-header.md
│   ├── bdqenh work in progress
│   │   └── bdqenh_termlist-header.md
│   ├── bdqffdq work in progress
│   │   ├── bdqffdq_termlist-footer.md
│   │   └── bdqffdq_termlist-header.md
│   └── guide to build docs/guide/ pages
│       ├── bdqffdq
│       │   ├── assertions.png
│       │   ├── bdqffdq_class_diagram.png
│       │   ├── bdqffdq_data_quality_layers.svg
│       │   ├── bdqffdq_data_quality_needs_amendment.svg
│       │   ├── bdqffdq_data_quality_needs_measure.svg
│       │   ├── bdqffdq_data_quality_needs_solutions_report_validation.svg
│       │   ├── bdqffdq_data_quality_needs_validation.svg
│       │   ├── dataqualityneeds.png
│       │   ├── index.md
│       │   └── resource_types.png
│       ├── implementers
│       │   ├── index.md
│       │   ├── TG2_test_validation_data.csv
│       │   └── TG2_test_validation_data_nonprintingchars.csv
│       └── users
│           └── index.md
├── draft_build-termlist.py script to build termlist files for docs/list/ from templates (plus rdf for dist/), draft refers to this being to build a draft standard
├── authors_configuration.yaml  list of authors and contributors
├── temp_namespaces.yaml used by draft_build-termlist.py to replace a rs.tdwg.org resource unavailable for a draft standard
└── temp_term-lists.csv used by draft_build-termlist.py to replace a rs.tdwg.org resource unavailable for a draft standard
</pre>

