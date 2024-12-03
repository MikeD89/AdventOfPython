# AoC 2024 - Day 3 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *
import re

data = get_data(day=3, year=2024)
testdata = get_testdata(day=3, year=2024)

def mul(a,b):
    return a * b

def part1():
    input = data
    reg = "mul\([0-9]+,[0-9]+\)"
    result = re.findall(reg, input)
    d = 0
    for r in result:
        d += eval(r)
        
    return d
    
def part2():
    input = data
    reg = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
    result = re.findall(reg, input)
    d = 0
    dd = True
    for r in result:
        if r == "do()":
            dd = True
        elif r == "don't()":
            dd = False
        elif dd:
            d += eval(r)
    return d

if __name__ == "__main__":
    print("-- AoC 2024 - Day 3 --\n")
    part("One", 3, 2024, part1, True)
    part("Two", 3, 2024, part2, True)