# AoC 2022 - Day 14 - Mike D
import math
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=14, year=2022)
testdata = get_testdata(day=14, year=2022)

def vector_length(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1])

def gen_grid(input):
    minX = 9999999999999
    maxX = 0
    maxY = 0
    for line in input.splitlines():
        coords = line.split(" -> ")
        for coord in coords:
            (x, y) = coord.split(",")
            x = int(x)
            y = int(y)
            if x > maxX:
                maxX = x
            if x < minX:
                minX = x
            if y > maxY:
                maxY = y

    maxY += 1
    maxX += 1
    w = maxX - minX
    grid = [["."] * w for _ in range(maxY)]

    gX = 500 - minX
    grid[0][gX] = "+"

    for line in input.splitlines():
        coords = line.split(" -> ")
        fr = None
        for coord in coords:
            (x, y) = coord.split(",")
            x = int(x)
            y = int(y)
            if fr == None:
                fr = (x, y)
            else:
                to = (x, y)
                v = (to[0] - fr[0], to[1] - fr[1])
                
                if not vector_length(v).is_integer():
                    print("found a diagonal line - logic error")
                    exit()

                # print(fr, to)
                for i in range(abs(v[0]) + 1):
                    xT = (fr[0] + (i if v[0] > 0 else -i)) - minX
                    yT = fr[1]
                    grid[yT][xT] = "#"
                    # print(xT, yT, i)

                for i in range(abs(v[1]) + 1):
                    xT = fr[0]-minX
                    yT = (fr[1] + (i if v[1] > 0 else -i))
                    grid[yT][xT] = "#"
                    # print(xT, yT)
                fr = to
         
    return grid, gX

def add_floor(grid):
    grid.append(["."] * len(grid[0]))
    grid.append(["#"] * len(grid[0]))

def expand(grid):
    n = len(grid[0]) * 2
    for _ in range(n):
        for row in grid:
            row.insert(0, ".")
            row.append(".")
    # fix the floor
    grid[-1] = ["#"] * len(grid[0])
    return n

def drop_sand(grid, gX):
    maxY = len(grid)
    maxX = len(grid[0])

    sX = gX
    sY = 0

    while True:
        if sY == maxY-1 or sX == maxX or sX == 0:
            return -1

        # falling through air
        if grid[sY+1][sX] == "+" or grid[sY+1][sX] == ".":
            sY += 1
            continue

        # hits a floor or sand
        if grid[sY+1][sX] == "#" or grid[sY+1][sX] == "o":
            # check if we can move left or right
            if grid[sY+1][sX-1] == ".": # left
                sX -= 1
                continue
            elif grid[sY+1][sX+1] == ".": # right
                sX += 1
                continue
            else: # we're on a flat surface
                # did we hit the finish?
                if grid[sY][sX] == "+":
                    return 0
                break

    grid[sY][sX] = "o"
    return 1

def drop_till_the_party_stops(grid, gX):
    i = 0
    while True:
        dropped = drop_sand(grid, gX)
        if dropped == 1:
            i+=1
        else:
            break
    return i

def part1():
    (grid, gX) = gen_grid(data)
    return drop_till_the_party_stops(grid, gX)   
    
def part2():
    (grid, gX) = gen_grid(data)

    add_floor(grid)
    e = expand(grid)
    gX += e

    return drop_till_the_party_stops(grid, gX) + 1

if __name__ == "__main__":
    print("-- AoC 2022 - Day 14 --\n")
    part("One", 14, 2022, part1, True)
    part("Two", 14, 2022, part2, True)