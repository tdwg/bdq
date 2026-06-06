# Python script to generate the Quick Reference Guide HTML
# (interactive sidebar: external navigation + on-the-fly filters)
# Usage: python generate_bdq_qrg_filtering.py
#
# @author tucotuco John Wieczorek
# @author chicoreus Paul J. Morris
# @author Claude 4.6 Sonnet
#
# Rewritten from generate_bdq_qrg.py to add interactive filtering and category sections by Claude 4.6 Sonnet

import os
import re
import html as html_lib
import pandas as pd
import yaml

try:
    import markdown
except ImportError:
    raise ImportError(
        "The 'markdown' package is required.  "
        "Install with:  pip install markdown"
    )

# ── File paths ────────────────────────────────────────────────────────────────
CSV_PATH        = '../_review/vocabulary/bdqtest_term_versions.csv'
OUTPUT_PATH     = '../_review/docs/terms/bdqtest/index.html'
DEPLOY_PATH     = '../../terms/bdqtest/index.html'
TEMPLATE_DIR    = '../_build_review/templates/terms/bdqtest_qrg'
HEADER_MD_PATH  = os.path.join(TEMPLATE_DIR, 'bdqtest_quickreference-header.md')
FOOTER_MD_PATH  = os.path.join(TEMPLATE_DIR, 'bdqtest_quickreference-footer.md')
DOC_CONFIG_PATH = os.path.join(TEMPLATE_DIR, 'document_configuration.yaml')


