#!/usr/bin/env python
"""Semester course planning.

See test code below. See ``doc`` directory in this project for further details.

Example: ./driver.py

[Results will be printed to the console.]

The contents of the input file ``CSE505/results/cse_courses.lp`` are as follows:

.. code-block:: clingo

    % Course atoms
    course(cse101, 3, "Undergraduate", 1, 1).
    course(cse102, 3, "Undergraduate", 0, 0).
    course(cse110, 3, "Undergraduate", 1, 1).
    .
    .
    .
    % Prerequisites for CSE113
    :- course(cse113, 4, "Undergraduate", 0, 1), 
    not course(ams151, _, "Undergraduate", _, _), 
    not course(mat125, _, "Undergraduate", _, _), 
    not course(mat131, _, "Undergraduate", _, _). 

    % Prerequisites for CSE114
    :- course(cse114, 4, "Undergraduate", 1, 0), 
    not course(cse101, _, "Undergraduate", _, _), 
    not course(ise108, _, "Undergraduate", _, _). 
"""
import os
import sys

# Add project root to the Python path
_PKG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_PKG_PATH)

# Import project modules
from src.kg.knowledge_graph import KnowledgeGraph, scrape_sbu_solar
from src.clapi.clapi import process_course_data_clingo, query_clingo

if not (os.path.exists("results")):
    os.mkdir("results")

results_dir: str = os.path.abspath("results")

# 1. Create knowledge graph if it does not exist
if (not (os.path.exists(f"{results_dir}/cse_courses.json"))) and (
    not (os.path.exists(f"{results_dir}/cse_courses.lp"))
):
    kg: KnowledgeGraph = scrape_sbu_solar(
        url="https://prod.ps.stonybrook.edu/psc/csprodg/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?",
        major_three_letter_code="cse",
        wait_time=10,
        headless=True,
        verbose=True,
        output_filename=f"{results_dir}/cse_courses",
    )
    kg.df.to_json(f"{results_dir}/cse_courses.json", orient="index", indent=4)

# 2. Convert JSON to Clingo if it does not exist
if not (os.path.exists(f"{results_dir}/cse_courses.lp")):
    clingo_file: str = process_course_data_clingo(
        json_file=f"{results_dir}/cse_courses.json",
        output_file=f"{results_dir}/cse_courses.lp",
    )

# 3. Query the knowledge graph
# NOTE: Not all of the files used in the query are
#   created (automatically) in this script.
query_result: str = query_clingo(
    knowledge=f"{results_dir}/cse_courses.lp",
    num_models=None,
    configuration="handy",
    parallel_mode=None,
    query=(
        f"{os.path.join(results_dir,'cse_prereqs.lp')}",
        f"{os.path.join(results_dir,'sem.lp')}",
    ),
)
