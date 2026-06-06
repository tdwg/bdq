# Python script to generate the Quick Reference Guide HTML
# (interactive sidebar: external navigation + on-the-fly filters)
# Usage: python generate_bdq_qrg_filtering.py
#
# @author tucotuco John Wieczorek
# @author chicoreus Paul J. Morris
# @author Claude 4.6 Sonnet
#
# Rewritten from generate_bdq_qrg.py to add interactive filtering and category sections by Claude 4.6 Sonnet

# Python script to generate the Quick Reference Guide HTML
# (interactive sidebar: external navigation + on-the-fly filters)
# Usage: python generate_bdq_qrg.py

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
    <!-- Site-wide stylesheets (provide .page-header, .review-banner, variables, etc.) -->
    <link rel="stylesheet" href="/assets/css/pygments.css">
    <link rel="stylesheet" href="/assets/css/site.css">
    <style>
        /* ── CSS custom-property fallbacks ──────────────────────────────────
           These mirror the values in site.css so the page renders correctly
           even if the external stylesheet fails to load.                    */
        :root {
            --bdq-brand:      #155799;
            --bdq-brand-2:    #159957;
            --bdq-link:       #0969da;
            --bdq-border:     #d0d7de;
            --bdq-muted:      #586069;
            --bdq-bg-soft:    #f6f8fa;
            --bdq-bg-soft-2:  rgba(129, 139, 152, 0.12);
            --bdq-review:     #c0392b;
            --bdq-text:       #24292f;
        }

        /* ── Base overrides / page-specific layout ───────────────────────── */
        html { scroll-behavior: smooth; }

        body {
            margin: 0; padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                         Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--bdq-text);
            background: #fff;
            /* NOT display:flex — flex lives on .content-wrapper's children */
            overflow-x: hidden;
        }

        /* Global link colour (site.css only scopes it to .doc-content a etc.) */
        a { color: var(--bdq-link); }

        /* ── Page-header fallback styles (site.css is the canonical source) ─ */
        .page-header {
            color: #fff;
            background-color: var(--bdq-brand);
            background-image: linear-gradient(120deg, var(--bdq-brand),
                                                      var(--bdq-brand-2));
            padding: 1.5rem 1rem;
        }
        .page-header-inner {
            max-width: 72rem; margin: 0 auto;
            display: flex; align-items: flex-start; gap: 1rem;
        }
        .site-logo-link { display: inline-flex; flex: 0 0 auto; align-items: center; }
        .site-logo      { width: 200px; height: 84px; display: block; }
        .page-header-text { min-width: 0; }
        .project-name   { margin: 0; font-size: 2rem; font-weight: 700;
                          border: none; }   /* suppress main h1 rule below */
        .project-name-link { color: #fff; text-decoration: none; }
        .project-name-link:hover { text-decoration: underline; }
        .project-tagline { margin: 0.5rem 0 0 0; opacity: 0.95; font-size: 1.05rem; }

        /* ── Review banner fallback (site.css is the canonical source) ────── */
        .review-banner {
            display: inline-block;
            margin: 0 0 1rem 0; padding: 0.5rem 0.85rem;
            font-weight: 700; font-size: 0.95rem;
            text-transform: uppercase; letter-spacing: 0.04em;
            color: #fff;
            background: var(--bdq-review);
            border-radius: 0.35rem;
        }

        /* ── Two-column layout ───────────────────────────────────────────── */
        /*
         * The fixed sidebar (240 px) sits outside normal flow.
         * .content-wrapper carries margin-left: 240px so page-header and
         * main content clear the sidebar without using flex on <body>.
         */
        .content-wrapper { margin-left: 240px; }

        main { padding: 20px; }

        /* ── Headings ────────────────────────────────────────────────────── */
        /* Scoped to main so the page-header h1 (.project-name) is unaffected */
        main h1 {
            border-bottom: 1px solid var(--bdq-border);
            padding-bottom: 0.3rem;
        }

        /* ── Sidebar (fixed, left) ───────────────────────────────────────── */
        aside.nav-menu {
            position: fixed; top: 0; left: 0; z-index: 200;
            height: 100vh; overflow-y: auto;
            background: var(--bdq-bg-soft);
            border-right: 1px solid var(--bdq-border);
            width: 240px; padding: 14px; box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                         Helvetica, Arial, sans-serif;
        }
        aside.nav-menu h2 {
            font-size: 0.95em; margin: 14px 0 6px 0;
            padding-bottom: 4px;
            border-bottom: 1px solid var(--bdq-border);
            color: var(--bdq-brand);
        }
        aside.nav-menu h2:first-child { margin-top: 0; }

        /* Back to top */
        .back-to-top { margin: 0 0 8px 0; font-size: 0.82em; }
        .back-to-top a { color: var(--bdq-link); text-decoration: none; }
        .back-to-top a:hover { text-decoration: underline; }

        /* External nav links */
        .sidebar-context-links { list-style: none; padding: 0; margin: 0 0 4px 0; }
        .sidebar-context-links li { margin: 5px 0; }
        .sidebar-context-links a {
            color: var(--bdq-link); text-decoration: none; font-size: 0.82em;
        }
        .sidebar-context-links a:hover { text-decoration: underline; }

        .menu-separator { border-top: 1px solid var(--bdq-border); margin: 10px 0; }

        /* Jump links */
        .jump-links { margin: 0 0 10px 0; }
        .jump-section-label {
            display: block; font-size: 0.75em; font-weight: bold;
            color: var(--bdq-muted); margin: 6px 0 2px 0;
        }
        .jump-link {
            display: inline-block; font-size: 0.8em; color: var(--bdq-brand);
            text-decoration: none; margin: 2px 2px 2px 0;
            padding: 2px 6px; border: 1px solid var(--bdq-border);
            border-radius: 3px; background: #fff;
        }
        .jump-link:hover { background: var(--bdq-bg-soft-2); }

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
            font-size: 0.8em; color: var(--bdq-text); margin-bottom: 3px;
        }
        #type-filters label, #category-filters label {
            display: block; font-size: 0.8em; margin: 3px 0; cursor: pointer;
        }
        #type-filters input, #category-filters input {
            margin-right: 4px; cursor: pointer;
        }
        .filter-select {
            width: 100%; font-size: 0.79em; padding: 3px 4px;
            border: 1px solid var(--bdq-border); border-radius: 3px;
            box-sizing: border-box;
        }
        .filter-select-multi { height: 130px; padding: 2px; }
        .filter-hint {
            display: block; font-size: 0.72em; color: var(--bdq-muted);
            font-style: italic; margin-top: 2px;
        }
        #clear-filters {
            font-size: 0.8em; padding: 4px 10px;
            background: var(--bdq-brand); color: #fff;
            border: none; border-radius: 3px; cursor: pointer; margin-top: 6px;
        }
        #clear-filters:hover:not(:disabled) { filter: brightness(1.2); }
        #clear-filters:disabled { background: var(--bdq-muted); cursor: default; }
        #filter-count {
            font-size: 0.76em; color: var(--bdq-muted);
            display: block; margin-top: 5px; font-style: italic;
        }

        /* ── Main content elements ───────────────────────────────────────── */
        .intro { margin: 20px 0; }
        .category-section { margin-bottom: 8px; }

        /*
         * Full-bleed header strips.
         * main has padding: 20px; left: -20px cancels that so the strip
         * starts flush with the content-wrapper edge.
         * Width = viewport − sidebar (240 px).
         */
        .field-header-wrapper {
            width: calc(100vw - 240px);
            position: relative; left: -20px;
            background: #cdd8de; padding: 4px 20px; box-sizing: border-box;
        }
        .field-header-wrapper h3 { margin: 0; font-size: 1em; color: var(--bdq-brand); }

        .class-header-wrapper {
            width: calc(100vw - 240px);
            position: relative; left: -20px;
            background: #dfe5d8; padding: 8px 20px; box-sizing: border-box;
            margin-bottom: 8px;
            border-top:    1px solid var(--bdq-border);
            border-bottom: 1px solid var(--bdq-border);
        }
        .class-header-wrapper h2 {
            margin: 0; font-size: 1.1em;
            color: var(--bdq-brand); border: none;
        }

        nav.field-index a.field-box {
            display: inline-block; margin: 5px; padding: 5px 10px;
            border: 1px solid var(--bdq-border); border-radius: 4px;
            background: var(--bdq-bg-soft); color: var(--bdq-brand);
            text-decoration: none; font-size: 0.75em;
        }
        nav.field-index a.field-box:hover { background: var(--bdq-bg-soft-2); }

        .term-section {
            border-top: 1px solid var(--bdq-border);
            padding-top: 12px; margin-top: 12px;
        }

        table.term-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        table.term-table td {
            vertical-align: top; padding: 4px;
            border-top: 1px solid var(--bdq-border);
        }
        table.term-table td.label {
            width: 25%; font-weight: bold; color: var(--bdq-brand);
        }

        .no-results-msg {
            display: none; padding: 16px 20px;
            color: var(--bdq-muted); font-style: italic;
            border: 1px dashed var(--bdq-border); border-radius: 4px; margin: 20px 0;
        }

        /* ── Responsive: collapse sidebar on narrow screens ─────────────── */
        @media (max-width: 768px) {
            aside.nav-menu {
                position: static; width: 100%; height: auto;
                border-right: none; border-bottom: 1px solid var(--bdq-border);
                overflow-y: visible; z-index: auto;
            }
            .content-wrapper { margin-left: 0; }
            .field-header-wrapper,
            .class-header-wrapper { width: 100vw; }
            .site-logo { width: 120px; height: 50px; }
            .project-name { font-size: 1.5rem; }
        }
    </style>
