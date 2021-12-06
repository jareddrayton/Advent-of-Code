import hashlib

def number(prefix="00000"):

    index = 346386

    answer = False

    while answer == False:
        
        puzzle_input = "iwrupvqb" + str(index)
        test = hashlib.md5(puzzle_input.encode())
        test = test.hexdigest()

        if test[:len(prefix)] == prefix:
            
            answer = True
            return index

        index += 1

print("Part One", number())
print("Part Two", number("000000"))