# ═══════════════════════════════════════════════════════════════════════════════
# HTML template  (###PLACEHOLDER### avoids brace-doubling in CSS/JS blocks)
# ═══════════════════════════════════════════════════════════════════════════════
TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>###PAGE_TITLE###</title>
    <!-- Site-wide stylesheets supply .page-header, .review-banner, CSS vars -->
    <link rel="stylesheet" href="/assets/css/pygments.css">
    <link rel="stylesheet" href="/assets/css/site.css">
    <style>
        /* ── CSS custom-property fallbacks (mirrors site.css) ────────────── */
        :root {
            --bdq-brand:     #155799;
            --bdq-brand-2:   #159957;
            --bdq-link:      #0969da;
            --bdq-border:    #d0d7de;
            --bdq-muted:     #586069;
            --bdq-bg-soft:   #f6f8fa;
            --bdq-bg-soft-2: rgba(129, 139, 152, 0.12);
            --bdq-review:    #c0392b;
            --bdq-text:      #24292f;
        }

        html { scroll-behavior: smooth; }

        body {
            margin: 0; padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                         Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--bdq-text);
            background: #fff;
            overflow-x: hidden;
        }

        a { color: var(--bdq-link); }

        /* ── Page-header fallback (canonical source: site.css) ───────────── */
        .page-header {
            color: #fff;
            background-color: var(--bdq-brand);
            background-image: linear-gradient(120deg,
                                var(--bdq-brand), var(--bdq-brand-2));
            padding: 1.5rem 1rem;
        }
        .page-header-inner {
            max-width: 72rem; margin: 0 auto;
            display: flex; align-items: flex-start; gap: 1rem;
        }
        .site-logo-link { display: inline-flex; flex: 0 0 auto; align-items: center; }
        .site-logo      { width: 200px; height: 84px; display: block; }
        .page-header-text { min-width: 0; }
        .project-name   { margin: 0; font-size: 2rem; font-weight: 700; border: none; }
        .project-name-link  { color: #fff; text-decoration: none; }
        .project-name-link:hover { text-decoration: underline; }
        .project-tagline { margin: 0.5rem 0 0 0; opacity: 0.95; font-size: 1.05rem; }

        /* ── Review banner fallback (canonical source: site.css) ─────────── */
        .review-banner {
            display: inline-block;
            margin: 1rem 0; padding: 0.5rem 0.85rem;
            font-weight: 700; font-size: 0.95rem;
            text-transform: uppercase; letter-spacing: 0.04em;
            color: #fff; background: var(--bdq-review); border-radius: 0.35rem;
        }

        /* ── Two-column layout ───────────────────────────────────────────── */
        .content-wrapper { margin-left: 240px; }
        main { padding: 20px; }

        /* ── Headings (scoped to main so page-header h1 is unaffected) ───── */
        main h1 {
            border-bottom: 1px solid var(--bdq-border);
            padding-bottom: 0.3rem; margin-top: 1.5rem;
        }
        main h1:first-of-type { margin-top: 0.5rem; }
        main h2 {
            border-bottom: 1px solid var(--bdq-border);
            padding-bottom: 0.2rem; margin-top: 1.5rem;
        }
        /* Suppress border on coloured-background wrapper headings */
        .class-header-wrapper h2 { border: none; padding-bottom: 0; margin-top: 0; }

        /* ── Fixed left sidebar ──────────────────────────────────────────── */
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
            padding-bottom: 4px; border-bottom: 1px solid var(--bdq-border);
            color: var(--bdq-brand);
        }
        aside.nav-menu h2:first-child { margin-top: 0; }

        .back-to-top { margin: 0 0 8px 0; font-size: 0.82em; }
        .back-to-top a { color: var(--bdq-link); text-decoration: none; }
        .back-to-top a:hover { text-decoration: underline; }

        .sidebar-context-links { list-style: none; padding: 0; margin: 0 0 4px 0; }
        .sidebar-context-links li { margin: 5px 0; }
        .sidebar-context-links a {
            color: var(--bdq-link); text-decoration: none; font-size: 0.82em;
        }
        .sidebar-context-links a:hover { text-decoration: underline; }

        .menu-separator { border-top: 1px solid var(--bdq-border); margin: 10px 0; }

        /* Jump / index links */
        .jump-links { margin: 0 0 10px 0; }
        .jump-section-label {
            display: block; font-size: 0.75em; font-weight: bold;
            color: var(--bdq-muted); margin: 0 0 4px 0;
        }
        .jump-link {
            display: inline-block; font-size: 0.8em; color: var(--bdq-brand);
            text-decoration: none; margin: 2px 2px 2px 0;
            padding: 2px 6px; border: 1px solid var(--bdq-border);
            border-radius: 3px; background: #fff;
        }
        .jump-link:hover { background: var(--bdq-bg-soft-2); }

        /* ── Filter panel ────────────────────────────────────────────────── */
        .filters-active-msg {
            display: none; font-size: 0.75em;
            background: #fff3cd; border: 1px solid #ffc107;
            border-radius: 3px; padding: 4px 8px; color: #856404;
            margin-bottom: 8px; font-weight: bold;
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

        /*
         * CHANGE 2 — Clear Filters button.
         * Disabled (no active filters): subtle grey, not distracting.
         * Enabled  (filters active):    prominent red — same hue as the
         *   "Under Review" banner, full sidebar width, bold label.
         * This makes it immediately obvious that filters are on and how
         * to reset them, which was the key piece of user feedback.
         */
        #clear-filters {
            font-size: 0.85em; padding: 6px 10px;
            color: #fff;
            border: none; border-radius: 3px;
            margin-top: 6px; width: 100%; font-weight: bold;
            cursor: default;
            background: #ccc;
            transition: background-color 0.15s;
        }
        #clear-filters:not(:disabled) {
            background: var(--bdq-review);   /* prominent red when active */
            cursor: pointer;
        }
        #clear-filters:not(:disabled):hover { filter: brightness(1.15); }
        #clear-filters:disabled { background: #ccc; color: #888; }

        #filter-count {
            font-size: 0.76em; color: var(--bdq-muted);
            display: block; margin-top: 5px; font-style: italic;
        }

        /* ── Main content ─────────────────────────────────────────────────── */
        .category-section { margin-bottom: 8px; }

        .field-header-wrapper {
            width: calc(100vw - 240px); position: relative; left: -20px;
            background: #cdd8de; padding: 4px 20px; box-sizing: border-box;
        }
        .field-header-wrapper h3 { margin: 0; font-size: 1em; color: var(--bdq-brand); }

        .class-header-wrapper {
            width: calc(100vw - 240px); position: relative; left: -20px;
            background: #dfe5d8; padding: 8px 20px; box-sizing: border-box;
            margin-bottom: 8px;
            border-top: 1px solid var(--bdq-border);
            border-bottom: 1px solid var(--bdq-border);
        }
        .class-header-wrapper h2 { margin: 0; font-size: 1.1em; color: var(--bdq-brand); }

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

        main ul   { margin: 0.5rem 0; padding-left: 1.5rem; }
        main ul li { margin: 0.3rem 0; }
        main ul ul { margin: 0.2rem 0; }

        .page-footer {
            margin-top: 3rem; padding-top: 1.5rem;
            border-top: 2px solid var(--bdq-border);
        }

        /* ── Responsive ──────────────────────────────────────────────────── */
        @media (max-width: 768px) {
            aside.nav-menu {
                position: static; width: 100%; height: auto;
                border-right: none; border-bottom: 1px solid var(--bdq-border);
                overflow-y: visible; z-index: auto;
            }
            .content-wrapper { margin-left: 0; }
            .field-header-wrapper,
            .class-header-wrapper { width: 100vw; }
            .site-logo  { width: 120px; height: 50px; }
            .project-name { font-size: 1.5rem; }
        }
    </style>
