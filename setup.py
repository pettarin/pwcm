#!/usr/bin/env python
# coding=utf-8

"""
Test building a Python wheel with a C extension
that contains multiversioning code.
"""

from setuptools import Extension
from setuptools import setup

from setupmeta import PKG_AUTHOR
from setupmeta import PKG_AUTHOR_EMAIL
from setupmeta import PKG_CLASSIFIERS
from setupmeta import PKG_KEYWORDS
from setupmeta import PKG_LICENSE
from setupmeta import PKG_LONG_DESCRIPTION
from setupmeta import PKG_NAME
from setupmeta import PKG_PACKAGES
from setupmeta import PKG_PACKAGE_DATA
from setupmeta import PKG_SHORT_DESCRIPTION
from setupmeta import PKG_URL
from setupmeta import PKG_VERSION

__author__ = "Alberto Pettarin"
__email__ = "alberto@albertopettarin.it"
__copyright__ = "Copyright 2017, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__status__ = "Beta"
__version__ = "0.0.1"


EXTENSION = Extension(
    name="pwcm.cext",
    sources=[
        "pwcm/cfunc.cpp",
        "pwcm/cext.cpp"
    ],
    include_dirs=[]
)


setup(
    name=PKG_NAME,
    version=PKG_VERSION,
    packages=PKG_PACKAGES,
    package_data=PKG_PACKAGE_DATA,
    description=PKG_SHORT_DESCRIPTION,
    long_description=PKG_LONG_DESCRIPTION,
    author=PKG_AUTHOR,
    author_email=PKG_AUTHOR_EMAIL,
    url=PKG_URL,
    license=PKG_LICENSE,
    keywords=PKG_KEYWORDS,
    classifiers=PKG_CLASSIFIERS,
    ext_modules=[EXTENSION]
)
