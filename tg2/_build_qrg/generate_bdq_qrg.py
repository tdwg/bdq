# Python script to generate the Quick Reference Guide HTML (custom order with separators)
# Usage: python generate_bdq_qrg.py

import pandas as pd
import os
import re

CSV_PATH = '../_review/vocabulary/bdqtest_term_versions.csv'
OUTPUT_PATH = '../_review/docs/terms/bdqtest/index.html'
DEPLOY_PATH = '../../terms/bdqtest/index.html'

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BDQ Tests and Assertions - Quick Reference Guide</title>
    <style>
        html, body {{ margin: 0; padding: 0; font-family: Arial, sans-serif; line-height: 1.5; overflow-x: hidden; }}
        body {{ display: flex; }}
        main {{ flex: 1; padding: 20px; max-width: calc(100% - 260px); margin-right: 240px; }}
        aside.nav-menu {{
          position: fixed;
          top: 0;
          right: 0;
          height: 100vh;
          overflow-y: auto;
          background: #fafafa;
          border-left: 1px solid #ccc;
          width: 240px;
          padding: 20px;
          box-sizing: border-box;
        }}
        h1, h2 {{ border-bottom: 1px solid #ccc; }}
        .intro {{ margin: 20px 0; }}
        nav.class-index a.class-box {{
            display: inline-block; margin: 2px; padding: 4px 8px;
            border: 1px solid #8da7b5; border-radius: 4px; background: #f1f6f9;
            color: #003c71; text-decoration: none; font-size: 0.9em;
        }}
        nav.class-index a.class-box:hover {{ background: #e1ecf4; }}
        .menu-separator {{ border-top: 1px solid #ccc; margin: 10px 0; }}
        .term-section {{ border-top: 1px solid #ddd; padding-top: 12px; margin-top: 12px; }}
        .field-header-wrapper {{
            width: 100vw;
            position: relative;
            left: -20px;
            background: #cdd8de;
            padding: 4px 20px;
            box-sizing: border-box;
        }}
        .field-header-wrapper h3 {{
            margin: 0;
            font-size: 1em;
            color: #003c71;
        }}
        .class-header-wrapper {{ 
            width: 100vw;
            position: relative;
            left: -20px;
            background: #dfe5d8;
            padding: 8px 20px;
            box-sizing: border-box;
            margin-bottom: 8px;
            border-bottom: 1px solid #ccc; 
            border-top: 1px solid #ccc; 
        }}
        .class-header-wrapper h2 {{
            margin: 0;
            font-size: 1.1em;
            color: #003c71;
            border-bottom: none;
        }}
        nav.field-index a.field-box {{
            display: inline-block;
            margin: 5px;
            padding: 5px 10px;
            border: 1px solid #8da7b5;
            border-radius: 4px;
            background: #f1f6f9;
            color: #003c71;
            text-decoration: none;
            font-size: 0.75em;
        }}
        nav.field-index a.field-box:hover {{
            background: #e1ecf4;
        }}
        table.term-table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
        table.term-table td {{ vertical-align: top; padding: 4px; border-top: 1px solid #ccc; }}
        table.term-table td.label {{ width: 25%; font-weight: bold; color: #003c71; }}
    </style>
</head>
<body>
    <main>
        <h1 id="top">BDQ Tests Quick Reference Guide</h1>
            <div class="intro">
              <p><strong>Draft Standard for Review</strong></p>
              <p>This document is intended to be an easy-to-read reference for the Tests maintained as part of the TDWG standard <a href="http://example.org/to_be_determined">BDQ</a> produced by the TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions and is maintained by the BDQ Maintenance Interest Group. This document lists the BDQ Tests, described by the <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/terms/bdqtest/bdqtest_qrg_term_descriptions.md">Terms Used in the BDQ Tests Quick Reference Guide</a>. Definitions, comments, and examples may include namespace abbreviations (e.g., <code>bdq:</code>, <code>dwc:</code>). These are required as the meaning for the word is defined specifically in that namespace. Thus, `dwc:Event` means Event as defined by Darwin Core at <a href="https://dwc.tdwg.org/terms/#event">https://dwc.tdwg.org/terms/#event</a>.</p>
              <p>This page is a non-normative descriptive document, not the <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md">full vocabulary definition document</a> for `bdqtest:` terms. It combines the normative Test names and terms with non-normative comments and examples that are meant to help people to use the Tests consistently. Further details can be found in <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md">The Biodiversity Data Quality (BDQ) Standard</a>, the <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/guide/bdqffdq/index.md">Fitness For Use Framework Ontology Guide</a>, and the <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/guide/implementers/index.md">BDQ Implementer's Guide</a>.</p>
              <p>If you have questions or suggestions, submit these to the <a href="https://github.com/tdwg/bdq/issues">BDQ Issues</a> page in GitHub. See the bottom of this document for how to cite the BDQ standard and this document in particular.</p>
            </div>
        {content}
    </main>
    <aside class="nav-menu">
        <a href="#top"><strong>&uarr; Back to Top</strong></a>
        <h3>Test Types</h3>
        <nav class="class-index">
            {class_links}
        </nav>
    </aside>
</body>
</html>'''

def linkify_urls(text):
    url_pattern = r'(https?://\S+)'  # matches URLs up to a space or end
    return re.sub(url_pattern, r'<a href="\1">\1</a>', text)

def build_term_section(term, columns):
    term_id = term.get('term_localName', term.get('Label', 'term')).strip().replace(' ', '_')
    label = term.get('Label', 'Unnamed Term')
    rows = ''
    for col in columns:
        value = str(term.get(col, '')).strip()
        if not value or value.lower() == 'nan':
            continue
        if col not in ['term_iri', 'iri']:
            value = linkify_urls(value)
        ## not all column headers use the labels shown in the QRG key, so we need to map them
        # important two for inteligibility are:
        # prefLabel -> Preferred Label
        # iri -> Term Version IRI
        termLabel = col
        if termLabel == 'iri':
           termLabel = 'Term Version IRI'
        if termLabel == 'prefLabel':
           termLabel = 'Preferred Label'
        if termLabel == 'ExpectedResponse':
           termLabel = 'Expected Response'
        if termLabel == 'AuthoritiesDefaults':
           termLabel = 'Source Authorities/Defaults'
        if termLabel == 'InformationElement:ActedUpon':
           termLabel = 'Information Elements Acted Upon'
        if termLabel == 'InformationElement:Consulted':
           termLabel = 'Information Elements Consulted'
        rows += f'<tr><td class="termLabel">{termLabel}</td><td>{value}</td></tr>'
    return f'<section class="term-section" id="{term_id}">\n<div class="field-header-wrapper"><h3>{label}</h3></div>\n<table class="term-table">{rows}</table>\n</section>'

def build_field_index(terms):
    links = []
    for term in terms:
        term_id = term.get('term_localName', term.get('Label', 'term')).strip().replace(' ', '_')
        label = term.get('Label', 'Unnamed Term')
        links.append(f'<a class="field-box" href="#{term_id}">{label}</a>')
    return f'<nav class="field-index">' + ''.join(links) + '</nav>'

def generate_qrg():
    print(f"Loading CSV from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH)
    df = df.astype(str).fillna('')

    if 'organized_in' not in df.columns:
        raise ValueError("Missing 'organized_in' column in source CSV.")

    columns = [col for col in df.columns if col.strip() and col != 'organized_in']
    # filter columns to one of quick reference guide key terms: Label, Preferred Label, Term Version IRI,Description, Expected Response, InformationElements ActedUpon, InformationElements Consulted, Parameters,SourceAuthorities/Defaults, Notes, Examples, Type.
    # "Label","issueNumber","historyNoteUrl","iri","term_iri","issued","term_localName","DateLastUpdated","prefLabel","IE Class","InformationElement:ActedUpon","InformationElement:Consulted","Parameters","ExpectedResponse","SpecificationGuid","MethodGuid","AuthoritiesDefaults","Description","Type","Resource Type","Dimension","Criterion","Enhancement","Examples","Source","References","Example Implementations (Mechanisms)","Link to Specification Source Code","Notes","IssueState","IssueLabels","UseCases","ArgumentGuids","status","flags","organized_in"
    columns = [col for col in columns if col in ['Label', 'prefLabel', 'iri', 'Description', 'ExpectedResponse', 'InformationElement:ActedUpon', 'InformationElement:Consulted', 'Parameters', 'AuthoritiesDefaults', 'Notes', 'Examples', 'Type', 'UseCases','Resource Type']]
    ordered_classes = ['Validation', 'Issue', 'Measure', 'Amendment']
    grouped = dict(tuple(df.groupby('organized_in')))
    grouped = {cls: grouped[cls] for cls in ordered_classes if cls in grouped}

    content = ''
    class_links = ''

    for group, terms in grouped.items():
        anchor = group.strip().replace(' ', '_')
        content += f'<div class="class-header-wrapper"><h2 id="{anchor}" class="class-header">{group}</h2></div>'
        content += build_field_index(terms.to_dict(orient='records'))

        class_links += f'<a class="class-box" href="#{anchor}">{group}</a>\n'
        for _, row in terms.iterrows():
            content += build_term_section(row, columns)

        class_links += '<div class="menu-separator"></div>\n'

    html = TEMPLATE.format(content=content, class_links=class_links)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"QRG successfully written to {OUTPUT_PATH}")
    with open(DEPLOY_PATH, 'w', encoding='utf-8') as f1:
        f1.write(html)
    print(f"QRG successfully written to {DEPLOY_PATH}")

if __name__ == '__main__':
    generate_qrg()
