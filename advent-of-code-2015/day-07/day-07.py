with open("day-07-input.txt", 'r') as f:
    instructions = f.readlines()

wires = {}

for instruction in instructions:
    instruction = instruction.strip()

    source, wire = instruction.split(" -> ")

    if wire not in wires.keys():
        wires[wire] = [[None],[],None]

    if " AND " in source:
        wires[wire][1] = (source.split(" AND "))
        wires[wire][2] = "AND"

    if " OR " in source:
        wires[wire][1] = (source.split(" OR "))
        wires[wire][2] = "OR"

    if "NOT " in source:
        wires[wire][1].append((source.split("NOT "))[1])
        wires[wire][2] = "NOT"
    
    if " RSHIFT " in source:
        wires[wire][1] = (source.split(" RSHIFT "))
        wires[wire][2] = "RSHIFT"

    if " LSHIFT " in source:
        wires[wire][1] = (source.split(" LSHIFT "))
        wires[wire][2] = "LSHIFT"
    
    if source.isnumeric() == True:
        wires[wire][0][0] = int(source)

    if source.isalpha() == True:
        wires[wire][1].append(source)

    
    print(wire, wires[wire])


print(wires["a"])

def calc(wire):
    for parent in wires[wire][1]:
        if wires[parent][1] == []:
            wires[wire] = wires[parent][0]
        



wires["a"][0][0] = calc("e")




# 2h29m12s57
# 14m00s01