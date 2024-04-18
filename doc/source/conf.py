# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# NOTE: Configuration options used are from:
#   https://github.com/pypa/setuptools/blob/main/docs/

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import pathlib
import datetime

from typing import Dict, List

_pkg_path: str = str(pathlib.Path(os.path.abspath(__file__)).parents[2])

##################################################
# Install selenium                               #
##################################################
#
# NOTE: This is a temporary fix to install selenium

import shlex
import subprocess

command = "pip install selenium"
command = shlex.split(command)

##################################################
# End Insall selenium                            #
##################################################

subprocess.run(command, check=True)

sys.path.insert(0, _pkg_path)
sys.path.append(_pkg_path)

from src import __author__, __version__

# -- Project information -----------------------------------------------------
_year: int = datetime.datetime.now().year

project: str = "cse-505-project"
copyright: str = f"{_year}, {__author__}"
author: str = f"{__author__}"

# The full version, including alpha/beta/rc tags
release: str = f"{__version__}"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions: List[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxarg.ext",
    "sphinx_autodoc_typehints",
    "rst.linker",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.autosummary",
    "sphinx_autopackagesummary",
    "sphinx.ext.viewcode",
]

autosummary_generate: bool = True

# master_doc: str = "index"

source_suffix: Dict[str, str] = {
    ".rst": "restructuredtext",
}

intersphinx_mapping: Dict[str, str] = {
    "python": ("https://docs.python.org/3", None),
}

intersphinx_mapping.update(
    {
        "pip": ("https://pip.pypa.io/en/latest", None),
        "build": ("https://pypa-build.readthedocs.io/en/latest", None),
        "PyPUG": ("https://packaging.python.org/en/latest/", None),
        "packaging": ("https://packaging.pypa.io/en/latest/", None),
        "twine": ("https://twine.readthedocs.io/en/stable/", None),
        "importlib-resources": (
            "https://importlib-resources.readthedocs.io/en/latest",
            None,
        ),
    }
)

# Add support for linking usernames
github_url = "https://github.com"
github_repo_org = "pypa"
github_repo_name = "CSE505"
github_repo_slug = f"{github_repo_org}/{github_repo_name}"
github_repo_url = f"{github_url}/{github_repo_slug}"
github_sponsors_url = f"{github_url}/sponsors"
extlinks = {
    "user": (f"{github_sponsors_url}/%s", "@%s"),  # noqa: WPS323
    "pypi": ("https://pypi.org/project/%s", "%s"),  # noqa: WPS323
    "wiki": ("https://wikipedia.org/wiki/%s", "%s"),  # noqa: WPS323
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["tests"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
