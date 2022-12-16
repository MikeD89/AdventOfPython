# AoC 2022 - Day 15 - Mike D
import math
import sys
import os
import string
from tqdm import tqdm
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=15, year=2022)
testdata = get_testdata(day=15, year=2022)


def vector_length(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calc_sensor_distance(sensors, beacons, i):
    return calculate_manhattan_distance(sensors[i][0], sensors[i][1], beacons[i][0], beacons[i][1])

def parse_data(input):
    sensors = []
    beacons = []
    for line in input.splitlines():
        sensor, beacon = line.split(":")
        sensor = sensor.replace("Sensor at x=", "").replace(" y=", "")
        (x, y) = sensor.split(",")
        sensors.append((int(x), int(y)))

        beacon = beacon.replace(" closest beacon is at x=", "").replace(" y=", "")
        (x, y) = beacon.split(",")
        beacons.append((int(x), int(y)))

    max_distance = 0
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]
        distance = calculate_manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])
        max_distance = max(max_distance, distance)

    minX = min([b[0] for b in sensors + beacons]) - max_distance
    minY = min([b[1] for b in sensors + beacons]) - max_distance
    maxX = max([b[0] for b in sensors + beacons]) + max_distance
    maxY = max([b[1] for b in sensors + beacons]) + max_distance
    minP = (minX, minY)
    maxP = (maxX, maxY)

    return (sensors, beacons, minP, maxP)

def find_intersections(sensors, beacons, minP, maxP, y):
    d = []
    for i in range(len(sensors)):
        d.append(calc_sensor_distance(sensors, beacons, i))

    v = set()
    # WITH THE POWER OF BRUTE FORCE WE SHALL PREVAIL
    for p in tqdm(range(minP[0], maxP[0] + 1)):
        point = (p, y)      
        
        for i in range(len(sensors)):
            sensor = sensors[i]
            beacon = beacons[i]
            distance = calculate_manhattan_distance(sensor[0], sensor[1], point[0], point[1])

            if sensor != point and beacon != point and distance <= d[i]:
                v.add(p)
                break

    return len(v)

def subtract_vector(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def find_point(sensors, beacons, minP, maxP, limit):
    for i in tqdm(range(len(sensors))):
        sensor = sensors[i]
        beacon = beacons[i]
        distance = calculate_manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])
        distance += 1

        vecs = [(sensor[0] - distance, sensor[1]),
                (sensor[0], sensor[1] - distance),
                (sensor[0] + distance, sensor[1]),
                (sensor[0], sensor[1] + distance)]

        perimiter = []
        for i, v in enumerate(vecs):
            v1 = vecs[i+1] if i < len(vecs) - 1 else vecs[0]
            p = v
            dX = 1 if v1[0] > v[0] else -1
            dY = 1 if v1[1] > v[1] else -1
            while True:
                last = True if p[0] == v1[0] and p[1] == v1[1] else False
                perimiter.append(p)
                p = (p[0] + dX, p[1] + dY)
                if last:
                    break

        for p in perimiter:
            if p[0] > limit or p[1] > limit or p[0] < 0 or p[1] < 0:
                continue

            valid = True
            for j in range(len(sensors)):
                second_sensor = sensors[j]
                second_beacon = beacons[j]
                bD = calculate_manhattan_distance(second_sensor[0], second_sensor[1], second_beacon[0], second_beacon[1])
                tD = calculate_manhattan_distance(second_sensor[0], second_sensor[1], p[0], p[1])

                if tD <= bD:
                    valid = False
                    break
            if valid:
                return p[0] * 4000000 + p[1]
    
    return None
        

def part1():
    tD = False
    input = testdata if tD else data
    (sensors, beacons, minP, maxP) = parse_data(input)

    y = 10 if tD else 2000000
    return find_intersections(sensors, beacons, minP, maxP, y)  
    
def part2():
    tD = False
    input = testdata if tD else data
    (sensors, beacons, minP, maxP) = parse_data(input)

    y = 20 if tD else 4000000
    return find_point(sensors, beacons, minP, maxP, y)  

if __name__ == "__main__":
    print("-- AoC 2022 - Day 15 --\n")
    # part("One", 15, 2022, part1, True)
    part("Two", 15, 2022, part2, True)
