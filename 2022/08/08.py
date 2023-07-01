#!/usr/bin/env python3
from functools import cache
import re

trees = []
max_x = 0  # use as in range(0, max_x)
max_y = 0

def is_visible(x: int, y: int) -> bool:
    tree = trees[y][x]
    if x == 0 or y == 0 or x == max_x-1 or y == max_y-1:
        return True

    # right
    if max(trees[y][x+1:], default=-1) < tree:
        return True
    if max(trees[y][:x], default=-1) < tree:
        return True
    if max([row[x] for row in trees[:y]], default=-1) < tree:
        return True
    if max([row[x] for row in trees[y+1:]], default=-1) < tree:
        return True
    return False


def score(x: int, y: int) -> int:
    res = 1
    tree = trees[y][x]
    # right
    distance = 0
    for t in trees[y][x+1:]:
        distance += 1
        if t >= tree:
            break
    res *= distance

    # left
    distance = 0
    for t in reversed(trees[y][:x]):
        distance += 1
        if t >= tree:
            break
    res *= distance

    # up
    distance = 0
    for t in reversed([row[x] for row in trees[:y]]):
        distance += 1
        if t >= tree:
            break
    res *= distance

    # down
    distance = 0
    for t in [row[x] for row in trees[y+1:]]:
        distance += 1
        if t >= tree:
            break
    res *= distance

    return res


with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
        trees.append([int(t) for t in line])
        max_x = len(line)
    max_y = len(trees)

    i = 0
    max_score = 0
    for y, row in enumerate(trees):
        for x, col in enumerate(row):
            i += 1 if is_visible(x, y) else 0
            max_score = max(score(x, y), max_score)

    print('Part 1', i)

    print('Part 2', max_score)
