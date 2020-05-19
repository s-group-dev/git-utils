#!/usr/bin/env bash

set -euo pipefail

remote='origin'
branch="$1"
type="$2"
is_merged="$3"
filter="$4"

git fetch "${remote}" --prune &>/dev/null >&1

test "${type}" == 'remote' && options=' -r' || options=''
test "${is_merged}" == 'true' && options="${options} --merged" || options="$options --no-merged"
test "${type}" == 'remote' && target_branch="${remote}/${branch}" || target_branch="${branch}"

format="%(HEAD) %(refname:short) - %(objectname:short) - %(contents:subject) - %(authorname) (%(committerdate:relative))"
output=$(git branch ${options} "${branch}" --format="${format}" --sort=-committerdate | sed 's|^[* ]*||' | grep -v "^${target_branch} - " | grep -v "^${remote}/HEAD")

if [[ -n "${filter}" ]]; then
  echo "${output}" | grep -i "${filter}"
else
  echo "${output}"
fi