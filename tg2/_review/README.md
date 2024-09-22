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
│       └── bdqdim templates and configuration files for bdqdim 
├── dist Generated csv distribution files for building other artifacts
│   ├── bdq.xml  Generated RDF for bdq vocabulary (built with draft_build-termlist.py)
│   ├── bdqdim.xml  Generated RDF for bdqdim vocabulary (built with draft_build-termlist.py)
│   └── bdqcore_tests_vertical.csv  List of test label, prefLabel, and fully qualified name, purpose?
├── docs  human readable documentation files ultimately to be built from files in build
│   ├── intro 
│   ├── vocabularies
│   ├── terms  Build targets for Quick reference guides Do not edit here
│   │   └── bdqcore
│   ├── list  Build targets for Human readable term list documents Do not edit here
│   │   ├── bdq
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqcore
│   │   ├── bdqcrit
│   │   ├── bdqdim
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqenh
│   │   └── bdqffdq
│   ├── guide descriptive document build targets Do not edit here 
│   │   ├── bdqffdq  build target for bdqffdq guide
│   │   ├── implementers build target for implementors guide
│   │   └── users build target for users guide
│   ├── synthetic
│   │   └── index.md
│   ├── maintenance
│   │   └── index.md
│   ├── references
│   ├── supplement
└── vocabulary ?should this just be the term version files, or do the deriviative vocabulary csv, xml, owl files go here?
    ├── bdq_term_versions.csv Term version file for bdq vocabulary copied from tg2/vocabularies/bdq_vocabulary_terms.csv
    ├── bdqdim_term_versions.csv Term version file for bdq vocabulary copied from tg2/vocabularies/bdq_dim_terms.csv
    ├── {term}\_terms.csv files, pending conversion to term version files.  
    ├── .xml rdf/xml files for vocabularies that will ultimately be deriviatives of term-version files ** Copy updates to here, DO NOT EDIT HERE **
    └── .csv files for vocabularies that will ultimately be deriviatives of term-version files ** Copy updates to here, DO NOT EDIT HERE ** 
</pre>

