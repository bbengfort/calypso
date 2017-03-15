#!/usr/bin/env python
# setup
# Setup script for installing calypso
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Wed Mar 15 12:56:08 2017 -0400
#
# Copyright (C) 2015 University of Maryland
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Setup script for installing calypso
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

# Read the __init__.py file for version info
version = None
versfile = os.path.join(os.path.dirname(__file__), "pleiades", "__init__.py")
with open(versfile, 'r') as versf:
    exec(versf.read(), namespace)
    version = namespace['get_version']()

## Discover the packages
packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures", "register", "notebooks"))

## Load the requirements
requires = []
with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())

## Define the classifiers
classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
)

## Define the keywords
keywords = ('calypso', 'workload', 'filesystem')

## Define the description
long_description = ""

## Define the configuration
config = {
    "name": "Calypso",
    "version": version,
    "description": "A read/write workload generator that creates lorem ipsum text documents.",
    "long_description": long_description,
    "license": "MIT",
    "author": "Benjamin Bengfort",
    "author_email": "bengfort@cs.umd.edu",
    "url": "https://github.com/bbengfort/calypso",
    "download_url": 'https://github.com/bbengfort/calypso/tarball/v%s' % version,
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "keywords": keywords,
    "zip_safe": True,
    "scripts": ['calypso.py'],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
