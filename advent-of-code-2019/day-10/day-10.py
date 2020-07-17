import math
import numpy as np
from operator import itemgetter

with open("day-10-input.txt", 'r') as f:
    asteroid_belt = f.readlines()

# Convert input test to numpy array of booleans
asteroid_belt = [list(asteroid.strip()) for asteroid in asteroid_belt]
asteroid_belt = [[True if a == "#" else False for a in b] for b in asteroid_belt]
asteroid_belt = np.array(asteroid_belt)

# Create a list of indexes from the numpy array that represent asteroids 
asteroids = list(zip(np.nonzero(asteroid_belt)[0], np.nonzero(asteroid_belt)[1]))

potential_stations = {}

for potential_station in asteroids:
    potential_stations[potential_station] = []
    for asteroid in asteroids:
        if asteroid != potential_station:
            sta_x_coord, sta_y_coord = potential_station
            ast_x_coord, ast_y_coord = asteroid

            angle = math.degrees(math.atan2(sta_y_coord - ast_y_coord, ast_x_coord - sta_x_coord))
            euc_distance = math.sqrt((ast_x_coord - sta_x_coord) ** 2 + (ast_y_coord - sta_y_coord) ** 2)
            
            potential_stations[potential_station].append((angle, ast_x_coord, ast_y_coord, euc_distance))

test = [(len(set([i[0] for i in v])), k) for k, v in potential_stations.items()]

print("Part 1:", max([i[0] for i in test]))
print("Part 2:")

print(sorted(test)[-1])
print(sorted(potential_stations[sorted(test)[-1][1]], key=itemgetter(0,3)))