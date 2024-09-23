<!--- This file is generated from templates by code, DO NOT EDIT by hand --->
<!--- Template for header, values provided from yaml configuration --->
# Biodiversity Data Quality List of Vocabularies.

Title
: Biodiversity Data Quality List of Vocabularies.

Date version issued
: 2024-09-10

Date created
: 2024-09-10

Part of TDWG Standard
: <http://example.org/to_be_determined>

Abstract
: This document is a reference for the (Draft) BDQ Core Standard, listing the vocabularies included in the BDQ Core Standard.

Contributors
: [Lee Belbin](https://orcid.org/0000-0001-8900-6203) ([Blatant Fabrications](https://www.wikidata.org/wiki/Q130304884)), [Arthur Chapman](https://orcid.org/0000-0003-1700-6962) ([Australian Biodiversity Information Services](http://www.wikidata.org/entity/Q100600913)), [Paul J. Morris](https://orcid.org/0000-0002-3673-444X) ([Museum of Comparative Zoology, Harvard University](http://www.wikidata.org/entity/Q1420782)), [John Wieczorek](https://orcid.org/0000-0003-1144-0290) ([VertNet](http://www.wikidata.org/entity/Q98382028)), [Yi-Ming Gan](https://orcid.org/0000-0001-7087-2646) ([Royal Belgian Institute of Natural Sciences](http://www.wikidata.org/entity/Q16665660)), [Antonio Mauro Saraiva](https://orcid.org/0000-0003-2283-1123) ([University of São Paulo, Research Center on Biodiversity and Computing](https://www.wikidata.org/wiki/Q835960)), [Alan Koch Veiga](http://orcid.org/0000-0003-2672-8115) , [Paula F Zermoglio](https://orcid.org/0000-0002-6056-5084) ([Instituto de Investigaciones en Recursos Naturales, Agroecología y Desarrollo Rural (IRNAD, CONICET-UNRN): San Carlos de Bariloche](https://www.irnad.com/)), [Alexander Thompson](https://orcid.org/0000-0002-8981-4048) ([Google](https://www.wikidata.org/wiki/Q95)), David Lowery 

Creator
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions

Bibliographic citation
: TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Biodiversity Data Quality List of Vocabularies.. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2024-09-10>

Draft Standard for Submission
# BDQ Core Vocabularies

This page provides an introduction and index to the six vocabularies introduced by this standard. The vocabularies are distinguished by their roles within applications of the standard to biodiversity data quality (BDQ) use cases. Each vocabulary has its own namespace and term list document. 

## Vocabularies central to BDQ Core

- [BDQ Core Tests and Assertions List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqcore_list/index.md) - this vocabulary is likely to be the focus of interest for both implementors and consumers of the outputs of implementations of tests and assertions.  This vocabulary uses the namespace abbreviation `bdqcore:` for the namespace `https://rs.tdwg.org/bdqcore`. The specifications defined in `bdqcore:` make use of terms from the other three vocabularies defined by the standard and listed below.
- [Fitness For Use Framework Ontology](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/bdqffdq/index.md) - this vocabulary, in the form of an ontology, provides the semantics of terms that describe data quality and fitness for use in the namespace `https://rs.tdwg.org/bdqffdq` (abbreviated `bdqffdq:`), these are the terms used to describe the tests in bdqcore:.

## Vocabularies supporting to BDQ Core

- [Test Specification Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdq/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdq` (abbreviated `bdq:`), which are to be used within the specifications of the tests covered by `bdqcore:`.  Provides values for bdqffdq:Parameter and bdqffdq:UseCase. 
- [Data Quality Dimension Controlled Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqdim/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqdim` (abbreviated `bdqdim:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:DataQualityDimension`. 
- [Data Quality Criteria Controlled Vocabulary List of Terms](https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqcrit/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqcrit` (abbreviated `bdqcrit:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Criterion`. 
- [Data Quality Enhancement Controlled Vocabulary List of Terms](../docs/list/bdqenh/index.md) - this vocabulary provides definitions of terms within the namespace `https://rs.tdwg.org/bdqenh` (abbreviated `bdqenh:`), which provides names and the preferred labels of values recommended for populating the specific term `bdqffdq:Enhancement`. 

## Cite BDQ Core

**To cite BDQ Core in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite the standard document upon which this page is built, use
the following:**

BDQ Core Maintenance Group 2024. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/bdq/doc/list/

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2024. Biodiversity Data Quality List of Vocabularies.. Biodiversity Information Standards (TDWG). <https://bdq.tdwg/org/vocabularies/2024-09-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)


