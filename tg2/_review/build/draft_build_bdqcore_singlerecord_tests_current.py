# Produce a CSV file with only the most recent version of each term_iri from bdqcore_term_versions.csv

import pandas as pd
import csv

input_csv = '../vocabulary/bdqcore_term_versions.csv'
output_csv = '../dist/bdqcore_singlerecord_tests_current.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv)

# Filter the DataFrame to include only rows where "Resource Type" is "SingleRecord"
df_single = df[df['Resource Type'] == 'SingleRecord']
   
# Ensure the DateLastUpdated column is in datetime format
df_single['DateLastUpdated'] = pd.to_datetime(df_single['DateLastUpdated'])
    
# Sort the DataFrame by term_iri and DateLastUpdated in descending order
df_sorted = df_single.sort_values(by=['term_iri', 'DateLastUpdated'], ascending=[True, False])

# Drop duplicates based on term_iri, keeping the first occurrence (which is the most recent)
df_filtered = df_sorted.drop_duplicates(subset='term_iri', keep='first')

df_output = df_filtered.sort_values(by=['issueNumber'], ascending=[True])
   
# Print the filtered DataFrame to output file
outputObject = open(output_csv, 'wt', encoding='utf-8')
outputObject.write(df_output.to_csv(index=False, quoting=csv.QUOTE_ALL))
outputObject.close()

