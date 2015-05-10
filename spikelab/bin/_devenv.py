# Insert the project root directory to the module search path.
# This script is intended to be imported from the script wrappers
# inside this directory.


import os
import sys


def _devenv():
    bindir = os.path.dirname(sys.argv[0])
    projectdir = os.path.dirname(bindir)
    sys.path.insert(0, projectdir)


_devenv()
