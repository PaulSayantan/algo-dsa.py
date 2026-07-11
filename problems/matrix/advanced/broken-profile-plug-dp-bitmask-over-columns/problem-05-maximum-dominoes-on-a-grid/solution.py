"""Maximum Dominoes on a Grid with Obstacles -- broken-profile / plug DP template.

Fill in `max_dominoes` with a cell-by-cell sweep that maximizes (instead of
counts) the number of dominoes placed, allowing free cells to stay uncovered.
"""

from __future__ import annotations

from typing import List


def max_dominoes(grid: List[str]) -> int:
    """Return the maximum number of 1x2 dominoes that fit on the free cells.

    Args:
        grid: List of n strings, each of length m. '.' marks a free cell that
            may be covered; '#' marks a blocked cell that must stay uncovered.
            Free cells are NOT required to be fully covered.

    Returns:
        The maximum number of non-overlapping dominoes placeable on free,
        orthogonally adjacent cell pairs. Lies in [0, free_cells // 2].

    Example:
        >>> max_dominoes(["...", ".#."])
        2
    """
    # TODO: implement using broken-profile / plug DP (bitmask over columns).
    # Sweep cells row-major over a width-min(n, m) profile. Store the MAX number
    # of dominoes for each profile (use -infinity for unreachable states). At an
    # empty free cell, branch over: leave it empty (value unchanged), place a
    # vertical domino (+1), or place a horizontal domino (+1). Take max at each
    # profile; the answer is the value of profile 0 after the last cell.
    pass


if __name__ == "__main__":
    print(max_dominoes(["...", "..."]))                          # expected: 3
    print(max_dominoes(["...", ".#."]))                          # expected: 2
    print(max_dominoes(["#..", ".#.", "..#"]))                   # expected: 2
    print(max_dominoes(["....", "....", "....", "...."]))        # expected: 8
