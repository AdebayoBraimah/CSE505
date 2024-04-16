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
    """Similar to MATLAB's ``fileparts`` function shown `here <https://www.mathworks.com/help/matlab/ref/fileparts.html>`_.

    Splits a full filename into:
        * file path
        * filename (no file path, no file extension)
        * file extension

    Usage example:
        >>> path_name, file_name, file_ext = file_parts('/Users/username/Desktop/file.txt')
        >>> path_name
        '/Users/username/Desktop'
        >>> file_name
        'file'
        >>> file_ext
        '.txt'

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
