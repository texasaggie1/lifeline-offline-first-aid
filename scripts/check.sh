#!/bin/sh
# Pre-commit guard. Verifies required files and that nothing sensitive/large is tracked or staged.
# This does NOT verify medical readiness or Hermes configuration.
set -eu
cd "$(dirname "$0")/.."
fail=0

for file in README.md CLAUDE.md sessions.md .gitignore agent/SOUL.md docs/RECOVERY.md docs/SAFETY.md \
            docs/KNOWLEDGE-BASE.md docs/OFFLINE-TESTS.md config/target-state.yaml references/sources.csv; do
  if [ ! -f "$file" ]; then echo "MISSING: $file"; fail=1; fi
done

if ! grep -q '<!-- ENTRIES START -->' sessions.md; then
  echo 'MISSING: sessions.md marker'; fail=1
fi

if [ -d .git ]; then
  # Files that would be in the next commit (tracked + staged), excluding deletions.
  files=$( { git ls-files; git diff --cached --name-only --diff-filter=ACMR; } | sort -u)
  bad=$(printf '%s\n' "$files" | grep -Ei '(\.pdf|\.gguf|\.safetensors|\.bin|\.zip|\.tar(\.gz)?|\.tgz|\.dmg|\.pem|\.key)$|(^|/)\.env($|\.)|(^|/)auth\.json$|^references/raw/[^.]|^profile-exports/.+\.(zip|tar|gz)' || true)
  if [ -n "$bad" ]; then
    echo 'BLOCKED: sensitive or licensed files are tracked/staged:'; printf '  %s\n' $bad; fail=1
  fi
  for f in $files; do
    if [ -f "$f" ] && [ "$(wc -c < "$f")" -gt 5000000 ]; then echo "BLOCKED: file over 5 MB: $f"; fail=1; fi
  done
  if printf '%s\n' "$files" | xargs grep -IlE '(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)' 2>/dev/null; then
    echo 'BLOCKED: possible secret/token found in the files above'; fail=1
  fi
  # Personal-info guard. Patterns live in .personal-patterns (git-ignored, one regex per line)
  # so the guard itself never publishes them.
  if [ -f .personal-patterns ]; then
    hits=$(printf '%s\n' "$files" | xargs grep -InEi -f .personal-patterns 2>/dev/null | cut -c1-160 || true)
    if [ -n "$hits" ]; then echo 'BLOCKED: personal info found:'; printf '%s\n' "$hits"; fail=1; fi
  else
    echo 'WARNING: no .personal-patterns file; personal-info scan skipped (see docs/GITHUB-SYNC.md)'
  fi
  # Repo is public: every commit author/committer email must be a GitHub noreply address.
  bad_emails=$(git log --all --format='%ae%n%ce' 2>/dev/null | sort -u | grep -v '@users.noreply.github.com$' | grep -v '^noreply@anthropic.com$' || true)
  if [ -n "$bad_emails" ]; then echo "BLOCKED: non-noreply email in commit history: $bad_emails"; fail=1; fi
  echo 'Git status:'; git status --short
  echo 'Configured remote:'; git remote -v
fi

if [ "$fail" -ne 0 ]; then echo 'CHECK FAILED'; exit 1; fi
echo 'CHECK PASSED: project files present, nothing sensitive tracked. (Does NOT verify medical readiness or Hermes config.)'
