# LIFELINE development history (newest first)

This file is a reconstruction from conversation messages on 2026-11-07. Times are approximate or omitted. Each NEW DEVELOPMENT entry MUST be prepended below this heading. This is not a log of personal medical emergencies or private patient conversations.

<!-- ENTRIES START -->

## 2026-11-07 | Full portable handoff and private GitHub request
- USER GOAL: Finish a detailed, simple-AI-readable project so another machine/model can resume work. Put instructions, first-aid source plans, recovery and logging in `~/Projects/LIFELINE`, synced to PRIVATE `texasaggie1/lifeline-offline-first-aid`.
- VERIFIED IN ASSISTANT ENVIRONMENT: Package files created for transfer; connected GitHub account was identified as texasaggie1. Earlier direct GitHub lookup for exact repository returned 404, and the connected GitHub file API did not expose repository creation. The assistant's filesystem is NOT the user's Mac filesystem.
- RESTRICTION: Do not say GitHub is synchronized until a private repo and commit SHA are confirmed.
- CRITICAL: Strict medical-content copyright review found ACS STOP THE BLEED material explicitly prohibits use in AI systems without written permission. Red Cross manual has restrictive reproduction rights. Source manifest and review workflow required.
- NEXT: Once Mac stable, create/confirm private repo, install handoff package into correct project directory, scan contents, push and verify. Preserve an encrypted Hermes profile export and model/reference offline backup.

## 2026-11-07 | MODEL PERFORMANCE FAILURE; MAC SYSTEM IMPACT
- USER OBSERVED: On 32 GB MacBook Pro, Hermes native Qwen3.8 27B loaded visually in ~10 seconds but the first `READY` request spent over a minute at 20% prompt processing, later reached ~97%, and did not complete promptly. Thinking ON/Medium, then OFF, both slow. User says first meaningful load took about 15 minutes; subsequent prompts took ~15 seconds to begin and streamed one word at a time.
- SYSTEM ISSUE: User reported Mac barely worked, fans full speed, and explicitly corrected that it was NOT recovered after force-quitting Hermes. NO later confirmation of stable recovery.
- INFERENCE: May involve model compute, long prefill, model/KV cache memory, swapping, background process, or other runtime issue. Exact cause was NOT proven. Never assume merely switching reasoning mode fixes it.
- DECISION: Do NOT reload 27B on this Mac. Try a significantly smaller local model only after system stability is restored. First candidate Qwen3.5 9B GGUF 4-bit; not installed/tested as of conversation end.
- NEXT: Confirm reboot/recovery and inspect Activity Monitor before any heavy model use. Benchmark small model with clean session and minimal tools.

## 2026-11-07 | Hermes local inference model selection
- LIFELINE native Local Models UI showed Qwen3.8 27B at about 17.3 GB, marked on-GPU. Later screenshot showed model installed and status `144K - all on GPU`, but this label does NOT prove responsiveness or RAM health.
- User asked for Qwen3.5 9B; it was not present in curated five-model catalog. `Find more models` Hugging Face search suggested. No subsequent download confirmed.
- Ollama listed `gemma4:latest` (9.5 GB), but attempts using Hermes custom provider `auto` failed to route. Native Hermes llama.cpp preferred for LIFELINE. No Honcho required.

## 2026-11-07 | Repo naming and source folder
- USER CHOICE: GitHub account `texasaggie1`, repository `lifeline-offline-first-aid`, PRIVATE.
- USER PREFERENCE: project under Projects. Finder screenshots showed `~/Projects/Lifeline-Offline-First-Aid`; also requested `~/Projects/LIFELINE` by name later.
- CAUTION: both directories may exist. Inspect/merge safely; do not delete either or overwrite unseen files automatically.
- IMPORTANT: A GitHub repo stores project files but cannot automatically restore Hermes Desktop installation, local GGUF weights, licensed PDFs, actual Bot profile or credentials. Separate backup required.

## 2026-11-07 | LIFELINE Bot created and scope set
- User confirmed LIFELINE Bot created in Hermes Desktop. Name `LIFELINE`, title `First-Aid Assistant`, description `Offline Emergency First-Aid Assistant`.
- Early custom SOUL text pasted in Bot; source-controlled `agent/SOUL.md` is expanded, NOT automatically applied.
- Chosen initial architecture: standalone local emergency-reference assistant on this Mac, not a cloud-based service, no daily memory service. Honcho/Ollama from an unrelated agent are not part of LIFELINE v1.
- CAPABILITIES: UI displayed tools for File Operations, Clarifying Questions, Browser, Code, Terminal, Web, Memory, voice, etc. Recommended restricted tools. Final toggle state not independently audited, and File Operations contains read/write/patch/search together.
- References and clinical review not complete.

## 2026-11-07 | Initial setup and model-connection investigation
- Hermes Desktop installed. Initial Ollama `gemma4:latest` custom endpoint was selectable but existing chat returned misleading API-key error. Detailed error: `provider 'auto' has no endpoint configured`, so provider routing failed.
- Desktop native Local Models UI showed installed llama.cpp runtime build b11671 / Metal, 32 GB unified memory. Decided to use native model engine instead of Ollama for LIFELINE.

## 2026-11-07 | Mission definition
- User desires an offline first-aid assistant in Hermes Desktop for prolonged network/world outage, initially ONLY on this Mac, available on demand without continuously occupying unified memory.
- Proposed knowledge architecture: curated locally downloaded official references + checked retrieval + independently readable first-aid manual, rather than trying to fine-tune a whole medical LLM.
- An unrelated Hermes agent on another machine uses Honcho + Ollama; LIFELINE should remain simpler and self-contained.
