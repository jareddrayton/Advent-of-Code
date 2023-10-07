from pathlib import Path


def parse_input():
    puzzle_input = Path(__file__).parent / "input.txt"
    with open(puzzle_input, "r") as f:
        directions = list(f.readline())
    return directions


def part_1():
    directions = parse_input()
    return directions.count("(") - directions.count(")")


def part_2():
    directions = parse_input()
    current_floor = 0
    for i, direction in enumerate(directions, start=1):
        if direction == "(":
            current_floor += 1
        elif direction == ")":
            current_floor -= 1

        if current_floor == -1:
            return i


if __name__ == "__main__":
    print("Part One:", part_1())
    print("Part Two:", part_2())
