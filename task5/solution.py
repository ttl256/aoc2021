import sys
from pprint import pprint
from itertools import repeat
from collections import namedtuple
from collections import defaultdict


Point = namedtuple("Point", "x y")


class Vent:
    def __init__(self, coords: list[Point, Point]):
        coords.sort(reverse=True)
        self.coords = coords
        self.span = self.get_span()

    def get_span(self):
        end, start = self.coords
        diff = Point(x=end.x - start.x, y=end.y - start.y)
        if max(abs(diff.x), abs(diff.y)) == 0:
            span = self.coords
        else:
            dx = (
                repeat(0)
                if diff.x == 0
                else (1 if diff.x > 0 else -1 for i in range(abs(diff.x)))
            )
            dy = (
                repeat(0)
                if diff.y == 0
                else (1 if diff.y > 0 else -1 for i in range(abs(diff.y)))
            )
            span = []
            span.append(start)
            sx, sy = start.x, start.y
            for ix, iy in zip(dx, dy):
                sx += ix
                sy += iy
                span.append(Point(sx, sy))

        return span


def parse(x):
    for line in x:
        ps = [Point(*map(int, s.strip().split(","))) for s in line.split("->")]
        yield ps


def main(filename):
    with open(filename) as f:
        vents_raw = parse(f)
        spans = (Vent(i).get_span() for i in vents_raw)
        d = defaultdict(int)
        for span in spans:
            for point in span:
                d[point] += 1

    print(sum(1 for v in d.values() if v >= 2))


if __name__ == "__main__":
    main(sys.argv[1])
