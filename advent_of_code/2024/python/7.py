from enum import Enum

from util.advent_of_code import AdventOfCode


class Operator(Enum):
    ADD = 1
    MUL = 2
    CONC = 3

    def apply(self, x, y):
        match self:
            case Operator.ADD:
                return x + y
            case Operator.MUL:
                return x * y
            case Operator.CONC:
                return int(str(x) + str(y))


class PartialEquation:
    def __init__(self, test_value, numbers):
        self.test_value = test_value
        self.numbers = numbers
        self.size = len(numbers)
        self.operators = []  # available operators for equation

    def __repr__(self):
        return f"{self.test_value}: {self.numbers}"

    def any_valid(self, agg: int | None = None, i=1):
        """
        Branches through all operators.
        Returns True if any branch is valid.
        """
        if not agg:
            agg = self.numbers[0]
        return any([self.valid(agg, op, i) for op in self.operators])

    def valid(self, agg, operator, i):
        """
        Recursive DFS
        Applies operator, checks if valid, continues recursion.
        """
        if i >= self.size:  # all numbers were reached
            return agg == self.test_value
        agg = operator.apply(agg, self.numbers[i])
        if agg <= self.test_value:
            return self.any_valid(agg, i + 1)
        else:
            return False


class Day7(AdventOfCode):
    def __init__(self):
        super().__init__(7)

    def parse_input(self, lines):
        equations = []
        for line in lines.splitlines():
            y, right = line.split(":")
            numbers = [int(x) for x in right.strip().split(" ")]
            equations.append(PartialEquation(int(y), numbers))
        return equations

    def set_operators(self, input, operators):
        """Helper for setting the available operators for all equations in input"""
        for eq in input:
            eq.operators = operators

    def part_one(self, input):
        self.set_operators(input, [Operator.ADD, Operator.MUL])
        res = sum([eq.test_value for eq in input if eq.any_valid()])
        assert res == 5030892084481
        return res

    def part_two(self, input):
        self.set_operators(input, [Operator.ADD, Operator.MUL, Operator.CONC])
        res = sum([eq.test_value for eq in input if eq.any_valid()])
        assert res == 91377448644679
        return res


Day7().run()
