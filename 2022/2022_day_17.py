# AoC 2022 - Day 17 - Mike D
import sys
import os
import string
import copy
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=17, year=2022)

horizontal = [['#','#','#','#']]
plus = [
    ['.', '#', '.'],
    ['#', '#', '#'],
    ['.', '#', '.']
]
lshape = [
    ['.','.','#'],
    ['.','.','#'],
    ['#','#','#']
]
line = [
    ['#'],
    ['#'],
    ['#'],
    ['#']
]
square = [
    ['#','#'],
    ['#','#']
]

testdata = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
rocks = [horizontal, plus, lshape, line, square]
width = 7
headroom = 7

debug = True

def add_rows(chamber, n):
    for i in range(n):
        row = ['.'] * width
        chamber.insert(0, row)
    return chamber

def cycle(n, wind, chamber):
    nextshape = 0
    falling = False
    x = 0
    y = 0
    shape = None
    
    for i in range(n):
        if debug:
            print(i)

        # check headroom
        h = 0
        if not falling:
            for j in range(headroom):
                if chamber[j].count('#') > 0:
                    h += 1
            chamber = add_rows(chamber, h)

        # what do we do?
        action = wind[i % len(wind)]
        if debug:
            print(x, y, falling, action)
        
        # do we have a shape?
        if not falling:
            shape = rocks[nextshape]
            nextshape = (nextshape + 1) % len(rocks)
            x = 2
            y = 4 - len(shape)
            falling = True

        # wind
        if action == '>':
            if not x + 1 > width - len(shape[0]):
                good = True
                for j in range (len(shape)):
                    if chamber[y+j][x+len(shape[0])] == '#':
                        good = False
                        break

                if good:
                    x += 1
        elif action == '<':
            if not x - 1 < 0:
                good = True
                for j in range (len(shape)):
                    if chamber[y+j][x-1] == '#':
                        good = False
                        break
                if good:
                    x -= 1

        # gravity 
        gravity = y + len(shape) < len(chamber)
        if gravity: 
            for j in range (len(shape[0])):
                if chamber[y+len(shape)][x+j] != '.':
                    gravity = False
        if gravity:
            y += 1
        else:
            falling = False
            for l in range(len(shape)):
                for m in range(len(shape[l])):
                    if shape[l][m] == '#':
                        chamber[y+l][x+m] = '#'
        
        # shape collision
        for j in range(len(shape)):
            for k in range(len(shape[j])):
                if shape[j][k] == '#':
                    if chamber[y+j][x+k] == '#':
                        falling = False
                        for l in range(len(shape)):
                            for m in range(len(shape[l])):
                                if shape[l][m] == '#':
                                    chamber[y+l][x+m] = '#'
                        break
            if not falling:
                break

        # print
        if debug:
            c = copy.deepcopy(chamber)
            if falling:
                for j in range(len(shape)):
                    for k in range(len(shape[j])):
                        if shape[j][k] == '#':
                            c[y+j][x+k] = '@'
            print_grid(c)


def part1():
    chamber = add_rows([], headroom)
    cycle(1000, testdata, chamber)
    return None
    
def part2():
    input = testdata
    return None

if __name__ == "__main__":
    print("-- AoC 2022 - Day 17 --\n")
    part("One", 17, 2022, part1, False)
    part("Two", 17, 2022, part2, False)