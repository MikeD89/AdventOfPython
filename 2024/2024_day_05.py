# AoC 2024 - Day 5 - Mike D
import math
import sys
import os
import string
from functools import cmp_to_key
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=5, year=2024)
testdata = get_testdata(day=5, year=2024)

def parse(input):
    first = []
    second = []
    firstt = True
    for line in input.splitlines():
        if line == "":
            firstt = False
            continue

        if firstt:
            first.append(line.split("|"))
        else:
            second.append(line.split(","))
    return first,second

def validate(update, rules):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        index_a = update.index(rule[0])
        index_b = update.index(rule[1])

        if index_b < index_a:
            return False
    return True

def fix(update, rules):
    def compare(x, y):
        for rule in rules:
            if rule[0] not in [x,y] or rule[1] not in [x,y]:
                continue
            index_a = update.index(rule[0])
            index_b = update.index(rule[1])
            return index_b - index_a

    return sorted(update, key=cmp_to_key(compare))

def part1():
    input = data
    rules,updates = parse(input)
    a = 0
    for update in updates:
        if(validate(update, rules)):
            a += int(update[math.floor(len(update)/2)])
            
    return a
    
def part2():
    input = data
    rules,updates = parse(input)
    a = 0
    for update in updates:
        if validate(update, rules):
            continue

        update = fix(update, rules)
        a += int(update[math.floor(len(update)/2)])
            
    return a

if __name__ == "__main__":
    print("-- AoC 2024 - Day 5 --\n")
    part("One", 5, 2024, part1, True)
    part("Two", 5, 2024, part2, True)