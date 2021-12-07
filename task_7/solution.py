import sys
from collections import defaultdict


def main(filename):
    with open(filename) as f:
        points = [int(i) for i in f.read().split(",")]
    weight = defaultdict(int)
    for point in points:
        weight[point] += 1

    fuel = {}
    for a in range(max(weight)):
        fuel[a] = sum(
            ((1 + (abs(a - b))) * (abs(a - b)) // 2) * v
            for b, v in weight.items()
            if a != b
        )

    # print(fuel)
    print(min(fuel.values()))


if __name__ == "__main__":
    main(sys.argv[1])
