with open("day-07-input.txt", 'r') as f:
    addresses = f.readlines()

parsed_adress = []

tables = []

total = 0

for address in addresses:
    address = address.strip()
    address = address.replace("[", "]")
    address = address.split("]")
    
    parsed_adress.append(address)

    aba = []

    for seq in address[::2]:
        for i in range(0, len(seq)-2):
            if seq[i:i+2] == seq[i+1:i+3][::-1] and seq[i] != seq[i+1]:
                aba.append(seq[i:i+3])
    
    for seq in address[1::2]:
        for a in aba:
            if seq.count(a[1:]+a[1]) > 0:
                total += 1
                break

print("Part Two:", total)