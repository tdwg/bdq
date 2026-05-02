#!/usr/bin/env python3
"""
Post-process selected generated Markdown files under tg2/_review/ to add links/tooltips.

Vocabulary linking: qualified forms only, inside inline code, e.g. `bdqffdq:InformationElement`.
Glossary linking: plain-text first occurrence, linking to anchors in _review/index.md.

@author GitHub Copilot with review and adjustments by Paul J. Morris @chicoreus

PROTECTED / DO-NOT-REWRITE AREAS
===============================
- Anything before section 2 begins (before first heading "## 2 ...").
- Any blacklisted section ranges (configurable per file).
- Markdown headings (lines starting with '#').
- Fenced code blocks ```...```.
- Markdown tables (pipe tables): contiguous runs of table lines.
- HTML <li>...</li> blocks: contiguous region from a line containing "<li" up to a line containing "</li>".
  (Conservative: if list items are nested/multiline, we protect the whole block.)

Also:
- Never modify existing markdown links [...](...).
- Only first eligible occurrence per (file, term) is linked.

ONLY THESE FILES ARE PROCESSED
==============================
- ../_review/docs/tutorial/index.md
- ../_review/index.md
- ../_review/docs/guide/bdqtest/index.md
- ../_review/docs/guide/users/index.md
- ../_review/docs/guide/implementers/index.md
- ../_review/docs/guide/bdqffdq/index.md
- ../_review/docs/supplement/index.md

Run from tg2/_build_review/:
  python3 postprocess_autolink_terms.py --dry-run
  python3 postprocess_autolink_terms.py

Dependencies:
  pip install rdflib
"""

from __future__ import annotations

import argparse
import csv
import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import rdflib
from rdflib import Graph, Namespace
from rdflib.namespace import SKOS


# -----------------------------
# Configuration / assumptions
# -----------------------------

BDQFFDQ_NS = "https://rs.tdwg.org/bdqffdq/terms/"
BDQFFDQ = Namespace(BDQFFDQ_NS)

TITLE_MAX_CHARS = 220
TERMLIST_DOC_DIR = "list"  # under ../_review/docs/


def ANCHOR_FN(local_name: str) -> str:
    """Anchor convention assumption: lowercased term_localName."""
    return local_name.lower()


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def safe_title(s: str) -> str:
    s = normalize_ws(html.unescape(s))
    if len(s) > TITLE_MAX_CHARS:
        s = s[: TITLE_MAX_CHARS - 1].rstrip() + "…"
    return s.replace('"', "'")


def glossary_anchor(label: str) -> str:
    a = re.sub(r"[^a-z0-9]+", "-", label.lower())
    a = re.sub(r"-{2,}", "-", a).strip("-")
    return a


@dataclass(frozen=True)
class QualifiedTerm:
    prefix: str
    local_name: str
    qname: str
    definition: str
    href_from_docs_root: str  # list/<prefix>/index.md#<anchor>


@dataclass(frozen=True)
class GlossaryTerm:
    term: str
    definition: str
    anchor: str


# -----------------------------
# Load vocabularies
# -----------------------------

def load_bdqffdq_qualified_terms(owl_path: Path) -> Dict[str, QualifiedTerm]:
    g = Graph()
    g.parse(str(owl_path), format="turtle")

    out: Dict[str, QualifiedTerm] = {}
    for subj, _, defn in g.triples((None, SKOS.definition, None)):
        s = str(subj)
        if not s.startswith(BDQFFDQ_NS):
            continue
        local = s.replace(BDQFFDQ_NS, "")
        qname = f"bdqffdq:{local}"
        out[qname] = QualifiedTerm(
            prefix="bdqffdq",
            local_name=local,
            qname=qname,
            definition=safe_title(str(defn)),
            href_from_docs_root=f"{TERMLIST_DOC_DIR}/bdqffdq/index.md#{ANCHOR_FN(local)}",
        )
    return out


def load_term_versions_csv(csv_path: Path, prefix: str) -> Dict[str, QualifiedTerm]:
    if not csv_path.exists():
        return {}

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        if "term_localName" not in fieldnames:
            raise SystemExit(f"ERROR: {csv_path} missing required column 'term_localName'. Found: {fieldnames}")
        if "definition" not in fieldnames:
            raise SystemExit(f"ERROR: {csv_path} missing required column 'definition'. Found: {fieldnames}")

        out: Dict[str, QualifiedTerm] = {}
        for row in reader:
            local = (row.get("term_localName") or "").strip()
            if not local:
                continue
            qname = f"{prefix}:{local}"
            out[qname] = QualifiedTerm(
                prefix=prefix,
                local_name=local,
                qname=qname,
                definition=safe_title(row.get("definition") or ""),
                href_from_docs_root=f"{TERMLIST_DOC_DIR}/{prefix}/index.md#{ANCHOR_FN(local)}",
            )
        return out


