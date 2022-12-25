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
    # code = "1R5R10"
    
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

def handle_coord_wrapping_flat(start, coord, grid, direction):
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
    return coord, direction

def get_next_coord(grid, start, direction, coord_wrapper):
    if direction == "R":
        c = (start[0] + 1, start[1])
    elif direction == "L":
        c = (start[0] - 1, start[1])
    elif direction == "U":
        c = (start[0], start[1] - 1)
    elif direction == "D":
        c = (start[0], start[1] + 1)

    return coord_wrapper(start, c, grid, direction)
    
def valid_square(grid, coord):
    return grid[coord[1]][coord[0]] != "#" 

def follow(grid, path: string, start, coord_wrapper):
    direction = "R"
    path = re.split("(R|L)", path)

    for p in path:
        if p == "R" or p == "L":
            direction = rotate(direction, p)
        else:
            for i in range(int(p)):
                dest, new_dir = get_next_coord(grid, start, direction, coord_wrapper)
                if valid_square(grid, dest):
                    grid[start[1]][start[0]] = get_print_char(direction)
                    direction = new_dir
                    start = dest
    # draw end
    grid[start[1]][start[0]] = get_print_char(direction)
    return start, direction

region_size = 50
one = (50, 0)
two = (100, 0)
three = (50, 50)
four = (0, 100)
five = (50, 100)
six = (0, 150)
regions = [[None, one,   two], 
          [None, three, None],
          [four, five, None],
          [six, None,  None]
         ]

def noinv(delta):
    return delta
def inv(delta):
    return 49 - delta
edges = [
    [one, "U", six, "R", noinv],
    [one, "L", four, "R", inv],
    [two, "U", six, "U", noinv],
    [two, "D", three, "L", noinv],
    [two, "R", five, "L", inv],
    [three, "L", four, "D", noinv],
    [three, "R", two, "U", noinv],
    [four, "U", three, "R", noinv],
    [four, "L", one, "R", inv],
    [five, "R", two, "L", inv],
    [five, "D", six, "L", noinv],
    [six, "R", five, "U", noinv],
    [six, "D", two, "D", noinv],
    [six, "L", one, "D", noinv],
]

def handle_coord_wrapping_cube(start, target, grid, direction):
    current_region = (start[0] // region_size, start[1] // region_size)
    current_region = regions[current_region[1]][current_region[0]]

    if target[0] < 0 or target[1] < 0 or target[0] >= len(grid[0]) or target[1] >= len(grid):
        target_region = None
    else:
        target_region = (target[0] // region_size, target[1] // region_size)
        target_region = regions[target_region[1]][target_region[0]]

    if current_region == None:
        print("off the cube!!")
        exit()
    
    # normal move?
    if target_region != None:
        return target, direction

    # find edge
    new_region = None
    new_direction = None
    delta_func = None
    for edge in edges:
        if edge[0] == current_region and edge[1] == direction:
            new_region = edge[2]
            new_direction = edge[3]
            delta_func = edge[4]
            break

    if new_region == None or new_direction == None:
        print("no edge found")
        exit()

    # edge diff 
    delta_x = start[0] - current_region[0]
    delta_y = start[1] - current_region[1]

    if direction == "R":
        delta = delta_y
    elif direction == "L":
        delta = delta_y
    elif direction == "U":
        delta = delta_x
    elif direction == "D":
        delta = delta_x

    delta = delta_func(delta)

    # calcualte new delta 
    if new_direction == "R":
        delta_x = 0
        delta_y = delta
    elif new_direction == "L":
        delta_x = region_size - 1
        delta_y = delta
    elif new_direction == "U":
        delta_x = delta
        delta_y = region_size - 1
    elif new_direction == "D":
        delta_x = delta
        delta_y = 0

    # calculate new target
    new_target = (new_region[0] + delta_x, new_region[1] + delta_y)
    return new_target, new_direction

def calculate_score(end, direction):
    direction = 0 if direction == "R" else 1 if direction == "D" else 2 if direction == "L" else 3
    return (1000 * (end[1] + 1)) + (4 * (end[0] + 1)) + direction

def part1():
    input = data
    grid, code, start = parse(input)
    end, direction = follow(grid, code, start, handle_coord_wrapping_flat)
    return calculate_score(end, direction)    
    
def part2():
    input = data
    grid, code, start = parse(input)
    end, direction = follow(grid, code, start, handle_coord_wrapping_cube)
    # for row in grid:
    #     print("".join(row))

    return calculate_score(end, direction)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 22 --\n")
    part("One", 22, 2022, part1, False)
    part("Two", 22, 2022, part2, True) #144012