def part_1(lines):
    def extract_digits(line):
        digits = [x for x in line if x.isdigit()]
        return int(digits[0] + digits[-1])

    return sum([extract_digits(line) for line in lines])


def part_2(lines):
    return sum(
        [
            int(extract_numbers(line, False) + extract_numbers(line, True))
            for line in lines
        ]
    )


def extract_numbers(line, reverse):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if reverse:
        line = line[::-1]
        numbers = [x[::-1] for x in numbers]

    digit = None
    i = 0
    while not digit:
        if line[i:][0].isdigit():
            digit = line[i:][0]
            break
        else:
            for j, number in enumerate(numbers, start=1):
                if line[i:].startswith(number):
                    digit = j
                    break
        i += 1

    return str(digit)


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        lines = [x.strip() for x in fh.readlines()]

    print(part_1(lines))
    print(part_2(lines))
