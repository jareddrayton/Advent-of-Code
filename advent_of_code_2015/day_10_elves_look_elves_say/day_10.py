def process_input(puzzle_input):
    output = ""
    count = 0
    current_digit = puzzle_input[0]

    for digit in puzzle_input:
        if digit == current_digit:
            count += 1
        else:
            output += f"{count}{current_digit}"
            current_digit = digit
            count = 1
    output += f"{count}{current_digit}"
    return output


def repeat_processing(puzzle_input, repeats):
    for _ in range(1, repeats + 1):
        puzzle_input = process_input(puzzle_input)

    return len(puzzle_input)


if __name__ == "__main__":
    puzzle_input = "1113122113"
    print("Part One:", repeat_processing(puzzle_input, 40))
    print("Part Two:", repeat_processing(puzzle_input, 50))
