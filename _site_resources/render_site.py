#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import markdown
from pygments.formatters import HtmlFormatter

# This script processes markdown and HTML files in the specified site root, rewriting links, replacing emoji shortcodes, for
# deployment of the Biodiversity Data Quality (BDQ) Interest Group and Standard documentation to bdq.tdwg.org.
# It converts markdown files to HTML, adds heading anchors, builds a table of contents, and renders the final pages using a provided HTML template.
# It uses a provided HTML template to render the final pages, adding features like a table of contents and review banners for draft content.
#
# @see the workflow in .github/workflows/pages.yml for how this script is used in the GitHub Actions workflow to render the site on push.
#
# @author GitHub Copilot (GPT-5.4), with guidance and manual adjustments by @chicoreus Paul J. Morris.
#

# This regex matches HTML attributes for href and src, capturing the prefix (up to the opening quote),
# the target value, and the closing quote.
HTML_HREF_RE = re.compile(r'(\b(?:href|src)=["\'])([^"\']+)(["\'])', re.IGNORECASE)

# This regex matches bare URLs in the text, capturing the URL itself.
# It matches http:// or https:// followed by non-whitespace characters, while avoiding common trailing punctuation.
BARE_URL_RE = re.compile(r'(?P<url>https?://[^\s<>()]+[^\s<>().,;:!?])')

# This regex splits a line into HTML tags and non-tag text fragments, so that text content in raw HTML lines
# can be processed without modifying the tags themselves.
HTML_TAG_RE = re.compile(r'(<[^>]+>)')

# This regex extracts the label text from a markdown link prefix like [label]( or ![alt](.
MARKDOWN_LINK_LABEL_RE = re.compile(r'!?\[([^\]]*)\]\($')

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

# Links to rs.tdwg.org/bdq* should be handled specially until those resources are live.
# For now, use "plain" so that such IRIs are shown as text and not rendered as clickable links.
# Later this can be changed to "rewrite" for a test-rs base, or "keep" when rs.tdwg.org is ready.
BDQ_RS_PREFIX = "https://rs.tdwg.org/bdq"
BDQ_RS_MODE = "plain"  # one of: "plain", "rewrite", "keep"
BDQ_RS_BASE = "https://test-rs.tdwg.org"


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


# This function returns True if a URL is in the BDQ rs.tdwg.org namespace that needs temporary special handling.
def is_bdq_rs_uri(url: str) -> bool:
    return url.startswith(BDQ_RS_PREFIX)


# This function applies the configured policy for BDQ rs.tdwg.org IRIs.
# - "keep": leave the URI unchanged
# - "rewrite": rewrite the rs.tdwg.org base to a configured test-rs base
# - "plain": return the original URI string; link suppression is handled by the caller
def rewrite_bdq_rs_uri(url: str) -> str:
    if BDQ_RS_MODE == "keep":
        return url
    if BDQ_RS_MODE == "rewrite":
        return url.replace("https://rs.tdwg.org", BDQ_RS_BASE, 1)
    return url


# This function safely parses a URL value. If urllib cannot parse it because of malformed
# bracket usage or other invalid URL structure, return None so the caller can preserve the
# original text instead of crashing the site build.
def safe_urlsplit(url: str):
    try:
        return urlsplit(url)
    except ValueError:
        print(f"Warning: invalid URL skipped during rewrite: {url}", file=sys.stderr)
        return None


# This function rewrites a URL target according to the specified rules, handling markdown links and special cases for certain filenames.
# If the URL cannot be parsed, it is returned unchanged so malformed content does not abort the build.
def rewrite_target(url: str) -> str:
    if is_bdq_rs_uri(url):
        return rewrite_bdq_rs_uri(url)

    parts = safe_urlsplit(url)
    if parts is None:
        return url

    if parts.scheme or parts.netloc:
        return url
    if not parts.path:
        return url

    path = parts.path

    if path.endswith("bdqffdq.owl"):
        # the OWL file is renamed to .ttl so that the content type is correctly recognized when delivered from the site.
        new_path = path[:-3] + "ttl"
    elif path.endswith("README.md"):
        new_path = path[:-9] + "index.html"
    elif path.endswith(".md"):
        new_path = path[:-3] + ".html"
    else:
        new_path = path

    return urlunsplit(("", "", new_path, parts.query, parts.fragment))


# This function parses the inside of a markdown inline link destination and separates the destination from an optional title.
# It handles:
#   dest
#   <dest>
#   dest "title"
#   <dest> "title"
#   dest 'title'
# It intentionally favors simple, forgiving parsing over strict CommonMark completeness so existing BDQ content is preserved.
def parse_markdown_link_target(raw_target: str) -> tuple[str, str | None]:
    s = raw_target.strip()
    if not s:
        return s, None

    if s.startswith("<"):
        close = s.find(">")
        if close != -1:
            dest = s[: close + 1]
            rest = s[close + 1 :].strip()
            return dest, rest or None
        return s, None

    # Walk from the end looking for a plausible quoted title.
    if len(s) >= 2 and s[-1] in {'"', "'"}:
        quote = s[-1]
        i = len(s) - 2
        while i >= 0:
            if s[i] == quote and (i == 0 or s[i - 1] != "\\"):
                maybe_dest = s[:i].rstrip()
                maybe_title = s[i:].strip()
                if maybe_dest:
                    return maybe_dest, maybe_title
            i -= 1

    m = re.match(r'^(\S+)(?:\s+(.+))?$', s)
    if not m:
        return s, None

    dest = m.group(1)
    title = m.group(2).strip() if m.group(2) else None
    return dest, title


