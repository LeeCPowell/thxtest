#!/usr/bin/env python3
# Test sum.py with a list of integers.

import subprocess

result = subprocess.check_output(["./../sum.py", "2", "3", "4"], universal_newlines=True)

assert result == 'Sum total:  9\n'
