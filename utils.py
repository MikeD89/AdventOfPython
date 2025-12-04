import os
import sys
from aocd import get_data, submit

from collections import defaultdict

def time_it(func, name=None):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        n = name if name else func.__name__
        print(f"-  Runtime: {end-start:.4f} seconds")
        return result
    return wrapper

# Runner
def part(part, day, year, func, submit_to_aoc):
    print(f'-- Part {part}')
    result = str(time_it(func)())
    print("-  Result:  " + result)
    if submit_to_aoc and result != "None":
        print("-  Submitting...")
        p = "a" if part == "One" else "b"
        submit(result, part=p, day=day, year=year)
    else:
        print("-  Not Submitting!")
    print()

def tests(runner, do):
    if not do:
        return
    print("-  Running Tests:")
    str(time_it(runner)())
    print()

def get_testdata(day, year):
    filename = str(year) + "_day_" + f"{day:02}" + ".txt"
    return load_testdata(year, filename)

def load_testdata(year, filename):
    testdata_path = os.path.join(os.path.dirname(__file__), str(year),  "testdata", filename)
    return open(testdata_path, "r").read()

def make_grid(w, h, fill):
    return [[fill] * w for _ in range(h)]

def print_grid(grid):
    print('\n'.join(''.join(str(x) for x in row) for row in grid))

def load_into_default_dict(input, filler="."):
    grid = defaultdict(lambda: defaultdict(lambda: filler))

    for  index, line in enumerate(input):
        for index_2, char in enumerate(line):
            grid[index][index_2] = char

    return grid