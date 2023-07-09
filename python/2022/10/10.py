#!/usr/bin/env python3
from functools import cache
import re

X = 1
cycle = 0
o = 0
pixels = [' ']*40*6
pixel_position = 0

def evaluate(o, pixel_position):
    if cycle == 20 or (cycle-20)%40 == 0:
        # print(f'Cycle {cycle}: X={X}')
        o += X*cycle
    if X in range((pixel_position%40)-1, (pixel_position%40)+2):
        pixels[pixel_position] = '󰝤'  # requires nerd font, otherwise use '#' or whatever
    return o, pixel_position+1


with open('input') as inp:
    o = 0
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
        if line == 'noop':
            cycle += 1
            o, pixel_position = evaluate(o, pixel_position)
        else:
            value = int(line.split(' ')[-1])
            cycle += 1
            o, pixel_position = evaluate(o, pixel_position)
            cycle += 1
            o, pixel_position = evaluate(o, pixel_position)
            X += value

    print('Part 1:', o)
    print('Part 2:')
    print(''.join(pixels[:40]))
    print(''.join(pixels[40:80]))
    print(''.join(pixels[80:120]))
    print(''.join(pixels[120:160]))
    print(''.join(pixels[160:200]))
    print(''.join(pixels[200:]))
