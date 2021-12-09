import sys
from collections import namedtuple, defaultdict
from typing import NamedTuple
from operator import mul
from functools import reduce

Point = namedtuple("Point", "x y")


class Data(NamedTuple):
    val: int
    neighbors: list


def parse(x):
    for line in x:
        yield list(map(int, line.strip()))


# def basin_size(neigbors, d, a):
#     if all(True if d[i].val == 9 else False for i in neigbors):
#         return 1
#     for n in neigbors:


def main(filename):
    with open(filename) as f:
        grid = [i for i in parse(f)]
    # print(grid)
    d = defaultdict(Data)
    for idr, r in enumerate(grid):
        for idc, c in enumerate(r):
            val = c
            my_row = [
                Point(i, idr) for i in range(len(r)) if i == idc - 1 or i == idc + 1
            ]
            my_column = [
                Point(idc, i) for i in range(len(grid)) if i == idr - 1 or i == idr + 1
            ]
            d[Point(idc, idr)] = Data(val, my_row + my_column)
    lows = {}
    for p, v in d.items():
        val, neighbors = v
        if val < min(d[n].val for n in neighbors):
            lows[p] = v

    a = defaultdict(list)
    for p, v in lows.items():
        # val, neighbors = v
        stack = [p]
        visited = set()
        while len(stack) > 0:
            cp = stack.pop()
            v1, n1 = d[cp]
            if cp in visited:
                continue
            visited.add(cp)
            a[p].append((cp, v1))
            for n in n1:
                if d[n].val == 9:
                    continue
                if d[n].val > v1:
                    stack.append(n)
                    print(stack)
    print(a)
    b = [len(v) for k, v in a.items()]
    b = sorted(b, reverse=True)
    print(reduce(mul, b[:3]))


if __name__ == "__main__":
    main(sys.argv[1])
