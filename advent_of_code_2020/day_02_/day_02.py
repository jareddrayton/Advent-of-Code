with open('input.txt', 'r') as f:
    nums = f.readlines()

def parse_input(policy):
    new = []
    for entry in policy:
        password = entry.split(':')[1].strip()
        char = entry.split()[1].strip(':')
        limits = entry.split()[0]
        limit_lower, limit_higher = limits.split('-')
        
        new.append([int(limit_lower), int(limit_higher), char, password])
    return new

def find_password(parsed_data):
    
    valid_password_count = 0
    for entry in parsed_data:
        
        if entry[0] <= entry[3].count(entry[2]) <= entry[1]:
            valid_password_count += 1

    return valid_password_count


def find_password_b(parsed_data):
    valid_password_count = 0
    
    for entry in parsed_data:
        a = entry[3][entry[0]-1] == entry[2]
        b = entry[3][entry[1]-1] == entry[2]
        if a ^ b:
            valid_password_count += 1
    return valid_password_count

a = parse_input(nums)
b = find_password(a)
c = find_password_b(a)
print(b)
print(c)