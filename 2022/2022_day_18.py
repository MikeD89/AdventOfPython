# AoC 2022 - Day 18 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=18, year=2022)
testdata = get_testdata(day=18, year=2022)

adjacents = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1],
]

def part1():
    input = data
    c = 0
    cubes = input.splitlines()
    for line in cubes:
        cube = [int(i) for i in line.split(",")]
        for offset in adjacents:
            test = [cube[i] + offset[i] for i in range(3)]
            adjacent = f"{test[0]},{test[1]},{test[2]}"
            if adjacent not in cubes:
                c += 1
    return c
    

def part2():
    input = data
    cubes = input.splitlines()
    cubes = [i.split(',') for i in cubes]
    cubes = [[int(i) for i in cube] for cube in cubes]
    
    largest = [0, 0, 0]
    for cube in cubes:
        for i in range(3):
            if cube[i] > largest[i]:
                largest[i] = cube[i]     
    largest = [i + 2 for i in largest]
    largest = max(largest)

    # make some lava
    air = [[[True for k in range(largest)] for j in range(largest)] for i in range(largest)]
    for cube in cubes:
        air[cube[0]+1][cube[1]+1][cube[2]+1] = False

    # find all outside air
    visited = set()
    queue = list()
    queue.append([0, 0, 0])
    while len(queue) > 0:
        cube = queue.pop(0)
        tp_cube = tuple(cube)
        if tp_cube in visited:
            continue
        visited.add(tuple(cube))
        
        for offset in adjacents:
            test = [cube[i] + offset[i] for i in range(3)]
            if test[0] >= largest or test[1] >= largest or test[2] >= largest or test[0] < 0 or test[1] < 0 or test[2] < 0:
                continue
            if air[test[0]][test[1]][test[2]]:
                air[test[0]][test[1]][test[2]] = False
                queue.append(test)

    # add all inside air to cube list
    for x in range(largest):
        for y in range(largest):
            for z in range(largest):
                if air[x][y][z]:
                    cubes.append([x-1, y-1, z-1])
            
    # find all sides
    c = 0
    for cube in cubes:
        for offset in adjacents:
            test = [cube[i] + offset[i] for i in range(3)]
            if test not in cubes:
                c += 1   

    return c

if __name__ == "__main__":
    print("-- AoC 2022 - Day 18 --\n")
    part("One", 18, 2022, part1, True)
    part("Two", 18, 2022, part2, True)
