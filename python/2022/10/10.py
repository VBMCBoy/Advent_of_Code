#!/usr/bin/env python3

from typing import Tuple


X = 1
cycle = 0
out1 = 0
pixels = [' ']*40*6
pixel_position = 0

def evaluate(out1: int, pixel_position: int) -> Tuple[int, int]:
    if cycle == 20 or (cycle-20)%40 == 0:
        # print(f'Cycle {cycle}: X={X}')
        out1 += X*cycle
    if X in range((pixel_position%40)-1, (pixel_position%40)+2):
        pixels[pixel_position] = '󰝤'  # requires nerd font, otherwise use '#' or whatever
    return out1, pixel_position+1


with open('input') as inp:
    out1 = 0
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
        if line == 'noop':
            cycle += 1
            out1, pixel_position = evaluate(out1, pixel_position)
        else:
            value = int(line.split(' ')[-1])
            cycle += 1
            out1, pixel_position = evaluate(out1, pixel_position)
            cycle += 1
            out1, pixel_position = evaluate(out1, pixel_position)
            X += value

    print('Part 1:', out1)
    print('Part 2:')
    print(''.join(pixels[:40]))
    print(''.join(pixels[40:80]))
    print(''.join(pixels[80:120]))
    print(''.join(pixels[120:160]))
    print(''.join(pixels[160:200]))
    print(''.join(pixels[200:]))
