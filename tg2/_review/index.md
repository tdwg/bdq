---
layout: home
---

# BDQ Core

{:.lead}
IRI of the BDQ Core standard
: <a href="https://www.tdwg.org/standards/ToBeDetermined">https://www.tdwg.org/standards/ToBeDetermined</a> This is the IRI that should be cited and to which hyperlinks should be made. 

Publisher
: <a href="https://www.tdwg.org/">Biodiversity Information Standards (TDWG)</a>

Status
: Draft Standard

Abstract
: BDQ Core is a **Draft** TDWG standard maintained by the [BDQ Core Maintenance Interest Group](https://www.tdwg.org/standards/bdq/#maintenance-group">). BDQ Core is based on a Data Quality Fitness for Use Framework (Veiga et al. 2017) which provides a vocabulary for how to describe and evaluate data quality. BDQ Core is a suite of tests and related vocabularies (see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889) that evaluate the 'quality' or 'fitness for use' of biodiversity data that is described using the [Darwin Core standard](https://dwc.tdwg.org/).

Preferred Citation
: BDQ Core Maintenance Group. 2024. Biodiversity Data Quality Core. https://www.tdwg.org/standards/ToBeDetermined

## Parts of the Standard

- [BDQ Core Introduction](docs/intro/index.md)
- [BDQ Core Quick Reference Guide](docs/terms/bdqcore/index.md)
- [BDQ Core Fitness For Use Framework Ontology Guide](docs/guide/bdqffdq/index.md)
- [BDQ Core User's Guide](docs/guide/users/index.md)
- [BDQ Core Vocabularies](docs/vocabularies/index.md)
  - [BDQ Core Tests and Assertions Landing Page](docs/bdqcore/index.md):
    - [BDQ Core Tests and Assertions List of Terms](docs/list/bdqcore/index.md):
      - File: [CSV List of Tests](vocabulary/bdqcore_terms.csv "Convenience CSV list of test descriptors.")
      - File: [Tests in RDF/XML](dist/bdqcore.xml "RDF/XML serialization of OWL representation of the tests descriptors.")
      - File: [Tests in Turtle](dist/bdqcore.ttl "Turtle serialization of OWL representation of the tests descriptors.")
  - [Fitness For Use Ontology Landing Page](docs/bdqffdq/index.md):
    - [Fitness For Use Framework Ontology List of Terms](docs/list/bdqffdq/index.md):
    - [Fitness For Use Framework Ontology Extension List](docs/extension/bdqffdq/index.md):
    - File [bdqffdq: Owl](vocabulary/bdqffdq.owl "Owl ontology for the bdqffdq framework.")
  - [Biodiversity Data Quality Controlled Vocabulary List of Terms](docs/list/bdq/index.md)
  - [Data Quality Dimension Controlled Vocabulary List of Terms](docs/list/bdqdim/index.md)
  - [Data Quality Criterion Controlled Vocabulary List of Terms](docs/list/bdqcrit/index.md)
  - [Data Quality Enhancement Controlled Vocabulary List of Terms](docs/list/bdqenh/index.md)
- [BDQ Core Implementer's Guide](docs/guide/implementers/index.md)
  - File: [Test Validation Data](docs/guide/implementers/TG2_test_validation_data.csv)
  - File: [Test Validation Data for non-printing characters](docs/guide/implementers/TG2_test_validation_data_nonprintingchars.csv)
- [Identifying Synthetic and Example Data](docs/synthetic/index.md)
- [BDQ Core Supplemental Information](docs/supplement/index.md)
- [References](docs/references/index.md)

## Appendix

- [BDQ Core Maintenance Guide (draft)](docs/maintenance/index.md)
- [GitHub repository](https://github.com/tdwg/bdq): where BDQ Core is maintained
