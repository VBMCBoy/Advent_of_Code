#!/usr/bin/env python3
from functools import cache
import re

with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue

        for i, SIZE in enumerate([4, 14]):
            start = SIZE
            while len(set(line[start-SIZE:start])) != SIZE:
                start += 1

            print(f'Part {i+1}', start)
