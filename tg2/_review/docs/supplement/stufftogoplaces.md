Material from the initial draft of the BDQ Core standard to be moved elsewhere.

Much of this goes in supplementary information or the guides.

Delete from here once moved elsewhere.



#### 3.4 Types of Test

The concept of 'tests' in this standard include Validation, Issue, Amendment and Measure. Responses from each of the tests MUST be structured data, and MUST NOT be simple pass fail flags. The Response from a test is an assertion which can form part of a data quality report or be wrapped in an annotation, and MUST include the following three components: 

1. Value is the returned result for the test, i.e. numeric for measures, a controlled vocabulary consisting of exactly COMPLIANT or NOT_COMPLIANT for Validations, NOT_ISSUE, POTENTIAL_ISSUE or ISSUE for Issues, either a numeric value or a controlled vocabulary consisting of COMPLETE or NOT_COMPLETE for Measures, and a data structure (e.g., a list of key value pairs) for proposed changes for Amendments.

2. Status provides a controlled vocabulary, metadata concerning the success, failure, or problems with the test. The Status also serves as a link to information about warning type values and where in the future, probabilistic assertions about the likeliness of the value could be made. 

3. The Remark supplies human-readable text describing reasons for the test result output.

Validation tests are phrased as positive statements, consistent with the Framework.  Validations evaluate values or in some cases, presence or lack of a value to see if input data have quality for some purpose. For example, VALIDATION_TAXONRANK_NOTEMPTY will return Response.status RUN_HAS_RESULT and Response.result COMPLIANT if a record under test contains a value in dwc:taxonRank, rather being phrased in the negative (i.e. VALIDATION_TAXONRANK_EMPTY) and flagging a problem.  Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT. The formal response of VALIDATIONs can take one of four forms. A Response.status of "EXTERNAL_PRREQUISITES_NOT_MET" when an external authority service is unavailable (bdq:sourceAuthority), a Response.status of "INTERNAL_PREREQUISITES_NOT_MET" when the values of the Information Elements are such that the test cannot be meaningfully run, a Response.status of "RUN_HAS_RESULT" when the prerequisites for running the test have been met, and in this situation, a Response.result of either "COMPLIANT" if the values of the Information Elements meet the criteria, or "NOT_COMPLIANT" when they do not. 

Issues are a form of warning flag where the test is drawing attention to potential problem with the value of a Darwin Core term for at least one use case. Issues are currently outside the Data Quality Fitness for Use Framework. Issues result in a Response.status of "RUN_HAS_RESULT" and a Response.status of "POTENTIAL_ISSUE" or "NOT_ISSUE". Human evaluation of potential issues require a human review. For example, ISSUE_DATAGENERALIZATIONS_NOTEMPTY will return a Response.result of POSSIBLE_ISSUE if dwc:dataGeneralizations contains a value, as the actual value in dwc:dataGeneralizations and the assertions it makes about what changes have been made to generalize other Darwin Core terms will require human review in the context of a particular use of the data to determine whether the data are fit for purpose or not.  

An Amendment may propose a change to an exisitng Darwin Core value or fill in a missing value. Amendments  is intended to improve one or more components of the quality of the record.  The Response.result from an Amendment MUST always be treated as a proposal for a change, and MUST NOT be blindly applied to a database or record when a data quality report is used for Quality Control of an existing record.  Consumers of Data Quality Reports under Quality Assurance uses MAY choose to accept all proposed amendments as part of a pipeline in preparing data for an analysis.  The Framework also supports changes to procedures but we have not framed any such tests in this form.  

A Measure returns a numeric value or INTERNAL_PREREQUISITES_NOT_MET. Most Measures count the number of Validation or Amendment tests that a specifified Response.Result. MEASURE_EVENTDATE_DURATIONINSECONDS returns a Response.result measuring the amount of time represented by the value in dwc:eventDate, and can be used in QualityAssurance under specific research data quality needs to identify Occurrences where the date observed or collected is known well enough for particular analytical needs (e.g. to at least one day for phenology studies, to at least one year for other purposes) that generally summarises the results of running the Validations and Amendments and in one case provides an indication of the length of the period of the value of dwc:eventDate. 

[From QRG]

[!--- we should remove the SingleRecord counting Measures, they don't fit particularly well into the framework, and we don't have either validation data or frameworks for evaluating correct implementation of them.  ---]

A MEASURE applies to a single record (bdqffdq:SingleRecord), but like all other tests, could be accumulated across multiple records (bdqffdq:MultiRecords). MEASUREs within the standard are MEASURE_VALIDATIONTESTS_COMPLIANT, MEASURE_VALIDATIONTESTS_NOTCOMPLIANT, MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET, MEASURE_AMENDMENTS_PROPOSED and MEASURE_EVENTDATE_DURATIONINSECONDS.   

For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not. Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes. Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.

