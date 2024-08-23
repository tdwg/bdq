Directories for build scripts, templates, and generated files for generating artifacts for the draft biodiversity data quality standard.

Structure follows that of https://github.com/tdwg/dwc/  

```
├── build Templates and build scripts
│   ├── bdq_standard Templates for the standard
│	│   └── index_template.md
│   ├── testcsvtoquickref.py To generate core_tests_quick_reference.md from csv
│   ├── testcsvtodoc.py (Draft) To generate core_tests.md from csv
│   ├── testmeasurecsvtodoc.py (Draft) To generate core_multirecord_measure_tests.md from csv
│   └── build.py
├── dist Generated csv distribution files for building rdf representations.
│
├── docs Generated human readable documentation.
│   ├── core_tests_quick_reference.md Content of quickreference guide to all tests in the bdqcore: namespace.
│   ├── core_multirecord_measure_tests.md  (Draft) details of each core MultiRecord measure test.
│   └── core_tests.md  (Draft) details of each core SingleRecord test.
│
├── vocabulary Generated term history files.
│   ├── bdq_term_versions.csv
│   └── bdqffdq_term_versions.csv
│
├── Maintinance.md Suggestions for maintainers
└── README.md  This document
