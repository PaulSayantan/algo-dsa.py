"""Parquet Tiling with Holes -- count domino tilings of a board with blocked cells.

Broken-profile / plug DP template. Fill in `count_tilings` with a cell-by-cell
sweep that treats a hole as an already-occupied cell.
"""

from __future__ import annotations

from typing import List


def count_tilings(grid: List[str]) -> int:
    """Count full 1x2 domino tilings of the free cells of a board with holes.

    Args:
        grid: List of n strings, each of length m. '.' marks a free cell that
            must be covered; '#' marks a hole that must stay uncovered.

    Returns:
        The number of ways to tile every free cell with 1x2 dominoes without
        covering any hole. Returns 0 when the free region cannot be tiled
        (e.g. an odd number of free cells). Fits in a signed 64-bit integer for
        boards up to 12 x 12.

    Example:
        >>> count_tilings(["##..", "....", "....", "...."])
        18
    """
    # TODO: implement using broken-profile / plug DP (bitmask over columns).
    # Sweep cells row-major over a width-min(n, m) profile. Treat a '#' cell as
    # already filled: do not place a piece on it and do not let a vertical
    # domino from above occupy it. Everything else matches the hole-free count.
    pass


if __name__ == "__main__":
    print(count_tilings(["....", "....", "....", "...."]))  # expected: 36
    print(count_tilings(["##..", "....", "....", "...."]))  # expected: 18
    print(count_tilings(["#...", "....", "...#"]))          # expected: 5
    print(count_tilings(["#...", "....", "....", "...#"]))  # expected: 0
