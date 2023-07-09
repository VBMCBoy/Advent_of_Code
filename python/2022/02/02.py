#!/usr/bin/env python3
case1 = {
        ('A', 'X'): 3 + 1,
        ('A', 'Y'): 6 + 2,
        ('A', 'Z'): 0 + 3,
        ('B', 'X'): 0 + 1,
        ('B', 'Y'): 3 + 2,
        ('B', 'Z'): 6 + 3,
        ('C', 'X'): 6 + 1,
        ('C', 'Y'): 0 + 2,
        ('C', 'Z'): 3 + 3,
        }

case2 = {
        ('A', 'X'): 0 + 3,
        ('A', 'Y'): 3 + 1,
        ('A', 'Z'): 6 + 2,
        ('B', 'X'): 0 + 1,
        ('B', 'Y'): 3 + 2,
        ('B', 'Z'): 6 + 3,
        ('C', 'X'): 0 + 2,
        ('C', 'Y'): 3 + 3,
        ('C', 'Z'): 6 + 1,
        }

score1 = 0
score2 = 0
with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
        opponent = line[0]
        reaction = line[2]
        score1 += case1[(opponent, reaction)]
        score2 += case2[(opponent, reaction)]


    print('Part 1', score1)
    print('Part 2', score2)
