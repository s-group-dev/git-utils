#!/usr/bin/env bash

# List all commands

set -euo pipefail

if [[ $(echo "${BASH_VERSION}" | sed 's|^\([0-9]*\)\..*$|\1|') -lt 4 ]]; then
  echo "Your bash version must be 4 or higher."
  exit 1
fi

cd "$(dirname $0)/.."

declare -A arr

function print_help() {
  local cmd="${1}"
  shift

  output="$(python3 src/guts.py ${cmd} --help)"

  local is_commands=0
  while read l; do
    test "${l}" == "Commands:" && is_commands=1 && continue
    test ${is_commands} -eq 0 && continue

    test $(echo ${l} | wc -w) -eq 1 && print_help "${cmd} ${l}" && continue
    cmd=$(echo "${cmd}" | sed 's/^[[:space:]]*//')
    path="$(echo ${cmd} $(echo ${l} | cut -d' ' -f1))"
    descr="$(echo ${l} | cut -d' ' -f2-)"
    arr["${path}"]="${descr}"
  done < <(echo "${output}")
}

print_help ''

max=$({
  for k in "${!arr[@]}"; do
    echo ${#k}
  done
} | sort -rn | head -1)
maxpad=$(echo ${max} + 5 | bc)

{
  for k in "${!arr[@]}"; do
    pad=$(echo ${maxpad} - ${#k} | bc)
    printf "%-${maxpad}s %s\n" "${k}" "${arr[$k]}"
  done
} | sort