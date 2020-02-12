with open("input.txt", 'r') as f:
    triangles = f.readlines()

triangles = [list(map(int,a.strip().split())) for a in triangles]

flattened_triangles = [y for x in triangles for y in x]

reshaped_triangles = []

for i in range(3):
    reshaped_triangles.append(flattened_triangles[i::3])

reshaped_triangles = [y for x in reshaped_triangles for y in x]

reshaped_triangles = [reshaped_triangles[i:i+3] for i in range(0, len(reshaped_triangles), 3)]

def isgreater(listofsides):
    total = 0
    
    for sides in listofsides:
        if sides[0] + sides[1] > sides[2] and sides[2] + sides[1] > sides[0] and sides[0] + sides[2] > sides[1]:
            total += 1
    return total

print("Part One:", isgreater(triangles))
print("Part Two:", isgreater(reshaped_triangles))