# Read the challenge data from text file
with open("1.txt", 'r') as f:
    modules = f.readlines()

# Simultaneously strip trailing new lines and convert strings to integers
modules = [int(module.strip()) for module in modules]

# Create a function with the fuel calculation logic that can be passed into map()
def mass_calc(module):
    mass = int(module / 3.0)
    mass -= 2
    return mass


fuel = list(map(mass_calc, modules))

print(sum(fuel))