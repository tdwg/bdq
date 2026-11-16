#!/usr/bin/env bash
# Draft build: the BDQ documents and dist/ from proposed changes (deployment_rs_tdwg_org.md, Section 13.1).
#
# A proposed change is made as a release under test in a local rs.tdwg.org checkout, without committing
# it: create the release directory there (process/bdq-revisions/bdq_new_release.py for Tests) and process
# it, as in "Changing a Test" in process/bdq-revisions/README.md (on a scratch worktree of the bdq branch).
# This script then
#   1. exports that checkout's working tree into this repository's generated copies
#      (export_rs_baseline.py --worktree),
#   2. regenerates the derived Test tables (copy_files.sh) and the documents (do_build.sh), with the
#      builders reading the same checkout (BDQ_RS_SOURCE),
#   3. marks every generated document as a draft, not issued (mark_draft.py).
#
# The result replaces the accepted state in this working tree: run it on a branch for the draft (never on
# master), and do not merge it; when the change is accepted and processed onto rs.tdwg.org's bdq branch,
# the ordinary export and build bring it in.
#
# Usage (from tg2/_make_review):
#     ./draft_build.sh <path to the rs.tdwg.org checkout> <date of the release under test, YYYY-MM-DD>
set -eu

if [ $# -ne 2 ]; then
    echo "Usage: $0 <rs.tdwg.org checkout> <release date YYYY-MM-DD>" >&2
    exit 2
fi
RS=$(cd "$1" && pwd)
RELEASE_DATE=$2
cd "$(dirname "$0")"

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" = "master" ]; then
    echo "draft_build.sh: on master; check out a branch for the draft first" >&2
    exit 1
fi
if [ ! -d "$RS/process/bdq-revisions/bdq-revisions-$RELEASE_DATE" ]; then
    echo "draft_build.sh: no release directory bdq-revisions-$RELEASE_DATE in $RS" >&2
    exit 1
fi

SOURCE="$(git -C "$RS" rev-parse --short HEAD) with uncommitted changes in a local checkout"
python3 export_rs_baseline.py --rs "$RS" --worktree
bash copy_files.sh
BDQ_RS_SOURCE="$RS" bash do_build.sh
python3 mark_draft.py --release-date "$RELEASE_DATE" --source "$SOURCE"
echo "Draft build from $RS (release $RELEASE_DATE under test) on branch $BRANCH: review with git diff; do not merge."
