"""_summary_
"""

from typing import List, Union

from src.kg.knowledge_graph import KnowledgeBase, KnowledgeGraph
from src.ergoai import json_to_ergo, query_ergoai

def create_schedule(courses: Union[str,KnowledgeBase,KnowledgeGraph], major: str, method: str = "clingo"):
    """_summary_
    """
    pass

def create_schedule_ergo(courses: Union[str,KnowledgeBase,KnowledgeGraph], major: str):
    pass

def create_schedule_clingo(courses: Union[str,KnowledgeBase,KnowledgeGraph], major: str):
    pass
