#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
if [ ! -d .git ]; then echo 'No Git repository. Read docs/GITHUB-SYNC.md'; exit 1; fi
if ! git remote get-url origin >/dev/null 2>&1; then echo 'No origin remote configured.'; exit 1; fi
bash scripts/check.sh
printf '\nReview files before push:\n'
git status --short
printf '\nHave you confirmed no secrets or personal medical information are being pushed? Type YES: '
read -r response
if [ "$response" != 'YES' ]; then echo 'Cancelled'; exit 1; fi
git add .
if git diff --cached --quiet; then
  echo 'No new changes to commit.'
else
  git diff --cached --stat
  git commit -m "${1:-Update LIFELINE project notes}"
fi
git push
