# Read the challenge data from text file
with open("1.txt", 'r') as f:
    modules = f.readlines()

# Simultaneously strip trailing new lines and convert strings to integers
modules = [int(module.strip()) for module in modules]

def mass_rec(mass):
    # Perform the division and rounding
    mass = int(mass / 3.0)
    mass -= 2
    
    # Check for the base case
    if mass < 0:
        return 0

    # Recursive Case
    return mass + mass_rec(mass)


print(mass_rec(1969))

#fuel_rec = list(map(mass_rec, modules))

#print(sum(fuel_rec))