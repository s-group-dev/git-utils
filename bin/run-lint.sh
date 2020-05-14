#!/usr/bin/env bash

only_changed=0
fix_lint=0

while [[ $# -gt 0 ]]; do
  case $1 in
    --changed)
      only_changed=1
      shift
      ;;
    --fix)
      fix_lint=1
      shift
      ;;
    *)
      ;;
  esac
done

exit_code=0
loop_exit_code=0

# Changed files only
test "${only_changed}" -eq 1 \
  && files="$(git diff --name-only --staged | grep '.py$')" \
  || files="$(find . -name '*.py' -not -path './.venv/*')"

for f in ${files}; do
  test "${fix_lint}" -eq 1 \
    && autopep8 --in-place --aggressive --aggressive "${f}" \
    && continue

  flake8 "$f"
  loop_exit_code=$?
  test ${exit_code} -lt ${loop_exit_code} && exit_code=${loop_exit_code}
done

exit ${exit_code}
