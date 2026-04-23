#!/bin/bash
set -eu

# From _make_review/:
cd ../_build_review/

echo "Running bdqffdq/bdqtest consistency audit..."
python3 tools/audit_bdqffdq_vs_bdqtest.py --owl ../_review/vocabulary/bdqffdq.owl --ttl ../_review/dist/bdqtest.ttl

python3 draft_build_bdqtest_qrg.py
python3 draft_build_bdqffdq.py
python3 draft_build-docs.py
python3 draft_build-termlist_bdqtest.py
python3 draft_build-termlist.py
python3 make_bdq_tests_vertical.py
cd ../_make_review/
