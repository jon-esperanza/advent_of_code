from collections import deque

from util.advent_of_code import AdventOfCode

all_directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

diagonal_directions = [[-1, -1], [1, 1], [-1, 1], [1, -1]]


class XMasState:
    """
    Holds state for a single word being searched in a given direction.
    """

    def __init__(self, direction, letters="XMAS"):
        self.letters_left = letters
        self.cells = []
        self.direction = direction

    def is_complete(self):
        return not self.letters_left

    def is_next(self, c):
        """Checks if given char is next in the search."""
        return self.letters_left[0] == c

    def update_state(self, i, j):
        """
        Removes left-most char from letters in search.
        Adds location of found letter to state.
        """
        self.letters_left = self.letters_left[1:]
        self.cells.append([i, j])
        return self.letters_left


class WordSearch:
    def __init__(self, input, search_directions, word):
        self.search_directions = search_directions
        self.word = word
        self.input = input
        self.row_len = len(input)
        self.col_len = len(input[0])

    def withinBounds(self, x, y):
        return 0 <= x < self.row_len and 0 <= y < self.col_len

    def find_all(self):
        """
        Multi-source BFS starting from first letter in word
        Queue tuple of (next [i][j], State)
        If grid[i][j] is next in search => update state
            If updated_state.is_complete => count++, stop
            Else: keep searching in direction (queue next char)
        else: stop
        """
        q = deque()
        found = 0
        states = []
        for i in range(self.row_len):
            for j in range(self.col_len):
                if self.input[i][j] == self.word[0]:
                    for x, y in self.search_directions:
                        if self.withinBounds(i + x, j + y):
                            init_state = XMasState(direction=[x, y], letters=self.word)
                            init_state.update_state(i, j)
                            q.append(([i + x, j + y], init_state))
        while q:
            (i, j), state = q.popleft()
            x, y = state.direction
            c = self.input[i][j]
            if state.is_next(c):
                state.update_state(i, j)
                if state.is_complete():
                    found += 1
                    states.append(state)
                else:
                    if self.withinBounds(i + x, j + y):
                        q.append(([i + x, j + y], state))
        return (found, states)

    def find_states_intersecting_letter(self, letter_index):
        """
        After finding all words:
        - group them by a desired letter position used
        - find words that intersect on desired letter
        """
        _, states = self.find_all()
        group_states = {}
        for state in states:
            key = state.cells[letter_index][0], state.cells[letter_index][1]
            if key not in group_states:
                group_states[key] = []
            group_states[key].append(state)
        x_states = []
        found = 0
        for _, states in group_states.items():
            if len(states) == 2:  # intersecting
                found += 1
                for x in states:
                    x_states.append(x)
        return (found, x_states)


class Day4(AdventOfCode):
    def __init__(self):
        super().__init__(4)

    def parse_input(self, lines):
        return [[c for c in x] for x in lines.splitlines()]

    def part_one(self, input):
        search = WordSearch(input, all_directions, "XMAS")
        found, _ = search.find_all()
        print(found)
        assert found == 2397
        return found

    def part_two(self, input):
        search = WordSearch(input, diagonal_directions, "MAS")
        found, _ = search.find_states_intersecting_letter(1)  # 1 is index of 'A'
        print(found)
        assert found == 1824
        return found


Day4().run()
