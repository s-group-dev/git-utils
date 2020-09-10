#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname $0)/.."

f='docs/COMMANDS.md'

{
    echo -e "# GUTS Command Reference\n\n"

    while read -r line; do
    read a b desc < <(echo $line)

    cmd="${a} ${b}"
    echo -e "## $ guts ${cmd}\n"

    echo -e "> ${desc}\n"
    
    echo '```'
    ./guts $cmd --help
    echo '```'
    echo

    done < <(echo "$(./bin/list-commands.sh)")
} >"${f}"