from string import ascii_lowercase, ascii_uppercase

with open("input.txt", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]


priority_dict = dict([(k, v) for v, k in enumerate(ascii_lowercase + ascii_uppercase, start=1)])


def part1():
    priority_total = 0
    for line in lines:
        middle = len(line) // 2
        bag_1, bag_2 = line[:middle], line[middle:]
        both = set(bag_1) & set(bag_2)
        for item_type in both:
            priority_total += priority_dict[item_type]
    print("Part 1:", priority_total)


def part2():
    priority_total = 0
    for i in range(0, len(lines), 3):
        bag_1, bag_2, bag_3 = lines[i], lines[i + 1], lines[i + 2]
        in_all = set(bag_1) & set(bag_2) & set(bag_3)
        for item_type in in_all:
            priority_total += priority_dict[item_type]
    print("Part 2:", priority_total)


if __name__ == "__main__":
    part1()
    part2()