# This function rebuilds a markdown link target from a rewritten destination and an optional title,
# preserving the title text exactly as it appeared in the source.
def format_markdown_link_target(dest: str, title: str | None) -> str:
    if title:
        return f"{dest} {title}"
    return dest


# This helper finds the index of the matching closing ] for a markdown link/image label starting at start_idx.
# It supports nested square brackets in the label text.
def find_matching_square_bracket(text: str, start_idx: int) -> int:
    depth = 0
    i = start_idx
    while i < len(text):
        ch = text[i]
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


# This helper finds the index of the matching closing ) for a markdown inline link destination/title block.
# It supports:
# - nested parentheses in bare destinations
# - angle-bracket destinations <...>
# - quoted titles after the destination
# It is a lightweight scanner, not a full CommonMark parser, but is much more robust than a simple regex.
def find_matching_paren(text: str, start_idx: int) -> int:
    depth = 0
    in_angle = False
    in_quote: str | None = None
    i = start_idx

    while i < len(text):
        ch = text[i]

        if in_quote is not None:
            if ch == in_quote and (i == 0 or text[i - 1] != "\\"):
                in_quote = None
            i += 1
            continue

        if in_angle:
            if ch == ">":
                in_angle = False
            i += 1
            continue

        if ch == "<":
            in_angle = True
        elif ch in {'"', "'"}:
            in_quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return i

        i += 1

    return -1


# This function scans a line of markdown and returns spans for inline links and images of the form
# [label](target) and ![alt](target). It is used both for rewriting links and for masking existing
# links before bare-URL processing, so the same notion of "existing link" is used consistently.
def find_markdown_inline_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    i = 0

    while i < len(text):
        start = i

        if text[i] == "!" and i + 1 < len(text) and text[i + 1] == "[":
            label_start = i + 1
        elif text[i] == "[":
            label_start = i
        else:
            i += 1
            continue

        label_end = find_matching_square_bracket(text, label_start)
        if label_end == -1:
            i += 1
            continue

        if label_end + 1 >= len(text) or text[label_end + 1] != "(":
            i = label_end + 1
            continue

        paren_start = label_end + 1
        paren_end = find_matching_paren(text, paren_start)
        if paren_end == -1:
            i = label_end + 1
            continue

        spans.append((start, paren_end + 1))
        i = paren_end + 1

    return spans


# This function masks existing markdown inline links/images in a text fragment so subsequent regex-based
# processing does not rewrite their destinations or visible text a second time.
def mask_markdown_inline_spans(text: str) -> tuple[str, list[str]]:
    spans = find_markdown_inline_spans(text)
    if not spans:
        return text, []

    masked_parts: list[str] = []
    originals: list[str] = []
    cursor = 0

    for idx, (start, end) in enumerate(spans):
        masked_parts.append(text[cursor:start])
        originals.append(text[start:end])
        masked_parts.append(f"@@LINK{idx}@@")
        cursor = end

    masked_parts.append(text[cursor:])
    return "".join(masked_parts), originals


# This function restores previously masked markdown inline links/images.
def unmask_markdown_inline_spans(text: str, originals: list[str]) -> str:
    if not originals:
        return text
    return re.sub(r"@@LINK(\d+)@@", lambda m: originals[int(m.group(1))], text)


# This function rewrites markdown inline links/images in a line using the inline scanner, converting .md links to .html
# and handling angle-bracketed links as well. It also suppresses links to BDQ rs.tdwg.org IRIs when BDQ_RS_MODE is "plain",
# leaving only their visible text. It preserves optional markdown link titles.
def rewrite_markdown_links(text: str) -> str:
    spans = find_markdown_inline_spans(text)
    if not spans:
        return text

    out: list[str] = []
    cursor = 0

    for start, end in spans:
        out.append(text[cursor:start])
        token = text[start:end]

        m = re.match(r'(?P<prefix>!?\[.*\]\()(?P<raw_target>.*)(?P<suffix>\))$', token, flags=re.S)
        if not m:
            out.append(token)
            cursor = end
            continue

        prefix = m.group("prefix")
        raw_target = m.group("raw_target")
        suffix = m.group("suffix")

        label_match = MARKDOWN_LINK_LABEL_RE.match(prefix)
        label = label_match.group(1) if label_match else ""

        dest, title = parse_markdown_link_target(raw_target)

        if dest.startswith("<") and dest.endswith(">"):
            inner = dest[1:-1].strip()
            if is_bdq_rs_uri(inner) and BDQ_RS_MODE == "plain":
                out.append(label if label else inner)
            else:
                rewritten_inner = rewrite_target(inner)
                out.append(f"{prefix}{format_markdown_link_target(f'<{rewritten_inner}>', title)}{suffix}")
        else:
            if is_bdq_rs_uri(dest) and BDQ_RS_MODE == "plain":
                out.append(label if label else dest)
            else:
                rewritten_dest = rewrite_target(dest)
                out.append(f"{prefix}{format_markdown_link_target(rewritten_dest, title)}{suffix}")

        cursor = end

    out.append(text[cursor:])
    return "".join(out)


