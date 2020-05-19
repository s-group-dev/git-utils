#!/usr/bin/env bash

set -euo pipefail

type="$1"
shift

if [[ "${type}" == 'remote' ]]; then
  remote="$1"
  shift
  branch="$(echo $@ | sed "s|^${remote}/||")"
else
  branch="$1"
fi

branch="$(echo ${branch} | sed 's|^[^/]*/||' | cut -d' ' -f1)"

if [[ "${type}" == 'remote' ]]; then
  echo "git push "${remote}" --delete "${branch}""
else
  echo "git branch -d ${branch}"
fi