# Session and Interaction History

## Purpose
`sessions.md` is readable developer context, **newest first**. It is not a substitute for a full transcript backup, and it must not become a cloud repository of patient data.

## Today
Manual/reviewed logging is enabled via `scripts/log_session.py`. After each build or maintenance interaction, prepend a concise entry. Hermes has its own session history inside the profile; a profile export backs that up separately.

Example:
```bash
cd ~/Projects/Lifeline-Offline-First-Aid
python3 scripts/log_session.py --summary "Validated Qwen cold start offline" --decision "Keep native model" --next "Add source retrieval tests"
```

The script prepends entries directly under `<!-- ENTRIES START -->`. You can add details manually, but always place newest first.

## Full automatic coverage (future work)
User requested context from every interaction. That requires a verified Hermes Desktop/profile post-turn hook or session-export API; this starter project does NOT claim that such logging is active. Before implementing, validate a supported Hermes integration and decide where sensitive emergency transcripts are kept. Suggested architecture: sanitized build summaries in `sessions.md`; encrypted local-only transcript store with retention/consent controls; never sync identifiable medical content to Git.

## Privacy rules
Do not record patient names, dates of birth, exact symptoms connected to an identifiable person, addresses, medication lists, protected health data, or keys in this Git-synced file.
