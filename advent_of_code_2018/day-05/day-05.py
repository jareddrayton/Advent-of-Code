import string

with open("day-05-input.txt", 'r') as f:
    polymers = list(f.readline())

alphabet = list(zip(string.ascii_lowercase, string.ascii_uppercase))

patterns = [[upper, lower] for upper, lower in alphabet] + [[lower, upper] for upper, lower in alphabet]

polymers1, polymers2 = polymers.copy(), polymers.copy()

def react(lst):

    index = 0
    while index <= len(lst):
        if lst[index:index+2] in patterns:
            del lst[index] 
            del lst[index]
            index -= 1
        else:
            index += 1
    return lst

print("Part One:", len(react(polymers1)))

shortest = []

for lower_case, upper_case in zip(string.ascii_lowercase, string.ascii_uppercase):
    new = []
    for abc in polymers2:
        if abc != lower_case and abc != upper_case:
            new.append(abc)
    shortest.append(len(react(new)))

print("Part Two:", min(shortest))
