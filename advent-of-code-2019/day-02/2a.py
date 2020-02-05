# Read the challenge data from text file
with open("2.txt", 'r') as f:
    modules = f.readline()

modules = modules.split(",")

print(modules)

modules = [int(module.strip()) for module in modules]

print(modules)

modules[1] = 12
modules[2] = 2

index = 0

while modules[index] != 99:
    if modules[index] == 1:
        modules[modules[index+3]] = modules[modules[index+1]] + modules[modules[index+2]]
        index += 4
    elif modules[index] == 2:
        modules[modules[index+3]] = modules[modules[index+1]] * modules[modules[index+2]]
        index += 4

print(modules[0])



######################################################





