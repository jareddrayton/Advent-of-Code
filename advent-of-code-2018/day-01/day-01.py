from itertools import cycle

with open("day-01-input.txt", 'r') as f:
    frequencies = f.readlines()

frequencies = [int(x.strip()) for x in frequencies]

start = 0

for digit in frequencies:
    start += digit

print("Part One:", start)

stored = {}

start = 0
counter = 0
loop = 0

for item in cycle(frequencies):
    start = start + item
    if start in stored.keys():
        print("Part Two:", start)
        break
    elif counter % len(frequencies)== 0:
        loop +=1
        pass
    stored[start] = 1
    counter +=1