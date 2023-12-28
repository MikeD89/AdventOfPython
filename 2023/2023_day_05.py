# AoC 2023 - Day 5 - Mike D
import sys
import os
import string
from aocd import get_data, submit
from tqdm import tqdm
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *
import functools
from tqdm.contrib.concurrent import process_map 


from multiprocessing import Pool


data = get_data(day=5, year=2023)
testdata = get_testdata(day=5, year=2023)

def parse(data):
    maps = []
    seeds = []
    lines = data.splitlines()
    i = 0
    m = []
    p = []

    while i < len(lines):
        line = lines[i]
        i+=1
        if line.startswith("seeds:"):
            seeds = line.split("seeds: ")[1].split(" ")
            seeds = [int(s) for s in seeds]
            continue
        if line == "":
            continue
        if line.find("map:") != -1:
            m = []
            maps.append(m)
        else:
            d = line.split(" ")
            d = {
                "dest": int(d[1]),
                "end": int(d[1]) + int(d[2]),
                "source": int(d[0]),
                "length": int(d[2]),
            }
            m.append(d)  
    return seeds, maps

def next(n, m):
    for r in m:
        if n >= r["dest"] and n < r["end"]:
            v = r["source"] + (n - r["dest"])
            return v
    return n

def process(seed, maps):
    for m in maps:
        seed = next(seed, m)
    return seed

def part1():
    input = data
    seeds, maps = parse(input)
    lowest = 99999999999999999999999999999999999999999999999999999999
    for seed in seeds:
        result = process(seed, maps)   
        if result < lowest:
            lowest = result

    return lowest
    
def parse_p2seeds(seeds):
    i = 0
    s = []
    while i < len(seeds):
        left = seeds[i]
        right = seeds[i+1]
        s.append((left, right))
        i+=2

    return s

def calc(start, length, maps):
    if length == 1:
        return min(process(start, maps), process(start+1, maps))
    
    half = int(length / 2)
    sv = process(start, maps)
    mv = process(start + half, maps)
    ee = process(start + length, maps)

    lowest = 9999999999999999999999999999
    if sv + half != mv:
        lowest = calc(start, half, maps)
    
    if mv + (length - half) != ee:
        lowest = calc(start + half, (length - half), maps)
    
    return lowest


def part2():
    input = data
    seeds, maps = parse(input)
    seeds = parse_p2seeds(seeds)

    lowest = 9999999999999999999999999999999999999999999
    for seed in seeds:
        min = calc(seed[0], seed[1], maps)
        if min < lowest:
            lowest = min
    return lowest

if __name__ == "__main__":
    print("-- AoC 2023 - Day 5 --\n")
    part("One", 5, 2023, part1, True)
    part("Two", 5, 2023, part2, True)