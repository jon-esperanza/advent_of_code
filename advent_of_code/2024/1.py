from inputs.input import read_input


def parse_input(lines):
    input_delimeter = "  "
    return [x.split(input_delimeter) for x in lines.splitlines()]


def run():
    ids = read_input("1.txt", parse_input)
    left_ids = [int(x[0]) for x in ids]
    right_ids = [int(x[1]) for x in ids]

    assert part_one(left_ids, right_ids) == 1319616
    assert part_two(left_ids, right_ids) == 27267728


def part_one(left_ids, right_ids):
    """
    Sort both lists respectively
    Calculate the Manhattan distance between each pair of locations.

    Manhattan distance is the sum of the absolute value of
    the difference between each location.
    """
    left_ids.sort()
    right_ids.sort()
    manhattan_distances = [
        abs(left_ids[i] - right_ids[i]) for i in range(len(left_ids))
    ]
    return sum(manhattan_distances)  # 1319616


def part_two(left_ids, right_ids):
    """
    Count how often each id from left_ids appears in right_ids
    Multiply each id on the left_ids by the number of times it appears in right_ids
    """
    frequencies = {}  # Switch to hashmap data structure for kv store
    for id in left_ids:
        if id not in frequencies:
            frequencies[id] = 0

    for id in right_ids:
        if id in frequencies:
            frequencies[id] += 1

    similarity_scores = [id * cnt for id, cnt in frequencies.items()]
    return sum(similarity_scores)  # 27267728


run()
