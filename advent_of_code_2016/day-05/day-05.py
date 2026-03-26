from hashlib import md5

puzzle_input = "wtnhxymk"


def part_1(prefix="00000"):
    index = 0
    password = ""

    while len(password) < 8:
        candidate = puzzle_input + str(index)
        hash = md5(candidate.encode()).hexdigest()

        if hash.startswith(prefix):
            password += hash[5]
        index += 1

    return password


def part_2(prefix="00000"):
    index = 0
    password = ["", "", "", "", "", "", "", ""]

    while not all(password):
        candidate = puzzle_input + str(index)
        hash = md5(candidate.encode()).hexdigest()

        if hash.startswith(prefix):
            if hash[5].isdigit() and int(hash[5]) < 8 and not password[int(hash[5])]:
                password[int(hash[5])] = hash[6]
        index += 1

    return "".join(password)


print("Part One:", part_1())
print("Part Two:", part_2())
