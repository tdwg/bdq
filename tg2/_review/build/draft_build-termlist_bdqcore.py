# Script to build Markdown pages that provide term metadata for complex vocabularies
# Steve Baskauf 2020-08-12 CC0
# updated 2021-02-11
# Modified Paul J. Morris for generating draft standard documents without rs.tdwg.org files 
# 2024-09-12
# This script merges static Markdown header and footer documents with generated term information tables loading data from in local csv and yaml files.
# Unlike the original, this version is intended to run entirely on local files.
# This script processes the bdqcore vocabulary as phrased with the bdqffdq vocabulary.

import re
# import requests   # best library to manage HTTP transactions
import csv        # library to read/write/parse CSV files
import json       # library to convert JSON to Python data structures
import pandas as pd  # library to handle data loaded from csv as data frames
import yaml       # Library to parse yaml files
import rdflib     # run sparql queries on rdf 
from rdflib import Graph
import function_lib # library of reusable functions for TDWG build scripts
from function_lib import build_authors_contributors_markdown, build_contributors_markdown, markdown_heading_to_link

# -----------------
# Configuration section
# -----------------

# This is a Python list of the names of the term lists for which documents are to be produced.
# One set of documents is produced for each term.  See assumptions below.
termLists = ['bdqcore']

# The RDF representation of the tests.
testRdfDocument = 'https://raw.githubusercontent.com/tdwg/bdq/refs/heads/master/tg2/_review/dist/bdqcore.xml'
prefixes = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdqcore: <https://rs.tdwg.org/bdqcore/terms/>
"""

# This is the base URL for raw files from the branch of the repo that has been pushed to GitHub
github_branch = 'master' # "master" for production, something else for development
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/bdq/' + github_branch + '/tg2/core/generation/'

# ----------------
# Assumptions 
# ---------------
# (1) The repository has build/ docs/ dist/ and vocabulary/ directories in the same parent directory.
# (2) This file is located in a build/ directory
# (3) This file produces human readable documents in the docs/ directory within docs/list/{term}/ directories
# (4) This file produces rdf artifacts in the the dist/ directory.
# (5) The source csv file for each term is vocabulary/{term}_terms.csv
# (6) A list of authors/contributors is in the build/ directory in: 
contributors_yaml_file = 'authors_configuration.yaml'
# (7) local replacements for metadata namespaces and term-lists.csv files 
# are in the build/ directory in the following files, which provide metadata for each term in termLists: 
term_list_document = "temp_term-lists.csv"
local_metadata_config_file = 'temp_namespaces.yaml'
# (8) {term}_termlist-header.md, {term}_termlist-footer.md files are in build/templates/list/{term}/ along with a document_configuration.yaml file
# see loop below through termLists
# headerFileName = 'templates/list/{}/{}_termlist-header.md'.format(term,term)
# footerFileName = 'templates/list/{}/{}_termlist-footer.md'.format(term,term)
# document_configuration_yaml_file = 'templates/list/{}/document_configuration.yaml'.format(term)

# The following configuration values apply to all terms in termLists: 

# If this list of terms is for terms in a single namespace, set the value of has_namespace to True. The value
# of has_namespace should be False for a list of terms that contains multiple namespaces.
has_namespace = True

# NOTE! There may be problems unless every term list is of the same vocabulary type since the number of columns will differ
# However, there probably aren't any circumstances where mixed types will be used to generate the same page.
## bdqcore not simple, using ontology, so terms fully hardcoded below.
vocab_type = 1 # 1 is simple vocabulary, 2 is simple controlled vocabulary, 3 is c.v. with broader hierarchy

# Terms in large vocabularies like Darwin and Audubon Cores may be organized into categories using tdwgutility_organizedInClass
# If so, those categories can be used to group terms in the generated term list document.
organized_in_categories = True

# If organized in categories, the display_order list must contain the IRIs that are values of tdwgutility_organizedInClass
# If not organized into categories, the value is irrelevant. There just needs to be one item in the list.

display_order = ['Type']
display_label = ['Type'] # these are the section labels for the categories in the page
display_comments = [''] # these are the comments about the category to be appended following the section labels
display_id = ['Type'] # these are the fragment identifiers for the associated sections for the categories

# ---------------
# Load header data
# ---------------

# Load the contributors YAML file from its local location.
with open(contributors_yaml_file) as cyf:
    contributors_yaml = yaml.load(cyf, Loader=yaml.FullLoader)

if has_namespace:
    # Load the configuration file used in the metadata creation process.
    #metadata_config_text = requests.get(githubBaseUri + 'process/config.yaml').text
    # PJM: Using local file for namespace when building draft documents
    metadata_config_text = open('temp_namespaces.yaml','r')
    metadata_config = yaml.load(metadata_config_text, Loader=yaml.FullLoader)
    namespace_uri = metadata_config['namespaces'][0]['namespace_uri']
    pref_namespace_prefix = metadata_config['namespaces'][0]['pref_namespace_prefix']

# ---------------
# Retrieve term list metadata from GitHub
# ---------------

## PJM: Unavailable for draft without rs.tdwg.org files
print('Loading term list metadata')
term_lists_info = []


print(term_list_document)
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
print(term_lists_info)
print()

# ---------------
# Load rdf
# ---------------

graph = rdflib.Graph()
graph.parse(testRdfDocument, format="xml")

# ---------------
# Create metadata table and populate using data from namespace databases in GitHub
# ---------------

for term in termLists: 
    print('Generating files for {}.'.format(term))
    headerFileName = 'templates/list/{}/{}_termlist-header.md'.format(term,term)
    footerFileName = 'templates/list/{}/{}_termlist-footer.md'.format(term,term)
    document_configuration_yaml_file = 'templates/list/{}/document_configuration.yaml'.format(term)
    outFileName = '../docs/list/{}/index.md'.format(term)
    outRDFFileName = '../dist/{}.xml'.format(term)
    # there isn't one for bdqcore, closest is bdqcore_terms.csv
    term_history_csv = "../vocabulary/bdqcore_terms.csv".format(term)

    # Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
    # load from local file
    with open(document_configuration_yaml_file) as dcfy:
        document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

    # Create column list - custom list for bdqcore terms.
    # TODO: This doesn't include everything in the RDF, need to get this document from the rdf, or build a csv with all the terms.
    column_list = ["Label","#","iri","term_iri","issued","term_localName","DateLastUpdated","prefLabel","IE Class","InformationElement:ActedUpon","InformationElement:Consulted","Parameters","Specification","AuthoritiesDefaults","Description","Criterion Label","Type","Resource Type","Dimension","Criterion","Enhancement","Examples","Source","References","Example Implementations (Mechanisms)","Link to Specification Source Code","Notes","IssueState","IssueLabels","UseCases"]
    #column_list = ['pref_ns_prefix', 'pref_ns_uri', 'term_localName', 'label', 'definition', 'usage', 'notes', 'term_modified', 'term_deprecated', 'type']
    if vocab_type == 2:
        column_list += ['controlled_value_string']
    #elif vocab_type == 3:
    #    column_list += ['controlled_value_string', 'skos_broader']
    #if organized_in_categories:
    #    column_list.append('tdwgutility_organizedInClass')
    # PJM?? version_iri appears in the documents as iri.
    #column_list.append('version_iri')
    
    print('Retrieving metadata about terms from all namespaces from GitHub')
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
                # TODO: This doesn't include everything in the RDF, need to get this document from the rdf, or build a csv with all the terms.
                row_list = [ row['Label'], row['#'], row['iri'], row['term_iri'], row['issued'], row['term_localName'], row['DateLastUpdated'], row['prefLabel'], row['IE Class'], row['InformationElement:ActedUpon'], row['InformationElement:Consulted'], row['Parameters'], row['Specification'], row['AuthoritiesDefaults'], row['Description'], row['Criterion Label'], row['Type'], row['Resource Type'], row['Dimension'], row['Criterion'], row['Enhancement'], row['Examples'], row['Source'], row['References'], row['Example Implementations (Mechanisms)'], row['Link to Specification Source Code'], row['Notes'], row['IssueState'], row['IssueLabels'], row['UseCases'] ]
                # row_list = [row['iri'], row['term_localName'], row['prefLabel'], row['label'], row['comments'], row['definition'], row['rdf_type'], row['organized_in'] ,row['issued'],row['status'],row['term_iri'],row['flags'] ]
        
                table_list.append(row_list)
                print(row_list)
        
    print('processing data')
    print(column_list)
    # Turn list of lists into dataframe
    terms_df = pd.DataFrame(table_list, columns = column_list)
    
    terms_sorted_by_label = terms_df.sort_values(by='Label')
    #terms_sorted_by_localname = terms_df.sort_values(by='term_localName')
    
    # This makes sort case insensitive
    terms_sorted_by_localname = terms_df.iloc[terms_df.prefLabel.str.lower().argsort()]
    #terms_sorted_by_localname
    print('done retrieving')
    print()
    
    # ---------------
    # generate the index of terms grouped by category and sorted alphabetically by lowercase term local name
    # ---------------
    
    print('Generating term index by CURIE')
    text = '### 3.1 Index By Term Name\n\n'
    text += '(See also [3.2 Index By Label](#32-index-by-label))\n\n'
    
    text += '**Classes**\n'
    text += '\n'
    for row_index,row in terms_sorted_by_localname.iterrows():
        if row['Type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
            curie = row['pref_ns_prefix'] + ":" + row['term_localName']
            curie_anchor = curie.replace(':','_')
            text += '[' + curie + '](#' + curie_anchor + ') |\n'
    text = text[:len(text)-2] # remove final trailing vertical bar and newline
    text += '\n\n' # put back removed newline
    
    for category in range(0,len(display_order)):
        text += '**' + display_label[category] + '**\n'
        text += '\n'
        if organized_in_categories:
            filtered_table = terms_sorted_by_localname[terms_sorted_by_localname['Type']==display_order[category]]
            filtered_table.reset_index(drop=True, inplace=True)
        else:
            filtered_table = terms_sorted_by_localname
            
        for row_index,row in filtered_table.iterrows():
            if row['rdf_type'] != 'http://www.w3.org/2000/01/rdf-schema#Class':
                # curie = row['pref_ns_prefix'] + ":" + row['term_localName']
                ## PJM: Assuming term is prefix for all terms in vocabulary file
                curie = term + ":" + row['term_localName']
                #curie = "bdqdim:" + row['term_localName']
                curie_anchor = curie.replace(':','_')
                text += '[' + curie + '](#' + curie_anchor + ') |\n'
        text = text[:len(text)-2] # remove final trailing vertical bar and newline
        text += '\n\n' # put back removed newline
    
    index_by_name = text
    
    #print(index_by_name)
    print()
    
    # ---------------
    # generate the index of terms by label
    # ---------------
    
    print('Generating term index by label')
    text = '\n\n'
    
    # Comment out the following two lines if there is no index by local names
    text = '### 3.2 Index By Label\n\n'
    text += '(See also [3.1 Index By Term Name](#31-index-by-term-name))\n\n'
    
    text += '**Tests**\n'
    text += '\n'
    for row_index,row in terms_sorted_by_label.iterrows():
        curie = "bdqcore:" + row['term_localName']
        curie_anchor = curie.replace(':','_')
        text += '[' + row['Label'] + '](#' + curie_anchor + ') |\n'
    text = text[:len(text)-2] # remove final trailing vertical bar and newline
    text += '\n\n' # put back removed newline
    
    for category in range(0,len(display_order)):
        if organized_in_categories:
            text += '**' + display_label[category] + '**\n'
            text += '\n'
            filtered_table = terms_sorted_by_label[terms_sorted_by_label['Type']==display_order[category]]
            filtered_table.reset_index(drop=True, inplace=True)
        else:
            filtered_table = terms_sorted_by_label
            
        for row_index,row in filtered_table.iterrows():
            if row_index == 0 or (row_index != 0 and row['label'] != filtered_table.iloc[row_index - 1].loc['label']): # this is a hack to prevent duplicate labels
                if row['rdf_type'] != 'http://www.w3.org/2000/01/rdf-schema#Class':
                    # curie_anchor = row['pref_ns_prefix'] + "_" + row['term_localName']
                    ## PJM: Assuming term is prefix for all terms in vocabulary file
                    curie = term + ":" + row['term_localName']
                    curie_anchor = curie.replace(':','_')
                    text += '[' + row['label'] + '](#' + curie_anchor + ') |\n'
        text = text[:len(text)-2] # remove final trailing vertical bar and newline
        text += '\n\n' # put back removed newline
    
    index_by_label = text
    print()
    
    #print(index_by_label)
    
    ## PJM: Decisions won't apply for draft standards.
    # decisions_df = pd.read_csv('https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/decisions/decisions-links.csv', na_filter=False)

    # ---------------
    # generate a table for each term, with terms grouped by category
    # ---------------
    
    ## PJM: SDS 3.3.3.1 Term list metadata 
    # Each term entry on the list SHOULD include the following items.
    # Term Name (Required)
    # Label 
    # Controlled Value (Required for controlled Vocabularies)
    # Term IRI (Required) The HTTP IRI that uniquely identifies the current term 
    # Term version IRI (Required) The HTTP IRI that identifies the version of the term that is currently in force. (Required if defined for vocabulary (is so for TDWG vocabularies)).
    # Modified
    # Decision
    # Definition (Required)
    # Type (Required) Values include "Class", "Property", and "Concept".
    
    # PJM: TODO: map from row column headers 
    
    
    print('Generating terms table')
    # generate the Markdown for the terms table
    text = '## 4 Vocabulary\n'
    if True:
        filtered_table = terms_sorted_by_localname
    
        # row_list = [ row['#'], row['GUID'], row['DateLastUpdated'], row['Label'], row['prefLabel'], row['IE Class'], row['InformationElement:ActedUpon'], row['InformationElement:Consulted'], row['Parameters'], row['Specification'], row['AuthoritiesDefaults'], row['Description'], row['Criterion Label'], row['Type'], row['Resource Type'], row['Dimension'], row['Criterion'], row['Enhancement'], row['Examples'], row['Source'], row['References'], row['Example Implementations (Mechanisms)'], row['Link to Specification Source Code'], row['Notes'], row['IssueState'], row['IssueLabels'], row['UseCases'] ]
        for row_index,row in filtered_table.iterrows():
            text += '<table>\n'
            curie =  "bdqcore:" + row['term_localName']
            curieAnchor = curie.replace(':','_')
            text += '\t<thead>\n'
            text += '\t\t<tr>\n'
            text += '\t\t\t<th colspan="2"><a id="' + curieAnchor + '"></a>Term Name  ' + curie + '</th>\n'
            text += '\t\t</tr>\n'
            text += '\t</thead>\n'
            text += '\t<tbody>\n'
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Label</td>\n'
            text += '\t\t\t<td>' + row['Label'] + '</td>\n'
            text += '\t\t</tr>\n'
            for column in column_list : 
                if column != "term_localName" and column != "#" and column != "Label" and column != "IssueState" and column != "IssueLabels" and column!="#" : 
                    if row[column] : 
                        text += '\t\t<tr>\n'
                        text += '\t\t\t<td>{}</td>\n'.format(column)
                        text += '\t\t\t<td>{}</td>\n'.format(row[column])
                        text += '\t\t</tr>\n'
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>skos:historyNote</td>\n'
            text += '\t\t\t<td>https://github.com/tdwg/bdq/issues/' + str(row['#']) + '</td>\n'
            text += '\t\t</tr>\n'

            testType = row['Type']

            sparql = prefixes + "SELECT ?method ?predicate ?label ?specification ?specificationLabel  WHERE {  ?specification rdfs:label ?specificationLabel .  ?method bdqffdq:hasSpecification ?specification .  ?method ?predicate ?label .  ?method  bdqffdq:for"+testType+" bdqcore:"+row['term_localName']+" .  FILTER ( ?predicate = rdfs:label ) }"
            queryResult = graph.query(sparql)
            print(sparql)
            for r in queryResult : 
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>bdqffdq:'+testType+'Method</td>\n'
                text += '\t\t\t<td>' + str(r['method']) + '</td>\n'
                text += '\t\t</tr>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>'+testType+'Method label</td>\n'
                text += '\t\t\t<td>' + str(r['label']) + '</td>\n'
                text += '\t\t</tr>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>bdqffdq:Specification</td>\n'
                text += '\t\t\t<td>' + str(r['specification']) + '</td>\n'
                text += '\t\t</tr>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Specification label</td>\n'
                text += '\t\t\t<td>' + str(r['specificationLabel']) + '</td>\n'
                text += '\t\t</tr>\n'
               
    
            ## PJM: Decisions won't apply for draft standards.
            # Look up decisions related to this term
            #for drow_index,drow in decisions_df.iterrows():
            #    if drow['linked_affected_resource'] == uri:
            #        text += '\t\t<tr>\n'
            #        text += '\t\t\t<td>Executive Committee decision</td>\n'
            #        text += '\t\t\t<td><a href="http://rs.tdwg.org/decisions/' + drow['decision_localName'] + '">http://rs.tdwg.org/decisions/' + drow['decision_localName'] + '</a></td>\n'
            #        text += '\t\t</tr>\n'                        
    
            text += '\t</tbody>\n'
            text += '</table>\n'
            text += '\n'
        text += '\n'
    term_table = text
    print('done generating')
    print()
    
    #print(term_table)
    
    # ---------------
    # Merge term table with header and footer Markdown, then save file
    # ---------------
    
    print('Merging term table with header and footer and saving file')
    #text = index_by_label + term_table
    text = index_by_name + index_by_label + term_table
    
    # read in header and footer, merge with terms table, and output
    
    headerObject = open(headerFileName, 'rt', encoding='utf-8')
    header = headerObject.read()
    headerObject.close()
    

    # Substitute values of ratification_date and contributors into the header template
    print(document_configuration_yaml)
    header = header.replace("<!--- Template for header, values provided from yaml configuration --->","")
    header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
    header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
    header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
    # Build the Markdown for the authors and contributors lists or the contributors list
    contributors = build_authors_contributors_markdown(contributors_yaml)
    header = header.replace('{authors_contributors}', contributors)
    contributors = build_contributors_markdown(contributors_yaml)
    header = header.replace('{contributors}', contributors)
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
    
    # Determine whether there was a previous version of the document.
    if document_configuration_yaml['doc_created'] != document_configuration_yaml['doc_modified']:
        # Load versions list from document versions data in the rs.tdwg.org repo and find most recent version.
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
    
    warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"
    
    ## Produce a table of contents from the headings 
    toc = ""
    regexHeadings = "^#+ [0-9]+.*"
    for line in (header+text).splitlines() :
        aHeading = re.search(regexHeadings,line)
        if (aHeading) : 
            toc = toc + "- " + markdown_heading_to_link(aHeading.group()) + "\n"
    header = header.replace('{toc}', toc)

    output = warning + header + text + footer
    outputObject = open(outFileName, 'wt', encoding='utf-8')
    outputObject.write(output)
    outputObject.close()
    
print('done')