# -----------------------------
# Load glossary terms from landing page table (_review/index.md)
# -----------------------------

_GLOSSARY_ROW_RE = re.compile(
    r"^\|\s*(?P<label>[^|]+?)\s*\|\s*(?P<definition>[^|]+?)\s*\|\s*(?P<context>[^|]+?)\s*\|\s*$"
)

def load_glossary_terms_from_landing(landing_md_path: Path) -> Dict[str, GlossaryTerm]:
    if not landing_md_path.exists():
        return {}

    lines = landing_md_path.read_text(encoding="utf-8").splitlines()

    header_idx = None
    for i, line in enumerate(lines):
        if "| **Label** |" in line and "| **Definition** |" in line and "| **Context** |" in line:
            header_idx = i
            break
    if header_idx is None:
        return {}

    terms: Dict[str, GlossaryTerm] = {}
    for line in lines[header_idx + 2 :]:
        if not line.strip().startswith("|"):
            break
        m = _GLOSSARY_ROW_RE.match(line.strip())
        if not m:
            continue
        label = normalize_ws(m.group("label"))
        definition = safe_title(m.group("definition"))
        if not label or label == "**Label**":
            continue
        terms[label] = GlossaryTerm(term=label, definition=definition, anchor=glossary_anchor(label))

    return terms


# -----------------------------
# Markdown protections / parsing helpers
# -----------------------------

FENCE_START_RE = re.compile(r"^\s*```")
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
LINK_SPAN_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")  # coarse "existing link" detector
HEADING_LINE_RE = re.compile(r"^\s*#")
SECTION2_START_RE = re.compile(r"^\s*##\s*2(?:\s|[.\-])")
SECTION_START_RE = re.compile(r"^\s*(#+)\s+(.+?)\s*$")


def split_fenced_blocks(md: str) -> List[Tuple[bool, str]]:
    """Return list of (is_fenced, chunk)."""
    out: List[Tuple[bool, str]] = []
    lines = md.splitlines(keepends=True)
    in_fence = False
    buf: List[str] = []

    def flush(flag: bool):
        nonlocal buf
        if buf:
            out.append((flag, "".join(buf)))
            buf = []

    for line in lines:
        if FENCE_START_RE.match(line):
            buf.append(line)
            flush(in_fence)
            in_fence = not in_fence
            continue
        buf.append(line)

    flush(in_fence)
    return out


def rel_href(from_file: Path, target_path: Path) -> str:
    from_dir = from_file.parent.resolve()
    target_path = target_path.resolve()
    try:
        return str(target_path.relative_to(from_dir)).replace("\\", "/")
    except Exception:
        return str(target_path).replace("\\", "/")


# -----------------------------
# Table detection (protect tables like fenced code blocks)
# -----------------------------

def is_table_line(line: str) -> bool:
    """
    True if line looks like part of a Markdown pipe table.
    We protect contiguous runs of such lines.
    """
    s = line.strip()
    if not s:
        return False
    if "|" not in s:
        return False
    return s.startswith("|") or s.endswith("|")


# -----------------------------
# HTML <li> block protection
# -----------------------------

LI_OPEN_RE = re.compile(r"<li\b", re.IGNORECASE)
LI_CLOSE_RE = re.compile(r"</li\s*>", re.IGNORECASE)

def li_state_transition(in_li: bool, line: str) -> bool:
    """
    Update in_li state for current line. Conservative:
    - if we see <li ...> we enter li-protected mode
    - we exit after a line containing </li>
    Nested <li> is not tracked; we protect until we see a close tag line.
    """
    if not in_li and LI_OPEN_RE.search(line):
        return True
    if in_li and LI_CLOSE_RE.search(line):
        return False
    return in_li


# -----------------------------
# Section blacklisting
# -----------------------------

@dataclass(frozen=True)
class SectionSpec:
    heading_text: str  # exact heading text after hashes


DEFAULT_BLACKLIST: Dict[str, List[SectionSpec]] = {
    "docs/guide/bdqffdq/index.md": [
        SectionSpec(heading_text="4 Fitness For Use Framework Summary of Mathematical Formalization (normative)")
    ],
    "docs/guide/implementers/index.md": [
        SectionSpec(heading_text="8.3 Examples of the Data for Conformance Testing (non-normative)")
    ]
}


