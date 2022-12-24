# AoC 2022 - Day 22 - Mike D
import sys
import os
import string
import re
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=22, year=2022)
testdata = get_testdata(day=22, year=2022)

facing = ["R", "D", "L", "U"]

def parse(input):
    code = input.splitlines()[-2:][1]
    maze = input.splitlines()[:-2]
    
    longest = max([len(line) for line in maze])
    grid = make_grid(longest, len(maze), " ")

    start = None

    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == "." and start is None:
                start = (x, y)
            grid[y][x] = char

    return grid, code, start

def rotate(direction, turn):
    if turn == "R":
        return facing[(facing.index(direction) + 1) % 4]
    else:
        return facing[(facing.index(direction) + 3) % 4]

def get_print_char(direction):
    if direction == "R":
        return ">"
    elif direction == "L":
        return "<"
    elif direction == "U":
        return "^"
    elif direction == "D":
        return "v"

def handle_coord_wrapping(coord, grid, direction):
    if direction == "R":
        if coord[0] >= len(grid[0]) or grid[coord[1]][coord[0]] == " ":
            for x in range(0, len(grid[0])):
                if grid[coord[1]][x] != " ":
                    coord = (x, coord[1])
                    break

    elif direction == "L":
        if coord[0] < 0 or grid[coord[1]][coord[0]] == " ":
            for x in range(len(grid[0]) - 1, -1, -1):
                if grid[coord[1]][x] != " ":
                    coord = (x, coord[1])
                    break

    elif direction == "U":
        if coord[1] < 0 or grid[coord[1]][coord[0]] == " ":
            for y in range(len(grid) - 1, -1, -1):
                if grid[y][coord[0]] != " ":
                    coord = (coord[0], y)
                    break

    elif direction == "D":
        if coord[1] >= len(grid) or grid[coord[1]][coord[0]] == " ":
            for y in range(0, len(grid)):
                if grid[y][coord[0]] != " ":
                    coord = (coord[0], y)
                    break
    return coord

def get_next_coord(grid, start, direction):
    if direction == "R":
        c = (start[0] + 1, start[1])
    elif direction == "L":
        c = (start[0] - 1, start[1])
    elif direction == "U":
        c = (start[0], start[1] - 1)
    elif direction == "D":
        c = (start[0], start[1] + 1)

    return handle_coord_wrapping(c, grid, direction)
    

def valid_square(grid, coord):
    return grid[coord[1]][coord[0]] != "#" 

def follow(grid, path: string, start):
    direction = "R"
    path = re.split("(R|L)", path)

    for p in path:
        if p == "R" or p == "L":
            direction = rotate(direction, p)
        else:
            for i in range(int(p)):
                dest = get_next_coord(grid, start, direction)
                if valid_square(grid, dest):
                    grid[start[1]][start[0]] = get_print_char(direction)
                    start = dest
    # draw end
    grid[start[1]][start[0]] = get_print_char(direction)
    return start, direction

def part1():
    grid, code, start = parse(data)
    end, direction = follow(grid, code, start)
    direction = 0 if direction == "R" else 1 if direction == "D" else 2 if direction == "L" else 3
    return (1000 * (end[1] + 1)) + (4 * (end[0] + 1)) + direction
    
def part2():
    input = testdata
    return None

if __name__ == "__main__":
    print("-- AoC 2022 - Day 22 --\n")
    part("One", 22, 2022, part1, True)
    part("Two", 22, 2022, part2, False)