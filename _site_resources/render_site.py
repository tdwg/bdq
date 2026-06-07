#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter
from pygments.styles.friendly import FriendlyStyle 
from pygments.token import Token

from render_site_links import (
    linkify_bare_urls_in_html_line,
    linkify_bare_urls_in_markdown_line,
    rewrite_html_links,
    rewrite_markdown_links,
)

# This script processes markdown and HTML files in the specified site root, rewriting links, replacing emoji shortcodes, for
# deployment of the Biodiversity Data Quality (BDQ) Interest Group and Standard documentation to bdq.tdwg.org.
# It converts markdown files to HTML, adds heading anchors, builds a table of contents, and renders the final pages using a provided HTML template.
# It uses a provided HTML template to render the site, adding features like a table of contents and review banners for draft content.
#
# @see the workflow in .github/workflows/pages.yml for how this script is used in the GitHub Actions workflow to render the site on push.
#
# @author GitHub Copilot (GPT-5.4), with guidance and manual adjustments by @chicoreus Paul J. Morris.
#

EMOJI_MAP = {
    ":green_book:": "📗",
    ":blue_book:": "📘",
    ":orange_book:": "📙",
    ":closed_book:": "📕",
    ":book:": "📖",
    ":books:": "📚",
    ":notebook:": "📓",
    ":warning:": "⚠️",
    ":information_source:": "ℹ️",
    ":white_check_mark:": "✅",
    ":x:": "❌",
    ":construction:": "🚧",
    ":hammer_and_wrench:": "🛠️",
    ":memo:": "📝",
    ":rocket:": "🚀",
    ":bulb:": "💡",
    ":link:": "🔗",
}


# This function extracts the title for the page from the first level-1 heading in the markdown text,
# stripping out any markdown link syntax. If no such heading is found, it returns a default title.
def first_heading_title(text: str) -> str:
    def strip_markdown_links(s: str) -> str:
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
        s = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", s)
        return s.strip()

    for line in text.splitlines():
        if line.startswith("# "):
            return strip_markdown_links(line[2:].strip())

    return "Biodiversity Data Quality (BDQ)"


# This function applies bare-URL linkification to a whole Markdown document before Markdown conversion.
# It skips fenced code blocks entirely. For ordinary Markdown lines it produces Markdown links, while for
# lines containing raw HTML it produces HTML anchor tags in the text nodes between tags.
def linkify_bare_urls(text: str) -> str:
    lines = text.splitlines()
    result = []

    fenced_re = re.compile(r"^([ \t]*)(```|~~~)")
    in_fence = False
    fence_marker = None

    for line in lines:
        fence_match = fenced_re.match(line)
        if fence_match:
            marker = fence_match.group(2)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            result.append(line)
            continue

        if in_fence:
            result.append(line)
            continue

        if "<" in line and ">" in line:
            result.append(linkify_bare_urls_in_html_line(line))
        else:
            result.append(linkify_bare_urls_in_markdown_line(line))

    return "\n".join(result)


# A simple function to replace emoji shortcodes with their corresponding Unicode characters.
def replace_emoji_shortcodes(text: str) -> str:
    for shortcode, glyph in EMOJI_MAP.items():
        text = text.replace(shortcode, glyph)
    return text


# Slugify function inspired by GitHub's algorithm, with an option to preserve case for better readability of anchors.
def slugify(text: str, *, preserve_case: bool = True) -> str:
    text = text.strip()
    if not preserve_case:
        text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


# Python-Markdown with sane_lists is stricter than GitHub's renderer. A top-level list that directly
# follows paragraph text may not be recognized as a list. This function inserts a blank line only
# before top-level lists, preserving nested list structure.
def ensure_blank_line_before_top_level_lists(text: str) -> str:
    lines = text.splitlines()
    result = []

    unordered_re = re.compile(r"^([ \t]*)([*+-])\s+.+$")
    ordered_re = re.compile(r"^([ \t]*)\d+\.\s+.+$")
    fenced_re = re.compile(r"^([ \t]*)(```|~~~)")
    atx_heading_re = re.compile(r"^[ \t]{0,3}#{1,6}\s+")
    blockquote_re = re.compile(r"^[ \t]{0,3}>\s?")
    html_block_re = re.compile(r"^[ \t]*<[^>]+>")
    blank_re = re.compile(r"^[ \t]*$")

    in_fence = False
    fence_marker = None

    for line in lines:
        fence_match = fenced_re.match(line)
        if fence_match:
            marker = fence_match.group(2)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            result.append(line)
            continue

        if in_fence:
            result.append(line)
            continue

        unordered_match = unordered_re.match(line)
        ordered_match = ordered_re.match(line)
        is_list = unordered_match or ordered_match

        if is_list:
            indent = len((unordered_match or ordered_match).group(1))
            is_top_level = indent == 0

            if is_top_level and result:
                prev = result[-1]
                prev_stripped = prev.strip()

                prev_is_block = (
                    blank_re.match(prev)
                    or atx_heading_re.match(prev)
                    or blockquote_re.match(prev)
                    or html_block_re.match(prev)
                    or unordered_re.match(prev)
                    or ordered_re.match(prev)
                )

                if prev_stripped and not prev_is_block:
                    result.append("")

        result.append(line)

    return "\n".join(result)


