Quickstart
============

To get started, perform the following:

.. code-block:: bash

    mkdir cse_courses

Construct knowledge graph
---------------------------

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

    ./src/schedule.py convert -json-file=cse_courses.json --clingo

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



