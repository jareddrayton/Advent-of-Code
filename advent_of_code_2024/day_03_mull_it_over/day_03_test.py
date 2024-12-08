from day_03 import part_1, part_2, parse_input


def test_part_1():
    memory = parse_input()
    assert part_1(memory) == 183788984


def test_part_2():
    memory = parse_input()
    assert part_2(memory) == 62098619