</head>
<body>

<!-- ── Fixed left sidebar ───────────────────────────────────────────────── -->
<aside class="nav-menu">

    <h2>BDQ Standard</h2>
    <ul class="sidebar-context-links">
        <li><a href="https://bdq.tdwg.org/draft/">&#127968; Landing page</a></li>
        <li><a href="https://bdq.tdwg.org/draft/#2-A-Roadmap-to-the-BDQ-Standard-non-normative">&#129517; Roadmap to the Standard</a></li>
        <li><a href="https://bdq.tdwg.org/draft/README.html">&#128203; Public Review</a></li>
    </ul>

    <div class="menu-separator"></div>

    <h2>On this Page</h2>

    <!-- Change 1: back-to-top is now under "On this Page" -->
    <p class="back-to-top">&uarr; <a href="#top"><strong>Back to top</strong></a></p>

    <!-- Hidden by JS when any filter is active -->
    <div class="jump-links" id="jump-links">
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
        <span class="filter-label">Filter by Category</span>
        <div id="category-filters">
            <label><input type="checkbox" name="category" value="TIME"  onchange="applyFilters()"> TIME</label>
            <label><input type="checkbox" name="category" value="SPACE" onchange="applyFilters()"> SPACE</label>
            <label><input type="checkbox" name="category" value="NAME"  onchange="applyFilters()"> NAME</label>
            <label><input type="checkbox" name="category" value="OTHER" onchange="applyFilters()"> OTHER</label>
        </div>
    </div>

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
        <select id="ie-filter" class="filter-select filter-select-multi"
                multiple onchange="applyFilters()">
            ###IE_OPTIONS###
        </select>
        <small class="filter-hint">Ctrl+click / &#8984;+click to select multiple.<br>
            No selection = no filter applied.</small>
    </div>

    <button id="clear-filters" onclick="clearFilters()" disabled>Clear Filters</button>
    <span id="filter-count"></span>

