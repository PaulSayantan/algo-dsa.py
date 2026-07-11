"""Lights Out: minimum presses to turn every light off (or -1 if impossible).

Empty solution template — fill in the logic yourself.
"""

from typing import List


def min_presses_lights_out(grid: List[List[int]]) -> int:
    """Return the minimum number of presses to switch every light off.

    Pressing a cell toggles it and its orthogonal neighbors. Each cell is
    pressed 0 or 1 times; order is irrelevant.

    Args:
        grid: An m x n grid where grid[i][j] is 1 (on) or 0 (off).

    Returns:
        The minimum number of presses to clear the board, or -1 if no sequence
        of presses can turn all lights off.

    Example:
        >>> min_presses_lights_out([[0]])
        0
    """
    # TODO: build the GF(2) system A p = b (column j = cells toggled by press j),
    #       run Gaussian elimination over GF(2), detect inconsistency (-> -1),
    #       then enumerate free variables to minimize the press count.
    pass


if __name__ == "__main__":
    # Example 1 -> expected 5
    print(min_presses_lights_out([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

    # Example 2 -> expected -1
    print(min_presses_lights_out([[1, 0, 0], [0, 0, 0]]))

    # Example 3 -> expected 0
    print(min_presses_lights_out([[0]]))
