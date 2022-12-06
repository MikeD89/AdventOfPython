# AoC 2022 - Day 6 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=6, year=2022)
testdata = get_testdata(day=6, year=2022)

def run(input, m):
    for i in range(len(input) - (m - 1)):
        block = input[i:i+m]
        if len(set(block)) == len(block):
            return i + m
    return 0

def part1():
    return run(data, 4)
   
def part2():
    return run(data, 14)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 6 --\n")
    part("One", 6, 2022, part1, True)
    part("Two", 6, 2022, part2, True)