# AoC 2022 - Day 8 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=8, year=2022)
testdata = get_testdata(day=8, year=2022)

def parse(input):
    out = []
    for line in input.splitlines():
        o = []
        for c in line:
            i = int(c)
            o.append(i)
        out.append(o)

    return out

def test_dir(x, y, xD, yD, g):
    og_v = g[y][x]
    count = 0
    while True:
        x += xD
        y += yD

        if x >= len(g[0]) or y >= len(g) or x < 0 or y < 0:
            break

        count += 1
        v = g[y][x]
        if v < og_v:
            continue

        return False, count
    return True, count

def test_cell(x, y, g):
    return any([test_dir(x, y, -1, 0, g)[0],
                test_dir(x, y, 1, 0, g)[0],
                test_dir(x, y, 0, -1, g)[0],
                test_dir(x, y, 0, 1, g)[0]])
                    
def score_tree(x, y, g):
    return test_dir(x, y, -1, 0, g)[1] * \
           test_dir(x, y, 1, 0, g)[1] * \
           test_dir(x, y, 0, -1, g)[1] * \
           test_dir(x, y, 0, 1, g)[1]
                          

def count_visible(g):
    count = 0
    for y in range(len(g)):
        for x in range(len(g[0])):
            if test_cell(x, y, g):
                count += 1
    return count

def part1():
    g = parse(data)
    return count_visible(g)
    
def part2():
    g = parse(data)
    return max([x for x in [score_tree(x, y, g) for y in range(len(g)) for x in range(len(g[0]))]])

if __name__ == "__main__":
    print("-- AoC 2022 - Day 8 --\n")
    part("One", 8, 2022, part1, True)
    part("Two", 8, 2022, part2, True)