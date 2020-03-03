import string

with open("day-05-input.txt", 'r') as f:
    polymers = list(f.readline())

patterns = [[u,l] for u,l in zip(string.ascii_lowercase, string.ascii_uppercase)] + [[l,u ] for u,l in zip(string.ascii_lowercase, string.ascii_uppercase)]

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

for l,u in zip(string.ascii_lowercase, string.ascii_uppercase):
    new = []
    for abc in polymers2:
        if abc != l and abc != u:
            new.append(abc)
    shortest.append(len(react(new)))

print("Part Two:", min(shortest))
