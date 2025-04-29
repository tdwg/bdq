# Script to build dist/bdqtest_tests_vertical.csv from vocabulary/bdqtest_term_versions.csv
#
# @author Paul J. Morris 
#
# Assumes run from tg2/_review/build directory.
#
import pandas
import re
import sys
with open ("../_review/vocabulary/bdqtest_term_versions.csv") as csvfile: 
	try: 
		sys.stdout = open("../_review/dist/bdqtest_tests_vertical.csv","w")
		# Header
		# "#","GUID","DateLastUpdated","Label","prefLabel","IE Class","InformationElement:ActedUpon","InformationElement:Consulted","Parameters","Specification","Description","Criterion Label","Type","Resource Type","Dimension","Examples","Source","References","Example Implementations (Mechanisms)","Link to Specification Source Code","Notes","IssueState","IssueLabels","UseCases"
		rawDataFrame = pandas.read_csv(csvfile)
		dataFrame = rawDataFrame.sort_values(by=['Type','IE Class', 'Label'],ascending=[False,True,True])
		# header
		print('"Label","prefLabel","qualifiedName"');
		for index, row in dataFrame.iterrows():
			print('"{}","{}","bdqtest:{}"'.format(row['Label'],row['prefLabel'],row['term_localName']))
	except pandas.errors.ParserError as e:
		sys.exit("Error reading file: {}".format(e)) 
