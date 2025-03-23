Files in this folder are for submission of BDQ Core for review as proposal for a new TDWG.

The best place to begin to review the proposal is on the [BDQ Core landing page](https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md).

Summary of files in this directory: 

<pre>
├── build  Build scripts and templates to assemble pages.
│   ├── see [build/README.md](build/README.md)
├── dist  Generated CSV distribution files for building other artifacts.
│   ├── bdq.xml  Generated RDF for bdq vocabulary (built with draft_build-termlist.py).
│   ├── bdqcore_singlerecord_tests_current.csv  CSV list of current bdqcore SingleRecord tests, for the convenience of implementers.
│   ├── bdqcore_tests_vertical.csv  List of test label, prefLabel, and fully qualified name.
│   ├── bdqcore.json  JSON serialization of the RDF representation of test descriptions, built by kurator-ffdq from bdq/tg2/core/TG2_tests.csv as bdq/tg2/core/TG2_tests.ttl.
│   ├── bdqcore.ttl  Turtle serialization of the RDF representation of test descriptions, built by kurator-ffdq from bdq/tg2/core/TG2_tests.csv as bdq/tg2/core/TG2_tests.ttl.
│   ├── bdqcore.xml  RDF/XML serialization of the RDF representation of test descriptions, built by kurator-ffdq from bdq/tg2/core/TG2_tests.csv as bdq/tg2/core/TG2_tests.xml.
│   ├── bdqcrit.xml  Generated RDF for bdqcrit vocabulary (built with draft_build-termlist.py).
│   ├── bdqdim.xml  Generated RDF for bdqdim vocabulary (built with draft_build-termlist.py).
│   └── bdqenh.xml  Generated RDF for bdqenh vocabulary (built with draft_build-termlist.py).
├── docs  Human-readable documentation files built from files in build directory.
│   ├── bdqcore  Landing page for bdqcore, with normative statements.
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── bdqffdq  Landing page for bdqffdq, with normative statements.
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── extension  Build targets for Human readable vocabulary extension documents.
│   │   └── bdqffdq
│   │       └── index.md  Generated extension document. **Do not edit.**
│   ├── guide  Descriptive document build targets.
│   │   ├── bdqffdq 
│   │   │   ├── *.svg and *.png  Files copied here from build. **Do not edit.**
│   │   │   └── index.md  Generated file. **Do not edit.**
│   │   ├── implementers
│   │   │   ├── index.md  Generated file. **Do not edit.**
│   │   │   ├── TG2_test_validation_data_nonprintingchars.csv **Do not edit.**
│   │   │   └── TG2_test_validation_data.csv **Do not edit.**
│   │   └── users
│   │       └── index.md  Generated file. **Do not edit.**
│   ├── intro  Generated Introduction to the standard.
│   │   ├── index.md  Generated file. **Do not edit.**
│   │   └── *.svg  Files copied here from build. **Do not edit.**
│   ├── list  Build targets for Human readable term list documents. **Do not edit.**
│   │   ├── bdq
│   │   │   └── index.md  Generated bdq term list document. **Do not edit.**
│   │   ├── bdqcore
│   │   │   └── index.md  Generated bdqcore term list document. **Do not edit.**
│   │   ├── bdqcrit
│   │   │   └── index.md  Generated bdqcrit term list document. **Do not edit.**
│   │   ├── bdqdim
│   │   │   └── index.md  Generated bdqdim term list document. **Do not edit.**
│   │   ├── bdqenh
│   │   │   └── index.md  Generated bdqenh term list document. **Do not edit.**
│   │   └── bdqffdq
│   │       └── index.md  Generated bdqffdq term list document. **Do not edit.**
│   ├── maintenance
│   │   └── index.md  Suggestions for maintenance group. **Editable.**
│   ├── references
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── supplement
│   │   └── index.md  Generated file. **Do not edit.**
│   │   └── *.png  Files copied here from build. **Do not edit.**
│   ├── synthetic
│   │   └── index.md  Generated file. **Do not edit.**
│   ├── terms  Build targets for Quick Reference Guides.
│   │   └── bdqcore
│   │       ├── bdqcore_qrg_term_descriptions.md  Terms used in the Quick Reference Guide to BDQ Core Tests. **Editable.**
│   │       ├── index.md  Generated file. **Do not edit.**
│   │       ├── qrg_index_by_dimension.md  Generated file. **Do not edit.**
│   │       ├── qrg_index_by_ie_actedupon.md  Generated file. **Do not edit.**
│   │       ├── qrg_index_by_ie_class.md  Generated file. **Do not edit.**
│   │       ├── qrg_index_by_usecase.md  Generated file. **Do not edit.**
│   │       └── qrg_multirecord_index.md  Generated file. **Do not edit.**
│   ├── vocabularies
│       └── index.md  Generated file. **Do not edit.**
├── index.md  Landing page for the standard. **Editable.**
├── README.md  This file. **Editable.**
└── vocabulary  Term version files for vocabularies.
    ├── see [vocabulary/README.md](vocabulary/README.md)
</pre>
