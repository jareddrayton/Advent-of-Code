with open("input.txt", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]


def make_sets(line):
    def make_set(elf):
        start, stop = elf.split("-")
        start, stop = int(start), int(stop)
        return set(range(start, stop + 1))

    elf_1, elf_2 = line.split(",")
    elf_1, elf_2 = make_set(elf_1), make_set(elf_2)
    return elf_1, elf_2


def part1():
    total = 0
    for line in lines:
        elf_1, elf_2 = make_sets(line)
        if len(elf_1) > len(elf_2):
            elf_2, elf_1 = elf_1, elf_2
        if len(elf_1 - elf_2) == 0:
            total += 1

    print("Part 1:", total)


def part2():
    total = 0
    for line in lines:
        elf_1, elf_2 = make_sets(line)
        if len(elf_1 & elf_2):
            total += 1

    print("Part 2:", total)


if __name__ == "__main__":
    part1()
    part2()
