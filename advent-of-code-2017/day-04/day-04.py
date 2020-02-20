with open("day-04-input.txt", 'r') as f:
    passphrases = f.readlines()

total_p1 = 0
total_p2 = 0

for passphrase in passphrases:
    passphrase = passphrase.strip().split()
    
    if len(set(passphrase)) == len(passphrase):
        total_p1 += 1

    passphrase = ["".join(sorted(a)) for a in passphrase]

    if len(set(passphrase)) == len(passphrase):
        total_p2 += 1

print("Part One:", total_p1)
print("Part Two:", total_p2)