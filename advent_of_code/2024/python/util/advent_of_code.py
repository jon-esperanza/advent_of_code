from abc import abstractmethod

from util.input import read_input


class AdventOfCode:
    def __init__(self, day):
        self.day = day

    def run(self):
        input = read_input(f"{self.day}.txt", self.parse_input)
        self.part_one(input)
        self.part_two(input)

    @abstractmethod
    def part_one(self, input):
        pass

    @abstractmethod
    def part_two(self, input):
        pass

    @abstractmethod
    def parse_input(self, lines):
        pass
