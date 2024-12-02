# AoC 2024 - Day 2 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=2, year=2024)
testdata = get_testdata(day=2, year=2024)

def is_safe(report):
    direction = 1 if report[0] < report[1] else -1

    for i in range(len(report)-1):
        t = report[i]
        n = report[i+1]
        d = n - t

        if direction == 1 and d < 0:
            return False
        if direction == -1 and d > 0:
            return False
        if abs(d) > 3 or abs(d) < 1:
            return False
            
    return True


def is_safe_with_tolerance(report):
    varients = []
    for i in range(len(report)):
        var = report.copy()
        del var[i]
        varients.append(var)
            
    for var in varients:
        if is_safe(var):
            return True

    return False

def part1():
    input = data
    input = [i.split(" ") for i in input.splitlines()]
    input = [[int(j) for j in i] for i in input]

    input = [i for i in input if is_safe(i)]

    return len(input)
    
def part2():
    input = data
    input = [i.split(" ") for i in input.splitlines()]
    input = [[int(j) for j in i] for i in input]

    input = [i for i in input if is_safe_with_tolerance(i)]

    return len(input)

if __name__ == "__main__":
    print("-- AoC 2024 - Day 2 --\n")
    part("One", 2, 2024, part1, True)
    part("Two", 2, 2024, part2, True)