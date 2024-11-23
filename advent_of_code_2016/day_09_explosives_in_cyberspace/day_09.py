from pathlib import Path
import re
import math


def part_1(compressed, uncompressed):
    regex = re.compile(r"\(\d+x\d+\)")
    match = regex.search(compressed)

    if match:
        uncompressed += compressed[: match.span()[0]]
        length, repeats = to_int(match)
        temp = compressed[match.span()[1] : match.span()[1] + length]
        temp = temp * repeats
        uncompressed += temp
        compressed = compressed[match.span()[1] + length :]
        return part_1(compressed, uncompressed)
    else:
        uncompressed += compressed
        return len(uncompressed)


def to_int(match: re.Match):
    length, repeats = match.group().split("x")
    length, repeats = int(length[1:]), int(repeats[:-1])
    return length, repeats


def check_no_overlap(string):
    if not string:
        return [True]
    regex = re.compile(r"\(\d+x\d+\)")
    match = regex.search(string)
    length, _ = to_int(match)
    new_str = string[match.span()[1] : match.span()[1] + length]
    if regex.search(new_str):
        return [False]
    else:
        return [True] + check_no_overlap(string[match.span()[1] + length :])


def part_2(string):
    regex = re.compile(r"\(\d+x\d+\)")
    match = regex.search(string)

    if not match:
        return len(string)

    num_l, num_r = to_int(match)

    if match.span()[0]:
        return len(string[: match.span()[0]]) + part_2(string[match.span()[0] :])

    if all(check_no_overlap(string)):
        foo = [math.prod(to_int(x)) for x in re.finditer(regex, string)]
        return sum(foo)

    l_string = string[match.span()[1] : match.span()[1] + num_l]
    r_string = string[match.span()[1] + num_l :]

    if r_string:
        return num_r * part_2(l_string) + part_2(r_string)

    if num_l == len(l_string):
        return num_r * (part_2(l_string))


if __name__ == "__main__":
    puzzle_input = Path(__file__).parent / "input.txt"

    with open(puzzle_input, "r") as fh:
        compressed = fh.read().strip()

    print("Part 1:", part_1(compressed, ""))
    print("Part 2:", part_2(compressed))
