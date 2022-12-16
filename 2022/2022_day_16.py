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

def score_perms(perm, totalValves, highest, graph, start, max_length, elephant):
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

        remaining = (totalValves) * (max_length - i)
        if((score + remaining) < highest):
            return 0

        for person in state:                
            if person['moving'] <= 0 and len(person['points']) > 0:
                # move
                next = person['points'].pop(0)
                person['moving'] = graph[person['current']]['travel'][next]
                person['current'] = next
            else:
                person['moving'] -= 1
                if person['moving'] == 0:
                    # open
                    open += graph[person['current']]['rate']

    return score

def depth_first_traversal(graph, start, destinations, max_length, elephant):
    totalValves = sum([graph[x]['rate'] for x in destinations if graph[x]['rate'] > 0])

    def helper(node, visited, length, highest):        
        # Visit the current node if it has not already been visited
        child_scores = []
        if node != start:
            visited.append(node)
            child_scores.append(score_perms(visited, totalValves, highest, graph, start, max_length, elephant))
            highest = max(child_scores[0], highest)

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

                child_scores.append(score)
        return highest

    # Start the traversal at the root node
    return  helper(start, [], 0, 0)



start = "AA"
tD = False
input = testdata if tD else data
graph = parse(input)
destinations = get_destinations(graph)

print("Calculate pathing...")
work_out_pathing(graph, destinations)

def part1():
    return depth_first_traversal(graph, start, destinations, 30, False)
    
def part2():
    return depth_first_traversal(graph, start, destinations, 26, True)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 16 --\n")
    part("One", 16, 2022, part1, False)
    # part("Two", 16, 2022, part2, False)

















# def generate_perms_p2(graph, start, destinations, max_length, o=2):
#     n = len(destinations)
#     nset = set(range(n))
#     def inner(p):
#         l = len(p)
#         if l > 1:
#             length = get_length(graph, p, start, destinations)
#             if length > max_length:
#                 retVal = []
#                 for i in range(o):
#                     retVal.append([p])
#                 return retVal
#         if l == n:
#             retVal = []
#             for i in range(o):
#                 retVal.append([p])
#             return retVal
#         r = []
#         for i in nset - set(p):
#             for rr in inner(p + (i,)):
#                 r.append(rr)
#         return r
                
#     return inner(())




    # current = [start]
    # traverse(destinations, current.copy())
    # print(c)


    # return highest



    # # push the first path into the queue
    # queue.append([start])
    # while queue:
    #     # get the first path from the queue
    #     path = queue.pop(0)
    #     # get the last node from the path
    #     node = path[-1]
    #     # path found
    #     if node == end:
    #         return path
    #     # enumerate all adjacent nodes, construct a 
    #     # new path and push it into the queue
    #     for adjacent in graph.get(node, []):
    #         new_path = list(path)
    #         new_path.append(adjacent)
    #         queue.append(new_path)




# def generate_perms(graph, start, destinations, max_length, elephant=False):
    
        
#     n = len(destinations)
#     nset = set(range(n))
#     def inner(p):
#         l = len(p)
#         if l > 1:
#             length = get_length(graph, p, start, destinations)
#             if length > max_length:
#                 score = score_perms(p, totalValves, highest, graph, start, destinations, max_length, elephant)
#                 return [score]
#         if l == n:
#             return [p]
#         return [r for i in nset - set(p)
#                 for r in inner(p + (i,))]
#     return inner(())