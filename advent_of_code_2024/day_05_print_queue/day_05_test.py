from day_05 import part_1, part_2, parse_input


def test_part_1():
    page_order, instr = parse_input("input.txt")
    assert 5762 == part_1(page_order, instr)


def test_part_2():
    page_order, instr = parse_input("input.txt")
    assert 4130 == part_2(page_order, instr)


def test_sample_part_1():
    page_order, instr = parse_input("sample_input.txt")
    assert 143 == part_1(page_order, instr)


def test_sample_part_2():
    page_order, instr = parse_input("sample_input.txt")
    assert 123 == part_2(page_order, instr)
