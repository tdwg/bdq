# Deploying BDQ content to rs.tdwg.org

This document describes work within the scope of [tdwg/bdq issue #340](https://github.com/tdwg/bdq/issues/340), "BDQ Review - Deploy BDQ Documentation from GitHub to TDWG web site": deploying the BDQ vocabularies to `rs.tdwg.org`, initially to the `bdq` branch of the `tdwg/rs.tdwg.org` repository (deployed at `bdq-public-review.rs.tdwg.org`), such that files in `rs.tdwg.org` become the source of truth for BDQ vocabulary metadata, rather than the files in the `tdwg/bdq` repository.

## Source of this document

This is an analysis originally produced by GitHub Copilot of the friction produced by the bdqffdq.owl ontology and the multiplicity of terms in the bdqtest vocabulary for deployment on rs.tdwg.org and how this friction might be approached.

**Revision note (2026-09-28):** Revised in place with Claude Code (Claude Opus 5.5) after checking each citation against the `rs.tdwg.org` repository (branch `bdq`, at that time identical to `master`) and this repository. Changes: corrected inaccurate citations and claims (ABCD handling, BDQ information element model, build pipeline, loader behavior); added deployment, routing, and `https` analysis; reframed the source of truth from "BDQ repository authoritative, rs.tdwg.org derived" to "rs.tdwg.org files authoritative for all BDQ vocabularies"; added sections on deploying the simple vocabularies (`bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval`), options for `bdqffdq` (including a hybrid CSV + axioms approach), options for `bdqtest`, and the changes needed in this repository. Line numbers cited below are as of this revision.

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

## Executive summary

`rs.tdwg.org` is fundamentally a **CSV/YAML-driven metadata publishing system**, not a general RDF graph host. Its normal workflow is:

1. maintain hand-edited CSV/YAML input files;
2. run Python processing (`process/process.py`) to generate current-term, version, hierarchy, redirect, and index CSV tables;
3. load those CSV files into BaseX as XML when the Docker image is built;
4. generate RDF/HTML dynamically through XQuery and content negotiation.

For BDQ this means:

- **The five simple vocabularies** (`bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval`) fit the normal pipeline. Each becomes its own vocabulary with one term list, processed by `process.py`, once small patches for `https` are made and a few data problems are fixed (Section 8).
- **`https` as the canonical protocol** is supported for term IRIs as things stand, but `process.py` and `html/restxq.xqm` hard-code `http://rs.tdwg.org/` for vocabulary, term list, and document IRIs. BDQ would be the first `https` vocabulary on rs.tdwg.org. The patches can be made on the `bdq` branch, but need agreement from the rs.tdwg.org maintainers and the TDWG Technical Architecture Group before merging to `master` (Section 7).
- **`bdqffdq`** cannot be represented as CSV rows without loss, because of 15 blank-node `owl:Restriction` ranges and 2 `owl:AllDisjointClasses` axioms. However, nearly everything else in the ontology is simple IRI- or literal-valued, so a hybrid, with term metadata in an rs.tdwg.org term list and the remaining axioms in a small Turtle file in rs.tdwg.org, is feasible (Section 9).
- **`bdqtest`** can have its source of truth in rs.tdwg.org, but the generic rs.tdwg.org serializer cannot produce the full per-test graph: `linked-classes.csv` links only one level deep, and many BDQ nodes have `urn:uuid` IRIs. Full-fidelity per-test RDF from rs.tdwg.org requires either generated per-test files served by a new route, or an extension of the serializer (Section 10).

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

The `@base <https://rs.tdwg.org/bdqffdq/terms#>` and the empty `:` prefix (`bdqffdq.owl:1`, `10`) are not used by any term and could be removed.

### 3.3 Consequence

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
- Methods, Specifications, information elements, Arguments, and Policies have `urn:uuid` IRIs, which cannot be dereferenced over HTTP; they can only appear inside a graph returned for some other IRI.

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

Splitting these into separate datasets (Specifications with linked Arguments, information elements with linked members) does not help per-Test dereferencing: the roots of those datasets have `urn:uuid` IRIs, which no HTTP request can reach, and a request for a Test IRI returns only the Test and its direct children.

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
| `bdqffdq` | Recommended: hybrid, a term list CSV plus a small axioms Turtle file, both in rs.tdwg.org. Alternatively, the whole ontology file in rs.tdwg.org | Term-level RDF: rs.tdwg.org serializer. Whole ontology: build step merging CSV and axioms | 9 |
| `bdqtest` | CSV (a flat, versioned term list plus auxiliary tables) in rs.tdwg.org | Term-level: rs.tdwg.org serializer (flat) or served generated files (full). Whole vocabulary: build step, in either repository | 10 |

### 6.3 What stays in `tdwg/bdq`

- The human-readable documents (List of Terms, guides, Quick Reference Guide) and their build scripts, published on `bdq.tdwg.org`; these become consumers of rs.tdwg.org data.
- Build, audit, and validation scripts (SHACL, SPARQL, consistency audits, `tg2/_make_review/do_build.sh:7-30`; `tg2/_build_review/tools/validate_bdqtest_against_shacl.py:5-20`, `85-87`). These should read from rs.tdwg.org (a local checkout, or `https://raw.githubusercontent.com/tdwg/rs.tdwg.org/<branch>/`).
- Generated distributions such as `bdqtest.ttl`, if they are built here from rs.tdwg.org data (Section 10).

---

## 7. `https` as the canonical protocol for BDQ IRIs

### 7.1 What already works

- Term IRIs in RDF output are built from the dataset's `domainRoot` in `constants.csv`, which `process.py` derives from the configured namespace URI (`process/process.py:119`, and `173` for the versions dataset), so `https://rs.tdwg.org/bdqdim/terms/` produces `https` term and term-version IRIs.
- Term lookup is by local name, so `https://…/bdqdim/terms/Completeness` and `http://…/bdqdim/terms/Completeness` both resolve.
- Term list version IRIs are derived from the term list URI (`process/process.py:414-416`), so they keep `https`.
- The `list_localName` for `term-lists.csv` is taken from path segments (`process/process.py:337-338`), independent of scheme.
- The server answers `https` requests (Section 1.4).

### 7.2 What needs changing

1. **`process/process.py:747`, `750`** hard-code `http://rs.tdwg.org/` for the vocabulary IRI and vocabulary version IRI. Patch: take the scheme from `termlist_uri` (e.g. `termlist_uri.split('//')[0] + '//rs.tdwg.org/' + vocab_subpath + '/'`).
2. **`html/restxq.xqm`** hard-codes `http://rs.tdwg.org/` in lookups for documents (`111-137`), vocabularies (`246-256`), vocabulary versions (`280-284`), term lists (`302-306`), and term list versions (`324-328`). Patch: when the `http` lookup finds nothing, retry with `https` (or the reverse). Without this, `https://rs.tdwg.org/bdqdim/terms/`, `https://rs.tdwg.org/bdqdim/`, and BDQ document IRIs return 404.
3. **`index/dereferencing-test.py:94`** skips URLs not beginning with `http://rs.tdwg.org/`. Patch: accept `https://rs.tdwg.org/` too.
4. **Consistency in this repository.** BDQ documents and data currently mix `https://rs.tdwg.org/bdq…` (the large majority) with some `http://rs.tdwg.org/bdq…` IRIs; the `http` occurrences should be changed.

### 7.3 Governance

BDQ would be the only `https` vocabulary on rs.tdwg.org; every existing `domainRoot` and hierarchy IRI is `http`. The patches can be made on the `bdq` branch for the public review, but merging them to rs.tdwg.org `master` needs agreement from the rs.tdwg.org maintainers and the TDWG Technical Architecture Group. That agreement should be sought early, as the IRIs cannot change after ratification.

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

### 8.2 Processing runs

`process.py` processes one vocabulary per run (`process/process-vocabulary.md:124`), so five runs are needed, one per vocabulary, each with:

- a hand-edited modification CSV, e.g. `process/bdq-revisions/bdq-revisions-YYYY-MM-DD/bdqdim_YYYY-MM-DD.csv`;
- a `config.yaml` with `vocab_type`, `date_issued`, `standard`, `list_of_terms_iri`, `decisions_text`, and one namespace block (`namespace_uri: https://rs.tdwg.org/bdqdim/terms/`, `pref_namespace_prefix: bdqdim`, `database: bdqdim`, `borrowed: false`, `new_term_list: true`, `termlist_uri: ''`, `prepend_url`, `use_namespace_in_fragment: true`, `separator: '_'`);
- a `vocab.yaml` with the vocabulary label and description, `dc_creator`, license, and (for the first run) the standard label and description;
- the document metadata files `document_configuration.yaml` and `authors_configuration.yaml` under `process/document_metadata_processing/rs.tdwg.org_bdq_doc_dim/` (or whatever directory name the IRI pattern gives), followed by a run of `tdwg_docs_metadata_update.py`.

The standard needs a real number: `process.py` extracts it from the standard IRI (`process/process.py:983`). BDQ documents still contain placeholders (`https://www.tdwg.org/standards/nnnn`, `http://example.org/to_be_determined`). The first run creates the standard record (from `process/files_for_new_template/new_standard.csv`); later runs with the same `date_issued` add their vocabulary versions to the same standard version.

`process.py` creates the dataset directories, `constants.csv`, `namespace.csv`, mapping and classes files, and the rows in `index/index-datasets.csv`, `term-lists/term-lists.csv`, and `html/redirects.csv`, from the templates in `process/files_for_new/`.

### 8.3 Column conversion

The current `*_term_versions.csv` columns map to the rs.tdwg.org hand-edited input columns (`process/example-spreadsheets/`) as follows:

| BDQ column | rs.tdwg.org input column | Notes |
|---|---|---|
| `term_localName` | `term_localName` | |
| `label` | `label` | The template maps `label` to both `rdfs:label` and `skos:prefLabel`. Where BDQ's `prefLabel` differs from `label` (e.g. `Assumed Default` vs `AssumedDefault`), add a `prefLabel` column and edit the mapping so `skos:prefLabel` comes from it. |
| `prefLabel` | see above | |
| `definition` | `definition` | Mapped to `rdfs:comment` and `skos:definition`. |
| `comments` | `notes` | Template maps `notes` to `dcterms:description`; `bdqffdq` uses `skos:note`, so consider changing the mapping for consistency. |
| `organized_in` | `tdwgutility_organizedInClass` | Needs cleaning: `bdqcrit`, `bdqdim`, `bdqenh` put the term list IRI here; `bdquc` and `bdqval` put a class CURIE; two `bdqval` rows contain the bare string `Data`. The value must be a full class IRI, or empty. |
| `rdf_type` | `type` | Must be a full IRI, not a CURIE. `bdqval` rows with `bdqffdq:Parameter, owl:NamedIndividual` need a second column (e.g. `type1`) also mapped to `rdf:type` (Section 2.2). |
| `controlled_value_string` | `controlled_value_string` | Mapped to `rdf:value`. |
| `hasFitnessRequirements`, `scopeNote` (`bdquc` only) | same | Extra columns need rows added to the column mapping files (`process/process-vocabulary.md` Section 3.1). |
| `iri`, `term_iri`, `issued`, `status` | none | Generated by `process.py`. |
| `flags` | none | Internal to BDQ; drop, or keep as an unmapped column. |

`vocab_type`: these terms are instances of `bdqffdq` classes with controlled value strings, but they are not SKOS concepts in a concept scheme. Type 1 (simple vocabulary) with an added `controlled_value_string` column fits better than type 2, which assumes `skos:inScheme`. `process.py` does not validate the `type` column, despite `process/create-vocabulary.md` saying it must be `rdf:Property`, `rdfs:Class`, or `skos:Concept`.

### 8.4 Data problems to fix before import

- `bdqenh` and `bdqcrit` version IRIs lack `/version/` (e.g. `https://rs.tdwg.org/bdqenh/terms/AssumedDefault-2024-09-30`).
- The `term_iri` values for `bdquc:SDM-Trees` and `bdqval:AggregatedTestResponseOutcomes` contain `/version/`.
- `bdquc:SDM-Trees` has controlled value `Species-Distribution-Modeling-Trees`, which does not match its local name, and its fitness requirements refer to `bdquc:Species-Distribution-Modeling-Trees`.

### 8.5 Version dates

`process.py` gives every version created in a run the single `date_issued` from `config.yaml`. The version IRIs currently cited in BDQ documents (`…-2024-09-30`, `…-2026-04-22`) will not exist on rs.tdwg.org. The first rs.tdwg.org version of each term should carry the date of the processing run (for the public review) and, after ratification, the ratification date; BDQ documents must be regenerated to cite the rs.tdwg.org version IRIs.

### 8.6 Redirects for HTML

`process.py` writes the `html/redirects.csv` row from `prepend_url`, `use_namespace_in_fragment`, and `separator` (`process/process.py:632-673`; `process/process-vocabulary.md:73-77`). The BDQ List of Terms documents already use anchors of the form `bdqdim_Completeness`, so `use_namespace_in_fragment: true` and `separator: '_'` fit, with `prepend_url` set to the published List of Terms URL plus `#` (currently `https://bdq.tdwg.org/draft/docs/list/bdqdim/#`; this should be changed to the final location before release).

### 8.7 Branch workflow

`process/process-vocabulary.md` Section 2.3 separates a source branch (steps 1-10, input files only) from a disposable derived branch (steps 11-17, generated files), so that the processing can be rerun from clean inputs. Because the `bdq` branch is the deployed branch (Section 1.4), it has to be the **derived** branch; the inputs should be kept on a separate source branch (e.g. `bdq-source`). To revise, correct the inputs on the source branch, then recreate `bdq` from it and rerun the processing. After ratification, a pull request from the source branch into `master` is merged by the rs.tdwg.org maintainers, who rerun the processing with the ratification date.

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

### 9.3 Option C (recommended): hybrid, term list CSV plus axioms file

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
   | `controlled_value_string` | `rdf:value` | plain |
   | `differentFrom`, `differentFrom1` | `owl:differentFrom` | iri |

   The per-term `dcterms:issued` in the ontology is replaced by the `dcterms:created`/`dcterms:modified` and term versions that `process.py` generates. `namespace.csv` needs `owl`, `skos`, and `bdqffdq` entries.

2. **Axioms file.** `bdqffdq/bdqffdq-axioms.ttl` in rs.tdwg.org containing the ontology header (`owl:Ontology`, label, notes, license, `owl:versionIRI`), the 15 `owl:Restriction` ranges, and the 2 `owl:AllDisjointClasses` axioms, i.e. about 80 triples. It is edited by hand when those structures change, which is rare.

3. **Merge step.** A script (in rs.tdwg.org `process/`, or in this repository reading from rs.tdwg.org) builds `bdqffdq.ttl`, `.rdf`, and `.jsonld` from `bdqffdq/bdqffdq.csv` plus the axioms file, using the same column mappings. When first built, it should be checked for graph isomorphism against the current `bdqffdq.owl` (rdflib `isomorphic`), apart from the intended changes (`dcterms:issued`, version IRI).

4. **Serving.**
   - Term IRIs (`https://rs.tdwg.org/bdqffdq/terms/{term}`) dereference through the generic handler from the term list: labels, definitions, types, subclass and subproperty links, named ranges, versions. Restriction ranges are absent from term-level responses.
   - The whole ontology is served either from generated files in rs.tdwg.org (a route like Option B1) or from `bdq.tdwg.org` (a redirect like Option A).
   - The ontology IRI `https://rs.tdwg.org/bdqffdq/terms` and the term list IRI `https://rs.tdwg.org/bdqffdq/terms/` resolve through the same handler (`html/restxq.xqm:289-310`). Either they are treated as the same resource, with that route (once patched for `https`, Section 7.2) returning the term list, which links to the ontology serializations, or a dedicated route returns the ontology.

5. **Ontology version IRI.** Replace `owl:versionIRI <https://rs.tdwg.org/bdqffdq/terms/1.0>` with the term list version IRI that `process.py` generates (`https://rs.tdwg.org/bdqffdq/version/terms/YYYY-MM-DD`), so the ontology version and the TDWG version hierarchy coincide. This also avoids `1.0` being read as a term local name.

6. **Editing workflow.** Term additions and changes go through the normal modification CSV and `process.py`; axiom changes are edits to the axioms file on the same source branch; the merge step is rerun. Editing in Protégé is no longer the primary workflow (Protégé can still be used to check the merged file).

Assessment: meets the target (source in rs.tdwg.org, term metadata in CSV), gives `bdqffdq` terms the same TDWG version history and dereferencing as other vocabularies, and keeps the graph-native parts in RDF. Costs: a custom mapping file, a merge script, the risk of the two sources drifting (mitigated by the isomorphism check and a check that every IRI in the axioms file is a term in the CSV), and term-level responses that omit restriction ranges. Effort: moderate.

---

## 10. Options for `bdqtest`

The goal is for the source of truth of `bdqtest` to be files in rs.tdwg.org, ideally with rs.tdwg.org delivering RDF for both individual Tests and the whole vocabulary; building the whole-vocabulary RDF in this repository is acceptable.

### 10.1 What has to move

- `bdqtest_term_versions.csv`: its input part becomes an rs.tdwg.org modification CSV for a `bdqtest` term list (`https://rs.tdwg.org/bdqtest/terms/`, database `bdqtest`), with renamed columns (no `:`, `(`, `)`, or spaces), and `iri`, `issued`, and `status` generated by `process.py`.
- The four GUID tables in `tg2/core/` (`TG2_tests_additional_guids.csv`, `information_element_guids.csv`, `TG2_policy_guids.csv`, `TG2_citation_guids.csv`) become auxiliary CSVs in the rs.tdwg.org `bdqtest` directory. They are identifiers that must stay stable, so they belong with the source of truth.
- `build_bdqtest_rdf.py` changes its inputs to these files (and should replace `kurator-ffdq` in `copy_files.sh`).

### 10.2 Option T1: flat term list in rs.tdwg.org; whole-vocabulary RDF built from it

- rs.tdwg.org holds the flat term list plus the auxiliary GUID tables, and `process.py` manages versions and status.
- Single-valued columns map to real predicates in the rs.tdwg.org mapping (e.g. `Type` to `rdf:type`, and Dimension, Criterion, Enhancement, and Resource Type as IRIs, using the same predicates as `build_bdqtest_rdf.py`). Packed columns (information elements, parameters, references, examples, use cases) are mapped as plain literals, or left unmapped.
- rs.tdwg.org serves a flat, partial description for each Test IRI through the generic handler.
- `build_bdqtest_rdf.py` builds the full `bdqtest.ttl`, `.rdf`, and `.jsonld` from the rs.tdwg.org files (in this repository or in rs.tdwg.org `process/`), and they are published on `bdq.tdwg.org` and/or committed to rs.tdwg.org, with a redirect or route for the whole vocabulary.

Assessment: source of truth in rs.tdwg.org with standard versioning, few rs.tdwg.org changes (only renamed columns and a custom mapping). But the per-Test RDF from rs.tdwg.org is not the full graph, so a Test IRI has two different RDF descriptions (the rs.tdwg.org response and the full distribution), in tension with the SDS principle that all representations carry the same data. Effort: moderate.

### 10.3 Option T2: normalized linked-class tables served by the generic serializer

Normalize `bdqtest` into a root table and linked child tables (Section 5). Because of the one-level depth and `urn:uuid` IRIs (Sections 2.3 and 4.3), a response for a Test IRI can contain the Test, its Method, Specification, and information element node IRIs, references, examples, and use-case links, but not the Arguments, the Parameters they are for, `composedOf` members, or Policies.

Assessment: better than T1 per Test, still not the full graph, and the normalized tables are harder to edit by hand than the current single table. Effort: moderate to large. On its own, not recommended.

### 10.4 Option T3: generated per-Test RDF files served by rs.tdwg.org

- Source as in T1 (flat term list and GUID tables in rs.tdwg.org, versioned by `process.py`).
- A BDQ-specific step, run in rs.tdwg.org after `process.py`, runs `build_bdqtest_rdf.py` on the rs.tdwg.org files and writes:
  - the whole vocabulary (`bdqtest.ttl`, `.rdf`, `.jsonld`), and
  - one graph per Test: the Test plus everything reachable from it that has no dereferenceable IRI of its own (Method, Specification, Arguments, information element nodes and their members, references, examples, policy memberships), in three serializations.
- A new route in `restxq.xqm`, `/bdqtest/terms/{id}`, returns the per-Test file for the requested media type (`file:read-text`), with a 303 pattern and extensions matching the generic handler. HTML is redirected via `html/redirects.csv` to the BDQ List of Terms or Quick Reference Guide. Test versions (`/bdqtest/terms/version/{id}`) can use the generic handler (flat) or the same mechanism.

Assessment: full-fidelity RDF for individual Tests and the whole vocabulary, both from rs.tdwg.org, with the source in rs.tdwg.org. Costs: a new route and a new processing step in rs.tdwg.org that the rs.tdwg.org maintainers must accept, about 254 × 3 generated files committed per release, and moving (or pinning a copy of) `build_bdqtest_rdf.py` to rs.tdwg.org. Effort: moderate to large.

### 10.5 Option T4: extend rs.tdwg.org for nested linked classes

Extend the loader and serializer so linked children can have their own linked children (nested `linked-classes.csv`), letting the generic handler emit the full per-Test graph from normalized tables.

Assessment: the most general solution, potentially useful for other graph-rich standards, but a significant change to rs.tdwg.org's core serializer, and it still leaves the derivations in Section 5.2 (policies, MultiRecord nodes) to be precomputed into tables. Effort: large. Not recommended for the public review timeline.

### 10.6 Recommendation for `bdqtest`

Use T1 for the public review, which moves the source of truth to rs.tdwg.org with standard versioning, and build the whole vocabulary from the rs.tdwg.org files. Adopt T3 as the target for full-fidelity per-Test RDF from rs.tdwg.org, discussing the new route with the rs.tdwg.org maintainers early.

### 10.7 Generated CSV lists and documents

This repository generates flat lists and documents from `bdqtest_term_versions.csv`, including:

- `tg2/_review/dist/bdqtest_singlerecord_tests_current.csv`, `bdqtest_multirecord_tests_current.csv` (`draft_build_bdqtest_singlerecord_tests_current.py`)
- `tg2/_review/dist/bdqtest_tests_vertical.csv` (`make_bdq_tests_vertical.py`)
- the Quick Reference Guide and filtering (`draft_build_bdqtest_qrg.py`, `generate_bdq_qrg_filtering.py`)
- the `bdqtest` List of Terms (`draft_build-termlist_bdqtest.py`) and other documents (`draft_build-docs.py`)

With T1 or T3, these can read the rs.tdwg.org current terms file (`bdqtest/bdqtest.csv`), which stays flat; column renames need a mapping back to the published column names so that implementers using the `dist` CSVs are not affected. If the source becomes non-flat (T2 or T4), these lists should be generated by SPARQL queries over the `bdqtest` RDF instead; the existing SPARQL template validation in `do_build.sh` is a starting point.

---

## 11. Concrete change list per file in rs.tdwg.org

### 11.1 Created by `process.py` for each new BDQ term list

For each of `bdqdim`, `bdqenh`, `bdqcrit`, `bdquc`, `bdqval`, and (Option C) `bdqffdq`, and (T1/T3) `bdqtest`: the `<db>/` and `<db>-versions/` directories with core CSV, `constants.csv`, `namespace.csv`, `-column-mappings.csv`, `-classes.csv`, `-replacements*.csv`, and `linked-classes.csv`; rows in `index/index-datasets.csv`, `term-lists/term-lists.csv` (and versions/members tables), `vocabularies/`, `vocabularies-versions/`, `standards/`, `standards-versions/`, and `html/redirects.csv` (`process/process.py:76-189`, `490-545`, `632-673`, `738-1215`).

### 11.2 Hand-edited inputs

- `process/bdq-revisions/bdq-revisions-YYYY-MM-DD/`: modification CSVs, `config.yaml`, and `vocab.yaml` per vocabulary (Section 8.2).
- Custom column mapping edits for extra columns (Sections 8.3, 9.3, 10.2).
- `process/document_metadata_processing/<doc-dir>/document_configuration.yaml` and `authors_configuration.yaml` per BDQ document.
- Option C: `bdqffdq/bdqffdq-axioms.ttl`. T1/T3: the `bdqtest` auxiliary GUID tables.

### 11.3 `process/process.py`

Patch lines `747` and `750` to take the scheme from the term list IRI (Section 7.2). No other change is needed for the simple vocabularies. T3 adds a separate BDQ-specific processing step rather than changing `process.py`.

### 11.4 `html/restxq.xqm`

- Fall back to an `https` lookup in the document, vocabulary, and term list handlers (Section 7.2).
- Option A or C: a route for the whole `bdqffdq` ontology (redirect, or file serving as in Option B1).
- T3: a route `/bdqtest/terms/{id}` serving generated per-Test files.

### 11.5 `index/dereferencing-test.py`

Accept `https://rs.tdwg.org/` URLs (`94`), and add BDQ examples: a term from each simple vocabulary, a `bdqffdq` term and the ontology, a `bdqtest` Test, and the BDQ documents.

### 11.6 Documentation in rs.tdwg.org

`process/process-vocabulary.md` and `README.md` should record that BDQ uses `https` IRIs, and describe any BDQ-specific steps (the `bdqffdq` merge, the `bdqtest` generation step).

### 11.7 No change needed

`index/load-db-from-github.py` and `docker/initialize-database.sh` need no change, provided BDQ CSV headers are valid XML names and datasets follow the standard layout.

---

## 12. Changes needed in `tdwg/bdq`

- Retire the five simple `*_term_versions.csv` files and, when moved, `bdqtest_term_versions.csv`, the `tg2/core/` GUID tables, and `bdqffdq.owl`; update `tg2/_review/vocabulary/README.md` to say they are frozen and that the source is rs.tdwg.org (the README already anticipates this).
- Point the build scripts at rs.tdwg.org. `tg2/_build_review/draft_build-termlist.py` reads `../_review/vocabulary/{term}_term_versions.csv` (`217`) and already has the rs.tdwg.org pattern commented out (`53`: `githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + github_branch + '/'`). Other readers of `bdqtest_term_versions.csv` include `build_bdqtest_rdf.py`, `draft_build_bdqtest_qrg.py`, `draft_build_bdqtest_singlerecord_tests_current.py`, `draft_build-docs.py`, `draft_build-termlist_bdqtest.py`, `generate_bdq_qrg_filtering.py`, `make_bdq_tests_vertical.py`, `postprocess_autolink_terms.py`, and `tools/find_current_tests_in_csv_missing_from_rdf.py`.
- Retire `tg2/_build_review/temp_term-lists.csv` and `temp_namespaces.yaml`.
- Replace `kurator-ffdq` in `tg2/_make_review/copy_files.sh:52-61` with `build_bdqtest_rdf.py`.
- Generate real RDF/XML and JSON-LD for `bdqffdq` if it is served from `bdq.tdwg.org`.
- Update List of Terms document metadata to TDWG document IRIs (Section 8.1) and cite rs.tdwg.org version IRIs (Section 8.5).
- Change the remaining `http://rs.tdwg.org/bdq…` IRIs to `https` (Section 7.2).
- Replace standard IRI placeholders once a number is assigned.

---

## 13. Recommended implementation approach

1. **Agree on `https`** with the rs.tdwg.org maintainers and the TDWG Technical Architecture Group, and patch `process.py`, `restxq.xqm`, and `dereferencing-test.py` on the `bdq` branch.
2. **Deploy the five simple vocabularies** through `process.py` (Section 8), using a source branch and `bdq` as the derived, deployed branch, and verify them on `bdq-public-review.rs.tdwg.org`.
3. **Deploy `bdqffdq` as a hybrid** (Option C): term list via `process.py`, axioms file, merge step, and a route or redirect for the whole ontology.
4. **Deploy `bdqtest` as a flat term list** with its GUID tables (T1), build the whole vocabulary from the rs.tdwg.org files, and plan T3 for full per-Test RDF.
5. **Switch the BDQ build** to read from rs.tdwg.org, and freeze the files in `tg2/_review/vocabulary/`.
6. After ratification, the rs.tdwg.org maintainers merge the source branch to `master`, rerun processing with the ratification date, and make a release.

---

## 14. Open questions for maintainers

1. Will the rs.tdwg.org maintainers and the TDWG Technical Architecture Group accept `https` as the canonical protocol for BDQ, and the corresponding patches to `process.py` and `restxq.xqm`?
2. Will the rs.tdwg.org maintainers accept routes that serve files directly (Options B1, C for the whole ontology, T3), a pattern rs.tdwg.org has not used before?
3. For `bdqffdq`, should the ontology IRI `https://rs.tdwg.org/bdqffdq/terms` and the term list IRI `https://rs.tdwg.org/bdqffdq/terms/` denote the same resource, or should one change?
4. What standard number will BDQ be assigned, and what are the final (non-`/draft/`) URLs for the BDQ documents on `bdq.tdwg.org`, to be used in `prepend_url` and in any redirect targets?
5. Should rs.tdwg.org CI adopt BDQ-specific semantic validation (SHACL/SPARQL checks), or should that remain in this repository, reading from rs.tdwg.org?

---

## 15. Final conclusion

rs.tdwg.org can be the source of truth for all BDQ vocabularies, with differing degrees of fit:

- The five simple vocabularies fit the standard `process.py` pipeline once small `https` patches are made and some data problems are fixed.
- `bdqffdq` fits as a hybrid: an ordinary term list for the per-term metadata, which is almost all of the ontology, plus a small axioms file for the restriction ranges and disjointness axioms, merged to produce the complete ontology.
- `bdqtest` can be versioned as a flat term list with its GUID tables in rs.tdwg.org, but full-fidelity per-Test RDF from rs.tdwg.org needs either generated per-Test files served by a new route (recommended target) or an extension of the serializer.

In every case, the term-version files become outputs of rs.tdwg.org processing, and the BDQ build in this repository becomes a consumer of rs.tdwg.org data.
