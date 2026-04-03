#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${1:-$(git rev-parse --show-toplevel)}"
TEMPLATES="$REPO_ROOT/tg2/_build_review/templates"

# Purpose:
#   Audit the BDQ Markdown *template* files under tg2/_build_review/templates for consistent, well-formed
#   normative guidance about (a) how the BDQ documents refer to ontology/vocabulary terms (Section 1.7
#   “Referring to Terms”), and (b) how term-list documents specify normative “Use of Terms” guidance
#   (Section 2 “Use of Terms” in the term-list templates).
#
#   The script is intended to support editorial and quality-control work by:
#     - Finding which templates contain Section 1.7 and verifying that the extracted 1.7 text is identical
#       across documents (using a stable end-marker sentence).
#     - Detecting missing/incorrect placement of the Section 1.7 marker sentence.
#     - Finding term-list templates that contain the “In an RDF context…” boilerplate guidance, checking
#       that the namespace prefix is templated (uses {pref_namespace_prefix}: rather than a hard-coded prefix),
#       and comparing the boilerplate wording across term lists while ignoring example term values.
#     - Counting how many paragraphs occur in Section 2 “Use of Terms” to distinguish term lists that
#       contain only the boilerplate paragraph from those that add additional normative statements.
#     - Reporting any templates that contain both the Section 1.7 marker (indicating the cross-document
#       “Referring to Terms” guidance) and a Section 2 “Use of Terms” section, to help avoid duplication
#       or unintended mixing of normative guidance.
#
# Author: GitHub Copilot (with human review and adjustments by Paul J. Morris)

if [[ ! -d "$TEMPLATES" ]]; then
  echo "ERROR: templates folder not found at: $TEMPLATES" >&2
  exit 1
fi

echo "Repo: $REPO_ROOT"
echo "Templates root: $TEMPLATES"
echo

# ----------------
# Generic helpers
# ----------------
contains_regex() { # $1=extended_regex $2=file
  grep -Eq "$1" "$2"
}

contains_fixed() { # $1=fixed_string $2=file
  grep -Fq "$1" "$2"
}

normalize_ws() {
  sed -E 's/[[:space:]]+/ /g; s/[[:space:]]+$//'
}

# ----------------
# (1) Section 1.7 helpers
# ----------------
marker_sentence="The BDQ documents use all these methods."

extract_1_7_block() { # $1=file
  awk -v marker="$marker_sentence" '
    { sub(/\r$/, "", $0) }
    /^### 1\.7 Referring to Terms \(normative\)/ {flag=1}
    flag {print}
    flag && index($0, marker) {exit}
  ' "$1"
}

file_has_marker_without_heading() { # $1=file
  awk -v marker="$marker_sentence" '
    { sub(/\r$/, "", $0) }
    /^### 1\.7 Referring to Terms \(normative\)/ {seen_heading=1}
    index($0, marker) {
      if (!seen_heading) { exit 0 }  # marker before heading -> "bad"
      else { exit 1 }                # marker after heading -> ok
    }
    END { exit 1 }                   # no marker at all -> not a match
  ' "$1"
}

# ----------------
# (2) "Use of Terms" boilerplate helpers
# ----------------

# Extract Section 2 body (everything after the "## 2 Use of Terms (normative)" heading up to next "## ").
extract_section_2_body() { # $1=file
  awk '
    { sub(/\r$/, "", $0) }
    /^##[[:space:]]+2[[:space:]]+Use[[:space:]]+of[[:space:]]+Terms([[:space:]]+\(normative\))?[[:space:]]*$/ {in2=1; next}
    in2 && /^##[[:space:]]/ {exit}
    in2 {print}
  ' "$1"
}

# Count paragraphs in Section 2 by "blank-line separated blocks of nonblank lines".
count_section_2_paragraphs() { # $1=file
  awk '
    { sub(/\r$/, "", $0) }

    /^##[[:space:]]+2[[:space:]]+Use[[:space:]]+of[[:space:]]+Terms([[:space:]]+\(normative\))?[[:space:]]*$/ {in2=1; next}
    in2 && /^##[[:space:]]/ {exit}

    in2 {
      if ($0 ~ /^[[:space:]]*$/) { inpara=0; next }
      if (!inpara) { count++; inpara=1 }
    }

    END { print count+0 }
  ' "$1"
}

# Extract Section 2 boilerplate block (for prefix check + wording hash):
# from "In an RDF context..." through (and including) the first occurrence of "MAY be used."
extract_section_2_boilerplate_block() { # $1=file
  extract_section_2_body "$1" | awk '
    /In an RDF context, a reference to a term in the/ {inbp=1}
    inbp {print}
    inbp && /MAY be used\./ {exit}
  '
}

