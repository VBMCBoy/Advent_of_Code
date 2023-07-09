#!/usr/bin/env python3
from copy import deepcopy
from functools import cache
import re
import cProfile
from typing import Tuple
from math import inf

# return None when falling is infinite
def get_next_pos(point: Tuple[int, int], stationary: set[Tuple[int, int]], max_y: float = inf, max_y_is_floor: bool = False) -> Tuple[int, int] | None:
    if point in stationary:
        raise ValueError(f'Point {point} is in stationary!')
    x, y = point

    if y+1 == max_y and not max_y_is_floor:  # check infinite fall
        return None
    elif y+1 == max_y and max_y_is_floor:  # floor is now directly below
        return (x, y)
    elif (x, y+1) not in stationary:  # check down
        return (x, y+1)
    elif (x-1, y+1) not in stationary:  # check down, left
        return (x-1, y+1)
    elif (x+1, y+1) not in stationary:  # check down, right
        return (x+1, y+1)
    else:  # comes to rest
        return (x, y)

stationary = set()
START_POINT = (500, 0)
max_y = 0
with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue

        stone_path = line.split(' -> ')
        startx, starty = stone_path.pop(0).split(',')
        while stone_path:
            endx, endy = stone_path.pop(0).split(',')
            startx, starty, endx, endy = int(startx), int(starty), int(endx), int(endy)
            for x in range(min(startx, endx), max(startx, endx)+1):
                for y in range(min(starty, endy), max(starty, endy)+1):
                    stationary.add((x, y))
                    max_y = max(max_y, y)
            startx, starty = endx, endy

    out1 = 0
    gone_infinite = False
    stationary_bak = deepcopy(stationary)
    while not gone_infinite:
        sand = START_POINT
        while True:
            new_point = get_next_pos(sand, stationary, max_y+2)
            if new_point == sand:
                stationary.add(new_point)
                out1 += 1
                break
            elif new_point == None:
                gone_infinite = True
                break
            else:
                sand = new_point
    print('Part 1:', out1)

    out2 = 0
    stuck = False
    stationary = stationary_bak
    while not stuck:
        sand = START_POINT
        while True:
            new_point = get_next_pos(sand, stationary, max_y+2, max_y_is_floor=True)
            if new_point == START_POINT:
                stuck = True
                break
            elif new_point == sand:
                stationary.add(new_point)
                out2 += 1
                break
            elif new_point == None:
                gone_infinite = True
                break
            else:
                sand = new_point
    print('Part 2:', out2+1)

