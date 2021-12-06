import numpy as np
import math

puzzle_input = 325489

print(int(math.sqrt(325489)))

size = int(math.sqrt(325489)) + 1

grid = np.full((size, size), 0)

print(grid)

x,y = size//2, size//2

index = 0

grid[x,y] = 1

grid[2,0] =1
grid[0,2] = 3


print(grid)

while index < puzzle_input:

    while 

    index += 1 