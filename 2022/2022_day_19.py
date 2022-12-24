# AoC 2022 - Day 19 - Mike D
import sys
import os
import string
import math
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

def strip_input(line):
    # its far too late at night to worry about regexing this...
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

class state:
    def __init__(self, bp, mins, state=None):
        self.bp = bp 
        self.remaining_minutes = mins
        self.score = 0 if state is None else state.score
        self.ore = 0 if state is None else state.ore
        self.clay = 0 if state is None else state.clay
        self.obsidian = 0 if state is None else state.obsidian
        self.ore_robots = 1 if state is None else state.ore_robots
        self.clay_robots = 0 if state is None else state.clay_robots
        self.obsidian_robots = 0 if state is None else state.obsidian_robots

    def add_builder(self, builder):
        self.ore -= builder.ore_cost
        self.clay -= builder.clay_cost
        self.obsidian -= builder.obsidian_cost
        self.ore_robots += builder.ore_built
        self.clay_robots += builder.clay_built
        self.obsidian_robots += builder.obsidian_built
        self.score += builder.geode_built * self.remaining_minutes

    def spend_time(self, n):
        self.remaining_minutes -= n
        self.ore += self.ore_robots * n
        self.clay += self.clay_robots * n
        self.obsidian += self.obsidian_robots * n

class builder:
    def __init__(self, ore_built, clay_built, obsidian_built, geode_built, ore_cost, clay_cost, obsidian_cost):
        self.ore_built = ore_built
        self.clay_built = clay_built
        self.obsidian_built = obsidian_built
        self.geode_built = geode_built
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost

    def calculate_time_cost(self, state: state):
        if state.ore >= self.ore_cost and state.clay >= self.clay_cost and state.obsidian >= self.obsidian_cost:
            return 1
        remaining_ore = self.ore_cost - state.ore
        remaining_clay = self.clay_cost - state.clay
        remaining_obsidian = self.obsidian_cost - state.obsidian

        if remaining_clay > 0 and state.clay_robots == 0:
            return -1
        if remaining_obsidian > 0 and state.obsidian_robots == 0:
            return -1

        remaining_ore_turns = math.ceil(remaining_ore / state.ore_robots)
        if remaining_clay > 0:
            remaining_clay_turns = math.ceil(remaining_clay / state.clay_robots)
        else: 
            remaining_clay_turns = 0

        if remaining_obsidian > 0:
            remaining_obsidian_turns = math.ceil(remaining_obsidian / state.obsidian_robots)
        else:
            remaining_obsidian_turns = 0

        return max(remaining_ore_turns + 1, remaining_clay_turns + 1, remaining_obsidian_turns + 1)


class blueprint:
    def __init__(self, lines):
        self.id = int(strip_input(lines[0]))
        obsidian_cost = [int(i) for i in strip_input(lines[3]).split(",")] # ore, clay
        geode_cost = [int(i) for i in strip_input(lines[4]).split(",")] # ore, obsidian
        self.builders = [
            builder(1, 0, 0, 0, int(strip_input(lines[1])), 0, 0),
            builder(0, 1, 0, 0, int(strip_input(lines[2])), 0, 0),
            builder(0, 0, 1, 0, obsidian_cost[0], obsidian_cost[1], 0),
            builder(0, 0, 0, 1, geode_cost[0], 0, geode_cost[1])
        ]
        self.max_ore_cost = max([b.ore_cost for b in self.builders])
        self.max_clay_cost = max([b.clay_cost for b in self.builders])
        self.max_obsidian_cost = max([b.obsidian_cost for b in self.builders])

    def is_pointless(self, b: builder, st: state):
        if self.max_ore_cost <= st.ore_robots and b.ore_built == 1:
            return True
        if self.max_clay_cost <= st.clay_robots and b.clay_built == 1:
            return True
        if self.max_obsidian_cost <= st.obsidian_robots and b.obsidian_built == 1:
            return True
        return False

td = False

data = get_data(day=19, year=2022)
testdata = get_testdata(day=19, year=2022)
input = testdata.split("\n\n") if td else  data.splitlines()
input = [i.replace(":", "!") for i in input]
input = [i.replace(".", "!") for i in input]
blueprints = [blueprint(i.splitlines()) for i in input] if td else [blueprint(i.split("! ")) for i in input]

def dfs(s):
    queue = [s]
    best_score = 0
    while len(queue) > 0:
        st = queue.pop(0)

        # is this state good?
        if st.score > best_score:
            best_score = st.score

        # best case scenario, can we do better?
        if st.score + ((st.remaining_minutes * (st.remaining_minutes - 1)) / 2) < best_score:
            continue

        for builder in st.bp.builders:
            time_cost = builder.calculate_time_cost(st)

            # filter impossible states
            if time_cost == -1:
                continue

            # filter pointless states
            if s.bp.is_pointless(builder, st):
                continue

            # filter unaffordable states 
            if st.remaining_minutes - time_cost < 0:
                continue

            new_state = state(st.bp, st.remaining_minutes, st)
            new_state.spend_time(time_cost)
            new_state.add_builder(builder)

            queue.append(new_state)
    return best_score

def part1():
    scores = [dfs(state(b, 24)) for b in blueprints]
    qualities = [(i + 1) * v for i, v in enumerate(scores)]
    return sum(qualities)
    
def part2():
    first_three = blueprints[:3]
    scores = [dfs(state(b, 32)) for b in first_three]
    return scores[0] * scores[1] * scores[2]

if __name__ == "__main__":
    print("-- AoC 2022 - Day 19 --\n")
    part("One", 19, 2022, part1, True)
    part("Two", 19, 2022, part2, True)

