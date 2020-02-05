with open("6.txt", 'r') as f:
    orbits = f.readlines()

#print(orbits)



new = [x.strip().split(')') for x in orbits]

#print(new)

a = [x[0] for x in new]
b = [x[1] for x in new]

#print(a)
#print(b)




tree = {}

# add parent and
for orbit in new:
    if orbit[0] not in tree:
        tree[orbit[0]] = [[],[]]
        tree[orbit[0]][0].append(orbit[1])
    elif orbit[0] in tree:
        tree[orbit[0]][0].append(orbit[1])

for orbit in new:
    if orbit[1] not in tree:
        tree[orbit[1]] = [[],[]]
        tree[orbit[1]][1].append(orbit[0])
    elif orbit[1] in tree:
        tree[orbit[1]][1].append(orbit[0])

print(tree)


# calculate 

orbit_total = 0

def step(count, key):

    
    #print(tree[key][1])
    if len(tree[key][1]) == 0:
        return count
    else:
        count += 1
        return step(count, tree[key][1][0])
    


for key in tree:

    orbit_total += step(0, key)

print(orbit_total)
print(len(tree.keys()))

    
print(tree["YOU"])
print(tree["SAN"])

def total(stops, key):

    
    #print(tree[key][1])
    if len(tree[key][1]) == 0:
        return stops
    else:
        stops.append(key)
        return total(stops, tree[key][1][0])


    
you = set(total([], "YOU"))
san = set(total([], "SAN"))

print(you)
print(san)

print(len(you.symmetric_difference(san)) -2 )