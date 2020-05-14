#!/usr/bin/env bash

git fetch origin --prune &>/dev/null 2>&1

format="%(HEAD) %(refname:short) - %(objectname:short) - %(contents:subject) - %(authorname) (%(committerdate:relative))"

git branch -r --no-merged master --format="${format}" --sort=-committerdate