with open ("input.txt", 'r') as f:
    bag_list = f.readlines()

bag_list = [bag.split('bags contain') for bag in bag_list]
bag_list = [[bag[0], bag[1].split(',')] for bag in bag_list]

def format(bags):
    for bag in bags:
        if bag.strip() == 'no other bags.':
            return []
    new = []
    
    for bag in bags:
        bag = bag.strip()
        a, b = bag.split(" ", 1)
        a = int(a)
        b = " ".join(b.split(" ")[:-1])
        new.append((a,b))
    
    return new

bag_dict = {}

for bag in bag_list:
    bag_dict[bag[0].strip()] = format(bag[1])

def find_num_parents(bags):
    if bags == []:
        return []
    new_parens = []
    for bag in bags:
        new_parens += bag_dict[bag][1]
    return new_parens + find_num_parents(new_parens)

def find_num_bags(parent):
    children = bag_dict[parent][0]
    descendants = 0
    if children == []:
        return 0
    for child in children:
        descendants += child[0] +  child[0] * find_num_bags(child[1])
    return descendants

for k, v in bag_dict.items():
    bag_dict[k] = [bag_dict[k], []]

for k, v in bag_dict.items():
    for child in v[0]:
        bag_dict[child[1]][1].append(k)

bag = 'shiny gold'

print("Part 1", len(set(find_num_parents(bag_dict[bag][1]) + bag_dict[bag][1])))
print("Part 2", find_num_bags(bag))