Data are found to be fit for some use if all Validations comprising that Use have a Response.result of COMPLIANT, and all (non-numeric) Measures comprising that Use have a Response.result of COMPLETE. The vast majority of the Core tests are Validations, phrased in the positive sense, intended as a core suite, to identify biodiversity data that are fit for the Core purposes, as identified in the user scenario analyses performed by BDQ Task Group 3.   

[End QRG addition]

All tests could be accumulated across multiple records (bdqffdq:MultiRecords). For each bdqffdq:SingleRecord Validation, there is a bdqffdq:MultiRecord Measure that returns COMPLETE when all records in the bdqffdq:MultiRecord have a Response.result of COMPLIANT, and NOT_COMPLETE when they are not.  Under QualityAssurance, these measures serve as the key criterion for identifying data which have quality for Core purposes.  Under QualityAssurance, a bdqffdq:MultiRecord is filtered to remove records that do not fit the bdqffdq:MultiRecord Measures for completeness, such that a filtered bdqffdq:MultiRecord has Response.result values of COMPLETE for all bdqffdq:MultiRecord Measures.    


#### Pairing

Tests are paired in that all AMENDMENTs require a corresponding VALIDATION that assesses some aspect of data quality. An AMENDMENT may be able to improve the quality of data with respect to that VALIDATION. 

Each test is designed to stand in isolation. This is by design to both support the mixing and matching of these and other tests to meet particular data quality needs, and so as not impose any particular model of test execution on implementation frameworks. Implementations of test execution frameworks may execute tests in on data records in parallel, on data records in sequence, as queries on data sets, on unique values. 

<!--- Ming: Use of MultiRecord measures to measure improvement in QA and QC, repeated in 5.2.3 --->
The framework expects that Quality Assurance is provided for through specification of a set of Measures defined to operate on a MultiRecord, and which specify a Response.result of COMPLETE or NOT_COMPLETE.  A MultiRecord Measure may specify that it is COMPLETE if all instances of a SingleRecord Validation are COMPLIANT.  

For Quality Control, MultiRecord Measures may be defined to return a count of Response.value of COMPLIANT for validations, and thus can provide a measure of how fit a data set is for some purpose, and what sort of work would be required to make it fit for that purpose.   

[End of QRG Text entry]



## 7. Implications for the Darwin Core Standard (John)

Early recognition that estimating 'fitness for use'/'quality was made difficult because of the lack of vocabularies...TG4.

Definitions, uses in the wild, and best practices for Taxon class ..ID terms.

[ Mention of issues arising such as use of dwc:country and dwc:countryCode and "High Seas"]

How to identify the High Seas.

## 9. Acronyms

| **Acronym** | **Explanation**                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------|
| ALA         | Atlas of Living Australia                                                                                      | 
| BDQ         | TDWG Biodiversity Data Quality Interest Group                                                                  |
| BISON       | Biodiversity Information Serving Our Nation                                                                    |
| CRIA        | Centro de Referência em Informação Ambiental                                                                   |
| EPSG        | European Petroleum Survey Group                                                                                |
| GBIF        | Global Biodiversity Information Facility                                                                       |
| iDigBio     | Integrated Digitized BioCollections                                                                            |
| IRI         | Internationalized Resource Identifier                                                                          |
| ISO         | International Standards Organization                                                                           |
| TDWG        | Biodiversity Information Standards                                                                             |
| TG1         | Biodiversity Data Quality Interest Group Task Group 1: Framework on Data Quality                               |
| TG2         | Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions                       |
| TG3         | Biodiversity Data Quality Interest Group Task Group 3: Data Quality Use Cases                                  |
| TG4         | Biodiversity Data Quality Interest Group Task Group 4: Best Practices for Development of Vocabularies of Value |


## 10. References

* Belbin L, Daly J, Hirsch T, Hobern D, Salle JL (2013) A specialist’s audit of aggregated occurrence records: An ‘aggregator’s’ perspective. ZooKeys 305: 67–76. doi: 10.3897/zookeys.305.5438
* Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889
* Rees ER, Nicholls M (2020). Suppl. material 2: Data Quality Use Case Study Result. https://biss.pensoft.net/article/download/suppl/5255738/.
* [RFC-2119] http://tools.ietf.org/html/rfc2119 Key words for use in RFCs to Indicate Requirement Levels. 1997. The Internet Engineering Task Force.
Sanderson et al. (2107) see Section 1.5
* Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12(6): e0178731. https://doi.org/10.1371/journal.pone.0178731
* Wieczorek J, Bloom D, Guralnick R, Blum S, Döring M, Giovanni R, Robertson T, Vieglais D (2012) Darwin Core: An Evolving Community-Developed Biodiversity Data Standard. PLoS ONE 7(1): e29715. https://doi.org/10.1371/journal.pone.0029715


---

## User guide



