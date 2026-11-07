# Rebuild LIFELINE After Losing the Mac

## Before a loss: create three backups
1. **GitHub**: public `texasaggie1/lifeline-offline-first-aid` repo containing these project docs/scripts. Run Git sync manually after development changes.
2. **Hermes profile export**: in Hermes Desktop use Command-K > `Export profile...` (or profile context menu), select LIFELINE, save archive to an encrypted backup drive. This preserves persona, sessions, memory, and settings but excludes credentials. Keep it **out of GitHub** by default. Do not assume CLI is installed just because Desktop runs.
3. **External offline drive**: copy the entire project tree, approved PDFs from `references/raw/`, and locally downloaded model data (find actual location from the installed Hermes version), plus the Hermes installer if license permits. Check restore permissions and test readability. Keep a printed quick-reference guide too.

Optional: Hermes machine-wide `hermes backup` is different from profile export and can contain credentials. Only use if needed and store encrypted. It excludes models/runtimes; don't treat it as an offline model backup.

## On a replacement Mac, when internet is available
1. Install Hermes Desktop from its official distribution and verify it runs.
2. Install Git or use built-in Git and authenticate to the maintainer GitHub account if you need to push (cloning a public repo needs no login).
3. Run `git clone git@github.com:texasaggie1/lifeline-offline-first-aid.git ~/Projects/Lifeline-Offline-First-Aid` (substitute actual repository owner; an HTTPS URL also works).
4. Open `CLAUDE.md` and `sessions.md`; follow `config/target-state.yaml` as a target, not an automatic deployment config.
5. In Hermes Desktop use Import profile... to import the previously saved LIFELINE profile archive. Verify it appears under its own identity; the exact name may differ, record it.
6. Reinstall/download the exact local model and quantization documented in `config/target-state.yaml` (or restore model bytes from offline drive). Confirm Metal acceleration, model selection, and no cloud provider fallback.
7. Restore permitted medical reference files into `~/Projects/Lifeline-Offline-First-Aid/references/raw/`. Validate filenames, versions, and checksums in `references/sources.csv`.
8. Reattach the local reference lookup skill/retrieval and test that responses cite actual local sources. A folder full of PDFs alone is not functional retrieval.
9. Inspect LIFELINE's Capabilities settings. Leave unrelated network, browser, terminal, code, automation and remote connectors disabled.
10. Execute `docs/OFFLINE-TESTS.md` disconnected and record PASS/FAIL results in `sessions.md`.

## If the network is already down
- Do not assume you can fetch GitHub, Hermes installer, Qwen model, new PDFs, or dependency packages.
- Use the prepositioned external offline drive. A fully restorable offline kit has to include every binary/component needed, with licenses observed.
- If AI is unavailable, open the readable medical manuals directly. Do not invent first-aid procedures from memory.

## What cannot be recreated by Git alone
Downloaded GGUF/model weights; installed Hermes app/runtime; unpublished profile changes; API credentials; content not yet committed; private or licensed PDF files ignored by Git; OS-level permission settings; local voice models; any external packages not mirrored to offline storage.

## Recovery acceptance criteria
The imported Bot starts without a network; local model gives a response after a cold boot; reference retrieval returns a dated local source; no hidden cloud fallback; system prompt/persona matches source-controlled `agent/SOUL.md`; behavior and 10-case medical response evaluation are reviewed by a qualified first-aid professional. Mark status in `sessions.md`.
