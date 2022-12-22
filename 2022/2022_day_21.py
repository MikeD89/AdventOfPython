# AoC 2022 - Day 21 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=21, year=2022)
testdata = get_testdata(day=21, year=2022)

monkeys = {}
for d in data.splitlines():
    key, value = d.split(": ")
    try:
        value = int(value)
        monkeys[key] = value
    except:
        value = value.split(" ")
        monkeys[key] = value

def get(key):
    value = monkeys[key]
    if type(value) == int:
        return value
    else:
        v1 = get(value[0])
        v2 = get(value[2])
        return int(eval(f"{v1} {value[1]} {v2}"))

def part1():
    return get("root")
    
def part2():
    input = testdata
    return None

if __name__ == "__main__":
    print("-- AoC 2022 - Day 21 --\n")
    part("One", 21, 2022, part1, False)
    part("Two", 21, 2022, part2, False)