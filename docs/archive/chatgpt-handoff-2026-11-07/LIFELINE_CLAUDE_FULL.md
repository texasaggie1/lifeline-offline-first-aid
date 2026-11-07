# CLAUDE.md - binding instructions for ANY development AI

PROJECT: LIFELINE Offline First Aid.
GITHUB: PRIVATE `texasaggie1/lifeline-offline-first-aid`.
LOCAL: `~/Projects/LIFELINE` preferred. Check for older `~/Projects/Lifeline-Offline-First-Aid` before any move.
DATE OF LAST KNOWN WORK: 2026-11-07.
STATUS: NOT READY FOR REAL MEDICAL EMERGENCIES.

These instructions are written so a small local model can follow them literally.

## 0. Read before doing anything
1. Read `START-HERE.md` fully.
2. Read `CHECKPOINT.md` fully.
3. Read `sessions.md` from TOP to BOTTOM. Newest session is at top.
4. Read `config/target-state.yaml` and relevant documentation for the task.
5. Check that any requested file or setting exists before stating success.

## 1. Mission and limits
Build a portable, on-demand, 100% offline-capable Hermes Desktop Bot called LIFELINE. Its purpose is to help a layperson find and understand reviewed first-aid instructions when normal networks or emergency services may be unavailable. Preserve immediate access to non-AI first-aid references.

This is a FIRST-AID REFERENCE AID, NOT a physician, diagnostic service, clinical decision system or replacement for training/911. Do not fine-tune on uncontrolled medical corpora. Do not claim results are medically validated without a dated human signoff and tests.

## 2. Nonnegotiable rules
- NEVER load or recommend reloading `Qwen3.8 27B` on the 32 GB MacBook unless the user explicitly authorizes a fresh benchmark after system recovery. Prior test severely degraded system usability.
- NEVER claim GitHub synced if the repo, branch and resulting commit SHA have not been verified.
- NEVER claim medical reference files are installed/retrievable when only URLs are present.
- NEVER ingest copyrighted first-aid training manuals without license and permission. ACS STOP THE BLEED v3 material explicitly prohibits uploading to AI without permission. Red Cross manual has restrictive terms. See `docs/KNOWLEDGE-BASE.md`.
- NEVER commit model weights, API keys, tokens, `.env`, profile exports, personal medical records, sensitive chat transcripts or unlicensed documents.
- NEVER silently enable a cloud model, browsing, remote connectors, cron, terminal, code execution, agent delegation, memory sync or Honcho for LIFELINE.
- NEVER claim SOUL instructions provide real file-system isolation. Tool toggles and OS rights must be validated.
- NEVER say the device is recovered if not observed. Last reported state: MAC NOT RECOVERED after heavy local inference.
- If uncertain, state `UNKNOWN` and what exact check would resolve it. Do not fill gaps with guesses.

## 3. Product decisions (locked unless user changes)
- Hermes Desktop is the interface, not a custom app.
- Hermes native managed `llama.cpp` / Metal is preferred inference; no Ollama for v1.
- Honcho is NOT required. Simple file-based build context and source-controlled instructions suffice.
- Do not run a model 24/7. Hermes docs say idle models unload after about 15 minutes, but confirm in this installation.
- Smaller model candidate: Qwen3.5 9B Q4_K_M. Alternative smaller GGUF may be tested. Accuracy and speed must be measured, not assumed.
- Use authorized, curated, versioned, searchable local medical references. Each source must have a review status and rights determination before AI ingestion.
- Have an independent PDF/printed quick reference. The AI may take time to load or may fail.

## 4. How the assistant should respond to emergencies (design spec)
- Recognize life threats. Prioritize emergency services and immediately accessible authoritative directions over conversational niceties.
- Ask only a single essential question at a time, and do not delay urgent guidance by interrogation.
- Refer to exact source title, edition/date and locally retrievable location when available.
- If source is missing, unclear, conflicting or not authorized, clearly say so; do not invent treatment, drug dosing, invasive procedures or diagnosis.
- Keep guidance short enough to use under stress. Long explanations are optional AFTER urgent actions.
- Must operate with Wi-Fi, Ethernet, Bluetooth network tethering and cloud fallback off.
- Never delay CPR/AED/bleeding control to wait for model startup when a trained bystander or offline manual is available.

