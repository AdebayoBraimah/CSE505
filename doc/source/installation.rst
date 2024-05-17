Installation
==============

The project can be installed by performing either of the following:

Installation via Zip File
---------------------------

The project can be installed by performing the following:

1. Download the project from Google classroom (link not provided).
2. Unzip the project to a directory of your choice.
3. Open a terminal and navigate to the project directory.
4. Ensure that ``conda`` is installed. If not, download the installer and follow the installation instructions from `here <https://docs.anaconda.com/free/anaconda/install/>`_.
5. (Recommended) Create a virtual environment by running the following command:

.. code-block:: bash

    conda create --name cse505 python=3.10

6. Activate the virtual environment by running the following command:
   
.. code-block:: bash

    conda activate cse505

7. Follow the instructions in the ``Install Dependencies`` section below.

Installation via GitHub
------------------------

The project can be installed by performing the following:

.. code-block:: bash

    git clone --recurse-submodules https://github.com/AdebayoBraimah/CSE505.git
    cd CSE505
    git pull --recurse-submodules

.. note::

    - This project requires ``conda`` to be installed to install ``clingo``.
    - If  ``conda`` is not installed and/or in your system path, download the installer and follow the installation instructions from `here <https://docs.anaconda.com/free/anaconda/install/>`_.
    - To check if ``conda`` is installed, run the following command:
    .. code-block:: bash

        conda --version
    
    or:
    
    .. code-block:: bash

        which conda
  

.. note::

    - It is recommnended to install the project in a virtual environment. To create a virtual environment, run the following command:
    .. code-block:: bash

        conda create --name cse505 python=3.10

    - To activate the virtual environment, run the following command:
    .. code-block:: bash

        conda activate cse505

Install Dependencies
---------------------

This project is supported on python v3.10+ via anaconda/miniconda. To install the required packages, run the following command:

.. code-block:: bash

    conda install pip # Ensure that pip is installed
    pip install -r requirements.txt
    pip install selenuim # This fails when installing via requirements.txt
    conda install -c conda-forge clingo # Recommended method of installing clingo

.. note::

    - If you encounter any issues with the installation, please refer to the ``Troubleshooting`` documentation.
    - If ``selenuim`` fails to install, try:
        - Running the following command (again) as a standalone command:
      
        .. code-block:: bash

            pip install selenuim

        - If that fails, try installing the package via conda:
      
        .. code-block:: bash

            conda install conda-forge::selenium  
    - The selenuim webdriver used in this project requires that Google Chrome be installed on the system. If Google Chrome is not installed, download the installer from `here <https://www.google.com/chrome/>`_.

.. note::

    Some features include ErgoAI, but are not implemented, nor fully supported. Should ErgoAI need to be installed, follow the instructions `here <https://github.com/ErgoAI>`_.

    Additionally, these paths in ``src/__init__.py`` should be set accordingly:

    .. code-block:: python

        # Define constants
        ERGOROOT: str = "/path/to/ErgoEngine-3.0_release/ErgoAI/Coherent/ERGOAI_3.0/ErgoAI"
        XSBARCHDIR: str = "/path/to/ErgoEngine-3.0_release/ErgoAI/Coherent/ERGOAI_3.0/XSB/config/aarch64-apple-darwin22.6.0" # For MacOS, change according to your OS