# Vocabulary term-version files for the BDQ standard

This directory contains the term-version CSV files of the seven BDQ vocabularies, from which this repository's build generates the vocabulary documents and RDF of the BDQ standard.

**These are not the source of truth.** The source of truth for all seven BDQ vocabularies is tdwg/rs.tdwg.org, branch `bdq-source`, `process/bdq-revisions/`, served at bdq-public-review.rs.tdwg.org (see [Where the BDQ standard is maintained](https://github.com/tdwg/bdq/blob/master/tg2/README.md#where-the-bdq-standard-is-maintained-sources-of-truth)). Every file here is a copy exported from rs.tdwg.org, in the published BDQ column names, by `tg2/_make_review/export_rs_baseline.py`, which records the rs.tdwg.org commit exported in [`tg2/_make_review/rs_tdwg_org_baseline.json`](https://github.com/tdwg/bdq/blob/master/tg2/_make_review/rs_tdwg_org_baseline.json) (`tg2/_make_review/deployment_rs_tdwg_org.md`, Section 13.1). Make changes in rs.tdwg.org, in a new release, then export again. **Generated, do not edit.**

**README.md**  This file.<br>
[**bdqdim_term_versions.csv**](bdqdim_term_versions.csv) Term version file for the `bdqdim:` Dimension vocabulary.<br>
[**bdqenh_term_versions.csv**](bdqenh_term_versions.csv) Term version file for the `bdqenh:` Enhancement vocabulary.<br>
[**bdqcrit_term_versions.csv**](bdqcrit_term_versions.csv) Term version file for the `bdqcrit:` Criterion vocabulary.<br>
[**bdquc_term_versions.csv**](bdquc_term_versions.csv) Term version file for the `bdquc:` Use Case vocabulary.<br>
[**bdqval_term_versions.csv**](bdqval_term_versions.csv) Term version file for the `bdqval:` supplemental vocabulary.<br>
[**bdqffdq_term_versions.csv**](bdqffdq_term_versions.csv) Term version file for the `bdqffdq:` Fitness For Use Framework Ontology terms: the current version of each term, with its types, superclasses, superproperties, and named ranges. The axioms that need blank nodes are in the vocabulary extension term list, and the whole ontology is in `../dist/`: [`bdqffdq.ttl`](../dist/bdqffdq.ttl) (Turtle), [`bdqffdq.owl`](../dist/bdqffdq.owl) and [`bdqffdq.rdf`](../dist/bdqffdq.rdf) (RDF/XML), and [`bdqffdq.jsonld`](../dist/bdqffdq.jsonld) (JSON-LD), generated in rs.tdwg.org by `process/build_ontology.py` (`tg2/_make_review/deployment_rs_tdwg_org.md`, Section 9.5).<br>
[**bdqtest_term_versions.csv**](bdqtest_term_versions.csv) Term version file for the `bdqtest:` Test descriptions vocabulary.<br>
[**rs_tdwg_org_baseline.json**](https://github.com/tdwg/bdq/blob/master/tg2/_make_review/rs_tdwg_org_baseline.json) (in `tg2/_make_review/`, as build information that is not part of the published standard) Provenance of the files above and of the generated files in `../dist/` and `tg2/core/`: the rs.tdwg.org repository, ref, and commit they were exported from, and a checksum of each file.

The ontology was kept here as `bdqffdq.owl` until 2026-11-15; it is now `../dist/bdqffdq.ttl`, beside its other serializations (`../dist/bdqffdq.owl` is the RDF/XML).
