# AoC 2022 - Day 4 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=4, year=2022)

testdata = [
"2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"]

def p1test(line, check):
    e1 = line.split(",")[0].split("-")
    e2 = line.split(",")[1].split("-")

    m = int(max(int(e1[0]), int(e1[1]), int(e2[0]), int(e2[1])))
    
    e1b =  [False] * (m)
    e2b =  [False] * (m)

    for i in range(int(e1[0]), int(e1[1])+1):
        e1b[i-1] = True

    for i in range(int(e2[0]), int(e2[1])+1):
        e2b[i-1] = True

    e1minuse2 = [a and not b for a, b in zip(e1b, e2b)]
    e2minuse1 = [a and not b for a, b in zip(e2b, e1b)]

    if(check):
        if not any(e1minuse2) or not any(e2minuse1):
            return True
    else:
        if e1b != e1minuse2 or e2b != e2minuse1:
            return True

    return False
    
    
def part1():
    s = 0
    for line in data.splitlines():
        if(p1test(line, True)):
            s += 1
    
    return s
    
def part2():
    s = 0
    for line in data.splitlines():
        if(p1test(line, False)):
            s += 1
    
    return s

def test_cases():
    for line in testdata:
        print(p1test(line, False))
    pass

if __name__ == "__main__":
    print("-- AoC 2022 - Day 4 --\n")
    tests(test_cases, True)
    part("One", 4, 2022, part1, True)
    part("Two", 4, 2022, part2, True)