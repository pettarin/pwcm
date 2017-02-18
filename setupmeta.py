#!/usr/bin/env python
# coding=utf-8

"""
Metadata for setting the pwcm package up
"""

import io

__author__ = "Alberto Pettarin"
__email__ = "alberto@albertopettarin.it"
__copyright__ = "Copyright 2017, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__status__ = "Beta"
__version__ = "0.0.1"


##############################################################################
#
# you might need to edit the information below this line
#
##############################################################################

# package version
# NOTE: generate a new one for each PyPI upload, otherwise it will fail
PKG_VERSION = "0.0.1"

# required packages to install
# NOTE: always use exact version numbers
# NOTE: this list should be the same as requirements.txt
PKG_INSTALL_REQUIRES = []

# required packages to install extra tools
PKG_EXTRAS_REQUIRE = {}

# packages to be distributed
PKG_PACKAGES = [
    "pwcm",
]

# data files to be distributed
# NOTE: .py files will be added automatically
PKG_PACKAGE_DATA = {
    "pwcm": [
        "*.cpp",
        "*.h",
        "*.md"
    ],
}

# scripts to be installed globally
# on Linux and Mac OS X, use the file without extension
# on Windows, use the file with .py extension
PKG_SCRIPTS = []

##############################################################################
#
# do not edit the metadata below this line
#
##############################################################################

# package name
PKG_NAME = "pwcm"

# package author
PKG_AUTHOR = "Alberto Pettarin"

# package author email
PKG_AUTHOR_EMAIL = "alberto@albertopettarin.it"

# package URL
PKG_URL = "https://github.com/pettarin/pwcm"

# package license
PKG_LICENSE = "MIT"

# human-readable descriptions
PKG_SHORT_DESCRIPTION = """A minimal working example of
C++ function multiversioning in Python wheels."""
try:
    PKG_LONG_DESCRIPTION = io.open("README.rst", "r", encoding="utf-8").read()
except:
    PKG_LONG_DESCRIPTION = PKG_SHORT_DESCRIPTION

# PyPI keywords
PKG_KEYWORDS = [
    "C",
    "Python wheel",
    "Python",
    "function multiversioning",
    "function",
    "gcc",
    "multiversion function"
    "multiversion",
    "multiversioning",
    "wheel",
]

# PyPI classifiers
PKG_CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: C",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
