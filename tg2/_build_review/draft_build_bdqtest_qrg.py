# Produce markdown document listing tests from 
# intermediate csv list of tests TG2_tests.csv 
# and TG2_multirecord_measure_tests.csv
#
# @author Paul J. Morris 
# @contributor John Wieczorek
#
# Run from tg2/_build_review directory.
#
# TODO; Include header/footer templates.
#
# Quick reference shows only: 
# prefLabel
# Label	
# Resource Type
# GUID	-> now term_localName
# DateLastUpdated	
# Description
# InformationElement:ActedUpon
# InformationElement:Consulted	
# ExpectedResponse -> as Specification
# Parameters
# Examples	
# UseCases
# Notes
#
import pandas	# provides data frames
import re		# regular expression library
import sys		# input/output
import yaml		# Library to parse yaml files
import rdflib	# Library to parse RDF files
import pandas as pd  # library to handle data loaded from csv as data frames
# To copy files from build/templates/ to /docs/
import glob
import shutil
import function_lib # library of reusable functions for TDWG build scripts
from function_lib import build_term_key, build_authors_contributors_markdown, build_contributors_markdown, build_authors_markdown, markdown_heading_to_link

# Configuration 

# Vocabulary file
inputTermsCsvFilename = "../_review/vocabulary/bdqtest_term_versions.csv"
inputTermsOwlFilename = "../_review/vocabulary/bdqffdq.owl"
# output file 
outputDirectory = "../_review/docs/terms/bdqtest/"
outputFilename = "{}index.md".format(outputDirectory)
outputUseCaseIndexFilename = "../_review/docs/terms/bdqtest/qrg_index_by_usecase.md"
outputInformationElementIndexFilename = "../_review/docs/terms/bdqtest/qrg_index_by_ie_actedupon.md"
outputIEClassIndexFilename = "../_review/docs/terms/bdqtest/qrg_index_by_ie_class.md"
outputDimensionIndexFilename = "../_review/docs/terms/bdqtest/qrg_index_by_dimension.md"
outputMultiRecordMeasureIndexFilename = "../_review/docs/terms/bdqtest/qrg_multirecord_index.md"
outputKeyFilename = '{}bdqtest_qrg_term_descriptions.md'.format(outputDirectory)
# Files for header/footer
contributors_yaml_file = 'authors_configuration.yaml'
term_list_document = "temp_term-lists.csv"
local_metadata_config_file = 'temp_namespaces.yaml'
sourceDirectory = 'templates/terms/bdqtest_qrg/'
headerFileName = '{}bdqtest_quickreference-header.md'.format(sourceDirectory)
footerFileName = '{}bdqtest_quickreference-footer.md'.format(sourceDirectory)
document_configuration_yaml_file = '{}document_configuration.yaml'.format(sourceDirectory)
keyHeaderFileName = '{}bdqtest_qrg_term_descriptions-header.md'.format(sourceDirectory)
# footerFileName is reused for keyFile
# This is the configuration file to build a key to the terms used to describe the vocabulary terms.
vocabulary_configuration_yaml_file = "{}../../list/bdqtest/vocabulary_configuration.yaml".format(sourceDirectory)

# TODO: Post ratification of the standard, this will have to be changed to the location for the docs-versions.csv file
# expected to be: githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + github_branch + '/'
github_branch = 'master'
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/bdq/' + github_branch + '/tg2/core/generation/'

has_namespace = True
namespace_uri = 'https://rs.tdwg.org/bdqtest'
pref_namespace_prefix = "bdqtest"

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

# Setup for header/footer templates

# Load the contributors YAML file from its local location.
with open(contributors_yaml_file) as cyf:
	contributors_yaml = yaml.load(cyf, Loader=yaml.FullLoader)

## Build key of vocabulary used in the Quick Reference Guide
terms_in_qrg = [ 'skos:prefLabel', 'rdfs:label', 'rdf:about', 'rdfs:comment','bdqffdq:hasAuthoritiesDefaults','bdqffdq:hasExpectedResponse','skos:example','bdqffdq:composedOf','skos:note','bdqffdq:Parameter','bdqffdq:Specification','rdf:type','bdqffdq:hasUseCase' ]
# Load the vocabulary configuration YAML file from its local location and filter to just the terms used in the Quick Reference Guide
with open(vocabulary_configuration_yaml_file) as vcfy:
	term_concept_dictionary = yaml.load(vcfy, Loader=yaml.FullLoader)
	term_concept_dictionary = {key: value for key, value in term_concept_dictionary.items() if value.get('term') in terms_in_qrg}

