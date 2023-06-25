#!/usr/bin/env python3
from functools import cache
import re

with open('example') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
