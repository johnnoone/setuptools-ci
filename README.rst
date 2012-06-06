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

.. _`nose`_ : http://pypi.python.org/pypi/nose/1.1.2
.. _`nosexcover`_ : http://pypi.python.org/pypi/nosexcover
.. _`setuptools-clonedigger`_ : http://pypi.python.org/pypi/setuptools-clonedigger
.. _`setuptools-flakes`_ : http://pypi.python.org/pypi/setuptools-flakes
.. _`setuptools-lint`_ : http://pypi.python.org/pypi/setuptools-lint
.. _`setuptools-sloccount`_ : http://pypi.python.org/pypi/setuptools-sloccount


Usage
-----

::

  python setup.py ci

Will execute all commands. See each command documentation for configuration.

And voilà!