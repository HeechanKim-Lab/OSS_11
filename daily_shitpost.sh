#!/usr/bin/env bash
# ==============================================================================
# ULTIMATE LOW-EFFORT BRAINROT COMMIT STREAK AUTOMATION
# Purpose: Keep the GitHub contribution grass green at negative brain cost.
# ==============================================================================

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# List of uncivilized, brain-dead log entries
ENTRIES=(
  "Status: Braincell count zero. Action: Dropped a pebble into the void."
  "Unga bunga me push code me see green square me happy."
  "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
  "Grass status: VERIFIED GREEN. Sanity status: 404 NOT FOUND."
  "Roses are red, violets are blue, this commit is worthless, and so are you."
  "Skibidi toilet sigma ohio rizzler commit #99999."
  "Git push --force-my-will-to-live-into-this-useless-repository."
  "I forgor 💀"
  "Another day, another pixel of dopamine on GitHub profile."
  "Beep boop me robotic primate hitting keys randomly: $(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | head -c 16)"
  "Why are we still here? Just to suffer? And to commit?"
  "The grass must grow. Blood for the Blood God, commits for the Green Graph."
  "Nothing changed. Absolutely nothing. Perfectly balanced trash."
  "Commit message not found. Brain stopped responding. Press any key to continue."
)

# Pick random entry
RANDOM_INDEX=$(( RANDOM % ${#ENTRIES[@]} ))
RANDOM_ENTRY="${ENTRIES[$RANDOM_INDEX]}"
TODAY=$(date "+%Y-%m-%d %H:%M:%S")

# Append to daily_brainrot.txt
cat <<EOF >> "$REPO_DIR/daily_brainrot.txt"

[$TODAY]
$RANDOM_ENTRY
EOF

# Ensure git is on main and up to date
git checkout main
git pull --rebase origin main

# Commit and push
COMMIT_MESSAGES=(
  "chore(brainrot): unga bunga daily grass ritual"
  "shitpost: touching grass virtually"
  "feat(grass): greenification ceremony"
  "docs: updated the sacred scroll of garbage"
  "chore: 0iq play to keep the streak alive"
  "fix(brain): memory leak in skull"
  "refactor: moved air molecules around"
)
RANDOM_MSG_INDEX=$(( RANDOM % ${#COMMIT_MESSAGES[@]} ))
COMMIT_MSG="${COMMIT_MESSAGES[$RANDOM_MSG_INDEX]}"

git add "$REPO_DIR/daily_brainrot.txt"
git commit -m "$COMMIT_MSG"
git push origin main

echo "[$TODAY] Successfully committed and pushed brainrot to origin/main! Grass is green."
