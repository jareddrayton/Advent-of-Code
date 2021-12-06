with open("input.txt", 'r') as f:
    directions = list(f.readline())

print("Part One:", directions.count("(") - directions.count(")") )

current_floor = 0

###################################################################

for i in range(len(directions)):
    
    if directions[i] == '(':
        current_floor += 1
    elif directions[i] == ')':
        current_floor -= 1
    
    if current_floor == -1:
        print("Part Two:", i+1)
        break