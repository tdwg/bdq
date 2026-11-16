#!/usr/bin/env python3
"""Mark the generated documents of a draft build as drafts (deployment_rs_tdwg_org.md, Section 13.1).

A draft build (draft_build.sh) generates the BDQ documents from a release under test in a local
rs.tdwg.org checkout: proposed changes that are not accepted. Their headers then cite versions that
rs.tdwg.org does not have (the release under test is not processed onto the deployed branch). This
script inserts a notice after the first top-level heading of every generated Markdown document in
tg2/_review/ and after the first <h1> of the pre-built Quick Reference Guide HTML, saying that the
document is a draft, not issued, and that the versions dated on the release under test are proposed.

Usage (from tg2/_make_review):
    python3 mark_draft.py --release-date YYYY-MM-DD --source "<rs.tdwg.org checkout and commit>"

Idempotent: a document that already has the notice is not changed.
"""

import argparse
import pathlib
import re
import sys

REVIEW = pathlib.Path(__file__).resolve().parent.parent / '_review'
MARK = '<!-- bdq-draft-notice -->'


def notice(release_date, source):
    return (f'{MARK}\n> **DRAFT, NOT ISSUED.** This document was built from proposed changes to the BDQ '
            f'standard that have not been accepted (rs.tdwg.org release {release_date} under test, '
            f'{source}). Versions dated {release_date} that it cites are proposed: they are not issued and '
            f'are not served by rs.tdwg.org. Do not cite this document.\n')


def mark_markdown(path, text_notice):
    text = path.read_text(encoding='utf-8')
    if MARK in text:
        return False
    match = re.search(r'^# .*\n', text, re.M)
    if not match:
        return False
    text = text[:match.end()] + '\n' + text_notice + '\n' + text[match.end():]
    path.write_text(text, encoding='utf-8')
    return True


def mark_html(path, text_notice):
    text = path.read_text(encoding='utf-8')
    if MARK in text:
        return False
    match = re.search(r'<h1 id="[^"]*">[^<]*</h1>\n?', text)
    if not match:
        return False
    body = text_notice.split('\n', 1)[1].lstrip('> ').strip()
    body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', body)
    html = f'{MARK}\n<blockquote><p>{body}</p></blockquote>\n'
    path.write_text(text[:match.end()] + html + text[match.end():], encoding='utf-8')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--release-date', required=True, help='date of the release under test, YYYY-MM-DD')
    parser.add_argument('--source', required=True, help='the rs.tdwg.org checkout and commit built from')
    args = parser.parse_args()
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', args.release_date):
        parser.error('--release-date must be YYYY-MM-DD')
    text_notice = notice(args.release_date, args.source)
    marked = [p for p in sorted(REVIEW.rglob('*.md')) if p.name != 'README.md' and mark_markdown(p, text_notice)]
    qrg = REVIEW / 'docs' / 'terms' / 'bdqtest' / 'index.html'
    if qrg.exists() and mark_html(qrg, text_notice):
        marked.append(qrg)
    print(f'Marked {len(marked)} documents as drafts')
    return 0


if __name__ == '__main__':
    sys.exit(main())
