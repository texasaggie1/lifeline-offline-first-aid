# LIFELINE Development Sessions

Newest entry first. Each new entry is **prepended** directly below the marker (use `python3 scripts/log_session.py`). This file records build and maintenance work and decisions — never patient-identifiable emergency chats. No automatic per-chat recorder exists yet (see `docs/SESSION-LOGGING.md`).

Entries dated 2026-11-07 before the Claude Code entry are a reconstruction of the ChatGPT conversation (merged from `sessions.md` and the ChatGPT handoff file now in `docs/archive/`). Times are approximate.

<!-- ENTRIES START -->

## 2026-11-07 19:40 -0600 | CDC stroke, seizure, heart-attack pages saved
- **Summary:** ATP 4-02.11 recorded and pushed (1b64d7f, remote verified). Opened three CDC pages in the browser pane (stroke signs, May 19 2026; first aid for seizures, May 15 2024; heart attack, Oct 24 2024), saved their main text as markdown captures in git-ignored references/raw/ with source headers, added sources.csv rows with sha256; references.py reports all 5 files OK. Coverage map updated: stroke, seizure, heart-attack gaps filled (heart attack source is recognition + call 911 only). CDC head-injury page not captured (ATP Ch. 11 covers it). Child/infant still a gap. Not reviewed.
- **Decision:** Web pages are stored as dated text captures; their hashes are maintainer-specific, users compare page dates.
- **Next:** User back at Mac: verify the bot in a new Hermes chat (local model, small prompt), cut context to 16-32K, then plan retrieval.

## 2026-11-07 14:32 -0600 | Army ATP 4-02.11 downloaded and mapped
- **Summary:** Committed+pushed reference guide (fe3737d, remote SHA verified). With user permission downloaded ATP 4-02.11 (12,665,561 bytes, 254-page PDF, sha256 a4a0650f...) from armypubs.army.mil into git-ignored references/raw/. Extracted text locally with PDFKit (pdftoppm not installed). Confirmed cover: 23 March 2026, Approved for public release, distribution unlimited, supersedes TC 4-02.1. No third-party copyright notices found. Coverage: CPR, choking, bleeding, shock, burns, head injury, anaphylaxis yes; stroke (heat stroke only), seizure, heart attack no; child/infant only brief notes. Added to sources.csv with download_url (references.py verifies both files OK) and a scenario coverage map in KNOWLEDGE-BASE.md. Not reviewed by a human. Herbal/edible-plant scope: user unsure, nothing added.
- **Decision:** ATP 4-02.11 is the primary public-domain source for trauma/airway scenarios, Tier 1 (lay) content only.
- **Next:** Save CDC stroke, seizure, heart-attack, head-injury pages via browser; find a pediatric source; decide herbal/plant scope; then design retrieval.

## 2026-11-07 14:19 -0600 | Reference library: user download guide + checker
- **Summary:** Reference documents stay out of Git (copyright), so each user must fetch them. Rewrote references/README.md as a step-by-step guide; added scripts/references.py (status: OK/MISSING/MISMATCH/UNPINNED per sources.csv row; fetch: downloads rows with a direct download_url and refuses files whose sha256 does not match); added download_url column to sources.csv (blank for the AHA file, which is manual). Tested: present file -> OK exit 0; file moved away -> MISSING exit 1 and fetch -> MANUAL; file restored. Linked from README quick start and RECOVERY step 7; refreshed stale README status line. User raised adding herbal/edible-plant content; not added, decision pending. Army ATP 4-02.11 download still awaiting user permission; nothing downloaded.
- **Decision:** No reference files in the repo ever; manifest + checksum script is how users rebuild the library.
- **Next:** User decision on ATP 4-02.11 download and on herbal/edible-plant scope; fill download_url/sha256 for each approved public-domain source.

