#!/usr/bin/env python
"""Graduation requirements project.

Warning:
    - Still a work in progress.

See test code below. See ``doc`` directory in this project for further details.

Example: ./app.py

[Results will be printed to the console.]

The contents of the input file ``CSE505/src/resources/cse.schedule.lp`` are as follows:

.. code-block:: clingo

    course(cse101, 3).
    course(cse102, 3).
    course(cse110, 3).
    .
    .
    .
    prerequisite(cse230, cse220).
    prerequisite(cse260, cse160).
    prerequisite(cse261, cse260).

    % Constants
    min_credits_per_semester(12).
    max_credits_per_semester(15).
    total_required_credits(80).

    % Assign courses to semesters (1..N), N is an upper bound on semesters, guessed here as 10
    semester(1..10).

    % Assign a course to exactly one semester
    1 { in_semester(C, S) : semester(S) } 1 :- course(C, _).

    % Constraint to ensure the minimum number of credits per semester
    :- semester(S), min_credits_per_semester(Min), #sum{Credits, C : course(C, Credits), in_semester(C, S)} < Min.

    % Ensure the total credits in each semester do not exceed the maximum allowed
    :- semester(S), max_credits_per_semester(Max), #sum{Credits, C : course(C, Credits), in_semester(C, S)} > Max.

    % Ensuring all prerequisites are met
    :- course(C, _), in_semester(C, SC), prerequisite(C, P), course(P, _), in_semester(P, SP), SP >= SC.

    % Define the maximum semester used
    max_semester_used(M) :- M = #max{S : in_semester(_, S)}.

    % Minimize the number of semesters used
    #minimize{M : max_semester_used(M)}.

    % Output control
    #show in_semester/2.
"""
import os
import sys

# Add project root to the Python path
_PKG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_PKG_PATH)

# Import project modules
from src import RESROURCEDIR
from src.schedule import create_schedule
from src.kg.knowledge_graph import KnowledgeGraph

# Specify input files
lp_file: str = os.path.join(RESROURCEDIR, "cse.schedule.lp")

# Create KnowledgeGraph object
kg: KnowledgeGraph = KnowledgeGraph(lp=lp_file)

# Create schedule
results: str = create_schedule(major="CSE", method="clingo", lp_file=kg.lp)

# Print results to console
print(results)
