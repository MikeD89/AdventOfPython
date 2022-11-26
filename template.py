# AoC YEAR - Day DAY - Mike D
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from aocd import get_data, submit
from utils import *

# Handle data
data = get_data(day=DAY, year=YEAR)

def print_data():
    print(data)

# Run Part 1
def part1():
    return None
    
# Run Part 2
def part2():
    return None

# Main 
if __name__ == "__main__":
    print("-- AoC YEAR - Day DAY --\n")
    part("One", DAY, YEAR, part1, False)
    part("Two", DAY, YEAR, part2, False)