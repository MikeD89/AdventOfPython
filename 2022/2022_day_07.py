# AoC 2022 - Day 7 - Mike D
import sys
import os
import string
from aocd import get_data, submit
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *

data = get_data(day=7, year=2022)
testdata = get_testdata(day=7, year=2022)

blacklist = ['parent', 'size', 'name']

def split(input):
    s = []
    for l in input.splitlines():
        if l.startswith("$"):
            s.append([l])
        else:
            s[-1].append(l)
    return s

def build_tree(input):
    parsed = {'name': '/'}
    current = parsed

    for line in input:
        cmd = line[0]
        if cmd == "$ cd /":
            current = parsed
        elif cmd == "$ ls":
            for l in line:
                if not l.startswith("$"):
                    (s, n) = l.split(" ")
                    if s == "dir":
                        current[n] = { 'parent': current, 'name': n }
                    else:  
                        current[n] = int(s)
                        
        elif cmd == "$ cd ..":
            current = current['parent']
        else:
            cmd = cmd.replace("$ cd ", "")
            current = current[cmd]
    return parsed

def calc_sizes(node):
    s = 0
    for k, v in node.items():
        if k in blacklist:
            pass
        elif isinstance(v, int):
            s += v
        else:
            calc_sizes(v)
            s += v['size']

    node['size'] = s

def count_dirs(t, cap=100000):
    s = 0
    if t['size'] < cap:
        s += t['size']
    for k, v in t.items():
        if k in blacklist:
            pass
        elif isinstance(v, int):
            pass
        else:
            s += count_dirs(v)
    return s  

def squish_dirs(t, o):
    o[t['name']] = t['size']
    
    for k, v in t.items():
        if k in blacklist:
            pass
        elif isinstance(v, int):
            pass
        else:
            squish_dirs(t[k], o)

def del_dir(sizes, td=70000000, unused=30000000):
    current_unused = td - sizes['/']
    missing = unused - current_unused

    lowest_num = None
    lowest_name = None

    for k, v in sizes.items():
        if v > missing and (lowest_num is None or v < lowest_num):
            lowest_num = v
            lowest_name = k
    
    return sizes[lowest_name]
    

def part1():
    i = split(data)
    t = build_tree(i)
    calc_sizes(t)

    return count_dirs(t)
    
def part2():
    i = split(data)
    t = build_tree(i)
    calc_sizes(t)

    sizes = {}
    squish_dirs(t, sizes)

    return del_dir(sizes)

if __name__ == "__main__":
    print("-- AoC 2022 - Day 7 --\n")
    part("One", 7, 2022, part1, True)
    part("Two", 7, 2022, part2, True)