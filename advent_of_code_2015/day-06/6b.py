import numpy as np

with open("input.txt", 'r') as f:
    instructions = f.readlines()

lights = np.zeros((1000, 1000))

def turn_off(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] -= 1
            if lights[i][j] < 0:
                lights[i][j] = 0

def turn_on(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] += 1

def toggle(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] += 2

for instruction in instructions:
    instruction = instruction.strip()

    if instruction.startswith("turn on"):
        a,b,c,d = map(int, instruction.strip("turn on ").replace(" through ", ',').split(","))
        turn_on(a,b,c,d)

    elif instruction.startswith("turn off"):
        a,b,c,d = map(int, instruction.strip("turn off ").replace(" through ", ',').split(","))
        turn_off(a,b,c,d)

    elif instruction.startswith("toggle"):
        a,b,c,d = map(int, instruction.strip("toggle ").replace(" through ", ',').split(","))
        toggle(a,b,c,d)
        
print("Part Two:", np.sum(lights))