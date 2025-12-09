# AoC 2025 - Day 7 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=7, year=2025)
testdata = get_testdata(day=7, year=2025)

# def beam(data, row, col):
#     # dead beams fall off the sides
#     if col < 0 or col >= len(data[0]):
#         return 0
    
#     data[row][col] = "|"  # mark the beam path

#     # beam goes down a row - did it escape?
#     next_row = row + 1
#     if next_row >= len(data):
#         return 0
    
#     # does it hit a splitter?
#     next_cell = data[next_row][col]
#     if next_cell == "^":
#         return beam(data, next_row, col - 1) + beam(data, next_row, col + 1)
#     else:
#         return beam(data, next_row, col)
    
def beam_non_recursive(data, col):
    ongoing_beams = [0 for _ in range(len(data))]
    ongoing_beams[col] = 1

    for row in range(len(data)):
        for beam, count in enumerate(ongoing_beams):
            if count == 0:
                continue
            character = data[row][beam]
            if character == "^":
                # split the beam
                data[row][beam - 1] = "|"
                data[row][beam + 1] = "|"

                ongoing_beams[beam - 1] += ongoing_beams[beam]
                ongoing_beams[beam + 1] += ongoing_beams[beam]
                ongoing_beams[beam] = 0

            else:
                # continue the beam downward
                data[row][beam] = "|"


    return sum(ongoing_beams)

def find_splits(data):
    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "^" and data[r-1][c] == "|":
                count += 1
    return count

def part1():
    input = [list(line) for line in data.splitlines()]
    start_col = input[0].index("S")
    beam_non_recursive(input, start_col)
    return find_splits(input)
    
def part2():
    input = [list(line) for line in data.splitlines()]
    start_col = input[0].index("S")
    count = beam_non_recursive(input, start_col)
    return count

if __name__ == "__main__":
    print("-- AoC 2025 - Day 7 --\n")
    part("One", 7, 2025, part1, True)
    part("Two", 7, 2025, part2, True)