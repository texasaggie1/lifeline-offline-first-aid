#!/usr/bin/env python3
"""Check (and optionally download) the local reference library listed in references/sources.csv.

The reference files themselves are NOT in Git (copyright, size). Each person who clones the repo
gets them from the official publisher. This script tells you what is missing and verifies what you have.

  python3 scripts/references.py           # status of every source (default)
  python3 scripts/references.py fetch     # download sources that have a direct download_url, verify sha256

Exit code 0 = every listed file present and matching; 1 = something missing or mismatched.
Downloading needs internet. Nothing here makes a document safe to use: see docs/KNOWLEDGE-BASE.md.
"""
import csv
import hashlib
import os
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'references' / 'sources.csv'


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def rows():
    with open(MANIFEST, newline='', encoding='utf-8') as f:
        return [r for r in csv.DictReader(f) if (r.get('local_filename') or '').strip()]


def check(row):
    """Return (state, detail). state is OK, MISSING, MISMATCH or UNPINNED."""
    path = ROOT / row['local_filename'].strip()
    expected = (row.get('sha256') or '').strip().lower()
    if not path.is_file():
        return 'MISSING', str(row['local_filename'])
    actual = sha256(path)
    if not expected:
        return 'UNPINNED', 'present; no sha256 recorded yet: ' + actual
    if actual != expected:
        return 'MISMATCH', 'expected ' + expected[:12] + '..., got ' + actual[:12] + '... (new edition or different capture?)'
    return 'OK', ''


def fetch(row):
    url = (row.get('download_url') or '').strip()
    dest = ROOT / row['local_filename'].strip()
    if not url:
        return 'MANUAL', 'no direct download; get it from ' + row.get('official_url', '?')
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'lifeline-reference-fetch/1.0'})
    fd, tmp = tempfile.mkstemp(dir=str(dest.parent), suffix='.part')
    try:
        with urllib.request.urlopen(req, timeout=120) as resp, os.fdopen(fd, 'wb') as out:
            while True:
                block = resp.read(1 << 20)
                if not block:
                    break
                out.write(block)
        expected = (row.get('sha256') or '').strip().lower()
        actual = sha256(tmp)
        if expected and actual != expected:
            os.unlink(tmp)
            return 'MISMATCH', 'download did not match the recorded sha256; NOT saved (publisher may have issued a new edition)'
        os.replace(tmp, dest)
        return ('OK', 'downloaded') if expected else ('UNPINNED', 'downloaded; record sha256 ' + actual)
    except Exception as e:  # network errors, HTTP errors
        if os.path.exists(tmp):
            os.unlink(tmp)
        return 'FAILED', str(e)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if mode not in ('status', 'fetch'):
        raise SystemExit(__doc__)
    bad = 0
    for row in rows():
        if mode == 'fetch' and check(row)[0] != 'OK':
            state, detail = fetch(row)
        else:
            state, detail = check(row)
        if state != 'OK':
            bad += 1
        ai = (row.get('ai_ingestion_allowed') or 'UNKNOWN').strip()
        print('%-9s %s  [AI use: %s]' % (state, row.get('title', '?'), ai))
        if detail:
            print('          ' + detail)
        if state == 'MISSING':
            print('          get it from: ' + row.get('official_url', '?'))
    print('\n%d source(s) need attention.' % bad if bad else '\nAll listed reference files present and verified.')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
