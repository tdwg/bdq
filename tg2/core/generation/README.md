Directories for build scripts, templates, and generated files for generating artifacts for the draft biodiversity data quality standard.

Structure follows that of https://github.com/tdwg/dwc/  

```
├── build Templates and build scripts
│   ├── bdq_standard Templates for the standard (early draft, deprecated, to remove) 
│	│   └── index_template.md (to remove)
│   ├── bdqdim draft experimental build files for bdqdim vocabulary
│   │   ├── build-termlist.py Modified copy of darwin core term list build file that uses local files instead of rs.tdwg.org
│   │   ├── document_configuration.yaml configuration file for bdqdim vocabulary 
│   │   ├── temp_namespaces.yaml local file to replace namespace file from rs.tdwg.org (for approved standards) 
│   │   ├── temp_term-lists.csv local file to replace term-lists file from rs.tdwg.org (for approved standards)
│   │   ├── bdqdim_termlist-header.md **copy** of header file from _review/build
│	│   └── bdqdim_termlist-footer.md **copy** of footer file from _review/build/
│   ├── testcsvtoquickref.py To generate core_tests_quick_reference.md from csv
│   ├── testcsvtodoc.py (Draft) To generate core_tests.md from csv
│   ├── testmeasurecsvtodoc.py (Draft) To generate core_multirecord_measure_tests.md from csv
│   ├── authors_configuration.yaml **copy** of authors_configuration file from _review/build/
│   └── build.py
├── dist Generated csv distribution files for building rdf representations.
│
├── docs Generated human readable documentation.
│   ├── core_tests_quick_reference.md Content of quickreference guide to all tests in the bdqcore: namespace.
│   ├── core_multirecord_measure_tests.md  (Draft) details of each core MultiRecord measure test.
│   ├── bdqdim draft generated bdqdim list of terms document merging header and footer
│	│   └── index.md generated
│   └── core_tests.md  (Draft) details of each core SingleRecord test.
│
├── vocabulary Generated term history files.
│   ├── bdq_term_versions.csv
│   └── bdqffdq_term_versions.csv
│
├── Maintinance.md Suggestions for maintainers
└── README.md  This document
