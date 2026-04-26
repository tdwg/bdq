#!/usr/bin/env python3
"""
Rewrite legacy information_element_guids.csv labels for MultiRecord aggregated-response ActedUpon IEs
from the pseudo-term form:

  Information Element ActedUpon bdqval:VALIDATION_X.Response

to the canonical form:

  Information Element ActedUpon bdqval:AggregatedTestResponseOutcomes for bdqtest:VALIDATION_X.Response

This preserves GUIDs (stable identifiers) while updating the human-readable label to match the
new modeling pattern in which:
  - composedOf uses the real term bdqval:AggregatedTestResponseOutcomes
  - aggregatesResponsesFrom links to the upstream bdqffdq:DataQualityNeed (typically a bdqtest:* term)

This script only rewrites rows that match the legacy pattern exactly; all other rows are preserved.

Input/Output are rectangular CSVs with consistent column counts per row.

Usage:
  python3 tg2/_build_review/scripts/rewrite_ie_guid_labels_for_aggregated_responses.py \
    --input tg2/core/information_element_guids.csv \
    --output tg2/core/information_element_guids.rewritten.csv

Optional:
  --dry-run        print what would change, but do not write output
  --in-place       overwrite input file (writes via temp file then replaces)
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
import pandas as pd


LEGACY_LABEL_RE = re.compile(
    r'^\s*Information Element ActedUpon\s+bdqval:(?P<upstream>[A-Z][A-Z0-9_]+)\.Response\s*$'
)

NEW_LABEL_TEMPLATE = (
    "Information Element ActedUpon bdqval:AggregatedTestResponseOutcomes "
    "for bdqtest:{upstream}.Response"
)


def rewrite_label(label: str) -> tuple[bool, str]:
    m = LEGACY_LABEL_RE.match(label or "")
    if not m:
        return (False, label)
    upstream = m.group("upstream")
    return (True, NEW_LABEL_TEMPLATE.format(upstream=upstream))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="tg2/core/information_element_guids.csv")
    ap.add_argument("--output", default="tg2/core/information_element_guids.rewritten.csv")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite --input (safe temp-file replace). Ignores --output.",
    )
    args = ap.parse_args()

    df = pd.read_csv(args.input, na_filter=False, dtype=str)

    # Basic validation
    for col in ("guid", "label"):
        if col not in df.columns:
            raise ValueError(f"Expected column '{col}' not found in {args.input}")

    changed = 0
    for idx, row in df.iterrows():
        old = row["label"]
        did, new = rewrite_label(old)
        if did and new != old:
            df.at[idx, "label"] = new
            changed += 1

    print(f"Rows rewritten: {changed}")
    if changed:
        # Show a small sample of changes for review
        sample = []
        for _, row in df.iterrows():
            # find rewritten rows by presence of AggregatedTestResponseOutcomes and "for bdqtest:"
            if "AggregatedTestResponseOutcomes" in row["label"] and "for bdqtest:" in row["label"]:
                sample.append(row["label"])
            if len(sample) >= 10:
                break
        if sample:
            print("Sample rewritten labels (up to 10):")
            for s in sample:
                print(f"  - {s}")

    if args.dry_run:
        print("Dry run: no output written.")
        return 0

    if args.in_place:
        # Write to temp, then replace input
        in_dir = os.path.dirname(os.path.abspath(args.input)) or "."
        fd, tmp_path = tempfile.mkstemp(prefix="information_element_guids.", suffix=".tmp.csv", dir=in_dir)
        os.close(fd)
        try:
            df.to_csv(tmp_path, index=False, lineterminator="\n")
            os.replace(tmp_path, args.input)
            print(f"Wrote updated file in-place: {args.input}")
        finally:
            try:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
            except Exception:
                pass
    else:
        df.to_csv(args.output, index=False, lineterminator="\n")
        print(f"Wrote updated file: {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())