boilerplate_is_under_section_2() { # $1=file
  [[ -n "$(extract_section_2_boilerplate_block "$1")" ]]
}

extract_backticked_prefix() {
  sed -n 's/.*`\([^`]*:\)`.*/\1/p' | head -n 1
}

canonicalize_use_terms_boilerplate() {
  normalize_ws \
  | sed -E 's/`[^`]+:`/`PREFIX:`/g' \
  | sed -E 's/`[A-Za-z0-9_]+:[A-Za-z0-9_.-]+`/`QNAME`/g' \
  | sed -E 's/`https?:\/\/[^`]+`/`IRI`/g' \
  | sed -E 's/\(local name, e\.g\., `[^`]+`\)/(local name, e.g., `LOCAL_NAME`)/g' \
  | sed -E 's/\(e\.g\., `[^`]+`\)/(e.g., `LABEL`)/g'
}

# ----------------
# Collect markdown files under templates
# ----------------
mapfile -t md_files < <(find "$TEMPLATES" -type f -name "*.md" | sort)
mapfile -t header_files < <(find "$TEMPLATES" -type f -name "*-header.md" | sort)

# ========== (1) ==========
echo "===================="
echo "(1) Files containing: ### 1.7 Referring to Terms (normative)"
echo "These should be the landing pages, guides, and extension documents"
echo "===================="

files_1_7=()
for f in "${md_files[@]}"; do
  if contains_regex '^### 1\.7 Referring to Terms \(normative\)' "$f"; then
    files_1_7+=("$f")
    echo "- $f"
  fi
done

