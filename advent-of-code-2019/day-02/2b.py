with open("2.txt", 'r') as f:
    modules = f.readline()

modules = modules.split(",")

# Convert the strings to integers
modules = [int(module.strip()) for module in modules]

def intcode(modulesb, n, v):
    #print(modulesa)
    #print(modulesa)
    modulesa = modulesb

    index = 0
    #print(modulesa)
    modulesa[1] = n
    modulesa[2] = v
    
    while modulesa[index] != 99:
        #print(index)
        if modulesa[index] == 1:
            modulesa[modulesa[index+3]] = modulesa[modulesa[index+1]] + modulesa[modulesa[index+2]]
            index += 4
        elif modulesa[index] == 2:
            modulesa[modulesa[index+3]] = modulesa[modulesa[index+1]] * modulesa[modulesa[index+2]]
            index += 4
        else:
            break

    return modulesa[0]

noun, verb = 99, 99

#print(type(modules))

# Iterate through all combinations of noun and verb value
for n in range(noun + 1):
    for v in range(verb + 1):
        
        # call the intcode executer and return the result of 
        test = intcode(modules, n, v)
        
        # check if it matches tartget result and break if true
        if test == 19690720:
            print("Answer", 100 * n + v)
            break

print("a", id(modules))