## 2026-11-07 12:35 -0600 | Bot lockdown: local model, tools cut, SOUL deployed
- **Summary:** With user approval: copied entire LIFELINE profile to ~/.hermes/backups/lifeline-profile-20261107-1234 (diff identical). Edited ~/.hermes/profiles/lifeline/config.yaml via exact-match replacement: model -> llamacpp Qwen3.5-9B-Q4_K_M @ 127.0.0.1:18434 (same format as Hermes' own default profile config); CLI toolsets 14 -> [clarify]. Deployed agent/SOUL.md to profile SOUL.md (cmp identical). Hermes Desktop was running; config not reverted after edit. No YAML parser available to validate; structure checked by eye.
- **Decision:** Lockdown applied by file edit; context-size reduction left for Hermes UI because the llamacpp preset is shared and Hermes-generated.
- **Next:** On the Mac: restart Hermes or open a NEW LIFELINE chat; confirm model picker shows Qwen3.5 9B; ask a test question; Claude reads logs to confirm local provider and smaller prompt (was ~12K tokens). Reduce context to 16-32K in Hermes model settings. To undo: restore backup folder.

## 2026-11-07 12:17 -0600 | Idle unload observed; bot model check
- **Summary:** User reports bot connected to unsloth Qwen3.5-9B-GGUF, ~15-20 s first load, quick replies. Verified: recent LIFELINE chats ran Qwen3.5-9B-Q4_K_M via local llamacpp (per-session selection; latencies 4-5 s at 12:09). Idle unload observed: model process exited within ~8 min of last use, memory free 77%. Still true: profile config.yaml default = cloud gpt-6.1-sol and 14 toolsets enabled (incl. web, delegation, memory) - affects new chats and prompt size (~12K tokens).
- **Decision:** Stay on Qwen3.5 9B (5.3 GB file). Do not fine-tune; teach via SOUL + vetted local references + graded tests. Compare a Gemma-class model later using the same test set.
- **Next:** Lock down bot in Hermes UI (default model, tools, SOUL, smaller context); then propose public-domain source list for the 10 test scenarios.

## 2026-11-07 12:14 -0600 | First push to public GitHub - verified
- **Summary:** Token-over-HTTPS push failed twice for the user (password prompt). Installed official GitHub CLI v2.103.3 to ~/.local/bin/gh (sha256 matched release checksums; signed by GitHub Developer ID). First interactive gh login stalled at a Y/n prompt the user could not answer in the terminal tab; reran non-interactively, user authorized via github.com/login/device; logged in as texasaggie1 (keyring). gh auth setup-git configured. git push -u origin main succeeded. VERIFIED: GitHub main SHA = local 755c36bfcb48c63c725fdc853190b833e2e05918, repo PUBLIC, 23 files, commit author email = noreply.
- **Decision:** Use gh CLI browser login for all future pushes; no passwords or tokens typed in terminal.
- **Next:** Back up LIFELINE Hermes profile, then set Qwen3.5 9B as profile default, trim toolsets to shrink the 11.7K-token prompt, reduce ctx to 16-32K, re-measure first reply; then idle-unload and offline cold-start tests.

## 2026-11-07 12:08 -0600 | Prepared repo for public sharing
- **Summary:** User created GitHub repo texasaggie1/lifeline-offline-first-aid as PUBLIC (verified: repo page returns HTTP 200 unauthenticated). First push attempt failed because an account password was used instead of a token; nothing pushed yet. Before first push: added README medical disclaimer and MIT LICENSE; removed personal details (home paths, other agent name) from all tracked files; rewrote commit authorship to GitHub noreply email; squashed local history into a single commit so no earlier version with personal info is published; check.sh now scans tracked files against a local git-ignored .personal-patterns list and blocks any non-noreply commit email. Full-history scan: no personal-pattern hits, only text files (largest 9 KB), no PDFs/weights/secrets.
- **Decision:** Repo is PUBLIC so the project can be shared. All docs updated from private to public. Commits must use texasaggie1@users.noreply.github.com.
- **Next:** User: create fine-grained token (Contents read/write, this repo only), run git push -u origin main, then Claude verifies the SHA on GitHub. Then: back up LIFELINE profile, set Qwen3.5 9B as default, trim toolsets, re-measure first reply.

## 2026-11-07 12:00 -0600 | Qwen3.5 9B first test recorded
- **Summary:** User reported unsloth Qwen3.5-9B-GGUF loads in ~20 s and replies almost instantly. Verified from Hermes logs: LIFELINE chat at 11:55 used Qwen3.5-9B-Q4_K_M (provider=custom, per-session); model load ~6 s; first reply ~31 s (llama) / 37 s (agent), dominated by 11,713-token system prompt at 440 tok/s; generation 20-22 tok/s; follow-up 8.9 s for 168 tokens with 99% prompt cache. llama-server RSS 9.6 GB at 262K ctx; system memory 36% free. 27B logs for comparison: ~3.5 tok/s gen, ~3 tok/s prompt. LIFELINE profile config.yaml default is STILL cloud gpt-6.1-sol; global default profile now Qwen3.5-9B. GitHub push still pending (no credentials on Mac; GitHub plugin failed to connect).
- **Decision:** Qwen3.5 9B Q4_K_M is the lead candidate. Not accepted until offline cold start + first-aid accuracy tests pass.
- **Next:** Set 9B as LIFELINE profile default (after profile backup); disable unneeded toolsets to shrink 11.7K-token prompt; consider ctx 16-32K; re-measure first reply; test idle unload; then offline cold-start test. GitHub: create empty private repo + one-time token push.

## 2026-11-07 11:53 -0600 | Claude Code takeover: audit, reorganize, git init
- **Summary:** Audited project and live Hermes install (read-only). Found: no .gitignore despite docs claiming one; AHA PDF in untracked top-level Medical-References/ (moved to git-ignored references/raw/, added to sources.csv with sha256, AI rights UNKNOWN); two conflicting doc sets from ChatGPT (newer handoff files cited 8 files that never existed) - merged into canonical CLAUDE.md + sessions.md, originals archived in docs/archive/. VERIFIED live LIFELINE profile config.yaml uses CLOUD provider openai-codex / gpt-6.1-sol with web, x_search, delegation, memory, image/video gen toolsets ON - violates mission; not changed (needs user approval + backup). VERIFIED Qwen3.5-9B-Q4_K_M.gguf (5.3 GB) is downloaded, sha256 03b74727...b7e8, not yet benchmarked. VERIFIED Mac stable (rebooted ~10:05, 88% mem free). Added docs/KNOWLEDGE-BASE.md, hardened scripts/check.sh (blocks PDFs/weights/.env/auth.json/archives/>5MB/token strings; tested: blocks staged PDF), added --title to log_session.py, fixed repo name/path across docs. git init on main. gh CLI not installed, no SSH keys: GitHub push NOT done.
- **Decision:** Keep project at ~/Projects/Lifeline-Offline-First-Aid (only copy). Repo texasaggie1/lifeline-offline-first-aid, private. ChatGPT handoff files archived, not deleted.
- **Next:** User creates empty private repo on github.com, then: git remote add origin https://github.com/texasaggie1/lifeline-offline-first-aid.git && git push -u origin main; record SHA. Then: back up profile + switch LIFELINE bot to local Qwen3.5 9B and strip toolsets to clarify (+ read-only file if enforceable); deploy agent/SOUL.md; benchmark 9B per CLAUDE.md section 7.

## 2026-11-07 | Full portable handoff and private GitHub request (ChatGPT)
- **Goal:** Build a detailed, small-AI-readable handoff so another machine or model can resume work, synced to PRIVATE `texasaggie1/lifeline-offline-first-aid`.
- **Done:** ChatGPT generated the handoff files in its own sandbox. Only three of them reached this Mac (`LIFELINE_START_HERE.md`, `LIFELINE_CLAUDE_FULL.md`, `LIFELINE_SESSIONS_FULL.md`). The files they cite (`CHECKPOINT.md`, `START-HERE.md`, `docs/PERFORMANCE-INCIDENT.md`, `docs/KNOWLEDGE-BASE.md`, `docs/INSTALL-HERMES.md`, `tests/scenarios.csv`, `scripts/check.py`, `.gitignore`) never arrived. GitHub repo lookup returned 404; ChatGPT could not create repos.
- **Critical finding (reported, not re-verified):** ACS STOP THE BLEED terms prohibit AI use without written permission. Red Cross manuals have restrictive reproduction terms.
- **Next:** Create or confirm the private repo, install the handoff into the project, scan it, push and verify. Preserve an encrypted Hermes profile export and an offline backup of the model and references.

## 2026-11-07 | MODEL PERFORMANCE FAILURE; MAC SYSTEM IMPACT (ChatGPT)
- **Observed by user:** On the 32 GB MacBook Pro, Hermes native Qwen3.8 27B appeared to load in ~10 s. The first `READY` request sat over a minute at 20% prompt processing, later reached ~97%, and did not finish promptly. Thinking ON/Medium and OFF were both slow. The first meaningful response took ~15 minutes; later prompts took ~15 s to start and streamed one word at a time.
- **System issue:** The Mac barely worked and fans ran at full speed. It did not recover after force-quitting Hermes.
- **Cause:** Not proven (compute, long prefill, KV cache memory, swapping or a runtime issue).
- **Decision:** Do NOT reload 27B on this Mac. Try a much smaller model once the Mac is stable. First candidate: Qwen3.5 9B Q4_K_M.

## 2026-11-07 | Hermes local inference model selection (ChatGPT)
- The Local Models UI showed Qwen3.8 27B at ~17.3 GB, "all on GPU", 144K context. That label does not prove responsiveness.
- Qwen3.5 9B was not in the curated catalog; "Find more models" (Hugging Face) was suggested.
- Ollama `gemma4:latest` (9.5 GB) failed to route through Hermes (`provider 'auto' has no endpoint configured`). Native Hermes llama.cpp is preferred. No Honcho.

## 2026-11-07 | Repo naming and source folder (ChatGPT)
- **User choice:** GitHub account `texasaggie1`, repo `lifeline-offline-first-aid`, PRIVATE. Project lives under `~/Projects`.
- GitHub stores project files only. It cannot restore the Hermes install, GGUF weights, licensed PDFs, the bot profile or credentials, so those need a separate backup.

## 2026-11-07 | LIFELINE Bot created and scope set (ChatGPT)
- User created the LIFELINE bot in Hermes Desktop. Name `LIFELINE`, title `First-Aid Assistant`, description `Offline Emergency First-Aid Assistant`, with a short custom SOUL.
- Target tools were File Operations and Clarifying Questions only. Final toggle state was not audited. File Operations bundles read, write, patch and search.
- Architecture: standalone local reference assistant on this Mac with no cloud and no daily memory service. Honcho and Ollama (used by an unrelated agent on another machine) are not part of LIFELINE.

## 2026-11-07 | Initial setup and model-connection investigation (ChatGPT)
- Hermes Desktop installed. The Ollama custom endpoint failed: `provider 'auto' has no endpoint configured`.
- The native Local Models UI showed llama.cpp b11671 / Metal and 32 GB unified memory. Decision: use the native engine.

## 2026-11-07 | Mission definition (ChatGPT)
- User wants an offline first-aid assistant in Hermes Desktop for prolonged network or infrastructure outages. It runs only on this Mac at first and loads on demand rather than always occupying memory.
- Architecture: curated local official references, checked retrieval and an independently readable manual. No fine-tuned medical LLM.
