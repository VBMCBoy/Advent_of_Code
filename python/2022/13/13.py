#!/usr/bin/env python3
from functools import cmp_to_key
from enum import Enum
import ast


class Result(Enum):
    CORRECT = 1,
    WRONG = 2,
    CONTINUE = 3

def compare(left: list | int, right: list | int) -> Result:
    if left == right:
        return Result.CONTINUE
    # both int: lower should come first, if equal: continue
    if type(left) == int and type(right) == int:
        if left < right:
            return Result.CORRECT
        elif left > right:
            return Result.WRONG
        else:
            return Result.CONTINUE

    # if one is int and other list: convert int to list
    if type(left) == int and type(right) == list:
        return compare([left], right)

    if type(left) == list and type(right) == int:
        return compare(left, [right])

    if type(left) == list and type(right) == list:
        for i, item in enumerate(left):
            try:
                c = compare(item, right[i])
                if c != Result.CONTINUE:
                    return c
            except:
                if len(left) < len(right):
                    return Result.CORRECT
                elif len(left) > len(right):
                    return Result.WRONG
        if len(left) < len(right):
            return Result.CORRECT
        elif len(left) > len(right):
            return Result.WRONG
        else:
            return Result.CONTINUE
    raise ValueError('how did we get here?')

with open('input') as inp:
    a, b = None, None
    lines = [[[2]], [[6]]]
    i = 1
    ret1 = 0
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            a, b = None, None
            continue

        line = ast.literal_eval(line)
        if a is None:
            a = line
        else:
            b = line
        lines.append(line)
        if a is not None and b is not None:
            if type(a) in [list, int] and type(b) in [list, int]:
                c = compare(a, b)
                if c == Result.CORRECT:
                    ret1 += i

                i += 1
    print('Part 1:', ret1)

    conversion = {
            Result.CORRECT: -1,
            Result.WRONG: 1,
            Result.CONTINUE: 0,
            }
    lines.sort(key=cmp_to_key(lambda a, b: conversion[compare(a, b)]))
    print('Part 2:', (lines.index([[2]])+1) * (lines.index([[6]])+1))
