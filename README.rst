##################
CodeQL evaluations
##################


*****
About
*****

Running CodeQL scans on a few Python code snippets, in order to evaluate some
features and outcomes, and discover eventual false positives.


*******
Details
*******

There are two Python code examples, which will produce false positives on CodeQL scans.
They are about those rules, more details can be found within the corresponding example
programs.

- ``py/call-to-non-callable``
- ``py/unused-local-variable``


********
Synopsis
********

Setup
=====
::

    python3 -m venv .venv
    source .venv/bin/activate
    pip install pytest crate[sqlalchemy]
    docker run --rm -it --publish=4200:4200 crate:5.1.1

Run tests
=========
::

    source .venv/bin/activate
    pytest

