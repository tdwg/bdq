Files in this folder are for submission of BDQ Core for review for standard track in TDWG.

Start on the [BDQ Core](https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md) landing page.

Work in progress description of files in this directory: 

<pre>
├── index.md  Landing page for the standard. **editable**
├── build  build scripts and templates to assemble pages
│   ├── authors_configuration.yaml list of authors and contributors used by build scripts
│   ├── .md files are working files that are to become templates but are not yet
│   ├── .py files build other artifacts
│   ├── draft_build-termlist.py builds the docs/{term}/index.md files and dist/{term}.xml files from templates, builds for draft standard
│   ├── temp_namespaces.yaml File for draft standard only, provides metadata for build scripts that comes from rs.tdwg.org for approved standards
│   ├── temp_term-lists.csv File for draft standard only, provides metadata for build scripts that comes from rs.tdwg.org for approved standards
│   └── templates template files used by build scripts 
│       ├── intro templates and configuration files for introduction page (docs/intro/index.md)
│       ├── supplement templates and configuration files for supplement page (docs/supplement/index.md)
│       ├── synthetic templates and configuration files for synthetic data page (docs/synthetic/index.md)
│       ├── vocabularies templates and configuration files for vocabularies landing page (docs/vocabularies/index.md)
│       ├── list templates for term list documents and dist rdf files 
│       │   ├── bdq templates and configuration files for bdq vocabulary (docs/list/bdq/index.md)
│       │   ├── bdqcore test documentation build files, work in progress (docs/list/bdqcore/index.md)
│       │   ├── bdqdim templates and configuration files for bdqdim vocabulary (docs/list/bdqdim/index.md)
│       │   ├── bdqcrit templates and configuration files for bdqcrit vocabulary (docs/list/bdqcrit/index.md)
│       │   └── bdqenh templates and configuration files for bdqenh vocabulary (docs/list/bdqenh/index.md)
│       ├── terms templates for quick reference guide 
│       │   └── bdqcore_qrg quick reference guide build files (for docs/terms/bdqcore/index.md)
│       ├── bdqffdq ontology documentation build files, work in progress
│       └── guide directory for templates for guides (users, implementors, bdqffdq).
│           ├── bdqffdq  source files for bdqffdq guide (docs/guide/bdqffdq/index.md)
│           ├── implementers source files for implementers guide (docs/guide/implementers/index.md)
│           └── users source files for users guide. (docs/guide/implemeters/index.md)
├── dist Generated csv distribution files for building other artifacts
│   ├── bdq.xml  Generated RDF for bdq vocabulary (built with draft_build-termlist.py)
│   ├── bdqdim.xml  Generated RDF for bdqdim vocabulary (built with draft_build-termlist.py)
│   ├── bdqenh.xml  Generated RDF for bdqenh vocabulary (built with draft_build-termlist.py)
│   ├── bdqcrit.xml  Generated RDF for bdqcrit vocabulary (built with draft_build-termlist.py)
│   ├── bdqcore.xml rdf/xml serialization of rdf representation of test descriptions, built by kurator-ffdq from bdq/tg2/core/TG2_tests.csv as bdq/tg2/core/TG2_tests.xml
│   ├── bdqcore.ttl turtle serialization of rdf representation of test descriptions, built by kurator-ffdq from bdq/tg2/core/TG2_tests.csv as bdq/tg2/core/TG2_tests.ttl
│   └── bdqcore_tests_vertical.csv  List of test label, prefLabel, and fully qualified name, purpose?
├── docs  human readable documentation files built from files in build/
│   ├── intro 
│   │   ├── .svg files, copied here from build, do not edit. 
│   │   └── index.md Generated file, do not edit..
│   ├── vocabularies
│   │   └── index.md Generated file, do not edit.
│   ├── terms  Build targets for Quick reference guides Do not edit here
│   │   └── bdqcore
│   ├── list  Build targets for Human readable term list documents Do not edit here
│   │   ├── bdq
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqcore
│   │   │   └── index.md  (work in progress) Generated term list document Do not edit.
│   │   ├── bdqcrit
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqdim
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   ├── bdqenh
│   │   │   └── index.md  Generated term list document Do not edit.
│   │   └── bdqffdq
│   ├── guide descriptive document build targets Do not edit here 
│   │   ├── bdqffdq 
│   │   │   ├── various .svg and png files, copied here from build, do not edit. 
│   │   │   └── index.md Generated file, do not edit..
│   │   ├── implementers
│   │   │   └── index.md Generated file, do not edit..
│   │   └── users
│   │       └── index.md Generated file, do not edit..
│   ├── synthetic
│   │   └── index.md Generated file, do not edit.
│   ├── maintenance
│   │   └── index.md  suggestions for maintinance group, **editable.**
│   ├── references
│   │   └── index.md list of references, **editable.**
│   └── supplement
│       └── index.md Generated file, do not edit.
└── vocabulary should just be the term version files, but not all as term version files yet
    ├── bdq_term_versions.csv Term version file for bdq vocabulary **editable**
    ├── bdqdim_term_versions.csv Term version file for bdqdim vocabulary **editable**
    ├── bdqenh_term_versions.csv Term version file for bdqenh vocabulary **editable**
    ├── bdqcrit_term_versions.csv Term version file for bdqcrit vocabulary **editable**
    ├── bdqcore_terms.csv bdqcore tests as csv file, pending conversion to term version file, copied from tg2/core/TG2_tests.csv, with multirecord measures appended  
    └── bdqffdq.owl probably goes in dist with no csv file here
</pre>

