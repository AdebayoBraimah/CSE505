"""Convert course data JSON to a logic language file (as a knowledge graph).

.. autosummary::
    :nosignatures:

    convert_course_data_to_clingo
    convert_course_data_to_ergo
"""

from typing import List, Optional, Union, Tuple

from src.clapi.clapi import process_course_data_clingo
from src.ergoai.ergoai import json_to_ergo
from src.kg.knowledge_graph import KnowledgeGraph, KnowledgeBase
from src.utils.util import timeit


# @timeit
def convert_course_data(
    json_file: Union[KnowledgeBase, KnowledgeGraph, str],
    output_file: str = None,
    repeatable_courses: List[Tuple[str, str, str]] = None,
    method="clingo",
) -> str:
    """Converts a JSON file to a logic language file (``Clingo`` or ``ErgoAI``).

    Args:
        json_file: Input JSON file (:py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be converted to a logic language file.
        output_file: Output filename. If not specified, then a new file of the same name is created, with a '.lp' or '.ergo' file extension. Defaults to None.
        repeatable_courses: List of tuples of other courses that are repeatable. Each tuple should have exactly 3 elements: course_id, times_repeatable, max_credits. Defaults to None.
        method: Method to use for converting/preprocessing data. Input should be either "``clingo``" or "``ergoai``" Defaults to "clingo".

    Raises:
        ValueError: If the input method is not supported.

    Returns:
        Output knowledge base file path.
    """
    if method == "clingo":
        return convert_course_data_to_clingo(
            json_file=json_file,
            output_file=output_file,
            repeatable_courses=repeatable_courses,
        )
    elif (method == "ergoai") or (method == "ergo"):
        return convert_course_data_to_ergo(json_file=json_file, output_file=output_file)
    else:
        raise ValueError(f"Method '{method}' is not supported.")


# @timeit
def convert_course_data_to_clingo(
    json_file: Union[KnowledgeBase, KnowledgeGraph, str],
    output_file: str = None,
    repeatable_courses: List[Tuple[str, str, str]] = None,
) -> str:
    """Converts a JSON file to a Clingo file.

    Usage example:
        >>> from src.scheduler.convert import convert_course_data_to_clingo
        >>> clingo_file = convert_course_data_to_clingo("cse_courses.json")
        >>> print(clingo_file)
        cse_courses.lp

    Args:
        json_file: Input JSON file (:py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be converted to Clingo file.
        output_file: Output filename. If not specified, then a new file of the same name is created, with a '.lp' file extension. Defaults to None.
        repeatable_courses: List of tuples of other courses that are repeatable. Each tuple should have exactly 3 elements: course_id, times_repeatable, max_credits. Defaults to None.

    Returns:
        Output Clingo knowledge base file path.
    """
    clingo_file: str = process_course_data_clingo(
        json_file=json_file,
        output_file=output_file,
        repeatable_courses=repeatable_courses,
    )
    return clingo_file


# @timeit
def convert_course_data_to_ergo(
    json_file: Union[KnowledgeBase, KnowledgeGraph, str],
    output_file: Optional[str] = None,
) -> str:
    """Converts a JSON file to an ERGO file.

    NOTE:
        - If a JSON file needs to be converted to an ERGO file, this function MUST be called first before calling :py:func:`~src.ergoai.ergoai.query_ergoai`.
        - If a :py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object is passed, then the object is updated with the ERGO file path.

    WARNING:
        - This function can only be once per session. If you need to convert multiple JSON files to ERGO files, you must start a new session each time, otherwise the current session will crash.

    Usage example:
        >>> from src.scheduler.convert import convert_course_data_to_ergo
        >>> ergo_file = convert_course_data_to_ergo("cse_courses.json")
        >>> print(ergo_file)
        cse_courses.ergo

    Args:
        json_file: Input JSON file (:py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be converted to ERGO file.
        output_file: output_file: Output filename. If not specified, then a new file of the same name is created, with a '.ergo' file extension. Defaults to None.

    Returns:
        Path to the output ERGO file.
    """
    ergo_file: str = json_to_ergo(json_file=json_file, output_file=output_file)
    return ergo_file
