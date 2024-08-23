# Produce markdown document listing tests from 
# intermediate csv list of tests TG2_tests.csv 
# 
# @author Paul J. Morris 
#
# Assumes run from generation/build directory of tg2 repository.
#
import pandas
import re
import sys
with open ("../../../vocabularies/bdq_vocabulary_terms.csv") as vocabfile: 
	vocabDataFrame = pandas.read_csv(vocabfile);
with open ("../../TG2_tests.csv", newline='') as csvfile:
	sys.stdout = open("../docs/core_tests.md","w")
	rawDataFrame = pandas.read_csv(csvfile)
	dataFrame = rawDataFrame.sort_values(by=['Type','IE Class', 'Label'],ascending=[False,True,True])
	header_names = list(dataFrame.columns)
	try: 
		print ("---")
		print ("title:  TDWG BDQ Core Tests")
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
				print("[",test,"](#",test,")", sep="", end=", ")
			print()
			print()
		# TODO: index by information element/information element class
		for index, row in dataFrame.iterrows():
			print("# ",row['prefLabel'])
			print()
			print("## ",row['Label'])
			print("https://rs.tdwg.org/bdq/{}".format(row['GUID']))
			print()
			print("## Description")
			print()
			print(row['Description'])
			print()
			print("## Specification")
			print()
			print(row['Specification'])
			print()
			for header in header_names: 
				if header == "Label":
					pass # shown above
				elif header == "Description":
					pass # shown above
				elif header == "Specification":
					pass
				elif header == "IssueState":
					pass # skip
				elif header == "IssueLabels":
					pass # skip
				elif header == "Source":
					pass # skip
				elif header == "IE class":
					pass # skip known from information elements
				elif header == "GUID":
					pass # skip, shown above
				elif header == "Link to Specification Source Code":
					print("## Link to example source code")
					print()
					value = row[header]
					print(value)
					print()
				elif header == "Examples":
					print("## Examples")
					print()
					examplesRaw = row[header]
					# examples are paired in the form [key:value response:value],[key:value response:value]
					# display as two lines without the enclosing square brackets.
					examples = [val.strip() for val in examplesRaw.split('],[')]
					for example in examples: 
						print(re.sub("\]$","",re.sub("^\[","",example)))
						print()
					print()
				elif header == "#":
					# print("| Rationale Management | https://github.com/tdwg/bdq/issues/",row[header],"|")
					print("## Rationale Management")
					print()
					print("[GitHub Issue: {}](https://github.com/tdwg/bdq/issues/{})".format(row[header],row[header]))
					print()
				else: 
					if not pandas.isna(row[header]) : 
						print("## ",header)
						print()
						# some values (citations) are html lists
						value = row[header]
						value = value.replace("<ul>","")
						value = value.replace("</ul>","")
						value = value.replace("<li>","- ")
						value = value.replace("</li>","\n")
						print(value)
						print()
			print()
			print("********************")
			print()
	except pandas.errors.ParserError as e:
		sys.exit("Error reading file: {}".format(e)) 
