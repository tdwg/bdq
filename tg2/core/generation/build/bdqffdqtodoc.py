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
	indexdataFrame = rawDataFrame.sort_values(by=['Entity'],ascending=[True])
	header_names = list(dataFrame.columns)
	# Entity,Type,Superclass(es),http://www.w3.org/2000/01/rdf-schema#comment,http://www.w3.org/2000/01/rdf-schema#label,
	try: 
		print ("---")
		print ("title:  TDWG BDQ Core Framework for data quality")
		print ("geometry: margin=1cm")
		print ("titlepage: true")
		print ("---")
		print ("Ontology Terms forming the BDQ Core Framework For Data Quality.")
		print()
		print("- [Classes](#Class-terms)")
		print("- [Named Individuals](#NamedIndividual-terms)")
		print("- [Object Properties](#ObjectProperty-terms)")
		print("- [Data Properties](#DataProperty-terms)")
		print()
		print("Alphabetical Index of classes")
		print()
		for index, row in indexdataFrame.iterrows():
			currentType = row['Type']
			if (currentType=="Class") : 
				parent = ""
				if (row["Superclass(es)"] != "http://www.w3.org/2002/07/owl#Thing") : 
					parent = row["Superclass(es)"]
					parent = parent.replace("https://rs.tdwg.org/bdqffdq/terms/","") 
				entity = row['Entity']
				entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
				print("- [{}](#{}) {}".format(entity,entity.replace(":",""),parent))
		print("********************")
		lastType = ""
		for index, row in dataFrame.iterrows():
			currentType = row['Type']
			if (currentType!=lastType) : 
				print()
				print("# {} terms".format(currentType))
				print()
				print("********************")
				print()
				lastType = currentType
			entity = row['Entity']
			entity = entity.replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:");
			print("##",entity)
			print()
			print("### Name")
			print()
			print(row['Entity'])
			print()
			print("### Preferred Label")
			print()
			print(row['http://www.w3.org/2004/02/skos/core#prefLabel'])
			print()
			print("### Label")
			print()
			print(row['http://www.w3.org/2000/01/rdf-schema#label'])
			print()
			print("### Type")
			print()
			print(row['Type'])
			print()
			if not pandas.isna(row["Superclass(es)"]) : 
				if (row["Superclass(es)"]!="http://www.w3.org/2002/07/owl#Thing") : 
					print("## Superclass")
					print()
					print(row['Superclass(es)'].replace("https://rs.tdwg.org/bdqffdq/terms/","bdqffdq:")) 
					print()
			print("### Definition")
			print()
			print(row['http://www.w3.org/2004/02/skos/core#definition'])
			print()
			if not pandas.isna(row["http://www.w3.org/2000/01/rdf-schema#comment"]) : 
				print("### Comment")
				print()
				print(row['http://www.w3.org/2000/01/rdf-schema#comment'])
				print()
			print()
			print("********************")
			print()
	except pandas.errors.ParserError as e:
		sys.exit("Error reading file: {}".format(e)) 

