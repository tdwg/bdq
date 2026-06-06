from __future__ import annotations

import re
import sys
from urllib.parse import urlsplit, urlunsplit

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

# Links to rs.tdwg.org/bdq* should be handled specially until those resources are live.
# For now, use "plain" so that such IRIs are shown as text and not rendered as clickable links.
# Later this can be changed to "rewrite" for a test-rs base, or "keep" when rs.tdwg.org is ready.
BDQ_RS_PREFIX = "https://rs.tdwg.org/bdq"
BDQ_RS_MODE = "plain"  # one of: "plain", "rewrite", "keep"
BDQ_RS_BASE = "https://test-rs.tdwg.org"


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


# This function parses the inside of a markdown inline link destination/title block and separates
# the destination from an optional title. It handles:
#   dest
#   <dest>
#   dest "title"
#   <dest> "title"
#   dest 'title'
#   dest (title)
# It is scanner-based so titles containing markdown links, brackets, or parentheses do not get
# folded into the destination.
def parse_markdown_link_target(raw_target: str) -> tuple[str, str | None]:
    s = raw_target.strip()
    if not s:
        return s, None

    if s.startswith("<"):
        i = 1
        while i < len(s):
            if s[i] == ">" and s[i - 1] != "\\":
                dest = s[: i + 1]
                rest = s[i + 1 :].strip()
                return dest, rest or None
            i += 1
        return s, None

    i = 0
    while i < len(s) and not s[i].isspace():
        i += 1

    dest = s[:i]
    rest = s[i:].strip()
    return dest, rest or None


# This function rebuilds a markdown link target from a rewritten destination and an optional title,
# preserving the title text exactly as it appeared in the source.
def format_markdown_link_target(dest: str, title: str | None) -> str:
    if title:
        return f"{dest} {title}"
    return dest


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

        open_paren = token.find("(")
        if open_paren == -1 or not token.endswith(")"):
            out.append(token)
            cursor = end
            continue

        prefix = token[: open_paren + 1]
        raw_target = token[open_paren + 1 : -1]
        suffix = ")"

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