# AoC 2023 - Day 6 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=6, year=2023)
testdata = get_testdata(day=6, year=2023)

def parse(input):
    input = input.splitlines()
    time = input[0]
    distance = input[1]
    time = time.split("Time:    ")[1]
    distance = distance.split("Distance:")[1]

    time = [int(t) for t in time.split(" ") if t != ""]
    distance =[int(t) for t in distance.split(" ") if t != ""]
    races =[]
    for i in range(len(time)):
        races.append([time[i], distance[i]])
    
    return races

def calc(time, distance):
    winners = 0
    for i in range(time):
        speed = i
        remaining = time - i
        total = speed * remaining
        if total > distance:
            winners += 1
    return winners

def part1():
    input = data
    input = parse(input)
    total = 1
    for i in input:
        total *= calc(i[0], i[1])
    
    return total
    
def part2():
    input = data
    input = parse(input)
    time = ""
    distance = ""
    for i in input:
        time = time + str(i[0])
        distance = distance + str(i[1])
   
    return calc(int(time), int(distance))

if __name__ == "__main__":
    print("-- AoC 2023 - Day 6 --\n")
    part("One", 6, 2023, part1, True)
    part("Two", 6, 2023, part2, True)