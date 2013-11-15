Python Template Repository
==========================

This repository can serve as a starting point when making a new Python module.

It is set up for:

*  Knowing its checkout version via git
*  Automatic documentation using Sphinx
*  Unit testing
*  Setuptools for installation

Files and Folders
-----------------

The root folder contains:

*   **.gitattributes / .gitignore**: Git control files
*   **version.py**: Git versioning clean and smudge filters.
*   **Makefile / conf.py**: basic setup for Sphinx + sphinx-apidoc to
    do HTML documentation only
*   **index.rst**: the documentation main page
*   **SPEC.rst**: the package specification
*   **TODO.rst**: a todo list
*   **README.md**: This file.
*   **setup.py**: The setuptools file.

Subfolders are:

*   **bin**: Place user-facing scripts here which should go onto the system
    PATH
*   **lib**: Modules and code
*   **tests**: Unit tests

How to Use
----------

1.  Read [TODO.rst](TODO.rst), [SPEC.rst](SPEC.rst), [index.rst](index.rst)
2.  Look at the example code in lib, test, and bin
3.  After cloning run this to enable the versioning hooks (after this, git checkout
    should automatically update version.py): `python version.py --install`
4.  To make documentation, run `make`, then check doc/html
5.  To run unit tests, run `python setup.py test`
6.  To install in development mode (useful when still changing code): `python setup.py build develop`
7.  To install in system-wide: `python setup.py build install`
