with open("day-04-input.txt", 'r') as f:
    room_scrambled = f.readlines()

template = "abcdefghijklmnopqrstuvwxyz"

room_parsed = []

for room in room_scrambled:
    room, hash_part = room.strip().split('[')
    hash_part = hash_part.strip(']')
    sector_id = int("".join([char for char in room if char.isdigit()]))
    encryp_name = "".join([char for char in room if not char.isdigit()])
    room_parsed.append([encryp_name, hash_part, sector_id])

def cipher(cipherd_text, offset):
    
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'

    cipher = [x for x in range(len(alphabet_string))]

    cipher = cipher[offset:] + cipher[:offset]

    trans = ""

    for letter in cipherd_text:
        if letter.isalpha():
            trans += (alphabet_string[cipher[alphabet_string.rindex(letter)]])
        else:
            trans += " "
    return trans

for i in range(len(room_parsed)):
    room_parsed[i][0] = cipher(room_parsed[i][0], room_parsed[i][2]%26)

for room in room_parsed:
    if room[0].count("pole") > 0:
        print("Part Two:", room[2])