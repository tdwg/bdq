# Script to build Markdown pages that are largely human readable text, filling in values from configuration files
#
# Modified from script by
# Steve Baskauf 2020-08-12 CC0
# updated 2021-02-11
# Modified Paul J. Morris for generating draft standard documents without rs.tdwg.org files
# 2024-09-12
# This script merges static Markdown header and footer documents with generated term information tables loading data from in local csv and yaml files.
# Unlike the original, this version is intended to run entirely on local files.

import re         # regular expressions
import csv        # library to read/write/parse CSV files
import json       # library to convert JSON to Python data structures
import pandas as pd  # library to handle data loaded from csv as data frames
import yaml       # Library to parse yaml files
# To copy image files from build/templates/ to /docs/
import glob
import shutil

# -----------------
# Configuration section
# -----------------

# This is a Python dictionary of the folders and files to be processed for templates to turn into documents.
# See assumptions below.
# directories, list of key:value pairs of templatePath:document
directories = {'toplevel/vocabularies':'vocabularies', 'toplevel/intro/':'intro', 'toplevel/supplement':'supplement', 'toplevel/synthetic':'synthetic'}

# This is the base URL for raw files from the branch of the repo that has been pushed to GitHub
github_branch = 'master' # "master" for production, something else for development
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/bdq/' + github_branch + '/tg2/core/generation/'

# ----------------
# Assumptions 
# ---------------
# (1) The repository has build/ docs/ dist/ and vocabulary/ directories in the same parent directory.
# (2) This file is located in a build/ directory
# (3) This file produces human readable documents in the docs/ directory within docs/{document} directories.
# (6) A list of authors/contributors is in the build/ directory in: 
contributors_yaml_file = 'authors_configuration.yaml'
# (7) local replacements for metadata namespaces and term-lists.csv files 
# are in the build/ directory in the following files, which provide metadata for each term in the standard 
term_list_document = "temp_term-lists.csv"
local_metadata_config_file = 'temp_namespaces.yaml'
# (8) {term}_termlist-header.md, {term}_termlist-footer.md files are in build/templates/{directory}/ along with a document_configuration.yaml file
# see loop below through termLists
# headerFileName = 'templates/{}/{}_termlist-header.md'.format(directory,document)
# footerFileName = 'templates/{}/{}_termlist-footer.md'.format(directory,document)
# document_configuration_yaml_file = 'templates/{}/document_configuration.yaml'.format(directory)

has_namespace = False

# ---------------
# Load header data
# ---------------

# Load the contributors YAML file from its local location.
with open(contributors_yaml_file) as cyf:
    contributors_yaml = yaml.load(cyf, Loader=yaml.FullLoader)

# ---------------
# Function definitions
# ---------------

# replace URL with link (function used with Audubon Core list of terms build script)
# Does not correctly handle URLs with close parens ) characters, so no longer used.
#
def createLinks(text):
    def repl(match):
        if match.group(1)[-1] == '.':
            return '<a href="' + match.group(1)[:-1] + '">' + match.group(1)[:-1] + '</a>.'
        return '<a href="' + match.group(1) + '">' + match.group(1) + '</a>'

    pattern = '(https?://[^\s,;\)"<]*)'
    result = re.sub(pattern, repl, text)
    return result

# 2021-08-06 Replace the createLinks() function with functions copied from the QRG build script written by S. Van Hoey
def convert_code(text_with_backticks):
    """Takes all back-quoted sections in a text field and converts it to
    the html tagged version of code blocks <code>...</code>
    """
    return re.sub(r'`([^`]*)`', r'<code>\1</code>', text_with_backticks)

def convert_link(text_with_urls):
    """Takes all links in a text field and converts it to the html tagged
    version of the link
    """
    def _handle_matched(inputstring):
        """quick hack version of url handling on the current prime versions data"""
        url = inputstring.group()
        return "<a href=\"{}\">{}</a>".format(url, url)

    regx = "(http[s]?://[\w\d:#@%/;$()~_?\+-;=\\\.&]*)(?<![\)\.,])"
    return re.sub(regx, _handle_matched, text_with_urls)

# Hack the code taken from the terms.tmpl template to insert the HTML necessary to make the semicolon-separated
# lists of examples into an HTML list.
# {% set examples = term.examples.split("; ") %}
# {% if examples | length == 1 %}{{ examples | first }}{% else %}<ul class="list-group list-group-flush">{% for example in examples %}<li class="list-group-item">{{ example }}</li>{% endfor %}</ul>{% endif %}
def convert_examples(text_with_list_of_examples: str) -> str:
    examples_list = text_with_list_of_examples.split('; ')
    if len(examples_list) == 1:
        return examples_list[0]
    else:
        output = '<ul class="list-group list-group-flush">\n'
        for example in examples_list:
            output += '  <li class="list-group-item">' + example + '</li>\n'
        output += '</ul>'
        return output

