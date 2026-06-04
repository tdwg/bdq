#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import markdown


INLINE_LINK_RE = re.compile(r'(!?\[[^\]]*\]\()([^)]+)(\))')
HTML_HREF_RE = re.compile(r'(\b(?:href|src)=["\'])([^"\']+)(["\'])', re.IGNORECASE)


def first_heading_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Biodiversity Data Quality (BDQ)"


def rewrite_target(url: str) -> str:
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return url
    if not parts.path:
        return url

    path = parts.path

    if path.endswith("README.md"):
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


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


def add_heading_ids(html_text: str) -> str:
    def repl(match):
        level = match.group(1)
        attrs = match.group(2) or ""
        inner = match.group(3)
        if "id=" in attrs:
            return match.group(0)
        plain = re.sub(r"<[^>]+>", "", inner)
        hid = slugify(plain)
        return f'<h{level}{attrs} id="{hid}">{inner}</h{level}>'

    return re.sub(r"<h([1-6])([^>]*)>(.*?)</h\\1>", repl, html_text, flags=re.S)


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render_page(template: str, *, title: str, body_html: str, under_review: bool, show_toc: bool) -> str:
    review_html = (
        '<div class="review-banner" role="note" aria-label="Under review">Under Review</div>'
        if under_review else ""
    )
    toc_html = """
<aside class="doc-sidebar">
  <nav class="page-toc" aria-label="On this page">
    <h2>On this page</h2>
    <ul id="toc-list"></ul>
    <p id="toc-empty" class="toc-empty" hidden>No headings available.</p>
  </nav>
</aside>
""" if show_toc else ""

    page = template
    page = page.replace("{{PAGE_TITLE}}", html.escape(title))
    page = page.replace("{{REVIEW_BANNER}}", review_html)
    page = page.replace("{{TOC_SIDEBAR}}", toc_html)
    page = page.replace("{{BODY_HTML}}", body_html)
    return page


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", required=True)
    parser.add_argument("--template", required=True)
    args = parser.parse_args()

    site = Path(args.site_root).resolve()
    template = load_template(Path(args.template).resolve())

    md = markdown.Markdown(extensions=["extra", "tables", "fenced_code", "sane_lists"])

    # First rewrite links in source markdown and any copied html
    for path in list(site.rglob("*.md")) + list(site.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        text = rewrite_markdown_links(text)
        text = rewrite_html_links(text)
        path.write_text(text, encoding="utf-8")

    markdown_files = sorted(site.rglob("*.md"))

    for md_path in markdown_files:
        text = md_path.read_text(encoding="utf-8")

        md.reset()
        body = md.convert(text)
        body = add_heading_ids(body)

        title = first_heading_title(text)
        rel = md_path.relative_to(site).as_posix()

        if rel == "README.md":
            out_path = site / "index.html"
            under_review = False
        elif md_path.name == "README.md":
            out_path = md_path.with_name("index.html")
            under_review = rel.startswith("draft/")
        else:
            out_path = md_path.with_suffix(".html")
            under_review = rel.startswith("draft/")

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            render_page(
                template,
                title=title,
                body_html=body,
                under_review=under_review,
                show_toc=True,
            ),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()