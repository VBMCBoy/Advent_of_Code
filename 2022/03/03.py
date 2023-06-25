#!/usr/bin/env python3

out1 = 0
out2 = 0
stack = []

def prio(c: str) -> int:
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38

with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue

        rucksack1 = set(line[:len(line)//2])
        rucksack2 = set(line[len(line)//2:])

        duplicates = rucksack1.intersection(rucksack2)

        for dup in duplicates:
            if dup.islower():
                out1 += prio(dup)
            else:
                out1 += prio(dup)


        stack.append(line)
        if len(stack) == 3:
            item = set(stack[0]).intersection(stack[1], stack[2])
            assert len(item) == 1
            item = item.pop()
            out2 += prio(item)
            stack = []

    print('Part 1', out1)
    print('Part 2', out2)
