with open("day-02-input.txt", 'r') as f:
    digits = f.readlines()

checksum_a = 0
checksum_b = 0

for digit in digits:
    digit = digit.strip().split()
    digit = list(map(int, digit))

    checksum_a += max(digit) - min(digit)

    for a in digit:
        for b in digit:
            if a % b == 0 and a != b:
                checksum_b += a // b

print("Part One:", checksum_a)
print("Part Two:", checksum_b)