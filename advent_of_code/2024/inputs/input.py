"""
Class responsible for reading input files
"""

import os

THIS_DIR = os.path.dirname(__file__)


def read_input(input_filename: str, func: callable):
    return __read_input(THIS_DIR, input_filename, func)


def __read_input(file_path, input_path, func):
    file_path = os.path.dirname(__file__)
    input_file = os.path.join(file_path, input_path)

    with open(input_file) as f:
        res = func(f.read())
    return res
