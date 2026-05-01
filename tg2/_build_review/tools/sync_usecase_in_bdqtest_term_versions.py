#!/usr/bin/env python3
"""
Sync a single Use Case value across BDQ test rows in bdqtest_term_versions.csv.

Given an input text file of the form:

  Use Case: bdqval:SDM-Trees
  Tests:
  VALIDATION_...
  ...

@author GitHub Copliot with human review and edits by Paul J. Morris @chicoreus

this script will:
  1) Read bdqtest_term_versions.csv
  2) Check that:
       - every listed Test label includes the given Use Case in the UseCases column, and
       - no other tests include that Use Case
  3) Report findings
  4) Optionally modify bdqtest_term_versions.csv:
       - Add the Use Case to the UseCases column for the listed tests when missing
       - Remove the Use Case from any other tests where present
     while making no other changes.

CSV quoting detection/writing:

  This repository's bdqtest_term_versions.csv may be produced by LibreOffice Calc with
  "Quote all text cells". That yields:
    - Header: quoted fields (e.g., "Label","issueNumber",...)
    - Data rows: text fields quoted, numeric/date-like fields unquoted, empty fields unquoted.

  This script detects a quoting strategy from the header + first data line:

    - quote_text:
        header is fully quoted AND
        first data line has at least one quoted non-empty field AND at least one unquoted non-empty field
        (i.e., it is a *mixed* row like: "VALIDATION...",20,"https://...",...,2025-03-07,...)

    - quote_all:
        header is fully quoted AND
        first data line appears fully quoted (every non-empty token quoted; empties may be "")

    - quote_minimal:
        otherwise

  Writing:
    - quote_text: quote header; quote non-empty text fields; leave numeric/date-like unquoted; leave empty unquoted.
    - quote_all: quote everything including empties.
    - quote_minimal: csv.QUOTE_MINIMAL; additionally force quoting of non-empty UseCases if modified.

Other notes:
  - The test identifier used is the BDQ Test Label in column 'Label'.
  - The UseCases column is treated as a comma-separated list (also tolerates ';' and '|').
  - When a UseCases value changes, it is re-serialized deterministically as ", " joined and
    case-insensitively sorted.
  - When no change is required for a row, the original UseCases string is preserved exactly.

Exit codes:
  0 = success (including when mismatches are found but --apply not requested)
  2 = input/parse error
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


USECASE_LINE_RE = re.compile(r"^\s*Use\s*Case\s*:\s*(?P<usecase>\S+)\s*$", re.IGNORECASE)
TEST_LABEL_RE = re.compile(r"^\s*([A-Z0-9_]+)\s*$")

_INT_RE = re.compile(r"^[+-]?\d+$")
_FLOAT_RE = re.compile(r"^[+-]?\d+\.\d+$")
_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def today_yyyy_mm_dd() -> str:
    return dt.date.today().isoformat()


def parse_spec_file(path: Path) -> Tuple[str, List[str]]:
    use_case: Optional[str] = None
    labels: List[str] = []
    in_tests = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        m = USECASE_LINE_RE.match(raw_line)
        if m:
            use_case = m.group("usecase").strip()
            continue

        if line.lower().startswith("tests"):
            in_tests = True
            continue

        if in_tests:
            m2 = TEST_LABEL_RE.match(raw_line)
            if not m2:
                raise ValueError(f"Unrecognized test label line in spec file: {raw_line!r}")
            labels.append(m2.group(1))

    if not use_case:
        raise ValueError("Spec file missing 'Use Case: ...' line.")
    if not labels:
        raise ValueError("Spec file contains no test labels under 'Tests:'.")

    seen: Set[str] = set()
    deduped: List[str] = []
    for lab in labels:
        if lab not in seen:
            seen.add(lab)
            deduped.append(lab)

    return use_case, deduped


def split_usecases(value: str) -> List[str]:
    if value is None:
        return []
    v = value.strip()
    if not v:
        return []
    v = v.replace("|", ",")
    v = v.replace(";", ",")
    parts = [p.strip() for p in v.split(",")]
    return [p for p in parts if p]


def join_usecases(usecases: Iterable[str]) -> str:
    items = [u.strip() for u in usecases if u and u.strip()]
    items_sorted = sorted(set(items), key=lambda s: s.lower())
    return ", ".join(items_sorted)


def load_csv_rows(csv_path: Path) -> Tuple[List[Dict[str, str]], List[str]]:
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row.")
        fieldnames = list(reader.fieldnames)
        rows = [dict(r) for r in reader]
    return rows, fieldnames


def _read_first_two_lines(csv_path: Path) -> Tuple[str, str]:
    with csv_path.open("r", encoding="utf-8") as f:
        header = f.readline()
        first = f.readline()
    return header.rstrip("\r\n"), first.rstrip("\r\n")


def _looks_like_fully_quoted_csv_line(line: str) -> bool:
    if not line:
        return False
    s = line.strip()
    return s.startswith('"') and s.endswith('"') and '","' in s


def _split_raw_csv_line_tokens(line: str) -> List[str]:
    """
    Split a CSV line into raw field tokens (not decoded), by scanning commas not inside quotes.

    This is robust for Calc output: fields may contain commas only inside quotes, and quotes
    are escaped as "" inside quoted fields.
    """
    tokens: List[str] = []
    buf: List[str] = []
    in_quotes = False
    i = 0
    while i < len(line):
        c = line[i]

        if c == '"':
            buf.append(c)
            if in_quotes:
                # escaped quote
                if i + 1 < len(line) and line[i + 1] == '"':
                    buf.append('"')
                    i += 2
                    continue
                in_quotes = False
            else:
                in_quotes = True
            i += 1
            continue

        if c == "," and not in_quotes:
            tokens.append("".join(buf))
            buf = []
            i += 1
            continue

        buf.append(c)
        i += 1

    tokens.append("".join(buf))
    return tokens


def _token_is_quoted(token: str) -> bool:
    t = token.strip()
    return len(t) >= 2 and t.startswith('"') and t.endswith('"')


def _token_is_empty(token: str) -> bool:
    # empty field in CSV is just nothing between delimiters
    return token == "" or token.strip() == ""


def _is_number_or_date_like(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    return bool(_INT_RE.match(s) or _FLOAT_RE.match(s) or _ISO_DATE_RE.match(s))


@dataclass(frozen=True)
class QuotingStrategy:
    name: str  # "quote_all" | "quote_text" | "quote_minimal"


def detect_quoting_strategy(csv_path: Path) -> QuotingStrategy:
    header, first = _read_first_two_lines(csv_path)

    if not _looks_like_fully_quoted_csv_line(header):
        return QuotingStrategy("quote_minimal")

    if not first:
        # With a fully-quoted header and no data, the file likely originated in Calc-style.
        return QuotingStrategy("quote_text")

    # Tokenize the raw first data row.
    tokens = _split_raw_csv_line_tokens(first)

    # Determine whether there is a mix of quoted/unquoted non-empty fields.
    quoted_nonempty = 0
    unquoted_nonempty = 0

    for tok in tokens:
        if _token_is_empty(tok):
            continue
        if _token_is_quoted(tok):
            quoted_nonempty += 1
        else:
            unquoted_nonempty += 1

    if quoted_nonempty > 0 and unquoted_nonempty > 0:
        # This is the Calc "quote text cells" signature (mixed row).
        return QuotingStrategy("quote_text")

    # If everything non-empty is quoted, treat as quote_all.
    if quoted_nonempty > 0 and unquoted_nonempty == 0:
        return QuotingStrategy("quote_all")

    # Otherwise fall back.
    return QuotingStrategy("quote_minimal")


def _quote_csv_cell(s: str) -> str:
    return '"' + s.replace('"', '""') + '"'


def _serialize_row_quote_all(fieldnames: Sequence[str], row: Dict[str, str]) -> str:
    # In quote_all, even empty fields become ""
    return ",".join(_quote_csv_cell(row.get(k, "") or "") for k in fieldnames)


def _serialize_row_quote_text(fieldnames: Sequence[str], row: Dict[str, str]) -> str:
    """
    Mimic LibreOffice Calc "quote all text cells":
      - empty -> empty (,,)
      - numeric/date-like -> unquoted
      - everything else -> quoted
    """
    out: List[str] = []
    for k in fieldnames:
        v = row.get(k, "") or ""
        if v == "":
            out.append("")
        elif _is_number_or_date_like(v):
            out.append(v)
        else:
            out.append(_quote_csv_cell(v))
    return ",".join(out)


def write_csv_rows_detected(
    csv_path: Path,
    fieldnames: Sequence[str],
    rows: Sequence[Dict[str, str]],
    strategy: QuotingStrategy,
) -> None:
    usecases_idx = fieldnames.index("UseCases") if "UseCases" in fieldnames else -1

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        if strategy.name == "quote_minimal":
            w = csv.writer(f, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
            w.writerow(list(fieldnames))
            for r in rows:
                values = [(r.get(k, "") or "") for k in fieldnames]
                if usecases_idx >= 0:
                    uc = values[usecases_idx]
                    if uc.strip():
                        # Force quotes as literal characters (stable across versions).
                        values[usecases_idx] = _quote_csv_cell(uc)
                w.writerow(values)
            return

        # Calc-like styles: always quote header cells
        f.write(",".join(_quote_csv_cell(h) for h in fieldnames) + "\n")

        for r in rows:
            if strategy.name == "quote_all":
                f.write(_serialize_row_quote_all(fieldnames, r) + "\n")
            elif strategy.name == "quote_text":
                f.write(_serialize_row_quote_text(fieldnames, r) + "\n")
            else:
                raise ValueError(f"Unknown strategy: {strategy.name}")


def index_rows_by_label(rows: Sequence[Dict[str, str]]) -> Dict[str, List[int]]:
    idx: Dict[str, List[int]] = {}
    for i, r in enumerate(rows):
        lab = (r.get("Label") or "").strip()
        if not lab:
            continue
        idx.setdefault(lab, []).append(i)
    return idx


def choose_row_for_label(rows: Sequence[Dict[str, str]], indices: List[int]) -> int:
    if len(indices) == 1:
        return indices[0]

    def parse_date(s: str) -> Optional[dt.date]:
        s = (s or "").strip()
        if not s:
            return None
        try:
            return dt.date.fromisoformat(s)
        except ValueError:
            return None

    best_i = indices[-1]
    best_d: Optional[dt.date] = None
    for i in indices:
        d = parse_date(rows[i].get("issued", ""))
        if d is None:
            continue
        if best_d is None or d > best_d:
            best_d = d
            best_i = i
    return best_i


def compute_membership(rows: Sequence[Dict[str, str]], use_case: str) -> Set[str]:
    present: Set[str] = set()
    for r in rows:
        lab = (r.get("Label") or "").strip()
        if not lab:
            continue
        ucs = split_usecases(r.get("UseCases", "") or "")
        if use_case in ucs:
            present.add(lab)
    return present


def update_usecases_value(original: str, use_case: str, should_have: bool) -> Tuple[str, bool]:
    ucs = split_usecases(original or "")
    s = set(ucs)

    if should_have:
        if use_case in s:
            return original, False
        s.add(use_case)
        return join_usecases(s), True

    if use_case not in s:
        return original, False
    s.remove(use_case)
    return join_usecases(s), True


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="Check and optionally synchronize a single Use Case value across bdqtest_term_versions.csv rows."
    )
    ap.add_argument("--csv", required=True, type=Path, help="Path to bdqtest_term_versions.csv")
    ap.add_argument("--spec", required=True, type=Path, help="Path to spec file containing Use Case and test labels")
    ap.add_argument("--apply", action="store_true", help="Apply changes to the CSV (otherwise report only)")
    ap.add_argument(
        "--post-ratification",
        action="store_true",
        help="Do not edit rows in place; append new changed rows with issued=<today> (and DateLastUpdated if present).",
    )
    ap.add_argument("--backup", action="store_true", help="Write a .bak copy of the original CSV when applying.")
    args = ap.parse_args(argv)

    use_case, labels = parse_spec_file(args.spec)

    rows, fieldnames = load_csv_rows(args.csv)
    label_to_indices = index_rows_by_label(rows)

    missing_labels = [lab for lab in labels if lab not in label_to_indices]
    if missing_labels:
        print("ERROR: Some labels from the spec were not found in the CSV 'Label' column:", file=sys.stderr)
        for lab in missing_labels:
            print(f"  - {lab}", file=sys.stderr)
        print("No changes were applied.", file=sys.stderr)
        return 2

    present_set = compute_membership(rows, use_case)
    desired_set = set(labels)

    should_have_but_missing = sorted(desired_set - present_set)
    should_not_have_but_present = sorted(present_set - desired_set)

    print(f"Use Case: {use_case}")
    print(f"Spec tests count: {len(labels)}")
    print(f"CSV tests count (rows): {len(rows)}")
    print()

    print("Checks:")
    if should_have_but_missing:
        print("  FAIL: These spec tests are missing the Use Case in UseCases:")
        for lab in should_have_but_missing:
            print(f"    - {lab}")
    else:
        print("  OK: All spec tests include the Use Case in UseCases.")

    if should_not_have_but_present:
        print("  FAIL: These non-spec tests include the Use Case but should not:")
        for lab in should_not_have_but_present:
            print(f"    - {lab}")
    else:
        print("  OK: No other tests include the Use Case in UseCases.")
    print()

    needs_change = bool(should_have_but_missing or should_not_have_but_present)
    if not args.apply:
        print("Dry run (no changes written).")
        return 0

    if not needs_change:
        print("No changes needed; CSV left unchanged.")
        return 0

    if args.backup:
        bak = args.csv.with_suffix(args.csv.suffix + ".bak")
        bak.write_text(args.csv.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Wrote backup: {bak}")

    strategy = detect_quoting_strategy(args.csv)
    print(f"Detected CSV quoting strategy: {strategy.name}")

    today = today_yyyy_mm_dd()
    planned_add = set(should_have_but_missing)
    planned_remove = set(should_not_have_but_present)

    if not args.post_ratification:
        changed_rows = 0
        for lab in sorted(planned_add | planned_remove):
            idxs = label_to_indices.get(lab)
            if not idxs:
                continue
            row_i = choose_row_for_label(rows, idxs)
            row = rows[row_i]
            before = row.get("UseCases", "")
            after, changed = update_usecases_value(before, use_case, should_have=(lab in desired_set))
            if changed:
                row["UseCases"] = after
                changed_rows += 1

        write_csv_rows_detected(args.csv, fieldnames, rows, strategy=strategy)
        print(f"Applied in-place updates. Rows changed: {changed_rows}")
        return 0

    if "issued" not in fieldnames:
        print("ERROR: --post-ratification requested but CSV has no 'issued' column.", file=sys.stderr)
        return 2

    date_last_updated_present = "DateLastUpdated" in fieldnames

    appended = 0
    new_rows = list(rows)

    for lab in sorted(planned_add | planned_remove):
        idxs = label_to_indices.get(lab)
        if not idxs:
            continue
        base_i = choose_row_for_label(rows, idxs)
        base_row = rows[base_i]

        before = base_row.get("UseCases", "")
        after, changed = update_usecases_value(before, use_case, should_have=(lab in desired_set))
        if not changed:
            continue

        new_row = dict(base_row)
        new_row["UseCases"] = after
        new_row["issued"] = today
        if date_last_updated_present:
            new_row["DateLastUpdated"] = today

        new_rows.append(new_row)
        appended += 1

    write_csv_rows_detected(args.csv, fieldnames, new_rows, strategy=strategy)
    print(f"Applied post-ratification updates by appending rows. Rows appended: {appended}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
