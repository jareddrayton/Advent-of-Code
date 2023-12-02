from collections import defaultdict
from math import prod


def valid_game(game):
    game_id, rounds = game.split(": ")
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for round in rounds.split("; "):
        colours = [x.split() for x in round.split(", ")]
        for count, colour in colours:
            if int(count) > limits[colour]:
                return False
    return int(game_id.split()[1])


def minimum(game):
    rounds = game.split(": ")[1]
    minimums = defaultdict(list)
    for round in rounds.split("; "):
        colours = [x.split() for x in round.split(", ")]
        for count, colour in colours:
            minimums[colour].append(int(count))
    minimums = [max(v) for v in minimums.values()]
    return prod(minimums)


def part_1(games):
    return sum([valid_game(game) for game in games])


def part_2(games):
    return sum([minimum(game) for game in games])


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        games = [x.strip() for x in fh.readlines()]
    print(part_1(games))
    print(part_2(games))
