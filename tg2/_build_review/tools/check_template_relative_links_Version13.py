#!/usr/bin/env python3
"""
Scan BDQ TG2 Markdown templates for relative links, and report:

(1) For each template document, a list of sections (Markdown headings) that contain
    >= 1 link, along with a count of links found within that section (excluding sections with 0 links).

(2) A list of links (file, line number, link text, link relative URI) that would be broken
    when Markdown documents are generated from the templates.

Author: Github Copilot (with user guidance and review from Paul J. Morris)

Key assumptions (per user clarification):
- Links are authored as if clicked from the GENERATED document’s location (not the template location).
- Template directory layout largely mirrors generated layout under tg2/_review/docs/, except:
    - templates/standard_landing/* generates to tg2/_review/index.md and is rooted at tg2/_review/

Anchor/fragment matching:
- This script matches fragments EXACTLY the way the local build does, by replicating
  tg2/_build_review/function_lib.py: markdown_heading_to_link() anchor generation.

That local logic is:
  anchor = heading_text.lower()
  anchor = anchor.replace(" ", "-")
  anchor = anchor.translate(str.maketrans("", "", "():,.?`'\""))

So fragments are validated against:
  (a) explicit HTML ids/names in the target file (id= / name=)
  (b) anchors derived from Markdown headings using the exact algorithm above

Options:
- --no-footers        : ignore all *-footer.md template files entirely
- --no-anchor-check   : skip fragment (#...) validation (still checks that target files exist)
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


class BrokenKind(str, Enum):
    TARGET_MISSING = "target_missing"
    ANCHOR_MISSING = "anchor_missing"
    OUTSIDE_REPO = "outside_repo"


@dataclass(frozen=True)
class LinkOccurrence:
    source_file: Path          # absolute template path
    source_file_rel: Path      # relative to repo root (for reporting)
    source_line: int
    section: str
    link_text: str
    raw_target: str


@dataclass(frozen=True)
class BrokenLink:
    source_file_rel: Path
    source_line: int
    link_text: str
    raw_target: str
    broken_kind: BrokenKind
    reason: str


INLINE_LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
FENCE_RE = re.compile(r"^(```+|~~~+)")
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "ftp://")

# HTML id/name extraction (tolerant; generated markdown often includes embedded HTML)
HTML_ID_RE = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
HTML_NAME_RE = re.compile(r"""\bname\s*=\s*["']([^"']+)["']""", re.IGNORECASE)


# EXACT punctuation removal set from function_lib.markdown_heading_to_link():
# anchor.translate(str.maketrans("", "", "():,.?`'\""))
BDQ_ANCHOR_STRIP_CHARS = "():,.?`'\""
BDQ_ANCHOR_STRIP_TABLE = str.maketrans("", "", BDQ_ANCHOR_STRIP_CHARS)


def iter_template_markdown_files(templates_root: Path, *, include_footers: bool) -> Iterable[Path]:
    for p in templates_root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".md", ".markdown"}:
            continue
        if not include_footers and p.name.endswith("-footer.md"):
            continue
        yield p


def strip_code_fences_and_collect(md_lines: List[str]) -> Tuple[List[Tuple[int, str]], List[Tuple[int, str]]]:
    in_fence = False
    headings: List[Tuple[int, str]] = []
    nonfenced: List[Tuple[int, str]] = []

    for i, line in enumerate(md_lines, start=1):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        m = HEADING_RE.match(line)
        if m:
            headings.append((i, m.group(2).strip()))
        nonfenced.append((i, line.rstrip("\n")))
    return headings, nonfenced


def section_for_line(line_no: int, headings: List[Tuple[int, str]]) -> str:
    current = "(no heading yet)"
    for h_line, h_text in headings:
        if h_line <= line_no:
            current = h_text
        else:
            break
    return current


def looks_like_external(target: str) -> bool:
    t = target.strip().lower()
    return t.startswith(EXTERNAL_SCHEMES)


def split_target(target: str) -> Tuple[str, str]:
    target = target.strip()
    if "#" in target:
        path_part, frag = target.split("#", 1)
        return path_part, frag
    return target, ""


def is_internal_anchor_only(path_part: str) -> bool:
    return path_part.strip() == ""


def normalize_rel_path(base_dir: Path, rel_target_path: str) -> Path:
    rel_target_path = rel_target_path.strip()
    if rel_target_path.startswith("<") and rel_target_path.endswith(">"):
        rel_target_path = rel_target_path[1:-1].strip()
    return (base_dir / rel_target_path).resolve()


def strip_optional_link_title(raw_target: str) -> str:
    """
    Handle Markdown link destinations with an optional title:
      path "title"
      path 'title'
      path (title)
    We only want the path portion for file resolution.

    Pragmatic parsing:
    - If destination begins with <...>, keep inside <...>
    - Else split on whitespace and keep the first token as the path.
      (Matches your template usage e.g. ../file.csv "Some title")
    """
    s = raw_target.strip()
    if s.startswith("<") and s.endswith(">"):
        return s[1:-1].strip()

    parts = s.split()
    if not parts:
        return s
    return parts[0].strip()


def bdq_anchor_from_heading_text(heading_text: str) -> str:
    """
    Exact implementation of function_lib.markdown_heading_to_link() anchor generation.
    """
    anchor = heading_text.lower()
    anchor = anchor.replace(" ", "-")
    anchor = anchor.translate(BDQ_ANCHOR_STRIP_TABLE)
    return anchor


def build_bdq_heading_anchor_index(md_path: Path) -> Dict[str, List[int]]:
    """
    Build an index of anchors derived from headings using the EXACT BDQ algorithm
    in function_lib.markdown_heading_to_link().
    """
    if not md_path.exists() or not md_path.is_file():
        return {}

    lines = md_path.read_text(encoding="utf-8", errors="replace").splitlines(True)
    headings, _ = strip_code_fences_and_collect(lines)

    index: Dict[str, List[int]] = {}
    for line_no, h_text in headings:
        anchor = bdq_anchor_from_heading_text(h_text)
        index.setdefault(anchor, []).append(line_no)
    return index


def build_explicit_anchor_id_index(md_path: Path) -> Set[str]:
    ids: Set[str] = set()
    if not md_path.exists() or not md_path.is_file():
        return ids

    text = md_path.read_text(encoding="utf-8", errors="replace")

    for m in HTML_ID_RE.finditer(text):
        ids.add(m.group(1))
    for m in HTML_NAME_RE.finditer(text):
        ids.add(m.group(1))

    return ids


def fragment_exists_in_target(md_path: Path, frag: str) -> Tuple[bool, str]:
    """
    Validate a fragment against:
      1) explicit HTML id/name attributes
      2) exact BDQ-generated heading anchors (function_lib.markdown_heading_to_link)
    """
    frag_raw = frag.strip()
    if not frag_raw:
        return True, ""

    # 1) explicit HTML ids/names (exact + case-insensitive)
    explicit_ids = build_explicit_anchor_id_index(md_path)
    if frag_raw in explicit_ids:
        return True, ""
    frag_lower = frag_raw.lower()
    if any(x.lower() == frag_lower for x in explicit_ids):
        return True, ""

    # 2) exact BDQ heading anchor generation
    anchor_index = build_bdq_heading_anchor_index(md_path)
    if frag_raw in anchor_index:
        return True, ""
    # also accept case-insensitive for robustness
    if frag_lower in {k.lower() for k in anchor_index.keys()}:
        return True, ""

    return False, f"Fragment not found in explicit id/name or BDQ heading anchors: #{frag_raw}"


def find_links_in_file(md_path: Path, repo_root: Path) -> List[LinkOccurrence]:
    lines = md_path.read_text(encoding="utf-8", errors="replace").splitlines(True)
    headings, nonfenced = strip_code_fences_and_collect(lines)

    occurrences: List[LinkOccurrence] = []
    source_file_rel = md_path.resolve().relative_to(repo_root)

    for line_no, line in nonfenced:
        for m in INLINE_LINK_RE.finditer(line):
            occurrences.append(
                LinkOccurrence(
                    source_file=md_path.resolve(),
                    source_file_rel=source_file_rel,
                    source_line=line_no,
                    section=section_for_line(line_no, headings),
                    link_text=m.group(1).strip(),
                    raw_target=m.group(2).strip(),
                )
            )
    return occurrences


def generated_base_dir_for_template(
    template_file: Path,
    *,
    templates_root: Path,
    generated_review_root: Path,
) -> Optional[Path]:
    """
    Infer the directory from which links are authored (generated location).

    rules:
      templates/standard_landing/* -> tg2/_review/
      templates/<rel_dir>/*        -> tg2/_review/docs/<rel_dir>/
    """
    try:
        rel_dir = template_file.parent.resolve().relative_to(templates_root.resolve())
    except ValueError:
        return None

    rel_dir_posix = str(rel_dir).replace("\\", "/")
    if rel_dir_posix.startswith("standard_landing"):
        return generated_review_root.resolve()

    return (generated_review_root / "docs" / rel_dir).resolve()


def resolve_target_from_generated_base(
    *,
    base_dir: Path,
    repo_root: Path,
    raw_target: str,
) -> Tuple[Optional[Path], str, str]:
    """
    Returns (resolved_path_or_None, normalized_path_only, fragment).
    """
    path_part, frag = split_target(raw_target)

    if looks_like_external(path_part):
        return None, path_part, frag

    lowered = path_part.strip().lower()
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+\-.]*:", lowered):
        # Other schemes (doi:, urn:, etc.) ignored
        return None, path_part, frag

    if is_internal_anchor_only(path_part):
        return (base_dir / "index.md").resolve(), "", frag

    path_only = strip_optional_link_title(path_part)
    resolved = normalize_rel_path(base_dir, path_only)

    try:
        resolved.relative_to(repo_root)
    except ValueError:
        return None, path_only, frag

    return resolved, path_only, frag


def validate_link(
    occ: LinkOccurrence,
    *,
    repo_root: Path,
    templates_root: Path,
    generated_review_root: Path,
    no_anchor_check: bool,
) -> Optional[BrokenLink]:
    base_dir = generated_base_dir_for_template(
        occ.source_file,
        templates_root=templates_root,
        generated_review_root=generated_review_root,
    )
    if base_dir is None:
        return BrokenLink(
            source_file_rel=occ.source_file_rel,
            source_line=occ.source_line,
            link_text=occ.link_text,
            raw_target=occ.raw_target,
            broken_kind=BrokenKind.OUTSIDE_REPO,
            reason="Could not infer generated base directory for template (not under templates_root?).",
        )

    resolved_target, path_only, frag = resolve_target_from_generated_base(
        base_dir=base_dir,
        repo_root=repo_root,
        raw_target=occ.raw_target,
    )
    if resolved_target is None:
        path_part, _ = split_target(occ.raw_target)
        if not looks_like_external(path_part) and not re.match(r"^[a-zA-Z][a-zA-Z0-9+\-.]*:", path_part.strip()):
            return BrokenLink(
                source_file_rel=occ.source_file_rel,
                source_line=occ.source_line,
                link_text=occ.link_text,
                raw_target=occ.raw_target,
                broken_kind=BrokenKind.OUTSIDE_REPO,
                reason=f"Target resolves outside repo from generated base {base_dir}: {path_only}",
            )
        return None

    if not resolved_target.exists():
        return BrokenLink(
            source_file_rel=occ.source_file_rel,
            source_line=occ.source_line,
            link_text=occ.link_text,
            raw_target=occ.raw_target,
            broken_kind=BrokenKind.TARGET_MISSING,
            reason=f"Target does not exist from generated base {base_dir}: {resolved_target}",
        )

    if frag and not no_anchor_check and resolved_target.is_file() and resolved_target.suffix.lower() in {".md", ".markdown"}:
        ok, msg = fragment_exists_in_target(resolved_target, frag)
        if not ok:
            return BrokenLink(
                source_file_rel=occ.source_file_rel,
                source_line=occ.source_line,
                link_text=occ.link_text,
                raw_target=occ.raw_target,
                broken_kind=BrokenKind.ANCHOR_MISSING,
                reason=f"{msg} (target {resolved_target})",
            )

    return None


def write_sections_report(occurrences: List[LinkOccurrence], out_path: Path) -> None:
    counts: Dict[Path, Dict[str, int]] = {}
    for occ in occurrences:
        counts.setdefault(occ.source_file_rel, {})
        counts[occ.source_file_rel][occ.section] = counts[occ.source_file_rel].get(occ.section, 0) + 1

    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["template_file", "section_heading", "link_count"])
        for file_rel in sorted(counts.keys()):
            for section in sorted(counts[file_rel].keys()):
                w.writerow([str(file_rel), section, counts[file_rel][section]])


def write_broken_links_report(broken: List[BrokenLink], out_path: Path) -> None:
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["template_file", "line", "link_text", "link_target", "broken_kind", "reason"])
        for b in broken:
            w.writerow([str(b.source_file_rel), b.source_line, b.link_text, b.raw_target, b.broken_kind.value, b.reason])


def guess_repo_root_from_tools_dir(cwd: Path) -> Path:
    # tools/ -> _build_review/ -> tg2/ -> repo root
    return (cwd / ".." / ".." / "..").resolve()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default="", help="Optional repo root; otherwise inferred from CWD.")
    ap.add_argument("--templates-root", default="", help="Optional templates root; otherwise inferred.")
    ap.add_argument(
        "--generated-review-root",
        default="",
        help="Optional generated review root; default is <repo_root>/tg2/_review",
    )
    ap.add_argument("--sections-out", default="sections_with_link_counts.csv")
    ap.add_argument("--broken-out", default="broken_links.csv")
    ap.add_argument("--no-footers", action="store_true", help="Do not scan any *-footer.md template files.")
    ap.add_argument("--no-anchor-check", action="store_true", help="Do not validate #fragment anchors.")

    args = ap.parse_args()

    cwd = Path.cwd().resolve()
    repo_root = Path(args.repo_root).resolve() if args.repo_root.strip() else guess_repo_root_from_tools_dir(cwd)

    templates_root = (
        Path(args.templates_root).resolve()
        if args.templates_root.strip()
        else (repo_root / "tg2" / "_build_review" / "templates").resolve()
    )

    generated_review_root = (
        Path(args.generated_review_root).resolve()
        if args.generated_review_root.strip()
        else (repo_root / "tg2" / "_review").resolve()
    )

    if not templates_root.exists():
        raise SystemExit(f"Templates root not found: {templates_root}")

    if not generated_review_root.exists():
        raise SystemExit(f"Generated review root not found: {generated_review_root}")

    include_footers = not args.no_footers

    all_occurrences: List[LinkOccurrence] = []
    for md in iter_template_markdown_files(templates_root, include_footers=include_footers):
        all_occurrences.extend(find_links_in_file(md, repo_root=repo_root))

    broken: List[BrokenLink] = []
    for occ in all_occurrences:
        b = validate_link(
            occ,
            repo_root=repo_root,
            templates_root=templates_root,
            generated_review_root=generated_review_root,
            no_anchor_check=args.no_anchor_check,
        )
        if b is not None:
            broken.append(b)

    sections_out = Path(args.sections_out).resolve()
    broken_out = Path(args.broken_out).resolve()

    write_sections_report(all_occurrences, sections_out)
    write_broken_links_report(broken, broken_out)

    print(f"Repo root: {repo_root}")
    print(f"Templates root: {templates_root}")
    print(f"Generated review root: {generated_review_root}")
    print(f"Scanning footer templates: {include_footers}")
    print(f"Anchor checking: {not args.no_anchor_check}")
    print(f"Found {len(all_occurrences)} inline links in templates.")
    print(f"Found {len(broken)} broken links (validated using exact BDQ fragment logic).")
    print(f"Wrote: {sections_out}")
    print(f"Wrote: {broken_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
