with open("day-04-input.txt", 'r') as f:
    room_scrambled = f.readlines()

room_parsed = []

for room in room_scrambled:
    
    room, hash_part = room.strip().split('[')
    hash_part = hash_part.strip(']')
    sector_id = int("".join([char for char in room if char.isdigit()]))
    encryp_name = "".join([char for char in room if char.isalpha()])
    room_parsed.append([encryp_name, hash_part, sector_id])

def isreal(room):

    template = "abcdefghijklmnopqrstuvwxyz"

    freq = []

    for c in template:
        freq.append([c, room[0].count(c)])

    check = []

    for _ in range(0,5):
        check.append(max(freq, key = lambda x: x[1]))
        freq.remove(max(freq, key = lambda x: x[1]))

    check = "".join([y for x in check for y in x][::2])

    if check == room[1]:
        return room[2]
    else:
        return 0

total = 0

for room in room_parsed:
    total += isreal(room)

print("Part One:", total)