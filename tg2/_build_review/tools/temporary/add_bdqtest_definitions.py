#!/usr/bin/env python3
"""
Generate or complete a 'definition' column for TDWG BDQ Test CSV files.

@author
    GPT-5.1 with human review and adjustments by @chicoreus Paul J. Morris

Overview
========
This script reads a CSV file containing BDQ Test term versions (e.g.
bdqtest_term_versions.csv) and ensures that each row has a human‑readable
definition constructed from existing columns.

It:

  * Handles both SingleRecord and MultiRecord tests (Validation, Amendment,
    Issue, Measure).
  * For SingleRecord tests:
      - Uses Type, Resource Type, Description, ExpectedResponse.
      - If AuthoritiesDefaults is present, extracts a short source authority
        name.
      - If Parameters is present, notes that behavior can be changed by those
        parameters.
  * For MultiRecord Measures:
      - Distinguishes QA measures (Label starts with MULTIRECORD_MEASURE_QA_)
        and COUNT measures (Label contains _COUNT_).
      - Adds phrases “for quality assurance” or “for quality control”
        respectively.
      - Resolves aggregatesResponsesFrom IRIs to their Label(s) by looking
        them up in the same CSV, and states the dependency in the definition.

Preservation behavior
=====================
ABSOLUTE requirements implemented:

  * If the input CSV does NOT have a 'definition' column:
      - Every existing byte of every existing column (header and data) is
        preserved EXACTLY.
      - The script appends a new ',<definition cell>' to the end of each row.
      - It does this by:
          - Reading the whole file as text lines (assuming no embedded newlines
            inside quoted fields).
          - Using CSV parsing ONLY to construct definitions and to serialize
            the new definition cell.
          - Concatenating the original line (minus its newline) plus
            '<delimiter><serialized-definition>' and then the original newline.

  * If the input CSV ALREADY has a 'definition' column:
      - The entire file is rewritten in “quote all” mode (csv.QUOTE_ALL),
        preserving all cell VALUES (including the existing definitions that
        are not changed) and column order, but normalizing quoting so that
        every field is quoted.
      - In this mode, any changed definition values are included, and all
        non‑definition values are preserved exactly as strings.

Robustness
==========
  * Parsing problems (e.g. AuthoritiesDefaults that cannot be shortened,
    unknown aggregatesResponsesFrom IRIs, or unexpected row structures)
    produce warnings on stderr, but a fallback definition is still created
    for every row.

Usage
=====
  Basic usage with defaults:

      python bdq_definitions.py

  Using a specific input file:

      python bdq_definitions.py -i my_tests.csv

  Specifying an output file:

      python bdq_definitions.py -i bdqtest_term_versions.csv -o bdqtest_term_versions_with_definitions.csv

  Show help:

      python bdq_definitions.py -h

Defaults
========
  * Default input:  bdqtest_term_versions.csv
  * Default output: <input_basename>_with_definitions.csv

Assumptions
===========
  * The input file does not contain embedded newlines inside fields. This is
    true for the current BDQ test CSVs; if that ever changes, raw‑line
    preservation logic would need to be updated.
"""

import argparse
import csv
import io
import re
import sys
from pathlib import Path
from typing import Dict, List

import pandas as pd

warnings: List[str] = []  # collect warning messages


def warn(msg: str):
    """Record a warning message to be printed at the end."""
    warnings.append(msg)


# ---------- Dialect detection ----------

def sniff_dialect(path: str) -> csv.Dialect:
    """
    Sniff the CSV dialect (delimiter, quotechar, etc.) from the input file.
    Falls back to csv.excel if sniffing fails.
    """
    try:
        with open(path, "r", newline="", encoding="utf-8") as f:
            sample = f.read(4096)
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            return dialect
    except Exception as e:
        warn(f"[Dialect sniff] Could not sniff CSV dialect from {path}: {e}; using csv.excel.")
        return csv.excel


# ---------- Helpers for SingleRecord Tests ----------

