"""Batch Updates and Region Sums (offline).

Apply many rectangle range-add updates to a zero matrix, then answer many
rectangle-sum queries. Solve with a 2D difference array (updates) followed by a
2D prefix-sum table (queries).
"""

from typing import List


def batch_updates_region_sums(
    m: int,
    n: int,
    updates: List[List[int]],
    queries: List[List[int]],
) -> List[int]:
    """Return the sum for each query after all updates are applied.

    Args:
        m: Number of rows in the matrix (initially all zeros).
        n: Number of columns in the matrix.
        updates: List of [r1, c1, r2, c2, v]; each adds v to every cell in the
            inclusive rectangle (r1, c1)-(r2, c2). v may be negative.
        queries: List of [r1, c1, r2, c2]; each asks for the sum of the
            inclusive rectangle (r1, c1)-(r2, c2) after all updates.

    Returns:
        A list of query answers in the same order as `queries`.

    Example:
        >>> batch_updates_region_sums(
        ...     3, 3,
        ...     [[0, 0, 1, 1, 5], [1, 1, 2, 2, 3]],
        ...     [[0, 0, 2, 2], [1, 1, 1, 1]],
        ... )
        [32, 8]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(
        batch_updates_region_sums(
            3, 3,
            [[0, 0, 1, 1, 5], [1, 1, 2, 2, 3]],
            [[0, 0, 2, 2], [1, 1, 1, 1]],
        )
    )
    # Expected: [32, 8]

    print(
        batch_updates_region_sums(
            2, 2,
            [[0, 0, 1, 1, 2], [0, 0, 0, 1, -1]],
            [[0, 0, 0, 1], [0, 0, 1, 1]],
        )
    )
    # Expected: [2, 6]
