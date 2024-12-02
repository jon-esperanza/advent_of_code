"""
Class responsible for reading input files
"""

import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dir = os.path.join(parent_dir, "inputs")


def read_input(input_filename: str, func: callable):
    return __read_input(input_dir, input_filename, func)


def __read_input(file_path, input_path, func):
    input_file = os.path.join(file_path, input_path)

    with open(input_file) as f:
        res = func(f.read())
    return res
