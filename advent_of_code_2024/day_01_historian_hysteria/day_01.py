from collections import Counter


def parse_input():
    with open("input.txt") as fh:
        lines = [line.split() for line in fh.readlines()]

    l_list = sorted([int(line[0]) for line in lines])
    r_list = sorted([int(line[1]) for line in lines])

    return l_list, r_list


def part_1(l_list, r_list):
    total = 0

    for x, y in zip(l_list, r_list):
        difference = abs(x - y)
        total += difference

    return total


def part_2(l_list, r_list):
    total = 0
    r_counts = Counter(r_list)

    for l_value in l_list:
        product = l_value * r_counts[l_value]
        total += product

    return total


if __name__ == "__main__":
    l_list, r_list = parse_input()
    print(part_1(l_list, r_list))
    print(part_2(l_list, r_list))
