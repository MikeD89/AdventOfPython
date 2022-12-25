# AoC 2022 - Day 25 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=25, year=2022)
testdata = get_testdata(day=25, year=2022)

def parse(line):
    v = 0
    p = 1
    for c in reversed(line):

        if c == "0":
            v += 0
        elif c == "1":
            v += p
        elif c == "2":
            v += (p * 2)
        elif c == "-":
            v -= 1 * p
        elif c == "=":
            v -= 2 * p

        p *= 5
    return v


def reverse(p: int):
    lookup = {0: "0", 1: "1", 2: "2", 3: '=', 4: "-"}

    v = []
    while p:
        r = p % 5
        p = p // 5
        if r == 3:
            p += 1
        elif r == 4:
            p += 1
        v.append(lookup[r])

    return "".join(reversed(v))

def part1():
    v = [parse(line) for line in data.splitlines()]
    print(sum(v))
    s = sum(v)
    return reverse(s)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 25 --\n")
    part("One", 25, 2022, part1, True)