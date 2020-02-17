import numpy as np

with open("day-08-input.txt", 'r') as f:
    instructions = f.readlines()

instructions = [instruction.strip() for instruction in instructions]

#print(instructions)

screen = np.zeros((5,50))

#print(screen)
screen[:3,:2] = 1
#print(screen[:3,:2])

for instruction in instructions:
    #print(instruction.split(" ",1))

    instruction = instruction.split(" ",1)
    if instruction[0] == 'rect':
        x,y = list(map(int, instruction[1].split("x")))
        screen[:x, :y] = 1

print(screen)


