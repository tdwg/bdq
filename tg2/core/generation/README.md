Directories for build scripts, templates, and generated files for generating artifacts for the draft biodiversity data quality standard.

Structure follows that of https://github.com/tdwg/dwc/  

```
├── build Templates and build scripts
│   ├── bdq_standard Templates for the standard
│	│   └── index_template.md
│   ├── testcsvtodoc.py To generate core_tests.md from csv
│   ├── testmeasurecsvtodoc.py To generate core_multirecord_measure_tests.md from csv
│   └── build.py
├── dist Generated csv distribution files for building rdf representations.
│
├── docs Generated human readable documentation.
│   ├── core_multirecord_measure_tests.md  Details of each core MultiRecord measure test.
│   └── core_tests.md  Details of each core SingleRecord test.
│
├── vocabulary Generated term history files.
│   ├── bdq_term_versions.csv
│   └── bdqffdq_term_versions.csv
│
└── README.md  This document
```