# ---------------
# Retrieve term list metadata from GitHub
# ---------------

## PJM: Unavailable for draft without rs.tdwg.org files
print('Loading term list metadata')
term_lists_info = []


#print(term_list_document)
##frame = pd.read_csv(githubBaseUri + term_list_document, na_filter=False)
#frame = pd.read_csv(term_list_document, na_filter=False)
#for termList in termLists:
#    term_list_dict = {'list_iri': termList}
#    term_list_dict = {'database': termList}
#    for index,row in frame.iterrows():
#        if row['database'] == termList:
#            term_list_dict['pref_ns_prefix'] = row['vann_preferredNamespacePrefix']
#            term_list_dict['pref_ns_uri'] = row['vann_preferredNamespaceUri']
#            term_list_dict['list_iri'] = row['list']
#    term_lists_info.append(term_list_dict)
#print(term_lists_info)
#print()

#############
## Process each document in directories dictionary
############
for templatePath, document in directories.items() :
    print('Filling in header and footer template and saving file')
    print('Generating files for {}.'.format(document))
    sourceDirectory = 'templates/{}/'.format(templatePath)
    headerFileName = '{}{}-header.md'.format(sourceDirectory,document)
    footerFileName = '{}{}-footer.md'.format(sourceDirectory,document)
    document_configuration_yaml_file = 'templates/{}/document_configuration.yaml'.format(templatePath)
    outputDirectory = '../docs/{}/'.format(document)
    outFileName = '{}index.md'.format(outputDirectory)

    # Load the document configuration YAML file from its local location.  For a draft standard, database is not available from rs.tdwg.org
    # load from local file
    with open(document_configuration_yaml_file) as dcfy:
        document_configuration_yaml = yaml.load(dcfy, Loader=yaml.FullLoader)

    ## Produce a table of contents from the headings 
    toc = ""
    regexHeadings = "^#+ [0-9]+.*"
    with open(headerFileName) as headerFile:
        for line in headerFile:
           aHeading = re.search(regexHeadings,line)
           if (aHeading) : 
               headingText = aHeading.group().replace("#","")
               headingAnchor = headingText.replace(" ","-").lower().replace(".","")[1:]
               toc = toc + "- [" + aHeading.group().replace("#","") + "](#" + headingAnchor + ")\n"
        headerFile.close()
    
    # read in header and footer, merge with terms table, and output
    headerObject = open(headerFileName, 'rt', encoding='utf-8')
    header = headerObject.read()
    headerObject.close()
    
    text = ""

    # Build the Markdown for the contributors list
    contributors = ''
    separator = ''
    for contributor in contributors_yaml:
        if contributor['contributor_iri'] :
            contributors += separator + '[' + contributor['contributor_literal'] + '](' + contributor['contributor_iri'] + ') '
        else : 
            contributors += separator + contributor['contributor_literal'] + ' '
        if contributor['affiliation'] :
            if contributor['affiliation_uri'] :
                contributors += '([' + contributor['affiliation'] + '](' + contributor['affiliation_uri'] + '))'
            else :
                contributors += '(' + contributor['affiliation'] + ')'
        separator = ", "
    
    # Substitute values of ratification_date and contributors into the header template
    print(document_configuration_yaml)
    header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
    header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
    header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
    header = header.replace('{contributors}', contributors)
    header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
    header = header.replace('{current_iri}', document_configuration_yaml['current_iri'])
    header = header.replace('{abstract}', document_configuration_yaml['abstract'])
    header = header.replace('{creator}', document_configuration_yaml['creator'])
    header = header.replace('{publisher}', document_configuration_yaml['publisher'])
    header = header.replace('{comment}', document_configuration_yaml['comment'])
    header = header.replace('{toc}','\n{}\n'.format(toc))
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
    
    output = warning + header + text + footer
    outputObject = open(outFileName, 'wt', encoding='utf-8')
    outputObject.write(output)
    outputObject.close()

    # Find image files to copy from templates and copy them over to docs
    for file in glob.glob('{}*.svg'.format(sourceDirectory)):
       print(file)
       shutil.copy(file, outputDirectory)
    for file in glob.glob('{}*.png'.format(sourceDirectory)):
       print(file)
       shutil.copy(file, outputDirectory)

print('done')

