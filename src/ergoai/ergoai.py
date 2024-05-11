"""ErgoAI module interface -- contains convenience functions.

.. autosummary::
    :nosignatures:

    json_to_ergo
    query_ergoai
"""

import os

from typing import Any, Optional, Union

from src import ERGOROOT, XSBARCHDIR
from src.utils import util
from src.utils.util import timeit
from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph

from pyergo import (
    pyergo_start_session,
    pyergo_end_session,
    pyergo_command,
    pyergo_query,
)


@timeit
def json_to_ergo(
    json_file: Union[KnowledgeBase, KnowledgeGraph, str],
    output_file: Optional[str] = None,
) -> str:
    """Converts a JSON file to an ERGO file.

    NOTE:
        - If a JSON file needs to be converted to an ERGO file, this function MUST be called first before calling :func:`query_ergoai`.
        - If a :py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object is passed, then the object is updated with the ERGO file path.

    DANGER:
        - This function can only be called/used once per python session. If you need to convert multiple JSON files to ERGO files, you must start a new session each time, otherwise subsequent calls to :func:`json_to_ergo` will cause the current python session to crash.

    Usage example:
        >>> from src.ergoai.ergoai import json_to_ergo
        >>> ergo_file = json_to_ergo(json_file="cse_courses.json")
        >>> print(ergo_file)
        cse_courses.ergo

    Args:
        json_file: Input JSON file (:py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be converted to ERGO file.
        output_file: Output filename. If not specified, then a new file of the same name is created, with a '.ergo' file extension. Defaults to None.

    Returns:
        Path to the output ERGO file.
    """
    if (isinstance(json_file, KnowledgeBase)) or (
        isinstance(json_file, KnowledgeGraph)
    ):
        kg: Union[KnowledgeBase, KnowledgeGraph] = json_file
        json_file = kg.json
    else:
        kg: Union[KnowledgeBase, KnowledgeGraph] = None

    # If output file is not provided, use the same filename
    if (output_file is None) or (output_file == ""):
        _filepath, _filename, _ = util.file_parts(json_file)
        output_file = os.path.join(_filepath, f"{_filename}.ergo")

    # Start ErgoAI session
    pyergo_start_session(XSBARCHDIR, ERGOROOT)

    # Perform command
    ergoai_command = f"'{json_file}'[parse2file('{output_file}')]@\json."
    pyergo_command(ergoai_command)

    # End ErgoAI session
    pyergo_end_session()

    # Update KnowledgeBase or KnowledgeGraph object
    if kg is not None:
        kg.ergo = os.path.abspath(output_file)

    return output_file


@timeit
def query_ergoai(
    knowledge: Union[KnowledgeBase, KnowledgeGraph], query: str
) -> Union[str, Any]:
    """Queries an ERGO knowledge base/graph using ErgoAI.

    WARNING:
        - This function is still a work in progress.

    Args:
        knowledge: Input knowledge base/graph ERGO file (or :py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be queried.
        query: Query to be passed to ErgoAI.

    Returns:
        Results of the query.
    """
    # NOTE: Query must be formatted like this: ?X[ancestor->?Y].

    # Start ErgoAI session
    pyergo_start_session(XSBARCHDIR, ERGOROOT)

    if (isinstance(knowledge, str)) and (knowledge.endswith(".ergo")):
        kg: Union[KnowledgeBase, KnowledgeGraph] = KnowledgeGraph(ergo=knowledge)
        knowledge: str = kg.ergo
    elif isinstance(knowledge, str):
        raise ValueError(
            "Knowledge must be a 'KnowledgeBase' or 'KnowledgeGraph' object."
        )

    if (isinstance(knowledge, KnowledgeBase)) or isinstance(knowledge, KnowledgeGraph):
        kg: Union[KnowledgeBase, KnowledgeGraph] = knowledge
        knowledge: str = kg.ergo

    # Remove file extension (if present)
    filepath: str
    filename: str

    filepath, filename, _ = util.file_parts(knowledge)
    knowledge: str = os.path.join(filepath, filename)

    pyergo_command(f"['{knowledge}'].")

    result = pyergo_query(f"{query}.")

    # ErgoAI example code
    # for ans in result:
    #     [(XVarName, XVarVal), (YVarName, YVarVal)] = ans[0]
    #     print(
    #         "ancestor of "
    #         + XVarName
    #         + "="
    #         + str(XVarVal)
    #         + " is "
    #         + YVarName
    #         + "="
    #         + str(YVarVal)
    #     )

    # Print results for now
    # for ans in result:
    #     print(ans[0])
    # return None

    return result
