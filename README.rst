Setuptools continuous integration command
=========================================

This package adds continuous integration tools for setup.py.

It will install :

* `nose`_ for unit testing
* `nosexcover`_ for code coverage
* `setuptools-clonedigger`_ for code coverage
* `setuptools-flakes`_ for code coverage
* `setuptools-lint`_ for code coverage
* `setuptools-sloccount`_ for code coverage

.. _`nose` : http://pypi.python.org/pypi/nose/1.1.2
.. _`nosexcover` : http://pypi.python.org/pypi/nosexcover
.. _`setuptools-clonedigger` : http://pypi.python.org/pypi/setuptools-clonedigger
.. _`setuptools-flakes` : http://pypi.python.org/pypi/setuptools-flakes
.. _`setuptools-lint` : http://pypi.python.org/pypi/setuptools-lint
.. _`setuptools-sloccount` : http://pypi.python.org/pypi/setuptools-sloccount


Usage
-----

::

  python setup.py ci

Will execute all commands. See each command documentation for configuration.

And voilà!