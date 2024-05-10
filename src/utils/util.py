"""Utility module for this project.

.. autosummary::
    :nosignatures:

    DependencyError
    file_parts
    check_dependencies
    timeit
"""

import os
import shutil
import time

from typing import Tuple


# TODO:
#   Add multiprocessing as a utility function
#   Add profiling as a utility function
#
#   from cProfile import Profile
#   from pstats import Stats
#   with Profile() as pr:
#       main()
#
class DependencyError(Exception):
    """Exception intended for unmet external dependencies"""

    pass


def timeit(func: callable) -> callable:
    """Timing (decorator) function to time the execution of a function.

    Prints the execution time of the function.

    Usage example:
        >>> @timeit
        ... def main():
        ...     print("Hello, World!")
        ...
        >>> main()
        Begin: main
        Hello, World!
        End: main Execution time: 0.00 sec.

    Args:
        func: Function to be timed.

    Returns:
        Decorated function.
    """

    def timed(*args, **kwargs):
        """Inner/nested function to time the execution of the function.

        Returns:
            Result of the function.
        """
        start_time = time.time()
        print("--------------------------------------------")
        print(f"Begin: {func.__name__}")
        print("--------------------------------------------\n")
        result = func(*args, **kwargs)
        end_time = time.time()
        print("--------------------------------------------")
        print(f"End: {func.__name__} Execution time: {end_time - start_time:.2f} sec.")
        print("--------------------------------------------\n")
        return result

    return timed


# TODO: Usage example
def check_dependencies(dependencies: Tuple[str]) -> bool:
    """Checks if the required dependencies are installed.

    Args:
        dependencies: Tuple of required dependencies.

    Raises:
        DependencyError: If any of the dependencies are not installed.

    Returns:
        True if all dependencies are installed.
    """
    for dependency in dependencies:
        if not shutil.which(dependency):
            raise DependencyError(f"Dependency '{dependency}' not found.")
    return True


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

    _filename, ext = os.path.splitext(file)
    filepath, filename = os.path.split(_filename)

    return filepath, filename, ext
