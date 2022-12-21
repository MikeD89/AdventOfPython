# AoC 2022 - Day 19 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=19, year=2022)
testdata = get_testdata(day=19, year=2022)

def strip_input(line):
    return line.replace("  Each ore robot costs ", "") \
               .replace("  Each clay robot costs ", "") \
               .replace("  Each obsidian robot costs ", "") \
               .replace("  Each geode robot costs ", "") \
               .replace(" ore and ", ",") \
               .replace(" ore.", "") \
               .replace(" clay.", "") \
               .replace(" obsidian.", "") \
               .replace("Blueprint ", "") \
               .replace(":", "")

class blueprint:
    def __init__(self, lines):
        self.id = int(strip_input(lines[0]))
        self.ore_cost = int(strip_input(lines[1]))
        self.clay_cost = int(strip_input(lines[2]))
        self.obsidian_cost = [int(i) for i in strip_input(lines[3]).split(",")]
        self.geode_cost = [int(i) for i in strip_input(lines[4]).split(",")]

def part1():
    input = testdata.split("\n\n")
    blueprints = [blueprint(i.splitlines()) for i in input]
    return None
    
def part2():
    input = testdata
    return None

if __name__ == "__main__":
    print("-- AoC 2022 - Day 19 --\n")
    part("One", 19, 2022, part1, False)
    part("Two", 19, 2022, part2, False)