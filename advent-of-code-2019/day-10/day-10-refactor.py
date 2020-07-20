import math
from operator import itemgetter
from itertools import cycle

def extract_asteroid_coords():
    with open("day-10-input.txt", 'r') as f:
        asteroid_belt = f.readlines()
    asteroid_coords = [(x, y) for y, row in enumerate(asteroid_belt) 
                              for x, col in enumerate(row.strip()) if col  == "#"]
    return asteroid_coords


def calculate_angle(ast_x_coord, sta_x_coord, sta_y_coord, ast_y_coord):
    angle = math.atan2(ast_x_coord - sta_x_coord, sta_y_coord - ast_y_coord)
    angle = math.degrees(angle)
    if angle < 0:
        angle += 360
    return angle


def build_station_info():
    stations = {}
    asteroids = extract_asteroid_coords()
    for potential_station in asteroids:
        stations[potential_station] = []
        for asteroid in asteroids:
            if asteroid != potential_station:
                sta_x_coord, sta_y_coord = potential_station
                ast_x_coord, ast_y_coord = asteroid
                angle = calculate_angle(ast_x_coord, sta_x_coord, sta_y_coord, ast_y_coord)
                euc_distance = math.hypot(ast_x_coord - sta_x_coord, ast_y_coord - sta_y_coord)
                stations[potential_station].append((angle, ast_x_coord, ast_y_coord, euc_distance))
    return stations


def part_one(potential_stations):
    unique_angles = [len(set([i[0] for i in v])) for v in potential_stations.values()]
    return max(unique_angles)


def part_two(stations):
    test = [(len(set([i[0] for i in v])), k) for k, v in stations.items()]
    monitoring_station = sorted(test)[-1][1]
    
    asteroids_ordered = sorted(stations[monitoring_station], key=itemgetter(0, 3))
    asteroids_destroy_order = [asteroids_ordered[0]]
    
    for asteroid in cycle(asteroids_ordered):
        if asteroids_destroy_order[-1][0] != asteroid[0]:
            asteroids_destroy_order.append(asteroid)
        if len(asteroids_destroy_order) == 200:
            break
    return asteroids_destroy_order[-1][1] * 100 + asteroids_destroy_order[-1][2]


if __name__ == '__main__':
    stations = build_station_info()
    print("Part 1:", part_one(stations))
    print("Part 2:", part_two(stations))
