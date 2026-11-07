# GitHub Sync (public repo)

GitHub is a versioned *source backup*. It does not replace encrypted backups of the Hermes profile, the model or the references.

**Repo:** `https://github.com/texasaggie1/lifeline-offline-first-aid` (**PUBLIC** — treat every commit as published to the world)
**Local:** `~/Projects/Lifeline-Offline-First-Aid`

## How pushing works on this Mac (set up 2026-11-07)
- GitHub CLI `gh` v2.103.3 (official release, checksum verified) installed at `~/.local/bin/gh`.
- Logged in via browser device flow: `gh auth login --hostname github.com --git-protocol https --web`. Run it so it can't stop at an interactive prompt (e.g. `< /dev/null`), then open https://github.com/login/device and enter the one-time code it prints. The token lives in the macOS Keychain.
- `gh auth setup-git` makes Git use that login, so `git push` needs no username, password or token.
- Check with: `~/.local/bin/gh auth status`. Revoke at GitHub → Settings → Applications → Authorized OAuth Apps → GitHub CLI.

## On a new Mac
Install `gh` (https://cli.github.com), run the login above and `gh auth setup-git`, then `git clone https://github.com/texasaggie1/lifeline-offline-first-aid.git ~/Projects/Lifeline-Offline-First-Aid`. Recreate your local `.personal-patterns` file (git-ignored) before committing.

## After each build session
1. `python3 scripts/log_session.py --title "..." --summary "..." --decision "..." --next "..."`
2. Review with `git diff && git status --short`.
3. Run `bash scripts/check.sh`. It blocks PDFs, model weights, `.env`, `auth.json`, archives, files over 5 MB, token-shaped strings, personal info listed in your local `.personal-patterns` file (git-ignored; one regex per line, e.g. your email and real name), and any commit email that is not a GitHub noreply address.
4. Run `bash scripts/sync.sh "Describe the change"`. It asks you to type YES, then commits and pushes.

## Limitations
- Pushing is manual and needs the network. Offline, keep committing locally and push once you're connected again.
- `sessions.md` is not auto-updated by Hermes (see `docs/SESSION-LOGGING.md`).
- The repo is public. Never push patient info, secrets, chats, profile archives, models, licensed PDFs, or the maintainer's personal details. Commits use the GitHub noreply email (`git config user.email`). If something sensitive is ever pushed, deleting it in a later commit is NOT enough — it stays in history; rotate any secret immediately and ask for help rewriting history.