</aside>

<!-- ── Content wrapper: offset right to clear the fixed sidebar ─────────── -->
<div class="content-wrapper">

    <!-- Site-consistent page header (matches other BDQ Standard pages) -->
    <div class="page-header">
        <div class="page-header-inner">
            <a class="site-logo-link" href="https://bdq.tdwg.org/bdq/"
               aria-label="TDWG home for this section">
                <img class="site-logo"
                     src="/assets/img/TDWG-Logo_horizontal-white.svg"
                     alt="TDWG logo">
            </a>
            <div class="page-header-text">
                <h1 class="project-name">
                    <a class="project-name-link" href="https://bdq.tdwg.org/bdq/">The
                    Biodiversity Data Quality (BDQ) Standard</a>
                </h1>
                <p class="project-tagline">Draft of the TDWG Biodiversity Data Quality
                Standard</p>
            </div>
        </div>
    </div>

    <!-- Main page content -->
    <main>
        <!-- Prominent "Under Review" banner -->
        <div class="review-banner" role="note" aria-label="Under review">Under Review</div>

        <h1 id="top">BDQ Tests Quick Reference Guide</h1>

        <div class="intro">
          <p>This document is intended to be an easy-to-read reference for the Tests maintained
          as part of the TDWG standard <a href="http://example.org/to_be_determined">BDQ</a>
          produced by the TDWG Biodiversity Data Quality Interest Group Task Group 2: Data
          Quality Tests and Assertions and is maintained by the BDQ Maintenance Interest Group.
          This document lists the BDQ Tests, described by the <a
          href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/terms/bdqtest/bdqtest_qrg_term_descriptions.md">Terms
          Used in the BDQ Tests Quick Reference Guide</a>. Definitions, comments, and examples
          may include namespace abbreviations (e.g., <code>bdqval:</code>, <code>dwc:</code>).
          These are required as the meaning for the word is defined specifically in that
          namespace. Thus, <code>dwc:Event</code> means Event as defined by Darwin Core at
          <a href="https://dwc.tdwg.org/terms/#event">https://dwc.tdwg.org/terms/#event</a>.</p>
          <p>This page is a non-normative descriptive document, not the <a
          href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/list/bdqtest/index.md">full
          vocabulary definition document</a> for <code>bdqtest:</code> terms. It combines the
          normative Test names and terms with non-normative comments and examples that are meant
          to help people to use the Tests consistently. Further details can be found in <a
          href="https://github.com/tdwg/bdq/blob/master/tg2/_review/index.md">The Biodiversity
          Data Quality (BDQ) Standard</a>, the <a
          href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/guide/bdqffdq/index.md">Fitness
          For Use Framework Ontology Guide</a>, and the <a
          href="https://github.com/tdwg/bdq/blob/master/tg2/_review/docs/guide/implementers/index.md">BDQ
          Implementer&#8217;s Guide</a>.</p>
          <p>If you have questions or suggestions, submit these to the <a
          href="https://github.com/tdwg/bdq/issues">BDQ Issues</a> page in GitHub. See the
          bottom of this document for how to cite the BDQ standard and this document in
          particular.</p>
        </div>

        <div id="no-results-msg" class="no-results-msg">
            No tests match the current filters.
            <a href="#" onclick="clearFilters(); return false;">Clear filters</a> to see all
            tests.
        </div>

        ###CONTENT###
    </main>

