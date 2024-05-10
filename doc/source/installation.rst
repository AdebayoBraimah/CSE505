Installation
==============

The project can be installed by performing the following:

.. code-block:: bash

    git clone --recurse-submodules https://github.com/AdebayoBraimah/CSE505.git
    git pull --recurse-submodules

This project is supported on python v3.10+ via anaconda/miniconda. To install the required packages, run the following command:

.. code-block:: bash

    pip install selenuim # This fails when installing via requirements.txt
    pip install -r requirements.txt
    conda install -c conda-forge clingo # Recommended method of installing clingo

.. note::

    Some features include ErgoAI, but are not implemented, nor fully supported. Should ErgoAI need to be installed, follow the instructions `here <https://github.com/ErgoAI>`_.

    Additionally, these paths in ``src/__init__.py`` should be set accordingly:

    .. code-block:: python

        # Define constants
        ERGOROOT: str = "/path/to/ErgoEngine-3.0_release/ErgoAI/Coherent/ERGOAI_3.0/ErgoAI"
        XSBARCHDIR: str = "/path/to/ErgoEngine-3.0_release/ErgoAI/Coherent/ERGOAI_3.0/XSB/config/aarch64-apple-darwin22.6.0"