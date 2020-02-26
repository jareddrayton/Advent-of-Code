with open("day-02-input.txt", 'r') as f:
    ids = f.readlines()

ids = [id.strip() for id in ids]

two = 0
three = 0

for new_id in ids:
    for digit in new_id:
        if new_id.count(digit) == 2:
            two += 1
            break
    for digit in new_id:
        if new_id.count(digit) == 3:
            three += 1
            break

print("Part One:", two * three)

for i, ida in enumerate(ids):
    differences = 0
    
    for j in range(i+1, len(ids)):
        differences = [x for x,y in zip(ida, ids[j]) if x == y]
        if len(differences) == len(ida)-1 :
            print("Part Two:", "".join(differences))
            break