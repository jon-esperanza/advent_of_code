#!/usr/bin/env bash

set -euo pipefail

DAY=$1
PYTHON_BOILERPLATE=$(cat <<-END
from util.advent_of_code import AdventOfCode
class Day$DAY(AdventOfCode):
    def __init__(self):
        super().__init__($DAY)

    def parse_input(self, lines):
        pass

    def part_one(self, input):
        pass

    def part_two(self, input):
        pass
Day$DAY().run()
END
)

if [ -z "$DAY" ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

# Create input file for the day, if it doesn't exist
INPUT_FILE="./advent_of_code/2024/inputs/$DAY.txt"
if [ -f "$INPUT_FILE" ]; then
    echo "Input file for day $DAY already exists"
else
    echo "Creating input file for day $DAY"
    touch "$INPUT_FILE"
fi

# Create python file for the day with boilerplate, if it doesn't exist
FILE="./advent_of_code/2024/python/$DAY.py"
if [ -f "$FILE" ]; then
    echo "Python file for day $DAY already exists"
else 
    touch "$FILE"
    echo "$PYTHON_BOILERPLATE" >> "$FILE"
fi

# TODO: add c++ file

