"""
This is the main module for 'Well-Named' repo
This module contains tests for even-color codes

Insted of having differnet logics for converting from and back to number and color pair, 
a dictionary called COLOR_PAIRS has been created for ease of retrieval and conversion
"""
from color_code_manual import generate_reference_manual
from color_code_converter import (
    get_color_from_pair_number,
    get_pair_number_from_color,
)


def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color


def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number


if __name__ == "__main__":
    generate_reference_manual()
    test_number_to_pair(4, "White", "Brown")
    test_number_to_pair(5, "White", "Slate")
    test_pair_to_number("Black", "Orange", 12)
    test_pair_to_number("Violet", "Slate", 25)
    test_pair_to_number("Red", "Orange", 7)
    print("Execution completed.")
