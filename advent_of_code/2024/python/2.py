from input import read_input


def parse_input(lines):
    input_delimeter = " "
    reports = lines.splitlines()
    return [
        [int(level) for level in levels.split(input_delimeter)] for levels in reports
    ]


def run():
    reports = read_input("2.txt", parse_input)
    assert part_one(reports) == 663
    assert part_two(reports) == 692


def part_one(reports: list[list[int]]):
    """
    Mark each report as safe or not safe.
    Count safe reports
    """
    reports_check = [is_safe(report) for report in reports]
    return sum(1 for report in reports_check if report)


def is_safe(report: list[int]):
    """
    Mark report unsafe if levels:
    - not monotonic
    - diff is not between 1 and 3

    Tolerance allows one bad level
    """
    diffs = [a - b for a, b in zip(report[:-1], report[1:])]
    dec = diffs[0] > 0  # if decreasing
    for diff in diffs:
        if dec and diff < 0:
            return False
        if not dec and diff > 0:
            return False
        if not (1 <= abs(diff) <= 3):
            return False
    return True


def part_two(reports: list[list[int]]):
    """
    If report is not safe, apply a dampner that checks
    if removing a single level makes the report safe
    """
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
        else:  # dampener
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1 :]):
                    safe_count += 1
                    break
    return safe_count


run()
