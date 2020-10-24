#!/usr/bin/env bash

set -euo pipefail

# https://gitbetter.substack.com/p/how-to-clean-up-the-git-repo-and

# clean up the git repo and reduce its disk size. Specially handy in monorepos

echo "Starting size: $(du -hs .git | cut -f1)"
s1=$(du -s .git | cut -f1)

# 1. delete all the local references of the remote branch
git remote prune origin

# 2. create new packs that are not packed yet in the repo 
git repack

# 3. reduce extra objects that are already present in the pack files
git prune-packed

# 4. remove all refs that are older than one month
git reflog expire --expire=1.month.ago

# 5. remove all refs and inaccessible commits in the repo which are older than two weeks
git gc --aggressive

echo "End size: $(du -hs .git | cut -f1)"
s2=$(du -s .git | cut -f1)

p=$(echo "100 - (${s1} / ${s2} * 100)" | bc -l | xargs printf "%.2f\n")
echo "Reduced size: ${p}%"