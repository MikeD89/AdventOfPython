# AoC 2025 - Day 2 - Mike D
import sys
import os
import string
import re
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=2, year=2025)
testdata = get_testdata(day=2, year=2025)

def part1():
    input = testdata
    input = input.split(",")
    total_invalid_count = 0
    total_invalid_total = 0
    for line in input:
        invalid_count = 0
        invalid_total = 0
        lower = line.split("-")[0]
        upper = line.split("-")[1]
        for i in range(int(lower), int(upper) + 1):
            l = len(str(i)) // 2
            lh = str(i)[:l]
            rh = str(i)[l:]
            if lh == rh:
                invalid_total += 1
                invalid_count += i
        # print(line, invalid_count, invalid_total)
        total_invalid_count += invalid_count
        total_invalid_total += invalid_total
    return total_invalid_count
    
def part2():
    input = data
    input = input.split(",")
    regex = re.compile(r"^([0-9]{1,})(\1{1,})$",  re.MULTILINE)
   
    invalid_count = 0
    for line in input:
        lower = line.split("-")[0]
        upper = line.split("-")[1]
        strs = []
        for i in range(int(lower), int(upper) + 1):
            strs.append(str(i))
            
        matches = regex.finditer("\n".join(strs))
        for match in matches:
            invalid_count += int(match.group())
    return invalid_count

if __name__ == "__main__":
    print("-- AoC 2025 - Day 2 --\n")
    part("One", 2, 2025, part1, False)
    part("Two", 2, 2025, part2, False)