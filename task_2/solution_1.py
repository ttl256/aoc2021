import sys
from operator import add, sub
from collections import namedtuple


def parse(x):
    for line in x:
        action, value = line.strip().split()
        yield action, int(value)


def destination(x):
    move = namedtuple("move", ["direction", "change"])
    move_desc = {
        "forward": move("distance", add),
        "up": move("depth", sub),
        "down": move("depth", add),
    }
    dst = {"distance": 0, "depth": 0}
    for action, value in x:
        realm = move_desc[action]
        dst[realm.direction] += realm.change(0, value)

    return dst


def main(filename):
    with open(filename) as f:
        print(destination(parse(f)))


if __name__ == "__main__":
    main(sys.argv[1])
