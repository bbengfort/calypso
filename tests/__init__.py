# tests
# Testing for the calypso library
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Mar 16 10:02:20 2017 -0400
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the calypso library
"""

##########################################################################
## Imports
##########################################################################

import unittest


##########################################################################
## Module Constants
##########################################################################

TEST_VERSION = "0.1" # Also the expected version of the package


##########################################################################
## Imports
##########################################################################

class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        """
        Assert the world is sane and 4 / 2 == 2.
        """
        self.assertEqual(4/2, 2)

    def test_import(self):
        """
        Can import the calypso library
        """
        try:
            import calypso
        except ImportError:
            self.fail("unable to import the calypso library")

    def test_version(self):
        """
        Perform package/test version check
        """
        import calypso
        self.assertEqual(TEST_VERSION, calypso.__version__)
