#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import markdown
from pygments.formatters import HtmlFormatter


INLINE_LINK_RE = re.compile(r'(!?\[[^\]]*\]\()([^)]+)(\))')
HTML_HREF_RE = re.compile(r'(\b(?:href|src)=["\'])([^"\']+)(["\'])', re.IGNORECASE)

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


def first_heading_title(text: str) -> str:
    def strip_markdown_links(s: str) -> str:
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
        s = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", s)
        return s.strip()

    for line in text.splitlines():
        if line.startswith("# "):
            return strip_markdown_links(line[2:].strip())

    return "Biodiversity Data Quality (BDQ)"


def rewrite_target(url: str) -> str:
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return url
    if not parts.path:
        return url

    path = parts.path

    if path.endswith("bdqffdq.owl"):
        new_path = path[:-3] + "ttl"
    elif path.endswith("README.md"):
        new_path = path[:-9] + "index.html"
    elif path.endswith(".md"):
        new_path = path[:-3] + ".html"
    else:
        new_path = path

    return urlunsplit(("", "", new_path, parts.query, parts.fragment))


def rewrite_markdown_links(text: str) -> str:
    def repl(match):
        prefix, target, suffix = match.groups()
        target = target.strip()
        if target.startswith("<") and target.endswith(">"):
            inner = target[1:-1].strip()
            return f"{prefix}<{rewrite_target(inner)}>{suffix}"
        return f"{prefix}{rewrite_target(target)}{suffix}"

    return INLINE_LINK_RE.sub(repl, text)


def rewrite_html_links(text: str) -> str:
    def repl(match):
        prefix, target, suffix = match.groups()
        return f"{prefix}{rewrite_target(target.strip())}{suffix}"

    return HTML_HREF_RE.sub(repl, text)


def replace_emoji_shortcodes(text: str) -> str:
    for shortcode, glyph in EMOJI_MAP.items():
        text = text.replace(shortcode, glyph)
    return text


def slugify(text: str, *, preserve_case: bool = True) -> str:
    text = text.strip()
    if not preserve_case:
        text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


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


def page_context(rel: str) -> dict[str, str | bool]:
    is_draft = rel.startswith("draft/")

    if is_draft:
        return {
            "is_draft": True,
            "site_header_title": "The Biodiversity Data Quality (BDQ) Standard",
            "site_header_tagline": "Draft of the TDWG Biodiversity Data Quality Standard",
            "site_header_link": "https://bdq.tdwg.org/bdq/",
        }

    return {
        "is_draft": False,
        "site_header_title": "Biodiversity Data Quality (BDQ)",
        "site_header_tagline": "The TDWG Biodiversity Data Quality Interest Group and Task Groups",
        "site_header_link": "https://bdq.tdwg.org/",
    }


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
) -> str:
    review_html = (
        '<div class="review-banner" role="note" aria-label="Under review">Under Review</div>'
        if under_review else ""
    )
    toc_html = """
<aside class="doc-sidebar">
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
        ],
        extension_configs={
            "codehilite": {
                "guess_lang": False,
                "use_pygments": True,
                "css_class": "highlight",
                "noclasses": False,
            }
        },
    )

    for path in list(site.rglob("*.md")) + list(site.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        text = rewrite_markdown_links(text)
        text = rewrite_html_links(text)
        text = replace_emoji_shortcodes(text)
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
        )

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
