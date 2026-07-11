"""Solve the Lights Out puzzle as a linear system over GF(2).

Fill in `lights_out` below. The intended technique is Gauss-Jordan elimination
over GF(2): model "press cell i?" as a 0/1 unknown, build one XOR equation per
light, and reduce the augmented system to RREF using row XORs (no division). Read
off a press pattern, or return None if the system is inconsistent.
"""

from typing import List, Optional


def lights_out(grid: List[List[int]]) -> Optional[List[List[int]]]:
    """Return a press pattern that turns every light off, or None if impossible.

    Args:
        grid: An m x n matrix of 0/1 values. grid[r][c] == 1 means that light is
            currently ON. Pressing a cell toggles it and its up/down/left/right
            neighbours.

    Returns:
        An m x n matrix p of 0/1 values where p[r][c] == 1 means "press (r, c)",
        such that applying all presses turns every light off. Returns None if no
        press pattern can clear the board.

    Example:
        >>> lights_out([[1, 1], [1, 1]])
        [[1, 1], [1, 1]]
        >>> lights_out([[0, 0], [0, 0]])
        [[0, 0], [0, 0]]
    """
    # TODO: implement using Gauss-Jordan elimination over GF(2).
    pass


if __name__ == "__main__":
    print(lights_out([[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]]))
    # expected (one valid answer): [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

    print(lights_out([[1, 1], [1, 1]]))    # expected: [[1, 1], [1, 1]]
    print(lights_out([[0, 0, 0],
                      [0, 0, 0]]))          # expected: [[0, 0, 0], [0, 0, 0]]
