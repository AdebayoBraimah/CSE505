"""Stony Brook University course scheduling module.

At the moment, this module only supports CSE majors.

WARNING:
    - This module is still a work in progress.

.. autosummary::
    :nosignatures:

    create_schedule
    create_schedule_ergo
    create_schedule_clingo
"""

import os
from typing import Union

from src import RESROURCEDIR
from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph, scrape_sbu_solar
from src.ergoai.ergoai import json_to_ergo, query_ergoai
from src.clapi.clapi import process_course_data_clingo, append_rules, query_clingo


def create_schedule(
    courses: Union[str, KnowledgeBase, KnowledgeGraph] = None,
    major: str = "CSE",
    query: str = None,
    method: str = "clingo",
    verbose: bool = False,
    lp_file: Union[str, KnowledgeBase, KnowledgeGraph] = None,
) -> str:
    """Creates a schedule based on the given courses, major, and query.

    Args:
        courses: Input knowledge base/graph file or URL of Stony Brook University courses.
        major: Major, represented as a three-letter code (e.g. "CSE").
        query: Query string (in the case of ``ERFO``) or file (in the case of ``Clingo``) to be used for scheduling.
        method: Method to be used for scheduling. Options are "ergo" and "clingo". Defaults to ``clingo``.
        verbose: If True, then additional information is printed to the console. Defaults to False.
        lp_file: Input ``clingo`` knowledge base/graph file of Stony Brook University courses. If provided, then the ``courses``, ``major``, and ``query`` arguments are ignored.

    Raises:
        ValueError: Arises when an invalid argument for ``method`` is provided.

    Returns:
        Schedule results.
    """
    if method.lower() == "ergo":
        results: str = create_schedule_ergo(courses=courses, major=major, query=query)
    elif method.lower() == "clingo":
        results: str = create_schedule_clingo(
            courses=courses,
            major=major,
            query_file=query,
            verbose=verbose,
            lp_file=lp_file,
        )
    else:
        raise ValueError(f"Invalid method: {method}")
    return results


def create_schedule_ergo(
    courses: Union[str, KnowledgeBase, KnowledgeGraph], major: str, query: str
) -> str:
    """Creates a schedule based on the given courses, major, and query using ErgoAI.

    Args:
        courses: Input knowledge base/graph file or URL of Stony Brook University courses.
        major: Major, represented as a three-letter code (e.g. "CSE").
        query: Query string to be used for scheduling.

    Raises:
        ValueError: Arises when an invalid argument for ``courses`` or ``major`` is provided.

    Returns:
        Schedule results.
    """
    if isinstance(courses, str):
        if (courses.beginwith("http")) and major:
            kg: KnowledgeGraph = scrape_sbu_solar(
                url=courses,
                major_three_letter_code=major,
                output_filename=os.path.join(
                    RESROURCEDIR, f"{major.lower()}.courses.json"
                ),
            )
        elif courses.endswith(".json"):
            kg: KnowledgeGraph = KnowledgeGraph(json=courses)
        elif courses.endswith(".ergo"):
            kg: KnowledgeGraph = KnowledgeGraph(ergo=courses)
        else:
            raise ValueError(f"Invalid input file: {courses}")
    elif isinstance(courses, KnowledgeBase) or isinstance(courses, KnowledgeGraph):
        kg: Union[KnowledgeBase, KnowledgeGraph] = courses
    else:
        raise ValueError(f"Invalid input type: {type(courses)}")

    if (
        (courses.endswith(".json"))
        or (courses.beginwith("http"))
        or (kg.json)
        or (not kg.ergo)
    ):
        _: str = json_to_ergo(
            json_file=kg,
            output_file=os.path.join(RESROURCEDIR, f"{major.lower()}.courses.ergo"),
        )

    results: str = query_ergoai(kg=kg, query=query)

    return results


def create_schedule_clingo(
    courses: Union[str, KnowledgeBase, KnowledgeGraph] = None,
    major: str = "CSE",
    query_file: str = None,
    verbose: bool = False,
    lp_file: Union[str, KnowledgeBase, KnowledgeGraph] = None,
) -> str:
    """Creates a schedule based on the given courses, major, and query using Clingo.

    Args:
        courses: Input knowledge base/graph file or URL of Stony Brook University courses.
        major: Major, represented as a three-letter code (e.g. "CSE").
        query_file: Query file to be used for scheduling.
        verbose: If True, then additional information is printed to the console. Defaults to False.
        lp_file: Input knowledge base/graph file of Stony Brook University courses. If provided, then the ``courses``, ``major``, and ``query_file`` arguments are ignored.

    Raises:
        ValueError: Arises when an invalid argument for ``courses`` or ``major`` is provided.

    Returns:
        Schedule results.
    """
    if lp_file:
        if isinstance(lp_file, str):
            if lp_file.endswith(".lp"):
                kg: KnowledgeGraph = KnowledgeGraph(lp=lp_file)
            else:
                raise ValueError(f"Invalid input file: {lp_file}")
        elif isinstance(lp_file, KnowledgeBase) or isinstance(lp_file, KnowledgeGraph):
            kg: Union[KnowledgeBase, KnowledgeGraph] = lp_file
        else:
            raise ValueError(f"Invalid input type: {type(lp_file)}")
    elif isinstance(courses, str):
        if (courses.beginwith("http")) and major:
            kg: KnowledgeGraph = scrape_sbu_solar(
                url=courses,
                major_three_letter_code=major,
                output_filename=os.path.join(
                    RESROURCEDIR, f"{major.lower()}.courses.json"
                ),
            )
        elif courses.endswith(".json"):
            kg: KnowledgeGraph = KnowledgeGraph(json=courses)
        elif courses.endswith(".lp"):
            kg: KnowledgeGraph = KnowledgeGraph(lp=courses)
        else:
            raise ValueError(f"Invalid input file: {courses}")
    elif isinstance(courses, KnowledgeBase) or isinstance(courses, KnowledgeGraph):
        kg: Union[KnowledgeBase, KnowledgeGraph] = courses
    else:
        raise ValueError(f"Invalid input type: {type(courses)}")

    if courses is not None:
        if (
            (courses.endswith(".json"))
            or (courses.beginwith("http"))
            or (kg.json)
            or (not kg.lp)
        ):
            _: str = process_course_data_clingo(file_path=kg, file_name=None)

    if lp_file:
        results: str = query_clingo(knowledge=kg.lp, verbose=verbose)
    else:
        output: str = append_rules(
            kg=[kg.lp, query_file],
            output_file=os.path.join(RESROURCEDIR, f"{major.lower()}.schedule.lp"),
        )
        results: str = query_clingo(knowledge=output, verbose=verbose)

    return results
