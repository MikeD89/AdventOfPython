# AoC 2022 - Day 24 - Mike D
import math
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=24, year=2022)
testdata = get_testdata(day=24, year=2022)

moves = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
facing = ["^", ">", "v", "<", "unused"]

def parse(input):
    width = len(input.splitlines()[0]) - 2
    height = len(input.splitlines()) - 2
    start = (0, -1)
    end = (width-1, height)

    blizzards = []
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char == ">" or char == "<" or char == "^" or char == "v":
                move = moves[facing.index(char)]
                blizzards.append((x - 1, y - 1, move))

    b_states = blizzard_states(blizzards, width, height)
    safe_cells = find_safe_cells(b_states, width, height, start, end)

    return safe_cells, start, end

def blizzard_states(blizzards, width, height):
    lcm = math.lcm(width, height)
    states = []

    for i in range(lcm):
        state = []           
        for i, blizzard in enumerate(blizzards):
            # store it 
            state.append((blizzard[0], blizzard[1]))

            # update it 
            x = blizzard[0] + blizzard[2][0]
            y = blizzard[1] + blizzard[2][1]
            if x < 0:
                x = width - 1
            elif x >= width:
                x = 0
            if y < 0:
                y = height - 1
            elif y >= height:
                y = 0
            blizzards[i] = (x, y, blizzard[2])
        states.append(state)
    return states

def find_safe_cells(blizzards, width, height, start, end):
    # because we can stand stationary, we should specifically look for safe cells, as standing on the spot is not a valid tactic
    all_cells = [(x, y) for x in range(width) for y in range(height)]
    safe_cells = []
    for blizzard in blizzards:
        safety = {start, end}
        for cell in all_cells:
            if cell not in blizzard:
                safety.add(cell)
        safe_cells.append(safety)
    return safe_cells

def traverse(safe_cells, start, end, time):
    queue = [start]
    while True:
        time += 1
        currently_safe = safe_cells[time % len(safe_cells)]
        targets = set()
        for item in queue:
            for move in moves:
                dest = (item[0] + move[0], item[1] + move[1])
                if dest == end:
                    return time
                    
                if dest in currently_safe:
                    targets.add(dest)
        queue = targets

input = testdata
safe_cells, start, end = parse(input)

def part1():    
    return traverse(safe_cells, start, end, 0)
    
def part2():
    time = traverse(safe_cells, start, end, 0)
    time = traverse(safe_cells, end, start, time)
    time = traverse(safe_cells, start, end, time)
    return time

if __name__ == "__main__":
    print("-- AoC 2022 - Day 24 --\n")
    part("One", 24, 2022, part1, True)
    part("Two", 24, 2022, part2, True)