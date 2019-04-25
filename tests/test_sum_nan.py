#!/usr/bin/env python3
# Test sum.py with non-integer input.

import subprocess

result = subprocess.check_output(["./../sum.py", "not", "a", "number"], universal_newlines=True)

assert result == 'List must contain only integers.\n'
