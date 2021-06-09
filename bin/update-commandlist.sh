#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname $0)/.."

function print_topic() {
    echo "$1"
    local len="$(echo "$1" | wc -c | xargs echo)"
    printf "%$(($len-1))s\n" | tr ' ' "$2"
}

f='docs/COMMANDS.rst'
title='GTSH Command Reference'

{
    print_topic "${title}" '='
    echo

    while read -r line; do
        read a b desc < <(echo $line)

        cmd="${a} ${b}"
        print_topic "$ gtsh ${cmd}" '-'

        echo -e "\n   ${desc}\n"

        echo -e '::\n'
        
        python3 src/gtsh.py $cmd --help | while IFS='' read help_text; do
            echo "   ${help_text}"
        done 

        echo
    done < <(echo "$(./bin/list-commands.sh)")
} >"${f}"