# Shared functions reused across build scripts
# Paul J. Morris 
# 2024-10-07
# This script contains a library of reusable functions to support scripts to 
# build of documents and term lists for tdwg standards and draft standards

import rdflib     # run sparql queries on rdf 
from rdflib import Graph

# Given a string containing a markdown heading, construct markdown for a link to that heading
def markdown_heading_to_link(input_heading) :
    retval = ""
    if (input_heading and input_heading.strip().startswith("#")) : 
        headingText = input_heading.strip().replace("#","")
        headingAnchor = headingText.replace(" ","-").replace("(","").replace(")","").replace(":","").lower().replace(".","")[1:]
        retval = "[" + headingText.strip() + "](#" + headingAnchor + ")"
    return retval

# Function build_term_key builds a markdown table of terms and examples 
# for each term used to describe terms in a term-list document.
#
# @param term_concept_dictionary a dictionary with keys for each term 
#   and values each being a dictionary with with keys label, term, normative
#   where the term is the fully qualified term name, and normative is a 
#   string with values of 'true', 'false', or '' 
# @param terms_sorted_by_locaiton a dictionary containing at least one 
#   record with entries for each term in the term_concept_dictionary
#   used to provide an example for each term.
# @return a markdown table of label, term, and metadata for each term in 
#   the term_concept_dictionary
def build_term_key(term_concept_dictionary, terms_sorted_by_localname) :
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
    definitionTable = ""
    definitionTable = definitionTable + "| Label | Term | Definition | Example | Normative | \n"
    definitionTable = definitionTable + "| ----- | ---- | ---------- | ------- | --------- |\n"
    termrow = terms_sorted_by_localname.iloc[0]
    for key, value in term_concept_dictionary.items() :
        if value['label'] and key in termrow.keys() : 
            label = value['label']
            termname = value['term']
            definition = ""
            if termname.startswith("skos:") : 
                graph = rdflib.Graph()
                graph.parse("https://www.w3.org/2009/08/skos-reference/skos.rdf", format="xml")
                sparql = prefixes + "SELECT ?subject ?object WHERE {  ?subject skos:definition ?object . FILTER ( ?subject = "+termname+" )  } "
                queryResult = graph.query(sparql)
                for r in queryResult : 
                    definition = r.object
            example = termrow[key]
            normative = value['normative']
            if normative == "true" :
                 normative = "normative"
            elif normative == "false" :
                 normative = "non-normative"
            definitionTable = definitionTable + "| {} | {} | {} | {} | {} |\n".format(label,termname,definition,example,normative)
    return definitionTable

# Function build_authors_contributors_markdown builds a markdown list of authors and contributors from 
# an object expected to be loaded from an authors_configuration.yaml file.
# a template file used with this function would be expected to contain a line: 
# {authors_contributors}  
# preceeded and followed by blank lines, not preceeded by a line containing Contributors or preceded by ': ' 
# and code using the output of this function would be expected to 
# be used by a builder script that does a replacement in the form
# contributors = build_authors_contributors_markdown(contributors_yaml)
# header = header.replace('{authors_contributors}', contributors)
#
# @param contributors_object an object with properties contributor_ird, contributor_literal, affiliation, affilitation_uri,
#  contributor_role, role_uri where the value of contributor_role is author or contributor, empty values will result in
#  elements being omitted from the markdown. 
#
# @return a text string representing the list of authors and contributors in the form specfied by section 3.2.3.1 of the
#  standards documentation section, that is [contributor_literal](contributor_iri) ([affiliation](affiliation_uri)), but
#  providing separate lists for authors and contributors following the semantics of role_uri, with these lists
#  being rendered as separate (Authors\n: authors and Contributors\n: contributors) markdown definition list lists: 
#
# @see build_contributors_markdown(contributors_object)
# @see build_authors_markdown(contributors_object)
def build_authors_contributors_markdown(contributors_object) : 

    # Build the Markdown for the authors and contributors lists
    authors = ''
    contributors = ''
    auth_separator = ''
    cont_separator = ''
    for contributor in contributors_object :
        if contributor['contributor_role'] == 'author' :
            if contributor['contributor_iri'] :
                authors += auth_separator + '[' + contributor['contributor_literal'] + '](' + contributor['contributor_iri'] + ') '
            else : 
                authors += auth_separator + contributor['contributor_literal'] + ' '
            if contributor['affiliation'] :
                if contributor['affiliation_uri'] :
                    authors += '([' + contributor['affiliation'] + '](' + contributor['affiliation_uri'] + '))'
                else :
                    authors += '(' + contributor['affiliation'] + ')'
            auth_separator = ", "
        else : 
            if contributor['contributor_iri'] :
                contributors += cont_separator + '[' + contributor['contributor_literal'] + '](' + contributor['contributor_iri'] + ') '
            else : 
                contributors += cont_separator + contributor['contributor_literal'] + ' '
            if contributor['affiliation'] :
                if contributor['affiliation_uri'] :
                    contributors += '([' + contributor['affiliation'] + '](' + contributor['affiliation_uri'] + '))'
                else :
                    contributors += '(' + contributor['affiliation'] + ')'
            cont_separator = ", "
    if len(authors) > 0 : 
       authors = "Authors\n: {}\n".format(authors)
    if len(contributors) > 0 : 
       contributors = "Contributors\n: {}\n".format(contributors)
    if len(authors) > 0 and len(contributors) > 0 : 
        result = "{}\n{}".format(authors,contributors)
    else :
        result = "{}{}".format(authors,contributors)
    return result    

