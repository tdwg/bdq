# Produce a CSV file with only the most recent version of each term_iri from bdqcore_term_versions.csv

import pandas as pd

input_csv = '../vocabulary/bdqcore_term_versions.csv'
output_csv = '../dist/bdqcore_siglerecord_tests_current.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv)
    
# Ensure the DateLastUpdated column is in datetime format
df['DateLastUpdated'] = pd.to_datetime(df['DateLastUpdated'])
    
# Sort the DataFrame by term_iri and DateLastUpdated in descending order
df_sorted = df.sort_values(by=['term_iri', 'DateLastUpdated'], ascending=[True, False])
    
# Drop duplicates based on term_iri, keeping the first occurrence (which is the most recent)
df_filtered = df_sorted.drop_duplicates(subset='term_iri', keep='first')
    
# Print the filtered DataFrame to output file
outputObject = open(output_csv, 'wt', encoding='utf-8')
outputObject.write(df_filtered.to_csv(index=False))
outputObject.close()

