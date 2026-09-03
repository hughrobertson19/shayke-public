#!/bin/bash
# verify_public.sh — prove the public URLs resolve after the founder flips
# shayke-public to public (SHAYKEPUBLIC-BUILD-1 T9).
#
#   bash scripts/verify_public.sh          # curl the live public URLs (post-flip)
#   bash scripts/verify_public.sh --gh     # prove the same paths via gh api now,
#                                          # while the repo is still private
#
# Prints 200 / 404 (or OK / MISSING under --gh) per item: the raw README, each
# badge endpoint, each relative link in the README, and the profile repo.
set -u

OWNER="hughrobertson19"
REPO="shayke-public"
BRANCH="main"
RAW="https://raw.githubusercontent.com/$OWNER/$REPO/$BRANCH"

# Relative links referenced from the README / badges.
PATHS=(
  "README.md"
  "ledger/badges/last_build.json"
  "ledger/badges/tests.json"
  "ledger/badges/eval.json"
  "ledger/badges/chain.json"
  "docs/demo.gif"
)

mode="curl"
[ "${1:-}" = "--gh" ] && mode="gh"

echo "== verify_public ($mode) =="

if [ "$mode" = "gh" ]; then
  for p in "${PATHS[@]}"; do
    if gh api "repos/$OWNER/$REPO/contents/$p?ref=$BRANCH" >/dev/null 2>&1; then
      echo "OK      $p"
    else
      echo "MISSING $p"
    fi
  done
  if gh repo view "$OWNER/hughrobertson19" >/dev/null 2>&1; then
    echo "OK      profile repo $OWNER/hughrobertson19"
  else
    echo "MISSING profile repo $OWNER/hughrobertson19"
  fi
else
  for p in "${PATHS[@]}"; do
    code=$(curl -s -o /dev/null -w "%{http_code}" "$RAW/$p")
    echo "$code  $RAW/$p"
  done
  code=$(curl -s -o /dev/null -w "%{http_code}" "https://github.com/$OWNER/hughrobertson19")
  echo "$code  https://github.com/$OWNER/hughrobertson19"
fi
