with open("day-06-input.txt", 'r') as f:
    messages = f.readlines()

messages = [message.strip() for message in messages]

messages = [x for y in messages for x in y]

new = []

for i in range(8):
    new.append(messages[i::8])

answer_1 = ""
answer_2 = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

for line in new:
    ab = []
    for char in alphabet:
        ab.append([line.count(char), char])
    answer_1 += max(ab)[1]
    answer_2 += min(ab)[1]

print("Part One:", answer_1)
print("Part Two:", answer_2)