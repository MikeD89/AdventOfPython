# AoC 2022 - Day 15 - Mike D
import sys
import os
import string
from tqdm import tqdm
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=15, year=2022)
testdata = get_testdata(day=15, year=2022)

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

def find_point(sensors, beacons, minP, maxP, y):
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]
        distance = calculate_manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])

        # get perimeter
        distance += 1
        

        

def part1():
    tD = False
    input = testdata if tD else data
    (sensors, beacons, minP, maxP) = parse_data(input)

    y = 10 if tD else 2000000
    return find_intersections(sensors, beacons, minP, maxP, y)  
    
def part2():
    tD = True
    input = testdata if tD else data
    (sensors, beacons, minP, maxP) = parse_data(input)

    y = 20 if tD else 4000000
    return find_point(sensors, beacons, minP, maxP, y)  

if __name__ == "__main__":
    print("-- AoC 2022 - Day 15 --\n")
    # part("One", 15, 2022, part1, True)
    part("Two", 15, 2022, part2, False)







    # print("- Populate Grid")
    # width = maxX + offsetX + 1 + max_distance
    # height = maxY + offsetY + 1 + max_distance
    # b = [0] * (width * height)
    # print(width, height)
    # grid = make_grid(width, height, ".")
    # for i in range(len(sensors)):
    #     sensors[i] = [sensors[i][0] + offsetX, sensors[i][1] + offsetY]
    #     beacons[i] = [beacons[i][0] + offsetX, beacons[i][1] + offsetY]
    #     grid[sensors[i][1]][sensors[i][0]] = "S"
    #     grid[beacons[i][1]][beacons[i][0]] = "B"

    # print("- Handle Sensors")
    # for i in range(len(sensors)):
    #     print("-- Sensor " + str(i))
    #     sensor = sensors[i]
    #     beacon = beacons[i]
    #     distance = calculate_manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])

    #     minBeaconX = sensor[0] - distance
    #     maxBeaconX = sensor[0] + distance
    #     minBeaconY = sensor[1] - distance
    #     maxBeaconY = sensor[1] + distance

    #     for y in range(minBeaconY, maxBeaconY + 1):
    #         for x in range(minBeaconX, maxBeaconX + 1):
    #             if abs(calculate_manhattan_distance(sensor[0], sensor[1], x, y)) <= distance:
    #                 if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
    #                     print("not big enough")
    #                     exit()
    #                 elif grid[y][x] == ".":
    #                     grid[y][x] = "#"
    # return grid, offsetX, offsetY