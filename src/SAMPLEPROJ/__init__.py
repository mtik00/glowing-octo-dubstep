#!/usr/bin/env python
"""
This module does awesome stuff!

Example::

    >>> from __future__ import print_function
    >>> from SAMPLEPROJ import f1
    >>> f1(1)
    >>>
"""
# Imports ######################################################################
from __future__ import print_function
from SAMPLEPROJ.logger import get_logger

# Metadata #####################################################################
__author__ = "Timothy McFadden"
__date__ = "99/99/9999"
__copyright__ = "Timothy McFadden, 2014"
__license__ = "MIT"
__version__ = "1.0.0dev"


# Globals ######################################################################
def f1(something):
    print("Hello World!", something)
    get_logger().critical("Hello again")
