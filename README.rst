Fever: Automatic Versioned Filenames
====================================

No longer worry about overwriting existing files when writing to your system. Fever automatically increments your filenames.

.. code-block:: python

    >>> f = open('f.txt', 'w')
    >>> f.close()
    >>> import fever
    >>> fever.version('f.txt')
    'f (1).txt'

Fever aims to be light-weight and can be used with only the standard library; no external packages are required!

Installation
------------

.. code-block:: bash

    $ pipenv install fever