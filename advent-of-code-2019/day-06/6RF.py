with open("6.txt", 'r') as f:
    orbits = f.readlines()

orbit_list = [x.strip().split(')') for x in orbits]

tree = {}

# nodes and child and arent data 
for orbit in orbit_list:
    if orbit[0] not in tree:
        tree[orbit[0]] = [[orbit[1]],[]]
    else:
        tree[orbit[0]][0].append(orbit[1])

for orbit in orbit_list:
    if orbit[1] not in tree:
        tree[orbit[1]] = [[],[orbit[0]]]
    else:
        tree[orbit[1]][1].append(orbit[0])

def orbit_count(count, key):
    # Recursive function to count all orbits for a particular node
    if len(tree[key][1]) == 0:
        return count
    else:
        count += 1
        return orbit_count(count, tree[key][1][0])

orbit_total = 0

# Call recursive function for every node and keep running total 
for key in tree:
    orbit_total += orbit_count(0, key)

print("Part 1:", orbit_total)

def total(stops, key):
    # Almost indentical recursive function but instead of returning number of orbits it returns a list of them
    if len(tree[key][1]) == 0:
        return stops
    else:
        stops.append(key)
        return total(stops, tree[key][1][0])

you = set(total([], "YOU"))
san = set(total([], "SAN"))

# Use the symetric distance 
print("Part 2:", len(you.symmetric_difference(san)) -2)