# Build Files for BDQ Core
 
This directory contains build files to generate files that constitute the proposed BDQ Core standard.

Editable master copies of templates for human readable vocabulary lists and human readable documentation live here.

<pre>
├── README.md  This file.
├── authors_configuration.yaml  Configuration file for the list of authors and contributors.
├── draft_build_bdqcore_qrg.py  Script to build the BDQCore Quick Reference Guide.
├── draft_build_bdqffdq.py  Script to build markdown documents for the BDQFFDQ Framework Ontology from the owl ontology.
├── draft_build-docs.py  Script to fill in template information and copy files that don't include terms from build/templates to docs/.
├── draft_build-termlist_bdqcore.py  Script to build bdqcore termlist for docs/list/ from templates, needs more complete input list,  draft refers to this being to build a draft standard.
├── draft_build-termlist.py  Script to build termlist files for docs/list/ from templates (plus rdf for dist/), draft refers to this being to build a draft standard.
├── function_lib.py  Shared functions reused across build scripts.
├── make_bdq_tests_vertical.py  Script to build an artifact containing a list of tests. ** NOTE: purpose unclear.**
├── references.md  The list of references for inclusion in other files.
├── temp_namespaces.yaml  Configuration file used by draft_build-termlist.py to replace an rs.tdwg.org resource unavailable for a draft standard.
├── temp_term-lists.csv  CSV file used by draft_build-termlist.py to replace an rs.tdwg.org resource unavailable for a draft standard.
├── vocabulary_configuration.yaml  Configuration file of key to terms used to describe terms in bdq, bdqdim, bdqenh, and bdqcrit.
└── templates  Templates for various docs files.
    ├── bdqcore  Templates to build the landing page for bdqcore.
    │   ├── bdqcore_landing-footer.md
    │   ├── bdqcore_landing-header.md  **Main text document for landing page.**
    │   └── document_configuration.yaml
    ├── bdqffdq  Templates used by draft_buid_bdqffdq.py to build landing page for bdqffdq /docs/bdqffdq/index.md.
    │   ├── bdqffdq_landing-footer.md
    │   ├── bdqffdq_landing-header.md  **Main text document for landing page. Includes mathematical forumulation.**
    │   ├── document_configuration.yaml
    │   └── vocabulary_configuration.yaml
    ├── extension  Templates used to produce /docs/extension/{term}/index.md vocabulary extension list files.
    │   └── bdqffdq  Files used by draft_build_bdqffdq.py to build docs/extension/bdqffdq/index.md extension list with additional axioms.
    │       ├── bdqffdq_extension-footer.md
    │       ├── bdqffdq_extension-header.md
    │       ├── document_configuration.yaml
    │       └── vocabulary_configuration.yaml
    ├── guide  Templates used by draft_build-docs.py to build docs/guide/ pages.
    │   ├── bdqffdq
    │   │   ├── assertions.png
    │   │   ├── bdqffdq_class_diagram.png
    │   │   ├── bdqffdq_data_quality_layers.svg
    │   │   ├── bdqffdq_data_quality_needs_amendment.svg
    │   │   ├── bdqffdq_data_quality_needs_measure.svg
    │   │   ├── bdqffdq_data_quality_needs_solutions_report_validation.svg
    │   │   ├── bdqffdq_data_quality_needs_validation.svg
    │   │   ├── bdqffdq-footer.md  **Main text document for the BDQFFDQ Guide.**
    │   │   ├── bdqffdq-header.md
    │   │   ├── dataqualityneeds.png
    │   │   ├── document_configuration.yaml
    │   │   └── resource_types.png
    │   ├── implementers
    │   │   ├── document_configuration.yaml
    │   │   ├── implementers-footer.md
    │   │   ├── implementers-header.md  **Main text document for the Implementer's Guide.**
    │   │   ├── TG2_test_validation_data_nonprintingchars.csv
    │   │   └── TG2_test_validation_data.csv
    │   └── users
    │       ├── document_configuration.yaml
    │       ├── users-footer.md
    │       └── users-header.md  **Main text document for the User's Guide**
    ├── intro  Templates used by draft_build-docs.py to build docs/intro/.
    │   ├── document_configuration.yaml
    │   ├── intro-footer.md
    │   ├── intro-header.md  **Main text document for the Introduction.**
    │   ├── workflow_single_iteration.svg
    │   └── workflow_two_iterations.svg
    ├── list  Term lists files that produce /docs/list/{term}/index.md and /dist/{term}.xml files using draft_build-termlist.py.
    │   ├── bdq  Templates that draft_build-termlist.py uses to build bdq terms list.
    │   │   ├── bdq_termlist-footer.md
    │   │   ├── bdq_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqcore  Templates that draft_build-termlist_bdqcore.py uses for build.
    │   │   ├── bdqcore_termlist-footer.md  
    │   │   ├── bdqcore_termlist-header.md
    │   │   ├── document_configuration.yaml
    │   │   └── vocabulary_configuration.yaml
    │   ├── bdqcrit  Templates that draft_build-termlist.py uses to build bdqcrit terms list.
    │   │   ├── bdqcrit_termlist-footer.md
    │   │   ├── bdqcrit_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqdim  Templates that draft_build-termlist.py uses to build bdqdim terms list.
    │   │   ├── bdqdim_termlist-footer.md
    │   │   ├── bdqdim_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqenh  Templates that draft_build-termlist.py uses to build bdqenh terms list.
    │   │   ├── bdqenh_termlist-footer.md
    │   │   ├── bdqenh_termlist-header.md
    │   │   └── document_configuration.yaml
    │   ├── bdqffdq  Templates that draft_build_bdqffdq.py uses for build.
    │   │   ├── bdqffdq_termlist-footer.md
    │   │   ├── bdqffdq_termlist-header.md
    │   │   └── document_configuration.yaml
    ├── references  Templates used by draft_build-docs.py to build docs/references/.
    │   ├── document_configuration.yaml
    │   ├── references-footer.md
    │   └── references-header.md  **NOTE: Bulk of content is in build/references.md above.**
    ├── supplement  Templates used by draft_build-docs.py to build docs/supplement/.
    │   ├── document_configuration.yaml
    │   ├── stufftogoplaces.md
    │   ├── supplement-footer.md
    │   └── supplement-header.md
    │   ├── TestsName.png    
    │   ├── TestsOther.png    
    │   ├── TestsSpace.png    
    │   ├── TestsTime.png    
    ├── synthetic  Templates used by draft_build-docs.py to build docs/synthetic/.
    │   ├── document_configuration.yaml
    │   ├── synthetic-footer.md
    │   └── synthetic-header.md
    ├── terms  Templates used to produce /docs/terms/{term}/index.md 
    │   └── bdqcore_qrg  Templates used by draft_build_bdqcore_qrg.py to build docs/terms/bdqcore/index.md Quick Reference Guide.
    │       ├── bdqcore_qrg_term_descriptions-header.md 
    │       ├── bdqcore_quickreference-footer.md
    │       ├── bdqcore_quickreference-header.md
    │       └── document_configuration.yaml
    └── vocabularies  Templates used by draft_build-docs.py to build docs/vocabularies/.
        ├── document_configuration.yaml
        ├── vocabularies-footer.md
        └── vocabularies-header.md
</pre>

