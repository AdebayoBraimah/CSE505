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

# TODO:
#   - Repeatable classes - Use course description to create separate file of atoms of repeatable classes,
#       including how many times can be repeated, and/or for up to how many credits.


def process_course_data_clingo(
    file_path: Union[KnowledgeBase, KnowledgeGraph, str], output_file: str = None
) -> str:
    """Converts a JSON file data to a Clingo.

    NOTE:
        - If a ``KnowledgeBase`` or ``KnowledgeGraph`` object is passed, then the Clingo filepath is updated in the object.

    Args:
        file_path: Input JSON file (or ``KnowledgeBase`` or ``KnowledgeGraph`` object) to be converted to ERGO file.
        output_file: Output filename. If not specified, then a new file of the same name is created, with an '.lp' file extension.

    Returns:
        Output clingo knowledge base/graph file path.
    """
    # Load JSON data from the file
    if (isinstance(file_path, KnowledgeBase)) or (
        isinstance(file_path, KnowledgeGraph)
    ):
        kg: Union[KnowledgeBase, KnowledgeGraph] = file_path
        file_path: str = kg.json
    else:
        kg: Union[KnowledgeBase, KnowledgeGraph] = None

    if output_file is None:
        output_file = file_path.replace(".json", ".lp")

    with open(file_path, "r") as file:
        data = json.load(file)

    courses_list = []
    prerequisites_list = []
    antirequisites_list = []

    # Process each course in the JSON data
    for course_code, details in data.items():
        # Extract course information
        course_name = course_code  # Simplified as the key

        credits = (
            int(details.get("Credits"))
            if isinstance(details.get("Credits"), (float, int))
            else _translate_range(details.get("Credits"))
        )
        prerequisites = details.get("Prerequisites", [])
        antirequisites = details.get("Antirequisites", [])

        # NOTE: Career must be quoted to avoid issues with Clingo
        #   in the future, the career should be defined as its own atom
        courses_list.append(
            f"course({course_name.lower()}, {credits}, \"{details.get('Career')}\", {int(details.get('spring1'))}, {int(details.get('fall1'))}, {int(details.get('spring2'))}, {int(details.get('fall2'))})."
        )
        # TODO: process corequisites
        # Process prerequisites
        if prerequisites != "NONE" and isinstance(prerequisites, list):
            for prereq_list in prerequisites:
                for prereq in prereq_list:
                    # Format and clean prerequisite course code
                    prereq_code = prereq.replace(" ", "").upper()
                    prerequisites_list.append(
                        f"prerequisite({course_name.lower()}, {prereq_code.lower()})."
                    )

        # Process antirequisites
        if antirequisites != "NONE" and isinstance(antirequisites, list):
            for antireq_list in antirequisites:
                for antireq in antireq_list:
                    # Format and clean prerequisite course code
                    antireq_code = antireq.replace(" ", "").upper()
                    antirequisites_list.append(
                        f"antirequisite({course_name.lower()}, {antireq_code.lower()})."
                    )
    output = courses_list + prerequisites_list + antirequisites_list
    _write_list_to_file(output, output_file)

    if kg:
        kg.lp = output_file

    return output_file


def _translate_range(input_string: str) -> str:
    # Split the string using ' - ' to separate the numbers
    parts = input_string.split(" - ")

    # Extract the integer part of each number by splitting on '.' and taking the first part
    start = parts[0].split(".")[0]
    end = parts[1].split(".")[0]

    # Concatenate with '..' for clingo
    result = start + ".." + end

    return result


def _write_list_to_file(data_list: List[str], filename: str) -> None:
    with open(filename, "w") as file:
        for item in data_list:
            file.write(item + "\n")
    return None


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


def process_honors_courses(file_path: str, outfile: str = None) -> None:
    """Processes (CSE) honors courses from a JSON file and writes them to a clingo file in the form: ``cse_honors(course_id)``.

    Usage example:
        >>> process_honors_courses(file_path="cse_courses.json")

    Args:
        file_path: Path to the JSON file containing course data.
        outfile: Output filename. If not specified, then the output file will just have '_honors.lp' appended to the input filename. Defaults to None.

    Returns:
        None.
    """
    # Load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)

    course_list: List[str] = []

    if outfile is None:
        outfile = file_path.replace(".json", "_honors.lp")

    # Iterate over each course
    for course_id, course_details in data.items():
        # Check if 'honors' is in the description
        if "honors" in course_details.get("Description", "").lower():
            course_list.append(f"cse_honors({course_id}).")

    # Write the list to a file
    _write_list_to_file(data_list=course_list, filename=outfile)

    return None
