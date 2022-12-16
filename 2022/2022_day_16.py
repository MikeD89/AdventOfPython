# AoC 2022 - Day 16 - Mike D
from itertools import product
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

def generate_perms(graph, start, destinations, max_length):
    n = len(destinations)
    nset = set(range(n))
    def inner(p):
        l = len(p)
        if l > 1:
            length = get_length(graph, p, start, destinations)
            if length > max_length:
                return [p]
        if l == n:
            return [p]
        return [r for i in nset - set(p)
                for r in inner(p + (i,))]
    return inner(())

def score_perms(graph, start, destinations, perms, max_length, elephant=True):
    highest = 0
    totalValves = sum([graph[x]['rate'] for x in destinations if graph[x]['rate'] > 0])
    for perm in tqdm(perms):
        state = []
        state.append({
            'points': list(perm) if not elephant else list(perm[0]),
            'moving': -1,
            'current': start
        })
        if elephant:
            state.append({
                'points': list(perm[1]) if elephant else [],
                'moving': -1,
                'current': start
            })

        score=0
        open=0
        for i in range(max_length):
            score += open
            remaining = (totalValves - open) * (max_length - i)

            if(remaining < highest):
                break

            for person in state:                
                if person['moving'] <= 0 and len(person['points']) > 0:
                    # move
                    next = person['points'].pop(0)
                    next = destinations[next]
                    person['moving'] = graph[person['current']]['travel'][next]
                    person['current'] = next
                else:
                    person['moving'] -= 1
                    if person['moving'] == 0:
                        # open
                        open += graph[person['current']]['rate']

        if score > highest:
            highest = score
    return highest

def part1():
    tD = False
    start = "AA"

    max_length = 30
    input = testdata if tD else data
    graph = parse(input)
    destinations = get_destinations(graph)

    print("Calculate pathing...")
    work_out_pathing(graph, destinations)

    print("Generating permutations...")
    perms = generate_perms(graph, start, destinations, max_length)

    print("Scoring...")
    best_perm = score_perms(graph, start, destinations, perms, max_length)
    return best_perm
    
def part2():
    tD = True
    start = "AA"

    max_length = 26
    input = testdata if tD else data
    graph = parse(input)
    destinations = get_destinations(graph)

    print("Calculate pathing...")
    work_out_pathing(graph, destinations)

    print("Generating permutations...")
    perms = generate_perms(graph, start, destinations, max_length)

    print(len(perms))

    perms = [[
        [destinations.index(x) for x in ["JJ", "BB", "CC"]],
        [destinations.index(x) for x in ["DD", "HH", "EE"]],
    ]]

    print("Scoring...")
    best_perm = score_perms(graph, start, destinations, perms, max_length)
    return best_perm

if __name__ == "__main__":
    print("-- AoC 2022 - Day 16 --\n")
    # part("One", 16, 2022, part1, True)
    part("Two", 16, 2022, part2, False)

def generate_perms_p2(graph, start, destinations, max_length, o=2):
    n = len(destinations)
    nset = set(range(n))
    def inner(p):
        l = len(p)
        if l > 1:
            length = get_length(graph, p, start, destinations)
            if length > max_length:
                retVal = []
                for i in range(o):
                    retVal.append([p])
                return retVal
        if l == n:
            retVal = []
            for i in range(o):
                retVal.append([p])
            return retVal
        r = []
        for i in nset - set(p):
            for rr in inner(p + (i,)):
                r.append(rr)
        return r
                
    return inner(())