# AoC 2023 - Day 2 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=2, year=2023)
testdata = get_testdata(day=2, year=2023)

def parse(line):
    l = line.split(": ")
    game = l[0]
    game = game.split(" ")[1]
    rounds = l[1].split("; ")
    r = []
    for round in rounds:
        cubes = round.split(", ")
        cubes = [b.split(" ") for b in cubes]
        r.append(cubes)
    
    return game, r

def isvalid(rounds, red, green, blue):
    for round in rounds:
        for cube in round:
            if cube[1] == "red":
                if int(cube[0]) > red:
                    return False
            elif cube[1] == "green":
                if int(cube[0]) > green:
                    return False
            elif cube[1] == "blue":
                if int(cube[0]) > blue:
                    return False
    return True


def min_game(rounds):
    r = 0
    g = 0
    b = 0
    for round in rounds:
        for cube in round:
            if cube[1] == "red":
                r = max(r, int(cube[0]))
            elif cube[1] == "green":
                g = max(g, int(cube[0]))
            elif cube[1] == "blue":
                b = max(b, int(cube[0]))
    return r, g, b

def part1():
    input = data
    v = 0
    for line in input.splitlines():
        game, rounds = parse(line)
        if isvalid(rounds, 12, 13, 14):
            v+=int(game)
    return v
    
def part2():
    input = data
    v = 0
    for line in input.splitlines():
        game, rounds = parse(line)
        r, g, b = min_game(rounds)
        power = r * g * b
        v+=power
    return v

if __name__ == "__main__":
    print("-- AoC 2023 - Day 2 --\n")
    part("One", 2, 2023, part1, True)
    part("Two", 2, 2023, part2, True)