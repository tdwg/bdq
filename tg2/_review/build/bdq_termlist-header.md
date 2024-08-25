# Test Specification Vocabulary List of Terms

**Title**: Test Specification Vocabulary List of Terms

**Date version issued**: {ratification_date}

**Date created**: {created_date}

**Part of TDWG Standard**: <{standard_iri}>

**This version**: <{current_iri}{ratification_date}>

**Latest version**: <{current_iri}>

{previous_version_slot}

**Abstract**: The BDQ Core list of terms used in the data quality tests using the `bdq:` namespace.

**Contributors**: Lee Belbin, Paul Morris, Arthur Chapman, John Wieczorek, Alan Koch Veiga, Paula F Zermoglio, Alex Thompson, Yi Ming Gan

**Creator**: TDWG Biodiversity Data Quality Interest Group: Task Group 2 (Data Quality Tests and Assertions)

**Bibliographic citation**
: TDWG Biodiversity Data Quality Interest Group. 2024. BDQ Dimensions Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <{current_iri}{ratification_date}>


## 1 Introduction (non-normitive)
[!--- JRW finished first draft to here ---]
This document includes terms that are part of the BDQ vocabulary (<http://rs.tdwg.org/version/bdq/{ratification_date}>). For details and rationale, see Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C, Benson A, Schigel D (2020). Developing Standards for Improved Data Quality and for Selecting Fit for Use Biodiversity Data. Biodiversity Information Science and Standards 4: e50889. https://doi.org/10.3897/biss.4.50889.

#### Definition of EMPTY

We need a reusable definition for EMPTY that can apply in any test where the concept is relevant. Here we define EMPTY as an information element that is either not present or does not contain any characters or values other than those in the range U+0000 to U+0020. 

An information element containing invalid characters (e.g. letters in an information element that would be expected to contain integers) or values (including string serializations of the NULL value) are NOTEMPTY and may be separately detected. The phrase "not present" is there to cover cases where a test implementation cannot tell if a particular data set under test includes a particular Darwin Core term. This allows the test implementations to be independent of, and agnostic about frameworks within which the tests are run, the nature of the data. For csv data, a column is either there or not in a data set, but in an rdf representation, some data objects could have relevant properties and others not - and the tests are independent of that. We considered, and explicitly rejected, treating common string serializations of null such as \N and NULL as empty values. If "\N" is present in a data set, the tests will explicitly treat that value as NOTEMPTY, and then try to evaluate it against whatever other criteria apply. 

This definition is not applicable to a discussion of what value to include in a controlled vocabulary to indicate that no meaningful value is present, so no suggestion is made that "EMPTY" should be used as a data value to represent some form of "Null", "Unknown", "Not Recorded", etc. Choices there would fall into the semantics for some set of controlled vocabularies. The relevance to such a discussion is that this definition would treat an empty string as an empty value, with no semantics attached as to why the value is empty.

For a simplied list of current terms, see the BDQ Core Quick Reference Guide {http://..........}.

Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4, the values of the `Term IRI` and `Definition` are normative. The values of `Term Name` `skos:pref:Label` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Examples` and `Notes`) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.3 Namespace abbreviations

The following namespace abbreviation is used in this document:

| Prefix | IRI |
| --- | --- |
| bdq: | http://rs.tdwg.org/bdq/terms/ |


## 2 Use of Terms

Due to the requirements of [bdq](https://rs.tdwg.org/bdq/terms), controlled value strings MUST be used as values of the `bdq:` namespace.

## 3 Term indices