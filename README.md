# CSE505 Course Project
Stony Brook CSE505 project repository

# Test Code & Driver program

To run the test code:

```bash
./app.py
```

NOTE: you may also need to change permissions on this file to run (in the case of UNIX systems):

```bash
chmod 755 app.py
```

The following should print to the screen:

```bash
[('?Subject', ERGOSymbol(value=_$_$_ergo'autogen1|1'1)), ('?Property', ERGOSymbol(value=aaa)), ('?Object', 1)]
[('?Subject', ERGOSymbol(value=_$_$_ergo'autogen1|1'1)), ('?Property', ERGOSymbol(value=bbb)), ('?Object', ERGOSymbol(value=_$_$_ergo'autogen1|2'1))]
[('?Subject', ERGOSymbol(value=_$_$_ergo'autogen1|2'1)), ('?Property', ERGOSymbol(value=ccc)), ('?Object', [1, 2, ERGOSymbol(value=_$_$_ergo'autogen1|3'1)])]
[('?Subject', ERGOSymbol(value=_$_$_ergo'autogen1|2'1)), ('?Property', ERGOSymbol(value=ddd)), ('?Object', ERGOSymbol(value=ppp))]
[('?Subject', ERGOSymbol(value=_$_$_ergo'autogen1|3'1)), ('?Property', ERGOSymbol(value=111)), ('?Object', 3)]
[('?Subject', ERGOSymbol(value=_$_$_ergo'autogen1|3'1)), ('?Property', ERGOSymbol(value=ppp)), ('?Object', 4)]
```

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

For details for ``Git Submodule`` can be found [here](https://gist.github.com/gitaarik/8735255).
