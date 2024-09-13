#!/usr/bin/env python3
import sys

# The mapper takes an input, processes it line by line, 
# and outputs key-value pairs
for line in sys.stdin:
    lin = line.strip()
    words = line.split()

    for word in words:
        print(f'{word}\t1')

    