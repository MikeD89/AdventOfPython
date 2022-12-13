# AoC YEAR - Day DAY - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=DAY, year=YEAR)
testdata = get_testdata(day=DAY, year=YEAR)

def part1():
    input = testdata
    return None
    
def part2():
    input = testdata
    return None

if __name__ == "__main__":
    print("-- AoC YEAR - Day DAY --\n")
    part("One", DAY, YEAR, part1, False)
    part("Two", DAY, YEAR, part2, False)