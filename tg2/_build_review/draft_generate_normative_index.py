#!/usr/bin/env python3
"""
Generate a Markdown index page listing all *normative* section headings across selected BDQ standard documents,
AND add a topical index section derived from BDQ concept topics.

Key behaviors (per requirements):
- Include: standard landing page, bdqffdq and bdqtest landing pages, guides under docs/guide/, and term-list documents under docs/list/.
- Exclude: tutorial and supplement, and the Quick Reference Guide under docs/terms/.
- For each included document: list each heading whose text contains "(normative)".
- Exclude section 1 headings from each document even if they are marked normative.
- Generated output includes TWO indices:
  1) Topical index: topic -> document -> normative sections (links)
  2) Document index: document -> normative sections (TOC style) (existing behavior retained)

Topical index:
- Topics and their cues MUST be loaded from a YAML file (default: tg2/_build_review/normative_topics.yaml).
- Topics should represent BDQ primary concepts (curated), not repeated editorial heading patterns like "Use of Terms".
- Topic assignment uses keyword/cue matches in BOTH:
  - normative heading titles, and
  - the section body text that follows each normative heading up to the next heading of same/higher level.
- Inline code tokens (`` `...` ``) are treated as strong signals because they usually denote BDQ ontology terms,
  qualified names, controlled values, etc.

This script is designed to be run from tg2/_build_review/ (e.g., by make_review/do_build.sh) and writes to:
  tg2/_review/docs/normative_index.md

@author GitHub Copilot, with guidance and manual adjustments by Paul J. Morris

"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple, Any
from collections import defaultdict

import yaml


# ----------------------------
# Paths and config
# ----------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REVIEW_ROOT = (SCRIPT_DIR / "../_review").resolve()

DOCS_DIR = REVIEW_ROOT / "docs"
STANDARD_LANDING = REVIEW_ROOT / "index.md"

OUTPUT_MD = DOCS_DIR / "normative_index.md"

TOPICS_YAML = SCRIPT_DIR / "normative_topics.yaml"

INCLUDE_PATHS = [
    STANDARD_LANDING,
    DOCS_DIR / "bdqffdq" / "index.md",
    DOCS_DIR / "bdqtest" / "index.md",
]

INCLUDE_DIRS = [
    DOCS_DIR / "guide",
    DOCS_DIR / "list",
]

EXCLUDE_DIR_NAMES = {
    "tutorial",
    "supplement",
    "terms",
}

EXCLUDE_PATH_SUBSTRINGS = [
    f"{os.sep}docs{os.sep}terms{os.sep}",
    f"{os.sep}docs{os.sep}tutorial{os.sep}",
    f"{os.sep}docs{os.sep}supplement{os.sep}",
]

# ----------------------------
# Parsing
# ----------------------------

HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)\s*$")
NORMATIVE_MARKER = "(normative)"
SECTION1_RE = re.compile(r"^\s*1(\s|[.\)])")  # matches "1 " or "1." or "1)"
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
CURIE_RE = re.compile(r"\b[a-z][a-z0-9_-]*:[A-Za-z][A-Za-z0-9._-]*\b")

# Tokenization helpers
WORD_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_-]{1,}")


# ----------------------------
# Stopwords / exclusions for topic mining
# ----------------------------

# We want "main concepts of BDQ", not repeated doc-structure headings like "Use of Terms".
# So (a) topics are curated via YAML, and (b) we can treat certain generic patterns as weak/no signal.
GENERIC_HEADING_PHRASES = {
    "use of terms",
    "guidance for use of terms",
    "use of ontology terms",
    "vocabulary",
    "term index",
    "table of contents",
}

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "being", "by",
    "can", "could", "do", "does", "did", "for", "from", "has", "have",
    "had", "how", "if", "in", "into", "is", "it", "its", "may", "might",
    "most", "must", "not", "of", "on", "or", "other", "should", "shall",
    "that", "the", "their", "then", "there", "these", "this", "those",
    "to", "under", "used", "use", "using", "was", "were", "what", "when",
    "where", "which", "who", "will", "with", "without",
    # doc structure noise
    "section", "sections", "introduction", "overview", "guidance", "about",
    "term", "terms", "vocabulary", "list", "index", "table", "contents",
    "normative", "non-normative", "non", "also", "see", "example", "examples",
}


# ----------------------------
# Data types
# ----------------------------

@dataclass(frozen=True)
class NormativeSection:
    """
    A normative heading plus the body text that follows it (until next heading of same/higher level).
    """
    level: int
    title: str
    anchor: str
    body: str
    order: int  # monotonically increasing within document for stable sorting

    def full_text(self) -> str:
        return f"{self.title}\n\n{self.body}".strip()


@dataclass(frozen=True)
class DocumentNormativeIndex:
    path: Path
    title: str
    rel_link: str
    sections: List[NormativeSection]


@dataclass(frozen=True)
class TopicDefinition:
    """
    Loaded from YAML.
    """
    id: str
    label: str
    description: str
    # cues are organized so we can weight them differently
    code_terms: List[str]
    curies: List[str]
    keywords: List[str]
    phrases: List[str]
    exclude_phrases: List[str]


# ----------------------------
# Markdown link helpers
# ----------------------------

def slugify_heading(heading_text: str) -> str:
    """
    Create a stable slug. Adjust if your renderer uses a different algorithm.
    """
    text = heading_text.strip().lower()
    text = text.replace("`", "")
    text = re.sub(r"&[a-z]+;", "", text)
    text = text.replace("(", "").replace(")", "")
    text = re.sub(r"[^a-z0-9 _-]+", "", text)
    text = text.replace("_", "-")
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")


def relpath_from_docs_root(md_path: Path) -> str:
    md_path = md_path.resolve()
    if md_path == STANDARD_LANDING.resolve():
        return "../index.md"
    return os.path.relpath(md_path, DOCS_DIR.resolve()).replace(os.sep, "/")


def read_markdown_title(md_path: Path) -> str:
    """
    Best effort: first H1 line (# ...) becomes the title; fallback to filename stem.
    """
    try:
        with md_path.open("r", encoding="utf-8") as f:
            for line in f:
                m = HEADING_RE.match(line.rstrip("\n"))
                if m and len(m.group("hashes")) == 1:
                    return m.group("title").strip()
    except FileNotFoundError:
        pass
    return md_path.stem


def is_excluded_path(p: Path) -> bool:
    s = str(p.resolve())
    for sub in EXCLUDE_PATH_SUBSTRINGS:
        if sub in s:
            return True
    parts = {part for part in p.parts}
    if parts & EXCLUDE_DIR_NAMES:
        return True
    return False


def discover_documents() -> List[Path]:
    docs: List[Path] = []
    for p in INCLUDE_PATHS:
        if p.exists() and not is_excluded_path(p):
            docs.append(p)

    for d in INCLUDE_DIRS:
        if not d.exists():
            continue
        for p in d.rglob("index.md"):
            if is_excluded_path(p):
                continue
            docs.append(p)

    # de-duplicate while preserving order
    seen = set()
    out: List[Path] = []
    for p in docs:
        rp = str(p.resolve())
        if rp in seen:
            continue
        seen.add(rp)
        out.append(p)
    return out


# ----------------------------
# Section extraction
# ----------------------------

def _find_next_any_heading_of_same_or_higher_level(lines: List[str], start_line: int, current_level: int) -> int:
    """
    Find line index of next heading (any) with level <= current_level, starting at start_line (inclusive).
    Returns len(lines) if none found.
    """
    for j in range(start_line, len(lines)):
        m = HEADING_RE.match(lines[j])
        if not m:
            continue
        lvl2 = len(m.group("hashes"))
        if lvl2 <= current_level:
            return j
    return len(lines)


def extract_normative_sections(md_path: Path) -> List[NormativeSection]:
    """
    Parse markdown and extract normative headings + their bodies.

    Normative heading rule:
      - heading contains "(normative)" in the title
      - NOT a section-1 heading (title begins with "1", "1.", "1)" etc.)
    """
    lines = md_path.read_text(encoding="utf-8").splitlines()

    normative_headings: List[Tuple[int, str, int, str]] = []  # (level, title, line_index, anchor)
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group("hashes"))
        title = m.group("title").strip()

        if NORMATIVE_MARKER not in title:
            continue
        if SECTION1_RE.match(title):
            continue

        anchor = slugify_heading(title)
        normative_headings.append((level, title, i, anchor))

    sections: List[NormativeSection] = []
    for order, (level, title, start_i, anchor) in enumerate(normative_headings):
        body_start = start_i + 1
        body_end = _find_next_any_heading_of_same_or_higher_level(lines, body_start, level)
        body = "\n".join(lines[body_start:body_end]).strip()
        sections.append(NormativeSection(level=level, title=title, anchor=anchor, body=body, order=order))

    return sections


def build_document_index(md_path: Path) -> Optional[DocumentNormativeIndex]:
    if not md_path.exists():
        return None
    sections = extract_normative_sections(md_path)
    if not sections:
        return None
    title = read_markdown_title(md_path)
    rel_link = relpath_from_docs_root(md_path)
    return DocumentNormativeIndex(path=md_path, title=title, rel_link=rel_link, sections=sections)


# ----------------------------
# Topic loading and matching
# ----------------------------

def _as_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i) for i in x]
    return [str(x)]


def load_topics(yaml_path: Path) -> List[TopicDefinition]:
    """
    Load curated topics and cues from YAML.

    Expected structure (suggested):
    topics:
      - id: response
        label: Responses and Assertions
        description: ...
        cues:
          code_terms: [...]
          curies: [...]
          keywords: [...]
          phrases: [...]
          exclude_phrases: [...]
    """
    if not yaml_path.exists():
        raise FileNotFoundError(
            f"Topic YAML file not found: {yaml_path}. "
            "Create it (e.g., tg2/_build_review/normative_topics.yaml) to enable topical indexing."
        )

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    topics_raw = data.get("topics", [])
    topics: List[TopicDefinition] = []

    for t in topics_raw:
        cues = t.get("cues", {}) or {}
        topics.append(
            TopicDefinition(
                id=str(t.get("id", "")).strip(),
                label=str(t.get("label", "")).strip(),
                description=str(t.get("description", "") or "").strip(),
                code_terms=_as_list(cues.get("code_terms")),
                curies=_as_list(cues.get("curies")),
                keywords=_as_list(cues.get("keywords")),
                phrases=_as_list(cues.get("phrases")),
                exclude_phrases=_as_list(cues.get("exclude_phrases")),
            )
        )

    # basic validation
    topics = [t for t in topics if t.id and t.label]
    if not topics:
        raise ValueError(f"No usable topics found in {yaml_path} (topics must have id and label).")
    return topics


def normalize_text(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def extract_inline_code_tokens(text: str) -> List[str]:
    return [normalize_text(t) for t in INLINE_CODE_RE.findall(text)]


def extract_curie_tokens(text: str) -> List[str]:
    return [normalize_text(t) for t in CURIE_RE.findall(text)]


def extract_word_tokens(text: str) -> List[str]:
    out: List[str] = []
    for tok in WORD_TOKEN_RE.findall(text.lower()):
        if tok in STOPWORDS:
            continue
        out.append(tok)
    return out


def heading_is_generic(title: str) -> bool:
    """
    Identify repeated editorial headings that should not drive topic assignment.
    We do NOT exclude them from the normative list; we just avoid letting them dominate topical mapping.
    """
    t = normalize_text(title)
    # strip numbering prefix "2.3 " etc for comparison
    t = re.sub(r"^\d+(\.\d+)*\s+", "", t)
    t = t.replace("(normative)", "").strip()
    return t in GENERIC_HEADING_PHRASES


def score_section_for_topic(section: NormativeSection, topic: TopicDefinition) -> int:
    """
    Score a topic against a section using cues from both heading and body.

    Weighting rationale:
    - inline code tokens are strong signals of BDQ ontology terms: +5 per match in heading, +3 in body.
    - curated CURIE cues: +4 per match in heading, +2 in body.
    - keywords: +2 per match in heading, +1 in body.
    - phrases: +2 if phrase appears anywhere in (heading+body).
    - exclude_phrases: -100 if appears anywhere (hard exclude).
    """
    title = section.title
    body = section.body
    title_l = normalize_text(title)
    body_l = normalize_text(body)
    full_l = normalize_text(title + "\n" + body)

    for bad in topic.exclude_phrases:
        if normalize_text(bad) and normalize_text(bad) in full_l:
            return -100

    inline_title = set(extract_inline_code_tokens(title))
    inline_body = set(extract_inline_code_tokens(body))
    curie_title = set(extract_curie_tokens(title))
    curie_body = set(extract_curie_tokens(body))

    # word token sets help keyword matching that isn't a phrase
    words_title = set(extract_word_tokens(title))
    words_body = set(extract_word_tokens(body))

    score = 0

    # Avoid generic headings dominating (e.g. "Use of Terms"):
    # if heading is generic, downweight heading-only matches (still allow body to contribute normally).
    generic = heading_is_generic(title)

    for cue in topic.code_terms:
        c = normalize_text(cue)
        if not c:
            continue
        if c in inline_title:
            score += 2 if generic else 5
        if c in inline_body:
            score += 3

    for cue in topic.curies:
        c = normalize_text(cue)
        if not c:
            continue
        if c in curie_title:
            score += 1 if generic else 4
        if c in curie_body:
            score += 2

    for kw in topic.keywords:
        k = normalize_text(kw)
        if not k:
            continue
        # keyword can match either word tokens or raw substring; we use tokens to avoid too many substring hits
        if k in words_title:
            score += 1 if generic else 2
        if k in words_body:
            score += 1

    for phrase in topic.phrases:
        p = normalize_text(phrase)
        if not p:
            continue
        if p in full_l:
            score += 2

    return score


def assign_topics(
    indices: List[DocumentNormativeIndex],
    topics: List[TopicDefinition],
    min_score: int = 4,
) -> Dict[str, Dict[str, List[Tuple[DocumentNormativeIndex, NormativeSection, int]]]]:
    """
    Returns:
      topic_id -> doc_rel_link -> list of (doc, section, score)
    """
    topic_hits: Dict[str, Dict[str, List[Tuple[DocumentNormativeIndex, NormativeSection, int]]]] = {
        t.id: {} for t in topics
    }

    for doc in indices:
        for sec in doc.sections:
            for topic in topics:
                score = score_section_for_topic(sec, topic)
                if score >= min_score:
                    per_doc = topic_hits[topic.id].setdefault(doc.rel_link, [])
                    per_doc.append((doc, sec, score))

    # Sort within each doc by original order, and dedupe by anchor.
    for tid, per_doc in topic_hits.items():
        for doc_link, entries in per_doc.items():
            # stable sort: by section order descending by score? better: order first, but keep score for tie-breakers if needed
            entries.sort(key=lambda x: x[1].order)
            seen = set()
            deduped = []
            for d, s, sc in entries:
                key = (d.rel_link, s.anchor)
                if key in seen:
                    continue
                seen.add(key)
                deduped.append((d, s, sc))
            per_doc[doc_link] = deduped

    return topic_hits


# ----------------------------
# Rendering
# ----------------------------

def heading_indent(level: int) -> str:
    if level <= 2:
        return "  "
    if level == 3:
        return "    "
    if level == 4:
        return "      "
    return "        "

def display_title(title: str) -> str:
    """
    For link text, omit the literal '(normative)' marker to reduce visual noise.
    Keep anchors unchanged (they still include '-normative').
    """
    return title.replace(" (normative)", "").replace("(normative)", "").rstrip()

def render_topical_index(indices: List[DocumentNormativeIndex], topics: List[TopicDefinition]) -> List[str]:
    lines: List[str] = []
    lines.append("## Topical index of normative sections (generated)")
    lines.append("")
    lines.append("This section groups normative sections by primary BDQ concepts using curated topic cues plus keyword matches in section headings and their following text.")
    lines.append("A section may appear under more than one topic.")
    lines.append("")

    hits = assign_topics(indices, topics)

    # render in YAML file order (topics list order)
    rendered_any = False
    for topic in topics:
        per_doc = hits.get(topic.id, {})
        if not per_doc:
            continue

        rendered_any = True
        lines.append(f"### {topic.label}")
        if topic.description:
            lines.append("")
            lines.append(topic.description)
        lines.append("")

        # deterministic doc order by document title (more readable than relpath)
        doc_entries = []
        for doc_link, entries in per_doc.items():
            if not entries:
                continue
            doc_title = entries[0][0].title
            doc_entries.append((doc_title.lower(), doc_title, doc_link, entries))
        doc_entries.sort(key=lambda x: x[0])

        for _, doc_title, doc_link, entries in doc_entries:
            lines.append(f"- **{doc_title}**: [{doc_link}]({doc_link})")
            for doc, sec, score in entries:
                # keep output clean; score can be useful during tuning but is noisy in final docs
                lines.append(f"  - [{display_title(sec.title)}]({doc.rel_link}#{sec.anchor})")
        lines.append("")

    if not rendered_any:
        lines.append("_No topical matches were produced. Check that the topic YAML file exists and contains cues that match the documents._")
        lines.append("")

    return lines

def render_document_index(indices: List[DocumentNormativeIndex]) -> List[str]:
    """
    Per-document TOC-style list of normative headings.

    Fix:
    - Compute list nesting from the *numeric section numbering* (e.g., 2.2.1), not from Markdown heading level.
    - Promote headings whose numbered parents (e.g., 2, 2.2) are NOT included in the normative set.
      Example: if 2.2 and 2 are not normative, then 2.2.1 should be rendered as a top-level entry under Document.
    - Nest headings under included parents when present (e.g., 3.1 under 3).
    """
    lines: List[str] = []
    lines.append("## List of normative sections in each document (generated)")
    lines.append("")
    lines.append("This section lists the normative sections in each BDQ Document.")
    lines.append("")

    # Matches a leading section number like "2", "2.2", "2.2.1" at start of heading title.
    number_re = re.compile(r"^\s*(\d+(?:\.\d+)*)\b")

    def parents(num: str) -> List[str]:
        parts = num.split(".")
        out = []
        while len(parts) > 1:
            parts = parts[:-1]
            out.append(".".join(parts))
        return out  # nearest parent first: ["2.2", "2"]

    def indent_for_depth(depth: int) -> str:
        # Depth 0 means "top-level under Document:" which is 2 spaces.
        return "  " * (depth + 1)

    for doc in indices:
        lines.append(f"## {doc.title}")
        lines.append("")
        lines.append(f"- Document: [{doc.rel_link}]({doc.rel_link})")

        # Build map: section -> section_number (if any)
        sec_num: Dict[NormativeSection, Optional[str]] = {}
        nums_present: set[str] = set()
        for sec in doc.sections:
            m = number_re.match(sec.title.replace("(normative)", "").strip())
            num = m.group(1) if m else None
            sec_num[sec] = num
            if num:
                nums_present.add(num)

        # Compute effective depths for numbered headings
        computed_depth: Dict[str, int] = {}

        def depth_for_num(num: str) -> int:
            if num in computed_depth:
                return computed_depth[num]

            # Find nearest included parent, if any.
            for p in parents(num):
                if p in nums_present:
                    d = depth_for_num(p) + 1
                    computed_depth[num] = d
                    return d

            computed_depth[num] = 0
            return 0

        # Render each normative section in document order
        for sec in doc.sections:
            num = sec_num.get(sec)
            if num:
                depth = depth_for_num(num)
            else:
                # No numbering: keep it top-level under Document
                depth = 0

            indent = indent_for_depth(depth)
            lines.append(f"{indent}- [{display_title(sec.title)}]({doc.rel_link}#{sec.anchor})")

        lines.append("")
        lines.append("")

    return lines

def render_markdown(indices: List[DocumentNormativeIndex], topics: List[TopicDefinition]) -> str:
    lines: List[str] = []
    lines.append("<!--- This file is generated by tg2/_build_review/generate_normative_index.py; DO NOT EDIT by hand --->")
    lines.append("")
    lines.append("# Index of Normative Sections in the BDQ Standard")
    lines.append("")
    lines.append("This page lists, for each included BDQ standard document, the section headings explicitly marked **(normative)**, and provides a topical index across those sections.")
    lines.append("")
    lines.append("Exclusions applied by the generator:")
    lines.append("- Section 1 headings in each document are excluded (even if marked normative).")
    lines.append("- Non-normative headings are excluded.")
    lines.append("- Tutorial and Supplement are excluded.")
    lines.append("- Quick Reference Guide (docs/terms) is excluded.")
    lines.append("")

    # 1) Topical index (added) — does not replace the existing per-doc index
    lines.extend(render_topical_index(indices, topics))
    lines.append("---")
    lines.append("")

    # 2) Existing per-document index
    lines.extend(render_document_index(indices))

    return "\n".join(lines).rstrip() + "\n"


# ----------------------------
# Main
# ----------------------------

def main() -> int:
    docs = discover_documents()
    indices: List[DocumentNormativeIndex] = []
    for md in docs:
        idx = build_document_index(md)
        if idx is not None:
            indices.append(idx)

    # Sort deterministically: standard landing first, then by relative link
    def sort_key(d: DocumentNormativeIndex) -> Tuple[int, str]:
        is_landing = 0
        if d.path.resolve() == STANDARD_LANDING.resolve():
            is_landing = -10
        return (is_landing, d.rel_link)

    indices.sort(key=sort_key)

    topics = load_topics(TOPICS_YAML)

    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text(render_markdown(indices, topics), encoding="utf-8")

    print(f"Wrote {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
