from util.advent_of_code import AdventOfCode


class Day2(AdventOfCode):
    def __init__(self):
        super().__init__(2)

    def parse_input(self, lines):
        input_delimeter = " "
        reports = lines.splitlines()
        return [
            [int(level) for level in levels.split(input_delimeter)]
            for levels in reports
        ]

    def part_one(self, input):
        """
        Mark each report as safe or not safe.
        Count safe reports
        """
        reports_check = [self.__is_safe(report) for report in input]
        res = sum(1 for report in reports_check if report)
        print(res)
        assert res == 663
        return res

    def part_two(self, input):
        """
        If report is not safe, apply a dampner that checks
        if removing a single level makes the report safe
        """
        safe_count = 0
        for report in input:
            if self.__is_safe(report):
                safe_count += 1
            else:  # dampener
                for i in range(len(report)):
                    if self.__is_safe(report[:i] + report[i + 1 :]):
                        safe_count += 1
                        break
        print(safe_count)
        assert safe_count == 692
        return safe_count

    def __is_safe(self, report: list[int]):
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


Day2().run()
