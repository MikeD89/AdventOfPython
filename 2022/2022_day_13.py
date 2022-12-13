# AoC 2022 - Day 13 - Mike D
import collections
import functools
import math
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=13, year=2022)
testdata = get_testdata(day=13, year=2022)

def compare(left, right):
    leftA = isinstance(left, collections.abc.Sequence)
    rightA = isinstance(right, collections.abc.Sequence)

    if not leftA and not rightA:
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0

    elif leftA and rightA:
        mR = max(len(left), len(right))
        for i in range(mR):
            if i >= len(left):
                return 1
            elif i >= len(right):
                return -1
            else:
                equal = compare(left[i], right[i])
                if equal == 1 or equal == -1:
                    return equal                

        if len(right) < len(left):
            return -1
        elif len(left) < len(right):
            return 1
        else:
            for i in range(len(left)):
                equal = compare(left[i], right[i])
                if equal == 1 or equal == -1:
                    return equal                

    elif leftA:
        r = [right]
        return compare(left, r)

    elif rightA:
        l = [left]
        return compare(l, right)

    else:
        print("Unexpected error")
        exit()

def part1():
    input = data
    input = input.splitlines()
    input = [input[i: i+2] for i in range(0, len(input), 3)]
    input = [[eval(i) for i in j] for j in input]
    input = [compare(i[0], i[1]) for i in input]
    input = [i+1 for i, x in enumerate(input) if x == 1]
    return sum(input)
    
def part2():
    input = data
    input = input.splitlines()
    input = [i for i in input if i != ""]
    input = [eval(j) for j in input]

    input.append(eval("[[2]]"))
    input.append(eval("[[6]]"))
    input.sort(key=functools.cmp_to_key(compare), reverse=True)

    two = input.index(eval("[[2]]")) + 1
    six = input.index(eval("[[6]]")) + 1
    return two * six

if __name__ == "__main__":
    print("-- AoC 2022 - Day 13 --\n")
    part("One", 13, 2022, part1, True)
    part("Two", 13, 2022, part2, True)