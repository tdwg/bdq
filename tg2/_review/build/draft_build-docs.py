# Script to build Markdown pages that are largely human readable text, filling in values from configuration files
#
# Modified from script by
# Steve Baskauf 2020-08-12 CC0
# updated 2021-02-11
# Modified Paul J. Morris for generating draft standard documents without rs.tdwg.org files
# 2024-09-12
# This script merges static Markdown header and footer documents with generated term information tables loading data from in local csv and yaml files.
# Unlike the original, this version is intended to run entirely on local files.

import re		# regular expressions
import csv		# library to read/write/parse CSV files
import json		# library to convert JSON to Python data structures
import pandas as pd  # library to handle data loaded from csv as data frames
import yaml		# Library to parse yaml files
# To copy image files from build/templates/ to /docs/
import glob
import shutil
# run sparql queries on rdf 
import rdflib     
from rdflib import Graph 
import function_lib # library of reusable functions for TDWG build scripts
from function_lib import build_authors_contributors_markdown, build_contributors_markdown, build_authors_markdown, markdown_heading_to_link


# -----------------
# Configuration section
# -----------------

# set debug = True for additional debugging output
debug = False

# This is a Python dictionary of the folders and files to be processed for templates to turn into documents.
# See assumptions below.
# directories, list of key:value pairs of templatePath:document
directories = {'vocabularies':'vocabularies', 'intro':'intro', 'supplement':'supplement', 'synthetic':'synthetic','guide/users':'users','guide/implementers':'implementers','guide/bdqffdq':'bdqffdq', 'bdqcore':'bdqcore_landing','references':'references'}

# This is the base URL for raw files from the branch of the repo that has been pushed to GitHub
github_branch = 'master' # "master" for production, something else for development
# TODO: Post ratification of the standard, this will have to be changed to the location for the docs-versions.csv file
# expected to be: githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + github_branch + '/'
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/bdq/' + github_branch + '/tg2/core/generation/'

