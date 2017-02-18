#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import sys

__author__ = "Alberto Pettarin"
__email__ = "alberto@albertopettarin.it"
__copyright__ = "Copyright 2017, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__status__ = "Beta"
__version__ = "0.0.1"


MAP = {
    0: "default",
    1: "SSE1",
    2: "SSE2",
    3: "SSE3",
    40: "SSE4a",
    41: "SSE4.1",
    42: "SSE4.2"
}


def main():
    try:
        from pwcm.cext import dosomething
        v = dosomething()
        if v not in MAP:
            print("[ERRO] C++ extension returned the unknown value: %d" % v)
        else:
            print("[INFO] C++ extension returned the known value: %s" % MAP[v])
    except Exception as e:
        print("[ERRO] Unable to run C++ extension. Exception raised:")
        print(e)
    sys.exit(0)


if __name__ == "__main__":
    main()
