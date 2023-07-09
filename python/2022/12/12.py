#!/usr/bin/env python3
from functools import cache
import re
from useful.dijkstra import DijkstraSolver, Node


def get_height(x, y, data) -> int:
    item = data[y][x]
    if item == 'S':
        item = 'a'
    elif item == 'E':
        item = 'z'
    return ord(item)

with open('input') as inp:
    start, target = None, None
    max_y, max_x = 0, 0
    data = []
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue
        data.append(line)

    solver = DijkstraSolver()
    print('Reading data...')
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == 'S':
                start = Node((x, y))
                solver.add_node(Node((x, y)))
                print('start', start)
            elif c == 'E':
                target = Node((x, y))
                solver.add_node(Node((x, y)))
                print('target', target)
            else:
                solver.add_node(Node((x, y)))

    print('Generating connections...')
    for vert in solver.vertices:
        pos = vert.content
        for v_ in [(pos[0],     pos[1] + 1),
                   (pos[0] + 1, pos[1]),
                   (pos[0],     pos[1] - 1),
                   (pos[0] - 1, pos[1])]:
            if v_ in solver.vertices:
                if get_height(v_[0], v_[1], data) in range(get_height(pos[0], pos[1], data)+2):
                    solver.add_edge(start=vert, end=Node(v_))


    print('Calculating path (Part 1)...')
    if start is not None and target is not None:
        path = solver.get_path_ucs(start, [target], only_length=True)
        if path is not None:
            print('Part 1:', path)
        else:
            print('Part 1: No path found!')
            exit(1)

    print('Calculating path (Part 2)...')
    start_points = {node for node in solver.vertices
                    if get_height(node.content[0], node.content[1], data) == ord('a')}
    to_remove = set()
    for s in start_points:
        if s.content[0] != 131 \
        and (get_height(s.content[0] + 1, s.content[1], data) == ord('c') \
        or get_height(s.content[0] + 1, s.content[1], data) == ord('a')):
            to_remove.add(s)
    start_points -= to_remove
    print(len(start_points), 'possible starting points')
    skip_points = set()
    best = None
    if target is not None:
        while start_points:
            print(len(start_points), 'remaining...')
            p = start_points.pop()

            path = solver.get_path_ucs(start=p, targets=[target], only_length=False)
            if path and type(path) == list:
                if not best:
                    best = path
                else:
                    if len(path) < len(best):
                        best = path

                if best == path:  # only check if there are shorter paths on this path if we replaced it
                    for node in path[1:]:
                        if get_height(node.content[0], node.content[1], data) == ord('a'):
                            start_points.remove(node)
                            # if we find additional starting points on this path, use these as starting point instead, that path will always be shorter
                            # and don't recalculate from those points
                            if best and len(best) > len(path[path.index(node):]):
                                best = path[path.index(node):]
                                print('found better...')
    if best is not None:
        print('Part 2:', len(best)-1)
    else:
        print('Part 2: No path found!')

