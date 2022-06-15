"""
This module contains utility functions related to color codes
"""
from even_color_codes import COLOR_PAIRS
from helper_functions import print_as_table


def get_color_from_pair_number(wire_pair_number):
    return COLOR_PAIRS[wire_pair_number]


def get_pair_number_from_color(major_color, minor_color):
    for pair_number, color_pair in COLOR_PAIRS.items():
        if (major_color, minor_color) == color_pair:
            return pair_number


def generate_reference_manual():
    """
    New feature that generates color code reference manual
    The manual will be printed neatly in table format
    """
    headers = ["pair_no", "Major_Color", "Minor_Color"]
    rows = [
        (pair_number,) + (color_pair) for pair_number, color_pair in COLOR_PAIRS.items()
    ]
    print_as_table(headers, rows)
