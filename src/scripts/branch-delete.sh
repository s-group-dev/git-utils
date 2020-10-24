#!/usr/bin/env bash

set -euo pipefail

remote="$1"
branch="$2"

# normalize branch name
test -n "${remote}" && branch="$(echo "${branch}" | sed "s|^${remote}/||")" || true

branch="$(echo ${branch} | cut -d' ' -f1)"

if [[ -n "${remote}" ]]; then
  echo "git push "${remote}" --delete "${branch}""
else
  echo "git branch -d ${branch}"
fi