</head>
<body>

<!-- ── Fixed left sidebar ──────────────────────────────────────────────────── -->
<aside class="nav-menu">

    <h2>BDQ Standard</h2>
    <ul class="sidebar-context-links">
        <li><a href="https://bdq.tdwg.org/draft/">&#127968; Landing page</a></li>
        <li><a href="https://bdq.tdwg.org/draft/#2-A-Roadmap-to-the-BDQ-Standard-non-normative">&#129517; Roadmap to the Standard</a></li>
        <li><a href="https://bdq.tdwg.org/draft/README.html">&#128203; Public Review</a></li>
    </ul>

    <div class="menu-separator"></div>

    <h2>On this Page</h2>

    <p class="back-to-top">&uarr; <a href="#top"><strong>Back to top</strong></a></p>

    <!--
      Single "Index" label; all category + test-type buttons together.
      Hidden by JS whenever any filter is active.
    -->
    <div class="jump-links" id="jump-links">
        <span class="jump-section-label">Index</span>
        ###CATEGORY_LINKS###<a
        class="jump-link" href="#Amendment">Amendment</a><a
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

    <!-- CHANGE 2: button is full-width, prominent red when active -->
    <button id="clear-filters" onclick="clearFilters()" disabled>
        &#10005; Clear All Filters
    </button>
    <span id="filter-count"></span>

</aside>

<!-- ── Everything else: cleared right of the sidebar ───────────────────────── -->
<div class="content-wrapper">

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
                <p class="project-tagline">Draft of the TDWG Biodiversity Data
                Quality Standard</p>
            </div>
        </div>
    </div>

    <main>
        <span id="top"></span>

        <div class="review-banner" role="note" aria-label="Under review">Under Review</div>

        ###HEADER_HTML###

        <div id="no-results-msg" class="no-results-msg">
            No tests match the current filters.
            <a href="#" onclick="clearFilters(); return false;">Clear filters</a>
            to see all tests.
        </div>

        ###CONTENT###

        <footer class="page-footer" aria-label="Document footer">
            ###FOOTER_HTML###
        </footer>
    </main>

</div><!-- .content-wrapper -->

