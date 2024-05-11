[![Documentation Status](https://readthedocs.org/projects/cse505/badge/?version=latest)](https://cse505.readthedocs.io/en/latest/?badge=latest)  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
      

# CSE505 Course Project
Stony Brook CSE505 project repository

NOTE: README.md doc is formatted for viewing on GitHub: https://github.com/AdebayoBraimah/CSE505

# Installation

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

```bash
--------------------------------------------
Begin: query_clingo  |  May-11-2024 04:00:08
--------------------------------------------

clingo version 5.7.1
Reading from ...projects/CSE505/results/cse_courses.lp ...
Solving...
Answer: 1
schedule(che129,spring) schedule(che132,spring) schedule(geo122,spring) schedule(ams110,fall) schedule(ams301,fall) schedule(cse304,fall) schedule(cse506,fall)
SATISFIABLE

Models       : 1+
Calls        : 1
Time         : 0.058s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.053s

--------------------------------------------
End: query_clingo Execution time: 0.07 sec.   |  May-11-2024 04:00:08
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
