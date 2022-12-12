# AoC 2022 - Day 12 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=12, year=2022)
testdata = get_testdata(day=12, year=2022)

def prnt(grid):
    print('\n'.join(''.join(str(x) for x in row) for row in grid))

def canStep(grid, src, dest):
    srcV = grid[src[0]][src[1]]
    destV = grid[dest[0]][dest[1]]

    srcI = getI(srcV)
    destI = getI(destV)

    return (destI + 1) - srcI >= 0 

def getI(i):
    if i == "S":
        return string.ascii_lowercase.index("a")
    elif i == "E":
        return string.ascii_lowercase.index("z")
    else:
        return string.ascii_lowercase.index(i)

def getNeighbours(grid, node):
    neighbours = []
    if node[1] + 1 < len(grid[0]):
        neighbours.append((node[0], node[1] + 1))
    if node[1] - 1 >= 0:
        neighbours.append((node[0], node[1] - 1))
    if node[0] + 1 < len(grid):
        neighbours.append((node[0] + 1, node[1]))
    if node[0] - 1 >= 0:
        neighbours.append((node[0] - 1, node[1]))
    neighbours = [n for n in neighbours if canStep(grid, node, n)]
    return neighbours

def end_func_p1(grid, node):
    return grid[node[0]][node[1]] == "S"

def end_func_p2(grid, node):
    return grid[node[0]][node[1]] == "a"

def bfs(grid, start, ef):
    queue = []
    queue.append([start])
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = getNeighbours(grid, node)
            for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if ef(grid, neighbour):
                        return new_path
            visited.add(node)
    return None


def parse(input):
    m = []
    start = None
    end = None
    for x, line in enumerate(input.splitlines()):
        l = []
        for y, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            l.append(c)
        m.append(l)
    return m, start, end

def run(input, eF):
    grid, start, end = parse(input)
    return len(bfs(grid, end, eF)) - 1

def part1():
    return run(data, end_func_p1)
    
def part2():
    return run(data, end_func_p2)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 12 --\n")
    part("One", 12, 2022, part1, True)
    part("Two", 12, 2022, part2, True)
