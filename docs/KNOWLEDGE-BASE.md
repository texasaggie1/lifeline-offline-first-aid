# Medical Knowledge Base: Licensing Gate and Candidate Sources

Nothing goes into LIFELINE's retrieval index until it passes this gate **and** is recorded in `references/sources.csv`.

## The gate (all must be YES)
1. **Authoritative:** published by a recognized first-aid/resuscitation body or government health agency.
2. **Current:** edition/date known and not superseded.
3. **Rights:** terms allow (a) keeping a local copy, and (b) using it in an AI/retrieval system. These are separate questions — a free public download does NOT grant (b).
4. **Recorded:** title, issuer, URL, edition, local filename, sha256, permission notes logged.
5. **Reviewed:** a qualified human (e.g., current first-aid/CPR instructor, EMT, nurse, physician) has reviewed it for lay use and signed off with a date.

If (3b) is NO or UNKNOWN, the document may still be kept as a **human-readable fallback** in `references/raw/` and on the printed/offline kit — just not indexed for the AI.

## Candidate sources and known status
| Source | Status | Notes |
|---|---|---|
| AHA Adult BLS Algorithm for Lay Rescuers (`Algorithm-BLS-Adult-Lay-Rescuer-250514.pdf`) | Local copy present; AI rights UNKNOWN | © American Heart Association. Check AHA's copyright/permissions terms before indexing. Fine as human-readable fallback. |
| ACS STOP THE BLEED course materials | **Do not ingest** | The prior assistant (ChatGPT, 2026-11-07) reported ACS terms explicitly prohibit AI use without written permission. Not independently re-verified — treat as prohibited until written permission is obtained. |
| American Red Cross First Aid/CPR manuals | Do not ingest without permission | Reported restrictive reproduction terms. Human-readable copy only if obtained legitimately. |
| MedlinePlus health-topic summaries (NLM) | Candidate | U.S. government topic pages are generally public domain, but the A.D.A.M. Medical Encyclopedia and other third-party content on MedlinePlus is copyrighted. Check each page. |
| CDC / NIH / FEMA / Ready.gov public pages | Candidate | U.S. federal works are generally public domain; confirm per page, watch for third-party images/content. |
| Military / government first-aid manuals (e.g., U.S. Army field first-aid publications) | Candidate | Often public domain and approved for public release; confirm distribution statement and edition currency. |

## Next actions
- Decide the v1 topic list (the 10 scenarios in `docs/OFFLINE-TESTS.md`).
- For each topic, pick one primary source that passes the gate; prefer public-domain government sources for AI indexing.
- Record every file in `references/sources.csv` with `shasum -a 256 <file>`.
- Documents are never committed; each user downloads them (`references/README.md`, `python3 scripts/references.py`).
