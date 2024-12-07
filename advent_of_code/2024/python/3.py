import re

from util.advent_of_code import AdventOfCode


class Day3(AdventOfCode):
    def __init__(self):
        super().__init__(3)

    def parse_input(self, lines):
        return "".join(lines.splitlines())  # single line

    def part_one(self, input):
        """
        Extract all valid mul(x, y)
        - stack?
        - how to identify mul keyword? clean string
        remove all characters that are not mul -- leave numbers
        """
        pattern = r"mul\(\d+,\d+\)"
        matches = re.findall(pattern, input)
        digit_pairs = [self.__extract_digits(x) for x in matches]
        res = sum([a * b for a, b in digit_pairs])
        return res

    def __extract_digits(self, string):
        """
        Extracts digits from a string of the form 'mul(x,y)'.
        """
        match = re.search(r"mul\((\d+),(\d+)\)", string)
        if match:
            return int(match.group(1)), int(match.group(2))
        else:
            return None, None

    def part_two(self, input):
        pattern = r"do\(\)(.*?)(?=don\'t\(\)|$)"
        matches = re.findall(pattern, "do()" + input)
        enabled = "".join(matches)
        res = self.part_one(enabled)
        assert res == 80570939
        return res


Day3().run()
