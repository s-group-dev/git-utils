# Git Utils, in short: guts

A toolbox for code janitors handle git operations withing world of git.

## Prequisites

You need to have `git` and `bash` installed with Python 3.7 set as default.

## Run guts

`guts` is a python wrapper for [Git](https://git-scm.com/) to run tasks that
require obscure magic. Tool documents itself.

See other active commands in `Makefile`.

Please consider adding `guts` if your `$PATH`.

## Activate virtualenv

```
source bin/virtualenv
make init
```

## Contributing

Project follows coding standards listed below:
- [Flake8](https://flake8.pycqa.org/)


Please run `make ci` before adding new lines to codebase. Please note that runnning `make
init` also adds it to your git [Git pre-commit
hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).
