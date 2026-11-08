# LIFELINE — Instructions for Claude and Other Coding Agents

**Project:** LIFELINE Offline First Aid
**Local path:** `~/Projects/Lifeline-Offline-First-Aid` (older docs mentioning `~/Projects/LIFELINE` are superseded)
**GitHub:** **PUBLIC** `texasaggie1/lifeline-offline-first-aid` (public since 2026-11-07 — anything committed is visible to everyone, forever, in history)
**Status:** NOT READY FOR REAL MEDICAL EMERGENCIES

## 0. Read first (every development or maintenance session)
1. This file, in full — especially **§2 Current status**.
2. `sessions.md` from the top (newest entry first).
3. `config/target-state.yaml` (intended settings, NOT live Hermes config).
4. `docs/SAFETY.md`, plus whichever doc the task touches (see §9).

Check that a file or setting actually exists before you say it does. If you aren't sure, write `UNKNOWN` and name the check that would settle it.

## 1. Mission
Build a portable, on-demand, 100% offline-capable Hermes Desktop bot called LIFELINE. It helps a layperson find and understand **reviewed** first-aid instructions when networks or emergency services may be unavailable. LIFELINE is a reference aid: not a physician, not a diagnostic or clinical-decision system, and not a replacement for training or 911. A non-AI fallback (printed card or readable PDF) must always exist.

## 2. Current status (last verified 2026-11-07 by Claude Code, from this Mac)
Use only these labels: `DONE (verified)`, `PARTIAL`, `NOT STARTED`, `BLOCKED`, `FAILED`, `UNKNOWN`.

