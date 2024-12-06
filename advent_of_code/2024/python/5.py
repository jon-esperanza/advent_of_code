from collections import deque

from util.advent_of_code import AdventOfCode


class Page:
    def __init__(self, id):
        self.id = id
        self.requires = []
        self.required_by = []

    def validUpdate(self, updates_after):
        """
        Checks if page requirements are not present after this page was updated.
        """
        return not any(
            [page in [x.id for x in self.requires] for page in updates_after]
        )

    def needs(self, page):
        if page not in self.requires:
            self.requires.append(page)

    def needed_by(self, page):
        if page not in self.required_by:
            self.required_by.append(page)


class Input:
    def __init__(self, rules, updates):
        self.rules = rules
        self.correct_updates, self.incorrect_updates = self.checked_updates(updates)

    def __dependency_graph(self, updates):
        """
        Builds dependency graph. Useful for topological sorting
        """
        pages = {}
        for update in updates:
            for rule in self.rules:
                x, y = [int(i) for i in rule.split("|")]
                if x in update and y in update:
                    if y not in pages:
                        pages[y] = Page(y)
                    if x not in pages:
                        pages[x] = Page(x)
                    pages[y].needs(pages[x])
                    pages[x].needed_by(pages[y])
        return pages

    def checked_updates(self, updates):
        """
        Partition updates based on all pages meeting requirements.
        """
        pages = self.__dependency_graph(updates)
        correct = []
        incorrect = []
        for update in updates:
            if all(  # all pages in update must be valid
                [
                    pages[pageId].validUpdate(update[idx + 1 :])
                    for idx, pageId in enumerate(update)
                ]
            ):
                correct.append(update)
            else:
                incorrect.append(update)
        return (correct, incorrect)

    def reorder(self, update):
        """
        Topological sort scoped to update.
        """
        pages_in_update = self.__dependency_graph([update])
        start = next((page for page in pages_in_update.values() if not page.requires))
        order = []
        q = deque([start])
        while q:
            page = q.popleft()
            if not page.requires and page.id not in order:
                order.append(page.id)
                for r in page.required_by:
                    if page in r.requires:
                        r.requires.remove(page)
                    q.append(r)
        return order


class Day5(AdventOfCode):
    def __init__(self):
        super().__init__(5)

    def parse_input(self, lines):
        rules = []
        updates = []
        for line in lines.splitlines():
            if "|" in line:
                rules.append(line.strip())
            elif line:
                updates.append([int(x) for x in line.strip().split(",")])
        return Input(rules, updates)

    def sum_medians(self, updates):
        sum = 0
        for update in updates:
            n = len(update)
            sum += update[n // 2]
        return sum

    def part_one(self, input):
        sum = self.sum_medians(input.correct_updates)
        print(sum)

    def part_two(self, input):
        reorder = [input.reorder(update) for update in input.incorrect_updates]
        sum = self.sum_medians(reorder)
        print(sum)


Day5().run()