# Function build_contributors_markdown builds a markdown list of contributors from 
# an object expected to be loaded from an authors_configuration.yaml file.
# a template file used with this function would be expected to contain the lines (
# in the form of a markdown definition list): 
# Contibutors
# : {contributors}  
# preceeded and followed by blank lines 
# and code using the output of this function would be expected to 
# be used by a builder script that does a replacement in the form
# contributors = build_contributor_markdown(contributors_yaml)
# header = header.replace('{contributors}', contributors)
#
# @param contributors_object an object with properties contributor_ird, contributor_literal, affiliation, affilitation_uri,
#  contributor_role, role_uri where the value of contributor_role is not used in rendering the markdown list, empty values will result in
#  elements being omitted from the markdown. 
#
# @return a text string representing the list of authors and contributors in the form specfied by section 3.2.3.1 of the
#  standards documentation section, that is [contributor_literal](contributor_iri) ([affiliation](affiliation_uri)).
# 
# @see build_authors_contributors_markdown(contributors_object)
# @see build_authors_markdown(contributors_object)
def build_contributors_markdown(contributors_object) : 

    # Build the Markdown for the contributors list
    contributors = ''
    separator = ''
    for contributor in contributors_object :
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
    return contributors    

# Function build_authors_markdown builds a markdown list of authors excluding
# contributors, where authors are identified by contributor_role=author, from 
# an object expected to be loaded from an authors_configuration.yaml file.
# a template file used with this function would be expected to contain the lines (
# in the form of a markdown definition list): 
# Authors
# : {authors}  
# preceeded and followed by blank lines 
# and code using the output of this function would be expected to 
# be used by a builder script that does a replacement in the form
# authors = build_authors_markdown(contributors_yaml)
# header = header.replace('{authors}', contributors)
#
# @param contributors_object an object with properties contributor_iri, contributor_literal, affiliation, affilitation_uri,
#  contributor_role, role_uri where the value of contributor_role is used to determine inclusion, empty values will result in
#  elements being omitted from the markdown.  
#
# @return a text string representing the list of authors in the form specfied by section 3.2.3.1 of the
#  standards documentation section, that is [contributor_literal](contributor_iri) ([affiliation](affiliation_uri))
#  limited to entries in contributor_yaml where the contributor_role = author.
# 
# @see build_authors_contributors_markdown(contributors_object)
# @see build_contributors_markdown(contributors_object)
def build_authors_markdown(contributors_object) : 

    # Build the Markdown for the contributors list
    contributors = ''
    separator = ''
    for contributor in contributors_object :
        if contributor['contributor_role'] == 'author' : 
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
    return contributors    

# ---------------
# Function definitions (drawn from dwc build)
# Steve Baskauf 2020-08-12 CC0
# updated 2021-02-11
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
