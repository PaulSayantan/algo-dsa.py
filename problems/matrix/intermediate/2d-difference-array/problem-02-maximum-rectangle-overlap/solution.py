"""Maximum Rectangle Overlap.

Given axis-aligned rectangles on a lattice, return the maximum number of
rectangles covering any single cell. Solve with a 2D difference array + prefix
sum, then take the max coverage value.
"""

from typing import List


def max_rectangle_overlap(rectangles: List[List[int]]) -> int:
    """Return the maximum overlap depth over all lattice cells.

    Each rectangle is [x1, y1, x2, y2] with inclusive corners and covers every
    integer cell (x, y) with x1 <= x <= x2 and y1 <= y <= y2.

    Args:
        rectangles: List of [x1, y1, x2, y2] rectangles with
            0 <= x1 <= x2 and 0 <= y1 <= y2.

    Returns:
        The greatest number of rectangles that simultaneously cover any one
        lattice cell.

    Example:
        >>> max_rectangle_overlap([[0, 0, 2, 2], [1, 1, 3, 3], [1, 1, 2, 2]])
        3
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(max_rectangle_overlap([[0, 0, 2, 2], [1, 1, 3, 3], [1, 1, 2, 2]]))
    # Expected: 3

    print(max_rectangle_overlap([[0, 0, 1, 1], [2, 2, 3, 3]]))
    # Expected: 1
