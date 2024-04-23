"""Clingo API module for organizing and processing course data.

.. autosummary::
    :nosignatures:

    process_course_data_clingo
    append_rules
    query_clingo
"""

import json
import sys
import shlex
import subprocess

from typing import List, Union

from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph
from src.utils.util import DependencyError, check_dependencies


def process_course_data_clingo(
    file_path: Union[KnowledgeBase, KnowledgeGraph, str], file_name: str = None
) -> Union[str, KnowledgeBase, KnowledgeGraph]:
    """Converts a JSON file data to a Clingo.

    NOTE:
        - If a ``KnowledgeBase`` or ``KnowledgeGraph`` object is passed, then the Clingo filepath is updated in the object.

    Args:
        file_path: Input JSON file (or ``KnowledgeBase`` or ``KnowledgeGraph`` object) to be converted to ERGO file.
        file_name: Output filename. If not specified, then a new file of the same name is created, with an '.lp' file extension.

    Returns:
        Output clingo knowledge base/graph file path.
    """
    # Load JSON data from the file
    if (isinstance(file_path, KnowledgeBase)) or (
        isinstance(file_path, KnowledgeGraph)
    ):
        kg: Union[KnowledgeBase, KnowledgeGraph] = file_path
        file_path: str = kg.json

    if output_file is None:
        output_file = file_path.replace(".json", ".lp")

    with open(file_path, "r") as file:
        data = json.load(file)

    courses_list = []
    prerequisites_list = []

    # Process each course in the JSON data
    for course_code, details in data.items():
        # Extract course information
        course_name = course_code  # Simplified as the key
        try:
            credits = (
                int(details["Credits"])
                if isinstance(details["Credits"], (float, int))
                else 3
            )  # Assuming default 3 if not clear
        except ValueError:
            continue
        prerequisites = details.get("Prerequisites", [])

        # Print course information
        # print(f"course({course_name.lower()}, {credits}).")

        courses_list.append(f"course({course_name.lower()}, {credits}).")

        # Process and print prerequisites
        if prerequisites != "NONE" and isinstance(prerequisites, list):
            for prereq_list in prerequisites:
                for prereq in prereq_list:
                    # Format and clean prerequisite course code
                    prereq_code = prereq.replace(" ", "").upper()
                    # print(f"prerequisite({course_name.lower()}, {prereq_code.lower()}).")
                    if "cs" in prereq_code.lower():
                        if prereq_code.lower() < course_name.lower():
                            prerequisites_list.append(
                                f"prerequisite({course_name.lower()}, {prereq_code.lower()})."
                            )
                        # prerequisites_list.append(f"prerequisite({course_name.lower()}, {prereq_code.lower()}).")

    output = courses_list + prerequisites_list
    _write_list_to_file(output, file_name)

    if kg:
        kg.lp = file_name

    return output


def _write_list_to_file(data_list, filename):
    with open(filename, "w") as file:
        for item in data_list:
            file.write(item + "\n")


def append_rules(file_list: List[str], output_file: str) -> str:
    """Appends the contents of multiple files into a single output file.
    Intended for use with Clingo ``.lp`` files.

    Args:
        file_list: Input list of files to be appended.
        output_file: New file to be created with the appended contents.

    Returns:
        Path to the output file.
    """
    try:
        # Open the output file in write mode (this will overwrite existing file)
        with open(output_file, "w") as outfile:
            # Iterate over the list of files
            for file_name in file_list:
                # Open each file in read mode
                with open(file_name, "r") as infile:
                    # Read the content of the file
                    content = infile.read()
                    # Write the content to the output file
                    outfile.write(content)
                    # Optionally add a newline between contents of different files
                    outfile.write("\n")
        # print(f"Contents appended successfully into {output_file}.")
        return output_file
    except Exception as e:
        print(f"An error occurred: {e}")


def query_clingo(
    knowledge: Union[KnowledgeBase, KnowledgeGraph, str], verbose: bool = False
) -> str:
    """Queries a Clingo knowledge base/graph file using a given query.

    WARNING:
        - This function assumes that ``clingo`` is installed and is accessible via the system path variable.

    NOTE:
        - The query must be included in the Clingo file.

    Args:
        knowledge: Input Clingo knowledge base/graph file (or ``KnowledgeBase`` or ``KnowledgeGraph`` object) to be queried.
        verbose: Prints verbose output if set to ``True``. Defaults to ``False``.

    Returns:
        Query results.
    """
    # Check if Clingo is installed
    try:
        check_dependencies(dependencies=("clingo",))
    except DependencyError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Set verbose option if specified
    if verbose:
        cmd_opt: str = "-V"
    else:
        cmd_opt: str = ""

    # Start Clingo session
    proc = subprocess.Popen(
        shlex.split(s=f"clingo {cmd_opt} {knowledge}"), stdout=subprocess.PIPE
    )

    output = proc.stdout.read().decode("utf-8")

    return output
