# AoC 2022 - Day 23 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=23, year=2022)
testdata = get_testdata(day=23, year=2022)
input = data.splitlines()

width = len(input[0])
height = len(input)
offset_width = width
offset_height = height
m = 3

grid = make_grid(width * m, height * m, ".")
def reset_grid():
    global grid
    grid = make_grid(width * m, height * m, ".")
    for td in enumerate(input):
        for x, c in enumerate(td[1]):   
            grid[td[0] + offset_height][x + offset_width] = c if c == "." else "#"
reset_grid()

move_order = ["n", "s", "w", "e"]

def get_kernel_coords(x, y):
    v = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            v.append((x + i, y + j))
    return v

def get_adjacent_coords(x, y, move):
    if move == "n":
        return [[x-1, y-1], [x, y-1], [x+1, y-1]]
    elif move == "e":
        return [[x+1, y-1], [x+1, y], [x+1, y+1]]
    elif move == "s":
        return [[x-1, y+1], [x, y+1], [x+1, y+1]]
    elif move == "w":
        return [[x-1, y-1], [x-1, y], [x-1, y+1]]

def round(n):
    proposed_moves = []
    destinations = {}
    unhappy = False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            e = grid[y][x]
            # elf on shelf?
            if e == ".":
                continue

            # is any adjacent square an elf?
            adjacents = get_kernel_coords(x, y)
            elf = False
            for a in adjacents:
                if grid[a[1]][a[0]] != ".":
                    elf = True
                    unhappy = True
                    break
            if not elf:
                continue
            
            # calcualte moves
            for i in range(len(move_order)):
                move = (i + n) % len(move_order)
                move = move_order[move]

                # is any square in the move direction an elf?
                adjacents = get_adjacent_coords(x, y, move)
                elf = False
                for a in adjacents:
                    if grid[a[1]][a[0]] != ".":
                        elf = True
                        break

                # if elf:
                #     next_move = (move_order.index(e) + 1) % len(move_order)
                #     e = move_order[next_move]
                #     grid[y][x] = e

                else:
                    if move == "n":
                        d = (x, y-1)
                    elif move == "e":
                        d = (x+1,y)
                    elif move == "s":
                        d = (x,y+1)
                    elif move == "w":
                        d = (x-1,y)

                    proposed_moves.append([x, y, move, d])
                    if d not in destinations:
                        destinations[d] = 1
                    else:
                        destinations[d] += 1

                    break

    # remove clashes
    for d in destinations:
        if destinations[d] > 1:
            for pm in proposed_moves:
                if pm[3] == d:
                    pm[3] = "clash"

    # move elves
    moved = False
    for pm in proposed_moves:
        if pm[3] == "clash":
            continue
        grid[pm[1]][pm[0]] = "."
        grid[pm[3][1]][pm[3][0]] = "#" 
        moved = True

    return moved


def count_tiles(p=False):
    min_x = len(grid[0])
    max_x = 0
    min_y = len(grid)
    max_y = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
    
    c = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if grid[y][x] == ".":
                c += 1
            if p:
                print(grid[y][x], end="")
        if p:
            print()
    return c

def part1():
    for i in range(10):
        round(i)

    return count_tiles()
    
def part2():
    reset_grid()

    i = 0
    while True:
        unhappy = round(i)
        if not unhappy:
            return i + 1
        i += 1

if __name__ == "__main__":
    print("-- AoC 2022 - Day 23 --\n")
    part("One", 23, 2022, part1, True)
    part("Two", 23, 2022, part2, True) 
