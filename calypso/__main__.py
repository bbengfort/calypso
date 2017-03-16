# calypso.__main__
# Command line utility for the calypso app. Also the module main entry point.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Mar 16 10:35:35 2017 -0400
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __main__.py [] benjamin@bengfort.com $

"""
Command line utility for the calypso app. Also the module main entry point.
"""

##########################################################################
## Imports
##########################################################################

import argparse

from .version import get_version


##########################################################################
## Utility Definition
##########################################################################

PROG         = "calypso"
DESCRIPTION  = "A read/write file system workload generator"
EPILOG       = "If there are any bugs or comments, submit an issue on GitHub"
COMMANDS     = {
    'generate': {

    },
}


##########################################################################
## Main Method
##########################################################################

def main(traceback=False):
    # Create the argument parser
    parser = argparse.ArgumentParser(
        prog=PROG, description=DESCRIPTION, epilog=EPILOG,
    )

    # Add the version argument
    parser.add_argument('-v', '--version', action='version', version=get_version())

    # Parse the arguments
    args = parser.parse_args()
    try:
        print("done")z
    except Exception as e:
        parser.error(str(e))


if __name__ == '__main__':
    main()
