from day_07 import build_circuit, part_1, part_2


def test_part_1():
    circuit = build_circuit()
    assert part_1(circuit) == 46065


def test_part_2():
    circuit = build_circuit()
    assert part_2(circuit) == 14134
