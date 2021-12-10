import sys


def score_corrupted(line):
    match = {")": "(", "]": "[", "}": "{", ">": "<"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    stack = []
    for c in line:
        if c in match.values():
            stack.append(c)
        elif c in match:
            last_left = stack[-1]
            if last_left == match[c]:
                stack.pop()
            else:
                return points[c]
    else:
        return 0


def score_incomplete(line):
    match = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for c in line:
        if c in match.values():
            stack.append(c)
        elif c in match:
            last_left = stack[-1]
            if last_left == match[c]:
                stack.pop()
            else:
                return
    # If we didn't return till now then the string isn't corrupted
    # and we have a stack filled with left-side brackets
    # Now mirror the stack to get right-side brackets
    else:
        points = {")": 1, "]": 2, "}": 3, ">": 4}
        # stack = ((<{
        reverse_match = {v: k for k, v in match.items()}
        # reversed(stack) -> {<((
        right_stack = [reverse_match[i] for i in reversed(stack)]
        # right_stack = }>))
        total = 0
        for i in right_stack:
            total *= 5
            total += points[i]
        return total


def main(filename):
    # Part 1
    with open(filename) as f:
        res = sum(score_corrupted(line) for line in f)
    print(res)
    # Part 2
    with open(filename) as f:
        l = []
        for i in f:
            res = score_incomplete(i)
            if res:
                l.append(res)
    l.sort()
    print(l[len(l) // 2])


if __name__ == "__main__":
    main(sys.argv[1])
