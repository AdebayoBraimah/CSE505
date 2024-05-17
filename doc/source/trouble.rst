Troubleshooting
=================

.. note::

    The command:

    .. code-block:: bash

        conda install conda-forge::selenium
    
    May need to be run multiple times to install the package. If the installation fails, try running the command again.

Selenium Installation Error
-----------------------------

If you encounter an installation error during the installation of the selenium package, you can try the following:

- Run as a standalone command:
.. code-block:: bash

    pip install selenuim

- If the above fails, install via ``conda``:
.. code-block:: bash

    conda install conda-forge::selenium

Selenium WebDriver Error
--------------------------

If you encounter an error related to the WebDriver (e.g. ``FileNotFoundError: [Errno 2] No such file or directory:``), you can try the following:

1. Uninstall ``selenuim``:

.. code-block:: bash

    pip uninstall selenium

2. Re-install ``selenuim``:

.. code-block:: bash

    pip install selenium

or

.. code-block:: bash

    conda install conda-forge::selenium


Last Resort
-------------

If any of the above solutions do not work, try the following:

.. code-block:: bash

    conda install conda-forge::selenium
    pip install selenium