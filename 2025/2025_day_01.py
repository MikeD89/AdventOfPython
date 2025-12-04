# AoC 2025 - Day 1 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=1, year=2025)
testdata = get_testdata(day=1, year=2025)

def part1():
    input = data
    a = 50
    r = 0
    for line in input.splitlines():
        if line.startswith("L"): 
            a -= int(line[1:])
        else:
            a += int(line[1:])
        a = a % 100
        if a == 0:
            r += 1
    return r
    
def part2():
    input = data
    a = 50
    r = 0
       
    for line in input.splitlines():
        diff = int(line[1:])
        for i in range(diff):
            if line.startswith("L"): 
                a -= 1
            else:
                a += 1

            a = a % 100
            if a == 0:
                r += 1
    return r

if __name__ == "__main__":
    print("-- AoC 2025 - Day 1 --\n")
    part("One", 1, 2025, part1, False)
    part("Two", 1, 2025, part2, True)