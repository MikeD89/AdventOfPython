# AoC 2022 - Day 1 - Mike D
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from aocd import lines, get_day_and_year
from utils import *

# Handle data
d, y = get_day_and_year()
# data = get_data(day=1, year=2022)

def get_data():
    elves = []
    i = 0
    elves.append(0)
    for line in lines:
        if line == "":
            i += 1
            elves.append(0)
        else:
            elves[i] += int(line)
    return elves

# Run Part 1
def part1():
    # return the largest value from the array
    return max(get_data())
    
# Run Part 2
def part2():
    e = get_data()
    total = 0
    for _ in range(3):
        total += max(e)
        e.remove(max(e))
    
    return total

# Main 
if __name__ == "__main__":
    print("-- AoC 2022 - Day " + d + " --\n")
    part("One", 1, 2022, part1, True)
    part("Two", 1, 2022, part2, True)