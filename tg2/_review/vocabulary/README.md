# Vocabulary term-version files for the BDQ standard

This directory contains the term-version CSV files from which this repository's build generates the vocabulary documents and RDF of the BDQ standard, and the Fitness For Use Framework Ontology (bdqffdq.owl).

**As of 2026-11-13 these are not the source of truth.** The source of truth for all seven BDQ vocabularies is tdwg/rs.tdwg.org, branch `bdq-source`, `process/bdq-revisions/`, served at bdq-public-review.rs.tdwg.org (see [Where the BDQ standard is maintained](../../README.md#where-the-bdq-standard-is-maintained-sources-of-truth)). Make changes there first, in a new release; the CSV files here are copies the build still reads, and must be updated by hand to match until the build reads rs.tdwg.org (`tg2/_make_review/deployment_rs_tdwg_org.md`, Section 13). "Editable" below means only that.

**README.md**  This file.<br>
[**bdqval_term_versions.csv**](bdqval_term_versions.csv) Term version file for `bdqval:` supplemental vocabulary. **Editable.**<br>
[**bdqtest_term_versions.csv**](bdqtest_term_versions.csv) Term version file for `bdqtest:` Test descriptions vocabulary. **Editable.**<br>
[**bdqcrit_term_versions.csv**](bdqcrit_term_versions.csv) Term version file for `bdqcrit:` Criterion vocabulary. **Editable.**<br>
[**bdqdim_term_versions.csv**](bdqdim_term_versions.csv) Term version file for `bdqdim:` Dimension vocabulary. **Editable.**<br>
[**bdqenh_term_versions.csv**](bdqenh_term_versions.csv) Term version file for `bdqenh:` Enhancement vocabulary. **Editable.**<br>
[**bdqtest_term_versions.csv**](bdqtest_term_versions.csv) Term version file for `bdqtest:` Test descriptions vocabulary. **Editable.**<br>
[**bdqffdq.owl**](bdqffdq.owl) OWL Ontology for `bdqffdq:` terms (Turtle). **Generated, do not edit.** Since 2026-11-09 the ontology is built in rs.tdwg.org from the `bdqffdq` term list and its axioms file (inputs on the `bdq-source` branch, `process/bdq-revisions/`) by `process/build_ontology.py`; this file is a copy of [`../dist/bdqffdq.ttl`](../dist/bdqffdq.ttl), kept here because the build and the documents still refer to this path. Make changes to the inputs in rs.tdwg.org and regenerate (see `tg2/_make_review/deployment_rs_tdwg_org.md`, Section 9.5).