# Similar logic to rewrite_markdown_links, but for HTML attributes like href and src.
# In plain mode for BDQ rs.tdwg.org IRIs, the href/src is left unchanged here; suppression of whole HTML anchors
# requires structural HTML rewriting and is intentionally not attempted in this attribute-only pass.
def rewrite_html_links(text: str) -> str:
    def repl(match):
        prefix, target, suffix = match.groups()
        stripped_target = target.strip()
        if is_bdq_rs_uri(stripped_target) and BDQ_RS_MODE == "plain":
            return f"{prefix}{stripped_target}{suffix}"
        return f"{prefix}{rewrite_target(stripped_target)}{suffix}"

    return HTML_HREF_RE.sub(repl, text)


# This function converts bare URLs in a plain Markdown text line into explicit Markdown links.
# It skips inline code spans delimited by backticks so that URLs inside code are not changed.
# It masks existing Markdown links before processing so URLs already present as link destinations
# are not rewritten a second time.
# It also suppresses linking for BDQ rs.tdwg.org IRIs in plain mode, leaving them visible as plain text.
# This is useful because some bare URLs are not autolinked consistently by the Markdown parser in all contexts.
def linkify_bare_urls_in_markdown_line(line: str) -> str:
    if "http://" not in line and "https://" not in line:
        return line

    parts = re.split(r'(`[^`]*`)', line)
    linked_parts = []

    for part in parts:
        if part.startswith("`") and part.endswith("`"):
            linked_parts.append(part)
            continue

        masked, originals = mask_markdown_inline_spans(part)

        def repl(match):
            url = match.group("url")
            if is_bdq_rs_uri(url) and BDQ_RS_MODE == "plain":
                return url
            rewritten_url = rewrite_target(url)
            return f'[{rewritten_url}]({rewritten_url})'

        masked = BARE_URL_RE.sub(repl, masked)
        masked = unmask_markdown_inline_spans(masked, originals)
        linked_parts.append(masked)

    return "".join(linked_parts)


# This function converts bare URLs in a line containing raw HTML into explicit HTML anchor tags.
# It splits the line into HTML tags and text fragments, preserving the tags unchanged while only
# linkifying URLs in the text content between tags. This avoids inserting Markdown link syntax
# into raw HTML blocks such as <li>...</li>, where Python-Markdown would otherwise leave it literal.
# It also masks existing Markdown inline links inside text fragments so their destinations are not
# rewritten a second time.
# It also suppresses linking for BDQ rs.tdwg.org IRIs in plain mode, leaving them visible as plain text.
def linkify_bare_urls_in_html_line(line: str) -> str:
    pieces = HTML_TAG_RE.split(line)
    result = []

    for piece in pieces:
        if not piece:
            continue

        if piece.startswith("<") and piece.endswith(">"):
            result.append(piece)
            continue

        # Protect existing markdown links in HTML text fragments.
        masked, originals = mask_markdown_inline_spans(piece)

        def repl(match):
            url = match.group("url")
            if is_bdq_rs_uri(url) and BDQ_RS_MODE == "plain":
                return url
            rewritten_url = rewrite_target(url)
            return f'<a href="{rewritten_url}">{rewritten_url}</a>'

        masked = BARE_URL_RE.sub(repl, masked)
        masked = unmask_markdown_inline_spans(masked, originals)
        result.append(masked)

    return "".join(result)

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
        # Retain second-level headings support for easy restoration later.
        # elif level_num == 3:
        #     items.append(f'<li class="toc-h3"><a href="#{escaped_hid}">{escaped_text}</a></li>')

    return "\n".join(items)


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# This function determines the context for rendering a page based on its relative path.
# If the path indicates that it's part of the draft section, it sets the context accordingly,
# including different header titles and sidebar content. Otherwise, it returns the context for regular pages.
# TODO: On ratification, /draft/ will move to /bdq/ and the logic here will need to be updated.
def page_context(rel: str) -> dict[str, str | bool]:
    # TODO: On ratification, this will change to rel.startswith("bdq/").
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

    # Configure the Markdown parser with the desired extensions and settings.
    # extra and tables are used for GitHub-style markdown features like tables and definition lists.
    # fenced_code and codehilite is used for syntax highlighting of fenced code blocks, with Pygments as the highlighter.
    # pymdownx.tilde is used to support strikethrough with ~~text~~ syntax.
    # sane_lists is included to make list parsing more consistent, but we
    #   also apply custom normalization to handle edge cases with GitHub's markdown rendering.
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

    pygments_css = HtmlFormatter(style="friendly").get_style_defs(".highlight")
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
            # Special case to render the draft README.md and index.md as separate files
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
