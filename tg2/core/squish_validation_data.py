# Combine the information element fields in 
# TG2_test_validation_data.csv to one input field
# in an easier file for maintainers to work with
# 
# @author Paul J. Morris 
#
# Assumes run from same directory as input and output files
#
import pandas
import re
import sys
expandedFileName = "TG2_test_validation_data.csv"
outputFileName = "test_validation_maintainer.csv"
outputHeaders =  ["LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Input.data","Response.status","Response.result","Response.comment","IssuesWithThisRow"]
with open (expandedFileName) as csvfile: 
	print("Reading validation records from: " + expandedFileName)
	outfile = open(outputFileName,"w")
	line = ''
	separator = ""
	for header in outputHeaders : 
		line = line + separator + '"{}"'.format(header)
		separator = ","
	line = line + '\n'
	outfile.write(line)
	linesProcessed = 0
	try:
		print("Writing, combining all InformationElements into one Input.data column to: " + outputFileName)
		rawDataFrame = pandas.read_csv(csvfile,header=0)
		dataFrame = rawDataFrame.sort_values(by=['dataID'],ascending=[True])
		header_names = list(dataFrame.columns)
		# combine all except: 
		# "LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Response.status","Response.result","Response.comment","IssuesWithThisRow",
		# into input.data
		separate = ["LineNumber","dataID","LineForTest","GitHubIssueNo","GUID","Label","Response.status","Response.result","Response.comment","IssuesWithThisRow"]
		header_names_to_combine = list(set(header_names).difference(separate))
		try: 
			for index, row in dataFrame.iterrows():
				combinedTerms = ''
				separator = ""
				for term in header_names_to_combine:
					if not pandas.isna(row[term]) : 
						combinedTerms += separator + "{}=\"\"{}\"\"".format(term,row[term])
						separator = ", "
				line = '"{}","{}","{}",'.format(str(row['LineNumber']),str(row['dataID']),str(row['LineForTest']))
				line += '"{}","{}","{}",'.format(str(row['GitHubIssueNo']),str(row['GUID']),str(row['Label']))
				if pandas.isna(row['Response.result']) :
					responseResult = ""
				else :
					responseResult = row['Response.result']
					responseResult = responseResult.replace('"','""')
				comment = row['Response.comment']
				comment = comment.replace('"','""')
				line += '"{}","{}","{}","{}",'.format(combinedTerms,str(row['Response.status']),responseResult,comment)
				if pandas.isna(row['IssuesWithThisRow']) :
					issues = ""
				else :
					issues = row['IssuesWithThisRow']
				line += '"{}"'.format(issues)
				line += '\n'
				outfile.write(line)
				linesProcessed += 1
		except pandas.errors.ParserError as e:
			sys.exit("Error reading file: {}".format(e)) 
	except Exception as e:
		sys.exit("Error: {}".format(e)) 
	outfile.close()
	print("done, wrote " + str(linesProcessed) + " lines")
