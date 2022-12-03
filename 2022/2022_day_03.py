# AoC 2022 - Day 3 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *
data = get_data(day=3, year=2022)

def score(c: str):
    uC = c.upper()
    if uC == c:
        return string.ascii_uppercase.index(c) + 27
    else:
        return string.ascii_lowercase.index(c) + 1

def process(lines):
    s = set()
    for line in lines:
        for char in line:
            s.add(char)

    for char in s:
        inline = [char in line for line in lines]
        if all(inline):
            return score(char)

# Run Part 1
def part1():
    total = 0
    for line in data.splitlines():
        s = int(len(line) / 2)
        total += process([line[:s], line[s:]])
    return total    
    
# Run Part 2
def part2():
    lines = data.splitlines()
    total = 0

    for i in range(0, len(lines), 3):
        total += process(lines[i:i+3])
    return total

# Main 
if __name__ == "__main__":
    print("-- AoC 2022 - Day 3 --\n")
    part("One", 3, 2022, part1, True)
    part("Two", 3, 2022, part2, True)