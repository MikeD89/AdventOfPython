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

td = True

data = get_data(day=19, year=2022)
testdata = get_testdata(day=19, year=2022)

input = testdata.split("\n\n") if td else  data.splitlines()
input = [i.replace(":", "!") for i in input]
input = [i.replace(".", "!") for i in input]
blueprints = [blueprint(i.splitlines()) for i in input] if td else [blueprint(i.split("! ")) for i in input]

def calc_blueprint_cost(bp: blueprint, minutes: int):
    print("blueprint ", bp.id)
    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0

    ore_robots = 1
    clay_robots = 0
    obsidian_robots = 0
    geode_robots = 0

    for min in range(1, minutes+1):
        ore_robots_delta = 0
        clay_robots_delta = 0
        obsidian_robots_delta = 0
        geode_robots_delta = 0
        robot_built = False

        if not robot_built and ore >= bp.geode_cost[0] and obsidian >= bp.geode_cost[1]:
            robot_built = True
            ore -= bp.geode_cost[0]
            obsidian -= bp.geode_cost[1]
            geode_robots_delta += 1
        
        if not robot_built and ore >= bp.obsidian_cost[0] and clay >= bp.obsidian_cost[1]:
            # are we making enough obsidian robots to keep up with geode production?
            # obsidian_ratio = bp.geode_cost[1] / bp.geode_cost[0]
            # if obsidian_robots < obsidian_ratio:
            robot_built = True
            ore -= bp.obsidian_cost[0]
            clay -= bp.obsidian_cost[1]
            obsidian_robots_delta += 1

        if not robot_built and ore >= bp.clay_cost:
            # are we making enough clay robots to keep up with obsdian production?
            # clay_ratio = bp.obsidian_cost[1] / bp.obsidian_cost[0]
            # if clay_robots < clay_ratio:            
            robot_built = True
            ore -= bp.clay_cost
            clay_robots_delta += 1

        # print(min, ore, ore_robots, clay, clay_robots, obsidian, obsidian_robots, geodes, geode_robots)
        ore += ore_robots
        clay += clay_robots
        obsidian += obsidian_robots
        geodes += geode_robots
        ore_robots += ore_robots_delta
        clay_robots += clay_robots_delta
        obsidian_robots += obsidian_robots_delta
        geode_robots += geode_robots_delta

    return geodes


def part1():
    geodes = [calc_blueprint_cost(bp, 24) for bp in blueprints]
    # geodes = [(i + 1) * v for i, v in enumerate(geodes)]
    print(geodes)
    return None
    
def part2():
    input = testdata
    return None

if __name__ == "__main__":
    print("-- AoC 2022 - Day 19 --\n")
    part("One", 19, 2022, part1, False)
    part("Two", 19, 2022, part2, False)