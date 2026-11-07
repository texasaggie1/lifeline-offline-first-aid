#!/usr/bin/env python3
"""Prepend a sanitized development note to sessions.md (newest first). Not an automatic chat logger."""
import argparse
from datetime import datetime
from pathlib import Path

p = argparse.ArgumentParser(description="Prepend a non-sensitive development session entry")
p.add_argument('--title', default='Development session', help='Short headline for the entry')
p.add_argument('--summary', required=True, help='What was actually done/observed; no PHI or secrets')
p.add_argument('--decision', default='None recorded')
p.add_argument('--next', default='None recorded')
p.add_argument('--date', default=None, help='Override the timestamp text')
a = p.parse_args()

path = Path(__file__).resolve().parent.parent / 'sessions.md'
source = path.read_text(encoding='utf-8')
marker = '<!-- ENTRIES START -->'
if marker not in source:
    raise SystemExit('Missing sessions.md marker; no changes made')

when = a.date or datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %z')
entry = (f'\n\n## {when} | {a.title}\n'
         f'- **Summary:** {a.summary}\n'
         f'- **Decision:** {a.decision}\n'
         f'- **Next:** {a.next}')
path.write_text(source.replace(marker, marker + entry, 1), encoding='utf-8')
print('Added newest-first session entry. Review content before any Git push.')
