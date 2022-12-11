# AoC 2022 - Day 11 - Mike D
import math
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=11, year=2022)
testdata = get_testdata(day=11, year=2022)

def parse(input):
    m = []
    for line in input.splitlines():
        if line.startswith("Monkey"):
            m.append({})
        elif line.startswith("  Starting items:"):
            m[len(m) - 1]["items"] = line.split(":")[1].split(",")
        elif line.startswith("  Operation: "):
            op = line.split(":")[1].split("new = old ")[1]
            m[len(m) - 1]["op"] = op.split(" ")
        elif line.startswith("  Test:"):
            m[len(m) - 1]["test"] = int(line.split(":")[1].split(" divisible by ")[1])
        elif line.startswith("    If true:"):
            m[len(m) - 1]["true"] = int(line.split(":")[1].split("to monkey ")[1])
        elif line.startswith("    If false:"):
            m[len(m) - 1]["false"] = int(line.split(":")[1].split("to monkey ")[1])
    return m

def print_monkiez(monkeys):
    for (i, m) in enumerate(monkeys):
        print(i, m["items"])

def post_inspect_part_1(worry, v):
    return worry // 3

def post_inspect_part_2(worry, v):
    return worry % v

def round(monkeys, rounds, post_inspect):
    inspects = []
    for m in monkeys:
        inspects.append(0)

    v = 1
    for m in monkeys:
        v *= int(m["test"])

    for n in range(rounds):
        for (i, m) in enumerate(monkeys):
            inspects[i] += len(m["items"])
            for item in m["items"] :
                worry = int(item)
                # op
                op = m['op']
                if op[0] == "*":
                    if op[1] == "old":
                        worry = worry * worry
                    else:
                        worry = worry * int(op[1])
                elif op[0] == "+":
                    worry += int(op[1])

                worry = post_inspect(worry, v)           

                # test
                if worry % m['test'] == 0:
                    monkeys[m['true']]['items'].append(worry)
                else:
                    monkeys[m['false']]['items'].append(worry)

            m['items'] = []

    return inspects

def run(input, n, post_inspect):
    monkeys = parse (input)
    inspects = round(monkeys, n, post_inspect)
    monkey_buisness = sorted(inspects)[len(monkeys) - 1] * sorted(inspects)[len(monkeys) - 2]
    return monkey_buisness

def part1():
    return run(data, 20, post_inspect_part_1)
    
def part2():
    return run(data, 10000, post_inspect_part_2)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 11 --\n")
    part("One", 11, 2022, part1, True)
    part("Two", 11, 2022, part2, True)