"""Command line interface (CLI) argument parser module for this project.

.. autosummary::
    :nosignatures:

    arg_parser
"""

import argparse


# TODO:
#   - Fill out the argument parser
#   - Add clingo output formatter
#   - Figure out way to display options for each subcommand in sphinx documentation
def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
    )

    # Parse Arguments

    mainargparser = parser.add_subparsers(
        title="subcommands",
        description="Data procurement, preprocessing and querying pipeline sections.",
        help="Type the 'subcommand' name followed by '-h' or '--help' for more information.",
    )

    # Main options
    mainoptions = parser.add_argument_group("Main Arguments")

    mainoptions.add_argument(
        "-o",
        "--output",
        "--output-file",
        type=str,
        metavar="<FILE>",
        dest="output",
        default=None,
        help="OPTIONAL: Output filename for the JSON/logic file. If not specified, then a new file with the major in the filename is created in the package's resource directory.",
    )

    mainoptions.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="OPTIONAL: Print output to screen.",
    )

    mainoptions.add_argument(
        "-c",
        "--clingo",
        action="store_true",
        dest="clingo",
        default=False,
        help="OPTIONAL: Convert JSON file to Clingo logic file. NOTE: Both or at least one of '--clingo' or '--ergo' must be specified for JSON conversion. Use Clingo to execute the query. NOTE: At least one of '--clingo' or '--ergo' must be specified for query execution.",
    )

    mainoptions.add_argument(
        "-e",
        "--ergo",
        "--ergoai",
        action="store_true",
        dest="ergoai",
        default=False,
        help="OPTIONAL: Convert JSON file to ErgoAI logic file. NOTE: Both or at least one of '--clingo' or '--ergo' must be specified for JSON conversion. WARNING: Ergo conversion can only be done once per python session. NOTE: At least one of '--clingo' or '--ergo' must be specified for query execution. DANGER: ErgoAI query execution is not fully supported.",
    )

    # Graph construction options
    graphoptions = mainargparser.add_parser(
        "graph",
        parents=[mainoptions],
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
        add_help=False,
        help="Creates knowledge graph of Stony Brook's course catalogue via an input knowledge base (as a URL).",
    )

    graphoptions.add_argument(
        "-m",
        "--major",
        type=str,
        metavar="<MAJOR>",
        dest="major",
        default=None,
        help="REQUIRED: SBU major three letter code (e.g. 'CSE' for computer science).",
    )

    # Define constants
    _COURSE_CATALOG_URL: str = (
        "https://prod.ps.stonybrook.edu/psc/csprodg/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?"
    )

    graphoptions.add_argument(
        "-u",
        "--url",
        type=str,
        metavar="<URL>",
        dest="url",
        default=_COURSE_CATALOG_URL,
        help="OPTIONAL: Stony brook Univiersity (SBU) course catalogue (knowledge base) URL. If not provided, then the default URL is used.",
    )

    graphoptions.add_argument(
        "-w",
        "--wait-time",
        type=int,
        metavar="<WAIT_TIME>",
        dest="wait_time",
        default=10,
        help="OPTIONAL: Maximum wait time (in seconds) for each click operation. Defaults to 10.",
    )

    graphoptions.add_argument(
        "--open-browser",
        action="store_false",
        dest="headless",
        default=True,
        help="OPTIONAL: Open browser during course catalog scraping.",
    )

    graphoptions.set_defaults(method="graph")

    # Graph conversion options JSON -> Clingo/ERGO
    convertoptions = mainargparser.add_parser(
        "convert",
        parents=[mainoptions],
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
        add_help=False,
        help="Convert knowledge graph JSON to logic file knowledge graph/base.",
    )

    convertoptions.add_argument(
        "-j",
        "--json",
        "--json-file",
        type=str,
        metavar="<FILE>",
        dest="json_file",
        default=None,
        help="REQUIRED: Input JSON file containing course information.",
    )

    convertoptions.set_defaults(method="convert")

    # Query options
    queryoptions = mainargparser.add_parser(
        "query",
        parents=[mainoptions],
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
        add_help=False,
        help="Executes queries provided a knowledge base/graph.",
    )

    queryoptions.add_argument(
        "-k",
        "--knowledge",
        type=str,
        metavar="<FILE>",
        dest="knowledge",
        default=None,
        help="OPTIONAL: Input knowledge base/graph file to be queried. NOTE: If using Clingo, the query can be in the knowlege base file.",
    )

    queryoptions.add_argument(
        "-n",
        "--num-models",
        type=int,
        metavar="<MODEL>",
        dest="num_models",
        default=None,
        help="OPTIONAL: Number of models to generate for Clingo queries. Defaults to None.",
    )

    queryoptions.add_argument(
        "-t",
        "--num-threads",
        type=int,
        metavar="<THREADS>",
        dest="parallel_mode",
        default=None,
        help="OPTIONAL: Maxiumu number of threads to use while executing Clingo queries. Defaults to None.",
    )

    queryoptions.add_argument(
        "--config",
        type=str,
        metavar="<STR>",
        dest="configuration",
        default="handy",
        help="OPTIONAL: Configuration for Clingo queries. Options are 'handy' or 'competition'. Further explanations of these options can be obtained by typing: 'clingo --help=3'  Defaults to 'handy'.",
    )

    queryoptions.add_argument(
        "-q",
        "--query",
        type=str,
        metavar="<FILE | STR>",
        dest="query",
        default=None,
        action="append",
        nargs="+",
        help="OPTIONAL: Query or query file paths to be passed to Clingo or ErgoAI. Clingo can take multiple input files. ErgoAI can only take string inputs. \nNOTE: Can be specified multiple times.",
    )

    queryoptions.set_defaults(method="query")

    return parser
