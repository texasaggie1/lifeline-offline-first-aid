# LIFELINE

> [!CAUTION]
> **Experimental. Not for real emergencies. Not medical advice.**
> LIFELINE is an unfinished hobby project. It has not been clinically validated, reviewed by medical professionals, or tested for emergency use. AI models can produce wrong or dangerous answers. **In an emergency, call your local emergency number (911 in the US) and follow the instructions of trained responders.** Take a certified first-aid/CPR course and keep a printed first-aid guide. The authors accept no liability for any use of this project (see `LICENSE`).

An offline-first emergency first-aid reference assistant running in Hermes Desktop on an Apple Silicon Mac. This repository is the **rebuild source of truth**, not the live Hermes profile and not a certified medical product.

> STATUS (2026-11-07): NOT READY FOR EMERGENCY USE. Hermes Desktop + LIFELINE bot exist, but the bot is currently pointed at a **cloud** model with web/memory tools on. The 27B local model failed (too slow); a 9B model (Qwen3.5 9B) passed a first speed test but is not yet configured as default or accuracy-tested. No reviewed references, retrieval, or offline tests yet. Live status table: `CLAUDE.md` §2.

## Goals
- Runs locally with no cloud connection when deployed.
- Loads the language model only when needed; no Honcho or Ollama dependency for LIFELINE.
- Uses only reviewed, dated local reference materials for procedural instructions.
- Replies with brief, actionable instructions and identifies when to call emergency services.
- Can be rebuilt after loss of the computer.

## What is backed up where?
1. **This public GitHub repo:** plans, instructions, SOUL template, non-sensitive development session history, scripts, reference source inventory, test plans.
2. **A Hermes profile export:** actual profile configuration/skills/sessions. Not stored in Git by default, because it may contain private conversation history. Export in Hermes Desktop with Command-K > Export profile, then store encrypted in a separate backup location.
3. **Offline external storage:** complete approved reference PDFs, model files where redistribution/licensing permits, exported profile, and a copy of the project. GitHub cannot be relied on during a network outage.

## Quick start on an existing Mac
1. Clone this repository to `~/Projects/Lifeline-Offline-First-Aid`.
2. Review `CLAUDE.md`, `docs/RECOVERY.md`, `docs/SAFETY.md`, and `config/target-state.yaml`.
3. In Hermes Desktop, open the LIFELINE Bot and confirm it has a separate profile, restricted tools, and a local model. Do not assume the Bot inherits a safe provider.
4. Export the **actual** LIFELINE profile using Hermes Desktop and back up the export securely, separate from Git.
5. Populate `references/raw/` with approved locally usable files, document their dates/licensing in `references/sources.csv`, and test local retrieval. The repo intentionally contains no claimed official medical PDFs.
6. Follow `docs/OFFLINE-TESTS.md` before declaring anything ready.
7. Keep `sessions.md` newest-first. Use `python3 scripts/log_session.py --summary '...' --decision '...' --next '...'` after a development interaction.

## GitHub
This repository is **public**. Read `docs/GITHUB-SYNC.md`. Model files, secrets, actual profile exports, personal or medical data and licensed PDFs are never pushed by default.

## Authoritative software documentation
- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes profile exports: https://hermes-agent.nousresearch.com/docs/reference/profile-commands
- Hermes desktop: https://hermes-agent.nousresearch.com/docs/user-guide/desktop

## Medical safety
LIFELINE is a support reference, not a replacement for training, emergency services or professional care. Keep independent printed/phone-readable first-aid instructions.

## License
Code and documentation in this repository: MIT (see `LICENSE`). Third-party medical references are **not** included and remain under their publishers' terms.
