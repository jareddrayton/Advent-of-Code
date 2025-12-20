import hashlib

puzzle_input = "wtnhxymk"

def number(prefix="00000"):

    index = 0

    password = ""

    while len(password) < 8:

        b = puzzle_input + str(index)
        test = hashlib.md5(b.encode())
        test = test.hexdigest()

        if test[:len(prefix)] == prefix:
            
            password += test[5]

        if len(password) == 8:
            return password

        index += 1

print("Part One:", number())

def numberb(prefix="00000"):

    index = 0

    password = [None, None, None, None, None, None, None, None]

    passa = 0

    while passa < 8:

        b = puzzle_input + str(index)
        test = hashlib.md5(b.encode())
        test = test.hexdigest()

        if test[:len(prefix)] == prefix:
            if test[5].isdigit() and int(test[5]) < 8 and password[int(test[5])] is None:
                password[int(test[5])] = test[6]
                passa += 1

        if passa == 8:
            return "".join(password)

        index += 1

print("Part Two:", numberb())