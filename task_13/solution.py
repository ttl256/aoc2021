import sys
from collections import namedtuple
import numpy as np


Point = namedtuple("Point", "x y")


def print_list(l):
    s = []
    for r in l:
        t = ["#" if i == 1 else "." for i in r]
        s.append(t)
    s1 = ["".join(r) for r in s]
    return "\n".join(s1)


def fold_horizontal(xs: list, y: int):
    top = xs[:y]
    bot = reversed(xs[y + 1 :])
    for idy, tb in enumerate(zip(top, bot)):
        tr, br = tb
        tmc = []
        for idx, tbc in enumerate(zip(tr, br)):
            tc, bc = tbc
            top[idy][idx] = tc or bc
    return top


def fold_vertical(xs: list, x: int):
    left = [row[:x] for row in xs]
    right = [row[x + 1 :] for row in xs]
    for idy, lr in enumerate(zip(left, right)):
        l, r = lr
        r = reversed(r)
        for idx, lrc in enumerate(zip(l, r)):
            lc, rc = lrc
            left[idy][idx] = lc or rc
    return left


def main(fpoints, ffolds):
    with open(fpoints) as f:
        points = [Point(*map(int, line.strip().split(","))) for line in f]
    print(points)
    l = []
    for row in range(max(p.y for p in points) + 1):
        l.append(
            [
                1 if Point(i, row) in points else 0
                for i in range(max(p.x for p in points) + 1)
            ]
        )
    print(print_list(l))
    with open(ffolds) as f:
        for line in f:
            s, v = line.strip().split("=")
            if "x" in s:
                l = fold_vertical(l, int(v))
            if "y" in s:
                l = fold_horizontal(l, int(v))
    print(print_list(l))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
