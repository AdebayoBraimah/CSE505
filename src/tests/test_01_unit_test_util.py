"""Tests for the package utility module.
"""

import pytest

import os
import pathlib
import sys

# Add package/module to PYTHONPATH
mod_path: str = os.path.join(str(pathlib.Path(os.path.abspath(__file__)).parents[2]))
sys.path.append(mod_path)


from src.utils.util import DependencyError, check_dependencies, file_parts


def test_dependency_error():
    """Test the DependencyError class."""
    with pytest.raises(DependencyError):
        raise DependencyError


def test_check_dependencies():
    """Test the check_dependencies function."""
    with pytest.raises(DependencyError):
        check_dependencies(("ls", "cat", "dog"))


def test_file_parts():
    """Test the file_parts function."""
    path_name, file_name, file_ext = file_parts("/Users/username/Desktop/file.txt")
    assert path_name == "/Users/username/Desktop"
    assert file_name == "file"
    assert file_ext == ".txt"

    path_name, file_name, file_ext = file_parts("/Users/username/Desktop/file")
    assert path_name == "/Users/username/Desktop"
    assert file_name == "file"
    assert file_ext == ""

    path_name, file_name, file_ext = file_parts("/Users/username/Desktop/file.")
    assert path_name == "/Users/username/Desktop"
    assert file_name == "file"
    assert file_ext == "."
