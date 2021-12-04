import sys
from collections import defaultdict


def parse(x):
    for i in x:
        yield [int(i) for i in i.strip()]


def bit_dict():
    return defaultdict(int)


def build_data(x):
    """
    {0: {0: m0, 1: n0},
     1: {0: m1, 1: n1},
     2: {0: m2, 1: n2},
     3: {0: m3, 1: n3}, ... }
    """
    d = defaultdict(bit_dict)
    for item in x:
        # item = [1, 0, 1, 1, 0]
        for idx, bit in enumerate(item):
            d[idx][bit] += 1
    return d


def main(filename):
    with open(filename) as f:
        data = build_data(parse(f))
        """
        gamma rate - most common bit
        epsilon rate - least common bit
        """
        # binary rates
        gamma_rate = [max(bit_dict, key=bit_dict.get) for pos, bit_dict in data.items()]
        epsilon_rate = [
            min(bit_dict, key=bit_dict.get) for pos, bit_dict in data.items()
        ]
        # int rates
        gamma_rate_int = int("".join(map(str, gamma_rate)), 2)
        epsilon_rate_int = int("".join(map(str, epsilon_rate)), 2)

        print(f"{gamma_rate=}, {gamma_rate_int=}")
        print(f"{epsilon_rate=}, {epsilon_rate_int=}")
        print(gamma_rate_int * epsilon_rate_int)


if __name__ == "__main__":
    main(sys.argv[1])
