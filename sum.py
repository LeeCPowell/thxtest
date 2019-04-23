#!/usr/bin/env python3
# Return sum of command line list of integers
import sys

try:
    assert len(sys.argv) > 1
except AssertionError:
    print('Enter list of integers to sum.')
else:
    try:
        result = sum(int(arg) for arg in sys.argv[1:])
        print('Sum total: ', result)
    except ValueError:
        print('List must contain only integers.')
