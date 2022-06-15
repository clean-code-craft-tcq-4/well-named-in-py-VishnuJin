"""
This module consist of constants of 25-pair color code, originally known as even-count color code
COLOR_PAIRS dictionary contains Pair number as Key and the major,minor tuple as value
"""

MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

COLOR_PAIRS = {
    pair_number + 1: color_pair
    for pair_number, color_pair in enumerate(
        [
            (major_color, minor_color)
            for major_color in MAJOR_COLORS
            for minor_color in MINOR_COLORS
        ]
    )
}
