with open("day-07-input.txt", 'r') as f:
    programs = f.readlines()

print(programs)

tree = {}

for program in programs:
    
    program = program.strip()
    parent, children = program.split(")")

    parent, weight = parent.split(" (")

    print(parent, weight)


    children = children.strip(" ->").split(", ")

    if parent not in tree.keys():
        tree[parent] = [[int(weight)], []]

    #if children != ['']:
    print(children)
    for child in children:
        if child in tree.keys():
            tree[child][1].append(parent)

for k,v in tree:
    print(k,v)
                

print(tree)


