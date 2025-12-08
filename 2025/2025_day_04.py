# AoC 2025 - Day 4 - Mike D
import sys
import os
import string
import numpy as np
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

kernel = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),       (0, 1),
              (1, -1),  (1, 0),  (1, 1)]
margin = 1

data = get_data(day=4, year=2025)
testdata = get_testdata(day=4, year=2025)

def process_grid(padded_grid, remove=True):
    count = 0
    for y in range(margin, len(padded_grid) - margin):
        for x in range(margin, len(padded_grid[y]) - margin):
            if padded_grid[y][x] != '@':
                continue
            kernel_characters = [padded_grid[y+dy][x+dx] for dy, dx in kernel]
            sum_kernel = sum([1 for c in kernel_characters if c == '@'])
            if sum_kernel < 4:
                count += 1
                if remove:
                    padded_grid[y][x] = '#'
    return count

def part1():
    input = data
    # turn input into a grid
    grid = [list(line) for line in input.splitlines()]
    padded_grid = np.pad(grid, pad_width=margin, mode='constant', constant_values='.')
    return process_grid(padded_grid, remove=False)
    
def part2():
    input = data
    # turn input into a grid
    grid = [list(line) for line in input.splitlines()]
    padded_grid = np.pad(grid, pad_width=margin, mode='constant', constant_values='.')
    count = 0

    while True:
        prev_count = count
        count += process_grid(padded_grid)
        if count == prev_count:
            break 
   
    return count

if __name__ == "__main__":
    print("-- AoC 2025 - Day 4 --\n")
    part("One", 4, 2025, part1, True)
    part("Two", 4, 2025, part2, True)