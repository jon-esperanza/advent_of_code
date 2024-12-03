from util.advent_of_code import AdventOfCode


class Day1(AdventOfCode):
    def __init__(self):
        super().__init__(1)

    def parse_input(self, lines):
        input_delimeter = "  "
        ids = [x.split(input_delimeter) for x in lines.splitlines()]
        return [int(x[0]) for x in ids], [int(x[1]) for x in ids]

    def part_one(self, input):
        """
        Sort both lists respectively
        Calculate the Manhattan distance between each pair of locations.

        Manhattan distance is the sum of the absolute value of
        the difference between each location.
        """
        input[0].sort()
        input[1].sort()
        manhattan_distances = [
            abs(input[0][i] - input[1][i]) for i in range(len(input[0]))
        ]
        res = sum(manhattan_distances)
        print(res)
        assert res == 1319616
        return res

    def part_two(self, input):
        """
        Count how often each id from left_ids appears in right_ids
        Multiply each id on the left_ids by the number of times it appears in right_ids
        """
        frequencies = {}  # Switch to hashmap data structure for kv store
        for id in input[0]:
            if id not in frequencies:
                frequencies[id] = 0

        for id in input[1]:
            if id in frequencies:
                frequencies[id] += 1

        similarity_scores = [id * cnt for id, cnt in frequencies.items()]
        res = sum(similarity_scores)
        print(res)
        assert res == 27267728
        return res


Day1().run()
