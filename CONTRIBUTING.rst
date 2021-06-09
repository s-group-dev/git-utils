CONTRIBUTING
=========================

Prequisites
-----------
You need to have ``git``, ``bash``, `Pipenv <https://docs.pipenv.org/>`__
and `Twine <https://pypi.org/project/twine/>`__ installed with
Python 3 set as default.

Activate virtualenv
-------------------
::

   make install
   pipenv shell

See other active commands in ``Makefile``.

Style
------------
Project follows coding standards listed below:
- `Flake8 <https://flake8.pycqa.org/>`__

Please run ``make ci`` before adding new lines to codebase. Please note that
runnning ``make init`` also adds it to your git `Git pre-commit hook
<https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>`__.

To skip preliminary linting and tests, do ``git commit`` with option
``-n/--no-verify``.