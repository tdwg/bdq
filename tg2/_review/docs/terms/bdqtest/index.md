<!--- This file is generated from templates by code, DO NOT EDIT by hand --->

<!--- layout: home --->

# BDQ Tests Quick Reference Guide
<!--- {:.lead} --->

Draft Standard for Review

<!--- Note: This document deliberately diverges from many of the SHOULD expecations of section 3.2.3 Layout and style of the SDS for the express purpose of simplicity. Some header values have been included in the first paragraph of text, others have been omitted, a table of contents has been omitted, the introduction and abstract are combined, the introduction is not given a heading, and, in consequence, headings are not numbered. --->

This document is intended to be an easy-to-read reference for the Tests maintained as part of the TDWG standard [BDQ](http://example.org/to_be_determined) produced by the TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions and is maintained by the BDQ Maintenance Interest Group. This document lists the BDQ Tests, described by the [Terms Used in the BDQ Tests Quick Reference Guide](bdqtest_qrg_term_descriptions.md). Definitions, comments, and examples may include namespace abbreviations (e.g., `bdq:`, `dwc:`). These are required as the meaning for the word is defined specifically in that namespace. Thus, `dwc:Event` means Event as defined by Darwin Core at https://dwc.tdwg.org/terms/#event.

This page is a descriptive document, not the full vocabulary definition document for `bdqtest:` terms. It combines the normative Test names and terms with non-normative comments and examples that are meant to help people to use the Tests consistently. Further details can be found in [The Biodiversity Data Quality (BDQ) Standard](../../../index.md), the [Fitness For Use Framework Ontology Guide](../../guide/bdqffdq/index.md), the [BDQ Implementer's Guide](../../guide/implementers/index.md). 

If you have questions or suggestions, submit these to the [BDQ Issues](https://github.com/tdwg/bdq/issues) page in GitHub. See the bottom of this document for how to cite the BDQ standard and this document in particular.

# Indexes to the Tests

## Linked Indexes

Index by: [UseCase](qrg_index_by_usecase.md), [InformationElement ActedUpon](qrg_index_by_ie_actedupon.md), [InformationElement Class](qrg_index_by_ie_class.md), [Data Quality Dimension](qrg_index_by_dimension.md), 

This document also includes `Measures` operating on Test `Responses` for `Multi Records` (datasets) indexed in [Multi Record Measures](qrg_multirecord_index.md)

## Alphabetical Index to Single Record Tests

Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFREC...
issueNumber                                                                            58
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/58
iri                                     https://rs.tdwg.org/bdqtest/terms/version/b60c...
term_iri                                https://rs.tdwg.org/bdqtest/terms/b60c8c58-013...
issued                                                                         2025-03-07
term_localName                                       b60c8c58-0137-4b6a-97e9-57d8ca5cf248
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                     Record-level
InformationElement:ActedUpon               bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:basisOfRecord is bdq:NotEmpty...
SpecificationGuid                           urn:uuid:5aabe3d4-d2c0-415c-8972-c834b543971a
MethodGuid                                  urn:uuid:31c40ce6-eecd-4304-bda7-0234993b079d
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_BASISOFRECORD_N...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 147, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFREC...
issueNumber                                                                           104
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/104
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f5dd...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f5dd74bd-6a2...
issued                                                                         2025-03-07
term_localName                                       f5dd74bd-6a22-4792-b675-c7ccf2a2c103
DateLastUpdated                                                                2024-08-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                     Record-level
InformationElement:ActedUpon               bdq:VALIDATION_BASISOFRECORD_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:f094b94f-09b6-4fb0-8ba4-24252a2101c4
MethodGuid                                  urn:uuid:99103239-1019-4d2e-b435-ecb28c190a3c
AuthoritiesDefaults                     bdq:sourceAuthority default = "Darwin Core bas...
Description                             Count the number of VALIDATION_BASISOFRECORD_S...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                        a723528a-ee73-44a7-818d-5315323ec4e9
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 193, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICA...
issueNumber                                                                           123
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/123
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a56f...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a56fb342-c8e...
issued                                                                         2025-03-06
term_localName                                       a56fb342-c8ee-4611-8aab-e6c6357e8875
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:21d0b5f6-5b3e-4810-8413-c975b7cf343a
MethodGuid                                  urn:uuid:b751c2ed-11a5-4bff-9c37-1eccc8138191
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_CLASSIFICATION_...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Cons...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        d6bc8db2-014b-47dc-9737-b0ecd98bf5bb
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 215, dtype: object
Row:
Label                                     MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND
issueNumber                                                                            77
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/77
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7270...
term_iri                                https://rs.tdwg.org/bdqtest/terms/7270a362-5f2...
issued                                                                         2025-03-06
term_localName                                       7270a362-5f2e-41f0-955a-d7a8eaaf0f17
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                          bdq:VALIDATION_CLASS_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:a2b39526-d08a-4a91-8b6d-aacf73677789
MethodGuid                                  urn:uuid:6d096b24-0eb1-4e6e-804f-6810e781d16f
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_CLASS_FOUND in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        cd12d17c-8404-40fa-bc15-5583564ddd14
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 163, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATE...
issueNumber                                                                            50
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/50
iri                                     https://rs.tdwg.org/bdqtest/terms/version/d68d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/d68dc111-970...
issued                                                                         2025-03-07
term_localName                                       d68dc111-9704-4fc5-a8eb-5fa084809202
DateLastUpdated                                                                2024-08-30
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTE...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:4343a7e0-7f0b-434d-99d4-e939ecb16e1f
MethodGuid                                  urn:uuid:2afcbce1-7cf8-4c5c-9df4-d267dc2df704
AuthoritiesDefaults                     bdq:sourceAuthority default = "10m-admin-1 bou...
Description                             Count the number of VALIDATION_COORDINATESCOUN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                                    bdq:Spatial-Temporal_Patterns
ArgumentGuids                           8a3f5702-a4e5-4b21-acb6-a4eae9a1ae09,972320cd-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 141, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATE...
issueNumber                                                                            56
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/56
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c6c9...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c6c998af-614...
issued                                                                         2025-03-07
term_localName                                       c6c998af-6145-4361-b1e6-52c5b790340a
DateLastUpdated                                                                2024-08-30
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSIS...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:4dd617df-a984-419f-b7b5-098b2023c4ab
MethodGuid                                  urn:uuid:315a198d-3811-40dd-918a-756f598f3294
AuthoritiesDefaults                     bdq:sourceAuthority default = "10m-admin-1 bou...
Description                             Count the number of VALIDATION_COORDINATESSTAT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           b7c56646-56f1-4094-b2be-8546c7e18102,cceaf335-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 145, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATE...
issueNumber                                                                            51
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/51
iri                                     https://rs.tdwg.org/bdqtest/terms/version/b67f...
term_iri                                https://rs.tdwg.org/bdqtest/terms/b67f41f4-198...
issued                                                                         2025-03-07
term_localName                                       b67f41f4-198c-41e9-9419-ba3919c1be8b
DateLastUpdated                                                                2024-08-30
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CO...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if either bdq:t...
SpecificationGuid                           urn:uuid:45cb9e13-7944-4535-a5ef-f6ededb77305
MethodGuid                                  urn:uuid:2bb364f7-118b-4258-8afe-978901e5cf67
AuthoritiesDefaults                     bdq:taxonIsMarine default = "World Register of...
Description                             Count the number of VALIDATION_COORDINATESTERR...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           3968f8d0-7364-4f3d-9993-96b8678f1653,cbb3483c-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 143, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATE...
issueNumber                                                                            87
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/87
iri                                     https://rs.tdwg.org/bdqtest/terms/version/0e23...
term_iri                                https://rs.tdwg.org/bdqtest/terms/0e239a55-0f1...
issued                                                                         2025-03-07
term_localName                                       0e239a55-0f19-4c68-bdbf-20580f27a647
DateLastUpdated                                                                2023-06-20
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                  bdq:VALIDATION_COORDINATES_NOTZERO.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalL...
SpecificationGuid                           urn:uuid:b482148e-9ac2-47ad-99b5-462508e9f360
MethodGuid                                  urn:uuid:8454615d-9cd4-49af-8fd3-c67e6be9c777
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_COORDINATES_NOT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                      Likeliness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation SPACE CODED Test Likeliness CORE
UseCases                                                    bdq:Spatial-Temporal_Patterns
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 177, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATE...
issueNumber                                                                           109
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/109
iri                                     https://rs.tdwg.org/bdqtest/terms/version/2d90...
term_iri                                https://rs.tdwg.org/bdqtest/terms/2d90d94b-d38...
issued                                                                         2025-03-07
term_localName                                       2d90d94b-d384-4bac-aa68-c6800d765882
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.R...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:coordina...
SpecificationGuid                           urn:uuid:f8dfc3fc-6580-4518-b2b4-595c29e9042e
MethodGuid                                  urn:uuid:a5bbeae3-9dc8-4a0c-9f68-58526e5d6a76
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_COORDINATEUNCER...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 201, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOD...
issueNumber                                                                            98
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/98
iri                                     https://rs.tdwg.org/bdqtest/terms/version/d71b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/d71be8d4-1a0...
issued                                                                         2025-03-07
term_localName                                       d71be8d4-1a04-4816-90c5-49808c823651
DateLastUpdated                                                                2024-11-10
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:countryCode is bdq:NotEmpty; ...
SpecificationGuid                           urn:uuid:d153d4bd-b39d-43b0-b00a-395ff3e2ca62
MethodGuid                                  urn:uuid:930eb72e-fe83-48ae-9698-ca46713721a3
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_COUNTRYCODE_NOT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Com...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 185, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOD...
issueNumber                                                                            20
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/20
iri                                     https://rs.tdwg.org/bdqtest/terms/version/3896...
term_iri                                https://rs.tdwg.org/bdqtest/terms/38966850-373...
issued                                                                         2025-03-07
term_localName                                       38966850-3737-4a67-953c-c231469e0489
DateLastUpdated                                                                2024-09-19
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_COUNTRYCODE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047
MethodGuid                                  urn:uuid:02f5a440-a473-42cf-a3f1-6c10334d5eb8
AuthoritiesDefaults                     bdq:sourceAuthority default = "ISO 3166 Countr...
Description                             Count the number of VALIDATION_COUNTRYCODE_STA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 111, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOU...
issueNumber                                                                            62
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/62
iri                                     https://rs.tdwg.org/bdqtest/terms/version/26b4...
term_iri                                https://rs.tdwg.org/bdqtest/terms/26b46375-df2...
issued                                                                         2025-03-07
term_localName                                       26b46375-df2b-4677-a2e5-f96f86b8e242
DateLastUpdated                                                                2024-09-25
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.R...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:6f1093a0-0da5-4691-a95e-184d6d55eeb0
MethodGuid                                  urn:uuid:3925c15a-2795-4cef-8a30-6e6e5e480eae
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Count the number of VALIDATION_COUNTRYCOUNTRYC...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 151, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTA...
issueNumber                                                                           201
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/201
iri                                     https://rs.tdwg.org/bdqtest/terms/version/8b73...
term_iri                                https://rs.tdwg.org/bdqtest/terms/8b73f37d-89e...
issued                                                                         2025-03-07
term_localName                                       8b73f37d-89ed-479a-8389-9e71ad2ac84d
DateLastUpdated                                                                2024-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOU...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:e5efdd20-d1fc-4287-91f9-15b9ce3f3aac
MethodGuid                                  urn:uuid:f1a7f272-9040-42da-9b64-62abedefb1b0
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Count the number of VALIDATION_COUNTRYSTATEPRO...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                        aabaaac7-b26c-478e-9f04-3e2fbdba4a96
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 235, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND
issueNumber                                                                            21
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/21
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f15c...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f15c38c3-d96...
issued                                                                         2025-03-07
term_localName                                       f15c38c3-d96d-4e9c-982d-410fb71cf2bc
DateLastUpdated                                                                2024-08-19
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                        bdq:VALIDATION_COUNTRY_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848
MethodGuid                                  urn:uuid:04cee4e0-0c83-40cc-8de2-e7391f0a97a9
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Count the number of VALIDATION_COUNTRY_FOUND i...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                        3e00109a-13d3-416d-9a91-127c99b47473
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 113, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NO...
issueNumber                                                                            42
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/42
iri                                     https://rs.tdwg.org/bdqtest/terms/version/6887...
term_iri                                https://rs.tdwg.org/bdqtest/terms/6887c881-dc5...
issued                                                                         2025-03-07
term_localName                                       6887c881-dc52-409b-8979-9c2f05e55569
DateLastUpdated                                                                2024-09-27
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                     bdq:VALIDATION_COUNTRY_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:country is bdq:NotEmpty or dw...
SpecificationGuid                           urn:uuid:34ef6ea2-de06-4d2c-88fe-2c779de8f7db
MethodGuid                                  urn:uuid:23e9d641-1349-4998-bdff-117e32c30eff
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_COUNTRY_NOTEMPT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 133, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTI...
issueNumber                                                                            76
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/76
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c72f...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c72fda2d-16e...
issued                                                                         2025-03-07
term_localName                                       c72fda2d-16e1-4ded-91a5-a7094339d603
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                               dwc:Identification
InformationElement:ActedUpon               bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:date...
SpecificationGuid                           urn:uuid:a25786df-a624-4ff2-8962-6b23e8b07b0b
MethodGuid                                  urn:uuid:67ddf706-c8ee-4cf2-a9d0-d161fc6b7d69
AuthoritiesDefaults                     bdq:earliestValidDate default = "1753-01-01",b...
Description                             Count the number of VALIDATION_DATEIDENTIFIED_...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                      Likeliness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Likeliness ISO/...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           13c17157-1714-4f67-848b-9dc031917fee,030797c0-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 161, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTI...
issueNumber                                                                            69
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/69
iri                                     https://rs.tdwg.org/bdqtest/terms/version/49b7...
term_iri                                https://rs.tdwg.org/bdqtest/terms/49b787eb-7dc...
issued                                                                         2025-03-07
term_localName                                       49b787eb-7dce-4ace-97f5-7cbb47cd8cb9
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                               dwc:Identification
InformationElement:ActedUpon              bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIden...
SpecificationGuid                           urn:uuid:89f8b2ea-fc35-4941-929a-0e32cfbeb1a6
MethodGuid                                  urn:uuid:4c6a5522-ae8c-42d3-a396-8fc3aee49ef9
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DATEIDENTIFIED_...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance ISO...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 157, dtype: object
Row:
Label                                     MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE
issueNumber                                                                           125
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/125
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7804...
term_iri                                https://rs.tdwg.org/bdqtest/terms/780480ff-8c4...
issued                                                                         2025-03-06
term_localName                                       780480ff-8c4a-4276-aaca-cbd1248de9fa
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                          bdq:VALIDATION_DAY_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:day ...
SpecificationGuid                           urn:uuid:2563ae15-a5bf-48fc-91f3-6df869aece2d
MethodGuid                                  urn:uuid:bb12babf-ca13-4289-9a3d-dde52bb8aff8
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DAY_INRANGE in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 217, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD
issueNumber                                                                           147
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/147
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c3e0...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c3e0100f-dfc...
issued                                                                         2025-03-06
term_localName                                       c3e0100f-dfc3-4379-a855-df878eef295e
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                         bdq:VALIDATION_DAY_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:day is b...
SpecificationGuid                           urn:uuid:c0fce1a1-8879-4175-8a71-ce037655c358
MethodGuid                                  urn:uuid:d9bfd4f7-e158-43ee-8ac4-1bc51bf33307
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DAY_STANDARD in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 225, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOT...
issueNumber                                                                           103
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/103
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f041...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f041ab17-d83...
issued                                                                         2025-03-07
term_localName                                       f041ab17-d834-4586-aa6b-090de2e571a8
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                     Record-level
InformationElement:ActedUpon                      bdq:VALIDATION_DCTYPE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dc:type is bdq:NotEmpty; otherwis...
SpecificationGuid                           urn:uuid:e1286c46-2a95-480d-89e4-f02681372eb7
MethodGuid                                  urn:uuid:95c2e363-5a99-4276-937d-98008ca893f9
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DCTYPE_NOTEMPTY...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 191, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STA...
issueNumber                                                                            91
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/91
iri                                     https://rs.tdwg.org/bdqtest/terms/version/fbe4...
term_iri                                https://rs.tdwg.org/bdqtest/terms/fbe47441-500...
issued                                                                         2025-03-07
term_localName                                       fbe47441-500f-44c7-a1bd-1e872edc5266
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                     Record-level
InformationElement:ActedUpon                      bdq:VALIDATION_DCTYPE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:b85129f0-28c2-4ede-aff2-5ce3791c6e86
MethodGuid                                  urn:uuid:8b06bef9-7fd4-4020-b08c-a07a1bf695b6
AuthoritiesDefaults                     DCMI Type Vocabulary" {[http://purl.org/dc/ter...
Description                             Count the number of VALIDATION_DCTYPE_STANDARD...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 181, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLAT...
issueNumber                                                                            79
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/79
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f0fb...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f0fb1c79-9e3...
issued                                                                         2025-03-07
term_localName                                       f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon              bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalL...
SpecificationGuid                           urn:uuid:a5111c0c-d198-4ecc-af10-809ae2b3ae01
MethodGuid                                  urn:uuid:6f3a7ebb-e857-42e0-8051-4d06feeb4ab2
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DECIMALLATITUDE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 167, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLAT...
issueNumber                                                                           119
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/119
iri                                     https://rs.tdwg.org/bdqtest/terms/version/bcea...
term_iri                                https://rs.tdwg.org/bdqtest/terms/bceae35a-52a...
issued                                                                         2025-03-07
term_localName                                       bceae35a-52ab-4968-846f-069ace766513
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon             bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:decimalLatitude is bdq:NotEmp...
SpecificationGuid                           urn:uuid:0067fa60-5503-490e-8c94-93fb79cc7da2
MethodGuid                                  urn:uuid:b12c8663-25e8-4c8a-abfc-edf4334d1aef
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DECIMALLATITUDE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 209, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLON...
issueNumber                                                                            30
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/30
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c70c...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c70c4950-224...
issued                                                                         2025-03-07
term_localName                                       c70c4950-2246-4acc-a59d-81eaa47edf2b
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon             bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalL...
SpecificationGuid                           urn:uuid:1a504f7f-21a7-49e1-a0dc-f51146957fa4
MethodGuid                                  urn:uuid:0ff56b48-f00e-45bd-822e-e04afbcef3e1
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DECIMALLONGITUD...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 121, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLON...
issueNumber                                                                            96
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/96
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f948...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f948a30e-808...
issued                                                                         2025-03-07
term_localName                                       f948a30e-8084-48d5-b1ca-d77c476f181f
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:decimalLongitude is bdq:NotEm...
SpecificationGuid                           urn:uuid:c893ee17-ee8b-43ec-bf17-97ac814ea502
MethodGuid                                  urn:uuid:908fc823-75a9-437e-be7c-5c72cd6b149e
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_DECIMALLONGITUD...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 183, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFES...
issueNumber                                                                           275
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/275
iri                                     https://rs.tdwg.org/bdqtest/terms/version/1b8a...
term_iri                                https://rs.tdwg.org/bdqtest/terms/1b8ae68e-63f...
issued                                                                         2025-03-07
term_localName                                       1b8ae68e-63f1-41c0-9025-fbe64db38d64
DateLastUpdated                                                                2024-02-09
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD....
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:fec2103b-5d46-4723-b2ec-8c8119b44aaf
MethodGuid                                  urn:uuid:fd15e0a4-f49d-4566-b700-a9b46c284e68
AuthoritiesDefaults                     bdq:sourceAuthority default = "Degree of Estab...
Description                             Count the number of VALIDATION_DEGREEOFESTABLI...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                                                bdq:Alien-Species
ArgumentGuids                                        8aac7359-311a-405f-8117-79bb4873011d
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 247, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYE...
issueNumber                                                                           131
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/131
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7775...
term_iri                                https://rs.tdwg.org/bdqtest/terms/7775309b-533...
issued                                                                         2025-03-06
term_localName                                       7775309b-5331-4a65-b839-cbe959948d33
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                 bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOf...
SpecificationGuid                           urn:uuid:62f754b5-a0a1-4b24-9982-b76e4e169f71
MethodGuid                                  urn:uuid:ca1bc131-fa85-4fdf-902d-ad20bd4ba0f4
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_ENDDAYOFYEAR_IN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 223, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHM...
issueNumber                                                                           268
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/268
iri                                     https://rs.tdwg.org/bdqtest/terms/version/130b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/130bb875-6b7...
issued                                                                         2025-03-07
term_localName                                       130bb875-6b7c-4965-b864-d53f9d05b2cd
DateLastUpdated                                                                2024-02-08
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Res...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:f1d3bf9c-5558-41dc-8e33-b17c499be016
MethodGuid                                  urn:uuid:f89147ba-03e5-432b-8040-0a2a4921d676
AuthoritiesDefaults                     bdq:sourceAuthority default = "Establishment M...
Description                             Count the number of VALIDATION_ESTABLISHMENTME...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                        0c051c38-621f-4a52-ae92-5077afd46446
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 245, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_...
issueNumber                                                                            36
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/36
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c825...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c8250600-de6...
issued                                                                         2025-03-06
term_localName                                       c8250600-de61-4047-9d7c-6e06a38c7994
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                    bdq:VALIDATION_EVENTDATE_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDat...
SpecificationGuid                           urn:uuid:29a1fdc6-326b-4017-880d-d11ff0225b8f
MethodGuid                                  urn:uuid:17f89e32-0174-4bf9-805e-ba7aec59477b
AuthoritiesDefaults                     bdq:earliestValidDate default ="1582-11-15",bd...
Description                             Count the number of VALIDATION_EVENTDATE_INRAN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance Par...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           8b223050-f314-4601-9e20-d5f3d59d8e79,2e5c3e37-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 125, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_...
issueNumber                                                                            33
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/33
iri                                     https://rs.tdwg.org/bdqtest/terms/version/3f62...
term_iri                                https://rs.tdwg.org/bdqtest/terms/3f62eaa2-747...
issued                                                                         2025-03-07
term_localName                                       3f62eaa2-747f-456b-85e6-1a6e74086a18
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                   bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:eventDate is bdq:NotEmpty; ot...
SpecificationGuid                           urn:uuid:1fae3f77-7fcb-42c6-ab43-1ff28adf4fa4
MethodGuid                                  urn:uuid:12499336-882b-4186-b5a2-4a806af2e35b
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_EVENTDATE_NOTEM...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation TIME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 123, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_...
issueNumber                                                                            66
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/66
iri                                     https://rs.tdwg.org/bdqtest/terms/version/bffd...
term_iri                                https://rs.tdwg.org/bdqtest/terms/bffd7499-aca...
issued                                                                         2025-03-06
term_localName                                       bffd7499-aca3-423f-bb43-f7bdc9260f4f
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                   bdq:VALIDATION_EVENTDATE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDat...
SpecificationGuid                           urn:uuid:80c8f69b-4ad3-40ee-bccd-de016bfae367
MethodGuid                                  urn:uuid:3f868855-cc39-4a1b-8050-bfa246416a47
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_EVENTDATE_STAND...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance ISO...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 153, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPO...
issueNumber                                                                            88
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/88
iri                                     https://rs.tdwg.org/bdqtest/terms/version/d3e2...
term_iri                                https://rs.tdwg.org/bdqtest/terms/d3e282a1-3ff...
issued                                                                         2025-03-06
term_localName                                       d3e282a1-3ff3-4ed0-bd08-fa23b6b8c161
DateLastUpdated                                                                2023-09-30
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon               bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if any of dwc:eventDate, dwc:year, d...
SpecificationGuid                           urn:uuid:b57460c4-16e1-4c1d-8a07-a53aee9e8922
MethodGuid                                  urn:uuid:87d34104-0a79-4f51-aeeb-1115ec56e237
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_EVENTTEMPORAL_N...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation TIME CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 179, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONS...
issueNumber                                                                            67
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/67
iri                                     https://rs.tdwg.org/bdqtest/terms/version/1919...
term_iri                                https://rs.tdwg.org/bdqtest/terms/1919f212-b7d...
issued                                                                         2025-03-06
term_localName                                       1919f212-b7db-4b6e-9697-41a715001bd6
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                     bdq:VALIDATION_EVENT_CONSISTENT.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDat...
SpecificationGuid                           urn:uuid:83d057ea-a6f6-49e6-ac3c-0c418776a0e0
MethodGuid                                  urn:uuid:449f44fe-0fef-42ff-a446-d693653b55d4
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_EVENT_CONSISTEN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Consistency CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 155, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND
issueNumber                                                                            28
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/28
iri                                     https://rs.tdwg.org/bdqtest/terms/version/9792...
term_iri                                https://rs.tdwg.org/bdqtest/terms/97928242-11a...
issued                                                                         2025-03-06
term_localName                                       97928242-11a9-4ab0-9dd7-3f0465834824
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                         bdq:VALIDATION_FAMILY_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:16f999d9-1cf5-4208-b2ca-1a93d6700085
MethodGuid                                  urn:uuid:0997d841-9db9-40a8-b6ec-5867e9091532
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_FAMILY_FOUND in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        146784a4-b53c-4245-a813-c41896761279
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 119, dtype: object
Row:
Label                                     MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND
issueNumber                                                                           122
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/122
iri                                     https://rs.tdwg.org/bdqtest/terms/version/977f...
term_iri                                https://rs.tdwg.org/bdqtest/terms/977f7e75-a88...
issued                                                                         2025-03-06
term_localName                                       977f7e75-a88e-4e29-a7b1-e8cdd35aa107
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                          bdq:VALIDATION_GENUS_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:15bbda19-dd18-471a-a5c3-56c7e543012f
MethodGuid                                  urn:uuid:b6cb27ac-e9b8-4a0c-b986-3e34069d8449
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_GENUS_FOUND in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        6304e753-423d-4188-bba4-0301c1a01769
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 213, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDA...
issueNumber                                                                            78
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/78
iri                                     https://rs.tdwg.org/bdqtest/terms/version/63fb...
term_iri                                https://rs.tdwg.org/bdqtest/terms/63fbaf3c-3d4...
issued                                                                         2025-03-07
term_localName                                       63fbaf3c-3d41-4ab6-bfc0-904f1b26835f
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon               bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:geodeticDatum is bdq:NotEmpty...
SpecificationGuid                           urn:uuid:a3c8b277-15fb-4ae8-afb1-e64fb6eb5241
MethodGuid                                  urn:uuid:6d1f3f11-98d9-4b26-a8e7-56fbc066c705
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_GEODETICDATUM_N...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 165, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDA...
issueNumber                                                                            59
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/59
iri                                     https://rs.tdwg.org/bdqtest/terms/version/8d8a...
term_iri                                https://rs.tdwg.org/bdqtest/terms/8d8aba5c-f58...
issued                                                                         2025-03-07
term_localName                                       8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63
DateLastUpdated                                                                2025-03-03
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon               bdq:VALIDATION_GEODETICDATUM_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:5cc05662-c029-4ba9-b32e-fb487ccba71c
MethodGuid                                  urn:uuid:344cb9f6-68e1-4d7c-a976-7edcd9f20935
AuthoritiesDefaults                     bdq:sourceAuthority = "EPSG" {[https://epsg.or...
Description                             Count the number of VALIDATION_GEODETICDATUM_S...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 149, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND
issueNumber                                                                            81
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/81
iri                                     https://rs.tdwg.org/bdqtest/terms/version/012e...
term_iri                                https://rs.tdwg.org/bdqtest/terms/012eade5-fc6...
issued                                                                         2025-03-06
term_localName                                       012eade5-fc64-458a-a13a-a614491bf4e0
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                        bdq:VALIDATION_KINGDOM_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:a90e100a-3522-4742-aa73-3b98a35ab826
MethodGuid                                  urn:uuid:7072bf93-bffc-4d83-ad51-b351c6e53260
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_KINGDOM_FOUND i...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        a5055cb3-b1e5-4070-90df-f875b0d9ae8a
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 169, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NO...
issueNumber                                                                           216
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/216
iri                                     https://rs.tdwg.org/bdqtest/terms/version/342b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/342bd81c-e2b...
issued                                                                         2025-03-06
term_localName                                       342bd81c-e2b7-41d8-b32b-013992d19f99
DateLastUpdated                                                                2024-01-28
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                     bdq:VALIDATION_KINGDOM_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:kingdom is bdq:NotEmpty; othe...
SpecificationGuid                           urn:uuid:e6f0a9ce-3e72-40fb-9fad-63cf5962f93e
MethodGuid                                  urn:uuid:f5bd0eee-4cdf-4455-876d-a46d92373a4e
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_KINGDOM_NOTEMPT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 239, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NO...
issueNumber                                                                            99
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/99
iri                                     https://rs.tdwg.org/bdqtest/terms/version/47ee...
term_iri                                https://rs.tdwg.org/bdqtest/terms/47ee20d9-508...
issued                                                                         2025-03-07
term_localName                                       47ee20d9-5087-4f76-a494-6fea05e50b8b
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                     Record-level
InformationElement:ActedUpon                     bdq:VALIDATION_LICENSE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dcterms:license is bdq:NotEmpty; ...
SpecificationGuid                           urn:uuid:d8b450af-47e6-4f5c-8154-6d6acbe9efa5
MethodGuid                                  urn:uuid:940621f5-4f24-48de-8b36-256101ca4987
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_LICENSE_NOTEMPT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                                            bdq:Record-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 187, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_ST...
issueNumber                                                                            38
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/38
iri                                     https://rs.tdwg.org/bdqtest/terms/version/9d5b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/9d5be694-f5d...
issued                                                                         2025-03-07
term_localName                                       9d5be694-f5da-465d-8c7e-27e6dac69f9f
DateLastUpdated                                                                2024-03-21
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                     Record-level
InformationElement:ActedUpon                     bdq:VALIDATION_LICENSE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:2a9dbd16-d427-471e-8db5-c1de2b2cf030
MethodGuid                                  urn:uuid:180c1a90-94c3-48b5-a9fe-4223d6f2bd60
AuthoritiesDefaults                     bdq:sourceAuthority default = "Creative Common...
Description                             Count the number of VALIDATION_LICENSE_STANDAR...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                                            bdq:Record-Management
ArgumentGuids                                        7308bf21-2648-40d8-bb2c-3f36d2789552
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 127, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_N...
issueNumber                                                                            40
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/40
iri                                     https://rs.tdwg.org/bdqtest/terms/version/bac8...
term_iri                                https://rs.tdwg.org/bdqtest/terms/bac852b5-1ba...
issued                                                                         2025-03-07
term_localName                                       bac852b5-1ba6-427b-aa8e-02018e99279c
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                    bdq:VALIDATION_LOCATION_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if at least one term needed to deter...
SpecificationGuid                           urn:uuid:30ed5e2d-ef30-4988-8dbb-12c119e94ac3
MethodGuid                                  urn:uuid:1f014694-573d-46e0-b38a-2acf71b32071
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_LOCATION_NOTEMP...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 131, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_I...
issueNumber                                                                           187
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/187
iri                                     https://rs.tdwg.org/bdqtest/terms/version/3de8...
term_iri                                https://rs.tdwg.org/bdqtest/terms/3de8af03-05d...
issued                                                                         2025-03-07
term_localName                                       3de8af03-05d4-4fd8-8e6d-ba886dc5446f
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                     bdq:VALIDATION_MAXDEPTH_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumD...
SpecificationGuid                           urn:uuid:cebc8ba0-ca02-4f1e-830e-ec693bc628e4
MethodGuid                                  urn:uuid:ed60f87e-7ab7-446a-8565-903dbe6408d2
AuthoritiesDefaults                     bdq:minimumValidDepthInMeters default="0",bdq:...
Description                             Count the number of VALIDATION_MAXDEPTH_INRANG...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Conformance Pa...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           edf69c59-056d-4c8a-b1fb-647ea684eb18,f41be58e-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 231, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATI...
issueNumber                                                                           112
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/112
iri                                     https://rs.tdwg.org/bdqtest/terms/version/6a3b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/6a3baf78-5ec...
issued                                                                         2025-03-07
term_localName                                       6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_MAXELEVATION_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumE...
SpecificationGuid                           urn:uuid:f9471802-a5f7-4f4e-9810-f3f4f43dad1a
MethodGuid                                  urn:uuid:a6035033-0779-4a75-99ea-f7112c1dde2b
AuthoritiesDefaults                     bdq:minimumValidElevationInMeters default = "-...
Description                             Count the number of VALIDATION_MAXELEVATION_IN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Likeliness Par...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           3ab181c2-a3d8-4317-af4d-f88181e2773a,1766715d-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 203, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_I...
issueNumber                                                                           107
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/107
iri                                     https://rs.tdwg.org/bdqtest/terms/version/9c66...
term_iri                                https://rs.tdwg.org/bdqtest/terms/9c66c116-664...
issued                                                                         2025-03-07
term_localName                                       9c66c116-6644-45b4-b4c7-db7a4ee7c500
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                     bdq:VALIDATION_MINDEPTH_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumD...
SpecificationGuid                           urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544
MethodGuid                                  urn:uuid:9cc301b1-e303-4abb-9d24-d31506de9436
AuthoritiesDefaults                     bdq:minimumValidDepthInMeters default="0",bdq:...
Description                             Count the number of VALIDATION_MINDEPTH_INRANG...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Conformance Pa...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           d23e61b3-07b6-4326-bac2-1457b030efef,9f12e2c3-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 197, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_L...
issueNumber                                                                            24
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/24
iri                                     https://rs.tdwg.org/bdqtest/terms/version/b212...
term_iri                                https://rs.tdwg.org/bdqtest/terms/b21256c2-4bb...
issued                                                                         2025-03-07
term_localName                                       b21256c2-4bb7-4deb-852d-a9eaa05345e7
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Resp...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumD...
SpecificationGuid                           urn:uuid:12f7f82e-ab1c-4690-92b8-ecc9328256c1
MethodGuid                                  urn:uuid:07e4c491-0d13-409d-b966-fbb9721e81cf
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_MINDEPTH_LESSTH...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 117, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATI...
issueNumber                                                                            39
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/39
iri                                     https://rs.tdwg.org/bdqtest/terms/version/0712...
term_iri                                https://rs.tdwg.org/bdqtest/terms/071267a0-d99...
issued                                                                         2025-03-07
term_localName                                       071267a0-d993-4961-a3f7-d8210810d167
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_MINELEVATION_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumE...
SpecificationGuid                           urn:uuid:2bb79221-0312-410a-aef6-f569485df6a6
MethodGuid                                  urn:uuid:1aa9c50e-7e8a-445f-9cf3-12af51a9ec10
AuthoritiesDefaults                     bdq:minimumValidElevationInMeters default = "-...
Description                             Count the number of VALIDATION_MINELEVATION_IN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Conformance Pa...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           6e07e4fe-ce7a-4e5f-9fa3-c26877b273a7,307b78fe-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 129, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATI...
issueNumber                                                                           108
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/108
iri                                     https://rs.tdwg.org/bdqtest/terms/version/be2e...
term_iri                                https://rs.tdwg.org/bdqtest/terms/be2eb717-b39...
issued                                                                         2025-03-07
term_localName                                       be2eb717-b390-47d1-b7ba-965a1101e215
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVAT...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:maximuml...
SpecificationGuid                           urn:uuid:f799fb5c-37e4-46d7-a07e-87eb071df9c6
MethodGuid                                  urn:uuid:a0486e4f-210d-4143-ae5a-f320bebc2cb5
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_MINELEVATION_LE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 199, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STAN...
issueNumber                                                                           126
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/126
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c3b4...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c3b4cd93-a37...
issued                                                                         2025-03-06
term_localName                                       c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                       bdq:VALIDATION_MONTH_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:month is...
SpecificationGuid                           urn:uuid:2c5dbdbb-feab-474c-bcca-bf6d1b90ae66
MethodGuid                                  urn:uuid:bb630881-2a79-4750-ae0f-36d0df2191f7
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_MONTH_STANDARD ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 219, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLIS...
issueNumber                                                                           259
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/259
iri                                     https://rs.tdwg.org/bdqtest/terms/version/36ea...
term_iri                                https://rs.tdwg.org/bdqtest/terms/36ea0a78-a07...
issued                                                                         2025-03-06
term_localName                                       36ea0a78-a079-4014-aca3-2f2b3b11e822
DateLastUpdated                                                                2024-02-07
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Re...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:namePublishedInYear is bdq:No...
SpecificationGuid                           urn:uuid:f09fc9ad-a449-4422-b32f-63d8ccf2501f
MethodGuid                                  urn:uuid:f8024a02-76c0-482a-b805-097d0cdc82e2
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_NAMEPUBLISHEDIN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 243, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCE...
issueNumber                                                                            47
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/47
iri                                     https://rs.tdwg.org/bdqtest/terms/version/0c9a...
term_iri                                https://rs.tdwg.org/bdqtest/terms/0c9a139e-5d2...
issued                                                                         2025-03-07
term_localName                                       0c9a139e-5d23-44de-a495-14ec08c61a1c
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:occurrenceID is bdq:NotEmpty;...
SpecificationGuid                           urn:uuid:3d9e1339-19d7-47e7-af9e-11905df82b6a
MethodGuid                                  urn:uuid:296e08b2-c044-4cef-930e-8d29c579c8d6
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_OCCURRENCEID_NO...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                                            bdq:Record-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 137, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCE...
issueNumber                                                                           117
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/117
iri                                     https://rs.tdwg.org/bdqtest/terms/version/298d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/298db0c9-a85...
issued                                                                         2025-03-07
term_localName                                       298db0c9-a85a-41ee-b111-d622fd969d71
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:occurrenceStatus is bdq:NotEm...
SpecificationGuid                           urn:uuid:c3a53898-c4ad-40e0-961b-b4ceafea37c7
MethodGuid                                  urn:uuid:af9591f4-d0ee-4301-bc59-d6a68d1d6813
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_OCCURRENCESTATU...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 207, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCE...
issueNumber                                                                           116
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/116
iri                                     https://rs.tdwg.org/bdqtest/terms/version/faca...
term_iri                                https://rs.tdwg.org/bdqtest/terms/faca6558-dbf...
issued                                                                         2025-03-07
term_localName                                       faca6558-dbff-4d26-a5cb-e11cdf632fe7
DateLastUpdated                                                                2025-02-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:fbe854d4-acf3-4c79-a654-81441fed644f
MethodGuid                                  urn:uuid:acc05ff6-b1c8-4001-8aad-930a9b9ccaf8
AuthoritiesDefaults                     bdq:sourceAuthority default = "Regex present/a...
Description                             Count the number of VALIDATION_OCCURRENCESTATU...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 205, dtype: object
Row:
Label                                     MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND
issueNumber                                                                            83
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/83
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f4fa...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f4fa449c-4b7...
issued                                                                         2025-03-06
term_localName                                       f4fa449c-4b74-4dcf-b4cf-0b73e1496375
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                          bdq:VALIDATION_ORDER_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:ae08b4b4-89ba-4972-b51f-912b132bd006
MethodGuid                                  urn:uuid:79096434-5b55-40e1-9afb-e138a11f82ba
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_ORDER_FOUND in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        c169404f-d797-40a1-9c84-3edb2383b759
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 173, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_ST...
issueNumber                                                                           277
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/277
iri                                     https://rs.tdwg.org/bdqtest/terms/version/15e0...
term_iri                                https://rs.tdwg.org/bdqtest/terms/15e0da1d-1a4...
issued                                                                         2025-03-07
term_localName                                       15e0da1d-1a43-4075-8454-b2e618cdd25b
DateLastUpdated                                                                2024-02-09
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                     bdq:VALIDATION_PATHWAY_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:c7c92ef0-284e-4c5d-8fc9-f1480bfe0b8e
MethodGuid                                  urn:uuid:ffae8e47-2181-4a83-b1c7-d0a893e79b67
AuthoritiesDefaults                     bdq:sourceAuthority default = "Pathway Control...
Description                             Count the number of VALIDATION_PATHWAY_STANDAR...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                        136039c5-6ceb-41ec-90b3-eb1cd37d6eed
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 249, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND
issueNumber                                                                            22
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/22
iri                                     https://rs.tdwg.org/bdqtest/terms/version/65e6...
term_iri                                https://rs.tdwg.org/bdqtest/terms/65e66ca0-e9d...
issued                                                                         2025-03-06
term_localName                                       65e66ca0-e9d1-4411-ad26-bb9c43f32afc
DateLastUpdated                                                                2022-03-25
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                         bdq:VALIDATION_PHYLUM_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:1193230f-f188-4917-92da-bba3390ed3fa
MethodGuid                                  urn:uuid:06f9faab-102a-452a-b6e0-4eafd8d7e71d
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_PHYLUM_FOUND in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        bd91e45d-691a-4d7e-9917-7b6231c05c43
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 115, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL...
issueNumber                                                                           101
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/101
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7da5...
term_iri                                https://rs.tdwg.org/bdqtest/terms/7da5428e-87b...
issued                                                                         2025-03-06
term_localName                                       7da5428e-87b2-4ec2-be82-05b9398b7577
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:scientif...
SpecificationGuid                           urn:uuid:d92c5e23-bf6a-483b-86c3-9374e12d01c7
MethodGuid                                  urn:uuid:94510668-a59f-41d3-84bb-30cd9715cb62
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_POLYNOMIAL_CONS...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation NAME CODED Test Consistency CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 189, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFIC...
issueNumber                                                                           244
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/244
iri                                     https://rs.tdwg.org/bdqtest/terms/version/dbf3...
term_iri                                https://rs.tdwg.org/bdqtest/terms/dbf3cece-1d8...
issued                                                                         2025-03-06
term_localName                                       dbf3cece-1d83-426e-a5e0-8158fcf9c0cd
DateLastUpdated                                                                2024-02-04
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMP...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:scientificNameAuthorship is b...
SpecificationGuid                           urn:uuid:e9ffc3b0-0fb8-4a7c-a588-a00085ba980b
MethodGuid                                  urn:uuid:f6c58791-279d-458b-b4ee-058a73a002ee
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_SCIENTIFICNAMEA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 241, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFIC...
issueNumber                                                                           212
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/212
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f174...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f174ad13-3c6...
issued                                                                         2025-03-06
term_localName                                       f174ad13-3c67-49f9-8d8b-aba4e933d6f6
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:scientif...
SpecificationGuid                           urn:uuid:e6c02558-8541-4292-9a11-2f4408d69699
MethodGuid                                  urn:uuid:f2f40350-4081-4402-8b2b-95f9ad8893a7
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_SCIENTIFICNAMEI...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 237, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFIC...
issueNumber                                                                           120
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/120
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a996...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a9962d33-ad0...
issued                                                                         2025-03-06
term_localName                                       a9962d33-ad08-453a-8938-2972425034c2
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:scientificNameID is bdq:NotEm...
SpecificationGuid                           urn:uuid:02242018-3e73-4e0a-8d6f-d1db06cf81a3
MethodGuid                                  urn:uuid:b1b04dc2-e74b-43f3-9f48-60ac08afcadb
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_SCIENTIFICNAMEI...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 211, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFIC...
issueNumber                                                                            46
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/46
iri                                     https://rs.tdwg.org/bdqtest/terms/version/4e70...
term_iri                                https://rs.tdwg.org/bdqtest/terms/4e70b0e4-3fd...
issued                                                                         2025-03-06
term_localName                                       4e70b0e4-3fd2-4899-802c-439671374eeb
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                 bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:3c2fe7e9-186f-4ceb-8274-8bbcb4a62de4
MethodGuid                                  urn:uuid:275ae9b2-4085-4946-9580-6a63844174cd
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_SCIENTIFICNAME_...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                        d9dc26f7-6c4e-4647-addc-20197ce50d2b
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 135, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFIC...
issueNumber                                                                            82
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/82
iri                                     https://rs.tdwg.org/bdqtest/terms/version/0f8b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/0f8b30e2-59d...
issued                                                                         2025-03-06
term_localName                                       0f8b30e2-59dc-46ba-8b91-62049cd1a4e2
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon              bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:scientificName is bdq:NotEmpt...
SpecificationGuid                           urn:uuid:a9c18563-f63e-42db-98e5-a3e6079086b7
MethodGuid                                  urn:uuid:74259ddf-188c-4e6f-96f2-9ed3a8adfbf7
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_SCIENTIFICNAME_...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 171, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD
issueNumber                                                                           283
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/283
iri                                     https://rs.tdwg.org/bdqtest/terms/version/e4d3...
term_iri                                https://rs.tdwg.org/bdqtest/terms/e4d35063-236...
issued                                                                         2025-03-07
term_localName                                       e4d35063-2366-4dda-8eaa-326340361da3
DateLastUpdated                                                                2024-02-09
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                         bdq:VALIDATION_SEX_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:72471db4-226c-454f-bbe8-5c1718e6c834
MethodGuid                                  urn:uuid:a0c48217-97a2-41e2-9540-61939f2628c5
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Sex Vocabu...
Description                             Count the number of VALIDATION_SEX_STANDARD in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Par...
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                        2964d61f-eab0-4a21-9ac6-3f6a7c4fbf86
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 251, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOF...
issueNumber                                                                           130
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/130
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7600...
term_iri                                https://rs.tdwg.org/bdqtest/terms/76008c6b-c56...
issued                                                                         2025-03-06
term_localName                                       76008c6b-c56a-4233-84e3-8584950037ec
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon               bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:startDay...
SpecificationGuid                           urn:uuid:53c6af68-6120-4da6-87d8-a3e9551b9671
MethodGuid                                  urn:uuid:c3d0ce9b-2f40-4cd7-8e67-085b137e8e89
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_STARTDAYOFYEAR_...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 221, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVI...
issueNumber                                                                           199
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/199
iri                                     https://rs.tdwg.org/bdqtest/terms/version/58fd...
term_iri                                https://rs.tdwg.org/bdqtest/terms/58fdd5c1-620...
issued                                                                         2025-03-07
term_localName                                       58fdd5c1-6201-49a1-a7cd-f49c210dc0b6
DateLastUpdated                                                                2024-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                  bdq:VALIDATION_STATEPROVINCE_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:d261fac1-ce61-4879-bc04-870fa885b578
MethodGuid                                  urn:uuid:eebb4a3c-30e8-43e5-96f5-eded890dd174
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Count the number of VALIDATION_STATEPROVINCE_F...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                        41461142-2c1e-4fc1-bc97-f83a7b2a893d
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 233, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_...
issueNumber                                                                           161
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/161
iri                                     https://rs.tdwg.org/bdqtest/terms/version/de66...
term_iri                                https://rs.tdwg.org/bdqtest/terms/de661615-b33...
issued                                                                         2025-03-06
term_localName                                       de661615-b338-4557-af5b-d44a89de40fa
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                   bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:taxonRank is bdq:NotEmpty; ot...
SpecificationGuid                           urn:uuid:c619ec9b-92ec-4047-a8d3-931e3324bf3e
MethodGuid                                  urn:uuid:dbb803cb-8b37-4db3-a562-b4f6036f9d17
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_TAXONRANK_NOTEM...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 227, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_...
issueNumber                                                                           162
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/162
iri                                     https://rs.tdwg.org/bdqtest/terms/version/602b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/602bc457-6b1...
issued                                                                         2025-03-06
term_localName                                       602bc457-6b1d-4f24-adef-d0d31bcdf2f0
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                   bdq:VALIDATION_TAXONRANK_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:c8964200-630e-47c6-baad-7e334fddbbdb
MethodGuid                                  urn:uuid:e95df0f4-b6b6-4e04-ad00-95eef6e8d993
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF TaxonRank ...
Description                             Count the number of VALIDATION_TAXONRANK_STAND...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        da536dda-d467-450e-8b0a-6b6903fd1a1b
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 229, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTE...
issueNumber                                                                           105
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/105
iri                                     https://rs.tdwg.org/bdqtest/terms/version/54d2...
term_iri                                https://rs.tdwg.org/bdqtest/terms/54d290e8-ac4...
issued                                                                         2025-03-06
term_localName                                       54d290e8-ac48-4f31-8af3-676363573217
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                       bdq:VALIDATION_TAXON_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if at least one term needed to deter...
SpecificationGuid                           urn:uuid:f38e3644-354d-4180-bc7c-c437cef1d606
MethodGuid                                  urn:uuid:9c5798cd-6176-41ed-8e91-35e3df1fa6d4
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_TAXON_NOTEMPTY ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 195, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAM...
issueNumber                                                                            70
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/70
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7827...
term_iri                                https://rs.tdwg.org/bdqtest/terms/782773c9-7b3...
issued                                                                         2025-03-06
term_localName                                       782773c9-7b37-483d-8ce2-c6683ba81882
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                    bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:8bd6f6de-49e4-4889-82e0-e4af093981e0
MethodGuid                                  urn:uuid:55b60dd8-7054-4736-b9ac-88bef8967fb2
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Count the number of VALIDATION_TAXON_UNAMBIGUO...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                        1f9a778a-7949-4574-8826-55de1e4c1e32
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 159, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS...
issueNumber                                                                           285
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/285
iri                                     https://rs.tdwg.org/bdqtest/terms/version/b5a1...
term_iri                                https://rs.tdwg.org/bdqtest/terms/b5a14d76-292...
issued                                                                         2025-03-07
term_localName                                       b5a14d76-292e-499b-b80f-9546243311a0
DateLastUpdated                                                                2024-11-11
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                  bdq:VALIDATION_TYPESTATUS_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:e4dbf38d-bdd7-4cf7-8c60-5b3bfc6af4ff
MethodGuid                                  urn:uuid:f84d0f30-9c93-43a4-8f75-8c853fc18fb5
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF TypeStatus...
Description                             Count the number of VALIDATION_TYPESTATUS_STAN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        63b0193f-a8df-4345-8d60-caf667cd62b0
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 253, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE
issueNumber                                                                            84
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/84
iri                                     https://rs.tdwg.org/bdqtest/terms/version/aee6...
term_iri                                https://rs.tdwg.org/bdqtest/terms/aee65eb8-8d1...
issued                                                                         2025-03-06
term_localName                                       aee65eb8-8d1e-4b8f-bd37-5822e29f5734
DateLastUpdated                                                                2024-08-23
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                         bdq:VALIDATION_YEAR_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:year is ...
SpecificationGuid                           urn:uuid:aee43366-0352-448a-a5ea-85ddc8605da1
MethodGuid                                  urn:uuid:7922ab56-6eae-4257-9691-d55d24842274
AuthoritiesDefaults                     bdq:earliestValidDate default = "1582",bdq:lat...
Description                             Count the number of VALIDATION_YEAR_INRANGE in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance Par...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                           9167035f-14a8-4a0f-81eb-86a5a93bf6d9,fa6e83af-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 175, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY
issueNumber                                                                            49
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/49
iri                                     https://rs.tdwg.org/bdqtest/terms/version/687d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/687d3ad1-93a...
issued                                                                         2025-03-06
term_localName                                       687d3ad1-93a3-4a1f-b69f-da5a1eb761a5
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord Counting Complian...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                        bdq:VALIDATION_YEAR_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:year is bdq:NotEmpty; otherwi...
SpecificationGuid                           urn:uuid:42f331f4-a5a8-48b4-a08e-57048d1d1a77
MethodGuid                                  urn:uuid:2a0843de-32f9-473e-984a-619dace9ee66
AuthoritiesDefaults                                                                   NaN
Description                             Count the number of VALIDATION_YEAR_NOTEMPTY i...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Control, compare the Response.resu...
IssueState                                                                           open
IssueLabels                              TG2 Validation TIME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 139, dtype: object
Row:
Label                                       MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY
issueNumber                                                                            58
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/58
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c8c6...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c8c61535-ab1...
issued                                                                         2025-03-07
term_localName                                       c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                     Record-level
InformationElement:ActedUpon               bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:basisOfRecord is bdq:NotEmpty...
SpecificationGuid                           urn:uuid:5aabe3d4-d2c0-415c-8972-c834b543971a
MethodGuid                                  urn:uuid:31c40ce6-eecd-4304-bda7-0234993b079d
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_BASISOFRECORD_NOTEMP...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 146, dtype: object
Row:
Label                                       MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD
issueNumber                                                                           104
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/104
iri                                     https://rs.tdwg.org/bdqtest/terms/version/241a...
term_iri                                https://rs.tdwg.org/bdqtest/terms/241a279c-76d...
issued                                                                         2025-03-07
term_localName                                       241a279c-76d5-499b-ab49-a47ad7f8df50
DateLastUpdated                                                                2024-08-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                     Record-level
InformationElement:ActedUpon               bdq:VALIDATION_BASISOFRECORD_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:f094b94f-09b6-4fb0-8ba4-24252a2101c4
MethodGuid                                  urn:uuid:99103239-1019-4d2e-b435-ecb28c190a3c
AuthoritiesDefaults                     bdq:sourceAuthority default = "Darwin Core bas...
Description                             Measure if all VALIDATION_BASISOFRECORD_STANDA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                        a723528a-ee73-44a7-818d-5315323ec4e9
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 192, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT
issueNumber                                                                           123
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/123
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a2be...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a2be4734-0a9...
issued                                                                         2025-03-06
term_localName                                       a2be4734-0a93-46dc-af4a-e2125b47dbd4
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:21d0b5f6-5b3e-4810-8413-c975b7cf343a
MethodGuid                                  urn:uuid:b751c2ed-11a5-4bff-9c37-1eccc8138191
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_CLASSIFICATION_CONSI...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Cons...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        d6bc8db2-014b-47dc-9737-b0ecd98bf5bb
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 214, dtype: object
Row:
Label                                                  MULTIRECORD_MEASURE_QA_CLASS_FOUND
issueNumber                                                                            77
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/77
iri                                     https://rs.tdwg.org/bdqtest/terms/version/2154...
term_iri                                https://rs.tdwg.org/bdqtest/terms/21541436-641...
issued                                                                         2025-03-06
term_localName                                       21541436-641d-45a9-938c-537484d94eb7
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                          bdq:VALIDATION_CLASS_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:a2b39526-d08a-4a91-8b6d-aacf73677789
MethodGuid                                  urn:uuid:6d096b24-0eb1-4e6e-804f-6810e781d16f
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_CLASS_FOUND in a rec...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        cd12d17c-8404-40fa-bc15-5583564ddd14
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 162, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_...
issueNumber                                                                            50
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/50
iri                                     https://rs.tdwg.org/bdqtest/terms/version/86c2...
term_iri                                https://rs.tdwg.org/bdqtest/terms/86c28d5e-f77...
issued                                                                         2025-03-07
term_localName                                       86c28d5e-f778-4230-88d8-64cc01478601
DateLastUpdated                                                                2024-08-30
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTE...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:4343a7e0-7f0b-434d-99d4-e939ecb16e1f
MethodGuid                                  urn:uuid:2afcbce1-7cf8-4c5c-9df4-d267dc2df704
AuthoritiesDefaults                     bdq:sourceAuthority default = "10m-admin-1 bou...
Description                             Measure if all VALIDATION_COORDINATESCOUNTRYCO...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                                    bdq:Spatial-Temporal_Patterns
ArgumentGuids                           8a3f5702-a4e5-4b21-acb6-a4eae9a1ae09,972320cd-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 140, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINC...
issueNumber                                                                            56
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/56
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7a8b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/7a8b0af3-fa7...
issued                                                                         2025-03-07
term_localName                                       7a8b0af3-fa7d-416a-921a-8992d56f8233
DateLastUpdated                                                                2024-08-30
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSIS...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:4dd617df-a984-419f-b7b5-098b2023c4ab
MethodGuid                                  urn:uuid:315a198d-3811-40dd-918a-756f598f3294
AuthoritiesDefaults                     bdq:sourceAuthority default = "10m-admin-1 bou...
Description                             Measure if all VALIDATION_COORDINATESSTATEPROV...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           b7c56646-56f1-4094-b2be-8546c7e18102,cceaf335-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 144, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALM...
issueNumber                                                                            51
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/51
iri                                     https://rs.tdwg.org/bdqtest/terms/version/478d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/478dee00-98d...
issued                                                                         2025-03-07
term_localName                                       478dee00-98d0-4154-b66c-eca64dbbf86d
DateLastUpdated                                                                2024-08-30
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CO...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if either bdq:t...
SpecificationGuid                           urn:uuid:45cb9e13-7944-4535-a5ef-f6ededb77305
MethodGuid                                  urn:uuid:2bb364f7-118b-4258-8afe-978901e5cf67
AuthoritiesDefaults                     bdq:taxonIsMarine default = "World Register of...
Description                             Measure if all VALIDATION_COORDINATESTERRESTRI...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           3968f8d0-7364-4f3d-9993-96b8678f1653,cbb3483c-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 142, dtype: object
Row:
Label                                          MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO
issueNumber                                                                            87
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/87
iri                                     https://rs.tdwg.org/bdqtest/terms/version/151b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/151b2d29-346...
issued                                                                         2025-03-07
term_localName                                       151b2d29-3460-4ba5-a226-86971dc8ad03
DateLastUpdated                                                                2023-06-20
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                  bdq:VALIDATION_COORDINATES_NOTZERO.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalL...
SpecificationGuid                           urn:uuid:b482148e-9ac2-47ad-99b5-462508e9f360
MethodGuid                                  urn:uuid:8454615d-9cd4-49af-8fd3-c67e6be9c777
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_COORDINATES_NOTZERO ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                      Likeliness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation SPACE CODED Test Likeliness CORE
UseCases                                                    bdq:Spatial-Temporal_Patterns
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 176, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_I...
issueNumber                                                                           109
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/109
iri                                     https://rs.tdwg.org/bdqtest/terms/version/d94b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/d94b0130-7a1...
issued                                                                         2025-03-07
term_localName                                       d94b0130-7a13-4fa8-955c-eff5c47bd9de
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.R...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:coordina...
SpecificationGuid                           urn:uuid:f8dfc3fc-6580-4518-b2b4-595c29e9042e
MethodGuid                                  urn:uuid:a5bbeae3-9dc8-4a0c-9f68-58526e5d6a76
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_COORDINATEUNCERTAINT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 200, dtype: object
Row:
Label                                         MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY
issueNumber                                                                            98
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/98
iri                                     https://rs.tdwg.org/bdqtest/terms/version/942f...
term_iri                                https://rs.tdwg.org/bdqtest/terms/942f63bd-d19...
issued                                                                         2025-03-07
term_localName                                       942f63bd-d19d-4214-bf8e-cec0055b8909
DateLastUpdated                                                                2024-11-10
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:countryCode is bdq:NotEmpty; ...
SpecificationGuid                           urn:uuid:d153d4bd-b39d-43b0-b00a-395ff3e2ca62
MethodGuid                                  urn:uuid:930eb72e-fe83-48ae-9698-ca46713721a3
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_COUNTRYCODE_NOTEMPTY...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Com...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 184, dtype: object
Row:
Label                                         MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD
issueNumber                                                                            20
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/20
iri                                     https://rs.tdwg.org/bdqtest/terms/version/fedf...
term_iri                                https://rs.tdwg.org/bdqtest/terms/fedf27b2-e01...
issued                                                                         2025-03-07
term_localName                                       fedf27b2-e01d-459f-98fc-7f0f39e3d4be
DateLastUpdated                                                                2024-09-19
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_COUNTRYCODE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:01b96157-e4a1-4884-95d7-3bcfc5f3c047
MethodGuid                                  urn:uuid:02f5a440-a473-42cf-a3f1-6c10334d5eb8
AuthoritiesDefaults                     bdq:sourceAuthority default = "ISO 3166 Countr...
Description                             Measure if all VALIDATION_COUNTRYCODE_STANDARD...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 110, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONS...
issueNumber                                                                            62
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/62
iri                                     https://rs.tdwg.org/bdqtest/terms/version/57b4...
term_iri                                https://rs.tdwg.org/bdqtest/terms/57b40d9a-67d...
issued                                                                         2025-03-07
term_localName                                       57b40d9a-67d7-4916-9c27-dbb395c6c27e
DateLastUpdated                                                                2024-09-25
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.R...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:6f1093a0-0da5-4691-a95e-184d6d55eeb0
MethodGuid                                  urn:uuid:3925c15a-2795-4cef-8a30-6e6e5e480eae
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Measure if all VALIDATION_COUNTRYCOUNTRYCODE_C...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 150, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UN...
issueNumber                                                                           201
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/201
iri                                     https://rs.tdwg.org/bdqtest/terms/version/23ac...
term_iri                                https://rs.tdwg.org/bdqtest/terms/23aced89-d61...
issued                                                                         2025-03-07
term_localName                                       23aced89-d613-479c-bc4c-837d74b73be0
DateLastUpdated                                                                2024-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOU...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:e5efdd20-d1fc-4287-91f9-15b9ce3f3aac
MethodGuid                                  urn:uuid:f1a7f272-9040-42da-9b64-62abedefb1b0
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Measure if all VALIDATION_COUNTRYSTATEPROVINCE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                        aabaaac7-b26c-478e-9f04-3e2fbdba4a96
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 234, dtype: object
Row:
Label                                                MULTIRECORD_MEASURE_QA_COUNTRY_FOUND
issueNumber                                                                            21
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/21
iri                                     https://rs.tdwg.org/bdqtest/terms/version/388e...
term_iri                                https://rs.tdwg.org/bdqtest/terms/388e74b3-2e1...
issued                                                                         2025-03-07
term_localName                                       388e74b3-2e18-4d78-8112-3142d1177e25
DateLastUpdated                                                                2024-08-19
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                        bdq:VALIDATION_COUNTRY_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:051f6ad7-1a4b-4e6c-8a1d-2af76de24848
MethodGuid                                  urn:uuid:04cee4e0-0c83-40cc-8de2-e7391f0a97a9
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Measure if all VALIDATION_COUNTRY_FOUND in a r...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                        3e00109a-13d3-416d-9a91-127c99b47473
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 112, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY
issueNumber                                                                            42
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/42
iri                                     https://rs.tdwg.org/bdqtest/terms/version/9c8d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/9c8df974-8fb...
issued                                                                         2025-03-07
term_localName                                       9c8df974-8fba-4537-8c67-31466787f732
DateLastUpdated                                                                2024-09-27
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                     bdq:VALIDATION_COUNTRY_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:country is bdq:NotEmpty or dw...
SpecificationGuid                           urn:uuid:34ef6ea2-de06-4d2c-88fe-2c779de8f7db
MethodGuid                                  urn:uuid:23e9d641-1349-4998-bdff-117e32c30eff
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_COUNTRY_NOTEMPTY in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 132, dtype: object
Row:
Label                                       MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE
issueNumber                                                                            76
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/76
iri                                     https://rs.tdwg.org/bdqtest/terms/version/6354...
term_iri                                https://rs.tdwg.org/bdqtest/terms/6354376c-0cf...
issued                                                                         2025-03-07
term_localName                                       6354376c-0cf2-435b-be40-850769c5a18a
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                               dwc:Identification
InformationElement:ActedUpon               bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:date...
SpecificationGuid                           urn:uuid:a25786df-a624-4ff2-8962-6b23e8b07b0b
MethodGuid                                  urn:uuid:67ddf706-c8ee-4cf2-a9d0-d161fc6b7d69
AuthoritiesDefaults                     bdq:earliestValidDate default = "1753-01-01",b...
Description                             Measure if all VALIDATION_DATEIDENTIFIED_INRAN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                      Likeliness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Likeliness ISO/...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           13c17157-1714-4f67-848b-9dc031917fee,030797c0-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 160, dtype: object
Row:
Label                                      MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD
issueNumber                                                                            69
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/69
iri                                     https://rs.tdwg.org/bdqtest/terms/version/5638...
term_iri                                https://rs.tdwg.org/bdqtest/terms/563872eb-f54...
issued                                                                         2025-03-07
term_localName                                       563872eb-f544-45a0-8f91-8098d62768d4
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                               dwc:Identification
InformationElement:ActedUpon              bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIden...
SpecificationGuid                           urn:uuid:89f8b2ea-fc35-4941-929a-0e32cfbeb1a6
MethodGuid                                  urn:uuid:4c6a5522-ae8c-42d3-a396-8fc3aee49ef9
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DATEIDENTIFIED_STAND...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance ISO...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 156, dtype: object
Row:
Label                                                  MULTIRECORD_MEASURE_QA_DAY_INRANGE
issueNumber                                                                           125
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/125
iri                                     https://rs.tdwg.org/bdqtest/terms/version/85dc...
term_iri                                https://rs.tdwg.org/bdqtest/terms/85dc5d02-984...
issued                                                                         2025-03-06
term_localName                                       85dc5d02-9847-420f-a026-6a0e70962d2a
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                          bdq:VALIDATION_DAY_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:day ...
SpecificationGuid                           urn:uuid:2563ae15-a5bf-48fc-91f3-6df869aece2d
MethodGuid                                  urn:uuid:bb12babf-ca13-4289-9a3d-dde52bb8aff8
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DAY_INRANGE in a rec...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 216, dtype: object
Row:
Label                                                 MULTIRECORD_MEASURE_QA_DAY_STANDARD
issueNumber                                                                           147
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/147
iri                                     https://rs.tdwg.org/bdqtest/terms/version/3710...
term_iri                                https://rs.tdwg.org/bdqtest/terms/371035f6-42b...
issued                                                                         2025-03-06
term_localName                                       371035f6-42b5-494f-86d9-de2f44a6cdc6
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                         bdq:VALIDATION_DAY_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:day is b...
SpecificationGuid                           urn:uuid:c0fce1a1-8879-4175-8a71-ce037655c358
MethodGuid                                  urn:uuid:d9bfd4f7-e158-43ee-8ac4-1bc51bf33307
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DAY_STANDARD in a re...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 224, dtype: object
Row:
Label                                              MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY
issueNumber                                                                           103
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/103
iri                                     https://rs.tdwg.org/bdqtest/terms/version/4d99...
term_iri                                https://rs.tdwg.org/bdqtest/terms/4d999a65-a43...
issued                                                                         2025-03-07
term_localName                                       4d999a65-a431-4a76-b591-e0d86dcf244b
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                     Record-level
InformationElement:ActedUpon                      bdq:VALIDATION_DCTYPE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dc:type is bdq:NotEmpty; otherwis...
SpecificationGuid                           urn:uuid:e1286c46-2a95-480d-89e4-f02681372eb7
MethodGuid                                  urn:uuid:95c2e363-5a99-4276-937d-98008ca893f9
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DCTYPE_NOTEMPTY in a...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 190, dtype: object
Row:
Label                                              MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD
issueNumber                                                                            91
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/91
iri                                     https://rs.tdwg.org/bdqtest/terms/version/d949...
term_iri                                https://rs.tdwg.org/bdqtest/terms/d9493fa0-d90...
issued                                                                         2025-03-07
term_localName                                       d9493fa0-d90e-41db-95f6-d1c1d243540e
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                     Record-level
InformationElement:ActedUpon                      bdq:VALIDATION_DCTYPE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:b85129f0-28c2-4ede-aff2-5ce3791c6e86
MethodGuid                                  urn:uuid:8b06bef9-7fd4-4020-b08c-a07a1bf695b6
AuthoritiesDefaults                     DCMI Type Vocabulary" {[http://purl.org/dc/ter...
Description                             Measure if all VALIDATION_DCTYPE_STANDARD in a...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 180, dtype: object
Row:
Label                                      MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE
issueNumber                                                                            79
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/79
iri                                     https://rs.tdwg.org/bdqtest/terms/version/3c8b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/3c8bc478-f6b...
issued                                                                         2025-03-07
term_localName                                       3c8bc478-f6b2-4533-b7ce-45bae5d186c2
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon              bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalL...
SpecificationGuid                           urn:uuid:a5111c0c-d198-4ecc-af10-809ae2b3ae01
MethodGuid                                  urn:uuid:6f3a7ebb-e857-42e0-8051-4d06feeb4ab2
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DECIMALLATITUDE_INRA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 166, dtype: object
Row:
Label                                     MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY
issueNumber                                                                           119
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/119
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a253...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a2535b23-440...
issued                                                                         2025-03-07
term_localName                                       a2535b23-4407-40bd-b23b-30c8185d72a2
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon             bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:decimalLatitude is bdq:NotEmp...
SpecificationGuid                           urn:uuid:0067fa60-5503-490e-8c94-93fb79cc7da2
MethodGuid                                  urn:uuid:b12c8663-25e8-4c8a-abfc-edf4334d1aef
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DECIMALLATITUDE_NOTE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 208, dtype: object
Row:
Label                                     MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE
issueNumber                                                                            30
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/30
iri                                     https://rs.tdwg.org/bdqtest/terms/version/6f7a...
term_iri                                https://rs.tdwg.org/bdqtest/terms/6f7a9b82-7d3...
issued                                                                         2025-03-07
term_localName                                       6f7a9b82-7d34-4111-a2a6-9efe5221fa44
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon             bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalL...
SpecificationGuid                           urn:uuid:1a504f7f-21a7-49e1-a0dc-f51146957fa4
MethodGuid                                  urn:uuid:0ff56b48-f00e-45bd-822e-e04afbcef3e1
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DECIMALLONGITUDE_INR...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 120, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY
issueNumber                                                                            96
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/96
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a94e...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a94e986e-dbc...
issued                                                                         2025-03-07
term_localName                                       a94e986e-dbc8-4147-872d-5f2727945654
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:decimalLongitude is bdq:NotEm...
SpecificationGuid                           urn:uuid:c893ee17-ee8b-43ec-bf17-97ac814ea502
MethodGuid                                  urn:uuid:908fc823-75a9-437e-be7c-5c72cd6b149e
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_DECIMALLONGITUDE_NOT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 182, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_S...
issueNumber                                                                           275
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/275
iri                                     https://rs.tdwg.org/bdqtest/terms/version/ba95...
term_iri                                https://rs.tdwg.org/bdqtest/terms/ba953672-652...
issued                                                                         2025-03-07
term_localName                                       ba953672-6526-4375-97e8-b4e9d1a7d3a0
DateLastUpdated                                                                2024-02-09
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD....
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:fec2103b-5d46-4723-b2ec-8c8119b44aaf
MethodGuid                                  urn:uuid:fd15e0a4-f49d-4566-b700-a9b46c284e68
AuthoritiesDefaults                     bdq:sourceAuthority default = "Degree of Estab...
Description                             Measure if all VALIDATION_DEGREEOFESTABLISHMEN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                                                bdq:Alien-Species
ArgumentGuids                                        8aac7359-311a-405f-8117-79bb4873011d
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 246, dtype: object
Row:
Label                                         MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE
issueNumber                                                                           131
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/131
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c04d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c04d428a-13d...
issued                                                                         2025-03-06
term_localName                                       c04d428a-13d0-4766-9df7-4dfb2ef5d5d8
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                 bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOf...
SpecificationGuid                           urn:uuid:62f754b5-a0a1-4b24-9982-b76e4e169f71
MethodGuid                                  urn:uuid:ca1bc131-fa85-4fdf-902d-ad20bd4ba0f4
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_ENDDAYOFYEAR_INRANGE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 222, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STAN...
issueNumber                                                                           268
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/268
iri                                     https://rs.tdwg.org/bdqtest/terms/version/8dfe...
term_iri                                https://rs.tdwg.org/bdqtest/terms/8dfed701-01a...
issued                                                                         2025-03-07
term_localName                                       8dfed701-01a9-415d-a9f8-539280b75975
DateLastUpdated                                                                2024-02-08
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Res...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:f1d3bf9c-5558-41dc-8e33-b17c499be016
MethodGuid                                  urn:uuid:f89147ba-03e5-432b-8040-0a2a4921d676
AuthoritiesDefaults                     bdq:sourceAuthority default = "Establishment M...
Description                             Measure if all VALIDATION_ESTABLISHMENTMEANS_S...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                        0c051c38-621f-4a52-ae92-5077afd46446
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 244, dtype: object
Row:
Label                                            MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE
issueNumber                                                                            36
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/36
iri                                     https://rs.tdwg.org/bdqtest/terms/version/d41a...
term_iri                                https://rs.tdwg.org/bdqtest/terms/d41a731b-2e2...
issued                                                                         2025-03-06
term_localName                                       d41a731b-2e2b-4442-9217-4c375ae92926
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                    bdq:VALIDATION_EVENTDATE_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDat...
SpecificationGuid                           urn:uuid:29a1fdc6-326b-4017-880d-d11ff0225b8f
MethodGuid                                  urn:uuid:17f89e32-0174-4bf9-805e-ba7aec59477b
AuthoritiesDefaults                     bdq:earliestValidDate default ="1582-11-15",bd...
Description                             Measure if all VALIDATION_EVENTDATE_INRANGE in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance Par...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           8b223050-f314-4601-9e20-d5f3d59d8e79,2e5c3e37-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 124, dtype: object
Row:
Label                                           MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY
issueNumber                                                                            33
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/33
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c23c...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c23cd67d-1b5...
issued                                                                         2025-03-07
term_localName                                       c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                   bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:eventDate is bdq:NotEmpty; ot...
SpecificationGuid                           urn:uuid:1fae3f77-7fcb-42c6-ab43-1ff28adf4fa4
MethodGuid                                  urn:uuid:12499336-882b-4186-b5a2-4a806af2e35b
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_EVENTDATE_NOTEMPTY i...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation TIME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 122, dtype: object
Row:
Label                                           MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD
issueNumber                                                                            66
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/66
iri                                     https://rs.tdwg.org/bdqtest/terms/version/14a1...
term_iri                                https://rs.tdwg.org/bdqtest/terms/14a1d51f-16e...
issued                                                                         2025-03-06
term_localName                                       14a1d51f-16ed-4148-9dc8-1e90157a9868
DateLastUpdated                                                                2024-09-16
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                   bdq:VALIDATION_EVENTDATE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDat...
SpecificationGuid                           urn:uuid:80c8f69b-4ad3-40ee-bccd-de016bfae367
MethodGuid                                  urn:uuid:3f868855-cc39-4a1b-8050-bfa246416a47
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_EVENTDATE_STANDARD i...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance ISO...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 152, dtype: object
Row:
Label                                       MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY
issueNumber                                                                            88
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/88
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f225...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f22539ef-029...
issued                                                                         2025-03-06
term_localName                                       f22539ef-029b-4edb-ad17-add4363f7395
DateLastUpdated                                                                2023-09-30
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon               bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if any of dwc:eventDate, dwc:year, d...
SpecificationGuid                           urn:uuid:b57460c4-16e1-4c1d-8a07-a53aee9e8922
MethodGuid                                  urn:uuid:87d34104-0a79-4f51-aeeb-1115ec56e237
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_EVENTTEMPORAL_NOTEMP...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation TIME CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 178, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT
issueNumber                                                                            67
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/67
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f375...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f375a3fd-4cf...
issued                                                                         2025-03-06
term_localName                                       f375a3fd-4cf5-4ef4-955e-d71762ede2d8
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                     bdq:VALIDATION_EVENT_CONSISTENT.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDat...
SpecificationGuid                           urn:uuid:83d057ea-a6f6-49e6-ac3c-0c418776a0e0
MethodGuid                                  urn:uuid:449f44fe-0fef-42ff-a446-d693653b55d4
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_EVENT_CONSISTENT in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Consistency CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 154, dtype: object
Row:
Label                                                 MULTIRECORD_MEASURE_QA_FAMILY_FOUND
issueNumber                                                                            28
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/28
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a07d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a07d7147-2db...
issued                                                                         2025-03-06
term_localName                                       a07d7147-2db8-48ce-81b8-e47595ad5f17
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                         bdq:VALIDATION_FAMILY_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:16f999d9-1cf5-4208-b2ca-1a93d6700085
MethodGuid                                  urn:uuid:0997d841-9db9-40a8-b6ec-5867e9091532
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_FAMILY_FOUND in a re...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        146784a4-b53c-4245-a813-c41896761279
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 118, dtype: object
Row:
Label                                                  MULTIRECORD_MEASURE_QA_GENUS_FOUND
issueNumber                                                                           122
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/122
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c5c8...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c5c8db83-3af...
issued                                                                         2025-03-06
term_localName                                       c5c8db83-3af0-4215-806f-e2f90574b138
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                          bdq:VALIDATION_GENUS_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:15bbda19-dd18-471a-a5c3-56c7e543012f
MethodGuid                                  urn:uuid:b6cb27ac-e9b8-4a0c-b986-3e34069d8449
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_GENUS_FOUND in a rec...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        6304e753-423d-4188-bba4-0301c1a01769
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 212, dtype: object
Row:
Label                                       MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY
issueNumber                                                                            78
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/78
iri                                     https://rs.tdwg.org/bdqtest/terms/version/488c...
term_iri                                https://rs.tdwg.org/bdqtest/terms/488c1dff-21e...
issued                                                                         2025-03-07
term_localName                                       488c1dff-21ec-4e68-a00a-7355505e180c
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon               bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:geodeticDatum is bdq:NotEmpty...
SpecificationGuid                           urn:uuid:a3c8b277-15fb-4ae8-afb1-e64fb6eb5241
MethodGuid                                  urn:uuid:6d1f3f11-98d9-4b26-a8e7-56fbc066c705
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_GEODETICDATUM_NOTEMP...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 164, dtype: object
Row:
Label                                       MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD
issueNumber                                                                            59
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/59
iri                                     https://rs.tdwg.org/bdqtest/terms/version/cb88...
term_iri                                https://rs.tdwg.org/bdqtest/terms/cb88b6d9-85b...
issued                                                                         2025-03-07
term_localName                                       cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e
DateLastUpdated                                                                2025-03-03
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon               bdq:VALIDATION_GEODETICDATUM_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:5cc05662-c029-4ba9-b32e-fb487ccba71c
MethodGuid                                  urn:uuid:344cb9f6-68e1-4d7c-a976-7edcd9f20935
AuthoritiesDefaults                     bdq:sourceAuthority = "EPSG" {[https://epsg.or...
Description                             Measure if all VALIDATION_GEODETICDATUM_STANDA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 148, dtype: object
Row:
Label                                                MULTIRECORD_MEASURE_QA_KINGDOM_FOUND
issueNumber                                                                            81
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/81
iri                                     https://rs.tdwg.org/bdqtest/terms/version/465d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/465d7ac1-d19...
issued                                                                         2025-03-06
term_localName                                       465d7ac1-d193-46c0-a302-56a9ef99215f
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                        bdq:VALIDATION_KINGDOM_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:a90e100a-3522-4742-aa73-3b98a35ab826
MethodGuid                                  urn:uuid:7072bf93-bffc-4d83-ad51-b351c6e53260
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_KINGDOM_FOUND in a r...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        a5055cb3-b1e5-4070-90df-f875b0d9ae8a
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 168, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY
issueNumber                                                                           216
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/216
iri                                     https://rs.tdwg.org/bdqtest/terms/version/3bc9...
term_iri                                https://rs.tdwg.org/bdqtest/terms/3bc9df8b-0f5...
issued                                                                         2025-03-06
term_localName                                       3bc9df8b-0f57-4157-9374-b56a99090b22
DateLastUpdated                                                                2024-01-28
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                     bdq:VALIDATION_KINGDOM_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:kingdom is bdq:NotEmpty; othe...
SpecificationGuid                           urn:uuid:e6f0a9ce-3e72-40fb-9fad-63cf5962f93e
MethodGuid                                  urn:uuid:f5bd0eee-4cdf-4455-876d-a46d92373a4e
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_KINGDOM_NOTEMPTY in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 238, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY
issueNumber                                                                            99
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/99
iri                                     https://rs.tdwg.org/bdqtest/terms/version/4fcc...
term_iri                                https://rs.tdwg.org/bdqtest/terms/4fccf163-933...
issued                                                                         2025-03-07
term_localName                                       4fccf163-9336-4f48-996c-57f5f66e72db
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                     Record-level
InformationElement:ActedUpon                     bdq:VALIDATION_LICENSE_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dcterms:license is bdq:NotEmpty; ...
SpecificationGuid                           urn:uuid:d8b450af-47e6-4f5c-8154-6d6acbe9efa5
MethodGuid                                  urn:uuid:940621f5-4f24-48de-8b36-256101ca4987
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_LICENSE_NOTEMPTY in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                                            bdq:Record-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 186, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_LICENSE_STANDARD
issueNumber                                                                            38
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/38
iri                                     https://rs.tdwg.org/bdqtest/terms/version/acd8...
term_iri                                https://rs.tdwg.org/bdqtest/terms/acd8d43e-7a2...
issued                                                                         2025-03-07
term_localName                                       acd8d43e-7a2a-4372-b887-fb53a9972dc9
DateLastUpdated                                                                2024-03-21
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                     Record-level
InformationElement:ActedUpon                     bdq:VALIDATION_LICENSE_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:2a9dbd16-d427-471e-8db5-c1de2b2cf030
MethodGuid                                  urn:uuid:180c1a90-94c3-48b5-a9fe-4223d6f2bd60
AuthoritiesDefaults                     bdq:sourceAuthority default = "Creative Common...
Description                             Measure if all VALIDATION_LICENSE_STANDARD in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                                            bdq:Record-Management
ArgumentGuids                                        7308bf21-2648-40d8-bb2c-3f36d2789552
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 126, dtype: object
Row:
Label                                            MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY
issueNumber                                                                            40
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/40
iri                                     https://rs.tdwg.org/bdqtest/terms/version/3b2e...
term_iri                                https://rs.tdwg.org/bdqtest/terms/3b2e4791-1a5...
issued                                                                         2025-03-07
term_localName                                       3b2e4791-1a5a-4087-9e8d-09c67cf8c816
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                    bdq:VALIDATION_LOCATION_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if at least one term needed to deter...
SpecificationGuid                           urn:uuid:30ed5e2d-ef30-4988-8dbb-12c119e94ac3
MethodGuid                                  urn:uuid:1f014694-573d-46e0-b38a-2acf71b32071
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_LOCATION_NOTEMPTY in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Completeness CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 130, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE
issueNumber                                                                           187
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/187
iri                                     https://rs.tdwg.org/bdqtest/terms/version/c73d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/c73d49d1-06e...
issued                                                                         2025-03-07
term_localName                                       c73d49d1-06e4-4272-8249-6a26e7f8abca
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                     bdq:VALIDATION_MAXDEPTH_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumD...
SpecificationGuid                           urn:uuid:cebc8ba0-ca02-4f1e-830e-ec693bc628e4
MethodGuid                                  urn:uuid:ed60f87e-7ab7-446a-8565-903dbe6408d2
AuthoritiesDefaults                     bdq:minimumValidDepthInMeters default="0",bdq:...
Description                             Measure if all VALIDATION_MAXDEPTH_INRANGE in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Conformance Pa...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           edf69c59-056d-4c8a-b1fb-647ea684eb18,f41be58e-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 230, dtype: object
Row:
Label                                         MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE
issueNumber                                                                           112
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/112
iri                                     https://rs.tdwg.org/bdqtest/terms/version/7c5a...
term_iri                                https://rs.tdwg.org/bdqtest/terms/7c5a6ba0-399...
issued                                                                         2025-03-07
term_localName                                       7c5a6ba0-399d-4570-878a-4a064e2406fe
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_MAXELEVATION_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumE...
SpecificationGuid                           urn:uuid:f9471802-a5f7-4f4e-9810-f3f4f43dad1a
MethodGuid                                  urn:uuid:a6035033-0779-4a75-99ea-f7112c1dde2b
AuthoritiesDefaults                     bdq:minimumValidElevationInMeters default = "-...
Description                             Measure if all VALIDATION_MAXELEVATION_INRANGE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Likeliness Par...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           3ab181c2-a3d8-4317-af4d-f88181e2773a,1766715d-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 202, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE
issueNumber                                                                           107
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/107
iri                                     https://rs.tdwg.org/bdqtest/terms/version/49d7...
term_iri                                https://rs.tdwg.org/bdqtest/terms/49d756a8-e65...
issued                                                                         2025-03-07
term_localName                                       49d756a8-e654-4267-a290-d1def5d2c5f9
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                     bdq:VALIDATION_MINDEPTH_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumD...
SpecificationGuid                           urn:uuid:f3e03531-7ee5-4721-aae2-f554389e0544
MethodGuid                                  urn:uuid:9cc301b1-e303-4abb-9d24-d31506de9436
AuthoritiesDefaults                     bdq:minimumValidDepthInMeters default="0",bdq:...
Description                             Measure if all VALIDATION_MINDEPTH_INRANGE in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Conformance Pa...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           d23e61b3-07b6-4326-bac2-1457b030efef,9f12e2c3-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 196, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH
issueNumber                                                                            24
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/24
iri                                     https://rs.tdwg.org/bdqtest/terms/version/fcab...
term_iri                                https://rs.tdwg.org/bdqtest/terms/fcabd2c9-392...
issued                                                                         2025-03-07
term_localName                                       fcabd2c9-392c-4841-a5d7-e2680c9587ab
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Resp...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumD...
SpecificationGuid                           urn:uuid:12f7f82e-ab1c-4690-92b8-ecc9328256c1
MethodGuid                                  urn:uuid:07e4c491-0d13-409d-b966-fbb9721e81cf
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_MINDEPTH_LESSTHAN_MA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 116, dtype: object
Row:
Label                                         MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE
issueNumber                                                                            39
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/39
iri                                     https://rs.tdwg.org/bdqtest/terms/version/1ba1...
term_iri                                https://rs.tdwg.org/bdqtest/terms/1ba18c8b-66a...
issued                                                                         2025-03-07
term_localName                                       1ba18c8b-66a6-47d9-a709-404439332dba
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                 bdq:VALIDATION_MINELEVATION_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumE...
SpecificationGuid                           urn:uuid:2bb79221-0312-410a-aef6-f569485df6a6
MethodGuid                                  urn:uuid:1aa9c50e-7e8a-445f-9cf3-12af51a9ec10
AuthoritiesDefaults                     bdq:minimumValidElevationInMeters default = "-...
Description                             Measure if all VALIDATION_MINELEVATION_INRANGE...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test Conformance Pa...
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                           6e07e4fe-ce7a-4e5f-9fa3-c26877b273a7,307b78fe-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 128, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_M...
issueNumber                                                                           108
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/108
iri                                     https://rs.tdwg.org/bdqtest/terms/version/44f0...
term_iri                                https://rs.tdwg.org/bdqtest/terms/44f00697-ca6...
issued                                                                         2025-03-07
term_localName                                       44f00697-ca66-43cf-8f16-646b40c0f514
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon            bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVAT...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:maximuml...
SpecificationGuid                           urn:uuid:f799fb5c-37e4-46d7-a07e-87eb071df9c6
MethodGuid                                  urn:uuid:a0486e4f-210d-4143-ae5a-f320bebc2cb5
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_MINELEVATION_LESSTHA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation SPACE CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 198, dtype: object
Row:
Label                                               MULTIRECORD_MEASURE_QA_MONTH_STANDARD
issueNumber                                                                           126
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/126
iri                                     https://rs.tdwg.org/bdqtest/terms/version/b3c2...
term_iri                                https://rs.tdwg.org/bdqtest/terms/b3c2bb86-e23...
issued                                                                         2025-03-06
term_localName                                       b3c2bb86-e239-4532-ae0c-b121ec1ee025
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                       bdq:VALIDATION_MONTH_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:month is...
SpecificationGuid                           urn:uuid:2c5dbdbb-feab-474c-bcca-bf6d1b90ae66
MethodGuid                                  urn:uuid:bb630881-2a79-4750-ae0f-36d0df2191f7
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_MONTH_STANDARD in a ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Spatial-Temporal_Patterns, bdq:Record-Mana...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 218, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOT...
issueNumber                                                                           259
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/259
iri                                     https://rs.tdwg.org/bdqtest/terms/version/1605...
term_iri                                https://rs.tdwg.org/bdqtest/terms/16059801-6ad...
issued                                                                         2025-03-06
term_localName                                       16059801-6adb-4e65-82f4-61eaa70d8df0
DateLastUpdated                                                                2024-02-07
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Re...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:namePublishedInYear is bdq:No...
SpecificationGuid                           urn:uuid:f09fc9ad-a449-4422-b32f-63d8ccf2501f
MethodGuid                                  urn:uuid:f8024a02-76c0-482a-b805-097d0cdc82e2
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_NAMEPUBLISHEDINYEAR_...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 242, dtype: object
Row:
Label                                        MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY
issueNumber                                                                            47
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/47
iri                                     https://rs.tdwg.org/bdqtest/terms/version/0028...
term_iri                                https://rs.tdwg.org/bdqtest/terms/0028ef9a-655...
issued                                                                         2025-03-07
term_localName                                       0028ef9a-6553-467b-a344-90327ed2babf
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:occurrenceID is bdq:NotEmpty;...
SpecificationGuid                           urn:uuid:3d9e1339-19d7-47e7-af9e-11905df82b6a
MethodGuid                                  urn:uuid:296e08b2-c044-4cef-930e-8d29c579c8d6
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_OCCURRENCEID_NOTEMPT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                                            bdq:Record-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 136, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY
issueNumber                                                                           117
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/117
iri                                     https://rs.tdwg.org/bdqtest/terms/version/d292...
term_iri                                https://rs.tdwg.org/bdqtest/terms/d2922585-207...
issued                                                                         2025-03-07
term_localName                                       d2922585-2070-4851-a033-15e51977f9dc
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:occurrenceStatus is bdq:NotEm...
SpecificationGuid                           urn:uuid:c3a53898-c4ad-40e0-961b-b4ceafea37c7
MethodGuid                                  urn:uuid:af9591f4-d0ee-4301-bc59-d6a68d1d6813
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_OCCURRENCESTATUS_NOT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 206, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD
issueNumber                                                                           116
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/116
iri                                     https://rs.tdwg.org/bdqtest/terms/version/2fea...
term_iri                                https://rs.tdwg.org/bdqtest/terms/2fea4571-92d...
issued                                                                         2025-03-07
term_localName                                       2fea4571-92d0-48a5-a5ba-6caecd647862
DateLastUpdated                                                                2025-02-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon            bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:fbe854d4-acf3-4c79-a654-81441fed644f
MethodGuid                                  urn:uuid:acc05ff6-b1c8-4001-8aad-930a9b9ccaf8
AuthoritiesDefaults                     bdq:sourceAuthority default = "Regex present/a...
Description                             Measure if all VALIDATION_OCCURRENCESTATUS_STA...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 204, dtype: object
Row:
Label                                                  MULTIRECORD_MEASURE_QA_ORDER_FOUND
issueNumber                                                                            83
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/83
iri                                     https://rs.tdwg.org/bdqtest/terms/version/773b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/773bb288-fef...
issued                                                                         2025-03-06
term_localName                                       773bb288-fef3-4968-a65a-a69c74d6ecb5
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                          bdq:VALIDATION_ORDER_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:ae08b4b4-89ba-4972-b51f-912b132bd006
MethodGuid                                  urn:uuid:79096434-5b55-40e1-9afb-e138a11f82ba
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_ORDER_FOUND in a rec...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        c169404f-d797-40a1-9c84-3edb2383b759
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 172, dtype: object
Row:
Label                                             MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD
issueNumber                                                                           277
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/277
iri                                     https://rs.tdwg.org/bdqtest/terms/version/ef31...
term_iri                                https://rs.tdwg.org/bdqtest/terms/ef31ba02-cea...
issued                                                                         2025-03-07
term_localName                                       ef31ba02-cea7-4d76-990f-99ebbd201fb4
DateLastUpdated                                                                2024-02-09
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                     bdq:VALIDATION_PATHWAY_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:c7c92ef0-284e-4c5d-8fc9-f1480bfe0b8e
MethodGuid                                  urn:uuid:ffae8e47-2181-4a83-b1c7-d0a893e79b67
AuthoritiesDefaults                     bdq:sourceAuthority default = "Pathway Control...
Description                             Measure if all VALIDATION_PATHWAY_STANDARD in ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                        136039c5-6ceb-41ec-90b3-eb1cd37d6eed
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 248, dtype: object
Row:
Label                                                 MULTIRECORD_MEASURE_QA_PHYLUM_FOUND
issueNumber                                                                            22
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/22
iri                                     https://rs.tdwg.org/bdqtest/terms/version/1736...
term_iri                                https://rs.tdwg.org/bdqtest/terms/17364d16-37b...
issued                                                                         2025-03-06
term_localName                                       17364d16-37b7-4ccb-9614-bfb95ff1bca9
DateLastUpdated                                                                2022-03-25
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                         bdq:VALIDATION_PHYLUM_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:1193230f-f188-4917-92da-bba3390ed3fa
MethodGuid                                  urn:uuid:06f9faab-102a-452a-b6e0-4eafd8d7e71d
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_PHYLUM_FOUND in a re...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        bd91e45d-691a-4d7e-9917-7b6231c05c43
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 114, dtype: object
Row:
Label                                        MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT
issueNumber                                                                           101
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/101
iri                                     https://rs.tdwg.org/bdqtest/terms/version/ef05...
term_iri                                https://rs.tdwg.org/bdqtest/terms/ef05b45b-13b...
issued                                                                         2025-03-06
term_localName                                       ef05b45b-13b8-4877-9e9d-fa44b332d83c
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:scientif...
SpecificationGuid                           urn:uuid:d92c5e23-bf6a-483b-86c3-9374e12d01c7
MethodGuid                                  urn:uuid:94510668-a59f-41d3-84bb-30cd9715cb62
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_POLYNOMIAL_CONSISTEN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Consistency
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation NAME CODED Test Consistency CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 188, dtype: object
Row:
Label                                   MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHI...
issueNumber                                                                           244
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/244
iri                                     https://rs.tdwg.org/bdqtest/terms/version/6dd6...
term_iri                                https://rs.tdwg.org/bdqtest/terms/6dd6fecf-6ba...
issued                                                                         2025-03-06
term_localName                                       6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7
DateLastUpdated                                                                2024-02-04
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMP...
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:scientificNameAuthorship is b...
SpecificationGuid                           urn:uuid:e9ffc3b0-0fb8-4a7c-a588-a00085ba980b
MethodGuid                                  urn:uuid:f6c58791-279d-458b-b4ee-058a73a002ee
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_SCIENTIFICNAMEAUTHOR...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 240, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE
issueNumber                                                                           212
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/212
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a952...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a9529e71-547...
issued                                                                         2025-03-06
term_localName                                       a9529e71-5470-4cb1-b04d-aa483926f532
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:scientif...
SpecificationGuid                           urn:uuid:e6c02558-8541-4292-9a11-2f4408d69699
MethodGuid                                  urn:uuid:f2f40350-4081-4402-8b2b-95f9ad8893a7
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_SCIENTIFICNAMEID_COM...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 236, dtype: object
Row:
Label                                    MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY
issueNumber                                                                           120
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/120
iri                                     https://rs.tdwg.org/bdqtest/terms/version/4cf8...
term_iri                                https://rs.tdwg.org/bdqtest/terms/4cf84216-c8a...
issued                                                                         2025-03-06
term_localName                                       4cf84216-c8a7-4865-a8e1-3ffd829d5a10
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon            bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:scientificNameID is bdq:NotEm...
SpecificationGuid                           urn:uuid:02242018-3e73-4e0a-8d6f-d1db06cf81a3
MethodGuid                                  urn:uuid:b1b04dc2-e74b-43f3-9f48-60ac08afcadb
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_SCIENTIFICNAMEID_NOT...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 210, dtype: object
Row:
Label                                         MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND
issueNumber                                                                            46
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/46
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a8ae...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a8aee02c-cf7...
issued                                                                         2025-03-06
term_localName                                       a8aee02c-cf7c-4104-a601-d8afc4f9cbe2
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                 bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:3c2fe7e9-186f-4ceb-8274-8bbcb4a62de4
MethodGuid                                  urn:uuid:275ae9b2-4085-4946-9580-6a63844174cd
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_SCIENTIFICNAME_FOUND...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                        d9dc26f7-6c4e-4647-addc-20197ce50d2b
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 134, dtype: object
Row:
Label                                      MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY
issueNumber                                                                            82
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/82
iri                                     https://rs.tdwg.org/bdqtest/terms/version/b4d6...
term_iri                                https://rs.tdwg.org/bdqtest/terms/b4d6a61c-64f...
issued                                                                         2025-03-06
term_localName                                       b4d6a61c-64ff-4da0-974c-63a73fd20836
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon              bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:scientificName is bdq:NotEmpt...
SpecificationGuid                           urn:uuid:a9c18563-f63e-42db-98e5-a3e6079086b7
MethodGuid                                  urn:uuid:74259ddf-188c-4e6f-96f2-9ed3a8adfbf7
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_SCIENTIFICNAME_NOTEM...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 170, dtype: object
Row:
Label                                                 MULTIRECORD_MEASURE_QA_SEX_STANDARD
issueNumber                                                                           283
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/283
iri                                     https://rs.tdwg.org/bdqtest/terms/version/1b3b...
term_iri                                https://rs.tdwg.org/bdqtest/terms/1b3bbac4-7c0...
issued                                                                         2025-03-07
term_localName                                       1b3bbac4-7c00-46d6-8179-1d57c92374ad
DateLastUpdated                                                                2024-02-09
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                         bdq:VALIDATION_SEX_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:72471db4-226c-454f-bbe8-5c1718e6c834
MethodGuid                                  urn:uuid:a0c48217-97a2-41e2-9540-61939f2628c5
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Sex Vocabu...
Description                             Measure if all VALIDATION_SEX_STANDARD in a re...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Par...
UseCases                                bdq:Alien-Species, bdq:Record-Management, bdq:...
ArgumentGuids                                        2964d61f-eab0-4a21-9ac6-3f6a7c4fbf86
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 250, dtype: object
Row:
Label                                       MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE
issueNumber                                                                           130
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/130
iri                                     https://rs.tdwg.org/bdqtest/terms/version/8c21...
term_iri                                https://rs.tdwg.org/bdqtest/terms/8c217eee-9cd...
issued                                                                         2025-03-06
term_localName                                       8c217eee-9cd0-48c3-aea0-90151c6c5bfd
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon               bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:startDay...
SpecificationGuid                           urn:uuid:53c6af68-6120-4da6-87d8-a3e9551b9671
MethodGuid                                  urn:uuid:c3d0ce9b-2f40-4cd7-8e67-085b137e8e89
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_STARTDAYOFYEAR_INRAN...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                               TG2 Validation TIME CODED Test Conformance CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 220, dtype: object
Row:
Label                                          MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND
issueNumber                                                                           199
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/199
iri                                     https://rs.tdwg.org/bdqtest/terms/version/9c1c...
term_iri                                https://rs.tdwg.org/bdqtest/terms/9c1cdf6a-0db...
issued                                                                         2025-03-07
term_localName                                       9c1cdf6a-0dbf-4828-a2e3-fb368f74d194
DateLastUpdated                                                                2024-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                 dcterms:Location
InformationElement:ActedUpon                  bdq:VALIDATION_STATEPROVINCE_FOUND.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:d261fac1-ce61-4879-bc04-870fa885b578
MethodGuid                                  urn:uuid:eebb4a3c-30e8-43e5-96f5-eded890dd174
AuthoritiesDefaults                     bdq:sourceAuthority default = "The Getty Thesa...
Description                             Measure if all VALIDATION_STATEPROVINCE_FOUND ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation SPACE CODED Test VOCABULARY Con...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                        41461142-2c1e-4fc1-bc97-f83a7b2a893d
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 232, dtype: object
Row:
Label                                           MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY
issueNumber                                                                           161
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/161
iri                                     https://rs.tdwg.org/bdqtest/terms/version/e0b8...
term_iri                                https://rs.tdwg.org/bdqtest/terms/e0b8cff1-332...
issued                                                                         2025-03-06
term_localName                                       e0b8cff1-3322-40d2-b8b2-b99fc9ae130a
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                   bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:taxonRank is bdq:NotEmpty; ot...
SpecificationGuid                           urn:uuid:c619ec9b-92ec-4047-a8d3-931e3324bf3e
MethodGuid                                  urn:uuid:dbb803cb-8b37-4db3-a562-b4f6036f9d17
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_TAXONRANK_NOTEMPTY i...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 226, dtype: object
Row:
Label                                           MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD
issueNumber                                                                           162
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/162
iri                                     https://rs.tdwg.org/bdqtest/terms/version/f320...
term_iri                                https://rs.tdwg.org/bdqtest/terms/f320ca83-848...
issued                                                                         2025-03-06
term_localName                                       f320ca83-8487-4011-b1ff-f4b1b4dd86ec
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                   bdq:VALIDATION_TAXONRANK_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:c8964200-630e-47c6-baad-7e334fddbbdb
MethodGuid                                  urn:uuid:e95df0f4-b6b6-4e04-ad00-95eef6e8d993
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF TaxonRank ...
Description                             Measure if all VALIDATION_TAXONRANK_STANDARD i...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                      bdq:Record-Management, bdq:Taxon-Management
ArgumentGuids                                        da536dda-d467-450e-8b0a-6b6903fd1a1b
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 228, dtype: object
Row:
Label                                               MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY
issueNumber                                                                           105
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/105
iri                                     https://rs.tdwg.org/bdqtest/terms/version/2a9d...
term_iri                                https://rs.tdwg.org/bdqtest/terms/2a9d4cfd-815...
issued                                                                         2025-03-06
term_localName                                       2a9d4cfd-815a-46e0-bb51-60724582b762
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                       bdq:VALIDATION_TAXON_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if at least one term needed to deter...
SpecificationGuid                           urn:uuid:f38e3644-354d-4180-bc7c-c437cef1d606
MethodGuid                                  urn:uuid:9c5798cd-6176-41ed-8e91-35e3df1fa6d4
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_TAXON_NOTEMPTY in a ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation NAME CODED Test Completeness CORE
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 194, dtype: object
Row:
Label                                            MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS
issueNumber                                                                            70
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/70
iri                                     https://rs.tdwg.org/bdqtest/terms/version/0df0...
term_iri                                https://rs.tdwg.org/bdqtest/terms/0df03601-376...
issued                                                                         2025-03-06
term_localName                                       0df03601-3768-4805-906a-bbd0a41b0fda
DateLastUpdated                                                                2023-09-18
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Taxon
InformationElement:ActedUpon                    bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:8bd6f6de-49e4-4889-82e0-e4af093981e0
MethodGuid                                  urn:uuid:55b60dd8-7054-4736-b9ac-88bef8967fb2
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF Backbone T...
Description                             Measure if all VALIDATION_TAXON_UNAMBIGUOUS in...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation NAME CODED Test VOCABULARY Conf...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:S...
ArgumentGuids                                        1f9a778a-7949-4574-8826-55de1e4c1e32
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 158, dtype: object
Row:
Label                                          MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD
issueNumber                                                                           285
historyNoteUrl                                     https://github.com/tdwg/bdq/issues/285
iri                                     https://rs.tdwg.org/bdqtest/terms/version/1ca3...
term_iri                                https://rs.tdwg.org/bdqtest/terms/1ca359ea-4df...
issued                                                                         2025-03-07
term_localName                                       1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88
DateLastUpdated                                                                2024-11-11
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                   dwc:Occurrence
InformationElement:ActedUpon                  bdq:VALIDATION_TYPESTATUS_STANDARD.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sour...
SpecificationGuid                           urn:uuid:e4dbf38d-bdd7-4cf7-8c60-5b3bfc6af4ff
MethodGuid                                  urn:uuid:f84d0f30-9c93-43a4-8f75-8c853fc18fb5
AuthoritiesDefaults                     bdq:sourceAuthority default = "GBIF TypeStatus...
Description                             Measure if all VALIDATION_TYPESTATUS_STANDARD ...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation OTHER CODED Test VOCABULARY Con...
UseCases                                bdq:Taxon-Management, bdq:Alien-Species, bdq:R...
ArgumentGuids                                        63b0193f-a8df-4345-8d60-caf667cd62b0
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 252, dtype: object
Row:
Label                                                 MULTIRECORD_MEASURE_QA_YEAR_INRANGE
issueNumber                                                                            84
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/84
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a050...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a0502c5f-608...
issued                                                                         2025-03-06
term_localName                                       a0502c5f-608b-4e59-99da-d9490bb4d93b
DateLastUpdated                                                                2024-08-23
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                         bdq:VALIDATION_YEAR_INRANGE.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        INTERNAL_PREREQUISITES_NOT_MET if dwc:year is ...
SpecificationGuid                           urn:uuid:aee43366-0352-448a-a5ea-85ddc8605da1
MethodGuid                                  urn:uuid:7922ab56-6eae-4257-9691-d55d24842274
AuthoritiesDefaults                     bdq:earliestValidDate default = "1582",bdq:lat...
Description                             Measure if all VALIDATION_YEAR_INRANGE in a re...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                     Conformance
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                             TG2 Validation TIME CODED Test Conformance Par...
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                           9167035f-14a8-4a0f-81eb-86a5a93bf6d9,fa6e83af-...
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 174, dtype: object
Row:
Label                                                MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY
issueNumber                                                                            49
historyNoteUrl                                      https://github.com/tdwg/bdq/issues/49
iri                                     https://rs.tdwg.org/bdqtest/terms/version/a8fe...
term_iri                                https://rs.tdwg.org/bdqtest/terms/a8fef8a8-e7c...
issued                                                                         2025-03-06
term_localName                                       a8fef8a8-e7c7-4a2d-adaf-7da99c896c93
DateLastUpdated                                                                2023-09-17
prefLabel                               Measurement over MultiRecord for QualityAssura...
IE Class                                                                        dwc:Event
InformationElement:ActedUpon                        bdq:VALIDATION_YEAR_NOTEMPTY.Response
InformationElement:Consulted                                                          NaN
Parameters                                                                            NaN
ExpectedResponse                        COMPLIANT if dwc:year is bdq:NotEmpty; otherwi...
SpecificationGuid                           urn:uuid:42f331f4-a5a8-48b4-a08e-57048d1d1a77
MethodGuid                                  urn:uuid:2a0843de-32f9-473e-984a-619dace9ee66
AuthoritiesDefaults                                                                   NaN
Description                             Measure if all VALIDATION_YEAR_NOTEMPTY in a r...
Type                                                                              Measure
Resource Type                                                                 MultiRecord
Dimension                                                                    Completeness
Criterion                                                                             NaN
Enhancement                                                                           NaN
Examples                                                                              NaN
Source                                                                                TG2
References                              Veiga AK, Saraiva AM, Chapman AD, Morris PJ, G...
Example Implementations (Mechanisms)                                                  NaN
Link to Specification Source Code                                                     NaN
Notes                                   For Quality Assurance, filter record set until...
IssueState                                                                           open
IssueLabels                              TG2 Validation TIME CODED Test Completeness CORE
UseCases                                bdq:Alien-Species, bdq:Spatial-Temporal_Patter...
ArgumentGuids                                                                         NaN
status                                                                        recommended
flags                                                                                 NaN
organized_in                                                                      Measure
Name: 138, dtype: object
- [AMENDMENT_BASISOFRECORD_STANDARDIZED](#AMENDMENT_BASISOFRECORD_STANDARDIZED)
- [AMENDMENT_COORDINATES_FROM_VERBATIM](#AMENDMENT_COORDINATES_FROM_VERBATIM)
- [AMENDMENT_COORDINATES_TRANSPOSED](#AMENDMENT_COORDINATES_TRANSPOSED)
- [AMENDMENT_COUNTRYCODE_FROM_COORDINATES](#AMENDMENT_COUNTRYCODE_FROM_COORDINATES)
- [AMENDMENT_COUNTRYCODE_STANDARDIZED](#AMENDMENT_COUNTRYCODE_STANDARDIZED)
- [AMENDMENT_DATEIDENTIFIED_STANDARDIZED](#AMENDMENT_DATEIDENTIFIED_STANDARDIZED)
- [AMENDMENT_DAY_STANDARDIZED](#AMENDMENT_DAY_STANDARDIZED)
- [AMENDMENT_DCTYPE_STANDARDIZED](#AMENDMENT_DCTYPE_STANDARDIZED)
- [AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED](#AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED)
- [AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED](#AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED)
- [AMENDMENT_EVENTDATE_FROM_VERBATIM](#AMENDMENT_EVENTDATE_FROM_VERBATIM)
- [AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY](#AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY)
- [AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR](#AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR)
- [AMENDMENT_EVENTDATE_STANDARDIZED](#AMENDMENT_EVENTDATE_STANDARDIZED)
- [AMENDMENT_EVENT_FROM_EVENTDATE](#AMENDMENT_EVENT_FROM_EVENTDATE)
- [AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT](#AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT)
- [AMENDMENT_GEODETICDATUM_STANDARDIZED](#AMENDMENT_GEODETICDATUM_STANDARDIZED)
- [AMENDMENT_LICENSE_STANDARDIZED](#AMENDMENT_LICENSE_STANDARDIZED)
- [AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM](#AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM)
- [AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM](#AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM)
- [AMENDMENT_MONTH_STANDARDIZED](#AMENDMENT_MONTH_STANDARDIZED)
- [AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT](#AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT)
- [AMENDMENT_OCCURRENCESTATUS_STANDARDIZED](#AMENDMENT_OCCURRENCESTATUS_STANDARDIZED)
- [AMENDMENT_PATHWAY_STANDARDIZED](#AMENDMENT_PATHWAY_STANDARDIZED)
- [AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON](#AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON)
- [AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID](#AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID)
- [AMENDMENT_SEX_STANDARDIZED](#AMENDMENT_SEX_STANDARDIZED)
- [AMENDMENT_TAXONRANK_STANDARDIZED](#AMENDMENT_TAXONRANK_STANDARDIZED)
- [AMENDMENT_TYPESTATUS_STANDARDIZED](#AMENDMENT_TYPESTATUS_STANDARDIZED)
- [ISSUE_ANNOTATION_NOTEMPTY](#ISSUE_ANNOTATION_NOTEMPTY)
- [ISSUE_COORDINATES_CENTEROFCOUNTRY](#ISSUE_COORDINATES_CENTEROFCOUNTRY)
- [ISSUE_DATAGENERALIZATIONS_NOTEMPTY](#ISSUE_DATAGENERALIZATIONS_NOTEMPTY)
- [ISSUE_ESTABLISHMENTMEANS_NOTEMPTY](#ISSUE_ESTABLISHMENTMEANS_NOTEMPTY)
- [MEASURE_AMENDMENTS_PROPOSED](#MEASURE_AMENDMENTS_PROPOSED)
- [MEASURE_EVENTDATE_DURATIONINSECONDS](#MEASURE_EVENTDATE_DURATIONINSECONDS)
- [MEASURE_VALIDATIONTESTS_COMPLIANT](#MEASURE_VALIDATIONTESTS_COMPLIANT)
- [MEASURE_VALIDATIONTESTS_NOTCOMPLIANT](#MEASURE_VALIDATIONTESTS_NOTCOMPLIANT)
- [MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET](#MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET)
- [VALIDATION_BASISOFRECORD_NOTEMPTY](#VALIDATION_BASISOFRECORD_NOTEMPTY)
- [VALIDATION_BASISOFRECORD_STANDARD](#VALIDATION_BASISOFRECORD_STANDARD)
- [VALIDATION_CLASSIFICATION_CONSISTENT](#VALIDATION_CLASSIFICATION_CONSISTENT)
- [VALIDATION_CLASS_FOUND](#VALIDATION_CLASS_FOUND)
- [VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT](#VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT)
- [VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT](#VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT)
- [VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT](#VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT)
- [VALIDATION_COORDINATES_NOTZERO](#VALIDATION_COORDINATES_NOTZERO)
- [VALIDATION_COORDINATEUNCERTAINTY_INRANGE](#VALIDATION_COORDINATEUNCERTAINTY_INRANGE)
- [VALIDATION_COUNTRYCODE_NOTEMPTY](#VALIDATION_COUNTRYCODE_NOTEMPTY)
- [VALIDATION_COUNTRYCODE_STANDARD](#VALIDATION_COUNTRYCODE_STANDARD)
- [VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT](#VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT)
- [VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS](#VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS)
- [VALIDATION_COUNTRY_FOUND](#VALIDATION_COUNTRY_FOUND)
- [VALIDATION_COUNTRY_NOTEMPTY](#VALIDATION_COUNTRY_NOTEMPTY)
- [VALIDATION_DATEIDENTIFIED_INRANGE](#VALIDATION_DATEIDENTIFIED_INRANGE)
- [VALIDATION_DATEIDENTIFIED_STANDARD](#VALIDATION_DATEIDENTIFIED_STANDARD)
- [VALIDATION_DAY_INRANGE](#VALIDATION_DAY_INRANGE)
- [VALIDATION_DAY_STANDARD](#VALIDATION_DAY_STANDARD)
- [VALIDATION_DCTYPE_NOTEMPTY](#VALIDATION_DCTYPE_NOTEMPTY)
- [VALIDATION_DCTYPE_STANDARD](#VALIDATION_DCTYPE_STANDARD)
- [VALIDATION_DECIMALLATITUDE_INRANGE](#VALIDATION_DECIMALLATITUDE_INRANGE)
- [VALIDATION_DECIMALLATITUDE_NOTEMPTY](#VALIDATION_DECIMALLATITUDE_NOTEMPTY)
- [VALIDATION_DECIMALLONGITUDE_INRANGE](#VALIDATION_DECIMALLONGITUDE_INRANGE)
- [VALIDATION_DECIMALLONGITUDE_NOTEMPTY](#VALIDATION_DECIMALLONGITUDE_NOTEMPTY)
- [VALIDATION_DEGREEOFESTABLISHMENT_STANDARD](#VALIDATION_DEGREEOFESTABLISHMENT_STANDARD)
- [VALIDATION_ENDDAYOFYEAR_INRANGE](#VALIDATION_ENDDAYOFYEAR_INRANGE)
- [VALIDATION_ESTABLISHMENTMEANS_STANDARD](#VALIDATION_ESTABLISHMENTMEANS_STANDARD)
- [VALIDATION_EVENTDATE_INRANGE](#VALIDATION_EVENTDATE_INRANGE)
- [VALIDATION_EVENTDATE_NOTEMPTY](#VALIDATION_EVENTDATE_NOTEMPTY)
- [VALIDATION_EVENTDATE_STANDARD](#VALIDATION_EVENTDATE_STANDARD)
- [VALIDATION_EVENTTEMPORAL_NOTEMPTY](#VALIDATION_EVENTTEMPORAL_NOTEMPTY)
- [VALIDATION_EVENT_CONSISTENT](#VALIDATION_EVENT_CONSISTENT)
- [VALIDATION_FAMILY_FOUND](#VALIDATION_FAMILY_FOUND)
- [VALIDATION_GENUS_FOUND](#VALIDATION_GENUS_FOUND)
- [VALIDATION_GEODETICDATUM_NOTEMPTY](#VALIDATION_GEODETICDATUM_NOTEMPTY)
- [VALIDATION_GEODETICDATUM_STANDARD](#VALIDATION_GEODETICDATUM_STANDARD)
- [VALIDATION_KINGDOM_FOUND](#VALIDATION_KINGDOM_FOUND)
- [VALIDATION_KINGDOM_NOTEMPTY](#VALIDATION_KINGDOM_NOTEMPTY)
- [VALIDATION_LICENSE_NOTEMPTY](#VALIDATION_LICENSE_NOTEMPTY)
- [VALIDATION_LICENSE_STANDARD](#VALIDATION_LICENSE_STANDARD)
- [VALIDATION_LOCATION_NOTEMPTY](#VALIDATION_LOCATION_NOTEMPTY)
- [VALIDATION_MAXDEPTH_INRANGE](#VALIDATION_MAXDEPTH_INRANGE)
- [VALIDATION_MAXELEVATION_INRANGE](#VALIDATION_MAXELEVATION_INRANGE)
- [VALIDATION_MINDEPTH_INRANGE](#VALIDATION_MINDEPTH_INRANGE)
- [VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH](#VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH)
- [VALIDATION_MINELEVATION_INRANGE](#VALIDATION_MINELEVATION_INRANGE)
- [VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION](#VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION)
- [VALIDATION_MONTH_STANDARD](#VALIDATION_MONTH_STANDARD)
- [VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY](#VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY)
- [VALIDATION_OCCURRENCEID_NOTEMPTY](#VALIDATION_OCCURRENCEID_NOTEMPTY)
- [VALIDATION_OCCURRENCESTATUS_NOTEMPTY](#VALIDATION_OCCURRENCESTATUS_NOTEMPTY)
- [VALIDATION_OCCURRENCESTATUS_STANDARD](#VALIDATION_OCCURRENCESTATUS_STANDARD)
- [VALIDATION_ORDER_FOUND](#VALIDATION_ORDER_FOUND)
- [VALIDATION_PATHWAY_STANDARD](#VALIDATION_PATHWAY_STANDARD)
- [VALIDATION_PHYLUM_FOUND](#VALIDATION_PHYLUM_FOUND)
- [VALIDATION_POLYNOMIAL_CONSISTENT](#VALIDATION_POLYNOMIAL_CONSISTENT)
- [VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY](#VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY)
- [VALIDATION_SCIENTIFICNAMEID_COMPLETE](#VALIDATION_SCIENTIFICNAMEID_COMPLETE)
- [VALIDATION_SCIENTIFICNAMEID_NOTEMPTY](#VALIDATION_SCIENTIFICNAMEID_NOTEMPTY)
- [VALIDATION_SCIENTIFICNAME_FOUND](#VALIDATION_SCIENTIFICNAME_FOUND)
- [VALIDATION_SCIENTIFICNAME_NOTEMPTY](#VALIDATION_SCIENTIFICNAME_NOTEMPTY)
- [VALIDATION_SEX_STANDARD](#VALIDATION_SEX_STANDARD)
- [VALIDATION_STARTDAYOFYEAR_INRANGE](#VALIDATION_STARTDAYOFYEAR_INRANGE)
- [VALIDATION_STATEPROVINCE_FOUND](#VALIDATION_STATEPROVINCE_FOUND)
- [VALIDATION_TAXONRANK_NOTEMPTY](#VALIDATION_TAXONRANK_NOTEMPTY)
- [VALIDATION_TAXONRANK_STANDARD](#VALIDATION_TAXONRANK_STANDARD)
- [VALIDATION_TAXON_NOTEMPTY](#VALIDATION_TAXON_NOTEMPTY)
- [VALIDATION_TAXON_UNAMBIGUOUS](#VALIDATION_TAXON_UNAMBIGUOUS)
- [VALIDATION_TYPESTATUS_STANDARD](#VALIDATION_TYPESTATUS_STANDARD)
- [VALIDATION_YEAR_INRANGE](#VALIDATION_YEAR_INRANGE)
- [VALIDATION_YEAR_NOTEMPTY](#VALIDATION_YEAR_NOTEMPTY)

********************

# The BDQ Tests

## Validations, Measures, Amendments operating on Single Records.

###  VALIDATION_BASISOFRECORD_NOTEMPTY

####  Validation dwc:basisOfRecord Not Empty
https://rs.tdwg.org/bdqtest/terms/ac2b7648-d5f9-48ca-9b07-8ad5879a2536/2023-09-17
Acts upon  SingleRecord

#### Description

Is there a value in dwc:basisOfRecord?

#### Specification

COMPLIANT if dwc:basisOfRecord is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:basisOfRecord

#### Examples

dwc:basisOfRecord="PreservedSpecimen": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:basisOfRecord is bdq:NotEmpty"

dwc:basisOfRecord="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:basisOfRecord is bdq:Empty"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_BASISOFRECORD_STANDARD

####  Validation dwc:basisOfRecord Standard
https://rs.tdwg.org/bdqtest/terms/42408a00-bf71-4892-a399-4325e2bc1fb8/2024-08-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:basisOfRecord occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; COMPLIANT if the value of dwc:basisOfRecord is valid in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:basisOfRecord

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]}{dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}

#### Examples

dwc:basisOfRecord="Taxon": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:basisOfRecord matches a standard label of one of the Darwin Core classes"

dwc:basisOfRecord="Specimen": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:basisOfRecord does not exactly match a standard label of one of the Darwin Core classes"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

The term dwc:basisOfRecord has the comment "Recommended best practice is to use a controlled vocabulary such as the set of local names of the identifiers for classes in Darwin Core." The list of these values can be determined by searching https://github.com/tdwg/dwc/blob/master/vocabulary/term_versions.csv for rows with status="recommended" and rdf_type="http://www.w3.org/2000/01/rdf-schema#Class". For Tests against a dwc:Occurrence record, the set of valid terms is more limited and embodied in the resource found at https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DCTYPE_NOTEMPTY

####  Validation dc:type Not Empty
https://rs.tdwg.org/bdqtest/terms/374b091a-fc90-4791-91e5-c1557c649169/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dc:type?

#### Specification

COMPLIANT if dc:type is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dc:type

#### Examples

dc:type="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dc:type is bdq:NotEmpty"

dc:type=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dc:type is bdq:Empty"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DCTYPE_STANDARD

####  Validation dc:type Standard
https://rs.tdwg.org/bdqtest/terms/cdaabb0d-a863-49d0-bc0f-738d771acba5/2023-09-18
Acts upon  SingleRecord

#### Description

Does the value of dc:type occur as a value in the DCMI type vocabulary?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; COMPLIANT if the value of dc:type is a term name in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dc:type

#### Default Parameter Values

DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List Of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}

#### Examples

dc:type="Event": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dc:type matches a term in DCMI Vocabulary"

dc:type="StillerImage": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dc:type does not match terms in DCMI Vocabulary"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. EXTERNAL_PREREQUISITES_NOT_MET is not a necessary path in the specification, the type literals may be hard coded in a Test implementation without an external call.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_LICENSE_NOTEMPTY

####  Validation dcterms:license Not Empty
https://rs.tdwg.org/bdqtest/terms/15f78619-811a-4c6f-997a-a4c7888ad849/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dcterms:license?

#### Specification

COMPLIANT if dcterms:license is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dcterms:license

#### Examples

dcterms:license="CC0 1.0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dcterms:license is bdq:NotEmpty"

dcterms:license=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dcterms:license is bdq:Empty"


#### Use Cases

bdq:Record-Management

#### Notes

The license at the record level might be derived from the license of the dataset from which the record is retrieved.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_LICENSE_STANDARD

####  Validation dcterms:license Standard
https://rs.tdwg.org/bdqtest/terms/3136236e-04b6-49ea-8b34-a65f25e3aba1/2024-03-21
Acts upon  SingleRecord

#### Description

Does the value of dcterms:license occur in bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dcterms:license is bdq:Empty; COMPLIANT if the value of the term dcterms:license is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dcterms:license

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Creative Commons 4.0 Licenses or CC0" {[https://creativecommons.org/]} { Regular Expression ^(http(s){0,1}://creativecommons.org/licenses/(by&#124;by-sa&#124;by-nc&#124;by-nc-sa&#124;by-nd&#124;by-nc-nd)/4.0/((deed&#124;legalcode)(.(id&#124;eu&#124;da&#124;de&#124;en&#124;es&#124;fr&#124;fy&#124;hr&#124;it&#124;lv&#124;lt&#124;mi&#124;ni&#124;no&#124;pl&#124;pt&#124;ro&#124;si&#124;fi&#124;sv&#124;tr&#124;cs&#124;el&#124;ru&#124;uk&#124;ar&#124;jp&#124;zh-hans&#124;zh-hant&#124;ko)){0,1})&#124;(http(s){0,1}://creativecommons.org/publicdomain/zero/1.0/((deed&#124;legalcode)(.(id&#124;eu&#124;da&#124;de&#124;en&#124;es&#124;fr&#124;fy&#124;hr&#124;it&#124;lv&#124;lt&#124;ni&#124;no&#124;pl&#124;pt&#124;ro&#124;si&#124;fi&#124;sv&#124;tr&#124;cs&#124;el&#124;ru&#124;uk&#124;ar&#124;jp&#124;zh-hans&#124;zh-hant&#124;ko)){0,1})))$ }

#### Examples

dcterms:license="https://creativecommons.org/licenses/by/4.0/": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT,Response.comment="dcterms:license matches a term in the bdq:sourceAuthority"

dcterms:license="GPL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dcterms:license does not match a term in the bdq:sourceAuthority"


#### Use Cases

bdq:Record-Management

#### Notes

The license at the record level might be derived from the license of the dataset from which the record is retrieved. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. The canonical form of the Creative Commons license IRI has nothing after the version (e.g., https://creativecommons.org/licenses/by/4.0/), but may be followed by deed or legalcode e.g. https://creativecommons.org/licenses/by/4.0/deed and this may be followed by a language code. However, only some two-letter language codes have translations, and some translations are identified by a longer string than the two-letter language code. Errors in the language code, or specifying a language code for which a translation doesn't exist returns a 404 error instead of redirecting to the more general license IRI. As of 2024-02-28 deed.mi doesn't exist yet, but legalcode.mi does.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT

####  Validation Coordinates dwc:countryCode Consistent
https://rs.tdwg.org/bdqtest/terms/adb27d29-9f0d-4d52-b760-a77ba57a69c9/2024-08-30
Acts upon  SingleRecord

#### Description

Do the geographic coordinates fall on or within the boundaries of the territory given in dwc:countryCode or its Exclusive Economic Zone?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if one or more of dwc:decimalLatitude, dwc:decimalLongitude, or dwc:countryCode are bdq:Empty or invalid; COMPLIANT if the geographic coordinates fall on or within the boundary defined by the union of the boundary of the country from dwc:countryCode plus it's Exclusive Economic Zone as found in the bdq:sourceAuthority, if any, plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:countryCode,dwc:decimalLatitude,dwc:decimalLongitude

#### Parameters

bdq:sourceAuthority,bdq:spatialBufferInMeters

#### Default Parameter Values

bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]},bdq:spatialBufferInMeters default = "3000"

#### Examples

dwc:countryCode="AR", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Coordinates match dwc:countryCode"

dwc:countryCode="CL", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Coordinates are in Argentina, not Chile"

dwc:countryCode="ZX", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=INTERNAL_PREREQUISTES_NOT_MET, Response.comment="Input field contains invalid values - ZX is not a valid ISO 3166-1-alpha-2 country code"


#### Use Cases

bdq:Spatial-Temporal_Patterns

#### Notes

dwc:coordinatePrecision and dwc:coordinateUncertaintyInMeters (if present) imply a potential displacement of the provided coordinates. These two terms can be considered spatial buffers. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is justified. When dwc:countryCode=XZ (for High Seas), the coordinate should fall into a marine region out side of the EEZ of any country. Taking the spatial buffers into account does however greatly complicate both the logic and the implementation of such Tests. The same applies to potential conversion of the Spatial Reference System (SRS) of dwc:decimalLatitude and dwc:decimalLongitude to the SRS used in the bdq:sourceAuthority.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT

####  Validation Coordinates dwc:stateProvince Consistent
https://rs.tdwg.org/bdqtest/terms/f18a470b-3fe1-4aae-9c65-a6d3db6b550c/2024-08-30
Acts upon  SingleRecord

#### Description

Do the geographic coordinates fall on or within the boundary from the bdq:sourceAuthority for the given dwc:stateProvince or within the distance given by bdq:spatialBufferInMeters outside that boundary?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or invalid, or dwc:stateProvince is bdq:Empty or not found in the bdq:sourceAuthority; COMPLIANT if the geographic coordinates fall on or within the boundary in the bdq:sourceAuthority for the given dwc:stateProvince (after coordinate reference system transformations, if any, have been accounted for), or within the distance given by bdq:spatialBufferInMeters outside that boundary; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:stateProvince,dwc:decimalLatitude,dwc:decimalLongitude

#### Parameters

bdq:sourceAuthority,bdq:spatialBufferInMeters

#### Default Parameter Values

bdq:sourceAuthority default = "10m-admin-1 boundaries" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/]},bdq:spatialBufferInMeters default = "3000"

#### Examples

dwc:stateProvince="Tasmania", dwc:decimalLatitude="-42.85", dwc:decimalLongitude="146.75": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Input fields contain interpretable values"

dwc:stateProvince="Córdoba", dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Input fields contain interpretable values but coordinates don't match dwc:stateProvince with buffer"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The geographic determination service is expected to return a list of names of first-level administrative divisions for geometries that the geographic point falls on or within, including a 3 km buffer around the administrative geometry. A match on any of those names should constitute a consistency, and dwc:countryCode should not be needed to make this determination, that is, this Test does not attempt to disambiguate potential duplicate first-level administrative division names. The level of buffering may be related to the scale of the underlying GIS layer being used. At a global scale, typical map scales used for borders and coastal areas are either 1:3M or 1:1M (Dooley 2005, Chapter 4). Horizontal accuracy at those scales is around 1.5-2.5km and 0.5-0.85 km respectively (Chapman & Wieczorek 2020).

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT

####  Validation Coordinates Terrestrial Marine
https://rs.tdwg.org/bdqtest/terms/b9c184ce-a859-410c-9d12-71a338200380/2024-08-30
Acts upon  SingleRecord

#### Description

Does the marine/non-marine biome of a taxon from the bdq:sourceAuthority match the biome at the location given by the coordinates?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if either bdq:taxonIsMarine or bdq:geospatialLand are not available; INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:scientificName is bdq:Empty or (2) the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or (3) if bdq:assumptionOnUnknownBiome is noassumption and the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine; COMPLIANT if (1) the taxon marine/nonmarine status from bdq:taxonIsMarine matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters or (2) if the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine and bdq:assumptionOnUnknownBiome matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:decimalLatitude,dwc:decimalLongitude

Consulted: 
dwc:scientificName

#### Parameters

bdq:taxonIsMarine,bdq:geospatialLand,bdq:spatialBufferInMeters,bdq:assumptionOnUnknownBiome

#### Default Parameter Values

bdq:taxonIsMarine default = "World Register of Marine Species (WoRMS)" {[https://www.marinespecies.org/]} {Web service [https://www.marinespecies.org/aphia.php?p=webservice]},bdq:geospatialLand default = "Union of NaturalEarth 10m-physical-vectors for Land and NaturalEarth Minor Islands" {[https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip], [https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_minor_islands.zip]},bdq:spatialBufferInMeters default = "3000",bdq:assumptionOnUnknownBiome default = "noassumption"

#### Examples

dwc:decimalLatitude="-41.0525925872862", dwc:decimalLongitude="-71.5310546742521", dwc:scientificName="Aegla neuquensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="The species is freshwater aquatic and the coordinates fall in a lake and thus COMPLIANT"

dwc:decimalLatitude="20.0", dwc:decimalLongitude="-30.0", dwc:scientificName="Viviparus contectus (Millet, 1813)": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is non-marine according to dwc:taxonIsMarine but coordinates are marine"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

dwc:coordinatePrecision and dwc:coordinateUncertaintyInMeters (if present) imply a potential displacement of the provided coordinates. These two terms can be considered spatial buffers. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is justified. Taking the spatial buffers into account does however greatly complicate both the logic and the implementation of such Tests. The same applies to potential conversion of the Spatial Reference System (SRS) of dwc:decimalLatitude and dwc:decimalLongitude to the SRS used in the bdq:sourceAuthority. Note that in the current implementation Tests treat "brackish" in WoRMS as both marine and terrestrial. Note that both bdq:taxonIsMarine and bdq:geospatialLand are bdq:sourceAuthorities, but as they form two parameters, distinct names are used for them.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COORDINATES_NOTZERO

####  Validation Coordinates Not Zero
https://rs.tdwg.org/bdqtest/terms/1bf0e210-6792-4128-b8cc-ab6828aa4871/2023-06-20
Acts upon  SingleRecord

#### Description

Are the values of either dwc:decimalLatitude or dwc:decimalLongitude numbers that are not equal to 0?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or is not interpretable as a number, or dwc:decimalLongitude is bdq:Empty or is not interpretable as a number; COMPLIANT if either the value of dwc:decimalLatitude is not = 0 or the value of dwc:decimalLongitude is not = 0; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:decimalLatitude,dwc:decimalLongitude

#### Examples

dwc:decimalLatitude="21.0534", dwc:decimalLongitude="81.0554": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatitude and dwc:decimalLongitude are not zero"

dwc:decimalLatitude="0", dwc:decimalLongitude="0",: Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatitude and dwc:decimalLongitude are zero"


#### Use Cases

bdq:Spatial-Temporal_Patterns

#### Notes

A record with 0.0 is interpreted as the string "0".

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COORDINATEUNCERTAINTY_INRANGE

####  Validation dwc:coordinateUncertaintyInMeters In Range
https://rs.tdwg.org/bdqtest/terms/c6adf2ea-3051-4498-97f4-4b2f8a105f57/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:coordinateUncertaintyInMeters a number between 1 and 20,037,509?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:coordinateUncertaintyInMeters is bdq:Empty; COMPLIANT if the value of dwc:coordinateUncertaintyInMeters is interpreted as a number between 1 and 20037509 inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:coordinateUncertaintyInMeters

#### Examples

dwc:coordinateUncertaintyInMeters="1": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:coordinateUncertaintyInMeters is in range"

dwc:coordinateUncertaintyInMeters="-1": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:coordinateUncertaintyInMeters is out of range"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The upper limit is one half the equatorial circumference of the earth.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COUNTRYCODE_NOTEMPTY

####  Validation dwc:countryCode Not Empty
https://rs.tdwg.org/bdqtest/terms/853b79a2-b314-44a2-ae46-34a1e7ed85e4/2024-11-10
Acts upon  SingleRecord

#### Description

Is there a value in dwc:countryCode?

#### Specification

COMPLIANT if dwc:countryCode is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:countryCode

#### Examples

dwc:countryCode="Australia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is bdq:NotEmpty"

dwc:countryCode="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is bdq:Empty"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

This Test will return 'NOT_COMPLIANT' for records on the "High seas" where dwc:countryCode is bdq:Empty. We recommend that data from the high seas (outside national jurisdictions) use dwc:countryCode = "XZ" and dwc:country = "High seas" until an agreement has been made.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COUNTRYCODE_STANDARD

####  Validation dwc:countryCode Standard
https://rs.tdwg.org/bdqtest/terms/0493bcfb-652e-4d17-815b-b0cce0742fbe/2024-09-19
Acts upon  SingleRecord

#### Description

Is the value of dwc:countryCode a valid ISO 3166-1-alpha-2 country code?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:countryCode

#### Default Parameter Values

bdq:sourceAuthority default = "ISO 3166 Country Codes" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}

#### Examples

dwc:countryCode="GL": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:countryCode is a valid ISO (ISO 3166-1-alpha-2 country codes) value"

dwc:countryCode="GRL": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:countryCode is NOT a valid ISO (ISO 3166-1-alpha-2 country codes) value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Locations outside of a jurisdiction covered by a country code may have a value in the field dwc:countryCode, the ISO user defined codes include XZ used by the UN for installations on the high seas and suitable for a marker for the high seas. Also available in the ISO user defined codes is ZZ, used by GBIF to mark unknown countries. This Test should accept both XZ and ZZ as COMPLIANT country codes. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT

####  Validation dwc:country dwc:countryCode Consistent
https://rs.tdwg.org/bdqtest/terms/b23110e7-1be7-444a-a677-cdee0cf4330c/2024-09-25
Acts upon  SingleRecord

#### Description

Does the ISO country code, determined from the value of dwc:country, equal the value of dwc:countryCode?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either of the terms dwc:country or dwc:countryCode are bdq:Empty; COMPLIANT if the values of dwc:country and dwc:countryCode match national-level country name and matching country code respectively in the bdq:sourceAuthority

#### Information Elements

Acted upon: 
dwc:country,dwc:countryCode

#### Default Parameter Values

bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}

#### Examples

dwc:country="Australia", dwc:countryCode="AU": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country matches dwc:countryCode"

dwc:country="United States Minor Outlying Islands", dwc:countryCode="US": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country does not match dwc:countryCode"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The country code determination service should be able to match the name of a country in the original or any language in the source authority. When dwc:countryCode="XZ" to mark the high seas, country should be empty until a time when a dwc:country="High seas" or similar is adopted. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS

####  Validation dwc:country dwc:stateProvince Unambiguous
https://rs.tdwg.org/bdqtest/terms/d257eb98-27cb-48e5-8d3c-ab9fca4edd11/2024-09-18
Acts upon  SingleRecord

#### Description

Is the combination of the values of the terms dwc:country, dwc:stateProvince unique in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the terms dwc:country and dwc:stateProvince are bdq:Empty; COMPLIANT if the combination of values of dwc:country and dwc:stateProvince are unambiguously resolved to a single result with a child-parent relationship in the bdq:sourceAuthority and the entity matching the value of dwc:country in the bdq:sourceAuthority is an ISO 3166 country-like administrative entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:country,dwc:stateProvince

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}

#### Examples

dwc:country="Argentina", dwc:stateProvince="Rio Negro": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country and dwc:stateProvince are unambiguous"

dwc:country="", dwc:stateProvince="WA": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country and dwc:stateProvince are ambiguous. Matches Western Australia, Washington State (US)"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

See table https://github.com/tdwg/bdq/issues/95#issuecomment-1226450014. A fail condition may arise from the content being internally inconsistent (not all of the information can be true at the same time), or from the vocabulary being incapable of uniquely resolving the combination of term values. This Test specifically does not consider the content of dwc:higherGeography. If dwc:country contains a value and dwc:stateProvince does not, this Test will return NOT_COMPLIANT. Use cases where knowledge to the level of country is adequate for the fitness of the data should not include this Test. @tucotuco: "Of #200 and #201, #201 is the strongest Test. If it passes for a record, #200 must necessarily also pass and doesn't tell you anything. If #201 fails, #200 could still pass and that would tell you that there are multiple matches on the dwc:country/dwc:stateProvince combo: It would tell you the nature of the problem. Along with #42 (dwc:country not empty), #200 would tell you whether there was an ambiguous combination of country (not empty) and dwc:stateProvince, such as would happen with Argentina/Buenos Aires. While if country is empty, then the ambiguity is purely at the dwc:stateProvince level".

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COUNTRY_FOUND

####  Validation dwc:country Found
https://rs.tdwg.org/bdqtest/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134/2024-08-19
Acts upon  SingleRecord

#### Description

Does the value of dwc:country occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:country is bdq:Empty; COMPLIANT if value of dwc:country is a place type equivalent to administrative entity of "nation" in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:country

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}

#### Examples

dwc:country="Eswatini": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country is a valid country name in the bdq:sourceAuthority"

dwc:country="Tasmania": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="Tasmania is not found at the level of national in the bdq:sourceAuthority"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Non-country information such as "high seas" will fail this Test (high seas should use dwc:countryCode = "XZ" and have dwc:country empty). Getty Place Types for administrative level "nation" are 81010 nation, 81011 independent sovereign nation, and 81012 independent nation. Multiple values in the dwc:country field (whether to signify on a border or in a list of possibilities) will fail this Test. Locations outside of a jurisdiction covered by a country code should not have a value in the field dwc:countryCode. This Test should find any matches at the Getty "nation" level including internationalized names and historical representations of that nation (where boundaries are same). This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_COUNTRY_NOTEMPTY

####  Validation dwc:country Not Empty
https://rs.tdwg.org/bdqtest/terms/6ce2b2b4-6afe-4d13-82a0-390d31ade01c/2024-09-27
Acts upon  SingleRecord

#### Description

Is there a value in dwc:country?

#### Specification

COMPLIANT if dwc:country is bdq:NotEmpty or dwc:countryCode has a value of "XZ" and either dwc:country is bdq:Empty or has a value of "High seas"; otherwise NOT_COMPLIANT ?

#### Information Elements

Acted upon: 
dwc:country

Consulted: 
dwc:countryCode

#### Examples

dwc:country="Eswatini": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:country is bdq:NotEmpty"

dwc:country="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:country is bdq:Empty"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Country is expected to be either bdq:Empty or, ideally, have a value of "High seas" or an agreed equivalent if material comes from the high seas, or from those portions of Antarctica outside of any sovereign nation.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DECIMALLATITUDE_INRANGE

####  Validation dwc:decimalLatitude In Range
https://rs.tdwg.org/bdqtest/terms/b6ecda2a-ce36-437a-b515-3ae94948fe83/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:decimalLatitude a number between -90 and 90 inclusive?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or the value is not interpretable as a number; COMPLIANT if the value of dwc:decimalLatitude is between -90 and 90, inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:decimalLatitude

#### Examples

dwc:decimalLatitude="0.0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatitude is in RANGE"

dwc:decimalLatitude="121.0534": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatitude is in not in RANGE"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DECIMALLATITUDE_NOTEMPTY

####  Validation dwc:decimalLatitude Not Empty
https://rs.tdwg.org/bdqtest/terms/7d2485d5-1ba7-4f25-90cb-f4480ff1a275/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:decimalLatitude?

#### Specification

COMPLIANT if dwc:decimalLatitude is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:decimalLatitude

#### Examples

dwc:decimalLatitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLatiitude is bdq:NotEmpty"

dwc:decimalLatitude="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLatiitude is bdq:Empty"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DECIMALLONGITUDE_INRANGE

####  Validation dwc:decimalLongitude In Range
https://rs.tdwg.org/bdqtest/terms/0949110d-c06b-450e-9649-7c1374d940d1/2023-09-17
Acts upon  SingleRecord

#### Description

Is the value of dwc:decimalLongitude a number between -180 and 180 inclusive?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLongitude is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:decimalLongitude is between -180 and 180 degrees, inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:decimalLongitude

#### Examples

dwc:decimalLongitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLongitude is in range"

dwc:decimalLongitude="181.0554": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLongitude >180"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DECIMALLONGITUDE_NOTEMPTY

####  Validation dwc:decimalLongitude Not Empty
https://rs.tdwg.org/bdqtest/terms/9beb9442-d942-4f42-8b6a-fcea01ee086a/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:decimalLongitude?

#### Specification

COMPLIANT if dwc:decimalLongitude is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:decimalLongitude

#### Examples

dwc:decimalLongitude="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:decimalLongitude is bdq:NotEmpty"

dwc:decimalLongitude=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:decimalLongitude is bdq:Empty"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_GEODETICDATUM_NOTEMPTY

####  Validation dwc:geodeticDatum Not Empty
https://rs.tdwg.org/bdqtest/terms/239ec40e-a729-4a8e-ba69-e0bf03ac1c44/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:geodeticDatum?

#### Specification

COMPLIANT if dwc:geodeticDatum is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:geodeticDatum

#### Examples

dwc:geodeticDatum="UTM": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:geodeticDatum is bdq:NotEmpty"

dwc:geodeticDatum="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:geodeticDatum is bdq:Empty."


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_GEODETICDATUM_STANDARD

####  Vaildation dwc:geodeticDatum Standard
https://rs.tdwg.org/bdqtest/terms/7e0c0418-fe16-4a39-98bd-80e19d95b9d1/2025-03-03
Acts upon  SingleRecord

#### Description

Does the value of dwc:geodeticDatum occur as a valid geographic CRS, geodetic Datum or ellipsoid in bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available, INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; COMPLIANT if the value of dwc:geodeticDatum is a valid code from the bdq:sourceAuthority (in the form Authority:Number) for a Datum, or ellipsoid, or for a CRS appropriate for a 2D geographic coordinate in degrees, or is the value "not recorded"; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:geodeticDatum

#### Default Parameter Values

bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index]}

#### Examples

dwc:geodeticDatum="EPSG:4326": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:geodeticDatum matches an unambiguous alphanumeric CRS or datum code value in the bdq:sourceAuthority"

dwc:geodeticDatum="7030": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:geodeticDatum doesn't match values in the bdq:sourceAuthority, 7030 is a bare number without an authority.


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Darwin Core recommends best practice is to use a controlled vocabulary. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. Chapman and Wieczorek (2020) recommend best practice is to use EPSG geographic CRS or Datum codes (https://epsg.io/) as a controlled vocabulary. Ideally, amend to the EPSG code for the geographic coordinate reference system (CRS), if known. Otherwise use the EPSG code for the geodetic datum, if known. Otherwise use the EPSG code of the ellipsoid, if known. If none of these is known, use the explicit value "not recorded". While "not recorded" is not a valid EPSG code, it is a valid value according to Darwin Core. The reference vocabularies of values for geodetic datums and ellipsoids needs to be made available and should map alternative representations of dwc:geodeticDatum strings to EPSG codes, such as "WGS84", "WGS_84", "WGS:84", "WGS 84" all with standard value "EPSG:4326".

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_LOCATION_NOTEMPTY

####  Validation dcterms:Location Not Empty
https://rs.tdwg.org/bdqtest/terms/58486cb6-1114-4a8a-ba1e-bd89cfe887e9/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in any of the Darwin Core spatial terms that could specify a location?

#### Specification

COMPLIANT if at least one term needed to determine the location of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:higherGeographyID,dwc:higherGeography,dwc:continent,dwc:country,dwc:countryCode,dwc:stateProvince,dwc:county,dwc:municipality,dwc:waterBody,dwc:island,dwc:islandGroup,dwc:locality,dwc:locationID,dwc:verbatimLocality,dwc:decimalLatitude,dwc:decimalLongitude,dwc:verbatimCoordinates,dwc:verbatimLatitude,dwc:verbatimLongitude,dwc:footprintWKT

#### Examples

dwc:locationID="https://opencontext.org/subjects/e54377f7-4452-4315-b676-40679b10c4d9", dwc:higherGeographyID="", dwc:higherGeography="",dwc:continent="", dwc:waterBody="", dwc:islandGroup="", dwc:island="", dwc:country="", dwc:countryCode="", dwc:stateProvince="", dwc:county="", dwc:municipality="", dwc:locality="", dwc:verbatimLocality="", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="", dwc:geodeticDatum="", dwc:verbatimCoordinates="", dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:footprintWKT="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:LocationID is bdq:NotEmpty"

dwc:locationID="", dwc:higherGeographyID="", dwc:higherGeography="", dwc:continent="", dwc:waterBody="", dwc:islandGroup="", dwc:island="", dwc:country="", dwc:countryCode="", dwc:stateProvince="", dwc:county="", dwc:municipality="", dwc:locality="", dwc:verbatimLocality="", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="", dwc:geodeticDatum="", dwc:verbatimCoordinates="", dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:footprintWKT="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All location fields are bdq:Empty"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Only fails if all of the relevant fields of the Darwin Core Location class are EMPTY or do not exist. Relevant Darwin Core fields include dwc:locationID, dwc:higherGeographyID, dwc:higherGeography, dwc:continent, dwc:waterBody, dwc:islandGroup, dwc:island, dwc:country, dwc:countryCode, dwc:stateProvince, dwc:county, dwc:municipality, dwc:locality, dwc:verbatimLocality, dwc:decimalLatitude, dwc:decimalLongitude, dwc:verbatimCoordinates, dwc:verbatimLatitude, dwc:verbatimLongitude, dwc:footprintWKT. Elevation and/or depth alone are deemed insufficient to meaningfully locate a position on the earth.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_MAXDEPTH_INRANGE

####  Validation dwc:maximumDepthInMeters In Range
https://rs.tdwg.org/bdqtest/terms/3f1db29a-bfa5-40db-9fd1-fde020d81939/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:maximumDepthInMeters within the Parameter range?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumDepthInMeters is bdq:Empty or is not interpretable as a number greater than or equal to zero; COMPLIANT if the value of dwc:maximumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:maximumDepthInMeters

#### Parameters

bdq:minimumValidDepthInMeters,bdq:maximumValidDepthInMeters

#### Default Parameter Values

bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"

#### Examples

dwc:maximumDepthInMeters="1200": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:maximumDepthInMeters is in range (<11,000)"

dwc:maximumDepthInMeters="99999": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:maximumDepthInMeters is not in range (>11,000)"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The Challenger Deep in the Mariana Trench is the deepest known point in Earth's oceans at 10,994 meters below sea level. We have rounded up bdq:maximumValidDepthInMeters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_MAXELEVATION_INRANGE

####  Validation dwc:maximumElevationInMeters In Range
https://rs.tdwg.org/bdqtest/terms/c971fe3f-84c1-4636-9f44-b1ec31fd63c7/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:maximumElevationInMeters within the Parameter range?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumElevationInMeters is bdq:Empty or the value cannot be interpreted as a number; COMPLIANT if the value of dwc:maximumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:maximumElevationInMeters

#### Parameters

bdq:minimumValidElevationInMeters,bdq:maximumValidElevationInMeters

#### Default Parameter Values

bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"

#### Examples

dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:maximumElevation is in is range"

dwc:maximumElevationInMeters="-500": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:maximumElevation is not in range, i.e. is <-430"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

We have rounded up the Parameter values. We are aware of sub-ice elevations in Antarctica to -3,500m and possible sampling in the atmosphere above the elevation of the top of Mt Everest should fail this Test if captured as elevation rather than as distanceAboveSurfaceInMeters. Elevations below the maximum elevation yet above the local surface will be false positives.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_MINDEPTH_INRANGE

####  Validation dwc:minimumDepthInMeters In Range
https://rs.tdwg.org/bdqtest/terms/04b2c8f3-c71b-4e95-8e43-f70374c5fb92/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:minimumDepthInMeters within the Parameter range?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters is bdq:Empty, or the value is not interpretable as number greater than or equal to zero; COMPLIANT if the value of dwc:minimumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:minimumDepthInMeters

#### Parameters

bdq:minimumValidDepthInMeters,bdq:maximumValidDepthInMeters

#### Default Parameter Values

bdq:minimumValidDepthInMeters default="0",bdq:maximumValidDepthInMeters default="11000"

#### Examples

dwc:minimumDepthInMeters="1": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumDepthInMeters is in range"

dwc:minimumDepthInMeters="12000": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumDepthInMeters is not in range"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The Challenger Deep in the Mariana Trench is the deepest known point in Earth's oceans at 10,994 meters below sea level. We have rounded up bdq:maximumValidDepthInMeters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH

####  Validation dwc:minimumDepthInMeters Less Than dwc:maximumDepthInMeters
https://rs.tdwg.org/bdqtest/terms/8f1e6e58-544b-4365-a569-fb781341644e/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:minimumDepthInMeters a number less than or equal to the value of dwc:maximumDepthInMeters?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters is bdq:Empty, or if either are interpretable as not zero or a positive number; COMPLIANT if the value of dwc:minimumDepthInMeters is less than or equal to the value of dwc:maximumDepthInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:minimumDepthInMeters,dwc:maximumDepthInMeters

#### Examples

dwc:minimumDepthInMeters="0", dwc:maximumDepthInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumDepthInMeters = dwc:maximumDepthInMeters"

dwc:minimumDepthInMeters="1", dwc:maximumDepthInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumDepthInMeters > dwc:maximumDepthInMeters"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_MINELEVATION_INRANGE

####  Validation dwc:minimumElevationInMeters In Range
https://rs.tdwg.org/bdqtest/terms/0bb8297d-8f8a-42d2-80c1-558f29efe798/2023-09-17
Acts upon  SingleRecord

#### Description

Is the value of dwc:minimumElevationInMeters within the Parameter range?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:minimumElevationInMeters

#### Parameters

bdq:minimumValidElevationInMeters,bdq:maximumValidElevationInMeters

#### Default Parameter Values

bdq:minimumValidElevationInMeters default = "-430",bdq:maximumValidElevationInMeters default = "8850"

#### Examples

dwc:minimumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumElevationInMeters is IN_RANGE"

dwc:minimumElevationInMeters="-500": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumElevationInMeters is NOT_IN_RANGE (<-430)"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

We have rounded up the Parameter values. We are aware of sub-ice elevations in Antarctica to -3,500m and possible sampling in the atmosphere above the elevation of the top of Mt Everest should fail this Test if captured as elevation rather than as distanceAboveSurfaceInMeters. Elevations below the maximum elevation yet above the local surface will be false positives.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION

####  Validation dwc:minimumElevationInMeters Less Than dwcmaximumElevationInMeters
https://rs.tdwg.org/bdqtest/terms/d708526b-6561-438e-aa1a-82cd80b06396/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:minimumElevationInMeters a number less than or equal to the value of dwc:maximumElevationInMeters?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumlevationInMeters or dwc:minimumElevationInMeters is bdq:Empty, or if either is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is a number less than or equal to the value of the number dwc:maximumElevationInMeters, otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:minimumElevationInMeters,dwc:maximumElevationInMeters

#### Examples

dwc:minimumElevationInMeters="0", dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:minimumElevationInMeters is equal to dwc: maximumElevationInMeters"

dwc:minimumElevationInMeters="1", dwc:maximumElevationInMeters="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:minimumElevationInMeters is greater than dwc:maximumElevationInMeters"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_STATEPROVINCE_FOUND

####  Validation dwc:stateProvince Found
https://rs.tdwg.org/bdqtest/terms/4daa7986-d9b0-4dd5-ad17-2d7a771ea71a/2024-09-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:stateProvince occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:stateProvince is bdq:Empty; COMPLIANT if the value of dwc:stateProvince occurs as an administrative entity that is a child to at least one entity representing an ISO 3166 country-like entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:stateProvince

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[https://www.getty.edu/research/tools/vocabularies/tgn/index.html]}

#### Examples

dwc:stateProvince="Florida": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:stateProvince found in bdq:sourceAuthority"

dwc:stateProvince="Taswegian": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:stateProvince not found in bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Multiple values in the dwc:stateProvince field (whether to signify on a border or in a list of possibilities) will fail this Test. This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DAY_INRANGE

####  Validation dwc:day In Range
https://rs.tdwg.org/bdqtest/terms/8d787cb5-73e2-4c39-9cd1-67c7361dc02e/2024-09-16
Acts upon  SingleRecord

#### Description

Is the value of dwc:day interpretable as a valid integer between 1 and 28 inclusive, or is it validly 29, 30 or 31 given the dwc:month and dwc:year?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:day is bdq:Empty, or (2) dwc:day is not interpretable as an integer, or (3) dwc:day is interpretable as an integer between 29 and 31 inclusive and dwc:month is not interpretable as an integer between 1 and 12, or (4) dwc:month is interpretable as the integer 2 and dwc:day is interpretable as the integer 29 and dwc:year is not interpretable as a valid ISO 8601 year; COMPLIANT if (1) the value of dwc:day is interpretable as an integer between 1 and 28 inclusive, or (2) dwc:day is interpretable as an integer between 29 and 30 and dwc:month is interpretable as an integer in the set (4,6,9,11), or (3) dwc:day is interpretable as an integer between 29 and 31 and dwc:month is interpretable as an integer in the set (1,3,5,7,8,10,12), or (4) dwc:day is interpretable as the integer 29 and dwc:month is interpretable as the integer 2 and dwc:year is interpretable as is a valid leap year (evenly divisible by 400 or (evenly divisible by 4 but not evenly divisible by 100)); otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:day,dwc:month,dwc:year

#### Examples

dwc:day="15", dwc:month="", dwc:year="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day is in range"

dwc:day="30", dwc:month="2", dwc:year="1952": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day is not in range"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

This Test must take into account the given month and year, if present, to account for leap years. This is part of a group of similar Tests (VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e, #VALIDATION_STARTDAYOFYEAR_INRANGE (85803c7e-2a5a-42e1-b8d3-299a44cafc46), VALIDATION_ENDDAYOFYEAR_INRANGE9a39d88c-7eee-46df-b32a-c109f9f81fb8)).

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DAY_STANDARD

####  Validation dwc:day Standard
https://rs.tdwg.org/bdqtest/terms/47ff73ba-0028-4f79-9ce1-ee7008d66498/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:day an integer between 1 and 31 inclusive?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:day

#### Examples

dwc:day="15": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day is in range"

dwc:day="32": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day is not in range"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

This is part of a group of similar Tests (VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e), VALIDATION_STARTDAYOFYEAR_INRANGE (85803c7e-2a5a-42e1-b8d3-299a44cafc46), VALIDATION_ENDDAYOFYEAR_INRANGE (9a39d88c-7eee-46df-b32a-c109f9f81fb8)).

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_ENDDAYOFYEAR_INRANGE

####  Validation dwc:endDayOfYear In Range
https://rs.tdwg.org/bdqtest/terms/9a39d88c-7eee-46df-b32a-c109f9f81fb8/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:endDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is bdq:Empty or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:endDayOfYear

Consulted: 
dwc:eventDate

#### Examples

dwc:eventDate="1949-01-15T12:34/1949-01-20T17:00", dwc:endDayOfYear="20": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:endDayOfYear is in range"

dwc:eventDate="", dwc:endDayOfYear="x": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:endDayOfYear is ambiguous, either "X" or "No data" or "10"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

See Test VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e). This Test only asks if dwc:endDayOfYear is a valid value for the relevant year, not if it is consistent with the end day of the range specified in dwc:eventDate. In a non-leap year, the valid range is 1-365 inclusive, in a leap year 366 is also valid. This Test should be run after the series of Tests that assure that dwc:eventDate is populated, if possible (i.e., AMENDMENT_EVENTDATE_FROM_VERBATIM (6d0a0c10-5e4a-4759-b448-88932f399812), AMENDMENT_EVENTDATE_STANDARDIZED (718dfc3c-cb52-4fca-b8e2-0e722f375da7), and AMENDMENT_EVENT_DATE_FROM_YEARMONTHDAY (3892f432-ddd0-4a0a-b713-f2e2ecbd879d)).

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_EVENTDATE_INRANGE

####  Validation dwc:eventDate In Range
https://rs.tdwg.org/bdqtest/terms/3cff4dc4-72e9-4abe-9bf3-8a30f1618432/2024-09-16
Acts upon  SingleRecord

#### Description

Is the value of dwc:eventDate entirely with the Parameter range?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the range of dwc:eventDate is entirely within the range bdq:earliestValidDate to bdq:latestValidDate, inclusive, otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:eventDate

#### Parameters

bdq:earliestValidDate,bdq:latestValidDate

#### Default Parameter Values

bdq:earliestValidDate default ="1582-11-15",bdq:latestValidDate default = "{current year}"

#### Examples

dwc:eventDate="1962-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate is IN_RANGE"

dwc:eventDate="2300-11-01T10:00": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate is NOT_IN_RANGE"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

This Test provides for a default earliest date, which is 1582-11-15 by convention. That date was chosen because ISO 8601-1 asserts that "the use of proleptic Gregorian calendar dates prior are not allowed in ISO 8601-1 without prior agreement of the parties exchanging data", and Darwin Core does not comment on this. Different calendars have been used at different times in different places, and the transcription of an original date in one calendar into dwc:eventDate, where a Gregorian Calendar is assumed, may or may not have been done with the correct translation of the date, and metadata may or not be present to even identify such records. Given the complexity, and ongoing nature of transitions between calendars, we do not advocate using this Test for quality assurance by selecting a transition date and using it as a threshold.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_EVENTDATE_NOTEMPTY

####  Validation dwc:eventDate Not Empty
https://rs.tdwg.org/bdqtest/terms/f51e15a6-a67d-4729-9c28-3766299d2985/2023-09-17
Acts upon  SingleRecord

#### Description

Is there a value in dwc:eventDate?

#### Specification

COMPLIANT if dwc:eventDate is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:eventDate

#### Examples

dwc:eventDate="1964-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventdate is bdq:NotEmpty"

dwc:eventDate="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate is bdq:Empty"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_EVENTDATE_STANDARD

####  Validation dwc:eventDate Standard
https://rs.tdwg.org/bdqtest/terms/4f2bf8fd-fc5c-493f-a44c-e7b16153c803/2024-09-16
Acts upon  SingleRecord

#### Description

Is the value of dwc:eventDate a valid ISO date?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; COMPLIANT if the value of dwc:eventDate is a valid ISO 8601 date; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:eventDate

#### Examples

dwc:eventDate="1963-03-08T14": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate contains a valid ISO 8601-1:2019 date"

dwc:eventDate="1963-03-08T14:67-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:eventDate does not contain a valid ISO 8601-1:2019 date"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

This Test should also pick up issues such as 29 Feb in a non-leap year.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_EVENTTEMPORAL_NOTEMPTY

####  Validation dwc:Event Temporal Not Empty
https://rs.tdwg.org/bdqtest/terms/41267642-60ff-4116-90eb-499fee2cd83f/2023-09-30
Acts upon  SingleRecord

#### Description

Is there a value in any of the terms dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate?

#### Specification

COMPLIANT if any of dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate are bdq:NotEmpty; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:eventDate,dwc:year,dwc:month,dwc:day,dwc:startDayOfYear,dwc:endDayOfYear,dwc:verbatimEventDate

#### Examples

dwc:day="", dwc:month="", dwc:year="", dwc:eventDate="1962-11-01T10:00-0600", dwc:verbatimEventDate="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:eventDate is bdq:NotEmpty"

dwc:dateIdentified="", dwc:day="", dwc:month="", dwc:year="", dwc:eventDate="", dwc:verbatimEventDate="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All input fields bdq:Empty"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Only fails if all of the relevant fields of the Darwin Core Event class are bdq:Empty or do not exist. Relevant Darwin Core fields include dwc:eventDate, dwc:verbatimEventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear. The terms dwc:eventID (if populated may or may not point to temporal information accessible to the user of the data) and dwc:eventTime (which is rare) are not included.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_EVENT_CONSISTENT

####  Validation dwc:Event Consistent
https://rs.tdwg.org/bdqtest/terms/5618f083-d55a-4ac2-92b5-b9fb227b832f/2023-09-18
Acts upon  SingleRecord

#### Description

Are the values in dwc:eventDate consistent with the values in dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty, or all of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear are bdq:Empty; COMPLIANT if all of the following conditions are met (1) dwc:year is bdq:Empty or dwc:eventDate has a precision of one year or finer and and is within a single year and the provided value of dwc:year matches the year expressed in dwc:eventDate, and (2) dwc:month is bdq:Empty or dwc:eventDate has a precision of one month or finer and is within a single month and the provided value in dwc:month matches the month represented by dwc:eventDate, and (3) dwc:day is bdq:Empty or dwc:eventDate has a precision of a day or less and is within a single day and the provided value in dwc:day matches the day represented by dwc:eventDate, and (4) dwc:startDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:startDayOfYear matches the start day of the year of the range represented by dwc:eventDate, and (5) dwc:endDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:endDayOfYear matches the end day of the year of the range represented by dwc:eventDate; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:eventDate,dwc:day,dwc:month,dwc:year,dwc:startDayOfYear,dwc:endDayOfYear

#### Examples

dwc:day="15", dwc:month="9", dwc:year="1949", dwc:eventDate="1949-09-15T12:34", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:day, dwc:month and dwc:year match dwc:eventDate"

dwc:day="15", dwc:month="9", dwc:year="1949", dwc:eventDate="1949-09-16T12:34", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:day does not match dwc:eventDate"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

This Test does not take a position on whether the value in dwc:eventDate, or the values in the atomic terms are correct, it simply points out the presence of inconsistencies. For this Test, dwc:eventTime is explicitly ignored. It may be useful to consider an additional Test that does evaluate dwc:eventTime and dwc:eventDate. In that case, but not in this Test, if the time is present in both dwc:eventDate and dwc:eventTime, and it is inconsistent, it may indicate an error in the dwc:eventDate, thus making it a problem that someone needs to evaluate. This Test will only assert consistency if the data are both internally consistent and are compliant with the term definitions, for example dwc:day, by its definition, can only be the day of an dwc:eventDate that has a precision of a day or better and is not a range that spans more than a single day. A dwc:day that was internally consistent with the first day of the year (that is, 1) of an dwc:eventDate that only had precision to a year would be consistent internally, but not consistent with the Darwin Core term definitions, and would not return COMPLIANT from this Test.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_MONTH_STANDARD

####  Validation dwc:month Standard
https://rs.tdwg.org/bdqtest/terms/01c6dafa-0886-4b7e-9881-2c3018c98bdc/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:month interpretable as an integer between 1 and 12 inclusive?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; COMPLIANT if the value of dwc:month is interpretable as an integer between 1 and 12 inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:month

#### Examples

dwc:month="10": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:month is in range"

dwc:month="v": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:month is ambiguous as "v" or "5""


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_STARTDAYOFYEAR_INRANGE

####  Validation dwc:startDayOfYear In Range
https://rs.tdwg.org/bdqtest/terms/85803c7e-2a5a-42e1-b8d3-299a44cafc46/2023-09-18
Acts upon  SingleRecord

#### Description

Is the value of dwc:startDayOfYear an integer between 1 and 365 inclusive, or 366 if a leap year?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:startDayOfYear is bdq:Empty or if the value of dwc:startDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find single year or a start year in a range); COMPLIANT if the value of dwc:startDayOfYear is an integer between 1 and 365, inclusive, or if the value of dwc:startDayOfYear is 366 and the start year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:startDayOfYear

Consulted: 
dwc:eventDate

#### Examples

dwc:eventDate="", dwc:startDayOfYear="15": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:startDayOfYear is in range"

dwc:eventDate="", dwc:startDayOfYear="0": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:startDayOfYear is not in range"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

See Test VALIDATION_DAY_INRANGE (8d787cb5-73e2-4c39-9cd1-67c7361dc02e). This Test only asks if dwc:startDayOfYear is a valid value for the relevant year, not if it is consistent with the start day of the range specified in dwc:eventDate. In a non-leap year, the valid range is 1-365 inclusive, in a leap year 366 is also valid. This Test should be run after the series of Tests that assure that dwc:eventDate is populated, if possible (i.e., AMENDMENT_EVENTDATE_FROM_VERBATIM (6d0a0c10-5e4a-4759-b448-88932f399812), AMENDMENT_EVENTDATE_STANDARDIZED (718dfc3c-cb52-4fca-b8e2-0e722f375da7), and AMENDMENT_EVENT_DATE_FROM_YEARMONTHDAY (3892f432-ddd0-4a0a-b713-f2e2ecbd879d)).

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_YEAR_INRANGE

####  Validation dwc:year In Range
https://rs.tdwg.org/bdqtest/terms/ad0c8855-de69-4843-a80c-a5387d20fbc8/2024-08-23
Acts upon  SingleRecord

#### Description

Is the value of dwc:year within the Parameter range?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:year is bdq:Empty or cannot be interpreted as an integer; COMPLIANT if the value of dwc:year is within the range bdq:earliestValidDate to bdq:latestValidDate inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:year

#### Parameters

bdq:earliestValidDate,bdq:latestValidDate

#### Default Parameter Values

bdq:earliestValidDate default = "1582",bdq:latestValidDate default = "{current year}"

#### Examples

dwc:year="1952": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:year is in RANGE"

dwc:year="9999": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:year is not in RANGE. The value in year has not yet come to pass."


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The results of this Test are time-dependent. Next year is not valid now. Next year it will be. This Test provides the option to designate lower and upper limits to the year. The upper limit, if not provided, should default to the year when the Test is run. This Test provides for a default earliest date (year), of 1582 by convention. That value was chosen because ISO 8601-1 asserts that "the use of proleptic Gregorian calendar dates prior are not allowed in ISO 8601-1 without prior agreement of the parties exchanging data", and Darwin Core provides no such prior agreement.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_YEAR_NOTEMPTY

####  Validation dwc:year Not Empty
https://rs.tdwg.org/bdqtest/terms/c09ecbf9-34e3-4f3e-b74a-8796af15e59f/2023-09-17
Acts upon  SingleRecord

#### Description

Is there a value in dwc:year?

#### Specification

COMPLIANT if dwc:year is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:year

#### Examples

dwc:year="1949": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:year is bdq:NotEmpty"

dwc:year="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:year is bdq:Empty"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DATEIDENTIFIED_INRANGE

####  Validation dwc:dateIdentified In Range
https://rs.tdwg.org/bdqtest/terms/dc8aae4b-134f-4d75-8a71-c4186239178e/2024-09-16
Acts upon  SingleRecord

#### Description

Is the value of dwc:dateIdentified within Parameters range and does it overlap with or is it later than dwc:eventDate?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:dateIdentified is bdq:Empty, or (2) dwc:dateIdentified contains an invalid value according to ISO 8601, or (3) bdq:includeEventDate=true and dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the value of dwc:dateIdentified is between bdq:earliestValidDate and bdq:latestValidDate inclusive and either (1) dwc:eventDate is bdq:Empty or bdq:includeEventDate=false, or (2) if dwc:eventDate is a valid ISO 8601 date and dwc:dateIdentified overlaps or is later than the dwc:eventDate; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:dateIdentified

Consulted: 
dwc:eventDate

#### Parameters

bdq:earliestValidDate,bdq:latestValidDate,bdq:includeEventDate

#### Default Parameter Values

bdq:earliestValidDate default = "1753-01-01",bdq:latestValidDate default = "{current day}",bdq:includeEventDate default = "true"

#### Examples

dwc:dateIdentified="1963-03-08T14:07-0600", dwc:eventDate="1962-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:dateIdentified is in range"

dwc:dateIdentified="1963-03-08T14:07-0600", dwc:eventDate="1964-11-01T10:00-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:dateIdentified before dwc:eventDate"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

There may be valid identifications prior to Linnaeus, but this Test will flag these under the default value of bdq:earliestValidDate, as for most biodiversity data, pre-Linnaean identification dates are likely to be errors. If a parameter is not set, then the default is 1753-01-01. This Test will, by design, flag as problematic cases (such as LTER plots and marine mammal sightings) where a known individual organism is identified by a specialist and then subsequently observed without new taxonomic identifications being made.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DATEIDENTIFIED_STANDARD

####  Validation dwc:dateIdentified Standard
https://rs.tdwg.org/bdqtest/terms/66269bdd-9271-4e76-b25c-7ab81eebe1d8/2024-09-16
Acts upon  SingleRecord

#### Description

Is the value of dwc:dateIdentified a valid ISO date?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; COMPLIANT if the value of dwc:dateIdentified contains a valid ISO 8601 date; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:dateIdentified

#### Examples

dwc:dateIdentified="1963-03-08T14:07": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:dateIdentified is a valid ISO 8601-1:2019 date"

dwc:dateIdentified="1963-03-08X14:07-0600": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:dateIdentified is not a valid ISO 8601-1:2019 date"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_DEGREEOFESTABLISHMENT_STANDARD

####  Validation dwc:degreeofEstablishment Standard
https://rs.tdwg.org/bdqtest/terms/060e7734-607d-4737-8b2c-bfa17788bf1a/2024-02-09
Acts upon  SingleRecord

#### Description

Does the value of dwc:degreeOfEstablishment occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; COMPLIANT if the value of dwc:degreeOfEstablishment is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:degreeOfEstablishment

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}

#### Examples

dwc:degreeOfEstablishment="cultivated": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:degreeOfEstablishment found in the bdq:sourceAuthority"

dwc:degreeOfEstablishment="grown in garden": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:degreeOfEstablishment not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species

#### Notes

This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_ESTABLISHMENTMEANS_STANDARD

####  Validation dwc:establishmentMeans Standard
https://rs.tdwg.org/bdqtest/terms/4eb48fdf-7299-4d63-9d08-246902e2857f/2024-02-08
Acts upon  SingleRecord

#### Description

Does the value of dwc:establishmentMeans occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; COMPLIANT if the value of dwc:establishmentMeans is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:establishmentMeans

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}

#### Examples

dwc:establishmentMeans="native": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:establishmentMeans found in the bdq:sourceAuthority"

dwc:establishmentMeans="cultivated": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:establishmentMeans not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_OCCURRENCEID_NOTEMPTY

####  Validation dwc:occurrenceID Not Empty
https://rs.tdwg.org/bdqtest/terms/c486546c-e6e5-48a7-b286-eba7f5ca56c4/2023-09-17
Acts upon  SingleRecord

#### Description

Is there a value in dwc:occurrenceID?

#### Specification

COMPLIANT if dwc:occurrenceID is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:occurrenceID

#### Examples

dwc:occurrenceID="https://www.inaturalist.org/observations/43047701": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceID conforms to GUID structure"

dwc:occurrenceID="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceID is bdq:Empty"


#### Use Cases

bdq:Record-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_OCCURRENCESTATUS_NOTEMPTY

####  Validation dwc:occurrenceStatus Not Empty
https://rs.tdwg.org/bdqtest/terms/eb4a17f6-6bea-4cdd-93dd-d5a7e9d1eccf/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:occurrenceStatus?

#### Specification

COMPLIANT if dwc:occurrenceStatus is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:occurrenceStatus

#### Examples

dwc:occurrenceStatus="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceStatus is bdq:NotEmpty"

dwc:occurrenceStatus="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceStatus is bdq:Empty"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_OCCURRENCESTATUS_STANDARD

####  Validation dwc:occurrenceStatus Standard
https://rs.tdwg.org/bdqtest/terms/7af25f1e-a4e2-4ff4-b161-d1f25a5c3e47/2025-02-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:occurrenceStatus occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:Empty; COMPLIANT if the value of dwc:occurrenceStatus is resolved in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:occurrenceStatus

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Regex present/absent" {["^(present\

#### Examples

dwc:occurrenceStatus="present": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:occurrenceStatus matches a term in the bdq:sourceAuthority"

dwc:occurrenceStatus="presence": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:occurrenceStatus does not match a term in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

The recommended controlled vocabulary for this term consists of "present" and "absent", which are the only two appropriate terms for a Darwin Core Occurrence. This is reflected in the dwc:occurrenceStatus vocabulary for this Test. There is currently a mismatch between the (authoritative) lower case values at https://dwc.tdwg.org/terms/#dwc:occurrenceStatus and the vocabulary at GBIF (https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts), which capitalized the first character. This Test must return NOT_COMPLIANT if there are case differences, leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_PATHWAY_STANDARD

####  Validation dwc:pathway Standard
https://rs.tdwg.org/bdqtest/terms/5424e933-bee7-4125-839e-d8743ea69f93/2024-02-09
Acts upon  SingleRecord

#### Description

Does the value of dwc:pathway occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; COMPLIANT if the value of dwc:pathway is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:pathway

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}

#### Examples

dwc:pathway="transportStowaway": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:pathway found in the bdq:sourceAuthority"

dwc:pathway="escapee": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:pathway not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_SEX_STANDARD

####  Validation dwc:sex Standard
https://rs.tdwg.org/bdqtest/terms/88d8598b-3318-483d-9475-a5acf9887404/2024-02-09
Acts upon  SingleRecord

#### Description

Does the value of dwc:sex occur in bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; COMPLIANT if the value of dwc:sex is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:sex

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}

#### Examples

dwc:sex="Male": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:sex found in the bdq:sourceAuthority"

dwc:sex="f": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:sex not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters. For reference, a list of synonyms for dwc:sex values can be found at https://registry.gbif.org/vocabulary/Sex/concepts.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_TYPESTATUS_STANDARD

####  Validation dwc:typeStatus Standard
https://rs.tdwg.org/bdqtest/terms/4833a522-12eb-4fe0-b4cf-7f7a337a6048/2024-11-11
Acts upon  SingleRecord

#### Description

Does the value of dwc:typeStatus occur in bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; COMPLIANT if the value of the first word in each &#124; delimited portion of dwc:typeStatus is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:typeStatus

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF TypeStatus Vocabulary" {[https://api.gbif.org/v1/vocabularies/TypeStatus]} {dwc:typeStatus vocabulary API [https://api.gbif.org/v1/vocabularies/TypeStatus/concepts]}

#### Examples

dwc:typeStatus="Holotype": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:typeStatus found in the bdq:sourceAuthority"

dwc:typeStatus="cleptotype": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:typeStatus not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_CLASSIFICATION_CONSISTENT

####  Validation Classification Consistent
https://rs.tdwg.org/bdqtest/terms/2750c040-1d4a-4149-99fe-0512785f2d5f/2023-09-18
Acts upon  SingleRecord

#### Description

Is the combination of higher classification taxonomic terms consistent using bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of the fields dwc:kingdom dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus are bdq:Empty; COMPLIANT if the combination of values of higher classification taxonomic terms (dwc:kingdom, dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus) are consistent with the lowest ranking matched element in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="Myrtales", dwc:superfamily="", dwc:family="Myrtaceae", dwc:subfamily="", dwc:tribe="", dwc:subtribe="",dwc:genus="Punica": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="The combination of values of higher classification taxonomic terms can be unambiguously resolved in the bdq:sourceAuthority"

dwc:kingdom="", dwc:phylum="Chordata", dwc:class="", dwc:order="Rhopalocera", dwc:superfamly="", dwc:family="Muricidae", dwc:subfamily="", dwc:tribe="", dwc:subtribe="", dwc:genus="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="The combination of values of higher classification taxonomic terms cannot be unambiguously resolved in the bdq:sourceAuthority"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

A fail condition may arise either from the taxon terms being internally inconsistent (not all of the information can be true at the same time), or from the vocabulary being incapable of resolving the combination of classification values. Additional Tests could be devised against a taxonomic authority to report the distinct failure conditions. This Test specifically does not consider the content of dwc:higherClassification.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_CLASS_FOUND

####  Validation dwc:class Found
https://rs.tdwg.org/bdqtest/terms/2cd6884e-3d14-4476-94f7-1191cfff309b/2023-09-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:class occur at the rank of Class in bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:class is bdq:Empty; COMPLIANT if the value of dwc:class is found as a value at the rank of Class in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:class

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:class="Insecta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:class has an equivalent at the rank of Class in the bdq:sourceAuthority"

dwc:class="Magnoleopsida": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT,Response.comment="dwc:class does not have an equivalent at the rank of Class in the bdq:sourceAuthority"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_FAMILY_FOUND

####  Validation dwc:family Found
https://rs.tdwg.org/bdqtest/terms/3667556d-d8f5-454c-922b-af8af38f613c/2023-09-17
Acts upon  SingleRecord

#### Description

Does the value of dwc:family occur at the rank of Family in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:family is bdq:Empty; COMPLIANT if the value of dwc:family is found as a value at the rank of Family in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:family

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:family="Agaricaceae": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="bdq:family has an equivalent at the rank of Family in the bdq:sourceAuthority"

dwc:family="Agaricacae": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="bdq:family does not have an equivalent at the rank of Family in the Parameterized Source Authority"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_GENUS_FOUND

####  Validation dwc:genus Found
https://rs.tdwg.org/bdqtest/terms/f2ce7d55-5b1d-426a-b00e-6d4efe3058ec/2023-09-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:genus occur at the rank of Genus in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:genus is bdq:Empty; COMPLIANT if the value of dwc:genus is found as a value at the rank of genus in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:genus

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:genus="Egernia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:genus has an equivalent at the rank of Genus in the Parameterized Source Authority"

dwc:genus="Egernea": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:genus does not have an equivalent at the rank of Genus in the bdq:sourceAuthority. This may be fixed using fuzzy matching at the AMENDMENT stage"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_KINGDOM_FOUND

####  Validation dwc:kingdom Found
https://rs.tdwg.org/bdqtest/terms/125b5493-052d-4a0d-a3e1-ed5bf792689e/2023-09-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:kingdom occur at the rank of Kingdom in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:kingdom is bdq:Empty; COMPLIANT if the value of dwc:kingdom is found as a value at the rank of kingdom in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:kingdom

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:kingdom="Animalia": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:kingdom has an equivalent at the rank of Kingdom in the bdq:sourceAuthority"

dwc:kingdom="Metazoa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:kingdom does not strictly have an equivalent at the rank of Kingdom in the Parameterized Source Authority (Metazoa is synonym of Animalia)"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_KINGDOM_NOTEMPTY

####  Validation dwc:kingdom Not Empty
https://rs.tdwg.org/bdqtest/terms/36ed36c9-b1a7-40b2-b5e2-0d012e772098/2024-01-28
Acts upon  SingleRecord

#### Description

Is there a value in dwc:kingdom?

#### Specification

COMPLIANT if dwc:kingdom is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:kingdom

#### Examples

dwc:kingdom="Fungi": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:kingdom is bdq:NotEmpty"

dwc:kingdom="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:kingdom is bdq:Empty"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY

####  Validation dwc:namePublishedInYear Not Empty
https://rs.tdwg.org/bdqtest/terms/ff59f77d-71e9-4eb1-aac9-8bd05c50ff70/2024-02-07
Acts upon  SingleRecord

#### Description

Is there a value in dwc:namePublishedInYear?

#### Specification

COMPLIANT if dwc:namePublishedInYear is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:namePublishedInYear

#### Examples

dwc:namePublishedInYear="2024": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:namePublishedInYear is bdq:NotEmpty"

dwc:namePublishedInYear="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:namePublishedInYear is bdq:Empty"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_ORDER_FOUND

####  Validation dwc:order Found
https://rs.tdwg.org/bdqtest/terms/81cc974d-43cc-4c0f-a5e0-afa23b455aa3/2023-09-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:order occur at the rank of Order in bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:order is bdq:Empty; COMPLIANT if the value of dwc:order is found as a value at the rank of Order in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:order

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:order="Lepidoptera": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:order has an equivalent at the rank of Order in the bdq:sourceAuthority"

dwc:order="Nymphalidae": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:order does not have an equivalent at the rank of Order in the bdq:sourceAuthority. Nymphalidae is a family, not an order"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_PHYLUM_FOUND

####  Validation dwc:phylum Found
https://rs.tdwg.org/bdqtest/terms/eaad41c5-1d46-4917-a08b-4fd1d7ff5c0f/2022-03-25
Acts upon  SingleRecord

#### Description

Does the value of dwc:phylum occur at the rank of Phylum in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdq:Empty; COMPLIANT if the value of dwc:phylum is found as a value at the rank of Phylum in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:phylum

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:phylum="Tracheophyta": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:phylum has an equivalent at the rank of Phylum in the bdq:sourceAuthority. GBIF.org uses Trachyophyta for the Phylum including ferns"

dwc:phylum="Trachyophyta": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:phylum does not have an equivalent at the rank of Phylum in the bdq:sourceAuthority."


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

The purpose of this Test is to check whether the value is a name that is a result of a nomenclatural act at this rank. This excludes unpublished names, misspellings and vernacular names. It is expected that the Test will designate the source authority against which to check. The same Test might return distinct results when using distinct source authorities.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_POLYNOMIAL_CONSISTENT

####  Validation Polynomial Consistent
https://rs.tdwg.org/bdqtest/terms/17f03f1f-f74d-40c0-8071-2927cfc9487b/2023-09-18
Acts upon  SingleRecord

#### Description

Is the polynomial represented in dwc:scientificName consistent with the equivalent values in dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty, or all of dwc:genericName, dwc:specificEpithet and dwc:infraspecificEpithet are bdq:Empty; COMPLIANT if the polynomial, as represented in dwc:scientificName, is consistent with bdq:NotEmpty values of dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:scientificName,dwc:genericName,dwc:specificEpithet,dwc:infraspecificEpithet

#### Examples

dwc:scientificName="Hakea decurrens ssp. physocarpa", dwc:genericName="", dwc:specificEpithet="decurrens", dwc:infraspecificEpithet="physocarpa": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="Values of all non-empty atomic terms are found in the polynomial"

dwc:scientificName="Hakea decurrens", dwc:genericName="Hakea", dwc:specificEpithet="decurrens", dwc:infraspecificEpithet="physocarpa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is inconsistent with atomic parts (dwc:genus, dwc:specificEpithet and dwc:infraspecificEpithet)"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

If dwc:specificEpithet is populated then this Test expects that the value dwc:specificEpithet is the name of the second or species epithet of the scientificName. If dwc:genericName is populated, this Test expects that the value of dwc:genus is the first word of the value of dwc:scientificName. If dwc:specificEpithet is populated then this Test expects that the value dwc:specificEpithet is the name of the first or species epithet of the scientificName. If dwc:infraspecificEpithet is populated, then this Test expects that the value of dwc:infraspecificEpithet is the name of the lowest or terminal infraspecific epithet of the scientificName, excluding any rank designation.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY

####  Validation dwc:scientificNameAuthorship Not Empty
https://rs.tdwg.org/bdqtest/terms/49f1d386-5bed-43ae-bd43-deabf7df64fc/2024-02-04
Acts upon  SingleRecord

#### Description

Is there a value in dwc:scientificNameAuthorship?

#### Specification

COMPLIANT if dwc:scientificNameAuthorship is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:scientificNameAuthorship

#### Examples

dwc:scientificNameAuthorship="(Györfi, 1952)": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameAuthorship is bdq:NotEmpty"

dwc:scientificNameAuthorship="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameAuthorship is bdq:Empty"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_SCIENTIFICNAMEID_COMPLETE

####  Validation dwc:scientificNameID Complete
https://rs.tdwg.org/bdqtest/terms/6eeac3ed-f691-457f-a42e-eaa9c8a71ce8/2023-09-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:scientificNameID contain a complete identifier?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty; COMPLIANT if (1) dwc:scientificNameID is a validly formed LSID, or (2) dwc:scientificNameID is a validly formed URN with at least NID and NSS present, or (3) dwc:scientificNameID is in the form scope:value, or (4) dwc:scientificNameID is a validly formed URI with host and path where path consists of more than just "/"; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:scientificNameID

#### Examples

dwc:scientificNameID="urn:lsid:zoobank.org:act:17ADF24F-027F-44F6-9543-D3D0260CE79E": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameID contains a URI and a namespace indicator"

dwc:scientificNameID="Hakea decurrens ssp. physocarpa": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameID does not contain a URI"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

If any single bdq:sourceAuthority such as GBIF is used, a valid and complete dwc:scientificNameID based on an alternative source authority is unlikely to provide a valid match. A text or number string as a namespace indicator without a URI will be ambiguous. As an example, GBIF's backbone taxonomy dataset can be found at https://doi.org/10.15468/39omei. When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID. Note that GBIF currently uses "TaxonID" for this entity. The terms NID, NSS, and URN are all Uniform Resource Identifiers - see the Wikipedia (2024) reference.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_SCIENTIFICNAMEID_NOTEMPTY

####  Validation dwc:scientificNameID Not Empty
https://rs.tdwg.org/bdqtest/terms/401bf207-9a55-4dff-88a5-abcd58ad97fa/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:scientificNameID?

#### Specification

COMPLIANT if dwc:scientificNameID is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:scientificNameID

#### Examples

dwc:scientificNameID="8fa58e08-08de-4ac1-b69c-1235340b7001": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificNameID is bdq:NotEmpty"

dwc:scientificNameID=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificNameID is bdq:Empty"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_SCIENTIFICNAME_FOUND

####  Validation dwc:scientificName Found
https://rs.tdwg.org/bdqtest/terms/3f335517-f442-4b98-b149-1e87ff16de45/2023-09-17
Acts upon  SingleRecord

#### Description

Is there a match of the contents of dwc:scientificName with the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty; COMPLIANT if there is a match of the contents of dwc:scientificName in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:scientificName

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:scientificName="Eucalyptus camaldulensis": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName found in the bdq:sourceAuthority"

dwc:scientificName="Capulus intort": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName was not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

The purpose of this Test is to detect errors in the scientific name but is dependent on the abilities of the parsing of the bdq:sourceAuthority. For research users of biodiversity data doing quality assurance, VALIDATION_TAXON_UNAMBIGUOUS (4c09f127-737b-4686-82a0-7c8e30841590) handles their needs, but for curators of datasets doing quality control, this Test provides a specific subset of targeted data cleaning, making it a valuable Test to include for the quality control case.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_SCIENTIFICNAME_NOTEMPTY

####  Validation dwc:scientificName Not Empty
https://rs.tdwg.org/bdqtest/terms/7c4b9498-a8d9-4ebb-85f1-9f200c788595/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:scientificName?

#### Specification

COMPLIANT if dwc:scientificName is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:scientificName

#### Examples

dwc:scientificName="?": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName is bdq:NotEmpty"

dwc:scientificName="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName is bdq:Empty"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_TAXONRANK_NOTEMPTY

####  Validation dwc:taxonRank Not Empty
https://rs.tdwg.org/bdqtest/terms/14da5b87-8304-4b2b-911d-117e3c29e890/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:taxonRank?

#### Specification

COMPLIANT if dwc:taxonRank is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:taxonRank

#### Examples

dwc:taxonRank="genus": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:taxonRank is bdq:NotEmpty"

dwc:taxonRank=" ": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:taxonRank is bdq:Empty"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_TAXONRANK_STANDARD

####  Validation dwc:taxonRank Standard
https://rs.tdwg.org/bdqtest/terms/7bdb13a4-8a51-4ee5-be7f-20693fdb183e/2023-09-18
Acts upon  SingleRecord

#### Description

Does the value of dwc:taxonRank occur in the bdq:sourceAuthority?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; COMPLIANT if the value of dwc:taxonRank is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
dwc:taxonRank

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}

#### Examples

dwc:taxonRank="kingdom": Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:taxonRank has an equivalent in the bdq:sourceAuthority"

dwc:taxonRank="sp.": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:taxonRank does not have an equivalent in the bdq:sourceAuthority"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

This Test must return NOT_COMPLIANT if there is leading or trailing whitespace or there are leading or trailing non-printing characters.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_TAXON_NOTEMPTY

####  Validation dwc:Taxon Not Empty
https://rs.tdwg.org/bdqtest/terms/06851339-843f-4a43-8422-4e61b9a00e75/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in any of the terms needed to determine that the taxon exists?

#### Specification

COMPLIANT if at least one term needed to determine the taxon of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:taxonID,dwc:scientificNameID,dwc:acceptedNameUsageID,dwc:parentNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:scientificName,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:infragenericEpithet,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:vernacularName,dwc:cultivarEpithet

#### Examples

dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:parentNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Eucalyptus gunnii", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:superfamily="", dwc:tribe="", dwc:subtribe="",dwc:family="", dwc:genus="", dwc:subgenus="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:vernacularName="" : Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="at least enough terms exist that identify that an entity exists"

dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:parentNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:superfamily="", dwc:tribe="", dwc:subtribe="",dwc:family="", dwc:genus="", dwc:subgenus="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:vernacularName="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="All input fields are bdq:Empty or missing"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

This tests for records that have no taxonomic (NAME) information. If there is any value for any of the Information Elements, this may be useful information. See example.

[🠱](#indexes-to-the-tests)
********************

###  VALIDATION_TAXON_UNAMBIGUOUS

####  Validation dwc:Taxon Unambiguous
https://rs.tdwg.org/bdqtest/terms/4c09f127-737b-4686-82a0-7c8e30841590/2023-09-18
Acts upon  SingleRecord

#### Description

Can the taxon be unambiguously resolved from bdq:sourceAuthority using the available taxon terms?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of dwc:scientificNameID, dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, dwc:cultivarEpithet are bdq:Empty; COMPLIANT if (1) dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority, or (2) dwc:scientificNameID is bdq:Empty and dwc:scientificName references a single taxon record in the bdq:sourceAuthority, or (3) if dwc:scientificName and dwc:scientificNameID are bdq:Empty and if a combination of the values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:cultivarEpithet, dwc:taxonRank, and dwc:scientificNameAuthorship can be unambiguously resolved to a unique taxon in the bdq:sourceAuthority, or (4) if ambiguity produced by multiple matches in (2) or (3) can be disambiguated to a unique Taxon using the values of dwc:tribe, dwc:subtribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID and dwc:vernacularName; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
dwc:taxonID,dwc:scientificName,dwc:scientificNameID,dwc:acceptedNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:infragenericEpithet,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:cultivarEpithet,dwc:vernacularName,dwc:scientificNameAuthorship,dwc:taxonRank

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Triplex rosaria Perry, 1811", dwc:higherClassification="", dwc:kingdom="Animalia", dwc:phylum="mollusca", dwc:class="Gastropoda", dwc:order="", dwc:family="Muricidae", dwc:subfamily="", dwc:genus="Chicoreus", dwc:genericName="Triplex", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="rosarium", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="Perry, 1811", dwc:taxonRank="",bdq:sourceAuthority=”marinespecies.org”: Response.status=RUN_HAS_RESULT, Response.result=COMPLIANT, Response.comment="dwc:scientificName matched to unique taxon record in WoRMS, unique fuzzy match on name and exact match on authorship. "

dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Graphis", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:family="", dwc:subfamily="", dwc:genus="", dwc:genericName="", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="", dwc:taxonRank="": Response.status=RUN_HAS_RESULT, Response.result=NOT_COMPLIANT, Response.comment="dwc:scientificName="Graphis" is ambiguous as could be either a lichen or a gastropod."


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

There are any number of potential controlled vocabularies that might be used for this Test, including local vocabularies and taxon specific vocabularies. If dwc:scientificNameID is bdq:Empty, use dwc:scientificName and dwc:CultivarEpithet to search for a unique taxon. If dwc:scientificName is bdq:Empty, check with the terms that form atomic parts of it (dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:taxonRank, dwc:scientificNameAuthorship), and if more than one match is found, use the remaining terms to try to disambiguate to a single Taxon record. The terms dwc:subgenus, dwc:genus, dwc:family, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:scientificNameID,, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID should not be used to make a match if dwc:scientificNameID and dwc:scientificName or dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:taxonRank, dwc:scientificNameAuthorship are bdq:Empty. Note that Test VALIDATION_SCIENTIFICNAME_FOUND (4c09f127-737b-4686-82a0-7c8e30841590) is a more specific Test for a subset of Information Elements from this Test.

[🠱](#indexes-to-the-tests)
********************

###  MEASURE_AMENDMENTS_PROPOSED

####  Measure Amendments Proposed
https://rs.tdwg.org/bdqtest/terms/03049fe5-a575-404f-b564-ae63f5a1cf8b/2024-08-18
Acts upon  SingleRecord

#### Description

A count of the number of distinct AMENDMENT Tests that have a Response.status="AMENDED" for a given record.

#### Specification

The number of Tests of output type AMENDMENT that have been run against the record and have proposed changes to the record (Result.status="AMENDED")

#### Information Elements
Consulted: 
bdq:AllAmendmentTestsRunOnSingleRecord

#### Examples

Response.status=RUN_HAS_RESULT, Response.result="17", Response.comment="17 Tests of TYPE AMENDMENT were run and proposed changes to the record."


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

[🠱](#indexes-to-the-tests)
********************

###  MEASURE_VALIDATIONTESTS_COMPLIANT

####  Measure Validation Tests Compliant
https://rs.tdwg.org/bdqtest/terms/45fb49eb-4a1b-4b49-876f-15d5034dfc73/2024-08-18
Acts upon  SingleRecord

#### Description

Measures the number of distinct VALIDATION Tests that have a Response.status="COMPLIANT" for a given record.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if no Tests of type VALIDATION were attempted to be run; Report the number of Tests of output type VALIDATION run against the record that were COMPLIANT (passed)

#### Information Elements
Consulted: 
bdq:AllValidationTestsRunOnSingleRecord

#### Examples

Response.status=RUN_HAS_RESULT, Response.result="7", Response.comment="7 VALIDATION Tests had Response.status="COMPLIANT" 


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of Tests that were attempted, add all three measures. To get the total number of Tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).

[🠱](#indexes-to-the-tests)
********************

###  MEASURE_VALIDATIONTESTS_NOTCOMPLIANT

####  Measure Validation Tests Not Compliant
https://rs.tdwg.org/bdqtest/terms/453844ae-9df4-439f-8e24-c52498eca84a/2024-08-22
Acts upon  SingleRecord

#### Description

A count of the number of distinct VALIDATION Tests that have a Response.status="NOT_COMPLIANT" for a given record.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if no Tests of type VALIDATION were attempted to be run; REPORT of the number of Tests of output type VALIDATION run against the record that have Response.result="NOT_COMPLIANT"

#### Information Elements
Consulted: 
bdq:AllValidationTestsRunOnSingleRecord

#### Examples

Response.status=RUN_HAS_RESULT, Response.result="37", Response.comment="37 VALIDATION Tests had Response.status="NOT_COMPLIANT."


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of Tests that were attempted, add all three measures. To get the total number of Tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).

[🠱](#indexes-to-the-tests)
********************

###  MEASURE_VALIDATIONTESTS_PREREQUISITESNOTMET

####  Measure Validation Tests Prerequisites Not Met
https://rs.tdwg.org/bdqtest/terms/49a94636-a562-4e6b-803c-665c80628a3d/2024-08-18
Acts upon  SingleRecord

#### Description

The number of distinct VALIDATION Tests that have a Response.status="EXTERNAL_PREREQUISITES_NOT_MET" or "INTERNAL_PREREQUISITES_NOT_MET" for a given record.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if no Tests of type VALIDATION were run; Report the number of Tests of output type VALIDATION that did not run because prerequisites for those Tests were not met (Result.status="INTERNAL_PREREQUISITES_NOT_MET" or "EXTERNAL_PREREQUISITES_NOT_MET")

#### Information Elements
Consulted: 
bdq:AllValidationTestsRunOnSingleRecord

#### Examples

Response.status=RUN_HAS_RESULT, Response.result="27", Response.comment="27 VALIDATION Tests had either INTERNAL_PREREQUISITES_NOT_MET" or "EXTERNAL_PREREQUISITES_NOT_MET"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

We have three individual measures for pass (MEASURE_VALIDATIONTESTS_COMPLIANT (45fb49eb-4a1b-4b49-876f-15d5034dfc73)), fail (MEASURE_VALIDATIONTESTS_NOTCOMPLIANT (453844ae-9df4-439f-8e24-c52498eca84a)), and PREREQUISITES_NOT_MET (49a94636-a562-4e6b-803c-665c80628a3d). To get the total number of Tests that were attempted, add all three measures. To get the total number of Tests that ran, add NOT_COMPLIANT (fail) and COMPLIANT (pass).

[🠱](#indexes-to-the-tests)
********************

###  MEASURE_EVENTDATE_DURATIONINSECONDS

####  Measure dwc:eventDate Duration In Seconds
https://rs.tdwg.org/bdqtest/terms/56b6c695-adf1-418e-95d2-da04cad7be53/2024-09-16
Acts upon  SingleRecord

#### Description

What is the duration of dwc:eventDate in seconds?

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; otherwise RUN_HAS_RESULT with the result being the duration (sensu ISO 8601) expressed in the dwc:eventDate, in seconds.

#### Information Elements

Acted upon: 
dwc:eventDate

#### Examples

dwc:eventDate="1880-05-08/10": Response.status=RUN_HAS_RESULT, Response.result="259200", Response.comment="dwc:eventDate duration is 3 days = 259,200 seconds"

dwc:eventDate="95": Response.status=INTERNAL_PREREQUISITES_NOT_MET, Response.result=NOT_REPORTED, Response.comment="dwc:eventDate does not contain a valid ISO 8601-1:2019 date"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The duration of a day is 86400 seconds. Implementations should treat all days as 86400 seconds, but should include leap days (but not leap seconds) in durations that encompass them. Consumers should treat assertions about event date duration as approximations, see: https://xkcd.com/2867/

[🠱](#indexes-to-the-tests)
********************

###  ISSUE_DATAGENERALIZATIONS_NOTEMPTY

####  Issue dwc:dataGeneralizations Not Empty
https://rs.tdwg.org/bdqtest/terms/13d5a10e-188e-40fd-a22c-dbaa87b91df2/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:dataGeneralizations?

#### Specification

POTENTIAL_ISSUE if dwc:dataGeneralizations is bdq:NotEmpty; otherwise NOT_ISSUE

#### Information Elements

Acted upon: 
dwc:dataGeneralizations

#### Examples

dwc:dataGeneralizations="placed on quarter degree grid": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="dwc:dataGeneralizations is bdq:NotEmpty"

dwc:dataGeneralizations="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="dwc:dataGeneralizations is bdq:Empty"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

This is not specific to spatial data, any value in the dwc:dataGeneralizations field will cause this flag to be raised, but the primary use case is expected to be that dwc:dataGeneralizations demonstrates obfuscated locations.

[🠱](#indexes-to-the-tests)
********************

###  ISSUE_COORDINATES_CENTEROFCOUNTRY

####  Issue Coordinates Center Of Country
https://rs.tdwg.org/bdqtest/terms/256e51b3-1e08-4349-bb7e-5186631c3f8e/2024-08-28
Acts upon  SingleRecord

#### Description

Are the supplied geographic coordinates within a defined buffer of the center of the country?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if any of dwc:countryCode, dwc:decimalLatitude, dwc:decimalLongitude are bdq:Empty; POTENTIAL_ISSUE if (1) the geographic coordinates are within the distance given by bdq:spatialBufferInMeters from the center of the supplied dwc:countryCode as represented in the bdq:sourceAuthority (or one of the centers, if the bdq:sourceAuthority provides more than one per country code) and (2) the dwc:coordinateUncertaintyInMeters is bdq:Empty or less than half the square root of the area of the country; otherwise NOT_ISSUE.

#### Information Elements

Acted upon: 
dwc:countryCode,dwc:decimalLatitude,dwc:decimalLongitude

Consulted: 
dwc:coordinateUncertaintyInMeters

#### Parameters

bdq:spatialBufferInMeters,bdq:sourceAuthority

#### Default Parameter Values

bdq:spatialBufferInMeters default = "5000",bdq:sourceAuthority default = "GBIF Catalogue of Country Centroides" {[https://raw.githubusercontent.com/jhnwllr/catalogue-of-centroids/master/PCLI.tsv]}

#### Examples

dwc:decimalLatitude="-35.38804", dwc:decimalLongitude="-65.154964", dwc:countryCode="AR": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="coordinates fall within buffered distance in the bdq:sourceAuthority for dwc:countryCode"

dwc:decimalLatitude="-34.184199", dwc:decimalLongitude="-65.509403", dwc:countryCode="AR": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="coordinates fall outside buffered distance in the bdq:sourceAuthority for dwc:countryCode"


#### Use Cases

bdq:Spatial-Temporal_Patterns

#### Notes

We have increased the buffer to 5000 meters to cater for differences that may have arisen due to the difference in geodetic datums.

[🠱](#indexes-to-the-tests)
********************

###  ISSUE_ESTABLISHMENTMEANS_NOTEMPTY

####  Issue dwc:establishmentMeans Not Empty
https://rs.tdwg.org/bdqtest/terms/acc8dff2-d8d1-483a-946d-65a02a452700/2023-09-18
Acts upon  SingleRecord

#### Description

Is there a value in dwc:establishmentMeans?

#### Specification

POTENTIAL_ISSUE if dwc:establishmentMeans is bdq:NotEmpty; otherwise NOT_ISSUE

#### Information Elements

Acted upon: 
dwc:establishmentMeans

#### Examples

dwc:establishmentMeans="?": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="dwc:establishmentMeans is bdq:NotEmpty"

dwc:establishmentMeans="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="dwc:establishmentMeans is bdq:Empty"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  ISSUE_ANNOTATION_NOTEMPTY

####  Issue Annotation Not Empty
https://rs.tdwg.org/bdqtest/terms/fecaa8a3-bbd8-4c5a-a424-13c37c4bb7b1/2023-09-18
Acts upon  SingleRecord

#### Description

Are there any annotations associated with the record?

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:annotationSystem is not available; POTENTIAL_ISSUE if an annotation in the bdq:annotationSystem exists with a matching bdq:annotationAlertIf; otherwise NOT_ISSUE.

#### Information Elements
Consulted: 
AllDarwinCoreTerms

#### Parameters

bdq:annotationSystem,bdq:annotationAlertIf

#### Default Parameter Values

bdq:annotationSystem default = "W3C Web Annotation" {[https://www.w3.org/annotation/]} {"oa:Annotation vocabulary" {[https://www.w3.org/TR/annotation-vocab/]},bdq:annotationAlertIf default = "oa:Annotation with oa:hasTarget having as object any dwciri:term instance that is part of the SingleRecord under Test." {[https://www.w3.org/TR/annotation-vocab/]}

#### Examples

bdq:annotationAlertIf="": Response.status=RUN_HAS_RESULT, Response.result=NOT_ISSUE, Response.comment="bdq:annotationAlertIf is bdq:Empty"

bdq:annotationAlertIf="?": Response.status=RUN_HAS_RESULT, Response.result=POTENTIAL_ISSUE, Response.comment="bdq:annotationAlertIf is bdq:NotEmpty"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

While there is a W3C standard on 'web annotation', there is no TDWG recommendation on how this standard could be applied to annotating Darwin Core records. While implementation of this Test is currently problematic, TG2 considers annotations attached to any aspect of a Darwin Core record justifies this Test as a placeholder in the hope of future developments.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_BASISOFRECORD_STANDARDIZED

####  Amendment dwc:basisOfRecord Standardized
https://rs.tdwg.org/bdqtest/terms/07c28ace-561a-476e-a9b9-3d5ad6e35933/2024-07-24
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:basisOfRecord using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; AMENDED the value of dwc:basisOfRecord if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:basisOfRecord

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Darwin Core basisOfRecord" {[https://dwc.tdwg.org/terms/#dwc:basisOfRecord]} {dwc:basisOfRecord vocabulary [https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml]}

#### Examples

dwc:basisOfRecord="Human obs": Response.status=AMENDED, Response.result=dwc:basisOfRecord="HumanObservation", Response.comment="dwc:basisOfRecord contains interpretable value"

dwc:basisOfRecord="FossilSpecimen": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:basisOfRecord contains match in the bdq:sourceAuthority so NOT_AMENDED"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The term dwc:basisOfRecord has the comment "Recommended best practice is to use a controlled vocabulary such as the set of local names of the identifiers for classes in Darwin Core." The list of these values can be determined by searching https://github.com/tdwg/dwc/blob/master/vocabulary/term_versions.csv for rows with status="recommended" and rdf_type="http://www.w3.org/2000/01/rdf-schema#Class". For example, the term http://rs.tdwg.org/dwc/terms/PreservedSpecimen has a local name PreservedSpecimen. For Tests against a dwc:Occurrence record, the set of valid terms is more limited and embodied in the resource found at https://rs.gbif.org/vocabulary/dwc/basis_of_record.xml, which contains the local name for the identifier, as well as preferred and alternate labels from which to standardize values.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_DCTYPE_STANDARDIZED

####  Amendment dc:type Standard
https://rs.tdwg.org/bdqtest/terms/bd385eeb-44a2-464b-a503-7abe407ef904/2024-08-16
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dc:type using the DCMI type vocabulary.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; AMENDED the value of dc:type if it can be unambiguously interpreted as a term name in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dc:type

#### Default Parameter Values

bdq:sourceAuthority is "DCMI Type Vocabulary" {[http://purl.org/dc/terms/DCMIType]} {"DCMI Type Vocabulary List Of Terms" [https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2010-10-11/]}

#### Examples

dc:type="evnt": Response.status=AMENDED, Response.result=dc:type="Event", Response.comment="dc:type contains an interpretable value"

dc:type="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dc:type contains an uninterpretable value"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

dc:type holds literals (e.g. PhysicalObject), while dcterms:type holds an IRI for the resource (e.g. http://purl.org/dc/dcmitype/PhysicalObject), see the Darwin Core RDF guide https://dwc.tdwg.org/rdf/#32-imported-dublin-core-terms-for-which-only-literal-objects-are-appropriate-normative. Implementations of this Amendment are expected be able to amend IRI values to the literals, as well as removing leading/trailing whitespace and correcting case errors in the literal.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_LICENSE_STANDARDIZED

####  Amendment dcterms:license Standardized
https://rs.tdwg.org/bdqtest/terms/dcbe5bd2-42a0-4aab-bb4d-8f148c6490f8/2023-09-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dcterms:license using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; AMENDED value of dcterms:license if it could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dcterms:license

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Creative Commons" {[https://creativecommons.org/]} {Creative Commons licenses [https://creativecommons.org/about/cclicenses/]}

#### Examples

dcterms:license="CC0": Response.status=AMENDED, Response.result=dcterms:license="https://creativecommons.org/publicdomain/zero/1.0/legalcode", Response.comment="Input field contains interpretable value"

dcterms:license="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dcterms:license contains uninterpretable value "X""


#### Use Cases

bdq:Record-Management

#### Notes

The license at the record level might be derived from the license of the dataset from which the record is retrieved.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_COORDINATES_FROM_VERBATIM

####  Amendment Coordinates From Verbatim
https://rs.tdwg.org/bdqtest/terms/3c2590c7-af8a-4eb4-af57-5f73ba9d1f8e/2024-08-20
Acts upon  SingleRecord

#### Description

Proposes an amendment to the values of dwc:decimalLatitude, dwc:decimalLongitude, and dwc:geodeticDatum from geographic coordinate information in the verbatim coordinates terms.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if 1) either dwc:decimalLatitude or dwc:decimalLongitude are bdq:NotEmpty, or 2) dwc:verbatimCoordinates and one of dwc:verbatimLatitude and dwc:verbatimLongitude are bdq:Empty; FILLED_IN the values of dwc:decimalLatitude, dwc:decimalLongitude and dwc:geodeticDatum (provided that the dwc:verbatimCoordinates can be unambiguously interpreted as geographic coordinates) from 1) dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimSRS or 2) dwc:verbatimCoordinates and dwc:verbatimSRS; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dwc:decimalLatitude,dwc:decimalLongitude,dwc:geodeticDatum

Consulted: 
dwc:verbatimCoordinates,dwc:verbatimLatitude,dwc:verbatimLongitude,dwc:verbatimCoordinateSystem,dwc:verbatimSRS

#### Examples

dwc:verbatimLatitude="-23.712", dwc:verbatimLongitude="139.92", dwc:verbatimCoordinates="", dwc:verbatimSRS="EPSG:4326", dwc:verbatimCoordinateSystem="decimal degrees",dwc:decimalLatitude="", dwc:decimalLongitude="": Response.status=FILLED_IN, Response.result=dwc:decimalLatitude="-23.712", dwc:decimalLongitude="139.92", dwc:geodeticDatum="EPSG:4326", Response.comment="Input fields contain interpretable values"

dwc:verbatimLatitude="", dwc:verbatimLongitude="", dwc:verbatimCoordinates="54K 0390210 7377243", dwc:verbatimSRS="EPSG:32754", dwc:verbatimCoordinateSystem="decimal degrees", dwc:decimalLatitude="", dwc:decimalLongitude="":: Response.status=NOT_AMENDED, Response.result="", Response.comment="In the wrong coordinate system"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Transformations between coordinate reference systems should not be made as a part of this Test. Though coordinate precision of the verbatim coordinates could also be interpreted during the process of amending decimal coordinates from verbatim coordinates, that amendment is recommended to be an independent Test. Note that dwc:verbatimLatitude, dwc:verbatimLongitude and dwc:verbatimCoordinates might all be populated, and they may or not be perfectly consistent with each other. An ideal implementation should check for the consistency of these three fields and not amend them if they are inconsistent.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_COORDINATES_TRANSPOSED

####  Amendment Coordinates Transposed
https://rs.tdwg.org/bdqtest/terms/f2b4a50a-6b2f-4930-b9df-da87b6a21082/2024-11-11
Acts upon  SingleRecord

#### Description

Proposes an amendment of the signs of dwc:decimalLatitude and/or dwc:decimalLongitude to align the location with the dwc:countryCode.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if any of dwc:decimalLatitude or dwc:decimalLongitude or dwc:countryCode are bdq:Empty; AMENDED dwc:decimalLatitude and dwc:decimalLongitude if the coordinates were transposed or one or more of the signs of the coordinates were reversed to align the location with dwc:countryCode according to the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:decimalLatitude,dwc:decimalLongitude

Consulted: 
dwc:countryCode

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]}

#### Examples

dwc:decimalLatitude="25.46", dwc:decimalLongitude="135.87", dwc:countryCode="AU": Response.status=AMENDED, Response.result=dwc:decimalLatitude="-25.46", dwc:decimalLongitude="135.87", Response.comment="dwc:decimalLatitude sign reversed to fit dwc:countryCode=AU"

dwc:decimalLatitude="25.46", dwc:decimalLongitude="135.87", dwc:countryCode="AX": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:countryCode is uninterpretable"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The dwc:geodeticDatum is not necessary for this Test. The maximum positional shift between any geographic coordinate reference system and WGS84 is less than 6 km, so any hemisphere Test that relies on a country code for consistency would not be affected by the potential shift. The prior VALIDATION for this Test is VALIDATION_COORDINATE_COUNTRYCODE_CONSISTENT (adb27d29-9f0d-4d52-b760-a77ba57a69c9).

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_COUNTRYCODE_FROM_COORDINATES

####  Amendment dwc:countryCode from Coordinates
https://rs.tdwg.org/bdqtest/terms/8c5fe9c9-4ba9-49ef-b15a-9ccd0424e6ae/2024-08-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary from the bdq:countryShapes that is attributable to a single valid ISO 3166-1-alpha-2 country code.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either dwc:decimalLatitude or dwc:decimalLongitude is bdq:Empty, or if dwc:countryCode is bdq:NotEmpty; FILLED_IN dwc:countryCode if dwc:decimalLatitude and dwc:decimalLongitude fall within a boundary in the bdq:sourceAuthority that is attributable to a single valid country code; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dwc:countryCode

Consulted: 
dwc:decimalLatitude,dwc:decimalLongitude

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "10m-admin-1 boundaries UNION with Exclusive Economic Zones" {[https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/] spatial UNION [https://www.marineregions.org/downloads.php#marbound]}

#### Examples

dwc:decimalLatitude="-25.23", dwc:decimalLongitude="135.43", dwc:countryCode="": Response.status=FILLED_IN, Response.result=dwc:countryCode="AU", Response.comment="dwc:decimalLatitude and dwc:decimalLongitude contain interpretable values"

dwc:decimalLatitude="-38.280937", dwc:decimalLongitude="72.047790", dwc:countryCode="": Response.status=NOT_AMENDED, Response.result="", Response.comment="Coordinates do not fall in the boundary of any country"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

This amendment simply fills dwc:countryCode from a lookup of dwc:decimalLatitude and dwc:decimalLongitude. dwc:coordinateUncertaintyInMeters and dwc:coordinatePrecision (if present) imply a buffer around the provided coordinates. Likewise, country polygons cannot be 100% accurate at all scales (Dooley 2005), so a spatial buffer of the country boundaries is also justified. Taking spatial buffers into account does, however, greatly complicate the logic and the implementation of this and related Tests. In this Test, a detection of multiple country codes by sampling within the buffer, while possible, is not considered.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_COUNTRYCODE_STANDARDIZED

####  Amendment dwc:countryCode Standard
https://rs.tdwg.org/bdqtest/terms/fec5ffe6-3958-4312-82d9-ebcca0efb350/2024-11-09
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:countryCode if it can be interpreted as an ISO 3166-1-alpha-2 country code.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISTITES_NOT_MET if the value of dwc:countryCode is bdq:Empty; AMENDED the value of dwc:countryCode if it can be unambiguously interpreted to a value in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:countryCode

#### Default Parameter Values

bdq:sourceAuthority default = "ISO 3166-1-alpha-2" {[https://www.iso.org/iso-3166-country-codes.html]} {ISO 3166-1-alpha-2 Country Code search [https://www.iso.org/obp/ui/#search]}

#### Examples

dwc:countryCode="Australia": Response.status=AMENDED, Response.result=dwc:countryCode="AU", Response.comment="dwc:countryCode contains an interpretable value"

dwc:countryCode="Aust.": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:countryCode contains an ambiguous value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

This Test supports conformance with the recommendation in the comment on dwc:countryCode: "Recommended best practice is to use an ISO 3166-1-alpha-2 country code." Three letter codes should be amended to the matching two-letter code.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT

####  Amendment dwc:geodeticDatum Assumed Default
https://rs.tdwg.org/bdqtest/terms/7498ca76-c4d4-42e2-8103-acacccbdffa7/2024-11-12
Acts upon  SingleRecord

#### Description

Proposes an amendment to fill in dwc:geodeticDatum using a parameterized value if the dwc:geodeticDatum is empty.

#### Specification

If dwc:geodeticDatum is bdq:Empty, fill in dwc:geodeticDatum using the value of bdq:defaultGeodeticDatum, report FILLED_IN and, if dwc:coordinateUncertaintyInMeters, dwc:decimalLatitude and dwc:decimalLongitude are bdq:NotEmpty, amend the value of dwc:coordinateUncertaintyInMeters by adding the maximum datum shift between the specified bdq:defaultGeodeticDatum and any other datum at the provided dwc:decimalLatitude and dwc:decimalLongitude and instead report AMENDED; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dwc:geodeticDatum,dwc:coordinateUncertaintyInMeters

Consulted: 
dwc:decimalLatitude,dwc:decimalLongitude

#### Parameters

bdq:defaultGeodeticDatum

#### Default Parameter Values

bdq:defaultGeodeticDatum default = "EPSG:4326"

#### Examples

dwc:geodeticDatum="[null]", dwc:decimalLatitude="-30.00", dwc:decimalLongitude="130.00", dwc:coordinateUncertaintyInMeters="50": Response.status=AMENDED, Response.result=dwc:geodeticDatum="EPSG:4326", dwc:coordinateUncertaintyInMeters="2836", Response.comment="dwc:godeticDatum is bdq:Empty so filled in with default and dwc:coordinateUncertaintyInMeters amended to maximum possible value"

dwc:geodeticDatum="WGS84", dwc:decimalLatitude="", dwc:decimalLongitude="", dwc:coordinateUncertaintyInMeters="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:geodeticDatum contains a value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The value of dwc:geodeticDatum applies to dwc:decimalLatitude and dwc:decimalLongitude, thus EPSG:4326 (https://epsg.org/crs_4326/WGS-84.html) is the appropriate EPSG code as it applies to the WGS84 datum used with a geographic coordinate system. If the dwc:coordinateUncertaintyInMeters is bdq:Empty, not interpretable, or not valid, this amendment should not provide a dwc:coordinateUncertaintyInMeters. If the dwc:coordinateUncertaintyInMeters is bdq:NotEmpty and is valid, this amendment should add to the dwc:coordinateUncertaintyInMeters the uncertainty contributed by the maximum datum shift at the given coordinates. Since different systems have differing requirements for what the default datum should be, it is left unspecified, but should match whatever the target datum is in AMENDMENT_COORDINATES_CONVERTED (620749b9-7d9c-4890-97d2-be3d1cde6da8). After the amendment is performed, the dwc:geodeticDatum field should be the assumed default datum as parameterized. An example implementation to determine the uncertainty added by asserting a default datum (datum shift) where a known datum is not declared can be found in [datumshiftproj.py](https://github.com/VertNet/georefcalculator/blob/master/source/python/datumshiftproj.py) in the source code for the [Georeferencing Calculator](http://georeferencing.org/georefcalculator/gc.html) (Wieczorek & Wieczorek 2021). Included in the source code is a [5-degree grid](https://github.com/VertNet/georefcalculator/blob/master/datumerrordata.js) of datum shifts from an unknown datum to WGS84.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_GEODETICDATUM_STANDARDIZED

####  Amendment dwc:geodeticDatum Standardized
https://rs.tdwg.org/bdqtest/terms/0345b325-836d-4235-96d0-3b5caf150fc0/2025-03-03
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:geodeticDatum using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; AMENDED the value of dwc:geodeticDatum if it could be unambiguously interpreted as a valid code from the bdq:sourceAuthority (in the form Authority:Number) for a Datum, Ellipsoid or a CRS appropriate for a 2D geographic coordinate in degrees, or as the value "not recorded"; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:geodeticDatum

#### Default Parameter Values

bdq:sourceAuthority = "EPSG" {[https://epsg.org]} {API for EPSG codes [https://apps.epsg.org/api/swagger/ui/index#/Datum]}

#### Examples

dwc:geodeticDatum="WGS84": Response.status=AMENDED, Response.result=dwc:geodeticDatum="EPSG:4326", Response.comment="dwc:geodeticDatum contains a valid code in the bdq:sourceAuthority"

dwc:geodeticDatum="WGS8": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:geodeticDatum contains an ambiguous value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Chapman and Wieczorek (2020) recommend best practice is to use EPSG codes (https://epsg.io/) as a controlled vocabulary. Ideally, amend to the EPSG code for the geographic coordinate reference system (CRS), if known. Otherwise use the EPSG code for the geodetic datum, if known. Otherwise use the EPSG code of the ellipsoid, if known. If none of these is known, use the explicit value "not recorded". The reference vocabularies of values for geodetic datums and ellipsoids needs to be made available and should map alternative representations of dwc:geodeticDatum strings to EPSG codes, such as "WGS84", "WGS_84", "WGS:84", "WGS 84", all with standard value "epsg:4326". NB. Do NOT change one datum to any other datum no matter how close they are or may appear to be. The same treatment should be given to all datums, which is to use their transformation algorithms to get the equivalent in epsg:4326. For reference, a vocabulary of synonyms for EPSG codes for values of dwc:geodeticDatum can be found at https://registry.gbif.org/vocabulary/GeodeticDatum/concepts and and for more information on obtaining the EPSG dataset, see https://docs.geotools.org/latest/userguide/library/referencing/epsg.html. For the purposes of this Test "not recorded" is not a value in the bdq:sourceAuthority and should result in NOT_AMENDED.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM

####  Amendment dwc:minimumDepthInMeters dwc:maximumDepthInMeters From dwc:verbatimDepth
https://rs.tdwg.org/bdqtest/terms/c5658b83-4471-4f57-9d94-bf7d0a96900c/2024-08-30
Acts upon  SingleRecord

#### Description

Proposes amendments of the values of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be interpreted from dwc:verbatimDepth.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters are bdq:NotEmpty or dwc:verbatimDepth is bdq:Empty; FILLED_IN the value of dwc:minimumDepthInMeters and dwc:maximumDepthInMeters if they can be unambiguously interpreted from dwc:verbatimDepth; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dwc:minimumDepthInMeters,dwc:maximumDepthInMeters

Consulted: 
dwc:verbatimDepth

#### Examples

dwc:minimumDepthInMeters="", dwc:maximumDepthInMeters="", dwc:verbatimDepth="10 feet": Response.status=FILLED_IN, Response.result=dwc:minimumDepthInMeters="3.048", dwc:maximumDepthInMeters="3.048", Response.comment="dwc:verbatimDepth contains interpretable values"

dwc:minimumDepthInMeters="", dwc:maximumDepthInMeters="", dwc:verbatimDepth="x": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:verbatimDepth does not contain an interpretable value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

If dwc:verbatimDepth has a single value rather than a range, the minimum and maximum values should be amended with the same value. When transforming units, the transformation should be reversible, not adjusting the number of significant digits or adjusting the rounding. For example, transform fathoms to meters by multiplying by 1.8288 and retaining added significant digits (verbatim depth of 10 fathoms to minimum and maximum depths in meters of 18.288). Implementations should be capable of interpreting verbatim data in at least meters, fathoms, and feet, in the form of either a single value or a range. The units must be specified in the verbatim data to be interpretable.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM

####  Amendment dwc:minimumElevationInMeters dwc:maximumElevationInMeters From dwc:verbatimElevation
https://rs.tdwg.org/bdqtest/terms/2d638c8b-4c62-44a0-a14d-fa147bf9823d/2024-08-30
Acts upon  SingleRecord

#### Description

Proposes an amendment or amendments to the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be interpreted from dwc:verbatimElevation.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters or dwc:maximumElevationInMeters are bdq:NotEmpty or dwc:verbatimElevation is bdq:Empty; FILLED_IN the values of dwc:minimumElevationInMeters and dwc:maximumElevationInMeters if they can be unambiguously interpreted from dwc:verbatimElevation; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:minimumElevationInMeters,dwc:maximumElevationInMeters

Consulted: 
dwc:verbatimElevation

#### Examples

dwc:verbatimElevation="100 feet", dwc:minimumElevationInMeters="", dwc:maximumElevationInMeters="": Response.status=FILLED_IN, Response.result=dwc:minimumElevationInMeters="30.48", dwc:maximumElevationInMeters="30.48", Response.comment="dwc:verbatimElevation contains an interpretable value"

dwc:verbatimElevation="x", dwc:minimumElevationInMeters="", dwc:maximumElevationInMeters="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:verbatimElevation contains an uninterpretable value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

If the dwc:verbatimElevation as a single value rather than a range, the minimum and maximum values should be amended with the same value. When transforming units, the transformation should be reversible, not adjusting the number of significant digits or adjusting the rounding. For example, transform yards to meters by multiplying by 0.9144 and retaining added significant digits (verbatim elevation of 10 yards to minimum and maximum depths in meters of 9.144). Implementations should be capable of interpreting verbatim data in at least meters,yards, feet, and kilometers in the form of either a single value or a range. The units must be specified in the verbatim data to be interpretable.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_DAY_STANDARDIZED

####  Amendment dwc:day Standardized
https://rs.tdwg.org/bdqtest/terms/b129fa4d-b25b-43f7-9645-5ed4d44b357b/2023-09-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:day as an integer between 1 and 31 inclusive.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; AMENDED the value of dwc:day if the value is unambiguously interpreted as an integer between 1 and 31 inclusive; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:day

#### Examples

dwc:day="23rd": Response.status=AMENDED, Response.result=dwc:day="23", Response.comment="dwc:day is interpretable as "23""

dwc:day="X": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:day is ambiguous, either a "X", "No data" or "10""


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

If dwc:day contains text that may be interpreted as Roman numerals, the result will be NOT_AMENDED as this is not standard. Values such as "3rd" or "12th" can be interpreted as the integers "3" and "12". Text such as "5th Friday" is ambiguous.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_EVENTDATE_FROM_VERBATIM

####  Amendment dwc:eventDate From dwc:verbatimEventDate
https://rs.tdwg.org/bdqtest/terms/6d0a0c10-5e4a-4759-b448-88932f399812/2024-09-16
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:eventDate from the content of dwc:verbatimEventDate.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:NotEmpty or the value of dwc:verbatimEventDate is bdq:Empty; FILLED_IN the value of dwc:eventDate if an unambiguous ISO 8601 date is interpreted from dwc:verbatimEventDate; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:eventDate

Consulted: 
dwc:verbatimEventDate

#### Examples

dwc:eventDate="", dwc:verbatimEventDate="Friday 29th Oct. 2021": Response.status=FILLED_IN, Response.result=dwc:eventDate="2021-10-29", Response.comment="dwc:verbatimEventDate contains an interpretable value (assuming some external lookup thesauri)"

dwc:eventDate="", dwc:verbatimEventDate="03/04/2020": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:verbatimEventDate is ambiguous - could be either 3rd April or 4th March"


#### Use Cases

bdq:Record-Management

#### Notes

If the proposed eventDate is prior to 1918-02-14, the Response.comment will include a note that the "verbatimDate was assumed to be in the Gregorian calendar". When running the Test, the original precision, e.g. year=1980, month=1 should be retained, e.g. dwc:eventDate should become 1980-01, not 1980-01-01/1980-01-31.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY

####  Amendment dwc:eventDate from dwc:year dwc:month dwc:day
https://rs.tdwg.org/bdqtest/terms/3892f432-ddd0-4a0a-b713-f2e2ecbd879d/2024-09-15
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:month and dwc:day.

#### Specification

INTERNAL _PREREQUISITES_NOT_MET if dwc:eventDate is not EMPTY or dwc:year is EMPTY or is not interpretable as an integer; FILLED_IN the value of dwc:eventDate if an ISO 8601 date was interpreted from the values in dwc:year, dwc:month and dwc:day; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:eventDate

Consulted: 
dwc:year,dwc:month,dwc:day

#### Examples

dwc:eventDate="", dwc:year="1420", dwc:month="10", dwc:day="29": Response.status=FILLED_IN, Response.result=dwc:eventDate="1420-10-29", Response.comment="dwc:year, dwc:month and dwc:day are interpretable, even if pre-Linnaeus"

dwc:eventDate="", dwc:year="2024", dwc:month="2", dwc:day="30": Response.status=NOT_AMENDED, Response.result=, Response.comment="Not a valid date"


#### Use Cases

bdq:Record-Management

#### Notes

An attempt to populate dwc:eventDate from dwc:verbatimEventDate and from dwc:startDayOfYear and dwc:endDayOfYear should be made before this Test is run. If dwc:year and dwc:day are present and interpretable, but dwc:month is not supplied or is not interpretable, then just the year should be given as the proposed amendment. This Test assumes that that dwc:year, dwc:month, dwc:day are in a Gregorian calendar, and that only those three pieces of information are needed to produce a dwc:eventDate (explicitly in ISO 8601-1 format, and thus using the Gregorian calendar). When running the Test, the original precision, e.g. dwc:year=1980, dwc:month=1 should be retained, e.g. dwc:eventDate should become 1980-01, not 1980-01-01/1980-01-31.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR

####  Amendment dwc:eventDate from dwc:year dwc:startDayOfYear dwc:endDayOfYear
https://rs.tdwg.org/bdqtest/terms/eb0a44fa-241c-4d64-98df-ad4aa837307b/2024-08-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:NotEmpty or any of dwc:year, dwc:startDayOfYear, or dwc:endDayOfYear are bdq:Empty; FILLED_IN the value of dwc:eventDate from values in dwc:year, dwc:startDayOfYear and dwc:endDayOfYear if the values in each are independently interpretable and if the value of dwc:startDayOfYear is less than the value of dwc:endDayOfYear; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:eventDate

Consulted: 
dwc:year,dwc:startDayOfYear,dwc:endDayOfYear

#### Examples

dwc:year="1901", dwc:startDayOfYear="15", dwc:endDayOfYear="25", dwc:eventDate="": Response.status=FILLED_IN, Response.result=dwc:eventDate="1901-01-15/1901-01-25", Response.comment="dwc:eventDate was interpreted from dwc:year, dwc:startDayOfYear and dwc:endDayOfYear"

dwc:year="1901", dwc:startDayOfYear="25", dwc:endDayOfYear="15", dwc:eventDate="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:startDayOfYear > dwc:endDayOfyear"


#### Use Cases

bdq:Record-Management

#### Notes

An attempt to populate dwc:eventDate from dwc:verbatimEventDate should be made before this Test is run. While year=1999, startDayOfYear=123 could be validly represented as an ISO date as either 1999-123 or 1999-05-03, the latter of these two forms SHOULD be used, thus, do not simply concatenate dwc:year and dwc:startDayOfYear. This Test is only for cases that fall within the one year (as given in dwc:year) and hence dwc:startDayOfYear will always be less than dwc:endDayOfYear.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_EVENTDATE_STANDARDIZED

####  Amendment dwc:eventDate Standardized
https://rs.tdwg.org/bdqtest/terms/718dfc3c-cb52-4fca-b8e2-0e722f375da7/2024-09-16
Acts upon  SingleRecord

#### Description

Proposes an amendment of the value of dwc:eventDate to a valid ISO date.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; AMENDED if the value of dwc:eventDate is not a properly formatted ISO 8601 date but is unambiguous, and altered to be a valid ISO 8601 date; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:eventDate

#### Examples

dwc:eventDate="2021-28-10": Response.status=AMENDED, Response.result=dwc:eventDate="2021-10-28", Response.comment="dwc:eventDate contains an interpretable value. Assuming year-day-month input format"

dwc:eventDate="10-28": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:eventDate contains an ambiguous value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

The intent of the amended range is to capture the original uncertainty where possible. As in the example, we amend "1999-11" instead of "1999-11-01/1999-11-31". An AMBIGUOUS response is possible.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_EVENT_FROM_EVENTDATE

####  Amendment dwc:Event from dwc:eventDate
https://rs.tdwg.org/bdqtest/terms/710fe118-17e1-440f-b428-88ba3f547d6d/2024-09-16
Acts upon  SingleRecord

#### Description

Proposes an amendment to values in any of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear or dwc:endDayOfYear from the content of dwc:eventDate.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or contains an invalid value according to ISO 8601; FILLED_IN if any of (1) dwc:day from dwc:eventDate if dwc:day is bdq:Empty and dwc:eventDate has a precision of a day or finer and is within a single day, (2) dwc:month from dwc:eventDate if dwc:month is bdq:Empty and dwc:eventDate has a precision of a single month or finer and is within a single month, (3) dwc:year from dwc:eventDate if dwc:year is bdq:Empty and dwc:eventDate has a precision of a single year or finer and is within a single year, (4) dwc:startDayOfYear and dwc:endDayOfYear if they are bdq:Empty and dwc:eventDate has a precision of a day or better; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dwc:year,dwc:month,dwc:day,dwc:startDayOfYear,dwc:endDayOfYear

Consulted: 
dwc:eventDate

#### Examples

dwc:eventDate="2023-01-26", dwc:year="2023", dwc:month="", dwc:day="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=FILLED_IN, Response.result=dwc:month="1", dwc:day="26", dwc:startDayOfYear="26", dwc:endDayOfYear="26", Response.comment="dwc:month, dwc:day, dwc:startDayOfyear and dwc:endDayOfYear filled in from dwc:eventDate"

dwc:eventDate="2023",dwc:year="2023", dwc:month="", dwc:day="", dwc:startDayOfYear="", dwc:endDayOfYear="": Response.status=NOT_AMENDED, Response.result=, Response.comment="No amendments possible"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Only fields that are empty will be have changes proposed, and only if dwc:eventDate has a valid ISO 8601-1 date. The dwc:eventDate is the canonical form of the event date (it is the first trusted form). If event date does not contain a range,dwc:startDayOfYear = dwc:endDayOfYear. Time (as compared to date) is not deemed a CORE component. Note, see sequencing Tests section of standards documents, run this amendment after any other amendment that may affect dwc:eventDate

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_MONTH_STANDARDIZED

####  Amendment dwc:month Standardized
https://rs.tdwg.org/bdqtest/terms/2e371d57-1eb3-4fe3-8a61-dff43ced50cf/2023-09-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:month as an integer between 1 and 12 inclusive.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; AMENDED the value of dwc:month if it can be unambiguously interpreted as an integer between 1 and 12 inclusive; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:month

#### Examples

dwc:month="IV": Response.status=AMENDED, Response.result=dwc:month="4", Response.comment="dwc:month interpreted as roman numerals "

dwc:month="October": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:month contains an uninterpretable value"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

Implementations should translate interpretable Roman numerals in the range I-XII in dwc:month as integer month values 1-12, as some natural science domains use roman numeral months to avoid language and day/month vs month/day order. In these cases, the result will be AMENDED numeric equivalents.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_DATEIDENTIFIED_STANDARDIZED

####  Amendment dwc:dateIdentified Standard
https://rs.tdwg.org/bdqtest/terms/39bb2280-1215-447b-9221-fd13bc990641/2024-09-16
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:dateIdentified to a valid ISO date.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; AMENDED if the value of dwc:dateIdentified is not a properly formatted ISO 8601 date but is unambiguous and altered to be a valid ISO 8601 date; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dwc:dateIdentified

#### Examples

dwc:dateIdentified="2021-28-10": Response.status=AMENDED, Response.result=dwc:dateIdentified="2021-10-28", Response.comment="dwc:dateIdentified assuming dwc:year, dwc:day and dwc:month"

dwc:dateIdentified="21-10-28": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:dateIdentified contains ambiguous values. It could be dd-mm-yy or yy-mm-dd"


#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

We reference Wikipedia for the ISO standard because the standard documents are not free.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_DEGREEOFESTABLISHMENT_STANDARDIZED

####  Amendment dwc:degreeOfEstablishment Standardized
https://rs.tdwg.org/bdqtest/terms/74ef1034-e289-4596-b5b0-cde73796697d/2024-04-16
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:degreeOfEstablishment using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; AMENDED the value of dwc:degreeOfEstablishment if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:degreeOfEstablishment

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Degree of Establishment Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/doe/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/DegreeOfEstablishment/concepts]}

#### Examples

dwc:degreeOfEstablishment="capt.": Response.status=AMENDED, Response.result=dwc:degreeOfEstablishment="captive", Response.comment="dwc:degreeOfEstablishment contains an interpretable value in the bdq:sourceAuthority"

dwc:degreeOfEstablishment="tree": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:degreeOfEstablishment does not contain an interpretable value in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species

#### Notes

For reference, synonyms for values of dwc:degreeOfEstablishment can be found at https://registry.gbif.org/vocabulary/DegreeOfEstablishment/concepts.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_ESTABLISHMENTMEANS_STANDARDIZED

####  Amendment dwc:establishmentMeans Standardized
https://rs.tdwg.org/bdqtest/terms/15d15927-7a22-43f8-88d6-298f5eb45c4c/2024-02-08
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:establishmentMeans using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; AMENDED the value of dwc:establishmentMeans if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:establishmentMeans

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Establishment Means Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/em/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/EstablishmentMeans/concepts]}

#### Examples

dwc:establishmentMeans="vag.": Response.status=AMENDED, Response.result=dwc:establishmentMeans="vagrant", Response.comment="dwc:establishmentMeans contains an interpretable value in the bdq:sourceAuthority"

dwc:establishmentMeans="cultivated": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:establishmentMeans is not an interpretable value in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT

####  Amendment dwc:occurrenceStatus Assumed Default
https://rs.tdwg.org/bdqtest/terms/96667a0a-ae59-446a-bbb0-b7f2b0ca6cf5/2024-11-13
Acts upon  SingleRecord

#### Description

Proposes an amendment of the value of dwc:occurrenceStatus to the default parameter value if dwc:occurrenceStatus, dwc:individualCount and dwc:organismQuantity are empty.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:NotEmpty; FILLED_IN the value of dwc:occurrenceStatus using the bdq:defaultOccurrenceStatus Parameter value if dwc:occurrenceStatus,dwc:individualCount and dwc:organismQuantity are bdq:Empty; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:occurrenceStatus

Consulted: 
dwc:individualCount,dwc:organismQuantity

#### Parameters

bdq:defaultOccurrenceStatus

#### Default Parameter Values

bdq:defaultOccurrenceStatus default = "present"

#### Examples

dwc:occurrenceStatus="", dwc:individualCount="", dwc:organismQuantity="": Response.status=FILLED_IN, Response.result=dwc:occurrenceStatus="present", Response.comment="dwc:occurrenceStatus is bdq:Empty; assumed "present""

dwc:occurrenceStatus="X", dwc:individualCount="10", dwc:organismQuantity="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:occurrenceStatus is bdq:NotEmpty"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

There is currently a capitalization mismatch between https://dwc.tdwg.org/terms/#dwc:occurrenceStatus recommended values and the GBIF vocabulary at (https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts).

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_OCCURRENCESTATUS_STANDARDIZED

####  Amendment dwc:occurrenceStatus Standardized
https://rs.tdwg.org/bdqtest/terms/f8f3a093-042c-47a3-971a-a482aaaf3b75/2025-03-03
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:occurrenceStatus using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:ocurrenceStatus is bdq:Empty; AMENDED the value of dwc:occurrenceStatus if it can be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:occurrenceStatus

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Regex present/absent" {["^(present\

#### Examples

dwc:occurrenceStatus="1": Response.status=AMENDED, Response.result=dwc:occurrenceStatus="present", Response.comment="Input field contains an interpretable value. "

dwc:occurrenceStatus="X": Response.status=NOT_AMENDED, Response.result=, Response.comment="Input field contains uninterpretable value "X"


#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

The recommended controlled vocabulary for this term consists of "present" and "absent", which are the only two appropriate terms for a Darwin Core Occurrence. This is reflected in the suggested dwc:occurrenceStatus vocabulary for this Test. Other values for dwc:occurrenceStatus should only arise under circumstances that do not refer to an Occurrence. The GBIF API is listed in the sourceAuthority. However, there is currently a mismatch between the lower case recommended values at https://dwc.tdwg.org/terms/#dwc:occurrenceStatus and the GBIF vocabulary at bdq:sourceAuthority that uses an upper case first letter (https://api.gbif.org/v1/vocabularies/OccurrenceStatus/concepts), thus implementations using the GBIF API should ensure that matches on alternate terms in that vocabulary are converted to the all lower case values in the present/absent vocabulary recommended in Darwin Core. Implementations should interpret the numeric value 1 as present, and the numeric value 0 as absent.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_PATHWAY_STANDARDIZED

####  Amendment dwc:pathway Standardized
https://rs.tdwg.org/bdqtest/terms/f9205977-f145-44f5-8cb9-e3e2e35ce908/2024-09-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:pathway using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; AMENDED the value of dwc:pathway if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:pathway

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "Pathway Controlled Vocabulary List of Terms" {[https://dwc.tdwg.org/pw/]} {GBIF vocabulary API [https://api.gbif.org/v1/vocabularies/Pathway/concepts]}

#### Examples

dwc:pathway="transportStowaway": Response.status=AMENDED, Response.result=dwc:pathway="transportStowaway", Response.comment="dwc:pathway found in the bdq:sourceAuthority"

dwc:pathway="escapeee": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:pathway not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For reference, synonyms for values of dwc:pathway can be found at https://registry.gbif.org/vocabulary/Pathway/concepts.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_SEX_STANDARDIZED

####  Amendment dwc:sex Standardized
https://rs.tdwg.org/bdqtest/terms/33c45ae1-e2db-462a-a59e-7169bb01c5d6/2024-03-25
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:sex using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; AMENDED the value of dwc:sex if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:sex

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Sex Vocabulary" [https://api.gbif.org/v1/vocabularies/Sex]} {"dwc:sex vocabulary API" [https://api.gbif.org/v1/vocabularies/Sex/concepts]}

#### Examples

dwc:sex="f": Response.status=AMENDED, Response.result=dwc:sex="Female", Response.comment="dwc:sex found in the bdq:sourceAuthority"

dwc:sex="x": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:sex not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For reference, a list of synonyms for dwc:sex values can be found at https://registry.gbif.org/vocabulary/Sex/concepts.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_TYPESTATUS_STANDARDIZED

####  Amendment dwc:typeStatus Standardized
https://rs.tdwg.org/bdqtest/terms/b3471c65-b53e-453b-8282-abfa27bf1805/2024-11-11
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:typeStatus using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; AMENDED the value of the first word in each &#124; delimited portion of dwc:typeStatus if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED.

#### Information Elements

Acted upon: 
dwc:typeStatus

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF TypeStatus Vocabulary" {[https://api.gbif.org/v1/vocabularies/TypeStatus]} {dwc:typeStatus vocabulary API [https://api.gbif.org/v1/vocabularies/TypeStatus/concepts]}

#### Examples

dwc:typeStatus="Holo.": Response.status=AMENDED, Response.result=dwc:typeStatus="Holotype", Response.comment="dwc:typeStatus found in the bdq:sourceAuthority"

dwc:typeStatus="x": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:typeStatus not found in the bdq:sourceAuthority"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

Valuable for data quality needs related to voucher specimens in natural science collections. Almost all occurrence data will have no value in dwc:typeStatus. For reference, a vocabulary of synonyms can be found for dwc:typeStatus at [https://registry.gbif.org/vocabulary/TypeStatus/concepts].

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_SCIENTIFICNAMEID_FROM_TAXON

####  Amendment dwc:scientificNameID from dwc:Taxon
https://rs.tdwg.org/bdqtest/terms/431467d6-9b4b-48fa-a197-cd5379f5e889/2023-09-17
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:scientificNameID if it can be unambiguously resolved from bdq:sourceAuthority using the available taxon terms.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:NotEmpty, or if all of dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, and dwc:cultivarEpithet are bdq:Empty, FILLED_IN the value of dwc:scientificNameID for an unambiguously resolved single taxon record in the bdq:sourceAuthority through (1) the value of dwc:scientificName or (2) if dwc:scientificName is bdq:Empty through values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship and dwc:cultivarEpithet, or (3) if ambiguity produced by multiple matches in (1) or (2) can be disambiguated to a single Taxon using the values of dwc:subtribe, dwc:tribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID, dwc:taxonomicRank, and dwc:vernacularName; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:scientificNameID

Consulted: 
dwc:taxonID,dwc:acceptedNameUsageID,dwc:originalNameUsageID,dwc:taxonConceptID,dwc:scientificName,dwc:higherClassification,dwc:kingdom,dwc:phylum,dwc:class,dwc:order,dwc:superfamily,dwc:family,dwc:subfamily,dwc:tribe,dwc:subtribe,dwc:genus,dwc:genericName,dwc:subgenus,dwc:specificEpithet,dwc:infraspecificEpithet,dwc:cultivarEpithet,dwc:vernacularName,dwc:scientificNameAuthorship,dwc:taxonRank

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:taxonID="", dwc:scientificNameID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Chicoreus palmarosae (Lamarck, 1822)", dwc:higherClassification="", dwc:kingdom="Animalia", dwc:phylum="Mollusca", dwc:class="Gastropoda", dwc:order="", dwc:family="Muricidae", dwc:subfamily="", dwc:genus="Chicoreus", dwc:genericName="Chicoreus", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="palmarosae", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="(Lamarck, 1822)", dwc:taxonRank="", bdq:sourceAuthority=”marinespecies.org”: Response.status=FILLED_IN, Response.result=dwc:scientificNameID="urn:lsid:marinespecies.org:taxname:208134", Response.comment="dwc:scientificName matched to unique taxon record in WoRMS, exact match on name and authorship. Resolvable at https://marinespecies.org/aphia.php?p=taxdetails&id=208134"

dwc:scientificNameID="", dwc:taxonID="", dwc:acceptedNameUsageID="", dwc:originalNameUsageID="", dwc:taxonConceptID="", dwc:scientificName="Graphis", dwc:higherClassification="", dwc:kingdom="", dwc:phylum="", dwc:class="", dwc:order="", dwc:family="", dwc:subfamily="", dwc:genus="", dwc:genericName="", dwc:subgenus="", dwc:infragenericEpithet="", dwc:specificEpithet="", dwc:infraspecificEpithet="", dwc:cultivarEpithet="", dwc:vernacularName="", dwc:scientificNameAuthorship="", dwc:taxonRank="": Response.status=NOT_AMENDED, Response.result=, Response.comment="dwc:scientificName="Graphis" is ambiguous as could be either a lichen or a gastropod."


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

Return a result with no value and a Result.status of NOT_AMENDED with a Response.comment of ambiguous if the information provided does not resolve to a unique result (e.g. if homonyms exist and there is insufficient information in the provided data, for example using the lowest ranking taxa in conjunction with dwc:dwc:scientificNameAuthorship, to resolve them). When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID

####  Amendment dwc:scientificName from dwc:scientificNameID
https://rs.tdwg.org/bdqtest/terms/f01fb3f9-2f7e-418b-9f51-adf50f202aea/2024-08-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:scientificName using the dwc:scientificNameID value from the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty, or dwc:scientificName is bdq:NotEmpty; FILLED_IN the value of dwc:scientificName if the value of dwc: scientificNameID could be unambiguously interpreted as a value in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:scientificName

Consulted: 
dwc:scientificNameID

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF Backbone Taxonomy" {[https://doi.org/10.15468/39omei]} {API endpoint [https://api.gbif.org/v1/species?datasetKey=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&name=]}

#### Examples

dwc:scientificNameID="gbif:8102122", dwc:scientificName="": Response.status=FILLED_IN, Response.result=dwc:scientificName="Harpullia pendula F.Muell.", Response.comment="dwc:scientificNameID contains an interpretable value"

dwc:scientificNameID="gbif:8a", dwc:scientificName="": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:scientificNameID does not contain an interpretable value"


#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

The value of dwc:scientificNameID is unambiguous if dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority. When referencing a GBIF taxon by GBIF's identifier for that taxon, use the the pseudo-namespace "gbif:" and the form "gbif:{integer}" as the value for dwc:scientificNameID. Implementers can be aware of the current GBIF api endpoint that can replace the pseduo-namespace gbif: when looking up the dwc:scientificNameID (taxonID in the gbif document), e.g. `s/gbif:/https:\/\/api.gbif.org\/v1\/species\// ` will transform the value taxonID=gbif:8102122 to the resolvable endpoint https://api.gbif.org/v1/species/8102122. The pseudo-namespace "gbif:" is recommended by GBIF to reference GBIF taxon records. Where resolvable persistent identifiers exist for dwc:scientificNameID values, they should be used in full, but implementers will need to support at least the "gbif:" pseudo-namespace.

[🠱](#indexes-to-the-tests)
********************

###  AMENDMENT_TAXONRANK_STANDARDIZED

####  Amendment dwc:taxonRank Standardized
https://rs.tdwg.org/bdqtest/terms/e39098df-ef46-464c-9aef-bcdeee2a88cb/2023-09-18
Acts upon  SingleRecord

#### Description

Proposes an amendment to the value of dwc:taxonRank using the bdq:sourceAuthority.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; AMENDED the value of dwc:taxonRank if it can be unambiguously matched to a term in the bdq:sourceAuthority; otherwise NOT_AMENDED

#### Information Elements

Acted upon: 
dwc:taxonRank

#### Parameters

bdq:sourceAuthority

#### Default Parameter Values

bdq:sourceAuthority default = "GBIF TaxonRank Vocabulary" [https://api.gbif.org/v1/vocabularies/TaxonRank]} {"dwc:taxonRank vocabulary API" [https://api.gbif.org/v1/vocabularies/TaxonRank/concepts]}}

#### Examples

dwc:taxonRank="sp.": Response.status=AMENDED, Response.result=dwc:taxonRank="species", Response.comment="dwc:taxonRank contains an interpretable value in the bdq:sourceAuthority"

dwc:taxonRank="sic.": Response.status=NOT_AMENDED, Response.result="", Response.comment="dwc:taxonRank does not contain an interpretable value in the bdq:sourceAuthority"


#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For reference, information about possible values of dwc:taxonRank can be found at https://registry.gbif.org/vocabulary/TaxonRank/concepts

[🠱](#indexes-to-the-tests)
********************


## Measures operating on Test Responses for Multi Records (datasets)

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:basisOfRecord Not Empty
https://rs.tdwg.org/bdqtest/terms/b60c8c58-0137-4b6a-97e9-57d8ca5cf248/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_BASISOFRECORD_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:basisOfRecord is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_BASISOFRECORD_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:basisOfRecord Standard
https://rs.tdwg.org/bdqtest/terms/f5dd74bd-6a22-4792-b675-c7ccf2a2c103/2024-08-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_BASISOFRECORD_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; COMPLIANT if the value of dwc:basisOfRecord is valid in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_BASISOFRECORD_STANDARD.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dc:type Not Empty
https://rs.tdwg.org/bdqtest/terms/f041ab17-d834-4586-aa6b-090de2e571a8/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DCTYPE_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dc:type is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DCTYPE_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DCTYPE_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dc:type Standard
https://rs.tdwg.org/bdqtest/terms/fbe47441-500f-44c7-a1bd-1e872edc5266/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DCTYPE_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; COMPLIANT if the value of dc:type is a term name in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DCTYPE_STANDARD.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dcterms:license Not Empty
https://rs.tdwg.org/bdqtest/terms/47ee20d9-5087-4f76-a494-6fea05e50b8b/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_LICENSE_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dcterms:license is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_LICENSE_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_LICENSE_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dcterms:license Standard
https://rs.tdwg.org/bdqtest/terms/9d5be694-f5da-465d-8c7e-27e6dac69f9f/2024-03-21
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_LICENSE_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dcterms:license is bdq:Empty; COMPLIANT if the value of the term dcterms:license is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_LICENSE_STANDARD.Response

#### Use Cases

bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_BASISOFRECORD_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:basisOfRecord Not Empty
https://rs.tdwg.org/bdqtest/terms/c8c61535-ab1a-4ec6-b4e9-f5f02541d7d8/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_BASISOFRECORD_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:basisOfRecord is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_BASISOFRECORD_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_BASISOFRECORD_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:basisOfRecord Standard
https://rs.tdwg.org/bdqtest/terms/241a279c-76d5-499b-ab49-a47ad7f8df50/2024-08-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_BASISOFRECORD_STANDARD in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:basisOfRecord is bdq:Empty; COMPLIANT if the value of dwc:basisOfRecord is valid in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_BASISOFRECORD_STANDARD.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DCTYPE_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dc:type Not Empty
https://rs.tdwg.org/bdqtest/terms/4d999a65-a431-4a76-b591-e0d86dcf244b/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DCTYPE_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dc:type is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DCTYPE_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DCTYPE_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dc:type Standard
https://rs.tdwg.org/bdqtest/terms/d9493fa0-d90e-41db-95f6-d1c1d243540e/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DCTYPE_STANDARD in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the value of dc:type is bdq:Empty; COMPLIANT if the value of dc:type is a term name in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DCTYPE_STANDARD.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_LICENSE_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dcterms:license Not Empty
https://rs.tdwg.org/bdqtest/terms/4fccf163-9336-4f48-996c-57f5f66e72db/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_LICENSE_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dcterms:license is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_LICENSE_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_LICENSE_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dcterms:license Standard
https://rs.tdwg.org/bdqtest/terms/acd8d43e-7a2a-4372-b887-fb53a9972dc9/2024-03-21
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_LICENSE_STANDARD in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dcterms:license is bdq:Empty; COMPLIANT if the value of the term dcterms:license is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_LICENSE_STANDARD.Response

#### Use Cases

bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESCOUNTRYCODE_CONSISTENT

####  Measurement over MultiRecord Counting Compliance of Validation Coordinates dwc:countryCode Consistent
https://rs.tdwg.org/bdqtest/terms/d68dc111-9704-4fc5-a8eb-5fa084809202/2024-08-30
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if one or more of dwc:decimalLatitude, dwc:decimalLongitude, or dwc:countryCode are bdq:Empty or invalid; COMPLIANT if the geographic coordinates fall on or within the boundary defined by the union of the boundary of the country from dwc:countryCode plus it's Exclusive Economic Zone as found in the bdq:sourceAuthority, if any, plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESSTATEPROVINCE_CONSISTENT

####  Measurement over MultiRecord Counting Compliance of Validation Coordinates dwc:stateProvince Consistent
https://rs.tdwg.org/bdqtest/terms/c6c998af-6145-4361-b1e6-52c5b790340a/2024-08-30
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or invalid, or dwc:stateProvince is bdq:Empty or not found in the bdq:sourceAuthority; COMPLIANT if the geographic coordinates fall on or within the boundary in the bdq:sourceAuthority for the given dwc:stateProvince (after coordinate reference system transformations, if any, have been accounted for), or within the distance given by bdq:spatialBufferInMeters outside that boundary; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATESTERRESTRIALMARINE_CONSISTENT

####  Measurement over MultiRecord Counting Compliance of Validation Coordinates Terrestrial Marine
https://rs.tdwg.org/bdqtest/terms/b67f41f4-198c-41e9-9419-ba3919c1be8b/2024-08-30
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if either bdq:taxonIsMarine or bdq:geospatialLand are not available; INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:scientificName is bdq:Empty or (2)  the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or (3) if bdq:assumptionOnUnknownBiome is noassumption and the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine; COMPLIANT if (1) the taxon marine/nonmarine status from bdq:taxonIsMarine matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters or (2)  if the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine and bdq:assumptionOnUnknownBiome matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATES_NOTZERO

####  Measurement over MultiRecord Counting Compliance of Validation Coordinates Not Zero
https://rs.tdwg.org/bdqtest/terms/0e239a55-0f19-4c68-bdbf-20580f27a647/2023-06-20
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COORDINATES_NOTZERO in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or is not interpretable as a number, or dwc:decimalLongitude is bdq:Empty or is not interpretable as a number; COMPLIANT if either the value of dwc:decimalLatitude is not = 0 or the value of dwc:decimalLongitude is not = 0; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATES_NOTZERO.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COORDINATEUNCERTAINTY_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:coordinateUncertaintyInMeters In Range
https://rs.tdwg.org/bdqtest/terms/2d90d94b-d384-4bac-aa68-c6800d765882/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:coordinateUncertaintyInMeters is bdq:Empty; COMPLIANT if the value of  dwc:coordinateUncertaintyInMeters is interpreted as a number between 1 and 20037509 inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:countryCode Not Empty
https://rs.tdwg.org/bdqtest/terms/d71be8d4-1a04-4816-90c5-49808c823651/2024-11-10
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COUNTRYCODE_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:countryCode is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCODE_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:countryCode Standard
https://rs.tdwg.org/bdqtest/terms/38966850-3737-4a67-953c-c231469e0489/2024-09-19
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COUNTRYCODE_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYCODE_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYCOUNTRYCODE_CONSISTENT

####  Measurement over MultiRecord Counting Compliance of Validation dwc:country dwc:countryCode Consistent
https://rs.tdwg.org/bdqtest/terms/26b46375-df2b-4677-a2e5-f96f86b8e242/2024-09-25
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either of the terms dwc:country or dwc:countryCode are bdq:Empty; COMPLIANT if the values of dwc:country and dwc:countryCode match national-level country name and matching country code respectively in the bdq:sourceAuthority

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRYSTATEPROVINCE_UNAMBIGUOUS

####  Measurement over MultiRecord Counting Compliance of Validation dwc:country dwc:stateProvince Unambiguous
https://rs.tdwg.org/bdqtest/terms/8b73f37d-89ed-479a-8389-9e71ad2ac84d/2024-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the terms dwc:country and dwc:stateProvince are bdq:Empty; COMPLIANT if the combination of values of dwc:country and dwc:stateProvince are unambiguously resolved to a single result with a child-parent relationship in the bdq:sourceAuthority and the entity matching the value of dwc:country in the bdq:sourceAuthority is an ISO 3166 country-like administrative entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:country Found
https://rs.tdwg.org/bdqtest/terms/f15c38c3-d96d-4e9c-982d-410fb71cf2bc/2024-08-19
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COUNTRY_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:country is bdq:Empty; COMPLIANT if value of dwc:country is a place type equivalent to administrative entity of "nation" in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRY_FOUND.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_COUNTRY_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:country Not Empty
https://rs.tdwg.org/bdqtest/terms/6887c881-dc52-409b-8979-9c2f05e55569/2024-09-27
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_COUNTRY_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:country is bdq:NotEmpty or dwc:countryCode has a value of "XZ" and either dwc:country is bdq:Empty or has a value of "High seas"; otherwise NOT_COMPLIANT ?

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRY_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLatitude In Range
https://rs.tdwg.org/bdqtest/terms/f0fb1c79-9e3d-4d6c-a5a9-087cf57ebd26/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DECIMALLATITUDE_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or the value is not interpretable as a number; COMPLIANT if the value of dwc:decimalLatitude is between -90 and 90, inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLATITUDE_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLatitude Not Empty
https://rs.tdwg.org/bdqtest/terms/bceae35a-52ab-4968-846f-069ace766513/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:decimalLatitude is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLongitude In Range
https://rs.tdwg.org/bdqtest/terms/c70c4950-2246-4acc-a59d-81eaa47edf2b/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DECIMALLONGITUDE_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLongitude is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:decimalLongitude is between -180 and 180 degrees, inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DECIMALLONGITUDE_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:decimalLongitude Not Empty
https://rs.tdwg.org/bdqtest/terms/f948a30e-8084-48d5-b1ca-d77c476f181f/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:decimalLongitude is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:geodeticDatum Not Empty
https://rs.tdwg.org/bdqtest/terms/63fbaf3c-3d41-4ab6-bfc0-904f1b26835f/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_GEODETICDATUM_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:geodeticDatum is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_GEODETICDATUM_STANDARD

####  Measurement over MultiRecord Counting Compliance of Vaildation dwc:geodeticDatum Standard
https://rs.tdwg.org/bdqtest/terms/8d8aba5c-f58a-49c9-a08d-1afb5ff1aa63/2025-03-03
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_GEODETICDATUM_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available, INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; COMPLIANT if the value of dwc:geodeticDatum is a valid code from the bdq:sourceAuthority (in the form Authority:Number) for a Datum, or ellipsoid, or for a CRS appropriate for a 2D geographic coordinate in degrees, or is the value "not recorded"; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_GEODETICDATUM_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_LOCATION_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dcterms:Location Not Empty
https://rs.tdwg.org/bdqtest/terms/bac852b5-1ba6-427b-aa8e-02018e99279c/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_LOCATION_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if at least one term needed to determine the location of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_LOCATION_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXDEPTH_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:maximumDepthInMeters In Range
https://rs.tdwg.org/bdqtest/terms/3de8af03-05d4-4fd8-8e6d-ba886dc5446f/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_MAXDEPTH_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumDepthInMeters is bdq:Empty or is not interpretable as a number greater than or equal to zero; COMPLIANT if the value of dwc:maximumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MAXDEPTH_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_MAXELEVATION_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:maximumElevationInMeters In Range
https://rs.tdwg.org/bdqtest/terms/6a3baf78-5ec3-4a84-8c6b-6876b3a4e3b5/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_MAXELEVATION_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumElevationInMeters is bdq:Empty or the value cannot be interpreted as a number; COMPLIANT if the value of dwc:maximumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MAXELEVATION_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:minimumDepthInMeters In Range
https://rs.tdwg.org/bdqtest/terms/9c66c116-6644-45b4-b4c7-db7a4ee7c500/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_MINDEPTH_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters is bdq:Empty, or the value is not interpretable as number greater than or equal to zero; COMPLIANT if the value of dwc:minimumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINDEPTH_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINDEPTH_LESSTHAN_MAXDEPTH

####  Measurement over MultiRecord Counting Compliance of Validation  dwc:minimumDepthInMeters Less Than dwc:maximumDepthInMeters
https://rs.tdwg.org/bdqtest/terms/b21256c2-4bb7-4deb-852d-a9eaa05345e7/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters is bdq:Empty, or if either are interpretable as not zero or a positive number; COMPLIANT if the value of dwc:minimumDepthInMeters is less than or equal to the value of dwc:maximumDepthInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:minimumElevationInMeters In Range
https://rs.tdwg.org/bdqtest/terms/071267a0-d993-4961-a3f7-d8210810d167/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_MINELEVATION_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINELEVATION_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_MINELEVATION_LESSTHAN_MAXELEVATION

####  Measurement over MultiRecord Counting Compliance of Validation dwc:minimumElevationInMeters Less Than dwcmaximumElevationInMeters
https://rs.tdwg.org/bdqtest/terms/be2eb717-b390-47d1-b7ba-965a1101e215/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumlevationInMeters or dwc:minimumElevationInMeters is bdq:Empty, or if either is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is a number less than or equal to the value of the number dwc:maximumElevationInMeters, otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_STATEPROVINCE_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:stateProvince Found
https://rs.tdwg.org/bdqtest/terms/58fdd5c1-6201-49a1-a7cd-f49c210dc0b6/2024-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_STATEPROVINCE_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:stateProvince is bdq:Empty; COMPLIANT if the value of dwc:stateProvince occurs as an administrative entity that is a child to at least one entity representing an ISO 3166 country-like entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_STATEPROVINCE_FOUND.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COORDINATESCOUNTRYCODE_CONSISTENT

####  Measurement over MultiRecord for QualityAssurance of Validation Coordinates dwc:countryCode Consistent
https://rs.tdwg.org/bdqtest/terms/86c28d5e-f778-4230-88d8-64cc01478601/2024-08-30
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if one or more of dwc:decimalLatitude, dwc:decimalLongitude, or dwc:countryCode are bdq:Empty or invalid; COMPLIANT if the geographic coordinates fall on or within the boundary defined by the union of the boundary of the country from dwc:countryCode plus it's Exclusive Economic Zone as found in the bdq:sourceAuthority, if any, plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COORDINATESSTATEPROVINCE_CONSISTENT

####  Measurement over MultiRecord for QualityAssurance of Validation Coordinates dwc:stateProvince Consistent
https://rs.tdwg.org/bdqtest/terms/7a8b0af3-fa7d-416a-921a-8992d56f8233/2024-08-30
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or invalid, or dwc:stateProvince is bdq:Empty or not found in the bdq:sourceAuthority; COMPLIANT if the geographic coordinates fall on or within the boundary in the bdq:sourceAuthority for the given dwc:stateProvince (after coordinate reference system transformations, if any, have been accounted for), or within the distance given by bdq:spatialBufferInMeters outside that boundary; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COORDINATESTERRESTRIALMARINE_CONSISTENT

####  Measurement over MultiRecord for QualityAssurance of Validation Coordinates Terrestrial Marine
https://rs.tdwg.org/bdqtest/terms/478dee00-98d0-4154-b66c-eca64dbbf86d/2024-08-30
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if either bdq:taxonIsMarine or bdq:geospatialLand are not available; INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:scientificName is bdq:Empty or (2)  the values of dwc:decimalLatitude or dwc:decimalLongitude are bdq:Empty or (3) if bdq:assumptionOnUnknownBiome is noassumption and the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine; COMPLIANT if (1) the taxon marine/nonmarine status from bdq:taxonIsMarine matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters or (2)  if the marine/nonmarine status of the taxon is not interpretable from bdq:taxonIsMarine and bdq:assumptionOnUnknownBiome matches the marine/nonmarine status of dwc:decimalLatitude and dwc:decimalLongitude on the boundaries given by bdq:geospatialLand plus an exterior buffer given by bdq:spatialBufferInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COORDINATES_NOTZERO

####  Measurement over MultiRecord for QualityAssurance of Validation Coordinates Not Zero
https://rs.tdwg.org/bdqtest/terms/151b2d29-3460-4ba5-a226-86971dc8ad03/2023-06-20
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COORDINATES_NOTZERO in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or is not interpretable as a number, or dwc:decimalLongitude is bdq:Empty or is not interpretable as a number; COMPLIANT if either the value of dwc:decimalLatitude is not = 0 or the value of dwc:decimalLongitude is not = 0; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATES_NOTZERO.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COORDINATEUNCERTAINTY_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:coordinateUncertaintyInMeters In Range
https://rs.tdwg.org/bdqtest/terms/d94b0130-7a13-4fa8-955c-eff5c47bd9de/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COORDINATEUNCERTAINTY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:coordinateUncertaintyInMeters is bdq:Empty; COMPLIANT if the value of  dwc:coordinateUncertaintyInMeters is interpreted as a number between 1 and 20037509 inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COORDINATEUNCERTAINTY_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COUNTRYCODE_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:countryCode Not Empty
https://rs.tdwg.org/bdqtest/terms/942f63bd-d19d-4214-bf8e-cec0055b8909/2024-11-10
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COUNTRYCODE_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:countryCode is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYCODE_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COUNTRYCODE_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:countryCode Standard
https://rs.tdwg.org/bdqtest/terms/fedf27b2-e01d-459f-98fc-7f0f39e3d4be/2024-09-19
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COUNTRYCODE_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the dwc:countryCode is bdq:Empty; COMPLIANT if dwc:countryCode can be unambiguously interpreted as a valid ISO 3166-1-alpha-2 country code in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYCODE_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COUNTRYCOUNTRYCODE_CONSISTENT

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:country dwc:countryCode Consistent
https://rs.tdwg.org/bdqtest/terms/57b40d9a-67d7-4916-9c27-dbb395c6c27e/2024-09-25
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if either of the terms dwc:country or dwc:countryCode are bdq:Empty; COMPLIANT if the values of dwc:country and dwc:countryCode match national-level country name and matching country code respectively in the bdq:sourceAuthority

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COUNTRYSTATEPROVINCE_UNAMBIGUOUS

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:country dwc:stateProvince Unambiguous
https://rs.tdwg.org/bdqtest/terms/23aced89-d613-479c-bc4c-837d74b73be0/2024-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if the terms dwc:country and dwc:stateProvince are bdq:Empty; COMPLIANT if the combination of values of dwc:country and dwc:stateProvince are unambiguously resolved to a single result with a child-parent relationship in the bdq:sourceAuthority and the entity matching the value of dwc:country in the bdq:sourceAuthority is an ISO 3166 country-like administrative entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COUNTRY_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:country Found
https://rs.tdwg.org/bdqtest/terms/388e74b3-2e18-4d78-8112-3142d1177e25/2024-08-19
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COUNTRY_FOUND in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:country is bdq:Empty; COMPLIANT if value of dwc:country is a place type equivalent to administrative entity of "nation" in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRY_FOUND.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_COUNTRY_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:country Not Empty
https://rs.tdwg.org/bdqtest/terms/9c8df974-8fba-4537-8c67-31466787f732/2024-09-27
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_COUNTRY_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:country is bdq:NotEmpty or dwc:countryCode has a value of "XZ" and either dwc:country is bdq:Empty or has a value of "High seas"; otherwise NOT_COMPLIANT ?

#### Information Elements

Acted upon: 
bdq:VALIDATION_COUNTRY_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLatitude In Range
https://rs.tdwg.org/bdqtest/terms/3c8bc478-f6b2-4533-b7ce-45bae5d186c2/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DECIMALLATITUDE_INRANGE in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLatitude is bdq:Empty or the value is not interpretable as a number; COMPLIANT if the value of dwc:decimalLatitude is between -90 and 90, inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLATITUDE_INRANGE.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DECIMALLATITUDE_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLatitude Not Empty
https://rs.tdwg.org/bdqtest/terms/a2535b23-4407-40bd-b23b-30c8185d72a2/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DECIMALLATITUDE_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:decimalLatitude is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLATITUDE_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLongitude In Range
https://rs.tdwg.org/bdqtest/terms/6f7a9b82-7d34-4111-a2a6-9efe5221fa44/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DECIMALLONGITUDE_INRANGE in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:decimalLongitude is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:decimalLongitude is between -180 and 180 degrees, inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLONGITUDE_INRANGE.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DECIMALLONGITUDE_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:decimalLongitude Not Empty
https://rs.tdwg.org/bdqtest/terms/a94e986e-dbc8-4147-872d-5f2727945654/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DECIMALLONGITUDE_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:decimalLongitude is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DECIMALLONGITUDE_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_GEODETICDATUM_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:geodeticDatum Not Empty
https://rs.tdwg.org/bdqtest/terms/488c1dff-21ec-4e68-a00a-7355505e180c/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_GEODETICDATUM_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:geodeticDatum is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_GEODETICDATUM_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_GEODETICDATUM_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Vaildation dwc:geodeticDatum Standard
https://rs.tdwg.org/bdqtest/terms/cb88b6d9-85b2-4cd5-9bfa-c0d96f79552e/2025-03-03
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_GEODETICDATUM_STANDARD in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available, INTERNAL_PREREQUISITES_NOT_MET if dwc:geodeticDatum is bdq:Empty; COMPLIANT if the value of dwc:geodeticDatum is a valid code from the bdq:sourceAuthority (in the form Authority:Number) for a Datum, or ellipsoid, or for a CRS appropriate for a 2D geographic coordinate in degrees, or is the value "not recorded"; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_GEODETICDATUM_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_LOCATION_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dcterms:Location Not Empty
https://rs.tdwg.org/bdqtest/terms/3b2e4791-1a5a-4087-9e8d-09c67cf8c816/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_LOCATION_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if at least one term needed to determine the location of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_LOCATION_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_MAXDEPTH_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:maximumDepthInMeters In Range
https://rs.tdwg.org/bdqtest/terms/c73d49d1-06e4-4272-8249-6a26e7f8abca/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_MAXDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumDepthInMeters is bdq:Empty or is not interpretable as a number greater than or equal to zero; COMPLIANT if the value of dwc:maximumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MAXDEPTH_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_MAXELEVATION_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:maximumElevationInMeters In Range
https://rs.tdwg.org/bdqtest/terms/7c5a6ba0-399d-4570-878a-4a064e2406fe/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_MAXELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumElevationInMeters is bdq:Empty or the value cannot be interpreted as a number; COMPLIANT if the value of dwc:maximumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MAXELEVATION_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_MINDEPTH_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumDepthInMeters In Range
https://rs.tdwg.org/bdqtest/terms/49d756a8-e654-4267-a290-d1def5d2c5f9/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_MINDEPTH_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters is bdq:Empty, or the value is not interpretable as number greater than or equal to zero; COMPLIANT if the value of dwc:minimumDepthInMeters is within the range of bdq:minimumValidDepthInMeters to bdq:maximumValidDepthInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINDEPTH_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_MINDEPTH_LESSTHAN_MAXDEPTH

####  Measurement over MultiRecord for QualityAssurance of Validation  dwc:minimumDepthInMeters Less Than dwc:maximumDepthInMeters
https://rs.tdwg.org/bdqtest/terms/fcabd2c9-392c-4841-a5d7-e2680c9587ab/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumDepthInMeters or dwc:maximumDepthInMeters is bdq:Empty, or if either are interpretable as not zero or a positive number; COMPLIANT if the value of dwc:minimumDepthInMeters is less than or equal to the value of dwc:maximumDepthInMeters; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_MINELEVATION_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumElevationInMeters In Range
https://rs.tdwg.org/bdqtest/terms/1ba18c8b-66a6-47d9-a709-404439332dba/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_MINELEVATION_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:minimumElevationInMeters is bdq:Empty or the value is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is within the range of bdq:minimumValidElevationInMeters to bdq:maximumValidElevationInMeters inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINELEVATION_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_MINELEVATION_LESSTHAN_MAXELEVATION

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:minimumElevationInMeters Less Than dwcmaximumElevationInMeters
https://rs.tdwg.org/bdqtest/terms/44f00697-ca66-43cf-8f16-646b40c0f514/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:maximumlevationInMeters or dwc:minimumElevationInMeters is bdq:Empty, or if either is not a number; COMPLIANT if the value of dwc:minimumElevationInMeters is a number less than or equal to the value of the number dwc:maximumElevationInMeters, otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_STATEPROVINCE_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:stateProvince Found
https://rs.tdwg.org/bdqtest/terms/9c1cdf6a-0dbf-4828-a2e3-fb368f74d194/2024-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_STATEPROVINCE_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:stateProvince is bdq:Empty; COMPLIANT if the value of dwc:stateProvince occurs as an administrative entity that is a child to at least one entity representing an ISO 3166 country-like entity in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_STATEPROVINCE_FOUND.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:day In Range
https://rs.tdwg.org/bdqtest/terms/780480ff-8c4a-4276-aaca-cbd1248de9fa/2024-09-16
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DAY_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:day is bdq:Empty, or (2) dwc:day is not interpretable as an integer, or (3) dwc:day is interpretable as an integer between 29 and 31 inclusive and dwc:month is not interpretable as an integer between 1 and 12, or (4) dwc:month is interpretable as the integer 2 and dwc:day is interpretable as the integer 29 and dwc:year is not interpretable as a valid ISO 8601 year; COMPLIANT if (1) the value of dwc:day is interpretable as an integer between 1 and 28 inclusive, or (2) dwc:day is interpretable as an integer between 29 and 30 and dwc:month is interpretable as an integer in the set (4,6,9,11), or (3) dwc:day is interpretable as an integer between 29 and 31 and dwc:month is interpretable as an integer in the set (1,3,5,7,8,10,12), or (4) dwc:day is interpretable as the integer 29 and dwc:month is interpretable as the integer 2 and dwc:year is interpretable as is a valid leap year (evenly divisible by 400 or (evenly divisible by 4 but not evenly divisible by 100)); otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_DAY_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DAY_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:day Standard
https://rs.tdwg.org/bdqtest/terms/c3e0100f-dfc3-4379-a855-df878eef295e/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DAY_STANDARD in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_DAY_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_ENDDAYOFYEAR_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:endDayOfYear In Range
https://rs.tdwg.org/bdqtest/terms/7775309b-5331-4a65-b839-cbe959948d33/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_ENDDAYOFYEAR_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is bdq:Empty or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate In Range
https://rs.tdwg.org/bdqtest/terms/c8250600-de61-4047-9d7c-6e06a38c7994/2024-09-16
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_EVENTDATE_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the range of dwc:eventDate is entirely within the range bdq:earliestValidDate to bdq:latestValidDate, inclusive, otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTDATE_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate Not Empty
https://rs.tdwg.org/bdqtest/terms/3f62eaa2-747f-456b-85e6-1a6e74086a18/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_EVENTDATE_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:eventDate is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTDATE_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:eventDate Standard
https://rs.tdwg.org/bdqtest/terms/bffd7499-aca3-423f-bb43-f7bdc9260f4f/2024-09-16
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_EVENTDATE_STANDARD in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; COMPLIANT if the value of dwc:eventDate is a valid ISO 8601 date; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTDATE_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENTTEMPORAL_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:Event Temporal Not Empty
https://rs.tdwg.org/bdqtest/terms/d3e282a1-3ff3-4ed0-bd08-fa23b6b8c161/2023-09-30
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if any of dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate are bdq:NotEmpty; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_EVENT_CONSISTENT

####  Measurement over MultiRecord Counting Compliance of Validation dwc:Event Consistent
https://rs.tdwg.org/bdqtest/terms/1919f212-b7db-4b6e-9697-41a715001bd6/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_EVENT_CONSISTENT in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty, or all of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear are bdq:Empty; COMPLIANT if all of the following conditions are met (1) dwc:year is bdq:Empty or dwc:eventDate has a precision of one year or finer and and is within a single year and the provided value of dwc:year matches the year expressed in dwc:eventDate, and (2) dwc:month is bdq:Empty or dwc:eventDate has a precision of one month or finer and is within a single month and the provided value in dwc:month matches the month represented by dwc:eventDate, and (3) dwc:day is bdq:Empty or dwc:eventDate has a precision of a day or less and is within a single day and the provided value in dwc:day matches the day represented by dwc:eventDate, and (4) dwc:startDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:startDayOfYear matches the start day of the year of the range represented by dwc:eventDate, and (5) dwc:endDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:endDayOfYear matches the end day of the year of the range represented by dwc:eventDate; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENT_CONSISTENT.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_MONTH_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:month Standard
https://rs.tdwg.org/bdqtest/terms/c3b4cd93-a37f-4a0a-89dd-7ce53669f1f3/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_MONTH_STANDARD in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; COMPLIANT if the value of dwc:month is interpretable as an integer between 1 and 12 inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MONTH_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_STARTDAYOFYEAR_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:startDayOfYear In Range
https://rs.tdwg.org/bdqtest/terms/76008c6b-c56a-4233-84e3-8584950037ec/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_STARTDAYOFYEAR_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:startDayOfYear is bdq:Empty or if the value of dwc:startDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find single year or a start year in a range); COMPLIANT if the value of dwc:startDayOfYear is an integer between 1 and 365, inclusive, or if the value of dwc:startDayOfYear is 366 and the start year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:year In Range
https://rs.tdwg.org/bdqtest/terms/aee65eb8-8d1e-4b8f-bd37-5822e29f5734/2024-08-23
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_YEAR_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:year is bdq:Empty or cannot be interpreted as an integer; COMPLIANT if the value of dwc:year is within the range bdq:earliestValidDate to bdq:latestValidDate inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_YEAR_INRANGE.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_YEAR_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:year Not Empty
https://rs.tdwg.org/bdqtest/terms/687d3ad1-93a3-4a1f-b69f-da5a1eb761a5/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_YEAR_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:year is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_YEAR_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DAY_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:day In Range
https://rs.tdwg.org/bdqtest/terms/85dc5d02-9847-420f-a026-6a0e70962d2a/2024-09-16
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DAY_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:day is bdq:Empty, or (2) dwc:day is not interpretable as an integer, or (3) dwc:day is interpretable as an integer between 29 and 31 inclusive and dwc:month is not interpretable as an integer between 1 and 12, or (4) dwc:month is interpretable as the integer 2 and dwc:day is interpretable as the integer 29 and dwc:year is not interpretable as a valid ISO 8601 year; COMPLIANT if (1) the value of dwc:day is interpretable as an integer between 1 and 28 inclusive, or (2) dwc:day is interpretable as an integer between 29 and 30 and dwc:month is interpretable as an integer in the set (4,6,9,11), or (3) dwc:day is interpretable as an integer between 29 and 31 and dwc:month is interpretable as an integer in the set (1,3,5,7,8,10,12), or (4) dwc:day is interpretable as the integer 29 and dwc:month is interpretable as the integer 2 and dwc:year is interpretable as is a valid leap year (evenly divisible by 400 or (evenly divisible by 4 but not evenly divisible by 100)); otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_DAY_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DAY_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:day Standard
https://rs.tdwg.org/bdqtest/terms/371035f6-42b5-494f-86d9-de2f44a6cdc6/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:day is bdq:Empty; COMPLIANT if the value of the field dwc:day is an integer between 1 and 31 inclusive; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_DAY_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_ENDDAYOFYEAR_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:endDayOfYear In Range
https://rs.tdwg.org/bdqtest/terms/c04d428a-13d0-4766-9df7-4dfb2ef5d5d8/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_ENDDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:endDayOfYear is bdq:Empty or if the value of dwc:endDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find a single year or an end year in a range); COMPLIANT if the value of dwc:endDayOfYear is an integer between 1 and 365 inclusive, or if the value of dwc:endDayOfYear is 366 and the end year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_ENDDAYOFYEAR_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_EVENTDATE_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate In Range
https://rs.tdwg.org/bdqtest/terms/d41a731b-2e2b-4442-9217-4c375ae92926/2024-09-16
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_EVENTDATE_INRANGE in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty or if the value of dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the range of dwc:eventDate is entirely within the range bdq:earliestValidDate to bdq:latestValidDate, inclusive, otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTDATE_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_EVENTDATE_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate Not Empty
https://rs.tdwg.org/bdqtest/terms/c23cd67d-1b5c-4e9f-a1ce-8cc6b3e9b365/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_EVENTDATE_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:eventDate is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTDATE_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_EVENTDATE_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:eventDate Standard
https://rs.tdwg.org/bdqtest/terms/14a1d51f-16ed-4148-9dc8-1e90157a9868/2024-09-16
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_EVENTDATE_STANDARD in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty; COMPLIANT if the value of dwc:eventDate is a valid ISO 8601 date; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTDATE_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_EVENTTEMPORAL_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:Event Temporal Not Empty
https://rs.tdwg.org/bdqtest/terms/f22539ef-029b-4edb-ad17-add4363f7395/2023-09-30
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_EVENTTEMPORAL_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if any of dwc:eventDate, dwc:year, dwc:month, dwc:day, dwc:startDayOfYear, dwc:endDayOfYear, dwc:verbatimEventDate are bdq:NotEmpty; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENTTEMPORAL_NOTEMPTY.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_EVENT_CONSISTENT

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:Event Consistent
https://rs.tdwg.org/bdqtest/terms/f375a3fd-4cf5-4ef4-955e-d71762ede2d8/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_EVENT_CONSISTENT in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:eventDate is bdq:Empty, or all of dwc:year, dwc:month, dwc:day, dwc:startDayOfYear and dwc:endDayOfYear are bdq:Empty; COMPLIANT if all of the following conditions are met (1) dwc:year is bdq:Empty or dwc:eventDate has a precision of one year or finer and and is within a single year and the provided value of dwc:year matches the year expressed in dwc:eventDate, and (2) dwc:month is bdq:Empty or dwc:eventDate has a precision of one month or finer and is within a single month and the provided value in dwc:month matches the month represented by dwc:eventDate, and (3) dwc:day is bdq:Empty or dwc:eventDate has a precision of a day or less and is within a single day and the provided value in dwc:day matches the day represented by dwc:eventDate, and (4) dwc:startDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:startDayOfYear matches the start day of the year of the range represented by dwc:eventDate, and (5) dwc:endDayOfYear is empty or dwc:eventDate has a precision of one day or finer and the provided value in dwc:endDayOfYear matches the end day of the year of the range represented by dwc:eventDate; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_EVENT_CONSISTENT.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_MONTH_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:month Standard
https://rs.tdwg.org/bdqtest/terms/b3c2bb86-e239-4532-ae0c-b121ec1ee025/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_MONTH_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:month is bdq:Empty; COMPLIANT if the value of dwc:month is interpretable as an integer between 1 and 12 inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_MONTH_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_STARTDAYOFYEAR_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:startDayOfYear In Range
https://rs.tdwg.org/bdqtest/terms/8c217eee-9cd0-48c3-aea0-90151c6c5bfd/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_STARTDAYOFYEAR_INRANGE in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:startDayOfYear is bdq:Empty or if the value of dwc:startDayOfYear is equal to 366 and (dwc:eventDate is bdq:Empty or the value of dwc:eventDate cannot be interpreted to find single year or a start year in a range); COMPLIANT if the value of dwc:startDayOfYear is an integer between 1 and 365, inclusive, or if the value of dwc:startDayOfYear is 366 and the start year interpreted from dwc:eventDate is a leap year; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_STARTDAYOFYEAR_INRANGE.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_YEAR_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:year In Range
https://rs.tdwg.org/bdqtest/terms/a0502c5f-608b-4e59-99da-d9490bb4d93b/2024-08-23
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_YEAR_INRANGE in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:year is bdq:Empty or cannot be interpreted as an integer; COMPLIANT if the value of dwc:year is within the range bdq:earliestValidDate to bdq:latestValidDate inclusive; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_YEAR_INRANGE.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_YEAR_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:year Not Empty
https://rs.tdwg.org/bdqtest/terms/a8fef8a8-e7c7-4a2d-adaf-7da99c896c93/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_YEAR_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:year is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_YEAR_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_INRANGE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:dateIdentified In Range
https://rs.tdwg.org/bdqtest/terms/c72fda2d-16e1-4ded-91a5-a7094339d603/2024-09-16
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DATEIDENTIFIED_INRANGE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:dateIdentified is bdq:Empty, or (2) dwc:dateIdentified contains an invalid value according to ISO 8601, or (3) bdq:includeEventDate=true and dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the value of dwc:dateIdentified is between bdq:earliestValidDate and bdq:latestValidDate inclusive and either (1) dwc:eventDate is bdq:Empty or bdq:includeEventDate=false, or (2) if dwc:eventDate is a valid ISO 8601 date and dwc:dateIdentified overlaps or is later than the dwc:eventDate; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DATEIDENTIFIED_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:dateIdentified Standard
https://rs.tdwg.org/bdqtest/terms/49b787eb-7dce-4ace-97f5-7cbb47cd8cb9/2024-09-16
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DATEIDENTIFIED_STANDARD in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; COMPLIANT if the value of dwc:dateIdentified contains a valid ISO 8601 date; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_INRANGE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:dateIdentified In Range
https://rs.tdwg.org/bdqtest/terms/6354376c-0cf2-435b-be40-850769c5a18a/2024-09-16
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DATEIDENTIFIED_INRANGE in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if (1) dwc:dateIdentified is bdq:Empty, or (2) dwc:dateIdentified contains an invalid value according to ISO 8601, or (3) bdq:includeEventDate=true and dwc:eventDate is not a valid ISO 8601 date; COMPLIANT if the value of dwc:dateIdentified is between bdq:earliestValidDate and bdq:latestValidDate inclusive and either (1) dwc:eventDate is bdq:Empty or bdq:includeEventDate=false, or (2) if dwc:eventDate is a valid ISO 8601 date and dwc:dateIdentified overlaps or is later than the dwc:eventDate; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DATEIDENTIFIED_INRANGE.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DATEIDENTIFIED_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:dateIdentified Standard
https://rs.tdwg.org/bdqtest/terms/563872eb-f544-45a0-8f91-8098d62768d4/2024-09-16
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DATEIDENTIFIED_STANDARD in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:dateIdentified is bdq:Empty; COMPLIANT if the value of dwc:dateIdentified contains a valid ISO 8601 date; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_DATEIDENTIFIED_STANDARD.Response

#### Use Cases

bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_DEGREEOFESTABLISHMENT_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:degreeofEstablishment Standard
https://rs.tdwg.org/bdqtest/terms/1b8ae68e-63f1-41c0-9025-fbe64db38d64/2024-02-09
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; COMPLIANT if the value of dwc:degreeOfEstablishment is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD.Response

#### Use Cases

bdq:Alien-Species

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_ESTABLISHMENTMEANS_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:establishmentMeans Standard
https://rs.tdwg.org/bdqtest/terms/130bb875-6b7c-4965-b864-d53f9d05b2cd/2024-02-08
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; COMPLIANT if the value of dwc:establishmentMeans is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCEID_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceID Not Empty
https://rs.tdwg.org/bdqtest/terms/0c9a139e-5d23-44de-a495-14ec08c61a1c/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_OCCURRENCEID_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:occurrenceID is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceStatus Not Empty
https://rs.tdwg.org/bdqtest/terms/298db0c9-a85a-41ee-b111-d622fd969d71/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:occurrenceStatus is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_OCCURRENCESTATUS_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:occurrenceStatus Standard
https://rs.tdwg.org/bdqtest/terms/faca6558-dbff-4d26-a5cb-e11cdf632fe7/2025-02-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_OCCURRENCESTATUS_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:Empty; COMPLIANT if the value of dwc:occurrenceStatus is resolved in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_PATHWAY_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:pathway Standard
https://rs.tdwg.org/bdqtest/terms/15e0da1d-1a43-4075-8454-b2e618cdd25b/2024-02-09
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_PATHWAY_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; COMPLIANT if the value of dwc:pathway is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_PATHWAY_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_SEX_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:sex Standard
https://rs.tdwg.org/bdqtest/terms/e4d35063-2366-4dda-8eaa-326340361da3/2024-02-09
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_SEX_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; COMPLIANT if the value of dwc:sex is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_SEX_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_TYPESTATUS_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:typeStatus Standard
https://rs.tdwg.org/bdqtest/terms/b5a14d76-292e-499b-b80f-9546243311a0/2024-11-11
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_TYPESTATUS_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; COMPLIANT if the value of the first word in each &#124; delimited portion of dwc:typeStatus is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_TYPESTATUS_STANDARD.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_DEGREEOFESTABLISHMENT_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:degreeofEstablishment Standard
https://rs.tdwg.org/bdqtest/terms/ba953672-6526-4375-97e8-b4e9d1a7d3a0/2024-02-09
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_DEGREEOFESTABLISHMENT_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:degreeOfEstablishment is bdq:Empty; COMPLIANT if the value of dwc:degreeOfEstablishment is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_DEGREEOFESTABLISHMENT_STANDARD.Response

#### Use Cases

bdq:Alien-Species

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_ESTABLISHMENTMEANS_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:establishmentMeans Standard
https://rs.tdwg.org/bdqtest/terms/8dfed701-01a9-415d-a9f8-539280b75975/2024-02-08
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_ESTABLISHMENTMEANS_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:establishmentMeans is bdq:Empty; COMPLIANT if the value of dwc:establishmentMeans is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_ESTABLISHMENTMEANS_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_OCCURRENCEID_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceID Not Empty
https://rs.tdwg.org/bdqtest/terms/0028ef9a-6553-467b-a344-90327ed2babf/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_OCCURRENCEID_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:occurrenceID is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_OCCURRENCEID_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceStatus Not Empty
https://rs.tdwg.org/bdqtest/terms/d2922585-2070-4851-a033-15e51977f9dc/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_OCCURRENCESTATUS_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:occurrenceStatus is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_OCCURRENCESTATUS_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_OCCURRENCESTATUS_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:occurrenceStatus Standard
https://rs.tdwg.org/bdqtest/terms/2fea4571-92d0-48a5-a5ba-6caecd647862/2025-02-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_OCCURRENCESTATUS_STANDARD in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:occurrenceStatus is bdq:Empty; COMPLIANT if the value of dwc:occurrenceStatus is resolved in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_OCCURRENCESTATUS_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_PATHWAY_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:pathway Standard
https://rs.tdwg.org/bdqtest/terms/ef31ba02-cea7-4d76-990f-99ebbd201fb4/2024-02-09
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_PATHWAY_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:pathway is bdq:Empty; COMPLIANT if the value of dwc:pathway is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_PATHWAY_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_SEX_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:sex Standard
https://rs.tdwg.org/bdqtest/terms/1b3bbac4-7c00-46d6-8179-1d57c92374ad/2024-02-09
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_SEX_STANDARD in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:sex is bdq:Empty; COMPLIANT if the value of dwc:sex is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_SEX_STANDARD.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_TYPESTATUS_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:typeStatus Standard
https://rs.tdwg.org/bdqtest/terms/1ca359ea-4df3-4dca-b92b-2bc8fa8e0c88/2024-11-11
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_TYPESTATUS_STANDARD in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:typeStatus is bdq:Empty; COMPLIANT if the value of the first word in each &#124; delimited portion of dwc:typeStatus is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_TYPESTATUS_STANDARD.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASSIFICATION_CONSISTENT

####  Measurement over MultiRecord Counting Compliance of Validation Classification Consistent
https://rs.tdwg.org/bdqtest/terms/a56fb342-c8ee-4611-8aab-e6c6357e8875/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_CLASSIFICATION_CONSISTENT in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of the fields dwc:kingdom dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus are bdq:Empty; COMPLIANT if the combination of values of higher classification taxonomic terms (dwc:kingdom, dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus) are consistent with the lowest ranking matched element in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_CLASS_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:class Found
https://rs.tdwg.org/bdqtest/terms/7270a362-5f2e-41f0-955a-d7a8eaaf0f17/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_CLASS_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:class is bdq:Empty; COMPLIANT if the value of dwc:class is found as a value at the rank of Class in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_CLASS_FOUND.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_FAMILY_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:family Found
https://rs.tdwg.org/bdqtest/terms/97928242-11a9-4ab0-9dd7-3f0465834824/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_FAMILY_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:family is bdq:Empty; COMPLIANT if the value of dwc:family is found as a value at the rank of Family in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_FAMILY_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_GENUS_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:genus Found
https://rs.tdwg.org/bdqtest/terms/977f7e75-a88e-4e29-a7b1-e8cdd35aa107/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_GENUS_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available;  INTERNAL_PREREQUISITES_NOT_MET if dwc:genus is bdq:Empty; COMPLIANT if the value of dwc:genus is found as a value at the rank of genus in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_GENUS_FOUND.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:kingdom Found
https://rs.tdwg.org/bdqtest/terms/012eade5-fc64-458a-a13a-a614491bf4e0/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_KINGDOM_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:kingdom is bdq:Empty; COMPLIANT if the value of dwc:kingdom is found as a value at the rank of kingdom in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_KINGDOM_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_KINGDOM_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:kingdom Not Empty
https://rs.tdwg.org/bdqtest/terms/342bd81c-e2b7-41d8-b32b-013992d19f99/2024-01-28
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_KINGDOM_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:kingdom is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_KINGDOM_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_NAMEPUBLISHEDINYEAR_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:namePublishedInYear Not Empty
https://rs.tdwg.org/bdqtest/terms/36ea0a78-a079-4014-aca3-2f2b3b11e822/2024-02-07
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:namePublishedInYear is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_ORDER_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:order Found
https://rs.tdwg.org/bdqtest/terms/f4fa449c-4b74-4dcf-b4cf-0b73e1496375/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_ORDER_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:order is bdq:Empty; COMPLIANT if the value of dwc:order is found as a value at the rank of Order in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_ORDER_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_PHYLUM_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:phylum Found
https://rs.tdwg.org/bdqtest/terms/65e66ca0-e9d1-4411-ad26-bb9c43f32afc/2022-03-25
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_PHYLUM_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdq:Empty; COMPLIANT if the value of dwc:phylum is found as a value at the rank of Phylum in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_PHYLUM_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_POLYNOMIAL_CONSISTENT

####  Measurement over MultiRecord Counting Compliance of Validation Polynomial Consistent
https://rs.tdwg.org/bdqtest/terms/7da5428e-87b2-4ec2-be82-05b9398b7577/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_POLYNOMIAL_CONSISTENT in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty, or all of dwc:genericName, dwc:specificEpithet and dwc:infraspecificEpithet are bdq:Empty; COMPLIANT if the polynomial, as represented in dwc:scientificName, is consistent with bdq:NotEmpty values of dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameAuthorship Not Empty
https://rs.tdwg.org/bdqtest/terms/dbf3cece-1d83-426e-a5e0-8158fcf9c0cd/2024-02-04
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:scientificNameAuthorship is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_COMPLETE

####  Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameID Complete
https://rs.tdwg.org/bdqtest/terms/f174ad13-3c67-49f9-8d8b-aba4e933d6f6/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set that are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty; COMPLIANT if (1) dwc:scientificNameID is a validly formed LSID, or (2) dwc:scientificNameID is a validly formed URN with at least NID and NSS present, or (3) dwc:scientificNameID is in the form scope:value, or (4) dwc:scientificNameID is a validly formed URI with host and path where path consists of more than just "/"; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAMEID_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:scientificNameID Not Empty
https://rs.tdwg.org/bdqtest/terms/a9962d33-ad08-453a-8938-2972425034c2/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:scientificNameID is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_FOUND

####  Measurement over MultiRecord Counting Compliance of Validation dwc:scientificName Found
https://rs.tdwg.org/bdqtest/terms/4e70b0e4-3fd2-4899-802c-439671374eeb/2023-09-17
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_SCIENTIFICNAME_FOUND in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty; COMPLIANT if there is a match of the contents of dwc:scientificName in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_SCIENTIFICNAME_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:scientificName Not Empty
https://rs.tdwg.org/bdqtest/terms/0f8b30e2-59dc-46ba-8b91-62049cd1a4e2/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:scientificName is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:taxonRank Not Empty
https://rs.tdwg.org/bdqtest/terms/de661615-b338-4557-af5b-d44a89de40fa/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_TAXONRANK_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if dwc:taxonRank is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXONRANK_STANDARD

####  Measurement over MultiRecord Counting Compliance of Validation dwc:taxonRank Standard
https://rs.tdwg.org/bdqtest/terms/602bc457-6b1d-4f24-adef-d0d31bcdf2f0/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_TAXONRANK_STANDARD in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; COMPLIANT if the value of dwc:taxonRank is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXONRANK_STANDARD.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_NOTEMPTY

####  Measurement over MultiRecord Counting Compliance of Validation dwc:Taxon Not Empty
https://rs.tdwg.org/bdqtest/terms/54d290e8-ac48-4f31-8af3-676363573217/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_TAXON_NOTEMPTY in a record set that are COMPLIANT.

#### Specification

COMPLIANT if at least one term needed to determine the taxon of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXON_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_COUNT_COMPLIANT_TAXON_UNAMBIGUOUS

####  Measurement over MultiRecord Counting Compliance of Validation dwc:Taxon Unambiguous
https://rs.tdwg.org/bdqtest/terms/782773c9-7b37-483d-8ce2-c6683ba81882/2023-09-18
Acts upon  MultiRecord

#### Description

Count the number of VALIDATION_TAXON_UNAMBIGUOUS in a record set that are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of dwc:scientificNameID, dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, dwc:cultivarEpithet are bdq:Empty; COMPLIANT if (1) dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority, or (2) dwc:scientificNameID is bdq:Empty and dwc:scientificName references a single taxon record in the bdq:sourceAuthority, or (3) if dwc:scientificName and dwc:scientificNameID are bdq:Empty and if a combination of the values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:cultivarEpithet, dwc:taxonRank, and dwc:scientificNameAuthorship can be unambiguously resolved to a unique taxon in the bdq:sourceAuthority, or (4) if ambiguity produced by multiple matches in (2) or (3) can be disambiguated to a unique Taxon using the values of dwc:tribe, dwc:subtribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID and dwc:vernacularName; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Control, compare the Response.result of this measure with the total number of records to assess work needed on the record set.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_CLASSIFICATION_CONSISTENT

####  Measurement over MultiRecord for QualityAssurance of Validation Classification Consistent
https://rs.tdwg.org/bdqtest/terms/a2be4734-0a93-46dc-af4a-e2125b47dbd4/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_CLASSIFICATION_CONSISTENT in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of the fields dwc:kingdom dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus are bdq:Empty; COMPLIANT if the combination of values of higher classification taxonomic terms (dwc:kingdom, dwc:phylum, dwc:class, dwc:order, dwc:superfamily, dwc:family, dwc:subfamily, dwc:tribe, dwc:subtribe, dwc:genus) are consistent with the lowest ranking matched element in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_CLASSIFICATION_CONSISTENT.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_CLASS_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:class Found
https://rs.tdwg.org/bdqtest/terms/21541436-641d-45a9-938c-537484d94eb7/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_CLASS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:class is bdq:Empty; COMPLIANT if the value of dwc:class is found as a value at the rank of Class in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_CLASS_FOUND.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_FAMILY_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:family Found
https://rs.tdwg.org/bdqtest/terms/a07d7147-2db8-48ce-81b8-e47595ad5f17/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_FAMILY_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:family is bdq:Empty; COMPLIANT if the value of dwc:family is found as a value at the rank of Family in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_FAMILY_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_GENUS_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:genus Found
https://rs.tdwg.org/bdqtest/terms/c5c8db83-3af0-4215-806f-e2f90574b138/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_GENUS_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available;  INTERNAL_PREREQUISITES_NOT_MET if dwc:genus is bdq:Empty; COMPLIANT if the value of dwc:genus is found as a value at the rank of genus in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_GENUS_FOUND.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_KINGDOM_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:kingdom Found
https://rs.tdwg.org/bdqtest/terms/465d7ac1-d193-46c0-a302-56a9ef99215f/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_KINGDOM_FOUND in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:kingdom is bdq:Empty; COMPLIANT if the value of dwc:kingdom is found as a value at the rank of kingdom in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_KINGDOM_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_KINGDOM_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:kingdom Not Empty
https://rs.tdwg.org/bdqtest/terms/3bc9df8b-0f57-4157-9374-b56a99090b22/2024-01-28
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_KINGDOM_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:kingdom is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_KINGDOM_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_NAMEPUBLISHEDINYEAR_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:namePublishedInYear Not Empty
https://rs.tdwg.org/bdqtest/terms/16059801-6adb-4e65-82f4-61eaa70d8df0/2024-02-07
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

COMPLIANT if dwc:namePublishedInYear is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_NAMEPUBLISHEDINYEAR_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_ORDER_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:order Found
https://rs.tdwg.org/bdqtest/terms/773bb288-fef3-4968-a65a-a69c74d6ecb5/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_ORDER_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:order is bdq:Empty; COMPLIANT if the value of dwc:order is found as a value at the rank of Order in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_ORDER_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_PHYLUM_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:phylum Found
https://rs.tdwg.org/bdqtest/terms/17364d16-37b7-4ccb-9614-bfb95ff1bca9/2022-03-25
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_PHYLUM_FOUND in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:phylum is bdq:Empty; COMPLIANT if the value of dwc:phylum is found as a value at the rank of Phylum in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_PHYLUM_FOUND.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_POLYNOMIAL_CONSISTENT

####  Measurement over MultiRecord for QualityAssurance of Validation Polynomial Consistent
https://rs.tdwg.org/bdqtest/terms/ef05b45b-13b8-4877-9e9d-fa44b332d83c/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_POLYNOMIAL_CONSISTENT in a record set are COMPLIANT or INTERNAL_PREREQUISITES_NOT_MET (indicating some empty value).

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty, or all of dwc:genericName, dwc:specificEpithet and dwc:infraspecificEpithet are bdq:Empty; COMPLIANT if the polynomial, as represented in dwc:scientificName, is consistent with bdq:NotEmpty values of dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_POLYNOMIAL_CONSISTENT.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameAuthorship Not Empty
https://rs.tdwg.org/bdqtest/terms/6dd6fecf-6ba1-425c-afbe-6a9ed7b65ed7/2024-02-04
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:scientificNameAuthorship is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAMEAUTHORSHIP_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_COMPLETE

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameID Complete
https://rs.tdwg.org/bdqtest/terms/a9529e71-5470-4cb1-b04d-aa483926f532/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_SCIENTIFICNAMEID_COMPLETE in a record set are COMPLIANT.

#### Specification

INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificNameID is bdq:Empty; COMPLIANT if (1) dwc:scientificNameID is a validly formed LSID, or (2) dwc:scientificNameID is a validly formed URN with at least NID and NSS present, or (3) dwc:scientificNameID is in the form scope:value, or (4) dwc:scientificNameID is a validly formed URI with host and path where path consists of more than just "/"; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAMEID_COMPLETE.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_SCIENTIFICNAMEID_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificNameID Not Empty
https://rs.tdwg.org/bdqtest/terms/4cf84216-c8a7-4865-a8e1-3ffd829d5a10/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_SCIENTIFICNAMEID_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:scientificNameID is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAMEID_NOTEMPTY.Response

#### Use Cases

bdq:Alien-Species, bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_FOUND

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificName Found
https://rs.tdwg.org/bdqtest/terms/a8aee02c-cf7c-4104-a601-d8afc4f9cbe2/2023-09-17
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_SCIENTIFICNAME_FOUND in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:scientificName is bdq:Empty; COMPLIANT if there is a match of the contents of dwc:scientificName in the bdq:sourceAuthority; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAME_FOUND.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_SCIENTIFICNAME_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:scientificName Not Empty
https://rs.tdwg.org/bdqtest/terms/b4d6a61c-64ff-4da0-974c-63a73fd20836/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_SCIENTIFICNAME_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:scientificName is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_SCIENTIFICNAME_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_TAXONRANK_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:taxonRank Not Empty
https://rs.tdwg.org/bdqtest/terms/e0b8cff1-3322-40d2-b8b2-b99fc9ae130a/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_TAXONRANK_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if dwc:taxonRank is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXONRANK_NOTEMPTY.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_TAXONRANK_STANDARD

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:taxonRank Standard
https://rs.tdwg.org/bdqtest/terms/f320ca83-8487-4011-b1ff-f4b1b4dd86ec/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_TAXONRANK_STANDARD in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if dwc:taxonRank is bdq:Empty; COMPLIANT if the value of dwc:taxonRank is in the bdq:sourceAuthority; otherwise NOT_COMPLIANT.

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXONRANK_STANDARD.Response

#### Use Cases

bdq:Record-Management, bdq:Taxon-Management

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_TAXON_NOTEMPTY

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:Taxon Not Empty
https://rs.tdwg.org/bdqtest/terms/2a9d4cfd-815a-46e0-bb51-60724582b762/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_TAXON_NOTEMPTY in a record set are COMPLIANT.

#### Specification

COMPLIANT if at least one term needed to determine the taxon of the entity exists and is bdq:NotEmpty; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXON_NOTEMPTY.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************

###  MULTIRECORD_MEASURE_QA_TAXON_UNAMBIGUOUS

####  Measurement over MultiRecord for QualityAssurance of Validation dwc:Taxon Unambiguous
https://rs.tdwg.org/bdqtest/terms/0df03601-3768-4805-906a-bbd0a41b0fda/2023-09-18
Acts upon  MultiRecord

#### Description

Measure if all VALIDATION_TAXON_UNAMBIGUOUS in a record set are COMPLIANT.

#### Specification

EXTERNAL_PREREQUISITES_NOT_MET if the bdq:sourceAuthority is not available; INTERNAL_PREREQUISITES_NOT_MET if all of dwc:scientificNameID, dwc:scientificName, dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:scientificNameAuthorship, dwc:cultivarEpithet are bdq:Empty; COMPLIANT if (1) dwc:scientificNameID references a single taxon record in the bdq:sourceAuthority, or (2) dwc:scientificNameID is bdq:Empty and dwc:scientificName references a single taxon record in the bdq:sourceAuthority, or (3) if dwc:scientificName and dwc:scientificNameID are bdq:Empty and if a combination of the values of the terms dwc:genericName, dwc:specificEpithet, dwc:infraspecificEpithet, dwc:cultivarEpithet, dwc:taxonRank, and dwc:scientificNameAuthorship can be unambiguously resolved to a unique taxon in the bdq:sourceAuthority, or (4) if ambiguity produced by multiple matches in (2) or (3) can be disambiguated to a unique Taxon using the values of dwc:tribe, dwc:subtribe, dwc:subgenus, dwc:genus, dwc:subfamily, dwc:family, dwc:superfamily, dwc:order, dwc:class, dwc:phylum, dwc:kingdom, dwc:higherClassification, dwc:taxonID, dwc:acceptedNameUsageID, dwc:originalNameUsageID, dwc:taxonConceptID and dwc:vernacularName; otherwise NOT_COMPLIANT

#### Information Elements

Acted upon: 
bdq:VALIDATION_TAXON_UNAMBIGUOUS.Response

#### Use Cases

bdq:Taxon-Management, bdq:Alien-Species, bdq:Spatial-Temporal_Patterns, bdq:Record-Management, bdq:Biotic-Relationships

#### Notes

For Quality Assurance, filter record set until this measure is COMPLETE.

[↑](#indexes-to-the-tests)
********************


## Acronyms

A list of Acronyms can be found in the [Acronyms](../../index.md#5-acronyms) section of the Biodiversity Data Quality (BDQ) landing page.

## Glossary

A glossary of terms additional to those in the various namespaces can be found in the [Glossary](../../index.md#6-glossary) section of the Biodiversity Data Quality (BDQ) landing page.

## References

The references for the BDQ standard can be found in the [References](../../index.md#7-references) section of the Biodiversity Data Quality (BDQ) landing page.

## Cite BDQ

**To cite BDQ in general, use the peer-reviewed article:**

Chapman AD, Belbin L, Zermoglio PF, Wieczorek J, Morris PJ, Nicholls
M, Rees ER, Veiga AK, Thompson A, Saraiva AM, James SA, Gendreau C,
Benson A, Schigel D (2020). Developing Standards for Improved Data
Quality and for Selecting Fit for Use Biodiversity Data.
Biodiversity Information Science and Standards 4: e50889.
https://doi.org/10.3897/biss.4.50889

**To cite this document specifically, use the following:**

TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions. 2025. BDQ Tests Quick Reference Guide. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/bdqtest/terms/2025-05-10>

**Biodiversity Information Standards (TDWG)**

This content made open by Biodiversity Information Standards (TDWG) is licensed under a [Licensed under a Creative Commons Attribution 4.0 International (CC BY) License.](http://creativecommons.org/licenses/by/4.0/)

