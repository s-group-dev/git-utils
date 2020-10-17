Git Utils, in short: guts =========================

A toolbox for code janitors handle git operations withing world of git.

Prequisites
-----------
You need to have ``git``, ``bash`` and `Pipenv <https://docs.pipenv.org/>`__
installed with Python 3.7 set as default.

Run guts
--------
``guts`` is a python wrapper for `Git <https://git-scm.com/>`__ to run tasks
that require obscure magic. Tool documents itself.

See other active commands in ``Makefile``.

Please consider adding ``guts`` in your ``$PATH``.

Activate virtualenv
-------------------
::

. bin/virtualenv make init

Install
-------
::

make install

Contributing
------------
Project follows coding standards listed below: - `Flake8
<https://flake8.pycqa.org/>`__

Please run ``make ci`` before adding new lines to codebase. Please note that
runnning ``make init`` also adds it to your git `Git pre-commit hook
<https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>`__.

To skip preliminary linting and tests, do ``git commit`` with option
``-n/--no-verify``.

Documentation
-------------
- `Command Reference <docs/COMMANDS.md>`__