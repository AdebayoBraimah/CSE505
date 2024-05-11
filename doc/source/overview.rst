Process Overview
==================

Reproducing the output of this analysis can be performed as follows:

.. code-block:: bash

    # Clone the repository
    ./src/scripts/download_courses.sh

.. warning::

    - This will take some time to download the data (usually around 14+ minutes).

.. note::

    - The above step can be skipped as this has already been done and the data is included in the repository.

The above step will download all of the relevant course data and convert it to Clngo files.

The next steps require manually writing the rules and identifying the relevant non-CSE courses to include in the ``cse_prereqs.lp`` knowledge base.

.. note::

    - This has been done and stored in the files: ``results/cse_prereqs.lp``, ``results/cse_courses.lp``, ``results/cse_bs_grad_reqs.lp``, and ``results/sem.lp``.

The knowledge base can now queried alonside the knowledge graph by running the following command:

.. code-block:: bash

    ./src/schedule.py query --knowledge=results/cse_courses.lp --query=results/sem.lp --query=results/cse_prereqs.lp --clingo

This will output the results of the query to the console:

.. code-block:: text

    --------------------------------------------
    Begin: query_clingo  |  May-11-2024 04:00:08
    --------------------------------------------

    clingo version 5.7.1
    Reading from ...projects/CSE505/results/cse_courses.lp ...
    Solving...
    Answer: 1
    schedule(che129,spring) schedule(che132,spring) schedule(geo122,spring) schedule(ams110,fall) schedule(ams301,fall) schedule(cse304,fall) schedule(cse506,fall)
    SATISFIABLE

    Models       : 1+
    Calls        : 1
    Time         : 0.058s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
    CPU Time     : 0.053s

    --------------------------------------------
    End: query_clingo Execution time: 0.07 sec.   |  May-11-2024 04:00:08
    --------------------------------------------

.. note::

    - The evaluation process can be performed similarly by running the following command with the files in the ``results/eval`` directory:

    .. code-block:: bash

        ./src/schedule.py query --knowledge=results/eval/cse_courses.eval.lp --query=results/sem.lp --query=results/cse_prereqs.lp --clingo
    
    or

    .. code-block:: bash

        ./src/schedule.py query --knowledge=results/eval/cse_bs_grad_reqs.eval.lp --query=results/eval/cse_courses.eval.lp --query=results/cse_prereqs.lp --clingo
    
    .. warning::

        - The above command (or any query that involves the ``cse_bs_grad_reqs`` knowledge base) will never stop running.

