# Shared functions reused across build scripts
# Paul J. Morris 
# 2024-10-07
# This script contains a library of reusable functions to support scripts to 
# build of documents and term lists for TDWG standards and draft standards

import rdflib     # run sparql queries on rdf 
from rdflib import Graph

# Given a string containing a markdown heading, construct markdown for a link to that heading
def markdown_heading_to_link(input_heading) :
    retval = ""
    if (input_heading and input_heading.strip().startswith("#")) : 
        headingText = input_heading.replace("#","").strip()
        headingAnchor = headingText.replace(" ","-").replace("(","").replace(")","").replace(":","").lower().replace(".","").replace(",","").replace('"','').replace("'","")[0:]
        retval = "[" + headingText.strip() + "](#" + headingAnchor + ")"
    return retval

# Function build_term_key builds a markdown table of terms and examples 
# for each term used to describe terms in a term-list document.
#
# @param term_concept_dictionary a dictionary with keys for each term 
#   and values each being a dictionary with with keys label, term, normative
#   where the term is the fully qualified term name, and normative is a 
#   string with values of 'true', 'false', or '' 
#   and optionally append, where append is a string to be appended to 
#   the end of the definitions providing local context to the definition
#   and optionally force, where if force is a string with the value 'true'
#   forces the term to appear in the output table even if not 
#   in terms_sorted_by_localname
# @param terms_sorted_by_localname a dictionary containing at least one 
#   record with entries for each term in the term_concept_dictionary
#   used to provide an example for each term.
# @return a markdown table of label, term, and metadata for each term in 
#   the term_concept_dictionary or where force=true in the 
#   term_concept_dictionary
def build_term_key(term_concept_dictionary, terms_sorted_by_localname) :
    # prefixes for sparql queries
    prefixes = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX bdqffdq: <https://rs.tdwg.org/bdqffdq/terms/>
    PREFIX bdqdim: <https://rs.tdwg.org/bdqdim/terms/>
    """
    ## Selected hard coded definitions not available for lookup.
    # Definitions drawn from the SDS Section 3.3.3.1
    # https://github.com/tdwg/vocab/blob/master/sds/documentation-specification.md#33-vocabulary-descriptions
    definition_dictionary = {
        "Term Version IRI":"The HTTP IRI that identifies the version of the term that is currently in force.",
        "Term IRI":"The HTTP IRI that uniquely identifies the current term.",
        "Term Name":"The term name is a controlled value that represents the class, property, or concept described by the term definition.",
        "term_localName":"The term name is a controlled value that represents the class, property, or concept described by the term definition.",
        "Controlled Value":"A string that is unique within a controlled vocabulary that identifies the concept in the context of a text-based metadata transfer system. The value MUST consist of Unicode characters.",
        "Modified":"The date in ISO 8601 Date format on which the most recent version of the term was issued.",
        "Decision":"The HTTP IRI representing the record of the Executive Committee decision affecting the term.",
        "Label":"A a word or short phrase that serves as a human-readable name for the term.",
        "Definition":"The normative definition of the term, written in English."
    }  
    definitionTable = ""
    definitionTable = definitionTable + "| Label (Term) | Normative | Definition | Example |\n"
    definitionTable = definitionTable + "| ------------ | --------- | ---------- | ------- |\n"
    termrow = terms_sorted_by_localname.iloc[0]
    for key, value in term_concept_dictionary.items() :
        force = False
        if 'force' in value and value['force'] :
            force = True
        if value['label'] and (key in termrow.keys() or force) : 
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
            elif termname.startswith("tdwgutility:") : 
                graph = rdflib.Graph()
                # tdwgutility rdf with definitions only delivered from the term names themselves.
                graph.parse("https://rs.tdwg.org/dwc/terms/attributes/" + termname.replace("tdwgutility:","") + ".rdf", format="xml")
                sparql = prefixes + "SELECT ?subject ?object WHERE {  ?subject skos:definition ?object . FILTER ( ?subject = "+termname+" )  } "
                queryResult = graph.query(sparql)
                for r in queryResult : 
                    definition = r.object
            elif termname.startswith("bdqffdq:") : 
                graph = rdflib.Graph()
                graph.parse("https://raw.githubusercontent.com/tdwg/bdq/refs/heads/master/tg2/_review/vocabulary/bdqffdq.owl", format="turtle")
                sparql = prefixes + "SELECT ?subject ?object WHERE {  ?subject skos:definition ?object . FILTER ( ?subject = "+termname+" )  } "
                queryResult = graph.query(sparql)
                for r in queryResult : 
                    definition = r.object
            elif termname.startswith("dcterms:") : 
                graph = rdflib.Graph()
                graph.parse("https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.rdf")
                # dcterms places the definition in the rdfs:comment
                sparql = prefixes + "SELECT ?subject ?object WHERE {  ?subject rdfs:comment ?object . FILTER ( ?subject = "+termname+" )  } "
                queryResult = graph.query(sparql)
                for r in queryResult : 
                    definition = r.object
            elif termname.startswith("owl:") : 
                graph = rdflib.Graph()
                graph.parse("https://www.w3.org/2002/07/owl")
                # owl places the definition in the rdfs:comment
                sparql = prefixes + "SELECT ?subject ?object WHERE {  ?subject rdfs:comment ?object . FILTER ( ?subject = "+termname+" )  } "
                queryResult = graph.query(sparql)
                for r in queryResult : 
                    definition = r.object
            elif termname.startswith("rdfs:") : 
                graph = rdflib.Graph()
                graph.parse("http://www.w3.org/2000/01/rdf-schema.rdf")
                # rdfs places the definition in the rdfs:comment
                sparql = prefixes + "SELECT ?subject ?object WHERE {  ?subject rdfs:comment ?object . FILTER ( ?subject = "+termname+" )  } "
                queryResult = graph.query(sparql)
                for r in queryResult : 
                    definition = r.object
            elif termname.startswith("rdf:") : 
                graph = rdflib.Graph()
                graph.parse("https://www.w3.org/1999/02/22-rdf-syntax-ns.rdf")
                # rdf places the definition in the rdfs:comment
                sparql = prefixes + "SELECT ?subject ?object WHERE {  ?subject rdfs:comment ?object . FILTER ( ?subject = "+termname+" )  } "
                queryResult = graph.query(sparql)
                for r in queryResult : 
                    definition = r.object
            if len(definition) == 0 : 
                if termname in definition_dictionary.keys() : 
                   definition = definition_dictionary.get(termname)
                elif label in definition_dictionary.keys() : 
                   definition = definition_dictionary.get(label)
            else :
                if label in definition_dictionary.keys() : 
                   definition = definition + " TDWG SDS: " + definition_dictionary.get(label)
            if 'append' in value and value['append'] :
                definition = definition + " In present context: " + value['append']

            if key in termrow.keys() : 
                example = termrow[key]
                if not example : 
                    ## first row does not contain a value, loop through to find a non-empty value
                    for row_index,row in terms_sorted_by_localname.iterrows():
                        if key in row.keys() and row[key] :
                            example = row[key]
                            break
                if example and example.find(' ')==-1 and len(example) > 20 : 
                   # long string without spaces
                   if example.startswith('https://') or example.startswith('http://') : 
                       spacedExample = example[:example.rfind("/")] + "/ " + example[example.rfind("/")+1:]
                       spacedExample = spacedExample.replace("/master/","/master/ ")
                       spacedExample = spacedExample.replace("/rs.tdwg.org/","/rs.tdwg.org/ ")
                       example = "[{}]({})".format(spacedExample,example)
                   if example.find('.') : 
                       example = example.replace(",",", ")
            else : 
                example = ""
            normative = value['normative']
            if normative == "true" :
                 normative = "normative"
            elif normative == "false" :
                 normative = "non-normative"
            definitionTable = definitionTable + "| {} ({}) | {} | {} | {} |\n".format(label,termname,normative,definition,example)
    return definitionTable

# Function build_authors_contributors_markdown builds a markdown list of authors and contributors from 
# an object expected to be loaded from an authors_configuration.yaml file.
# a template file used with this function would be expected to contain a line: 
# {authors_contributors}  
# preceded and followed by blank lines, not preceded by a line containing Contributors or preceded by ': ' 
# and code using the output of this function would be expected to 
# be used by a builder script that does a replacement in the form
# contributors = build_authors_contributors_markdown(contributors_yaml)
# header = header.replace('{authors_contributors}', contributors)
#
# @param contributors_object an object with properties contributor_iri, contributor_literal, affiliation, affiliation_uri,
#  contributor_role, role_uri where the value of contributor_role is author or contributor, empty values will result in
#  elements being omitted from the markdown. 
#
# @return a text string representing the list of authors and contributors in the form specified by section 3.2.3.1 of the
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
# Contributors
# : {contributors}  
# preceded and followed by blank lines 
# and code using the output of this function would be expected to 
# be used by a builder script that does a replacement in the form
# contributors = build_contributor_markdown(contributors_yaml)
# header = header.replace('{contributors}', contributors)
#
# @param contributors_object an object with properties contributor_iri, contributor_literal, affiliation, affiliation_uri,
#  contributor_role, role_uri where the value of contributor_role is not used in rendering the markdown list, empty values will result in
#  elements being omitted from the markdown. 
#
# @return a text string representing the list of authors and contributors in the form specified by section 3.2.3.1 of the
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
# preceded and followed by blank lines 
# and code using the output of this function would be expected to 
# be used by a builder script that does a replacement in the form
# authors = build_authors_markdown(contributors_yaml)
# header = header.replace('{authors}', contributors)
#
# @param contributors_object an object with properties contributor_iri, contributor_literal, affiliation, affiliation_uri,
#  contributor_role, role_uri where the value of contributor_role is used to determine inclusion, empty values will result in
#  elements being omitted from the markdown.  
#
# @return a text string representing the list of authors in the form specified by section 3.2.3.1 of the
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
