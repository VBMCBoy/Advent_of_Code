#!/usr/bin/env python3
from functools import cache
import re
from useful.dijkstra import DijkstraSolver, Node

with open('example') as inp:
    for y, line in enumerate(inp.readlines()):
        line = line.strip()
        if line == '':
            continue

        start = None
        target = None
        for x, c in enumerate(line):
            if c == 'S':
                start = Node((x, y))


