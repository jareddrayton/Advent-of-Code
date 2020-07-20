import math
from operator import itemgetter
from itertools import cycle

def extract_asteroid_coords():
    with open("day-10-input.txt", 'r') as f:
        asteroid_belt = f.readlines()
    asteroid_coords = [(x, y) for y, row in enumerate(asteroid_belt) 
                              for x, col in enumerate(row.strip()) if col  == "#"]
    return asteroid_coords


def calculate_angle(x_diff, y_diff):
    angle = math.atan2(x_diff, y_diff)
    angle = math.degrees(angle)
    if angle < 0:
        angle += 360
    return angle


def station_positions(asteroids, potential_station):
    x = []
    for asteroid in asteroids:
        if asteroid != potential_station:
            x_diff = asteroid[0] - potential_station[0]
            y_diff = potential_station[1] - asteroid[1]
            angle = calculate_angle(x_diff, y_diff)
            euc_distance = math.hypot(x_diff, y_diff)
            x.append((angle, euc_distance, asteroid[0], asteroid[1]))
    return x


def build_stations_dict():
    stations = {}
    asteroids = extract_asteroid_coords()
    for station in asteroids:
        stations[station] = station_positions(asteroids, station)
    return stations


def part_one(stations):
    test = [(len(set([i[0] for i in v])), k) for k, v in stations.items()]
    return sorted(test)[-1]


def part_two(stations):
    monitoring_station = part_one(stations)[1]
    asteroids_ordered = sorted(stations[monitoring_station], key=itemgetter(0, 1))
    asteroids_destroy_order = [asteroids_ordered[0]]
    
    for asteroid in cycle(asteroids_ordered):
        if asteroids_destroy_order[-1][0] != asteroid[0]:
            asteroids_destroy_order.append(asteroid)
        if len(asteroids_destroy_order) == 200:
            nth_asteroid = asteroids_destroy_order[-1]
            break

    return nth_asteroid[2] * 100 + nth_asteroid[3]


if __name__ == '__main__':
    stations = build_stations_dict()
    print("Part 1:", part_one(stations)[0])
    print("Part 2:", part_two(stations))
