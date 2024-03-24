#!/usr/bin/env python
"""Graduation requirements project.

Still a work in progress.

See test code in this python file for further details.
"""
# TODO: Finish writing documentation
import os
from src.ergoai.ergoai import query_ergoai

test_file: str = os.path.abspath("foo.ergo")
query: str = "?Subject[?Property->?Object]"

query_ergoai(knowledge=test_file, query=query)
