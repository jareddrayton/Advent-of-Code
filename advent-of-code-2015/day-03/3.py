with open("input.txt", 'r') as f:
    directions = list(f.readline())

DX = {'v': 0, '^': 0, '<': -1, '>': 1}
DY = {'v': -1, '^': 1, '<': 0, '>': 0}

santa = directions[::2]
robo = directions[1::2]

def delivery_route(directions):

    houses = {}

    x_coord, y_coord = 0, 0

    for direction in directions:
        
        houses[str(x_coord) + ',' + str(y_coord)] = 1
        
        x_coord += DX[direction]
        y_coord += DY[direction]

    return set(houses.keys())

delivery_route(santa)

print("Part One:", len(delivery_route(directions)))

print("Part Two:", len(delivery_route(santa).union(delivery_route(robo))))