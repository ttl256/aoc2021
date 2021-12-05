import sys
from dataclasses import dataclass
from itertools import repeat
from collections import namedtuple


Point = namedtuple("Point", "x y")


class Vent:
    def __init__(self, coords: list[Point, Point]):
        coords.sort(reverse=True)
        self.coords = coords
        self.span = self.get_span()

    def get_span(self):
        end, start = self.coords
        diff = Point(x=end.x - start.x, y=end.y - start.y)
        if diff.x == 0:
            ax = repeat(0)
        else:
            ax = (1 if diff.x > 0 else -1 for i in range(abs(diff.x)))
        if diff.y == 0:
            ay = repeat(0)
        else:
            ay = (1 if diff.y > 0 else -1 for i in range(abs(diff.y)))
        inc_vector = zip(ax, ay)
        span = []
        span.append(start)
        bx = start.x
        by = start.y
        for ix, iy in inc_vector:
            bx += ix
            by += iy
            span.append(Point(x=bx, y=by))

        return span


def parse(x):
    for line in x:
        ps = [Point(*map(int, s.strip().split(","))) for s in line.split("->")]
        yield ps


def max_val(x):
    res = 0
    for i in x:
        t = max(max(i))
        if t > res:
            res = t
    return res


def main(filename):
    with open(filename) as f:
        vents_raw = list(parse(f))
    l = max_val(vents_raw)
    # st_p = [[a, b] for a, b in vents_raw if a.x == b.x or a.y == b.y]
    grid = [0 for i in range((l + 1) * (l + 1))]
    vents = [Vent(i) for i in vents_raw]
    a = [i.get_span() for i in vents]
    for vent in a:
        for p in vent:
            grid[l * p.y + p.x] += 1
    res = sum(1 for i in grid if i >= 2)
    print(res)


if __name__ == "__main__":
    main(sys.argv[1])
