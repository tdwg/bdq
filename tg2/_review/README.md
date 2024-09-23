Files in this folder are for submission of BDQ Core for review for standard track in TDWG.

Start on the [BDQ Core](https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md) landing page.


Work in progress description of files in this directory: 

<pre>
├── build  build scripts and templates to assemble pages
│   ├── authors_configuration.yaml list of authors and contributors used by build scripts
│   ├── .md files are working files that are to become templates but are not yet
│   ├── .py files build other artifacts
│   ├── draft_build-termlist.py builds the docs/{term}/index.md files and dist/{term}.xml files from templates, builds for draft standard
│   ├── temp_namespaces.yaml File for draft standard only, provides metadata for build scripts that comes from rs.tdwg.org for approved standards
│   ├── temp_term-lists.csv File for draft standard only, provides metadata for build scripts that comes from rs.tdwg.org for approved standards
│   └── templates template files used by build scripts 
│       ├── terms templates for term list documents and dist rdf files 
│       │   ├── bdq templates and configuration files for bdq vocabulary
│       │   ├── bdqdim templates and configuration files for bdqdim vocabulary
│       │   ├── bdqcrit templates and configuration files for bdqcrit vocabulary
│       │   └── bdqenh templates and configuration files for bdqenh vocabulary
│       ├── bdqffdq ontology documentation build files, work in progress
│       ├── bdqcore test documentation build files, work in progress
│       ├── bdqcore_qrg quick reference guide build files (for docs/terms/bdqcore), work in progress
│       └── guide directory for templates for guides (users, implementors, bdqffdq).
│           ├── bdqffdq  source files for bdqffdq guide
│           ├── implementers source files for implementers guide
│           └── users source files for users guide.
├── dist Generated csv distribution files for building other artifacts
│   ├── bdq.xml  Generated RDF for bdq vocabulary (built with draft_build-termlist.py)
│   ├── bdqdim.xml  Generated RDF for bdqdim vocabulary (built with draft_build-termlist.py)
│   ├── bdqenh.xml  Generated RDF for bdqenh vocabulary (built with draft_build-termlist.py)
│   ├── bdqcrit.xml  Generated RDF for bdqcrit vocabulary (built with draft_build-termlist.py)
│   └── bdqcore_tests_vertical.csv  List of test label, prefLabel, and fully qualified name, purpose?
├── docs  human readable documentation files built from files in build/
│   ├── intro 
│   │   ├── .svg files, copied here from build, do not edit. 
│   │   └── index.md Generated file, do not edit..
│   ├── vocabularies
│   │   └── index.md Generated file, do not edit.
│   ├── terms  Build targets for Quick reference guides Do not edit here
│   │   └── bdqcore
│   ├── list  Build targets for Human readable term list documents Do not edit here
│   │   ├── bdq
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqcore
│   │   ├── bdqcrit
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqdim
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqenh
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   └── bdqffdq
│   ├── guide descriptive document build targets Do not edit here 
│   │   ├── bdqffdq 
│   │   │   ├── various .svg and png files, copied here from build, do not edit. 
│   │   │   └── index.md Generated file, do not edit..
│   │   ├── implementers
│   │   │   └── index.md Generated file, do not edit..
│   │   └── users
│   │       └── index.md Generated file, do not edit..
│   ├── synthetic
│   │   └── index.md Generated file, do not edit.
│   ├── maintenance
│   │   └── index.md
│   ├── references
│   └── supplement
│       └── index.md Generated file, do not edit.
└── vocabulary ?should this just be the term version files, or do the deriviative vocabulary csv, xml, owl files go here?
    ├── bdq_term_versions.csv Term version file for bdq vocabulary copied from tg2/vocabularies/bdq_vocabulary_terms.csv
    ├── bdqdim_term_versions.csv Term version file for bdq vocabulary copied from tg2/vocabularies/bdqdim_terms.csv
    ├── bdqenh_term_versions.csv Term version file for bdq vocabulary copied from tg2/vocabularies/bdqenh_terms.csv
    ├── bdqcrit_term_versions.csv Term version file for bdq vocabulary copied from tg2/vocabularies/bdqcrit_terms.csv
    ├── {term}\_terms.csv files, pending conversion to term version files.  
    ├── .xml rdf/xml files for vocabularies that will ultimately be deriviatives of term-version files ** Copy updates to here, DO NOT EDIT HERE **
    └── .csv files for vocabularies that will ultimately be deriviatives of term-version files ** Copy updates to here, DO NOT EDIT HERE ** 
</pre>