| Area | Status | Evidence / notes |
|---|---|---|
| Hermes Desktop installed | DONE (verified) | `/Applications/Hermes.app`; data in `~/.hermes` |
| LIFELINE bot/profile exists | DONE (verified) | `~/.hermes/profiles/lifeline/` |
| Bot uses a LOCAL model | PARTIAL | 2026-11-07 12:34: profile `config.yaml` set to `llamacpp` / `Qwen3.5-9B-Q4_K_M` @ `127.0.0.1:18434` (format copied from Hermes' own default profile). Not yet confirmed in a NEW chat or with networking off |
| Bot tools restricted | PARTIAL | 2026-11-07 12:34: CLI toolsets cut from 14 to `clarify` only. Takes effect on new chats (Hermes restart may be needed). OS-level isolation not enforced |
| Deployed SOUL matches `agent/SOUL.md` | DONE (verified) | Copied 2026-11-07 12:34; byte-identical (`cmp`) |
| Qwen3.8 27B (Q4_K_M, 15 GB) | FAILED | Downloaded. Tested 2026-11-07: ~15 min first response, Mac nearly unusable. **Do not load it again** unless the user explicitly asks for a fresh benchmark |
| Qwen3.5 9B Q4_K_M (5.3 GB, unsloth GGUF) | PARTIAL — **lead candidate** | Tested in a LIFELINE chat at 11:55 on 2026-11-07, measured from the llama-server logs. Model loads in ~6 s. The first reply took ~31–37 s, mostly spent processing an 11.7K-token system prompt bloated by enabled tools. Follow-ups start in under 1 s and stream at ~20–22 tok/s. Server RSS 9.6 GB with a 262K context. The chat chose the model per session (`provider=custom`); the profile's default is still the cloud model. Not yet: offline test, first-aid accuracy test, idle unload |
| Mac stability after the 27B incident | DONE (verified) | Rebooted ~10:05; 88% memory free at 11:50; no llama/Hermes process running |
| Hermes profile export (backup) | PARTIAL | File copy of the whole profile at `~/.hermes/backups/lifeline-profile-20261107-1234` (pre-lockdown; local only, contains credentials files). A Hermes Desktop "Export profile" to encrypted media is still NOT done |
| Medical references | PARTIAL | 5 files in `references/raw/` (2 PDFs + CDC stroke/seizure/heart-attack text captures), both sha256-verified by `scripts/references.py`: AHA Adult BLS lay algorithm (AI rights UNKNOWN) and Army ATP 4-02.11 (23 Mar 2026, "approved for public release, distribution unlimited" confirmed on cover). Neither reviewed. Coverage map: `docs/KNOWLEDGE-BASE.md` |
| Local retrieval | NOT STARTED | Not designed. A folder of PDFs is not RAG |
| Offline cold-start tests | NOT STARTED | `docs/OFFLINE-TESTS.md` |
| Medical human review | NOT STARTED | |
| Git repo + public GitHub | DONE (verified) | First push 2026-11-07: `main` @ `755c36b` matches GitHub; 23 files; PUBLIC. Push with `git push` (gh CLI login). Never write "synced" without checking the remote SHA |

## 3. Nonnegotiable rules
1. Never claim medical certification, clinical validation or safe emergency use without dated human signoff and documented tests.
2. Procedure instructions come only from current, approved, dated, locally available references. Never invent steps, drug doses, invasive procedures or diagnoses.
3. In life-threatening situations, advise calling emergency services. Never let model startup delay CPR, AED use or bleeding control.
4. Final runtime has **no** cloud provider or fallback, Honcho, remote connectors, web, browser, terminal, code execution, cron, delegation/A2A, memory sync or autonomy.
5. Keep out of Git: patient info, identifiable symptoms, contact details, credentials, `.env`, `auth.json`, chat exports, profile archives, model weights, and any PDF without confirmed redistribution rights. **Because the repo is public, also keep out the maintainer's personal details** (real name, email, home-directory paths, other projects/agents). Commits use the GitHub noreply email. `.gitignore` enforces most of this and `scripts/check.sh` checks it (including a local, untracked `.personal-patterns` list) — don't weaken either.
6. A separate profile or SOUL is **not** an OS sandbox, and File Operations includes write/patch. Don't treat isolation as enforced until it's tested.
7. Every medical source needs a row in `references/sources.csv`: title, issuer, URL, edition/date, filename, sha256, permission notes, review status, reviewer and date. **A public download does not mean AI ingestion is allowed** (see `docs/KNOWLEDGE-BASE.md`).
8. Never enable a new model or tool without an offline cold-start test.
9. **Performance guard:** Never load Qwen3.8 27B on this 32 GB Mac. When benchmarking any model, use a new session, minimal tools and Thinking OFF; make at most two attempts; stop at once if the Mac slows down.
10. Don't edit the live Hermes profile (`~/.hermes/profiles/lifeline/`) without a backup copy and the user's explicit approval. Prefer the Hermes Desktop UI.

## 4. Locked product decisions (change only if the user says so)
- Hermes Desktop is the interface (no custom app).
- Inference: Hermes native llama.cpp/Metal. No Ollama, no Honcho for v1.
- The model loads on demand, not 24/7. Hermes idle unload (reportedly ~15 min) is unverified on this install.
- Use small, fast models first; measure accuracy and speed rather than trusting benchmark scores.
- Knowledge comes from curated, licensed, versioned local references plus tested retrieval. No fine-tuning on uncontrolled medical corpora.

## 5. Emergency response design spec
Lead with the life threat and an emergency-services prompt. Give short numbered steps from a cited local source (title, edition, section/page). Ask one essential question at a time. If a source is missing, unclear, conflicting or not authorized, say so. Answers must work with Wi-Fi, Ethernet, Bluetooth tethering and cloud all off.

## 6. Every development session
1. Read the §0 files. State one small goal.
2. Make the smallest safe change and test it (expected vs. actual).
3. Update the §2 status table and any doc whose source of truth changed.
4. Prepend a log entry: `python3 scripts/log_session.py --title '...' --summary '...' --decision '...' --next '...'`. Record failures as well as successes. Never record unverified success.
5. Run `bash scripts/check.sh`, then review `git status` and `git diff`.
6. Commit only after the human approves. Push with `bash scripts/sync.sh "message"` (human-initiated).

**Emergency or medical interactions:** care comes first. Don't log mid-emergency, and never put patient information in Git. No per-turn Hermes logging hook exists yet (`docs/SESSION-LOGGING.md`).

## 7. Model selection protocol
Record: model ID, quantization, file size and sha256, Hermes version, macOS version, RAM pressure before and after, cold start, time to first token, 50-word answer latency, tokens/sec, fan and responsiveness, and idle unload. Accept a model only after **both** the latency test and the document-grounded first-aid tests pass. Store results in `config/target-state.yaml`.

## 8. Restore definition of done
On a new Apple Silicon Mac: repo cloned, Hermes installed, profile imported from an encrypted export, local model restored, medical library restored and searchable, external services disabled, and every test in `docs/OFFLINE-TESTS.md` passed with networking off. Steps: `docs/RECOVERY.md`.

## 9. Project layout
- `CLAUDE.md`: this file (rules and current status)
- `sessions.md`: newest-first development log (no patient data)
- `README.md`: human overview
- `agent/SOUL.md`: source-controlled persona. Not auto-deployed; paste it into the bot in Hermes
- `config/target-state.yaml`: intended settings and measured results (not live config)
- `docs/SAFETY.md`: medical, runtime and privacy controls
- `docs/KNOWLEDGE-BASE.md`: source licensing gate and candidate sources
- `docs/OFFLINE-TESTS.md`: acceptance gate
- `docs/RECOVERY.md`: rebuild after losing the Mac
- `docs/GITHUB-SYNC.md`: GitHub push steps
- `docs/SESSION-LOGGING.md`: logging design and limits
- `docs/archive/`: superseded ChatGPT handoff files (historical only; they reference files that never existed)
- `references/sources.csv`: source and permission manifest (tracked). `references/README.md`: how each user gets the documents
- `references/raw/`: local reference files (git-ignored)
- `profile-exports/`: Hermes profile exports (git-ignored except README)
- `scripts/`: `check.sh` (pre-commit guard), `log_session.py`, `sync.sh`, `references.py` (check/download the reference library)