<script>
(function () {
    'use strict';

    var totalCount = document.querySelectorAll('.term-section').length;
    document.getElementById('filter-count').textContent = totalCount + ' tests total';

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

        /*
         * CHANGE 2 — Scroll to the very top of the page and clear any URL
         * hash before doing any DOM work.
         *
         * Why this matters:
         *   - When filters hide/show elements the total page height changes.
         *     Without this reset, the browser keeps the old scroll offset,
         *     which can land anywhere — including the footer (Glossary).
         *   - A stale #hash in the URL can cause the browser to jump to a
         *     term that is now hidden, producing erratic scroll behaviour
         *     when the user then changes the filter again.
         *
         * Using behavior:'instant' avoids a distracting animation;
         * the user asked the filter to change, so a clean-cut reset is
         * the right UX.
         */
        window.scrollTo({ top: 0, behavior: 'instant' });
        if (window.location.hash) {
            history.replaceState(
                null, '',
                window.location.pathname + window.location.search
            );
        }

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
        document.getElementById('jump-links').style.display =
            anyActive ? 'none' : '';

        /* ── Hide topic-category index sections while any filter is active ── */
        document.querySelectorAll('.category-section').forEach(function (el) {
            el.style.display = anyActive ? 'none' : '';
        });

        /* ── Show / hide individual term sections ── */
        var visibleCount = 0;
        document.querySelectorAll('.term-section').forEach(function (sec) {
            var show = true;

            if (selectedTypes.length > 0 &&
                    selectedTypes.indexOf(sec.dataset.type) === -1) show = false;

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

            wrapper.querySelectorAll('a.field-box[data-target]').forEach(
                function (link) {
                    var target = document.getElementById(link.dataset.target);
                    link.style.display =
                        (target && target.style.display !== 'none') ? '' : 'none';
                }
            );
        });

        document.getElementById('no-results-msg').style.display =
            (anyActive && visibleCount === 0) ? 'block' : 'none';

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
        Array.from(document.getElementById('ie-filter').options).forEach(
            function (o) { o.selected = false; }
        );
        applyFilters();   /* applyFilters() also scrolls to top */
    };

}());
</script>

