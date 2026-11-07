# GitHub Sync (public repo)

GitHub is a versioned *source backup*. It does not replace encrypted backups of the Hermes profile, the model or the references.

**Repo:** `https://github.com/texasaggie1/lifeline-offline-first-aid` (**PUBLIC** — treat every commit as published to the world)
**Local:** `~/Projects/Lifeline-Offline-First-Aid`

## One-time setup (this Mac, as of 2026-11-07: no `gh` CLI, no SSH keys)
1. In a browser signed in as `texasaggie1`, open https://github.com/new
   - Repository name: `lifeline-offline-first-aid`
   - Visibility: **Public** (chosen 2026-11-07 so the project can be shared)
   - Do **not** add a README, .gitignore or license (the repo must be empty)
2. Make sure the local repo exists and has a commit (`git log -1`).
3. Connect and push:
   ```bash
   cd ~/Projects/Lifeline-Offline-First-Aid
   git remote add origin https://github.com/texasaggie1/lifeline-offline-first-aid.git
   git push -u origin main
   ```
   On the first push over HTTPS, Git asks for a username (`texasaggie1`) and password. The password must be a **Personal Access Token**: GitHub → Settings → Developer settings → Fine-grained tokens, scoped to this repo only with *Contents: Read and write*. macOS Keychain remembers it. Type it yourself; never paste a token into an AI chat or commit it.
4. Verify: `git log -1 --format=%H` matches the latest commit shown on the GitHub repo page, and the page shows the expected visibility. Record the SHA in `sessions.md`.

Alternative: install GitHub CLI (`gh`) from https://cli.github.com, then run `gh auth login`, followed by `gh repo create texasaggie1/lifeline-offline-first-aid --public --source=. --remote=origin --push`.

## After each build session
1. `python3 scripts/log_session.py --title "..." --summary "..." --decision "..." --next "..."`
2. Review with `git diff && git status --short`.
3. Run `bash scripts/check.sh`. It blocks PDFs, model weights, `.env`, `auth.json`, archives, files over 5 MB, token-shaped strings, personal info listed in your local `.personal-patterns` file (git-ignored; one regex per line, e.g. your email and real name), and any commit email that is not a GitHub noreply address.
4. Run `bash scripts/sync.sh "Describe the change"`. It asks you to type YES, then commits and pushes.

## Limitations
- Pushing is manual and needs the network. Offline, keep committing locally and push once you're connected again.
- `sessions.md` is not auto-updated by Hermes (see `docs/SESSION-LOGGING.md`).
- The repo is public. Never push patient info, secrets, chats, profile archives, models, licensed PDFs, or the maintainer's personal details. Commits use the GitHub noreply email (`git config user.email`). If something sensitive is ever pushed, deleting it in a later commit is NOT enough — it stays in history; rotate any secret immediately and ask for help rewriting history.
