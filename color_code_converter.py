"""
This module contains utility functions related to color codes
"""
from even_color_codes import COLOR_PAIRS


def get_color_from_pair_number(wire_pair_number):
    """
    (int) -> tuple(str)

    accepts pair number as input and returns tuple containing major and minor color
    """
    return COLOR_PAIRS[wire_pair_number]


def get_pair_number_from_color(major_color, minor_color):
    """
    (str, str) -> int

    accepts major and minor colors as input and returns respective pair number
    """
    for pair_number, color_pair in COLOR_PAIRS.items():
        if (major_color, minor_color) == color_pair:
            return pair_number
