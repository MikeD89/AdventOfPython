# AoC 2025 - Day 5 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=5, year=2025)
testdata = get_testdata(day=5, year=2025)

def process_input(input):
    ranges = []
    numbers = []
    finding_ranges = True
    for line in input.splitlines():
        if line == "":
            finding_ranges = False
            continue
        if finding_ranges:
            ranges.append(line.split("-"))
        else:
            numbers.append(line)
    return ranges, numbers

def part1():
    input = data
    ranges, numbers = process_input(input)
    count = 0
    for num in numbers:
        num_value = int(num)
        for r in ranges:
            low = int(r[0])
            high = int(r[1])
            if low <= num_value <= high:
                count += 1 
                break
    return count

def part2():
    input = data
    ranges, _ = process_input(input)

    starts = [(int(r[0]), +1) for r in ranges]
    ends = [(int(r[1]), -1) for r in ranges]
    all = sorted(starts + ends, key=lambda r: int(r[0]))

    start = -1
    active = 0

    merged_ranges = []
    for i in range(len(all)):
        value = all[i][0]
        delta = all[i][1]
        if active == 0:
            start = value
        
        active += delta
        if active == 0:
            merged_ranges.append((start, value))

    count = 0
    for r in merged_ranges:
        count += (r[1] - r[0] + 1)
    return count

if __name__ == "__main__":
    print("-- AoC 2025 - Day 5 --\n")
    part("One", 5, 2025, part1, True)
    part("Two", 5, 2025, part2, True)