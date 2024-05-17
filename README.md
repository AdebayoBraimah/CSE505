[![Documentation Status](https://readthedocs.org/projects/cse505/badge/?version=latest)](https://cse505.readthedocs.io/en/latest/?badge=latest)  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
      

# CSE505 Course Project
Stony Brook CSE505 project repository

NOTE: README.md doc is formatted for viewing on GitHub: https://github.com/AdebayoBraimah/CSE505

# Project Details

See the project details below pertaining to where things are, what was done, what was found, and how to run and test this program.

More detailed information and demos are located in the following locations:

* **Project report**: Contains project information and comprehensive details.
* **Online documentation**: Contains project API documentation, installation instructions, demonstrations, and testing instructions.

## Structure/Organization

* ``.dev``: Developer tools/scripts directory.
* ``doc``: Documents directory -- contains ``rst`` files used to build HTML documentation (located here: https://cse505.readthedocs.io/en/latest/?badge=latest).
* ``report``: Contains the project presentation and report (both as PDFs, and the corresponding ``LaTeX`` code for the report).
* ``results`` contains the results of the correctness tests and evaluation.
* ``src``: Contains project source files (in python, clingo and bash (as a wrapper script)).
* ``driver.py``: Driver program (in python).
* ``requirements.txt``: Python package dependencies for the project.

## Course scheduler

The program is schedule builder for Stony Brook CSE course scheduling for the fall and spring semesters. The schedule builder essentially builds a course schedule for an undergraduate Stony Brook CSE student. The constraints are to be enrolled in a minimum of 12 credits (to maintain full-time student status) and a maximum of 18 credits (as more credits logistically becomes difficult to manage). Additionally, the course work is intended to help the student schedule courses that help the student towards satifisfyying the undergraduate CSE requirements.

## Findings

Using clingo as a schedule builder to create a schedule from the beginning of an undergraduate student's career to the end was a highly non-trivial task -- as the approach suffered from: grounding overhead and combinatorial explosion (due to the large number of possible courses offered). Using clingo to schedule courses for two semesters was far more manageable.

## Tests

### Unit tests

Unit tests were implemented mostly for utility functions, and can be run with the following command:

```bash
pytest src/tests
```

### Correctness testing and evaluation

Correctness testing and evaluation can be performed with the following command:

```bash
# eval - 2 sem
./src/schedule.py query \
--knowledge=results/eval/cse_courses.eval.lp \
--query=results/sem.lp \
--query=results/cse_prereqs.lp \
--clingo
```

Which should have the following output to the console:

```text
--------------------------------------------
Begin: query  |  May-16-2024 02:22:03
--------------------------------------------

--------------------------------------------
Begin: query_clingo  |  May-16-2024 02:22:03
--------------------------------------------

clingo version 5.7.1
Reading from results/eval/cse_courses.eval.lp ...
Solving...
Answer: 1
schedule(ams310,spring) schedule(bio204,spring) schedule(che129,spring) 
schedule(che131,spring) schedule(ams161,fall) schedule(bio201,fall) 
schedule(bio204,fall) schedule(che131,fall) schedule(che133,fall)
SATISFIABLE

Models       : 1+
Calls        : 1
Time         : 0.013s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.013s

--------------------------------------------
End: query_clingo Execution time: 0.02 sec.   |  May-16-2024 02:22:03
--------------------------------------------

--------------------------------------------
End: query Execution time: 0.02 sec.   |  May-16-2024 02:22:03
--------------------------------------------
```

Comparing the above with the following course atoms:

```text
% Spring
course(ams310, 3, "Undergraduate", 1, 1).
course(bio204, 2, "Undergraduate", 1, 1).
course(che129, 4, "Undergraduate", 1, 1).
course(che131, 4, "Undergraduate", 1, 1).

% Spring total: 13 credits

% Fall
course(ams161, 3, "Undergraduate", 1, 1).
course(bio201, 3, "Undergraduate", 1, 1).
course(bio204, 2, "Undergraduate", 1, 1).
course(che131, 4, "Undergraduate", 1, 1).
course(che133, 1, "Undergraduate", 1, 1).

% Fall total: 13 credits
```

The following shows that the output is correct (assuming the prerequisites have been met).

The evaluation was performed against a user (me), in which the user manually created a schedule, and the time to do so was compared. The results of this evaluation is shown in the bar graphs in ``report/cse-505-project/figures/eval``.

# Report and Presentation

The project report and presentation are located in the ``report`` directory.

# Installation

NOTE: 
- More detailed installation instructions are located in the HTML documentation linked above.
- Troubleshooting information is also located in the HTML documentation linked above.

This project runs using python v3.10 via miniconda. The python dependencies can be installed as follows:

```bash
pip install selenuim
pip install -r requirements.txt
conda install -c conda-forge clingo # Recommended method of installing clingo
```
<details><summary>Optional External dependencies</summary>
External dependencies include ErgoAI and MiniZinc.
At the moment, the driver program does not use these components.
</details>


# Quickstart

## Test Code & Driver program

To run the test code:

```bash
./driver.py
```


<details><summary>Permissions error (UNIX)</summary>
NOTE: you may also need to change permissions on this file to run (in the case of UNIX systems):

In the case of permissions errors, try:         

```bash
chmod 755 ./driver.py
```
</details>           


The following should print to the screen:

```text
--------------------------------------------
Begin: query_clingo  |  May-16-2024 00:43:51
--------------------------------------------

clingo version 5.7.1
Reading from ...projects/CSE505/results/cse_courses.lp ...
Solving...
Answer: 1
schedule(bio204,spring) schedule(che129,spring) schedule(geo102,spring) schedule(geo122,spring) schedule(ast203,fall) schedule(ast205,fall) schedule(ams301,fall) schedule(cse304,fall)
SATISFIABLE

Models       : 1+
Calls        : 1
Time         : 0.063s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.059s

--------------------------------------------
End: query_clingo Execution time: 0.16 sec.   |  May-16-2024 00:43:51
--------------------------------------------
```

# Documentation

Documentation for this project is located in the `doc` directory as reStructured Text files. HTML version of this documentation can be found here: https://cse505.readthedocs.io/en/latest/?badge=latest

# Evaluation

Should evaluation need to be performed, then running the following commands would accomplish the this:

```bash
# 2 sem
./src/schedule.py query --knowledge=results/cse_courses.lp --query=results/sem.lp --query=results/cse_prereqs.lp --clingo

# 12 sem approach # NOTE: This will not stop running
./src/schedule.py query --knowledge=results/cse_courses.lp --query=results/cse_bs_grad_reqs.lp --query=results/cse_prereqs.lp --clingo

# eval - 2 sem
./src/schedule.py query --knowledge=results/eval/cse_courses.eval.lp --query=results/sem.lp --query=results/cse_prereqs.lp --clingo

# eval - 12 sem # NOTE: This will not stop running
./src/schedule.py query --knowledge=results/eval/cse_bs_grad_reqs.eval.lp --query=results/eval/cse_courses.eval.lp --query=results/cse_prereqs.lp --clingo
```

# Dev Notes

The ``.dev`` directory contains the necessary files (e.g. scripts and requirements for conda environment).

## Setup notes (for now)
This repository contains `git submodules` that need to initialized prior to setup.

To do so, please follow the instructions below.

### `Git Submodule` setup initialiation

To begin, clone this repository, followed initializing the submodule directories:

```sh
git clone --recurse-submodules https://github.com/AdebayoBraimah/CSE505.git
```

To update your local repository:
```sh
git pull --recurse-submodules
```

For changes/updates made in the submodule:
```sh
git submodule update
```

For details for ``Git Submodule`` can be found [here](https://gist.github.com/gitaarik/8735255).
