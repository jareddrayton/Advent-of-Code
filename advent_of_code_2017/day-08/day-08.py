with open("day-08-input.txt", 'r') as f:
    instructions = f.read().splitlines()

registers = {}

for register in instructions:
    register = register.split()
    registers[register[0]] = 0

inc_dec = {"inc": 1, "dec": -1}

highest = 0

for instruction in instructions:
    reg, sign, amount, iff, reg2, condition, amount2 = instruction.split()

    if condition == "==" and registers[reg2] == int(amount2):
        registers[reg] += inc_dec[sign] * int(amount)
    elif condition == "!=" and registers[reg2] != int(amount2):
        registers[reg] += inc_dec[sign] * int(amount)
    elif condition == "<" and registers[reg2] < int(amount2):
        registers[reg] += inc_dec[sign] * int(amount)
    elif condition == ">" and registers[reg2] > int(amount2):
        registers[reg] += inc_dec[sign] * int(amount)
    elif condition == "<=" and registers[reg2] <= int(amount2):
        registers[reg] += inc_dec[sign] * int(amount)
    elif condition == ">=" and registers[reg2] >= int(amount2):
        registers[reg] += inc_dec[sign] * int(amount)
    
    if max(registers.values()) > highest:
        highest = max(registers.values())

print("Part One:", max(registers.values()))
print("Part Two:", highest)