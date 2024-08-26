---
layout: home
---

# BDQ Core Vocabularies

{:.lead}
This page provides an introduction and index to the four vocabularies introduced by this standard. The vocabularies are distinguished by their roles within applications of the standard to biodiversity data quality (BDQ) use cases. Each vocabulary has its own namespace and term list document. 

- [BDQ Core Tests and Assertions List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/index.md) - this vocabulary is likely to be the focus of interest for both implementors and consumers of the outputs of implementations of tests and assertions. This vocabulary uses the namespace abbreviation `bdqcore:` for the namespace `https://rs.tdwg.org/bdqcore`. The specifications defined in `bdqcore:` make use of terms from the other three vocabularies defined by the standard and listed below.
- [Fitness For Use Framework Ontology](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqffdq/index.md) - this vocabulary, in the form of an ontology, provides the semantics of terms that describe data quality and fitness for use in the namespace `https://rs.tdwg.org/bdqffdq` (abbreviated `bdqffdq:`).
- [Test Specification Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdq/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdq` (abbreviated `bdq:`), which are to be used within the specifications of the tests covered by `bdqcore:` 
- [Data Quality Dimension Controlled Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqdim/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqdim` (abbreviated `bdqdim:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:DataQualityDimension`. The Data Quality Dimension term distinguishes whether a test or assertion should be categorized as `Completeness`, `Conformance`, `Consistency`, `Likeliness`, `Reliability`, or `Resolution`.
