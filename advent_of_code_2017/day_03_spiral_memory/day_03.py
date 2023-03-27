from itertools import count

puzzle_input = 325489

dx = {"U": 0, "L": -1, "D": 0, "R": 1}
dy = {"U": 1, "L": 0, "D": -1, "R": 0}


def sum_adjacent_squares(x, y, ds):
    if x == 0 and y == 0:
        return 1
    return sum(
        [
            ds.get((x + 1, y), 0),
            ds.get((x - 1, y), 0),
            ds.get((x, y + 1), 0),
            ds.get((x, y - 1), 0),
            ds.get((x + 1, y + 1), 0),
            ds.get((x - 1, y + 1), 0),
            ds.get((x + 1, y - 1), 0),
            ds.get((x - 1, y - 1), 0),
        ]
    )


def direction_generator():
    x_gen = count(1, 2)
    y_gen = count(2, 2)
    while True:
        x, y = next(x_gen), next(y_gen)
        pattern = "R" * x + "U" * x + "L" * y + "D" * y
        for letter in pattern:
            yield letter


def part_1():

    answer = 0
    current_x, current_y = 0, 0

    for i, direction in enumerate(direction_generator(), start=1):

        if not i == puzzle_input:
            current_x += dx[direction]
            current_y += dy[direction]
        else:
            answer = abs(0 - current_x) + abs(0 - current_y)
            break

    return answer


def part_2():

    ds = {}
    answer = 0
    current_x, current_y = 0, 0

    for direction in direction_generator():
        answer = sum_adjacent_squares(current_x, current_y, ds)

        ds[current_x, current_y] = answer

        current_x += dx[direction]
        current_y += dy[direction]

        if answer > puzzle_input:
            break

    return answer


print("Part 1:", part_1())
print("Part 2:", part_2())