if [[ ${#files_1_7[@]} -eq 0 ]]; then
  echo "No matches."
fi
echo

echo "--------------------"
echo "(1a) Are the 1.7 blocks identical? (sha256 of normalized extracted block)"
echo "     NOTE: extraction ends at marker sentence: \"$marker_sentence\""
echo "--------------------"
if [[ ${#files_1_7[@]} -gt 0 ]]; then
  tmpfile="$(mktemp)"
  for f in "${files_1_7[@]}"; do
    extract_1_7_block "$f" | normalize_ws | sha256sum | awk -v file="$f" '{print $1 "\t" file}' >> "$tmpfile"
  done

  unique_count="$(cut -f1 "$tmpfile" | sort | uniq | wc -l | tr -d ' ')"
  if [[ "$unique_count" == "1" ]]; then
    echo "Yes."
  else
    echo "No. Hashes:"
    sort "$tmpfile" | awk -F'\t' '{print $1 "  " $2}'
  fi
  rm -f "$tmpfile"
fi
echo

echo "--------------------"
echo "(1b) Sanity check: files with a 1.7 heading but missing the marker sentence"
echo "--------------------"
missing_marker=0
if [[ ${#files_1_7[@]} -gt 0 ]]; then
  for f in "${files_1_7[@]}"; do
    if ! extract_1_7_block "$f" | grep -Fq "$marker_sentence"; then
      echo "- $f"
      missing_marker=$((missing_marker + 1))
    fi
  done
fi
if [[ $missing_marker -eq 0 ]]; then
  echo "None."
fi
echo

echo "--------------------"
echo "(1c) Reverse sanity check: files containing the marker sentence but WITHOUT a prior 1.7 heading"
echo "--------------------"
reverse_bad=0
for f in "${md_files[@]}"; do
  if contains_fixed "$marker_sentence" "$f"; then
    if file_has_marker_without_heading "$f"; then
      echo "- $f"
      reverse_bad=$((reverse_bad + 1))
    fi
  fi
done
if [[ $reverse_bad -eq 0 ]]; then
  echo "None."
fi
echo

# ========== (2) ==========
echo "===================="
echo "(2) Section 2 Use of Terms checks"
echo "===================="

echo "--------------------"
echo "(2a) Files containing: 'In an RDF context, a reference to a term in the' (anywhere)"
echo "Tese should be all of the term-list documents"
echo "--------------------"
files_use_terms_anywhere=()
for f in "${md_files[@]}"; do
  if contains_fixed "In an RDF context, a reference to a term in the" "$f"; then
    files_use_terms_anywhere+=("$f")
    echo "- $f"
  fi
done
if [[ ${#files_use_terms_anywhere[@]} -eq 0 ]]; then
  echo "No matches."
fi
echo

echo "--------------------"
echo "(2b) Prefix templating check: files where the Section 2 boilerplate does NOT use '{pref_namespace_prefix}:'"
echo "--------------------"
bad_prefix=0
for f in "${files_use_terms_anywhere[@]}"; do
  block="$(extract_section_2_boilerplate_block "$f")"
  if [[ -z "$block" ]]; then
    continue
  fi
  actual_prefix="$(printf "%s" "$block" | extract_backticked_prefix)"
  if [[ "$actual_prefix" != "{pref_namespace_prefix}:" ]]; then
    echo "- NOT_USING_{pref_namespace_prefix}: actual=${actual_prefix:-<not found>}  $f"
    bad_prefix=$((bad_prefix + 1))
  fi
done
if [[ $bad_prefix -eq 0 ]]; then
  echo "All Section 2 boilerplate occurrences use '{pref_namespace_prefix}:'."
fi
echo

echo "--------------------"
echo "(2c) Paragraph count check: files with '## 2 Use of Terms' and number of paragraphs in that section"
echo "     Expectation with current formatting: 1 = boilerplate only; >1 = boilerplate + additional text"
echo "--------------------"
files_with_section2=()
for f in "${md_files[@]}"; do
  if contains_regex '^##[[:space:]]+2[[:space:]]+Use[[:space:]]+of[[:space:]]+Terms' "$f"; then
    files_with_section2+=("$f")
  fi
done

if [[ ${#files_with_section2[@]} -eq 0 ]]; then
  echo "No files contain a '## 2 Use of Terms' section."
else
  tmpfile="$(mktemp)"
  for f in "${files_with_section2[@]}"; do
    n="$(count_section_2_paragraphs "$f")"
    printf "%s\t%s\n" "$n" "$f" >> "$tmpfile"
  done

  sort -n -k1,1 "$tmpfile" | awk -F'\t' '{printf "%s  %s\n", $1, $2}'
  rm -f "$tmpfile"
fi
echo

echo "--------------------"
echo "(2d) Wording alignment: does the Section 2 boilerplate differ beyond examples?"
echo "     (Compares canonicalized Section 2 boilerplate text across files where it exists.)"
echo "--------------------"
tmpfile="$(mktemp)"
count_blocks=0
for f in "${files_use_terms_anywhere[@]}"; do
  block="$(extract_section_2_boilerplate_block "$f")"
  if [[ -z "$block" ]]; then
    continue
  fi
  count_blocks=$((count_blocks + 1))
  canon_hash="$(
    printf "%s" "$block" \
      | canonicalize_use_terms_boilerplate \
      | sha256sum | awk '{print $1}'
  )"
  printf "%s\t%s\n" "$canon_hash" "$f" >> "$tmpfile"
done

if [[ $count_blocks -eq 0 ]]; then
  echo "No Section 2 boilerplate blocks found to compare."
else
  unique_count="$(cut -f1 "$tmpfile" | sort | uniq | wc -l | tr -d ' ')"
  if [[ "$unique_count" == "1" ]]; then
    echo "Boilerplate wording is aligned (differences are only in examples/values/whitespace)."
  else
    echo "Boilerplate wording differs across files (beyond examples). Hashes:"
    sort "$tmpfile" | awk -F'\t' '{print $1 "  " $2}'
  fi
fi
rm -f "$tmpfile"
echo

# ========== (3) ==========
echo "===================="
echo "(3) *-header.md templates missing 1.7"
echo "These should be the term-list documents and multiple supporting documents"
echo "===================="

missing=0
for f in "${header_files[@]}"; do
  if ! contains_regex '^### 1\.7 Referring to Terms \(normative\)' "$f"; then
    echo "- $f"
    missing=$((missing + 1))
  fi
done

if [[ $missing -eq 0 ]]; then
  echo "None."
fi
echo

# ========== (4) ==========
echo "===================="
echo "(4) Files containing BOTH: Section 1.7 (with marker sentence) AND Section 2 'Use of Terms'"
echo "There should be none of these"
echo "===================="

both=0
for f in "${md_files[@]}"; do
  # Section 1.7 with marker: easiest stable proxy is that marker sentence exists and the 1.7 heading exists.
  has_17=0
  if contains_regex '^### 1\.7 Referring to Terms \(normative\)' "$f" && contains_fixed "$marker_sentence" "$f"; then
    has_17=1
  fi

  # Section 2 Use of Terms heading present (normative or not; tolerate missing "(normative)")
  has_2=0
  if contains_regex '^##[[:space:]]+2[[:space:]]+Use[[:space:]]+of[[:space:]]+Terms' "$f"; then
    has_2=1
  fi

  if [[ "$has_17" -eq 1 && "$has_2" -eq 1 ]]; then
    echo "- $f"
    both=$((both + 1))
  fi
done

if [[ $both -eq 0 ]]; then
  echo "None."
fi
echo
