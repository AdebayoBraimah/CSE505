"""Module to download/scrape files from Stony Brook University's Solar System.

.. autosummary::
    :nosignatures:

    procure_course_data
"""

import os
from typing import Optional, Union
from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph, scrape_sbu_solar
from src.utils.util import timeit


# @timeit
def procure_course_data(
    url: Union[str, KnowledgeBase],
    major: str,
    output: Optional[str] = None,
    headless: bool = True,
    verbose: bool = False,
    wait_time: int = 10,
) -> KnowledgeGraph:
    """Procures course data from Stony Brook University's Solar System for a select major.
    If the output file exists, then this function will simply return a :py:class:`~src.kg.knowledge_graph.KnowledgeBase` object.

    Usage example:
        >>> from src.scheduler.download import procure_course_data
        >>> url = "https://prod.ps.stonybrook.edu/psc/csprodg/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?"
        >>> kg = procure_course_data(url, "CSE", output="cse_courses.json")
        >>> print(kg.json)
        cse_courses.json
        >>> kg = procure_course_data(url, "CSE", "cse_courses.json")
        >>> print(kg.json)
        cse_courses.json

    Args:
        url: URL of Stony Brook University course catalog as string or :py:class:`~src.kg.knowledge_graph.KnowledgeBase` object.
        major: Major, represented as a three-letter code (e.g. "CSE").
        output: Output filename for the JSON file. Defaults to None.
        headless: Do not open brower. Defaults to True.
        verbose: Print output to screen. Defaults to False.
        wait_time: Maximum wait time (in seconds) for each click operation. Defaults to 10.

    Returns:
        :py:class:`~src.kg.knowledge_graph.KnowledgeBase` object containing course information that corresponds to a set of output JSON, and CSV files.
    """
    if (output is not None) and (os.path.exists(output)):
        kg: KnowledgeGraph = KnowledgeGraph(json=output)
    else:
        kg: KnowledgeGraph = scrape_sbu_solar(
            url=url,
            major_three_letter_code=major,
            output_filename=output,
            headless=headless,
            verbose=verbose,
            wait_time=wait_time,
        )
    return kg
