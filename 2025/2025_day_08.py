# AoC 2025 - Day 8 - Mike D
import sys
import os
import string
import collections
import numpy as np
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=8, year=2025)
testdata = get_testdata(day=8, year=2025)

def split(input):
    input = [input.split(",") for input in input.splitlines()]
    return np.array([list(map(int, row)) for row in input])

def vector_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# def find_closest_pair(input, remove=True):
#     distances = np.linalg.norm(input[:, None] - input, axis=-1)
#     np.fill_diagonal(distances, np.inf)
#     # return the smallest distance
#     min_index = np.unravel_index(np.argmin(distances, axis=None), distances.shape)
#     # remove from input 
#     if remove:
#         input = np.delete(input, min_index, axis=0)
#     return min_index, input

def find_all_pairs(input):
    N = len(input)
    distances = np.linalg.norm(input[:, None] - input, axis=-1)
    np.fill_diagonal(distances, np.inf)
    i, j = np.triu_indices(N, k=1)  
    dists = distances[i, j] 
    order = np.argsort(dists)
    pairs = list(zip(i[order], j[order]))
    return pairs

def connect_closest_pairs(input, remaining_connections=10, debug=False):
    circuits = []
    sorted_indices = find_all_pairs(input)

    for (i, j) in sorted_indices:
        if remaining_connections <= 0:
            break
        remaining_connections -= 1

        added = -1
        for index, circuit in enumerate(circuits):
            if (i in circuit) and (j in circuit):
                # already in circuit
                added = -2
                break

            if (i in circuit) or (j in circuit):
                if added == -1:
                    # expand existing circuit
                    circuit.add(j)
                    circuit.add(i)
                    added = index
                else:
                    # merge circuits
                    circuits[added].update(circuit)
                    circuits.pop(index)

        # -1 = not added / -2 = already accounted for / anything else = index of where it was unioned
        # this is grim but it works!
        if added == -1:
            # add the pair to the circuit
            circuits.append(set([i, j]))

        closed_loop = len(circuits) == 1 and len(circuits[0]) == len(input)
        if closed_loop:
            return circuits, (input[i], input[j])

        if debug:
            print(input[i], input[j], remaining_connections)
            # mapped_circuits = [frozenset([tuple(input[i]) for i in circuit]) for circuit in circuits]
            # print(remaining_connections, (i, j), circuits)
    return circuits, None

def part1():
    input = split(data)
    connections, _ = connect_closest_pairs(input, 1000, False)
    sizes = sorted([len(a) for a in connections], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]
    
def part2():
    input = split(data)
    _, closer = connect_closest_pairs(input, 1000000000000000000000, False)
    return closer[0][0].astype(np.int64) * closer[1][0].astype(np.int64)

if __name__ == "__main__":
    print("-- AoC 2025 - Day 8 --\n")
    part("One", 8, 2025, part1, True)
    part("Two", 8, 2025, part2, True)