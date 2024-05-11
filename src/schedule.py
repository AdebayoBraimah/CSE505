#!/usr/bin/env python3
"""Stony Brook University course scheduling module.

At the moment, this module mainly supports CSE majors.

.. autosummary::
    :nosignatures:

    main
"""
import os
import sys

from typing import Any, Dict, Iterable, List, Tuple

# Add project root to the Python path
_PKG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_PKG_PATH)

# Import project modules
from src.cli.parser import arg_parser
from src.scheduler import download, convert, query as qry


def main() -> None:
    """Main function for the course scheduling module.

    Raises:
        ValueError: Arises if method is not ``download``, ``convert``, or ``query``, or if required arguments are not provided.

    Returns:
        None
    """
    parser = arg_parser()
    args = parser.parse_args()

    # Print help message in the case of no arguments
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        args: Dict[str, Any] = vars(args)

    # Get variable names
    method: str = args.get("method")

    # Download
    url: str = args.get("url")
    major: str = args.get("major")
    output: str = args.get("output")  # appears in download and convert
    wait_time: int = args.get("wait_time")
    headless: bool = args.get("headless")
    verbose: bool = args.get("verbose")

    # Convert
    json_file: str = args.get("json_file")
    clingo: bool = args.get("clingo")  # appears in convert and query
    ergoai: bool = args.get("ergoai")  # appears in convert and query

    # Query
    knowledge: str = args.get("knowledge")
    num_models: int = args.get("num_models")
    config: str = args.get("configuration")
    parallel_mode: int = args.get("parallel_mode")
    query: Iterable[str] = _flatten_nested_list_to_tuple(args.get("query"))

    # Perform actions
    if method == "graph":
        if (not url) or (not major):
            raise ValueError("URL and major are required for downloading course data.")
        download.procure_course_data(
            url=url,
            major=major,
            output=output,
            headless=headless,
            verbose=verbose,
            wait_time=wait_time,
        )
    elif method == "convert":
        if (not json_file) or ((not clingo) and (not ergoai)):
            raise ValueError(
                "JSON file and conversion method are required for converting course data."
            )
        if clingo:
            convert.convert_course_data(
                json_file=json_file,
                output_file=output,
                method="clingo",
            )
        if ergoai:
            convert.convert_course_data(
                json_file=json_file,
                output_file=output,
                method="ergoai",
            )
    elif method == "query":
        if (not knowledge) or ((not clingo) and (not ergoai)):
            raise ValueError(
                "Knowledge base and execution method are required for querying course data."
            )
        if clingo:
            qry.query(
                knowledge=knowledge,
                method="clingo",
                verbose=verbose,
                num_models=num_models,
                configuration=config,
                parallel_mode=parallel_mode,
                query=query,
            )
        elif ergoai:
            qry.query(
                knowledge=knowledge,
                method="ergoai",
                query=query,
            )
    else:
        raise ValueError(f"Method '{method}' is not supported.")
    return None


def _flatten_nested_list_to_tuple(nested_list: List[List[str]]) -> Tuple[str]:
    """Flatten a nested list and convert it to a tuple.

    Args:
        nested_list: Nested list to be flattened.

    Returns:
        Flattened tuple.
    """
    result: List[str] = []

    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                flatten(item)
            else:
                result.append(item)

    flatten(nested_list)
    return tuple(result)


# Call main function
if __name__ == "__main__":
    main()
