#!/usr/bin/env python
"""Creates python virtual environment at a specified path.

Example usage (in this project, on UNIX systems):

./create_env.py --conda --path=$(pwd)/../.env --python-version=3.10

Run:

pip install -r requirements.txt

NOTE: The '-c'/'--conda' option is a bit unreliable at the moment.
"""

import os
import sys
import subprocess
import shlex
import shutil
import argparse

from typing import Any, Dict, List


class DependencyError(Exception):
    """Exception intended for unment dependencies"""

    pass


def main() -> None:
    parser = arg_parser()
    args = parser.parse_args()

    # Print help message in the case of no arguments
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        args: Dict[str, Any] = vars(args)

    # Get variable names
    conda: bool = args.get("conda")
    venv: bool = args.get("venv")
    path: str = args.get("path")
    py_version: str = args.get("py_version")

    if (path is None) or (path == ""):
        raise RuntimeError(
            f"'-p', '--path' option must be specified, and cannot be empty."
        )

    if conda:
        manager: str = "conda"
    elif venv:
        manager: str = "venv"

    create_environment(manager=manager, path=path, py_version=py_version)

    return None


def create_environment(manager: str, path: str, py_version: str | None):
    path: str = os.path.abspath(path=path)
    command: str = env_command(manager=manager, path=path, py_version=py_version)
    check_dependency(command=command)

    python_cmd_exec: List[str] = shlex.split(s=command, comments=False, posix=True)

    subprocess.run(python_cmd_exec)

    if manager == "conda":
        python_cmd_exec: List[str] = shlex.split(
            s=f"{manager} activate {path}", comments=False, posix=True
        )
        print(python_cmd_exec)
        # subprocess.run(python_cmd_exec)
        # subprocess.run(shlex.split(s=f"{manager} install python --yes", comments=False, posix=True))
        # subprocess.run(shlex.split(s=f"{manager} install pip --yes", comments=False, posix=True))

    return None


def env_command(manager: str, path: str, py_version: str | None) -> str:
    if (py_version is not None) and (float(py_version)):
        py_install_version: str = f" python={py_version}"
    else:
        py_install_version: str = ""

    if manager == "conda":
        command: str = (
            f"{manager} create -p {path} {py_install_version} --no-default-packages --yes"
        )

    elif manager == "venv":
        command: str = f"python -m {manager} {path}"
    else:
        print("Invalid environment manager. Please choose either 'conda' or 'venv'.")
    return command


def check_dependency(command: str, raise_exc: bool = False) -> bool:
    """Checks the dependency of an input command string.

    Example usage:
        >>> command = conda create -p conda_env --no-default-packages --yes

    Args:
        command: Input command line string.
        raise_exc: Raises exception if dependency is not met. Defaults to False.

    Raises:
        DependencyError: Exception raised if dependency is not met, and ``raise_exc`` is ``True``.

    Returns:
        Boolean, ``True`` if dependency is met, and false otherwise.
    """
    _tmp: List[str] = shlex.split(command)
    _cmd: str = _tmp[0]

    if not shutil.which(_cmd) and raise_exc:
        raise DependencyError(f"Command executable not found in system path: {_cmd}")
    elif not shutil.which(_cmd):
        return False
    else:
        return True


def arg_parser() -> argparse.ArgumentParser:
    """Command line interface (CLI) argument parser.

    Returns:
       Argument parser object.
    """
    # Init parser
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
        # , formatter_class=argparse.RawTextHelpFormatter)
    )

    # Parse Arguments
    reqoptions = parser.add_argument_group("Required Arguments")

    reqoptions.add_argument(
        "-p",
        "--path",
        dest="path",
        type=str,
        metavar="<STR>",
        default=None,
        help="REQUIRED: Absolute path to virtual environment to be created.",
    )

    optoptions = parser.add_argument_group("Optional Arguments")

    optoptions.add_argument(
        "-v",
        "--venv",
        dest="venv",
        default=True,
        action="store_true",
        help="OPTIONAL: Use python's built-in 'venv' to create the virtual environment. Used by default if not specified.",
    )

    optoptions.add_argument(
        "-c",
        "--conda",
        dest="conda",
        default=False,
        action="store_true",
        help="OPTIONAL: Use ana(conda) to create the virtual environment.",
    )

    optoptions.add_argument(
        "-py",
        "--py",
        "--python-version",
        dest="py_version",
        metavar="<3.10>",
        type=str,
        default=None,
        help="OPTIONAL: Python version to be installed by conda [Default: Current version of python].",
    )

    # args: argparse.ArgumentParser.parse_args = parser.parse_args()

    return parser


if __name__ == "__main__":
    main()
