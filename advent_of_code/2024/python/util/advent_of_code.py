from abc import abstractmethod

from util.input import read_input
from util.timer import timed


class AdventOfCode:
    def __init__(self, day):
        self.day = day

    def run(self):
        input = timed(read_input, print_result=False)(
            f"{self.day}.txt", self.parse_input
        )
        timed(self.part_one)(input)
        timed(self.part_two)(input)

    @abstractmethod
    def part_one(self, input):
        pass

    @abstractmethod
    def part_two(self, input):
        pass

    @abstractmethod
    def parse_input(self, lines):
        pass
