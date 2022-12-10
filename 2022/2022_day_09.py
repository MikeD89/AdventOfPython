# AoC 2022 - Day 9 - Mike D
import math
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=9, year=2022)
testdata = get_testdata(day=9, year=2022)

def tail_move(last, knot):
    dX = last[0] - knot[0]
    dY = last[1] - knot[1]

    if abs(dX) > 1 or abs(dY) > 1:
        mX = 0 if dX is 0 else -1 if dX < 0 else 1
        mY = 0 if dY is 0 else -1 if dY < 0 else 1
        return [knot[0] + mX, knot[1] + mY]
    else:
        return knot

def head_move(knot, c):
    x, y = knot[0], knot[1]
    if c == 'R':
        x += 1
    elif c == 'L':
        x -= 1
    elif c == 'U':
        y += 1
    elif c == 'D':
        y -= 1
    return [x, y]

def intr(c, l, knots, pos):
    for i in range(l):
        for (i, knot) in enumerate(knots):
            if i == 0:
                knots[i] = head_move(knot, c)
            else:
                last = knots[i - 1]
                knots[i] = tail_move(last, knot)
            
            if i == len(knots) - 1:
                pos.add(tuple(knots[i]))

def run(input, k):
    knots = [[0, 0]] * (k + 1)
    pos = set()
    pos.add((0, 0))

    for line in input.splitlines():
        c, l = line[0], int(line[1:])
        intr(c, l, knots, pos)

    return len(pos)

def part1():
    return run(data, 1)
    
def part2():
    return run(data, 9)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 9 --\n")
    part("One", 9, 2022, part1, True)
    part("Two", 9, 2022, part2, True)