import sys
from collections import Counter, defaultdict


def parse(line):
    segments, time = line.split("|")
    segments = [sorted(s.strip()) for s in segments.split()]
    time = ["".join(sorted(t.strip())) for t in time.split()]
    return segments, time


def segment_search(scramble, time):
    mapping = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }
    mapping = {k: sorted(v) for k, v in mapping.items()}
    scramble = [sorted(i) for i in scramble]
    print(mapping)
    print(scramble)
    letter_counter = defaultdict(int)
    for k, v in mapping.items():
        for l in v:
            letter_counter[l] += 1
    new_letter_counter = defaultdict(int)
    for number in scramble:
        for l in number:
            new_letter_counter[l] += 1
    print(letter_counter)
    print(new_letter_counter)
    letter_mapping = {}
    for k, v in new_letter_counter.items():
        if v == 4:
            letter_mapping["e"] = k
        if v == 6:
            letter_mapping["b"] = k
        if v == 9:
            print(v)
            letter_mapping["f"] = k
    for word in scramble:
        if len(word) == 2:
            word.remove(letter_mapping["f"])
            letter_mapping["c"] = word[0]
    for k, v in new_letter_counter.items():
        if k != letter_mapping["c"] and v == 8:
            letter_mapping["a"] = k
    for word in scramble:
        if len(word) == 4:
            for l in ("b", "c", "f"):
                word.remove(letter_mapping[l])
            letter_mapping["d"] = word[0]
    for l in new_letter_counter:
        if l not in letter_mapping.values():
            letter_mapping["g"] = l
    new_mapping = defaultdict(list)
    for k, v in mapping.items():
        for l in v:
            new_mapping[k].append(letter_mapping[l])
    new_mapping = {k: "".join(sorted(v)) for k, v in new_mapping.items()}
    res = [str(k) for w in time for k, v in new_mapping.items() if w == v]
    res = int("".join(res))
    return res
    # return new_mapping


def main(filename):
    c = 0
    with open(filename) as f:
        for line in f:
            segs, time = parse(line)
            res = segment_search(segs, time)
            c += res
    print(c)


if __name__ == "__main__":
    main(sys.argv[1])
