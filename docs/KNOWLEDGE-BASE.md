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
| **U.S. Army ATP 4-02.11** (23 Mar 2026; supersedes TC 4-02.1) | **Local copy present; AI use LIKELY** | Cover confirmed 2026-11-07: "Approved for public release, distribution is unlimited." No third-party copyright notices in extracted text. Written for soldiers: use Tier 1 / lay content only, never Tier 2 or invasive steps (e.g., needle decompression). Direct link in `sources.csv`. |
| Other military / government first-aid manuals | Candidate | Often public domain; confirm distribution statement and edition currency. |
| CDC stroke / seizure / head-injury / heart-attack pages | Candidate | Needed for scenarios ATP 4-02.11 doesn't cover. CDC blocks automated download; save via browser. |

## Coverage of the 10 test scenarios (as of 2026-11-07, from tables of contents and text search, not yet human-reviewed)
| Scenario | Source on hand | Where | Gap / caution |
|---|---|---|---|
| Adult unresponsive / CPR | AHA lay algorithm; ATP 4-02.11 | ATP paras 6-44 to 6-49 | ATP is combat-oriented; defer to AHA for civilian sequence once AI rights are known |
| Adult choking | ATP 4-02.11 | Ch. 5, figs 5-11 to 5-20 | Fig. 5-17 caption says chest thrust depth 1.5-2 in; reviewer to reconcile with current guidance |
| Severe bleeding | ATP 4-02.11 | Ch. 4 (Tier 1 tourniquet, packing, pressure) | Tier 1 only |
| Shock | ATP 4-02.11 | Ch. 7 | |
| Burns | ATP 4-02.11 | Ch. 12 | |
| Head injury | ATP 4-02.11 | Ch. 11 | Add CDC danger-signs page for civilian follow-up |
| Anaphylaxis | ATP 4-02.11 | Paras 7-30 to 7-35 | Epinephrine auto-injector use: check wording is lay-appropriate |
| Stroke | none | ATP covers heat stroke only | **Gap**: CDC F.A.S.T. page |
| Seizure | none | ATP mentions seizures only as a head-injury sign | **Gap**: CDC seizure first-aid page |
| Heart attack | none | not covered | **Gap**: CDC heart-attack page |
| Child / infant | partial | ATP CPR section gives brief child/infant notes only | **Gap**: no dedicated pediatric source |

Also in ATP 4-02.11 (possible later scenarios): fractures/splinting (Ch. 13), bites and stings (Ch. 16), heat and cold injuries (Ch. 17), eye trauma (Ch. 10), psychological first aid (Ch. 20).

## Next actions
- Decide the v1 topic list (the 10 scenarios in `docs/OFFLINE-TESTS.md`).
- For each topic, pick one primary source that passes the gate; prefer public-domain government sources for AI indexing.
- Record every file in `references/sources.csv` with `shasum -a 256 <file>`.
- Documents are never committed; each user downloads them (`references/README.md`, `python3 scripts/references.py`).
