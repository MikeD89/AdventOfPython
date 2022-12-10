# AoC 2022 - Day 10 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=10, year=2022)
testdata = get_testdata(day=10, year=2022)

def check(c, x):
    if c == 20 or (c - 20) % 40 == 0:
        return c * x
    return 0

def print_crt(values):
    print('\n'.join(''.join(str(x) for x in row) for row in values))

def run(input):
    c = 0
    x = 1
    q = None
    sum = 0
    w = 40
    h = 6

    crt = []
    for i in range(h):
        r = []
        for j in range(w):
            r.append(".")
        crt.append(r)
    
    queue = []
    for line in input.splitlines():
        queue.append(line)
    
    while queue != []:
        c += 1

        vP = (c - 1) // w
        hP = (c - 1) % w
        render = (x - 1 == hP) or (x == hP) or (x + 1 == hP)
        # print(c, " - ", vP, hP, " - ", x, " - ", render)

        if render:
            crt[vP][hP] = "#"

        if q != None:
            x += q
            q = None
        else:
            line = queue.pop(0)

            if line == "noop":
                pass
            else:
                q = int(line.split(" ")[1])           

        sum += check(c, x)

    # print(crt)
    print_crt(crt)
    return sum

def part1():
    return run(data)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 10 --\n")
    part("One", 10, 2022, part1, True)