def is_blacklisted_section_start(rel_path: str, heading_text: str, blacklist: Dict[str, List[SectionSpec]]) -> bool:
    specs = blacklist.get(rel_path, [])
    return any(heading_text.strip() == s.heading_text for s in specs)


# -----------------------------
# Replacement logic
# -----------------------------

def link_vocab_first_inline_qname_per_file(
    text: str,
    from_file: Path,
    review_docs_root: Path,
    vocab_index: Dict[str, QualifiedTerm],
    seen: set[Tuple[str, str]],
) -> str:
    def repl(m: re.Match) -> str:
        token = m.group(1)
        qt = vocab_index.get(token)
        if not qt:
            return m.group(0)

        key = (str(from_file), qt.qname)
        if key in seen:
            return m.group(0)

        href_target = review_docs_root / qt.href_from_docs_root
        href_rel = rel_href(from_file, href_target)
        seen.add(key)
        return f"`{token}` [{qt.qname}](<{href_rel}> \"{qt.definition}\")"

    return INLINE_CODE_RE.sub(repl, text)


def link_glossary_first_plain_text_per_file(
    text: str,
    from_file: Path,
    review_root: Path,
    glossary_index: Dict[str, GlossaryTerm],
    seen: set[Tuple[str, str]],
) -> str:
    if not glossary_index:
        return text
    if not any(t in text for t in glossary_index.keys()):
        return text

    # mask inline code spans
    code_spans: List[str] = []
    def mask_code(m: re.Match) -> str:
        code_spans.append(m.group(0))
        return f"@@CODE{len(code_spans)-1}@@"
    masked = INLINE_CODE_RE.sub(mask_code, text)

    # mask existing links
    link_spans: List[str] = []
    def mask_link(m: re.Match) -> str:
        link_spans.append(m.group(0))
        return f"@@LINK{len(link_spans)-1}@@"
    masked = LINK_SPAN_RE.sub(mask_link, masked)

    terms_sorted = sorted(glossary_index.values(), key=lambda x: len(x.term), reverse=True)
    landing_md = review_root / "index.md"

    for gt in terms_sorted:
        key = (str(from_file), gt.term)
        if key in seen:
            continue

        pat = re.compile(rf"(?<![\w])({re.escape(gt.term)})(?![\w])")
        m = pat.search(masked)
        if not m:
            continue

        href_rel = rel_href(from_file, landing_md) + f"#{gt.anchor}"
        replacement = f'[{gt.term}](<{href_rel}> "{gt.definition}")'
        masked = masked[: m.start(1)] + replacement + masked[m.end(1) :]

        seen.add(key)

    masked = re.sub(r"@@LINK(\d+)@@", lambda m: link_spans[int(m.group(1))], masked)
    masked = re.sub(r"@@CODE(\d+)@@", lambda m: code_spans[int(m.group(1))], masked)
    return masked


