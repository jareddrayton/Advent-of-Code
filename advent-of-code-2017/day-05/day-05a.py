with open("day-05-input.txt", 'r') as f:
    steps = f.read().splitlines()

steps = list(map(int,steps))

index, total = 0,0

while index < len(steps):
    a = index
    index += steps[index]
    steps[a] += 1
    total +=1

print("Part One:", total)