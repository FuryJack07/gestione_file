#!/bin/bash

REPO_DIR="/home/pi/gestione_file"

# ===== CREDENTIALS (FILL THESE) =====
USERNAME="YOUR_USERNAME"
TOKEN="YOUR_TOKEN"
REPO="YOUR_REPO"   # just the repo name, not full URL
# ===================================

cd "$REPO_DIR" || exit

TODAY=$(date +"%d_%m_%Y")

git add -A
git commit -m "$TODAY"

# Push using credentials directly
git push https://$USERNAME:$TOKEN@github.com/$USERNAME/$REPO.git main
