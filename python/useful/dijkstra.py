from typing import Any, Dict, Iterable, List
from math import inf
from heapq import heappush, heappop, heapify


class Node():
    def __init__(self, content: Any) -> None:
        self.content = content

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Node:
            return self.content == __value.content
        return self.content == __value

    def __lt__(self, __value: object) -> bool:
        if type(__value) == Node:
            return self.content < __value.content
        return self.content < __value

    def __gt__(self, __value: object) -> bool:
        if type(__value) == Node:
            return self.content > __value.content
        return self.content > __value

    def __hash__(self) -> int:
        return self.content.__hash__()

    def __str__(self) -> str:
        return f'Node:{self.content}'

    def __repr__(self) -> str:
        return self.__str__()


class Edge():
    def __init__(self, start: Node, end: Node, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self) -> str:
        return f'Edge[{self.start} -> {self.end} {self.weight}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Edge:
            return self.start == __value.start and self.end == __value.end and self.weight == __value.weight
        else:
            return self == __value

    def __hash__(self) -> int:
        return hash((self.start, self.end, self.weight))


class DijkstraSolver():
    def __init__(self) -> None:
        self.vertices = set()
        self.edges = set()
        self.neighbors = dict()

    def add_node(self, node: Node) -> None:
        self.vertices.add(node)
        self.neighbors[node] = set()

    def add_edge(self, start: Node, end: Node, weight: int = 1):
        if type(start) != Node:
            raise ValueError(f'start: expected Node, but got {type(start)}')
        if type(end) != Node:
            raise ValueError(f'end: expected Node, but got {type(end)}')
        if start not in self.vertices:
            raise ValueError(f'start: Node is not in vertices')
        if end not in self.vertices:
            raise ValueError(f'end: Node is not in vertices')

        self.edges.add(Edge(start, end, weight))
        self.neighbors[start].add((end, weight))

    def get_path_ucs(self, start: Node, targets: Iterable[Node], only_length: bool = False) -> List[Node] | float | None:
        distances: Dict[Node, float] = {node: inf for node in self.vertices}
        distances[start] = 0.0

        prev: Dict[Node, Node | None] = {node: None for node in self.vertices}
        prev[start] = start

        Q = [(distances[start], start)]
        heapify(Q)

        end = None

        while Q:
            p, u = heappop(Q)
            if p != distances[u]:
                continue
            if u in targets:
                end = u

            # for conn in set([e for e in self.edges if e.start == u and e.end in self.vertices]):
            for v, weight in self.neighbors[u]:
                alt = distances[u] + weight
                if alt < distances[v]:
                    distances[v] = alt
                    prev[v] = u
                    heappush(Q, (alt, v))

        # now we have dist, prev
        if end:
            ret = [end]
            current = end
            if only_length:
                return distances[end]

            while current is not start:
                if current == None or current not in prev.keys():
                    return None
                else:
                    ret.insert(0, prev[current])
                current = prev[current]
            return ret
        else:
            return None


