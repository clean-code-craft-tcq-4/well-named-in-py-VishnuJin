"""
This module consist of independent helper functions
"""


def print_as_table(headers, rows):
    print("Color code reference")
    print()
    format_row = "{:^15}" * (len(headers))
    print(format_row.format(*headers))

    for row in rows:
        print(format_row.format(*row))
