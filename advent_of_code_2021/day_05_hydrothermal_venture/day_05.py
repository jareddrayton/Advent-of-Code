import numpy as np

with open('input.txt', 'r') as f:
    vents = [list(map(int, (line.strip().replace(' -> ', ',').split(',')))) for line in f.readlines() if line.strip()]

max_x = max([vent[0] for vent in vents] + [vent[2] for vent in vents])
max_y = max([vent[1] for vent in vents] + [vent[3] for vent in vents])

horiz_verti = [vent for vent in vents if vent[0] == vent[2] or vent[1] == vent[3]]

ocean_floor = np.zeros((max_x+1, max_y+1), dtype=int)

for coord in horiz_verti:
    x_1, x_2 = sorted([coord[0], coord[2]])
    y_1, y_2 = sorted([coord[1], coord[3]])
    ocean_floor[y_1:y_2+1, x_1:x_2+1] += 1

overlaps  = np.ma.masked_where(ocean_floor > 1, ocean_floor)
print('Part 1:', np.sum(overlaps.mask))

for coord in vents:
    if coord not in horiz_verti:
        x_1, y_1, x_2, y_2 = coord
        coord = [(x_1, y_1), (x_2, y_2)]
        a,b = sorted(coord)
        x_1, y_1, x_2, y_2 = a + b

        x_coords = list(range(x_1, x_2+1))
        if y_1 > y_2:
            y_coords = list(range(y_1, y_2-1, -1))
        else:
            y_coords = list(range(y_1, y_2+1))
        
        for x, y in zip(x_coords, y_coords):
            ocean_floor[y, x] += 1

overlaps  = np.ma.masked_where(ocean_floor > 1, ocean_floor)
print('Part 2:', np.sum(overlaps.mask))
