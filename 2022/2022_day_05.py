# AoC 2022 - Day 5 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=5, year=2022)
testdata = get_testdata(day=5, year=2022)

def get_data_split(d):
    for (i, line) in enumerate(d.splitlines()):
        if line == "":
            return i

def split_data(d, i):
    d = d.splitlines()
    return d[:i], d[i+1:]

def process_columns(d):
    n = d[len(d) - 1:][0].split(" ")
    n = [x for x in n if x != ""]
    r = d[:len(d) - 1]

    rows = []

    # rotate the data into stacks
    for i in n:
        c = int(i) + (3 * (int(i) - 1))
        row = []
                    
        for line in reversed(r):
            if line[c] != " ":
                row.append(line[c])
        rows.append(row)
        
    return rows

def process_commands(rows, commands, cratemover):
    for command in commands:
        command = command.replace("move ", "") \
                         .replace(" to ", " ") \
                         .replace(" from ", " ") \
                         .split(" ")
        command = [int(x) for x in command]
        cratemover(rows, command[0], command[1], command[2])

    return rows

def cratemover_9000(rows, quantity, from_column, to_column):
    for _ in range(quantity):
        rows[to_column - 1].append(rows[from_column - 1].pop())

def cratemover_9001(rows, quantity, from_column, to_column):
    substack = []
    for _ in range(quantity):
        substack.append(rows[from_column - 1].pop())
    for c in reversed(substack):
        rows[to_column - 1].append(c)

def read_crates(rows):
    message = ""
    for row in rows:
        message += row.pop()
    return message

def run(input, cratemover):
    ds = get_data_split(input)
    cols, commands = split_data(input, ds)
    rows = process_columns(cols)
    rows = process_commands(rows, commands, cratemover)
    message = read_crates(rows)
    return message

def part1():
    return run(data, cratemover_9000)
    
def part2():
    return run(data, cratemover_9001)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 5 --\n")
    part("One", 5, 2022, part1, True)
    part("Two", 5, 2022, part2, True)