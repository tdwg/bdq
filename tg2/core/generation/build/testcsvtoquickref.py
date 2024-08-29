# Produce markdown document listing tests from 
# intermediate csv list of tests TG2_tests.csv 
# and TG2_multirecord_measure_tests.csv
#
# @author Paul J. Morris 
#
# Assumes run from generation/build directory of tg2 repository.
#
# TODO; Include header/footer templates.
#
# Quick reference shows only: 
# prefLabel
# Label	
# Resource Type
# GUID	
# DateLastUpdated	
# Description
# InformationElement:ActedUpon
# InformationElement:Consulted	
# Specification
# Parameters
# Examples	
# UseCases
# Notes
#
import pandas
import re
import sys
with open ("../../../vocabularies/bdq_vocabulary_terms.csv") as vocabfile: 
	try: 
		vocabDataFrame = pandas.read_csv(vocabfile);
	except pandas.errors.ParserError as e:
		sys.exit("Error reading vocabulary csv file: {}".format(e)) 
with open ("../../TG2_multirecord_measure_tests.csv", newline='') as multirecordcsvfile:
	try: 
		rawDataFrame = pandas.read_csv(multirecordcsvfile)
		multirecordDataFrame = rawDataFrame.sort_values(by=['Type','IE Class', 'Label'],ascending=[False,True,True])
		multirecordheader_names = list(multirecordDataFrame.columns)
	except pandas.errors.ParserError as e:
		sys.exit("Error reading multirecord measure csv file: {}".format(e)) 
with open ("../../TG2_tests.csv", newline='') as csvfile:
	sys.stdout = open("../docs/core_tests_quick_reference.md","w")
	rawDataFrame = pandas.read_csv(csvfile)
	dataFrame = rawDataFrame.sort_values(by=['Type','IE Class', 'Label'],ascending=[False,True,True])
	header_names = list(dataFrame.columns)
	try: 
		print ("---")
		print ("title:  TDWG BDQ Core Tests Quick Reference")
		print ("geometry: margin=1cm")
		print ("titlepage: true")
		print ("---")
		usecaseDict = dict()
		for index, row in dataFrame.iterrows():
			usecasesTerm = str(row["UseCases"])
			test = row['Label']
			foundUseCases = [val.strip() for val in usecasesTerm.split(',')]
			for useCase in foundUseCases: 
				usecaseDict.setdefault(useCase,[]).append(test)
		print("# Tests by UseCase")
		for useCase in usecaseDict.keys(): 
			print("## ",useCase)
			print()
			definitionRow = vocabDataFrame.loc[vocabDataFrame["namespace:Term"]==useCase]
			try: 
				definitionCell = definitionRow.iloc[0]["Definition"]
				print(definitionCell)
			except: 
				print("error extracting definition")
			print()
			for test in usecaseDict[useCase]:
				print("- [",test,"](#",test,")", sep="")
			print()
			print()
		# TODO: index by information element/information element class
		print()
		print("********************")
		print()
		print("# Validations, Amendments, Measures operating on SingleRecords.")
		print()
		for index, row in dataFrame.iterrows():
			print("## ",row['prefLabel'])
			print()
			print("### ",row['Label'])
			print("https://rs.tdwg.org/bdqcore/terms/{}/{}".format(row['GUID'],row['DateLastUpdated']))
			print("Acts upon ",row['Resource Type'])
			print()
			print("### Description")
			print()
			print(row['Description'])
			print()
			print("### Specification")
			print()
			print(row['Specification'])
			print()
			print("### Information Elements")
			if not pandas.isna(row['InformationElement:ActedUpon']) : 
				print()
				print("Acted Upon: ")
				print(row['InformationElement:ActedUpon'])
				print()
			if not pandas.isna(row['InformationElement:Consulted']) : 
				print("Consulted: ")
				print(row['InformationElement:Consulted'])
				print()
			if not pandas.isna(row['Parameters']) : 
				print("### Parameters")
				print()
				print(row['Parameters'])
				print()
			if not pandas.isna(row['AuthoritiesDefaults']) : 
				print("### Source Authorities and Default Parameter Values")
				print()
				print(row['AuthoritiesDefaults'])
				print()
			print("### Examples")
			print()
			examplesRaw = row['Examples']
			# examples are paired in the form [key:value response:value],[key:value response:value]
			# display as two lines without the enclosing square brackets.
			examples = [val.strip() for val in examplesRaw.split('],[')]
			for example in examples: 
				print(re.sub("\]$","",re.sub("^\[","",example)))
				print()
			print()
			print("### Use Cases")
			print()
			print(row['UseCases'])
			print()
			if not pandas.isna(row['Notes']) : 
				print("### Notes")
				print()
				print(row['Notes'])
				print()
			print("********************")
			print()
		print()
		print("# Measures operating on test Responses for MultiRecords (data sets).")
		print()
		for index, row in multirecordDataFrame.iterrows():
			# TODO: need pref label in multirecord csv.
			# print("## ",row['prefLabel'])
			print("## ",row['Label'])
			print()
			print("### ",row['Label'])
			print("https://rs.tdwg.org/bdqcore/terms/{}/{}".format(row['GUID'],row['DateLastUpdated']))
			print("Acts upon ",row['Resource Type'])
			print()
			print("### Description")
			print()
			print(row['Description'])
			print()
			print("### Specification")
			print()
			print(row['Specification'])
			print()
			print("### Information Elements")
			if not pandas.isna(row['InformationElement:ActedUpon']) : 
				print()
				print("Acted Upon: ")
				print(row['InformationElement:ActedUpon'])
				print()
			if not pandas.isna(row['InformationElement:Consulted']) : 
				print("Consulted: ")
				print(row['InformationElement:Consulted'])
				print()
			if not pandas.isna(row['Parameters']) : 
				print("### Parameters")
				print()
				print(row['Parameters'])
				print()
			print("### Use Cases")
			print()
			print(row['UseCases'])
			print()
			print("### Notes")
			print()
			print(row['Notes'])
			print()
			print("********************")
			print()
	except pandas.errors.ParserError as e:
		sys.exit("Error reading core test csv file: {}".format(e)) 
