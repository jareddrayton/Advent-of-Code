import re

with open("input.txt", 'r') as fh:
    lines = [line.strip() for line in fh.readlines()]

regex = r'(\\\\)|(\\")|(\\x[\d|a-f]{2})'

def part1():
    line_length = []
    encoded_length = []
    for line in lines:
        total = len(line) - 2
        matches = re.findall(regex, line)
        if matches:
            for match in matches:
                if match[0]:
                    total -= 1
                if match[1]:
                    total -= 1
                if match[2]:
                    total -= 3
        line_length.append(len(line))
        encoded_length.append(total)

    return sum(line_length) - sum(encoded_length)

def part2():
    line_length = []
    encoded_length = []
    for line in lines:
        total = len(line) + 4
        matches = re.findall(regex, line)
        if matches:
            for match in matches:
                if match[0]:
                    total += 2
                if match[1]:
                    total += 2
                if match[2]:
                    total += 1
        line_length.append(len(line))
        encoded_length.append(total)

    return sum(encoded_length)- sum(line_length)

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
