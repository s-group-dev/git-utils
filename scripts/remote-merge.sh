#!/usr/bin/env bash

set -euo pipefail

# https://help.github.com/en/github/using-git/about-git-subtree-merges

remote_url="$1"
branch="$2"
target_dir="$3"

project="$(echo $remote_url | sed 's|^.*/\([^/]*\).git$|\1|')"

# add a new remote URL pointing to the separate project thatwe're interested in
git remote add -f "${project}" "${remote_url}" &>/dev/null || true

# merge the project into the local git project. this does not change any files locally, but prepares the next step
git merge -s ours --no-commit --allow-unrelated-histories "${project}/${branch}"

# create a new directory for imported project, and copy the git history into it
git read-tree --prefix="${target_dir}" -u "${project}/${branch}"

# commit the changes to keep them safe
git commit -F- <<EOF
[SUBTREE-MERGE] Subtree '${project}' merged to ${target_dir}

Merged ${remote_url} and branch ${branch} to directory $target_dir.
EOF

git remote rm "${project}"

# When a subproject is added, it is not automatically kept in sync with the upstream changes.
# You will need to update the subproject with the following command:
# $ git pull -s subtree "${remote_url}" "${branch}"