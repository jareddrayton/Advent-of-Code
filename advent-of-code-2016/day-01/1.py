with open("input.txt", 'r') as f:
    directions = f.readline()

orientation = ["N", "E", "S", "W"]

start_x, start_y = 0, 0

x, y = start_x, start_y

dx = {"N": 0, "E": 1, "S": 0, "W": -1}
dy = {"N": 1, "E": 0, "S": -1, "W": 0}

directions = directions.split(" ")

visited = {}

visited_twice = []

for direction in directions:
    
    direction = direction.strip(",")

    if direction[0] == "L":
        orientation = orientation[-1:] + orientation[:-1]
    elif direction[0] == "R":
        orientation = orientation[1:] + orientation[:1]
    
    for _ in range(int(direction[1:])):
        x +=  dx[orientation[0]] 
        y +=  dy[orientation[0]]
        
        located = str(x) + ',' + str(y)

        if located in visited.keys():
            visited_twice.append(located)
        else:
            visited[located] = None
  
a, b = visited_twice[0].split(",") 
        
print("Part One:", abs(int(x)-start_x) + abs(int(y)-start_y))
print("Part Two:", abs(int(a)-start_x) + abs(int(b)-start_y))