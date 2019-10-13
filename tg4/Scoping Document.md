# Vocabularies of values Scoping Document


A current best practice for vocabulary building is a chartered deliverable from the Vocabularies Task Group of the TDWG Data Quality Interest Group. Such best practice would set the minimum requirements that a TDWG vocabulary of values should comply with. These include vocabulary metadata and documentation (e.g., authoritative sources/authorship, versioning, recommended usage, etc.). Vocabulary building within TDWG must follow the TDWG Standards Documentation Specification, which provides a way to consistently describe vocabularies both in human and machine-readable forms, but does not specify what content is needed for metadata and documentation of a vocabulary. Other standards should also be taken into consideration, such as the ISO 25964 standard (particularly ISO 25964-2, regarding thesauri and interoperability with other vocabularies), and the ANSI/NISO Z39.19-2005 (R2010) (regarding monolingual controlled vocabularies). Also relevant is the TDWG Darwin Core RDF Guide, which describes appropriate uses of the dwc and dwciri namespaces for literal and object values.


## Terms scope

Initial focus for building vocabularies of values will be built on the Darwin Core standard, as one of the most frequently used standards for biodiversity data sharing. It is acknowledged that some Darwin Core terms are paralleled in or associated with terms in other existing and developing standards (e.g., ABCD), and that therefore the effort made for Darwin Core vocabularies of values would apply to those other standards as well. It is recommended, however, that additional terms from other standards such as ABCD, be specifically targeted in the future. 
Within the Darwin Core Standard there are some specific terms for which it is recommended to use “a controlled vocabulary” . The list of those terms has been gathered [here](https://github.com/tdwg/bdq/wiki/Vocabularies-needed-for-Darwin-Core-terms). That document includes existing vocabularies that are suggested for use for each term.
There are other terms which may benefit from the use of controlled values, but which currently are not recommended to do so (e.g., license, identificationQualifier). Taxon name terms are explicitly beyond the scope of this Task Group.
This Task Group therefore intends to first target a subset of Darwin Core terms for building TDWG vocabularies of values, or identifying existing external vocabularies. This subset includes the terms a) listed as [needing a vocabulary for the implementation of Data Quality Tests](https://github.com/tdwg/bdq/wiki/Vocabularies-needed-for-Darwin-Core-terms) (developed by the Data Quality Tests and Assertions Task Group [BDQ TG2](https://github.com/tdwg/bdq/tree/master/tg2),  among which are dwc:basisOfRecord/rdf:type, dcterms:license/xmpRights:UsageTerm, dwc:continent, dwc:country, dwc:countryCode, dwc/dwciri:geodeticDatum, dwc/dwciri:identificationQualifier, dwc[/dwciri]:taxonomicStatus, etc.); b) that have been targeted by other active interest groups/task groups (e.g., dwc/dwciri:establishmentMeans, dwc/dwciri:occurrenceStatus, worked by the Invasive Organism Information task group); and c) terms that have been identified to be widely used in the community (such as dwc/dwciri:sex, dwc/dwciri:lifeStage and dwc/dwciri:reproductiveCondition). This might not necessarily imply de novo construction of vocabularies, but should include the assessment of already existing vocabularies and declaration of adoption of any of those if appropriate. The mechanism for tackling vocabulary building within the TDWG infrastructure (i.e., Interest Groups and Task Groups involved) is discussed below.


## Types of vocabularies needed

Over many years of working with biodiversity data, the community has repeatedly come to the conclusion that it is of pressing importance to have shared vocabularies of values, given the vasts amounts of data published through aggregators and the heterogeneity found in those data. This conclusion also arises from the work of building the Tests and Assertions, where many of the core tests have been identified to need them. Major factors contributing to heterogeneity in the data are the use of different words to describe single concepts, e.g., over 22 thousand values for dwc:sex in GBIF. This heterogeneity could be greatly reduced by providing lists of unique values from which data providers could pick, in a schema that could provide values tied to definitions and which could accommodate alternative options such as synonyms and language-dependent values. A reasonable solution would be to build multilingual thesauri  of terms.
Thesauri are controlled vocabularies  in which concepts are represented by preferred terms, and where relationships between concepts are explicitly declared. The preferred terms can be accompanied by synonyms, which could be used to look up preferred values and, through amendments, allow for better data quality and easier data cleaning. In multilingual thesauri each concept is represented by a preferred term in each of the languages used, but there is still a single structure of hierarchical and associative relationships between concepts which is independent of the language used (ISO 25964-1). One possible schema that could be used to build the thesauri is the Simple Knowledge Organization System (SKOS), which could be used to produce human and machine-readable vocabularies.
The construction of novel thesauri within TDWG would need to follow the TDWG Standards Documentation Specification regarding human-readable documentation and metadata description for machine-readability. This specification will be included in the Current Best Practice that this Task Group will create (see the [Task Group Charter](https://www.tdwg.org/community/bdq/tg-4/)).
It is acknowledged that a more semantically-related use of vocabularies would be valuable to leverage a linked open data model where automated reasoning is allowed. For this purpose, the need for ontologies for certain terms is recognized, and would be recommended . Examples of such terms are rdf:type (the object analogue for literals in dwc:basisOfRecord) and dcterms:type. However, for other terms the development of ontologies, aside from being resource-consuming, might not be the most efficient solution, at least in the short and mid-term. Instead, as described before, thesauri would answer the community need and provide a suitable means of solving the heterogeneity issue. This, however, does not prevent building or adopting existing appropriate ontologies in the future as needed.
Among the terms for which this task group will develop exemplary controlled vocabularies, we will examine one Darwin Core term which sensibly takes both literal values (in the dwc namespace), and references to non-literal objects (in the dwciri namespace), and develop: 1) competency questions for that term, 2) a simple controlled vocabulary of values for that term, 3) a thesaurus for that term, and 4) an ontology for that term. The task group will identify required metadata elements for each of those forms of the vocabulary, and from this exercise, develop a best practice document for vocabulary development.



