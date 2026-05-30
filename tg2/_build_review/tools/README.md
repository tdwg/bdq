# Utiity scriipts for quality control of the BDQ build files

## Scripts to check the bdqtest: source files

* check_citation_guids_resolve.sh - check whether citation GUID URLs have a live landing page

`bash check_citation_guids_resolve.sh -h` for usage instructions

## Scripts to check the bdqtest: RDF representations

* bdq_usecase_test_labels_Version4.py List BDQ Tests by Use Case from bdqtest.ttl, excluding `MultiRecord` `Measures`

`python3 bdq_usecase_test_labels_Version4.py -h` for usage instructions

* validate_sparql_in_templates.py - check whether SPARQL queries in templates are valid and return results when executed against the bdqtest RDF data. **Must Pass for Build to Succeed**

`python3 validate_sparql_in_templates.py -h` for usage instructions

* audit_bdqffdq_vs_bdqtest.py - compare the BDQ FFDQ and BDQ Test RDF files to identify differences in use cases, tests, and information elements.  **Must Pass for Build to Succeed**

```
python3 audit_bdqffdq_vs_bdqtest.py --owl ../_review/vocabulary/bdqffdq.owl --ttl ../_review/dist/bdqtest.ttl
```

* audit_bdqtest_vocab_usage.py - analyze the usage of vocabulary terms in the BDQ Test RDF file to identify any inconsistencies or missing terms. **Must Pass for Build to Succeed**

```
python3 tools/audit_bdqtest_vocab_usage.py --bdqtest _review/dist/bdqtest.ttl --bdqval _review/dist/bdqval.xml --bdqcrit _review/dist/bdqcrit.xml --bdqdim _review/dist/bdqdim.xml --bdqenh _review/dist/bdqenh.xml
```

* find_current_tests_in_csv_missing_from_rdf.py - compare the list of tests in the current CSV file with the tests represented in the RDF data to identify any missing tests.

## Scripts to check templates and assembled documents

* check_template_relative_links_Version13.py - check whether relative links in templates correctly produce links to anchors in generated documents.

`python3 check_template_relative_links_Version13.py -h` for usage instructions

* scan_bdq_templates_term_reference_sections_v15_Version3.sh - scan the templates for consistency in sections 1.7 Referring to Terms and 2 Use of Terms.

`bash scan_bdq_templates_term_reference_sections_v15_Version3.sh` to execute, expects to run from this directory.

* grep_for_spelling.sh - scan the templates for common misspellings and typos.

## Query the RDF data to generate lists of use cases, tests, and information elements

* list_multirecord_measures_for_usecase_tests.py - list the `MultiRecord` `Measures` that are associated with each use case and test in the RDF data.
* list_unique_acted_upon_information_elements.py - list the unique `InformationElements` that are acted upon by `Tests` in the RDF data by use case.
* list_use_cases_and_tests_to_csv.py - generate a CSV file listing the use cases and tests represented in the RDF data, along with their associated information elements and other relevant details.

## Other scripts

* sync_usecase_in_bdqtest_term_versions.py 
* use_case_information_elements_value_requirement.py 

* temporary/ - a directory for working file that carry out some cleanup step not for long term use

