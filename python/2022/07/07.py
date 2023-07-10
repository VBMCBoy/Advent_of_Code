#!/usr/bin/env python3

class Element():
    def get_size(self) -> int:
        self.parent = None
        self.children = []
        raise NotImplemented

class Directory(Element):
    def __init__(self, name: str, parent: Element | None) -> None:
        if name != '/' and parent is None:
            raise ValueError(f'Tried to create item with name {name} and no parent.')

        self.size = 0
        self.name = name
        self.children = []
        self.parent = parent

    def add_child(self, item: Element):
        self.children.append(item)

    def get_size(self) -> int:
        return sum([c.get_size() for c in self.children])

class File(Element):
    def __init__(self, size: int, name: str, parent: Element) -> None:
        self.size = size
        self.name = name
        self.parent = parent
        self.children = None

    def get_size(self) -> int:
        return self.size

root_dir = Directory('/', None)
current_dir = root_dir

with open('input') as inp:
    for line in inp.readlines():
        line = line.strip()
        if line == '':
            continue

        if line == '$ cd /':
            current_dir = root_dir
        elif line.startswith('dir '):
            current_dir.children.append(Directory(name=line.replace('dir ', ''), parent=current_dir))
        elif line == '$ cd ..':
            if current_dir.parent:
                current_dir = current_dir.parent
        elif line.startswith('$ cd '):
            current_dir = [d for d in current_dir.children if d.name == line.replace('$ cd ', '')][0]
        elif line == '$ ls':
            pass
        else:
            size, name = line.split(' ')
            current_dir.children.append(File(size=int(size), name=name, parent=current_dir))

    dirs = [root_dir]
    out1 = 0
    REQUIRED_SPACE = 30000000 - (70_000_000 - root_dir.get_size())
    out2 = root_dir.get_size()
    while dirs:
        d = dirs.pop()
        if type(d) == Directory and d.get_size() <= 100_000:
            out1 += d.get_size()
        if type(d) == Directory and d.get_size() >= REQUIRED_SPACE:
            out2 = min(out2, d.get_size())
        if d.children:
            dirs += d.children

    print(out1)
    print(out2)



