with open("day-07-input.txt", 'r') as f:
    addresses = f.readlines()

parsed_adress = []

tables = []

for address in addresses:
    address = address.strip()
    address = address.replace("[", "]")
    address = address.split("]")
    
    parsed_adress.append(address)

    table = []

    for seq in address:
        truth = False
        for i in range(0,len(seq)-3):
            if seq[i:i+2] == seq[i+2:i+4][::-1] and seq[i] != seq[i+1]:
                truth = True
                break
        table.append(truth)

    tables.append(table)

total = 0

for table in tables:
    if any(table[1::2]) == False and any(table[0::2]):
        total += 1

print("Part One:", total)