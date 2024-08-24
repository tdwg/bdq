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
with open ("../../../vocabularies/bdqffdq_export.csv", newline='') as csvfile:
	sys.stdout = open("../docs/bdqffdq.md","w")
	rawDataFrame = pandas.read_csv(csvfile)
	dataFrame = rawDataFrame.sort_values(by=['Type','Superclass(es)', 'Entity'],ascending=[True,True,True])
	header_names = list(dataFrame.columns)
	# Entity,Type,Superclass(es),http://www.w3.org/2000/01/rdf-schema#comment,http://www.w3.org/2000/01/rdf-schema#label,
	try: 
		print ("---")
		print ("title:  TDWG BDQ Core Framework for data quality")
		print ("geometry: margin=1cm")
		print ("titlepage: true")
		print ("---")
		for index, row in dataFrame.iterrows():
			print("# ",row['http://www.w3.org/2000/01/rdf-schema#label'])
			print()
			print("## Name")
			print()
			print(row['Entity'])
			print()
			print("## Type")
			print()
			print(row['Type'])
			print()
			print("## Superclass")
			print()
			print(row['Superclass(es)'])
			print()
			print("## Comment")
			print()
			print(row['http://www.w3.org/2000/01/rdf-schema#comment'])
			print()
			print()
			print("********************")
			print()
	except pandas.errors.ParserError as e:
		sys.exit("Error reading file: {}".format(e)) 

