# Produce markdown document listing bdqffdq Framework terms
# from intermediate csv list of terms bdqffdq_export
# 
# First cut at a human readable display of the ontology
#
# @author Paul J. Morris 
#
# Assumes run from generation/build directory of tg2 repository.
#
import pandas
import re
import sys
import yaml       # Library to parse yaml files
import rdflib     # run sparql queries on rdf 
from rdflib import Graph

# Configuration 

prefixes = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdqdim: <https://rs.tdwg.org/bdqdim/terms/>
"""

# Vocabulary file
inputTermsOwlFilename = "../vocabulary/bdqffdq.owl"
bdqffdqOwlDocument = 'https://raw.githubusercontent.com/tdwg/bdq/refs/heads/master/tg2/_review/{}'.format(inputTermsOwlFilename)
# output file 
outputDirectory = "../docs/terms/bdqffdq/"
outputFilename = "{}index.md".format(outputDirectory)
# Files for header/footer
contributors_yaml_file = 'authors_configuration.yaml'
term_list_document = "temp_term-lists.csv"
local_metadata_config_file = 'temp_namespaces.yaml'
sourceDirectory = 'templates/terms/bdqffdq_qrg/'
headerFileName = '{}bdqffdq_quickreference-header.md'.format(sourceDirectory)
footerFileName = '{}bdqffdq_quickreference-footer.md'.format(sourceDirectory)
document_configuration_yaml_file = '{}/document_configuration.yaml'.format(sourceDirectory)

has_namespace = True
namespace_uri = 'https://rs.tdwg.org/bdqffdq'
pref_namespace_prefix = "bdqffdq"


# Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
# load from local file
with open(document_configuration_yaml_file) as dcfy:
	document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

# Load header 
headerObject = open(headerFileName, 'rt', encoding='utf-8')
header = headerObject.read()
headerObject.close()
header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
header = header.replace('{comment}', document_configuration_yaml['comment'])
year = document_configuration_yaml['doc_modified'].split('-')[0]
    
# ---------------
# Load rdf
# ---------------

graph = rdflib.Graph()
graph.parse(inputTermsOwlFilename, format="ttl")

text = "\n"
text = text + "- [Classes](#Class-terms)\n"
text = text + "- [Object Properties](#ObjectProperty-terms)\n"
text = text + "- [Data Properties](#DataProperty-terms)\n"
text = text + "- [Named Individuals](#NamedIndividual-terms)\n"
text = text + "\n"

text = text + "## Alphabetical Index of classes\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:Class . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "## Alphabetical Index of object properties\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:ObjectProperty . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "## Alphabetical Index of data properties\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:DatatypeProperty . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "## Alphabetical Index of named individuals\n\n"
sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:NamedIndividual . } "
queryResult = graph.query(sparql)
for r in queryResult : 
	term = r.subject
	term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
	text = text + "[{}](#{})\n".format(term,term)

text = text + "\n## Class terms\n"
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
	text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

text = text + "## ObjectProperty terms\n"
sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?range ?restrictedRange ?restriction  (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:ObjectProperty . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . OPTIONAL { ?subject rdfs:subPropertyOf ?parent } . OPTIONAL { ?subject rdfs:range ?range . optional { ?range a owl:Restriction . ?range owl:onProperty ?restrictedRange . ?range  ?restriction ?x . FILTER ( ?restriction = owl:someValuesFrom ) }  } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?definition ?comment ORDER BY ?subject"
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
	text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

text = text + "## DataProperty terms\n"
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
	text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
	text = text + "\n********************\n\n"

text = text + "## NamedIndividual terms\n"
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
	text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
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
    
warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"
    
print("writing to {}".format(outputFilename))
output = warning + header + text + footer
outputObject = open(outputFilename, 'wt', encoding='utf-8')
outputObject.write(output)
outputObject.close()

print("Done")
