#!/usr/bin/env python3
# Test sum.py with null input.

import subprocess

result = subprocess.check_output(["./../sum.py"], universal_newlines=True)

assert result == 'Enter list of integers to sum.\n'
