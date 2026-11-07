# Getting the Reference Library

**This repository does not contain the medical reference documents.** Most are copyrighted, and even public-domain ones are large and change by edition. Everyone who sets up LIFELINE downloads them from the official publisher into `references/raw/` (which Git ignores).

LIFELINE is not "trained" on these files. The model stays as it is; the documents are what it looks things up in and quotes from (retrieval, not yet built), and they are also the human-readable fallback if the AI is unavailable.

## Steps (do this while you still have internet)
1. See what you need:
   ```bash
   python3 scripts/references.py
   ```
   Each line says `OK`, `MISSING`, `MISMATCH` or `UNPINNED`, and where to get missing files.
2. Download the ones that have a direct link (checked against the recorded sha256; a file that doesn't match is not saved):
   ```bash
   python3 scripts/references.py fetch
   ```
3. For lines marked `MANUAL`, open the official URL shown, download the document yourself, and save it into `references/raw/` with **exactly** the filename listed in `sources.csv`. Do not use mirrors or re-uploads.
4. Run step 1 again until every line says `OK`.
5. Copy `references/raw/` to your offline backup drive (see `docs/RECOVERY.md`). If the network is down you cannot fetch anything.

## If a file says MISMATCH
The publisher probably released a new edition. Don't just accept it: a new edition must be re-reviewed before LIFELINE relies on it. Keep the new file aside, tell the maintainer (open a GitHub issue), and they'll update the edition, sha256 and review status in `sources.csv`. For web pages saved as PDF, the hash always differs between captures; compare the page's "last reviewed" date with `edition_date` instead.

## Rules for adding a source (maintainers)
- It must pass the licensing gate in `docs/KNOWLEDGE-BASE.md`. A free download does not mean AI use is allowed.
- Add a row to `sources.csv` with title, issuer, official URL, edition/date, `local_filename` (under `references/raw/`), `sha256` (`shasum -a 256 <file>`), permission notes, `ai_ingestion_allowed`, review status, reviewer and date. Fill `download_url` only with a direct file link on the publisher's own site.
- Never commit the document itself. `scripts/check.sh` blocks PDFs and anything under `references/raw/`.

**Status (2026-11-07):** 1 source listed (AHA adult BLS lay-rescuer algorithm; AI use UNKNOWN; not reviewed). Candidate sources under research: `docs/KNOWLEDGE-BASE.md`. Nothing is indexed for the AI yet.
