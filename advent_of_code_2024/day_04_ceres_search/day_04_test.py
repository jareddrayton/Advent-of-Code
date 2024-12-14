from day_04 import parse_input, WordSearch


def test_part_1():
    wordsearch = parse_input()
    ws = WordSearch(wordsearch)
    assert ws.part_1() == 2447


def test_part_2():
    wordsearch = parse_input()
    ws = WordSearch(wordsearch)
    assert ws.part_2() == 1868
