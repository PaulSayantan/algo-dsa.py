"""Largest All-Zero Submatrix.

Return the area of the biggest axis-aligned rectangle of all 0s in a
binary matrix. Empty solution template — fill in the logic yourself.
"""

from typing import List


def largest_all_zero_submatrix(grid: List[List[int]]) -> int:
    """Return the area of the largest all-zero rectangle in ``grid``.

    Args:
        grid: An n x m matrix whose entries are 0 or 1.

    Returns:
        The maximum number of cells in an axis-aligned rectangle made up
        entirely of 0s. Returns 0 if the matrix has no 0.

    Example:
        >>> largest_all_zero_submatrix([[0, 0, 1], [0, 0, 1], [0, 0, 0]])
        6
    """
    # TODO: implement.
    # Hint: maintain height[j] = consecutive 0s ending at the current row in
    # column j (a 1 resets height[j] to 0), then run largest-rectangle-in-
    # histogram (monotonic stack) on each row and keep the maximum.
    pass


if __name__ == "__main__":
    print(largest_all_zero_submatrix([[0, 0, 1],
                                      [0, 0, 1],
                                      [0, 0, 0]]))  # expected: 6
    print(largest_all_zero_submatrix([[1, 0, 0],
                                      [0, 0, 0],
                                      [1, 0, 0]]))  # expected: 6
    print(largest_all_zero_submatrix([[1, 1],
                                      [1, 1]]))      # expected: 0
