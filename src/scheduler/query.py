"""Executes queries of some knowledge base.

.. autosummary::
    :nosignatures:

    query
"""

from typing import Union

from src.clapi.clapi import query_clingo
from src.ergoai.ergoai import query_ergoai
from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph


def query(
    knowledge: Union[KnowledgeBase, KnowledgeGraph, str],
    method: str = "clingo",
    verbose: bool = False,
    num_models: int = None,
    configuration: str = "handy",
    parallel_mode: int = None,
    query: str = None,
) -> str:
    """Executes queries for some knowledge base.

    WARNING:
        - ErgoAI queries are not fully supported.

    Usage example:
        >>> from src.scheduler.query import query
        >>> result = query(knowledge="cse_courses.json", method="clingo", verbose=True)
        >>> print(result)
        ...
        >>> result = query(knowledge="cse_courses.json", method="ergoai", query="?X[ancestor->?Y].")
        >>> print(result)
        ...

    Args:
        knowledge: Input knowledge base/graph file (or :py:class:`~src.kg.knowledge_graph.KnowledgeBase` or :py:class:`~src.kg.knowledge_graph.KnowledgeGraph` object) to be queried.
        method: Method to use for querying the knowledge base. Options are "clingo" or "ergoai". Defaults to "clingo".
        verbose: Print output to screen. Defaults to False.
        num_models: Number of models to generate for Clingo queries. Defaults to None.
        configuration: Configuration for Clingo queries. Options are "handy" or "competition". Defaults to "handy".
        parallel_mode: Parallel mode, maximum number of threads. Defaults to None.
        query: Query to be passed to ErgoAI. Defaults to None.

    Raises:
        ValueError: _description_

    Returns:
        _description_
    """
    if method.lower() == "clingo":
        result: str = query_clingo(
            knowledge=knowledge,
            verbose=verbose,
            num_models=num_models,
            configuration=configuration,
            parallel_mode=parallel_mode,
        )
    elif (method.lower() == "ergoai") or (method.lower() == "ergo"):
        result: str = query_ergoai(knowledge=knowledge, query=query)
    else:
        raise ValueError(f"Method '{method}' is not supported.")
    return result
