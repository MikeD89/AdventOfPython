# AoC 2023 - Day 4 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=4, year=2023)
testdata = get_testdata(day=4, year=2023)

def parseline(line: string):
    id, nums = line.split(":")
    id = int(id.split("Card ")[1])
    winning, have = nums.split(" | ")
    winning = [int(x) for x in winning.split(" ") if '' != x]
    have = [int(x) for x in have.split(" ") if '' != x]
    return id, winning, have
    
def count_matches(winning, have):
    wins = 0
    for n in have:
        if n in winning:
            wins+=1 
    return wins

def score(wins):
    if wins == 0:
        return 0
    s = 1
    for i in range(wins-1):
        s *= 2
    return s

def part1():
    input = data
    total = 0
    for line in input.splitlines():
        id, winning, have = parseline(line)
        wins = count_matches(winning, have)
        points = score(wins)
        total += points
        
    return total

def process(id, winning, have, count):
    value = 1
    wins = count_matches(winning, have)
    for ii in range(id+1, id+1+wins):
        value += count.get(ii, 0)
    return value

    
def part2():
    input = data
    count = {}
    for line in reversed(input.splitlines()):
        id, winning, have = parseline(line)
        count[id] = process(id, winning, have, count) 
    return sum(count.values())

if __name__ == "__main__":
    print("-- AoC 2023 - Day 4 --\n")
    part("One", 4, 2023, part1, True)
    part("Two", 4, 2023, part2, True)