#!/bin/bash
# From the root of the bdq repository tree:
cd tg2/_build_review/
python3 draft_build_bdqtest_qrg.py
python3 draft_build_bdqffdq.py
python3 draft_build-docs.py
python3 draft_build-termlist_bdqtest.py
python3 draft_build-termlist.py
python3 make_bdq_tests_vertical.py
cd ../_make_review/
