[![Documentation Status](https://readthedocs.org/projects/cse505/badge/?version=latest)](https://cse505.readthedocs.io/en/latest/?badge=latest)  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
      

# CSE505 Course Project
Stony Brook CSE505 project repository

NOTE: README.md doc is formatted for viewing on GitHub: https://github.com/AdebayoBraimah/CSE505

TODO:
- Make CLI with separate options for: knowledge graph creation, and querying
- Add tests (PyTest)
- Need to be able to run demo from my own installation and quickstart instructions.
- Update documentation
- Use semester restriction to reduce combinatorial explosion (Ie CSE 101 can only be in semester 1 along with other beginner classes)
- Add self evaluation results to repo with corresponding commands

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
./app.py
```


<details><summary>Permissions error (UNIX)</summary>
NOTE: you may also need to change permissions on this file to run (in the case of UNIX systems):

In the case of permissions errors, try:         

```bash
chmod 755 ./app.py
```
</details>           


The following should print to the screen:

```bash
clingo version 5.7.1
Reading from ...s/CSE505/src/resources/cse.schedule.lp
Solving...
UNSATISFIABLE

Models       : 0
Calls        : 1
Time         : 5.223s (Solving: 5.22s 1st Model: 0.00s Unsat: 5.22s)
CPU Time     : 5.220s
```

# Documentation

Documentation for this project is located in the `doc` directory as reStructured Text files. HTML version of this documentation can be found here: https://cse505.readthedocs.io/en/latest/?badge=latest

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
