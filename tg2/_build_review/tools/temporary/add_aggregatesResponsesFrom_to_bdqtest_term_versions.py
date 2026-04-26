#!/usr/bin/env python3
"""
Add `aggregatesResponsesFrom` column to bdqtest_term_versions.csv and migrate
MultiRecord Measure rows that currently encode aggregated inputs as pseudo-terms
like `bdqval:VALIDATION_FOO.Response`.

Changes vs earlier draft:
  - Inserts `aggregatesResponsesFrom` immediately after `InformationElement:ActedUpon`
    when the column is newly added.
  - Ensures the output CSV is structurally rectangular (same number of columns per row)
    by using the DataFrame's column set for all rows (pandas guarantees this) and by
    writing with the csv module quoting rules.
  - Preserves all existing data and headers (only modifies the two target columns for
    matching rows; adds the new header if absent).

Usage:
  python3 tg2/_build_review/scripts/add_aggregatesResponsesFrom_to_bdqtest_term_versions.py \
    --input tg2/_review/vocabulary/bdqtest_term_versions.csv \
    --output tg2/_review/vocabulary/bdqtest_term_versions.with_aggregatesResponsesFrom.csv
"""

from __future__ import annotations

import argparse
import sys
import re
import pandas as pd


PSEUDO_RESPONSE_RE = re.compile(r"^\s*bdqval:(?P<label>[A-Z][A-Z0-9_]+)\.Response\s*$")


def insert_column_after(df: pd.DataFrame, new_col: str, after_col: str) -> pd.DataFrame:
    """
    Return a new DataFrame with `new_col` inserted immediately after `after_col`.
    If new_col already exists, returns df unchanged.
    """
    if new_col in df.columns:
        return df
    if after_col not in df.columns:
        # Fall back to appending at end, but this should not happen for this CSV.
        df[new_col] = ""
        return df

    cols = list(df.columns)
    insert_at = cols.index(after_col) + 1
    cols.insert(insert_at, new_col)

    df2 = df.copy()
    df2[new_col] = ""
    # Reorder columns
    df2 = df2[cols]
    return df2


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--input",
        default="tg2/_review/vocabulary/bdqtest_term_versions.csv",
        help="Path to bdqtest_term_versions.csv (master copy).",
    )
    ap.add_argument(
        "--output",
        default="tg2/_review/vocabulary/bdqtest_term_versions.with_aggregatesResponsesFrom.csv",
        help="Path to write the revised CSV for review.",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write output; print summary only.",
    )
    args = ap.parse_args()

    # Read. Use na_filter=False to preserve empty strings, and keep everything as text.
    df = pd.read_csv(args.input, na_filter=False, dtype=str)

    required_cols = ["Label", "term_iri", "Type", "Resource Type", "InformationElement:ActedUpon"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Expected column '{col}' was not found in the input CSV.")

    new_col = "aggregatesResponsesFrom"

    # Insert aggregatesResponsesFrom next to InformationElement:ActedUpon (if missing).
    df = insert_column_after(df, new_col=new_col, after_col="InformationElement:ActedUpon")

    # Build lookup map: upstream test Label -> upstream term_iri (unversioned).
    label_to_term_iri = {}
    for _, row in df.iterrows():
        label = (row.get("Label") or "").strip()
        term_iri = (row.get("term_iri") or "").strip()
        if label and term_iri:
            label_to_term_iri[label] = term_iri

    scanned = 0
    matched = 0
    updated = 0
    unresolved = 0
    already_set = 0

    for idx, row in df.iterrows():
        if (row.get("Type") or "").strip() != "Measure":
            continue
        if (row.get("Resource Type") or "").strip() != "MultiRecord":
            continue

        scanned += 1
        acted = (row.get("InformationElement:ActedUpon") or "").strip()

        m = PSEUDO_RESPONSE_RE.match(acted)
        if not m:
            continue

        matched += 1
        upstream_label = m.group("label")
        upstream_term_iri = label_to_term_iri.get(upstream_label, "").strip()

        if not upstream_term_iri:
            unresolved += 1
            print(
                f"WARNING: row {idx}: could not resolve upstream Label '{upstream_label}' "
                f"from InformationElement:ActedUpon='{acted}'. Leaving row unchanged.",
                file=sys.stderr,
            )
            continue

        existing = (row.get(new_col) or "").strip()
        if existing:
            already_set += 1
            if existing != upstream_term_iri:
                print(
                    f"WARNING: row {idx}: {new_col} already set to '{existing}' "
                    f"but inferred upstream is '{upstream_term_iri}'. Overwriting.",
                    file=sys.stderr,
                )

        df.at[idx, new_col] = upstream_term_iri
        df.at[idx, "InformationElement:ActedUpon"] = "bdqval:AggregatedTestResponseOutcomes"
        updated += 1

    print("Migration summary:")
    print(f"  MultiRecord Measure rows scanned: {scanned}")
    print(f"  Rows with pseudo-response actedUpon matched: {matched}")
    print(f"  Rows updated: {updated}")
    print(f"  Rows unresolved (left unchanged): {unresolved}")
    print(f"  Rows where aggregatesResponsesFrom was already set: {already_set}")

    if args.dry_run:
        print("Dry run: no output written.")
        return 0

    # Write. Pandas ensures rectangular output; index=False preserves the original structure.
    # lineterminator='\n' avoids CRLF surprises across platforms.
    df.to_csv(args.output, index=False, lineterminator="\n")
    print(f"Wrote updated CSV to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())