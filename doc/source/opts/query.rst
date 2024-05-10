Query
--------

The ``query`` subcommand is used to execute queries provided a knowledge base/graph in either Clingo or ErgoAI. 

.. warning::
    
    - If the query is not satisfiable, then a :py:class:`~src.clapi.clapi.ClingoSatistfiablityError` is raised.


.. code-block:: text
    
    usage: schedule.py query [-h] [-o <FILE>] [-v] [-c] [-e] [-k <FILE>] [-n <MODEL>] [-t <THREADS>]
                            [--config <STR>] [-q <FILE | STR> [<FILE | STR> ...]]
                            {graph,convert,query} ...

    positional arguments:
    {graph,convert,query}                                Type the 'subcommand' name followed by '-h'
                                                        or '--help' for more information.
        graph                                              Creates knowledge graph of Stony Brook's
                                                        course catalogue via an input knowledge base
                                                        (as a URL).
        convert                                            Convert knowledge graph JSON to logic file
                                                        knowledge graph/base.
        query                                              Executes queries provided a knowledge
                                                        base/graph.

    options:
    -h, --help                                           show this help message and exit
    -o <FILE>, --output <FILE>, --output-file <FILE>     OPTIONAL: Output filename for the JSON/logic
                                                        file. If not specified, then a new file with
                                                        the major in the filename is created in the
                                                        package's resource directory.
    -v, --verbose                                        OPTIONAL: Print output to screen.
    -c, --clingo                                         OPTIONAL: Convert JSON file to Clingo logic
                                                        file. NOTE: Both or at least one of '--
                                                        clingo' or '--ergo' must be specified for
                                                        JSON conversion. Use Clingo to execute the
                                                        query. NOTE: At least one of '--clingo' or '
                                                        --ergo' must be specified for query
                                                        execution.
    -e, --ergo, --ergoai                                 OPTIONAL: Convert JSON file to ErgoAI logic
                                                        file. NOTE: Both or at least one of '--
                                                        clingo' or '--ergo' must be specified for
                                                        JSON conversion. WARNING: Ergo conversion can
                                                        only be done once per python session. NOTE:
                                                        At least one of '--clingo' or '--ergo' must
                                                        be specified for query execution. DANGER:
                                                        ErgoAI query execution is not fully
                                                        supported.
    -k <FILE>, --knowledge <FILE>                        OPTIONAL: Input knowledge base/graph file to
                                                        be queried. NOTE: If using Clingo, the query
                                                        can be in the knowlege base file.
    -n <MODEL>, --num-models <MODEL>                     OPTIONAL: Number of models to generate for
                                                        Clingo queries. Defaults to None.
    -t <THREADS>, --num-threads <THREADS>                OPTIONAL: Maxiumu number of threads to use
                                                        while executing Clingo queries. Defaults to
                                                        None.
    --config <STR>                                       OPTIONAL: Configuration for Clingo queries.
                                                        Options are 'handy' or 'competition'. Further
                                                        explanations of these options can be obtained
                                                        by typing: 'clingo --help=3' Defaults to
                                                        'handy'.
    -q <FILE | STR> [<FILE | STR> ...], --query <FILE | STR> [<FILE | STR> ...]
                                                        OPTIONAL: Query or query file paths to be
                                                        passed to Clingo or ErgoAI. Clingo can take
                                                        multiple input files. ErgoAI can only take
                                                        string inputs. NOTE: Can be specified
                                                        multiple times.
