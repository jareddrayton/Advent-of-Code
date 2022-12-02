with open("input.txt", "r") as fh:
    lines = fh.readlines()


mapping_shape = {"X": 1, "Y": 2, "Z": 3}

mapping_outcome = {
    "AX": 3,
    "BY": 3,
    "CZ": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
}


def part1():

    score = 0

    for line in lines:
        opponent, player = line.split()
        outcome = f"{opponent}{player}"
        score += mapping_outcome[outcome] + mapping_shape[player]

    print("Part 1:", score)


def part2():

    score = 0

    for line in lines:
        opponent, result_type = line.split()

        # Need to Lose
        if result_type == "X":
            if opponent == "A":
                score += mapping_outcome["AZ"] + mapping_shape["Z"]
            elif opponent == "B":
                score += mapping_outcome["BX"] + mapping_shape["X"]
            elif opponent == "C":
                score += mapping_outcome["CY"] + mapping_shape["Y"]
        # Need to Draw
        elif result_type == "Y":
            if opponent == "A":
                score += mapping_outcome["AX"] + mapping_shape["X"]
            elif opponent == "B":
                score += mapping_outcome["BY"] + mapping_shape["Y"]
            elif opponent == "C":
                score += mapping_outcome["CZ"] + mapping_shape["Z"]
        # Need to win
        elif result_type == "Z":
            if opponent == "A":
                score += mapping_outcome["AY"] + mapping_shape["Y"]
            elif opponent == "B":
                score += mapping_outcome["BZ"] + mapping_shape["Z"]
            elif opponent == "C":
                score += mapping_outcome["CX"] + mapping_shape["X"]

    print("Part 2:", score)


if __name__ == "__main__":
    part1()
    part2()