## 5. Developer operating procedure (every DEV turn)
1. Read required files and check `CHECKPOINT.md`.
2. State one small goal and the prerequisite.
3. Make the smallest safe change. Protect current files and profiles from overwrite.
4. Test it, with expected vs actual results.
5. Update `CHECKPOINT.md` with verified status.
6. **Prepend** a timestamped, non-sensitive entry in `sessions.md` (use `python3 scripts/log_session.py ...`). The newest MUST be first.
7. Run `python3 scripts/check.py` and inspect `git status` / `git diff`.
8. Commit and push only after repo is confirmed PRIVATE and reviewed. See `docs/GITHUB-SYNC.md`.
9. Report what completed, what did not, and one concrete next step.

Do NOT record raw personal emergency conversations in Git. `sessions.md` covers build and maintenance interactions. If a request to log literally every medical chat arises, implement a separate encrypted, consent-aware local audit and never expose patient information to GitHub.

## 6. Model-selection test protocol
- First stabilize Mac, then test a SMALL GGUF in Hermes native runtime.
- New session, minimal toolset, Thinking OFF/Minimal.
- Record: model ID, quantization, downloaded bytes, Hermes version, macOS version, 32 GB device, RAM pressure before/after, local runtime state, cold start, first token, 50-word answer latency, measured tokens/sec, fan and responsiveness, and idle unload.
- Two attempts max per candidate. If app hangs or system slows down, STOP test immediately and restore normal operation.
- Accept only after both latency AND document-grounded first-aid test review pass. A model that replies `READY` quickly is not clinically validated.

## 7. Reference and licensing protocol
- Read `docs/KNOWLEDGE-BASE.md` and `references/sources.csv` FIRST.
- Download only sources whose terms allow the proposed use. Do not assume public download means AI ingestion is authorized.
- Public-domain MedlinePlus health TOPIC SUMMARY pages can be candidates, but MedlinePlus Encyclopedia and third-party content may be copyrighted.
- Keep human-readable original sources separately even if they cannot be ingested by an AI.
- For each added document, record title, publisher, revision, exact URL, permission, local path, hash, last checked, independent review date and status.
- Only generate emergency procedure cards AFTER source and qualified human review.

## 8. Restore protocol
- Clone PRIVATE repo; check identity and .gitignore before first push.
- Restore Hermes profile from encrypted export and local models/references from encrypted offline drive.
- Rebuild only on replacement machine after internet is available, OR use prepositioned full offline kit.
- Trust project-local skill only after examining it and confirm the Bot can see it; do NOT assume just committing SKILL.md activates it.
- Perform network-disconnected cold-start and scenario tests.

## 9. Status labels
Use exactly: `DONE (verified)`, `PARTIAL`, `NOT STARTED`, `BLOCKED`, `FAILED`, `UNKNOWN`.
Never promote a status to DONE merely because a procedure was written.

## 10. Documents by purpose
`START-HERE.md`: newcomer instructions
`CHECKPOINT.md`: immediate state
`sessions.md`: newest-first history
`agent/SOUL.md`: desired persona, not auto-synced
`docs/INSTALL-HERMES.md`: UI steps
`docs/PERFORMANCE-INCIDENT.md`: unsafe performance history
`docs/KNOWLEDGE-BASE.md`: medical source and rights
`docs/RECOVERY.md`: rebuild and verify
`docs/OFFLINE-TESTS.md`: acceptance criteria
`docs/GITHUB-SYNC.md`: private GitHub steps
`docs/SESSION-LOGGING.md`: per-turn logging design
`config/target-state.yaml`: target only
`tests/scenarios.csv`: tests not yet run
