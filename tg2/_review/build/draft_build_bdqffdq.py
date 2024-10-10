# Produce markdown documents for the bdqffdq Framework 
# onntology from the owl ontology.
#
# Produces the term list, the extension list, and a
# landing pad page from templates and the ontology.
# 
# @author Paul J. Morris 
#
# Assumes run from generation/build directory of tg2 repository.
#
import re
import sys
import pandas as pd  # library to handle data loaded from csv as data frames
import yaml       # Library to parse yaml files
import rdflib     # run sparql queries on rdf 
from rdflib import Graph
import function_lib # library of reusable functions for TDWG build scripts
from function_lib import build_term_key, build_authors_contributors_markdown, build_contributors_markdown, build_authors_markdown

# Configuration: common configuration

prefixes = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdqdim: <https://rs.tdwg.org/bdqdim/terms/>
PREFIX bdqcrit: <https://rs.tdwg.org/bdqcrit/terms/>
PREFIX bdqenh: <https://rs.tdwg.org/bdqenh/terms/>
"""

# Vocabulary file
inputTermsOwlFilename = "../vocabulary/bdqffdq.owl"
bdqffdqOwlDocument = 'https://raw.githubusercontent.com/tdwg/bdq/refs/heads/master/tg2/_review/{}'.format(inputTermsOwlFilename)

# Common Files and information
contributors_yaml_file = 'authors_configuration.yaml'
term_list_document = "temp_term-lists.csv"
local_metadata_config_file = 'temp_namespaces.yaml'
has_namespace = True
namespace_uri = 'https://rs.tdwg.org/bdqffdq'
pref_namespace_prefix = "bdqffdq"
#term = "bdqffdq"

# Note: Each of the three documents has a configuration section below.

# ---------------
# Retrieve common term list metadata
# ---------------

## PJM: Unavailable from rs.tdwg.org for a draft standard lacking entries in rs.tdwg.org files
print('Loading term list metadata')
term_lists_info = []

frame = pd.read_csv(term_list_document, na_filter=False)
term_list_dict = {'list_iri': 'bdqffdq'}
term_list_dict = {'database': 'bdqffdq'}
for index,row in frame.iterrows():
    if row['database'] == 'bdqffdq':
        term_list_dict['pref_ns_prefix'] = row['vann_preferredNamespacePrefix']
        term_list_dict['pref_ns_uri'] = row['vann_preferredNamespaceUri']
        term_list_dict['list_iri'] = row['list']
term_lists_info.append(term_list_dict)

# Load the contributors YAML file from its local location.
with open(contributors_yaml_file) as cyf:
	contributors_yaml = yaml.load(cyf, Loader=yaml.FullLoader)

#############################################################
# Document 1: Landing page 

# Configuration 

# Files 
outputDirectory = "../docs/bdqffdq/"
sourceDirectory = 'templates/bdqffdq/'
outputFilename = "{}index.md".format(outputDirectory)
headerFileName = '{}bdqffdq_landing-header.md'.format(sourceDirectory)
footerFileName = '{}bdqffdq_landing-footer.md'.format(sourceDirectory)
document_configuration_yaml_file = '{}/document_configuration.yaml'.format(sourceDirectory)

# Name, Preferred Label, Definition, SubClass Of, Range, Comments, DifferentFrom
term_concept_dictionary = {
    "iri": {"label":"Term Version IRI","term":"rdf:about","normative":"true"}, 
    "term_iri": {"label":"Term IRI","term":"dcterms:isVersionOf","normative":"true"}, 
    "term_localName": {"label":"Name","term":"rdf:value","normative":"true"}, 
    "prefLabel": {"label":"Preferred Label","term":"skos:prefLabel","normative":"false"}, 
    "comments": {"label":"Comments","term":"rdfs:comment","normative":"false"}, 
    "definition": {"label":"Definition","term":"skos:definition","normative":"true"}, 
    "rdf_type": {"label":"Type","term":"rdf:type","normative":"true"}, 
    "superclass": {"label":"SubClass Of","term":"rdfs:subClassOf","normative":"true"}, 
    "range": {"label":"","Range":"","term":"rdf:","normative":"true"}, 
    "differentFrom": {"label":"DifferentFrom","term":"owl:","normative":"true"}, 
}

# Build Landing Page Document

# Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
# load from local file
with open(document_configuration_yaml_file) as dcfy:
	document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

# build definition table
graph = rdflib.Graph()
graph.parse(inputTermsOwlFilename, format="ttl")
# TODO: range, differentFrom 
# column_list = ['term_iri', 'iri', 'term_localName', 'prefLabel', 'label', 'comments', 'definition', 'rdf_type', 'superclass', 'range', 'differentFrom']
column_list = ['term_iri', 'iri', 'term_localName', 'prefLabel', 'label', 'comments', 'definition', 'rdf_type', 'superclass']
sparql = prefixes + "SELECT DISTINCT (str(?subject) as ?term_iri) (str(?subject) as ?iri) (?subject as ?term_localName)  ?prefLabel ?label ?comment ?definition ?rdf_type (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:Class . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . ?subject rdf:type ?rdf_type . ?subject rdfs:label ?label . OPTIONAL { ?subject rdfs:subClassOf ?parent } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?label ?comment ?definition ?rdf_type ORDER BY ?subject"
queryResult = graph.query(sparql)

terms_df = pd.DataFrame(queryResult, columns = column_list)
terms_sorted_by_label = terms_df.sort_values(by='label')
terms_sorted_by_localname = terms_df.iloc[terms_df.term_localName.str.lower().argsort()]

definitionTable = build_term_key(term_concept_dictionary,terms_sorted_by_localname)

# Load header 
headerObject = open(headerFileName, 'rt', encoding='utf-8')
header = headerObject.read()
headerObject.close()
# Substitute values of ratification_date and contributors into the header template
header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
# Build the Markdown for the authors and contributors lists, or the authors list, or the contributors list
contributors = build_authors_contributors_markdown(contributors_yaml)
header = header.replace('{authors_contributors}', contributors)
contributors = build_contributors_markdown(contributors_yaml)
header = header.replace('{contributors}', contributors)
contributors = build_authors_markdown(contributors_yaml)
header = header.replace('{authors}', contributors)
header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
header = header.replace('{current_iri}', document_configuration_yaml['current_iri'])
header = header.replace('{abstract}', document_configuration_yaml['abstract'])
header = header.replace('{creator}', document_configuration_yaml['creator'])
header = header.replace('{publisher}', document_configuration_yaml['publisher'])
header = header.replace('{comment}', document_configuration_yaml['comment'])
year = document_configuration_yaml['doc_modified'].split('-')[0]
header = header.replace('{year}', year)
if has_namespace:
    header = header.replace('{namespace_uri}', namespace_uri)
    header = header.replace('{pref_namespace_prefix}', pref_namespace_prefix)
header = header.replace('{term_key}', definitionTable)

# ---------------
# Load rdf, format for landing page
# ---------------
text = ""

graph = rdflib.Graph()
graph.parse(inputTermsOwlFilename, format="ttl")

text = "\n"
text = text + "- [Classes](#41-Class-terms)\n"
text = text + "- [Object Properties](#42-ObjectProperty-terms)\n"
text = text + "- [Data Properties](#43-DataProperty-terms)\n"
text = text + "- [Named Individuals](#44-NamedIndividual-terms)\n"
text = text + "\n"

text = text + "#### 3.2.1 Alphabetical Index of classes\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:Class . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "#### 3.2.2 Alphabetical Index of object properties\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:ObjectProperty . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "#### 3.2.3 Alphabetical Index of data properties\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:DatatypeProperty . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "#### 3.2.4 Alphabetical Index of named individuals\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:NamedIndividual . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "\n## 4 Vocabulary\n"
text = text + "\n### 4.1 Class terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:Class . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . OPTIONAL { ?subject rdfs:subClassOf ?parent } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?definition ?comment ORDER BY ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	text = text + "- Definition: {}\n".format(r.definition)
	if (r.parents) :
		text = text + "- SubClass Of: {}\n".format(r.parents.replace("https://rs.tdwg.org/bdqffdq/terms/",""))
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

text = text + "### 4.2 ObjectProperty terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?range ?restrictedRange ?restriction  (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:ObjectProperty . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . OPTIONAL { ?subject rdfs:subPropertyOf ?parent } . OPTIONAL { ?subject rdfs:range ?range . optional { ?range a owl:Restriction . ?range owl:onProperty ?restrictedRange . ?range  ?restriction ?x . FILTER ( ?restriction != owl:onProperty && ?restriction != rdf:type  ) }  } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?definition ?comment ORDER BY ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	text = text + "- Definition: {}\n".format(r.definition)
	if (r.parents) :
		text = text + "- SubClass Of: {}\n".format(r.parents.replace("https://rs.tdwg.org/bdqffdq/terms/",""))
	if (r.range) :
		if (r.restriction) :
			text = text + "- Range [ {} {} ]\n".format(r.restriction.replace("http://www.w3.org/2002/07/owl#","owl:"), r.restrictedRange.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
		else :
			text = text + "- Range {}\n".format(r.range.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"


text = text + "### 4.3 DataProperty terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?range WHERE { ?subject a owl:DatatypeProperty . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . ?subject rdfs:comment ?comment . OPTIONAL { ?subject rdfs:range ?range }  }  ORDER BY ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:")
	term = entity.replace("bdqffdq:","")
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	text = text + "- Definition: {}\n".format(r.definition)
	if (r.range) :
		text = text + "- Range {}\n".format(r.range.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:").replace("http://www.w3.org/2001/XMLSchema#","xsd:"))
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

text = text + "### 4.4 NamedIndividual terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?type ?differentFrom WHERE {  ?subject a owl:NamedIndividual . ?subject a ?type . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . ?subject rdfs:comment ?comment . FILTER ( ?type != owl:NamedIndividual) . OPTIONAL { ?subject owl:differentFrom ?differentFrom }  }  ORDER BY ?type ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	rtype = r.type.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	text = text + "- Type: {}\n".format(rtype)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	if (r.differentFrom) :
		different = r.differentFrom.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
		text = text + "- DifferentFrom: {}\n".format(different)
	text = text + "- Definition: {}\n".format(r.definition)
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"


# Load footer 
footerObject = open(footerFileName, 'rt', encoding='utf-8')
footer = footerObject.read()
footerObject.close()
footer = footer.replace('{license_statement}', document_configuration_yaml['license_statement'])
footer = footer.replace('{publisher}', document_configuration_yaml['publisher'])
footer = footer.replace('{license_uri}', document_configuration_yaml['license_uri'])
footer = footer.replace('{publisher}', document_configuration_yaml['publisher'])
footer = footer.replace('{creator}', document_configuration_yaml['creator'])
footer = footer.replace('{year}', year)
footer = footer.replace('{document_title}', document_configuration_yaml['documentTitle'])
footer = footer.replace('{current_iri}', document_configuration_yaml['current_iri'])
footer = footer.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
   
## Produce a table of contents from the headings 
toc = ""
regexHeadings = "^#+ [0-9]+.*"
with open(headerFileName) as headerFile:
	for line in headerFile:
		aHeading = re.search(regexHeadings,line)
		if (aHeading) : 
			headingText = aHeading.group().replace("#","")
			headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
			toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
	headerFile.close()
for line in iter(text.splitlines()) : 
	aHeading = re.search(regexHeadings,line)
	if (aHeading) : 
		headingText = aHeading.group().replace("#","")
		headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
		toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
with open(footerFileName) as footerFile:
	for line in footerFile:
		aHeading = re.search(regexHeadings,line)
		if (aHeading) : 
			headingText = aHeading.group().replace("#","")
			headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
			toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
	footerFile.close()
header = header.replace('{toc}', toc)

warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"
    
print("writing to {}".format(outputFilename))
output = warning + header + text + footer
outputObject = open(outputFilename, 'wt', encoding='utf-8')
outputObject.write(output)
outputObject.close()

output = ""
warning = ""
header = ""
text = ""
footer = ""

#############################################################
# Document 2: Term-index document

# Configuration: Files 
outputDirectory = "../docs/list/bdqffdq/"
sourceDirectory = 'templates/list/bdqffdq/'
outputFilename = "{}index.md".format(outputDirectory)
headerFileName = '{}bdqffdq_termlist-header.md'.format(sourceDirectory)
footerFileName = '{}bdqffdq_termlist-footer.md'.format(sourceDirectory)
document_configuration_yaml_file = '{}/document_configuration.yaml'.format(sourceDirectory)

term_concept_dictionary = {
    "iri": {"label":"Term Version IRI","term":"rdf:about","normative":"true"}, 
    "term_iri": {"label":"Term IRI","term":"dcterms:isVersionOf","normative":"true"}, 
    "term_localName": {"label":"Term Name","term":"rdf:value","normative":"true"}, 
    "prefLabel": {"label":"Preferred Label","term":"skos:prefLabel","normative":"false"}, 
    "label": {"label":"Label","term":"rdfs:label","normative":"true"}, 
    "comments": {"label":"Comments","term":"rdfs:comment","normative":"false"}, 
    "definition": {"label":"Definition","term":"skos:definition","normative":"true"}, 
    "rdf_type": {"label":"Type","term":"rdf:type","normative":"true"}, 
    "superclass": {"label":"Superclass","term":"rdfs:subClassOf","normative":"true"}, 
    "organized_in": {"label":"","term":"","normative":""}, 
    "issued": {"label":"Modified","term":"dcterms:issued","normative":""}, 
    "status": {"label":"Status","term":"tdwgutility:status","normative":""}, 
    "flags": {"label":"","term":"","normative":""}, 
    "controlled_value_string": {"label":"Controlled Value","term":"","normative":"true"}
}

# Build Term-List Document

# Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
# load from local file
with open(document_configuration_yaml_file) as dcfy:
	document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

# Build definition table
graph = rdflib.Graph()
graph.parse(inputTermsOwlFilename, format="ttl")
#column_list = ['iri', 'term_localName', 'prefLabel', 'label', 'comments', 'definition', 'rdf_type', 'organized_in','issued','status','term_iri','flags']
column_list = ['term_iri', 'iri', 'term_localName', 'prefLabel', 'label', 'comments', 'definition', 'rdf_type', 'superclass']
sparql = prefixes + "SELECT DISTINCT (str(?subject) as ?term_iri) (str(?subject) as ?iri) (?subject as ?term_localName)  ?prefLabel ?label ?comment ?definition ?rdf_type (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:Class . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . ?subject rdf:type ?rdf_type . ?subject rdfs:label ?label . OPTIONAL { ?subject rdfs:subClassOf ?parent } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?label ?comment ?definition ?rdf_type ORDER BY ?subject"
queryResult = graph.query(sparql)

terms_df = pd.DataFrame(queryResult, columns = column_list)
terms_sorted_by_label = terms_df.sort_values(by='label')
terms_sorted_by_localname = terms_df.iloc[terms_df.term_localName.str.lower().argsort()]

definitionTable = build_term_key(term_concept_dictionary,terms_sorted_by_localname)

# Load header 
headerObject = open(headerFileName, 'rt', encoding='utf-8')
header = headerObject.read()
headerObject.close()
# Substitute values of ratification_date and contributors into the header template
header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
# Build the Markdown for the authors and contributors lists, or the authors list, or the contributors list
contributors = build_authors_contributors_markdown(contributors_yaml)
header = header.replace('{authors_contributors}', contributors)
contributors = build_contributors_markdown(contributors_yaml)
header = header.replace('{contributors}', contributors)
contributors = build_authors_markdown(contributors_yaml)
header = header.replace('{authors}', contributors)
header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
header = header.replace('{current_iri}', document_configuration_yaml['current_iri'])
header = header.replace('{abstract}', document_configuration_yaml['abstract'])
header = header.replace('{creator}', document_configuration_yaml['creator'])
header = header.replace('{publisher}', document_configuration_yaml['publisher'])
header = header.replace('{comment}', document_configuration_yaml['comment'])
year = document_configuration_yaml['doc_modified'].split('-')[0]
header = header.replace('{year}', year)
if has_namespace:
    header = header.replace('{namespace_uri}', namespace_uri)
    header = header.replace('{pref_namespace_prefix}', pref_namespace_prefix)
header = header.replace('{term_key}', definitionTable)

# ---------------
# Load rdf, format for Term-List Document
# ---------------
text = ""

graph = rdflib.Graph()
graph.parse(inputTermsOwlFilename, format="ttl")

text = "\n"
text = text + "- [Classes](#41-Class-terms)\n"
text = text + "- [Object Properties](#42-ObjectProperty-terms)\n"
text = text + "- [Data Properties](#43-DataProperty-terms)\n"
text = text + "- [Named Individuals](#44-NamedIndividual-terms)\n"
text = text + "\n"

text = text + "#### 3.1 Alphabetical Index of classes\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:Class . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "#### 3.2 Alphabetical Index of object properties\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:ObjectProperty . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "#### 3.3 Alphabetical Index of data properties\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:DatatypeProperty . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "#### 3.4 Alphabetical Index of named individuals\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:NamedIndividual . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "\n## 4 Vocabulary\n"
# TODO: term-list terms, formatted as table
text = text + "\n**TODO: term-list terms, formatted as table**\n"
text = text + "\n### 4.1 Class terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:Class . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . OPTIONAL { ?subject rdfs:subClassOf ?parent } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?definition ?comment ORDER BY ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	text = text + "- Definition: {}\n".format(r.definition)
	if (r.parents) :
		text = text + "- SubClass Of: {}\n".format(r.parents.replace("https://rs.tdwg.org/bdqffdq/terms/",""))
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

text = text + "### 4.2 ObjectProperty terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?range ?restrictedRange ?restriction  (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:ObjectProperty . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . OPTIONAL { ?subject rdfs:subPropertyOf ?parent } . OPTIONAL { ?subject rdfs:range ?range . optional { ?range a owl:Restriction . ?range owl:onProperty ?restrictedRange . ?range  ?restriction ?x . FILTER ( ?restriction != owl:onProperty && ?restriction != rdf:type  ) }  } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?definition ?comment ORDER BY ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	text = text + "- Definition: {}\n".format(r.definition)
	if (r.parents) :
		text = text + "- SubClass Of: {}\n".format(r.parents.replace("https://rs.tdwg.org/bdqffdq/terms/",""))
	if (r.range) :
		if (r.restriction) :
			text = text + "- Range [ {} {} ]\n".format(r.restriction.replace("http://www.w3.org/2002/07/owl#","owl:"), r.restrictedRange.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
		else :
			text = text + "- Range {}\n".format(r.range.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"


text = text + "### 4.3 DataProperty terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?range WHERE { ?subject a owl:DatatypeProperty . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . ?subject rdfs:comment ?comment . OPTIONAL { ?subject rdfs:range ?range }  }  ORDER BY ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:")
	term = entity.replace("bdqffdq:","")
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	text = text + "- Definition: {}\n".format(r.definition)
	if (r.range) :
		text = text + "- Range {}\n".format(r.range.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:").replace("http://www.w3.org/2001/XMLSchema#","xsd:"))
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

text = text + "### 4.4 NamedIndividual terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?type ?differentFrom WHERE {  ?subject a owl:NamedIndividual . ?subject a ?type . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . ?subject rdfs:comment ?comment . FILTER ( ?type != owl:NamedIndividual) . OPTIONAL { ?subject owl:differentFrom ?differentFrom }  }  ORDER BY ?type ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "### {}\n\n".format(term)
	text = text + "- Name: {}\n".format(entity)
	rtype = r.type.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	text = text + "- Type: {}\n".format(rtype)
	text = text + "- Preferred Label: {}\n".format(r.prefLabel)
	if (r.differentFrom) :
		different = r.differentFrom.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
		text = text + "- DifferentFrom: {}\n".format(different)
	text = text + "- Definition: {}\n".format(r.definition)
	text = text + "- Comments: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

## Produce a table of contents from the headings 
toc = ""
regexHeadings = "^#+ [0-9]+.*"
with open(headerFileName) as headerFile:
	for line in headerFile:
		aHeading = re.search(regexHeadings,line)
		if (aHeading) : 
			headingText = aHeading.group().replace("#","")
			headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
			toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
	headerFile.close()
for line in iter(text.splitlines()) : 
	aHeading = re.search(regexHeadings,line)
	if (aHeading) : 
		headingText = aHeading.group().replace("#","")
		headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
		toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
header = header.replace('{toc}', toc)

# Load footer 
footerObject = open(footerFileName, 'rt', encoding='utf-8')
footer = footerObject.read()
footerObject.close()
footer = footer.replace('{license_statement}', document_configuration_yaml['license_statement'])
footer = footer.replace('{publisher}', document_configuration_yaml['publisher'])
footer = footer.replace('{license_uri}', document_configuration_yaml['license_uri'])
footer = footer.replace('{publisher}', document_configuration_yaml['publisher'])
footer = footer.replace('{creator}', document_configuration_yaml['creator'])
footer = footer.replace('{year}', year)
footer = footer.replace('{document_title}', document_configuration_yaml['documentTitle'])
footer = footer.replace('{current_iri}', document_configuration_yaml['current_iri'])
footer = footer.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
    
warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"
    
print("writing to {}".format(outputFilename))
output = warning + header + text + footer
outputObject = open(outputFilename, 'wt', encoding='utf-8')
outputObject.write(output)
outputObject.close()

output = ""
warning = ""
header = ""
text = ""
footer = ""
#############################################################
# Document 3: Vocabulary Extension document

# Configuration: Files

outputDirectory = "../docs/extension/bdqffdq/"
sourceDirectory = 'templates/extension/bdqffdq/'
outputFilename = "{}index.md".format(outputDirectory)
headerFileName = '{}bdqffdq_extension-header.md'.format(sourceDirectory)
footerFileName = '{}bdqffdq_extension-footer.md'.format(sourceDirectory)
document_configuration_yaml_file = '{}/document_configuration.yaml'.format(sourceDirectory)

# Build Vocabulary Extension document

# Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
# load from local file
with open(document_configuration_yaml_file) as dcfy:
	document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

# Load header 
headerObject = open(headerFileName, 'rt', encoding='utf-8')
header = headerObject.read()
headerObject.close()
# Substitute values of ratification_date and contributors into the header template
header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
# Build the Markdown for the authors and contributors lists, or the authors list, or the contributors list
contributors = build_authors_contributors_markdown(contributors_yaml)
header = header.replace('{authors_contributors}', contributors)
contributors = build_contributors_markdown(contributors_yaml)
header = header.replace('{contributors}', contributors)
contributors = build_authors_markdown(contributors_yaml)
header = header.replace('{authors}', contributors)
header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
header = header.replace('{current_iri}', document_configuration_yaml['current_iri'])
header = header.replace('{abstract}', document_configuration_yaml['abstract'])
header = header.replace('{creator}', document_configuration_yaml['creator'])
header = header.replace('{publisher}', document_configuration_yaml['publisher'])
header = header.replace('{comment}', document_configuration_yaml['comment'])
year = document_configuration_yaml['doc_modified'].split('-')[0]
header = header.replace('{year}', year)
if has_namespace:
    header = header.replace('{namespace_uri}', namespace_uri)
    header = header.replace('{pref_namespace_prefix}', pref_namespace_prefix)
header = header.replace('{term_key}', definitionTable)

## Page content

text = "\n"
text = text + "- [Range Axioms](#41-Range Axioms]\n"
text = text + "- [Different From Axioms](#41-Different From Axipms]\n"
text = text + "\n## 4 Vocabulary Extension\n"
text = text + "\n### 4.1 Range Axioms\n"
sparql = prefixes + "SELECT ?subject ?type ?range ?restriction ?restrictedRange WHERE { ?subject rdf:type ?type . ?subject rdfs:range ?range. optional { ?range a owl:Restriction . ?range owl:onProperty ?restrictedRange . ?range  ?restriction ?x . FILTER ( ?restriction != owl:onProperty && ?restriction != rdf:type  ) } } ORDER BY ?type ?subject "
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "#### {}\n\n".format(term)
	text = text + "| Property | Value |\n"
	text = text + "| -------- | ----- |\n"
	text = text + "| Name | {} |\n".format(entity)
	text = text + "| Type | {} |\n".format(r.type.replace("http://www.w3.org/2002/07/owl#","owl:"))
	if (r.range) :
		if (r.restriction) :
			text = text + "| Range | [ {} {} ] |\n".format(r.restriction.replace("http://www.w3.org/2002/07/owl#","owl:"), r.restrictedRange.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
		else :
			text = text + "| Range | {} |\n".format(r.range.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:").replace("http://www.w3.org/2001/XMLSchema#","xsd:"))
	text = text + "\n\n"

text = text + "### 4.2 Different From Axioms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?type ?differentFrom WHERE {  ?subject a owl:NamedIndividual . ?subject a ?type . FILTER ( ?type != owl:NamedIndividual) .  ?subject owl:differentFrom ?differentFrom  }  ORDER BY ?type ?subject"
queryResult = graph.query(sparql)
for r in queryResult : 
	entity = r.subject
	entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
	term = entity.replace("bdqffdq:","");
	text = text + "#### {}\n\n".format(term)
	text = text + "| Property | Value |\n"
	text = text + "| -------- | ----- |\n"
	text = text + "| Name | {} |\n".format(entity)
	text = text + "| Type | {} |\n".format(r.type.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
	text = text + "| Different From | {} |\n".format(r.differentFrom.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
	text = text + "\n\n"

## Produce a table of contents from the headings 
toc = ""
regexHeadings = "^#+ [0-9]+.*"
with open(headerFileName) as headerFile:
	for line in headerFile:
		aHeading = re.search(regexHeadings,line)
		if (aHeading) : 
			headingText = aHeading.group().replace("#","")
			headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
			toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
	headerFile.close()
for line in iter(text.splitlines()) : 
	aHeading = re.search(regexHeadings,line)
	if (aHeading) : 
		headingText = aHeading.group().replace("#","")
		headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
		toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
header = header.replace('{toc}', toc)

# Load footer 
footerObject = open(footerFileName, 'rt', encoding='utf-8')
footer = footerObject.read()
footerObject.close()
footer = footer.replace('{license_statement}', document_configuration_yaml['license_statement'])
footer = footer.replace('{publisher}', document_configuration_yaml['publisher'])
footer = footer.replace('{license_uri}', document_configuration_yaml['license_uri'])
footer = footer.replace('{publisher}', document_configuration_yaml['publisher'])
footer = footer.replace('{creator}', document_configuration_yaml['creator'])
footer = footer.replace('{year}', year)
footer = footer.replace('{document_title}', document_configuration_yaml['documentTitle'])
footer = footer.replace('{current_iri}', document_configuration_yaml['current_iri'])
footer = footer.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
    
warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"
    
print("writing to {}".format(outputFilename))
output = warning + header + text + footer
outputObject = open(outputFilename, 'wt', encoding='utf-8')
outputObject.write(output)
outputObject.close()

################
print("Done")


    

