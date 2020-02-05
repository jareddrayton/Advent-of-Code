with open("3.txt", "r") as f:
    a,b = f.readlines()


a = a.split(",")
b = b.split(",")


def walk_func(steps):

    all_points = []

    path = [(0,0)]
    
    x_coord, y_coord = 0, 0
    
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

            for x in range(path[i][0] -1, x_coord -1, -1):
                all_points.append((x, y_coord))

        elif direction == "U":
            y_coord += distance 

            for x in range(path[i][1], y_coord):
                all_points.append((x_coord, x + 1))
            
        elif direction == "D":
            y_coord -= distance 

            for x in range(path[i][1] -1, y_coord - 1, -1):
                all_points.append((x_coord, x))

        path.append((x_coord, y_coord))
        
        #print(path)
        #Sprint(all_points)
        #print("")


    return set(all_points), all_points


lista, outa = walk_func(a)
listb, outb = walk_func(b)


def manhattan_dist(tup):
    x_1, y_1 = tup
    
    return abs(x_1-0) + abs(y_1-0)


intersects = list(lista.intersection(listb))

print("Intersections", intersects)

new = []

#print(outa)
#print(outb)


for intersect in intersects:
    print("Intersection", intersect)
    #print(outa.index(intersect))
    #print(outb.index(intersect))
    new.append(outa.index(intersect)+outb.index(intersect))


#distances = list(map(manhattan_dist, intersects))

#print(distances)

#print(min(distances))

print(new)
print(min(new), "Smallest value in new")

