from pprint import pprint
import sys
from dataclasses import dataclass, field
from collections import namedtuple
import itertools
from typing import TextIO
import numpy as np

Coords = namedtuple("Coords", "x y")


@dataclass(order=True)
class Point:
    coords: Coords
    value: int
    neighbors: set[Coords] = field(default_factory=set, compare=False, hash=False)
    flashed: bool = field(default=False, compare=False, hash=False)

    def add_neighbor(self, v: Coords):
        self.neighbors.add(v)


@dataclass
class Graph:
    points: dict[Coords, Point] = field(default_factory=dict)
    flashes = 0

    def __str__(self):
        my = max(pn.y for pn in self.points) + 1
        mx = max(pn.x for pn in self.points) + 1
        l = [0 for y in range(my) for x in range(mx)]
        for pn, po in self.points.items():
            l[my * pn.y + pn.x] = po.value
        l = np.array(l)
        l = l.reshape([my, mx])
        s = ["".join(map(str, r)) for r in l]
        return "\n".join(s)

    def add_point(self, point: Point):
        self.points[point.coords] = point

    def add_edge(self, u: Coords, v: Coords):
        if u and v in self.points:
            self.points[u].add_neighbor(v)
            self.points[v].add_neighbor(u)

    def one(self):
        for p in self.points:
            self.points[p].value += 1

    def flash(self):
        for pn, po in self.points.items():
            if po.value > 9:
                stack = []
                stack.append(pn)
                visited = set()
                while len(stack) > 0:
                    cp = stack.pop()
                    if cp in visited:
                        continue
                    self.points[cp].value = 0
                    self.points[cp].flashed = True
                    self.flashes += 1
                    visited.add(cp)
                    for n in self.points[cp].neighbors:
                        if not self.points[n].flashed:
                            self.points[n].value += 1
                            if self.points[n].value > 9:
                                stack.append(n)

    def flash_reset(self):
        for p in self.points:
            self.points[p].flashed = False

    def total_flashes(self):
        self.flashes = 0


def parse(f: TextIO):
    for line in f:
        yield [int(i) for i in line.strip()]


def main(filename):
    with open(filename) as f:
        rows = list(parse(f))
    # Build graph
    g = Graph()
    for idy, y in enumerate(rows):
        for idx, x in enumerate(y):
            g.add_point(Point(Coords(idx, idy), value=x))
    for pn, po in g.points.items():
        for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if (dx, dy) != (0, 0):
                g.add_edge(pn, Coords(pn.x + dx, pn.y + dy))

    steps = 0
    while True:
        g.one()
        g.flash()
        g.flash_reset()
        steps += 1
        if g.flashes == len(g.points):
            break
        else:
            g.total_flashes()

    print(g)
    print(g.flashes)
    print(steps)


if __name__ == "__main__":
    main(sys.argv[1])
