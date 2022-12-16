# AoC 2022 - Day 16 - Mike D
from itertools import product
import json
import sys
import os
from itertools import permutations
from tqdm import tqdm
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=16, year=2022)
testdata = get_testdata(day=16, year=2022)

def parse(input):
    d = {}
    for line in input.splitlines():
        (valve, tunnels) = line.split(";")
        valve = valve.replace("Valve ", "").replace(" has flow rate", "")
        valve = valve.split("=")

        key = valve[0]
        d[key] = {}
        d[key]['self'] = key
        d[key]['rate'] = int(valve[1])
        d[key]['tunnels'] = tunnels.replace(" tunnels lead to valves ", "").replace(" tunnel leads to valve ", "").replace(" ", "").split(",")
    return d

def work_out_pathing(graph, destinations):
    for valve in tqdm(graph):
        graph[valve]['paths'] = {}
        graph[valve]['travel'] = {}

        if valve not in destinations and valve != "AA":
            continue

        for othervalve in graph:
            if valve != othervalve and graph[othervalve]['rate'] > 0:
                graph[valve]['paths'][othervalve] = find_quickest_route_through_graph(graph, valve, othervalve)
                graph[valve]['travel'][othervalve] = len(graph[valve]['paths'][othervalve]) - 1

def find_quickest_route_through_graph(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]['tunnels']:
        if node not in path:
            newpath = find_quickest_route_through_graph(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def calculate_scores(graph, current, remaining_time, open=[]):
    scores = {}
    for valve in graph:
        if valve != current:
            continue
        for othervalve in graph:
            if valve != othervalve:
                fr = graph[valve]
                to = graph[othervalve]

                if othervalve in open:
                    continue

                # no flow?
                if to['rate'] == 0:
                    continue
                
                # distance
                dist = fr['travel'][othervalve]
                score = to['rate']
                total_score = score * (remaining_time - dist)

                # add to scores
                scores[othervalve] = total_score
    return scores

def get_destinations(graph):
    desinations = []
    for valve in graph:
        if graph[valve]['rate'] != 0:
            desinations.append(valve)
    return desinations

def get_length(graph, points, start, destinations):
    l = []
    last = start
    for i in range(len(points)):
        current = destinations[points[i]]
        l.append(graph[last]['travel'][current])
        last = current
    return sum(l)

def score_perms(perm, totalValves, highest, graph, start, max_length):
    points = list(perm)
    moving = -1
    current = start
        
    score=0
    open=0
    for i in range(max_length):
        score += open

        remaining = (totalValves) * (max_length - i)
        if((score + remaining) < highest):
            return 0
            
        if moving <= 0 and len(points) > 0:
            # move
            next = points.pop(0)
            moving = graph[current]['travel'][next]
            current = next
        else:
            moving -= 1
            if moving == 0:
                # open
                open += graph[current]['rate']

    return score

def depth_first_traversal(graph, start, destinations, max_length):
    data = []
    def helper(node, visited, length, highest): 
        nonlocal data       
        # Visit the current node if it has not already been visited
        if node != start:
            visited.append(node)
            score = score_perms(visited, totalValves, highest, graph, start, max_length)
            if(score != 0):
                data.append([score, visited.copy()])
            highest = max(score, highest)

        # Recursively traverse each child of the current node
        for child in destinations:
            if child not in visited:
                # only if the child isn't too long
                distance = graph[node]['travel'][child] + length
                if distance > max_length:
                    continue

                score = helper(child, visited.copy(), distance, highest)
                if score > highest:
                    highest = score
        return highest

    # Start the traversal at the root node
    return  helper(start, [], 0, 0), data

start = "AA"
tD = False
input = testdata if tD else data
graph = parse(input)
destinations = get_destinations(graph)
totalValves = sum([graph[x]['rate'] for x in destinations if graph[x]['rate'] > 0])

print("Calculate pathing...")
work_out_pathing(graph, destinations)

def part1():
    p1A, _ = depth_first_traversal(graph, start, destinations, 30)
    return p1A
    
def part2():
    global destinations

    # naive approach - lets take the best possible human path and have nelly hoover up the rest
    # this is way faster than part 1 - note to self - reduce the time dimension first!!!!!

    human_answer, data = depth_first_traversal(graph, start, destinations, 26)

    all_humans = [x[1] for x in data if x[0] == human_answer]
    all_humans.sort(key=lambda x: len(x))
    shortest = all_humans[0]

    # get the destinations that are not in the shortest path
    elephant_destinations = [x for x in destinations if x not in shortest]
    elephant_answer, data = depth_first_traversal(graph, start, elephant_destinations, 26)
    
    return human_answer + elephant_answer

if __name__ == "__main__":
    print("-- AoC 2022 - Day 16 --\n")
    part("One", 16, 2022, part1, True)
    part("Two", 16, 2022, part2, True)