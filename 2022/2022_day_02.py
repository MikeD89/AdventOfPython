# AoC 2022 - Day 2 - Mike D
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from aocd import get_data, submit
from utils import *

# Handle data
data = get_data(day=2, year=2022)

# 1 rock, 2 paper, 3 scissors
# 0 lost, 3 draw, 6 win
def score(win, lose, option):
    score = 1 if option == "x" else 2 if option == "y" else 3
    if win:
        return score + 6
    elif lose:
        return score + 0
    else:
        return score + 3

# a rock, b paper, c scissors
# x rock, y paper, z scissors
# x = lose, y = draw, z = win
def calc_score(you, me):
    lose = (me == "z" and you == "a") or (me == "x" and you == "b") or (me == "y" and you == "c")
    win = (me == "y" and you == "a") or (me == "z" and you == "b") or (me == "x" and you == "c")
    return score(win, lose, me)

# a rock, b paper, c scissors
def calc_score_p2(you, result):
    win = False
    lose = False

    if result == "z": # win
        me = "y" if you == "a" else "z" if you == "b" else "x"
        win = True
    elif result == "x": # lose
        me = "z" if you == "a" else "x" if you == "b" else "y"
        lose = True
    else: #draw
        me = "x" if you == "a" else "y" if you == "b" else "z"

    return score(win, lose, me)

# Run Part 1
def part1():
    score = 0
    for line in data.splitlines():
        line = line.lower()
        (you, me) = line.split(" ")
        score += calc_score(you, me)
    return score
    
# Run Part 2
def part2():
    score = 0
    for line in data.splitlines():
        line = line.lower()
        (you, me) = line.split(" ")
        score += calc_score_p2(you, me)
    return score

# Main 
if __name__ == "__main__":
    print("-- AoC 2022 - Day 2 --\n")
    part("One", 2, 2022, part1, True)
    part("Two", 2, 2022, part2, True)