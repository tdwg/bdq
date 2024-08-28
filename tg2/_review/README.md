Files in this folder are for submission of BDQ Core for review for standard track in TDWG.

Start on the [BDQ Core](https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md) landing page.


Work in progress description of files in this directory: 

<pre>
├── build  build scripts and templates to assemble pages
│   ├── .md files are working files that are to become templates but are not yet
│   ├── .py files build other artifacts
│   └── templates template files used by build scripts
├── dist Generated csv distribution files for building other artifacts
│   └── bdqcore_tests_vertical.csv  List of test label, prefLabel, and fully qualified name, purpose?
├── docs  human readable documentation files ultimately to be built from files in build
│   ├── bdq
│   ├── bdqdim
│   ├── bdqffdq
│   ├── implementers
│   ├── intro
│   ├── list
│   ├── maintenance
│   ├── references
│   ├── supplement
│   ├── terms
│   ├── users
│   └── vocabularies
└── vocabulary ?should this just be the term version files, or do the deriviative vocabulary csv, xml, owl files go here?
    ├── .xml rdf/xml files for vocabularies that will ultimately be deriviatives of term-version files ** Copy updates to here, DO NOT EDIT HERE **
    ├── .csv files for vocabularies that will ultimately be deriviatives of term-version files ** Copy updates to here, DO NOT EDIT HERE ** 
    └── term_versions location for and proposed stubs for term-version files to which lines are only appended from which vocabulary artifacts will be built.
</pre>

