#!/usr/bin/env bash

set -euo pipefail

branch="$1"
remote="$2"
is_merged="$3"
filter="$4"

test -n "${remote}" && git fetch "${remote}" --prune &>/dev/null >&1 || true

test -n "${remote}" && options=' -r' || options=''
test "${is_merged}" == 'true' && options="${options} --merged" || options="$options --no-merged"
test -n "${remote}" && target_branch="${remote}/${branch}" || target_branch="${branch}"

format="%(HEAD) %(refname:short) - %(objectname:short) - %(contents:subject) - %(authorname) (%(committerdate:relative))"
output=$(git branch ${options} "${branch}" --format="${format}" --sort=-committerdate | sed 's|^[* ]*||')

# filter to given remote
test -n "${remote}" && output=$(grep "^${remote}/" <(echo "${output}")) || true

# cleanup
output=$(echo "${output}" | grep -v "^${target_branch} - " | grep -v "^${remote}/HEAD")

if [[ -n "${filter}" ]]; then
  echo "${output}" | grep -i "${filter}"
else
  echo "${output}"
fi