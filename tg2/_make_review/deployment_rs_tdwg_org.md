# Deploying BDQ content to rs.tdwg.org

This document describes work within the scope of [tdwg/bdq issue #340](https://github.com/tdwg/bdq/issues/340), "BDQ Review - Deploy BDQ Documentation from GitHub to TDWG web site": deploying the BDQ vocabularies to `rs.tdwg.org`, initially to the `bdq` branch of the `tdwg/rs.tdwg.org` repository (deployed at `bdq-public-review.rs.tdwg.org`), such that files in `rs.tdwg.org` become the source of truth for BDQ vocabulary metadata, rather than the files in the `tdwg/bdq` repository.

## Source of this document

This is an analysis originally produced by GitHub Copilot of the friction produced by the bdqffdq.owl ontology and the multiplicity of terms in the bdqtest vocabulary for deployment on rs.tdwg.org and how this friction might be approached.

**Revision note (2026-09-28):** Revised in place with Claude Code (Claude Opus 5.5) after checking each citation against the `rs.tdwg.org` repository (branch `bdq`, at that time identical to `master`) and this repository. Changes: corrected inaccurate citations and claims (ABCD handling, BDQ information element model, build pipeline, loader behavior); added deployment, routing, and `https` analysis; reframed the source of truth from "BDQ repository authoritative, rs.tdwg.org derived" to "rs.tdwg.org files authoritative for all BDQ vocabularies"; added sections on deploying the simple vocabularies (`bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval`), options for `bdqffdq` (including a hybrid CSV + axioms approach), options for `bdqtest`, and the changes needed in this repository. A further revision the same day added the summary for the TDWG Technical Architecture Group and rs.tdwg.org maintainers, and Section 7.4 on making the protocol a per-vocabulary choice. A third revision added Section 3.3 on whether the `bdqffdq` blank nodes must be blank, Section 9.4 on a blank-node-free ontology, and Section 10.6 on resolvable IRIs for `bdqtest` structural nodes. A fourth revision added the OWL profile of `bdqffdq` (Section 3.2), expanded item 3 of the summary for the TAG, added links for the reader to the draft standard, and added Section 11 on metadata records for the human-readable documents (renumbering later sections). A fifth revision recorded that the landing page is covered by the standard record, and added a note for @tucotuco on document paths and names. Line numbers cited below are as of this revision. **Revision note (2026-09-30):** Added the standard bootstrap and review-status caveats after checking `process.py` and `tdwg_docs_metadata_update.py` on the `rs.tdwg.org` branch `bdq`. **Revision note (2026-11-09):** Work started on the `rs.tdwg.org` branches (Section 8.7, status). `master` (`18a520dc`, 61 commits ahead) was merged into `bdq`, and the source branch `bdq-source` was created from the result. Those commits include large changes to `process/process.py`, `process/document_metadata_processing/tdwg_docs_metadata_update.py`, `html/restxq.xqm`, and `html/html.xqm`, so **the line numbers cited below for those files refer to the pre-merge `bdq` (`b5e3c680`) and are now stale**. They will be rechecked, and the analysis revised where needed, as each step is carried out. A further revision the same day added a short policy for tracking rs.tdwg.org `master` (Section 8.7), and replaced the claim that a real standard number is needed before processing with a survey of standard numbers and placeholders and the decision to use `http://www.tdwg.org/standards/YYY` for the public review (Section 8.2.1). A third revision the same day rewrote Sections 8.2 and 8.2.1 for the release-level `process.py` now on rs.tdwg.org `master`: there is one `config.yaml` and one run for the whole BDQ release, `vocab.yaml` is no longer used, document metadata are declared in `config.yaml` instead of being processed by `tdwg_docs_metadata_update.py`, and the run needs placeholder decision metadata (decided: `decision_number: YYY`) and List of Terms document IRIs. Sections 11.1, 11.2, 11.4, and 12.2, which describe the old document workflow, have not been revised yet. A fourth revision the same day added the implementation status and test results of the per-vocabulary protocol change (Section 7.4, status; Sections 12.3 to 12.6). A fifth revision the same day rewrote Section 8.3 from BDQ's own RDF (`vocab_type: 2`, mapping table, mapping files kept as inputs, conversion checks, rerun constraint), added a status note to Section 8.4, and recorded the `--config` option in Section 8.2. A sixth revision the same day recorded these decisions: List of Terms document IRIs `https://rs.tdwg.org/{vocabulary}/doc/list/` (Sections 8.2.1, 11.3), `recommended` version status, and standard status `Draft Standard`. It also added the evaluation of same-release reruns, the whitespace and served-output findings including the JSON-LD bug (Section 8.3), @tucotuco's support for `--config` (Section 8.2), and questions 11 and 12 (Section 15). A seventh revision the same day recorded the inputs for the five simple vocabularies and the review-only conversion script `bdq_to_rs.py` on `bdq-source`, which is to be replaced by authoritative information in `rs.tdwg.org` (Section 8.3, *Conversion*; Section 8.7, status), and that the rerun fix is committed on `bdq-source` (Section 8.3, *Rerunning*). An eighth revision the same day recorded the deployment of the five simple vocabularies to `bdq-public-review.rs.tdwg.org` (Section 8.7, status). A ninth revision the same day corrected the count of dual-typed `bdqval` terms to 16 and the records affected by the JSON-LD bug (Darwin Core translations are not served), and recorded the fix and tdwg/rs.tdwg.org#619 (Section 8.3, *Served output*; Section 15, question 11). A tenth revision the same day recorded two decisions: Option C for `bdqffdq`, with a replicable, valid OWL ontology generated in rs.tdwg.org from the term list and a parallel axioms file by a general, documented tool (Section 9.5); and whole-vocabulary serializations of all BDQ vocabularies as artifacts of this repository's build in `tg2/_review/dist/`, separate from rs.tdwg.org's per-term serializations (Section 6.4). It updated the summary, Sections 6.2, 9.3, 13, and questions 2 and 3 of Section 15 accordingly. It also recorded that the generator is a general, documented tool; that `rdf:value` stays in rs.tdwg.org, following the TDWG Standards Documentation Specification (Section 4.5.4), while the generated OWL serializations replace it with `skos:notation` to stay in OWL 2 DL (Sections 3.2, 9.5); and that the axioms file follows SDS Section 4.4.2.2 (vocabulary extension term lists). An eleventh revision the same day recorded further `bdqffdq` decisions: the ontology IRI becomes the vocabulary IRI and the axioms the extension term list `https://rs.tdwg.org/bdqffdq/extension/` (SDS 4.4.2.2); `skos:notation` at term level beside `rdf:value`; form 2 for the 15 restriction ranges, with the analysis; cardinalities as prose and SHACL; `owl:AllDifferent` for the response codes and the SHACL rules for one result per Response; no disjointness for the families; ROBOT as an optional dependency; and the fix to the Vocabulary Extension document's rendering (Section 9.5; Section 15, questions 3 and 6; Section 13). A twelfth revision the same day recorded the `bdqffdq` inputs, deployment, generator, and the regenerated BDQ documents (Section 9.5, status), the dropping of the pairwise `owl:differentFrom` statements and no `owl:AllDifferent` for `ResourceType`, the comparison with the previous `bdqffdq.owl`, the term dates and the SDS Section 4.5 point about entailment properties (questions 13 and 14), and updated Section 13. It also recorded two decisions: on the review site the draft dates become placeholder term versions through a sequence of draft releases, becoming real term versions on ratification (Section 8.5), and the entailment-property boundary stays as it is, for discussion. A thirteenth revision the same day added Section 9.6, the `bdqffdq` extension term list as implemented on `bdq-source` and deployed on bdq-public-review.rs.tdwg.org (a term list record with versions and distributions, and its axioms served with its RDF), the decision to follow rs.tdwg.org's practice for distributions rather than SDS 4.4.3, and question 15. **Revision note (2026-11-10):** recorded the merge of rs.tdwg.org `master` `9aa8f5a6` into `bdq-source` and `bdq` (Section 8.7, status), pull request tdwg/rs.tdwg.org#621 for the JSON-LD fix (Section 15, question 11), and an observation for the rs.tdwg.org maintainers on the missing `dcterms:modified` of term lists (Section 9.6). A second revision the same day recorded that options T1 and T2 for `bdqtest` are rejected: the public review needs the full graph of each Test, both as the complete serializations and per Test, so T3 is the option for the review (Summary item 4; Sections 6.2, 10, 10.7, 14; question 2); and that, at least for now, the structural nodes of `bdqtest` keep their `urn:uuid:` identifiers rather than getting resolvable IRIs (Section 10.6; question 5). A third revision the same day added Section 10.9, the T3 design as work in progress: what a Test's graph contains (with the guide's example as the reference), the design, the two dates of a Test, findings on the current generation, documents, and FilteredPush implementations, the version IRI form as open (question 16, leaning C), the counting Measures, and a triple store as a future direction; and added `bdqtest` follow-ups to Section 13. **Revision note (2026-11-12):** recorded that the `bdqffdq` extension term list is versioned on changes to its axioms or to its member terms, and that the faithful axioms are dated 2024-10-01, a release of their own (decided 2026-11-12); and added the procedure for changing the axioms, with the resulting versions and two gaps, decision links (agreed: the decision should link to the extension term list) and the Vocabulary Extension document (Section 9.6; question 15). A second revision the same day recorded the implementation of the decision links (Section 9.6; question 15). A third revision the same day rewrote Section 11 for the release-level `process.py` (documents declared in `config.yaml`) and recorded decisions: document IRIs under the vocabulary for documents about one vocabulary and under `bdq` for the others; the Quick Reference Guide as one document with supporting pages; the index of normative sections as a development and review artifact, not a document; only the latest version of each document on the review site; and the corrected `bdquc` List of Terms title (Sections 11, 13; question 7). A fourth revision the same day recorded the document records for the ten documents other than the Lists of Terms (Section 11.4, steps 1 and 2); the corrected `document_configuration.yaml` files; option (a), document headers that cite the document versions in rs.tdwg.org (Section 11.4, step 5); the site's links to bdq-public-review.rs.tdwg.org; and follow-ups (Section 13). A fifth revision the same day recorded the landing page changes: its header cites the standard, and its Section 3.3.3 lists the decided IRIs; and the site's plain-text handling of IRIs not yet served (Section 13).

## Scope and source context

This note describes how the `tdwg/rs.tdwg.org` repository currently stores source metadata and generates/publishes machine-readable and human-readable representations of TDWG standards components, and what changes would be required to make it the home of the source of truth for all seven BDQ vocabularies:

| Prefix | Current source in `tdwg/bdq` | Character |
|---|---|---|
| `bdqdim:` | `tg2/_review/vocabulary/bdqdim_term_versions.csv` | flat list of `bdqffdq:DataQualityDimension` individuals |
| `bdqenh:` | `tg2/_review/vocabulary/bdqenh_term_versions.csv` | flat list of `bdqffdq:Enhancement` individuals |
| `bdqcrit:` | `tg2/_review/vocabulary/bdqcrit_term_versions.csv` | flat list of `bdqffdq:Criterion` individuals |
| `bdquc:` | `tg2/_review/vocabulary/bdquc_term_versions.csv` | flat list of `bdqffdq:UseCase` individuals, with extra columns |
| `bdqval:` | `tg2/_review/vocabulary/bdqval_term_versions.csv` | flat, mixed list (Parameters, AbstractInformationElements, SKOS concepts) |
| `bdqffdq:` | `tg2/_review/vocabulary/bdqffdq.owl` (Turtle, despite the extension) | OWL ontology |
| `bdqtest:` | `tg2/_review/vocabulary/bdqtest_term_versions.csv` plus GUID tables in `tg2/core/` | graph-rich Test descriptions |

Two decisions frame the rest of this document:

1. **Source of truth.** Files in `rs.tdwg.org` are to be the source of truth for every BDQ vocabulary. Consistent with the normal rs.tdwg.org workflow, as @tucotuco noted in #340, term-version files are a *product* of `rs.tdwg.org` processing (which governs `status`, `issued`, and version IRIs), not an input. The `*_term_versions.csv` files in this repository will therefore cease to be edited here; see [Creating a vocabulary spreadsheet](https://github.com/tdwg/rs.tdwg.org/blob/master/process/create-vocabulary.md) for what the inputs look like.
2. **Canonical protocol.** All BDQ-minted IRIs (terms, term lists, vocabularies, all versions, and BDQ document IRIs) use `https://rs.tdwg.org/` as their canonical form. The standard IRI keeps the TDWG form `http://www.tdwg.org/standards/NNN`.

The BDQ build system includes generation, audit, and validation scripts under `tg2/_build_review` and `tg2/_make_review`. See `tg2/_make_review/copy_files.sh:11-12`, `52-61`; `tg2/_make_review/do_build.sh:7-30`; `.github/workflows/pages.yml:43-50`, `91-99`, `128-145`.

---

## Summary for the TDWG Technical Architecture Group and rs.tdwg.org maintainers

`rs.tdwg.org` is fundamentally a **CSV/YAML-driven metadata publishing system**, not a general RDF graph host. Hand-edited CSV/YAML inputs are processed by `process/process.py` into current-term, version, hierarchy, redirect, and index CSV tables; these are loaded into BaseX as XML when the Docker image is built, and XQuery generates RDF and HTML through content negotiation (Section 1). BDQ raises six issues for this system. Each needs a decision or agreement from the TAG and/or the rs.tdwg.org maintainers.

The draft standard is published for review at <https://bdq.tdwg.org/draft/>; issue [#340](https://github.com/tdwg/bdq/issues/340) tracks this deployment, which is being prepared on the [`bdq` branch of rs.tdwg.org](https://github.com/tdwg/rs.tdwg.org/tree/bdq).

**1. `https` as the canonical protocol.** BDQ uses `https://rs.tdwg.org/` for all of its IRIs; every existing TDWG vocabulary uses `http://rs.tdwg.org/`. Term IRIs already work with `https`, but `process.py` hard-codes `http` for vocabulary IRIs, and `html/restxq.xqm` and `html/html.xqm` hard-code `http` when looking up and displaying vocabularies, term lists, their versions, and documents.
*Proposal:* make the protocol a per-vocabulary property determined by the IRIs recorded in the rs.tdwg.org tables. `process.py` takes the scheme from the `namespace_uri` in each vocabulary's `config.yaml`, and `restxq.xqm` looks a requested path up under both schemes and uses whichever IRI is recorded. Existing standards keep `http` with no change to their data or behavior; new standards can choose `https`. About a dozen lines change, with no new configuration (Section 7.4).
*Decision needed:* does the TAG accept `https` as a canonical protocol for new TDWG vocabularies, and do the rs.tdwg.org maintainers accept the patches?

**2. Where the source of truth lives.** BDQ wants the rs.tdwg.org files to be the source of truth for all seven BDQ vocabularies, with the BDQ repository consuming them, as for Darwin Core and Audiovisual Core. Term-version files become outputs of rs.tdwg.org processing (Section 6).
*No rs.tdwg.org change is needed for the principle*, but items 3 and 4 depend on it.

**3. An OWL ontology (`bdqffdq`).** The Fitness For Use Framework ontology ([guide](https://bdq.tdwg.org/draft/docs/guide/bdqffdq/index.html), [list of terms](https://bdq.tdwg.org/draft/docs/list/bdqffdq/), [Turtle](https://bdq.tdwg.org/draft/vocabulary/bdqffdq.ttl)) defines 51 classes, 43 object and datatype properties, and 15 named individuals.

*OWL level.* Checked with the OWL API 5.1.0 profile checker, the current file is not quite OWL 2 DL, because of two annotation problems: `rdf:value`, which is reserved vocabulary, is used on the 13 named individuals, and `skos:scopeNote` is used without being declared. Declaring `skos:scopeNote` as an annotation property and replacing `rdf:value` with a declared annotation property (for example `skos:notation`) puts it in OWL 2 DL. Its logical axioms are otherwise light: with the range fix below, the only thing outside the OWL 2 EL, QL, and RL profiles is the use of `xsd:date` for the dates of terms (Section 3.2). `rdf:value` is, however, the TDWG convention for controlled value strings ([Standards Documentation Specification](http://rs.tdwg.org/sds/doc/specification/), Section 4.5.4), followed by rs.tdwg.org's column mappings and by BDQ's other vocabularies. *Decided (2026-11-09):* rs.tdwg.org keeps `rdf:value`, and the OWL serializations generated from rs.tdwg.org replace it with `skos:notation`, so each layer follows its own conventions (Section 9.5).

*Blank nodes.* The ontology contains 15 `owl:Restriction` ranges and 2 `owl:AllDisjointClasses` axioms, which are blank nodes (78 triples). OWL 2 DL requires such structures to be blank nodes, so they cannot simply be given identifiers (Section 3.3). Blank nodes are normal in OWL ontologies: **the need to avoid them is a limitation imposed by rs.tdwg.org**, whose tables describe only named resources, not by OWL or by BDQ. For `bdqffdq`, they can be removed with two changes:
- *A fix to the semantics.* All 15 restrictions have the form `P rdfs:range [ owl:onProperty P ; owl:someValuesFrom C ]`, which says that every value of P must itself have some P whose value is a C, for example that `bdqcrit:Complete`, used as a value of `bdqffdq:hasCriterion`, has a criterion of its own. The intended meaning is `P rdfs:range C`. Replacing them with named-class ranges corrects the meaning and removes 15 blank nodes. This fix is needed whatever the deployment.
- *No change in meaning.* Each `owl:AllDisjointClasses` axiom is defined as pairwise disjointness of its members, so the two axioms can be replaced by 9 `owl:disjointWith` statements between named classes (3 + 6).

With both changes (and the two annotation fixes), the ontology has no blank nodes, is in OWL 2 DL, and every statement in it is about a named term, so it fits entirely in an rs.tdwg.org term list (Sections 3.3, 9.4). Future versions that need class expressions (unions, cardinality restrictions) would meet the rs.tdwg.org limitation again.

*Options* (Section 9):
- *A.* rs.tdwg.org only redirects to an ontology file published from the BDQ repository (the ABCD pattern). Small effort, but the source stays outside rs.tdwg.org.
- *B.* The ontology file itself is kept in the rs.tdwg.org repository and served from there (a new pattern: returning file content) or redirected to.
- *C (decided).* Term metadata is an ordinary rs.tdwg.org term list processed by `process.py`, so `bdqffdq` terms get normal TDWG versions and dereferencing, and a build step produces the whole ontology from it. With the changes above, no other source is needed (Section 9.4); otherwise the restrictions and axioms are kept in a small Turtle file beside the term list (Section 9.3).

*Decided (2026-11-09):* Option C, with a generator in rs.tdwg.org producing the whole ontology, and the whole-ontology files published from the BDQ repository's `tg2/_review/dist/` with the other vocabularies' files (Sections 6.4, 9.5). *Decision needed:* whether rs.tdwg.org will redirect the ontology IRI to those files; and whether the TAG sees a need for rs.tdwg.org to support ontologies with blank nodes in general, for BDQ's future versions or for other standards.

**4. A graph-rich vocabulary (`bdqtest`).** Each Test is described by a nested graph (Test → Specification → Argument → Parameter; information elements composed of several terms; policies), with many nodes identified by `urn:uuid`. A diagram of this structure is in [BDQ Tests: Concepts and Use, 2.1.1 Conceptual map: how BDQ uses the term "Test"](https://bdq.tdwg.org/draft/docs/guide/bdqtest/index.html#211-conceptual-map-how-bdq-uses-the-term-test-non-normative), and example RDF for one Test is in [Fitness For Use Framework Ontology: Concepts and Use, 2.6 Example representation of a BDQ Test](https://bdq.tdwg.org/draft/docs/guide/bdqffdq/index.html#26-example-representation-of-a-bdq-test-non-normative). The 254 Tests are listed in the [BDQ Tests List of Terms](https://bdq.tdwg.org/draft/docs/list/bdqtest/) and the [Quick Reference Guide](https://bdq.tdwg.org/draft/docs/terms/bdqtest/), and the whole vocabulary is available as [Turtle](https://bdq.tdwg.org/draft/dist/bdqtest.ttl). The rs.tdwg.org serializer emits one value per cell and links child tables only one level deep, so it cannot produce the full graph for a Test (Sections 2, 4, 5). Options (Section 10):
*Requirement (decided 2026-11-10):* for the public review, the full graph of each Test must be deliverable, both as the complete `bdqtest` serializations and as a serialization per Test. Options that deliver less are rejected (Section 10).
- *T1 (rejected).* A flat, versioned `bdqtest` term list and its GUID tables in rs.tdwg.org. rs.tdwg.org would serve only a partial description of each Test.
- *T2 (rejected).* Normalized linked-class tables. More complete per Test, still not the full graph.
- *T3 (proposed for the public review).* A BDQ-specific processing step in rs.tdwg.org generates the full graph of each Test as RDF files, served by a new route; the complete serializations are built from the same rs.tdwg.org files.
- *T4.* Extend the rs.tdwg.org loader and serializer to support nested linked tables. The most general option, and a large change.
*Decision needed:* whether rs.tdwg.org will accept a vocabulary-specific processing step and a file-serving route (T3), or prefers a general extension (T4). Either delivers the full graphs; T1 and T2 do not.

*Non-resolvable identifiers for structural nodes.* The nodes that give a Test its internal structure are identified by `urn:uuid:` IRIs, which cannot be dereferenced: in the current `bdqtest.ttl`, 253 Methods, 253 Specifications, 63 Arguments, 147 information element nodes (ActedUpon and Consulted), and 16 Policies. They are essentially internal to the description of each Test, and can be seen only inside a graph returned for some other IRI.
*Question:* should these nodes be resolvable, for example as `https://rs.tdwg.org/bdqtest/specification/{uuid}`? Resolvable IRIs would let each node be described where it is identified, and would make normalized linked tables (T2) sufficient, because each kind of node could be the root of its own dataset. The cost is several hundred more TDWG-minted IRIs to keep stable and version under the Vocabulary Maintenance Specification, and changes to the BDQ documents and RDF distributions, which already use the `urn:uuid:` values (Section 10.6). *Decided (2026-11-10), at least for now:* no; the structural nodes keep their `urn:uuid:` identifiers, which is why a Test's IRI must deliver the full graph of its related nodes (Section 10, requirement).

**5. Serving files, and CI.** Options B, C, and T3 all involve rs.tdwg.org returning pre-generated RDF files, which it has not done before (the ABCD handlers only redirect). Separately, BDQ has SHACL and SPARQL validation that could run in rs.tdwg.org CI or remain in the BDQ repository (Section 15).

**6. Metadata records for the human-readable documents.** Apart from the landing page, which is covered by the standard record, the standard has 17 human-readable components: an ontology landing page, an ontology extension document, five guides, a supplement, a tutorial, a Quick Reference Guide, and seven Lists of Terms (the generated index of normative sections is a development and review artifact, not a document). Each needs document metadata in rs.tdwg.org (`docs/`, `docs-versions/`, `docs-roles/`) so that its IRI dereferences, written by `process.py` from the `documents` declared in the release `config.yaml`, converted from YAML files that BDQ already maintains. The work is mostly mechanical; the document IRIs used in the drafts do not follow TDWG patterns and several collide with vocabulary or term list IRIs, so new document IRIs were agreed (Section 11).
*Decided 2026-11-12:* the document IRIs, `https://rs.tdwg.org/{vocabulary}/doc/{name}/` for documents about one vocabulary and `https://rs.tdwg.org/bdq/doc/{name}/` for the others; the Quick Reference Guide is one document (Section 11.3).

The five simple BDQ vocabularies (`bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval`) fit the standard `process.py` pipeline, but still need the preparation in Section 8: column-mapping additions (8.3), data fixes (8.4), version-date choices (8.5), HTML redirects (8.6), and the standard-record bootstrap (8.2.1). Until a standard number is assigned, the placeholder `http://www.tdwg.org/standards/YYY` is used (Section 8.2.1). The `bdq` branch of rs.tdwg.org is already deployed at `bdq-public-review.rs.tdwg.org` (Section 1.4), so all of this can be demonstrated there before anything is merged to `master`.

---

## 1. Current rs.tdwg.org architecture

### 1.1 Input and generated metadata

The rs.tdwg.org workflow assumes that hand-edited CSV plus YAML configuration are combined to generate the authoritative CSV files used to build both machine-readable and human-readable outputs (`process/process-vocabulary.md:41-67`). As Steve Baskauf explains in [Understanding TDWG standards documentation](https://baskauf.blogspot.com/2019/10/understanding-standards-documentation.html), the CSV files in the rs.tdwg.org repository are the authoritative source of standards metadata; List of Terms documents are built from them by Maintenance Group scripts, and RDF is generated from them on the fly.

The main processing script is `process/process.py`. It:

- creates mapping and configuration files for new term lists (`process/process.py:76-189`);
- generates term-version metadata (`process/process.py:232-333`);
- generates or updates current term metadata, and updates term-list, index, and redirect tables (`process/process.py:336-675`; the `index/index-datasets.csv` and `term-lists/term-lists.csv` rows at `490-545`, `html/redirects.csv` at `632-673`);
- propagates changes up to vocabulary and standard metadata (`process/process.py:738-1215`);
- loops over the namespaces given in `config.yaml` (`process/process.py:1218-1319`).

Version IRIs are generated by appending the `date_issued` from `config.yaml` to the term local name under `<namespace>version/`, and replacement links are generated automatically (`process/process.py:280-296`; see also `process/process-vocabulary.md:208-215`). Every version created in one run gets the same `date_issued`.

### 1.2 BaseX loading and runtime publication

The repository does not store RDF. CSV files are loaded into BaseX as XML:

- `docker/initialize-database.sh:23-32` starts BaseX and runs the loader; it runs at Docker image build time.
- The Dockerfile invokes the loader against the **local checkout copied into the image**, not against GitHub. `index/load-db-from-github.py` reads local files unless the path begins with `http` (`index/load-db-from-github.py:101-115`). Loading from GitHub happens only in the loader's GUI, which hard-codes the `master` branch (`44`, `86`).
- `index/load-db-from-github.py:208-252` loads `constants.csv`, auxiliary CSVs, core metadata, and linked metadata. Each dataset is named by column index 1 of `index/index-datasets.csv` (`192`), which is both the database name and the directory name.
- CSV headers become XML element names, with only spaces replaced (`index/load-db-from-github.py:128`). Headers containing `:`, `(`, or `)` produce invalid XML.

At runtime, XQuery in `html/restxq.xqm` performs dereferencing and serialization:

- dataset dumps: `html/restxq.xqm:29-74` (the `.htm` link hard-codes GitHub `tree/master`, line 47)
- representation selection and response generation: `html/restxq.xqm:1054-1100`
- 303 content-negotiation redirects: `html/restxq.xqm:1178-1192`
- record and linked-resource RDF generation: `html/restxq.xqm:1688-1809`
- per-column property emission: `html/restxq.xqm:1961-2003`

`restxq.xqm` also reads some CSVs directly from `/usr/src/rs.tdwg.org` at request time: `index/index-datasets.csv` (`76-84`), `term-lists/term-lists.csv` (`364-376`), `html/redirects.csv` (`1105`), and `docs/docs.csv`.

HTML term pages advertise alternate serializations via `.htm`, `.ttl`, `.rdf`, and `.json` links (`html/html.xqm:395-403`).

### 1.3 Routing of IRIs to databases

There is no hard-coded list of vocabularies for generic terms. The handler for `/{vocab}/{ns}/{local-id}` looks up `list_localName = "{vocab}/{ns}/"` in `term-lists/term-lists.csv` and uses that row's `database` column (`html/restxq.xqm:360-379`). The term-version handler uses `database || "-versions"` (`396`), so the `versions_database` column is ignored and the versions database must be named `<database>-versions`. Records are found by the `baseIriColumn` value (the local name) only (`find-db`, `1589-1603`).

Handlers for vocabularies, term lists, term list versions, vocabulary versions, and documents build lookup strings with a hard-coded `http://rs.tdwg.org/` (`html/restxq.xqm:111-137`, `246-256`, `280-284`, `302-306`, `324-328`). Hard-coded special cases also exist for Darwin Core, `/dwc/terms/attributes`, docs, decisions, the index, ABCD, TAPIR, and others (`88-630`, `640-1040`).

### 1.4 Deployment

Per `DEPLOYMENT.md`, the GBIF build system:

- rebuilds and deploys the `master` branch to `http://test.rs.tdwg.org/`;
- deploys GitHub releases to `http://rs.tdwg.org/`;
- deploys specific tracked branches for public reviews. **The `bdq` branch is already enabled and deployed at `http://bdq-public-review.rs.tdwg.org/`** (`https` is also supported; a request for `https://bdq-public-review.rs.tdwg.org/dwc/terms/recordedBy` with `Accept: text/turtle` returns a 303 as expected).

Because the image is built from the checked-out branch, whatever CSVs are committed on `bdq` are what `bdq-public-review.rs.tdwg.org` serves.

### 1.5 Validation currently in rs.tdwg.org

Existing validation focuses on dereferencing and content negotiation rather than ontology semantics or SHACL validation. The dereferencing test probes multiple Accept headers for example URLs from each database and from document IRIs (`index/dereferencing-test.py:7`, `26-60`, `63-148`). It skips any example URL that does not begin with `http://rs.tdwg.org/` (`94`), so it would currently skip every BDQ IRI.

---

## 2. What the current rs.tdwg.org data model assumes

### 2.1 One column maps to one property occurrence

The basic mapping model is explicit in the standard term mapping template:

`header,predicate,type,value,attribute,subject_id`
(`process/files_for_new/current_terms/simple-vocabulary-column-mappings.csv:1-19`)

At serialization time, `html/restxq.xqm` iterates over columns and mapping rows, and if a cell is non-empty, emits exactly one literal or IRI value for that mapped property (`html/restxq.xqm:1975-1991`). There is no splitting of cell values anywhere: no `tokenize` or delimiter split in `restxq.xqm`, `load-db-from-github.py`, or `process.py` (the splits in `process.py` all split IRIs on `/` or version names on `-`). The loader turns each cell into one XML element, escaping only `&`, `<`, and `>` (`index/load-db-from-github.py:118-143`).

This means that, by default, the system assumes:

- one relevant value per populated cell;
- one mapping row per emitted property occurrence;
- no splitting of comma-separated, bracketed, or otherwise compound cell content into multiple RDF assertions.

### 2.2 Bounded repetition is handled by repeated columns

The existing workaround for a small, bounded number of values is a set of fixed, repeated columns mapped to the same predicate: `replaces_term`, `replaces1_term`, and `replaces2_term` all map to `dcterms:replaces` (`process/files_for_new/current_terms/simple-vocabulary-column-mappings.csv:7-9`). This is sufficient for the bounded multiplicity in the simple BDQ vocabularies and most of `bdqffdq` (Sections 8 and 9.3).

### 2.3 Unbounded multiplicity is handled by linked tables

rs.tdwg.org has a mechanism for one-to-many relationships using:

- a root dataset;
- auxiliary child CSV tables;
- `linked-classes.csv` to describe how those child tables link to the root;
- XQuery that walks those linked child resources and emits both backward and (optionally) forward RDF links.

Examples: documents link to authors, formats, and versions (`docs/linked-classes.csv:1-4`); term lists link to versions and members (`term-lists/linked-classes.csv:1-3`); linked-resource generation is in `html/restxq.xqm:1739-1800`; linked metadata is built by `index/load-db-from-github.py:145-175` and loaded at `247-252`.

How it works (`index/load-db-from-github.py:156-167`, `html/restxq.xqm:1749-1771`):

- The header is `link_column,link_property,suffix1,link_characters,suffix2,filename,forward_link`. For each linked file, the loader also requires `<fileroot>-classes.csv` and `<fileroot>-column-mappings.csv`.
- A child row joins its root by `domainRoot || child[link_column]` (`1754`): children link only to the root record.
- The child IRI is a blank node if `suffix1` starts with `_:` (`1759`); taken from the child column named by `suffix1` if `link_characters` is `http` (`1763`); otherwise `rootIRI#<suffix1><link_characters><suffix2>`. All 158 existing rows use the `http` mode.
- `link_property` is the child-to-root link; `forward_link`, if not empty, is the root-to-child link (`1749`).

Limitations relevant to BDQ:

- **Linking is one level deep.** A child cannot have its own children, so nesting such as Test → Specification → Argument → Parameter, or an information element node with `bdqffdq:composedOf` members, cannot be expressed in one dataset.
- **Extra classes on the same row** are built by `construct-iri` (`html/restxq.xqm:2019-2035`) as `baseIRI+suffix` or a blank node; an IRI cannot be taken from a column this way.

### 2.4 Repeatability metadata does not change serialization

Some vocabularies include columns like `tdwgutility_repeatable` (described at `process/create-vocabulary.md:98`), but these are published as metadata properties; they do not change how RDF is emitted.

---

## 3. Why `bdqffdq.owl` does not fit the ordinary term-list model unchanged

### 3.1 `bdqffdq.owl` is an ontology, not just a term list

The ontology begins with ontology-level assertions: the ontology IRI `https://rs.tdwg.org/bdqffdq/terms` typed as `owl:Ontology`, `owl:versionIRI <https://rs.tdwg.org/bdqffdq/terms/1.0>`, `dcterms:issued`, and ontology-level notes and label (`tg2/_review/vocabulary/bdqffdq.owl:12-16`). The file is Turtle, despite its `.owl` extension.

### 3.2 Its structure

Parsing the ontology (981 triples) gives:

- 51 `owl:Class`, 36 `owl:ObjectProperty`, 7 `owl:DatatypeProperty`, 5 `owl:AnnotationProperty`, 1 `rdfs:Datatype`, 15 `owl:NamedIndividual` (typed also as `bdqffdq:ResponseResult`, `bdqffdq:ResponseStatus`, or `bdqffdq:ResourceType`);
- per-term metadata: `rdfs:label`, `skos:prefLabel`, `rdfs:comment`, `skos:definition`, `skos:note`, `skos:scopeNote`, `dcterms:issued`, `rdf:value`;
- structural properties with IRI values and bounded multiplicity: `rdfs:subClassOf` (at most 3 per class, never a blank node), `rdfs:subPropertyOf` (at most 4), `rdf:type` (at most 2), `owl:differentFrom` (at most 2), and `rdfs:range` (1 per property);
- **graph-native structures**: 15 `rdfs:range` values that are anonymous `owl:Restriction` nodes (e.g. `bdqffdq.owl:209-242`, `335-339`), and 2 `owl:AllDisjointClasses` axioms with `owl:members` RDF lists (`bdqffdq.owl:1421-1439`). Only 78 triples involve blank nodes.

All 15 restrictions have the same form, a property whose range is a restriction on that same property, for example:

```turtle
bdqffdq:hasCriterion rdfs:range [ rdf:type owl:Restriction ;
                                  owl:onProperty bdqffdq:hasCriterion ;
                                  owl:someValuesFrom bdqffdq:Criterion ] .
```

This says that anything that is the value of `bdqffdq:hasCriterion` must itself have some `bdqffdq:hasCriterion` value that is a `bdqffdq:Criterion`. A reasoner would therefore infer that `bdqcrit:Complete`, used as a value, has a criterion of its own. The intended meaning is almost certainly `bdqffdq:hasCriterion rdfs:range bdqffdq:Criterion`. This is a modeling question for the BDQ maintainers, but it affects deployment (Section 9.4).

**OWL level.** Checked with the OWL API 5.1.0 profile checker (`Profiles.OWL2_DL`, `OWL2_EL`, `OWL2_QL`, `OWL2_RL`), the current file:

- is **not in OWL 2 DL**, with 15 violations, all in annotations: `rdf:value` (reserved vocabulary) is used as an annotation property on the 13 named individuals (`bdqffdq:ResponseResult`, `bdqffdq:ResponseStatus`, and `bdqffdq:ResourceType` values), and `skos:scopeNote` is used on 2 terms without being declared;
- is in OWL 2 DL once `skos:scopeNote` is declared as an `owl:AnnotationProperty` and `rdf:value` is replaced by a declared annotation property (for example `skos:notation`);
- is outside OWL 2 EL and QL only because of `xsd:date` (declared as a datatype and used for the `dcterms:issued` dates of terms), which is not in those profiles' datatype maps, and outside OWL 2 RL also because of the 15 existential restrictions used as ranges;
- after the changes in Section 3.3 item 2 as well, is in OWL 2 DL with no blank nodes, and is outside OWL 2 EL, QL, and RL only because of `xsd:date`.

The logical content is therefore light (subclass and subproperty hierarchies, ranges, disjointness, distinct individuals). The `rdf:value` problem matters for deployment. The [Standards Documentation Specification](http://rs.tdwg.org/sds/doc/specification/) (SDS), Section 4.5.4, says that each controlled vocabulary term MUST have a string unique within its vocabulary, which SHOULD be a plain literal value of `rdf:value`. rs.tdwg.org's column mapping templates follow this (`controlled_value_string` → `rdf:value`), as do BDQ's other vocabularies. SDS 4.5.4 is written for `skos:Concept` terms, but the 13 `bdqffdq` individuals are controlled values in practice (the response codes that implementations emit). The convention is at the RDF level and predates any OWL 2 DL concern: it conflicts with OWL 2 DL only when such a term list becomes part of an ontology. *Decided 2026-11-09:* `rdf:value` stays in rs.tdwg.org, and the generator replaces it with `skos:notation` in the OWL serializations (Section 9.5).

The `@base <https://rs.tdwg.org/bdqffdq/terms#>` and the empty `:` prefix (`bdqffdq.owl:1`, `10`) are not used by any term and could be removed.

### 3.3 Must these nodes be blank?

**In OWL 2 DL, yes.** The [OWL 2 mapping to RDF graphs](https://www.w3.org/TR/owl2-mapping-to-rdf/) represents anonymous class expressions (such as `owl:Restriction`), the main node of n-ary axioms (such as `owl:AllDisjointClasses`), and the cells of RDF lists (such as `owl:members`) as blank nodes, and an RDF graph is parsed as an OWL 2 DL ontology only if those nodes are blank. If the restriction nodes are given IRIs, the graph remains valid RDF and has a meaning under the OWL 2 RDF-Based Semantics (OWL 2 Full), but it is no longer OWL 2 DL: DL reasoners and the OWL API, used by Protégé, would not read the restrictions as class expressions. An IRI-named restriction cannot be written in the OWL 2 functional syntax at all. Naming a class and declaring it `owl:equivalentClass` to the restriction does not help, because the restriction on the right-hand side is still a blank node.

The ways to give these structures identifiers, or to avoid them, are:

1. **Skolemize for storage only.** [RDF 1.1 skolemization](https://www.w3.org/TR/rdf11-concepts/#section-skolemization) replaces each blank node with a skolem IRI (e.g. `https://rs.tdwg.org/.well-known/genid/bdqffdq-hasCriterion-range`), which can then be stored in tables like any other resource. The build step that generates the ontology must turn the skolem IRIs back into blank nodes. This keeps the current semantics, but the skolem IRIs must never appear in the published ontology, and a term-level response generated from those tables would not be OWL 2 DL.
2. **Remove the blank nodes by changing the ontology.** Replace each restriction range with a named-class range (Section 3.2), and replace each `owl:AllDisjointClasses` axiom with pairwise `owl:disjointWith` statements between named classes: 3 for the first axiom (3 members) and 6 for the second (4 members). `owl:AllDisjointClasses` is defined as pairwise disjointness, so this second change does not alter the meaning. The first change does alter the meaning, to what appears to be the intended one. Every remaining triple then has a named subject and a named or literal object.
3. **Keep them as blank nodes** in an axioms file (Option C, Section 9.3).

### 3.4 Consequence

There is no existing rs.tdwg.org pathway that takes an RDF file and publishes its triples through the database-backed negotiation system. The closest precedent is the ABCD handler (`html/restxq.xqm:772-814`), which **only redirects**: it returns a 303 to externally hosted `https://abcd.tdwg.org/ontology/abcd_concepts.{owl,ttl,jsonld}` or to an HTML fragment. It never returns file content. Options for `bdqffdq` are evaluated in Section 9.

---

## 4. Why `bdqtest` does not fit a single-table current-term model

### 4.1 The source data contains repeated and structured relationships

`bdqtest_term_versions.csv` (254 Tests, all `recommended`: 149 Measures, 72 Validations, 29 Amendments, 4 Issues) has a richer model than a normal TDWG term-list row. Its header (`tg2/_review/vocabulary/bdqtest_term_versions.csv:1`) includes:

- `InformationElement:ActedUpon`
- `aggregatesResponsesFrom`
- `InformationElement:Consulted`
- `Parameters`
- `AuthoritiesDefaults`
- `References`
- `Example Implementations (Mechanisms)`
- `UseCases`
- `ArgumentGuids`

Several of these headers (`InformationElement:ActedUpon`, `Example Implementations (Mechanisms)`) would produce invalid XML element names in the rs.tdwg.org loader (Section 1.2), so any rs.tdwg.org version of this table needs renamed columns.

Examples of multiple values packed into single cells:

- multiple acted-upon information elements: `dwc:minimumDepthInMeters,dwc:maximumDepthInMeters` (`bdqtest_term_versions.csv:5`, also `27`)
- multiple acted-upon and multiple consulted information elements in the same row (`bdqtest_term_versions.csv:11`, `41`, `64`)
- multiple parameters (`bdqtest_term_versions.csv:23`)
- multiple Use Cases and multiple examples are common
- references may be supplied as HTML list content containing multiple URLs

### 4.2 BDQ already requires custom parsing logic

The BDQ Python RDF builder, `tg2/_build_review/build_bdqtest_rdf.py`, performs semantics that rs.tdwg.org does not perform generically:

- splits information-element CSV lists into multiple IRIs: `474-504`
- creates special MultiRecord aggregated acted-upon nodes: `507-541`
- parses HTML/plaintext references into multiple `dcterms:references` links: `137-176`, `739-744`
- parses multiple examples from `[...],[...]` syntax: `181-203`, `797-799`
- creates `bdqffdq:Argument` nodes by pairing `Parameters` with values from `AuthoritiesDefaults`: `580-618`, `809`
- collects repeated `UseCases` into policy collections and creates UseCase / Policy resources: `811-850`
- serializes to Turtle, RDF/XML, and JSON-LD: `855-865`

It takes as input the term-version CSV plus four GUID tables in `tg2/core/`: `TG2_tests_additional_guids.csv` (Method and Specification `urn:uuid` IRIs per Test), `information_element_guids.csv` (information element `urn:uuid` IRIs by label), `TG2_policy_guids.csv`, and `TG2_citation_guids.csv` (`build_bdqtest_rdf.py:1-40`, `875-910`).

**Current state of the build pipeline:** `build_bdqtest_rdf.py` is not yet invoked by `copy_files.sh`, `do_build.sh`, or `pages.yml`. `tg2/_make_review/copy_files.sh:52-61` still generates `tg2/_review/dist/bdqtest.{xml,ttl,json}` with the Java `kurator-ffdq` `test-util.sh`, and `pages.yml` publishes the committed `bdqtest.ttl` without regenerating it.

### 4.3 How BDQ models information elements and arguments

Multiplicity in the BDQ graph is not always where the CSV suggests:

- Each Test has **one** `bdqffdq:hasActedUponInformationElement` (and at most one `bdqffdq:hasConsultedInformationElement`) pointing to a shared information element node whose `urn:uuid` IRI is looked up from `information_element_guids.csv`. The multiple Darwin Core terms are `bdqffdq:composedOf` members of that node (`build_bdqtest_rdf.py:487-504`, `710-734`).
- Arguments hang off the Specification, not off the Test (`build_bdqtest_rdf.py:606`).
- Methods, Specifications, information elements, Arguments, and Policies have `urn:uuid` IRIs, which cannot be dereferenced over HTTP; they can only appear inside a graph returned for some other IRI. In the current `tg2/_review/dist/bdqtest.ttl` there are 253 Methods, 253 Specifications, 63 Arguments, 147 information element nodes, and 16 Policies, against 253 Tests (Section 10.6).

### 4.4 Consequence

If the columns of `bdqtest_term_versions.csv` were mapped directly through the rs.tdwg.org serializer, the packed relationships would become opaque string literals, and the nested structure would be absent. That is valid RDF, but not a lossless or semantically adequate publication of `bdqtest`. Options are evaluated in Section 10.

---

## 5. Using `linked-classes.csv` for BDQ multiplicity

The `linked-classes.csv` mechanism (Section 2.3) is the rs.tdwg.org-native way to represent one-to-many relationships, and it can represent some of `bdqtest`, but its one-level depth limits it.

### 5.1 What linked classes can represent for a Test

With the Test as the root record, one level of linked children can carry:

- the Test's Method, Specification, and information element nodes (one each, with IRIs taken from a column using the `http` mode);
- the Test's references (as `dcterms:BibliographicResource` children);
- the Test's examples;
- the Test's use-case memberships.

### 5.2 What linked classes cannot represent

- Arguments of a Specification, and the Parameter each Argument is for (depth 2 and 3 from the Test);
- `bdqffdq:composedOf` members of an information element node (depth 2);
- Policy aggregation, which is derived from use-case memberships and policy-type classification rather than literal row expansion (`build_bdqtest_rdf.py:811-850`);
- MultiRecord acted-upon nodes derived from `aggregatesResponsesFrom` (`507-541`).

Splitting these into separate datasets (Specifications with linked Arguments, information elements with linked members) does not help per-Test dereferencing while the roots of those datasets have `urn:uuid` IRIs, which no HTTP request can reach, and a request for a Test IRI returns only the Test and its direct children. It would help if those nodes were given resolvable IRIs (Section 10.6).

So linked classes are a partial fit for `bdqtest` and no fit for the `bdqffdq` axioms.

---

## 6. Source of truth

### 6.1 Target

The target is that the **files in the `rs.tdwg.org` repository are the source of truth for every BDQ vocabulary**, and that this repository's build reads from `rs.tdwg.org` (for List of Terms documents, the Quick Reference Guide, generated CSV lists, and RDF distributions) instead of from `tg2/_review/vocabulary/`. This is the normal TDWG pattern: `process-vocabulary.md:67` requires List of Terms build scripts to draw from the authoritative CSV files in rs.tdwg.org.

Consequently, the term-version files are outputs of rs.tdwg.org processing (`<database>-versions/<database>-versions.csv`), not inputs, as @tucotuco noted in #340. Changes to terms after deployment are made by adding hand-edited modification CSVs under `rs.tdwg.org/process/` and running `process.py`, following the [Vocabulary Maintenance Specification](http://rs.tdwg.org/vms/doc/specification/).

### 6.2 Feasibility per vocabulary

| Vocabulary | Source of truth in rs.tdwg.org | Who generates RDF | Section |
|---|---|---|---|
| `bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval` | CSV, via `process.py`, standard pattern | rs.tdwg.org serializer | 8 |
| `bdqffdq` | *Decided (2026-11-09):* hybrid, a term list CSV plus a parallel axioms Turtle file, both in rs.tdwg.org (Option C) | Term-level RDF: rs.tdwg.org serializer. Whole ontology: a generator in rs.tdwg.org merging CSV and axioms, run by the BDQ build into `tg2/_review/dist/` (Section 6.4) | 9, 9.5 |
| `bdqtest` | CSV (a flat, versioned term list plus auxiliary tables) in rs.tdwg.org | Per Test: the full graph, as generated files served by rs.tdwg.org (T3; flat descriptions, T1 and T2, are rejected). Whole vocabulary: the complete serializations, built from the rs.tdwg.org files (Section 6.4) | 10 |

### 6.3 What stays in `tdwg/bdq`

- The human-readable documents (List of Terms, guides, Quick Reference Guide) and their build scripts, published on `bdq.tdwg.org`; these become consumers of rs.tdwg.org data.
- Build, audit, and validation scripts (SHACL, SPARQL, consistency audits, `tg2/_make_review/do_build.sh:7-30`; `tg2/_build_review/tools/validate_bdqtest_against_shacl.py:5-20`, `85-87`). These should read from rs.tdwg.org (a local checkout, or `https://raw.githubusercontent.com/tdwg/rs.tdwg.org/<branch>/`).
- Generated distributions such as `bdqtest.ttl`, if they are built here from rs.tdwg.org data (Section 10).

### 6.4 Whole-vocabulary serializations

*Decided 2026-11-09.* The complete serializations of every BDQ vocabulary (the five simple vocabularies, `bdqffdq`, and `bdqtest`) are artifacts of the BDQ build. They are written to `tg2/_review/dist/` in this repository and published from there on `bdq.tdwg.org`, so that this repository produces a single artifact containing the entire standard: documents and vocabulary files together.

The two repositories then have separate roles:

- **rs.tdwg.org** holds the source of truth (Section 6.1) and serializes individual resources on demand: terms, term versions, term lists, vocabularies, the standard, and documents. It does not store or serve whole-vocabulary files.
- **This repository's build** reads the rs.tdwg.org files and generates the whole-vocabulary files, as it already does for the simple vocabularies (`draft_build-termlist.py` writes `dist/bdq{dim,enh,crit,uc,val}.xml`) and for `bdqtest` (`dist/bdqtest.{ttl,xml,json}`).

The per-term responses and the whole-vocabulary files are generated independently from the same rs.tdwg.org files, and neither depends on the other. To make an artifact reproducible, the build should record the rs.tdwg.org commit it read (for example, a pinned commit of the `bdq` branch) in the artifact.

Consequences:

- rs.tdwg.org needs no route that returns whole-vocabulary files for BDQ, which narrows question 2 of Section 15 for `bdqffdq`; per-Test files for `bdqtest` (option T3) are a separate question.
- The ontology file, now `tg2/_review/vocabulary/bdqffdq.owl` and published as `https://bdq.tdwg.org/draft/vocabulary/bdqffdq.ttl`, becomes a generated file in `dist/` (`bdqffdq.ttl`, `bdqffdq.rdf`, `bdqffdq.jsonld`), built from rs.tdwg.org (Section 9.5).
- Links from rs.tdwg.org to a whole-vocabulary file, in particular the ontology IRI `https://rs.tdwg.org/bdqffdq/terms`, are redirects to `bdq.tdwg.org` (as in Option A), and need stable, non-`/draft/` targets before ratification (Section 15, questions 3 and 4).

---

## 7. `https` as the canonical protocol for BDQ IRIs

### 7.1 What already works

- Term IRIs in RDF output are built from the dataset's `domainRoot` in `constants.csv`, which `process.py` derives from the configured namespace URI (`process/process.py:119`, and `173` for the versions dataset), so `https://rs.tdwg.org/bdqdim/terms/` produces `https` term and term-version IRIs.
- Term lookup is by local name, so `https://…/bdqdim/terms/Completeness` and `http://…/bdqdim/terms/Completeness` both resolve.
- Term list version IRIs are derived from the term list URI (`process/process.py:414-416`), so they keep `https`.
- The `list_localName` for `term-lists.csv` is taken from path segments (`process/process.py:337-338`), independent of scheme.
- The server answers `https` requests (Section 1.4).

### 7.2 What needs changing

1. **`process/process.py:747`, `750`** hard-code `http://rs.tdwg.org/` for the vocabulary IRI and vocabulary version IRI.
2. **`html/restxq.xqm`** hard-codes `http://rs.tdwg.org/` in lookups for documents (`111-137`), vocabularies (`246-256`), vocabulary versions (`280-284`), term lists (`302-306`), and term list versions (`324-328`). Without a change, `https://rs.tdwg.org/bdqdim/terms/`, `https://rs.tdwg.org/bdqdim/`, and BDQ document IRIs return 404.
3. **`html/html.xqm`** assumes `http` when generating HTML pages: a term's version IRI is only shown if `term_isDefinedBy` contains `http://rs.tdwg.org/` (`265`), and a vocabulary page builds its "this version" IRI from `http://rs.tdwg.org/version/` (`509`).
4. **`index/dereferencing-test.py:94`** skips URLs not beginning with `http://rs.tdwg.org/`.
5. **Consistency in this repository.** BDQ documents and data currently mix `https://rs.tdwg.org/bdq…` (the large majority) with some `http://rs.tdwg.org/bdq…` IRIs; the `http` occurrences should be changed.

Section 7.4 describes how to make items 1-4 per-vocabulary.

### 7.3 Governance

BDQ would be the first `https` vocabulary on rs.tdwg.org; every existing `domainRoot` and hierarchy IRI is `http`. The patches can be made on the `bdq` branch for the public review, but merging them to rs.tdwg.org `master` needs agreement from the rs.tdwg.org maintainers and the TDWG Technical Architecture Group. That agreement should be sought early, as the IRIs cannot change after ratification.

### 7.4 Making the protocol a per-vocabulary choice

**This is possible, and it needs no new configuration.** Existing standards can keep `http` with no change to their data or to how their IRIs behave, while a new standard (or a new vocabulary) can use `https`. The protocol becomes a property of each vocabulary, determined by the IRIs recorded for it in the rs.tdwg.org tables.

#### Why the data already carries the choice

- **Terms and term versions:** RDF subjects are built from the `domainRoot` in each dataset's own `constants.csv` (Section 7.1), so the scheme is already per term list.
- **Hierarchy and documents:** the `term-lists`, `term-lists-versions`, `vocabularies`, `vocabularies-versions`, and `docs` datasets have an empty `domainRoot` and use the full IRI as their `baseIriColumn` (`list`, `vocabulary`, `current_iri`; see e.g. `term-lists/constants.csv`, `vocabularies/constants.csv`, `docs/constants.csv`). A record is found by exact match on that full IRI (`page:find-db`, `html/restxq.xqm:1589-1603`), and the same string becomes the RDF subject. So a row recorded as `https://rs.tdwg.org/bdqdim/terms/` is published with an `https` subject once the handler can find it; the only obstacle is that the handler constructs its lookup string with `http`.
- **Requests carry no scheme.** Behind the proxy, RESTXQ sees only the path (`/bdqdim/terms/`), and the same response is served whether the client used `http` or `https`. The canonical IRI therefore cannot come from the request; it has to come from the data, and it does.

#### Implementation

1. **`process/process.py`.** The scheme is already configured per vocabulary: each processing run has its own `config.yaml`, whose `namespace_uri` gives the scheme. Replace the hard-coded prefix at `747` and `750` with the scheme of the term list IRI, e.g.

   ```python
   scheme = termlist_uri.split('//')[0]   # 'http:' or 'https:'
   vocabularyUri = scheme + '//rs.tdwg.org/' + vocab_subpath + '/'
   vocabularyVersionUri = scheme + '//rs.tdwg.org/version/' + vocab_subpath + '/' + date_issued
   ```

   For every existing vocabulary, `scheme` is `http:`, so the output is unchanged. Everything else `process.py` generates for a term list (term, term version, term list version, `list_localName`, redirects) already follows the namespace. The standard IRI comes from `config.yaml` unchanged, and the dataset index IRIs (`http://rs.tdwg.org/index/…`) describe rs.tdwg.org itself, so they stay `http`. `tdwg_docs_metadata_update.py` takes document IRIs from `document_configuration.yaml` and has no hard-coded scheme.

   Optional safeguard: have `process.py` refuse to create a vocabulary, term list, or document whose path is already recorded under the other scheme.

2. **`html/restxq.xqm`.** Add one helper that resolves a path to whichever IRI is recorded, trying `http` first so existing vocabularies take the same path as now:

   ```xquery
   declare function page:canonical-iri($path, $db)
   {
     let $http := "http://rs.tdwg.org/" || $path
     let $https := "https://rs.tdwg.org/" || $path
     return
       if (page:find-db($http, $db)) then $http
       else if (page:find-db($https, $db)) then $https
       else $http   (: not found under either; the caller returns 404 as now :)
   };
   ```

   In each of the twelve lookups listed in Section 7.2 item 2, replace `"http://rs.tdwg.org/" || $path` with `page:canonical-iri($path, $db)`. The resolved IRI is then passed to `page:handle-repesentation` or `page:see-also` exactly as now, so the RDF subject is the recorded IRI. The special cases in the same handlers (`decisions`, `index`, and the Darwin Core guides) keep their fixed `http` IRIs. The cost is one extra `find-db` for `https` records only; `http` records are found at the first attempt.

3. **`html/html.xqm`.** Replace the test at `265` with `matches($record/term_isDefinedBy/text(), '^https?://rs\.tdwg\.org/')`, and build the vocabulary version IRI at `509` from the scheme of `$record/vocabulary/text()` rather than from a hard-coded `http://rs.tdwg.org/version/`.

4. **`index/dereferencing-test.py:94`.** Accept both `http://rs.tdwg.org/` and `https://rs.tdwg.org/` prefixes. For `https` vocabularies, add checks that the RDF subjects returned are the `https` IRIs.

5. **Documentation.** Add to `process/process-vocabulary.md` and the `config.yaml` comments that the scheme of `namespace_uri` sets the canonical protocol for the whole vocabulary (vocabulary, term list, terms, and versions), that TDWG vocabularies created before this change use `http`, and that a vocabulary's scheme cannot change after it is first processed. Document IRIs follow whatever is set in `document_configuration.yaml`, and should use the same scheme as the standard's vocabularies.

#### Behavior after the change

| Case | Before | After |
|---|---|---|
| Existing `http` vocabulary, requested over `http` or `https` | resolves; `http` subjects | unchanged |
| New `https` vocabulary term, requested over either scheme | resolves; `https` subjects | unchanged |
| New `https` vocabulary, term list, their versions, or document, requested over either scheme | 404 | resolves; `https` subjects |
| Path not recorded under either scheme | 404 | 404 |

#### Alternatives considered

- **An explicit setting**, such as a `canonical_scheme` column in `term-lists.csv`, `vocabularies.csv`, and `docs.csv`, or a list of `https` vocabularies read by `restxq.xqm`. This makes the choice easier to see, but duplicates information already in the recorded IRIs and can contradict them. Not recommended.
- **Switching everything to `https`.** This would change the canonical IRIs of every existing TDWG vocabulary, which is not acceptable for ratified standards.
- **A single fallback without the helper** (retry with `https` in each handler). Equivalent in behavior, but repeats the logic in every handler.

#### Status (2026-11-09): implemented and tested on `bdq-source`

Implemented in rs.tdwg.org commit `231e8a2c` on `bdq-source` ([tdwg/rs.tdwg.org@231e8a2c](https://github.com/tdwg/rs.tdwg.org/commit/231e8a2c)), against the code merged from `master` (Section 8.7). The design above held. Because of the rewrite of `process.py` on `master`, the details differ from the implementation steps above:

- **`process.py`.** The vocabulary IRI is no longer built from the term list IRI: it is now configured explicitly per vocabulary (`vocabulary` in `config.yaml`), so its scheme is already set by configuration. Only the vocabulary version IRI was still hard-coded to `http`, in two places: the metadata update and the release report. Both now use a helper, `vocabularyVersionIri`, that takes the scheme from the configured vocabulary IRI. The optional safeguard was implemented in preflight validation. It rejects a non-borrowed `rs.tdwg.org` term list whose scheme differs from its vocabulary's, and a vocabulary or term list already recorded under the other scheme.
- **`restxq.xqm`.** `page:canonical-iri` was added as above, and used in the twelve generic lookups for documents, document versions, vocabularies, vocabulary versions, term lists, and term list versions. The Darwin Core, `decisions`, and `index` special cases keep their fixed `http` IRIs. The serializer's IRI helpers (`page:expand-iri`, `page:wrap-turtle-iri`) already accepted `https://`, and needed no change.
- **`html.xqm`.** Implemented as above: the term version test, and the vocabulary "this version" IRI.
- **`dereferencing-test.py`.** Implemented as above for database examples. The document test also cut `current_iri` at a fixed position, which would garble `https` document IRIs; it now uses the same prefix handling. The checks of `https` RDF subjects are still to be added with the BDQ examples (Section 12.5).
- **Documentation.** `process/process-vocabulary.md` Section 3.3 now describes the rule. The `config.yaml` comments were not changed, because on `master` that file is the current Darwin Core release declaration, not a template.

**Tests.**

- *No change for existing vocabularies.* A dry run of the current Darwin Core 2026-10-13 release with the patched `process.py` passes preflight and proposes no file changes, and its output is identical to the unpatched processor's. Docker images built from `bdq` (unpatched) and `bdq-source` (patched) gave identical responses to 118 requests (existing documents and their versions, vocabularies and their versions, term lists and their versions, terms, Darwin Core special cases, `decisions`, `index`, and 404 cases, each with every Accept header and extension), apart from randomly generated blank node identifiers. `index/dereferencing-test.py` gave identical results against both (268 pattern, 312 document, and 120 legacy requests).
- *`https` resolution.* A test-only image (never committed) duplicated the `acorient` vocabulary, its term list, their versions, the `ac/doc/orient` document and its versions, and their standard part rows, under `https` IRIs. All of these resolved, with `303` responses followed by `200` responses whose RDF subjects are the `https` IRIs, and their HTML pages were generated. The vocabulary page's "This version" and "Latest version" links use `https`. The same paths return 404 on images without these records. The `html.xqm` term version test was checked directly in BaseX.
- *Observation (unchanged behavior).* A vocabulary's HTML page fails, with an empty 404, if the vocabulary is not a part of any standard, because `html:find-standard` requires exactly one standard. This does not affect BDQ, whose vocabularies `process.py` records as parts of the standard.

---

## 8. Deploying the simple vocabularies (`bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval`)

These are flat term lists and can go through the standard `process.py` pipeline described in `process/process-vocabulary.md` Section 3.

### 8.1 Structure in the TDWG hierarchy

With the namespaces BDQ already uses (e.g. `https://rs.tdwg.org/bdqdim/terms/`), `process.py` derives the vocabulary from the first path segment of the term list (`process/process.py:743-747`). Each prefix therefore becomes its own vocabulary with one term list:

| Level | IRI (example for `bdqdim`) |
|---|---|
| Standard | `http://www.tdwg.org/standards/NNN` (number to be assigned) |
| Vocabulary | `https://rs.tdwg.org/bdqdim/` |
| Vocabulary version | `https://rs.tdwg.org/version/bdqdim/YYYY-MM-DD` |
| Term list | `https://rs.tdwg.org/bdqdim/terms/` |
| Term list version | `https://rs.tdwg.org/bdqdim/version/terms/YYYY-MM-DD` |
| Term | `https://rs.tdwg.org/bdqdim/terms/Completeness` |
| Term version | `https://rs.tdwg.org/bdqdim/terms/version/Completeness-YYYY-MM-DD` |
| List of Terms document | `https://rs.tdwg.org/bdq/doc/dim/` |

This matches the Audiovisual Core precedent, where the subjectOrientation controlled vocabulary is its own vocabulary (`http://rs.tdwg.org/acorient/values/`) within the Audiovisual Core standard, with its List of Terms document at `http://rs.tdwg.org/ac/doc/orient/`.

`tg2/_build_review/temp_term-lists.csv` uses term list IRIs such as `https://rs.tdwg.org/bdq/bdqdim/`, which match neither the namespaces nor this pattern; it should be retired. The current List of Terms documents give "This version" as `https://rs.tdwg.org/bdqdim/terms/2026-06-03`, conflating the term list with the document; this should become a document version IRI such as `https://rs.tdwg.org/bdq/doc/dim/YYYY-MM-DD`.

### 8.2 Processing run

*Revised 2026-11-09 for the release-level `process.py` now on rs.tdwg.org `master` (`process/process-vocabulary.md` Sections 1.3, 2, and 3). Earlier revisions of this section described one run per vocabulary, each with its own `config.yaml` and `vocab.yaml`, and a separate `tdwg_docs_metadata_update.py` run per document. That workflow no longer applies: `vocab.yaml` is not used, and document metadata are processed by `process.py` from `config.yaml`.*

One run of `process.py` processes one complete release of one Standard. The BDQ standard is therefore one release, declared in one `config.yaml` and processed in one run, from the `process` directory: `python process.py --dry-run` to preview, then `python process.py`. The inputs, kept on `bdq-source`, are:

- **A release directory**, `process/bdq-revisions/bdq-revisions-YYYY-MM-DD/`. It holds one release-input CSV per namespace, named by prefix (`bdqdim.csv`, `bdqenh.csv`, `bdqcrit.csv`, `bdquc.csv`, `bdqval.csv`, and later `bdqffdq.csv` and `bdqtest.csv`), and a copy of the `config.yaml` used.
- **`process/config.yaml`**, the release declaration, with:
  - *release-level settings:* `standard: http://www.tdwg.org/standards/YYY`, `standard_label`, `standard_description`, `date_issued`, `local_offset_from_utc`, `decision_number`, `decisions_text`, `revision_directory: bdq-revisions`, `release_directory: bdq-revisions/bdq-revisions-YYYY-MM-DD`, and `document_defaults`;
  - *`vocabularies`:* one entry per BDQ vocabulary, with `vocabulary` (e.g. `https://rs.tdwg.org/bdqdim/`), `vocab_type`, `list_of_terms_iri`, `vocabulary_label`, `vocabulary_description`, `dc_creator`, `dcterms_license`, and one namespace (`namespace_uri: https://rs.tdwg.org/bdqdim/terms/`, `pref_namespace_prefix: bdqdim`, `database: bdqdim`, `label`, `description`, `borrowed: false`, `utility_namespace: false`, `new_term_list: true`, `termlist_uri: ''`, `prepend_url`, `use_namespace_in_fragment: true`, `separator: '_'`). With the per-vocabulary protocol change (Section 7.4), the `https` scheme of `vocabulary` and `namespace_uri` sets the scheme of everything minted for the vocabulary, and preflight validation rejects a vocabulary that mixes schemes;
  - *`documents`:* the complete list of the Standard's direct Documents. Each entry has its `document` IRI, its metadata (title, abstract, creator, media type, access URL, browser redirect URI), and its `contributors`. These entries replace the per-document `document_configuration.yaml` and `authors_configuration.yaml` files, so BDQ's existing files (Section 11.2) are converted into them. **Each vocabulary's `list_of_terms_iri` must also be declared here**, because the processor takes the List of Terms metadata from it. The List of Terms document IRIs (Section 11.3) are therefore needed, at least provisionally, before the first run.

`config.yaml` declares the complete current composition of the Standard, and rerunning the same release converges on the current inputs (`process-vocabulary.md` Sections 3.7 and 7.4). The release can therefore be built up in steps with the same `date_issued`. The first step covers the five simple vocabularies and their Lists of Terms; later steps add `bdqffdq`, `bdqtest`, and the other documents, rerunning each time. Each rerun reconciles the parts of the Standard and the Standard version snapshot to what `config.yaml` then declares.

`process.py` used to read only `process/config.yaml`, which on `master` holds the current Darwin Core release. Replacing it with the BDQ release declaration on `bdq-source` would conflict with every later change to it on `master`. `bdq-source` therefore adds a `--config PATH` option ([tdwg/rs.tdwg.org@7772340a](https://github.com/tdwg/rs.tdwg.org/commit/7772340a)). The BDQ declaration stays in its release directory, and the run is `python process.py --config bdq-revisions/bdq-revisions-YYYY-MM-DD/config.yaml`, leaving `process/config.yaml` unchanged. The default is unchanged, so this does not assume any particular branch arrangement. It was proposed to the rs.tdwg.org maintainers, and @tucotuco supports making the configuration location a parameter, with corresponding changes to the process documentation ([comment on #340](https://github.com/tdwg/bdq/issues/340#issuecomment-6744546653)). This fits the current recommendation to keep a copy of `config.yaml` in the active revisions directory (e.g. `process/dwc-revisions/dwc-revisions-2026-10-13/config.yaml`).

### 8.2.1 First run: bootstrapping the BDQ standard record

`process.py` creates the standard record itself when the configured standard does not exist yet (`update_standard_metadata`). There is no separate bootstrap step: the first BDQ run creates the standard, its first version, its parts, and the vocabularies and documents. On the `bdq-source` and `bdq` branches (Section 8.7):

1. **Standard IRI.** For the public review, use the placeholder `http://www.tdwg.org/standards/YYY` (see *Standard number* below), and replace it with the assigned number on ratification.
2. **Standard metadata.** Set `standard_label` and `standard_description` at the release level of `config.yaml`. They are used to create the standard row and the standard version row.
3. **Release date.** Preflight requires `date_issued` in `YYYY-MM-DD` form, so a placeholder date such as MIDS's `2026-MM-DD` is rejected. Use the date of the public-review processing run (Section 8.5).
4. **Decision.** `decision_number` and `decisions_text` are required. The processor creates a record `decision-{date_issued}_{decision_number}`, labelled "TDWG Executive Committee decision {decision_number}", in `decisions/decisions.csv`, and links each new or changed term to it in `decisions/decisions-links.csv`. A public review has no Executive Committee decision. *Decision for the public review:* `decision_number: YYY`, matching the standard number placeholder, with `decisions_text` stating that the terms are published for public review and are not ratified. This creates the record `decision-{date_issued}_YYY` on the `bdq` branch only. On ratification it is replaced by the real decision and the processing is rerun.
5. **Document IRIs.** *Decided 2026-11-09:* each List of Terms document IRI is `https://rs.tdwg.org/{vocabulary}/doc/list/`, e.g. `https://rs.tdwg.org/bdqval/doc/list/`. This mirrors the published location (`https://bdq.tdwg.org/draft/docs/list/bdqval/`, which becomes the `browserRedirectUri`), follows the Darwin Core pattern (`http://rs.tdwg.org/dwc/doc/list/`), and is served by the existing document route (Section 11.3). Declare these documents in `documents`.
6. **Run.** Commit the inputs on `bdq-source` and bring them into `bdq`. On `bdq`, run `python process.py --dry-run`, then `python process.py`, and commit the output.
7. **Inspect** `standards/standards.csv`, `standards/standards-parts.csv`, `standards/standards-versions.csv`, `standards-versions/*`, `decisions/*`, the vocabulary, term list, and document tables, and the release report and log (`process/reports/release-report-YYYY-MM-DD.md`, `process/logs/process-YYYY-MM-DD.log`). The processor leaves `status`, `category`, and `citation` empty in a new standard row. `bdq-source` adds optional release settings `standard_status` and `standard_category` ([tdwg/rs.tdwg.org@2e42cc7d](https://github.com/tdwg/rs.tdwg.org/commit/2e42cc7d)). *Decided:* `standard_status: Draft Standard` for the public review; the category is not set.

`process.py` marks the new standard version, and the new term, term list, and vocabulary versions, `recommended`. *Decided 2026-11-09:* keep `recommended`. Semantically, that is what the draft asserts: these are the versions it recommends. Existing data uses only `recommended`, `superseded`, and `deprecated`, so a separate value such as `public-review` would need a processor change and could break consumers that select recommended versions. The draft status is carried by the standard record (`Draft Standard`, step 7) and the placeholder decision (step 4).

**Standard number.** Checked on rs.tdwg.org `master` as of 2026-11-09:

- *Numbers in use* (`standards/standards.csv`, `docs/docs.csv`): 101–117 (prior standards, and ABCD, SDD, TCS), 147 (SDS), 150 (GUID AS), 312 (NCD), 449 (TAPIR), 450 (Darwin Core), 638 (Audiovisual Core), 640 (ABCDDNA), 642 (VMS), 643 (Latimer Core, 2024). The numbers are not in date order (SDS and VMS, both 2017, are 147 and 642); they appear to come from the former TDWG website, which now uses slugs (`/standards/dwc/`), and `/standards/639/`, `/641/`, and `/644/` return 404. The next number in sequence would be 644, but MIDS is also in public review and may be ratified first. The number is assigned by TDWG.
- *Placeholders used before.* `x` in the rs.tdwg.org templates (`process/files_for_new_template/new_standard.csv`) and in `config.yaml` comments for Latimer Core before 643 was assigned; `12345` on the unratified `efg` branch (2021); `XXX`, with version date `2026-MM-DD`, on the `mids` public-review branch (2026), which ran `process.py` with it; `nnn` in old rs.tdwg.org README files. Latimer Core was set up after ratification and never used a placeholder.
- *A real number is not needed for processing.* rs.tdwg.org does not route standard IRIs (they resolve on `www.tdwg.org`), so the number is metadata only. The earlier `process.py` took the number from the IRI as a string, which a placeholder satisfies, and the current `process.py` does not extract it at all. (Earlier revisions of this document said a real number was a prerequisite; that was wrong.)
- *Decision for the public review:* `http://www.tdwg.org/standards/YYY`, following the MIDS pattern but distinct from MIDS's `XXX`, since MIDS is still in review. The placeholder becomes part of the standard and standard version IRIs on the `bdq` branch, so on ratification it is replaced in the inputs on `bdq-source` and the processing is rerun (Section 8.7).

BDQ documents still contain other placeholders (`https://www.tdwg.org/standards/nnnn`, `http://example.org/to_be_determined`).

For each new term list, `process.py` creates the dataset directories, `constants.csv`, `namespace.csv`, mapping and classes files, and the rows in `index/index-datasets.csv`, `term-lists/term-lists.csv`, and `html/redirects.csv`, from the templates in `process/files_for_new/`.

### 8.3 Column conversion

*Revised 2026-11-09.* The mapping is taken from the RDF that BDQ already publishes for these vocabularies: `tg2/_review/dist/bdq{dim,enh,crit,uc,val}.xml`, written by `tg2/_build_review/draft_build-termlist.py`. That RDF describes term versions; the same properties apply to the terms.

**Vocabulary type.** Use `vocab_type: 2`, the simple controlled vocabulary template (`simple-cv-column-mappings.csv`), not type 1 as an earlier revision proposed. BDQ's RDF uses `skos:inScheme` and `rdf:value`, which are in the type 2 template, and does not use `tdwgutility:organizedInClass`, which only the type 1 template has. `bdqval` also contains `skos:Concept` terms.

**Definitions.** As in BDQ's RDF and in rs.tdwg.org practice since 2017 (all term vocabularies, and all templates for new term lists), `definition` is mapped to both `rdfs:comment` (for backward compatibility) and `skos:definition`, with language `en`. The template rows are kept unchanged.

| BDQ column | Predicate in BDQ's RDF | rs.tdwg.org input column and mapping |
|---|---|---|
| `term_localName` | (subject) | `term_localName` |
| `label` | `rdfs:label`, `@en` | `label` → `rdfs:label`, `@en`. The template's second row, `label` → `skos:prefLabel`, is replaced by the next row. |
| `prefLabel` | `skos:prefLabel`, `@en` | new column `prefLabel` → `skos:prefLabel`, `@en` |
| `definition` | `rdfs:comment` and `skos:definition`, `@en` | `definition`, as in the template |
| `comments` | `skos:note`, `rdf:XMLLiteral` (content wrapped in `<div xmlns="http://www.w3.org/1999/xhtml">`) | `notes` → `skos:note`, datatype `rdf:XMLLiteral`, replacing the template's `dcterms:description`. Each cell holds the complete XHTML `div`. Empty cells emit nothing, whereas BDQ's RDF has an empty `div`. |
| `rdf_type` | `rdf:type`, one per comma-separated value | `type`, and a new column `type1`, both → `rdf:type`, as full IRIs. Only `bdqval`'s `bdqffdq:Parameter, owl:NamedIndividual` rows use `type1`. |
| (fixed) | `skos:inScheme` the term list IRI (e.g. `https://rs.tdwg.org/bdqdim/terms/`) | `skos_inScheme`, holding the full term list IRI. The template's namespace prefix is removed from the mapping, because Darwin Core uses this column for a concept scheme term's local name. |
| `term_localName` | `rdf:value` | `controlled_value_string` → `rdf:value`, plain literal, filled from `term_localName` |
| `hasFitnessRequirements` (`bdquc`) | `bdqffdq:hasFitnessRequirements`, `rdf:XMLLiteral` | new column `hasFitnessRequirements`, same predicate and datatype; `bdqffdq` is added to `namespace.csv` |
| `scopeNote` (`bdquc`) | `skos:scopeNote`, `xsd:string` | `usage` → `skos:scopeNote`, datatype `xsd:string` instead of the template's `@en` |
| `organized_in` | not emitted | dropped |
| `iri`, `term_iri`, `issued`, `status` | version metadata | generated by `process.py` |
| `flags` | not emitted | dropped |

The same changes are made to the versions mapping (`simple-cv-versions-column-mappings.csv`), so that term version RDF matches as well.

**Mapping files.** `process.py` always creates a new term list's mapping files from the templates and has no option for a custom mapping. As `process/process-vocabulary.md` Section 3.10 describes, the generated files are edited after the first run. To keep this reproducible, the BDQ mapping files (`<db>-column-mappings.csv`, `<db>-versions-column-mappings.csv`, and `namespace.csv` for each dataset) are kept as inputs on `bdq-source`, in `process/bdq-revisions/bdq-revisions-YYYY-MM-DD/mappings/<dataset>/`, and copied into the dataset directories after `process.py` has run. `process.py` never reads them; they are used only when BaseX loads the data.

**Conversion.** A conversion script reads `tg2/_review/vocabulary/*_term_versions.csv`, the List of Terms `document_configuration.yaml` files, and `authors_configuration.yaml`. It writes the release-input CSVs (all five with the same columns), the mapping files, and the release `config.yaml`. It checks that every XML literal is well-formed. Four `hasFitnessRequirements` values and one `comments` value contain `<ul><li>` markup.

The script is `process/bdq-revisions/bdq_to_rs.py` on `bdq-source` (commit `c513a26c`). It produced the inputs in `process/bdq-revisions/bdq-revisions-2026-11-09/` (commit `c87d2a06`) from this repository's `master` at `10a5d682`, and rerunning it reproduces them exactly. **It is for the public review only.** It is a one-way bootstrap from the files in this repository, not part of the rs.tdwg.org workflow, and is intended to be replaced by authoritative information kept in `rs.tdwg.org` (Section 6). From now on, the release-input CSVs, `config.yaml`, and mapping files on `bdq-source` are the source and are edited directly. Rerunning the script would overwrite those edits. The script's header and the `bdq-revisions/README.md` say this.

**Checks (scratch copy of `bdq-source`, 2026-11-09).**

- `process.py --dry-run` and a full run of the five vocabularies succeed.
- In the shared tables, only BDQ rows are added. The one change to existing rows is the modification date of six shared datasets in `index/index-datasets.csv`, which `process.py` updates when a release adds records to them (`process-vocabulary.md` Section 4.8).
- Every new BDQ IRI uses `https`.
- The triples produced by applying the BDQ mappings to the generated current-term CSVs, following the serializer's rules for `iri`, `language`, `datatype`, and `plain`, equal BDQ's own RDF for all 44 terms. The only differences are the `dcterms:created` and `dcterms:modified` that rs.tdwg.org adds, and the 9 empty `skos:note` values in BDQ's `bdqval` RDF, which rs.tdwg.org does not emit.

**Rerunning.** A release that creates new term lists cannot currently be rerun with the same `date_issued`. With `new_term_list: true`, preflight rejects the term lists, which now exist. With `false`, processing fails, because a term list that is not new must have an earlier version. The same happens to the release's new documents (e.g. the Lists of Terms).

*Evaluation (2026-11-09).* This is a gap in `process.py`, not a safeguard:

- `process/process-vocabulary.md` (Sections 3.7 and 7.4) makes same-release idempotence the intended invariant ("processing the same release again produces no repository metadata changes"), and makes correcting an input and rerunning on the same branch the supported workflow, instead of recreating the branch.
- Reruns already work for existing term lists: rerunning the Darwin Core 2026-10-13 release proposes no changes. Vocabularies and standards already handle a version created earlier in the same release (`alreadyAddedVocab`, `alreadyAddedStandard`). Only term lists and documents that the release itself creates lack this, so the gap affects every new standard, vocabulary, or term list, including MIDS.
- What protects a published release in deployment is the version date. A new `date_issued` creates new versions that supersede the old, while a same-date rerun rewrites the versions of that date. Refusing same-date reruns protects nothing that the date does not already protect.

*Fix, committed on `bdq-source` (`7f0120b9`, pushed 2026-11-09; not yet on rs.tdwg.org `master`).* Treat a term list or document whose only versions are dated `date_issued` as created by this release, with no predecessor, as the first run did. The changes are a small helper in `generate_current_terms_metadata` and an early return in `_document_predecessor`. With them, rerunning the BDQ release (`new_term_list: false`) changes no files, and a further dry run proposes none. Correcting one definition and rerunning changes exactly that term and its same-date version, in place. The BDQ mapping files are kept, because templates are copied only when `new_term_list` is `true`. The fix is a single commit that applies cleanly to `master`, for the rs.tdwg.org maintainers to consider. With it, the BDQ release can be rerun on `bdq` after correcting its inputs; after the first run, `new_term_list` is set to `false`.

**Whitespace.** Five BDQ definitions end with a space (`bdqcrit:Consistent`, `bdquc:SDM-Trees`, `bdquc:Spatial-Temporal_Patterns`, `bdqval:Empty`, `bdqval:NotEmpty`). The rs.tdwg.org loader trims it, so the conversion trims trailing whitespace from plain-text fields, and the input CSVs match what is served.

**Served output (local Docker image, 2026-11-09).** All 44 terms were fetched as Turtle, RDF/XML, and JSON-LD, and compared with BDQ's RDF. Turtle and RDF/XML match, apart from the whitespace above and the empty notes. JSON-LD loses one of the two `rdf:type` values of the 16 `bdqval` terms typed `bdqffdq:Parameter` and `owl:NamedIndividual`. This is an existing rs.tdwg.org bug: the JSON-LD serializer writes a repeated predicate as duplicate keys in one JSON object, and JSON parsers keep only the last. It also affects production: in the current data, 29 records have two `dcterms:replaces` values (10 Darwin Core terms and 13 term versions, for example `http://rs.tdwg.org/dwc/terms/eventDate`; 2 terms and 2 versions in `dwcore`; 1 term and 1 version in `curatorial`). An earlier revision of this section also counted the multilingual values in `dwc-translations`; those records repeat `skos:prefLabel` and `skos:definition`, but they do not appear to be served (Section 15, question 11).

*Fix (2026-11-09).* The JSON branch of `page:describe-resource` in `html/restxq.xqm` now groups the pairs by predicate and writes one key with an array when a predicate has more than one value (commit `fcac8741` on `bdq-source`, a single commit that applies cleanly to `master`). Tested on a local image: of 308 resources in four formats, only the JSON-LD of resources with duplicate keys changed, and the fixed JSON-LD is valid and isomorphic to the Turtle. It is deployed on `bdq-public-review.rs.tdwg.org`, e.g. `https://bdq-public-review.rs.tdwg.org/dwc/terms/eventDate.json`. Reported to the rs.tdwg.org maintainers as [tdwg/rs.tdwg.org#619](https://github.com/tdwg/rs.tdwg.org/issues/619).

### 8.4 Data problems to fix before import

*Status 2026-11-09.* The first two problems do not affect the import, because `iri` and `term_iri` are generated by `process.py`. The mapping follows BDQ's RDF, which takes `rdf:value` from `term_localName`, so the third problem does not reach rs.tdwg.org either. Its content still needs a decision by the BDQ maintainers. The `controlled_value_string` column differs from the local name for `bdquc:SDM-Trees` and `bdquc:Spatial-Temporal_Patterns`, and the fitness requirements of `SDM-Trees` refer to a term that does not exist.

- `bdqenh` and `bdqcrit` version IRIs lack `/version/` (e.g. `https://rs.tdwg.org/bdqenh/terms/AssumedDefault-2024-09-30`).
- The `term_iri` values for `bdquc:SDM-Trees` and `bdqval:AggregatedTestResponseOutcomes` contain `/version/`.
- `bdquc:SDM-Trees` has controlled value `Species-Distribution-Modeling-Trees`, which does not match its local name, and its fitness requirements refer to `bdquc:Species-Distribution-Modeling-Trees`. `bdquc:Spatial-Temporal_Patterns` has controlled value `Spatial-Temporal Patterns`.

### 8.5 Version dates

`process.py` gives every version created in a run the single `date_issued` from `config.yaml`. The version IRIs currently cited in BDQ documents (`…-2024-09-30`, `…-2026-04-22`) will not exist on rs.tdwg.org. The first rs.tdwg.org version of each term should carry the date of the processing run (for the public review) and, after ratification, the ratification date; BDQ documents must be regenerated to cite the rs.tdwg.org version IRIs.

*Decided 2026-11-09:* on `bdq-public-review.rs.tdwg.org`, the BDQ draft dates become term versions, so that the review site shows what the term versions will look like in production. In the draft these versions are placeholders (that happen to reflect the terms' history); on ratification and going to production, they become real term versions with the release date. Each BDQ source term has one version, dated when its current content last changed (`issued` in the `*_term_versions.csv` files, `dcterms:issued` in `bdqffdq.owl`). The dates belong on the term versions (SDS Section 4.3: `dcterms:issued` of a version; `dcterms:created` and `dcterms:modified` of the current term), not in the ontology. The release is replayed as a sequence of draft releases, one per date, each adding the terms whose content dates from it, with that term's faithfully converted content:

| Date | Terms first versioned |
|---|---|
| 2024-04-13 | `bdqffdq`: 1 (`Response`) |
| 2024-09-30 | `bdqdim` 6, `bdqenh` 5, `bdqcrit` 8; `bdqffdq` 100 |
| 2026-03-23 | `bdqffdq`: 1 (`hasFitnessRequirements`) |
| 2026-04-13 | `bdqffdq`: 4 (the four Response subclasses) |
| 2026-04-22 | `bdquc` 3, `bdqval` 19 |
| 2026-04-23 | `bdqval` 1 (`AggregatedTestResponseOutcomes`); `bdqffdq` 1 (`aggregatesResponsesFrom`, which has no date in `bdqffdq.owl`; added on 2026-04-23 in tdwg/bdq `fe55c9ff`, with `AggregatedTestResponseOutcomes`) |
| 2026-04-26 | `bdquc` 1 |
| 2026-04-27 | `bdqval` 1 |
| 2026-05-16 | `bdqffdq`: 2 (`QualityAssurance`, `QualityControl`) |
| 2026-11-09 | the decided `bdqffdq` changes (Section 9.5): new versions only of the terms whose rows change |

The version IRIs then follow rs.tdwg.org's pattern with the BDQ dates (e.g. `https://rs.tdwg.org/bdqdim/terms/version/Completeness-2024-09-30`), which also resolves the version IRIs cited in BDQ documents, except for the `bdqenh` and `bdqcrit` IRIs that lack `/version/` (Section 8.4). Each draft release declares the composition of the standard at that date (the vocabularies that exist, and their Lists of Terms), so standard, vocabulary, and term list versions follow the same dates. On `bdq`, the derived output of the single 2026-11-09 run is reverted with new commits and the sequence is processed, so no force-push is needed. `bdqtest` follows the same approach when it is deployed.
### 8.6 Redirects for HTML

`process.py` writes the `html/redirects.csv` row from `prepend_url`, `use_namespace_in_fragment`, and `separator` (`process/process.py:632-673`; `process/process-vocabulary.md:73-77`). The BDQ List of Terms documents already use anchors of the form `bdqdim_Completeness`, so `use_namespace_in_fragment: true` and `separator: '_'` fit, with `prepend_url` set to the published List of Terms URL plus `#` (currently `https://bdq.tdwg.org/draft/docs/list/bdqdim/#`; this should be changed to the final location before release).

### 8.7 Branch workflow

`process/process-vocabulary.md` Section 2.3 separates a source branch (steps 1-10, input files only) from a disposable derived branch (steps 11-17, generated files), so that the processing can be rerun from clean inputs. Because the `bdq` branch is the deployed branch (Section 1.4), it has to be the **derived** branch; the inputs should be kept on a separate source branch (e.g. `bdq-source`). To revise, correct the inputs on the source branch, then recreate `bdq` from it and rerun the processing. After ratification, a pull request from the source branch into `master` is merged by the rs.tdwg.org maintainers, who rerun the processing with the ratification date.

**Status (2026-11-09).** On `rs.tdwg.org`:

- `bdq` is the derived, deployed branch. `origin/master` (`18a520dc`) was merged into it (merge commit `b5b3d28c`), so its files are again identical to `master`'s before any BDQ content is added.
- `bdq-source` (the source branch) was created from that merge commit. It holds only the hand-edited inputs: release-input CSVs, `config.yaml` (including the document declarations), column mapping edits, and the code patches in Section 7.4.
- Only these two branches of `rs.tdwg.org` receive commits for this work. `master`, releases, and production `rs.tdwg.org` are unchanged. Commits reference tdwg/bdq#340.
- `bdq-source` (pushed 2026-11-09, at `c513a26c`) holds, besides the protocol patches (Section 7.4): the `--config` option and optional `standard_status` / `standard_category` settings (Section 8.2), the same-release rerun fix and the JSON-LD fix (Section 8.3), and the inputs for the five simple vocabularies, with the review-only conversion script (Section 8.3, *Conversion*).
- **The five simple vocabularies are deployed** (2026-11-09). `bdq-source` was merged into `bdq` (`c6633213`), the release was processed with `process.py --config bdq-revisions/bdq-revisions-2026-11-09/config.yaml`, the BDQ mapping files were copied into place, and the output was committed separately (`7990425b`, 132 files). In the shared tables only BDQ rows were added, apart from the six modification dates in `index/index-datasets.csv` (Section 8.3, *Checks*). A local Docker image of that checkout was checked, and `index/dereferencing-test.py` passed (760 requests, no errors). After the push, GBIF rebuilt https://bdq-public-review.rs.tdwg.org. It gives the same responses over `http` and `https`, and the dereferencing test passes against it. Term IRIs redirect browsers to the `/draft/` Lists of Terms, and all versions are dated 2026-11-09. Next: `bdqffdq` and `bdqtest` (Section 14, steps 3 and 4), which need the decisions in Section 15.
- *2026-11-10:* rs.tdwg.org `master` `9aa8f5a6` (deletion of `standards/standards.ttl`, tdwg/rs.tdwg.org#620; data-only) merged into `bdq-source` (`3d89aa65`) and from there into `bdq` (`1b1ab375`), without reprocessing.
- `master` is under active development, including the processing code (`process/`, `html/*.xqm`), not only standards data. Its new commits are reviewed regularly and merged by agreement: first into `bdq-source`, then into `bdq`. If `bdq` already holds processing output and `master` changes the shared tables that `process.py` writes, `bdq` is rebuilt from `bdq-source` and the processing is rerun, rather than resolving CSV conflicts by hand. Changes to the processing procedure on `master` are reflected in this plan.

---

## 9. Options for `bdqffdq`

### 9.1 Option A: ABCD-style redirect to a file published from this repository

The ontology file stays in `tdwg/bdq`, is published on `bdq.tdwg.org` (GitHub Pages), and rs.tdwg.org only redirects, following `html/restxq.xqm:772-814`: a route `/bdqffdq/terms/{path}` returns a 303 to `https://bdq.tdwg.org/…/bdqffdq.ttl`, `.rdf`, or `.jsonld` according to the Accept header, and to `https://bdq.tdwg.org/…/list/bdqffdq/#bdqffdq_{path}` for HTML.

This mechanism works with `bdq.tdwg.org`:

- Literal path segments take priority over the generic `/{vocab}/{ns}/{local-id}` route in RESTXQ, as the ABCD route already relies on.
- GitHub Pages serves `.ttl` as `text/turtle` with `access-control-allow-origin: *` (checked for `https://bdq.tdwg.org/draft/vocabulary/bdqffdq.ttl`).
- A 303 from each term IRI of a slash namespace to the whole ontology document is a standard linked data pattern.

Caveats:

1. `bdqffdq.owl` is Turtle, but GitHub Pages serves `.owl` as `application/rdf+xml`. A redirect for RDF/XML must point to a real RDF/XML serialization (e.g. `bdqffdq.rdf` generated with rdflib in the build); likewise JSON-LD.
2. The ontology IRI `https://rs.tdwg.org/bdqffdq/terms` (no trailing slash) is matched by the term list route (`/{namespace}/{local-id}`, `html/restxq.xqm:289-310`), not by `/bdqffdq/terms/{path}`; it needs its own route. The version IRI `…/bdqffdq/terms/1.0` would be caught by `{path}` and redirected to the current ontology rather than to version 1.0.
3. Redirect targets are hard-coded in `restxq.xqm`, so changing them needs an rs.tdwg.org release. `/draft/` is not a stable location. The ABCD precedent illustrates the risk: `https://abcd.tdwg.org/ontology/abcd_concepts.ttl`, a current ABCD redirect target, returns 404.
4. Individual `bdqffdq` terms get no rs.tdwg.org records: no term versions, no presence in the term list or vocabulary hierarchy, no `dump`.
5. **The source of truth stays in `tdwg/bdq`, which does not meet the target in Section 6.**

Effort: small (one route in `restxq.xqm`, serializations in the BDQ build).

### 9.2 Option B: the whole ontology file stored in rs.tdwg.org

The Turtle file lives in the rs.tdwg.org repository (e.g. `bdqffdq/bdqffdq.ttl`) and is edited there (with Protégé or carefully by hand). Either:

- **B1:** `restxq.xqm` returns the file directly with the right media type (`file:read-text` on `/usr/src/rs.tdwg.org/bdqffdq/…`), with pre-generated `.rdf` and `.jsonld` files alongside. This is a new pattern for rs.tdwg.org, needing review by its maintainers; or
- **B2:** the BDQ build copies the file from rs.tdwg.org to `bdq.tdwg.org`, and rs.tdwg.org redirects as in Option A.

Assessment: meets the target that the source is in rs.tdwg.org, but not as CSV. Caveats 2 and 4 of Option A still apply; caveat 3 applies to B2. Term-level versioning is whatever the ontology file records (currently only `owl:versionIRI` and per-term `dcterms:issued`), outside the TDWG version model. Effort: small to moderate.

### 9.3 Option C (decided): hybrid, term list CSV plus axioms file

*Decided 2026-11-09.* The design as carried out is in Section 9.5.

Term metadata is maintained as an ordinary rs.tdwg.org term list processed by `process.py`; the few triples that cannot be rows are kept in a small Turtle file in rs.tdwg.org; the complete ontology is generated by merging the two.

Why it is feasible: except for 78 blank-node triples, every triple in `bdqffdq.owl` is an IRI- or literal-valued property of a named term, with bounded multiplicity (at most 3 `rdfs:subClassOf`, 4 `rdfs:subPropertyOf`, 2 `rdf:type`, 2 `owl:differentFrom` per term; Section 3.2), which fixed repeated columns handle (Section 2.2).

What is needed:

1. **Term list.** A term list `https://rs.tdwg.org/bdqffdq/terms/` in vocabulary `https://rs.tdwg.org/bdqffdq/`, database `bdqffdq`, created by `process.py` with a custom column mapping. Input columns and mappings:

   | Column | Predicate | Mapping type |
   |---|---|---|
   | `term_localName` | (subject) | |
   | `label` | `rdfs:label` | language `en` |
   | `prefLabel` | `skos:prefLabel` | language `en` |
   | `definition` | `rdfs:comment`, `skos:definition` | language `en` |
   | `notes` | `skos:note` | language `en` |
   | `usage` | `skos:scopeNote` | language `en` |
   | `type`, `type1` | `rdf:type` | iri |
   | `subClassOf`, `subClassOf1`, `subClassOf2` | `rdfs:subClassOf` | iri |
   | `subPropertyOf`, `subPropertyOf1`, `subPropertyOf2`, `subPropertyOf3` | `rdfs:subPropertyOf` | iri |
   | `range` | `rdfs:range` | iri (only where the range is a named class or datatype; restriction ranges go in the axioms file) |
   | `controlled_value_string` | `rdf:value`, as in the template and SDS 4.5.4; replaced by `skos:notation` in the generated OWL serializations (Sections 3.2, 9.5) | plain |
   | `differentFrom`, `differentFrom1` | `owl:differentFrom` | iri |

   The per-term `dcterms:issued` in the ontology is replaced by the `dcterms:created`/`dcterms:modified` and term versions that `process.py` generates. `namespace.csv` needs `owl`, `skos`, and `bdqffdq` entries. The generated ontology must declare the annotation properties it uses (`skos:prefLabel`, `skos:definition`, `skos:note`, `skos:scopeNote`, `skos:notation`, `dcterms:created`, `dcterms:modified`, and any others in the mapping), or it will not be OWL 2 DL.

2. **Axioms file.** This is what the SDS (Section 4.4.2.2) calls a *vocabulary extension term list*: axioms asserted in a document separate from the basic term list, itself typed `owl:Ontology`, while the basic term list SHOULD NOT be declared an `owl:Ontology`. Whether it gets its own term list IRI (e.g. `https://rs.tdwg.org/bdqffdq/axioms/`), as in the SDS example, is open. `bdqffdq/bdqffdq-axioms.ttl` in rs.tdwg.org containing the ontology header (`owl:Ontology`, label, notes, license, `owl:versionIRI`), the 15 `owl:Restriction` ranges, and the 2 `owl:AllDisjointClasses` axioms, i.e. about 80 triples. It is edited by hand when those structures change, which is rare.

3. **Merge step.** A script (in rs.tdwg.org `process/`, or in this repository reading from rs.tdwg.org) builds `bdqffdq.ttl`, `.rdf`, and `.jsonld` from `bdqffdq/bdqffdq.csv` plus the axioms file, using the same column mappings. When first built, it should be checked for graph isomorphism against the current `bdqffdq.owl` (rdflib `isomorphic`), apart from the intended changes (`dcterms:issued`, version IRI).

4. **Serving.**
   - Term IRIs (`https://rs.tdwg.org/bdqffdq/terms/{term}`) dereference through the generic handler from the term list: labels, definitions, types, subclass and subproperty links, named ranges, versions. Restriction ranges are absent from term-level responses.
   - The whole ontology is served either from generated files in rs.tdwg.org (a route like Option B1) or from `bdq.tdwg.org` (a redirect like Option A).
   - The ontology IRI `https://rs.tdwg.org/bdqffdq/terms` and the term list IRI `https://rs.tdwg.org/bdqffdq/terms/` resolve through the same handler (`html/restxq.xqm:289-310`). Either they are treated as the same resource, with that route (once patched for `https`, Section 7.2) returning the term list, which links to the ontology serializations, or a dedicated route returns the ontology.

5. **Ontology version IRI.** Replace `owl:versionIRI <https://rs.tdwg.org/bdqffdq/terms/1.0>` with the term list version IRI that `process.py` generates (`https://rs.tdwg.org/bdqffdq/version/terms/YYYY-MM-DD`), so the ontology version and the TDWG version hierarchy coincide. This also avoids `1.0` being read as a term local name.

6. **Editing workflow.** Term additions and changes go through the normal modification CSV and `process.py`; axiom changes are edits to the axioms file on the same source branch; the merge step is rerun. Editing in Protégé is no longer the primary workflow (Protégé can still be used to check the merged file).

Assessment: meets the target (source in rs.tdwg.org, term metadata in CSV), gives `bdqffdq` terms the same TDWG version history and dereferencing as other vocabularies, and keeps the graph-native parts in RDF. Costs: a custom mapping file, a merge script, the risk of the two sources drifting (mitigated by the isomorphism check and a check that every IRI in the axioms file is a term in the CSV), and term-level responses that omit restriction ranges. Effort: moderate.

### 9.4 Option C without an axioms file: a blank-node-free ontology

If the BDQ maintainers make the two changes in Section 3.3 item 2 (named-class ranges instead of the 15 restrictions, pairwise `owl:disjointWith` instead of the 2 `owl:AllDisjointClasses` axioms), the whole ontology fits the term list of Option C:

- the `range` column holds every property's range;
- a `disjointWith` column set holds the disjointness statements (at most 3 per class for the current axioms, so `disjointWith`, `disjointWith1`, `disjointWith2`);
- the ontology header (`owl:Ontology`, label, notes, license, `owl:versionIRI`) is the only content left outside the term list. It can be a few lines in the generating script's configuration, or be generated from the term list and vocabulary records in rs.tdwg.org.

Term-level responses from rs.tdwg.org then carry every statement about each term, and the whole ontology is simply the union of the term records plus the header, so there is nothing to drift. The merge step reduces to serializing the term list in three formats, and the ontology stays in OWL 2 DL.

Future ontology changes that need class expressions (for example, unions or cardinality restrictions) would bring back the need for an axioms file, so the option C machinery should be kept available.

Assessment: the simplest way to make rs.tdwg.org CSV the complete source of truth for `bdqffdq`. It depends on a modeling decision by the BDQ maintainers about the 15 ranges, which should be made before the public review, since it changes the ontology's meaning. Effort: small, beyond Option C's term list.

### 9.5 Decision: Option C, with the ontology generated in rs.tdwg.org

*Decided 2026-11-09:* Option C. Term metadata is a term list CSV, and a parallel axioms file holds what cannot be rows. Both are kept and processed in rs.tdwg.org in the same way, and a replicable, valid OWL ontology is generated from them in several serializations by a generator in rs.tdwg.org. The whole-ontology files are artifacts of the BDQ build in `tg2/_review/dist/` (Section 6.4), separate from the per-term responses that rs.tdwg.org serializes on demand. This follows the layered approach of SDS Section 4.4.2.2, *Vocabulary extension term lists*: axioms are asserted in a document separate from the basic term list, the basic term list is not itself declared an `owl:Ontology`, and an enhanced vocabulary combines the two (SDS's example is Audubon Core with an axioms term list of `owl:Restriction`s). The axioms file is such an extension term list, and the generated ontology is the combination. Section 9.4 remains possible later: if the BDQ maintainers remove the blank nodes (Section 15, question 6), the axioms file shrinks to the ontology header, and nothing else changes.

Design:

1. **Inputs, on `bdq-source`.** In the BDQ release directory, beside the other vocabularies' inputs: `bdqffdq.csv` (the release-input CSV, with the columns of Section 9.3 item 1), the column mapping files and `namespace.csv` in `mappings/bdqffdq/` and `mappings/bdqffdq-versions/`, and `bdqffdq-axioms.ttl`. The axioms file holds the ontology header (label, notes, license; `owl:versionIRI` is filled in by the generator) and the axioms that need blank nodes: the 15 restriction ranges and the 2 `owl:AllDisjointClasses` axioms.
2. **Processing.** `bdqffdq` is added to the BDQ release `config.yaml` and processed by `process.py` with the other vocabularies, as a rerun of the same release (Section 8.2). Like the mapping files, the axioms file is then copied into the dataset directory (`bdqffdq/bdqffdq-axioms.ttl`), so that `bdq` holds the current axioms next to the current terms (`bdqffdq/bdqffdq.csv`), and each release directory keeps the inputs of that release. The axioms file is not loaded into BaseX: term-level responses carry everything in the term list, but not the restriction ranges or disjointness axioms. *Superseded 2026-11-09 by Section 9.6:* `process.py` now handles the axioms file itself, as the extension term list, and rs.tdwg.org serves the axioms with that list's RDF.
3. **Generator, in rs.tdwg.org.** *Decided 2026-11-09: a general tool, not specific to BDQ, documented with how to describe an ontology in rs.tdwg.org* (a term list with its column mappings, plus an axioms file for what cannot be rows), so that other standards can use it. A script reads a dataset directory (the current-term CSV, its column mappings, `namespace.csv`, and the axioms file) and the term list version from `term-lists-versions/`, and writes the ontology as Turtle, RDF/XML, and JSON-LD. It applies the column mappings with the serializer's rules (`iri`, `language`, `datatype`, `plain`), so the ontology and the per-term responses state the same thing. It sets `owl:versionIRI` to the term list version IRI (Section 9.3 item 5) and declares every annotation property it uses. Output is deterministic, so the same inputs always give the same files. The files are written outside the repository by default and are not committed to rs.tdwg.org; the BDQ build runs the generator against a checkout of rs.tdwg.org and writes them to `dist/`.
4. **Validity.** The generator fails if: the axioms file refers to a `bdqffdq` IRI that is not a term in the CSV; a term has no `rdf:type`; or the result is not OWL 2 DL (checked with the OWL API profile checker, e.g. `robot validate-profile --profile DL`). On the first build, the result is compared with `bdqffdq.owl` for graph isomorphism, apart from the intended differences (`dcterms:issued` replaced by `dcterms:created`/`modified`, the version IRI, and the annotation fixes below).
5. **Layer-appropriate serializations.** *Decided 2026-11-09.* rs.tdwg.org keeps the TDWG conventions, and the generator makes the OWL serializations OWL 2 DL without forcing any ontology produced with it into OWL 2 Full:
   - the term list keeps `rdf:value` for controlled value strings (SDS 4.5.4), so term-level responses from rs.tdwg.org follow TDWG convention and match BDQ's other vocabularies;
   - in the OWL serializations, the generator replaces `rdf:value` with `skos:notation`, declared as an annotation property, rather than dropping it, so the value string is kept. This is a general, documented rule of the tool (a table of reserved-vocabulary annotation properties and their substitutes, with `rdf:value` → `skos:notation` as the default), and the generated ontology states it in a note;
   - the generator declares the other annotation properties it uses (e.g. `skos:scopeNote`).
   The layers then differ in one known, documented way. SKOS uses `skos:notation` for codes that identify a concept within a scheme, usually with a datatype; a plain literal is allowed. Whether rs.tdwg.org should also emit `skos:notation` beside `rdf:value` at term level is left open.
6. **Data preparation.** The first inputs are converted from `tg2/_review/vocabulary/bdqffdq.owl`, as the simple vocabularies' inputs were (Section 8.3), with `rdf:value` kept as `controlled_value_string`.

*Decisions of 2026-11-09 (continued):*

- **IRIs, following SDS Section 4.4.2.2.** The ontology IRI is the vocabulary IRI `https://rs.tdwg.org/bdqffdq/` (the "enhanced vocabulary", typed both `tdwgutility:Vocabulary` and `owl:Ontology`), replacing `https://rs.tdwg.org/bdqffdq/terms`; `owl:versionIRI` is the vocabulary version IRI. The basic term list `https://rs.tdwg.org/bdqffdq/terms/` is not declared an `owl:Ontology`. The axioms file is the extension term list `https://rs.tdwg.org/bdqffdq/extension/` (typed `owl:Ontology`), matching BDQ's existing Vocabulary Extension document. `process.py` has no notion of a term list holding only axioms, so recording the extension term list needs a change to `process.py` (to be designed).
- **`skos:notation` at term level too.** The `bdqffdq` term list maps `controlled_value_string` to both `rdf:value` (SDS 4.5.4) and `skos:notation`, so the term-level responses and the OWL serializations share `skos:notation`; the generator leaves `rdf:value` out of the OWL serializations.
- **Restriction ranges: form 2** (see *The 15 restriction ranges* below).
- **Cardinality and subject expectations** stay as normative prose in the Concepts and Use guide, checked with SHACL, not as OWL axioms: OWL axioms are absolute, so they cannot express SHOULD, and under the open world assumption they do not flag missing or extra values.
- **ROBOT** (BSD-3-Clause, OBO Foundry, built on the OWL API) is an optional dependency of the generator, used for the OWL 2 DL profile check, the Turtle and RDF/XML serializations, and a reasoner check. Without it the generator still builds the files (rdflib) and reports that they were not validated. ROBOT is distributed as a jar and as Docker images (`obolibrary/robot`, `obolibrary/odkfull`); it is not packaged for Debian or Homebrew.

**The 15 restriction ranges.** All have the form `P rdfs:range [ owl:onProperty P ; owl:someValuesFrom C ]`, which says that every value of P itself has some P whose value is a C. Checked against `bdqtest` and the five simple vocabularies, 8 of the properties are used 864 times; in every use the value is typed C, and no value has P itself, so the axioms entail false statements (for `:v1 bdqffdq:hasCriterion bdqcrit:Found`, that `bdqcrit:Found` has a `hasCriterion` of its own, and so on without end) while not entailing that `bdqcrit:Found` is a `Criterion`. The Concepts and Use guide (Section 3.1) states the intent: "An axiom places an `owl:restriction` on the object of the `bdqffdq:forValidation` object property as a `bdqffdq:Validation`", and gives the expected subjects separately (e.g. "`bdqffdq:hasCriterion` … SHOULD have an individual with a type that is a `bdqffdq:Validation` or a `bdqffdq:Issue` as its subject"). The alternatives compared were: (1) a global range `P rdfs:range C`; (2) a range as a restriction on the subject class, `S rdfs:subClassOf [ owl:onProperty P ; owl:allValuesFrom C ]`; (3) existence, `S rdfs:subClassOf [ owl:onProperty P ; owl:someValuesFrom C ]`, which reads a SHOULD as a MUST; (4) qualified cardinality, under which two values of a property that should have one are inferred to be the same individual rather than reported.

*Decided 2026-11-09: form 2*, the restriction that the guide describes. The axioms, with the subject classes from the guide:

| Subject class S | Property P | All values from C |
|---|---|---|
| `AmendmentMethod` | `forAmendment` | `Amendment` |
| `IssueMethod` | `forIssue` | `Issue` |
| `MeasurementMethod` | `forMeasure` | `Measure` |
| `ValidationMethod` | `forValidation` | `Validation` |
| `Validation` | `hasCriterion` | `Criterion` |
| `Issue` | `hasCriterion` | `Criterion` |
| `DataQualityNeed` | `hasDataQualityDimension` | `DataQualityDimension` |
| `Amendment` | `hasEnhancement` | `Enhancement` |
| `DataQualityMethod` | `hasSpecification` | `Specification` |
| `Policy` | `hasUseCase` | `UseCase` |
| `Implementation` | `implementedBy` | `Mechanism` |
| `Implementation` | `usesSpecification` | `Specification` |
| `Amendment` | `improvedBy` | `ImprovementTarget` |
| `ImprovementTarget` | `targetedIssue` | `Issue` |
| `ImprovementTarget` | `targetedMeasure` | `Measure` |
| `ImprovementTarget` | `targetedValidation` | `Validation` |

Notes: `hasCriterion` has two subject classes, so there are 16 axioms. For `improvedBy`, the current axiom has the wrong class as well as the wrong form: its filler is `Amendment`, but the property's note says it "Originally had Domain: Amendment and Range: ImprovementTarget", and the guide's example query uses `?amendment bdqffdq:improvedBy ?it`. For the four `ImprovementTarget` properties, the subject class comes from their definitions, since the guide gives no subject statement. The guide's subject statement for `forMeasure` names `bdqffdq:MeasureMethod`, which does not exist; the class is `bdqffdq:MeasurementMethod` (a follow-up for the guide, Section 13). With these axioms (and `skos:notation` in place of `rdf:value`, `skos:scopeNote` declared), ROBOT 1.9.11 reports the ontology in OWL 2 DL, and HermiT finds it consistent merged with `bdqtest.ttl` and the five simple vocabularies. The axioms keep blank nodes, so they stay in the extension term list.

**`owl:differentFrom` and `owl:AllDisjointClasses`.** The ontology has 8 `owl:differentFrom` statements, all between opposite response codes (e.g. `COMPLIANT`/`NOT_COMPLIANT`, `AMENDED`/`NOT_AMENDED`). They say only that the two IRIs name different individuals (OWL has no unique names assumption), and cover few of the pairs: 3 of the 15 among the 6 `ResponseStatus` values, 5 of the 21 among the 7 `ResponseResult` values. With no functional properties or cardinality restrictions in the ontology, they have no effect on their own, and they do not say that a Response cannot have two results. The 2 `owl:AllDisjointClasses` axioms (the four Test types; `AbstractInformationElement`, `ActedUpon`, `Consulted`) are real constraints, and the current data satisfies them: each of the 253 Tests and 147 information element nodes in `bdqtest` has one of the types.

*Decided 2026-11-09:*

- The `ResponseStatus` and `ResponseResult` values are distinct codes: each set gets an `owl:AllDifferent` axiom (`[ a owl:AllDifferent ; owl:distinctMembers ( … ) ]`) in the extension term list. The 8 pairwise statements are then redundant and are dropped from the term list. `ResourceType` (`SingleRecord`, `MultiRecord`) gets no `owl:AllDifferent`: "record" is a fuzzy enough concept.
- "One status and one result per Response" belongs in SHACL, not OWL. `tg2/core/bdqffdq_SHACL_constraints.ttl` already had exactly one `hasResponseStatus` and `sh:in` lists of the allowed status and result codes for each Response subclass, but nothing limiting `hasResponseResult` to one value. Added (Warning, as for status): at most one `hasResponseResult`, at most one `hasResponseResultValue` (a literal), and not both (guide Section 2.4.1) (`8f47bf06`). A related fix (`21c76e1c`): the 14 SPARQL-based constraints had `sh:severity` inside the `sh:sparql` node, where it is ignored, so their SHOULD rules were reported as Violations; the severity is now on each shape. `bdqtest` still conforms, and the SPARQL queries embedded in the documentation templates still pass (`validate_sparql_in_templates.py --strict`: 21 executed, 6 skipped).
- The parallel families (`*Method`, `*Policy`, `*Response`) and the `*Concept` groupings are not made disjoint: they serve for grouping rather than reasoning.

*Rendering fix.* The Vocabulary Extension document showed each restriction range as `[ owl:someValuesFrom bdqffdq:hasCriterion ]` (the restricted property in place of the class), because the query in `draft_build_bdqffdq.py` did not select the filler. Fixed in this repository (`510510f6`); the document now shows `[ owl:onProperty bdqffdq:hasCriterion ; owl:someValuesFrom bdqffdq:Criterion ]`. Once the form 2 axioms are in place, the document's range section needs to show subclass restrictions instead (Section 13).

**Status (2026-11-09): `bdqffdq` deployed, ontology generated.**

- *Inputs on `bdq-source`.* `e229ed37`: a faithful conversion of `bdqffdq.owl` by the review-only `process/bdq-revisions/bdqffdq_to_rs.py` (109 terms in `bdqffdq.csv`, 81 axiom triples in `bdqffdq-axioms.ttl`; the converter checks that the two reproduce `bdqffdq.owl` apart from documented differences), the `config.yaml` entry (vocabulary `https://rs.tdwg.org/bdqffdq/`, `vocab_type: 1`, List of Terms document `https://rs.tdwg.org/bdqffdq/doc/list/`, `prepend_url` `https://bdq.tdwg.org/draft/docs/list/bdqffdq/#` with no namespace in the fragment, matching the List of Terms anchors), and `new_term_list: false` for the five term lists created by the first run. `ada883fd`: the decided changes (form 2, `owl:AllDifferent`, the extension term list header, `differentFrom` dropped). The vocabulary record carries the ontology's label and note.
- *Deployed.* `bdq-source` merged into `bdq` (`92d21a4d`) and processed (`425e18c0`): only `bdqffdq` rows added (399 lines), the five existing vocabularies unchanged. Checked in a local Docker image (dereferencing test: 772 requests, no errors) and on `bdq-public-review.rs.tdwg.org` over `http` and `https` (responses identical to the image). Two full dereferencing runs against the live site stopped on connection timeouts after about 120 and 200 requests, with no error responses before that; the live server appears to throttle a sustained run.
- *Generator.* `process/build_ontology.py` with `process/process-ontology.md` (referenced from `process-vocabulary.md` Section 3.12) on `bdq-source` (`8ffe39b5`); `rdflib` added to `requirements.txt`. For `bdqffdq`: 1348 triples, OWL 2 DL and consistent (ROBOT 1.9.11, HermiT); output deterministic. Problems found and fixed while testing: rdflib's `pretty-xml` writer drops statements on list nodes (plain `xml` is used); OWL API writes `xsd:string` literals as plain literals (equal in RDF 1.1); some rdflib writers depend on the string hash seed (fixed).
- *In this repository.* `3350a4ea`: the generated `tg2/_review/dist/bdqffdq.{ttl,rdf,jsonld}`; `tg2/_review/vocabulary/bdqffdq.owl` is now a copy of `dist/bdqffdq.ttl` (kept because the build, templates, and site refer to that path; the README marks it as generated); SHACL imports `https://rs.tdwg.org/bdqffdq/`. `0f1f74ea`: the Vocabulary Extension shows the restrictions on classes (Section 4.2), `owl:AllDifferent` (4.3.6), and `owl:differentFrom` (4.3.7, none); the key's examples come from the axioms; the guide links each property to its restrictions; superclass lists show only named classes; the guide's named-range links were missing `#`. `feb38123`: the guide's 11 sentences about restricted properties describe the restrictions; `MeasureMethod` corrected to `MeasurementMethod`; documents regenerated (audits, strict SPARQL checks, and SHACL validation pass). Also `4aff59f0`: raw strings for two regular expressions in `function_lib.py` (Python 3.12+ warnings; same values).
- *Comparison with the previous `bdqffdq.owl`.* Labels, preferred labels, definitions, comments, notes, and scope notes of all 109 terms are identical; types, superclasses, superproperties, named ranges, and the two `owl:AllDisjointClasses` axioms are unchanged. The differences are the intended ones (header, form 2, `owl:AllDifferent`, `skos:notation`, declarations, rs.tdwg.org term metadata), plus the definitions of `bdqffdq:COMPLETE` and `bdqffdq:amendmentProperty`, which lacked the `@en` tag that every other definition had and now have it.

*Term dates.* The previous `bdqffdq.owl` gave each current term a `dcterms:issued` (2024-09-30 for 100 terms; 2026-04-13, 2026-05-16, 2026-03-23, 2024-04-13 for the others; six of them untyped). SDS Section 4.3 puts `dcterms:issued` on versions ("the date on which a version was published"), and `dcterms:created` and `dcterms:modified` on the current resource (the dates the first and the most recent versions were issued); rs.tdwg.org does exactly that. In the SDS these are dates of versions issued by TDWG, and BDQ's dates mark draft revisions that TDWG never issued, so for the first release `created` = `modified` = the release date is consistent with the SDS. *Decided 2026-11-09:* on the review site the draft dates become term versions, processed as a sequence of draft releases (Section 8.5). They are placeholders for the draft (that happen to reflect the terms' history), which become real term versions with the release date on ratification; they live on the term versions, not in the ontology.

*Entailment properties in the basic term list.* SDS Section 4.5: "Properties that extend the meaning of terms by introducing machine-computable entailments SHOULD NOT be included with the basic properties … Rather they SHOULD be included in a vocabulary extension list." `rdfs:subClassOf`, `rdfs:subPropertyOf`, and `rdfs:range` are such properties, and are currently columns of the basic `bdqffdq` term list. Following the SDS strictly would split the inputs into a basic term list (labels, definitions, types, notes) and an extension list made of a CSV for the row-shaped axioms and the Turtle file for the blank-node axioms. *Decided 2026-11-09:* recorded as a point for discussion; for now the boundary stays where it is (named superclasses, superproperties, and ranges in the term list; blank-node axioms in the extension term list) (Section 15, question 14).

Open points: the generator's name and the place of its documentation (proposed: `process/build_ontology.py`, documented in `process/process-ontology.md` and referenced from `process/process-vocabulary.md`); and how `process.py` records the extension term list.

### 9.6 The extension term list in rs.tdwg.org

*Implemented 2026-11-09 on `bdq-source` and deployed on bdq-public-review.rs.tdwg.org; needs the agreement of the rs.tdwg.org maintainers (Section 15, question 15).*

**What the SDS asks.** A vocabulary extension term list is a term list in its own right (SDS 2.2.3, 3.3.3): "A vocabulary extension MUST be identified by a different IRI from the basic term list"; it is typed `owl:Ontology` (4.1); it may list terms defined elsewhere, asserting "additional properties for those terms… for example: subclass relationships, ranges, or cardinality restrictions" (2.2.3); it is versioned like other term lists (2.3); its human-readable representation is a separate document (3.3.3); its distributions are linked with `dcterms:hasFormat` (2.2.4, 4.4.3); and it is part of the vocabulary that combines it with the basic term list (4.4.2.3). Before this step, rs.tdwg.org had no extension term list and no way to represent one: the `bdqffdq` axioms file sat next to the current terms with no record, versions, or dereferencing.

**Two parts.**

1. *A term list record with versions and distributions* (`bdq-source` `05e5cd69`, `d7cc3f8e`). A vocabulary declares its extension term lists under `extension_lists` in `config.yaml` (IRI, label, description, dataset, axioms file name, distribution base URL, optional browser redirect). In each release in which the list is new, its axioms change (the release directory contains the axioms file, and its axioms differ from the current ones), or one of its member terms has a new version since the list's latest version, `process.py` (new module `process/extension_lists.py`, `bdq-source` `7ad0c5bf` for the member-term rule):
   - writes the current axioms, with `owl:versionIRI`, as Turtle, RDF/XML, and JSON-LD (`<dataset>/<dataset>-axioms.*`), and an immutable copy for the version (`<dataset>/axioms-versions/`), deterministically;
   - records the term list (`term-lists/term-lists.csv`) and its members, the vocabulary's terms that the axioms are about (as for a list of borrowed terms); its dated version, with the term versions applicable on that date as members and a replacement link to the previous version; and the join that gives `dcterms:hasVersion`;
   - records its distributions in two new linked tables, `term-lists/term-lists-formats.csv` and `term-lists-versions/term-lists-versions-formats.csv`;
   - adds it to the vocabulary and creates the vocabulary and standard versions through the existing `update_vocabulary_metadata` and `update_standard_metadata`;
   - records the browser redirect in `term-lists/term-lists-redirects.csv`, which `html/restxq.xqm` uses to redirect HTML requests for the list and its versions to the human-readable document.

   A release that changes neither the axioms nor a member term creates no version; a same-release rerun rewrites the version of that date. Documented in `process/process-ontology.md`, Section 4.

   *Versioning (decided 2026-11-12):* the list is versioned on changes to its axioms or to its member terms, so a version takes the date of the most recent change of either, and always lists the current versions of the terms it is about. (First implemented on changes to the axioms only.) In synthetic tests, a change to `bdqffdq:Validation` alone created an extension list version with unchanged axioms, and a change to a term the axioms do not mention (`bdqffdq:QualityControl`) created none.

2. *The axioms served with the list's RDF* (`bdq-source` `5946a6a0`). `term-lists/term-lists-axioms.csv` gives the axioms files of each extension list IRI and version IRI, and `html/restxq.xqm` (`page:with-axioms`) appends them to the RDF that rs.tdwg.org serializes from the tables: the Turtle is appended, the RDF/XML node elements are inserted into the same `rdf:RDF` (with any missing prefix declarations), and the JSON-LD nodes are appended to the `@graph`. The list IRI, and each version IRI, then return both the metadata and the axioms, so the IRI can be the object of `owl:imports`, as the SDS layered model assumes.

**Distributions: current TDWG practice rather than SDS 4.4.3.** *Decided 2026-11-09.* SDS 4.4.3 gives each distribution `ac:accessURI`, `dcterms:modified`, and `dc:format`. No dataset in rs.tdwg.org uses `ac:accessURI`, and none declares the `ac:` prefix; adding it would add an unused prefix declaration to every term list and term list version response. rs.tdwg.org describes Document distributions (`docs/docs-formats.csv`, used for every standard's documents, including recent ones such as the Humboldt Extension) with `dcterms:hasFormat` to the access URL as the distribution's IRI, typed `foaf:Document`, with `dc:format`. The extension term list follows that practice, so no prefix is added and existing responses are unchanged.

**Interim limitation.** The term list record is typed `tdwgutility:TermList` only, because the term list class is fixed per dataset; the axioms themselves type the list `owl:Ontology`, and with part 2 both are in the same response.

**Observation for the rs.tdwg.org maintainers (not specific to BDQ).** Term list records served by rs.tdwg.org have `dcterms:created` but no `dcterms:modified` (e.g. `https://rs.tdwg.org/bdqdim/terms/` on bdq-public-review.rs.tdwg.org, and the term lists on production rs.tdwg.org). The shared mapping `term-lists/term-lists-column-mappings.csv` maps a column `version_modified` to `dcterms:modified` and `owl:versionInfo`, but `term-lists/term-lists.csv` has `list_modified` instead, so neither is emitted. The extension term list inherits this.

**`bdqffdq`.** `https://rs.tdwg.org/bdqffdq/extension/` is declared from the 2024-10-01 release, a release of the faithful axioms alone, dated by their history in this repository: the axioms of `bdqffdq.owl` (restriction ranges, `owl:AllDisjointClasses`) last changed on 2024-10-01 (`8005faba`) before the decided changes, and every term they refer to exists by then (decided 2026-11-12; first placed in 2024-04-13, then in 2024-09-30). Its versions are `https://rs.tdwg.org/bdqffdq/version/extension/2024-10-01` (faithful axioms, superseded; 28 member terms) and `…/2026-11-09` (decided axioms, recommended; 50 member terms); every `bdqffdq` vocabulary version from 2024-10-01 includes the applicable extension list version. The 2024-10-01 release creates the vocabulary version `https://rs.tdwg.org/version/bdqffdq/2024-10-01` (members: the term list version of 2024-09-30 and the extension list version of 2024-10-01), a standard version, and a decision, and no term versions or List of Terms document versions. HTML requests redirect to the Vocabulary Extension document, `https://bdq.tdwg.org/draft/docs/extension/bdqffdq/` (provisional `/draft/` location). The distributions' access URLs point to files on the `bdq` branch of tdwg/rs.tdwg.org (`https://raw.githubusercontent.com/tdwg/rs.tdwg.org/bdq/bdqffdq/…`); in production, `distribution_base_url` would point to `master`. On bdq-public-review.rs.tdwg.org the list is served at `https://bdq-public-review.rs.tdwg.org/bdqffdq/extension/`; the identifier `https://rs.tdwg.org/bdqffdq/extension/` resolves at rs.tdwg.org only after the work is merged to `master` and production is redeployed.

**Changing the axioms** (*documented 2026-11-12*, `process/process-ontology.md` Section 5). The source of the axioms is the axioms file in the release directories; the derived files on `bdq`, the generated ontology, and this repository's `bdqffdq.owl` and `dist/bdqffdq.*` are outputs. A change is a new release: on `bdq-source`, a release directory for the date of the change, with the complete `config.yaml` (`new_term_list: false` throughout, `extension_lists` declared), header-only release-input CSVs (unless terms change too), and a copy of the current axioms with the change; a new term the axioms refer to is added in the same release. It is processed on `bdq` (`--dry-run`, then the run), the ontology is regenerated with ROBOT to check that it is still OWL 2 DL and consistent, and, after the Docker check, pushed. The release creates a new extension list version (members recomputed; it replaces the previous version, which becomes superseded; the list IRI returns the new axioms), a new `bdqffdq` vocabulary version (whose members are the unchanged term list version and the new extension list version), a new standard version, and a decision linked to the extension term list; it creates no term versions and no List of Terms document version. The generated ontology gets the new vocabulary version as its `owl:versionIRI`, and this repository's build regenerates `dist/` and the Vocabulary Extension document. On the review site the dates are placeholders; after ratification the same mechanics would run on rs.tdwg.org `master` under the Vocabulary Maintenance Specification.

- *Decision links* (*decided and implemented 2026-11-12*, `bdq-source` `4e6ccaef`). `process.py` linked a release's decision only to changed terms (`decisions/decisions-links.csv`), so a release that changed only the axioms recorded a decision that linked to nothing. It now also links the decision to each extension term list that the release creates a version of. Existing decision links point to current resources (term IRIs, never version IRIs), so the link is to `https://rs.tdwg.org/bdqffdq/extension/`. Reprocessing the release sequence added exactly two rows, for the decisions of 2024-10-01 and 2026-11-09, and changed nothing else (question 15).
- *The Vocabulary Extension document* (remaining gap). HTML requests for the list redirect to that document, which is not a document record in rs.tdwg.org, so an axioms change creates no document version, and the document is regenerated by this repository's build. Once it is declared under `documents` in the release `config.yaml`, a release that changes the axioms should mark it `modified: true`, which gives it a version of the same date (`process.py` versions an existing document other than a List of Terms only when it is so marked). Part of the document metadata work (Section 11; document IRIs open, Section 11.3).

**Tests** (local Docker images, then bdq-public-review.rs.tdwg.org). All eleven releases process; rerunning the last release changes no file; only BDQ rows and the six dataset modification dates in `index/index-datasets.csv` change. For the list and both versions, each format parses and equals the metadata plus the axioms (graph isomorphism; e.g. 243 triples for the list, 129 of metadata and 115 of axioms). 276 other term list and term list version responses are byte-identical to before. The dereferencing test passes (772 requests, no errors). The generated ontology is unchanged.

---

## 10. Options for `bdqtest`

The goal is for the source of truth of `bdqtest` to be files in rs.tdwg.org, ideally with rs.tdwg.org delivering RDF for both individual Tests and the whole vocabulary; building the whole-vocabulary RDF in this repository is acceptable.

*Requirement (decided 2026-11-10):* for the public review, the full graph of each Test (the Test and everything that describes it: Method, Specification, Arguments and the Parameters they are for, information element nodes and their members, references, examples, and policy memberships) must be deliverable both as the complete `bdqtest` serializations and as a serialization per Test, dereferenceable from the Test's IRI. A Test is defined by that whole graph; a partial description is not an adequate representation of it. The structural nodes in that graph keep their non-resolvable `urn:uuid:` identifiers (Section 10.6), so the Test's IRI is the only way to reach them. Options T1 and T2, which deliver a partial description per Test, are therefore rejected (Sections 10.2, 10.3).

### 10.1 What has to move

- `bdqtest_term_versions.csv`: its input part becomes an rs.tdwg.org modification CSV for a `bdqtest` term list (`https://rs.tdwg.org/bdqtest/terms/`, database `bdqtest`), with renamed columns (no `:`, `(`, `)`, or spaces), and `iri`, `issued`, and `status` generated by `process.py`.
- The four GUID tables in `tg2/core/` (`TG2_tests_additional_guids.csv`, `information_element_guids.csv`, `TG2_policy_guids.csv`, `TG2_citation_guids.csv`) become auxiliary CSVs in the rs.tdwg.org `bdqtest` directory. They are identifiers that must stay stable, so they belong with the source of truth.
- `build_bdqtest_rdf.py` changes its inputs to these files (and should replace `kurator-ffdq` in `copy_files.sh`).

### 10.2 Option T1: flat term list in rs.tdwg.org; whole-vocabulary RDF built from it

*Rejected (2026-11-10).* A Test IRI would dereference to a flat, partial description, missing the Specification, Arguments, information elements, and the rest of the Test's graph, which does not meet the requirement above. Retained here as the record of the analysis; the flat term list and GUID tables remain the source in T3.

- rs.tdwg.org holds the flat term list plus the auxiliary GUID tables, and `process.py` manages versions and status.
- Single-valued columns map to real predicates in the rs.tdwg.org mapping (e.g. `Type` to `rdf:type`, and Dimension, Criterion, Enhancement, and Resource Type as IRIs, using the same predicates as `build_bdqtest_rdf.py`). Packed columns (information elements, parameters, references, examples, use cases) are mapped as plain literals, or left unmapped.
- rs.tdwg.org serves a flat, partial description for each Test IRI through the generic handler.
- `build_bdqtest_rdf.py` builds the full `bdqtest.ttl`, `.rdf`, and `.jsonld` from the rs.tdwg.org files (in this repository or in rs.tdwg.org `process/`), and they are published on `bdq.tdwg.org` and/or committed to rs.tdwg.org, with a redirect or route for the whole vocabulary.

Assessment: source of truth in rs.tdwg.org with standard versioning, few rs.tdwg.org changes (only renamed columns and a custom mapping). But the per-Test RDF from rs.tdwg.org is not the full graph, so a Test IRI has two different RDF descriptions (the rs.tdwg.org response and the full distribution), in tension with the SDS principle that all representations carry the same data. Effort: moderate.

### 10.3 Option T2: normalized linked-class tables served by the generic serializer

*Rejected (2026-11-10).* Still a partial graph per Test (no Arguments, Parameters, `composedOf` members, or Policies), which does not meet the requirement above.

Normalize `bdqtest` into a root table and linked child tables (Section 5). Because of the one-level depth and `urn:uuid` IRIs (Sections 2.3 and 4.3), a response for a Test IRI can contain the Test, its Method, Specification, and information element node IRIs, references, examples, and use-case links, but not the Arguments, the Parameters they are for, `composedOf` members, or Policies.

Assessment: better than T1 per Test, still not the full graph, and the normalized tables are harder to edit by hand than the current single table. Effort: moderate to large. Rejected.

### 10.4 Option T3: generated per-Test RDF files served by rs.tdwg.org

- Source: a flat `bdqtest` term list and the GUID tables in rs.tdwg.org, versioned by `process.py` (as described for T1).
- A BDQ-specific step, run in rs.tdwg.org after `process.py`, runs `build_bdqtest_rdf.py` on the rs.tdwg.org files and writes:
  - the whole vocabulary (`bdqtest.ttl`, `.rdf`, `.jsonld`), and
  - one graph per Test: the Test plus everything reachable from it that has no dereferenceable IRI of its own (Method, Specification, Arguments, information element nodes and their members, references, examples, policy memberships), in three serializations.
- A new route in `restxq.xqm`, `/bdqtest/terms/{id}`, returns the per-Test file for the requested media type (`file:read-text`), with a 303 pattern and extensions matching the generic handler. HTML is redirected via `html/redirects.csv` to the BDQ List of Terms or Quick Reference Guide. Test versions (`/bdqtest/terms/version/{id}`) can use the generic handler (flat) or the same mechanism.

Assessment: full-fidelity RDF for individual Tests and the whole vocabulary, both from rs.tdwg.org, with the source in rs.tdwg.org. Costs: a new route and a new processing step in rs.tdwg.org that the rs.tdwg.org maintainers must accept, about 254 × 3 generated files committed per release, and moving (or pinning a copy of) `build_bdqtest_rdf.py` to rs.tdwg.org. Effort: moderate to large.

### 10.5 Option T4: extend rs.tdwg.org for nested linked classes

Extend the loader and serializer so linked children can have their own linked children (nested `linked-classes.csv`), letting the generic handler emit the full per-Test graph from normalized tables.

Assessment: the most general solution, potentially useful for other graph-rich standards, but a significant change to rs.tdwg.org's core serializer, and it still leaves the derivations in Section 5.2 (policies, MultiRecord nodes) to be precomputed into tables. Effort: large. Not recommended for the public review timeline.

### 10.6 Resolvable IRIs for the structural nodes

The Methods, Specifications, Arguments, information element nodes, and Policies in `bdqtest` are identified by `urn:uuid:` IRIs (Section 4.3). They could instead be minted as resolvable IRIs under rs.tdwg.org, keeping the UUIDs as local names, for example `https://rs.tdwg.org/bdqtest/specification/01b96157-e4a1-4884-95d7-3bcfc5f3c047`.

Effects:

- Each kind of node could be the root of its own rs.tdwg.org dataset, with its children in linked tables one level down: Specifications with their Arguments, information element nodes with their `composedOf` members, Policies with their Tests. A request for a Test would return the Test with links to its Method, Specification, and information elements, and a client would follow those links for the rest. This would not, on its own, deliver the full graph of a Test from the Test's IRI (a client would have to follow the links), so it does not replace T3 or T4 for the requirement above; and the derived structures (policy aggregation, MultiRecord nodes) would still have to be precomputed into tables.
- Each node would be described where it is identified, in line with linked data practice.
- Several hundred more TDWG-minted IRIs (about 730 in the current `bdqtest.ttl`) would need stability, versioning, and routing (`term-lists.csv` rows, or routes, for each new path).
- The BDQ standard's documents, the RDF distributions, and any implementations that record these identifiers use the `urn:uuid:` values now. Changing them before ratification is possible; changing them afterwards would not be. Keeping the `urn:uuid:` values and linking them to the new IRIs with `owl:sameAs` is possible, but adds triples and complexity.

*Decided 2026-11-10, at least for now:* the structural nodes do not get resolvable IRIs; they keep their `urn:uuid:` identifiers. They are therefore described only within the graph of the Test they belong to, which is why a resolvable Test IRI must deliver the full graph of its related nodes (Section 10, requirement; T3). The analysis above stays as the record, should the question be reopened (see the Summary, item 4, and Section 15, question 5).

### 10.7 Recommendation for `bdqtest`

*Revised 2026-11-10.* T1 and T2 are rejected: the public review needs the full graph of each Test, both in the complete `bdqtest` serializations and per Test (Section 10, requirement). Use T3 for the public review: the source of truth in rs.tdwg.org (flat term list and GUID tables, versioned by `process.py`), the full graph of each Test generated as RDF files and served from the Test's IRI by rs.tdwg.org, and the complete serializations built from the same files (Section 6.4). T4 remains the general alternative if the rs.tdwg.org maintainers prefer extending the serializer, but is not feasible for the review timeline. The route and processing step need the rs.tdwg.org maintainers' agreement (Section 15, question 2); the extension term list (Section 9.6), which appends files to a list's RDF, is a precedent for serving content read from files. The design, and what remains open, are in Section 10.9.

### 10.8 Generated CSV lists and documents

This repository generates flat lists and documents from `bdqtest_term_versions.csv`, including:

- `tg2/_review/dist/bdqtest_singlerecord_tests_current.csv`, `bdqtest_multirecord_tests_current.csv` (`draft_build_bdqtest_singlerecord_tests_current.py`)
- `tg2/_review/dist/bdqtest_tests_vertical.csv` (`make_bdq_tests_vertical.py`)
- the Quick Reference Guide and filtering (`draft_build_bdqtest_qrg.py`, `generate_bdq_qrg_filtering.py`)
- the `bdqtest` List of Terms (`draft_build-termlist_bdqtest.py`) and other documents (`draft_build-docs.py`)

With T3, these can read the rs.tdwg.org current terms file (`bdqtest/bdqtest.csv`), which stays flat; column renames need a mapping back to the published column names so that implementers using the `dist` CSVs are not affected. If the source becomes non-flat (T4), these lists should be generated by SPARQL queries over the `bdqtest` RDF instead; the existing SPARQL template validation in `do_build.sh` is a starting point.

### 10.9 T3 design: work in progress

*Started 2026-11-10. This section records where the design and the analysis stand; more thinking is needed before `bdqtest` is processed, in particular on the version IRIs (10.9.6).*

#### 10.9.1 What "a Test" is

The graph that a Test's IRI must deliver (Section 10, requirement) is defined by the example in the Fitness For Use Framework Ontology: Concepts and Use guide, Section 2.6 (`VALIDATION_COUNTRY_FOUND`), which is the reference for the generated per-Test graphs:

- the Test version (typed, labelled, `dcterms:isVersionOf` its term IRI, `dcterms:issued`), with its links to information elements, Criterion, Dimension, Enhancement, Resource Type, and citations;
- its Method (`forValidation` etc. pointing to the Test version), the Method's Specification, and the Specification's Arguments;
- its information element nodes in full (`composedOf` the Darwin Core terms);
- its citations as `dcterms:BibliographicResource` with `dcterms:bibliographicCitation`;
- minimal descriptions (type and label) of the named terms it uses: Criterion, Dimension, Enhancement, Resource Type, Parameters, Use Cases;
- each Policy that includes it, with the Policy's label and `hasUseCase`, and only this Test's `includedInPolicy` (the example's Validation Policy covers 50 Validations; the example shows one);
- links only, not descriptions, for `composedOf` members and for other Tests (`aggregatesResponsesFrom`, which is for the inputs of a Test).

The embedded SPARQL queries in the documentation (all `SELECT`) traverse the same structure (Policy → Test, Method → Test, Method → Specification), and Supplement 2.4.1 reads the Test node as the "Term Version IRI" (`?iri dcterms:isVersionOf ?term_iri`).

The current generator, kurator-ffdq, builds the same structure with RDFBeans: every model class is an `@RDFBean`; a Test bean nests its information elements, Resource Type, Dimension, and Criterion as beans (hence their minimal descriptions); `composedOf` and `aggregatesResponsesFrom` are plain URI lists; Methods nest the Specification, which nests the Arguments; Policies nest the Use Case and list all their Tests. `TestUtil` saves each Test, Method, and Policy as roots into one repository and serializes the union; there is no per-Test output. `build_bdqtest_rdf.py` reproduces this. A per-Test graph is therefore the closure of the Test's bean, plus the closure of its Method's bean, plus its Policies restricted to this Test. The union of all per-Test graphs is the complete graph.

In the current `dist/bdqtest.ttl` (8651 triples): 253 Tests (148 Measures, 72 Validations, 29 Amendments, 4 Issues), a Test's own graph of 31 to 68 triples (35 on average), 99 information element nodes shared between Tests (keyed by label), 16 Policies with up to 106 Tests each, and 72 `aggregatesResponsesFrom` links.

#### 10.9.2 Design (proposed)

1. *Source in rs.tdwg.org:* `bdqtest.csv` as a flat term list with renamed columns, processed by `process.py` with versions; the four GUID tables of `tg2/core/` as auxiliary inputs kept with the term list.
2. *The graph is a graph of a Test version*, as BDQ models it (Methods point to the version). A version IRI dereferences to its metadata from the tables plus its full graph; a Test's term IRI dereferences to the term's metadata plus the full graph of its current version. This is the mechanism of the extension term list (Section 9.6), applied per Test.
3. *Per-version graph files generated during processing:* a pinned copy of `build_bdqtest_rdf.py` (BDQ-specific, kept with the BDQ inputs) generates the complete graph from the rs.tdwg.org files and cuts it into one graph per Test version (10.9.1), written once per version as Turtle, RDF/XML, and JSON-LD and never changed afterwards. Check: the union of the current versions' graphs equals the complete graph; and the generated graph of `VALIDATION_COUNTRY_FOUND` matches the example in the guide, Section 2.6.
4. *Serving, generic:* for a dataset with a lookup table (e.g. `bdqtest/bdqtest-graphs.csv`, IRI → file), `restxq.xqm` appends the file to the term's or version's RDF, as `page:with-axioms` does for extension lists; other datasets are unaffected. HTML redirects to the List of Terms.
5. *Complete serializations:* built by this repository's build with the same generator against a pinned rs.tdwg.org commit (`dist/bdqtest.{ttl,rdf,jsonld}`, Section 6.4).

Needs the rs.tdwg.org maintainers' agreement: the generic lookup in `restxq.xqm`, generating files during processing, and about 750 committed files for each release that changes Tests (Section 15, question 2). *Decided 2026-11-12:* implemented on the BDQ branches and deployed for the review before that agreement, and flagged for the maintainers, as the extension term list was (Section 9.6).

#### 10.9.3 The two dates of a Test

Each Test has two date properties with different meanings:

- `issued`: the most recent change of any sort. This is TDWG versioning, so it dates a term version in rs.tdwg.org.
- `DateLastUpdated` (`bdqffdq:hasDateLastUpdated`): the most recent change in substance (e.g. defined behavior) that implementers must pay attention to. It is part of the Test's content, carried as a column and emitted in the Test's graph, not a version date.

There is an implicit assumption, which the data bear out: every `DateLastUpdated` is also the `issued` date of the version that made that substantive change. For any `DateLastUpdated` there is a corresponding issued version (there may be newer ones), so `DateLastUpdated` also allows the construction of a particular version IRI. In `bdqtest_term_versions.csv`, `DateLastUpdated` is earlier than `issued` for 253 Tests and equal for 1, never later.

*Decided 2026-11-12:* each Test gets both versions on the review site. Each Test therefore has at least two meaningful versions: the one issued on its `DateLastUpdated`, which implementations must match, and the latest, issued on `issued`. For the placeholder versions on bdq-public-review.rs.tdwg.org (Section 8.5), each Test would be added in the draft release on its `DateLastUpdated` and get a further version in the release on its `issued` date: 35 `DateLastUpdated` dates (2022-03-25 to 2025-03-03) and 6 `issued` dates (2024-09-17, 2024-09-24, 2024-09-25, 2025-03-06, 2025-03-07, 2026-04-24), 40 dates in all, interleaved with the existing draft releases. The content of the earlier version is a placeholder with the Test's current content: its behavior is the same by definition, and non-behavioral differences are not recovered (they could be reconstructed from this repository's history if wanted). Every version's graph carries `bdqffdq:hasDateLastUpdated`.

#### 10.9.4 Findings: the current generation and documents

The current generation identifies a Test version in four ways, with two dates:

| Where | Form | Date |
|---|---|---|
| `bdqtest` RDF (kurator-ffdq `TestUtil.java`, lines 697-698; `build_bdqtest_rdf.py`): `rdf:about`, and the object of `forValidation` etc. | `…/bdqtest/terms/<uuid>-<date>` | `issued` |
| `bdqtest` List of Terms, "Term Version IRI" | `…/bdqtest/terms/version/<uuid>-<date>` | `DateLastUpdated` |
| Quick Reference Guide | `…/bdqtest/terms/<uuid>/<date>` | `DateLastUpdated` |
| `bdqtest_term_versions.csv`, `iri` column | `…/bdqtest/terms/version/<uuid>-<date>` | `DateLastUpdated` |

The List of Terms and the Quick Reference Guide use `DateLastUpdated` for 253 of 254 Tests (the exception is the Test whose two dates are equal). The RDF uses `issued` for the version, consistent with the semantics above, but neither kurator-ffdq nor `build_bdqtest_rdf.py` emits `DateLastUpdated`: there is no `bdqffdq:hasDateLastUpdated` in `bdqtest.ttl`, although `bdqffdq` defines the property (range `xsd:date`). The Implementers guide says implementations pick out a Test by its "Term Version IRI (`rdf:about`)", while the List of Terms gives a different IRI under that name.

#### 10.9.5 Findings: the implementations

The FilteredPush libraries annotate each Test method with `@Provides("<uuid>")` (the term name) and `@ProvidesVersion("…")` (a version identifier). Of 203 `@ProvidesVersion` values in `event_date_qc`, `sci_name_qc`, `geo_ref_qc`, and `rec_occur_qc` (checked 2026-11-10):

| Library | Values | Forms | Date matches |
|---|---|---|---|
| `event_date_qc` | 35 | 26 `…/bdqtest/terms/version/<uuid>-<date>`, 9 bare `<uuid>-<date>` | `DateLastUpdated` 25, `issued` 1 |
| `sci_name_qc` | 54 | 38 `…/bdqtest/terms/<uuid>/<date>`, 16 `…/bdq/terms/<uuid>/<date>` | `DateLastUpdated` 33, neither 3, Test not in the CSV 18 |
| `geo_ref_qc` | 52 | 48 `…/bdqtest/terms/<uuid>/<date>`, 4 `…/bdq/terms/…` | `DateLastUpdated` 48, neither 1, not in the CSV 3 |
| `rec_occur_qc` | 62 | 54 `…/bdqtest/terms/<uuid>/<date>`, 8 `…/bdq/terms/…` | `DateLastUpdated` 42, neither 1, not in the CSV 19 |

No implementation uses the RDF's `…/terms/<uuid>-<issued>`. Where the date matches, it is `DateLastUpdated` (148 cases; `issued` once): implementations identify the behavioral version they implement, which fits the semantics in 10.9.3, and, by the assumption there, each such identifier names a real earlier term version, written in one of several spellings. The 5 values matching neither date, and the 40 citing Tests not in the current CSV (older or retired Tests, many in the `bdq/` namespace), are for the implementations to update.

#### 10.9.6 Open: the version IRI form

SDS 2.3.2: "Typically, the IRI of a version is formed by appending the ISO 8601 creation date of the resource to the IRI of the abstract resource", with examples such as `http://rs.tdwg.org/dwc/terms/MaterialSample-2014-10-23`. BDQ's identifiers followed that guidance (`…/bdqtest/terms/<uuid>-<date>`). rs.tdwg.org's implementation differs: every TDWG-minted term version in rs.tdwg.org (38 datasets, including Darwin Core) uses `…/terms/version/<local name>-<date>`, `process.py` generates only that form, and the SDS's own example does not resolve on production rs.tdwg.org (`http://rs.tdwg.org/dwc/terms/MaterialSample-2014-10-23` returns 404, `…/dwc/terms/version/MaterialSample-2014-10-23` resolves). This is an inconsistency between the SDS and rs.tdwg.org, to be raised with the rs.tdwg.org maintainers and probably the TAG (Section 15, question 16).

Options, none decided:

- *A:* rs.tdwg.org's form, `…/terms/version/<uuid>-<date>`, as for every other TDWG vocabulary; identifiers in implementations and documents change.
- *B:* BDQ's SDS form, `…/terms/<uuid>-<date>`, as the canonical version IRI; needs a per-vocabulary version IRI form in `process.py` and routing that resolves `…/terms/<uuid>-<date>` as a version.
- *C:* a canonical form in rs.tdwg.org, with the other forms in use (the SDS form, `…/terms/<uuid>/<date>`, the older `bdq/` namespace) resolving to it by redirects. (Correction 2026-11-12: `index/legacy-urls.csv` is not a redirect mechanism, only a list of URLs that `dereferencing-test.py` checks; rs.tdwg.org's legacy redirects are routes in `restxq.xqm`.) Because every form in use can be normalized to the pair (UUID, date), and every `DateLastUpdated` names a version (10.9.3), C can make every identifier in use resolve to the version it names.

*Decided 2026-11-12 (a form of C):* the canonical version IRI is rs.tdwg.org's `…/terms/version/<local name>-<date>`, as for every TDWG vocabulary, so `process.py` needs no change. An opt-in, per-vocabulary fallback in `restxq.xqm` redirects the SDS 2.3.2 form `…/terms/<local name>-<date>` to the canonical IRI when that version exists; it applies only to the vocabularies that opt in (the BDQ vocabularies), so existing vocabularies, for which such URLs return 404, are unaffected. It also makes the SDS-form version IRIs in the generated Lists of Terms resolve (Section 13). The Quick Reference Guide's `…/terms/<uuid>/<date>` and the forms used in implementations (including the older `bdq/` namespace) are not redirected: they are fixed at their source (Section 13). Still for the maintainers: the inconsistency between SDS 2.3.2 and rs.tdwg.org (question 16). Related: what an implementation should cite (a version IRI, or the term IRI with `hasDateLastUpdated`), and whether the Implementers guide's "Term Version IRI (`rdf:about`)" should be clarified. The choice must be made before `bdqtest` is processed, because `process.py` bakes the version IRIs into the data.

#### 10.9.7 Open: the single-record Measures that count Test outcomes

Four single-record Measures count the outcomes of other Tests on the same record: `MEASURE_VALIDATIONTESTS_COMPLIANT`, `MEASURE_VALIDATIONTESTS_NOTCOMPLIANT`, `MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET` (Consulted `bdqval:AllValidationTestsRunOnSingleRecord`), and `MEASURE_AMENDMENTS_PROPOSED` (Consulted `bdqval:AllAmendmentTestsRunOnSingleRecord`). None has an ActedUpon information element. `MEASURE_AMENDMENTS_PROPOSED` should be included in `bdqtest` (the current builders exclude it, because of its token), and needs a defined information element to be included. *Decided 2026-11-12:* they are modeled before `bdqtest` is processed. These Measures are oddities that likely need more careful modeling; the aggregating multi-record Measures, which use ActedUpon `bdqval:AggregatedTestResponseOutcomes` with `aggregatesResponsesFrom` the input Tests, are one pattern to consider.

#### 10.9.8 Future direction, out of scope for the review

The ideal is a triple store holding `bdqtest` (and the other BDQ vocabularies), so that SPARQL queries could return, for example, all Tests relevant to a Use Case, or the Tests acting on a given Darwin Core term. The design above does not preclude it: the per-Test graphs and the complete serializations are ordinary RDF that can be loaded into a triple store later, and the SPARQL queries embedded in the BDQ documents (validated against `bdqtest.ttl` by `validate_sparql_in_templates.py`) would carry over.

---

## 11. Metadata records for the human-readable documents

Every human-readable component of a TDWG standard is a document in the TDWG hierarchy (a part of the standard, alongside its vocabularies), with a permanent IRI that dereferences through rs.tdwg.org. `html/restxq.xqm` serves documents from the `docs` and `docs-versions` datasets (route `/{vocab}/doc/{local-id}` and `/{vocab}/doc/{local-id}/{date}`), redirecting browsers to the document's `browserRedirectUri` and returning RDF metadata otherwise.

*Revised 2026-11-12.* This section was written for the workflow before the release-level `process.py` (Section 8.2), in which each document was processed separately by `tdwg_docs_metadata_update.py` from per-document YAML files. That workflow is gone; Sections 11.1, 11.2, and 11.4 now describe the current one.

### 11.1 What a document record consists of

- `docs/docs.csv`: one row per document (`documentTitle`, `current_iri`, `doc_created`, `doc_modified`, `publisher`, license, `citation`, `creator`, `comment`, `accessUrl`, `browserRedirectUri`, `dcterms_isPartOf` (the standard IRI), `abstract`);
- `docs-versions/docs-versions.csv`: one row per version, with `version_iri` = `current_iri` + issue date;
- `docs/docs-authors.csv` and `docs-roles/docs-roles.csv`: contributors, their roles, ORCIDs, and affiliations;
- `docs/docs-formats.csv`: the media type and URL of the source file (e.g. the raw Markdown).

All of these are written by `process.py` from the `documents` array of the release `config.yaml` (`process/process-vocabulary.md`, Sections 3.3 and 3.4): one entry per document of the standard, with its `document` IRI, its metadata (`documentTitle`, `abstract`, `creator`, `mediaType`, `accessUrl`, `browserRedirectUri`; common values in `document_defaults`), and its `contributors`. `dcterms_isPartOf` is the standard IRI, and the dates come from the release. The `documents` array lists every current document of the standard, not only those changed in the release. A document that is new in a release gets its first version in that release; an existing document other than a List of Terms gets a new version only when the release marks it `modified: true`. The seven Lists of Terms are already declared this way (Section 8.2.1).

### 11.2 What BDQ already has

BDQ keeps a `document_configuration.yaml` in the old rs.tdwg.org format for each document, in `tg2/_build_review/templates/*/` (e.g. `templates/guide/bdqtest/document_configuration.yaml`), and one shared `tg2/_build_review/authors_configuration.yaml`. They are converted into `documents` entries, as was done for the Lists of Terms (`process/bdq-revisions/bdq_to_rs.py`), with these changes:

- `current_iri` becomes the `document` IRI decided in Section 11.3;
- `dcterms_isPartOf` (`http://example.org/to_be_determined` in the drafts) is dropped: `process.py` sets the standard IRI, `http://www.tdwg.org/standards/YYY` for the review;
- `browserRedirectUri`: the provisional `/draft/` URL on `bdq.tdwg.org`, as for the Lists of Terms; the final URL is open (Section 15);
- `accessUrl`: the raw Markdown URL in tdwg/bdq;
- `doc_created` and `doc_modified` are dropped: `process.py` sets them from the release;
- contributors: all BDQ documents currently share one author list, converted from `authors_configuration.yaml`; documents with different authors or roles get their own `contributors`.

The `bdquc` List of Terms was titled "BDQ Use Case Controlled Vocabulary", without "List of Terms", unlike the other six. *Corrected 2026-11-12* in the rs.tdwg.org inputs (`bdq-source` `4d70b833`) and in `tg2/_build_review/templates/list/bdquc/document_configuration.yaml`; the published document's heading changes with the next build.

### 11.3 Document IRIs

*Decided 2026-11-12* (scheme B): a document about one vocabulary has its IRI under that vocabulary, `https://rs.tdwg.org/{vocabulary}/doc/{name}/`, as the Lists of Terms already do (`https://rs.tdwg.org/{vocabulary}/doc/list/`, decided 2026-11-09); a document about the standard as a whole has its IRI under the standard's abbreviation, `https://rs.tdwg.org/bdq/doc/{name}/`. All are `https`.

| Document | Source in this repository | Document IRI |
|---|---|---|
| The BDQ Standard (landing page) | `tg2/_review/index.md` | not a document: covered by the standard record `http://www.tdwg.org/standards/YYY`, as for other TDWG standards |
| Fitness For Use Framework Ontology | `docs/bdqffdq/index.md` | `https://rs.tdwg.org/bdqffdq/doc/ontology/` |
| Fitness For Use Framework Ontology Vocabulary Extension | `docs/extension/bdqffdq/index.md` | `https://rs.tdwg.org/bdqffdq/doc/extension/` |
| Fitness For Use Framework Ontology: Concepts and Use | `docs/guide/bdqffdq/index.md` | `https://rs.tdwg.org/bdqffdq/doc/guide/` |
| BDQ Tests: Concepts and Use | `docs/guide/bdqtest/index.md` | `https://rs.tdwg.org/bdqtest/doc/guide/` |
| Quick Reference Guide | `docs/terms/bdqtest/index.md`, with its supporting pages | `https://rs.tdwg.org/bdqtest/doc/qrg/` |
| BDQ Implementer's Guide | `docs/guide/implementers/index.md` | `https://rs.tdwg.org/bdq/doc/implementers/` |
| BDQ User's Guide | `docs/guide/users/index.md` | `https://rs.tdwg.org/bdq/doc/users/` |
| Guide to Marking and Identifying Synthetic and Modified Data | `docs/guide/synthetic/index.md` | `https://rs.tdwg.org/bdq/doc/synthetic/` |
| BDQ Supplemental Information | `docs/supplement/index.md` | `https://rs.tdwg.org/bdq/doc/supplement/` |
| Tutorial: From Use Case to Test | `docs/tutorial/index.md` | `https://rs.tdwg.org/bdq/doc/tutorial/` |
| Lists of Terms (7) | `docs/list/{vocabulary}/index.md` | `https://rs.tdwg.org/{vocabulary}/doc/list/` (decided 2026-11-09, Section 8.2.1) |

Reasons: it is consistent with the Lists of Terms decision; the path says which vocabulary a document is about, so short names such as `guide` can repeat (as `ac/doc/guide/` does) without names that encode the kind of document; it needs no new routes, since every IRI has one name segment after `doc/` (`restxq.xqm` treats a second segment as a version date); and it follows the `docs/list/`, `docs/guide/`, `docs/extension/` layout of the published documents. Existing TDWG standards put all their documents under the standard's abbreviation (Darwin Core: 12 documents under `dwc/doc/`, including per-vocabulary Lists of Terms such as `dwc/doc/doe/`; Audiovisual Core: 10 under `ac/doc/`); BDQ's per-vocabulary documents depart from that, as its Lists of Terms already do.

These IRIs do not collide with the vocabulary and term list IRIs: the ontology document is distinct from the ontology `https://rs.tdwg.org/bdqffdq/` (the vocabulary IRI, Section 9.5), and the Vocabulary Extension document from the extension term list `https://rs.tdwg.org/bdqffdq/extension/` (Section 9.6), whose HTML representation it is (SDS 3.3.3), just as a List of Terms is distinct from its term list.

*Also decided 2026-11-12:*

- **The Quick Reference Guide is one document.** Its term descriptions page (`bdqtest_qrg_term_descriptions.md`) and its index pages (`qrg_index_by_dimension.md`, `qrg_index_by_ie_actedupon.md`, `qrg_index_by_ie_class.md`, `qrg_index_by_usecase.md`, `qrg_multirecord_index.md`) are supporting parts of it, not separate documents.
- **The index of normative sections** (`docs/normative_index.md`) is not a document of the standard: it is an artifact that helps development and review.
- **On the review site, each document has only its latest version**, dated 2026-11-09 (declared in that release), not placeholder versions from draft dates as the terms have (Section 8.5). The Lists of Terms keep the versions that the release sequence gives them.

Document version IRIs are `{document IRI}{YYYY-MM-DD}`, e.g. `https://rs.tdwg.org/bdq/doc/supplement/2026-11-09`. Like the List of Terms IRIs, they are baked into records by `process.py`, so they must not change after ratification.

### 11.4 Processing steps

1. Convert each document's `document_configuration.yaml` and the shared contributors into a `documents` entry (Section 11.2), with the IRI from Section 11.3, in the 2026-11-09 release `config.yaml` on `bdq-source` (review only: a conversion script, like `bdq_to_rs.py`, and afterwards the entries are edited in place). *Done 2026-11-12:* `process/bdq-revisions/bdq_docs_to_rs.py` (`bdq-source` `94c6196e`) declares the ten documents other than the Lists of Terms. `accessUrl` and `browserRedirectUri` are derived from each document's published location (the `/draft/` pages, provisional), and the publisher and license come from `document_defaults`, as for the Lists.
2. Process the release sequence on `bdq` (Section 8.5); the documents get their first version in the 2026-11-09 release. The standard version of 2026-11-09 lists them as parts. *Done 2026-11-12* (`bdq` `10172532`, a same-release rerun of 2026-11-09): only the document tables and the standard's parts changed; deployed on bdq-public-review.rs.tdwg.org, where each document IRI and its 2026-11-09 version return RDF and redirect HTML requests to the published page.
3. In later releases, mark a document `modified: true` when it changes; a release that changes the `bdqffdq` axioms also marks the Vocabulary Extension document (Section 9.6).
4. The document IRIs are `https`. The document handlers in `restxq.xqm` find the scheme of an IRI from the data (`page:canonical-iri` tries `http`, then `https`), not from a list of vocabularies, so the `bdq/doc/` IRIs need no change; checked 2026-11-12.
5. In this repository, the build writes the IRIs into each document's header ("This version", "Latest version", "Previous version", citation). *Done 2026-11-12* (option (a), decided 2026-11-12): `current_iri` in each `document_configuration.yaml` is the document IRI, and the version cited ("This version", "Date version issued", citation year, "Previous version") is the latest version of the document in rs.tdwg.org's `docs-versions/docs-versions.csv`, read from the `bdq` branch for the review (`function_lib.rs_document_version`; `master` after ratification), rather than `doc_modified`, which named versions that do not exist in rs.tdwg.org. A document without versions there falls back to `doc_modified`. The move of the `document_configuration.yaml` content to rs.tdwg.org remains a follow-up (Section 13).
6. Add each document to `index/dereferencing-test.py`, and check that the HTML redirect goes to the published page.

---

## 12. Concrete change list per file in rs.tdwg.org

### 12.1 Created by `process.py` for each new BDQ term list

For each of `bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval`, and (Option C) `bdqffdq`, and (T1/T3) `bdqtest`: the `<db>/` and `<db>-versions/` directories with core CSV, `constants.csv`, `namespace.csv`, `-column-mappings.csv`, `-classes.csv`, `-replacements*.csv`, and `linked-classes.csv`; rows in `index/index-datasets.csv`, `term-lists/term-lists.csv` (and versions/members tables), `vocabularies/`, `vocabularies-versions/`, `standards/`, `standards-versions/`, and `html/redirects.csv` (`process/process.py:76-189`, `490-545`, `632-673`, `738-1215`).

### 12.2 Hand-edited inputs

- `process/bdq-revisions/bdq-revisions-YYYY-MM-DD/`: modification CSVs, `config.yaml`, and `vocab.yaml` per vocabulary (Section 8.2).
- Custom column mapping edits for extra columns (Sections 8.3, 9.3, 10.2).
- `process/document_metadata_processing/<doc-dir>/document_configuration.yaml` and `authors_configuration.yaml` per BDQ document.
- Option C: `bdqffdq/bdqffdq-axioms.ttl`. T1/T3: the `bdqtest` auxiliary GUID tables.

### 12.3 `process/process.py`

*Done* (`bdq-source`, Section 7.4 status): vocabulary version IRIs take the scheme of the configured vocabulary IRI, and preflight validates the scheme. No other change is needed for the simple vocabularies. T3 adds a separate BDQ-specific processing step rather than changing `process.py`.

### 12.4 `html/restxq.xqm`

- *Done:* add `page:canonical-iri` and use it in the document, vocabulary, and term list handlers and their version handlers, so each resolves to whichever scheme is recorded (Section 7.4).
- *Done:* `html/html.xqm`: make the term version test and the vocabulary version IRI scheme-aware (Section 7.4).
- Option A or C: a route for the whole `bdqffdq` ontology (redirect, or file serving as in Option B1).
- T3: a route `/bdqtest/terms/{id}` serving generated per-Test files.

### 12.5 `index/dereferencing-test.py`

Accept `https://rs.tdwg.org/` URLs (*done*, for database and document examples) and check that `https` vocabularies return `https` subjects, and add BDQ examples: a term from each simple vocabulary, a `bdqffdq` term and the ontology, a `bdqtest` Test, and the BDQ documents.

### 12.6 Documentation in rs.tdwg.org

`process/process-vocabulary.md` Section 3.3 now records the per-vocabulary protocol rule (*done*). It and `README.md` should also record that BDQ uses `https` IRIs, and describe any BDQ-specific steps (the `bdqffdq` merge, the `bdqtest` generation step).

### 12.7 No change needed

`index/load-db-from-github.py` and `docker/initialize-database.sh` need no change, provided BDQ CSV headers are valid XML names and datasets follow the standard layout.

---

## 13. Changes needed in `tdwg/bdq`

- Retire the five simple `*_term_versions.csv` files and, when moved, `bdqtest_term_versions.csv`, the `tg2/core/` GUID tables, and `bdqffdq.owl`; update `tg2/_review/vocabulary/README.md` to say they are frozen and that the source is rs.tdwg.org (the README already anticipates this).
- Point the build scripts at rs.tdwg.org. `tg2/_build_review/draft_build-termlist.py` reads `../_review/vocabulary/{term}_term_versions.csv` (`217`) and already has the rs.tdwg.org pattern commented out (`53`: `githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + github_branch + '/'`). Other readers of `bdqtest_term_versions.csv` include `build_bdqtest_rdf.py`, `draft_build_bdqtest_qrg.py`, `draft_build_bdqtest_singlerecord_tests_current.py`, `draft_build-docs.py`, `draft_build-termlist_bdqtest.py`, `generate_bdq_qrg_filtering.py`, `make_bdq_tests_vertical.py`, `postprocess_autolink_terms.py`, and `tools/find_current_tests_in_csv_missing_from_rdf.py`.
- Retire `tg2/_build_review/temp_term-lists.csv` and `temp_namespaces.yaml`.
- Replace `kurator-ffdq` in `tg2/_make_review/copy_files.sh:52-61` with `build_bdqtest_rdf.py`.
- Generate `dist/bdqffdq.{ttl,rdf,jsonld}` by running the rs.tdwg.org ontology generator in the build, replacing `tg2/_review/vocabulary/bdqffdq.owl` and `vocabulary/bdqffdq.ttl` (Sections 6.4, 9.5).
- Generate all whole-vocabulary files in `tg2/_review/dist/` from rs.tdwg.org files, and record the rs.tdwg.org commit they were built from (Section 6.4).
- ~~Update the document IRIs in all document headers and `document_configuration.yaml` files~~ *Done 2026-11-12* (`dea12bcb`, `b7492f52`; Section 11.4): `current_iri` is the decided document IRI in all 17 `document_configuration.yaml` files (with `accessUrl` and `browserRedirectUri` corrected), and the headers' "This version", "Date version issued", citation year, and "Previous version" come from the document versions in rs.tdwg.org. *Done 2026-11-12* (`f9a01c34`): the landing page, which is not a document (Section 11.3), has the standard IRI as `current_iri`, and its header cites the standard's versions in rs.tdwg.org (`http://www.tdwg.org/standards/YYY/version/<date>`; `function_lib.rs_document_version` falls back to `standards-versions.csv`); it had cited `http://rs.tdwg.org/bdqffdq/2026-06-03`.
- The generated Lists of Terms cite term versions in the SDS 2.3.2 form `…/terms/<local name>-<date>` (e.g. `https://rs.tdwg.org/bdqcrit/terms/NotEmpty-2024-09-30`), which rs.tdwg.org does not serve: its term version IRIs are `…/terms/version/<local name>-<date>` (question 16). With the site's links to bdq-public-review.rs.tdwg.org (below), these links return 404.
- ~~The landing page gives `https://rs.tdwg.org/bdq/` as a "Vocabulary IRI"~~ *Done 2026-11-12* (`f9a01c34`): Section 3.3.3 "Landing Page IRIs" of the landing page lists the standard, vocabulary, term list, vocabulary extension, and document IRIs as decided (Sections 8.2.1, 9.5, 9.6, 11.3), with the documents' pages, how HTML and RDF are served, and that the IRIs are served at bdq-public-review.rs.tdwg.org for the review. It had linked 21 pages on bdq.tdwg.org that do not exist, the nonexistent `https://rs.tdwg.org/bdq/` as the `bdqval` vocabulary IRI, and RDF on bdq.tdwg.org. Section 1.8's example namespace IRI, whose closing quote had become part of its link, is now in code with its trailing slash. All 29 links to bdq-public-review.rs.tdwg.org in Section 3.3.3 resolve.
- `generate_bdq_qrg_filtering.py` uses `doc_created` as the date of the Quick Reference Guide's supporting pages; it should use the Quick Reference Guide's version from rs.tdwg.org, like the headers.
- *Done 2026-11-12* (`097a86ad`): the site (`_site_resources/render_site_links.py`) links `https://rs.tdwg.org/bdq…` IRIs to the same paths on `https://bdq-public-review.rs.tdwg.org`, showing the IRI as the link text; IRIs not yet deployed there stay plain text: the `bdqtest` vocabulary, its RDF, terms, term list, and List of Terms (`e71048be`, `2b16beef`; its other documents are linked). The placeholder standard IRI `http://www.tdwg.org/standards/YYY` and its version IRIs are plain text too (`2b16beef`). Autolinks in the document headers, which had remained links to rs.tdwg.org, follow the same rule. After ratification, the mode becomes "keep", and the `bdqtest` entries are removed when it is deployed.
- ~~Correct the `bdquc` List of Terms title~~ Done 2026-11-12: "BDQ Use Case Controlled Vocabulary List of Terms" in `tg2/_build_review/templates/list/bdquc/document_configuration.yaml` and in the rs.tdwg.org inputs (Section 11.2); the published document's heading changes with the next build.
- *Done 2026-11-09 (Section 9.5, status):* the generated ontology replaces `bdqffdq.owl` (form 2 axioms, ontology IRI `https://rs.tdwg.org/bdqffdq/`), the Vocabulary Extension renders the restrictions on classes and `owl:AllDifferent`, and the guide is corrected. Remaining: move the build's references from `vocabulary/bdqffdq.owl` to `dist/bdqffdq.ttl`, and have the build run `build_ontology.py` against a pinned rs.tdwg.org commit instead of copying its output (Section 6.4).
- Apply the `bdqffdq` fixes: declare `skos:scopeNote` (done by the generator; `rdf:value` is kept in the source and replaced in the OWL serializations, Section 9.5), replace the 15 restriction ranges with named-class ranges, and (for Section 9.4) replace `owl:AllDisjointClasses` with pairwise `owl:disjointWith` (Sections 3.2, 3.3).
- Change the remaining `http://rs.tdwg.org/bdq…` IRIs to `https` (Section 7.2).
- Replace standard IRI placeholders once a number is assigned.
- `bdqtest` generation (Section 10.9.4): emit `bdqffdq:hasDateLastUpdated` in every Test's graph; build version IRIs from `issued` everywhere (List of Terms, Quick Reference Guide, the `iri` column), in the form decided under Section 10.9.6; clarify in the Implementers guide what an implementation cites; define the information element of `MEASURE_AMENDMENTS_PROPOSED` and include it (Section 10.9.7).

---

## 14. Recommended implementation approach

1. **Agree on per-vocabulary `https`** with the rs.tdwg.org maintainers and the TDWG Technical Architecture Group, and patch `process.py`, `restxq.xqm`, `html.xqm`, and `dereferencing-test.py` on the `bdq` branch (Section 7.4).
2. **Deploy the five simple vocabularies** through `process.py` (Section 8), completing the standard-record bootstrap first (Section 8.2.1), using a source branch and `bdq` as the derived, deployed branch, and verify them on `bdq-public-review.rs.tdwg.org`.
3. **Deploy `bdqffdq` as a hybrid** (Option C): term list via `process.py`, axioms file, merge step, and a route or redirect for the whole ontology. If the BDQ maintainers first replace the restriction ranges and `owl:AllDisjointClasses` axioms (Section 3.3), no axioms file is needed (Section 9.4).
4. **Deploy `bdqtest` with full graphs** (T3): the flat term list and GUID tables in rs.tdwg.org as the source, the full graph of each Test generated and served from its IRI, and the complete serializations built from the same files. T1 and T2 are rejected (Section 10).
5. **Switch the BDQ build** to read from rs.tdwg.org, and freeze the files in `tg2/_review/vocabulary/`.
6. After ratification, the rs.tdwg.org maintainers merge the source branch to `master`, rerun processing with the ratification date, and make a release.

---

## 15. Open questions for maintainers

1. Will the TDWG Technical Architecture Group accept `https` as a canonical protocol for new TDWG vocabularies, chosen per vocabulary, and will the rs.tdwg.org maintainers accept the corresponding patches to `process.py`, `restxq.xqm`, and `html.xqm` (Section 7.4)?
2. Will the rs.tdwg.org maintainers accept routes that serve files directly (Option B1, T3), a pattern rs.tdwg.org has not used before? *For `bdqtest`, needed:* T3 is required for the public review, since T1 and T2 are rejected (Section 10.7). *For `bdqffdq`, not needed:* the whole-ontology files are published from this repository's `dist/` (Sections 6.4, 9.5). A narrower case is now implemented on `bdq-source`: rs.tdwg.org appends a vocabulary extension term list's axioms, read from files, to that list's RDF (Section 9.6; question 15).
3. For `bdqffdq`, should the ontology IRI `https://rs.tdwg.org/bdqffdq/terms` and the term list IRI `https://rs.tdwg.org/bdqffdq/terms/` denote the same resource, or should one change? *Decided 2026-11-09:* following SDS 4.4.2.2, the ontology IRI becomes the vocabulary IRI `https://rs.tdwg.org/bdqffdq/`, and the axioms are the extension term list `https://rs.tdwg.org/bdqffdq/extension/` (Section 9.5). With the whole-ontology files in `dist/` (Section 6.4), the ontology IRI could redirect to them by media type. SDS Section 4.4.2.2 gives the combined ontology its own IRI, distinct from the basic term list, which is not declared an `owl:Ontology`; this suggests keeping the two IRIs distinct.
4. What standard number will BDQ be assigned, and what are the final (non-`/draft/`) URLs for the BDQ documents on `bdq.tdwg.org`, to be used in `prepend_url` and in any redirect targets? Until it is assigned, the placeholder `http://www.tdwg.org/standards/YYY` is used on the `bdq` branch (Section 8.2.1).
5. Should the structural nodes of `bdqtest` (Methods, Specifications, Arguments, information element nodes, Policies), now identified by non-resolvable `urn:uuid:` IRIs, be given resolvable rs.tdwg.org IRIs (Section 10.6)? *Decided (2026-11-10), at least for now:* no (Section 10.6).
6. For `bdqffdq`, will the BDQ maintainers replace the 15 restriction ranges with named-class ranges (and the `owl:AllDisjointClasses` axioms with pairwise `owl:disjointWith`), making the ontology free of blank nodes (Sections 3.3, 9.4)? *Decided 2026-11-09:* no; the ranges become restrictions on the subject classes (`owl:allValuesFrom`, form 2), as the Concepts and Use guide describes, and stay in the extension term list (Section 9.5).
7. What IRIs should the BDQ documents have, including the Quick Reference Guide and its index pages (Section 11.3)? The landing page is covered by the standard record. *Lists of Terms decided:* `https://rs.tdwg.org/{vocabulary}/doc/list/`. *Decided 2026-11-12:* scheme B, with the Quick Reference Guide as one document and the index of normative sections not a document (Section 11.3).
8. Should rs.tdwg.org support ontologies with blank nodes (class expressions) in general, for future versions of `bdqffdq` or for other standards (Section 3.3)?
9. Should rs.tdwg.org CI adopt BDQ-specific semantic validation (SHACL/SPARQL checks), or should that remain in this repository, reading from rs.tdwg.org?
10. For public review, are the generated `recommended` standard-version status and version date, and any `recommended` term, vocabulary, and term-list versions, acceptable on `bdq-public-review.rs.tdwg.org`, or do they need adjusting (Section 8.2.1; `process/process.py:1110`)? *Decided:* keep `recommended`; the standard record's status is `Draft Standard`.
11. Will the rs.tdwg.org maintainers fix the JSON-LD serializer so that a repeated predicate becomes one key with an array of values, rather than duplicate keys of which parsers keep only the last (Section 8.3, *Served output*)? This changes JSON-LD served for existing vocabularies (e.g. `dwc:eventDate`), as a correction. Filed as [tdwg/rs.tdwg.org#619](https://github.com/tdwg/rs.tdwg.org/issues/619), with a proposed fix (`fcac8741` on `bdq-source`). The rs.tdwg.org maintainers confirmed the problem (it was known since about 2020: the JSON-LD validates, but a triplestore loads only one of the values). The fix is proposed in pull request [tdwg/rs.tdwg.org#621](https://github.com/tdwg/rs.tdwg.org/pull/621), from a branch off `master` with the commit cherry-picked, tested against production rs.tdwg.org (216 resources in four formats: 823 responses byte-identical, 30 JSON-LD responses corrected, recovering 243 triples; dereferencing test passes).
12. Will the rs.tdwg.org maintainers accept the same-release rerun fix for term lists and documents created by the release (Section 8.3, *Rerunning*)?
13. Should the `bdqffdq` (and other BDQ) draft revision dates be kept, either as earlier TDWG versions or as information outside the SDS date properties, or should the first rs.tdwg.org release date stand as the date the terms were created (Section 9.5, *Term dates*)? *Decided 2026-11-09:* kept on the review site, as placeholder term versions with the draft dates, processed as a sequence of draft releases; on ratification they become real term versions with the release date (Section 8.5).
14. Following SDS Section 4.5, should the entailment-producing properties of `bdqffdq` (`rdfs:subClassOf`, `rdfs:subPropertyOf`, `rdfs:range`) move from the basic term list to the extension list, and how should rs.tdwg.org represent an extension list that has row-shaped axioms (Section 9.5, *Entailment properties*)? *For discussion;* for now the boundary stays where it is.
15. Will the rs.tdwg.org maintainers accept vocabulary extension term lists as implemented on `bdq-source` (Section 9.6): the `extension_lists` declaration in `config.yaml` and `process/extension_lists.py`; the new linked tables for term list distributions, following the Document distributions rather than SDS 4.4.3's `ac:accessURI`; the lookup tables for browser redirects and axioms; and `restxq.xqm` appending an extension list's axioms to its RDF, the first time rs.tdwg.org returns content from a file rather than only from its tables (question 2)? And the link from a release's decision to the extension term list when the release creates a version of it, by the list's IRI (Section 9.6, *Changing the axioms*)?
16. TDWG version IRIs: SDS 2.3.2 forms a version IRI by appending the date to the IRI of the resource (`…/terms/<local name>-<date>`), while every TDWG-minted term version in rs.tdwg.org uses `…/terms/version/<local name>-<date>`, and the SDS's own examples do not resolve on rs.tdwg.org. Which form is canonical for `bdqtest`, whose identifiers followed the SDS and are used by implementations, and should the other forms in use resolve to it (Section 10.9.6; current leaning: option C)?

---

## 16. Final conclusion

rs.tdwg.org can be the source of truth for all BDQ vocabularies, with differing degrees of fit:

- The five simple vocabularies fit the standard `process.py` pipeline, but still need the Section 8 preparation: column-mapping additions (8.3), data fixes (8.4), version-date choices (8.5), HTML redirects (8.6), and the standard-record bootstrap (8.2.1).
- `bdqffdq` fits as a hybrid: an ordinary term list for the per-term metadata, which is almost all of the ontology, plus a small axioms file for the restriction ranges and disjointness axioms, merged to produce the complete ontology. If the restriction ranges, which appear to be unintended, are replaced by named-class ranges and the disjointness axioms by pairwise `owl:disjointWith`, the ontology has no blank nodes and the term list alone is enough.
- `bdqtest` can be versioned as a flat term list with its GUID tables in rs.tdwg.org, but full-fidelity per-Test RDF from rs.tdwg.org needs either generated per-Test files served by a new route (recommended target) or an extension of the serializer.

In every case, the term-version files become outputs of rs.tdwg.org processing, and the BDQ build in this repository becomes a consumer of rs.tdwg.org data.
