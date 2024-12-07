import sys
from enum import Enum

from util.advent_of_code import AdventOfCode


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def get_adjustments(self):
        match self:
            case self.UP:
                return [-1, 0]
            case self.RIGHT:
                return [0, 1]
            case self.DOWN:
                return [1, 0]
            case self.LEFT:
                return [0, -1]

    def next(self):
        match self:
            case self.UP:
                return self.RIGHT
            case self.RIGHT:
                return self.DOWN
            case self.DOWN:
                return self.LEFT
            case self.LEFT:
                return self.UP


class Guard:
    def __init__(self, start, direction=Direction.UP):
        self.position = start
        self.direction = direction
        self.consecutive_rotations = 0
        self.prev_action = ""

    def rotate(self):
        if self.prev_action == "rotate":
            self.consecutive_rotations += 1
        self.direction = self.direction.next()
        self.prev_action = "rotate"
        return self

    def forward(self):
        i, j = self.position
        x, y = self.direction.get_adjustments()
        self.position = [i + x, j + y]
        self.prev_action = "forward"
        self.consecutive_rotations = 0
        return self

    def stuck(self):
        return self.consecutive_rotations >= 4


class Map(object):
    def __init__(self, init_grid, path=[], hide_guard=False):
        self.grid = init_grid
        self.n = len(init_grid)
        self.m = len(init_grid[0])
        self.start = self.find_guard()
        self.distinct_positions = 0
        self.path = path

    def find_guard(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == "^":
                    return Guard([i, j])

    def mark_position(self, i, j, direction):
        """
        Adds position to guard path if not already in path
        """
        if (i, j, direction) in self.path:
            return False
        self.path.append((i, j, direction))
        return True

    def mark_routes(self, guard: Guard):
        """
        Recursively walk through route and mark positions on path.
        Returns False if loop is encountered.
        """
        if guard.stuck():
            return True
        (i, j), direction = guard.position, guard.direction
        x, y = guard.direction.get_adjustments()
        if 0 <= i + x < self.n and 0 <= j + y < self.m:
            in_front = self.grid[i + x][j + y]
            if in_front == "#" or in_front == "O":  # rotate
                return self.mark_routes(guard.rotate())
            else:  # mark and go forward
                if not self.mark_position(i, j, direction):
                    return False
                return self.mark_routes(guard.forward())
        else:
            self.mark_position(i, j, direction)
            return True

    def place_obstacle(self, i, j):
        """
        Places obstacle on grid if it is not already on the guard's path.
        """
        if (i, j) in [(x[0], x[1]) for x in self.path]:
            return False
        self.grid[i][j] = "O"
        return True

    def remove(self, i, j):
        self.grid[i][j] = "."


sys.setrecursionlimit(20000000)  # lol


class Day6(AdventOfCode):
    def __init__(self):
        super().__init__(6)

    def parse_input(self, lines):
        return Map([list(x) for x in lines.split()])

    def part_one(self, input):
        input.mark_routes(input.start)
        res = len(set([(i, j) for i, j, _ in input.path]))
        assert res == 5086
        return res

    def part_two(self, input):
        guard_path_positions = input.path  # Traverse backwards through guard path
        traps = 0
        while len(guard_path_positions) > 1:  # Skip starting position
            x, y, _ = guard_path_positions.pop()  # Remove last position in path
            i, j, g_direction = guard_path_positions[
                -1
            ]  # Start from next position in path
            new_map = Map(
                input.grid, guard_path_positions.copy(), True
            )  # New map state
            guard = Guard([i, j], g_direction)  # Starting guard state
            if new_map.place_obstacle(x, y):  # If able to place obstacle
                if not new_map.mark_routes(guard):  # If loop encountered
                    traps += 1
                new_map.remove(x, y)
        assert traps == 1770
        return traps


Day6().run()
