#!/usr/bin/env python3
import re

out1 = 0
out2 = 0
with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
        r = re.compile(r'^(\d+)-(\d+),(\d+)-(\d+)$')
        m = r.match(line)
        assert m is not None
        a1, a2, b1, b2 = m.groups()
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

        if (a1 in range(b1, b2+1) and a2 in range(b1, b2+1)
            or b1 in range(a1, a2+1) and b2 in range(a1, a2+1)):
            out1+=1

        if (a1 in range(b1, b2+1) or a2 in range(b1, b2+1)
            or b1 in range(a1, a2+1) or b2 in range (a1, a2+1)):
            out2 += 1


    print('Part 1', out1)
    print('Part 2', out2)
