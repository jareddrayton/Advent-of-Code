with open("3.txt", "r") as f:
    a,b = f.readlines()


a = a.split(",")
b = b.split(",")


def walk_func(steps):

    a_list = []

    x_coord = 0
    y_coord = 0
    
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    for step in steps:

        step = step.strip()
        direction = step[0]
        distance = int(step[1:])

        if direction == "U":
            y_coord = y_coord + distance 
        elif direction =="D":
            y_coord = y_coord - distance
        elif direction == "R":
            x_coord = x_coord + distance
        elif direction == "L":
            x_coord = x_coord - distance

        a_list.append((x_coord, y_coord))

        if x_coord > max_x:
            max_x = x_coord
        if y_coord > max_y:
            max_y = y_coord
        if x_coord < max_x:
            min_x = x_coord
        if y_coord < max_y:
            min_y = y_coord
    
    limits = max_x, min_x, max_y, min_y

    return a_list, limits


def manhattan_dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

lista, limits_a = walk_func(a)
listb, limits_b = walk_func(b)


def grid_size(limits_a, limits_b):

    XMAX = max(limits_a[0], limits_b[0])
    XMIN = min(limits_a[1], limits_b[1])
    YMAX = max(limits_a[2], limits_b[2])
    YMIN = min(limits_a[3], limits_b[3])

    return XMAX + abs(XMIN), YMAX + abs(YMIN)

shape = grid_size(limits_a, limits_b)

print(shape)

def empty_grid():
    
    grid = [["-" for x in range(shape[0])] for x in range(shape[1])]
    
    return grid

#print(empty_grid(shape))

print(lista)

def path(lista):
    
    grid = empty_grid()

    print(lista)
    prevx = 0
    prevy = 0
    for coord in lista:
        x,y = coord
        
        for i in range(prevx, x):
            grid[i][prevy] = "X"

    
    return "a"

grid_a = path(lista)


