"""
this module contains functionalities related to color code reference manual
"""
from even_color_codes import COLOR_PAIRS
from format_output import print_as_table


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
