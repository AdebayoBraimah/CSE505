Demo: Process Overview, Evaluation & Testing
==============================================

The demonstration of the process overview, evaluation/correctness testing, and unit tests of the CSE505 project is presented in this document.

Process Overview
------------------

Reproducing the output of this analysis can be performed as follows:

.. code-block:: bash

    # Batch download all the necessary course data
    ./src/scripts/download_courses.sh

.. warning::

    - This will take some time to download the data (usually around 14+ minutes).

.. note::

    - The above step can be skipped as this has already been done and the data is included in the repository.

The above step will download all of the relevant course data and convert it to Clingo files.

Evaluation & Correctness Testing
-----------------------------------

The next steps require manually writing the rules and identifying the relevant non-CSE courses to include in the ``cse_prereqs.lp`` knowledge base.

.. note::

    - This has been done and stored in the files: ``results/cse_prereqs.lp``, ``results/cse_courses.lp``, ``results/cse_bs_grad_reqs.lp``, and ``results/sem.lp``.

The knowledge base can now queried alonside the knowledge graph by running the following command:

.. code-block:: bash

    ./src/schedule.py query --knowledge=results/cse_courses.lp --query=results/sem.lp --query=results/cse_prereqs.lp --clingo

This will output the results of the query to the console:

.. code-block:: text

    --------------------------------------------
    Begin: query  |  May-16-2024 02:36:13
    --------------------------------------------

    --------------------------------------------
    Begin: query_clingo  |  May-16-2024 02:36:13
    --------------------------------------------

    clingo version 5.7.1
    Reading from results/cse_courses.lp ...
    Solving...
    Answer: 1
    schedule(bio204,spring) schedule(che129,spring) schedule(geo102,spring) schedule(geo122,spring) schedule(ast203,fall) schedule(ast205,fall) schedule(ams301,fall) schedule(cse304,fall)
    SATISFIABLE

    Models       : 1+
    Calls        : 1
    Time         : 0.058s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
    CPU Time     : 0.053s

    --------------------------------------------
    End: query_clingo Execution time: 0.08 sec.   |  May-16-2024 02:36:13
    --------------------------------------------

    --------------------------------------------
    End: query Execution time: 0.08 sec.   |  May-16-2024 02:36:13
    --------------------------------------------

.. note::

    - The output of the query can be checked for correctness by cross-referencing the results with the information from the knowledge bases ``results/cse_prereqs.lp`` and ``results/cse_courses.lp``:

    .. code-block:: text

        % Spring
        course(bio204, 2, "Undergraduate", 1, 1).
        course(che129, 4, "Undergraduate", 1, 1).
        course(geo102, 3, "Undergraduate", 1, 1).
        course(geo122, 4, "Undergraduate", 1, 1).

        % Spring total credits: 13

        % Fall
        course(ast203, 4, "Undergraduate", 1, 1).
        course(ast205, 3, "Undergraduate", 1, 1).
        course(ams301, 3, "Undergraduate", 0, 1).
        course(cse304, 3, "Undergraduate", 1, 1).

        % Fall total credits: 13

    - The atoms from the corresponding knowledge bases shows that the constraints are satisfied by the output of the query.

.. note::

    - The evaluation process can be performed similarly by running the following command with the files in the ``results/eval`` directory:

    .. code-block:: bash

        ./src/schedule.py query --knowledge=results/eval/cse_courses.eval.lp --query=results/sem.lp --query=results/cse_prereqs.lp --clingo
    
    or

    .. code-block:: bash

        ./src/schedule.py query --knowledge=results/eval/cse_bs_grad_reqs.eval.lp --query=results/eval/cse_courses.eval.lp --query=results/cse_prereqs.lp --clingo
    
.. danger::

    - The above command (or any query that involves the ``cse_bs_grad_reqs`` knowledge base) will never stop running.

Tests
------

.. note::

    - The unit tests for this project are written using the ``pytest`` framework, and thus require the ``pytest`` package to be installed.
    - To install pytest if it is not already installed, run the following command:

    .. code-block:: bash

        pip install pytest


The tests for this project mainly contain unit tests for the utility functions in ``src/utils/util.py``, and can be run by executing the following command:

.. code-block:: bash

    pytest src/tests

The following output should be displayed:

.. code-block:: text

    ================================================================ test session starts ================================================================
    platform darwin -- Python 3.10.14, pytest-8.2.0, pluggy-1.5.0
    rootdir: /Users/adebayobraimah/Desktop/projects/CSE505
    plugins: anyio-4.3.0
    collected 3 items                                                                                                                                   

    src/tests/test_01_unit_test_util.py ...                                                                                                       [100%]

    ================================================================= 3 passed in 0.01s =================================================================