# Configuration for loading owl for bdqffdq into guide/bdqffdq/
prefixes = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdqdim: <https://rs.tdwg.org/bdqdim/terms/>
"""
inputTermsOwlFilename = "../vocabulary/bdqffdq.owl"
bdqffdqOwlDocument = 'https://raw.githubusercontent.com/tdwg/bdq/refs/heads/master/tg2/_review/{}'.format(inputTermsOwlFilename)

referencesFileName = "references.md"

# ----------------
# Assumptions 
# ---------------
# (1) The repository has build/ docs/ dist/ and vocabulary/ directories in the same parent directory.
# (2) This file is located in a build/ directory
# (3) This file produces human readable documents in the docs/ directory within docs/{document} directories.
# (6) A list of authors/contributors is in the build/ directory in: 
contributors_yaml_file = 'authors_configuration.yaml'
# (7) local replacements for metadata namespaces and term-lists.csv files 
# are in the build/ directory in the following files, which provide metadata for each term in the standard 
term_list_document = "temp_term-lists.csv"
local_metadata_config_file = 'temp_namespaces.yaml'
# (8) {term}_termlist-header.md, {term}_termlist-footer.md files are in build/templates/{directory}/ along with a document_configuration.yaml file
# see loop below through termLists
# headerFileName = 'templates/{}/{}_termlist-header.md'.format(directory,document)
# footerFileName = 'templates/{}/{}_termlist-footer.md'.format(directory,document)
# document_configuration_yaml_file = 'templates/{}/document_configuration.yaml'.format(directory)

has_namespace = False

# ---------------
# Load header data
# ---------------

# Load the contributors YAML file from its local location.
with open(contributors_yaml_file) as cyf:
	contributors_yaml = yaml.load(cyf, Loader=yaml.FullLoader)

# ---------------
# Retrieve term list metadata from GitHub
# ---------------

## PJM: Unavailable for draft without rs.tdwg.org files
print('Loading term list metadata')
term_lists_info = []


#print(term_list_document)
##frame = pd.read_csv(githubBaseUri + term_list_document, na_filter=False)
#frame = pd.read_csv(term_list_document, na_filter=False)
#for termList in termLists:
#	term_list_dict = {'list_iri': termList}
#	term_list_dict = {'database': termList}
#	for index,row in frame.iterrows():
#		if row['database'] == termList:
#			term_list_dict['pref_ns_prefix'] = row['vann_preferredNamespacePrefix']
#			term_list_dict['pref_ns_uri'] = row['vann_preferredNamespaceUri']
#			term_list_dict['list_iri'] = row['list']
#	term_lists_info.append(term_list_dict)
#print(term_lists_info)
#print()

# Load References for inclusion in templates when requested.
referencesObject = open(referencesFileName, 'rt', encoding='utf-8')
references = referencesObject.read()
referencesObject.close()

#############
## Process each document in directories dictionary
############
for templatePath, document in directories.items() :
	print('Filling in header and footer template and saving file')
	print('Generating files for {}.'.format(document))
	sourceDirectory = 'templates/{}/'.format(templatePath)
	headerFileName = '{}{}-header.md'.format(sourceDirectory,document)
	footerFileName = '{}{}-footer.md'.format(sourceDirectory,document)
	document_configuration_yaml_file = 'templates/{}/document_configuration.yaml'.format(templatePath)
	if document.find("_landing") > -1 :
		outputDirectory = '../docs/{}/'.format(templatePath)
	elif templatePath.find("guide/") == -1 :
		outputDirectory = '../docs/{}/'.format(document)
	else :
		outputDirectory = '../docs/guide/{}/'.format(document)
	outFileName = '{}index.md'.format(outputDirectory)
	print('Generating files as {}.'.format(outFileName))

	# Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
	# load from local file
	with open(document_configuration_yaml_file) as dcfy:
		document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

	# read in header and footer, merge with terms table, and output
	headerObject = open(headerFileName, 'rt', encoding='utf-8')
	header = headerObject.read()
	headerObject.close()
	
	text = ""

	# Substitute values of ratification_date and contributors into the header template
	if debug :
		print(document_configuration_yaml)
	header = header.replace("<!--- Template for header, values provided from yaml configuration --->","")
	header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
	header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
	header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
	# Build the Markdown for the authors and contributors lists or the contributors list or the authors list
	contributors = build_authors_contributors_markdown(contributors_yaml)
	header = header.replace('{authors_contributors}', contributors)
	contributors = build_contributors_markdown(contributors_yaml)
	header = header.replace('{contributors}', contributors)
	contributors = build_authors_markdown(contributors_yaml)
	header = header.replace('{authors}', contributors)
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
		header = header.replace('{pref_namespace_prefix}', term)
	header = header.replace('{references}', references)

	if document == 'bdqcore_landing' : 
		# Special handling of bdqcore landing page, load minimal test list, add to header
		
		# Load data
		data_url = "../vocabulary/bdqcore_term_versions.csv"
		frame = pd.read_csv(data_url, na_filter=False)
		table_list = []
		column_list = ["Label","issueNumber","historyNoteUrl","iri","term_iri","issued","term_localName","DateLastUpdated","prefLabel","IE Class","InformationElement:ActedUpon","InformationElement:Consulted","Parameters","ExpectedResponse","AuthoritiesDefaults","Description","Type","Resource Type","Dimension","Criterion","Enhancement","Examples","Source","References","Example Implementations (Mechanisms)","Link to Specification Source Code","Notes","IssueState","IssueLabels","UseCases","ArgumentGuids","status"]
		for index,row in frame.iterrows():
			row_list = [ row['Label'], row['issueNumber'], row['historyNoteUrl'], row['iri'], row['term_iri'], row['issued'], row['term_localName'], row['DateLastUpdated'], row['prefLabel'], row['IE Class'], row['InformationElement:ActedUpon'], row['InformationElement:Consulted'], row['Parameters'], row['ExpectedResponse'], row['AuthoritiesDefaults'], row['Description'], row['Type'], row['Resource Type'], row['Dimension'], row['Criterion'], row['Enhancement'], row['Examples'], row['Source'], row['References'], row['Example Implementations (Mechanisms)'], row['Link to Specification Source Code'], row['Notes'], row['IssueState'], row['IssueLabels'], row['UseCases'], row["ArgumentGuids"], row['status'] ]
			table_list.append(row_list)
		terms_df = pd.DataFrame(table_list, columns = column_list)
		terms_sorted_by_label = terms_df.sort_values(by='Label')

		# Index
		text = '\n### 4.1 Index By Test Label\n\n'
		text += '\n'
		for row_index,row in terms_sorted_by_label.iterrows():
			if row['Label'].find('MULTIRECORD') == -1 : 
				curie = "bdqcore:" + row['term_localName']
				curie_anchor = curie.replace(':','_')
				text += '[' + row['Label'] + '](#' + curie_anchor + ') |\n'
		text = text[:len(text)-2] # remove final trailing vertical bar and newline
		text += '\n'

		# Vocabulary terms with minimal data
		text += '\n## 5 Vocabulary Summary\n'
		for row_index,row in terms_sorted_by_label.iterrows():
			if row['Label'].find('MULTIRECORD') == -1 :
				curie =  "bdqcore:" + row['term_localName']
				curieAnchor = curie.replace(':','_')
				text += '- <a id="' + curieAnchor + '"></a>' + row['Label'] + '\n'
				text += '  - Description: ' + row['Description'] + '\n'
				text += '  - View in Quick Reference Guide: [Link](../terms/bdqcore/index.md#' + row['Label'] + ')\n'
				text += '  - View in Term-List: [Link](../list/bdqcore/index.md#' + curieAnchor + ')\n'
				text += '\n'

		# Append to end of header
		header = header + '\n' + text
		text = ""

		# End special case handling of bdqcore_landing ********************************

	if document == 'bdqffdq' : 
		# Special handling of bdqffdq, load minimal ontology documentation, add to header
		# ---------------
		# Load rdf
		# ---------------
		
		graph = rdflib.Graph()
		graph.parse(inputTermsOwlFilename, format="ttl")
		
		indextext = "\n"
		indextext = indextext + "- [Classes](#51-Class-terms)\n"
		indextext = indextext + "- [Object Properties](#52-ObjectProperty-terms)\n"
		indextext = indextext + "- [Data Properties](#53-DataProperty-terms)\n"
		indextext = indextext + "- [Named Individuals](#54-NamedIndividual-terms)\n"
		indextext = indextext + "\n"
		
		indextext = indextext + "### 4.1 Alphabetical Index of classes\n\n"
		sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:Class . } "
		queryResult = graph.query(sparql)
		for r in queryResult : 
			term = r.subject
			term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
			indextext = indextext + "[{}](#{})\n".format(term,term)
		
		indextext = indextext + "\n"
		indextext = indextext + "### 4.2 Alphabetical Index of object properties\n\n"
		sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:ObjectProperty . } "
		queryResult = graph.query(sparql)
		for r in queryResult : 
			term = r.subject
			term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
			indextext = indextext + "[{}](#{})\n".format(term,term)
		
		indextext = indextext + "\n"
		indextext = indextext + "### 4.3 Alphabetical Index of data properties\n\n"
		sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:DatatypeProperty . } "
		queryResult = graph.query(sparql)
		for r in queryResult : 
			term = r.subject
			term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
			indextext = indextext + "[{}](#{})\n".format(term,term)
		
		indextext = indextext + "\n"
		indextext = indextext + "### 4.4 Alphabetical Index of named individuals\n\n"
		sparql = prefixes + "SELECT ?subject WHERE {  ?subject a owl:NamedIndividual . } "
		queryResult = graph.query(sparql)
		for r in queryResult : 
			term = r.subject
			term = term.replace("https://rs.tdwg.org/bdqffdq/terms/","")
			indextext = indextext + "[{}](#{})\n".format(term,term)
		
		# put index text into header.
		header = header.replace('{term_index}','\n{}\n'.format(indextext))

		text = ""
		text = text + "### 5.1 Class terms\n"
		sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:Class . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . OPTIONAL { ?subject rdfs:subClassOf ?parent } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?definition ?comment ORDER BY ?subject"
		queryResult = graph.query(sparql)
		for r in queryResult : 
			entity = r.subject
			entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
			term = entity.replace("bdqffdq:","");
			text = text + "### {}\n\n".format(term)
			text = text + "- Name: {}\n".format(entity)
			# text = text + "- Preferred Label: {}\n".format(r.prefLabel)
			text = text + "- Definition: {}\n".format(r.definition)
			if (r.parents) :
				text = text + "- SubClass Of: {}\n".format(r.parents.replace("https://rs.tdwg.org/bdqffdq/terms/",""))
			# text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
			text = text + "\n********************\n\n"
		
		text = text + "### 5.2 ObjectProperty terms\n"
		sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?range ?restrictedRange ?restriction  (GROUP_CONCAT(?parent; SEPARATOR='; ') AS ?parents)  WHERE {  ?subject a owl:ObjectProperty . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . OPTIONAL { ?subject rdfs:subPropertyOf ?parent } . OPTIONAL { ?subject rdfs:range ?range . optional { ?range a owl:Restriction . ?range owl:onProperty ?restrictedRange . ?range  ?restriction ?x . FILTER ( ?restriction != owl:onProperty && ?restriction != rdf:type  ) }  } . ?subject rdfs:comment ?comment } GROUP BY ?subject ?prefLabel ?definition ?comment ORDER BY ?subject"
		queryResult = graph.query(sparql)
		for r in queryResult : 
			entity = r.subject
			entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
			term = entity.replace("bdqffdq:","");
			text = text + "### {}\n\n".format(term)
			text = text + "- Name: {}\n".format(entity)
			# text = text + "- Preferred Label: {}\n".format(r.prefLabel)
			text = text + "- Definition: {}\n".format(r.definition)
			if (r.parents) :
				text = text + "- SubClass Of: {}\n".format(r.parents.replace("https://rs.tdwg.org/bdqffdq/terms/",""))
			if (r.range) :
				if (r.restriction) :
					text = text + "- Range [ {} {} ]\n".format(r.restriction.replace("http://www.w3.org/2002/07/owl#","owl:"), r.restrictedRange.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
				else :
					text = text + "- Range {}\n".format(r.range.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:"))
			# text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
			text = text + "\n********************\n\n"
		
		text = text + "### 5.3 DataProperty terms\n"
		sparql = prefixes + "SELECT DISTINCT ?subject ?prefLabel ?definition ?comment ?range WHERE { ?subject a owl:DatatypeProperty . ?subject skos:definition ?definition . ?subject skos:prefLabel ?prefLabel . ?subject rdfs:comment ?comment . OPTIONAL { ?subject rdfs:range ?range }  }  ORDER BY ?subject"
		queryResult = graph.query(sparql)
		for r in queryResult : 
			entity = r.subject
			entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:")
			term = entity.replace("bdqffdq:","")
			text = text + "### {}\n\n".format(term)
			text = text + "- Name: {}\n".format(entity)
			# text = text + "- Preferred Label: {}\n".format(r.prefLabel)
			text = text + "- Definition: {}\n".format(r.definition)
			if (r.range) :
				text = text + "- Range {}\n".format(r.range.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:").replace("http://www.w3.org/2001/XMLSchema#","xsd:"))
			# text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
			text = text + "\n********************\n\n"
		
		text = text + "### 5.4 NamedIndividual terms\n"
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
			# text = text + "- Preferred Label: {}\n".format(r.prefLabel)
			if (r.differentFrom) :
				different = r.differentFrom.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
				text = text + "- DifferentFrom: {}\n".format(different)
			text = text + "- Definition: {}\n".format(r.definition)
			# text = text + "- Notes: {}\n".format(r.comment.replace("\n\n","\n").replace("\n","  \n"))
			text = text + "\n********************\n\n"

		# put terms into header.
		header = header.replace('{term_list}','\n{}\n'.format(text))
		text = ""

		# End special case handling of bdqffdq ********************************
	
	# Determine whether there was a previous version of the document.
	if document_configuration_yaml['doc_created'] != document_configuration_yaml['doc_modified']:
		# Load versions list from document versions data in the rs.tdwg.org repo and find most recent version.
		# TODO: This file will need to be created post ratification, it contains the columsn current_iri and version_iri
		## example from Darwin Core:
		## current_iri,version_iri
		## http://rs.tdwg.org/abcd/doc/primer/,http://rs.tdwg.org/abcd/doc/primer/2006-07-27
		versions_data_url = githubBaseUri + 'docs/docs-versions.csv'
		versions_list_df = pd.read_csv(versions_data_url, na_filter=False)
		# Slice all rows for versions of this document.
		matching_versions = versions_list_df[versions_list_df['current_iri']==document_configuration_yaml['current_iri']]
		# Sort the matching versions by version IRI in descending order so that the most recent version is first.
		matching_versions = matching_versions.sort_values(by=['version_iri'], ascending=[False])
		# The previous version is the second row in the dataframe (row 1).
		# The version IRI is in the second column (column 1).
		most_recent_version_iri = matching_versions.iat[1, 1]
		#print(most_recent_version_iri)
	
		# Insert the previous version information into the header
		previous_version_metadata_string = '''Previous version
	: <''' + most_recent_version_iri + '''>
	
	'''
		# Insert the previous version information into the designated slot.
		header = header.replace('{previous_version_slot}\n\n', previous_version_metadata_string)
	else:
		# If there was no previous version, remove the slot from the header.
		header = header.replace('{previous_version_slot}\n\n', '')
	


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
	footer = footer.replace('{references}', references)

	## Produce a table of contents from the headings 
	toc = ""
	regexHeadings = "^#+ [0-9]+.*"
	for line in (header+text+footer).splitlines() :
		aHeading = re.search(regexHeadings,line)
		if (aHeading) : 
			toc = toc + "- " + markdown_heading_to_link(aHeading.group()) + "\n"
	header = header.replace('{toc}', toc)
	
	warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"
	
	output = warning + header + text + footer
	outputObject = open(outFileName, 'wt', encoding='utf-8')
	outputObject.write(output)
	outputObject.close()

	# Run 
	# tree templates | grep -v yaml | grep -v "\.md" 
	# to find file types that should be copied over

	# Find image files to copy from templates and copy them over to docs
	for file in glob.glob('{}*.svg'.format(sourceDirectory)):
		print(file)
		shutil.copy(file, outputDirectory)
	for file in glob.glob('{}*.png'.format(sourceDirectory)):
		print(file)
		shutil.copy(file, outputDirectory)
	for file in glob.glob('{}*.jpg'.format(sourceDirectory)):
		print(file)
		shutil.copy(file, outputDirectory)
	# Find csv files (with test validation data) to copy from templates and copy them over to docs
	for file in glob.glob('{}*.csv'.format(sourceDirectory)):
		print(file)
		shutil.copy(file, outputDirectory)

print('done ({})'.format(__file__))

