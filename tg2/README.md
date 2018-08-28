<h1>TG2: Data Quality Tests and Assertions</h1>

Link to tests: https://github.com/tdwg/bdq/projects/2
<h2>Motivation</h2>
Other than data availability, ‘Data Quality’ is probably the most significant issue for users of biodiversity data and this is specially so for the research community.
This Task Group is reviewing practical aspects relating to ‘data quality’ with a goal to provide Best Current Practice at the key interface between data users and data providers: tests and their resulting assertions.
If an internationally agreed standard suite of core tests can be implemented by all Data Providers and hopefully Data Collectors, then greater and more appropriate use could be made of biodiversity data. 
Data providers and particularly aggregators such as GBIF and its nodes would have increased credibility with the user communities and can provide more effective information for judging fitness for use.
The tests and assertions will initially be based on the Darwin Core standard.
I (Lee Belbin) raised the need for a practical set of tools related to Data Quality at the TDWG 2010 Conference at Woods Hole. What I was asking for was at least the public display of the rules that were being used by GBIF to flag issues in their records. This didn’t happen, so we are trying again using tests from a range of agencies.

<h2>Goals Outputs and Outcomes</h2>
A set of tests and resulting data assertions that are in use by key Data Providers to flag record issues (January 2017).
A set of principles that have emerged in the process of identifying and refining the tests and assertions. These would be expected to form the basis of a paper on ‘data quality’ tests and assertions’ (~January 2017).
A set of in-use software tools that can be used to assist with data quality (January 2017). These will be based on the GBIF Data Quality software resource.
Create a set of fundamental publications related to ‘data quality’ (March  2017 )
Submit a standard set of tests and assertions for consideration as a TDWG Standard (August 2018).

<h2>Strategy</h2>
The tests and rules generating assertions at the record-level are more fundamental than the tools or workflows that will be based on them. The priority will therefore be to create a comprehensive list of these tests, rules and assertions along with where and how they are used. For example, GBIFs set can be found at https://github.com/gbif/gbif-api/blob/master/src/main/java/org/gbif/api/vocabulary/OccurrenceIssue.java while the Atlas of Living Australia has a more comprehensive site at http://biocache.ala.org.au/ws/assertions/codes. These will form the base. Other Data Providers include iDigBio, VertNet, OBIS, CRIA and BISON.

<h2>Becoming Involved</h2>
This Task Group would welcome anyone who has a practical interest in data quality and/or has experience with the tests, rules, assertions, tools or workflows.
Please contact the Convener

<h2>History/Context</h2>
The Task Group was established in 2014 as a Task Group of the TDWG Data Quality Interest Group viz, Task Group 2: Tools, Services and Workflows. The new name and charter better reflects the work and goals of the Task Group as tests and assertions are more stable and longer lasting than the tools which will link to the relevant tests and workflows that will also depend on them. Services seems better placed with the TDWG Biodiversity Services and Clients IG.

<h2>Outcomes</h2>
The group has been working for over a year to evaluate the tests that have been run by-
<ul>
<li>The Atlas of Living Australia (ALA)</<li>
<li>The Gblobal Biodiversity Information Facility (GBIF)</li>
<li>iDigBio</li>
<li>Ocean Biogeographic Information Facility (OBIS)</li>
<li>Centro de Referência em Informação Ambiental (CRIA)</li>
<li>Biodiversity Information Serving Our Nation (BISON)</li>
<li>Vertnet</li>
  </ul>
  
and to refine these and new tests to produce a core suite of tests and assertions that can be found at https://docs.google.com/spreadsheets/d/1uwnUtcMSe88AytUt_mSepeLTz54tMvV9llO2pBnObhE. In the process, we have come up with a standard suite of descriptors for each of the tests.
  
A suite of test code and test data for each test is in development by iDigBio and hopefully will be be available not long after the core suite of tests are finalised.
  
  
