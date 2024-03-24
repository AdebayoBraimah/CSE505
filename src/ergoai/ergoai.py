"""ErgoAI module interface -- contains convenience functions.
"""

import os

from typing import Union

from src import ERGOROOT, XSBARCHDIR
from src.utils.util import file_parts
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


def json_to_ergo(json_file: str) -> str:
    pass


def query_ergoai(
    knowledge: Union[KnowledgeBase, KnowledgeGraph, str], query: str
) -> None:
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

    filepath, filename, _ = file_parts(knowledge)
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
    for ans in result:
        print(ans[0])
    return None
