"""Clingo API module for organizing and processing course data.

.. autosummary::
    :nosignatures:

    process_course_data_clingo
    translate_range
    append_rules
    query_clingo
    process_honors_courses
    process_repeatable_courses
"""

import re
import json
import sys
import shlex
import subprocess

from typing import Any, Dict, Iterable, List, Union, Tuple

from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph
from src.utils.util import DependencyError, check_dependencies


class ClingoSatistfiablityError(Exception):
    """Exception raised when Clingo returns ``UNSATISFIABLE``."""

    pass


class ClingoSyntaxError(Exception):
    """Exception raised when there is a parsing/syntax error in the Clingo file."""

    pass


# TODO: Clingo -- Remove semester offering information, and see if that helps.
def process_course_data_clingo(
    json_file: Union[KnowledgeBase, KnowledgeGraph, str],
    output_file: str = None,
    repeatable_courses: List[Tuple[str, str, str]] = None,
) -> str:
    """Converts a JSON file data to a Clingo.
    This function processes course data from a JSON file and writes it to a Clingo file in the form:
    ``course(course_id, credits, career, spring1, fall1, spring2, fall2).``

    The corresponding rules for antirequisites, prerequisites, and corequisites are also generated if present, and are of the form:
        - Antirequisites:
            ``:- course(course_id, _, career, _, _, _, _), course(antireq_id, _, career, _, _, _, _).``
        - Prerequisites:
            ``:- course(course_id, _, career, _, _, _, _), not course(prereq_id, _, career, _, _, _, _).``
        - Corequisites:
            ``:- course(course_id, _, career, _, _, _, _), not course(coreq_id, _, career, _, _, _, _).``

    NOTE:
        - If a :py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object is passed, then the Clingo output filepath is updated in the object.

    Usage example:
        >>> clingo_file = process_course_data_clingo(json_file="course_data.json")

    Args:
        json_file: Input JSON file (or :py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be converted to Clingo.
        output_file: Output filename. If not specified, then a new file of the same name is created, with an '.lp' file extension. Defaults to None.
        repeatable_courses: List of tuples of other courses that are repeatable. Each tuple should have exactly 3 elements: course_id, times_repeatable, max_credits. Defaults to None.

    Returns:
        Output Clingo knowledge base file path.
    """
    # Load JSON data from the file
    if (isinstance(json_file, KnowledgeBase)) or (
        isinstance(json_file, KnowledgeGraph)
    ):
        kg: Union[KnowledgeBase, KnowledgeGraph] = json_file
        json_file: str = kg.json
    else:
        kg: Union[KnowledgeBase, KnowledgeGraph] = None

    if output_file is None:
        output_file: str = json_file.replace(".json", ".lp")

    with open(json_file, "r") as file:
        data: Dict[Dict[str, Any]] = json.load(file)

    predicates: List[str] = []
    rules: List[str] = []

    for course_id, course_info in data.items():
        # Generate course predicates
        # offered_spring1 = int(course_info["spring1"])
        # offered_fall1 = int(course_info["fall1"])
        # offered_spring2 = int(course_info["spring2"])
        # offered_fall2 = int(course_info["fall2"])

        offered_spring: int = int(course_info.get("spring"))
        offered_fall: int = int(course_info.get("fall"))

        credits: Union[float, int] = (
            int(course_info.get("Credits"))
            if isinstance(course_info.get("Credits"), (float, int))
            else translate_range(course_info.get("Credits"))
        )

        career: str = course_info.get("Career")

        predicates.append(
            # f'course({course_id.lower()}, {credits}, "{career}", {offered_spring1}, {offered_fall1}, {offered_spring2}, {offered_fall2}).'
            f'course({course_id.lower()}, {credits}, "{career}", {offered_spring}, {offered_fall}).'
            # f'course({course_id.lower()}, {credits}, "{career}").'
        )

        # Generate antirequisite rules
        if course_info.get("Antirequisites") != "NONE":
            rules.append(f"% Antirequisites for {course_id.upper()}")
            for antireq_group in course_info.get("Antirequisites"):
                for antireq in antireq_group:
                    rules.append(
                        # f':- course({course_id.lower()}, {credits}, "{career}", {offered_spring1}, {offered_fall1}, {offered_spring2}, {offered_fall2}), \n   course({antireq.lower()}, _, "{career}", _, _, _, _). \n'
                        f':- course({course_id.lower()}, {credits}, "{career}", {offered_spring}, {offered_fall}), \n   course({antireq.lower()}, _, "{career}", _, _). \n'
                        # f':- course({course_id.lower()}, {credits}, "{career}"), \n   course({antireq.lower()}, _, "{career}"). \n'
                    )

        # Generate prerequisite rules
        if course_info.get("Prerequisites") != "NONE":
            rules.append(f"% Prerequisites for {course_id.upper()}")
            for prereq_group in course_info.get("Prerequisites"):
                group_conditions = ", ".join(
                    [
                        # f'\n   not course({prereq.lower()}, _, "{career}", _, _, _, _)'
                        f'\n   not course({prereq.lower()}, _, "{career}", _, _)'
                        # f'\n   not course({prereq.lower()}, _, "{career}")'
                        for prereq in prereq_group
                    ]
                )
                rules.append(
                    # f':- course({course_id.lower()}, {credits}, "{career}", {offered_spring1}, {offered_fall1}, {offered_spring2}, {offered_fall2}), {group_conditions}. \n'
                    f':- course({course_id.lower()}, {credits}, "{career}", {offered_spring}, {offered_fall}), {group_conditions}. \n'
                    # f':- course({course_id.lower()}, {credits}, "{career}"), {group_conditions}. \n'
                )

        # Generate corequisite rules
        if course_info.get("Corequisites") != "NONE":
            rules.append(f"% Corequisites for {course_id.upper()}")
            for coreq_group in course_info.get("Corequisites"):
                for coreq in coreq_group:
                    rules.append(
                        # f':- course({course_id.lower()}, {credits}, "{career}", {offered_spring1}, {offered_fall1}, {offered_spring2}, {offered_fall2}), \n   not course({coreq.lower()}, _, "{career}", {offered_spring1}, {offered_fall1}, {offered_spring2}, {offered_fall2}). \n'
                        f':- course({course_id.lower()}, {credits}, "{career}", {offered_spring}, {offered_fall}), \n   not course({coreq.lower()}, _, "{career}", {offered_spring}, {offered_fall}). \n'
                        # f':- course({course_id.lower()}, {credits}, "{career}"), \n   not course({coreq.lower()}, _, "{career}"). \n'
                    )

    # Process honors courses
    honors: List[str] = process_honors_courses(file_path=json_file)

    if honors:
        honors.insert(0, "\n% Honors Courses")

    # TODO: Uncomment this later
    # # Process repeatable courses
    # repeatable: List[str] = process_repeatable_courses(
    #     json_file=json_file, other_courses=repeatable_courses
    # )

    # if repeatable:
    #     repeatable.insert(0, "\n% Repeatable Courses")

    # Write predicates and rules to file
    output = (
        ["% Course atoms"]
        + predicates
        + honors
        # + repeatable
        + ["\n% Course Rules \n"]
        + rules
    )
    _write_list_to_file(output, output_file)

    if kg:
        kg.lp = output_file

    return output_file


