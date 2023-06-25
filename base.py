#!/usr/bin/env python3

with open('example') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
