# AoC 2025 - Day 3 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=3, year=2025)
testdata = get_testdata(day=3, year=2025)

def part1():
    input = data
    total = 0
    for bank in input.splitlines():
        max_index = 0
        max_jolt = 0
        for index, jolt in enumerate(bank[:-1]):
            if int(jolt) > max_jolt:
                max_index = index
                max_jolt = int(jolt) 

        max_num = int(str(max_jolt) + "0")
        for i in range(max_index+1, len(bank)):
            max_num = max(max_num, int(str(max_jolt) + bank[i]))

        total += max_num
    
    return total
    
def part2():
    input = data
    required_size = 12
    total = 0
    for bank in input.splitlines():
        stack = []
        for index, str_jolt in enumerate(bank):
            # pop the crud off the stack
            jolt = int(str_jolt)

            while True:
                can_delete = len(stack) > 0
                required_to_add = required_size - len(stack)
                remaining_to_check = len(bank) - index
                safe_to_delete = remaining_to_check - required_to_add > 0

                if can_delete and stack[-1] < jolt and safe_to_delete:
                    stack.pop()
                else:
                    break

            # add the new value, if there is room
            if len(stack) + 1 <= required_size:
                stack.append(jolt)

        total += int("".join([str(s) for s in stack]))
    
    return total

if __name__ == "__main__":
    print("-- AoC 2025 - Day 3 --\n")
    part("One", 3, 2025, part1, True)
    part("Two", 3, 2025, part2, True)