with open("3.txt", "r") as f:
    a,b = f.readlines()

a = a.split(",")
b = b.split(",")

def walk_func(steps):

    all_points = []

    path = [(0,0)]
    
    x_coord = 0
    y_coord = 0
    
    for i, step in enumerate(steps):

        step = step.strip()
        direction = step[0]
        distance = int(step[1:])

        if direction == "R":
            x_coord += distance

            for x in range(path[i][0], x_coord + 1):
                all_points.append((x, y_coord))

        if direction == "L":
            x_coord -= distance

            for x in range(path[i][0], x_coord -1, -1):
                all_points.append((x, y_coord))

        elif direction == "U":
            y_coord += distance 

            for x in range(path[i][1], y_coord):
                all_points.append((x_coord, x + 1))
            
        elif direction == "D":
            y_coord -= distance 

            for x in range(path[i][1], y_coord - 1, -1):
                all_points.append((x_coord, x))


        path.append((x_coord, y_coord))
        
        #print(path)
        #print(all_points)
        #print("")
            


    return set(all_points)


lista = walk_func(a)
listb = walk_func(b)



def manhattan_dist(tup):
    x_1, y_1 = tup
    
    return abs(x_1-0) + abs(y_1-0)


intersects = list(lista.intersection(listb))

print("Intersections", intersects)

distances = list(map(manhattan_dist, intersects))

distances.remove(0)

print(distances)

print(min(distances))


