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
from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph

from pyergo import (
    pyergo_start_session,
    pyergo_end_session,
    pyergo_command,
    pyergo_query,
    HILOGFunctor,
    PROLOGFunctor,
    ERGOVariable,
    ERGOString,
    ERGOIRI,
    ERGOSymbol,
    ERGOIRI,
    ERGOCharlist,
    ERGODatetime,
    ERGODuration,
    ERGOUserDatatype,
    pyxsb_query,
    pyxsb_command,
    XSBFunctor,
    XSBVariable,
    XSBAtom,
    XSBString,
    PYERGOException,
    PYXSBException,
)


def json_to_ergo(
    json_file: Union[KnowledgeBase, KnowledgeGraph, str],
    output_file: Optional[str] = None,
) -> str:
    """Converts a JSON file to an ERGO file.

    NOTE:
        - If a JSON file needs to be converted to an ERGO file, this function MUST be called first before calling ``pyergo_query``.
        - If a KnowledgeBase or KnowledgeGraph object is passed, then the object is updated with the ERGO file path.

    Args:
        json_file: Input JSON file (``KnowledgeBase`` or ``KnowledgeGraph`` object) to be converted to ERGO file.
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


def query_ergoai(
    knowledge: Union[KnowledgeBase, KnowledgeGraph, str], query: str
) -> Union[str, Any]:
    """Queries an ERGO knowledge base/graph using ErgoAI.

    WARNING:
        - This function is still a work in progress.

    Args:
        knowledge: Input knowledge base/graph ERGO file (or ``KnowledgeBase`` or ``KnowledgeGraph`` object) to be queried.
        query: Query to be passed to ErgoAI.

    Returns:
        Results of the query.
    """
    # NOTE: Query must be formatted like this: ?X[ancestor->?Y].
    # TODO: Need to add argument for queries to pass to
    #   ErgoAI.

    # Start ErgoAI session
    pyergo_start_session(XSBARCHDIR, ERGOROOT)

    # TODO: Convert JSON to ERGO files
    if isinstance(knowledge, str):
        pass

    if isinstance(knowledge, KnowledgeBase):
        # store as knowledge graph file
        pass

    if isinstance(knowledge, KnowledgeGraph):
        # store as file
        pass

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