# build definition table (key) for terms used in the Quick Reference Guide
#
# Code copied from the build bdqtest terms-list script, modified to construct the key for the terms used in the Quick Reference Guide.
termLists = ['bdqtest']
term = 'bdqtest'
term_history_csv = "../_review/vocabulary/bdqtest_term_versions.csv".format(term)
term_lists_info = []
# column_list tuned to just columns in the Quick Reference Guide.
column_list = ["Label","iri","term_iri","term_localName","prefLabel","InformationElement:ActedUpon","InformationElement:Consulted","Parameters","ExpectedResponse","AuthoritiesDefaults","Description","Type","Resource Type","Examples","Notes","UseCases","status"]
# Likely will be provided from rs.tdwg.org after ratification, currently obtain from local file
#frame = pd.read_csv(githubBaseUri + term_list_document, na_filter=False)
frame = pd.read_csv(term_list_document, na_filter=False)
for termList in termLists:
    term_list_dict = {'list_iri': termList}
    term_list_dict = {'database': termList}
    for index,row in frame.iterrows():
        if row['database'] == termList:
            term_list_dict['pref_ns_prefix'] = row['vann_preferredNamespacePrefix']
            term_list_dict['pref_ns_uri'] = row['vann_preferredNamespaceUri']
            term_list_dict['list_iri'] = row['list']
    term_lists_info.append(term_list_dict)
# Create list of lists metadata table
table_list = []
for term_list in term_lists_info:
    if (term_list['pref_ns_prefix']==term) : 
        # retrieve versions metadata for term list
        # PJM: This is unavailable for a draft standard.
        versions_url = githubBaseUri + term_list['database'] + '-versions/' + term_list['database'] + '-versions.csv'
        #versions_df = pd.read_csv(versions_url, na_filter=False)
        
        # retrieve current term metadata for term list
        # data_url = githubBaseUri + term_list['database'] + '/' + term_list['database'] + '.csv'
        # PJM: Using local file
        data_url = term_history_csv # "../../../../vocabularies/bdqdim_terms.csv"
        frame = pd.read_csv(data_url, na_filter=False)
        for index,row in frame.iterrows():
            # PJM: TODO: just use column list?
            # row_list tuned to just columns in the Quick Reference Guide.
            row_list = [ row['Label'], row['iri'], row['term_iri'], row['term_localName'], row['prefLabel'], row['InformationElement:ActedUpon'], row['InformationElement:Consulted'], row['Parameters'], row['ExpectedResponse'], row['AuthoritiesDefaults'], row['Description'], row['Type'], row['Resource Type'], row['Examples'], row['Notes'], row['UseCases'], row["status"] ]
    
            table_list.append(row_list)
    
# Turn list of lists into dataframe
terms_df = pd.DataFrame(table_list, columns = column_list)
# Limit output to just current terms 
terms_df = terms_df.loc[terms_df['status']=='recommended']
terms_sorted_by_label = terms_df.sort_values(by='Label')
# This makes sort case insensitive
terms_sorted_by_localname = terms_df.iloc[terms_df.prefLabel.str.lower().argsort()]

definitionTable = build_term_key(term_concept_dictionary,terms_sorted_by_localname)

# Load the vocabulary and produce the Quick Reference Guide

with open ("../_review/vocabulary/bdq_term_versions.csv") as vocabfile: 
	try: 
		vocabDataFrame = pandas.read_csv(vocabfile);
	except pandas.errors.ParserError as e:
		sys.exit("Error reading bdq vocabulary csv file: {}".format(e)) 