def shorten_authorities(auth_text: str, row_label: str) -> str:
    """
    Produce a short, human-readable phrase from AuthoritiesDefaults.

    Typical input examples:
      'bdqval:sourceAuthority default = "The Getty Thesaurus of Geographic Names (TGN)" {[...]}'
      'bdqval:sourceAuthority = "DCMI Type Vocabulary" {[...]}'

    Returns something like:
      'The Getty Thesaurus of Geographic Names (TGN)'
      'DCMI Type Vocabulary'

    On any parsing problem, returns the original text and records a warning.
    """
    if not auth_text:
        return ""

    try:
        # 1. Drop everything from the first '{' onward (URLs, extra notes).
        no_braces = auth_text.split("{", 1)[0].strip()

        # 2. If there is a quoted string, use the first one.
        m = re.search(r'"([^"]+)"', no_braces)
        if m:
            return m.group(1).strip()

        # 3. Otherwise, try the part after '=' (e.g. after 'default =').
        if "=" in no_braces:
            right = no_braces.split("=", 1)[1].strip()
            # Drop leading "default" if present
            if right.lower().startswith("default"):
                right = right.split(None, 1)[1] if " " in right else ""
            return right.strip() or no_braces

        # 4. Fallback: return the trimmed text.
        return no_braces

    except Exception as e:
        warn(f"[AuthoritiesDefaults parse issue in {row_label}] {e}; using raw text.")
        return auth_text.strip()


def build_singlerecord_definition(row: Dict[str, str]) -> str:
    """
    Construct a definition for SingleRecord tests (Validation, Amendment, Issue, Measure).
    """
    test_type     = (row.get("Type") or "").strip()
    resource_type = (row.get("Resource Type") or "").strip()
    desc          = (row.get("Description") or "").strip()
    expected      = (row.get("ExpectedResponse") or "").strip()
    auth_defaults = (row.get("AuthoritiesDefaults") or "").strip()
    params        = (row.get("Parameters") or "").strip()
    label         = (row.get("Label") or "").strip()

    parts: List[str] = []

    # Intro: "A <Type> Test, applied to a <Resource Type>"
    if test_type:
        intro = f"A {test_type} Test"
    else:
        intro = "A Test"

    if resource_type:
        intro += f", applied to a {resource_type}"
    parts.append(intro + ",")

    # Description
    if desc:
        if not desc.endswith((".", "?", "!")):
            desc += "."
        parts.append(f"that evaluates: {desc}")
    else:
        parts.append("that evaluates the relevant criteria.")

    # ExpectedResponse next (before authority/parameter clauses)
    if expected:
        expected_clean = " ".join(expected.split())
        if not expected_clean.endswith((".", "?", "!")):
            expected_clean += "."
        parts.append(f"It returns: {expected_clean}")

    # Authorities/parameters
    short_auth = ""
    if auth_defaults:
        short_auth = shorten_authorities(auth_defaults, label)

    if short_auth and not params:
        # Source authority only, no parameters
        parts.append(f"It uses the source authority: {short_auth}.")
    elif short_auth and params:
        # Has source authority and parameters
        parts.append(
            f"It uses the following default authority and/or parameter values: {short_auth}."
        )
        parts.append(
            f"Its behavior can be altered by the following parameter(s): {params}."
        )
    elif params:
        # Parameters but no authority text
        parts.append(
            f"Its behavior can be altered by the following parameter(s): {params}."
        )

    return " ".join(parts)


# ---------- Helpers for MultiRecord Measures ----------

def build_iri_to_label_map(df: pd.DataFrame) -> Dict[str, str]:
    """
    Build a map from term_iri -> Label using the rows in the same file.
    """
    iri_to_label: Dict[str, str] = {}
    for _, r in df.iterrows():
        term_iri = str(r.get("term_iri") or "").strip()
        if term_iri:
            iri_to_label[term_iri] = str(r.get("Label") or "").strip()
    return iri_to_label


def resolve_aggregates(agg_str: str, iri_to_label: Dict[str, str], row_label: str) -> str:
    """
    Resolve aggregatesResponsesFrom IRIs to Labels,
    falling back to the IRI and warning if a lookup fails.
    Handles comma-separated lists.
    """
    if not agg_str:
        return ""

    pieces = [s.strip() for s in agg_str.split(",") if s.strip()]
    labels: List[str] = []

    for iri in pieces:
        try:
            label = iri_to_label.get(iri, "")
            if label:
                labels.append(label)
            else:
                labels.append(iri)
                warn(f"[Lookup issue in {row_label}] Could not resolve aggregatesResponsesFrom IRI: {iri}")
        except Exception as e:
            labels.append(iri)
            warn(f"[Lookup error in {row_label}] {e}; using IRI: {iri}")

    return ", ".join(labels)


