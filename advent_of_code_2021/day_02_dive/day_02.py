with open('input.txt', 'r') as f:
    instructions = [line.strip().split(' ') for line in f.readlines()]

def part1():

    depth, horizontal = 0, 0

    for instruction in instructions:
        if instruction[0] == 'up':
            depth += int(instruction[1]) * -1
        elif instruction[0] == 'down': 
            depth += int(instruction[1])
        elif instruction[0] == 'forward':
            horizontal += int(instruction[1])

    print(depth * horizontal)

def part2():

    aim, depth, horizontal = 0, 0, 0

    for instruction in instructions:
        if instruction[0] == 'up':
            aim += int(instruction[1]) * -1
        elif instruction[0] == 'down': 
            aim += int(instruction[1])
        elif instruction[0] == 'forward':
            horizontal += int(instruction[1])
            depth += aim * int(instruction[1])

    print(depth * horizontal)

part1()
part2()