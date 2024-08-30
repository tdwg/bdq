**NOTE** This is just a placeholder for the Data Quality Dimension Controlled Vocabulary term list document, which will be generated by code.

# Data Quality Dimension Controlled Vocabulary List of Terms

**Title**: Data Quality Criterion Controlled Vocabulary List of Terms

**Namespace URI**: <http://rs.tdwg.org/bdqcrit/values/>

**Preferred namespace abbreviation**: bdqcrit:

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: <http://www.tdwg.org/standards/[*******]>

**This document version**: <{current_iri}{ratification_date}>

**Latest version of document**: <http://rs.tdwg.org/bdq/doc/crit/>

{previous_version_slot}

**Abstract**: The BDQ Core term `Criterion`, describes in general terms, how a bdqffdq:Validation or bdqffdq:Issue assess whether data conform to expectations or requirements. For example, "precision" in "coordinate precision of single records". Includes Completeness, Conformance, Consistency, Likeliness, Reliability, and Resolution. 

**Contributors**: Lee Belbin, Paul J. Morris, Arthur Chapman, John Wieczorek, Alan Koch Veiga, Paula F Zermoglio, Alex Thompson, Anytonio M Saraiva, Yi Ming Gan

**Creator**: TDWG Biodiversity Data Quality Interest Group: Task Group 1 (Framework on Data Quality) and Task Group 2 (Data Quality Tests and Assertions)

**Bibliographic citation**: TDWG Biodiversity Data Quality Interest Group. 2024. BDQ Criteria Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <{current_iri}{ratification_date}>


## 1 Introduction
This document includes terms intended to be used as a controlled value for BDQ Core tests with local name `Criterion`.  For details and rationale, see Veiga AK, Saraiva AM, Chapman AD, Morris PJ, Gendreau C, Schigel D, & Robertson TJ (2017). A conceptual framework for quality assessment and management of biodiversity data. PLOS ONE 12 (6): https://doi.org/10.1371/journal.pone.0178731>

### 1.1 Data Quality Criteria

The scope of the standard is the fundamental information about core tests of type bdqffdq:Validation or bdqffdq:Issue. The Criterion describes, in abstract terms how data can be evaluated for fittness.  A criterion expresses in general terms what a bdqffdq:Specification expresses in specific terms.   Criteria have an informal relationship to bdqffdq:Dimensions, expressed here in the comments, these relationships could be formalized, but we have not done so.  

### 1.2 Data Quality Criteria Vocabulary

<!-- Generated table of terms goes here --->

| term_localName | definition | comments |
| --------------------- | ----------- | ------------- |
| Complete | Data are present and sufficiently comprehensive for use. | Data in a bdqffdq:InformationElement are present and sufficiently comprehensive for use.  Corresponding dimension is bdqdim:Completeness |
| Consistent | A data are internally consistent and consistent with any authorities consulted.  | A set of bdqffdq:InformationElements and bdq:sourceAuthorities are consistent.   Corresponding dimension is bdqdim:Consistency |
| Found | Data conform to the values in an authority. | Data in a bdqffdq:InformationElement conform to a bdq:sourceAuthority.  Corresponding dimension is bdqdim:Conformance |
| InRange | Data conform to an expected range of values. | Data in a bdqffdq:InformationElement conform to an expected range of values.  Corresponding dimension is bdqdim:Conformance |
| Likely | Data are likely to be true or expected values. | Data in a bdqffdq:InformationElement is likely to be true or expected values.  Corresponding dimension is bdqdim:Likelyness |
| NotEmpty | Some data value is present. | Some value is present in a bdqffdq:InformationElement.  Corresponding dimension is bdqdim:Completeness.   See also bdq:EMPTY and bdq:NOT_EMPTY |
| Standard | Data conform to a format, syntax, data type, or standard. | Data in a bdqffdq:InformationElement conform to a format, syntax, data type, or standard.  Corresponding dimension is bdqdim:Conformance |
| Unambiguous | Data adequately identify a unique entity. | Data in a bdqffdq:InformationElement adequately identifies a unique entity.  Corresponding dimension is bdqdim:Conformance |

<!-- End generated table of terms --->

## 1.3 Use of Terms

Due to the requirements of [bdqffdq](https://rs.tdwg.org/bdqffdq/terms), controlled values from this vocabulary are REQUIRED values of `bdqffdq:Criterion`.

### 2 Status of the content of this document

In Section 1.2 the values of the `Term IRI`, `Definition` and `Controlled value` are normative. The values of `Term Name`, 'Comments' and `skos:prefLabel` are non-normative. 

### 2.1 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).
