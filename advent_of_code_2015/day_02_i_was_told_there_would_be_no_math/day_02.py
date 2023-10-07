from collections import namedtuple
from pathlib import Path


def parse_input():
    Present = namedtuple("Present", ["length", "width", "height"])

    puzzle_input = Path(__file__).parent / "input.txt"
    with open(puzzle_input, "r") as f:
        dimensions = f.readlines()

    dimensions = [list(map(int, x.strip().split("x"))) for x in dimensions]
    presents = [Present(*dimensions) for dimensions in dimensions]

    return presents


def part_1():
    presents = parse_input()
    wrapping = 0

    for present in presents:
        sides_A = 2 * present.length * present.width
        sides_B = 2 * present.length * present.height
        sides_C = 2 * present.width * present.height

        wrapping += sides_A + sides_B + sides_C + min(sides_A, sides_B, sides_C) // 2

    return wrapping


def part_2():
    presents = parse_input()
    ribbon = 0

    for present in presents:
        volume = present.length * present.width * present.height

        sides_A = 2 * present.length + 2 * present.width
        sides_B = 2 * present.length + 2 * present.height
        sides_C = 2 * present.width + 2 * present.height

        ribbon += volume + min(sides_A, sides_B, sides_C)

    return ribbon


if __name__ == "__main__":
    print("Part One:", part_1())
    print("Part Two:", part_2())
