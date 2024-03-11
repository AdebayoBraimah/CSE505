# CSE505 Course Project
Stony Brook CSE505 project repository

# Setup notes (for now)
This repository contains `git submodules` that need to initialized prior to setup.

To do so, please follow the instructions below.

## `Git Submodule` setup initialiation

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
