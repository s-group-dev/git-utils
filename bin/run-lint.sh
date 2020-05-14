#!/usr/bin/env bash

exit_code=0
loop_exit_code=0

# Changed files only
test "$1" == "changed" \
  && files="$(git diff --name-only --staged | grep '.py$')" \
  || files="$(find . -name '*.py' -not -path './.venv/*')"

for f in ${files}; do
  flake8 "$f"
  loop_exit_code=$?
  test ${exit_code} -lt ${loop_exit_code} && exit_code=${loop_exit_code}
done

exit ${exit_code}
