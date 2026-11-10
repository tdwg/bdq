# Vocabulary term-version files for the BDQ standard

This directory contains the master canonical term-version CSV files from which the the vocabularies in the BDQ standard are generated. It also contains the master file for the Fitness For Use Framework Ontology, which is an OWL file (bdqffdq.owl), not a CSV term-version file.

These files will eventually be built on rs.tdwg.org rather than being maintained here.

**README.md**  This file.<br>
[**bdqval_term_versions.csv**](bdqval_term_versions.csv) Term version file for `bdqval:` supplemental vocabulary. **Editable.**<br>
[**bdqtest_term_versions.csv**](bdqtest_term_versions.csv) Term version file for `bdqtest:` Test descriptions vocabulary. **Editable.**<br>
[**bdqcrit_term_versions.csv**](bdqcrit_term_versions.csv) Term version file for `bdqcrit:` Criterion vocabulary. **Editable.**<br>
[**bdqdim_term_versions.csv**](bdqdim_term_versions.csv) Term version file for `bdqdim:` Dimension vocabulary. **Editable.**<br>
[**bdqenh_term_versions.csv**](bdqenh_term_versions.csv) Term version file for `bdqenh:` Enhancement vocabulary. **Editable.**<br>
[**bdqtest_term_versions.csv**](bdqtest_term_versions.csv) Term version file for `bdqtest:` Test descriptions vocabulary. **Editable.**<br>
[**bdqffdq.owl**](bdqffdq.owl) OWL Ontology for `bdqffdq:` terms (Turtle). **Generated, do not edit.** Since 2026-11-09 the ontology is built in rs.tdwg.org from the `bdqffdq` term list and its axioms file (inputs on the `bdq-source` branch, `process/bdq-revisions/`) by `process/build_ontology.py`; this file is a copy of [`../dist/bdqffdq.ttl`](../dist/bdqffdq.ttl), kept here because the build and the documents still refer to this path. Make changes to the inputs in rs.tdwg.org and regenerate (see `tg2/_make_review/deployment_rs_tdwg_org.md`, Section 9.5).

