"""Utility module for this project.

.. autosummary::
    :nosignatures:

    file_parts

.. autoclass:: DownloadBar # does not exist -- use this for classes
    :members:
"""

import os

from typing import Tuple


def file_parts(file: str) -> Tuple[str, str, str]:
    """Similar to MATLAB's ``fileparts`` function.
    Splits a full filename into:
        * file path
        * filename (no file path, no file extension)
        * file extension

    Args:
        file: Input file filename.

    Returns:
        Tuple:
            * file path
            * filename (no file path, no file extension)
            * file extension
    """
    file: str = os.path.abspath(file)

    # Extract and organize strings
    filepath: str
    ext: str
    _filename: str

    filepath, _filename = os.path.split(file)
    _, ext = os.path.splitext(file)
    filename: str = _filename[: -len(ext)]

    return filepath, filename, ext
