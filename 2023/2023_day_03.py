# AoC 2023 - Day 3 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

dirs = [
        [-1, -1], [ 0, -1], [ 1, -1],
        [-1,  0], [ 0,  0], [ 1,  0],
        [-1,  1], [ 0,  1], [ 1,  1],
      ]

data = get_data(day=3, year=2023)
testdata = get_testdata(day=3, year=2023)

def find_nums(input):
    grid = load_into_default_dict(input, '.')
    nums = []

    num = None
    valid = False
    
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            # start of a number
            if char.isdigit():
                num = char if num is None else num + char
            else:
                # is it end of number?
                if num is not None and valid:
                    nums.append(int(num))
                valid = False
                num = None

            # check surrounding numbers
            if num is not None and not valid:
                for dir in dirs:
                    other = grid[y + dir[1]][x + dir[0]]
                    if not other.isnumeric() and other != ".":
                        valid = True
    return nums



def find_gears(input):
    grid = load_into_default_dict(input, '.')
    gears = defaultdict(lambda: [])

    num = None
    valid = None
    
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            # start of a number
            if char.isdigit():
                num = char if num is None else num + char
            else:
                # is it end of number?
                if num is not None and valid is not None:
                    gears[valid].append(int(num))
                valid = None
                num = None

            # check surrounding numbers
            if num is not None and valid is None:
                for dir in dirs:
                    other = grid[y + dir[1]][x + dir[0]]
                    if other == "*":
                        valid = (y + dir[1], x + dir[0])
    return gears


def part1():
    input = data.splitlines()
    n = find_nums(input)
    return sum(n)

    
def part2():
    input = data.splitlines()
    gears = find_gears(input)
    sum = 0
    for gear in gears:
        nums = gears[gear]
        if len(nums) == 2:
            sum += (nums[0] * nums[1])
    return sum

if __name__ == "__main__":
    print("-- AoC 2023 - Day 3 --\n")
    part("One", 3, 2023, part1, True)
    part("Two", 3, 2023, part2, True)