Contributing to ``src``
====================================

This document is adapted from `https://git.fmrib.ox.ac.uk/fsl/fslpy/-/blob/master/doc/contributing.rst <https://git.fmrib.ox.ac.uk/fsl/fslpy/-/blob/master/doc/contributing.rst>`_        

Created by Paul McCarthy

**NOTE**: This document is a work in progress.

Development model
-----------------


* All development occurs on the ``main`` branch.


Commit messages
---------------


To aid readability, all commit messages should be prefixed with one or more of
the following labels (these conventions were inherited from: `nibabel <https://github.com/nipy/nibabel>`_, and `NumPy <https://numpy.org/devdocs/dev/development_workflow.html>`_):
               
  * **BF**    : Bug fix              
  * **RF**    : Refactoring
  * **ENH**   : Enhancement/new feature
  * **BW**    : Addresses backward-compatibility
  * **OPT**   : Optimization (performance improvements)
  * **BK**    : Breaks something and/or tests fail
  * **PL**    : Making pylint happier
  * **DOC**   : For all kinds of documentation related commits
  * **TEST**  : For adding or changing tests
  * **MNT**   : For administrative/maintenance changes
  * **CI**    : For continuous-integration changes
  * **STY**   : Commits that do not affect the meaning (white-space, formatting, missing semi-colons, etc), but change the style.
  * **BLD**   : Commits that affect build components such as build tool, ci pipeline, dependencies, project version etc.
  * **OPS**   : Commits that affect operational components like infrastructure, deployment, backup, recovery etc.
  * **CHORE** : Miscellaneous commits (e.g. modifying .gitignore)
  * **API**   : An (incompatible) API change
  * **DEV**   : Development tool or utility
  * **REV**   : Revert an earlier commit
  * **TYP**   : Static typing


Breaking Changes Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Breaking changes should be indicated by an ``!`` before the ``:`` in the subject line e.g. ``ENH!: remove status endpoint``.


Testing
-------


Unit and integration tests are currently run with ``github workflows``, ``pytest`` and
``coverage`` (**However, this is not yet implemented**).
