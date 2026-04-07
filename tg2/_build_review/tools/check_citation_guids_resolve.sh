#!/usr/bin/env bash
#
# Check whether the "guid" URLs in a CSV have a live landing page.
#
# We treat a GUID as having a "live landing page" if, after following redirects:
#   - it returns 2xx or 3xx, OR
#   - it returns 401 or 403 (reachable but access-restricted), OR
#   - HEAD is unsupported/blocked but a minimal GET (Range: 0-0) succeeds under the same rules.
#
# Usage:
#   check_citation_guids_resolve.sh <TG2_citation_guids.csv>
#
# Options:
#   -h, --help   Show help and exit
#
# @author github copilot with user guidance and review from Paul J. Morris

set -euo pipefail

print_help() {
  cat <<'EOF'
check_citation_guids_resolve.sh - check whether citation GUID URLs have a live landing page

Usage:
  check_citation_guids_resolve.sh <TG2_citation_guids.csv>

The CSV is expected to have a header row and "guid" as the first column, e.g.:
  "guid","citation"
  "https://doi.org/10.15468/doc-gg7h-s853","Chapman ..."

Definition used:
  A URL is considered "live" if the final HTTP status after redirects is:
    - 2xx or 3xx (success/redirect), OR
    - 401 or 403 (reachable but access-restricted)

Behavior:
  - Extracts the first CSV column (guid), skipping the header row.
  - For each URL:
      1) try HTTP HEAD (follows redirects)
      2) if that is not "live", fall back to a minimal HTTP GET using Range: 0-0
  - Exits 1 if any URLs are not live, otherwise exits 0.

Options:
  -h, --help   Show this help and exit
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  print_help
  exit 0
fi

CSV_FILE="${1:-}"
if [[ -z "$CSV_FILE" ]]; then
  print_help
  exit 2
fi

if [[ ! -r "$CSV_FILE" ]]; then
  echo "ERROR: cannot read CSV file: $CSV_FILE" >&2
  exit 2
fi

UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
ACCEPT='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

# Extract first CSV column (guid), skipping header, stripping surrounding quotes.
# Assumes no embedded commas in the guid column.
mapfile -t URLS < <(
  tail -n +2 "$CSV_FILE" \
    | awk -F',' '{print $1}' \
    | sed -E 's/^"//; s/"$//; s/\r$//'
)

is_live_code() {
  local code="${1:-}"
  [[ "$code" =~ ^2[0-9][0-9]$ || "$code" =~ ^3[0-9][0-9]$ || "$code" == "401" || "$code" == "403" ]]
}

curl_head() {
  local url="$1"
  local out code effective
  out="$(
    curl -A "$UA" -H "Accept: $ACCEPT" -sS -L -I --max-time 25 \
      -w $'\n%{http_code}\n%{url_effective}\n' \
      "$url" 2>/dev/null || true
  )"
  code="$(printf "%s" "$out" | tail -n 2 | head -n 1)"
  effective="$(printf "%s" "$out" | tail -n 1)"
  printf "%s %s" "$code" "$effective"
}

curl_get_range() {
  local url="$1"
  local out code effective
  out="$(
    curl -A "$UA" -H "Accept: $ACCEPT" -sS -L --range 0-0 --max-time 25 \
      -o /dev/null \
      -w $'%{http_code}\n%{url_effective}\n' \
      "$url" 2>/dev/null || true
  )"
  code="$(printf "%s" "$out" | tail -n 2 | head -n 1)"
  effective="$(printf "%s" "$out" | tail -n 1)"
  printf "%s %s" "$code" "$effective"
}

total=0
ok=0
bad=0

echo "Checking ${#URLS[@]} GUID URLs from: $CSV_FILE"
echo "Rule: live if final HTTP status is 2xx/3xx/401/403 (HEAD, else GET(range))."
echo

for url in "${URLS[@]}"; do
  [[ -z "$url" ]] && continue
  total=$((total+1))

  read -r head_code head_effective <<<"$(curl_head "$url")"
  if is_live_code "$head_code"; then
    ok=$((ok+1))
    printf "LIVE %s  HEAD -> %s\n" "$head_code" "$head_effective"
    continue
  fi

  read -r get_code get_effective <<<"$(curl_get_range "$url")"
  if is_live_code "$get_code"; then
    ok=$((ok+1))
    printf "LIVE %s  GET(range) -> %s  (HEAD was %s)\n" "$get_code" "$get_effective" "${head_code:-000}"
  else
    bad=$((bad+1))
    printf "DEAD HEAD=%s GET=%s  %s\n" "${head_code:-000}" "${get_code:-000}" "$url"
  fi
done

echo
echo "Summary:"
echo "  total: $total"
echo "  live:  $ok"
echo "  dead:  $bad"

if [[ "$bad" -gt 0 ]]; then
  exit 1
fi
