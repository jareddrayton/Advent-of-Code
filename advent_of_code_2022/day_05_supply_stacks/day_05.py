from copy import deepcopy

with open("input.txt", "r") as fh:
    stacks, moves = fh.read().split("\n\n")
    stacks, moves = stacks.split("\n"), moves.split("\n")


def convert_stacks(stacks):

    stack_no = stacks.pop().split()
    stack_dict = {k: [] for k in stack_no}

    for i, stack in enumerate(stack_no, start=1):
        ind = i * 4
        for line in stacks:
            stack_dict[stack].append(line[ind - 4 : ind])

    stack_dict = {k: v[::-1] for k, v in stack_dict.items()}
    stack_dict = {k: [x[1] for x in v if x[1].isalpha()] for k, v in stack_dict.items()}

    return stack_dict


stacks = convert_stacks(stacks)


def apply_instructions(moves, part):

    new_stacks = deepcopy(stacks)
    for move in moves:

        _, quantity, _, origin, _, destination = move.strip().split()

        queue = []

        for _ in range(0, int(quantity)):
            letter = new_stacks[origin].pop()
            queue.append(letter)
        if part == "1":
            new_stacks[destination] += queue
        if part == "2":
            new_stacks[destination] += queue[::-1]
    result = [v[-1] for k, v in new_stacks.items()]

    return "".join(result)


if __name__ == "__main__":
    print("Part 1:", apply_instructions(moves, "1"))
    print("Part 2:", apply_instructions(moves, "2"))
