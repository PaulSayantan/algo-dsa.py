"""Anti-clockwise (counter-clockwise) spiral traversal of a matrix.

Return all elements of an m x n matrix in counter-clockwise spiral order,
starting at the top-left corner and moving DOWN the left column first.
"""

from typing import List


def anticlockwise_spiral_order(matrix: List[List[int]]) -> List[int]:
    """Return matrix elements in counter-clockwise spiral order.

    The traversal begins at the top-left cell and follows the direction
    cycle: down the left column, right along the bottom row, up the right
    column, left along the top row, then spirals inward.

    Args:
        matrix: A non-empty m x n grid of integers.

    Returns:
        A list containing every element of ``matrix`` exactly once, in
        counter-clockwise spiral order.

    Example:
        >>> anticlockwise_spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 4, 7, 8, 9, 6, 3, 2, 5]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(anticlockwise_spiral_order(grid))
    # Expected: [1, 4, 7, 8, 9, 6, 3, 2, 5]
