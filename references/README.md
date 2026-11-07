# Verified Medical Reference Library

`references/raw/` is reserved for downloaded offline reference documents. It is ignored by Git to avoid copyright/license issues and unnecessary repository bloat. All references need a manifest entry in `sources.csv`.

Initial candidates:
- American Heart Association CPR/ECC official lay-rescuer algorithms: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/algorithms
- American Red Cross first aid and CPR resources: https://www.redcross.org/take-a-class/first-aid (restrictive terms; human-readable only unless permission obtained)
- American College of Surgeons STOP THE BLEED: https://www.stopthebleed.org/ (**do not ingest into AI** without written permission)

See `docs/KNOWLEDGE-BASE.md` for the licensing gate and public-domain candidates.

**Status (2026-11-07):** One file present locally (AHA adult BLS lay-rescuer algorithm); AI-use rights UNKNOWN; not reviewed or indexed. A PDF saved in a folder is not automatically available to a language model. Build and test an actual local retrieval tool before describing this as a functioning knowledge base.

For each addition, fill `sources.csv` with the document title, issuer, official URL, year/edition, saved file name, checksum, license or permitted-use basis, review status and date. Where redistribution is forbidden, keep the document on encrypted local/external media and do not commit it.