# Python-Markdown is stricter than GitHub about nested list indentation.
# Normalize nested list indentation to multiples of 4 spaces while preserving top-level items.
def normalize_nested_list_indentation(text: str) -> str:
    lines = text.splitlines()
    result = []

    unordered_re = re.compile(r"^([ \t]*)([*+-])(\s+.+)$")
    ordered_re = re.compile(r"^([ \t]*)(\d+\.)(\s+.+)$")
    fenced_re = re.compile(r"^([ \t]*)(```|~~~)")

    in_fence = False
    fence_marker = None

    for line in lines:
        fence_match = fenced_re.match(line)
        if fence_match:
            marker = fence_match.group(2)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            result.append(line)
            continue

        if in_fence:
            result.append(line)
            continue

        m_unordered = unordered_re.match(line)
        m_ordered = ordered_re.match(line)

        if m_unordered:
            indent, bullet, rest = m_unordered.groups()
            indent_len = len(indent.replace("\t", "    "))
            if indent_len > 0:
                level = max(1, indent_len // 2)
                indent = " " * (level * 4)
            result.append(f"{indent}{bullet}{rest}")
        elif m_ordered:
            indent, marker, rest = m_ordered.groups()
            indent_len = len(indent.replace("\t", "    "))
            if indent_len > 0:
                level = max(1, indent_len // 2)
                indent = " " * (level * 4)
            result.append(f"{indent}{marker}{rest}")
        else:
            result.append(line)

    return "\n".join(result)


# Apply Markdown list normalization steps in sequence.
def normalize_markdown_lists(text: str) -> str:
    text = ensure_blank_line_before_top_level_lists(text)
    text = normalize_nested_list_indentation(text)
    return text


# This function adds id attributes to heading tags in the HTML, generating anchors based on the text content of the headings.
def add_heading_ids(html_text: str) -> str:
    def repl(match):
        level = match.group(1)
        attrs = match.group(2) or ""
        inner = match.group(3)

        plain = re.sub(r"<[^>]+>", "", inner).strip()
        primary_anchor = slugify(plain, preserve_case=True)
        lower_anchor = slugify(plain, preserve_case=False)

        anchors = [
            f'<a id="{primary_anchor}" class="anchor-target" aria-hidden="true"></a>'
        ]
        if lower_anchor != primary_anchor:
            anchors.append(
                f'<a id="{lower_anchor}" class="anchor-target" aria-hidden="true"></a>'
            )

        if "id=" in attrs:
            heading_html = f'<h{level}{attrs}>{inner}</h{level}>'
        else:
            heading_html = f'<h{level}{attrs} id="{primary_anchor}">{inner}</h{level}>'

        return "".join(anchors) + heading_html

    return re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", repl, html_text, flags=re.S)


# This function builds the HTML for the table of contents by extracting headings from
# the body HTML and creating a list of links to those headings.
def build_toc_html(body_html: str) -> str:
    headings = re.findall(r"<h([1-6])[^>]*id=[\"']([^\"']+)[\"'][^>]*>(.*?)</h\1>", body_html, flags=re.S)

    items = []

    for level, hid, inner in headings:
        level_num = int(level)
        text = re.sub(r"<[^>]+>", "", inner).strip()
        escaped_text = html.escape(text)
        escaped_hid = html.escape(hid)

        if level_num == 2:
            items.append(f'<li><a href="#{escaped_hid}">{escaped_text}</a></li>')

    return "\n".join(items)


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# This function determines the context for rendering a page based on its relative path.
# If the path indicates that it's part of the draft section, it sets the context accordingly,
# including different header titles and sidebar content. Otherwise, it returns the context for regular pages.
# TODO: On ratification, /draft/ will move to /bdq/ and the logic here will need to be updated.
def page_context(rel: str) -> dict[str, str | bool]:
    is_draft = rel.startswith("draft/")

    if is_draft:
        return {
            "is_draft": True,
            "site_header_title": "The Biodiversity Data Quality (BDQ) Standard",
            "site_header_tagline": "Draft of the TDWG Biodiversity Data Quality Standard",
            "site_header_link": "https://bdq.tdwg.org/bdq/",
            "sidebar_context_html": """
<div class="sidebar-context">
  <h2>BDQ Standard</h2>
  <ul class="sidebar-context-links">
    <li><a href="https://bdq.tdwg.org/draft/">Landing page</a></li>
    <li><a href="https://bdq.tdwg.org/draft/#2-A-Roadmap-to-the-BDQ-Standard-non-normative">🧭 Roadmap to the Standard</a></li>
    <li><a href="https://bdq.tdwg.org/draft/README.html">Public Review</a></li>
  </ul>
</div>
""",
        }

    return {
        "is_draft": False,
        "site_header_title": "Biodiversity Data Quality (BDQ)",
        "site_header_tagline": "The TDWG Biodiversity Data Quality Interest Group and Task Groups",
        "site_header_link": "https://bdq.tdwg.org/",
        "sidebar_context_html": """
<div class="sidebar-context">
  <ul class="sidebar-context-links">
    <li><a href="https://bdq.tdwg.org/">BDQ Interest Group</a></li>
  </ul>
</div>
""",
    }


# This function takes the template and various pieces of content and context, and renders the
# final HTML page by replacing placeholders in the template with the provided content.
# It also conditionally includes a review banner and a table of contents sidebar based on the context.
def render_page(
    template: str,
    *,
    title: str,
    body_html: str,
    toc_items_html: str,
    under_review: bool,
    show_toc: bool,
    header_title: str,
    header_tagline: str,
    header_link: str,
    sidebar_context_html: str,
) -> str:
    review_html = (
        '<div class="review-banner" role="note" aria-label="Under review">Under Review</div>'
        if under_review else ""
    )
    toc_html = """
<aside class="doc-sidebar">
  {{SIDEBAR_CONTEXT}}
  <nav class="page-toc" aria-label="On this page">
    <h2>On this page</h2>
    <ul id="toc-list">
{{TOC_ITEMS}}
    </ul>
    <p id="toc-empty" class="toc-empty" hidden>No headings available.</p>
  </nav>
</aside>
""" if show_toc else ""

    if show_toc:
        toc_html = toc_html.replace("{{TOC_ITEMS}}", toc_items_html)
        toc_html = toc_html.replace("{{SIDEBAR_CONTEXT}}", sidebar_context_html)

    page = template
    page = page.replace("{{PAGE_TITLE}}", html.escape(title))
    page = page.replace("{{REVIEW_BANNER}}", review_html)
    page = page.replace("{{TOC_SIDEBAR}}", toc_html)
    page = page.replace("{{BODY_HTML}}", body_html)
    page = page.replace("{{SITE_HEADER_TITLE}}", html.escape(header_title))
    page = page.replace("{{SITE_HEADER_TAGLINE}}", html.escape(header_tagline))
    page = page.replace("{{SITE_HEADER_LINK}}", html.escape(header_link))
    return page


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", required=True)
    parser.add_argument("--template", required=True)
    args = parser.parse_args()

    site = Path(args.site_root).resolve()
    template = load_template(Path(args.template).resolve())

    md = markdown.Markdown(
        extensions=[
            "extra",
            "tables",
            "fenced_code",
            "sane_lists",
            "codehilite",
            "md_in_html",
            "pymdownx.tilde",
        ],
        extension_configs={
            "codehilite": {
                "guess_lang": False,
                "use_pygments": True,
                "css_class": "highlight",
                "noclasses": False,
            },
            "pymdownx.tilde": {
                "subscript": False,
            },
        },
    )

    for path in list(site.rglob("*.md")) + list(site.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        text = rewrite_markdown_links(text)
        text = rewrite_html_links(text)
        text = replace_emoji_shortcodes(text)

        if path.suffix == ".md":
            text = normalize_markdown_lists(text)
            text = linkify_bare_urls(text)

        path.write_text(text, encoding="utf-8")

    class FriendlyNoErrorStyle(FriendlyStyle):
        styles = {**FriendlyStyle.styles, Token.Error: ""}

    pygments_css = HtmlFormatter(style=FriendlyNoErrorStyle).get_style_defs(".highlight")
    pygments_css_path = site / "assets" / "css" / "pygments.css"
    pygments_css_path.write_text(pygments_css, encoding="utf-8")

    markdown_files = sorted(site.rglob("*.md"))

    for md_path in markdown_files:
        text = md_path.read_text(encoding="utf-8")

        md.reset()
        body = md.convert(text)
        body = add_heading_ids(body)
        toc_items_html = build_toc_html(body)

        title = first_heading_title(text)
        rel = md_path.relative_to(site).as_posix()
        ctx = page_context(rel)

        if rel == "README.md":
            out_path = site / "index.html"
        elif rel == "draft/README.md":
            out_path = site / "draft" / "README.html"
        elif md_path.name == "README.md":
            out_path = md_path.with_name("index.html")
        else:
            out_path = md_path.with_suffix(".html")

        rendered = render_page(
            template,
            title=title,
            body_html=body,
            toc_items_html=toc_items_html,
            under_review=bool(ctx["is_draft"]),
            show_toc=True,
            header_title=str(ctx["site_header_title"]),
            header_tagline=str(ctx["site_header_tagline"]),
            header_link=str(ctx["site_header_link"]),
            sidebar_context_html=str(ctx["sidebar_context_html"]),
        )

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
