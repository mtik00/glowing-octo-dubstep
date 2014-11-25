#!/usr/bin/env python
"""This module is used to provide functionality to
`python -m SAMPLEPROJDIRNAME`

By default, it will print out the module name, version, and location.
"""
from __future__ import print_function
from os import path
import sys


if __name__ == '__main__':
    # Read the version from our project
    this_directory = path.abspath(path.dirname(__file__))
    package_dir = path.join(this_directory, "..")
    sys.path.insert(0, package_dir)
    from SAMPLEPROJDIRNAME import __version__

    print("running [{0}] version [{1}] from [{2}]".format(
        "SAMPLEPROJDIRNAME", __version__, this_directory))
