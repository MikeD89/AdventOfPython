# AoC 2025 - Day 6 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=6, year=2025)
testdata = get_testdata(day=6, year=2025)

def calc(numbers, symbol):
    if len(numbers) > 0:
        calc = symbol.join(numbers)
        return eval(calc)
    return 0

def part1():
    input = data.splitlines()
    total = 0

    # pad
    longest_line = max([len(line) for line in input])
    input = [line.ljust(longest_line, " ") for line in input]

    numbers = []
    symbol = ""
    for i in range(len(input[0])):
        new_symbol = input[-1][i]
        if new_symbol != " ":
            total += calc(numbers, symbol)

            symbol = new_symbol
            # create empty list for each row
            numbers = ["" for _ in range(len(input)-1)]

        for j in range(len(input)-1):
            num = input[j][i]
            if num != " ":
                numbers[j] += num
    total += calc(numbers, symbol)
    return total
    
def part2():
    input = data.splitlines()
    total = 0

    # pad
    longest_line = max([len(line) for line in input])
    input = [line.ljust(longest_line, " ") for line in input]

    numbers = []
    symbol = ""
    for i in range(len(input[0])):
        new_symbol = input[-1][i]
        if new_symbol != " ":
            total += calc(numbers, symbol)
            symbol = new_symbol
            numbers = []

        new_number = ""
        for j in range(len(input)-1):
            num = input[j][i]
            if num != " ":
                new_number += num
        if new_number != "":
            numbers.append(new_number)
    total += calc(numbers, symbol)
    return total

if __name__ == "__main__":
    print("-- AoC 2025 - Day 6 --\n")
    part("One", 6, 2025, part1, True)
    part("Two", 6, 2025, part2, True)