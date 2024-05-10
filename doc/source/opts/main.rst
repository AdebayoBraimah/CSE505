Main menu
--------------

The main menu is the entry point for the command line interface (CLI) for this project. 
The main menu is the main argument parser for the project, and has three subcommands: ``graph``, ``convert``, and ``query``. 
Each subcommand has its own argument parser. 
The main menu has the following arguments:

.. code-block:: text
    
    usage: schedule.py [-h] [-o <FILE>] [-v] [-c] [-e] {graph,convert,query} ...

    Command line interface (CLI) argument parser module for this project.

    options:
    -h, --help                                        show this help message and exit

    subcommands:
    Data procurement, preprocessing and querying pipeline sections.

    {graph,convert,query}                             Type the 'subcommand' name followed by '-h' or '
                                                        --help' for more information.
        graph                                           Creates knowledge graph of Stony Brook's course
                                                        catalogue via an input knowledge base (as a
                                                        URL).
        convert                                         Convert knowledge graph JSON to logic file
                                                        knowledge graph/base.
        query                                           Executes queries provided a knowledge
                                                        base/graph.

    Main Arguments:
    -o <FILE>, --output <FILE>, --output-file <FILE>  OPTIONAL: Output filename for the JSON/logic
                                                        file. If not specified, then a new file with the
                                                        major in the filename is created in the
                                                        package's resource directory.
    -v, --verbose                                     OPTIONAL: Print output to screen.
    -c, --clingo                                      OPTIONAL: Convert JSON file to Clingo logic
                                                        file. NOTE: Both or at least one of '--clingo'
                                                        or '--ergo' must be specified for JSON
                                                        conversion. Use Clingo to execute the query.
                                                        NOTE: At least one of '--clingo' or '--ergo'
                                                        must be specified for query execution.
    -e, --ergo, --ergoai                              OPTIONAL: Convert JSON file to ErgoAI logic
                                                        file. NOTE: Both or at least one of '--clingo'
                                                        or '--ergo' must be specified for JSON
                                                        conversion. WARNING: Ergo conversion can only be
                                                        done once per python session. NOTE: At least one
                                                        of '--clingo' or '--ergo' must be specified for
                                                        query execution. DANGER: ErgoAI query execution
                                                        is not fully supported.


.. danger::

    - While ``--ergo`` is an option, it is not fully supported, especially for query execution.
