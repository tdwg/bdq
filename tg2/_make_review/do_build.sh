#!/bin/bash
cd ../_review/build/
python3 draft_build_bdqcore_qrg.py
python3 draft_build_bdqffdq.py
python3 draft_build-docs.py
python3 draft_build-termlist_bdqcore.py
python3 draft_build-termlist.py
python3 make_bdq_tests_vertical.py
cd ../../_make_review/
