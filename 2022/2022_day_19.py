# AoC 2022 - Day 19 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

def strip_input(line):
    return line.strip().replace("Each ore robot costs ", "") \
                       .replace("Each clay robot costs ", "") \
                       .replace("Each obsidian robot costs ", "") \
                       .replace("Each geode robot costs ", "") \
                       .replace(" ore and ", ",") \
                       .replace(" ore", "") \
                       .replace(" clay", "") \
                       .replace(" obsidian.", "") \
                       .replace(" obsidian!", "") \
                       .replace("Blueprint ", "") \
                       .replace("!", "") \


class blueprint:
    def __init__(self, lines):
        self.id = int(strip_input(lines[0]))
        self.ore_cost = int(strip_input(lines[1]))
        self.clay_cost = int(strip_input(lines[2]))
        self.obsidian_cost = [int(i) for i in strip_input(lines[3]).split(",")]
        self.geode_cost = [int(i) for i in strip_input(lines[4]).split(",")]

td = False

data = get_data(day=19, year=2022)
testdata = get_testdata(day=19, year=2022)

input = testdata.split("\n\n") if td else  data.splitlines()
input = [i.replace(":", "!") for i in input]
input = [i.replace(".", "!") for i in input]
blueprints = [blueprint(i.splitlines()) for i in input] if td else [blueprint(i.split("! ")) for i in input]

def calc_blueprint_cost(bp: blueprint, minutes: int):
    ore = 0
    clay = 0

    ore_robots = 1
    clay_robots = 0

    for min in range(minutes):
        ore += ore_robots


def part1():
    costs = []
    for bp in blueprints:
        costs.append(calc_blueprint_cost(bp, 24))
    return None
    
def part2():
    input = testdata
    return None

if __name__ == "__main__":
    print("-- AoC 2022 - Day 19 --\n")
    part("One", 19, 2022, part1, False)
    part("Two", 19, 2022, part2, False)