# AoC 2023 - Day 1 - Mike D
import sys
import inflect
import re
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=1, year=2023)
testdata = get_testdata(day=1, year=2023)

def do(line):
    first = ""
    last = ""
    for l in line:
        if l.isnumeric():
            first = l
            break
    for l in reversed(line):
        if l.isnumeric():
            last = l 
            break

    n = first+last 
    n = int(n)
    return n

def part1():
    input = data
    d = 0
    for line in input.splitlines():
        d+=do(line)
    return d
    
def part2():
    input = data
    d = 0
    p = inflect.engine()
    
    for line in input.splitlines():
        for n in range(1, 10):
            s = p.number_to_words(n)
            line = line.replace(s, s[:1] + str(n) + s[-2:])
    
        result = do(line)
        d+=result
    return d

if __name__ == "__main__":
    print("-- AoC 2023 - Day 1 --\n")
    part("One", 1, 2023, part1, True)
    part("Two", 1, 2023, part2, True)