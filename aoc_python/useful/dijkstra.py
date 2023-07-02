from typing import Any, List, Tuple
from math import inf
from copy import deepcopy


class Node():
    def __init__(self, content: Any) -> None:
        self.content = content

    def __eq__(self, __value: object) -> bool:
        return self.content == __value

    def __lt__(self, __value: object) -> bool:
        return self.content < __value

    def __gt__(self, __value: object) -> bool:
        return self.content > __value

class DijkstraSolver():
    def __init__(self, vertices: set[Node], edges: set[Tuple[Node, Node, int]]) -> None:
        self.vertices = vertices
        self.edges = edges

        self.randknoten = set()
        self.pfade = dict()
        self.distanzen = dict()


    def add_node(self, node: Node, edges: set[Tuple[Node, Node, int]]) -> None:
        self.vertices.add(node)
        self.edges |= edges

    # TODO maybe cache this?
    def get_path(self, start: Node, end: Node) -> List[Node] | None:
        self.distanzen[start] = {node: inf for node in self.vertices}
        self.distanzen[start][start] = 0

        p = dict()
        p[start] = start
        U = deepcopy(self.vertices)
        R = set()
        R.add(start)


        while R:
            u = min(U, key=lambda x: self.distanzen[start][x])
            U.remove(u)
            R.remove(u)

            for conn in set([e for e in self.edges if e[0] == u]):
                v = conn[1]
                if self.distanzen[start][u] + conn[2] < self.distanzen[start][v]:
                    self.distanzen[start][v] = self.distanzen[start][u] + conn[2]
                    p[v] = u
                    R.add(v)

        ret = [end]
        current = end
        while current is not start:
            if current == None:
                return None
            ret.insert(0, p[start][current])
            current = p[start][current]
        return ret