def build_multirecord_definition(row: Dict[str, str], iri_to_label: Dict[str, str]) -> str:
    """
    Construct a definition for MultiRecord Measure tests that aggregate
    results from other tests.
    """
    label         = (row.get("Label") or "").strip()
    resource_type = (row.get("Resource Type") or "").strip()  # expected "MultiRecord"
    desc          = (row.get("Description") or "").strip()
    expected      = (row.get("ExpectedResponse") or "").strip()
    agg_from      = (row.get("aggregatesResponsesFrom") or "").strip()

    # Determine QA vs COUNT vs generic
    if label.startswith("MULTIRECORD_MEASURE_QA_"):
        eval_phrase = "that evaluates for quality assurance:"
    elif "_COUNT_" in label:
        eval_phrase = "that evaluates for quality control:"
    else:
        eval_phrase = "that evaluates:"

    parts: List[str] = []

    # Intro: "A Measure, applied to a MultiRecord, that evaluates ..."
    intro = f"A Measure, applied to a {resource_type}, {eval_phrase}"
    parts.append(intro)

    # Description
    if desc:
        if not desc.endswith((".", "?", "!")):
            desc += "."
        parts.append(desc)
    else:
        parts.append("aggregated outcomes from other Tests.")

    # ExpectedResponse
    if expected:
        expected_clean = " ".join(expected.split())
        if not expected_clean.endswith((".", "?", "!")):
            expected_clean += "."
        parts.append(f"It returns: {expected_clean}")

    # Aggregates from which Tests?
    resolved = ""
    if agg_from:
        resolved = resolve_aggregates(agg_from, iri_to_label, label)

    if resolved:
        parts.append(
            f"It is based on the aggregated outcomes of the Test(s): {resolved}."
        )

    return " ".join(parts)


# ---------- Dispatcher ----------

def build_definition_for_row(row: Dict[str, str], iri_to_label: Dict[str, str]) -> str:
    """
    Choose appropriate builder based on Resource Type.
    Always returns a non-empty definition string.
    """
    resource_type = (row.get("Resource Type") or "").strip()
    try:
        if resource_type == "MultiRecord":
            definition = build_multirecord_definition(row, iri_to_label)
        else:
            definition = build_singlerecord_definition(row)
    except Exception as e:
        # Last-resort fallback: very generic definition
        label = (row.get("Label") or "").strip()
        warn(f"[Definition build error in {label}] {e}; using fallback definition.")
        definition = f"A Test definition could not be fully constructed automatically for Label={label}."

    # Ensure we don't return an empty string
    if not definition.strip():
        label = (row.get("Label") or "").strip()
        warn(f"[Empty definition in {label}] Using minimal fallback.")
        definition = f"A Test for Label={label}."

    return definition


# ---------- Main logic ----------

