import math
from itertools import cycle

with open("input.txt", "r") as f:
    trees = f.readlines()

trees = list(zip(*[list(tree.strip()) for tree in trees]))

def calc(r, d):
    counter_x, counter_y = 0, 0
    trees_total = 0
    for column in cycle(trees):
        if counter_x % r == 0 and counter_x != 0:
            counter_y += d
            if column[counter_y] == "#":
                trees_total += 1
        counter_x += 1
        if counter_y == len(trees[0]) - 1:
            return trees_total
    
slopes_list = [(1, 1),(3, 1), (5, 1), (7, 1), (1, 2)]

print('Part 1', calc(3,1))
print('Part 2', math.prod([calc(*slope) for slope in slopes_list]))
