#!/usr/bin/env python3

elves = [0]
with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            elves.append(0)
        else:
            elves[-1] += int(line)


    print('Part 1', max(elves))

    print('Part 2', sum(sorted(elves)[-3:]))