</body>
</html>'''


# ═══════════════════════════════════════════════════════════════════════════════
# YAML loading
# ═══════════════════════════════════════════════════════════════════════════════

def _load_yaml(path):
    with open(path, 'r', encoding='utf-8') as fh:
        return yaml.safe_load(fh) or {}


# ═══════════════════════════════════════════════════════════════════════════════
# Template-variable helpers
# ═══════════════════════════════════════════════════════════════════════════════

def _camel_to_snake(name):
    s = re.sub(r'([A-Z][a-z]+)', r'_\1', name)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)
    return s.lower().lstrip('_')


_YAML_ALIASES = {
    'standard_iri':   'dcterms_isPartOf',
    'document_title': 'documentTitle',
}


def _build_template_vars(yaml_cfg):
    """
    Build a flat {placeholder: value} dict from the YAML configuration.

    Rules:
    1.  Every YAML key is stored as-is.
    2.  A snake_case alias is added for every camelCase key.
    3.  Explicit aliases in _YAML_ALIASES fill any remaining gaps.
    4.  'year' and 'ratification_date' are derived from 'doc_created'.
    5.  'comment' defaults to '' — it is NOT populated from 'abstract'.
    """
    v = {}
    for k, val in yaml_cfg.items():
        str_val = str(val) if val is not None else ''
        v[k] = str_val
        snake = _camel_to_snake(k)
        if snake != k:
            v[snake] = str_val

    for alias, source_key in _YAML_ALIASES.items():
        if alias not in v:
            v[alias] = v.get(source_key, v.get(_camel_to_snake(source_key), ''))

    doc_created = v.get('doc_created', '')
    if doc_created and len(doc_created) >= 4:
        v.setdefault('year',             doc_created[:4])
        v.setdefault('ratification_date', doc_created)

    # comment: use only what YAML supplies; never fall back to abstract
    v.setdefault('comment', '')

    return v


# ═══════════════════════════════════════════════════════════════════════════════
# CHANGE 1 — Markdown hide-block removal
# ═══════════════════════════════════════════════════════════════════════════════

def _remove_hide_blocks(text):
    """
    Remove blocks enclosed by the BDQ hide-block markers:

        <!--- START HIDE IN HTML --->
        ...any content...
        <!--- END HIDE IN HTML --->

    Both the markers themselves AND the content between them are deleted.
    Whitespace padding around the marker text is tolerated.
    Multiple non-overlapping blocks in one file are all removed.

    This runs BEFORE the general <!--- ... ---> comment strip so that the
    END marker is never consumed prematurely by the general strip.
    """
    return re.sub(
        r'<!---\s*START HIDE IN HTML\s*--->.*?<!---\s*END HIDE IN HTML\s*--->',
        '',
        text,
        flags=re.DOTALL
    )


# ═══════════════════════════════════════════════════════════════════════════════
# Markdown → HTML conversion
# ═══════════════════════════════════════════════════════════════════════════════

def _rewrite_md_links(html_text):
    """
    Rewrite href="…path.md" → href="…path.html" (preserving #fragment).
    External http(s) URLs and fragment-only anchors are left untouched.
    """
    def _fix(m):
        path = m.group(1)
        frag = m.group(2) or ''
        return f'href="{path}.html{frag}"'

    return re.sub(r'href="([^"#][^"]*?)\.md(#[^"]*?)?"', _fix, html_text)


def convert_md_template(md_path, variables):
    """
    Load a BDQ markdown template, substitute variables, and return HTML.

    Steps:
    1.  Read file.
    2.  Remove <!--- START HIDE IN HTML ---> … <!--- END HIDE IN HTML --->
        blocks (markers + content both deleted).   [CHANGE 1]
    3.  Strip remaining <!--- … ---> comment blocks.
    4.  Substitute {variable} placeholders.
    5.  Warn about unresolved {placeholder} tokens.
    6.  Normalise line endings.
    7.  Convert markdown → HTML via python-markdown
        (extensions: 'extra' for tables/nested-lists, 'toc' for heading ids).
    8.  Rewrite .md hrefs → .html.

    Note: strip_trailing_h2 parameter removed — use the
    <!--- START HIDE IN HTML ---> marker in the template instead.
    """
    if not os.path.exists(md_path):
        print(f"Warning: template not found: {md_path}")
        return ''

    with open(md_path, 'r', encoding='utf-8') as fh:
        text = fh.read()

    # 2. Remove HIDE blocks before any other processing
    text = _remove_hide_blocks(text)

    # 3. Strip remaining <!--- ... ---> comment blocks
    text = re.sub(r'<!---.*?--->', '', text, flags=re.DOTALL)

    # 4. Variable substitution
    for key, val in variables.items():
        text = text.replace('{' + key + '}', val)

    # 5. Warn about remaining unresolved tokens
    remaining = sorted(set(re.findall(r'\{([a-zA-Z_]\w*)\}', text)))
    if remaining:
        print(f"Warning [{os.path.basename(md_path)}]: "
              f"unresolved template variables: {remaining}")

    # 6. Normalise line endings
    text = text.replace('\r\n', '\n')

    # 7. Convert markdown → HTML
    md_proc = markdown.Markdown(
        extensions=['extra', 'toc'],
        extension_configs={
            'toc': {'permalink': False}
        }
    )
    html_text = md_proc.convert(text)

    # 8. Rewrite .md links → .html
    html_text = _rewrite_md_links(html_text)

    return html_text


# ═══════════════════════════════════════════════════════════════════════════════
# BDQ-specific HTML-section builders
# ═══════════════════════════════════════════════════════════════════════════════

def normalize_list_attr(value):
    """Pipe-separated string for HTML data-* attributes from a delimited value."""
    v = str(value).strip()
    if not v or v.lower() == 'nan':
        return ''
    return '|'.join(p.strip() for p in re.split(r'\s*[,;|]\s*', v) if p.strip())


def extract_categories(issue_labels_value):
    """
    Return pipe-separated TIME/SPACE/NAME/OTHER categories present in IssueLabels.
    A single test may belong to more than one category.
    """
    s = str(issue_labels_value or '').upper()
    return '|'.join(c for c in ('TIME', 'SPACE', 'NAME', 'OTHER') if c in s)


def get_unique_values_from_column(df, col):
    """Sorted list of unique individual values from a delimited column."""
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
    return '\n            '.join(
        f'<option value="{html_lib.escape(v, quote=True)}">'
        f'{html_lib.escape(v, quote=True)}</option>'
        for v in values
    )


def build_usecase_options(values):
    """
    value= keeps the full 'bdquc:'-prefixed name (matches data-usecases);
    visible label strips any 'xyz:' namespace prefix for readability.
    """
    lines = []
    for v in values:
        val_esc     = html_lib.escape(v, quote=True)
        display     = re.sub(r'^[a-z]+:', '', v)
        display_esc = html_lib.escape(display, quote=True)
        lines.append(f'<option value="{val_esc}">{display_esc}</option>')
    return '\n            '.join(lines)


def linkify_urls(text):
    return re.sub(r'(https?://\S+)', r'<a href="\1">\1</a>', text)


def build_term_section(term, columns, term_type='', usecases='',
                        ie_acted='', categories=''):
    """
    Build a <section class="term-section"> for one BDQ test.

    CHANGE 3 — Dual anchors:
      Primary   id  on the <section>: term_localName (the GUID)
        → supports  https://…/bdqtest/#b129fa4d-b25b-43f7-9645-5ed4d44b357b
      Secondary id  on a <span>      : Label (the uppercase test name)
        → supports  https://…/bdqtest/#AMENDMENT_DAY_STANDARDIZED

    The <span> is placed as the first child of the <section>, immediately
    before the coloured field-header strip, so both anchors scroll the
    user to the same visual position.

    Other data attributes for JS filtering:
      data-type       – Amendment / Issue / Measure / Validation
      data-usecases   – pipe-separated bdquc: use-case identifiers
      data-ie         – pipe-separated Information Elements Acted Upon
      data-categories – pipe-separated TIME/SPACE/NAME/OTHER
    """
    # Primary anchor: GUID (term_localName)
    term_id  = (term.get('term_localName', term.get('Label', 'term'))
                .strip().replace(' ', '_'))
    label    = term.get('Label', 'Unnamed Term')
    # Secondary anchor: Label (e.g. AMENDMENT_DAY_STANDARDIZED)
    label_id = label.strip().replace(' ', '_')

    type_attr       = html_lib.escape(str(term_type).strip(),         quote=True)
    usecases_attr   = html_lib.escape(normalize_list_attr(usecases),  quote=True)
    ie_attr         = html_lib.escape(normalize_list_attr(ie_acted),  quote=True)
    categories_attr = html_lib.escape(str(categories).strip(),        quote=True)
    term_id_esc     = html_lib.escape(term_id,                        quote=True)
    label_id_esc    = html_lib.escape(label_id,                       quote=True)

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

    # Build the secondary label anchor span.
    # Only emitted when label_id is non-empty and actually differs from the
    # GUID (they always differ in practice, but guard anyway to avoid
    # duplicate id= attributes).
    secondary_anchor = ''
    if label_id and label_id != term_id:
        secondary_anchor = (
            f'<span id="{label_id_esc}" aria-hidden="true"></span>\n'
        )

    return (
        f'<section class="term-section" id="{term_id_esc}"'
        f' data-type="{type_attr}"'
        f' data-usecases="{usecases_attr}"'
        f' data-ie="{ie_attr}"'
        f' data-categories="{categories_attr}">\n'
        f'{secondary_anchor}'                      # label anchor (CHANGE 3)
        f'<div class="field-header-wrapper"><h3>{label}</h3></div>\n'
        f'<table class="term-table">{rows}</table>\n'
        f'</section>'
    )


def build_field_index(terms):
    """
    <nav class="field-index"> quick-jump block.
    Links use the GUID (term_localName) as href and data-target so the JS
    filter can sync link visibility with the section.
    """
    links = []
    for term in terms:
        term_id = (term.get('term_localName', term.get('Label', 'term'))
                   .strip().replace(' ', '_'))
        label = term.get('Label', 'Unnamed Term')
        links.append(
            f'<a class="field-box" href="#{term_id}"'
            f' data-target="{term_id}">{label}</a>'
        )
    return '<nav class="field-index">' + ''.join(links) + '</nav>'


def build_category_sections(df):
    """Navigation-index section per topic category (TIME/SPACE/NAME/OTHER)."""
    col = 'IssueLabels'
    if col not in df.columns:
        return ''
    out = []
    for cat in ('TIME', 'SPACE', 'NAME', 'OTHER'):
        mask   = df[col].apply(lambda v: cat in str(v or '').upper())
        subset = df[mask]
        if subset.empty:
            continue
        terms = sorted(subset.to_dict('records'),
                        key=lambda r: r.get('Label', '').lower())
        out.append(
            f'<section class="category-section" id="cat-{cat}">\n'
            f'  <div class="class-header-wrapper"><h2>{cat}</h2></div>\n'
            f'  {build_field_index(terms)}\n'
            f'</section>\n'
        )
    return ''.join(out)


def build_category_links(df):
    """Sidebar jump-link <a> tags for each present category."""
    col = 'IssueLabels'
    if col not in df.columns:
        return ''
    links = []
    for cat in ('TIME', 'SPACE', 'NAME', 'OTHER'):
        if df[col].apply(lambda v: cat in str(v or '').upper()).any():
            links.append(f'<a class="jump-link" href="#cat-{cat}">{cat}</a>')
    return ''.join(links)


# ═══════════════════════════════════════════════════════════════════════════════
# Main entry point
# ═══════════════════════════════════════════════════════════════════════════════

def generate_qrg():
    print(f"Loading CSV from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH)
    df = df.astype(str).fillna('')

    if 'organized_in' not in df.columns:
        raise ValueError("Missing 'organized_in' column in source CSV.")

    # ── Load YAML and build template variables ──────────────────────────────
    if os.path.exists(DOC_CONFIG_PATH):
        yaml_cfg = _load_yaml(DOC_CONFIG_PATH)
    else:
        print(f"Warning: document configuration not found: {DOC_CONFIG_PATH}")
        yaml_cfg = {}

    tpl_vars = _build_template_vars(yaml_cfg)

    # ── Convert markdown templates to HTML ──────────────────────────────────
    # CHANGE 1: strip_trailing_h2 removed; the template now uses
    # <!--- START HIDE IN HTML ---> markers instead.
    header_html = convert_md_template(HEADER_MD_PATH, tpl_vars)
    footer_html = convert_md_template(FOOTER_MD_PATH, tpl_vars)

    # ── Display columns (CSV order preserved) ───────────────────────────────
    display_cols = {
        'Label', 'prefLabel', 'iri', 'Description', 'ExpectedResponse',
        'InformationElement:ActedUpon', 'aggregatesResponsesFrom',
        'InformationElement:Consulted', 'Parameters', 'AuthoritiesDefaults',
        'Notes', 'Examples', 'Type', 'UseCases', 'Resource Type',
    }
    columns = [c for c in df.columns if c.strip() and c in display_cols]

    ordered_classes = ['Amendment', 'Issue', 'Measure', 'Validation']
    grouped = dict(tuple(df.groupby('organized_in')))
    grouped = {cls: grouped[cls] for cls in ordered_classes if cls in grouped}

    unique_usecases = get_unique_values_from_column(df, 'UseCases')
    unique_ies      = get_unique_values_from_column(df, 'InformationElement:ActedUpon')

    # ── Build main content ──────────────────────────────────────────────────
    content = build_category_sections(df)

    for group, terms in grouped.items():
        anchor = group.strip().replace(' ', '_')
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

    # ── Page title for <title> element ─────────────────────────────────────
    page_title = html_lib.escape(
        tpl_vars.get('document_title',
                      tpl_vars.get('documentTitle',
                                    'BDQ Tests Quick Reference Guide'))
    )

    # ── Substitute all ###PLACEHOLDER### markers ────────────────────────────
    html_out = TEMPLATE
    html_out = html_out.replace('###PAGE_TITLE###',     page_title)
    html_out = html_out.replace('###HEADER_HTML###',    header_html)
    html_out = html_out.replace('###FOOTER_HTML###',    footer_html)
    html_out = html_out.replace('###CONTENT###',        content)
    html_out = html_out.replace('###CATEGORY_LINKS###', build_category_links(df))
    html_out = html_out.replace('###USECASE_OPTIONS###',
                                  build_usecase_options(unique_usecases))
    html_out = html_out.replace('###IE_OPTIONS###',
                                  build_select_options(unique_ies))

    # ── Write output ────────────────────────────────────────────────────────
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(html_out)
    print(f"QRG successfully written to {OUTPUT_PATH}")

    with open(DEPLOY_PATH, 'w', encoding='utf-8') as f:
        f.write(html_out)
    print(f"QRG successfully written to {DEPLOY_PATH}")


if __name__ == '__main__':
    generate_qrg()

