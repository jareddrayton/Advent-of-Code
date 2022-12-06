with open("input.txt", "r") as fh:
    signal = fh.read()


def find_message(buffer_size):

    index = 0
    buffer = []
    while index < len(signal):
        buffer.append(signal[index])
        if len(set(buffer[-buffer_size:])) == buffer_size:
            result = len(buffer)
            break
        index += 1
    return result


if __name__ == "__main__":
    print("Part 1:", find_message(4))
    print("Part 2:", find_message(14))
