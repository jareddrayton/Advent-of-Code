from day_10 import repeat_processing


puzzle_input = "1113122113"


def test_part_1():
    assert repeat_processing(puzzle_input, 40) == 360154


def test_part_2():
    assert repeat_processing(puzzle_input, 50) == 5103798
