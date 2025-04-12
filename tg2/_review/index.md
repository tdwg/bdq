<!--- layout: home --->
# Biodiversity Data Quality Core
<!--- {:.lead} --->

**IRI of the Biodiversity Data Quality Core standard**<br>
<a href="https://www.tdwg.org/standards/bdq">https://www.tdwg.org/standards/bdq</a> This is the IRI that should be cited and to which hyperlinks should be made. 

**Publisher**<br>
<a href="https://www.tdwg.org/">Biodiversity Information Standards (TDWG)</a>

**Status**
Draft Standard

**Abstract**
Biodiversity Data Quality (BDQ) Core is a TDWG standard maintained by the [Biodiversity Data Quality Core Maintenance Interest Group](https://www.tdwg.org/standards/bdq/#maintenance-group">). BDQ Core is based on a Data Quality Fitness for Use Framework (Veiga 2016, Veiga et al. 2017), which provides a vocabulary for how to describe and evaluate data quality. BDQ Core consists of a suite of tests and related vocabularies (see Chapman et al. 2020) that evaluate the 'quality' or 'fitness for use' of biodiversity data described using the [Darwin Core standard](https://dwc.tdwg.org/).

**Preferred Citation**
Biodiversity Data Quality Core Maintenance Group. 2024. Biodiversity Data Quality Core. https://www.tdwg.org/standards/bdq

## Parts of the Standard

### I. Entry-Level Overview & Practical Orientation
[Biodiversity Data Quality Core Introduction](docs/intro/index.md)<br>
[BDQ Core Quick Reference Guide](docs/terms/bdqcore/index.md)<br>
[BDQ Core User's Guide](docs/guide/users/index.md)<br>

### II. Implementation & Application
[BDQ Core Implementer's Guide](docs/guide/implementers/index.md)<br>
[BDQ Core Tests and Assertions](docs/bdqcore/index.md)<br>
[BDQ Core: Identifying Synthetic and Modified Data](docs/synthetic/index.md)
- File: [Test Validation Data](docs/guide/implementers/TG2_test_validation_data.csv)
- File: [Test Validation Data for non-printing characters](docs/guide/implementers/TG2_test_validation_data_nonprintingchars.csv)
  
### III. Vocabularies and Controlled Terms
[BDQ Core List of Vocabularies](docs/vocabularies/index.md)<br>
[BDQ Core Tests and Assertions List of Terms](docs/list/bdqcore/index.md)
- File: [CSV List of Single Record Tests](dist/bdqcore_singlerecord_tests_current.csv)
- File: [CSV List of Multi Record Tests](dist/bdqcore_multirecord_tests_current.csv)
- File: [CSV List of all Tests](vocabulary/bdqcore_term_versions.csv)
- File: [Tests in RDF/XML](dist/bdqcore.xml)
- File: [Tests in Turtle](dist/bdqcore.ttl)
- File: [Tests in JSON-LD](dist/bdqcore.json)<br>

[Biodiversity Data Quality Controlled Vocabulary List of Terms](docs/list/bdq/index.md)
- File [bdq: RDF](dist/bdq.xml "RDF/XML serialization of the bdq terms.")<br>

[Data Quality Criterion Controlled Vocabulary List of Terms](docs/list/bdqcrit/index.md)
- File [bdqcrit: RDF](dist/bdqcrit.xml "RDF/XML serialization of the bdqcrit terms.")<br>

[Data Quality Dimension Controlled Vocabulary List of Terms](docs/list/bdqdim/index.md)
- File [bdqdim: RDF](dist/bdqdim.xml "RDF/XML serialization of the bdqdim terms.")<br>

[Data Quality Enhancement Controlled Vocabulary List of Terms](docs/list/bdqenh/index.md)
- File [bdqenh: RDF](dist/bdqenh.xml "RDF/XML serialization of the bdqcrit terms.")

### IV. Conceptual Foundation (Advanced Users & Information Architects)
[Fitness For Use Framework Ontology Guide](docs/guide/bdqffdq/index.md)<br>
[Fitness For Use Ontology](docs/bdqffdq/index.md)<br>
[Fitness For Use Framework Ontology List of Terms](docs/list/bdqffdq/index.md)
- File [bdqffdq: Owl](vocabulary/bdqffdq.owl "OWL ontology for the bdqffdq framework.")<br>

[Fitness For Use Framework Ontology Vocabulary Extension](docs/extension/bdqffdq/index.md)

### V. Supporting and Informative Material
[BDQ Core Supplemental Information](docs/supplement/index.md)<br>
[BDQ Core Bibliography](docs/references/index.md)<br>
[BDQ Core Maintenance Guide](docs/maintenance/index.md)<br>
[BDQ Core Maintenance GitHub repository](https://github.com/tdwg/bdq)
