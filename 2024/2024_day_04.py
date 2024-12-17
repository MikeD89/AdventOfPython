# AoC 2024 - Day 4 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=4, year=2024)
testdata = get_testdata(day=4, year=2024)

dirs = [[-1, -1], [-1, +0], [-1, +1], 
        [+0, -1],           [+0, +1], 
        [+1, -1], [+1, +0], [+1, +1]]

wanted = "XMAS"

def in_range(input, x, y):
    if y < 0 or y >= len(input):
        return False
    if x < 0 or x >= len(input[0]):
        return False
    return True

def doXmasCheck(input, x, y, d):
    s = ""
    for i in range(len(wanted)):
        if not in_range(input, x, y):
            return False
        
        if input[x][y] == wanted[len(s)]:
            s += input[x][y]
            x += d[0]
            y += d[1]
        else:
            return False
    return True

def part1():
    c = 0
    input = data
    input = [[y for y in x] for x in input.split("\n")]
    for x in range (len(input)):
        for y in range (len(input[0])): 
            for d in dirs:
                if doXmasCheck(input, x, y, d):
                    c += 1
              
            
    return c

one = [[-1, -1], [+1, +1]]
two = [[-1, +1], [+1, -1]]
b = [one, two]

def doXXmasCheck(input, x, y):
    if input[x][y] == "A":
        for bb in b:
            s = []
            for dir in bb:
                xx = x + dir[0]
                yy = y + dir[1]
                if not in_range(input, xx, yy):
                    return False
                s += input[xx][yy]
            
            if "M" not in s or "S" not in s:
                return False
    else:
        return False

    return True

def part2():
    d = 0
    input = data
    input = [[y for y in x] for x in input.split("\n")]
    for x in range (len(input)):
        for y in range (len(input[0])): 
            if doXXmasCheck(input, x, y):
                d += 1
    return d

if __name__ == "__main__":
    print("-- AoC 2024 - Day 4 --\n")
    part("One", 4, 2024, part1, True)
    part("Two", 4, 2024, part2, True)