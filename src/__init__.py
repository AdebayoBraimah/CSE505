# -*- coding: utf-8 -*-
#
# Adebayo Braimah
# Stony Brook University, Dept. of Computer Science
#
# Copyright 2024 Stony Brook University
#
# TODO: <LICENCSE HERE>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Project python package for CSE 505 project using ErgoAI.

..autosummary::
    ergoai
    kg
    utils
"""

import os
import sys

# TODO: Need to find a way to automate this
#   rather than hard coding this.
#
# Define constants
ERGOROOT: str = (
    "/Users/adebayobraimah/bin/ErgoEngine-3.0_release/ErgoAI/Coherent/ERGOAI_3.0/ErgoAI"
)
XSBARCHDIR: str = (
    "/Users/adebayobraimah/bin/ErgoEngine-3.0_release/ErgoAI/Coherent/ERGOAI_3.0/XSB/config/aarch64-apple-darwin22.6.0"
)

# Append ERGO ROOT directory to system path
sys.path.append(ERGOROOT.replace("\\", "/") + "/python")


__author__ = "Adebayo Braimah"
__credits__ = [
    "Adebayo Braimah",
    "Stony Brook University",
    "Stony Brook University, Dept. of Computer Science",
]
__license__ = "<LICENSE HERE>"
__version__ = "0.0.1"
__maintainer__ = "Adebayo Braimah"
__email__ = "adebayo.braimah@stonybrook.edu"
__status__ = "Development"
