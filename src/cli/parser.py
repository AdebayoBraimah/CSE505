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

    graphoptions = mainargparser.add_parser(
        "graph",
        # parents=[reqoptions],
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
        add_help=False,
        help="Creates knowledge graph of Stony Brook's course catalogue via an input knowledge base (as a URL).",
    )

    convertoptions = mainargparser.add_parser(
        "convert",
        # parents=[reqoptions],
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
        add_help=False,
        help="Convert knowledge graph JSON to logic file knowledge graph/base.",
    )

    queryoptions = mainargparser.add_parser(
        "query",
        # parents=[reqoptions],
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
        add_help=False,
        help="Executes queries provided a knowledge base/graph.",
    )

    return parser
