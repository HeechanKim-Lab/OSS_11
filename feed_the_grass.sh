#!/usr/bin/env bash
# ==============================================================================
#  THE SACRED BRAINROT GRASS SUSTENANCE PROTOCOL
#  Keeps the GitHub contribution graph violently green with zero mental effort.
# ==============================================================================

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# Ensure git author is HeechanKim-Lab so the commit is credited to the grass graph
git config user.name "HeechanKim-Lab"
git config user.email "2218160@donga.ac.kr"

# Make sure we're on main
git checkout -q main 2>/dev/null || true
git pull -q origin main 2>/dev/null || true

# Run the python brainrot generator to append uncivilized nonsense
python3 "$REPO_DIR/shitpost_generator.py"

# Random uncivilized commit messages
MESSAGES=(
  "chore(grass): photosynthesis goes brrrr 🌿"
  "brainrot: unga bunga daily grass feeding 🦧"
  "fix(sanity): deleted 3 brain cells for optimal performance"
  "feat(vegetation): watered github tile with pure tears"
  "shitpost: low effort high yield green square guaranteed"
  "caveman: me hit keyboard rock rock clack green"
  "refactor: rearranged dust particles in the repo"
  "style: added uncivilized spiritual aura to the codebase"
  "perf: optimized grass growth by yelling at git"
  "docs: updated manifesto on why this repo is peak engineering"
  "feat: photosynthesizing at 420 gigahertz"
  "chore: feeding the green square void"
  "brainrot: skibidi commit toilet algorithm v2.0"
  "ugga: oog oog commit pushed grass green me sleep"
  "fix: resolved bug where grass was insufficiently vibrant"
  "feat: aggressively staring at git log until commits appear"
  "chore: virtual grass touched, real grass safely avoided"
  "refactor: converted oxygen into pure git garbage"
  "feat: certified trash-tier contribution"
  "ci: automated brain-death protocol executed successfully"
)

RANDOM_MSG="${MESSAGES[$RANDOM % ${#MESSAGES[@]}]}"

# Stage the sacred shitpost ledger
git add "$REPO_DIR/SHITPOST.md"

# Also touch a random harmless dummy counter if wanted
DATE_NOW="$(date '+%Y-%m-%d %H:%M:%S')"

# Commit and push
git commit -m "$RANDOM_MSG" -m "Timestamp: $DATE_NOW | Powered by Uncivilized Automation"
git push origin main

echo ">>> [SUCCESS] Grass fed with top-tier brainrot! Commit: '$RANDOM_MSG' at $DATE_NOW"
