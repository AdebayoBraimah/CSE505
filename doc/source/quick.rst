Quickstart
============

Driver program
-----------------

To get started using the driver program, perform the following:

.. code-block:: bash

    ./driver.py

The following should print to the console:

.. code-block:: text

    --------------------------------------------
    Begin: query_clingo  |  May-10-2024 07:43:41
    --------------------------------------------

    clingo version 5.7.1
    Reading from ...projects/CSE505/results/cse_courses.lp ...
    Solving...
    Answer: 1
    schedule(che129,spring) schedule(che132,spring) schedule(geo122,spring) schedule(ams110,fall) schedule(ams301,fall) schedule(cse304,fall) schedule(cse506,fall)
    SATISFIABLE

    Models       : 1+
    Calls        : 1
    Time         : 0.057s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
    CPU Time     : 0.053s

    --------------------------------------------
    End: query_clingo Execution time: 0.12 sec.   |  May-10-2024 07:43:41
    --------------------------------------------

Construct knowledge graph
---------------------------

To get started, perform the following:

.. code-block:: bash

    mkdir cse_courses

Now run the following command:

.. code-block:: bash

    ./src/schedule.py graph --major=cse --verbose --output=cse_courses/cse_courses

.. warning::

    This command will take a while to run, as it scrapes the course catalog for all CSE courses.

Once completed, the file ``cse_courses/cse_courses.json`` will contain the course information of all CSE courses.

Convert knowledge graph to knowledge base
--------------------------------------------------

Next, converting the JSON file (knowledge graph) to a clingo knowledge base of atoms and predicates can be performed by running the following command:

.. code-block:: bash

    ./src/schedule.py convert --json-file=cse_courses.json --clingo

This will create the file ``cse_courses/cse_courses.lp``.

Query knowledge base
---------------------

Finally, to generate a schedule, run the following command:

.. code-block:: bash

    ./src/schedule.py query --knowledge=cse_courses/cse_courses.lp --query=cse_reqs.lp --clingo

.. note::

    The file ``cse_reqs.lp`` contains the requirements for the CSE major, and is not created automatically (i.e. must be created manually).

.. warning::
    
    - If the query is not satisfiable, then a :py:class:`~src.clapi.clapi.ClingoSatistfiablityError` is raised.



