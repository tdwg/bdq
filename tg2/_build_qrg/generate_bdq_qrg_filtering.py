# Python script to generate the Quick Reference Guide HTML
# (interactive sidebar: external navigation + on-the-fly filters)
# Usage: python generate_bdq_qrg_filtering.py
#
# @author tucotuco John Wieczorek
# @author chicoreus Paul J. Morris
# @author Claude 4.6 Sonnet
#
# Rewritten from generate_bdq_qrg.py to add interactive filtering and category sections by Claude 4.6 Sonnet

import pandas as pd
import os
import re
import html as html_lib

CSV_PATH = '../_review/vocabulary/bdqtest_term_versions.csv'
OUTPUT_PATH = '../_review/docs/terms/bdqtest/index.html'
DEPLOY_PATH = '../../terms/bdqtest/index.html'

# Template uses ###NAME### markers so CSS/JS curly-braces need no escaping.
TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BDQ Tests and Assertions - Quick Reference Guide</title>
    <style>
        html, body {
            margin: 0; padding: 0;
            font-family: Arial, sans-serif; line-height: 1.5; overflow-x: hidden;
        }
        body { display: flex; }
        main {
            flex: 1; padding: 20px;
            max-width: calc(100% - 260px); margin-right: 240px;
        }

        /* ── Sidebar ─────────────────────────────────────────── */
        aside.nav-menu {
            position: fixed; top: 0; right: 0;
            height: 100vh; overflow-y: auto;
            background: #fafafa; border-left: 1px solid #ccc;
            width: 240px; padding: 14px; box-sizing: border-box;
        }
        aside.nav-menu h2 {
            font-size: 0.95em; margin: 14px 0 6px 0;
            padding-bottom: 4px; border-bottom: 1px solid #ccc;
            color: #003c71;
        }
        aside.nav-menu h2:first-child { margin-top: 0; }

        .sidebar-context-links { list-style: none; padding: 0; margin: 0 0 4px 0; }
        .sidebar-context-links li { margin: 5px 0; }
        .sidebar-context-links a {
            color: #003c71; text-decoration: none; font-size: 0.82em;
        }
        .sidebar-context-links a:hover { text-decoration: underline; }

        .menu-separator { border-top: 1px solid #ccc; margin: 10px 0; }

        /* Jump links */
        .jump-links { margin: 0 0 10px 0; }
        .jump-section-label {
            display: block; font-size: 0.75em; font-weight: bold;
            color: #555; margin: 6px 0 2px 0;
        }
        .jump-link {
            display: inline-block; font-size: 0.8em; color: #003c71;
            text-decoration: none; margin: 2px 2px 2px 0;
            padding: 2px 6px; border: 1px solid #8da7b5;
            border-radius: 3px; background: #f1f6f9;
        }
        .jump-link:hover { background: #e1ecf4; }

        /* Filter panel */
        .filters-active-msg {
            display: none; font-size: 0.75em;
            background: #fff3cd; border: 1px solid #ffc107;
            border-radius: 3px; padding: 2px 6px; color: #856404;
            margin-bottom: 8px;
        }
        .filter-group { margin-bottom: 10px; }
        .filter-label {
            display: block; font-weight: bold;
            font-size: 0.8em; color: #333; margin-bottom: 3px;
        }
        #type-filters label {
            display: block; font-size: 0.8em; margin: 3px 0; cursor: pointer;
        }
        #type-filters input { margin-right: 4px; cursor: pointer; }
        .filter-select {
            width: 100%; font-size: 0.79em; padding: 3px 4px;
            border: 1px solid #bbb; border-radius: 3px; box-sizing: border-box;
        }
        #clear-filters {
            font-size: 0.8em; padding: 4px 10px;
            background: #003c71; color: white;
            border: none; border-radius: 3px; cursor: pointer; margin-top: 6px;
        }
        #clear-filters:hover:not(:disabled) { background: #005a9e; }
        #clear-filters:disabled { background: #aaa; cursor: default; }
        #filter-count {
            font-size: 0.76em; color: #555;
            display: block; margin-top: 5px; font-style: italic;
        }

        /* ── Main content ─────────────────────────────────────── */
        h1, h2 { border-bottom: 1px solid #ccc; }
        .intro { margin: 20px 0; }

        .category-section { margin-bottom: 8px; }
        .class-wrapper {}

        .field-header-wrapper {
            width: 100vw; position: relative; left: -20px;
            background: #cdd8de; padding: 4px 20px; box-sizing: border-box;
        }
        .field-header-wrapper h3 { margin: 0; font-size: 1em; color: #003c71; }

        .class-header-wrapper {
            width: 100vw; position: relative; left: -20px;
            background: #dfe5d8; padding: 8px 20px; box-sizing: border-box;
            margin-bottom: 8px;
            border-bottom: 1px solid #ccc; border-top: 1px solid #ccc;
        }
        .class-header-wrapper h2 {
            margin: 0; font-size: 1.1em; color: #003c71; border-bottom: none;
        }

        nav.field-index a.field-box {
            display: inline-block; margin: 5px; padding: 5px 10px;
            border: 1px solid #8da7b5; border-radius: 4px;
            background: #f1f6f9; color: #003c71;
            text-decoration: none; font-size: 0.75em;
        }
        nav.field-index a.field-box:hover { background: #e1ecf4; }

        .term-section { border-top: 1px solid #ddd; padding-top: 12px; margin-top: 12px; }

        table.term-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        table.term-table td {
            vertical-align: top; padding: 4px; border-top: 1px solid #ccc;
        }
        table.term-table td.label { width: 25%; font-weight: bold; color: #003c71; }

        .no-results-msg {
            display: none; padding: 16px 20px; color: #666; font-style: italic;
            border: 1px dashed #ccc; border-radius: 4px; margin: 20px 0;
        }
    </style>
</head>
<body>

<main>
    <h1 id="top">BDQ Tests Quick Reference Guide</h1>
    <div class="intro">
      <p><strong>Draft Standard for Review</strong></p>
      <p>This document is intended to be an easy-to-read reference for the Tests maintained as part
      of the TDWG standard <a href="http://example.org/to_be_determined">BDQ</a> produced by the
      TDWG Biodiversity Data Quality Interest Group Task Group 2: Data Quality Tests and Assertions
      and is maintained by the BDQ Maintenance Interest Group. This document lists the BDQ Tests,
      described by the <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/terms/bdqtest/bdqtest_qrg_term_descriptions.md">Terms
      Used in the BDQ Tests Quick Reference Guide</a>. Definitions, comments, and examples may
      include namespace abbreviations (e.g., <code>bdqval:</code>, <code>dwc:</code>). These are
      required as the meaning for the word is defined specifically in that namespace. Thus,
      <code>dwc:Event</code> means Event as defined by Darwin Core at
      <a href="https://dwc.tdwg.org/terms/#event">https://dwc.tdwg.org/terms/#event</a>.</p>
      <p>This page is a non-normative descriptive document, not the
      <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md">full
      vocabulary definition document</a> for <code>bdqtest:</code> terms. It combines the normative
      Test names and terms with non-normative comments and examples that are meant to help people to
      use the Tests consistently. Further details can be found in
      <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md">The Biodiversity Data
      Quality (BDQ) Standard</a>, the
      <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/guide/bdqffdq/index.md">Fitness
      For Use Framework Ontology Guide</a>, and the
      <a href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/guide/implementers/index.md">BDQ
      Implementer&#8217;s Guide</a>.</p>
      <p>If you have questions or suggestions, submit these to the
      <a href="https://github.com/tdwg/bdq/issues">BDQ Issues</a> page in GitHub. See the bottom
      of this document for how to cite the BDQ standard and this document in particular.</p>
    </div>

    <div id="no-results-msg" class="no-results-msg">
        No tests match the current filters.
        <a href="#" onclick="clearFilters(); return false;">Clear filters</a> to see all tests.
    </div>

    ###CONTENT###
</main>

<aside class="nav-menu">

    <h2>BDQ Standard</h2>
    <ul class="sidebar-context-links">
        <li>&uarr; <a href="#top"><strong>Back to top</strong></a></li>
        <li><a href="https://bdq.tdwg.org/draft/">&#127968; Landing page</a></li>
        <li><a href="https://bdq.tdwg.org/draft/#2-A-Roadmap-to-the-BDQ-Standard-non-normative">&#129517; Roadmap to the Standard</a></li>
        <li><a href="https://bdq.tdwg.org/draft/README.html">&#128203; Public Review</a></li>
    </ul>

    <div class="menu-separator"></div>

    <h2>On this Page</h2>

    <div class="jump-links">
        <span class="jump-section-label">By Category:</span>
        ###CATEGORY_LINKS###
        <span class="jump-section-label">By Test Type:</span>
        <a class="jump-link" href="#Amendment">Amendment</a><a
        class="jump-link" href="#Issue">Issue</a><a
        class="jump-link" href="#Measure">Measure</a><a
        class="jump-link" href="#Validation">Validation</a>
    </div>

    <div class="filters-active-msg" id="filters-active-msg">&#9888; Filters active</div>

    <div class="filter-group">
        <span class="filter-label">Filter by Test Type</span>
        <div id="type-filters">
            <label><input type="checkbox" name="type" value="Amendment"  onchange="applyFilters()"> Amendment</label>
            <label><input type="checkbox" name="type" value="Issue"      onchange="applyFilters()"> Issue</label>
            <label><input type="checkbox" name="type" value="Measure"    onchange="applyFilters()"> Measure</label>
            <label><input type="checkbox" name="type" value="Validation" onchange="applyFilters()"> Validation</label>
        </div>
    </div>

    <div class="filter-group">
        <label class="filter-label" for="usecase-filter">Filter by Use Case</label>
        <select id="usecase-filter" class="filter-select" onchange="applyFilters()">
            <option value="">All Use Cases</option>
            ###USECASE_OPTIONS###
        </select>
    </div>

    <div class="filter-group">
        <label class="filter-label" for="ie-filter">Filter by Information Element Acted Upon</label>
        <select id="ie-filter" class="filter-select" onchange="applyFilters()">
            <option value="">All Information Elements</option>
            ###IE_OPTIONS###
        </select>
    </div>

    <button id="clear-filters" onclick="clearFilters()" disabled>Clear Filters</button>
    <span id="filter-count"></span>

</aside>

<script>
(function () {
    'use strict';

    var totalCount = document.querySelectorAll('.term-section').length;
    document.getElementById('filter-count').textContent = totalCount + ' tests total';

    /**
     * Returns true when filterValue is empty (no filter active) OR when it
     * matches one of the pipe-separated tokens in dataValue exactly.
     */
    function matchesList(dataValue, filterValue) {
        if (!filterValue) return true;
        if (!dataValue)   return false;
        var parts = dataValue.split('|');
        for (var i = 0; i < parts.length; i++) {
            if (parts[i].trim() === filterValue.trim()) return true;
        }
        return false;
    }

    window.applyFilters = function () {

        /* ── Collect active filter values ── */
        var checkedBoxes  = document.querySelectorAll('#type-filters input:checked');
        var selectedTypes = Array.from(checkedBoxes).map(function (cb) { return cb.value; });
        var selectedUC    = document.getElementById('usecase-filter').value;
        var selectedIE    = document.getElementById('ie-filter').value;
        var anyActive     = selectedTypes.length > 0 || !!selectedUC || !!selectedIE;

        /* ── Update sidebar indicators ── */
        document.getElementById('clear-filters').disabled = !anyActive;
        document.getElementById('filters-active-msg').style.display = anyActive ? 'block' : 'none';

        /* ── Hide topic-category nav sections while a filter is active ── */
        document.querySelectorAll('.category-section').forEach(function (el) {
            el.style.display = anyActive ? 'none' : '';
        });

        /* ── Show / hide individual term sections ── */
        var visibleCount = 0;
        document.querySelectorAll('.term-section').forEach(function (sec) {
            var show = true;

            if (selectedTypes.length > 0 &&
                    selectedTypes.indexOf(sec.dataset.type) === -1) {
                show = false;
            }
            if (show && !matchesList(sec.dataset.usecases, selectedUC)) show = false;
            if (show && !matchesList(sec.dataset.ie,       selectedIE)) show = false;

            sec.style.display = show ? '' : 'none';
            if (show) visibleCount++;
        });

        /* ── Show / hide class wrappers; sync their quick-nav links ── */
        document.querySelectorAll('.class-wrapper').forEach(function (wrapper) {
            var terms      = Array.from(wrapper.querySelectorAll('.term-section'));
            var anyVisible = terms.some(function (s) { return s.style.display !== 'none'; });
            wrapper.style.display = anyVisible ? '' : 'none';

            /* Hide field-box links whose target term is now hidden */
            wrapper.querySelectorAll('a.field-box[data-target]').forEach(function (link) {
                var target = document.getElementById(link.dataset.target);
                link.style.display = (target && target.style.display !== 'none') ? '' : 'none';
            });
        });

        /* ── No-results message ── */
        document.getElementById('no-results-msg').style.display =
            (anyActive && visibleCount === 0) ? 'block' : 'none';

        /* ── Count line ── */
        document.getElementById('filter-count').textContent = anyActive
            ? 'Showing ' + visibleCount + ' of ' + totalCount + ' tests'
            : totalCount + ' tests total';
    };

    window.clearFilters = function () {
        document.querySelectorAll('#type-filters input').forEach(function (cb) {
            cb.checked = false;
        });
        document.getElementById('usecase-filter').value = '';
        document.getElementById('ie-filter').value      = '';
        applyFilters();
    };

}());
</script>

</body>
</html>'''


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def normalize_list_attr(value):
    """
    Convert a comma / semicolon / pipe-separated string to a pipe-separated
    string suitable for use in HTML data-* attributes.
    Returns '' for empty or 'nan' inputs.
    """
    v = str(value).strip()
    if not v or v.lower() == 'nan':
        return ''
    parts = re.split(r'\s*[,;|]\s*', v)
    return '|'.join(p.strip() for p in parts if p.strip())


def get_unique_values_from_column(df, col):
    """
    Return a sorted list of unique individual values from a delimited column.
    Handles comma / semicolon / pipe separators and ignores 'nan' cells.
    """
    if col not in df.columns:
        return []
    all_vals = set()
    for raw in df[col]:
        v = str(raw).strip()
        if v and v.lower() != 'nan':
            for part in re.split(r'\s*[,;|]\s*', v):
                part = part.strip()
                if part:
                    all_vals.add(part)
    return sorted(all_vals)


def build_select_options(values):
    """Return a newline-joined string of <option> tags for the given values."""
    lines = []
    for v in values:
        esc = html_lib.escape(v, quote=True)
        lines.append(f'<option value="{esc}">{esc}</option>')
    return '\n            '.join(lines)


# CHANGE 3: Use case dropdown strips the 'bdquc:' namespace prefix from the
# human-readable display text while keeping the full prefixed value in the
# value= attribute so it still matches data-usecases attributes exactly.
def build_usecase_options(values):
    """
    Build <option> tags for use-case values.
    The value= attribute retains the full 'bdquc:'-prefixed name so the JS
    filter matches correctly against data-usecases; the visible label strips
    any namespace prefix for readability.
      e.g.  bdquc:Spatial-Temporal_Patterns  →  display: Spatial-Temporal_Patterns
    """
    lines = []
    for v in values:
        val_esc     = html_lib.escape(v, quote=True)
        display     = re.sub(r'^[a-z]+:', '', v)          # strip leading 'xyz:' prefix
        display_esc = html_lib.escape(display, quote=True)
        lines.append(f'<option value="{val_esc}">{display_esc}</option>')
    return '\n            '.join(lines)


def linkify_urls(text):
    """Wrap bare http(s) URLs in <a> tags."""
    return re.sub(r'(https?://\S+)', r'<a href="\1">\1</a>', text)


# ---------------------------------------------------------------------------
# HTML-section builders
# ---------------------------------------------------------------------------

def build_term_section(term, columns, term_type='', usecases='', ie_acted=''):
    """
    Build a <section class="term-section"> element for one BDQ test.

    Data attributes for JS filtering:
      data-type      – organized_in value (Amendment / Issue / Measure / Validation)
      data-usecases  – pipe-separated use-case identifiers (full bdquc: names)
      data-ie        – pipe-separated Information Elements Acted Upon
    """
    term_id = term.get('term_localName', term.get('Label', 'term')).strip().replace(' ', '_')
    label   = term.get('Label', 'Unnamed Term')

    type_attr     = html_lib.escape(str(term_type).strip(),        quote=True)
    usecases_attr = html_lib.escape(normalize_list_attr(usecases), quote=True)
    ie_attr       = html_lib.escape(normalize_list_attr(ie_acted), quote=True)

    # CHANGE 4 (partial): added 'UseCases' and 'aggregatesResponsesFrom' mappings
    label_map = {
        'iri':                          'Term Version IRI',
        'prefLabel':                    'Preferred Label',
        'ExpectedResponse':             'Expected Response',
        'AuthoritiesDefaults':          'Source Authorities/Defaults',
        'InformationElement:ActedUpon': 'Information Elements Acted Upon',
        'InformationElement:Consulted': 'Information Elements Consulted',
        'aggregatesResponsesFrom':      'Aggregates Responses From',
        'UseCases':                     'Use Cases',
    }

    rows = ''
    for col in columns:
        value = str(term.get(col, '')).strip()
        if not value or value.lower() == 'nan':
            continue
        if col not in ['term_iri', 'iri', 'AuthoritiesDefaults']:
            value = linkify_urls(value)

        term_label = label_map.get(col, col)

        if col == 'Examples':
            value = value.replace('],[', '],<br>[')

        rows += f'<tr><td class="label">{term_label}</td><td>{value}</td></tr>'

    return (
        f'<section class="term-section" id="{term_id}"'
        f' data-type="{type_attr}"'
        f' data-usecases="{usecases_attr}"'
        f' data-ie="{ie_attr}">\n'
        f'<div class="field-header-wrapper"><h3>{label}</h3></div>\n'
        f'<table class="term-table">{rows}</table>\n'
        f'</section>'
    )


def build_field_index(terms):
    """
    Build a <nav class="field-index"> quick-jump block.
    Each link carries data-target so the JS filter can show/hide it
    in sync with its target term section.
    """
    links = []
    for term in terms:
        term_id = term.get('term_localName', term.get('Label', 'term')).strip().replace(' ', '_')
        label   = term.get('Label', 'Unnamed Term')
        links.append(
            f'<a class="field-box" href="#{term_id}" data-target="{term_id}">{label}</a>'
        )
    return '<nav class="field-index">' + ''.join(links) + '</nav>'


# CHANGE 1: Replaced _row_category_from_issuelabels (single-return helper)
# with a direct per-category substring mask in both functions below.
# The old helper matched only the FIRST category found, so a test whose
# IssueLabels contained "NAME SPACE TIME OTHER" (e.g.,
# MEASURE_VALIDATIONTESTS_NOTCOMPLIANT) appeared only under TIME.
# The new approach checks each category independently, so a test can
# correctly appear in multiple category navigation sections.

def build_category_sections(df):
    """
    Build a navigation-index section for each topic category
    (TIME / SPACE / NAME / OTHER).  A single test may appear in more than
    one category section because IssueLabels can contain multiple keywords.
    """
    categories = ['TIME', 'SPACE', 'NAME', 'OTHER']
    col = 'IssueLabels'
    if col not in df.columns:
        return ''

    out = []
    for cat in categories:
        # Independent substring test per category — no first-match-only problem.
        mask   = df[col].apply(lambda v: cat in str(v or '').upper())
        subset = df[mask]
        if subset.empty:
            continue
        terms = sorted(subset.to_dict('records'), key=lambda r: r.get('Label', '').lower())
        out.append(
            f'<section class="category-section" id="cat-{cat}">\n'
            f'  <div class="class-header-wrapper"><h2>{cat}</h2></div>\n'
            f'  {build_field_index(terms)}\n'
            f'</section>\n'
        )
    return ''.join(out)


def build_category_links(df):
    """
    Build sidebar jump-link anchors to the category sections.
    Uses the same independent per-category mask as build_category_sections.
    Returns jump-link-classed <a> tags to match the sidebar styling.
    """
    categories = ['TIME', 'SPACE', 'NAME', 'OTHER']
    col = 'IssueLabels'
    if col not in df.columns:
        return ''

    links = []
    for cat in categories:
        mask = df[col].apply(lambda v: cat in str(v or '').upper())
        if mask.any():
            links.append(f'<a class="jump-link" href="#cat-{cat}">{cat}</a>\n')
    return ''.join(links)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def generate_qrg():
    print(f"Loading CSV from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH)
    df = df.astype(str).fillna('')

    if 'organized_in' not in df.columns:
        raise ValueError("Missing 'organized_in' column in source CSV.")

    # CHANGE 2: added 'aggregatesResponsesFrom' to the display column set.
    # This column sits between InformationElement:ActedUpon and
    # InformationElement:Consulted in the CSV and is meaningful for Measure
    # tests that aggregate results from other tests.
    display_cols = {
        'Label', 'prefLabel', 'iri', 'Description', 'ExpectedResponse',
        'InformationElement:ActedUpon', 'aggregatesResponsesFrom',
        'InformationElement:Consulted', 'Parameters', 'AuthoritiesDefaults',
        'Notes', 'Examples', 'Type', 'UseCases', 'Resource Type',
    }
    # Preserve the column order as it appears in the CSV
    columns = [c for c in df.columns if c.strip() and c in display_cols]

    ordered_classes = ['Amendment', 'Issue', 'Measure', 'Validation']
    grouped = dict(tuple(df.groupby('organized_in')))
    grouped = {cls: grouped[cls] for cls in ordered_classes if cls in grouped}

    # Collect unique values for the filter dropdowns
    unique_usecases = get_unique_values_from_column(df, 'UseCases')
    unique_ies      = get_unique_values_from_column(df, 'InformationElement:ActedUpon')

    # ── Build main content ──────────────────────────────────────────────────
    # Category navigation sections come first (hidden by JS when filters active)
    content = build_category_sections(df)

    # One .class-wrapper per test type
    for group, terms in grouped.items():
        anchor  = group.strip().replace(' ', '_')
        content += '<div class="class-wrapper">\n'
        content += (
            f'<div class="class-header-wrapper">'
            f'<h2 id="{anchor}" class="class-header">{group}</h2>'
            f'</div>\n'
        )
        content += build_field_index(terms.to_dict(orient='records'))

        for _, row in terms.iterrows():
            content += build_term_section(
                row, columns,
                term_type=group,
                usecases=str(row.get('UseCases', '')),
                ie_acted=str(row.get('InformationElement:ActedUpon', '')),
            )

        content += '</div>\n'   # .class-wrapper

    # ── Substitute placeholders ─────────────────────────────────────────────
    html_output = TEMPLATE
    html_output = html_output.replace('###CONTENT###',         content)
    html_output = html_output.replace('###CATEGORY_LINKS###',  build_category_links(df))
    html_output = html_output.replace('###USECASE_OPTIONS###', build_usecase_options(unique_usecases))
    html_output = html_output.replace('###IE_OPTIONS###',      build_select_options(unique_ies))

    # ── Write output ────────────────────────────────────────────────────────
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(html_output)
    print(f"QRG successfully written to {OUTPUT_PATH}")

    with open(DEPLOY_PATH, 'w', encoding='utf-8') as f1:
        f1.write(html_output)
    print(f"QRG successfully written to {DEPLOY_PATH}")


if __name__ == '__main__':
    generate_qrg()