def translate_range(input_string: str) -> str:
    """Converts a range of numbers in a string to a Clingo-compatible format.

    Usage example:
        >>> translate_range("0 - 9")
        '0..9'

    Args:
        input_string: Input string containing a range of numbers (e.g. 0 - 9).

    Returns:
        Clingo-compatible range format (e.g. 0..9).
    """
    # Split the string using ' - ' to separate the numbers
    parts = input_string.split(" - ")

    # Extract the integer part of each number by splitting on '.' and taking the first part
    start = parts[0].split(".")[0]
    end = parts[1].split(".")[0]

    # Concatenate with '..' for clingo
    result = start + ".." + end

    return result


def _write_list_to_file(data_list: List[str], filename: str) -> None:
    """Writes a list of data (strings) to a file.

    Args:
        data_list: Input list of data to be written to the file.
        filename: Output filename.

    Returns:
        None
    """
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
    knowledge: Union[KnowledgeBase, KnowledgeGraph, str],
    verbose: bool = False,
    num_models: int = None,
    configuration: str = "handy",
    parallel_mode: int = None,
) -> str:
    """Queries a Clingo knowledge base/graph file using a given query.

    WARNING:
        - This function assumes that ``clingo`` is installed and is accessible via the system path variable.

    NOTE:
        - The query must be included in the Clingo file.

    Args:
        knowledge: Input Clingo knowledge base/graph file (or :py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be queried.
        verbose: Prints verbose output if set to ``True``. Defaults to ``False``.
        num_models: Number of models to generate. Defaults to None.
        configuration: Clingo configuration. Defaults to "handy".
        parallel_mode: Parallel mode, maximum number of threads. Defaults to None.

    Returns:
        Query results.

    Raises:
        ClingoSatistfiablityError: If the query returns ``UNSATISFIABLE``.
        ClingoSyntaxError: If there is a parsing/syntax error in the Clingo file.
        DependencyError: If Clingo is not installed or added to the system path variable.
    """
    # Check if Clingo is installed
    try:
        check_dependencies(dependencies=("clingo",))
    except DependencyError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Check if the input is a KnowledgeBase or KnowledgeGraph object
    if (isinstance(knowledge, KnowledgeBase)) or (
        isinstance(knowledge, KnowledgeGraph)
    ):
        kg: Union[KnowledgeBase, KnowledgeGraph] = knowledge
        knowledge: str = kg.lp
    else:
        kg: Union[KnowledgeBase, KnowledgeGraph] = None

    # Set configuration options
    if verbose:
        cmd_opt: str = "-V"
    else:
        cmd_opt: str = ""

    if num_models is not None:
        cmd_opt += f"-n {num_models}"

    if parallel_mode is not None:
        cmd_opt += f"--parallel-mode {parallel_mode}"

    if configuration is not None:
        cmd_opt += f"--configuration={configuration}"

    # Start Clingo session
    proc = subprocess.Popen(
        shlex.split(s=f"clingo {cmd_opt} {knowledge}"), stdout=subprocess.PIPE
    )

    output = proc.stdout.read().decode("utf-8")

    # Check if the output contains 'UNSATISFIABLE'
    if "UNSATISFIABLE" in output:
        raise ClingoSatistfiablityError("The query returned UNSATISFIABLE.")
    elif "ERROR" in output:
        raise ClingoSyntaxError("There was a parsing/syntax error in the Clingo file.")

    return output


