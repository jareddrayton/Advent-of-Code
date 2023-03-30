from itertools import product
from math import prod

import numpy as np

with open("input.txt", "r") as f:
    height_map = np.array([list(map(int, line.strip())) for line in f.readlines()])


def generate_adjacent(i: int, j: int) -> list:
    """Given a point on a grid, generate the adjacent point values and remove
    those which are out of bounds. Includes the given point.

    :param i: i index
    :type i: int
    :param j: j index
    :type j: int
    :return: List of adjacent coordinates tuples.
    :rtype: list
    """
    candidate_coords = [(i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    adjacent_coords = [(i, j) for i, j in candidate_coords if y_max > i > -1 and x_max > j > -1]

    return adjacent_coords


def is_low_point(window):
    point_values = [height_map[x, y] for x, y in window]
    unique_value = point_values.count(min(point_values)) == 1
    equal_point = min(point_values) == height_map[i, j]
    return True if unique_value and equal_point else False


y_max, x_max = height_map.shape
lowest_points = set()

coords = product(range(0, y_max), range(0, x_max))

for coord in coords:
    i, j = coord
    window = generate_adjacent(i, j)
    if is_low_point(window):
        lowest_points.add(coord)

total = 0

for point in lowest_points:
    x, y = point
    total += height_map[x, y] + 1


basins = {}
checked_points = set()


def basin_finder(point: tuple) -> list:

    x, y = point

    adjacent_points = generate_adjacent(x, y)
    adjacent_points = [(x, y) for x, y in adjacent_points if (x, y) not in checked_points]
    adjacent_points = [(x, y) for x, y in adjacent_points if height_map[x, y] != 9]

    points = [point]

    for adjacent_point in adjacent_points:
        checked_points.add(point)
        points += basin_finder(adjacent_point)

    return points


for i in range(0, height_map.shape[0]):
    for j in range(0, height_map.shape[1]):
        if (i, j) not in checked_points and height_map[i, j] != 9:
            basin = basin_finder((i, j))
            basins[(i, j)] = len(set(basin))

result = sorted(basins.values())[-3:]


assert total == 558
print("Part 1:", total)

assert prod(result) == 882942
print("Part 2:", prod(result))
