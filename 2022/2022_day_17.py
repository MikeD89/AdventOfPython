# AoC 2022 - Day 17 - Mike D
import sys
import os
import string
import copy
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

input_data = get_data(day=17, year=2022)
testdata = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
# testdata = "."

horizontal = [['#','#','#','#']]
plus = [
    ['.', '#', '.'],
    ['#', '#', '#'],
    ['.', '#', '.']
]
invplus = [
    ['.', '#', '.'],
    ['#', '#', '#'],
    ['#', '.', '#']
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

rocks = [horizontal, plus, lshape, line, square]
width = 7
headroom = 7

# TD
# testdata = ">>>><<<<<<>>>>>><<<<<<>>>>>>"
# linething = [
#     ['#','#','#','#','#'],
#     ['.','.','.','.','#'],
#     ['.','.','.','.','#'],
# ]

# rocks = [linething, square]
# TD

class data:
    def __init__(self, wind):
        self.chamber = []
        self.wind = wind
        self.i = -1
        self.x = 0
        self.y = 0
        self.nextshape = 0
        self.rock_count = -1
        self.falling = False
        self.shape = None

def add_rows(d, n):
    for i in range(n):
        row = ['.'] * width
        d.chamber.insert(0, row)

def check_headroom(d):
    # check headroom
    h = 0
    if not d.falling:
        for j in range(headroom):
            if d.chamber[j].count('#') > 0:
                h += 1
        add_rows(d, h)

def check_next_shape(d):
    # do we have a shape?
    if not d.falling:
        d.shape = rocks[d.nextshape]
        d.nextshape = (d.nextshape + 1) % len(rocks)
        d.x = 2
        d.y = 4 - len(d.shape)
        d.falling = True

def blow_wind(d):
    action = d.wind[d.i % len(d.wind)]
    good = False
    right = action == '>'

    if right and not d.x + 1 > width - len(d.shape[0]):
        good = True
    elif not right and not d.x - 1 < 0:
        good = True
       
    # check every point in d.shape can move in d.chamber
    if good:
        for i in range (len(d.shape)):
            for j in range (len(d.shape[i])):
                chamber_x = d.x+j+1 if right else d.x+j-1

                if d.shape[i][j] == '#' and d.chamber[d.y+i][chamber_x] == '#':
                    good = False
                    break
            if not good:
                break

    if good and right:
        d.x += 1
        return True
    elif good and not right:
        d.x -= 1
        return True
    return False

def handle_gravity(d, slide):
    gravity = d.y + len(d.shape) < len(d.chamber)
    if gravity: 
        for i in range (len(d.shape)):
            for j in range (len(d.shape[i])):
                if d.shape[i][j] == '#':
                    if d.chamber[d.y+i+1][d.x+j] != '.':
                        gravity = False
    if gravity:
        d.y += 1
    else:
        d.falling = False
        for l in range(len(d.shape)):
            for m in range(len(d.shape[l])):
                if d.shape[l][m] == '#':
                    d.chamber[d.y+l][d.x+m] = '#'

def handle_collision(d):
    for j in range(len(d.shape)):
        for k in range(len(d.shape[j])):
            if d.shape[j][k] == '#':
                if d.chamber[d.y+j][d.x+k] == '#':
                    d.falling = False
                    for l in range(len(d.shape)):
                        for m in range(len(d.shape[l])):
                            if d.shape[l][m] == '#':
                                d.chamber[d.y+l][d.x+m] = '#'
                    break
        if not d.falling:
            break

def print_debug(d):
    action = d.wind[d.i % len(d.wind)]
    print(d.i, d.falling, action)
    c = copy.deepcopy(d.chamber)
    if d.falling:
        for j in range(0, min(25, len(d.shape))):
            for k in range(len(d.shape[j])):
                if d.shape[j][k] == '#':
                    c[d.y+j][d.x+k] = '@'
    print_grid(c)

def check_p1_exit(d, total_rocks):
    if not d.falling:
        d.rock_count += 1
        if d.rock_count > total_rocks:
            return len(d.chamber)
    return None

def cycle(total_rocks, d, debug):
    add_rows(d, headroom)
    
    while True:
        exit = check_p1_exit(d, total_rocks)
        if exit:
            return exit

        d.i += 1
        check_headroom(d)
        check_next_shape(d)
        slide = blow_wind(d)
        handle_gravity(d, slide)
        handle_collision(d)
        if debug:
            print_debug(d)

def part1():
    d = data(input_data)
    return cycle(2022, d, False) - headroom
    
def part2():
    d = data(input_data)
    return cycle(1000000000000, d, False) - headroom

if __name__ == "__main__":
    print("-- AoC 2022 - Day 17 --\n")
    part("One", 17, 2022, part1, False)
    # part("Two", 17, 2022, part2, False)