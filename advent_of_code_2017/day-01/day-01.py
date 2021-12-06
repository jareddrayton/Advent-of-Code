with open("day-01-input.txt", 'r') as f:
    digits = f.readline()

digits = list(map(int,digits))

total = 0

for i in range(len(digits)-1):
    if digits[i] == digits[i+1]:
        total += digits[i]

if digits[0:1] == digits[-1:]:
    total += digits[0]

print("Part One:", total)

digits = digits[:] + digits[:]

totalb = 0

for i in range(len(digits)//2 ):
    if digits[i] == digits[i+len(digits)//4]:
        totalb += digits[i]

print("Part Two:", totalb)