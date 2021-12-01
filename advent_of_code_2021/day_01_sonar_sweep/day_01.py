with open('input.txt', 'r') as f:
    depths = [int(line.strip()) for line in f.readlines()]

increases = 0

for i in range(0, len(depths) -1):
    if depths[i+1] > depths[i]:
        increases += 1

increases_window = 0

for i in range(0, len(depths) -3):
    if sum(depths[i+1:i+4]) > sum(depths[i:i+3]):
        increases_window += 1

print('Part 1:', increases)
print('Part 2:', increases_window)
