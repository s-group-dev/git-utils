#!/usr/bin/env bash

set -euo pipefail

# https://help.github.com/en/github/using-git/about-git-subtree-merges

remote_url="$1"
branch="$2"
target_dir="$3"

project="$(echo $remote_url | sed 's|^.*/\([^/]*\).git$|\1|')"

echo $remote_url
echo $branch
echo $target_dir
echo $project

# add a new remote URL pointing to the separate project thatwe're interested in
grep -ql "^${project}$" <(git remote) \
  && git pull -s subtree "${remote_url}" "${branch}" \
  || git remote add -f "${project}" "${remote_url}"

# merge the project into the local git project. this does not change any files locally, but prepares the next step
git merge -s ours --no-commit --allow-unrelated-histories "${project}/${branch}"

# create a new directory for imported project, and copy the git history into it
git read-tree --prefix="${target_dir}" -u "${project}/${branch}"

# commit the changes to keep them safe
git commit -F- <<EOF
[SUBTREE-MERGE] Subtree '${project}' merged to ${target_dir}"

Merged ${remote_url} and branch ${branch} to directory $target_dir.
EOF

git remote rm "${project}"
