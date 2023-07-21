#!/usr/bin/env python3
from functools import cache
import re
import cProfile
from math import inf
from typing import Tuple

file_name, y_val, ranging = 'input', 2000000, 4000000
# file_name, y_val, ranging = 'example', 10, 20

# caching slows down and high RAM usage...
# @cache
def manhattan_distance(ax: int, ay: int, bx: int, by: int) -> int:
    return abs(ax-bx)+abs(ay-by)

# with x, y = 0; radius = 2: (0, 2), (1, 1), (2, 0), (1, -1), (0, -2), (-1, -1), (-2, 0), (-1, 1)
def get_manhattan_circle(x: int, y: int, radius: int) -> set[Tuple[int, int]]:
    ret = set()
    for i in range(radius+1):
        test = radius-i
        ret.add((x+test, y+i))
        ret.add((x+test, y-i))
        ret.add((x-test, y+i))
        ret.add((x-test, y-i))
    return ret

sensor_beacon_pairs = set()
with open(file_name) as inp:
    # Parsing
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue

        match = re.compile(r'^Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$').match(line)

        if match is not None:
            sensor_x, sensor_y, beacon_x, beacon_y = match.groups()
            sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y) 
            sensor_beacon_pairs.add(((sensor_x, sensor_y), (beacon_x, beacon_y)))


# Part 1
not_possible = set()
for height in [y_val]:
    for sensor, beacon in sensor_beacon_pairs:
        dist = manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])

        if sensor[1] not in range(height-dist, height+dist+1):
            # sensor cannot reach that height anyway
            continue
        else:
            remaining = dist - abs(abs(sensor[1]) - abs(height))
            not_possible.add((height, (sensor[0]-remaining, sensor[0]+remaining)))

ranges = sorted(list(not_possible))
out1 = set()
for height, r in ranges:  # PERF this loop takes too long...
    for val in range(r[0], r[1]+1):
        # out1.add((height, val))
        out1.add((val, height))
for sensor, beacon in sensor_beacon_pairs:
    out1.discard(beacon)
print('Part 1:', len(out1))

# Part 2
out2 = None
point_visible = False
for sensor, beacon in sensor_beacon_pairs:
    to_test = set()  # clearing the set often makes some points checked multiple times, but this is fine, keeping all points exhausts my RAM
    dist = manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])
    to_test.update(get_manhattan_circle(sensor[0], sensor[1], dist+1))
    print('o', end='', flush=True)
    to_test = {t for t in to_test if t[0] in range(ranging+1) and t[1] in range(ranging+1)}
    print('O', end='', flush=True)
    point_visible = False
    print(f' will test {len(to_test)} points...', end='', flush=True)
    for point in to_test:  # PERF this also takes forever... lots of points
        for sensor, beacon in sensor_beacon_pairs:
            dist = manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])
            if manhattan_distance(sensor[0], sensor[1], point[0], point[1]) <= dist:  # point can be seen by some sensor
                point_visible = True
                break  # check next point
        if not point_visible:  # point was not seen by any sensor
            out2 = (point[0]*4000000) + point[1]
            print('Part 2:', out2)
            exit(0)
        point_visible = False
    print('x', flush=True)