def process_honors_courses(file_path: str) -> List[str]:
    """Processes honors courses from a JSON file and writes them to a list in the form: ``honors(course_id)``.

    NOTE:
        - Mainly intended for use with SBU CSE courses.

    Usage example:
        >>> process_honors_courses(file_path="cse_courses.json")

    Args:
        file_path: Path to the JSON file containing course data.

    Returns:
        List of honors courses.
    """
    # Load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)

    course_list: List[str] = []

    # Iterate over each course
    for course_id, course_details in data.items():
        # Check if 'honors' is in the description
        if ("honors" in course_details.get("CourseTitle", "").lower()) or (
            ("honors" in course_details.get("Description", "").lower())
        ):
            course_list.append(f"honors({course_id.lower()}).")
    return course_list


# TODO:
#
# The repeatable atom should have all info, no '_'.
# e.g. repeatable(cse593, 6, 12).
def process_repeatable_courses(
    json_file: str, other_courses: Iterable[Tuple[str, str, str]] = None
) -> List[str]:
    """Processes repeatable courses from a JSON file and writes them to a list in the form: ``repeatable(course_id, times_repeatable, max_credits)``.

    NOTE:
        - The input JSON file should contain course data.
        - The repeatable courses are identified based on the course description.
        - The function also accepts a list of other courses that are repeatable.

    Usage example:
        >>> process_repeatable_courses(json_file="course_data.json", other_courses=[("cse593", "_", "_")]
        ['repeatable(cse390, 2, _).',
         'repeatable(cse391, 2, _).',
         'repeatable(cse392, 2, _).',
         'repeatable(cse393, 2, _).',
         'repeatable(cse394, 2, _).',
         'repeatable(cse475, 2, _).',
         'repeatable(cse488, _, 12).',
         .
         .
         .
         'repeatable(cse593, _, _).',
         .
         .
         .
         'repeatable(cse693, 2, _).']

    Args:
        json_file: Input JSON file containing course data.
        other_courses: Iterable of tuples of other courses that are repeatable. Each tuple should have exactly 3 elements: course_id, times_repeatable, max_credits. Defaults to None.

    Raises:
        ValueError: If each course tuple does not have exactly 3 elements, or if any of the 2nd or 3rd elements of the tuple do not contain an integer or the string "_".

    Returns:
        List of repeatable courses.
    """
    with open(json_file, "r") as file:
        data: Dict[Dict[str, Any]] = json.load(file)

    atoms: List[str] = []

    # Add other repeatable courses
    if other_courses is not None:
        for course_info in other_courses:
            if not course_info[0].upper() in data.keys():
                print(f"Course {course_info[0]} not found in the JSON file.")
                continue
            if (
                (len(course_info) != 3)
                or (not _check_repeatable_input(course_info[1]))
                or (not _check_repeatable_input(course_info[2]))
            ):
                raise ValueError("Each course tuple should have exactly 3 elements.")
            atom = f"repeatable({course_info[0]}, {course_info[1]}, {course_info[2]})."
            atoms.append(atom)

    for course_id, course_info in data.items():
        description = course_info["Description"].lower()
        if ("repeat" in description) and (not course_id in atoms):
            times = "_"
            max_credits = "_"
            if "more than twice" in description:
                times = 2
            elif "repeated once" in description:
                times = 2
            elif "repeated twice" in description:
                times = 3
            elif ("credits" in description.lower()) and (
                _extract_credits(description) is not None
            ):
                max_credits = _extract_credits(description)
            else:
                # NOTE: Uncommenting the line below will set the default value of times to 2.
                #   This behavior may not be desired in all cases.
                # times: int = 2
                continue
            atom: str = f"repeatable({course_id.lower()}, {times}, {max_credits})."
            atoms.append(atom)

    # Sort the atoms
    atoms: List[str] = sorted(atoms)
    return atoms


def _extract_credits(description: str) -> int:
    """Helper function that extracts the number of credits from a course description.

    Args:
        description: Course description string.

    Returns:
        Number of credits.
    """
    # Search for one or more digits followed by the word 'credits'
    match = re.search(r"(\d+) credits", description)
    if match:
        # Return the number found
        return int(match.group(1))
    else:
        return None


def _check_repeatable_input(course_info: str) -> bool:
    """Helper function that checks if the input for repeatable courses is valid.
    Valid input is either an integer or the string "_".

    Args:
        course_info: Input course information.

    Returns:
        True if the input is valid, False otherwise.
    """
    try:
        int(course_info)
        return True
    except ValueError:
        if course_info == "_":
            return True
        else:
            return False
