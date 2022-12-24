# AoC 2022 - Day 21 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=21, year=2022)
testdata = get_testdata(day=21, year=2022)
human = "humn"

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
    
def check():
    value = monkeys["root"]
    v1 = get(value[0])
    v2 = get(value[2])
    return v1 == v2

def part2():
    base = monkeys.copy()
    # work out the path from humn to root
    path = []
    key = "humn"
    while key != "root":
        for k, v in monkeys.items():
            if type(v) == list and key in v:
                path.append(k)
                key = k
                break


    path.remove("root")
    v1 = monkeys["root"][0]
    v2 = monkeys["root"][2]
    solve_for = v1
    if v2 not in path:
        solve_for = v2
    target = get(solve_for)
        

    # invert the path and solve the correct answer each step
    path.reverse()
    for p in path:
        v1 = monkeys[p][0]
        op = monkeys[p][1]
        v2 = monkeys[p][2]

        solve_for = v1
        if v2 not in path:
            solve_for = v2
        solve_for_v1 = solve_for == v1

        other = get(solve_for)

        if op == "+":
            target = target - other
        elif op == "-":
            if solve_for_v1:
                target =  other - target
            else:
                target = target + other
        elif op == "*":
            target = target / other
        elif op == "/":
            if solve_for_v1:
                target =  other / target
            else:
                target = target * other
    return int(target)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 21 --\n")
    part("One", 21, 2022, part1, False)
    part("Two", 21, 2022, part2, True)