# Utiity scriipts for quality control of the BDQ build files

## Scripts to check the bdqtest: source files

* check_citation_guids_resolve.sh - check whether citation GUID URLs have a live landing page

`bash check_citation_guids_resolve.sh -h` for usage instructions

## Scripts to check the bdqtest: RDF representations

* bdq_usecase_test_labels_Version4.py List BDQ Tests by Use Case from bdqtest.ttl, excluding `MultiRecord` `Measures`

`python3 bdq_usecase_test_labels_Version4.py -h` for usage instructions

## Scripts to check templates and assembled documents

* check_template_relative_links_Version13.py - check whether relative links in templates correctly produce links to anchors in generated documents.
`python3 check_template_relative_links_Version13.py -h` for usage instructions

* scan_bdq_templates_term_reference_sections_v15_Version3.sh - scan the templates for consistency in sections 1.7 Referring to Terms and 2 Use of Terms.
`bash scan_bdq_templates_term_reference_sections_v15_Version3.sh` to execute, expects to run from this directory.
