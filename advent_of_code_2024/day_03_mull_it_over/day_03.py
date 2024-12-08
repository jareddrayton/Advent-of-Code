import re


def parse_input():
    with open("input.txt") as fh:
        lines = [line.strip() for line in fh.readlines()]
        lines = "".join(lines)

    return lines


def part_1(memory):
    regex_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

    matches: list[str] = regex_pattern.findall(memory)
    total = 0
    for match in matches:
        lh, rh = match.split(",")
        total += int(lh[4:]) * int(rh[:-1])
    return total


def part_2(memory):
    regex = r"don\'t\(\).*?(do\(\)|$)"
    memory = re.sub(regex, "", memory, count=0, flags=0)
    return part_1(memory)


if __name__ == "__main__":
    memory = parse_input()
    print(part_1(memory))
    print(part_2(memory))
