import sys
from collections import defaultdict


def life(x: dict[int, int], days):
    for day in range(days):
        tmp = defaultdict(int)
        for state, num in x.items():
            # Update 6 and 8, also clear 0
            if state == 0:
                tmp[6] += num
                tmp[8] += num
            # Move one life cycle down
            else:
                tmp[state - 1] += num
        yield sum(tmp.values())
        x = tmp


def main(filename):
    with open(filename) as f:
        data = list(map(int, f.read().split(",")))
    # Build initial dict with key = current cycle, value = number of members
    d = defaultdict(int)
    for f in data:
        d[f] += 1
    # Run through all days and get num of fish in the last day
    days = 256
    for num in life(d, days):
        res = num
    print(res)


if __name__ == "__main__":
    main(sys.argv[1])