def main():
    parser = argparse.ArgumentParser(
        description="Generate or complete a 'definition' column for BDQ Test CSV files.",
    )
    parser.add_argument(
        "-i", "--input",
        default="bdqtest_term_versions.csv",
        help="Input CSV file (default: bdqtest_term_versions.csv)",
    )
    parser.add_argument(
        "-o", "--output",
        help=(
            "Output CSV file. "
            "If not specified, uses '<input_basename>_with_definitions.csv'."
        ),
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: Input CSV '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_name(
            input_path.stem + "_with_definitions" + input_path.suffix
        )

    # Sniff dialect for quoting/delimiter style
    dialect = sniff_dialect(str(input_path))
    delimiter   = getattr(dialect, "delimiter", ",")
    quotechar   = getattr(dialect, "quotechar", '"')
    doublequote = getattr(dialect, "doublequote", True)
    escapechar  = getattr(dialect, "escapechar", None)

    # Load into pandas for semantic work (definitions, iri_to_label)
    df = pd.read_csv(
        input_path,
        dtype=str,
        sep=delimiter,
        quotechar=quotechar,
        doublequote=doublequote,
        escapechar=escapechar,
    ).fillna("")

    iri_to_label = build_iri_to_label_map(df)

    has_definition_col = "definition" in df.columns
    def_idx = None
    if has_definition_col:
        def_idx = list(df.columns).index("definition")

    # Precompute definitions by row index
    index_to_def: Dict[int, str] = {}
    for idx, row in df.iterrows():
        row_dict = {col: str(row[col] or "") for col in df.columns}
        existing_def = row_dict.get("definition", "")
        if has_definition_col and existing_def.strip():
            # Preserve existing text as value; we'll still reserialize in quote-all mode.
            index_to_def[idx] = existing_def
        else:
            index_to_def[idx] = build_definition_for_row(row_dict, iri_to_label)

    # Case 1: no 'definition' column -> strict preservation of all existing text
    if not has_definition_col:
        # Read raw lines with newlines preserved
        with open(input_path, "r", encoding="utf-8", newline="") as fin:
            raw_lines = fin.read().splitlines(keepends=True)

        if not raw_lines:
            print("ERROR: Input file is empty.", file=sys.stderr)
            sys.exit(1)

        # Detect newline sequence from first line
        first_line = raw_lines[0]
        if first_line.endswith("\r\n"):
            newline_seq = "\r\n"
        elif first_line.endswith("\n"):
            newline_seq = "\n"
        else:
            newline_seq = "\n"

        # Build a one-cell CSV writer for serializing definition cells
        def serialize_cell(value: str) -> str:
            buf = io.StringIO()
            w = csv.writer(
                buf,
                delimiter=delimiter,
                quotechar=quotechar,
                doublequote=doublequote,
                escapechar=escapechar,
                quoting=csv.QUOTE_MINIMAL,
            )
            w.writerow([value])
            cell_line = buf.getvalue().rstrip("\r\n")
            return cell_line

        with open(output_path, "w", encoding="utf-8", newline="") as fout:
            # Header line: append new header cell
            header_line = raw_lines[0]
            header_no_nl = header_line.rstrip("\r\n")
            new_header = f"{header_no_nl}{delimiter}{quotechar}definition{quotechar}{newline_seq}"
            fout.write(new_header)

            # Data lines: append serialized definition cell
            for row_index, raw_line in enumerate(raw_lines[1:], start=0):
                # df row index 0 corresponds to second physical line (row_index 0 here)
                if row_index not in index_to_def:
                    # No semantic row; just copy line
                    fout.write(raw_line)
                    continue
                def_value = index_to_def[row_index]
                raw_no_nl = raw_line.rstrip("\r\n")
                serialized_def = serialize_cell(def_value)
                fout.write(f"{raw_no_nl}{delimiter}{serialized_def}{newline_seq}")

    # Case 2: 'definition' column exists -> rewrite entire file in quote-all mode
    else:
        with open(input_path, "r", encoding="utf-8", newline="") as fin, \
             open(output_path, "w", encoding="utf-8", newline="") as fout:

            reader = csv.reader(
                fin,
                delimiter=delimiter,
                quotechar=quotechar,
                doublequote=doublequote,
                escapechar=escapechar,
            )

            writer = csv.writer(
                fout,
                delimiter=delimiter,
                quotechar=quotechar,
                doublequote=doublequote,
                escapechar=escapechar,
                quoting=csv.QUOTE_ALL,  # switch to quote-all format
                lineterminator=getattr(dialect, "lineterminator", "\n") or "\n",
            )

            # Header
            header_fields = next(reader)
            writer.writerow(header_fields)

            # Data rows
            row_index = 0
            for fields in reader:
                if row_index in index_to_def and def_idx is not None:
                    # Overwrite or preserve definition cell with precomputed value
                    # (value is the same if the user provided one).
                    # Ensure fields list is long enough
                    if def_idx >= len(fields):
                        # Append missing cells up to def_idx
                        while len(fields) < def_idx:
                            fields.append("")
                        fields.append(index_to_def[row_index])
                    else:
                        fields[def_idx] = index_to_def[row_index]
                writer.writerow(fields)
                row_index += 1

    # Print warnings, if any
    if warnings:
        print("Warnings encountered while generating definitions:", file=sys.stderr)
        for w in warnings:
            print(" -", w, file=sys.stderr)


if __name__ == "__main__":
    main()
