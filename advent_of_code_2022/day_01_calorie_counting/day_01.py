with open("input.txt", "r") as fh:
    lines = fh.read().split("\n\n")
    lines = [line.split("\n") for line in lines]
    lines = [list(map(int, line)) for line in lines]
    lines = [sum(line) for line in lines]


def part1():
    result = max(lines)
    print("Part 1:", result)


def part2():
    result = sum(sorted(lines)[-3:])
    print("Part 2:", result)


if __name__ == "__main__":
    part1()
    part2()
