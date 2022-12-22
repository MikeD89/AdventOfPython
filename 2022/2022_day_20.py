# AoC 2022 - Day 20 - Mike D
import sys
import os
import string
from itertools import cycle
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=20, year=2022)
testdata = get_testdata(day=20, year=2022)
key = 811589153

zero = None
order = []
for i, v in enumerate(data.splitlines()):
    val = int(v)
    if val == 0:
        zero = i
    val = tuple([i, val])
    order.append(val)

def mix(d, encyrpted):
    for i in range(len(d)):
        value = order[i]
        value = tuple([value[0], value[1] * key]) if encyrpted else value
        current_index = d.index(value)
        new_index = (current_index + value[1]) % (len(d) - 1)
        d.insert(new_index % len(data), d.pop(current_index))
    return d

def gps(d):
    zero_index = d.index(tuple([zero, 0]))
    a = (zero_index + 1000) % len(d)
    b = (zero_index + 2000) % len(d)
    c = (zero_index + 3000) % len(d)
    return d[a][1] + d[b][1] + d[c][1]

def part1():
    d = order.copy()
    d = mix(d, False)
    return gps(d)   
    
def part2():
    d = order.copy()
    d = [tuple([v[0], v[1] * key]) for v in d]
    for i in range(10):
        d = mix(d, True)
    return gps(d)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 20 --\n")
    part("One", 20, 2022, part1, True)
    part("Two", 20, 2022, part2, True)