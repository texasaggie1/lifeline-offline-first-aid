# Medical, Privacy and System Safety Controls

## Medical
- This project is experimental and not certified/validated for emergency medical decisions.
- Do not trust a general LLM alone. Build reviewed emergency cards and a retrieval layer over dated, authoritative, local source material.
- Use original published layperson first-aid sources from reputable organizations. Keep their original titles/editions; verify updates and permissions before reproducing or transforming text.
- Never fabricate medication doses or invasive procedures; never mix conflicting editions silently.
- Use human reviewer signoff before declaring readiness. Keep independent printed/PDF manuals.

## Runtime
- Offline means model + inference runtime + retrieval + references + interface all work with internet disabled. A local model by itself is insufficient.
- Cloud provider fallback, remote tools, browser, code execution, task delegation, A2A, cron, remote connectors and automatic updates should be off for LIFELINE.
- Native Hermes profiles isolate state but are **not OS filesystem sandboxes**. File Operations includes write/patch. Use OS sandbox/permission controls and read-only copies if strict enforcement is needed.
- Reduce context and resources to keep the everyday Mac responsive. Record cold start and idle RAM behavior rather than assuming automatic unloading.

## Privacy
- Git tracks build metadata and source instructions only. Do not commit identifiable medical incidents or histories.
- Profile exports can contain conversation content and memories, even if secrets are stripped. Keep in encrypted backup storage, not ordinary Git.
- To capture every interaction, implement a supported per-turn hook and filtering/redaction tested for the installed Hermes version. Until then logging is a deliberate post-session step, not an automatic guarantee.