def process_markdown_file(
    md_file: Path,
    review_root: Path,
    review_docs_root: Path,
    vocab_index: Dict[str, QualifiedTerm],
    glossary_index: Dict[str, GlossaryTerm],
    dry_run: bool,
    blacklist: Dict[str, List[SectionSpec]],
) -> bool:
    original = md_file.read_text(encoding="utf-8")
    fenced_parts = split_fenced_blocks(original)

    seen: set[Tuple[str, str]] = set()

    allow_rewrites = False  # after section 2
    in_blacklisted_section = False
    current_blacklisted_level: Optional[int] = None

    # file relative path under review_root for blacklist lookup
    try:
        rel_path = str(md_file.resolve().relative_to(review_root.resolve())).replace("\\", "/")
    except Exception:
        rel_path = md_file.name

    out_chunks: List[str] = []

    for is_fenced, chunk in fenced_parts:
        if is_fenced:
            out_chunks.append(chunk)
            continue

        lines = chunk.splitlines(keepends=True)
        new_lines: List[str] = []

        in_table = False
        in_li = False

        for line in lines:
            # Update LI state first; if we're in <li> protection, do nothing.
            # Note: if <li> and </li> on same line, li_state_transition enters then exits on same line,
            # but we still protect this line by checking LI_OPEN_RE/LI_CLOSE_RE presence below.
            entering_li = (not in_li) and bool(LI_OPEN_RE.search(line))
            in_li = li_state_transition(in_li, line)
            if entering_li or in_li or LI_CLOSE_RE.search(line):
                new_lines.append(line)
                continue

            # Table protection: protect contiguous table lines
            if is_table_line(line):
                in_table = True
                new_lines.append(line)
                continue
            else:
                if in_table:
                    in_table = False

            # Section/heading tracking (headings are not rewritten and they control state)
            msec = SECTION_START_RE.match(line.rstrip("\n"))
            if msec:
                heading_marks = msec.group(1)
                heading_text = msec.group(2).strip()
                level = len(heading_marks)

                if SECTION2_START_RE.match(line):
                    allow_rewrites = True

                if is_blacklisted_section_start(rel_path, heading_text, blacklist):
                    in_blacklisted_section = True
                    current_blacklisted_level = level
                elif in_blacklisted_section and current_blacklisted_level is not None and level <= current_blacklisted_level:
                    in_blacklisted_section = False
                    current_blacklisted_level = None

                new_lines.append(line)
                continue

            # Never rewrite any heading line (extra safety)
            if HEADING_LINE_RE.match(line):
                new_lines.append(line)
                continue

            # Rule: before section 2 => no rewrites
            if not allow_rewrites:
                new_lines.append(line)
                continue

            # Rule: blacklisted section => no rewrites
            if in_blacklisted_section:
                new_lines.append(line)
                continue

            # Rewrite
            line2 = link_vocab_first_inline_qname_per_file(line, md_file, review_docs_root, vocab_index, seen)
            line3 = link_glossary_first_plain_text_per_file(line2, md_file, review_root, glossary_index, seen)
            new_lines.append(line3)

        out_chunks.append("".join(new_lines))

    new_text = "".join(out_chunks)
    changed = new_text != original
    if changed and not dry_run:
        md_file.write_text(new_text, encoding="utf-8")
    return changed


# -----------------------------
# Main
# -----------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--review-root", default="../_review", help="tg2/_review")
    ap.add_argument("--docs-root", default="../_review/docs", help="tg2/_review/docs")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    review_root = Path(args.review_root)
    review_docs_root = Path(args.docs_root)

    if not review_root.exists():
        raise SystemExit(f"review root not found: {review_root}")
    if not review_docs_root.exists():
        raise SystemExit(f"docs root not found: {review_docs_root}")

    target_files = [
        review_docs_root / "tutorial/index.md",
        review_root / "index.md",
        review_docs_root / "guide/bdqtest/index.md",
        review_docs_root / "guide/users/index.md",
        review_docs_root / "guide/implementers/index.md",
        review_docs_root / "guide/bdqffdq/index.md",
        review_docs_root / "supplement/index.md",
    ]
    missing = [p for p in target_files if not p.exists()]
    if missing:
        raise SystemExit("One or more target files do not exist:\n- " + "\n- ".join(str(p) for p in missing))

    # Load vocab indices
    vocab_index: Dict[str, QualifiedTerm] = {}

    bdqffdq_owl = review_root / "vocabulary/bdqffdq.owl"
    if not bdqffdq_owl.exists():
        raise SystemExit(f"bdqffdq owl not found: {bdqffdq_owl}")
    vocab_index.update(load_bdqffdq_qualified_terms(bdqffdq_owl))

    vocab_csvs = {
        "bdqval": review_root / "vocabulary/bdqval_term_versions.csv",
        "bdqcrit": review_root / "vocabulary/bdqcrit_term_versions.csv",
        "bdqdim": review_root / "vocabulary/bdqdim_term_versions.csv",
        "bdqenh": review_root / "vocabulary/bdqenh_term_versions.csv",
    }
    for prefix, path in vocab_csvs.items():
        if not path.exists():
            raise SystemExit(f"Required term versions file not found: {path}")
        vocab_index.update(load_term_versions_csv(path, prefix))

    glossary_index = load_glossary_terms_from_landing(review_root / "index.md")

    changed_files: List[Path] = []
    for md in target_files:
        changed = process_markdown_file(
            md_file=md,
            review_root=review_root,
            review_docs_root=review_docs_root,
            vocab_index=vocab_index,
            glossary_index=glossary_index,
            dry_run=args.dry_run,
            blacklist=DEFAULT_BLACKLIST,
        )
        if changed:
            changed_files.append(md)

    if changed_files:
        print(f"Changed {len(changed_files)} markdown file(s):")
        for p in changed_files:
            print(f"- {p}")
        if args.dry_run:
            print("\nDry run: no files were written.")
    else:
        print("No changes made.")

    if not glossary_index:
        print("WARNING: No glossary table parsed from ../_review/index.md.")
        print("         Expected header: | **Label** | **Definition** | **Context** |")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
