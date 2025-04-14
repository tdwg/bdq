# Script to build Markdown pages that provide term metadata for complex vocabularies
# Steve Baskauf 2020-08-12 CC0
# updated 2021-02-11
# Modified Paul J. Morris for generating draft standard documents without rs.tdwg.org files
# 2024-09-12
# This script merges static Markdown header and footer documents with generated term information tables loading data from in local csv and yaml files.
# Unlike the original, this version is intended to run entirely on local files.

import re
# import requests   # best library to manage HTTP transactions
import csv        # library to read/write/parse CSV files
import json       # library to convert JSON to Python data structures
import pandas as pd  # library to handle data loaded from csv as data frames
import yaml       # Library to parse yaml files
import rdflib     # run sparql queries on rdf 
from rdflib import Graph
import function_lib # library of reusable functions for TDWG build scripts
from function_lib import build_term_key, build_authors_contributors_markdown
from function_lib import build_contributors_markdown, build_authors_markdown
from function_lib import generate_markdown_toc

# -----------------
# Configuration section
# -----------------

# set debug = True for additional debugging output
debug = False

# prefixes for sparql queries
prefixes = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
PREFIX bdqdim: <https://rs.tdwg.org/bdqdim/terms/>
"""

# This is a Python list of the names of the term lists for which documents are to be produced.
# One set of documents is produced for each term.  See assumptions below.
termLists = ['bdqdim','bdq','bdqenh','bdqcrit']

# This is the base URL for raw files from the branch of the repo that has been pushed to GitHub
github_branch = 'master' # "master" for production, something else for development
# TODO: Post ratification of the standard, this will have to be changed to the location for the docs-versions.csv file
# expected to be: githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + github_branch + '/'
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/bdq/' + github_branch + '/tg2/core/generation/'

# This is the configuration file to build a key to the terms used to describe the vocabulary terms.
vocabulary_configuration_yaml_file = "vocabulary_configuration.yaml"

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
# (9) Each vocabulary has the same list of terms, dictionary to build key loaded from a common configuration file.
#
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
vocab_type = 2 # 1 is simple vocabulary, 2 is simple controlled vocabulary, 3 is c.v. with broader hierarchy

# Terms in large vocabularies like Darwin and Audubon Cores may be organized into categories using tdwgutility_organizedInClass
# If so, those categories can be used to group terms in the generated term list document.
organized_in_categories = False

# If organized in categories, the display_order list must contain the IRIs that are values of tdwgutility_organizedInClass
# If not organized into categories, the value is irrelevant. There just needs to be one item in the list.

display_order = ['']
display_label = ['Vocabulary'] # these are the section labels for the categories in the page
display_comments = [''] # these are the comments about the category to be appended following the section labels
display_id = ['Vocabulary'] # these are the fragment identifiers for the associated sections for the categories

# Load the vocabulary configuration YAML file from its local location.  
# load from local file
with open(vocabulary_configuration_yaml_file) as vcfy:
   term_concept_dictionary = yaml.load(vcfy, Loader=yaml.FullLoader)

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

if debug :
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
if debug :
    print(term_lists_info)
    print()

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
    term_history_csv = "../vocabulary/{}_term_versions.csv".format(term)
    if term == 'bdq' : 
        organized_in_categories = True
        display_order = ['Data','bdq:Parameter','bdqffdq:UseCase','bdqffdq:InformationElement']
        display_label = ['Data','bdq:Parameter','bdqffdq:UseCase','bdqffdq:InformationElement']
    else : 
        organized_in_categories = False
        display_order = ['']
        display_label = ['Vocabulary']

    # Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
    # load from local file
    with open(document_configuration_yaml_file) as dcfy:
        document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

    # Create column list
    column_list = ['iri', 'term_localName', 'prefLabel', 'label', 'comments', 'definition', 'rdf_type', 'organized_in','issued','status','term_iri','flags']
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
                row_list = [row['iri'], row['term_localName'], row['prefLabel'], row['label'], row['comments'], row['definition'], row['rdf_type'], row['organized_in'] ,row['issued'],row['status'],row['term_iri'],row['flags'] ]
        
                # PJM: TODO: column headers in term version files for simple vocabularies: 
                # iri,term_localName,prefLabel,label,definition,comments,organized_in,issued,status,replaces,rdf_type,term_iri,flags
        
                # row_list = [term_list['pref_ns_prefix'], term_list['pref_ns_uri'], row['term_localName'], row['label'], row['rdfs_comment'], row['dcterms_description'], row['examples'], row['term_modified'], row['term_deprecated'], row['rdf_type'], row['tdwgutility_abcdEquivalence'], row['replaces_term'], row['replaces1_term']]
                #row_list = [term_list['pref_ns_prefix'], term_list['pref_ns_uri'], row['term_localName'], row['label'], row['definition'], row['usage'], row['notes'], row['term_modified'], row['term_deprecated'], row['type']]
                if vocab_type == 2:
                    row_list += [row['controlled_value_string']]
                    if debug :
                        print(row_list)
        #        elif vocab_type == 3:
        #            if row['skos_broader'] =='':
        #                row_list += [row['controlled_value_string'], '']
        #            else:
        #                row_list += [row['controlled_value_string'], term_list['pref_ns_prefix'] + ':' + row['skos_broader']]
        #        if organized_in_categories:
        #            row_list.append(row['tdwgutility_organizedInClass'])
        
                # Borrowed terms really don't have implemented versions. They may be lacking values for version_status.
                # In their case, their version IRI will be omitted.
        #        found = False
        #        for vindex, vrow in versions_df.iterrows():
        #            if vrow['term_localName']==row['term_localName'] and vrow['version_status']=='recommended':
        #                found = True
        #                version_iri = vrow['version']
        #                # NOTE: the current hack for non-TDWG terms without a version is to append # to the end of the term IRI
        #                if version_iri[len(version_iri)-1] == '#':
        #                    version_iri = ''
        #        if not found:
        #            version_iri = ''
        #        row_list.append(version_iri)
        
                table_list.append(row_list)
                if debug :
                    print(row_list)
        
    print('processing data')
    if debug :
        print(column_list)
    # Turn list of lists into dataframe
    terms_df = pd.DataFrame(table_list, columns = column_list)
    
    terms_sorted_by_label = terms_df.sort_values(by='label')
    #terms_sorted_by_localname = terms_df.sort_values(by='term_localName')
    
    # This makes sort case insensitive
    terms_sorted_by_localname = terms_df.iloc[terms_df.term_localName.str.lower().argsort()]
    #terms_sorted_by_localname
    print('done retrieving')
    if debug :
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
        if row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
            curie = row['pref_ns_prefix'] + ":" + row['term_localName']
            curie_anchor = curie.replace(':','_')
            text += '[' + curie + '](#' + curie_anchor + ') |\n'
    text = text[:len(text)-2] # remove final trailing vertical bar and newline
    text += '\n\n' # put back removed newline
    
    for category in range(0,len(display_order)):
        text += '**' + display_label[category] + '**\n'
        text += '\n'
        if organized_in_categories:
            filtered_table = terms_sorted_by_localname[terms_sorted_by_localname['organized_in']==display_order[category]]
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
    
    # ---------------
    # generate the index of terms by label
    # ---------------
    
    print('Generating term index by label')
    text = '\n\n'
    
    # Comment out the following two lines if there is no index by local names
    text = '### 3.2 Index By Label\n\n'
    text += '(See also [3.1 Index By Term Name](#31-index-by-term-name))\n\n'
    
    text += '**Classes**\n'
    text += '\n'
    for row_index,row in terms_sorted_by_label.iterrows():
        if row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
            ## PJM: Assuming term is prefix for all terms in vocabulary file
            curie = term + ":" + row['term_localName']
            curie_anchor = curie.replace(':','_')
            text += '[' + row['label'] + '](#' + curie_anchor + ') |\n'
    text = text[:len(text)-2] # remove final trailing vertical bar and newline
    text += '\n\n' # put back removed newline
    
    for category in range(0,len(display_order)):
        if organized_in_categories:
            text += '**' + display_label[category] + '**\n'
            text += '\n'
            filtered_table = terms_sorted_by_label[terms_sorted_by_label['organized_in']==display_order[category]]
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
    
    ## PJM: Decisions won't apply for draft standards.
    # decisions_df = pd.read_csv('https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/decisions/decisions-links.csv', na_filter=False)

    # PJM: TODO: Write xml
    outputRdfHeader = "<rdf:RDF\n"
    outputRdfHeader += 'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n'
    outputRdfHeader += 'xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"\n'
    outputRdfHeader += 'xmlns:xsd="http://www.w3.org/2001/XMLSchema#"\n'
    outputRdfHeader += 'xmlns:owl="http://www.w3.org/2002/07/owl#"\n'
    outputRdfHeader += 'xmlns:dc="http://purl.org/dc/elements/1.1/"\n'
    outputRdfHeader += 'xmlns:bdq="https://rs.tdwg.org/bdq/terms/"\n'
    outputRdfHeader += 'xmlns:bdqdim="https://rs.tdwg.org/bdqdim/terms/"\n'
    outputRdfHeader += 'xmlns:bdqenh="https://rs.tdwg.org/bdqenh/terms/"\n'
    outputRdfHeader += 'xmlns:bdqcrit="https://rs.tdwg.org/bdqcrit/terms/"\n'
    outputRdfHeader += 'xmlns:bdqcore="https://rs.tdwg.org/bdqcore/terms/"\n'
    outputRdfHeader += 'xmlns:bdqffdq="https://rs.tdwg.org/bdqffdq/terms/"\n'
    outputRdfHeader += 'xmlns:dcterms="http://purl.org/dc/terms/"\n'
    outputRdfHeader += 'xmlns:dwc="http://rs.tdwg.org/dwc/terms/"\n'
    outputRdfHeader += 'xmlns:skos="http://www.w3.org/2004/02/skos/core#"\n'
    outputRdfHeader += 'xmlns:tdwgutility="http://rs.tdwg.org/dwc/terms/attributes/"\n'
    outputRdfHeader += 'xmlns:foaf="http://xmlns.com/foaf/0.1/"\n'
    outputRdfHeader += 'xmlns:dwciri="http://rs.tdwg.org/dwc/iri/"\n'
    outputRdfHeader += ">\n"
    #
    outputRdf = ""
    #
    outputRdfFooter = '<rdf:Description rdf:about="http://rs.tdwg.org/{}/terms/">\n'.format(term)
    outputRdfFooter += '     <dc:format>application/rdf+xml</dc:format>\n'
    outputRdfFooter += '     <dc:creator>Biodiversity Information Standards (TDWG)</dc:creator>\n'
    outputRdfFooter += '     <dcterms:references rdf:resource="http://rs.tdwg.org/{}/terms/"/>\n'.format(term)
    #outputRdfFooter += '     <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2021-09-01T22:18:44-05:00</dcterms:modified>\n'
    outputRdfFooter += '     <rdf:type rdf:resource="http://xmlns.com/foaf/0.1/document"/>\n'
    outputRdfFooter += '</rdf:Description>\n'
    outputRdfFooter += '\n'
    outputRdfFooter += '</rdf:RDF>\n'
    
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
    # Dictionary of column heading: dictionary of label:, term, (could include normative}

    definitionTable = build_term_key(term_concept_dictionary, terms_sorted_by_localname)

    print('Generating terms table')
    # generate the Markdown for the terms table
    text = '## 4 Vocabulary\n'
    if True:
        filtered_table = terms_sorted_by_localname
    
    #for category in range(0,len(display_order)):
    #    if organized_in_categories:
    #        text += '### 4.' + str(category + 1) + ' ' + display_label[category] + '\n'
    #        text += '\n'
    #        text += display_comments[category] # insert the comments for the category, if any.
    #        filtered_table = terms_sorted_by_localname[terms_sorted_by_localname['tdwgutility_organizedInClass']==display_order[category]]
    #        filtered_table.reset_index(drop=True, inplace=True)
    #    else:
    #        filtered_table = terms_sorted_by_localname
    
        for row_index,row in filtered_table.iterrows():
            # row_list = [row['iri'], row['term_localName'], row['prefLabel'], row['label'], row['comments'], row['definition'], row['rdf_type'], row['organized_in'] ,row['issued'],row['status'],row['term_iri'],row['flags'] ]
            outputRdf += '<rdf:Description rdf:about="{}">\n'.format(row['iri'])
            outputRdf += '     <rdfs:isDefinedBy rdf:resource="http://rs.tdwg.org/{}/terms/"/>\n'.format(term)
            outputRdf += '     <dcterms:isPartOf rdf:resource="http://rs.tdwg.org/{}/terms/"/>\n'.format(term)
            outputRdf += '     <dcterms:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#date">{}</dcterms:issued>\n'.format(row['issued'])
            outputRdf += '     <tdwgutility:status rdf:datatype="http://www.w3.org/2001/XMLSchema#string">recommended</tdwgutility:status>\n'
            outputRdf += '     <rdfs:label xml:lang="en">{}</rdfs:label>\n'.format(row['label'])
            outputRdf += '     <skos:prefLabel xml:lang="en">{}</skos:prefLabel>\n'.format(row['prefLabel'])
            outputRdf += '     <rdfs:comment xml:lang="en">{}</rdfs:comment>\n'.format(row['comments'])
            outputRdf += '     <skos:definition xml:lang="en">{}</skos:definition>\n'.format(row['definition'])
            outputRdf += '     <rdf:value>{}</rdf:value>\n'.format(row['term_localName'])
            outputRdf += '     <skos:inScheme rdf:resource="http://rs.tdwg.org/{}/terms/"/>\n'.format(term)
            outputRdf += '     <rdf:type rdf:resource="{}"/>\n'.format(row['rdf_type'])
            outputRdf += '     <dcterms:isVersionOf rdf:resource="http://rs.tdwg.org/{}/terms/{}"/>\n'.format(term,row['term_localName'])
            outputRdf += '</rdf:Description>\n'
            text += '<table>\n'
            curie = term + ":" + row['term_localName']
            curieAnchor = curie.replace(':','_')
            text += '\t<thead>\n'
            text += '\t\t<tr>\n'
            text += '\t\t\t<th colspan="2"><a id="' + curieAnchor + '"></a>Term Name  ' + curie + '</th>\n'
            text += '\t\t</tr>\n'
            text += '\t</thead>\n'
            text += '\t<tbody>\n'
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Term IRI</td>\n'
            uri = row['term_iri']
            # uri = "http://rs.tdwg.org/bdq/bdqdim/terms/" + row['term_localName']
            text += '\t\t\t<td><a href="' + uri + '">' + uri + '</a></td>\n'
            text += '\t\t</tr>\n'
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Modified</td>\n'
            text += '\t\t\t<td>' + row['issued'] + '</td>\n'
            text += '\t\t</tr>\n'
    
            if row['iri'] != '':
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Term version IRI</td>\n'
                text += '\t\t\t<td><a href="' + row['iri'] + '">' + row['iri'] + '</a></td>\n'
                text += '\t\t</tr>\n'
    
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Label</td>\n'
            text += '\t\t\t<td>' + row['label'] + '</td>\n'
            text += '\t\t</tr>\n'
    
    #        if row['term_deprecated'] != '':
    #            text += '\t\t<tr>\n'
    #            text += '\t\t\t<td></td>\n'
    #            text += '\t\t\t<td><strong>This term is deprecated and should no longer be used.</strong></td>\n'
    #            text += '\t\t</tr>\n'
    #
    #            for dep_index,dep_row in filtered_table.iterrows():
    #                if dep_row['replaces_term'] == uri:
    #                    text += '\t\t<tr>\n'
    #                    text += '\t\t\t<td>Is replaced by</td>\n'
    #                    text += '\t\t\t<td><a href="#' + dep_row['pref_ns_prefix'] + "_" + dep_row['term_localName'] + '">' + dep_row['pref_ns_uri'] + dep_row['term_localName'] + '</a></td>\n'
    #                    text += '\t\t</tr>\n'
    #                if dep_row['replaces1_term'] == uri:
    #                    text += '\t\t<tr>\n'
    #                    text += '\t\t\t<td>Is replaced by</td>\n'
    #                    text += '\t\t\t<td><a href="#' + dep_row['pref_ns_prefix'] + "_" + dep_row['term_localName'] + '">' + dep_row['pref_ns_uri'] + dep_row['term_localName'] + '</a></td>\n'
    #                    text += '\t\t</tr>\n'
    
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Definition</td>\n'
            text += '\t\t\t<td>' + row['definition'] + '</td>\n'
            text += '\t\t</tr>\n'
    
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Comments</td>\n'
            # text += '\t\t\t<td>' + row['rdfs_comment'] + '</td>\n'
            text += '\t\t\t<td>' + row['comments'] + '</td>\n'
            #text += '\t\t\t<td>' + row['definition'] + '</td>\n'
            text += '\t\t</tr>\n'
    
    #        if row['dcterms_description'] != '':
    #        #if row['notes'] != '':
    #            text += '\t\t<tr>\n'
    #            text += '\t\t\t<td>Notes</td>\n'
    #            text += '\t\t\t<td>' + convert_link(convert_code(row['dcterms_description'])) + '</td>\n'
    #            #text += '\t\t\t<td>' + convert_link(convert_code(row['notes'])) + '</td>\n'
    #            text += '\t\t</tr>\n'
    #
    #        if row['examples'] != '':
    #        #if row['usage'] != '':
    #            text += '\t\t<tr>\n'
    #            text += '\t\t\t<td>Examples</td>\n'
    #            text += '\t\t\t<td>' + convert_examples(convert_link(convert_code(row['examples']))) + '</td>\n'
    #            #text += '\t\t\t<td>' + convert_link(convert_code(row['usage'])) + '</td>\n'
    #            text += '\t\t</tr>\n'
    #
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Status</td>\n'
            text += '\t\t\t<td>' + row['status'] + '</td>\n'
            text += '\t\t</tr>\n'

            if vocab_type == 2 or vocab_type ==3: # controlled vocabulary
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Controlled value</td>\n'
                text += '\t\t\t<td>' + row['controlled_value_string'] + '</td>\n'
                text += '\t\t</tr>\n'
    
    #        if vocab_type == 3 and row['skos_broader'] != '': # controlled vocabulary with skos:broader relationships
    #            text += '\t\t<tr>\n'
    #            text += '\t\t\t<td>Has broader concept</td>\n'
    #            curieAnchor = row['skos_broader'].replace(':','_')
    #            text += '\t\t\t<td><a href="#' + curieAnchor + '">' + row['skos_broader'] + '</a></td>\n'
    #            text += '\t\t</tr>\n'
    
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Type</td>\n'
            if row['rdf_type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property':
                text += '\t\t\t<td>rdfs:Property</td>\n'
            elif row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
                text += '\t\t\t<td>rdfs:Class</td>\n'
            elif row['rdf_type'] == 'http://www.w3.org/2004/02/skos/core#Concept':
                text += '\t\t\t<td>skos:Concept</td>\n'
            else:
                text += '\t\t\t<td>' + row['rdf_type'] + '</td>\n' # this should rarely happen
                #text += '\t\t\t<td>' + row['type'] + '</td>\n' # this should rarely happen
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
    if debug :
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
    if debug : 
        print(document_configuration_yaml)
    header = header.replace("<!--- Template for header, values provided from yaml configuration --->","")
    header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
    header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
    header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
    # Build the Markdown for the authors and contributors lists or the contributors list or the authors list
    contributors = build_authors_contributors_markdown(contributors_yaml)
    header = header.replace('{authors_contributors}', contributors)
    contributors = build_contributors_markdown(contributors_yaml)
    header = header.replace('{authors_contributors}', contributors)
    contributors = build_authors_markdown(contributors_yaml)
    header = header.replace('{authors}', contributors)
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
    header = header.replace('{term_key}', definitionTable)
    
    # Determine whether there was a previous version of the document.
    if document_configuration_yaml['doc_created'] != document_configuration_yaml['doc_modified']:
        # Load versions list from document versions data in the rs.tdwg.org repo and find most recent version.
		# TODO: This file will need to be created post ratification, it contains the columsn current_iri and version_iri
		## example from Darwin Core:
		## current_iri,version_iri
		## http://rs.tdwg.org/abcd/doc/primer/,http://rs.tdwg.org/abcd/doc/primer/2006-07-27
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
    
	## Produce a table of contents from the headings 
    toc = generate_markdown_toc((header+text+footer).splitlines())
    header = header.replace('{toc}', toc)

    warning = "<!--- This file is generated from templates by code, DO NOT EDIT by hand --->\n"
    
    output = warning + header + text + footer
    outputObject = open(outFileName, 'wt', encoding='utf-8')
    outputObject.write(output)
    outputObject.close()

    rdfOutput = outputRdfHeader + outputRdf + outputRdfFooter
    outputObject = open(outRDFFileName, 'wt', encoding='utf-8')
    outputObject.write(rdfOutput)
    outputObject.close()
    
print('done ({})'.format(__file__))

