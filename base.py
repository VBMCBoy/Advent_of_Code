#!/usr/bin/env python3
from functools import cache
import re
import cProfile

with open('example') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
