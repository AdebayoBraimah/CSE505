Graph
--------

Creates a knowledge graph of Stony Brook's course catalog via an input knowledge base (as a URL).
The URL, if not specified, defaults to the Stony Brook University course catalog, located `here <https://prod.ps.stonybrook.edu/psc/csprodg/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?>`_.

.. warning::

    This command takes a while to run, as it scrapes the course catalog for all of the offered courses for the specified major.

.. code-block:: text
    
    usage: schedule.py graph [-h] [-o <FILE>] [-v] [-c] [-e] [-m <MAJOR>] [-u <URL>] [-w <WAIT_TIME>]
                            [--open-browser]
                            {graph,convert,query} ...

    positional arguments:
    {graph,convert,query}                             Type the 'subcommand' name followed by '-h' or '
                                                        --help' for more information.
        graph                                           Creates knowledge graph of Stony Brook's course
                                                        catalogue via an input knowledge base (as a
                                                        URL).
        convert                                         Convert knowledge graph JSON to logic file
                                                        knowledge graph/base.
        query                                           Executes queries provided a knowledge
                                                        base/graph.

    options:
    -h, --help                                        show this help message and exit
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
    -m <MAJOR>, --major <MAJOR>                       REQUIRED: SBU major three letter code (e.g.
                                                        'CSE' for computer science).
    -u <URL>, --url <URL>                             OPTIONAL: Stony brook Univiersity (SBU) course
                                                        catalogue (knowledge base) URL. If not provided,
                                                        then the default URL is used.
    -w <WAIT_TIME>, --wait-time <WAIT_TIME>           OPTIONAL: Maximum wait time (in seconds) for
                                                        each click operation. Defaults to 10.
    --open-browser                                    OPTIONAL: Open browser during course catalog
                                                        scraping.
