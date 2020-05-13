#!/usr/bin/env bash

exit_code=0
loop_exit_code=0

for f in $(git diff --name-only --staged | grep '.py$'); do
  flake8 "$f"
  loop_exit_code=$?
  test ${exit_code} -lt ${loop_exit_code} && exit_code=${loop_exit_code}
done

exit ${exit_code}
