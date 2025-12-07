from itertools import pairwise


def parse_input():
    with open("input.txt", "r") as fh:
        reports = [[int(level) for level in report.strip().split()] for report in fh.readlines()]
    return reports


def differ(report):
    for a, b in pairwise(report):
        if not 1 <= abs(a - b) <= 3:
            return False
    return True


def is_monotonic(report):
    for a, b in pairwise(report):
        if (b - a) < 0:
            return False
    return True


def is_safe(report):
    return differ(report) and (is_monotonic(report) or is_monotonic(reversed(report)))


def drop_one(report):
    yield report
    for i in range(len(report)):
        yield report[:i] + report[i + 1 :]


def part_1(reports: list[str]):
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
    return safe_reports


def part_2(reports: list[str]):
    safe_reports = 0
    for report in reports:
        for rep in drop_one(report):
            if is_safe(rep):
                safe_reports += 1
                break
    return safe_reports


if __name__ == "__main__":
    reports = parse_input()
    print(part_1(reports))
    print(part_2(reports))
