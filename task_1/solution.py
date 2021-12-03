import sys
from math import inf


def is_increases(x):
        a, b = inf, 0
        for i in x:
            b = int(i)
            if b > a:
                yield True
            a = b


def window(x, window_size=None):
    window = []
    for i in x:
        window.append(int(i))
        if len(window) == window_size:
            yield sum(window)
            del window[0]


def main(filename):
    with open(filename) as f:
        task1_1 = sum(is_increases(f))
    with open(filename) as f:
        task1_2 = sum(is_increases(window(f, window_size=3)))
    print(task1_1)
    print(task1_2)


if __name__ == "__main__":
    main(sys.argv[1])

