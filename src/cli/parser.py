"""Command line interface (CLI) argument parser module for this project.

.. autosummary::
    :nosignatures:

    arg_parser
"""

import os
import sys
import argparse


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

    return parser
