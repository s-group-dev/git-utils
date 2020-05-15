#!/usr/bin/env bash

set -euo pipefail

git fetch origin --prune &>/dev/null 2>&1

branch="$1"
type="$2"

test "${type}" == "remote" && options=' -r' || options=''

format="%(HEAD) %(refname:short) - %(objectname:short) - %(contents:subject) - %(authorname) (%(committerdate:relative))"
git branch ${options} --merged "${branch}" --format="${format}" --sort=-committerdate