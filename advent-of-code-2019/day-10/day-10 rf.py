import math
from operator import itemgetter
from itertools import cycle

with open("day-10-input.txt", 'r') as f:
    asteroid_belt = f.readlines()


def calculate_angle():
    pass

asteroids = [(x, y) for y, row in enumerate(asteroid_belt) 
                    for x, col in enumerate(list(row.strip())) if col  == "#"]

potential_stations = {}

for potential_station in asteroids:
    potential_stations[potential_station] = []
    for asteroid in asteroids:
        if asteroid != potential_station:
            sta_x_coord, sta_y_coord = potential_station
            ast_x_coord, ast_y_coord = asteroid
            
            angle = math.degrees(math.atan2(ast_x_coord - sta_x_coord, sta_y_coord - ast_y_coord))
            if angle < 0:
                angle += 360
            
            euc_distance = math.sqrt((ast_x_coord - sta_x_coord) ** 2 + 
                                    (ast_y_coord - sta_y_coord) ** 2)

            potential_stations[potential_station].append((angle, ast_x_coord, ast_y_coord, euc_distance))

test = [(len(set([i[0] for i in v])), k) for k, v in potential_stations.items()]

best = sorted(test)[-1][1]

asteroids_ordered = []

for asteroid in cycle(sorted(potential_stations[best], key=itemgetter(0, 3))):
    if asteroids_ordered == []:
        asteroids_ordered.append(asteroid)
    elif asteroids_ordered[-1][0] != asteroid[0]:
        asteroids_ordered.append(asteroid)
    
    if len(asteroids_ordered) == 200:
        break

print("Part 1:", max([i[0] for i in test]))
print("Part 2:", asteroids_ordered[-1][1] * 100 + asteroids_ordered[-1][2])