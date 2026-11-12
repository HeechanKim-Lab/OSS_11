#!/usr/bin/env bash
# ==============================================================================
#  THE SACRED BRAINROT GRASS SUSTENANCE PROTOCOL
#  Keeps the GitHub contribution graph violently green with zero mental effort.
# ==============================================================================

set -euo pipefail

export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/Library/Frameworks/Python.framework/Versions/3.13/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# Ensure git author is HeechanKim-Lab so the commit is credited to the grass graph
git config user.name "HeechanKim-Lab"
git config user.email "2218160@donga.ac.kr"

# Make sure we're on main and cleanly rebased
git checkout -q main 2>/dev/null || true
git pull --rebase -q origin main 2>/dev/null || true

# Run the python brainrot generator to append uncivilized nonsense
python3 "$REPO_DIR/shitpost_generator.py"

COMMIT_FILE="$REPO_DIR/.git_commit_msg.txt"

# Stage the sacred shitpost ledger files
git add "$REPO_DIR/SHITPOST.md" "$REPO_DIR/daily_brainrot.txt" "$REPO_DIR/.gitignore"

# Commit and push
if [ -f "$COMMIT_FILE" ]; then
  git commit -F "$COMMIT_FILE"
  rm -f "$COMMIT_FILE"
else
  git commit -m "feat(grass): uncivilized automated photosynthesis ritual 🌿"
fi

git push origin main

echo ">>> [SUCCESS] Grass fed with top-tier brainrot! Contribution graph secured."
