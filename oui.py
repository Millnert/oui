#!/usr/bin/python3
"""Simple shell to use ouidb."""

import sys
from ouidb import OUIDB

if __name__ == '__main__':
    ODB = OUIDB()
    print(ODB.lookup(sys.argv[1]))
