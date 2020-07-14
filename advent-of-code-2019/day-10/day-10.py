import math
import numpy as np

with open("day-10-input.txt", 'r') as f:
    asteroid_belt = f.readlines()

# Convert input test to numpy array of booleans
asteroid_belt = [list(asteroid.strip()) for asteroid in asteroid_belt]
asteroid_belt = [[True if a == "#" else False for a in b] for b in asteroid_belt]
asteroid_belt = np.array(asteroid_belt)

# Create a list of indexs from numpy array that 
keys = list(zip(np.nonzero(asteroid_belt)[0], np.nonzero(asteroid_belt)[1]))

stations = {}

for station in keys:
    stations[station] = set()
    #print(len(stations.keys()))
    for asteroid in stations.keys():
        if asteroid != station:
            #radians = math.atan2(station[1]-asteroid[1], asteroid[0]-station[0]) + math.pi
            #stations[station].add(int(math.degrees(radians) * 100) / 100.0)
            stations[station].add(round(math.atan2(station[1]-asteroid[1], asteroid[0]-station[0]) +math.pi,1) )

test = []

for k,v in stations.items():
    test.append(len(v))
    #print(k,v)

#print(test) 
#print(len(test))
print(max(test))