import sys
from collections import defaultdict
from pprint import pprint


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


def sieve(x, bit_pos=0, bit_keep=None):
    if len(x) == 1:
        return x[0]
    t = {0: min, 1: max}
    pick = t[bit_keep]
    data = build_data(x)
    cur_bit = data[bit_pos]
    # Check for equal number of 0 and 1
    if len(set(cur_bit.values())) == 1:
        common_bit = bit_keep
    else:
        common_bit = pick(cur_bit, key=cur_bit.get)
    new_list = [i for i in x if i[bit_pos] == common_bit]
    return sieve(new_list, bit_pos=bit_pos + 1, bit_keep=bit_keep)


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

    with open(filename) as f:
        a = list(parse(f))
        res1 = sieve(a, bit_pos=0, bit_keep=1)
        print(res1)
        res2 = sieve(a, bit_pos=0, bit_keep=0)
        print(res2)
        res1_int = int("".join(map(str, res1)), 2)
        print(res1_int)
        res2_int = int("".join(map(str, res2)), 2)
        print(res2_int)
        print(res1_int * res2_int)


if __name__ == "__main__":
    main(sys.argv[1])
