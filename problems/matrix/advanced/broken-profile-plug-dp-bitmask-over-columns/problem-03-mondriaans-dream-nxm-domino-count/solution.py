"""Mondriaan's Dream -- count domino tilings of an n x m board.

Broken-profile / plug DP template. Fill in `count_tilings` with a cell-by-cell
sweep carrying a width-min(n, m) bitmask profile.
"""

from __future__ import annotations


def count_tilings(n: int, m: int) -> int:
    """Count full 1x2 domino tilings of an n x m board.

    Args:
        n: Number of rows (1 <= n <= 12).
        m: Number of columns (1 <= m <= 12).

    Returns:
        The number of distinct ways to tile the whole board with 1x2 dominoes.
        Returns 0 when n * m is odd. Fits in a signed 64-bit integer for boards
        up to 12 x 12.

    Example:
        >>> count_tilings(4, 4)
        36
    """
    # TODO: implement using broken-profile / plug DP (bitmask over columns).
    # Sweep cells in row-major order over a width-w = min(n, m) profile.
    # State bit j records whether the next cell in column j is already filled
    # by a vertical domino coming from the row above. At each empty cell branch
    # over: place a vertical domino (set the bit) or a horizontal domino
    # (mark the neighbouring column). The answer is the count of profile 0
    # after the final cell.
    pass


if __name__ == "__main__":
    print(count_tilings(2, 2))  # expected: 2
    print(count_tilings(3, 3))  # expected: 0
    print(count_tilings(3, 4))  # expected: 11
    print(count_tilings(4, 4))  # expected: 36
    print(count_tilings(8, 8))  # expected: 12988816
