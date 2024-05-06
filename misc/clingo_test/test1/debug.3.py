import os
import sys

_PKG_PATH: str = "/Users/adebayobraimah/Desktop/projects/CSE505"
sys.path.append(_PKG_PATH)

# from src.clapi.clapi import _write_list_to_file, translate_range
from src.clapi.clapi import process_course_data_clingo

json_file = "/Users/adebayobraimah/Desktop/projects/CSE505/misc/clingo_test/test1/cse_courses.json"

process_course_data_clingo(json_file, repeatable_courses=None)
