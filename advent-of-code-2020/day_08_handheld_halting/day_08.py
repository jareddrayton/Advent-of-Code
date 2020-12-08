import copy
from operator import itemgetter

with open ("input.txt", 'r') as f:
    code = f.readlines()

def format(code):
    code = [loc.strip().split() for loc in code]
    code = [[a[0], int(a[1]), 0] for a in code ]
    return code

def find_infinite_loop(code, limit):
    
    accumulator = 0
    index = 0
    infinite = True
    
    while code[index][2] < limit:
        if code[index][0] == "acc":
            accumulator += code[index][1]
            index += 1
        elif code[index][0] == "jmp":
            index += code[index][1]
        elif code[index][0] == "nop":
            index += 1
        
        if index == len(code):
            infinite = False
            return (accumulator, infinite)
        
        code[index][2] += 1
    
    return (accumulator, infinite)       


def find_termintating_loop(code):
    
    replacement_lines = [(i, a[0]) for i, a in enumerate(code) if a[0] == "nop" or a[0] == "jmp"]

    for line in replacement_lines:
        new = copy.deepcopy(code)
        if new[line[0]][0] == "nop":
            new[line[0]][0] = "jmp"
        elif new[line[0]][0] == "jmp":
            new[line[0]][0] = "nop"

        result = find_infinite_loop(new, 4)

        if result[1] == False:
            return result

format_code = format(code)

print("Part 1", find_infinite_loop(format_code, 2))
print("Part 2", find_termintating_loop(format_code))
