# START HERE: LIFELINE handoff for a small AI

Date of handoff: 2026-11-07. Project status: NOT READY FOR EMERGENCY USE.

## You are the replacement assistant

Your job is to continue building an OFFLINE, FIRST-AID REFERENCE ASSISTANT named LIFELINE in Hermes Desktop on an Apple Silicon Mac. You are NOT being asked to deliver actual medical care. Do NOT guess at completed work.

Read files in this exact order:
1. `CHECKPOINT.md` (what is done and not done)
2. `sessions.md` (top entry is newest)
3. `CLAUDE.md` (rules for all development agents)
4. `config/target-state.yaml` (intended configuration, NOT live settings)
5. `docs/PERFORMANCE-INCIDENT.md` (IMPORTANT: damaged performance on previous Mac)
6. `docs/KNOWLEDGE-BASE.md` (source rights and medical review)
7. `docs/RECOVERY.md` (reinstall on another Mac)

## Critical facts
- Owner requested GitHub PRIVATE repo `texasaggie1/lifeline-offline-first-aid`.
- Preferred project directory: `~/Projects/LIFELINE`. An existing folder was seen at `~/Projects/Lifeline-Offline-First-Aid`. Do not overwrite/rename one over another without checking both.
- Hermes Desktop was installed. LIFELINE Bot was created, with initial SOUL/persona text.
- Hermes built-in local inference uses llama.cpp with Metal acceleration; Ollama and Honcho are NOT needed for LIFELINE v1.
- Tested model `Qwen3.8 27B` was FAR TOO SLOW on the 32 GB MacBook Pro. First response effectively took ~15 minutes; later response was very slow word by word. Mac became almost unresponsive and fans ran full speed. DO NOT REOPEN THIS MODEL until computer is stable and user explicitly agrees.
- Smaller alternative `Qwen3.5 9B Q4_K_M` was proposed but NOT confirmed installed, tested or selected.
- Original Ollama had `gemma4:latest`, but it was NOT confirmed working through Hermes Desktop for this agent.
- Native first-aid retrieval, medical-source permissions, offline cold start, and clinical validation remain UNFINISHED.
- GitHub repository creation and remote push were NOT verified as complete in this handoff. Do NOT say 'synced' unless GitHub remote and commit are verified.

## What to do NEXT (in order)
1. Protect user's computer: If the Mac is still slow, fans loud, or memory pressured, STOP. Do not load Qwen3.8 27B. Check Activity Monitor / restart normally when possible, then confirm stable.
2. Preserve source: check `~/Projects/LIFELINE` and `~/Projects/Lifeline-Offline-First-Aid` before copying. Do not overwrite existing work.
3. Confirm GitHub repository is private and exists. If missing, use `docs/GITHUB-SYNC.md` to create it with `gh` or GitHub web UI. Do NOT make a public repo.
4. Push this repo after `.gitignore` and `scripts/check.py` pass. Record remote URL and commit SHA in `sessions.md`.
5. Export actual Hermes LIFELINE profile via Hermes Desktop Command-K -> Export profile. Keep export encrypted and OFF GitHub. A project folder is not a profile backup.
6. Choose a SMALL fast local model (first candidate Qwen3.5 9B 4-bit); measure cold start, prompt processing, streaming speed, max memory and idle unloading. If not responsive, compare another small model. Do not select by benchmark score alone.
7. Audit LIFELINE Bot: source-controlled `agent/SOUL.md` must be deployed to actual Bot; no online fallback; no Honcho; no remote connectors, browser, terminal/code or cron. Local read/search only where enforceable. Settings may differ by app version.
8. Build legal, dated local first-aid reference packs. START with licensing gate. NEVER ingest ACS STOP THE BLEED materials into AI: official ACS terms explicitly prohibit AI integration without permission. See `docs/KNOWLEDGE-BASE.md`.
9. Build and test local retrieval against authorized content. Merely storing PDFs is NOT a knowledge base.
10. Complete offline and medical review acceptance tests in `docs/OFFLINE-TESTS.md` before calling LIFELINE usable.

## Every development turn
- At the end of every DEV session, prepend a factual entry to `sessions.md` using `python3 scripts/log_session.py ...`.
- Record both success and failure; never invent or silently omit failed attempts.
- DO NOT put names, personal medical incidents, passwords, transcripts, model weights or restricted PDFs in Git.
- Run `python3 scripts/check.py` before Git commit/push.
- If you cannot perform an action, say exactly why and record a specific next step. Do not pretend changes are already on the user's Mac.

## To answer the user
First: say what you actually verified. Then: give ONE concrete next action. Do not burden user with lengthy exploratory troubleshooting until stable. For emergency medical questions, tell the user to call emergency services if possible and use verified first-aid references; never wait for a slow model.
