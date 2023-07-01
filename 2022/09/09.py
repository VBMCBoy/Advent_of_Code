#!/usr/bin/env python3
from functools import cache
import re
from typing import Tuple

with open('input') as inp:
    for LENGTH in [2, 10]:
        rope: list[Tuple[int, int]] = [(0, 0)]*LENGTH
        tail_positions = set()
        tail_positions.add(tuple([0, 0]))

        inp.seek(0) # necessary if we want to read twice
        for line in inp.readlines():
            line = line.strip()
            if line == '':
                continue
            direction, count = line.split(' ')
            count = int(count)

            # rope movement
            for _ in range(count):
                if direction == 'R':
                    rope[0] = (rope[0][0] + 1, rope[0][1])
                elif direction == 'L':
                    rope[0] = (rope[0][0] - 1, rope[0][1])
                elif direction == 'U':
                    rope[0] = (rope[0][0], rope[0][1] + 1)
                elif direction == 'D':
                    rope[0] = (rope[0][0], rope[0][1] - 1)
                else:
                    raise ValueError

                # [(4, 2), (3, 0)]
                # print('start:', rope)
                for i, knot in enumerate(rope):
                    if i == 0:
                        continue
                    previous = rope[i-1]
                    if abs(knot[0] - previous[0]) in [0, 1] and abs(knot[1] - previous[1]) in [0, 1]: # close enough, don't move
                        continue
                    if previous[0] == knot[0]: # x axis is the same, only approach on y
                        if knot[1] < previous[1]:
                            knot = (knot[0], knot[1] + 1)
                        elif knot[1] > previous[1]:
                            knot = (knot[0], knot[1] - 1)
                    elif previous[1] == knot[1]:  # y axis is the same, only approach on x
                        if knot[0] < previous[0]:
                            knot = (knot[0] + 1, knot[1])
                        elif knot[0] > previous[0]:
                            knot = (knot[0] - 1, knot[1])
                    else:  # no axes match
                        # first check how to move x
                        if knot[0] < previous[0]:
                            knot = (knot[0] + 1, knot[1])
                        elif knot[0] > previous[0]:
                            knot = (knot[0] - 1, knot[1])
                        # then check how to move y
                        if knot[1] < previous[1]:
                            knot = (knot[0], knot[1] + 1)
                        elif knot[1] > previous[1]:
                            knot = (knot[0], knot[1] - 1)

                    rope[i] = knot
                # print('now:', rope)

                tail_positions.add(rope[-1])


        print('Rope length:', LENGTH, 'Unique tail positions:', len(tail_positions))
