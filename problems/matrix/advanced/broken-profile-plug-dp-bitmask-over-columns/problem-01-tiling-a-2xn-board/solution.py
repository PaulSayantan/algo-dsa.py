"""Tiling a 2xN board with 1x2 dominoes -- broken-profile / plug DP template.

Fill in `count_tilings` using a cell-by-cell sweep over the 2 x N grid while
carrying a bitmask "profile" of the moving frontier.
"""

from __future__ import annotations


def count_tilings(n: int) -> int:
    """Count the ways to tile a 2 x n board with 1x2 dominoes.

    Args:
        n: The number of columns of the board (the board has exactly 2 rows).
           1 <= n <= 60.

    Returns:
        The number of distinct full tilings using horizontal and vertical
        dominoes. Fits in a signed 64-bit integer for n <= 60.

    Example:
        >>> count_tilings(3)
        3
    """
    # TODO: implement using broken-profile / plug DP (bitmask over columns).
    # Suggested state: sweep cells in row-major order over a 2-column-wide
    # profile; a bit marks a frontier cell already filled by a vertical domino
    # reaching in from the previous column.
    pass


if __name__ == "__main__":
    # Sample runs (expected results shown as comments, NOT asserted).
    print(count_tilings(1))  # expected: 1
    print(count_tilings(2))  # expected: 2
    print(count_tilings(3))  # expected: 3
    print(count_tilings(4))  # expected: 5
