import numpy as np
from pathlib import Path

np.set_printoptions(suppress=True, linewidth=np.nan)
puzzle_input = Path(__file__).parent / "input.txt"
with open(puzzle_input, "r") as fh:
    instructions = fh.readlines()

A = 50
B = 6

screen = np.zeros((B, A))

for instruction in instructions:
    instruction = instruction.strip().split()

    match instruction:
        case "rect", x:
            C, D = x.split("x")
            C, D = int(C), int(D)
            screen[:D, :C] = 1
        case "rotate", "row", row, _, x:
            row = int(row.split("=")[-1])
            x = int(x)
            new = screen[row, :]
            new = list(new[-x:]) + list(new[:-x])
            screen[row, :] = new
        case ["rotate", "column", column, _, x]:
            column = int(column.split("=")[-1])
            x = int(x)
            new = screen[:, column]
            new = list(new[-x:]) + list(new[:-x])
            screen[:, column] = new


def part_1():
    return np.count_nonzero(screen)


def part_2():
    print(screen)
    return "ZJHRKCPLYJ"


if __name__ == "__main__":
    part_1()
    part_2()
