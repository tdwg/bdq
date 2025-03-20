Files in this folder are for submission of BDQ Core for review as proposal for a new TDWG.

The best place to begin to review the proposal is on the [BDQ Core landing page](https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md).

Summary of files in this directory: 

<pre>
├── build  Build scripts and templates to assemble pages.
│   ├── authors_configuration.yaml  List of authors and contributors used by build scripts.
│   ├── README.md  Provides more details on build scripts and templates.
│   ├── .py files  Build other artifacts.
│   ├── draft_build-termlist.py  Builds the docs/{term}/index.md files and dist/{term}.xml files from templates, builds for draft standard.
│   ├── temp_namespaces.yaml  File for draft standard only, provides metadata for build scripts that comes from rs.tdwg.org for approved standards.
│   ├── temp_term-lists.csv  File for draft standard only, provides metadata for build scripts that comes from rs.tdwg.org for approved standards.
│   └── templates  Template files used by build scripts .
│       ├── intro Templates and configuration files for introduction page (docs/intro/index.md).
│       ├── supplement  Templates and configuration files for supplement page (docs/supplement/index.md).
│       ├── synthetic  Templates and configuration files for synthetic data page (docs/synthetic/index.md).
│       ├── vocabularies  Templates and configuration files for vocabularies landing page (docs/vocabularies/index.md).
│       ├── extension  Templates for vocabulary extension files, additional axioms added to vocabularies .
│       │   └── bdqffdq  Templates and configuration files for bdqffdq extension list (docs/extension/bdqenh/index.md).
│       ├── list  Templates for term list documents and dist rdf files.
│       │   ├── bdq  Templates and configuration files for bdq vocabulary (docs/list/bdq/index.md).
│       │   ├── bdqcore  Test documentation build files, work in progress (docs/list/bdqcore/index.md).
│       │   ├── bdqdim  Templates and configuration files for bdqdim vocabulary (docs/list/bdqdim/index.md).
│       │   ├── bdqcrit  Templates and configuration files for bdqcrit vocabulary (docs/list/bdqcrit/index.md).
│       │   └── bdqenh  Templates and configuration files for bdqenh vocabulary (docs/list/bdqenh/index.md).
│       ├── terms  Templates for Quick Reference Guide.
│       │   └── bdqcore_qrg  Quick Reference Guide build files (for docs/terms/bdqcore/index.md).
│       ├── bdqffdq  Ontology landing page build files (for docs/bdqffdq/index.md).
│       ├── bdqcore  TODO: Test landing page build files (for docs/bdqcore/index.md).
│       └── guide  Templates for guides (Users, Implementors, BDQFFDQ).
│           ├── bdqffdq  Source files for BDQFFDQ Guide (docs/guide/bdqffdq/index.md).
│           ├── implementers  Source files for Implementers Guide (docs/guide/implementers/index.md).
│           └── users  Source files for Users Guide (docs/guide/implemeters/index.md).
├── dist  Generated CSV distribution files for building other artifacts.
│   ├── bdq.xml  Generated RDF for bdq vocabulary (built with draft_build-termlist.py).
│   ├── bdqdim.xml  Generated RDF for bdqdim vocabulary (built with draft_build-termlist.py).
│   ├── bdqenh.xml  Generated RDF for bdqenh vocabulary (built with draft_build-termlist.py).
│   ├── bdqcrit.xml  Generated RDF for bdqcrit vocabulary (built with draft_build-termlist.py).
│   ├── bdqcore.xml  RDF/XML serialization of rdf representation of test descriptions, built by kurator-ffdq from bdq/tg2/core/TG2_tests.csv as bdq/tg2/core/TG2_tests.xml.
│   ├── bdqcore.ttl  Turtle serialization of rdf representation of test descriptions, built by kurator-ffdq from bdq/tg2/core/TG2_tests.csv as bdq/tg2/core/TG2_tests.ttl.
│   ├── bdqcore_singlerecord_tests_current.csv  CSV list of current bdqcore SingleRecord tests, for the convenience of implementers.
│   └── bdqcore_tests_vertical.csv  List of test label, prefLabel, and fully qualified name.
├── docs  Human-readable documentation files built from files in build directory.
│   ├── intro  Generated Introduction to the standard.
│   │   ├── index.md  Generated file. **Do not edit.**
│   │   └── *.svg  files copied here from build. **Do not edit.**
│   ├── bdqcore  Landing page for bdqcore, with normative statements.
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── bdqffdq  Landing page for bdqffdq, with normative statements.
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── vocabularies
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── terms  Build targets for Quick reference guides. **Do not edit.**
│   │   └── bdqcore
│   ├── list  Build targets for Human readable term list documents. **Do not edit.**
│   │   ├── bdq
│   │   │   └── index.md  Generated term list document. **Do not edit.**
│   │   ├── bdqcore
│   │   │   └── index.md  (work in progress) Generated term list document. **Do not edit.**
│   │   ├── bdqcrit
│   │   │   └── index.md  Generated term list document. **Do not edit.**
│   │   ├── bdqdim
│   │   │   └── index.md  Generated term list document. **Do not edit.**
│   │   ├── bdqenh
│   │   │   └── index.md  Generated term list document. **Do not edit.**
│   │   └── bdqffdq
│   │   │   └── index.md  Generated term list document. **Do not edit.**
│   ├── extension  Build targets for Human readable vocabulary extension documents. **Do not edit.**
│   │   └── bdqffdq
│   │       └── index.md  Generated extension document. **Do not edit.**
│   ├── guide  Descriptive document build targets. **Do not edit.**
│   │   ├── bdqffdq 
│   │   │   ├── *.svg and *.png  files copied here from build. **Do not edit.**
│   │   │   └── index.md  Generated file. **Do not edit.**
│   │   ├── implementers
│   │   │   └── index.md  Generated file. **Do not edit.**
│   │   └── users
│   │       └── index.md  Generated file. **Do not edit.**
│   ├── synthetic
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── maintenance
│   │   └── index.md  Suggestions for maintenance group. **editable.**
│   ├── references
│   │   └── index.md  Generated file. **Do not edit. NOTE: Moved to build/references.md.**
│   └── supplement
│       └── index.md  Generated file. **Do not edit.**
├── index.md  Landing page for the standard. **editable**
├── README.md  This file. **editable**
└── vocabulary  Should just be the term version files, but not all as term version files yet.
    ├── bdq_term_versions.csv  Term version file for bdq vocabulary. **editable**
    ├── bdqdim_term_versions.csv  Term version file for bdqdim vocabulary. **editable**
    ├── bdqenh_term_versions.csv  Term version file for bdqenh vocabulary. **editable**
    ├── bdqcrit_term_versions.csv  Term version file for bdqcrit vocabulary. **editable**
    ├── bdqcore_term_versions.csv  Term version file for bdqcore vocabulary. Copied from tg2/core/TG2_tests.csv, with multirecord measures appended.
    └── bdqffdq.owl  Probably goes in dist with no csv file here.
</pre>
