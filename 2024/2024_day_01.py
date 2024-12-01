# AoC 2024 - Day 1 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=1, year=2024)
testdata = get_testdata(day=1, year=2024)

def part1():
    input = data
    
    lines = input.splitlines()
    left = [int(l.split("   ")[0]) for l in lines]
    right = [int(l.split("   ")[1]) for l in lines]

    left = sorted(left)
    right = sorted(right)
    d = 0

    for i in range(len(left)):
        m = max(left[i], right[i])
        mm = min(left[i], right[i])

        d += m - mm

    return d
    
def part2():
    input = data

    lines = input.splitlines()
    left = [int(l.split("   ")[0]) for l in lines]
    right = [int(l.split("   ")[1]) for l in lines]

    d = 0

    for i in left:
        d += i * right.count(i)

    return d

if __name__ == "__main__":
    print("-- AoC 2024 - Day 1 --\n")
    part("One", 1, 2024, part1, False)
    part("Two", 1, 2024, part2, True)