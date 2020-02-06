with open("input.txt", 'r') as f:
    present_dimensions = f.readlines()

present_dimensions =  [list(map(int,x.strip().split('x'))) for x in present_dimensions] 

total = 0

for present in present_dimensions:
    l = 2 * present[0] * present[1]
    w = 2 * present[0] * present[2]
    h = 2 * present[1] * present[2]

    total += (l+w+h) + min(l,w,h)/2

print("Part One:", total)

ribbon = 0 

for present in present_dimensions:
    
    volume = present[0] * present[1] * present[2]
    
    l = 2 * present[0] + 2 * present[1]
    w = 2 * present[0] + 2 * present[2]
    h = 2 * present[1] + 2 * present[2]

    ribbon += volume + min(l,w,h)

print("Part Two:", ribbon)