with open (inputTermsCsvFilename, newline='') as csvfile:
	sys.stdout = open(outputFilename,"w")
	outputUseCaseIndex = open(outputUseCaseIndexFilename,"w")
	outputInformationElementIndex = open(outputInformationElementIndexFilename,"w")
	outputIEClassIndex = open(outputIEClassIndexFilename,"w")
	outputDimensionIndex = open(outputDimensionIndexFilename,"w")
	outputMultiRecordMeasureIndex = open(outputMultiRecordMeasureIndexFilename,"w")
	rawDataFrame = pandas.read_csv(csvfile)
	dataFrame = rawDataFrame.sort_values(by=['Type','IE Class', 'Label'],ascending=[False,True,True])
	# Filter out multirecord mesures into one data frame
	multirecordDataFrame = dataFrame[dataFrame['Label'].str.startswith('MULTIRECORD_MEASURE',na=False)]
	multirecordheader_names = list(multirecordDataFrame.columns)
	# Exclude multirecord measures from dataFrame, limit to singe record tests
	dataFrame = dataFrame[~dataFrame['Label'].str.startswith('MULTIRECORD_MEASURE',na=False)]
	header_names = list(dataFrame.columns)
	try: 
		# Load header, replace fields

		# Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
		# load from local file
		with open(document_configuration_yaml_file) as dcfy:
			document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

	
		# read in header and footer, merge with terms table, and output
		headerObject = open(headerFileName, 'rt', encoding='utf-8')
		header = headerObject.read()
		headerObject.close()

		## Produce a table of contents from the headings in the header
		toc = ""
		regexHeadings = "^#+ [0-9]+.*"
		for line in (header).splitlines() :
			aHeading = re.search(regexHeadings,line)
			if (aHeading) : 
				toc = toc + "- " + markdown_heading_to_link(aHeading.group()) + "\n"
	
		# Substitute values of ratification_date and contributors into the header template
		header = header.replace("<!--- Template for header, values provided from yaml configuration --->","")
		header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
		header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
		header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
		# Build the Markdown for the authors and contributors lists or the contributors list
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
		header = header.replace('{maintainer}', document_configuration_yaml['maintainer'])
		header = header.replace('{doc_modified}', document_configuration_yaml['doc_modified'])
		header = header.replace('{toc}','\n{}'.format(toc))
		year = document_configuration_yaml['doc_modified'].split('-')[0]
		header = header.replace('{year}', year)
		if has_namespace:
			header = header.replace('{namespace_uri}', namespace_uri)
			header = header.replace('{pref_namespace_prefix}', pref_namespace_prefix)
	
		warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"

		# Provide a list of definitions of terms in the Quick Reference Guide in a separate document.
		keyHeaderObject = open(keyHeaderFileName, 'rt', encoding='utf-8')
		keyHeader = keyHeaderObject.read()
		keyHeaderObject.close()
		keyHeader = keyHeader.replace('{term_key}', definitionTable)
		# file is written below.  If not needed, place {term_key} tag into header file for qrg and 
		# remove references to outputKeyFile below (after construction of footer.

		# write the header to the output file
		print(warning)
		print(header)

		# Index by UseCase
		usecaseDict = dict()
		for index, row in dataFrame.iterrows():
			usecasesTerm = str(row["UseCases"])
			test = row['Label']
			term_localName = row['term_localName']
			foundUseCases = [val.strip() for val in usecasesTerm.split(',')]
			for useCase in foundUseCases: 
				usecaseDict.setdefault(useCase,{})[test] = term_localName
				
		outputUseCaseIndex.write("# BDQ Test Index by Use Case (non-normative)\n")
		outputUseCaseIndex.write("This document is non-normative and part of the [BDQ Tests Quick Reference Guide](index.md).\n")

		for useCase in usecaseDict.keys(): 
			outputUseCaseIndex.write("## "+useCase)
			outputUseCaseIndex.write("\n")
			definitionRow = vocabDataFrame.loc["bdq:"+vocabDataFrame["term_localName"]==useCase]
			try: 
				definitionCell = definitionRow.iloc[0]["definition"]
				outputUseCaseIndex.write(definitionCell)
				outputUseCaseIndex.write("\n")
			except: 
				outputUseCaseIndex.write("error extracting definition\n")
			outputUseCaseIndex.write("\n")
			for test in usecaseDict[useCase]:
				outputUseCaseIndex.write(f'{test}\n')
				outputUseCaseIndex.write(f'- Term IRI: https://rs.tdwg.org/bdqtest/terms/{usecaseDict[useCase][test]}\n')
				outputUseCaseIndex.write(f'- [Quick Reference Guide](index.md#{test})\n')
				outputUseCaseIndex.write(f'- [Term List](../../list/bdqtest/index.md#bdqtest_{usecaseDict[useCase][test]})\n\n')
			outputUseCaseIndex.write("\n\n")

		# Index by information element
		informationelementDict = dict()
		for index, row in dataFrame.iterrows():
			informationelementsTerm = str(row['InformationElement:ActedUpon'])
			test = row['Label']
			term_localName = row['term_localName']
			foundInformationElements = [val.strip() for val in informationelementsTerm.split(',')]
			for ie in foundInformationElements: 
				informationelementDict.setdefault(ie,{})[test] = term_localName
		outputInformationElementIndex.write("# BDQ Test Index by Information Element Acted Upon (non-normative)\n")
		outputInformationElementIndex.write("This document is non-normative and part of the [BDQ Tests Quick Reference Guide](index.md).\n")
		for ie in informationelementDict.keys(): 
			outputInformationElementIndex.write("## "+ie)
			outputInformationElementIndex.write("\n\n")
			for test in informationelementDict[ie]:
				outputInformationElementIndex.write(f'{test}\n')
				outputInformationElementIndex.write(f'- Term IRI: https://rs.tdwg.org/bdqtest/terms/{informationelementDict[ie][test]}\n')
				outputInformationElementIndex.write(f'- [Quick Reference Guide](index.md#{test})\n')
				outputInformationElementIndex.write(f'- [Term List](../../list/bdqtest/index.md#bdqtest_{informationelementDict[ie][test]})\n\n')
			outputInformationElementIndex.write("\n")

		# Index by information element class
		informationelementDict = dict()
		for index, row in dataFrame.iterrows():
			informationelementsTerm = str(row['IE Class'])
			test = row['Label']
			term_localName = row['term_localName']
			foundInformationElements = [val.strip() for val in informationelementsTerm.split(',')]
			for ie in foundInformationElements: 
				informationelementDict.setdefault(ie,{})[test] = term_localName
		outputIEClassIndex.write("# BDQ Test Index by Information Element Class (non-normative)\n")
		outputIEClassIndex.write("This document is non-normative and part of the [BDQ Tests Quick Reference Guide](index.md).\n")
		for ie in informationelementDict.keys(): 
			outputIEClassIndex.write("## "+ie)
			outputIEClassIndex.write("\n\n")
			for test in informationelementDict[ie]:
				outputIEClassIndex.write(f'{test}\n')
				outputIEClassIndex.write(f'- Term IRI: https://rs.tdwg.org/bdqtest/terms/{informationelementDict[ie][test]}\n')
				outputIEClassIndex.write(f'- [Quick Reference Guide](index.md#{test})\n')
				outputIEClassIndex.write(f'- [Term List](../../list/bdqtest/index.md#bdqtest_{informationelementDict[ie][test]})\n\n')
			outputIEClassIndex.write("\n")

		# Index by dimension
		# TODO: Add definitions of dimensions from bdqdim vocabulary
		dimensionDict = dict()
		for index, row in dataFrame.iterrows():
			dimensionsTerm = str(row['Dimension'])
			test = row['Label']
			term_localName = row['term_localName']
			foundDimensions = [val.strip() for val in dimensionsTerm.split(',')]
			for dim in foundDimensions: 
				dimensionDict.setdefault(dim,{})[test] = term_localName
		outputDimensionIndex.write("# BDQ Test Index by Data Quality Dimension (non-normative)\n")
		outputDimensionIndex.write("This document is non-normative and part of the [BDQ Tests Quick Reference Guide](index.md).\n")
		for dim in dimensionDict.keys(): 
			outputDimensionIndex.write("## "+dim)
			outputDimensionIndex.write("\n\n")
			for test in dimensionDict[dim]:
				outputDimensionIndex.write(f'{test}\n')
				outputDimensionIndex.write(f'- Term IRI: https://rs.tdwg.org/bdqtest/terms/{dimensionDict[dim][test]}\n')
				outputDimensionIndex.write(f'- [Quick Reference Guide](index.md#{test})\n')
				outputDimensionIndex.write(f'- [Term List](../../list/bdqtest/index.md#bdqtest_{dimensionDict[dim][test]})\n\n')
			outputDimensionIndex.write("\n")

		# Index for multirecord measures
		outputMultiRecordMeasureIndex.write("# BDQ Multi Record Measure Test Index (non-normative)\n\n")
		outputMultiRecordMeasureIndex.write("This document is non-normative and part of the [BDQ Tests Quick Reference Guide](index.md).\n")
		for index, row in multirecordDataFrame.sort_values('Label').iterrows():
			outputMultiRecordMeasureIndex.write(f'{row["Label"]}\n')
			outputMultiRecordMeasureIndex.write(f'- Term IRI: https://rs.tdwg.org/bdqtest/terms/{row["term_localName"]}\n')
			outputMultiRecordMeasureIndex.write(f'- [Quick Reference Guide](index.md#{row["Label"]})\n')
			outputMultiRecordMeasureIndex.write(f'- [Term List](../../list/bdqtest/index.md#bdqtest_{row["term_localName"]})\n\n')

		#
		# Base alphabetical index.
		for index, row in dataFrame.sort_values('Label').iterrows():
			print("- [{}](#{})".format(row['Label'],row['Label']))
		print()
		print("********************")
		print()
		print("# The BDQ Tests")
		print()
		print("## Validations, Measures, Amendments operating on Single Records.")
		print()
		for index, row in dataFrame.iterrows():
			print("### ",row['Label'])
			print()
			print("#### ",row['prefLabel'])
			print("https://rs.tdwg.org/bdqtest/terms/{}/{}".format(row['term_localName'],row['DateLastUpdated']))
			print("Acts upon ",row['Resource Type'])
			print()
			print("#### Description")
			print()
			print(row['Description'])
			print()
			print("#### Expected Response")
			print()
			print(row['ExpectedResponse'])
			print()
			print("#### Information Elements")
			if not pandas.isna(row['InformationElement:ActedUpon']) : 
				print()
				print("Acted upon: ")
				print(row['InformationElement:ActedUpon'])
				print()
			if not pandas.isna(row['InformationElement:Consulted']) : 
				print("Consulted: ")
				print(row['InformationElement:Consulted'])
				print()
			if not pandas.isna(row['Parameters']) : 
				print("#### Parameters")
				print()
				print(row['Parameters'])
				print()
			if not pandas.isna(row['AuthoritiesDefaults']) : 
				if not pandas.isna(row['Parameters']) : 
					print("#### Default Parameter Values")
				else: 
					print("#### Source Authority")
				print()
				print(row['AuthoritiesDefaults'])
				print()
			print("#### Examples")
			print()
			examplesRaw = row['Examples']
			# examples are paired in the form [key:value response:value],[key:value response:value]
			# display as two lines without the enclosing square brackets.
			examples = [val.strip() for val in examplesRaw.split('],[')]
			for example in examples: 
				print(re.sub("\]$","",re.sub("^\[","",example)))
				print()
			print()
			print("#### Use Cases")
			print()
			print(row['UseCases'])
			print()
			if not pandas.isna(row['Notes']) : 
				print("#### Notes")
				print()
				print(row['Notes'])
				print()
			print("[🠱](#indexes-to-the-tests-non-normative)")
			print("********************")
			print()
		print()
		print("## Measures operating on Test Responses for Multi Records (datasets)")
		print()
		for index, row in multirecordDataFrame.iterrows():
			print("### ",row['Label'])
			print()
			print("#### ",row['prefLabel'])
			print("https://rs.tdwg.org/bdqtest/terms/{}/{}".format(row['term_localName'],row['DateLastUpdated']))
			print("Acts upon ",row['Resource Type'])
			print()
			print("#### Description")
			print()
			print(row['Description'])
			print()
			print("#### Specification")
			print()
			print(row['ExpectedResponse'])
			print()
			print("#### Information Elements")
			if not pandas.isna(row['InformationElement:ActedUpon']) : 
				print()
				print("Acted upon: ")
				print(row['InformationElement:ActedUpon'])
				print()
			if not pandas.isna(row['InformationElement:Consulted']) : 
				print("Consulted: ")
				print(row['InformationElement:Consulted'])
				print()
			if not pandas.isna(row['Parameters']) : 
				print("#### Parameters")
				print()
				print(row['Parameters'])
				print()
			print("#### Use Cases")
			print()
			print(row['UseCases'])
			print()
			print("#### Notes")
			print()
			print(row['Notes'])
			print()
			print("[↑](#indexes-to-the-tests-non-normative)")
			print("********************")
			print()
		print()

		# Footer
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
		print(footer)

		# Write out the key to the terms used in the Quick Reference Guide in a separate file.	
		outputKeyFile = open(outputKeyFilename,"w")
		outputKeyFile.write(warning)
		outputKeyFile.write(keyHeader)
		outputKeyFile.write("\n")
		outputKeyFile.write(footer)
		outputKeyFile.close()

	except pandas.errors.ParserError as e:
		sys.exit("Error reading core test csv file: {}".format(e)) 
