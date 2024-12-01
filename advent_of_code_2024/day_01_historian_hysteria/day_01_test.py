from day_01 import part_1, part_2, parse_input


def test_part_1():
    l_list, r_list = parse_input()
    assert part_1(l_list, r_list) == 2815556


def test_part_2():
    l_list, r_list = parse_input()
    assert part_2(l_list, r_list) == 23927637