## Vocabularies building strategy

Given the variety of Darwin Core terms that could use well-defined vocabularies of values, this Task Group recommends that no single strategy should be adopted for their creation, but that different methods be used depending on the nature and uses of each term to be controlled. Commonalities for the development of vocabularies of values probably include examination of existing vocabularies pertinent to the term at hand to help elucidate whether an applicability statement or a TDWG technical standard is needed for the term, and the framing of competency questions concerning the term to elucidate whether reasoning is important to the use of the term. It is anticipated that internationalization and support for non-normative translations of normative definitions will be requirements for all TDWG vocabularies.
For the creation of vocabularies of values it is expected that groups of different origins (interest groups, task groups, or groups whose main activities are outside TDWG) would work on specific terms, as they contribute the domain expertise (e.g., invasive species group for vocabularies for terms such as dwc:establishmentMeans). It is recommended that the [TDWG Technical Architecture Group (TAG)](https://www.tdwg.org/about/committees/tag/) take a coordination role for the review and gathering of vocabularies of value, as it already has links across all TDWG interest groups and can oversee interoperability. For terms that are cross-discipline (e.g., dwc:basisOfRecord, dwc:lifeStage), it may be appropriate that task groups are created under the TAG, each charged with building a specific vocabulary or applicability statement. By adopting this strategy, and under TDWG’s current organization, once a vocabulary is completed the corresponding Task Group would be closed and the maintenance of the vocabulary could be taken up by the TAG itself of by a maintenance group that could be established for a particular vocabulary or a set of vocabularies. It is expected that task groups would be constituted bringing together relevant stakeholders. For instance, this might imply leveraging the capacity of coordinating the participation of different discipline-specific groups within the community, fostering involvement of members representing different languages. It is also expected that other relevant Interest Groups and Task Groups would be involved (e.g., Darwin Core Maintenance Interest Group, Biodiversity Data Quality Interest Group).



## References


Vocabulary Maintenance Specification Task Group. 2017. Standards Documentation Specification. Biodiversity Information Standards (TDWG).
https://github.com/tdwg/vocab/blob/master/sds/documentation-specification.md#tdwg-standards-documentation-specification

Vocabulary Maintenance Specification Task Group. 2017. Vocabulary Maintenance Standard. Biodiversity Information Standards (TDWG) http://www.tdwg.org/standards/642

ISO 25964 - the international standard for thesauri and interoperability with other vocabularies. https://en.wikipedia.org/wiki/ISO_25964

ANSI/NISO Z39.19-2005 (R2010), Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies. https://en.wikipedia.org/wiki/ISO_25964

Miles, Bechhofer. 2009. SKOS Simple Knowledge Organization System Reference. https://www.w3.org/TR/2009/REC-skos-reference-20090818/. Also: 
https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System

Vocabularies Task Group Charter, TDWG Data Quality Interest Group. https://www.tdwg.org/community/bdq/tg-4/. 

Baskauf. 2017. Controlled values (again). The connection between The Darwin Core Hour and the TDWG Standards Documentation Specification. 
http://baskauf.blogspot.com/2017/03/controlled-values-again.html

Baskauf. 2017. Using the TDWG Standards Documentation Specification with a Controlled Vocabulary. http://baskauf.blogspot.com/2017/05/using-tdwg-standards-documentation.html