</div><!-- .content-wrapper -->

<script>
(function () {
    'use strict';

    var totalCount = document.querySelectorAll('.term-section').length;
    document.getElementById('filter-count').textContent = totalCount + ' tests total';

    /**
     * Returns true when filterValue is empty OR when it exactly matches one
     * of the pipe-separated tokens stored in dataValue.
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

        var selectedTypes = Array.from(
            document.querySelectorAll('#type-filters input:checked')
        ).map(function (cb) { return cb.value; });

        var selectedCats = Array.from(
            document.querySelectorAll('#category-filters input:checked')
        ).map(function (cb) { return cb.value; });

        var selectedUC = document.getElementById('usecase-filter').value;

        var selectedIEs = Array.from(
            document.getElementById('ie-filter').selectedOptions
        ).map(function (o) { return o.value; });

        var anyActive = selectedTypes.length > 0 || selectedCats.length > 0 ||
                        !!selectedUC            || selectedIEs.length  > 0;

        /* ── Update sidebar chrome ── */
        document.getElementById('clear-filters').disabled = !anyActive;
        document.getElementById('filters-active-msg').style.display =
            anyActive ? 'block' : 'none';

        /* Hide jump-link navigation while filters are active */
        document.getElementById('jump-links').style.display = anyActive ? 'none' : '';

        /* Hide topic-category index sections when any filter is active */
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

            if (show && selectedCats.length > 0) {
                var catMatch = selectedCats.some(function (cat) {
                    return matchesList(sec.dataset.categories, cat);
                });
                if (!catMatch) show = false;
            }

            if (show && !matchesList(sec.dataset.usecases, selectedUC)) show = false;

            if (show && selectedIEs.length > 0) {
                var ieMatch = selectedIEs.some(function (ie) {
                    return matchesList(sec.dataset.ie, ie);
                });
                if (!ieMatch) show = false;
            }

            sec.style.display = show ? '' : 'none';
            if (show) visibleCount++;
        });

        /* ── Show / hide class wrappers; sync quick-nav links ── */
        document.querySelectorAll('.class-wrapper').forEach(function (wrapper) {
            var terms      = Array.from(wrapper.querySelectorAll('.term-section'));
            var anyVisible = terms.some(function (s) {
                return s.style.display !== 'none';
            });
            wrapper.style.display = anyVisible ? '' : 'none';

            wrapper.querySelectorAll('a.field-box[data-target]').forEach(function (link) {
                var target = document.getElementById(link.dataset.target);
                link.style.display =
                    (target && target.style.display !== 'none') ? '' : 'none';
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
        document.querySelectorAll('#category-filters input').forEach(function (cb) {
            cb.checked = false;
        });
        document.getElementById('usecase-filter').value = '';
        Array.from(document.getElementById('ie-filter').options).forEach(function (o) {
            o.selected = false;
        });
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
    Convert a comma / semicolon / pipe-separated string into a pipe-separated
    string for use in HTML data-* attributes.
    Returns '' for empty or 'nan' inputs.
    """
    v = str(value).strip()
    if not v or v.lower() == 'nan':
        return ''
    parts = re.split(r'\s*[,;|]\s*', v)
    return '|'.join(p.strip() for p in parts if p.strip())


def extract_categories(issue_labels_value):
    """
    Scan IssueLabels for TIME / SPACE / NAME / OTHER keywords and return a
    pipe-separated string of every category found.  A single test may belong
    to more than one category.
    """
    s = str(issue_labels_value or '').upper()
    found = [cat for cat in ('TIME', 'SPACE', 'NAME', 'OTHER') if cat in s]
    return '|'.join(found)


def get_unique_values_from_column(df, col):
    """
    Return a sorted list of unique individual values from a delimited column.
    Handles comma / semicolon / pipe separators; ignores 'nan' cells.
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
    """Return <option> tags for a plain single-select dropdown."""
    lines = []
    for v in values:
        esc = html_lib.escape(v, quote=True)
        lines.append(f'<option value="{esc}">{esc}</option>')
    return '\n            '.join(lines)


def build_usecase_options(values):
    """
    Build <option> tags for use-case values.
    value= keeps the full 'bdquc:'-prefixed name (matches data-usecases);
    visible label strips the namespace prefix for readability.
    """
    lines = []
    for v in values:
        val_esc     = html_lib.escape(v, quote=True)
        display     = re.sub(r'^[a-z]+:', '', v)
        display_esc = html_lib.escape(display, quote=True)
        lines.append(f'<option value="{val_esc}">{display_esc}</option>')
    return '\n            '.join(lines)


def linkify_urls(text):
    """Wrap bare http(s) URLs in <a> tags."""
    return re.sub(r'(https?://\S+)', r'<a href="\1">\1</a>', text)


# ---------------------------------------------------------------------------
# HTML-section builders
# ---------------------------------------------------------------------------

def build_term_section(term, columns, term_type='', usecases='',
                        ie_acted='', categories=''):
    """
    Build a <section class="term-section"> for one BDQ test.

    Data attributes for JS filtering:
      data-type       – organized_in value (Amendment / Issue / Measure / Validation)
      data-usecases   – pipe-separated use-case identifiers (full bdquc: names)
      data-ie         – pipe-separated Information Elements Acted Upon
      data-categories – pipe-separated TIME/SPACE/NAME/OTHER from IssueLabels
    """
    term_id = term.get('term_localName', term.get('Label', 'term')).strip().replace(' ', '_')
    label   = term.get('Label', 'Unnamed Term')

    type_attr       = html_lib.escape(str(term_type).strip(),         quote=True)
    usecases_attr   = html_lib.escape(normalize_list_attr(usecases),  quote=True)
    ie_attr         = html_lib.escape(normalize_list_attr(ie_acted),  quote=True)
    categories_attr = html_lib.escape(str(categories).strip(),        quote=True)

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
        f' data-ie="{ie_attr}"'
        f' data-categories="{categories_attr}">\n'
        f'<div class="field-header-wrapper"><h3>{label}</h3></div>\n'
        f'<table class="term-table">{rows}</table>\n'
        f'</section>'
    )


def build_field_index(terms):
    """
    Build a <nav class="field-index"> quick-jump block.
    Each link carries data-target so the JS filter can sync its visibility
    with its target term section.
    """
    links = []
    for term in terms:
        term_id = term.get('term_localName', term.get('Label', 'term')).strip().replace(' ', '_')
        label   = term.get('Label', 'Unnamed Term')
        links.append(
            f'<a class="field-box" href="#{term_id}" data-target="{term_id}">{label}</a>'
        )
    return '<nav class="field-index">' + ''.join(links) + '</nav>'


def build_category_sections(df):
    """
    Build a navigation-index section for each topic category.
    Independent per-category masks allow a test to appear in multiple sections.
    """
    categories = ['TIME', 'SPACE', 'NAME', 'OTHER']
    col = 'IssueLabels'
    if col not in df.columns:
        return ''

    out = []
    for cat in categories:
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
    """Build sidebar jump-link <a> tags for each present category."""
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

    display_cols = {
        'Label', 'prefLabel', 'iri', 'Description', 'ExpectedResponse',
        'InformationElement:ActedUpon', 'aggregatesResponsesFrom',
        'InformationElement:Consulted', 'Parameters', 'AuthoritiesDefaults',
        'Notes', 'Examples', 'Type', 'UseCases', 'Resource Type',
    }
    # Preserve column order as it appears in the CSV
    columns = [c for c in df.columns if c.strip() and c in display_cols]

    ordered_classes = ['Amendment', 'Issue', 'Measure', 'Validation']
    grouped = dict(tuple(df.groupby('organized_in')))
    grouped = {cls: grouped[cls] for cls in ordered_classes if cls in grouped}

    unique_usecases = get_unique_values_from_column(df, 'UseCases')
    unique_ies      = get_unique_values_from_column(df, 'InformationElement:ActedUpon')

    # ── Build main content ──────────────────────────────────────────────────
    content = build_category_sections(df)

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
                term_type  = group,
                usecases   = str(row.get('UseCases', '')),
                ie_acted   = str(row.get('InformationElement:ActedUpon', '')),
                categories = extract_categories(row.get('IssueLabels', '')),
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
