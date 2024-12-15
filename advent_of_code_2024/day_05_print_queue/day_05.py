from pathlib import Path

def parse_input(fn) -> tuple:
    puzzle_path = Path(__file__).parent / fn
    with open(puzzle_path) as fh:
        page_order,  updates = fh.read().split("\n\n")

    page_order: list[tuple[int]] = [tuple(map(int, x.split("|"))) for x in page_order.split("\n")]
    updates: list[list[int]] = [list(map(int, x.split(","))) for x in updates.split("\n")]

    return page_order, updates

def check(page_orders, page, adjacent, direction):
    if not adjacent:
        return True
    if direction == "r":
        for update in page_orders:
            for n in adjacent:
                if update == (n, page):
                    return False
    if direction == "l":
        for update in page_orders:
            for n in adjacent:
                if update == (page, n):
                    return False
    return True

def filter_page_orders(page_rules, page_order):
    page_rules_subset = set()
    for page_rule in page_rules:
        for page in page_order:
            if page in page_rule:
                page_rules_subset.add(page_rule)
    return page_rules_subset

def is_valid(page_orders, instruction):
    for i, page in enumerate(instruction):
        x = int(page)
        l = instruction[:i]
        r = instruction[i+1:]
        check_l = check(page_orders, x, l, "l")
        check_r = check(page_orders, x, r, "r")
        if not check_l and check_r:
            return False
    return True

def part_1(page_order, instr):
    total = 0
    for inst in instr:
        foo_bar = filter_page_orders(page_order, inst)
        if is_valid(foo_bar, inst):
            total += inst[len(inst) // 2]
    return total

def is_not_valid(page_order, inst):
    for i, x in enumerate(inst):
        for j, y in enumerate(inst[i+1:], start=i+1):
            for order in page_order:
                if x == order[1] and y == order[0]:
                    inst[i] = order[0]
                    inst[j] = order[1]
                    return is_not_valid(page_order, inst)
    return inst

def part_2(page_order, instr):
    total = 0
    for inst in instr:
        foo_bar = filter_page_orders(page_order, inst)
        if not is_valid(foo_bar, inst):
            foo = is_not_valid(page_order, inst)
            total += foo[len(foo) // 2]
    return total

if __name__ == "__main__":
    page_order, instr = parse_input("input.txt")
    print(part_1(page_order, instr))              
    print(part_2(page_order, instr))
